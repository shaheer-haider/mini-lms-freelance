# Generated by Django 4.0.4 on 2022-07-04 19:05

import ckeditor.fields
import classroom.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assignment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('icon', models.CharField(default='article', max_length=100, verbose_name='Icon')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('picture', models.ImageField(upload_to=classroom.models.user_directory_path)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('syllabus', ckeditor.fields.RichTextField()),
                ('amount', models.CharField(default=0, max_length=55)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.category')),
                ('enrolled', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('graded', 'Graded')], default='pending', max_length=10, verbose_name='Status')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.course')),
                ('graded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.submission')),
            ],
        ),
    ]
