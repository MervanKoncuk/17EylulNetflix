from django.contrib import admin
from .models import *
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('isim', 'user', 'slug')
    list_display_links = ('isim', 'user')
    list_filter = ('user',)
    search_fields = ('isim',)
    # list_editable = ('slug',)
    readonly_fields = ('id', 'slug')
# Register your models here.
admin.site.register(Profile, ProfilAdmin)
admin.site.register(Hesap)