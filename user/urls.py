from Libraries import *
from user.views import *

urlpatterns = [
    path('registration/', reg_user, name="registration"),
]
