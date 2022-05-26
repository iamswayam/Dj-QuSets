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

# admin.site.register(Company)
# admin.site.register(Employee)
# admin.site.register(Library)
# admin.site.register(Book)

@admin.register(
    Company,
    Employee,
    Library,
    Book,
    Author,
    EmployeeMembership,
)

class DefaultAdmin(ImportExportModelAdmin):
    """
    Subclass of ExportActionModelAdmin with import/export functionality.
    """