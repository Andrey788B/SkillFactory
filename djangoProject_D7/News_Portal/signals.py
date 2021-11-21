from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_managers
from .models import News


@receiver(post_save, sender=News) #sender - модель instance-сущность
def notify_managers_Appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.description} {instance.time}'
    else:
        subject = f'Appointment changed for {instance.description} {instance.time}'

    mail_managers(
        subject=subject,
        message=instance.message,
    )