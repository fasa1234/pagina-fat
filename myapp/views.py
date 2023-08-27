from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("index page")
def hello(request, username):
    print(username)
    return HttpResponse("<h2>hello %s</h2>" %username)

def about(request):
    return HttpResponse('about')
