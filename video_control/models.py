import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from multiselectfield import MultiSelectField

from .utils import Filters, Woman_or_man, resized_every_photo


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """ Create and save a regular User with the given email and password. """
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """ Create and save a SuperUser with the given email and password. """
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ Create fields for user model and install a manager."""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    slug = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class Profile(models.Model):
    """ Create fields for profile model. """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=False)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="profile_photo/",
                               default="profile_photo/default.png")
    sex = models.CharField(max_length=10, choices=Woman_or_man.get_woman_or_man())
    telegram = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.name


class Video(models.Model):
    """ Create fields for video model. """
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = MultiSelectField(choices=Filters.get_filter_types())
    video = models.FileField(upload_to='videos/', max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.thumbnail = resized_every_photo(self.thumbnail, self.title)
        super().save(*args, **kwargs)


class Photo(models.Model):
    """ Create fields for photo model. """
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = MultiSelectField(choices=Filters.get_filter_types())
    photo = models.ImageField(upload_to='photos/')
    resized_photo = models.ImageField(upload_to='resized_photos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            self.resized_photo = resized_every_photo(self.photo, self.name)
            if self.resized_photo is not None:
                super().save(*args, **kwargs)
