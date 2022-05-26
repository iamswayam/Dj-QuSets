from django.shortcuts import render
from .models import Book, Company, Employee, Library
from django.db.models import Prefetch   

# print(Employee.objects.all())


def home(request):
    # employees = Employee.objects.all().prefetch_related('library_set')
    employees = Employee.objects.all().filter(company__name="Infosys")
                # .select_related('company')
                # .prefetch_related(('staff__courses').order_by('-begin'))
                # )
    # .select_related('company')
    # for employee in employees:
    #     print(f"FIL_TER: {employee}")
    return render(request, 'home.html', {"employees": employees})

def home2(request):

    # employees = Employee.objects.all()
    # employees = Employee.objects.select_related("company").all()
    employees = Employee.objects.prefetch_related(
                    Prefetch('library__book', queryset=Book.objects.order_by('name'))
                        ).filter(library__book__name="Washington DC book")
    print(employees)
    # print(f"SEL_REL: {companies}")
    # print(f"OUTPUT:- {employees}")

    # for employee in employees:
    #     print(f"SEL_REL: {employee.id}: {employee.name}")
    queryset = {
        "employees": employees
    }
    return render(request, 'home2.html', queryset)
    
# def home3(request):

#     employees = Employee.objects.all()

#     for employee in employees:
#         print(employee.library_set.all())
#     return None
