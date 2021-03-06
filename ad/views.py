from Libraries import *
# ------------------------- models
from ad.models import Ad, Category, Favourites
from url_names import Names
from user.models import AdditionalUserInfo, Messages
#-------------------------


def add_ad(request):
    return render(request, Names.ad_new)


def main(request):
    page = request.GET.get('page','1')
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 9999999)
    if int(page) > 100:
        return redirect('main')
    category = request.GET.get('category', '')
    search = request.GET.get('search', '')
    list_cat = Category.objects.values('category')
    flag = False

    for ls in list_cat:
        if ls.get('category').upper() == category.upper():
            flag = True
            break

    if not flag or category == '':
        category = "General"
    if search == "" and category != "":
        alls = Ad.objects.select_related('user',
                                         'category').values('id', 'title','description',
                                                               'user__first_name', 'price',
                                                               'category__category', 'img').filter(category__category=category)[:1000]
    else:
        alls = Category.objects.raw('''select t1.id, t1.title, t1.description, t1.price, t1.img,
                                        c.category as category__category,
                                        u.first_name as user__first_name
                                    from (select * from avito.ad as a 
                                            where (a.title like %s 
                                            or a.description like %s) 
                                            and a.price between %s and %s 
                                            limit 1000) as t1
                                    inner join avito.category as c on t1.category_id = c.id
                                    inner join avito.auth_user as u on t1.user_id = u.id
                                    ORDER by t1.id asc ;''', ["%" + search + "%", "%" + search + "%",
                                                              price_from, price_to])

    paginator = Paginator(alls, 10)

    mes_num=""
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        mes = Messages.objects.filter(to_whom_send=user, read_status=False)
        if mes.count() > 0:
            mes_num = mes.count()
        else:
            mes_num = ""

    content = {"data": paginator.get_page(page),
               "category":category,
               "mes": mes_num,
               "search": search,
               "price_from": price_from,
               "price_to": price_to}

    return render(request, Names.main, content)


def show_ad(request, id):
    ad = Ad.objects.get(id=id)
    date = ad.creation_date.date()
    time = ad.creation_date.time()
    title = ad.title
    description = ad.description
    user = User.objects.get(id=ad.user_id)
    ad_name = user.username
    email = user.email
    user_info = AdditionalUserInfo.objects.get(user_id=user.id)
    category = ad.category.category
    price = ad.price
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        mes = Messages.objects.filter(to_whom_send=user, read_status=False)
        if mes.count() > 0:
            mes_num = mes.count()
        else:
            mes_num = ""
    else:
        mes_num=""
    content = {
        "title": title,
        "description": description,
        "ad_name": ad_name,
        "email": email,
        "phone": user_info.phone_mobile,
        "city": user_info.city,
        "metro": user_info.metro,
        "country": user_info.country,
        "id": ad.id,
        "mes": mes_num,
        "category": category,
        "date": date,
        "time": time,
        "price": price,
    }
    return render(request, Names.show_ad , content)


#ajax
def send_msg_seller(request):
    if request.method == "GET":
        message = request.GET.get("message", "")
        if len(message) > 0:
            id_whom = Ad.objects.get(id=request.GET.get("id", "")).user_id
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


#ajax
def make_favourite(request):
    id_ad = request.GET.get('id', '')
    if id_ad != '':
        user = User.objects.get(username=request.user)
        f = Favourites.objects.create(ad_id=id_ad, user=user)
        answer = {"answer": "Объявление было добавлено!"}
        return HttpResponse(json.dumps(answer), content_type="application/json")
    else:
        answer = {"answer": "Объявление не было найдено"}
        return HttpResponse(json.dumps(answer), content_type="application/json")


def test_add(request):
    ad = Ad.objects.filter(id__lt = 1000000)
    y = 0
    for x in ad:
        if y == 5:
            y = 0
        y += 1
        x.category_id = y
        x.save()
    return redirect('main')
    # user = User.objects.get(username=request.user)
    # for x in range(16000000):
    #     Ad.objects.create(user=user, title="tilt",
    #                       description="ezpzlemonsqeezy", price=5000)
    # print(x)
    # ad = Ad.objects.filter(user_id=5).select_related('user')[:100]
    # for a in ad:
    #     print(a.user.username)
    # cat = Category.objects.get(pk=4)
    # for x in range(3001,4000):
    #     ad = Ad.objects.get(id=x)
    #     ad.category = cat
    #     ad.save()
    return redirect('main')


def test_data():
    ad = Ad.objects.all()
    for x in ad:
        x.img="users/avatars/logo-ubuntu.png"
        x.save()
    # gq = ""
    # wp = gq
    # r = redis.StrictRedis(host='localhost', port=6379, db=1)
    # for x in range(1000000):
    #     id = json.loads(r.get("main" + str(x)).decode('utf-8').replace("'", '"')).get('id')
    #
    # print(id)


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



