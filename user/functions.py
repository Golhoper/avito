from Libraries import *


def get_login(login):
    try:
        usr = User.objects.get(username=login)
        if usr:
            login_ans = "busy"
    except:
        if login == "":
            login_ans = "error"
        else:
            login_ans = "free"
    return login_ans


def get_email(email):
    try:
        user = User.objects.get(email=email)
        if user:
            email_ans = "incorrect"
    except:
        email_ans = "correct"

    return email_ans


def get_password(password, password_r):
    if password != password_r or (password == '' or password_r == ''):
        password_ans = "not equal"
    else:
        password_ans = "equal"
    return password_ans


def empty_log_pasw(login, password):
    if login != '':
        login_ans = "filled"
    else:
        login_ans = "empty"

    if password != '':
        password_ans = "filled"
    else:
        password_ans = "empty"

    content = {
        "login": login_ans,
        "password": password_ans,
    }

    return content


def error_log_pasw():
    content = {
        "login": "unknown",
        "password": "unknown",
    }
    return content