from django_filters import FilterSet
from .models import *


class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_type' : ['exact'],
            'room_price' : ['gt','lt'],
            'room_status' : ['exact'],
            'all_inclusive' : ['exact'],
            }