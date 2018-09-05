from Libraries import *
from ad.views import *


urlpatterns = [
    path('add_new/', add_ad, name="add_ad"),
    re_path('add_new_check/$', add_ad_check, name="add_ad_check"), #ajax
    path('test/', test_add, name="test"),
    re_path('^(?P<id>\w+)/$', show_ad, name="show_ad"),
    re_path('send_msg_seller/$', send_msg_seller, name="send_msg_seller"),

]