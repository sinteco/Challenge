from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'jenkins_job.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('DjangoApp.urls'))
]
