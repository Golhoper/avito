from Libraries import *
from user.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('registration/', reg_user, name="registration"),
    re_path('registration_check/$', reg_check, name="reg_check"),

    path('login/', log_user, name="login"),
    re_path('login_check/$', log_check, name="log_check"),

    path('logout/', logout_user, name="logout"),

    path('profile/', profile_user, name="profile"),
    re_path('profile_check/$', profile_user_check, name="profile_check"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
