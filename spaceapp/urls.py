from django.urls import path
from . import views

app_name = 'spaceapp'

urlpatterns = [
    path('base/', views.base_page, name='base'),
    path('project/', views.project_page, name='project'),
    path('develops/', views.develops_page, name='develops'),
    path('feedback/', views.feedback_page, name='feedback'),
    path('GJ504b/', views.GJ504b_page, name='GJ504b'),
    path('gliese/', views.gliese_page, name='gliese'),
    path('kepler/', views.kepler_page, name='kepler'),
    path('nimro/', views.nimro_page, name='nimro'),
    path('prometheus/', views.prometheus_page, name='prometheus'),
    path('tanos/', views.tanos_page, name='tanos'),
    path('chimaira/', views.chimaira_page, name='chimaira'),
    path('search/', views.search_box_action, name='search'),
    ]
