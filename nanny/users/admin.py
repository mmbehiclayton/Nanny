from django.contrib import admin

# Register your models here.
from . models import NannyProfile



class NannyProfileAdmin(admin.ModelAdmin):
    list_display= ('nanny_user','phone_number','state','city','religion','education','ethinicity','date_of_birth',)
    list_filter=('education',)
    
admin.site.register(NannyProfile, NannyProfileAdmin)