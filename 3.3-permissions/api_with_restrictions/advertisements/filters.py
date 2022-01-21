from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter

from advertisements.models import Advertisement

class AdvertisementFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter()
    """Фильтры для объявлений."""
    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']