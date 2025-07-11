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
  const pickContent = document.querySelector('.pickContent1');
  const regions = pickContent.querySelectorAll('.inputRegion');

  regions.forEach(region => {
    region.addEventListener('click', () => {
      // 모든 dropdown 닫기
      document.querySelectorAll('.inputRegionDropdown1, .inputRegionDropdown2').forEach(dropdown => {
        dropdown.style.display = 'none';
      });

      // region 다음에 있는 dropdown만 열어주기
      const dropdown = region.nextElementSibling;
      if (dropdown && (dropdown.classList.contains('inputRegionDropdown1') || dropdown.classList.contains('inputRegionDropdown2'))) {
        dropdown.style.display = 'block';
      }
    });
  });

  // 드롭다운 내부 클릭 시 닫기
  document.querySelectorAll('.inputRegionDropdown1 div, .inputRegionDropdown2 div').forEach(item => {
    item.addEventListener('click', (e) => {
      console.log('선택된 값:', e.target.textContent);
      // 부모 dropdown 닫기
      e.target.closest('.inputRegionDropdown1, .inputRegionDropdown2').style.display = 'none';
    });
  });

  // 외부 클릭 시 닫기
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.pickContent1')) {
      document.querySelectorAll('.inputRegionDropdown1, .inputRegionDropdown2').forEach(dropdown => {
        dropdown.style.display = 'none';
      });
    }
  });
});