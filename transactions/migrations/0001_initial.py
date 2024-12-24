# Generated by Django 4.2.6 on 2024-08-08 17:03

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Sale Date')),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('discount_percentage', models.FloatField(default=0.0)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('amount_change', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('customer', models.ForeignKey(db_column='customer', on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.customer')),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('total_detail', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.ForeignKey(db_column='item', on_delete=django.db.models.deletion.DO_NOTHING, to='store.item')),
                ('sale', models.ForeignKey(db_column='sale', on_delete=django.db.models.deletion.CASCADE, related_name='saledetail_set', to='transactions.sale')),
            ],
            options={
                'verbose_name': 'Sale Detail',
                'verbose_name_plural': 'Sale Details',
                'db_table': 'sale_details',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='vendor', unique=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField(blank=True, null=True, verbose_name='Delivery Date')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('delivery_status', models.CharField(choices=[('P', 'Pending'), ('S', 'Successful')], default='P', max_length=1, verbose_name='Delivery Status')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Price per item (Ksh)')),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='accounts.vendor')),
            ],
            options={
                'ordering': ['order_date'],
            },
        ),
    ]