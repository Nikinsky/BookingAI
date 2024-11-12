from django.urls import path
from .views import *

urlpatterns = [
    path('', HotelView.as_view({'get': 'list', 'post':'create',}), name='hotel_list'),
    path('<int:pk>/', HotelDetailViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='hotel_detail'),

    path('hotel_list',HotelListViewSet.as_view({'get':'list'}), name='hotellist_list'),

    path('user', UserProfileView.as_view({'get': 'list', 'post':'create',}), name='user_list'),
    path('user/<int:pk>/', UserProfileView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='user_detail'),

    path('room', RoomView.as_view({'get': 'list', 'post':'create',}), name='room_list'),
    path('room/<int:pk>/', RoomDetailViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='room_detail'),

    path('review', ReviewView.as_view({'get': 'list', 'post':'create',}), name='review_list'),
    path('review/<int:pk>/', ReviewView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='review_detail'),

    path('booking', BookingView.as_view({'get': 'list', 'post':'create',}), name='booking_list'),
    path('booking/<int:pk>/', BookingView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='booking_detail'),

    path('check', ImageProductView.as_view(), name='check_image')

]
