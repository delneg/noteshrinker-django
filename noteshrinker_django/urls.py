"""noteshrinker_django URL Configuration

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
from django.conf.urls import include,url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from noteshrinker import views as noteshrinker_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('noteshrinker.urls'))

]
urlpatterns += i18n_patterns(
    url(_(r'^$'), noteshrinker_views.PictureCreateView.as_view(), name='index'),
)
