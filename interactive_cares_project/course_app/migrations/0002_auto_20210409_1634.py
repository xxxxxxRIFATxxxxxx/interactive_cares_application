# Generated by Django 3.1.7 on 2021-04-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='intro_video_embed_tag',
            new_name='intro_video_embed_src_link',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='video_embed_tag',
            new_name='video_embed_src_link',
        ),
        migrations.AlterField(
            model_name='course',
            name='material_files_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='support_group_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
