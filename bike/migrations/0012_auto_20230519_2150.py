# Generated by Django 3.0.7 on 2023-05-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0011_auto_20230519_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='state',
            field=models.CharField(choices=[('BA', 'Bagmati'), ('GA', 'Gandaki'), ('SP', 'Sudhurpaschim'), ('LU', 'Lumbini'), ('KA', 'Karnali'), ('MD', 'Madhesh'), ('P1', 'Province 1')], max_length=100),
        ),
    ]
