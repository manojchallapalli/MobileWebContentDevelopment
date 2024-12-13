# Generated by Django 3.1.4 on 2021-05-02 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210502_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='service',
            field=models.CharField(choices=[('PAINTING', 'PAINTING'), ('CARPENTERING', 'CARPENTERING'), ('HOUSE SHIFTING', 'HOUSE SHIFTING'), ('FOOD CATERING', 'FOOD CATERING'), ('LAUNDRY/DRY WASH', 'LAUNDRY/DRY WASH'), ('PLUMBERING', 'PLUMBERING'), ('CONSTRUCTION', 'CONSTRUCTION'), ('MECHANICS', 'MECHANICS'), ('INTERIOR DESIGNING', 'INTERIOR DESIGNING'), ('TECHNICIANS', 'TECHNICIANS'), ('PRINTING', 'PRINTING'), ('UNISEX PARLOR', 'UNISEX PARLOR'), ('OTHER', 'OTHER')], max_length=150),
        ),
    ]
