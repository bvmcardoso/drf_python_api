from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.api.serializers import (ReviewSerializer,
                                           StreamPlatformSerializer,
                                           WatchListSerializer)
from watchlist_app.models import Review, StreamPlatform, WatchList

# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True, context={"request": request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         platform = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(platform, context={"request": request})
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, pk):
#         stream_platform = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(stream_platform, data=request.data)
#         if serializer.is_valid():
#             serializer.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response(serializer.errors)        
            
class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
        
        
class StreamPlatformAV(APIView):
    def get(self, request):
        stream_platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream_platforms, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(stream_platform, context={"request": request})
            return Response(serializer.data)
        except StreamPlatform.DoesNotExist:
            return Response(
                {"error": "Stream platform does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors)


class WatchListAV(APIView):
    def get(self, request):
        watch_list = WatchList.objects.all()
        serializer = WatchListSerializer(watch_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class WatchListDetailAV(APIView):
    def get(self, request, pk):
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {"error": "Watchlist does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = WatchListSerializer(watch_list)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        watch_list = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watch_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors)


class ReviewList(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        movie = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=movie)


# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewDetail(
#     mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
# ):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
