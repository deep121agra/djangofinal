from django.contrib import admin
from vendor.models import Vendor
#from django.contrib
# Register your models here.
# Now i want to make a class in it it can do noting it can represent a all detils in a admin.py 
class VendorAdmin(admin.ModelAdmin):
    list_display=('user','vendor_name','is_approved','created_at')
    list_display_links=('user','vendor_name')
admin.site.register(Vendor,VendorAdmin)
