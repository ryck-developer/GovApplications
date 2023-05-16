from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('api/login/', views.LoginAPIView.as_view(), name='login-api'),
    path('api/cookie/', views.HandlerCookie.as_view(), name='cookie-api'),
    path('get-csrf-token/', views.ReturnCookie.as_view(), name='get-csrf-token'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('adspy/', views.AdspyView.as_view(), name='adspy'),
    path('advault/', views.AdvaultView.as_view(), name='advault'),
    path('bigspy/', views.BigspyView.as_view(), name='bigspy'),
    path('adheart-node/', views.AdheartNodeView.as_view(), name='adheart2'),
    path('pipiads/', views.PipiadsView.as_view(), name='pipiads'),
]
