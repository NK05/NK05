from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'autocomplete': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))


class CustomizeForm(forms.Form):
    tier = forms.ChoiceField(required=False)
    addons = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple)
    qty = forms.IntegerField(min_value=1, initial=1)
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))

    def __init__(self, *args, **kwargs):
        solution = kwargs.pop('solution', None)
        super().__init__(*args, **kwargs)
        tier_choices = [('', 'Select a tier')]
        addon_choices = []
        if solution:
            tier_choices += [(tier['name'], f"{tier['name']} (${tier['price']})") for tier in solution.get('tiers', [])]
            addon_choices = [(addon['name'], f"{addon['name']} (${addon['price']})") for addon in solution.get('addons', [])]
        self.fields['tier'].choices = tier_choices
        self.fields['addons'].choices = addon_choices
        self.fields['tier'].widget.attrs.update({'class': 'form-select mt-2 w-full rounded-lg px-4 py-3'})
        self.fields['qty'].widget.attrs.update({'class': 'form-input mt-2 w-full rounded-lg px-4 py-3'})
        self.fields['notes'].widget.attrs.update({'class': 'form-textarea mt-2 w-full rounded-lg px-4 py-3'})


class DeployForm(forms.Form):
    name = forms.CharField(max_length=120)
    org = forms.CharField(label='Organization', max_length=160)
    email = forms.EmailField()
    phone = forms.CharField(required=False, max_length=40)
    preferred_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['name', 'org', 'email', 'phone', 'preferred_date']:
            self.fields[field_name].widget.attrs.update({'class': 'form-input mt-2 w-full rounded-lg px-4 py-3'})
        self.fields['notes'].widget.attrs.update({'class': 'form-textarea mt-2 w-full rounded-lg px-4 py-3'})
