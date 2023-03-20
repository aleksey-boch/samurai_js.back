from django.contrib import admin

from .models import User, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'login', 'status', 'created_at', 'updated_at',)
    list_display_links = ('id', 'name', 'email', 'login',)
    search_fields = ('name', 'email', 'login',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'looking_for_a_job',
                    'looking_for_a_job_description', 'created_at', 'updated_at',)
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'looking_for_a_job_description',)
    # list_editable = ('user_id',)
    # prepopulated_fields = {}


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
