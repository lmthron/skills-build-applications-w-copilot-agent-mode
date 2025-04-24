from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit API!",
        "url": "https://miniature-eureka-pjxwr5969v539p6q.8000.app.github.dev",
    })
