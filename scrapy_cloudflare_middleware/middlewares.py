"""This module contains the ``CloudFlareMiddleware``"""

from cfscrape import get_tokens

import logging


class CloudFlareMiddleware:
    """Scrapy middleware to bypass the CloudFlare's anti-bot protection"""

    @staticmethod
    def is_cloudflare_challenge(response):
        """Test if the given response contains the cloudflare's anti-bot protection"""

        return (
            response.status == 503
            and response.headers.get('Server', '').startswith(b'cloudflare')
            and 'jschl_vc' in response.text
            and 'jschl_answer' in response.text
        )

    def process_response(self, request, response, spider):
        """Handle the a Scrapy response"""

        if not self.is_cloudflare_challenge(response):
            return response

        logger = logging.getLogger('cloudflaremiddleware')

        logger.debug(
            'Cloudflare protection detected on %s, trying to bypass...',
            response.url
        )

        cloudflare_tokens, __ = get_tokens(
            request.url,
            user_agent=spider.settings.get('USER_AGENT')
        )

        logger.debug(
            'Successfully bypassed the protection for %s, re-scheduling the request',
            response.url
        )

        request.cookies.update(cloudflare_tokens)
        request.priority = 99999

        return request
