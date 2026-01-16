import json
import random
import string
from datetime import datetime
from pathlib import Path

from django.conf import settings


def _storage_path():
    storage_dir = Path(settings.BASE_DIR) / 'storage'
    storage_dir.mkdir(parents=True, exist_ok=True)
    return storage_dir / 'quote_requests.json'


def _safe_load_records(path):
    if not path.exists():
        return []
    try:
        with path.open('r', encoding='utf-8') as handle:
            data = json.load(handle)
        if isinstance(data, list):
            return data
    except json.JSONDecodeError:
        backup_name = f"quote_requests.corrupt.{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.json"
        backup_path = path.with_name(backup_name)
        try:
            path.replace(backup_path)
        except OSError:
            pass
    return []


def _generate_record_id():
    stamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"QR-{stamp}-{suffix}"


def append_quote_request(record):
    path = _storage_path()
    records = _safe_load_records(path)
    record_id = _generate_record_id()
    record['id'] = record_id
    records.append(record)
    with path.open('w', encoding='utf-8') as handle:
        json.dump(records, handle, indent=2)
    return record_id
