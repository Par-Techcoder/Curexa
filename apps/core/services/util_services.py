from django.utils import timezone

def full_name(first, middle, last):
    """Return a full name display name like 'John D. Doe'."""
    if middle:
        return f"{first} {middle[0]}. {last}"
    return f"{first} {last}"

def enum_name(enum_cls, value, default=None):
    """Get enum name from value, or default if not found."""
    if value in enum_cls._value2member_map_:
        return enum_cls(value).name
    return default



def age_from_dob(dob, on_date=None):
    """Calculate age from date of birth."""
    if not dob:
        return None   # or 0, or "", based on API needs

    if on_date is None:
        on_date = timezone.now().date()

    years = on_date.year - dob.year
    if (on_date.month, on_date.day) < (dob.month, dob.day):
        years -= 1
    return years