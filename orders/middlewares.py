from datetime import timezone

import pytz
from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django_timezone')
        zones = pytz.all_timezones
        if tzname in zones:
            tz = pytz.timezone(tzname)
            timezone.activate(tz)
            timezone.localtime(timezone.now())
        else:
            timezone.deactivate()
        return self.get_response(request)

