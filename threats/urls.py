from django.conf.urls import url, include
from rest_framework import routers
import views

urlpatterns = [
    url(r'^$', views.APIRoot.as_view(), name='api_root'),
    url(r'^api/details/(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)$', views.IPDetailsView.as_view(), name='threat_details'),
    url(r'^api/details/$', views.IPList.as_view(), name='threat_list'),
    url(r'^api/traffic/$', views.VisitorList.as_view(), name='visitor_traffic'),
]
