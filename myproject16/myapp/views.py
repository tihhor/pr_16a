from django.shortcuts import render

# Create your views here.
# render start.html page
def start(request):
    return render(request, "start.html")

# render myapp.html page
def myapp(request):
    return render(request, "myapp.html")
