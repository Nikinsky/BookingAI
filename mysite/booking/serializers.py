
from rest_framework import serializers
from .models import *




class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()







class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'phone_number', 'age', 'user_role']

class UserProfileOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']






class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']



class HotelSerializers(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(read_only=True, many=True)
    owner = UserProfileOwnerSerializer()
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['name_hotel', 'owner', 'description', 'address', 'city', 'country', 'created_date', 'start', 'hotel_video', 'created_date', 'average_rating', 'hotel_images']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class HotelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name_hotel']












class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRoom
        fields = ['room_image']


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = [ 'room_number', 'room_type', 'room_price', 'all_inclusive', 'room_description']


class RoomListSerializer(serializers.ModelSerializer):

    room_images  = RoomImageSerializer(many=True)
    class Meta:
        model = Room
        fields = ['room_number','room_type','room_status',
                  'room_price','room_images','all_inclusive']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(read_only=True,many=True)
    class Meta:
        model = Room
        fields = ['hotel', 'room_number', 'room_type',
                  'room_status','room_price','all_inclusive',
                  'room_description','room_images']


class RoomNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number']




class ReviewListSerializer(serializers.ModelSerializer):
    user_name = UserProfileSerializer()

    class Meta:
        model = Review
        fields = ['id','user_name','hotel','text','stars','parent']



class ReviewSerializer(serializers.ModelSerializer):
    user_name = UserProfileOwnerSerializer()
    hotel = HotelNameSerializer()
    class Meta:
        model = Review
        fields = ['user_name', 'hotel', 'text', 'stars', 'parent']




class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(read_only=True,many=True)
    average_rating = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Hotel
        fields = ['name_hotel','country','city','hotel_images','start','average_rating']


    def get_average_rating(self,obj):
        return obj.get_average_rating()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(read_only=True, many=True)
    review = ReviewSerializer(many=True,read_only=True)
    rooms = RoomSerializer(read_only=True,many=True)
    owner = UserProfileSerializer()
    average_rating =  serializers.SerializerMethodField()


    class Meta:
        model = Hotel
        fields = ['name_hotel','description','country',
                  'city','address','start','hotel_images',
                  'hotel_video','review'
                  ,'owner','created_date','rooms','average_rating'
                  ]


    def get_average_rating(self,obj):
        return obj.get_average_rating()





class BookingSerializer(serializers.ModelSerializer):
    hotel_book = HotelNameSerializer()
    room_book = RoomNumberSerializer()
    user_book = UserProfileOwnerSerializer()
    check_in = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    check_out = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Booking
        fields = ['hotel_book', 'room_book', 'user_book', 'check_in', 'check_out', 'total_price', 'status_book']
