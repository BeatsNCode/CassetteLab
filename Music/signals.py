from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created

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

    print(user_email)
    print(reset_password_url)

    msg = EmailMessage(
    from_email='info@cassette-lab.com',
    to=[f'{user_email}'],
    )
    msg.template_id = "d-5ac6ba54547740aab7b7713362e4e34a"
    msg.dynamic_template_data = {
    "reset_password_url": reset_password_url
    }
    msg.send(fail_silently=False)