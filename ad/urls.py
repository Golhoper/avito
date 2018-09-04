from Libraries import *
from ad.views import *


urlpatterns = [
    path('add_new/', add_ad, name="add_ad"),
    re_path('add_new_check/$', add_ad_check, name="add_ad_check"), #ajax
    path('test/', test_add, name="test"),
]