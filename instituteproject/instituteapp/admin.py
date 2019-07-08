from django.contrib import admin

from instituteapp.models import ContactData,FeedbackData

class AdminContactData(admin.ModelAdmin):
    list_display = ['name','email','mobile','courses','shift']
class AdminFeedbackData(admin.ModelAdmin):
    list_display = ['name','rating','date','feedback']

admin.site.register(ContactData,AdminContactData)
admin.site.register(FeedbackData,AdminFeedbackData)