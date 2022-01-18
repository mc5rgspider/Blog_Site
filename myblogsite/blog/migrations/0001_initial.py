# Generated by Django 3.2.5 on 2022-01-13 02:19
from django.db import migrations, models
#Model defines Migration
#No dependencies to other migrations
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            #name of model
            name=‘Blog’,
            #Add fields for id, title, description and date
            fields=[
                (‘id’, models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=‘ID’)),
                (‘title’, models.CharField(max_length=150)),
                (‘description’, models.TextField()),
                (‘date’, models.DateField()),
            ],
        ),
    ]