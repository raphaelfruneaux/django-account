from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'gsti.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('polls.urls')),
    url(r'^account/', include('account.urls', namespace="account")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
