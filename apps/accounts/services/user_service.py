from apps.accounts.models import User

def user_create_or_check(email):
    """
    Create a user if it doesn't exist or return the existing user.
    """
    user = User.objects.get_or_create(email=email,defaults={"username": email.split("@")[0]})
    return user