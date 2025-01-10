from django.contrib import admin
from . import models


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'short_subject', 'created_at']

    def short_subject(self, obj):
        return obj.subject[:20]
    short_subject.short_description = 'Subject'


