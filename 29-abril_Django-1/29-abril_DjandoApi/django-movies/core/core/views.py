from django.http import JsonResponse
from datetime import datetime


def get_datetime(request):
    now = datetime.now()

    html = f"<html><body> <h1>Son las {now} </h1></body></html>"
    # return HttpResponse(html)

    response = {"datetime": now}
    return JsonResponse(response)
