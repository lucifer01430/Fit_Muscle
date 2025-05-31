from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Icon, Service, Trainer, ClassSchedule, GalleryImage,
    Testimonial, Notification, ScheduleBackground, MembershipPlan 
)

@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ['name', 'default_icon_preview', 'hover_icon_preview']

    def default_icon_preview(self, obj):
        if obj.default_icon:
            return format_html('<img src="{}" style="height:30px;" />', obj.default_icon.url)
        return "-"
    default_icon_preview.short_description = "Dark Icon"

    def hover_icon_preview(self, obj):
        if obj.hover_icon:
            return format_html('<img src="{}" style="height:30px;" />', obj.hover_icon.url)
        return "-"
    hover_icon_preview.short_description = "White Icon"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'trainer', 'icon', 'duration']
    list_filter = ['trainer']
    search_fields = ['title', 'trainer__name']

@admin.register(ScheduleBackground)
class ScheduleBackgroundAdmin(admin.ModelAdmin):
    list_display = ['name', 'preview']

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px;" />', obj.image.url)
        return "-"
    preview.short_description = "Preview"

@admin.register(ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ['name', 'day', 'start_time', 'end_time', 'trainer', 'service']
    list_filter = ['day', 'trainer', 'service']
    search_fields = ['name', 'trainer__name', 'service__title']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'preview']

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:30px;" />', obj.image.url)
        return "-"
    preview.short_description = "Image"

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'duration_text', 'preview']

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px;" />', obj.image.url)
        return "-"
    preview.short_description = "Image"


admin.site.register(Trainer)
admin.site.register(GalleryImage)



