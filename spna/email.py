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
        Click here to visit the admin site
        https://scottishpna.herokuapp.com/spna_admin/
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
    msg = form.email_body.strip('<p>')  #does not work. need to strip characters or get rid of html tags.
    print(msg, 'msg')
    message = msg
    from_email = 'info@scottishpna.org'
    
    addys = form.email_to
    # print(type(addys), 'addys type')
    email_list = addys.strip('][').split(', ')
    # print(type(email_list), 'email list type')
    recipient_list = email_list

    # print(subject, message, from_email, recipient_list)
    
    send_mail(subject, message, from_email, recipient_list)
