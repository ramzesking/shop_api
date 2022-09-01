from django.core.mail import send_mail


def send_confirmation_email(user, code):
    # code = user.activation_code
    code = code
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    # to_email = user.email
    to_email = user
    send_mail(
        'Здравствуйте активийруйте ваш аккаунт!',
        f'Что-бы активировать ваш аккаунт нужно перейти по ссылке: {full_link}',
        'johnsnowtest73@gmail.com',
        [to_email,],
        fail_silently=False)

def send_notification(user, id):
    code=user.activation_code
    to_email=user.email
    send_mail(
        'Subject', 
        f'yout code for reset password:{code}',
        'from@example.com', 
        [to_email,],
        fail_silently=False
    )

def send_notofication(user,id):
    # code=user.activation_code
    to_email=user.email
    send_mail(
        'Уведомление о создании заказа!!!',
        f'Вы создали заказ номер:{id}б ожидайте звонка',
        'from@example.com',
        [to_email],
        fail_silently=False
    )