from django.db import models

class Breakfast(models.Model):
    MEALS = [
    ('DM1', 'Dummy Meal 1'),
    ('DM2', 'Dummy Meal 2'),
    ('DM3', 'Dummy Meal 3'),
    ('DM4', 'Dummy Meal 4'),
    ('DM5', 'Dummy Meal 5'),
    ]

    time = models.TimeField()
    meal = models.CharField(choices=MEALS, max_length=4)
    mid = models.IntegerField()

    def __str__(self):
        return self.mid


class Lunch(models.Model):
    MEALS = [
    ('DM6', 'Dummy Meal 6'),
    ('DM7', 'Dummy Meal 7'),
    ('DM8', 'Dummy Meal 8'),
    ('DM9', 'Dummy Meal 9'),
    ('DM10', 'Dummy Meal 10'),
    ]

    time = models.TimeField()
    meal = models.CharField(choices=MEALS, max_length=4)
    mid = models.IntegerField()

    def __str__(self):
        return self.mid

class Dinner(models.Model):
    MEALS = [
    ('DM11', 'Dummy Meal 11'),
    ('DM12', 'Dummy Meal 12'),
    ('DM13', 'Dummy Meal 13'),
    ('DM14', 'Dummy Meal 14'),
    ('DM15', 'Dummy Meal 15'),
    ]

    time = models.TimeField()
    meal = models.CharField(choices=MEALS, max_length=4)
    mid = models.IntegerField()

    def __str__(self):
        return self.mid     

class User(models.Model):
    pass

class Subscription(models.Model):
    HOSTELS = [
        ('A', 'Abuja'),
        ('N', 'Naraguta'),
        ('P', 'PG'),
        ('Z', 'Zion'),
    ]
    breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE)
    lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE)
    dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE)
    hostel = models.CharField(choices=HOSTELS, max_length=1, default='N')
    block = models.CharField(max_length=20)
    room_no = models.IntegerField()
    sid = models.BigAutoField(primary_key=True)

class Coupon(models.Model):
    pass

