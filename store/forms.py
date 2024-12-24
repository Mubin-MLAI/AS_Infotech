from django import forms
from .models import Item, Delivery, Sdd,Hdd,Processor,M_2,Nvme,Ram


class ItemForm(forms.ModelForm):
    """
    A form for creating or updating an Item in the inventory.
    """
    class Meta:
        model = Item
        fields = [
            'name',
            'serialno',            # Serial number field
            'make_and_models',     # Make and models field
            'processor',           # Processor field
            'ram',                 # RAM field
            'ram_qty',             # RAM quantity field
            'hdd',                 # HDD field
            'hdd_qty',             # HDD quantity field
            'ssd',                 # SSD field
            'ssd_qty',             # SSD quantity field
            'smps',                # SMPS field
            'smps_status',         # SMPS status field
            'motherboard',         # Motherboard field
            'motherboard_status',  # Motherboard status field
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'serialno': forms.TextInput(attrs={'class': 'form-control'}),
            'make_and_models': forms.TextInput(attrs={'class': 'form-control'}),
            'processor': forms.Select(attrs={'class': 'form-control'}),
            'ram': forms.Select(attrs={'class': 'form-control'}),
            'ram_qty': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'hdd': forms.Select(attrs={'class': 'form-control'}),
            'hdd_qty': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'ssd': forms.Select(attrs={'class': 'form-control'}),
            'ssd_qty': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'smps': forms.Select(attrs={'class': 'form-control'}),
            'smps_status': forms.Select(attrs={'class': 'form-control'}),
            'motherboard': forms.Select(attrs={'class': 'form-control'}),
            'motherboard_status': forms.Select(attrs={'class': 'form-control'}),
        }

class ItemForm(forms.ModelForm):
    """
    A form for creating or updating an Item in the inventory.
    """
    class Meta:
        model = Item
        fields = [
            'name', 'serialno', 'make_and_models', 'processor', 'ram', 'ram_qty', 'hdd', 
            'hdd_qty', 'ssd', 'ssd_qty', 'smps', 'smps_status', 'motherboard', 'motherboard_status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'serialno': forms.TextInput(attrs={'class': 'form-control'}),
            'make_and_models': forms.TextInput(attrs={'class': 'form-control'}),
            
            # ForeignKey fields with select dropdowns
            'processor': forms.Select(attrs={'class': 'form-control'}),
            'ram': forms.Select(attrs={'class': 'form-control'}),
            'ram_qty': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'hdd': forms.Select(attrs={'class': 'form-control'}),
            'hdd_qty': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'ssd': forms.Select(attrs={'class': 'form-control'}),
            'ssd_qty': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'smps': forms.Select(attrs={'class': 'form-control'}),
            'smps_status': forms.Select(attrs={'class': 'form-control'}),
            'motherboard': forms.Select(attrs={'class': 'form-control'}),
            
            
            # Quantity fields (NumberInput with min validation)
            
            
            
            
            # Status fields as select dropdowns
            
            
        }
        labels = {
            'name': 'Item Name',
            'serialno': 'Serial Number',
            'make_and_models': 'Make and Model',
            'processor': 'Processor',
            'ram': 'RAM',
            'ram_qty': 'RAM Quantity',
            'hdd': 'HDD',
            'hdd_qty': 'HDD Quantity',
            'ssd': 'SSD',
            'ssd_qty': 'SSD Quantity',
            'smps': 'SMPS',
            'smps_status': 'SMPS Status',
            'motherboard': 'Motherboard',
            'motherboard_status': 'Motherboard Status',
        }


class RamForm(forms.ModelForm):
    """
    A form for creating or updating ram.
    """
    class Meta:
        model = Ram
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Ram Details',
                'aria-label': 'Ram Details'
            }),
        }
        labels = {
            'name': 'RAM',
        }

class HddForm(forms.ModelForm):
    """
    A form for creating or updating hdd.
    """
    class Meta:
        model = Hdd
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Hdd Details',
                'aria-label': 'Hdd Details'
            }),
        }
        labels = {
            'name': 'HDD',
        }

class ProcessorForm(forms.ModelForm):
    """
    A form for creating or updating Processor.
    """
    class Meta:
        model = Processor
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Processor Details',
                'aria-label': 'Processor Details'
            }),
        }
        labels = {
            'name': 'Processor',
        }

class SddForm(forms.ModelForm):
    """
    A form for creating or updating Sdd.
    """
    class Meta:
        model = Sdd
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Sdd name',
                'aria-label': 'Sdd name'
            }),
            'capacity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter capacity in GB',
                'aria-label': 'capacity in GB'
            }),
            'product code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ssd product code ',
                'aria-label': 'ssd product code'
            }),
        }
        labels = {
            'name': 'SSD',
        }

class M_2Form(forms.ModelForm):
    """
    A form for creating or updating M_2.
    """
    class Meta:
        model = M_2
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter M.2 name',
                'aria-label': 'M.2 name'
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter model number ',
                'aria-label': 'model number'
            }),
            'capacity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter capacity in GB',
                'aria-label': 'capacity in GB'
            }),
            'product code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter M.2 product code ',
                'aria-label': 'M.2 product code'
            }),
        }
        labels = {
            'name': 'M.2',
        }

class NvmeForm(forms.ModelForm):
    """
    A form for creating or updating M_2.
    """
    class Meta:
        model = Nvme
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Nvme name',
                'aria-label': 'Nvme name'
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter model number ',
                'aria-label': 'model number'
            }),
            'capacity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter capacity in GB',
                'aria-label': 'capacity in GB'
            }),
            'product code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Nvme product code ',
                'aria-label': 'Nvme product code'
            }),
        }
        labels = {
            'name': 'NVME',
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'item',
            'customer_name',
            'phone_number',
            'location',
            'date',
            'is_delivered'
        ]
        widgets = {
            'item': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select item',
            }),
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter customer name',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter delivery location',
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select delivery date and time',
                'type': 'datetime-local'
            }),
            'is_delivered': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'label': 'Mark as delivered',
            }),
        }
