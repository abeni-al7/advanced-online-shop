# Generated by Django 5.0.12 on 2025-02-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
