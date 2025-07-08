document.addEventListener('DOMContentLoaded', () => {

  const toggleIcons = document.querySelectorAll('.toggleIcon');

  toggleIcons.forEach((icon, index) => {
    icon.addEventListener('click', (e) => {
      e.stopPropagation();

      const contentId = `toggleContent${index + 1}`;
      const content = document.getElementById(contentId);

      if (content) {
        if (content.style.display === 'block') {
          content.style.display = 'none';
          icon.textContent = '>';
        } else {
          content.style.display = 'block';
          icon.textContent = 'v';
        }
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const toggleBoxes = document.querySelectorAll('.toggleContent4Box');

  toggleBoxes.forEach(box => {
    const fakeCheckbox = box.querySelector('.fakeCheckBox');
    const realCheckbox = box.querySelector('.toggleContent4Checkbox');

    fakeCheckbox.addEventListener('click', () => {
      fakeCheckbox.classList.toggle('checked');
      realCheckbox.checked = fakeCheckbox.classList.contains('checked');

      if (realCheckbox.checked) {
        fakeCheckbox.textContent = '✓';
      } else {
        fakeCheckbox.textContent = '';
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const contractBoxes = document.querySelectorAll('.contractWriteBox');

  contractBoxes.forEach(box => {
    const fakeCheckbox = box.querySelector('.fakeCheckBox');
    const realCheckbox = box.querySelector('.contractWriteCheckbox');

    fakeCheckbox.addEventListener('click', () => {
      fakeCheckbox.classList.toggle('checked');
      realCheckbox.checked = fakeCheckbox.classList.contains('checked');

      if (realCheckbox.checked) {
        fakeCheckbox.textContent = '✓';
      } else {
        fakeCheckbox.textContent = '';
      }
    });
  });
});