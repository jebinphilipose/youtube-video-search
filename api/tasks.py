import random
import requests
from celery import shared_task
from datetime import datetime
from dateutil.relativedelta import relativedelta
from decouple import config, Csv
from requests.exceptions import HTTPError


@shared_task
def fetch_youtube_videos():
    current_time = datetime.now()
    # Fetch latest videos published in the past one day
    published_after = current_time + relativedelta(days=-1)
    # Convert to RFC 3339
    published_after = published_after.replace(microsecond=0).isoformat("T") + "Z"
    # Support multiple API keys and pick any random one for each request
    api_key = random.choice(config('YOUTUBE_API_KEYS', cast=Csv()))
    api_endpoint = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': config('YOUTUBE_SEARCH_QUERY'),
        'key': api_key,
        'type': 'video',
        'order': 'date',
        'publishedAfter': published_after,
        'maxResults': 50,
    }

    try:
        response = requests.get(api_endpoint, params=params)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()

        data = response.json()

        print(data)

        for item in data['items']:
            pass

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return False
    except Exception as err:
        print(f'Other error occurred: {err}')
        return False
    else:
        return True
