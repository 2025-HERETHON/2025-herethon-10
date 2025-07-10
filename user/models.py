from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# 로그인 처리 위한 유저 매니저
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수 항목입니다.')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, name, password, **extra_fields)

# 사용자 기본 정보 (user_profile)
class User(AbstractBaseUser):
    GENDER_CHOICES = [('여성', '여성'), ('남성', '남성')]
    JOB_CHOICES = [
        ('대학생', '대학생'),
        ('취준생', '취준생'),
        ('직장인', '직장인'),
        ('프리랜서', '프리랜서'),
        ('기타', '기타'),
    ]
    profile_image = models.ImageField(upload_to='profile_images/')
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True)
    job = models.CharField(max_length=20, choices=JOB_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

# 독립 계획 정보 (user_independenceplan)
class IndependencePlan(models.Model):
    
    ROOMATE_CHOICES = [('동거인 없음', '동거인 없음'), ('동거인 있음', '동거인 있음')]
    RESIDENCE_CHOICES = [('원룸', '원룸'), ('기숙사', '기숙사'), ('쉐어하우스', '쉐어하우스'), ('아직 정하지 못했어요', '아직 정하지 못했어요'),]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # area_si = models.CharField(max_length=20, choices=AREA_CHOICES, null=True, blank=True)
    # area_sgg = models.CharField(max_length=50, null=True, blank=True)
    area_si = models.CharField(max_length=20)   # 시/도
    area_sgg = models.CharField(max_length=20)  # 시/군/구
    # area_sgg 값은 시/도(area_si) 선택에 따라 프론트에서 동적 생성 필요
    
    max_rent_budget = models.IntegerField()
    max_manage_budget = models.IntegerField()
    max_deposit_budget = models.IntegerField()
    has_roomate = models.CharField(max_length=20, choices=ROOMATE_CHOICES)
    roomate_count = models.IntegerField(null=True, blank=True)
    residence_type = models.CharField(max_length=20, choices=RESIDENCE_CHOICES, null=True, blank=True)
    move_date = models.CharField(max_length=7)  # YYYY-MM 형식

    def __str__(self):
        return f"{self.user.name}의 독립 계획"