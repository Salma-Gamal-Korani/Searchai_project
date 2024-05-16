# Generated by Django 5.0.3 on 2024-05-15 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_rename_user_id_book_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='content',
            new_name='answerContent',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='content',
            new_name='questionContent',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
