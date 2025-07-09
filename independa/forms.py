from django import forms
from .models import ContractChecklist, ResidencyChecklist, RoomCondition, WomenSafetyPreference, MovingChecklist

class ContractChecklistForm(forms.ModelForm):
    # RoomCondition 필드를 직접 폼에 추가
    noise = forms.BooleanField(label="주변 소음", required=False)
    infrastructure = forms.BooleanField(label="주변 인프라", required=False)
    safety = forms.BooleanField(label="주변 안전도", required=False)
    no_leakage = forms.BooleanField(label="누수 없음", required=False)
    no_mold = forms.BooleanField(label="곰팡이 없음", required=False)
    bathroom_drainage = forms.BooleanField(label="화장실 물빠짐", required=False)
    windows_doors_work = forms.BooleanField(label="창문 및 방화문 작동", required=False)
    wallpaper_flooring = forms.BooleanField(label="도배 및 장판 상태", required=False)
    water_condition = forms.BooleanField(label="수도 상태", required=False)
    boiler_condition = forms.BooleanField(label="보일러 상태", required=False)
    lighting = forms.BooleanField(label="채광", required=False)
    basic_options = forms.BooleanField(label="기본 옵션", required=False)

    # WomenSafetyPreference 필드 직접 추가
    female_only_room = forms.BooleanField(label="여성 전용 원룸 또는 여성 전용 층", required=False)
    female_parking = forms.BooleanField(label="여성 전용 주차장", required=False)
    female_gym = forms.BooleanField(label="여성 전용 헬스 시설", required=False)
    female_study_cafe = forms.BooleanField(label="여성 전용 스터디카페", required=False)
    safe_night_street = forms.BooleanField(label="여성 안심 귀갓길", required=False)

    class Meta:
        model = ContractChecklist
        exclude = ['checklist_group', 'user', 'created_at', 'updated_at', 'room_condition', 'women_safety_preference']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # FK 인스턴스가 있으면 초기값 세팅
        if self.instance.pk:
            rc = self.instance.room_condition
            if rc:
                self.fields['noise'].initial = rc.noise
                self.fields['infrastructure'].initial = rc.infrastructure
                self.fields['safety'].initial = rc.safety
                self.fields['no_leakage'].initial = rc.no_leakage
                self.fields['no_mold'].initial = rc.no_mold
                self.fields['bathroom_drainage'].initial = rc.bathroom_drainage
                self.fields['windows_doors_work'].initial = rc.windows_doors_work
                self.fields['wallpaper_flooring'].initial = rc.wallpaper_flooring
                self.fields['water_condition'].initial = rc.water_condition
                self.fields['boiler_condition'].initial = rc.boiler_condition
                self.fields['lighting'].initial = rc.lighting
                self.fields['basic_options'].initial = rc.basic_options

            ws = self.instance.women_safety_preference
            if ws:
                self.fields['female_only_room'].initial = ws.female_only_room
                self.fields['female_parking'].initial = ws.female_parking
                self.fields['female_gym'].initial = ws.female_gym
                self.fields['female_study_cafe'].initial = ws.female_study_cafe
                self.fields['safe_night_street'].initial = ws.safe_night_street

    def save(self, commit=True):
        checklist = super().save(commit=False)

        # RoomCondition 저장 처리
        rc = checklist.room_condition or RoomCondition()
        rc.noise = self.cleaned_data['noise']
        rc.infrastructure = self.cleaned_data['infrastructure']
        rc.safety = self.cleaned_data['safety']
        rc.no_leakage = self.cleaned_data['no_leakage']
        rc.no_mold = self.cleaned_data['no_mold']
        rc.bathroom_drainage = self.cleaned_data['bathroom_drainage']
        rc.windows_doors_work = self.cleaned_data['windows_doors_work']
        rc.wallpaper_flooring = self.cleaned_data['wallpaper_flooring']
        rc.water_condition = self.cleaned_data['water_condition']
        rc.boiler_condition = self.cleaned_data['boiler_condition']
        rc.lighting = self.cleaned_data['lighting']
        rc.basic_options = self.cleaned_data['basic_options']
        rc.save()
        checklist.room_condition = rc

        # WomenSafetyPreference 저장 처리
        ws = checklist.women_safety_preference or WomenSafetyPreference()
        ws.female_only_room = self.cleaned_data['female_only_room']
        ws.female_parking = self.cleaned_data['female_parking']
        ws.female_gym = self.cleaned_data['female_gym']
        ws.female_study_cafe = self.cleaned_data['female_study_cafe']
        ws.safe_night_street = self.cleaned_data['safe_night_street']
        ws.save()
        checklist.women_safety_preference = ws

        if commit:
            checklist.save()

        return checklist


class MovingChecklistForm(forms.ModelForm):
    # 이사 하루 전
    unplug_appliances = forms.BooleanField(label="냉장고, 세탁기 미리 전원 차단하기", required=False)
    keep_valuables_separately = forms.BooleanField(label="귀중품, 중요 서류는 따로 보관하기", required=False)
    check_new_home_password = forms.BooleanField(label="새 집 열쇠, 도어락 비밀번호 재확인하기", required=False)
    confirm_moving_time = forms.BooleanField(label="이사 업체와 이사 시작 확인하기", required=False)
    finish_trash_sorting = forms.BooleanField(label="쓰레기 분리수거 및 집 정리 마무리하기", required=False)

    # 이사 당일
    check_truck_arrival_time = forms.BooleanField(label="이사 차량 도착 시간 확인하기", required=False)
    take_photos_of_old_home = forms.BooleanField(label="기존 집 상태 사진 찍어두기 (보증금 문제 대비)", required=False)

    # 새 집 점검하기
    check_leaks = forms.BooleanField(label="누수 확인하기", required=False)
    check_power_outlets = forms.BooleanField(label="콘센트 및 전기 확인하기", required=False)
    check_water_supply = forms.BooleanField(label="수도 작동 확인하기", required=False)

    # 설치 기사 방문 체크하기
    check_appliance_installer = forms.BooleanField(label="가전 설치 기사", required=False)
    check_internet_installer = forms.BooleanField(label="인터넷 설치 기사", required=False)

    # 이사 후
    complete_address_registration = forms.BooleanField(label="전입신고 완료하기 (동주민센터 또는 정부24)", required=False)
    change_address = forms.BooleanField(label="주소 변경하기 (은행, 학교, 직장 등)", required=False)
    check_deposit_settlement = forms.BooleanField(label="보증금 정산 확인하기", required=False)
    check_trash_disposal_rules = forms.BooleanField(label="쓰레기 배출 규칙 확인하기", required=False)
    check_residence_insurance = forms.BooleanField(label="거주지 화재보험, 전세보증금 보험 등 확인하기", required=False)

    class Meta:
        model = MovingChecklist
        exclude = exclude = ['checklist_group', 'user', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 초기값 설정
        if self.instance.pk:
            for field_name in self.fields:
                self.fields[field_name].initial = getattr(self.instance, field_name)

    def save(self, commit=True):
        checklist = super().save(commit=False)

        for field_name in self.fields:
            setattr(checklist, field_name, self.cleaned_data.get(field_name))

        if commit:
            checklist.save()
        return checklist


# class ResidencyChecklistForm(forms.ModelForm):
#     class Meta:
#         model = ResidencyChecklist
#         exclude = ['user', 'checklist_group', 'created_at']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # 필드 초기값 설정
#         if self.instance.pk:
#             for field in self.fields:
#                 self.fields[field].initial = getattr(self.instance, field)

#     def save(self, commit=True):
#         checklist = super().save(commit=False)

#         for field in self.fields:
#             setattr(checklist, field, self.cleaned_data.get(field))

#         if commit:
#             checklist.save()
#         return checklist

class ResidencyChecklistForm(forms.ModelForm):
    # 기본 점검
    check_utilities = forms.BooleanField(label="전기, 수도, 가스 정상 작동 재확인하기", required=False)
    check_heating = forms.BooleanField(label="냉온수, 보일러, 샤워기 점검하기", required=False)
    set_doorlock_password = forms.BooleanField(label="도어락 비밀번호 설정 및 강화하기", required=False)

    # 안전·보안 점검
    check_fire_detector = forms.BooleanField(label="화재 감지기 및 가스차단기 확인하기", required=False)
    check_window_locks = forms.BooleanField(label="창문, 현관문 잠금장치 점검하기", required=False)
    locate_circuit_breaker = forms.BooleanField(label="전기차단기 위치 파악해두기", required=False)

    # 생활 정착
    check_recycling_days = forms.BooleanField(label="분리수거 요일 및 분리수거장 확인하기", required=False)
    setup_wifi_appliances = forms.BooleanField(label="와이파이, TV, 가전 설치 마무리하기", required=False)
    prepare_emergency_kit = forms.BooleanField(label="응급약품 구비해두기", required=False)

    # 생활 필수품 보충하기
    prepare_laundry_detergent = forms.BooleanField(label="세탁 세제 및 주방 세제", required=False)
    prepare_kitchen_supplies = forms.BooleanField(label="키친타올 및 행주", required=False)
    prepare_toiletries = forms.BooleanField(label="화장지 및 물티슈", required=False)
    prepare_garbage_bags = forms.BooleanField(label="종량제봉투 (지역구 전용)", required=False)
    prepare_drinking_water = forms.BooleanField(label="생수 또는 정수기", required=False)

    class Meta:
        model = ResidencyChecklist
        exclude = ['user', 'checklist_group', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            for field_name in self.fields:
                self.fields[field_name].initial = getattr(self.instance, field_name)

    def save(self, commit=True):
        checklist = super().save(commit=False)

        for field_name in self.fields:
            setattr(checklist, field_name, self.cleaned_data.get(field_name))

        if commit:
            checklist.save()
        return checklist