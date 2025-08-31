from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, mobile, aadhar, address, role, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            mobile=mobile,
            aadhar=aadhar,
            address=address,
            role=role,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, mobile, aadhar, address, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(
            email=email,
            name=name,
            mobile=mobile,
            aadhar=aadhar,
            address=address,
            role='admin',
            password=password,
            **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('staff_admin', 'Staff Admin'),
    ]

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    aadhar = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    images = models.ImageField(upload_to='accounts/images/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    issuedate = models.DateField(null=True, blank=True)
    valid_till = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile', 'aadhar', 'address']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.name} ({self.role})"
