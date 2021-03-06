from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from students import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="students/main.html")),
    url(r'^console/', TemplateView.as_view(template_name="students/console.html")),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    # API DATA
    url(r'^students_login/$', views.students_login, name='students_login'),
]

# Change admin site title
admin.site.site_header = ("Students Platform SQL")
admin.site.site_title = ("ST Platform")
