from celery import shared_task


@shared_task
def fetch_youtube_videos():
    print('Latest videos are fetched every 15 seconds asyncronously...')
    return True
