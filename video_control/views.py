import math

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, UpdateView

from .forms import RegistrationForm, LoginForm, UpdatePasswordForm, UpdateProfileForm
from .models import Video, Photo, Profile, User


class ShowVideos(ListView):
    """ Show all videos. """
    model = Video
    template_name = 'video_control/videos.html'
    context_object_name = 'videos'
    paginate_by = 9

    def get_queryset(self):
        return Video.objects.all().order_by('-created_at')


class ShowPhotos(ListView):
    """ Show all photos. """
    model = Photo
    template_name = 'video_control/photos.html'
    context_object_name = 'photos'
    paginate_by = 9

    def get_queryset(self):
        return Photo.objects.all().order_by('-created_at')


class DetailPhoto(DetailView):
    """ Show one photo. """
    model = Photo
    template_name = 'video_control/detail_photo.html'


class DetailVideo(DetailView):
    """ Show one video. """
    model = Video
    template_name = 'video_control/detail_video.html'


class Registration(FormView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = '/login/'
    success_message = 'Вы успешно зарегистрировались!'

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)


class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    slug_field = 'user__slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        """ Связывает модель Profile с моделью User, при помощи slug. """
        try:
            return self.model.objects.get(user__slug=self.kwargs['slug'])
        except self.model.DoesNotExist:
            user = User.objects.get(slug=self.kwargs['slug'])
            profile = self.model.objects.create(user=user)
            return profile


class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    """
    Изменение пароля пользователя
    """
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('photo_list')
    template_name = 'registration/change_password.html'
    success_message = 'Ваш пароль был успешно изменён!'


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'registration/change_profile.html'

    def get_object(self, queryset=None):
        return self.model.objects.get(user__slug=self.kwargs['slug'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        profile = self.get_object()
        profile.avatar = form.cleaned_data['avatar']
        profile.age = form.cleaned_data['age']
        profile.sex = form.cleaned_data['sex']
        profile.bio = form.cleaned_data['bio']
        profile.telegram = form.cleaned_data['telegram']
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.kwargs['slug']})


class RandomHomeList(ListView):
    template_name = 'home.html'
    context_object_name = 'random_content'
    paginate_by = 6

    def get_queryset(self):
        random_video = list(Video.objects.all().order_by('?')[:4])
        random_photo = list(Photo.objects.all().order_by('?')[:4])
        return random_video + random_photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        half_len_get_queryset = math.ceil(len(self.get_queryset()) / 2)
        context['random_video'] = self.get_queryset()[:half_len_get_queryset]
        context['random_photo'] = self.get_queryset()[half_len_get_queryset:]
        return context


