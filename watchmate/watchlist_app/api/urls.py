from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path("list", views.WatchListAV.as_view(), name="watchlist"),
    path("<int:pk>", views.WatchListDetailAV.as_view(), name="watchlist-detail"),
    path("stream", views.StreamPlatformAV.as_view(), name="stream-platform"),
    path("stream/<int:pk>", views.StreamPlatformDetailAV.as_view(), name="stream-platform-detail"),
]
