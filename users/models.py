from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk:
            raise Exception("Group name cannot be updated after creation.")
        super().save(*args, **kwargs)

class UserProfileManager(BaseUserManager):
    def create_user(self, full_name, mobile_number, joining_date, salary, address, dob,
                    role, documents, bank_account, password=None, **extra_fields):
        if not mobile_number:
            raise ValueError("Mobile number is required.")
        user = self.model(
            full_name=full_name,
            mobile_number=mobile_number,
            joining_date=joining_date,
            salary=salary,
            address=address,
            dob=dob,
            role=role,
            documents=documents,
            bank_account=bank_account,
            **extra_fields
        )
        user.set_password(password or f"{full_name[:4].lower()}{mobile_number[-4:]}")
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(full_name="Admin", mobile_number=mobile_number,
                                joining_date="2000-01-01", salary=0, address="N/A",
                                dob="2000-01-01", role=None, documents=None,
                                bank_account={}, password=password, **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, unique=True)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    dob = models.DateField()
    role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    documents = models.FileField(upload_to='documents/', blank=True, null=True)
    bank_account = models.JSONField()
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []
