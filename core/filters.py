import django_filters as filters
from core import models


class AccountSearch(filters.FilterSet):
    class Meta:
        model = models.Account
        fields = ['user', ]
