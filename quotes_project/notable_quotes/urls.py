from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("quotes/", views.all_quotes, name="all_quotes"),
    path("authors/<int:author_id>/", views.author_details, name="author_detail"),
    path("category/<str:category_name>/", views.display_categories, name="category_name"),
]