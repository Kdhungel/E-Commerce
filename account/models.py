from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class AccountManager(BaseUserManager):

    def createUser(self, fName, lName, userName, email, password= None):
         if not email:
             raise ValueError('Email Address field cannot be empty')

         if not userName:
             raise ValueError('Username field cannot be empty')

         user = self.model(
             email=self.normalize_email(email),
             userName=userName,
             fName=fName,
             lName=lName,
         )
         user.set_password(password)
         user.save(using=self._db)
         return user

    def create_superuser(self, fName, lName, userName, email, password):
        user = self.createUser(
        email=self.normalize_email(email),
        userName=userName,
        password=password,
        fName=fName,
        lName=lName,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phoneNumber = models.CharField(max_length=14, unique=True)
    password = models.CharField(max_length=100)

    #required for custom user model
    dateJoined = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)

    #snake case mandatory
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userName', 'fName', 'lName']

    objects = AccountManager()


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
