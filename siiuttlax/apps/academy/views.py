from django.shortcuts import render, redirect
from .forms import ProfessorForm, StudentForm
from .models import Professor, Student

def create_prof(request):
    if request.method == 'POST':
        form=ProfessorForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            first_name=form.cleaned_data['first_name']
            password=form.cleaned_data['password']
            category=form.cleaned_data['category']
            employee_number=form.cleaned_data['employee_number']

            Professor.objects.create_user(
                username=username,
                first_name=first_name,
                password=password,
                category=category,
                employee_number=employee_number
            )
            return redirect('academy:professors_create')

    form=ProfessorForm()
    return render(request,
                'academy/create_professor.html',
                {'form':form})
def create_student(request):
    form=StudentForm()
    return render(request,
                'academy/create_student.html',
                {'form':form})

