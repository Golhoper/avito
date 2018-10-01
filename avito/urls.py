from Libraries import *
from django.conf import settings
from django.conf.urls.static import static
from ad.views import *
import debug_toolbar


urlpatterns = [
    path('', main, name="main"),
    path('user/', include('user.urls')),
    path('ad/', include('ad.urls')),
    path('^__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)