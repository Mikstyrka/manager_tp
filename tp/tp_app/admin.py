from django.contrib import admin
from tp_app.models import Years_vacancies, Years_averageSalaryManager, Years_vacanciesManager, Years_averageSalary, \
    key_skill

admin.site.register(Years_averageSalary)
admin.site.register(Years_vacancies)
admin.site.register(Years_averageSalaryManager)
admin.site.register(Years_vacanciesManager)
admin.site.register(key_skill)