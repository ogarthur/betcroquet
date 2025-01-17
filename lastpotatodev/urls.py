"""lastpotatodev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from main_app import views as mViews
from betcroquet_app import views as bViews
from user_mgmt_app import views as uViews

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',bViews.index,name='index'),
    path('admin/', admin.site.urls),
    path('main_app/',include('main_app.urls')),
    path('user_mgmt_app/',include('user_mgmt_app.urls')),
    path('betcroquet_app/',include('betcroquet_app.urls')),
    #path('logout/',views.user_logout,name='logout'),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
