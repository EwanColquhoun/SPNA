from django.core.mail import send_mail


# stackmail is what mark uses

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
        https://8000-ewancolquhoun-spna-jrhwr7uwb6e.ws-eu38.gitpod.io/spna_admin/
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
        Username - {user.username}
        First Name - {user.first_name}
        Last Name - {user.last_name}
        Email - {user.email}
        Message - {user.message}
        Click here to visit the admin site
        https://8000-ewancolquhoun-spna-jrhwr7uwb6e.ws-eu38.gitpod.io/spna_admin/
        Thanks.""",
        None,
        ['info@scottishpna.org'],
        fail_silently=True,
    )


def send_admin_email(form):
    """
    Retrieves the form data and send email accordingly.
    """
    subject = form.email_subject
    message = form.email_body
    from_email = 'info@scottishpna.org'
    
    addys = form.email_to
    # print(type(addys), 'addys type')
    email_list = addys.strip('][').split(', ')
    # print(type(email_list), 'email list type')
    recipient_list = email_list

    # print(subject, message, from_email, recipient_list)
    
    send_mail(subject, message, from_email, recipient_list)
