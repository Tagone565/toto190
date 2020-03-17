
from django.contrib import admin
from django.conf.urls import url, include
from .views import registerpage, home, Userlogout, service, contact, Aboutus, Myacount
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),
     url(r'',registerpage, name='register'),
     url('',home, name='login'),
     url(r'^logout/$',Userlogout, name='logout'),
     url(r'^service/$',service, name='service'),
     url(r'^contact/$',contact, name='contact'),
     url(r'^about/$', Aboutus, name='about'),
     url(r'^MyAccount/$', Myacount, name='account'),
     url(r'index/', include('Mypics.urls'))



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
