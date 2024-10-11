from django.contrib import admin
from .models import *

class CartegoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('cartegory_name',)}
    list_display = ('cartegory_name','slug')

admin.site.register(cartegory, CartegoryAdmin)