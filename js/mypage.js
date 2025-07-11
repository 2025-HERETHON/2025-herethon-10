document.addEventListener('DOMContentLoaded', () => {
  const toggleBoxes = document.querySelectorAll('.checkboxBox');

  toggleBoxes.forEach(box => {
    const fakeCheckbox = box.querySelector('.fakeCheckbox');
    const realCheckbox = box.querySelector('.realCheckbox');
    const group = box.dataset.group;

    fakeCheckbox.addEventListener('click', () => {

      const sameGroupBoxes = document.querySelectorAll(`.checkboxBox[data-group="${group}"]`);

      sameGroupBoxes.forEach(b => {
        const otherFake = b.querySelector('.fakeCheckbox');
        const otherReal = b.querySelector('.realCheckbox');

        otherFake.classList.remove('checked');
        otherReal.checked = false;
      });

      fakeCheckbox.classList.add('checked');
      realCheckbox.checked = true;
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const inputs = document.querySelectorAll('.budget');

  inputs.forEach(input => {
    input.addEventListener('input', () => {
      input.value = input.value.replace(/\D/g, '');

      if (input.value.length > 3) {
        input.value = input.value.slice(0, 3);
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const regions = document.querySelectorAll('.dropdownBox');

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