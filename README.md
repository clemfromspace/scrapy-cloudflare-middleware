[![PyPI](https://img.shields.io/pypi/v/scrapy_cloudflare_middleware.svg)](https://pypi.python.org/pypi/scrapy_cloudflare_middleware)

## Scrapy "CloudFlare" middleware

A Scrapy middleware to bypass the CloudFlare's anti-bot protection, based on [cloudflare-scrape](https://github.com/Anorov/cloudflare-scrape).

### Installation
```
pip install scrapy_cloudflare_middleware
```

### Usage

Add the middleware to your `DOWNLOADER_MIDDLEWARES` settings

```python
DOWNLOADER_MIDDLEWARES = {
    # The priority of 560 is important, because we want this middleware to kick in just before the scrapy built-in `RetryMiddleware`.
    'scrapy_cloudflare_middleware.middlewares.CloudFlareMiddleware': 560
}
```

Done.
Happy scraping !






