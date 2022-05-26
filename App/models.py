from django.db import models
import uuid


class Company(models.Model):
    name = models.CharField(max_length=100)

    class Meta: 
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=60)
    author = models.ForeignKey(
        Author, 
        on_delete=models.PROTECT, 
        null=True
    )

    def __str__(self):
        if self.author is None:
            return self.name
        else:
            return f"{self.name} - {self.author}"

class Library(models.Model):
    name = models.CharField(max_length=60)
    book = models.ManyToManyField(
        Book,
        related_name="library"
    )
    
    class Meta: 
        verbose_name_plural = "libraries"

    def __str__(self):
        return self.name

class Employee(models.Model):
    fName = models.CharField("first name", max_length=50)
    mName = models.CharField("middle name", max_length=50, blank=True)
    lName = models.CharField("last name", max_length=50, blank=True)
    age = models.PositiveIntegerField()
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="employees"
    )
    library = models.ManyToManyField(
        Library, 
        related_name="employees",
        through="EmployeeMembership",
    )

    def get_full_name(self):
        return f"{self.fName} {self.mName} {self.lName}"

    def __str__(self):
        return f"{self.get_full_name()} - {self.company}"

class EmployeeMembership(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=True,
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
    )
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
    )
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.id} - {self.employee.get_full_name()} - {self.employee.company}"

