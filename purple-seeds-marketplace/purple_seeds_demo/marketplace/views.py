from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import CustomizeForm, DeployForm, LoginForm
from .services import catalog, pricing, storage


DEMO_USERNAME = 'demo'
DEMO_PASSWORD = 'demo12345'


def ensure_demo_user():
    User = get_user_model()
    if not User.objects.exists():
        User.objects.create_user(username=DEMO_USERNAME, password=DEMO_PASSWORD)


def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('portal')
    return redirect('login')


def login_view(request):
    ensure_demo_user()
    form = LoginForm(request.POST or None)
    error = None
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user:
            login(request, user)
            return redirect('portal')
        error = 'Invalid credentials. Please try again.'
    return render(
        request,
        'auth/login.html',
        {
            'form': form,
            'error': error,
            'demo_username': DEMO_USERNAME,
            'demo_password': DEMO_PASSWORD,
        },
    )


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def portal(request):
    return render(request, 'portal.html', {'active_step': 'portal'})


@login_required
def marketplace(request):
    suite = request.GET.get('suite', 'software')
    subcat = request.GET.get('subcat')
    query = request.GET.get('q')

    suites = catalog.list_suites()
    suite_keys = {item['key'] for item in suites}
    if suite not in suite_keys:
        suite = suites[0]['key']

    subcategories = catalog.list_subcategories(suite)
    solutions = catalog.list_solutions(suite=suite, subcat=subcat, q=query)

    return render(
        request,
        'marketplace.html',
        {
            'suites': suites,
            'active_suite': suite,
            'subcategories': subcategories,
            'active_subcat': subcat,
            'query': query or '',
            'solutions': solutions,
            'active_step': 'marketplace',
        },
    )


@login_required
def solution_detail(request, slug):
    solution = catalog.get_solution_by_slug(slug)
    return render(
        request,
        'solution_detail.html',
        {
            'solution': solution,
            'active_step': 'marketplace',
        },
    )


@login_required
def customize(request, slug):
    solution = catalog.get_solution_by_slug(slug)
    if not solution:
        return render(request, 'customize.html', {'solution': None, 'active_step': 'customize'})

    draft = request.session.get('quote_draft', {})
    initial = {}
    if draft.get('solution_slug') == slug:
        initial = {
            'tier': draft.get('tier') or '',
            'addons': draft.get('addons') or [],
            'qty': draft.get('qty') or 1,
            'notes': draft.get('notes') or '',
        }

    if request.method == 'POST':
        form = CustomizeForm(request.POST, solution=solution)
        if form.is_valid():
            cleaned = form.cleaned_data
            request.session['quote_draft'] = {
                'solution_id': solution['id'],
                'solution_slug': solution['slug'],
                'tier': cleaned.get('tier') or None,
                'addons': cleaned.get('addons') or [],
                'qty': cleaned.get('qty') or 1,
                'notes': cleaned.get('notes') or '',
            }
            draft = request.session['quote_draft']
            initial = cleaned
    else:
        form = CustomizeForm(solution=solution, initial=initial)

    tier_name = draft.get('tier')
    addon_names = draft.get('addons') or []
    qty = draft.get('qty') or 1
    quote = pricing.compute_quote(solution, tier_name, addon_names, qty)

    return render(
        request,
        'customize.html',
        {
            'solution': solution,
            'form': form,
            'quote': quote,
            'draft': draft,
            'active_step': 'customize',
        },
    )


@login_required
def deploy(request):
    draft = request.session.get('quote_draft')
    solution = catalog.get_solution_by_id(draft.get('solution_id')) if draft else None

    if not draft or not solution:
        return render(request, 'deploy.html', {'solution': None, 'active_step': 'deploy'})

    quote = pricing.compute_quote(
        solution,
        draft.get('tier'),
        draft.get('addons') or [],
        draft.get('qty') or 1,
    )

    if request.method == 'POST':
        form = DeployForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            record = {
                'created_at': timezone.now().isoformat(),
                'user': {'username': request.user.username},
                'contact': {
                    'name': cleaned['name'],
                    'org': cleaned['org'],
                    'email': cleaned['email'],
                    'phone': cleaned.get('phone') or '',
                },
                'solution': {
                    'id': solution['id'],
                    'slug': solution['slug'],
                    'title': solution['title'],
                },
                'draft': {
                    'tier': draft.get('tier'),
                    'addons': draft.get('addons') or [],
                    'qty': draft.get('qty') or 1,
                    'notes': draft.get('notes') or '',
                },
                'totals': {
                    'base': quote['base_price'],
                    'addons_total': quote['addons_total'],
                    'total': quote['total'],
                },
                'preferred_date': cleaned.get('preferred_date').isoformat() if cleaned.get('preferred_date') else '',
                'deploy_notes': cleaned.get('notes') or '',
            }
            record_id = storage.append_quote_request(record)
            request.session['last_submission_id'] = record_id
            request.session['quote_draft'] = draft
            return render(
                request,
                'deploy.html',
                {
                    'solution': solution,
                    'quote': quote,
                    'form': form,
                    'success': True,
                    'submission_id': record_id,
                    'active_step': 'deploy',
                },
            )
    else:
        initial = {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
        }
        form = DeployForm(initial=initial)

    return render(
        request,
        'deploy.html',
        {
            'solution': solution,
            'quote': quote,
            'form': form,
            'success': False,
            'active_step': 'deploy',
        },
    )


@login_required
def support(request):
    submission_id = request.session.get('last_submission_id')
    return render(
        request,
        'support.html',
        {
            'submission_id': submission_id,
            'active_step': 'support',
        },
    )
