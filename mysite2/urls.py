"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myapp import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',v.index),
    url(r'^fixtures',v.fixtures),
    url(r'^contact',v.contact),
    url(r'^historyoficc',v.historyoficc),
    url(r'^ranking',v.ranking),
    url(r'^vision',v.vision),
    url(r'^members',v.members),
    url(r'^gallery',v.gallery),
    url(r'^team',v.team),
    url(r'^batsman',v.batsman),
    url(r'^bowler',v.bowler),
    url(r'^allrounder',v.allrounder),
        
]

urlpatterns += staticfiles_urlpatterns()
