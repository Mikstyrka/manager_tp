from django.shortcuts import render
from tp_app.models import Years_averageSalary, Years_averageSalaryManager, Years_vacancies, Years_vacanciesManager


def index(request):
    return render(request, 'index.html')

def page1(request):
    averageSalary = Years_averageSalary.objects.all()
    averageSalaryManager = Years_averageSalaryManager.objects.all()
    vacancies = Years_vacancies.objects.all()
    managerVacancies = Years_vacanciesManager.objects.all()
    return render(request, 'page1.html', {'averageSalary': averageSalary, 'averageSalaryManager': averageSalaryManager, 'vacancies': vacancies, 'managerVacancies': managerVacancies})

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')

def page4(request):
    return render(request, 'page4.html')