from django.urls import path
from . import views

app_name = 'CairBot'
urlpatterns = [
	path("chat/", views.home,name='home'),
	path('get-response/', views.get_response),
	path("display/", views.display,name='display'),
	path('classify/', views.classify),


	]






