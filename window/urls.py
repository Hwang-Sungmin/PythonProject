from django.urls import path
from . import views as window_views
app_name = "window"

urlpatterns = [
    path('window/', window_views.show, name = "show"),   
    path('test/', window_views.test, name='test')
]