from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("authors/<int:author_id>/", views.author_details, name="author_detail"),
    path("categories/<str:category_name>/", views.display_categories, name="category_name"),
]