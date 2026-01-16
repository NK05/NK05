from typing import List


def compute_quote(solution, tier_name, addon_names, qty):
    tiers = solution.get('tiers', []) if solution else []
    addons = solution.get('addons', []) if solution else []
    tier_price = 0
    tier_label = None

    for tier in tiers:
        if tier['name'] == tier_name:
            tier_price = tier['price']
            tier_label = tier['name']
            break

    addon_names = addon_names or []
    addons_total = 0
    addon_labels: List[str] = []
    for addon in addons:
        if addon['name'] in addon_names:
            addons_total += addon['price']
            addon_labels.append(addon['name'])

    qty = qty or 1
    subtotal = tier_price + addons_total
    total = subtotal * qty

    breakdown_lines = []
    if tier_label:
        breakdown_lines.append(f"Tier: {tier_label} (${tier_price})")
    if addon_labels:
        breakdown_lines.append(f"Add-ons: {', '.join(addon_labels)} (${addons_total})")
    breakdown_lines.append(f"Quantity: {qty}")

    return {
        'base_price': tier_price,
        'addons_total': addons_total,
        'subtotal': subtotal,
        'total': total,
        'breakdown_lines': breakdown_lines,
    }
