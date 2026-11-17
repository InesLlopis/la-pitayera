from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
# UD5.1.b
class MyUserManager(BaseUserManager):
    def create_user(
        self, email, password=None, username=None
    ):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=256, null=True, blank=True, verbose_name='Nombre de usuario')
    email = models.EmailField(unique=True)
    create_date = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    
    objects = MyUserManager()