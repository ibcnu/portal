from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    # PermissionManager,
    # Permission,
    # GroupManager,
    # Group,
    # UserManager,
)


class UserManager(BaseUserManager):
    # def create_user(self, fullname, email, password=None):
    def create_user(self, email, fullname, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.fullname = fullname
        user.staff = False
        user.admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_staffuser(self, fullname, email, password):
    def create_staffuser(self, email, fullname, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            # fullname,
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    # def create_superuser(self, fullname, email, password):
    def create_superuser(self, email, fullname, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            # fullname,
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    fullname = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []  # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
