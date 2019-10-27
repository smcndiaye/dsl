from django.urls import path
from . import views


app_name = 'cair'
urlpatterns = [
    path('mededice/', views.simple_upload, name='simple_upload'),
	#path('offres/', views.offres, name='offres'),
	#path('actualite/', views.actualite, name='actualite'),
	#path('contact/', views.get_response, name='contact'),
	# path('demandes/', views.demandes, name='demandes'),
	#path("presentation", views.presentation, name="presentation"),

	]

