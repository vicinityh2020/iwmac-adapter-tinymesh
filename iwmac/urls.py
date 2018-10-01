from django.urls import path

from . import views

urlpatterns = [
    path('objects', views.thing_descriptor, name='objects_view'),
    path('test-event', views.test_event, name='test_event')
]