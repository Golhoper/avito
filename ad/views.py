from Libraries import *
from url_names import Names
from django.views.decorators.cache import cache_page
from django.core.cache import *
import time, redis
from django.core.cache import caches
#------------------------- models
from ad.models import Ad
from user.models import AdditionalUserInfo, Messages
#-------------------------


def add_ad(request):
    return render(request, Names.ad_new)


def main(request):
    num = 10
    all = Ad.objects.all()[:num]

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        mes = Messages.objects.filter(to_whom_send=user, read_status=False)
        if mes.count() > 0:
            mes_num = mes.count()
        else:
            mes_num = ""
    content = {"data": all, "mes": mes_num}
    return render(request, Names.main, content)


def show_ad(request, id):
    ad = Ad.objects.get(id=id)
    title = ad.title
    description = ad.description
    user = User.objects.get(id=ad.user_id)
    ad_name = user.username
    email = user.email
    user_info = AdditionalUserInfo.objects.get(user_id=user.id)
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        mes = Messages.objects.filter(to_whom_send=user, read_status=False)
        if mes.count() > 0:
            mes_num = mes.count()
        else:
            mes_num = ""
    content = {
        "title": title,
        "description": description,
        "ad_name": ad_name,
        "email": email,
        "phone": user_info.phone_mobile,
        "city": user_info.city,
        "metro": user_info.metro,
        "country": user_info.country,
        "id": user.id,
        "mes": mes_num,
    }
    return render(request, Names.show_ad , content)


#ajax
def send_msg_seller(request):
    if request.method == "GET":
        message = request.GET.get("message", "")
        if len(message) > 0:
            id_whom = request.GET.get("id", "")
            id_who = User.objects.get(username=request.user).id

            m = Messages.objects.create(message=message, who_send=User.objects.get(id=id_who),
                                        to_whom_send=User.objects.get(id=id_whom), read_status=False)

            content = {"answer": "Message sent!"}
            return HttpResponse(json.dumps(content), content_type="application/json")

    content = {"answer": "stop"}
    return HttpResponse(json.dumps(content), content_type="application/json")


#ajax
def add_ad_check(request):
    if request.method == "GET":
        title = request.GET.get("title", "")
        description = request.GET.get("description", "")
        price = request.GET.get("price", "")
        user = User.objects.get(username=request.user)

        a = Ad()
        a.title = title
        a.description = description
        a.price = price
        a.user = user
        a.save()

        content = {"answer": "saved"}
        return HttpResponse(json.dumps(content), content_type="application/json")
    else:
        content = {"answer": "something goes wrong"}
        return HttpResponse(json.dumps(content), content_type="application/json")



def test_add(request):
    # user = User.objects.get(username=request.user)
    # for x in range(100000):
    #     Ad.objects.create(user=user, title="title",
    #                       description="description", price=1000)

    return redirect('main')


def test_data():
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    for x in range(100000):
        id = json.loads(r.get("main" + str(x)).decode('utf-8').replace("'", '"')).get('id')
        if id == 90000:
            break
    print(id)


'''
tests

def get_data_redis():
    num = 100000

    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    # time1 = time.time()
    # r.delete('test3')
    # if r.get('test3') is None:
    #     # print("inside if")
    #     alls = Ad.objects.all()[:num].values('id', 'title', 'description')
    #     y=0
    #     for x in alls:
    #         r.set("main"+str(y),x)
    #         y+=1
    # for x in range(40):
    #     print(r.get("main"+str(x)))
    print(r.get("main90000"))
        # r.set('test3', alls)
    # b = r.get('test3').decode('utf-8').replace("'", '"')
    # b_s = b[10:len(b)-1]
    # print(b_s)
    # data = json.loads(b_s)

    # print(r.get('test3'))
    # s = json.dumps(data, indent=4, sort_keys=True)
    # time2 = time.time()
    # s = json.dumps(data)
    # print("time redis: " + str(time2 - time1))
    # return data
    # r.flushall()
    
    
def get_data(num):
    # all = Ad.objects.all()[:num]
    a = cache.get('lst')
    if a is None:
        alls = Ad.objects.all()[:num].values('id', 'title', 'description')
        cache.set("lst", alls, 60)
        # if cache.get("lst"):
            # print("memcached created")
    else:
        alls = a
        # print("from memcached")
    # if a:
    #     for x in a:
    #         print(x.get("id"))

    return alls
'''



