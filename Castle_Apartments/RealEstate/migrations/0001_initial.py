# Generated by Django 2.2.1 on 2019-05-07 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=99)),
                ('zip_code', models.CharField(max_length=3)),
                ('size', models.CharField(max_length=10)),
                ('bedrooms', models.CharField(max_length=2)),
                ('type', models.CharField(max_length=99)),
                ('price', models.CharField(max_length=999)),
                ('on_sale', models.BooleanField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Signup.Members')),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=9999)),
                ('real_estate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RealEstate.RealEstates')),
            ],
        ),
    ]
