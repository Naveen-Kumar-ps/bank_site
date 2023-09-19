from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('new',views.new,name='new'),
    path('logout',views.logout,name='logout'),
    path('newpage',views.newpage,name='newpage'),
    path('message/',views.msg,name='msg'),


]
