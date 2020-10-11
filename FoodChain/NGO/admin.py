from django.contrib import admin
from .models import Belongs,Cities,otherDetails,foodAvbl,Measurement

admin.site.register(Belongs)
admin.site.register(Cities)
admin.site.register(otherDetails)
admin.site.register(foodAvbl)
admin.site.register(Measurement)

