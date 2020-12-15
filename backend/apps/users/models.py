from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):

    # 일반사용자 생성
    def create_user(self, email, username, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(            
            email = self.normalize_email(email),            
            username = username,
            date_of_birth = date_of_birth,
            date_joined = timezone.now(),
            is_superuser = 0,
            is_staff = 0,
            is_active = 1
        )

        # django의 비밀번호 생성 메소드
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 생성
    def create_superuser(self, email, password, username, date_of_birth):
        user = self.create_user(
            email = self.normalize_email(email),            
            password = password,
            username = username,
            date_of_birth = date_of_birth
        )

        user.is_superuser = 1
        user.is_staff = 1
        user.save(using=self._db)

        return user
        
class User(AbstractBaseUser):
    email = models.CharField(unique=True, max_length=254)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)    
    is_superuser = models.IntegerField()    
    date_of_birth = models.DateTimeField()
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    objects = UserManager()

    # 사용자 ID로 사용할 필드
    USERNAME_FIELD = 'email'
    
    # 필수입력 필드
    REQUIRED_FIELDS = ['username', 'date_of_birth']

    # 관리자 페이지 등과 같은 django에서 제공하는 패키지의 회원정보 모델을 사용하여
    # 접근 가능 여부에 대한 값을 반환하는 메소드 - True로 해야지만 관리자 계정을 생성하고 관리자 페이지를 사용할 수 있다.
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email        

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자 목록"      

