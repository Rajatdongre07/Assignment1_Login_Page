from django.shortcuts import render


def showIndex(request):
    return render (request, "loginpage.html")

def showLogin(request):
    Username = request.POST.get("t1")
    Password = request.POST.get("t2")

    if Username == "Rajat" and Password == "django":
        return render(request,"Welcome.html")
    else:
        return render(request,"error.html")
