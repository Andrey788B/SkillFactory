from time import sleep
from django.core.mail import send_mail


@app.task
def send_email_task():
  sleep(10)
  send_mail('Тема письма', 'Тело письма', 'адрес_отправителя@mail.com', ['адрес_получателя@mail.com'])

