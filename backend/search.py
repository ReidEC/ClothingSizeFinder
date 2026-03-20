import os
import json

BASE_DIR = os.path.dirname(__file__)
CHART_PATH = os.path.join(BASE_DIR, 'size_charts.json')

with open(CHART_PATH, 'r', encoding='utf-8') as f:
    SIZE_DATA = json.load(f).get('brands', [])

def _to_float(val):
    try:
        return float(val)
    except (TypeError, ValueError):
        return None

def _in_range_with_margin(user_val, range_pair, margin=2.0):
    if user_val is None:
        return True
    try:
        low, high = float(range_pair[0]), float(range_pair[1])
    except Exception:
        return False
    return (user_val >= (low - margin)) and (user_val <= (high + margin))

def search_clothing(dimensions, description=None, type=None):
    """
    dimensions: dict with keys 'chest','waist','neck','sleeve','inseam' (in inches)
    description: optional string
    type: 'tops' or 'bottoms'
    Returns: dict with results list
    """
    if not isinstance(dimensions, dict):
        return {'query': description or '', 'dimensions': dimensions, 'results': [], 'total': 0}

    user = {
        'chest': _to_float(dimensions.get('chest')),
        'waist': _to_float(dimensions.get('waist')),
        'neck':  _to_float(dimensions.get('neck')),
        'sleeve': _to_float(dimensions.get('sleeve')),
        'inseam': _to_float(dimensions.get('inseam'))
    }

    print(f"DEBUG: User measurements = {user}")
    print(f"DEBUG: SIZE_DATA loaded = {len(SIZE_DATA)} brands")

    req_type = None
    if description:
        desc = description.lower()
        if 'hoodie' in desc or 'shirt' in desc:
            req_type = 'shirt'
    if type == 'bottoms':
        req_type = 'bottoms'  # add logic for bottoms if needed

    print(f"DEBUG: Requested type = {req_type}")

    matches = []
    for brand in SIZE_DATA:
        if req_type and req_type not in brand.get('type', []):
            continue
        for size_label, measures in brand.get('sizes', {}).items():
            ok = True
            for key in ('chest', 'waist', 'neck', 'sleeve', 'inseam'):
                user_val = user.get(key)
                if user_val is None:
                    continue
                if key not in measures:
                    ok = False
                    break
                if not _in_range_with_margin(user_val, measures[key], margin=2.0):
                    ok = False
                    break
            if ok:
                print(f"DEBUG: Match found - {brand.get('name')} {size_label}")
                matches.append({
                    'brand': brand.get('name'),
                    'size': size_label,
                    'measurements': measures,
                    'type': brand.get('type', [])
                })

    print(f"DEBUG: Total matches = {len(matches)}")
    
    return {
        'query': description or '',
        'dimensions': dimensions,
        'type': type,
        'results': matches,
        'total': len(matches)
    }