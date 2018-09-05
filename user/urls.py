from Libraries import *
from user.views import *


urlpatterns = [
    path('registration/', reg_user, name="registration"),
    re_path('registration_check/$', reg_check, name="reg_check"), #ajax

    path('login/', log_user, name="login"),
    re_path('login_check/$', log_check, name="log_check"), #ajax

    path('logout/', logout_user, name="logout"),

    path('profile/', profile_user, name="profile"),
    re_path('profile_check/$', profile_user_check, name="profile_check"), #ajax
    re_path('profile_delete/$', profile_user_delete, name="profile_delete"), #ajax
    re_path('make_read/(?P<id>\w+)/$', make_read, name="make_read")
]

