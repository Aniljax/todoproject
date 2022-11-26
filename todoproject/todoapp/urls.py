from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('submit',views.submit,name='submit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('list',views.list,name='list'),
    path('complete/<eachtodo_id>',views.completedTasks,name='complete')
    
  



]