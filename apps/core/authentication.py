from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAuthentication(JWTAuthentication):
    def get_header(self, request):
        raw_token = request.COOKIES.get('access')
        if raw_token:
            return f"Bearer {raw_token}"
        return None
