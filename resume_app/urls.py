from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("",views.index, name='resume'),
    path('index', views.index, name='index'),
    path('project', views.project, name='project'),
    path('blog', views.blog, name='blog'),
    path('addblog', views.addblogs),
    path('contact', views.contact, name='contact'),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
