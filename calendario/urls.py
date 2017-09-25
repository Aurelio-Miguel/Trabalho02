from django.conf.urls import url
from django.contrib import admin

from agenda.views import agenda


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^agendas/', agenda, name='agenda'),
    url(r'^agendas/usuario/(\+d)/', agenda, name='agenda'),
]
