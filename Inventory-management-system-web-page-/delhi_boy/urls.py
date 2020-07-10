from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
urlpatterns = [

    path('',views.signup,name='signup'),
    path('content/',views.goods_smuggle,name='content'),
    path('home/',views.homepage,name='home')

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
