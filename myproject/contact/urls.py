from django.conf.urls import url
from .forms import ContactForm
from contact import views

urlpatterns = (
    url(r'^$', views.contact, name='contact'),
)