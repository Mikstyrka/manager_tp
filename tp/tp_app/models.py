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


class skill_2015(models.Model):
    position = models.IntegerField(blank=False)
    skill = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.position)

class skill_2016(models.Model):
    position = models.IntegerField(blank=False)
    skill = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.position)

class skill_2017(models.Model):
    position = models.IntegerField(blank=False)
    skill = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.position)

class skill_2018(models.Model):
    position = models.IntegerField(blank=False)
    skill = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.position)

class skill_2019(models.Model):
    position = models.IntegerField(blank=False)
    skill = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.position)

class skill_2020(models.Model):
    position = models.IntegerField(blank=False)
    skill = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.position)

class skill_2021(models.Model):
    position = models.IntegerField(blank=False)
    skill = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.position)

class skill_2022(models.Model):
    position = models.IntegerField(blank=False)
    skill = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.position)

class level_salary(models.Model):
    city = models.CharField(max_length=50, blank=False)
    salary = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.city)

class vacancies_city(models.Model):
    city = models.CharField(max_length=50, blank=False)
    vacancies = models.FloatField(blank=False)

    def __str__(self):
        return str(self.city)