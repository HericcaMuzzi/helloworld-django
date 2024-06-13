from django.http import HttpResponse

def home(request):
    return HttpResponse("Hericca Muzzi - Cloud Computing & Site Reliability Engineering")
