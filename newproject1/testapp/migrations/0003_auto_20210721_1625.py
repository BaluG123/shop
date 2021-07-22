# Generated by Django 3.2.3 on 2021-07-21 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_items1'),
    ]

    operations = [
        migrations.CreateModel(
            name='items2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('image1', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link', models.CharField(max_length=10000)),
                ('price', models.IntegerField()),
                ('off_price', models.IntegerField()),
                ('off_p', models.IntegerField()),
                ('site', models.CharField(choices=[('amazon', 'Amazon'), ('flifkart', 'Flifkart'), ('ajio', 'Ajio')], default='amazon', max_length=100)),
                ('company', models.CharField(choices=[('puma', 'Puma'), ('adidas', 'Adidas'), ('nike', 'Nike'), ('h&m', 'H&M')], default='null', max_length=100)),
                ('item2', models.CharField(choices=[('t-shirt', 'T-short'), ('shirt', 'Shirt'), ('pant', 'Pant'), ('shoe', 'Shoe')], default='null', max_length=100)),
                ('item_name2', models.CharField(max_length=100)),
                ('image2', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link2', models.CharField(max_length=10000)),
                ('price2', models.IntegerField()),
                ('off_price2', models.IntegerField()),
                ('off_p2', models.IntegerField()),
                ('site2', models.CharField(choices=[('amazon', 'Amazon'), ('flifkart', 'Flifkart'), ('ajio', 'Ajio')], default='amazon', max_length=100)),
                ('company2', models.CharField(choices=[('puma', 'Puma'), ('adidas', 'Adidas'), ('nike', 'Nike'), ('h&m', 'H&M')], default='null', max_length=100)),
                ('item_name3', models.CharField(max_length=100)),
                ('image3', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link3', models.CharField(max_length=10000)),
                ('price3', models.IntegerField()),
                ('off_price3', models.IntegerField()),
                ('off_p3', models.IntegerField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('site3', models.CharField(choices=[('amazon', 'Amazon'), ('flifkart', 'Flifkart'), ('ajio', 'Ajio')], default='amazon', max_length=100)),
                ('company3', models.CharField(choices=[('puma', 'Puma'), ('adidas', 'Adidas'), ('nike', 'Nike'), ('h&m', 'H&M')], default='null', max_length=100)),
                ('item3', models.CharField(choices=[('t-shirt', 'T-short'), ('shirt', 'Shirt'), ('pant', 'Pant'), ('shoe', 'Shoe')], default='null', max_length=100)),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
        migrations.AlterField(
            model_name='items1',
            name='item',
            field=models.CharField(choices=[('t-shirt', 'T-shirt'), ('shirt', 'Shirt'), ('pant', 'Pant'), ('shoe', 'Shoe')], default='null', max_length=100),
        ),
    ]
