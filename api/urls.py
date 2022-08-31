from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.apiHome.as_view()),
]

router = DefaultRouter()

router.register(r'employee', views.EmployeeViewSet, basename='employees')
router.register(r'company', views.CompanyViewSet, basename='companies')
router.register(r'library', views.LibraryViewSet, basename='libraries')
router.register(r'book', views.BookViewSet, basename='books')
router.register(r'membership', views.MembershipViewSet, basename='membership')
router.register(r'author', views.AuthorViewSet, basename='authors')

urlpatterns = router.urls