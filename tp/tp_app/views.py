from django.shortcuts import render
from tp_app.models import Years_averageSalary, Years_averageSalaryManager, Years_vacancies, Years_vacanciesManager, \
    level_salary, vacancies_city, skill_2015, skill_2016, skill_2017, skill_2018, skill_2019, skill_2020, skill_2021, \
    skill_2022


def index(request):
    return render(request, 'index.html')

def page1(request):
    averageSalary = Years_averageSalary.objects.all()
    averageSalaryManager = Years_averageSalaryManager.objects.all()
    vacancies = Years_vacancies.objects.all()
    managerVacancies = Years_vacanciesManager.objects.all()
    return render(request, 'page1.html', {'averageSalary': averageSalary, 'averageSalaryManager': averageSalaryManager, 'vacancies': vacancies, 'managerVacancies': managerVacancies})

def page2(request):
    level = level_salary.objects.all()
    vac = vacancies_city.objects.all()
    return render(request, 'page2.html', {'level': level, 'vac': vac})

def page3(request):
    s2015 = skill_2015.objects.all()
    s2016 = skill_2016.objects.all()
    s2017 = skill_2017.objects.all()
    s2018 = skill_2018.objects.all()
    s2019 = skill_2019.objects.all()
    s2020 = skill_2020.objects.all()
    s2021 = skill_2021.objects.all()
    s2022 = skill_2022.objects.all()
    return render(request, 'page3.html',{'s15': s2015, 's16': s2016, 's17': s2017, 's18': s2018, 's19': s2019, 's20': s2020, 's21': s2021, 's22': s2022})

def page4(request):
    return render(request, 'page4.html')