from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

# Emails to Admin
def contact_email(contact):
    """
    Sends the admin an email when there is a new contact request.
    """
    send_mail(
        'Contact Request',
        f"""
        CONTACT,
        You have a new contact request from {contact.name}
        Telephone - {contact.phone_number}
        Email - {contact.email}
        Message - {contact.message}
        Click here to visit the admin site
        https://scottishpna.herokuapp.com/spna_admin/
        Thanks.""",
        None,
        ['info@scottishpna.org'],
        fail_silently=True,
    )

def cancel_email(user):
    """
    Sends the admin an email when the member cancels sub.
    """
    send_mail(
        'Cancelled Subscription',
        f"""
        Cancelled SPNA MEMBERSHIP,
        {user.spnamember.fullname} has chosen to end their subscription on {user.spnamember.paid_until}.
        Here are their details:
        Email - {user.email}
        Phone - {user.spnamember.phone}
        Nursery - {user.spnamember.nursery}

        Click here to visit the admin site
        https://scottishpna.herokuapp.com/spna_admin/
        Thanks.""",
        None,
        ['info@scottishpna.org'],
        fail_silently=True,
    )

def payment_error_admin(request, error, payment):
    """
    Sends the admin an email when there is a payment error.
    """
    send_mail(
        'Payment error',
        f"""
        Payment error with Stripe,

        Full Name - {request.user.spnamember.fullname}
        Email - {request.user.email}
        Phone - {request.user.spnamember.phone}
        Nursery - {request.user.spnamember.nursery}
        Subscription Renewal date - {request.user.spnamember.paid_until}

        Type = {payment}
        There was a problem with payment. Please check the stripe dashboard for more information:
        Error: {error}

        Click here to visit the admin site
        https://scottishpna.herokuapp.com/spna_admin/
        Thanks.""",
        None,
        ['info@scottishpna.org'],
        fail_silently=True,
    )

def register_email(user):
    """
    Sends the admin an email when there is a new member signup.
    """
    send_mail(
        'New Member',
        f"""
        NEW MEMBER,
        You have a new member request from {user.first_name}
        Full Name - {user.spnamember.fullname}
        Email - {user.email}
        Phone - {user.spnamember.phone}
        Nursery - {user.spnamember.nursery}
        Subscription Renewal date - {user.spnamember.paid_until}

        Click here to visit the admin site
        https://scottishpna.herokuapp.com/spna_admin/
        Thanks.""",
        None,
        ['info@scottishpna.org'],
        fail_silently=True,
    )


# Emails to Member
def cancel_email_to_member(user):
    """
    Sends the admin an email when the member cancels sub.
    """
    send_mail(
        'SPNA Subscription cancelled',
        f"""
        Hi {user.spnamember.fullname},

        We are sorry to see that you are leaving the SPNA. Please get in touch
        if there is anyting we can do to change your mind regarding your membership.

        Kind regards,

        The SPNA team.

        """,
        None,
        [{user.email}],
        fail_silently=True,
    )

def welcome_email_to_member(user):
    """
    Sends the admin an email when the member cancels sub.
    """
    send_mail(
        'Welcome to the SPNA',
        f"""
        Hi {user.first_name},

        Welcome to the Scottish Private Nursery Association (SPNA). We are delighted to have you on board.
        We are always looking for member contributions or feedback, so please don't hesitate to get in touch
        with us at:
            info@spna.org


        Kind regards,

        The SPNA team.

        """,
        None,
        [{user.email}],
        fail_silently=True,
    )

def upgrade_email_to_member(member):
    """
    Sends the member an email when their subscription has been updated.
    """
    send_mail(
        'SPNA Subscription changed',
        f"""
        Hi {member.user.first_name},

        The change to your subscription has been successful. Thank you!

        Your plan is now {member.subscription}, valid until {member.paid_until}
        If you did not request a change please contact us at: info@scottishpna.org


        Kind regards,

        The SPNA team.

        """,
        None,
        [{member.user.email}],
        fail_silently=True,
    )

def failed_payment_to_member(user):
    """
    Sends the member an email when their payment fails.
    """
    send_mail(
        'SPNA - Failed payment method',
        f"""
        Hi {user.first_name},

        Please be advised that your payment has failed for your SPNA subscription. Please login to
        scottishpna.herokuapp.com to update your payment methods on your profile page. Payments will take a few days to process. If you haven't received
        a confirmation email after that time, please contact admin.

        Kind regards,

        The SPNA team.

        """,
        None,
        [{user.email}],
        fail_silently=True,
    )

# Email from Admin
def send_admin_email(form):
    """
    Retrieves the form data and send email accordingly.
    """
    subject = form.email_subject
    msg = form.email_body.strip('<p>')  #does not work. need to strip characters or get rid of html tags.
    message = msg
    from_email = settings.DEFAULT_FROM_EMAIL

    addys = form.email_to
    email_list = addys.strip('][').split(', ')
    recipient_list = email_list

    message_one = (subject, message, from_email, recipient_list)
    # print(subject, message, from_email, recipient_list)

    send_mass_mail((message_one,), fail_silently=False)

def test_email():

    send_mail(
        'SPNA - Failed payment method',
        """
        Hi, this is a test email
        """,
        None,
        [{'ewancolquhoun@hotmail.com'}],
        fail_silently=True,
    )