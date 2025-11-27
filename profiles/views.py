from django.shortcuts import render, get_object_or_404

from .models import UserProfile


# Create your views here.
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    """Display the user profile"""
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
