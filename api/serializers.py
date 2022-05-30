from App.models import Author, Book, Company, Employee, Library
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class BaseSerailizer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(read_only=True)


class AuthorSerializer(BaseSerailizer):
    """
    AuthorSerializer
    """

    class Meta:
        model= Author
        fields = [
          "name"
        ]


class BookSerializer(BaseSerailizer):
    """
    CompanySerializer
    """
    author = serializers.CharField(read_only=True)

    class Meta:
        model= Book
        fields = [
          "name",
          "author"
        ]

    # def create(self, validated_data):
    #     author_datas = validated_data.pop('author', None)
    #     employee = Employee.objects.create(**validated_data)
    #     for author_data in author_datas:
    #         Book.objects.create(employee=employee, **author_data)
    #         return employee

class EmployeeNameSerializer(BaseSerailizer):
    """
    EmployeeNameSerializer
    """

    employee_name = serializers.CharField(read_only=True, source="get_full_name")

    class Meta:
        model= Employee
        fields = [
          "employee_name",
          "id",
        ]


class LibrarySerializer(BaseSerailizer):
    """
    CompanySerializer
    """
    books = BookSerializer(source="book", many=True)
    employees = EmployeeNameSerializer(many=True)

    class Meta:
        model= Library
        fields = [
          "name",
          "books",
          "employees",
        ]


class EmployeeSerializer(WritableNestedModelSerializer, BaseSerailizer):
    """
    EmployeeSerializer
    """
    first_name = serializers.CharField(source="fName")
    middle_name = serializers.CharField(source="mName", allow_blank=True)
    last_name = serializers.CharField(source="lName", allow_blank=True)
    age = serializers.IntegerField()
    company = serializers.CharField()
    library = LibrarySerializer(many=True)
    membership = serializers.BooleanField()

    class Meta:
        model= Employee
        fields = [
          "id",
          "first_name",
          "middle_name",
          "last_name",
          "age",
          "company",
          "library",
          "membership",
        ]


class CompanySerializer(BaseSerailizer):
    """
    CompanySerializer
    """
    employees = EmployeeNameSerializer(many=True)

    class Meta:
        model= Company
        fields = [
          "name", 
          "employees",
        ]


class EmployeeMembershipSerializer(BaseSerailizer):
    """
    CompanySerializer
    """
    employee = serializers.CharField()
    validity = serializers.DateField(source="expiry_date", read_only=True)

    class Meta:
        model= Company
        fields = [
          "employee", 
          "validity",
        ]





