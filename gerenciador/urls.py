"""gerenciador URL Configuration

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

from agenda import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.lista),
    url(r'^adiciona/$', views.adiciona),
    url(r'^item/(?P<nr_item>\d+)/$', views.item),
    url(r'^remove/(?P<nr_item>\d+)/$', views.remove),
=======
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.lista),
    url(r'adiciona/$', views.adiciona),
    url(r'^admin/', admin.site.urls ),
>>>>>>> e40b9e8788a8e771bf01112953d17bc201882407




]
