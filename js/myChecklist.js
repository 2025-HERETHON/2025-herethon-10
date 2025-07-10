document.addEventListener('DOMContentLoaded', () => {
  const toggleIcons = document.querySelectorAll('.toggleBox');

  toggleIcons.forEach((icon, index) => {
    icon.addEventListener('click', (e) => {
      e.stopPropagation();

      const contentId = `toggleContent${index + 1}`;
      const content = document.getElementById(contentId);
      const img = icon.querySelector('img');

      if (content) {
        if (content.style.display === 'block') {
          content.style.display = 'none';
          img.src = '../img/chevron-right.png';
        } else {
          content.style.display = 'block';
          img.src = '../img/chevron-down.png';
        }
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const allBoxes = document.querySelectorAll(
    '.toggleContent4Box, .contractWriteBox, .moveBox, .habitationBox'
  );

  allBoxes.forEach(box => {
    const fakeCheckbox = box.querySelector('.fakeCheckBox');
    let realCheckbox = null;

    // 어떤 클래스명을 가진 체크박스인지 확인
    realCheckbox =
      box.querySelector('.toggleContent4Checkbox') ||
      box.querySelector('.contractWriteCheckbox') ||
      box.querySelector('.moveCheckbox') ||
      box.querySelector('.habitationCheckbox');

    if (fakeCheckbox && realCheckbox) {
      fakeCheckbox.addEventListener('click', () => {
        fakeCheckbox.classList.toggle('checked');
        realCheckbox.checked = fakeCheckbox.classList.contains('checked');

        if (realCheckbox.checked) {
          fakeCheckbox.textContent = '✓';
        } else {
          fakeCheckbox.textContent = '';
        }
      });
    }
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const checkboxes = document.querySelectorAll('.goodBadCheckbox');

  checkboxes.forEach(box => {
    const fakeCheckbox = box.querySelector('.goodBadFakeCheckbox');
    const realCheckbox = box.querySelector('.goodBadRealCheckbox');
    const img = fakeCheckbox.querySelector('img');

    fakeCheckbox.addEventListener('click', () => {
      fakeCheckbox.classList.toggle('checked');
      realCheckbox.checked = fakeCheckbox.classList.contains('checked');

      if (realCheckbox.checked) {
        img.src = '../img/bad.png';
      } else {
        img.src = '../img/good.png';
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  let currentIndex = 1;

  // 총 몇 개 체크리스트인지
  const totalChecklists = 3;

  // 체크리스트 article들
  const checklists = [
    document.getElementById('checklist1'),
    document.getElementById('checklist2'),
    document.getElementById('checklist3')
  ];

  // 진행률 article들
  const progressContents = [
    document.getElementById('checklistProgressContent1'),
    document.getElementById('checklistProgressContent2'),
    document.getElementById('checklistProgressContent3')
  ];

  // 초기 설정 → 첫 번째만 보이게
  function showChecklist(index) {
    checklists.forEach((el, i) => {
      el.style.display = (i + 1 === index) ? 'flex  ' : 'none';
    });
    progressContents.forEach((el, i) => {
      el.style.display = (i + 1 === index) ? 'flex' : 'none';
    });
  }

  showChecklist(currentIndex);

  // nextPage 버튼
  document.querySelectorAll('.nextPage').forEach(btn => {
    btn.addEventListener('click', () => {
      if (currentIndex < totalChecklists) {
        currentIndex += 1;
        showChecklist(currentIndex);
      }
    });
  });

  // previousPage 버튼
  document.querySelectorAll('.previousPage').forEach(btn => {
    btn.addEventListener('click', () => {
      if (currentIndex > 1) {
        currentIndex -= 1;
        showChecklist(currentIndex);
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const regions = document.querySelectorAll('.inputRegion');

  regions.forEach(region => {
    region.addEventListener('click', () => {
      // 현재 region 숨김
      region.style.display = 'none';

      // 바로 다음 sibling 이 inputRegionDropdown 라고 가정
      const dropdown = region.nextElementSibling;
      if (dropdown && dropdown.classList.contains('inputRegionDropdown')) {
        dropdown.style.display = 'flex';

        // 드롭다운 안의 항목들 클릭 시 다시 돌아오기
        const dropdownItems = dropdown.querySelectorAll('div');
        dropdownItems.forEach(item => {
          item.addEventListener('click', () => {
            dropdown.style.display = 'none';
            region.style.display = 'flex'; // display:flex 로 원래대로 복구
          });
        });
      }
    });
  });
});

// var container = document.getElementById('map');
// var options = {
//     center: new kakao.maps.LatLng(33.450701, 126.570667),
//     level: 3
// };

// var map = new kakao.maps.Map(container, options);