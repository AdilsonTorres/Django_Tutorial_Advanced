from django .http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Yoou're ate the polls index.")
