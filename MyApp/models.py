from django.db import models


class user_member(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    passwrd = models.CharField(max_length=50)
    city = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=50)
    def __str__(self):
        return self.username


class Brand(models.Model):
    b_id = models.AutoField(primary_key=True)
    b_name = models.CharField(max_length=255)
    b_image = models.FileField(upload_to="brands/",default=None)
    def __str__(self):
        return self.b_name


class Testimonial(models.Model):
    t_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField()
    t_description = models.CharField(max_length=255)
    t_rating = models.CharField(max_length=255)
    t_isActive = models.BooleanField()
    def __str__(self):
        return self.t_description


class Vehicle(models.Model):
    v_id = models.AutoField(primary_key=True)
    v_name = models.CharField(max_length=255)
    v_description = models.TextField()
    v_bodyType = models.CharField(max_length=255)
    v_brand = models.IntegerField()
    v_brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    v_fuelType = models.CharField(max_length=255)
    v_engine = models.CharField(max_length=255)
    v_powerWindow = models.BooleanField()
    v_bluetooth = models.BooleanField()
    v_keylessStart = models.BooleanField()
    v_cruiseControl = models.BooleanField()
    v_navigation = models.BooleanField()
    v_heatedSeats = models.BooleanField()
    v_price = models.CharField(max_length=255)
    v_image = models.FileField(upload_to="VehicleImages/", default=None)
    def __str__(self):
        return self.v_name


class ContactUs(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=255)
    c_email = models.CharField(max_length=255)
    c_desc = models.CharField(max_length=255)
    def __str__(self):
        return self.c_name


class Subscriber(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_email = models.CharField(max_length=255)
    def __str__(self):
        return self.s_email


class BookingInfo(models.Model):
    b_id = models.AutoField(primary_key=True)
    b_bookdate = models.DateTimeField()
    b_returndate = models.DateTimeField(null=True)
    b_vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    b_user = models.ForeignKey(user_member, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.b_user.username



#    Vehicles
#    id
#    name 
#   image


# Create your models here.
