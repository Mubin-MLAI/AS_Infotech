import django_tables2 as tables
from .models import Item, Delivery


class ItemTable(tables.Table):
    """
    Table representation for Item model.
    """
    class Meta:
        model = Item
        template_name = "django_tables2/semantic.html"
        fields = (
            'id', 'name', 'serialno', 'make_and_models', 
            'processor', 'ram', 'ram_qty', 'hdd', 'hdd_qty', 
            'ssd', 'ssd_qty', 'smps', 'motherboard', 
            'smps_status', 'motherboard_status'
        )
        order_by_field = 'id'  # or any other field you prefer


class DeliveryTable(tables.Table):
    """
    Table representation for Delivery model.
    """
    class Meta:
        model = Delivery
        fields = (
            'id', 'item', 'customer_name', 'phone_number',
            'location', 'date', 'is_delivered'
        )
