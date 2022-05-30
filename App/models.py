from django.db import models
import datetime

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

    def get_books(self):
        return ", ".join([b.name for b in self.book.all()])

    def get_authors(self):
        return ", ".join([b.author.name for b in self.book.all()])

    def get_books_with_author(self):
        return ", ".join(f"{b.name} ({b.author})"for b in self.book.all())

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Employee details.
    """

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
    membership = models.BooleanField(
        default=False,
    )
    idCard_pic = models.ImageField(
        "ID card image",
        upload_to=None, 
        height_field=None, 
        width_field=None, 
        max_length=100,
        blank=True,
    )

    def get_full_name(self):
        verbose_name = "Full Name"
        return f"{self.fName} {self.mName} {self.lName}"
    
    def __str__(self):
        return f"{self.get_full_name()} - {self.company}"


class MembershipDuration(models.TextChoices):
    """
    Enumerated choices for the membership duration.
    """

    ONE_MONTH = 30, "30 Days - 1 Month"
    THREE_MONTH = 90, "90 Days - 3 months"
    SIX_MONTH = 180, "180 Days - 6 months"
    ONE_YEAR = 365, "365 Days - 1 Year"


class EmployeeMembership(models.Model):

    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        unique=True,
    )
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
    )
    date_joined = models.DateField(auto_now_add=True)
    duration = models.CharField(
        max_length=125,
        choices=MembershipDuration.choices,
        default=MembershipDuration.ONE_MONTH,
    )

    def expiry_date(self):
        self.expiry_date = self.date_joined + datetime.timedelta(days=int(self.duration))
        return self.expiry_date

    def __str__(self):
        return f"{self.employee.id} - {self.employee.get_full_name()} - {self.employee.company}"











    # membership_expiry = models.DateField(null=True, editable=False)

    # def save(self, *args, **kwargs):
    #     if self.membership_expiry is None:
    #         self.membership_expiry = self.date_joined.date() + datetime.timedelta(days=30)
    #     super(EmployeeMembership, self).save(*args, **kwargs)