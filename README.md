# YouTube Video Search

## Project Overview

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Getting Started

### Prerequisites

* Python 3.0
* pip3
* virtualenv
* Git
* PostgreSQL

### Project Setup

1. Clone this repo: `git clone https://github.com/jebinphilipose/youtube-video-search.git && cd youtube-video-search`
2. Create a virtual environment: `virtualenv --python=/usr/bin/python3 ./venv`
3. Activate virtualenv: `source venv/bin/activate`
4. Upgrade pip and install dependencies: `pip install --upgrade pip && pip install -r requirements.txt`
5. Change **DBNAME**, **DBUSER** & **DBPASS** accordingly in `database_setup.sh`
6. Create a `.env` file in project root and set **SECRET_KEY**, **ALLOWED_HOSTS**, **DEBUG**, **DB_NAME**, **DB_USER**, **DB_PASSWORD**, **DB_HOST**, **DB_PORT**, **CELERY_BROKER_URL**, **CELERY_RESULT_BACKEND**, **YOUTUBE_SEARCH_QUERY** & **YOUTUBE_API_KEYS**
7. Setup database and create initial records: `bash database_setup.sh`
8. Run the server: `python manage.py runserver`
9. Open 2nd terminal instance and run: `celery -A youtube_video_search worker -l INFO`
10. Open 3rd terminal instance and run: `celery -A youtube_video_search beat -l INFO`
11. Step 9 and 10 will run the asynchronous periodic celery task to fetch latest YouTube videos
12. Access dashboard at [http://localhost:8000/](http://localhost:8000/)


## API Endpoints

* GET [/api/v1/videos/](http://localhost:8000/api/v1/videos/) --> Returns the stored video data in a paginated response sorted in descending order of published datetime
* To change page, use query param, for eg. [/api/v1/videos/?page=2](http://localhost:8000/api/v1/videos/?page=2)

## Requirements met

* Server calls the YouTube API continuously in background (async) every 15 seconds. Celery is used as the task queue and Redis as the message broker to perform asynchronous tasks.
* A GET API is implemented which returns the stored video data in a paginated response sorted in descending order of published datetime.
* It is scalable and optimised. In production, nginx web server can be used to load balance gunicorn app workers.
* [BONUS] Added support for supplying multiple API keys, it randomly uses a key from the exported API key list. Note: API keys for different Google accounts should be used, because if quota is exceeded on a particular account, all keys for that account will be rate-limited.
* [BONUS] Made a dashboard to view the stored videos with filters and sorting options (optional), visit [http://localhost:8000/](http://localhost:8000/).