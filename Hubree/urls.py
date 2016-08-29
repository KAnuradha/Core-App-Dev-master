"""Hubree URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# from registration.views import create_user, register_user, register_form, home
# from login.views import login_user, login
# from activate.views import activate_user
# from signup.views import signup
from registration.views import create, generate_email, resend,accounts
from login.views import home, log_in, login, forgot,password
from activate.views import activate_user
from signup.views import signup
from property.views import main, show, save_property

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home),
    url(r'^signup/$',signup),
    url(r'^log_in/$',log_in),
    url(r'^login/$', login),
    url(r'^create/$', create),
    url(r'^forgot/$',password),
    url(r'^forgotpassword/$', forgot),
    url(r'^generate_email/$',generate_email),
    url(r'^activate_user/$', activate_user), 
    url(r'^accounts/$', accounts),
    url(r'^resend/$', resend),
    url(r'^main/$', main),
    url(r'^show/$', show),
    url(r'^save_property/$',save_property),
]
