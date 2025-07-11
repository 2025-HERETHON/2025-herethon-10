document.addEventListener('DOMContentLoaded', () => {
  const pickContent = document.getElementById('filterBigBox');
  const regions = pickContent.querySelectorAll('.filter');

  regions.forEach(region => {
    region.addEventListener('click', (e) => {
      e.stopPropagation();

      // 모든 dropdown 닫기
      document.querySelectorAll('.inputRegionDropdown1, .inputRegionDropdown2').forEach(dropdown => {
        dropdown.style.display = 'none';
      });

      // region의 부모(.filterSmallBox)의 다음 형제를 열어준다
      const dropdown = region.closest('.filterSmallBox').nextElementSibling;
      if (dropdown && 
         (dropdown.classList.contains('inputRegionDropdown1') || 
          dropdown.classList.contains('inputRegionDropdown2'))) {
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
    if (!e.target.closest('#filterBigBox')) {
      document.querySelectorAll('.inputRegionDropdown1, .inputRegionDropdown2').forEach(dropdown => {
        dropdown.style.display = 'none';
      });
    }
  });
});