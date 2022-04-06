from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    class Meta: 
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=60)
    employees = models.ManyToManyField(Employee)
    
    class Meta: 
        verbose_name = "library"
        verbose_name_plural = "libraries"

    def __str__(self):
        return self.name