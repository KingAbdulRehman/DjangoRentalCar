from django.contrib import admin
from MyApp.models import user_member, Brand, Testimonial, ContactUs, Vehicle, Subscriber, BookingInfo

admin.site.register(user_member)
admin.site.register(Brand)
admin.site.register(Testimonial)
admin.site.register(ContactUs)
admin.site.register(Vehicle)
admin.site.register(Subscriber)
admin.site.register(BookingInfo)

# Register your models here.
