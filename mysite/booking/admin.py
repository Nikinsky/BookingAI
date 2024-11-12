from django.contrib import admin
from .models import *


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

class RoomImageInline(admin.TabularInline):
    model = ImageRoom
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageInline]

class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]



admin.site.register(UserProfile)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Review)
admin.site.register(Booking)
