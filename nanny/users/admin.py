from django.contrib import admin

# Register your models here.
from . models import Profile



class ProfileAdmin(admin.ModelAdmin):
    list_display= ('nanny_user','phone_number','is_employer','state','city','religion','education','ethinicity','date_of_birth',)
    list_filter=('education',)
    
admin.site.register(Profile, ProfileAdmin)