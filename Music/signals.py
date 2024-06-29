from django.core.cache import cache
from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from datetime import datetime, timedelta

# Define the time interval for rate limiting (15 minutes)
RATE_LIMIT_INTERVAL = timedelta(minutes=15)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """

    user_email = reset_password_token.user.email
    reset_password_url = "{}?token={}".format(
        instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
        reset_password_token.key
    )

    # Generate a unique cache key for each user
    cache_key = f"password_reset_email_last_sent_{user_email}"

    # Check when the last email was sent
    last_sent_time = cache.get(cache_key)


    if last_sent_time is None or (datetime.now() - last_sent_time) > RATE_LIMIT_INTERVAL:
        # If last_sent_time is None (no email sent before) or enough time has passed, send the email
        msg = EmailMessage(
            from_email='info@cassette-lab.com',
            to=[f'{user_email}']
        )
        msg.template_id = "d-5ac6ba54547740aab7b7713362e4e34a"
        msg.dynamic_template_data = {
            "reset_password_url": reset_password_url
        }
        msg.send(fail_silently=False)

        # Update the cache with the current timestamp
        cache.set(cache_key, datetime.now(), RATE_LIMIT_INTERVAL.total_seconds())

        print(f"Password reset email sent to {user_email}")
    else:
        # Rate limit exceeded, do not send another email
        print(f"Rate limit exceeded for sending password reset email to {user_email}")
