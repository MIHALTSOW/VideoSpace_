# Generated by Django 5.1.1 on 2024-10-16 16:47

import django.db.models.deletion
import multiselectfield.db.fields
import uuid
import video_control.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('animals & pets', 'animals & pets'), ('anime', 'anime'), ('art & design', 'art & design'), ('auto & technique', 'auto & technique'), ('blogging', 'blogging'), ('cartoons', 'cartoons'), ('celebrity', 'celebrity'), ('dance', 'dance'), ('fashion & beauty', 'fashion & beauty'), ('food & kitchen', 'food & kitchen'), ('gaming', 'gaming'), ('live pictures', 'live pictures'), ('mashup', 'mashup'), ('memes', 'memes'), ('movies & TV', 'movies & TV'), ('music', 'music'), ('nature & travel', 'nature & travel'), ('science & technology', 'science & technology'), ('sports', 'sports'), ('stand-up & Jokes', 'stand-up & Jokes')], max_length=229)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('animals & pets', 'animals & pets'), ('anime', 'anime'), ('art & design', 'art & design'), ('auto & technique', 'auto & technique'), ('blogging', 'blogging'), ('cartoons', 'cartoons'), ('celebrity', 'celebrity'), ('dance', 'dance'), ('fashion & beauty', 'fashion & beauty'), ('food & kitchen', 'food & kitchen'), ('gaming', 'gaming'), ('live pictures', 'live pictures'), ('mashup', 'mashup'), ('memes', 'memes'), ('movies & TV', 'movies & TV'), ('music', 'music'), ('nature & travel', 'nature & travel'), ('science & technology', 'science & technology'), ('sports', 'sports'), ('stand-up & Jokes', 'stand-up & Jokes')], max_length=229)),
                ('video', models.FileField(upload_to='videos/')),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', video_control.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, default='profile_photo/default.png', null=True, upload_to='profile_photo/')),
                ('sex', multiselectfield.db.fields.MultiSelectField(choices=[('Man', 'Man'), ('Woman', 'Woman')], max_length=9)),
                ('telegram', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
