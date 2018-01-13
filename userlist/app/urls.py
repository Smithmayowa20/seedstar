from django.conf.urls import url
from . import views
from django.views.generic import (TemplateView, 
    RedirectView,
)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [url(r'^$',views.index,name='index'),
url(r'^list/$',views.list_users,name='list_users'),
url(r'^add/$',views.add_user,name='add_user')] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)