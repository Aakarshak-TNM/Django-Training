# Generated by Django 3.2.24 on 2024-02-21 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial_manual'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='standard_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.standard'),
        ),
    ]
