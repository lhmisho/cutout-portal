from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Requirement)
admin.site.register(Addons)
admin.site.register(Instruction)
admin.site.register(Order)