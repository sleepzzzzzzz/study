# Generated by Django 3.2.7 on 2021-09-16 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='addon',
            field=models.ManyToManyField(to='catalog.Product'),
        ),
        migrations.AlterField(
            model_name='addon',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category'),
        ),
    ]