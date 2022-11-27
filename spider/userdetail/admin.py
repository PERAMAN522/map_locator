from django.contrib import admin
from .models import Userdetails,Country,State,City
# Register your models here.
admin.site.register(Userdetails)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)