"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include, patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rango import urls as rango_urls

from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'


urlpatterns = [
    #url(r'^$', 'rango.views.index_home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include(rango_urls)), # ADD THIS NEW TUPLE!
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
]

#The django-registration-redux package provides a number of different registration backends, depending on your needs. 
    #For example you may want a two-step process, where user are sent a confirmation email, and a verification link. 
    #Here we will be using the simple one-step registration process, where a user sets up their account by entering in a username, email, 
    #and password, and is automatically logged in.

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
