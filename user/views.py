from Libraries import *
from url_names import Names
from user.functions import get_login, get_email, get_password


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
            print("here")
            pass

    else:
        return HttpResponse("None", content_type="text/html")