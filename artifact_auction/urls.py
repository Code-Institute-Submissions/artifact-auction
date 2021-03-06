"""artifact_auction URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from home.views import index

from accounts import urls as urls_accounts
from artifacts import urls as urls_artifacts
from checkout import urls as urls_checkout
from collection import urls as urls_collection
from contact import urls as urls_contact
from history import urls as urls_history
from reviews import urls as urls_reviews
from search import urls as urls_search
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^admin/', admin.site.urls),
    url(r'^artifacts/', include(urls_artifacts)),
    url(r'^collection/', include(urls_collection)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^contact/', include(urls_contact)),
    url(r'^history/', include(urls_history)),
    url(r'^search/', include(urls_search)),    
    url(r'^review/', include(urls_reviews)),  
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
