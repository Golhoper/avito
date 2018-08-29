from Libraries import *


#--------------------------------- For login and register path


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


#--------------------------------- End login register path
#--------------------------------- For profile path


def profile_birthday(birthday):
    try:
        year, month, day = birthday.split('.')
        datetime.datetime(int(year), int(month), int(day))
        birthday_ans = True
    except:
        birthday_ans = False
    return birthday_ans


def profile_country(country):
    if len(country) > 0:
        country_ans = True
    else:
        country_ans = False
    return country_ans


def profile_city(city):
    if len(city) > 0:
        city_ans = True
    else:
        city_ans = False
    return city_ans


def profile_street(street):
    if len(street) > 0:
        street_ans = True
    else:
        street_ans = False
    return street_ans


def profile_house_number(house_number):
    if str(house_number).isdigit():
        house_number_ans = True
    else:
        house_number_ans = False
    return house_number_ans


def profile_house_block(house_block):
    if str(house_block).isdigit():
        house_block_ans = True
    else:
        house_block_ans = False
    return house_block_ans

#--------------------------------- End profile path

