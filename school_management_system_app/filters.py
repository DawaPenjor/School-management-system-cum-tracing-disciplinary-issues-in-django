import django_filters
from .models import *
from django_filters import CharFilter, NumberFilter


class StaffFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    Employee_ID = NumberFilter(
        field_name='Employee_ID', lookup_expr='icontains')

    class Meta:
        model = StaffDetail
        fields = [
            'name',
            'Employee_ID'
        ]


class StudentFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    section = CharFilter(field_name='section', lookup_expr='icontains')

    class Meta:
        model = StudentDetail
        fields = [
            'name',
            'section',
        ]
