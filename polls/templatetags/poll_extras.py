
from polls.models import Customer, Video
from django import template
register = template.Library()

@register.simple_tag()
def get_customer():
    return Customer.objects.all()

@register.simple_tag()
def get_video():
    return Video.objects.all()