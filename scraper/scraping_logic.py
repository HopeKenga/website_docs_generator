import time
import requests
import logging
from bs4 import BeautifulSoup
from celery import shared_task
from fake_useragent import UserAgent
from django.core.cache import cache

logger = logging.getLogger(__name__)
@shared_task(bind=True, max_retries=3)
def scrape_website_task(self, url):
    cache_key = f'website:{url}'
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    user_agent = UserAgent().random  # randomise the user agent string and mimic a regular browser.
    headers = {'User-Agent': user_agent}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        scraped_data = {
            'url': url,
            'title': title,
        }

        cache.set(cache_key, scraped_data, timeout=86400)  # Cache for one day
        return scraped_data

    except requests.RequestException as e:
        logger.error(f'Error scraping {url}: {e}')
        # Simple exponential backoff
        retry_delay = 2 ** self.request.retries
        raise self.retry(exc=e, countdown=retry_delay)
