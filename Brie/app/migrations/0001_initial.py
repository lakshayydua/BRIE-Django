# Generated by Django 2.0.3 on 2018-03-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('isbn', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=500)),
                ('language', models.CharField(max_length=200)),
                ('publication', models.CharField(max_length=1000)),
                ('pages', models.IntegerField()),
                ('pub_date', models.IntegerField()),
                ('pub_month', models.IntegerField()),
                ('pub_year', models.IntegerField()),
                ('book_url', models.CharField(max_length=500)),
                ('img_url', models.CharField(max_length=500)),
                ('google_price', models.CharField(max_length=100)),
                ('barnes_price', models.CharField(max_length=100)),
                ('indie_price', models.CharField(max_length=100)),
                ('amazon_price', models.CharField(blank=True, max_length=100)),
                ('r1', models.CharField(blank=True, max_length=1000)),
                ('r2', models.CharField(blank=True, max_length=1000)),
                ('r3', models.CharField(blank=True, max_length=1000)),
                ('r4', models.CharField(blank=True, max_length=1000)),
                ('r5', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
