# Generated by Django 4.0 on 2022-02-17 10:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0003_alter_note_creation_date_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-created'], 'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.RemoveField(
            model_name='note',
            name='creation_date_time',
        ),
        migrations.AddField(
            model_name='note',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created on'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Created by'),
        ),
    ]