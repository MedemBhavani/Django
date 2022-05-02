from django.urls import path
from . import views

urlpatterns=[
    #path('',views.register,name='Register'),
    path('',views.login,name="login"),
    path('logout',views.logout,name="logout"),
]