from django.contrib import admin
from django.urls import path
from natureapp import views
# from .views import index,login,logout,cards,posts


urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', views.adminn, name="adminn"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/<int:verify>/', views.signup, name='signup'),
    path('delete_record/<int:user_id>/', views.delete_record, name='delete'),
    path('update_record/<int:user_id>/', views.update_record, name='update'),
]


