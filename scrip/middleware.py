from django.conf import settings
from django.contrib import auth
from django.utils import timezone
from datetime import timedelta

class AutoLogout:
    def process_request(self, request):
        if not request.user.is_authenticated():
            # not logged in
            return
        
        try:
            if timezone.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            pass

        request.session['last_touch'] = timezone.now()


