from django.http import JsonResponse

from django.conf import settings

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit API!",
        "url": f"https://miniature-eureka-pjxwr5969v539p6q{settings.CODESPACE_API_SUFFIX}",
    })
