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