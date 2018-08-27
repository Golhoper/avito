from Libraries import *
from url_names import Names


def reg_user(request):
    if request.method == "POST":
        data = request.POST
        login = request.POST["login"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password = request.POST["password"]
        password_r = request.POST["password_r"]
        email = request.POST["email"]

        try:
            usr = User.objects.get(username=login)
            if usr:
                login_ans = "busy"
        except:
            login_ans = "free"

        content = {
            "login_ans": login_ans,

        }

    return render(request, Names.registration, content)