# Generated by Django 5.0.7 on 2024-11-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0004_book_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Biography', 'Biography'), ('Drama', 'Drama'), ('Romantic', 'Romantic'), ('Comedy', 'Comedy'), ('War', 'War'), ('Gangster', 'Gangster'), ('Horror', 'Horror'), ('Finance', 'Finance')], max_length=50),
        ),
    ]
