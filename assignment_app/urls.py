from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('number/<int:number>',views.show),
    path('edit/<int:number>', views.edit),
    path('delete/<int:number>',views.destroy),
    #path('delete',views.destroy),

]
