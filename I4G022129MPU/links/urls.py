from django.urls import path
from . import views

app_name = "links"

urlpatterns = [
    path("create/", views.LinkCreateView.as_view(), name="api_create"),
    path("update/<int:pk>", views.LinkUpdateView.as_view(), name="api_update"),
    path("delete/<int:pk>", views.LinkDeleteView.as_view(), name="api_delete"),
    path("", views.LinkListView.as_view(), name="api_list"),
]