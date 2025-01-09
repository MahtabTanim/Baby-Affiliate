from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product_list/", views.product_list, name="product_list"),
    path("products/<int:id>/", views.products, name="product_detail"),
]
