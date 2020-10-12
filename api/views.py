from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer

# Create your views here.


class VideoListView(generics.ListAPIView):
    """
    GET api/v1/videos/
    """
    queryset = Video.objects.all().order_by('-published_at')
    serializer_class = VideoSerializer
