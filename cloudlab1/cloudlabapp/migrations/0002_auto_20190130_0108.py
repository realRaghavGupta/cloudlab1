# Generated by Django 2.1.5 on 2019-01-30 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudlabapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('author_name', models.CharField(max_length=20)),
                ('publish_year', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]