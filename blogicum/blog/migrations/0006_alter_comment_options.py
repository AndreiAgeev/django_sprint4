# Generated by Django 3.2.16 on 2024-05-03 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_at',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]