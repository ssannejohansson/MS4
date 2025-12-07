from django.shortcuts import render


# Create your views here.
def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


""" Custom error handlers """


def custom_404_view(request, exception):
    return render(request, "errors/404.html", status=404)


def custom_500_view(request):
    return render(request, "errors/500.html", status=500)


def custom_403_view(request, exception):
    return render(request, "errors/403.html", status=403)


def custom_405_view(request, exception):
    return render(request, "errors/405.html", status=405)
