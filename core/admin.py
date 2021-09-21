from django.contrib import admin
from .models import Subscription, Breakfast, Lunch, Dinner, User

admin.site.register(Subscription)
admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)
admin.site.register(User)