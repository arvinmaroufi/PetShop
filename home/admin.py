from django.contrib import admin
from . import models


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'short_subject', 'created_at']

    def short_subject(self, obj):
        if len(obj.subject) > 20:
            return obj.subject[:20] + '...'
        return obj.subject
    short_subject.short_description = 'موضوع'


