from Libraries import *
from django.conf import settings
from django.conf.urls.static import static
from ad.views import *


urlpatterns = [
    path('', main, name="main"),
    path('user/', include('user.urls')),
    path('ad/', include('ad.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
