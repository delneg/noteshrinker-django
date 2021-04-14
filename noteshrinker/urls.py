from django.conf import settings
from django.conf.urls import url

from . import views
from .views import (
    PictureDeleteView,
)

app_name = 'noteshrinker'
urlpatterns = [
    url(r'^shrink$', views.shrink, name='shrink'),
    url(r'^download_pdf', views.download_pdf, name='download_pdf'),
    url(r'^download_zip', views.download_zip, name='download_zip'),
    url(r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), name='upload-delete'),
    # url(r'^view/$', PictureListView.as_view(), name='upload-view'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
