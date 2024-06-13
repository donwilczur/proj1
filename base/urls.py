from django.urls import path, include
from .views import authView, home, logout_view
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path("", home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls"),name="login"),
    path("update_item/", views.updateItem, name="update_item"),
    path("future/", views.future, name="future"),
]