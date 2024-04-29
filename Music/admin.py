from django.contrib import admin 
from Music.models import Artist, Track
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import AppUser

# Register your models here.
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = AppUser

    list_display = ('username', 'email', 'is_active',
                    'is_staff', 'is_superuser', 'last_login',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class TrackInline(admin.TabularInline):
    model = Track
    extra = 0

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [TrackInline]

class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'genre', 'duration']

admin.site.register(AppUser, UserAdmin)
admin.site.unregister(Group)