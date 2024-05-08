# Generated by Django 5.0.2 on 2024-04-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content_type',
            field=models.CharField(choices=[('t', 'text/plain'), ('m', 'text/markdown'), ('b', 'application/base64'), ('p', 'image/png;base64'), ('j', 'image/jpeg;base64')], default='t', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_type',
            field=models.CharField(choices=[('t', 'text/plain'), ('m', 'text/markdown'), ('b', 'application/base64'), ('p', 'image/png;base64'), ('j', 'image/jpeg;base64')], max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='extern_id',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]