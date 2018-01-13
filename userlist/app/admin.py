from django.contrib import admin

# Register your models here.

from .models import Users
class UserAdmin(admin.ModelAdmin):
    model = Users
    list_display = ('name', 'email','created_at','updated_at')
	
admin.site.register(Users,UserAdmin)