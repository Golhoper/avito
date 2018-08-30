from Libraries import *
from url_names import Names
from ad.models import Ad


def add_ad(request):
    return render(request, Names.ad_new)


#ajax
def add_ad_check(request):
    if request.method == "GET":
        title = request.GET.get("title", "")
        description = request.GET.get("description", "")
        price = request.GET.get("price", "")

        user = User.objects.get(username=request.user)
        try:
            a = Ad.objects.get(user=user)
            a.title = title
            a.description = description
            a.price = price
            a.user = user
            a.save()
        except:
            a = Ad()
            a.title = title
            a.description = description
            a.price = price
            a.user = user
            a.save()

        content = {
            "answer": "saved",
        }
        return HttpResponse(json.dumps(content), content_type="application/json")