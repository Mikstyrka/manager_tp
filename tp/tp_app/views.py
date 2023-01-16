import json
import re

import requests
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
    name = []
    description = []
    skills = []
    company = []
    salary = []
    region = []
    date = []
    k = 0
    params = {
        'text': 'NAME:Менеджер IT'
    }
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    data_sort = json.loads(data)
    req.close()
    for i in data_sort["items"]:
        if k != 10:
            skill = []
            requ = requests.get('https://api.hh.ru/vacancies/' + i['id']).content.decode()
            requ_sort = json.loads(requ)
            name.append(requ_sort['name'])
            description.append(re.sub(r"<[^>]+>", "", requ_sort['description'], flags=re.S))
            for j in requ_sort['key_skills']:
                skill.append(j['name'])
            skills.append(skill)
            company.append(requ_sort['employer']['name'])
            if requ_sort['salary'] == None:
                salary.append('Не указан')
            else:
                if requ_sort['salary']['from'] == None:
                    if requ_sort['salary']['currency'] != None:
                        salary.append('до ' + str(requ_sort['salary']['to']) + ' ' + str(requ_sort['salary']['currency']))
                    else:
                        salary.append('до ' + str(requ_sort['salary']['to']))
                elif requ_sort['salary']['to'] == None:
                    if requ_sort['salary']['currency'] != None:
                        salary.append('от ' + str(requ_sort['salary']['from']) + ' ' + str(requ_sort['salary']['currency']))
                    else:
                        salary.append('от ' + str(requ_sort['salary']['from']))
                else:
                    if requ_sort['salary']['currency'] != None:
                        salary.append(str(requ_sort['salary']['from']) + ' - ' + str(requ_sort['salary']['to']) + ' ' + str(requ_sort['salary']['currency']))
                    else:
                        salary.append(str(requ_sort['salary']['from']) + ' - ' + str(requ_sort['salary']['to']))
            region.append(requ_sort['area']['name'])
            date.append(requ_sort['published_at'])
            k += 1
        else:
            pass
    return render(request, 'page4.html', {'name': name, 'description': description, 'skills': skills, 'company': company, 'salary': salary, 'region': region, 'date': date})