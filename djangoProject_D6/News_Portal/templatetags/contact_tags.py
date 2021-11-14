from django import template
from News_Portal.forms import ContactForm

register = template.Library()


@register.inclusion_tag("flatpages/form.html")
def contact_form():
    return {"contact_form": ContactForm()}
