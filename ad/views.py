from Libraries import *
from url_names import Names
from ad.models import Ad
from django.views.decorators.cache import cache_page
from django.core.cache import *
from functools import lru_cache
import time, redis
from django.core.cache import caches


def add_ad(request):
    return render(request, Names.ad_new)


def main(request):
    # get_data_redis()
    # test_data()
    num = 10
    # time1 = time.time()
    all = get_data(num)
    # time2 = time.time()
    # print(time2-time1)
    # paginator = Paginator(all, 50)

    # page = request.GET.get("page", 2)
    # info = paginator.get_page(page)
    content = {"data": all}
    return render(request, Names.main, content)


def test_data():
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    for x in range(100000):
        id = json.loads(r.get("main" + str(x)).decode('utf-8').replace("'", '"')).get('id')
        if id == 90000:
            break
    print(id)

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
