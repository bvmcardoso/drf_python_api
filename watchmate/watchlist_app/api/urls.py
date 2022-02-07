from watchlist_app.api import views
from django.urls import path

urlpatterns = [
    path("list", views.WatchListAV.as_view(), name="watchlist"),
    path("<int:pk>", views.WatchListDetailAV.as_view(), name="watchlist-detail"),
]
