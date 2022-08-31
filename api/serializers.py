from App.models import Author, Book, Company, Employee, EmployeeMembership, Library
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class BaseSerailizer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(read_only=True)


class BookSerializer(BaseSerailizer):
    """
    CompanySerializer
    """
    author = serializers.CharField(read_only=True)

    class Meta:
        model= Book
        fields = [
          "id",
          "name",
          "author"
        ]

class AuthorSerializer(BaseSerailizer):
    """
    AuthorSerializer
    """
    books = BookSerializer(many=True, source="book_set")

    class Meta:
        model= Author
        fields = [
          "id",
          "name",
          "books",
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


class EmployeeMembershipSerializer(BaseSerailizer):
    """
    EmployeeMembership
    """
    employee = serializers.CharField()
    validity = serializers.DateField(source="expiry_date", read_only=True)

    class Meta:
        model= EmployeeMembership
        fields = [
          "employee", 
          "validity",
        ]


class LibrarySerializer(BaseSerailizer):
    """
    LibrarySerializer
    """
    books = BookSerializer(source="book", many=True)
    membership = EmployeeMembershipSerializer(many=True, source="employeemembership_set")


    class Meta:
        model= Library
        fields = [
          "name",
          "books",
          "membership",
        ]

    # def get_membership(self, obj):
    #   return EmployeeMembershipSerializer(obj.membership.all(), many=True).data

    # def create(self, validated_data):
    #     member_data = validated_data.pop('membership')
    #     outcome = Library.objects.create(**validated_data)
    #     for data in member_data:
    #         EmployeeMembership.objects.create(outcome=outcome, **data)
    #     return outcome


class EmployeeSerializer(WritableNestedModelSerializer, BaseSerailizer):
    """
    EmployeeSerializer
    """
    first_name = serializers.CharField(source="fName")
    middle_name = serializers.CharField(source="mName", allow_blank=True)
    last_name = serializers.CharField(source="lName", allow_blank=True)
    age = serializers.IntegerField()
    company = serializers.CharField()
    membership_validity = serializers.DateField(source="employeemembership.expiry_date")


    class Meta:
        model= Employee
        fields = [
          "id",
          "first_name",
          "middle_name",
          "last_name",
          "age",
          "company",
          "membership_validity",
        ]

    # def create(self, validated_data):
    #     member_data = validated_data.pop('membership')
    #     outcome = Library.objects.create(**validated_data)
    #     for data in member_data:
    #         EmployeeMembership.objects.create(outcome=outcome, **data)
    #     return outcome


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








