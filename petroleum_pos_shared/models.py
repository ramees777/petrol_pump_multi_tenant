from django.db import models

# Create your models here.
# from django.contrib.auth.hashers import make_password
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# from django.utils.translation import ugettext_lazy as _
# import os

# from rest_framework import status


# # Create your models here.




# class AccountManager(BaseUserManager):
#     def create_user(self,email,password):
#         if not email:
#             raise ValueError('User must have an email address')
#         # if not username:
#         #     raise ValueError('User must have a username')
#         user = self.model(
#             email = self.normalize_email(email),
#             # fullname = fullname,
#             # phone = phone,
#             # username = username
#         )
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,email,password):
#         user = self.create_user(
#             email = self.normalize_email(email),
#             # username = username,
#             # phone=phone,
#             password=password,
#             # fullname=fullname
#         )

#         user.is_staff = True
#         user.is_admin = True
#         user.is_super_admin = True

#         user.save(using=self._db)
#         return user


# class Account(AbstractBaseUser):
#     # fullname = models.CharField(max_length=30,blank=True,null=True)
#     # username = models.CharField(max_length=30,unique=True)
#     # phone = models.CharField(max_length=15,unique=True)
#     email = models.EmailField(max_length=100,unique=True)

#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_owner = models.BooleanField(default=False)
#     is_super_admin = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'

#     # REQUIRED_FIELDS = ['phone']

#     objects = AccountManager()
    
#     class Meta:
#         db_table = 'account'

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin
    
#     def has_module_perms(self, add_label):
#         return True

# def get_upload_path(instance, filename):
#     return os.path.join(
#         "%s" % instance.account.email, filename)
    
# class Company(models.Model):
#     account = models.OneToOneField(
#         Account, on_delete=models.CASCADE, related_name='account')
#     en_name = models.CharField(max_length=30)
#     ar_name = models.CharField(max_length=30)
#     en_place = models.CharField(max_length=30)
#     ar_place = models.CharField(max_length=30)
#     en_district = models.CharField(max_length=30)
#     ar_district = models.CharField(max_length=30)
#     cr_no = models.CharField(max_length=15)
#     vat_no = models.CharField(max_length=15)
#     lan_no = models.CharField(max_length=15)
#     logo = models.ImageField(
#         _('logo'), upload_to=get_upload_path, null=True)
#     status = models.BooleanField(default=True)
#     phone = models.CharField(max_length=15,unique=True)
    
    
#     class Meta:
#         db_table = 'company'
        
#     def __str__(self):
#         return self.en_name

# class Employee(models.Model):
#     account = models.OneToOneField(
#         Account, on_delete=models.CASCADE, related_name='employee')
#     company= models.ForeignKey(Company, on_delete=models.CASCADE,
#                             null=True, related_name='company')
#     name = models.CharField(max_length=30, unique=True)
#     phone = models.CharField(max_length=15,unique=True)
    
#     def __str__(self):
#         return self.account.email
    
#     class Meta:
#         db_table = 'employee'
    
