"""ops_server URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from cmdb import views
from utils import get_code_img

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^api/', include("api.urls")),
    url(r'^cmdb/', include("cmdb.urls")),
    url(r'^rbac/', include("rbac.urls")),
    url(r'^firmware/', include("firmware.urls")),
    url(r'^task/', include("task.urls")),
    url(r'^login/', views.login),
    url(r'^get_code/', get_code_img.get_code),
    url(r'^logout/', views.logout),
    url(r'^index/', views.index),
    url(r'^index_v3/', views.index_v3),
    url(r'^403/', views.forbidden),
    url(r'^$', views.index),

]

handler404 = views.page_not_found