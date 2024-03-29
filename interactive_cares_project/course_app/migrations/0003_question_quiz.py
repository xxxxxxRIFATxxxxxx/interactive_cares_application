# Generated by Django 3.1.7 on 2021-04-09 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_auto_20210409_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.course')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.module')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_1', models.TextField(blank=True, null=True)),
                ('option_2', models.TextField(blank=True, null=True)),
                ('option_3', models.TextField(blank=True, null=True)),
                ('option_4', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.course')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.module')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.quiz')),
            ],
        ),
    ]
