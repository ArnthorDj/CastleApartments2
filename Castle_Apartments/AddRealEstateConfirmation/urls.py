
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="add_real_estate_confirmation_index"),
]