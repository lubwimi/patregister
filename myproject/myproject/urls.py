"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from patregister import views
from contact import views as contactviews

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', contactviews.contact, name='contact'),
    url(r'^register/$', views.registform, name='register'),
    url(r'^medlem/$', views.medlem, name='medlem'),
    url(r'^get/(?P<medlem_id>\d+)/$', views.your_medlem),
    url(r'^search/$', views.search_medlem, name='search'),
    url(r'^registuser/$', views.registeruser, name='registuser'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^medlem/delete/(?P<medlem_id>[0-9]+)/$', views.delete, name='delete'),
    
    url(r'^admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
