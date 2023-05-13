from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel, UUIDModel
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(UUIDModel, TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    name = models.CharField(null=True, max_length=255, verbose_name='Nome')
    email = models.EmailField(max_length=255, unique=True, verbose_name='E-mail')
    is_staff = models.BooleanField(default=False, verbose_name='É da equipe')
    is_superuser = models.BooleanField(default=False, verbose_name='É super usuário?')
    is_active = models.BooleanField(default=True, verbose_name='Está ativo?')
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class LogAcess(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    browser = models.CharField(null=True, max_length=255, verbose_name='navegador do usuario')
    device = models.CharField(null=True, max_length=255, verbose_name='dispositivo do usuario')
    ip_address = models.CharField(null=True, max_length=255, verbose_name='ip do usuario')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Data de criação')

    class Meta:
        verbose_name = 'Acesso'
        verbose_name_plural = 'Acessos'
        
class Product(UUIDModel, TimeStampedModel):
    class ProductName(models.TextChoices):
        ADHEART = 'ADHEART', 'Adheart'
        ADSPY = 'ADSPY', 'Adspy'
        ADVAULT = 'ADVAULT', 'Advault'
        PIPIADS = 'PIPIADS', 'Pipiads'
        BISPY = 'BISPY', 'Bispy'
        ADHEART2 = 'ADHEART2','Adheart2'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    name = models.CharField(max_length=100, choices=ProductName.choices, verbose_name='Nome')
    expires = models.DateField(null=True, verbose_name='Expira em')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'



class AllCookies(UUIDModel, TimeStampedModel):
    cookie = models.CharField(max_length=255, verbose_name='cookies gerados')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Data de criação')

    class Meta:
        verbose_name = 'cookie'
        verbose_name_plural = 'cookies'
        ordering = ["-pk"]