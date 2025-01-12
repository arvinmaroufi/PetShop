from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.ContactUs)
class ContactUsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['email', 'short_subject', 'get_created_jalali']

    def short_subject(self, obj):
        if len(obj.subject) > 20:
            return obj.subject[:20] + '...'
        return obj.subject
    short_subject.short_description = 'موضوع'

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')


@admin.register(models.FAQ)
class FaqAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['short_question', 'get_created_jalali']

    def short_question(self, obj):
        if len(obj.question) > 30:
            return obj.question[:30] + '...'
        return obj.question
    short_question.short_description = 'سوال'

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')


