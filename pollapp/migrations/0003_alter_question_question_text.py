# Generated by Django 5.0.7 on 2024-08-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0002_testing1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=300),
        ),
    ]
