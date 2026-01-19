from datetime import datetime
from apps.core.constants.id_prefixes import ROLE_PREFIX_MAP

def generate_user_ids(user_id: int, role: int) -> str:
    prefix = ROLE_PREFIX_MAP.get(role)

    if not prefix:
        raise ValueError("Invalid user role")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefix}-{timestamp}-{user_id:06d}"
