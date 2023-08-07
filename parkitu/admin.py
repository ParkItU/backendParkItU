from django.contrib import admin

from parkitu.models import Cars

from parkitu.models import Details
from parkitu.models import Garages

admin.site.register(Cars)
admin.site.register(Details)
admin.site.register(Garages)
