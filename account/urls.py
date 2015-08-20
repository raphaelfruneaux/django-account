from django.conf.urls import url

import views


urlpatterns = [
    url(r'^sign-in/$', views.sign_in, name='signin'),
    url(r'^sign-up/$', views.sign_up, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    ]