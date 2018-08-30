from Libraries import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('user/', include('user.urls')),
    path('ad/', include('ad.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
