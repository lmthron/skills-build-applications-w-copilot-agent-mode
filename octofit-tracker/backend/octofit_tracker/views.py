from django.http import JsonResponse

from django.conf import settings

# The API endpoint is accessible at the codespace URL with the suffix '-8000.app.github.dev'.
def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit API!",
        "url": f"https://miniature-eureka-pjxwr5969v539p6q-8000.app.github.dev",
    })
