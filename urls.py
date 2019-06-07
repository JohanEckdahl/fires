from django.urls import path
from . import views
from . import tables
app_name = 'fires'

urlpatterns = [path('skogsstyrelsen/', views.skogsstyrelsen, name='fires'),
		       path('fires/', views.fires, name='fires'),
		       path('', views.fires, name='index'),
	          ]
