from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import datetime
import datetime


class Contact(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(max_length=2000, null=False, blank=False)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "name: " + self.name, " => subject: " + self.subject


class Update(models.Model):
    to = models.CharField(max_length=2000)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=2000, null=False, blank=False)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "name: " + self.to


class Staff(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    serial = models.CharField(max_length=12)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=12)
    email = models.EmailField()
    idno = models.IntegerField()
    age = models.IntegerField(default=18)
    date = models.DateTimeField(default=datetime.datetime.now)
    profile = models.ImageField(upload_to="images", null=False, default='default.jpg')
    address = models.CharField(max_length=50, default='John')
    other1 = models.CharField(max_length=50, default='Doe')
    other2 = models.CharField(max_length=50, default='Jane')
    other3 = models.CharField(max_length=50, default='phil')

    def __str__(self):
        return "name: " + self.username


a = datetime.datetime.today()
b = a.date()
c = a.time()
y = a.year
m = a.month
d = a.day


class Sell(models.Model):
    staff = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=10)
    fuel = models.CharField(max_length=50)
    litres = models.FloatField(default=1)
    f = models.IntegerField(default=0)
    amount = models.FloatField(default=0)
    date = models.DateTimeField(default=datetime.datetime.now)
    year = models.IntegerField(default=y)
    month = models.IntegerField(default=m)
    day = models.IntegerField(default=d)

    def __str__(self):
        return "customer: " + self.number_plate


class Category(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=1)
    date = models.DateTimeField(default=datetime.datetime.now)
    other1 = models.CharField(max_length=50, default='Doe')
    other2 = models.CharField(max_length=50, default='Jane')
    other3 = models.CharField(max_length=50, default='phil')

    def __str__(self):
        return "Category: " + self.name


class About(models.Model):
    num = models.IntegerField(default=1)
    details = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    other1 = models.CharField(max_length=50, default='Doe')
    other2 = models.CharField(max_length=50, default='Jane')
    other3 = models.CharField(max_length=50, default='phil')
