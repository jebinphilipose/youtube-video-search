from django.shortcuts import render
from api.models import Video


# Create your views here.
def index(request):
    if request.method == 'GET':
        videos = Video.objects.filter(search_query='music').order_by('-published_at')
        return render(request, 'youtube_video_search/dashboard.html',
                      {'videos': videos,
                       'sort': 'desc',
                       'query': 'music'})

    else:
        query = request.POST['query']
        sort = request.POST['sort']
        videos = Video.objects.filter(search_query=query)
        if sort == 'asc':
            videos = videos.order_by('published_at')
        elif sort == 'desc':
            videos = videos.order_by('-published_at')

        return render(request, 'youtube_video_search/dashboard.html',
                      {'videos': videos,
                       'sort': sort,
                       'query': query})
