from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^api/user/(?P<user_id>[0-9]+)/$', views.getUser, name='getUser'),
    url(r'^api/user/', views.getAllUsers, name='getAllUsers'),
    url(r'^api/job/', views.getAllJobs, name='getAllJobs'),
    url(r'^api/job/(?P<job_id>[0-9]+)/$', views.getJob, name='getJob'),
]