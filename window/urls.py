from django.urls import path
from . import views as window_views
app_name = "window"

urlpatterns = [
    path('window/', window_views.menu, name = "menu"),
    path('window/about', window_views.about, name = "about"),
   
    path('show/<str:topic_title>/', window_views.show, name='show'),
]