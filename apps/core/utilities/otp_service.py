import random
import re
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail

OTP_EXPIRY_SECONDS = 300  # 5 minutes
OTP_ATTEMPT_LIMIT = 5
OTP_SEND_LIMIT = 5
OTP_RESEND_COOLDOWN = 30  # seconds

def generate_otp():
    return str(random.randint(100000, 999999))

def is_valid_contact(contact):    
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    phone_regex = r'^\+?\d{10,15}$'
    return bool(re.match(email_regex, contact) or re.match(phone_regex, contact))

def send_otp_code(contact, purpose="login"):
    if not is_valid_contact(contact):
        return None, "Invalid contact"

    send_key = f"otp_send_count:{contact}:{purpose}"
    last_sent_key = f"otp_last_sent:{contact}:{purpose}"

    if cache.get(last_sent_key):
        return None, "Please wait before requesting another OTP."

    send_count = cache.get(send_key, 0)
    if send_count >= OTP_SEND_LIMIT:
        return None, "OTP send limit reached. Try later."

    otp_code = generate_otp()
    cache.set(f"otp:{contact}:{purpose}", otp_code, timeout=OTP_EXPIRY_SECONDS)
    cache.set(send_key, send_count + 1, timeout=3600)  # 1 hour send limit
    cache.set(last_sent_key, True, timeout=OTP_RESEND_COOLDOWN)  # cooldown

    send_mail(
        subject="Your OTP Code",
        message=f"Your OTP code is {otp_code}. It will expire in {OTP_EXPIRY_SECONDS // 60} minutes.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[contact],
        fail_silently=False,
    )
    print(f"[DEBUG] OTP for {contact} is {otp_code}")

    return otp_code, None

def verify_otp_code(contact, otp_code, purpose="login"):
    cache_key = f"otp:{contact}:{purpose}"
    stored_code = cache.get(cache_key)

    if not stored_code:
        return False, "OTP expired"

    attempt_key = f"otp_attempt:{contact}:{purpose}"
    attempts = cache.get(attempt_key, 0)
    if attempts >= OTP_ATTEMPT_LIMIT:
        return False, "Too many failed attempts"

    if stored_code == otp_code:
        cache.delete(cache_key)
        cache.delete(attempt_key)
        return True, None

    cache.set(attempt_key, attempts + 1, timeout=OTP_EXPIRY_SECONDS)
    return False, "Invalid OTP"
