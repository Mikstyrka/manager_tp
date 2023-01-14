from django.db import models


class Years_averageSalary(models.Model):
    years = models.IntegerField(blank=False)
    average_salary = models.FloatField(blank=False)

    def __str__(self):
        return str(self.years)

class Years_vacancies(models.Model):
    years = models.IntegerField(blank=False)
    all_vacancies = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.years)

class Years_averageSalaryManager(models.Model):
    years = models.IntegerField(blank=False)
    average_salaryManager = models.FloatField(blank=False)

    def __str__(self):
        return str(self.years)

class Years_vacanciesManager(models.Model):
    years = models.IntegerField(blank=False)
    vacancies_manager = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.years)

class key_skill(models.Model):
    position = models.IntegerField(blank=False)
    skill = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.position)