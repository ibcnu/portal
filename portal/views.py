from django.shortcuts import render
# from django.http import HttpResponse

# template = 'admin_theme/'
# template = 'sb-admin/'
# template = 'bs-dashboard/'
theme = ''


def index(request):
    context = {
        'title': "Dashboard",
        'header': "Hello, world. You're at the index.",
    }

    return render(request, 'bs-dashboard/index.html', context)


def login(request):
    context = {
        'title': "Login",
        'header': "Hello, world. You're at the login.",
    }

    return render(request, 'login.html', context)


def logout(request):
    context = {
        'title': "Logout",
        'header': "Hello, world. You're at the logout.",
    }

    return render(request, 'logout.html', context)
