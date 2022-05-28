from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

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
    ]
    search_fields = [
        "id",
        "_employee_",
    ]

    @admin.display(ordering='employee__get_full_name')
    def _employee_(self, obj):
        return f"{obj.employee.fName} {obj.employee.mName} {obj.employee.lName}"


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

@admin.register(
    Company,
    Library,
    Author,
)

class DefaultAdmin(ImportExportModelAdmin):
    """
    Subclass of ExportActionModelAdmin with import/export functionality.
    """