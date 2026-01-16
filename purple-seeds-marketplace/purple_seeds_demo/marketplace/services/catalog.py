CATALOG = [
    {
        'id': 'ps_hr',
        'slug': 'hr-module',
        'suite': 'software',
        'subcategory': 'People Ops',
        'title': 'HR Module',
        'short_description': 'Automate onboarding, payroll sync, and performance reviews with a unified HR hub.',
        'best_for': ['Growing teams', 'Policy compliance', 'Manager self-service'],
        'features': ['Onboarding workflows', 'Leave management', 'Performance reviews', 'Document vault'],
        'tiers': [
            {'name': 'Essentials', 'price': 45},
            {'name': 'Growth', 'price': 95},
            {'name': 'Enterprise', 'price': 165},
        ],
        'addons': [
            {'name': 'Payroll Sync', 'price': 35},
            {'name': 'Compliance Toolkit', 'price': 25},
        ],
    },
    {
        'id': 'ps_crm',
        'slug': 'crm',
        'suite': 'software',
        'subcategory': 'Revenue',
        'title': 'CRM',
        'short_description': 'Pipeline visibility, automated follow-ups, and unified customer profiles.',
        'best_for': ['Sales teams', 'Account managers', 'Forecast accuracy'],
        'features': ['Deal stages', 'Email sequences', 'Customer timeline', 'Revenue analytics'],
        'tiers': [
            {'name': 'Starter', 'price': 59},
            {'name': 'Professional', 'price': 119},
            {'name': 'Elite', 'price': 189},
        ],
        'addons': [
            {'name': 'Conversation Intelligence', 'price': 40},
            {'name': 'Sales Playbooks', 'price': 30},
            {'name': 'Forecast AI', 'price': 55},
        ],
    },
    {
        'id': 'ps_erp',
        'slug': 'erp-core',
        'suite': 'software',
        'subcategory': 'Operations',
        'title': 'ERP Core',
        'short_description': 'Unified finance, procurement, and inventory controls built for scale.',
        'best_for': ['Multi-location ops', 'Inventory-heavy teams', 'Finance leaders'],
        'features': ['Procurement workflows', 'Inventory planning', 'Multi-entity ledger', 'Audit trails'],
        'tiers': [
            {'name': 'Foundation', 'price': 140},
            {'name': 'Scale', 'price': 240},
        ],
        'addons': [
            {'name': 'Advanced Forecasting', 'price': 60},
            {'name': 'Vendor Portal', 'price': 35},
        ],
    },
    {
        'id': 'ps_pos',
        'slug': 'pos',
        'suite': 'software',
        'subcategory': 'Retail',
        'title': 'POS',
        'short_description': 'Fast checkout, synchronized inventory, and omnichannel reporting.',
        'best_for': ['Retail stores', 'Pop-ups', 'Multi-store managers'],
        'features': ['Barcode scanning', 'Mobile checkout', 'Inventory sync', 'Promotions engine'],
        'tiers': [
            {'name': 'Counter', 'price': 39},
            {'name': 'Omni', 'price': 89},
        ],
        'addons': [
            {'name': 'Loyalty Program', 'price': 20},
            {'name': 'Gift Cards', 'price': 15},
        ],
    },
    {
        'id': 'ps_lms',
        'slug': 'lms',
        'suite': 'software',
        'subcategory': 'Training',
        'title': 'LMS',
        'short_description': 'Launch courses, track completion, and certify teams at scale.',
        'best_for': ['Enablement', 'Compliance training', 'Customer education'],
        'features': ['Course builder', 'Live sessions', 'Certificates', 'Progress analytics'],
        'tiers': [
            {'name': 'Launch', 'price': 49},
            {'name': 'Accelerate', 'price': 99},
        ],
        'addons': [
            {'name': 'Content Library', 'price': 35},
        ],
    },
    {
        'id': 'ps_projects',
        'slug': 'project-management',
        'suite': 'software',
        'subcategory': 'Operations',
        'title': 'Project Management',
        'short_description': 'Plan, assign, and ship work with real-time delivery tracking.',
        'best_for': ['Cross-functional teams', 'Client delivery', 'Resource planning'],
        'features': ['Gantt timelines', 'Workload views', 'Client portals', 'Automations'],
        'tiers': [
            {'name': 'Team', 'price': 44},
            {'name': 'Studio', 'price': 88},
        ],
        'addons': [
            {'name': 'Resource Forecasting', 'price': 30},
        ],
    },
    {
        'id': 'ps_accounting',
        'slug': 'accounting-suite',
        'suite': 'software',
        'subcategory': 'Finance',
        'title': 'Accounting Suite',
        'short_description': 'Automated invoicing, reconciliation, and cash-flow insights.',
        'best_for': ['Finance teams', 'Consultancies', 'Service businesses'],
        'features': ['Invoicing', 'Bank sync', 'Expense controls', 'Revenue dashboards'],
        'tiers': [
            {'name': 'Ledger', 'price': 55},
            {'name': 'Controller', 'price': 110},
        ],
        'addons': [
            {'name': 'Multi-currency', 'price': 25},
            {'name': 'Revenue Recognition', 'price': 45},
        ],
    },
    {
        'id': 'ps_field',
        'slug': 'field-service',
        'suite': 'software',
        'subcategory': 'Operations',
        'title': 'Field Service',
        'short_description': 'Dispatch technicians, optimize routes, and capture signatures onsite.',
        'best_for': ['Service teams', 'Facilities', 'Maintenance providers'],
        'features': ['Dispatch board', 'Route optimization', 'Mobile forms', 'Asset history'],
        'tiers': [
            {'name': 'Dispatch', 'price': 69},
            {'name': 'Optimize', 'price': 129},
        ],
        'addons': [
            {'name': 'Customer SMS Alerts', 'price': 18},
        ],
    },
    {
        'id': 'ps_inventory',
        'slug': 'inventory-control',
        'suite': 'software',
        'subcategory': 'Supply Chain',
        'title': 'Inventory Control',
        'short_description': 'Real-time stock accuracy with forecasting and reorder automation.',
        'best_for': ['Warehouses', 'Retail chains', 'Manufacturers'],
        'features': ['Cycle counts', 'Reorder points', 'Batch tracking', 'Supplier analytics'],
        'tiers': [
            {'name': 'Stock', 'price': 65},
            {'name': 'Predict', 'price': 125},
        ],
        'addons': [
            {'name': 'RFID Integration', 'price': 50},
        ],
    },
    {
        'id': 'ps_it_office',
        'slug': 'it-office',
        'suite': 'hardware',
        'subcategory': 'IT & Office',
        'title': 'IT & Office Kit',
        'short_description': 'Device bundles, network setup, and secure endpoint management.',
        'best_for': ['New offices', 'Hybrid teams', 'IT refresh cycles'],
        'features': ['Device provisioning', 'Network baseline', 'Endpoint security', 'Asset labeling'],
        'tiers': [
            {'name': 'Essential', 'price': 220},
            {'name': 'Pro', 'price': 420},
        ],
        'addons': [
            {'name': 'Onsite Setup', 'price': 180},
            {'name': 'Extended Warranty', 'price': 75},
        ],
    },
    {
        'id': 'ps_security',
        'slug': 'security-systems',
        'suite': 'hardware',
        'subcategory': 'Security Systems',
        'title': 'Security Systems',
        'short_description': 'Integrated access control, cameras, and monitoring dashboards.',
        'best_for': ['Facilities', 'Retail', 'Corporate campuses'],
        'features': ['HD cameras', 'Access control', 'Incident alerts', 'Cloud monitoring'],
        'tiers': [
            {'name': 'Monitor', 'price': 300},
            {'name': 'Guardian', 'price': 520},
        ],
        'addons': [
            {'name': '24/7 Monitoring', 'price': 90},
            {'name': 'Smart Locks', 'price': 65},
        ],
    },
    {
        'id': 'ps_retail_hardware',
        'slug': 'retail-hardware',
        'suite': 'hardware',
        'subcategory': 'Retail',
        'title': 'Retail Hardware',
        'short_description': 'Counter-ready scanners, printers, and payment terminals.',
        'best_for': ['Brick-and-mortar', 'Pop-up shops', 'Fast checkout'],
        'features': ['Receipt printers', 'Barcode scanners', 'Payment terminals', 'Device staging'],
        'tiers': [
            {'name': 'Counter', 'price': 260},
            {'name': 'Multi-lane', 'price': 460},
        ],
        'addons': [
            {'name': 'Spare Devices', 'price': 80},
        ],
    },
    {
        'id': 'ps_display',
        'slug': 'display-communication',
        'suite': 'hardware',
        'subcategory': 'Display & Communication',
        'title': 'Display & Communication',
        'short_description': 'Digital signage and unified communications for modern spaces.',
        'best_for': ['Retail signage', 'Corporate comms', 'Hospitality'],
        'features': ['4K displays', 'Content scheduling', 'Unified comms', 'Remote monitoring'],
        'tiers': [
            {'name': 'Signage', 'price': 280},
            {'name': 'Experience', 'price': 510},
        ],
        'addons': [
            {'name': 'Content Studio', 'price': 40},
        ],
    },
    {
        'id': 'ps_hosting',
        'slug': 'hosting-domain',
        'suite': 'web_cloud',
        'subcategory': 'Hosting & Domain',
        'title': 'Hosting & Domain',
        'short_description': 'Performance hosting, domain management, and SSL security.',
        'best_for': ['New websites', 'Fast migrations', 'Marketing teams'],
        'features': ['Managed hosting', 'SSL certificates', 'Global CDN', 'Daily backups'],
        'tiers': [
            {'name': 'Launch', 'price': 35},
            {'name': 'Scale', 'price': 79},
        ],
        'addons': [
            {'name': 'Managed SEO', 'price': 45},
            {'name': 'Migration Support', 'price': 55},
        ],
    },
    {
        'id': 'ps_backup',
        'slug': 'cloud-backup-failover',
        'suite': 'web_cloud',
        'subcategory': 'Cloud Backup & Failover',
        'title': 'Cloud Backup & Failover',
        'short_description': 'Protect critical data with automated backups and recovery.',
        'best_for': ['Regulated teams', 'High availability', 'Risk mitigation'],
        'features': ['Geo-redundant storage', 'Recovery testing', 'RTO dashboards', 'Encryption'],
        'tiers': [
            {'name': 'Secure', 'price': 85},
            {'name': 'Resilient', 'price': 155},
        ],
        'addons': [
            {'name': 'Disaster Simulation', 'price': 70},
        ],
    },
    {
        'id': 'ps_clinics',
        'slug': 'tech-clinics-onsite',
        'suite': 'web_cloud',
        'subcategory': 'Tech Clinics & Onsite IT Support',
        'title': 'Tech Clinics & Onsite IT Support',
        'short_description': 'Scheduled onsite IT sessions plus remote helpdesk coverage.',
        'best_for': ['Hybrid teams', 'IT backlog relief', 'Quarterly audits'],
        'features': ['Onsite clinics', 'Remote helpdesk', 'Device tune-ups', 'IT roadmaps'],
        'tiers': [
            {'name': 'Clinic', 'price': 120},
            {'name': 'Managed', 'price': 210},
        ],
        'addons': [
            {'name': 'Executive Desk', 'price': 60},
        ],
    },
    {
        'id': 'ps_collab',
        'slug': 'collaboration-tools',
        'suite': 'web_cloud',
        'subcategory': 'Collaboration Tools',
        'title': 'Collaboration Tools',
        'short_description': 'Secure chat, video, and file sharing tuned for productivity.',
        'best_for': ['Distributed teams', 'Client collaboration', 'Project delivery'],
        'features': ['Chat channels', 'Video rooms', 'Shared drives', 'Guest access'],
        'tiers': [
            {'name': 'Teamwork', 'price': 49},
            {'name': 'Workspace', 'price': 95},
        ],
        'addons': [
            {'name': 'Compliance Archive', 'price': 28},
        ],
    },
]


def list_suites():
    return [
        {'key': 'software', 'label': 'Software Suite'},
        {'key': 'hardware', 'label': 'Hardware Suite'},
        {'key': 'web_cloud', 'label': 'Web & Cloud Services'},
    ]


def list_subcategories(suite_key):
    subcats = [item['subcategory'] for item in CATALOG if item['suite'] == suite_key]
    return sorted(set(subcats))


def list_solutions(suite=None, subcat=None, q=None):
    results = CATALOG
    if suite:
        results = [item for item in results if item['suite'] == suite]
    if subcat:
        results = [item for item in results if item['subcategory'].lower() == subcat.lower()]
    if q:
        needle = q.strip().lower()
        if needle:
            results = [
                item for item in results
                if needle in item['title'].lower() or needle in item['short_description'].lower()
            ]
    return results


def get_solution_by_slug(slug):
    for item in CATALOG:
        if item['slug'] == slug:
            return item
    return None


def get_solution_by_id(item_id):
    for item in CATALOG:
        if item['id'] == item_id:
            return item
    return None
