document.getElementById('pen').addEventListener('click', function() {
    document.getElementById('uploadInput').click();
});

  document.querySelectorAll('.custom-dropdown').forEach(dropdown => {
    const selected = dropdown.querySelector('.selected');
    const options = dropdown.querySelector('.options');
    const hiddenInput = dropdown.querySelector('input');

    selected.addEventListener('click', () => {
      // 다른 드롭다운 닫기
      document.querySelectorAll('.options').forEach(opt => {
        if (opt !== options) opt.style.display = 'none';
      });
      // 현재 드롭다운 토글
      options.style.display = options.style.display === 'block' ? 'none' : 'block';
    });

    options.querySelectorAll('li').forEach(option => {
      option.addEventListener('click', () => {
        selected.textContent = option.textContent;
        hiddenInput.value = option.dataset.value;
        options.style.display = 'none';
      });
    });

    document.addEventListener('click', (e) => {
      if (!dropdown.contains(e.target)) {
        options.style.display = 'none';
      }
    });
  });


const sidoDropdown = document.getElementById('sidoDropdown');
const sigunguDropdown = document.getElementById('sigunguDropdown');
const sidoSelect = document.getElementById('sido');
const sigunguSelect = document.getElementById('sigungu');

// 드롭다운 열고 닫기
function toggleOptions(dropdown) {
  const options = dropdown.querySelector('.options2');
  const isOpen = options.style.display === 'block';
  document.querySelectorAll('.options2').forEach(opt => opt.style.display = 'none');
  options.style.display = isOpen ? 'none' : 'block';
}

// 옵션 선택
function selectOption(dropdown, text, value, selectEl) {
  dropdown.querySelector('.selected2').textContent = text;
  selectEl.value = value;
  dropdown.querySelector('.options2').style.display = 'none';
}

// 시도 목록 불러오기
fetch('/api/sido')
  .then(res => res.json())
  .then(data => {
    const sidoOptions = sidoDropdown.querySelector('.options2');
    sidoOptions.innerHTML = '';
    data.forEach(sido => {
      const li = document.createElement('li');
      li.textContent = sido.name;
      li.dataset.value = sido.code;
      li.addEventListener('click', () => {
        selectOption(sidoDropdown, sido.name, sido.code, sidoSelect);
        // 시군구 초기화
        sigunguDropdown.querySelector('.selected2').textContent = '시/군/구';
        sigunguDropdown.querySelector('.options2').innerHTML = '';
        sigunguSelect.value = '';
        sigunguSelect.disabled = false;

        // 시군구 목록 불러오기
        fetch(`/api/sigungu?sido=${sido.code}`)
          .then(res => res.json())
          .then(sigunguData => {
            const sigunguOptions = sigunguDropdown.querySelector('.options2');
            sigunguOptions.innerHTML = '';
            sigunguData.forEach(sigungu => {
              const li = document.createElement('li');
              li.textContent = sigungu.name;
              li.dataset.value = sigungu.code;
              li.addEventListener('click', () => {
                selectOption(sigunguDropdown, sigungu.name, sigungu.code, sigunguSelect);
              });
              sigunguOptions.appendChild(li);
            });
          });
      });
      sidoOptions.appendChild(li);
    });
  });

// 드롭다운 클릭 이벤트
sidoDropdown.querySelector('.selected2').addEventListener('click', () => toggleOptions(sidoDropdown));
sigunguDropdown.querySelector('.selected2').addEventListener('click', () => toggleOptions(sigunguDropdown));

// 외부 클릭 시 닫기
document.addEventListener('click', (e) => {
  if (!sidoDropdown.contains(e.target)) {
    sidoDropdown.querySelector('.options2').style.display = 'none';
  }
  if (!sigunguDropdown.contains(e.target)) {
    sigunguDropdown.querySelector('.options2').style.display = 'none';
  }
});

const radios = document.querySelectorAll('.with-check');
const roommateCountWrapper = document.getElementById('roommateCountWrapper');

radios.forEach(radio => {
  radio.addEventListener('change', () => {
    if (radio.value === 'yes' && radio.checked) {
      roommateCountWrapper.style.display = 'block';
    } else if (radio.value === 'no' && radio.checked) {
      roommateCountWrapper.style.display = 'none';
      roommateCountWrapper.querySelector('input').value = '';
    }
  });
});

// 성별 라디오 버튼 제어 (name 없이)
const genderRadios = document.querySelectorAll('#gender input[type="radio"]');
genderRadios.forEach(radio => {
  radio.addEventListener('click', () => {
    genderRadios.forEach(r => r.checked = (r === radio));
  });
});

// 동거인 여부 라디오 버튼 제어 (name 없이)
const withRadios = document.querySelectorAll('#with input[type="radio"]');
withRadios.forEach(radio => {
  radio.addEventListener('click', () => {
    withRadios.forEach(r => r.checked = (r === radio));
  });
});
