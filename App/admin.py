from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
import datetime


from .models import (
    Book, 
    Company, 
    Employee, 
    Library,
    Author,
    EmployeeMembership,
)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    
    ordering=['id']
    list_display = [
        "id",
        "name",
        "age",
        "company",
        "membership",
    ]
    search_fields = [
        "id",
        "fName",
        "mName",
        "lName",
    ]
    list_filter = (
        "company__name", 
        "membership",
    )
    
    # @admin.display(ordering='name')
    def name(self, obj):
        return f"{obj.fName} {obj.mName} {obj.lName}"


@admin.register(EmployeeMembership)
class EmployeeMembershipAdmin(admin.ModelAdmin):

    ordering=['date_joined']
    list_display = [
        "date_joined",
        "_employee_",
        "company",
        "expiry_date",
    ]
    search_fields = [
        "_employee_",
        "company__name",
    ]
    list_filter = [
        (
        "date_joined", 
        DateRangeFilter
        ),
    ]

    def _employee_(self, obj):
        return f"{obj.employee.fName} {obj.employee.mName} {obj.employee.lName}"

    def company(self, obj):
        return obj.employee.company


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    ordering=['id']
    list_display = [
        "id",
        "name",
        "author",
    ]
    search_fields = [
        "id",
        "name",
        "author",
    ]
    list_filter = (
        "author",
    )


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):

    ordering=['id']
    list_display = [
        "id",
        "name",
        "books",
    ]
    search_fields = [
        "name",
        "book__name",
    ]

    @admin.display(ordering='book__name')
    def books(self, obj):
        return obj.get_books_with_author()

@admin.register(
    Company,
    Author,
)

class DefaultAdmin(ImportExportModelAdmin):
    """
    Subclass of ExportActionModelAdmin with import/export functionality.
    """