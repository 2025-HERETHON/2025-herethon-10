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
        # return f"등기부등본 확인사항 (ID: {self.id})"
        return f"{self.user.name}'s Contract Checklist"

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

    # 이사 하루 전
    unplug_appliances = models.BooleanField(default=False, verbose_name="냉장고, 세탁기 미리 전원 차단하기")
    keep_valuables_separately = models.BooleanField(default=False, verbose_name="귀중품, 중요 서류는 따로 보관하기")
    check_new_home_password = models.BooleanField(default=False, verbose_name="새 집 열쇠, 도어락 비밀번호 재확인하기")
    confirm_moving_time = models.BooleanField(default=False, verbose_name="이사 업체와 이사 시작 확인하기")
    finish_trash_sorting = models.BooleanField(default=False, verbose_name="쓰레기 분리수거 및 집 정리 마무리하기")

    # 이사 당일
    check_truck_arrival_time = models.BooleanField(default=False, verbose_name="이사 차량 도착 시간 확인하기")
    take_photos_of_old_home = models.BooleanField(default=False, verbose_name="기존 집 상태 사진 찍어두기 (보증금 문제 대비)")

    # 새 집 점검하기
    check_leaks = models.BooleanField(default=False, verbose_name="누수 확인하기")
    check_power_outlets = models.BooleanField(default=False, verbose_name="콘센트 및 전기 확인하기")
    check_water_supply = models.BooleanField(default=False, verbose_name="수도 작동 확인하기")

    # 설치 기사 방문 체크하기
    check_appliance_installer = models.BooleanField(default=False, verbose_name="가전 설치 기사")
    check_internet_installer = models.BooleanField(default=False, verbose_name="인터넷 설치 기사")

    # 이사 후
    complete_address_registration = models.BooleanField(default=False, verbose_name="전입신고 완료하기 (동주민센터 또는 정부24)")
    change_address = models.BooleanField(default=False, verbose_name="주소 변경하기 (은행, 학교, 직장 등)")
    check_deposit_settlement = models.BooleanField(default=False, verbose_name="보증금 정산 확인하기")
    check_trash_disposal_rules = models.BooleanField(default=False, verbose_name="쓰레기 배출 규칙 확인하기")
    check_residence_insurance = models.BooleanField(default=False, verbose_name="거주지 화재보험, 전세보증금 보험 등 확인하기")

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.name}'s Moving Checklist"

    


#입주 체크리스트
class ResidencyChecklist(models.Model):
    checklist_group = models.ForeignKey('ChecklistGroup', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 기본 점검
    check_utilities = models.BooleanField(default=False, verbose_name="전기, 수도, 가스 정상 작동 재확인하기")
    check_heating = models.BooleanField(default=False, verbose_name="냉온수, 보일러, 샤워기 점검하기")
    set_doorlock_password = models.BooleanField(default=False, verbose_name="도어락 비밀번호 설정 및 강화하기")

    # 안전·보안 점검
    check_fire_detector = models.BooleanField(default=False, verbose_name="화재 감지기 및 가스차단기 확인하기")
    check_window_locks = models.BooleanField(default=False, verbose_name="창문, 현관문 잠금장치 점검하기")
    locate_circuit_breaker = models.BooleanField(default=False, verbose_name="전기차단기 위치 파악해두기")

    # 생활 정착
    check_recycling_days = models.BooleanField(default=False, verbose_name="분리수거 요일 및 분리수거장 확인하기")
    setup_wifi_appliances = models.BooleanField(default=False, verbose_name="와이파이, TV, 가전 설치 마무리하기")
    prepare_emergency_kit = models.BooleanField(default=False, verbose_name="응급약품 구비해두기")

    # 생활 필수품 보충하기
    prepare_laundry_detergent = models.BooleanField(default=False, verbose_name="세탁 세제 및 주방 세제")
    prepare_kitchen_supplies = models.BooleanField(default=False, verbose_name="키친타올 및 행주")
    prepare_toiletries = models.BooleanField(default=False, verbose_name="화장지 및 물티슈")
    prepare_garbage_bags = models.BooleanField(default=False, verbose_name="종량제봉투 (지역구 전용)")
    prepare_drinking_water = models.BooleanField(default=False, verbose_name="생수 또는 정수기")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Residency Checklist"

class CheckAll(models.Model):
    checklist_group = models.ForeignKey(ChecklistGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    contract_all = models.BooleanField(default=False)
    moving_all = models.BooleanField(default=False)
    residency_all = models.BooleanField(default=False)
    
    
class SavedPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kakao_id = models.CharField(max_length=50)
    category_group_code = models.CharField(max_length=10)
    place_name = models.CharField(max_length=255)
    place_url = models.URLField()
    road_address_name = models.CharField(max_length=255)
    x = models.CharField(max_length=30)
    y = models.CharField(max_length=30)

    class Meta:
        unique_together = ('user', 'kakao_id')  # 중복 저장 방지