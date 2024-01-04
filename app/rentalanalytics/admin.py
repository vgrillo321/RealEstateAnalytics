from django.contrib import admin

# Register your models here.
from django.contrib import admin

# import the model Todo
from .models import RentalProperties

# create a class for the admin-model integration
class RentalAdmin(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ("address","price","size", "pricePerSqft")

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(RentalProperties,RentalAdmin)
