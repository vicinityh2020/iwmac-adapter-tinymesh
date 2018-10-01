import sys

import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Sensor

# Create your views here.
@csrf_exempt
def test_event(request):
    # ip = "192.168.1.200:81"
    ip = "POSTMAN_API"
    test_url = f'http://{ip}/services/iwmac_plant/parameter_values.php'

    sensors = Sensor.objects.all()

    # TODO: populate params with elements

    post_data = {
        "jsonrpc": "2.0",
        "method": "read",
        "params": {
            "parameters": [
                {
                    "unit": "BAC01",
                    "element": "rt40_setpunkt_natt_tilluft_2_95"
                },
                {
                    "unit": "BAC01",
                    "element": "rt40_setpunkt_natt_tilluft_2_95"
                },
                {
                    "unit": "BAC01",
                    "element": "rt40_setpunkt_natt_tilluft_2_95"
                }
            ],
            "id": "0000",
            "token": "eyJ0d3bsdU"
        },
        "id": 1
    }

    try:
        resp = requests.post(url=test_url, json=post_data)
    except requests.exceptions.ConnectionError as ce:
        print(ce.strerror, file=sys.stderr)
        return JsonResponse(data={"error": True}, status=500)

    if resp.status_code != requests.status_codes.codes.OK:
        return JsonResponse(data={"error": True}, status=requests.status_codes.codes.NOT_FOUND)

    # TODO: use filter(id__in(ARRAY_OF_IDS_CHANGED))

    # TODO: for all retrieved: check if timestamp > timestamp.old
    # TODO: if yes:
    # TODO: 1. store new value & timestamp.
    # TODO: 2. add to event array object

    # TODO: Publish events

    return JsonResponse(data=resp.text, status=requests.status_codes.codes.OK)


@csrf_exempt
def thing_descriptor(request):
    return JsonResponse(data=settings.THING_DESCRIPTION, status=requests.status_codes.codes.OK)
