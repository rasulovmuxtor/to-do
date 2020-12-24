from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('update/<pk>',views.update,name='update'),
    path('delete/<pk>',views.delete,name='delete'),
    path('sign-up/',views.reg,name='sign-up'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logouter,name='logout')
]