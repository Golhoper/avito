from Libraries import *
from url_names import Names
from user.functions import *
from user.models import AdditionalUserInfo, Messages
from .forms import ProfileForm
from ad.models import Favourites


def reg_user(request):
    return render(request, Names.registration)

#ajax
def reg_check(request):
    if request.method == "GET":
        login = request.GET.get("login", '')
        first_name = request.GET.get("first_name", '')
        last_name = request.GET.get("last_name", '')
        password = request.GET.get("password", '')
        password_r = request.GET.get("password_r", '')
        email = request.GET.get("email", 'None')

        login_ans = get_login(login)
        email_ans = get_email(email)
        password_ans = get_password(password, password_r)

        if login_ans != "free" or email_ans == "incorrect" or password_ans == "not equal":
            content = {
                "login": login_ans,
                "email": email_ans,
                "password": password_ans,
            }

            return HttpResponse(json.dumps(content), content_type="application/json")
        else:
            User.objects.create_user(username=login, email=email, password=password,
                                     first_name=first_name, last_name=last_name,
                                     is_active=1, is_superuser=0, is_staff=0)
            group = Group.objects.get(name='user')
            User.objects.get(username=login).groups.add(group)
            content = {
                "login": "back to login"
            }
            print(content)
            return HttpResponse(json.dumps(content), content_type="application/json")


def log_user(request):
    return render(request, Names.login)


#ajax
def log_check(request):
    if request.method == "GET":
        login_c = request.GET.get("login", '')
        password = request.GET.get("password", '')

        if login != '' and password != '':
            user = authenticate(username=login_c, password=password)

            if user is not None:
                group = User.objects.get(username=login_c).groups.get()
                if user.is_active == 1 and str(group) == "user":
                    login(request, user)
                    content = {"login": "go to profile"}
                    return HttpResponse(json.dumps(content), content_type="application/json")
            else:
                content = error_log_pasw()
                return HttpResponse(json.dumps(content), content_type="application/json")
        else:
            content = empty_log_pasw(login, password)
            return HttpResponse(json.dumps(content), content_type="application/json")


def logout_user(request):
    logout(request)
    return redirect('login')


def profile_user(request):
    if request.method == "POST":
        MyProfileForm = ProfileForm(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            user = User.objects.get(username=request.user)
            try:
                profile = AdditionalUserInfo.objects.get(user=user)
                profile.avatar = MyProfileForm.cleaned_data["picture"]
                profile.save()
            except:
                profile = AdditionalUserInfo.objects.create(user=user,
                                                            avatar=MyProfileForm.cleaned_data["picture"])
            content = {
                "answer": "Изображение сохранено"
            }
            return render(request, Names.profile_user)
    else:
        user = User.objects.get(username=request.user)
        try:
            ad = AdditionalUserInfo.objects.get(user=user)
            mes = Messages.objects.filter(to_whom_send=user, read_status=False)
            if mes.count() > 0:
                mes_num = mes.count()
                mes_list = mes
            else:
                mes_num = 0
                mes_list = ""

            if ad.birthday == None:
                birth = ""
            else:
                birth = ad.birthday
            content = {
                "birthday": birth,
                "country": ad.country,
                "city": ad.city,
                "street": ad.street,
                "house_number": ad.house_number,
                "house_block": ad.house_block,
                "avatar": ad.avatar,
                "mes": mes_num,
                "mes_list": mes_list,
            }

            return render(request, Names.profile_user, content)
        except:
            content = {}
            return render(request, Names.profile_user, content)


#ajax
def profile_user_check(request):
    if request.method == "GET":

        birthday = request.GET.get("birthday", "")
        country = request.GET.get("country", "")
        city = request.GET.get("city", "")
        street = request.GET.get("street", "")
        house_number = request.GET.get("house_number", "")
        house_block = request.GET.get("house_block", "")

        birthday_ans = profile_birthday(birthday)
        country_ans = profile_country(country)
        city_ans = profile_city(city)
        street_ans = profile_street(street)
        house_number_ans = profile_house_number(house_number)
        house_block_ans = profile_house_block(house_block)

        user = User.objects.get(username=request.user)
        try:
            info = AdditionalUserInfo.objects.get(user=user)
            if birthday_ans:
                info.birthday = birthday
            if country_ans:
                info.country = country
            if city_ans:
                info.city = city
            if street_ans:
                info.street = street
            if house_number_ans:
                info.house_number = house_number
            if house_block_ans:
                info.house_block = house_block
            info.save()
            answer = "Данные были изменены!"
        except:
            a = AdditionalUserInfo.objects.create(user=user, country=country, city=city,
                                              street=street, house_number=house_number, house_block=house_block)
            if birthday_ans:
                a.birthday = birthday
                a.save()
            answer = "Данные сохранены"

        content = {
            "answer": answer,
        }
        return HttpResponse(json.dumps(content), content_type="application/json")

    content = {
        "answer": "Изменений не было"
    }
    return HttpResponse(json.dumps(content), content_type="application/json")


#ajax
def profile_user_delete(request):
    user = User.objects.get(username=request.user)
    AdditionalUserInfo.objects.get(user=user).delete()
    content = {
        "answer": "deleted",
    }
    return HttpResponse(json.dumps(content), content_type="application/json")


def make_read(request, id):
    content = {
        "answer": 56,
    }
    return HttpResponse(json.dumps(content), content_type="application/json")


def show_favourites(request):
    user = User.objects.get(username=request.user)
    favs = Favourites.objects.select_related('user', 'ad')\
        .filter(user=user).values('ad__title', 'ad__description', 'ad__id')
    return render(request, Names.favourites, {"favs": favs})


def delete_fav(request):
    id = request.GET.get('id', '')
    print(id)
    user = User.objects.get(username=request.user)
    Favourites.objects.get(ad_id=id, user=user).delete()
    answer = {
        "answer": "Запись была удалена",
    }
    return HttpResponse(json.dumps(answer), content_type="application/json")

