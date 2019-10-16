from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import User, Entry, Image


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Entry)
class Entry(admin.ModelAdmin):
    pass
    
@admin.register(Image)
class Entry(admin.ModelAdmin):
    pass