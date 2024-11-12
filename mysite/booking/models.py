from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField







class UserProfile(AbstractUser):
    STATUS_CHOICES = (
        ('Пользователь', 'Пользователь'), # Клиент (может бронировать и оставлять отзывы),
        ('Владелец_отеля', 'Владелец_отеля'), # Владелец (может добавлять отели и управлять номерами)
        ('admin', 'admin') # Администратор (полный доступ к данным).
    )
    user_role = models.CharField(max_length=32, choices=STATUS_CHOICES, default='Пользователь')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(70)], null=True, blank=True)



class Hotel(models.Model):
    name_hotel = models.CharField(max_length=32)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32, verbose_name='city')
    country = models.CharField(max_length=32)
    created_date = models.DateField()
    start = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    hotel_video = models.FileField(upload_to='hotel_image/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name_hotel} - {self.country}'

    def get_average_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return (round(sum(rating.stars for rating in ratings) / ratings.count(), 1))
        return 0

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotel',  on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_image/')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.PositiveSmallIntegerField(default=0)
    TYPE_CHOICES = (
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('одноместный', 'одноместный'),
    )
    room_type = models.CharField(max_length=16, choices=TYPE_CHOICES, default="свободен")
    STATUS_CHOICES = (
        ("свободен", "свободен"),
        ("забронирован", "забронирован"),
        ("занят", "занят"),
    )
    room_status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='свободен')
    room_price = models.PositiveIntegerField()
    all_inclusive = models.BooleanField(default=False)
    room_description = models.TextField()

    def __str__(self):
        return f'{self.hotel} - kvartira {self.room_number}'


class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_image')
    room_image = models.ImageField(upload_to='room_images/')



class Review(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.user_name} - {self.hotel}, {self.stars}'


class Booking(models.Model):
    hotel_book = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_book = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_book = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_BOOK_CHOICES = (
        ('отменено', 'отменено'),
        ('подтверждено', 'подтверждено')
    )
    status_book = models.CharField(max_length=16, choices=STATUS_BOOK_CHOICES)

    def __str__(self):
        return f'{self.user_book}, {self.hotel_book}, {self.room_book}, {self.status_book}'