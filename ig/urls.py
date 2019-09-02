from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns=[
    url('^home/$',views.index,name = 'index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$',views.signup, name='signup'),  
    url(r'^logout/$',auth_views.logout, {"next_page": '/'}),
    url(r'^login/$',auth_views.login, {"next_page": '/'}), 
    url(r'^admin/', admin.site.urls),
    url('profile/', views.index, name='profile'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^image/(?P<image_id>\d+)', views.image, name='image'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
    url(r'^search/', views.search, name='search'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)