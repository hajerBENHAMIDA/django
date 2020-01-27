from django.contrib import admin
from .models import Employee

# Register your models here.
class mydata(admin.ModelAdmin):
    list_display = ('ename','eemail','econtact','eid')
    
admin.site.register(Employee,mydata)

