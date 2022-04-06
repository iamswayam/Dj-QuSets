from django.contrib import admin
from .models import Company, Employee, Library

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Library)