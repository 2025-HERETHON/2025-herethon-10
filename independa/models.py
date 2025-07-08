from django.db import models
from user.models import User
# Create your models here.

class ChecklistGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

#계약 체크리스트
class ContractChecklist(models.Model):
    checklist_group = models.ForeignKey(ChecklistGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #<계약 준비>
    #예산 설정하기
    min_rent_budget = models.IntegerField()
    min_manage_budget = models.IntegerField()
    min_deposit_budget = models.IntegerField()
    
    #<계약 전>
    #등기부등본 확인하기
    owner_verified = models.BooleanField("집주인 신원 및 소유권 확인", default=False)
    mortgage_verified = models.BooleanField("선순위 채권(근저당) 유무 확인", default=False)
    illegal_building_verified = models.BooleanField("위법 건축물 여부 확인", default=False)

    #주변환경 확인하기
    room_condition = models.OneToOneField('RoomCondition', on_delete=models.CASCADE, null=True, blank=True)
    deposit_insurance = models.BooleanField("전세 보증금 반환 보증 가입", default=False)
    
    #여성 전용 공간 확인하기
    women_safety_preference = models.OneToOneField('WomenSafetyPreference', on_delete=models.CASCADE, null=True, blank=True)
    
    #<계약서 작성>
    contract_write = models.BooleanField(default=False, verbose_name="계약서 작성하기")
    contract_copy_keep = models.BooleanField(default=False, verbose_name="계약서 사본 보관하기")
    deposit_transfer = models.BooleanField(default=False, verbose_name="계약금 및 보증금 이체하기")
    cost_receipt_keep = models.BooleanField(default=False, verbose_name="계약관련 비용 이체 영수증 보관하기")
    move_in_report = models.BooleanField(default=False, verbose_name="전입신고 하기")
    receive_move_in_date = models.BooleanField(default=False, verbose_name="입주 확정일자 받기")
    change_address = models.BooleanField(default=False, verbose_name="주소 이전하기")
    transfer_public_utilities = models.BooleanField(default=False, verbose_name="공과금 명의 이전하기")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"등기부등본 확인사항 (ID: {self.id})"

class RoomCondition(models.Model):
    noise = models.BooleanField("주변 소음", default=False)                   # 주변 소음
    infrastructure = models.BooleanField("주변 인프라", default=False)          # 주변 인프라
    safety = models.BooleanField("주변 안전도", default=False)                  # 주변 안전도
    no_leakage = models.BooleanField("누수 없음", default=False)              # 누수 없음
    no_mold = models.BooleanField("곰팡이 없음", default=False)                 # 곰팡이 없음
    bathroom_drainage = models.BooleanField("화장실 물빠짐", default=False)       # 화장실 물빠짐
    windows_doors_work = models.BooleanField("창문 및 방화문 작동", default=False)      # 창문 및 방화문 작동
    wallpaper_flooring = models.BooleanField("도배 및 장판 상태", default=False)      # 도배 및 장판 상태
    water_condition = models.BooleanField("수도 상태", default=False)         # 수도 상태
    boiler_condition = models.BooleanField("보일러 상태", default=False)        # 보일러 상태
    lighting = models.BooleanField("채광", default=False)                # 채광
    basic_options = models.BooleanField("기본 옵션", default=False)           # 기본 옵션

class WomenSafetyPreference(models.Model):
    female_only_room = models.BooleanField("여성 전용 원룸 또는 여성 전용 층", default=False)
    female_parking = models.BooleanField("여성 전용 주차장", default=False)
    female_gym = models.BooleanField("여성 전용 헬스 시설", default=False)
    female_study_cafe = models.BooleanField("여성 전용 스터디카페", default=False)
    safe_night_street = models.BooleanField("여성 안심 귀갓길", default=False)


#이사 체크리스트
class MovingChecklist(models.Model):
    checklist_group = models.ForeignKey(ChecklistGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # moving_date = models.DateField(null=True, blank=True)
    # moving_company = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


#입주 체크리스트
class ResidencyChecklist(models.Model):
    checklist_group = models.ForeignKey(ChecklistGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

class CheckAll(models.Model):
    checklist_group = models.ForeignKey(ChecklistGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    contract_all = models.BooleanField(default=False)
    moving_all = models.BooleanField(default=False)
    residency_all = models.BooleanField(default=False)