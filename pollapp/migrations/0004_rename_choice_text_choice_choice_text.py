# Generated by Django 5.0.7 on 2024-08-05 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0003_alter_question_question_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_Text',
            new_name='choice_text',
        ),
    ]
