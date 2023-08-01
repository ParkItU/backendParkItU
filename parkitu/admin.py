from django.contrib import admin

from .models import Car
from .models import Detail
from .models import Garage

admin.site.register(Car)
admin.site.register(Detail)
admin.site.register(Garage)
