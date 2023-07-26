from django.contrib import admin

from .models import Cars
from .models import Details
from .models import Garages

admin.site.register(Cars)
admin.site.register(Details)
admin.site.register(Garages)
