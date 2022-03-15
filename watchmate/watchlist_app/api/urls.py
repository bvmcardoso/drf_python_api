from django.urls import include, path
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views

router = DefaultRouter()
router.register("stream", views.StreamPlatformVS, basename="streamplatform")


urlpatterns = [
    path("list", views.WatchListAV.as_view(), name="watchlist"),
    path("<int:pk>", views.WatchListDetailAV.as_view(), name="watchlist-detail"),
    path("", include(router.urls)),
    # path("stream", views.StreamPlatformAV.as_view(), name="streamplatform"),
    # path("stream/<int:pk>", views.StreamPlatformDetailAV.as_view(), name="streamplatform-detail"),
    # path("review", views.ReviewList.as_view(), name="review-list"),
    # path("review/<int:pk>", views.ReviewDetail.as_view(), name="review-detail"),
    # path("stream/<int:pk>/review", views.ReviewList.as_view(), name="review-list"),
    # path("stream/review/<int:pk>", views.ReviewDetail.as_view(), name="review-detail"),
    # path("stream/<int:pk>/review-create", views.ReviewCreate.as_view(), name="review-create"),
]
