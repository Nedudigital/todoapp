from django.urls import path
from .views import list_view, detail_view, update_view, create_view

urlpatterns = [
    path('',list_view, name="list"),
    path('create/',create_view, name="create"),
    path('detail/', detail_view, name="detail"),
    path('update/', update_view, name="update"),
]