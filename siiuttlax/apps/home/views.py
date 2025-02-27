from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    user = request.user
    try:
        if user.professor:
            type_user = 'professor'
        elif user.student:
            type_user = 'student'
    except:
        type_user = 'other'
    context = {
        "user": user,
        "type_user": type_user
    }
    return render(request, 'home/home.html', context)
