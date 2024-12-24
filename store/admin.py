"""
Module: admin.py

Django admin configurations for managing categories, items, and deliveries.

This module defines the following admin classes:
- CategoryAdmin: Configuration for the Category model in the admin interface.
- ItemAdmin: Configuration for the Item model in the admin interface.
- DeliveryAdmin: Configuration for the Delivery model in the admin interface.
"""

from django.contrib import admin
from .models import Sdd, Item, Delivery, Hdd, M_2, Nvme, Ram,Processor


class RamAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Ram model.
    """
    list_display = ('name', 'slug')
    search_fields = ('name',)
    ordering = ('name',)

class ProcessorAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Processor model.
    """
    list_display = ('name', 'slug')
    search_fields = ('name',)
    ordering = ('name',)

class HddAdmin(admin.ModelAdmin):
    """
    Admin configuration for the hdd model.
    """
    list_display = ('name', 'slug')
    search_fields = ('name',)
    ordering = ('name',)

class SddAdmin(admin.ModelAdmin):
    """
    Admin configuration for the hdd model.
    """
    list_display = ('name', 'slug',"capcity","product_code")
    search_fields = ('name','capcity', 'product_code')
    ordering = ('name',)

class M_2Admin(admin.ModelAdmin):
    list_display = ('name', 'model', 'capacity', 'product_code')  # Corrected attributes
    search_fields = ('name', 'model', 'product_code')  # Add any fields you want searchable
    list_filter = ('capacity',)  # Optional: add filtering based on capacity

class NvmeAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'capacity', 'product_code')  # Corrected attributes
    search_fields = ('name', 'model', 'product_code')  # Add any fields you want searchable
    list_filter = ('capacity',)  # Optional: add filtering based on capacity


class ItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Item model.
    """
    list_display = (
        "serialno","make_and_models","processor","ram","hdd","ssd","smps","motherboard"
    )
    # search_fields = ('name', 'category__name', 'vendor__name')
    # list_filter = ('category', 'vendor')
    ordering = ('name',)


class DeliveryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Delivery model.
    """
    list_display = (
        'item', 'customer_name', 'phone_number',
        'location', 'date', 'is_delivered'
    )
    search_fields = ('item__name', 'customer_name')
    list_filter = ('is_delivered', 'date')
    ordering = ('-date',)


admin.site.register(Ram, RamAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Sdd, SddAdmin)
admin.site.register(Hdd, HddAdmin)
admin.site.register(M_2, M_2Admin)
admin.site.register(Nvme, NvmeAdmin)
admin.site.register(Processor, ProcessorAdmin)
