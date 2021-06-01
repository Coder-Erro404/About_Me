from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("",views.index, name='resume'),
    path('index', views.index, name='index'),
    path('project', views.projects, name='project'),
    path('blogs', views.blogs , name='blogs'),
    path('documents', views.documents , name='documents'),
    # path('addblog', views.addblogs),
    path('contact', views.contact, name='contact'),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
