from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^api/user/(?P<user_id>[0-9]+)/$', views.getUser, name='getUser'),
    # ex: /polls/5/results/
    url(r'^(?P<user_id>[0-9]+)/results/$', views.results, name='results'),

]