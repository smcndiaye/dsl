from django.urls import path
from . import views
#from . import bokeh

app_name = 'ateapp'
urlpatterns = [
    path('', views.index, name='index'),
	path('medical/', views.medical, name='medical'),
	path('Globe/', views.Globe, name='Globe'),
	path('data_viz/', views.data_viz, name='data_viz'),
	path('data/', views.data, name='data'),
	path("nlp/", views.nlp, name="nlp"),
	path("resume/", views.resume, name="resume"),

	#path("<single_slug>", views.single_slug, name="single_slug"),
	]






