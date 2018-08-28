from Libraries import *
from url_names import Names
from user.functions import get_login, get_email, get_password, empty_log_pasw, error_log_pasw


def reg_user(request):
    return render(request, Names.registration)


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
            return render(request, Names.login)


def log_user(request):
    return render(request, Names.login)


def log_check(request):
    if request.method == "GET":
        login = request.GET.get("login", '')
        password = request.GET.get("password", '')

        if login != '' and password != '':
            user = authenticate(username=login, password=password)

            if user is not None:
                group = User.objects.get(username=login).groups.get()
                if user.is_active == 1 and str(group) == "user":
                    login(request, user)
                    return render(request, Names.main)
            else:
                content = error_log_pasw()
                return HttpResponse(json.dumps(content), content_type="application/json")
        else:
            print(1)
            content = empty_log_pasw(login, password)
            return HttpResponse(json.dumps(content), content_type="application/json")