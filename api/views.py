import re
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import permissions, status, viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from App.models import (
      Book, 
      Company, 
      Employee, 
      Library,
      EmployeeMembership,
)
from .serializers import (
      BookSerializer, 
      EmployeeSerializer, 
      CompanySerializer, 
      LibrarySerializer,
      EmployeeMembershipSerializer,
)


class apiHome(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request,format=None):  
        wc_msg="Welcome to this Project"
        return Response(wc_msg, status=status.HTTP_200_OK)


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    """
    EmployeeViewSet
    """

    filter_backends = [
        DjangoFilterBackend,
    ]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    CompanyViewSet
    """

    filter_backends = [
        DjangoFilterBackend,
    ]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

    # def create(self, request, *args, **kwargs):
    #     new_category = EmployeeSerializer(data=request.data)
    #     if new_category.is_valid:
    #         return Response(EmployeeSerializer(new_category).data)
    

class LibraryViewSet(viewsets.ModelViewSet):
    """
    LibraryViewSet
    """

    filter_backends = [
        DjangoFilterBackend,
    ]
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
class BookViewSet(viewsets.ModelViewSet):
    """
    BookViewSet
    """

    filter_backends = [
        DjangoFilterBackend,
    ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MembershipViewSet(viewsets.ModelViewSet):
    """
    BookViewSet
    """

    filter_backends = [
        DjangoFilterBackend,
    ]
    queryset = EmployeeMembership.objects.all()
    serializer_class = EmployeeMembershipSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]







    # def get_queryset(self):
    #     return self.queryset

    # def get_queryset(self):
    #     return self.request.user.accounts.all()