# Generated by Django 2.0.6 on 2020-06-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_job', models.CharField(max_length=50)),
                ('rating', models.FloatField(default=0.0)),
                ('customer_image', models.ImageField(upload_to='customer_image')),
            ],
        ),
    ]