from Libraries import *
from user.views import *

urlpatterns = [
    path('registration/', reg_user, name="registration"),
    re_path('registration_check/$', reg_check, name="reg_check")
]
