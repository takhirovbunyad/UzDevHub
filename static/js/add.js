document.addEventListener('DOMContentLoaded', () => {
  const addBtn = document.getElementById('open-add-modal');
  const modal = document.getElementById('add-modal');
  const step1 = document.getElementById('form-step-1');
  const step2 = document.getElementById('form-step-2');
  const nextBtn = document.getElementById('next-btn');
  const backBtn = document.getElementById('back-btn');
  const submitBtn = document.getElementById('submit-btn');
  const closeBtn = document.getElementById('close-modal');

  addBtn.addEventListener('click', () => {
    modal.classList.add('show');
    step1.style.display = 'block';
    step2.style.display = 'none';
  });

  closeBtn.addEventListener('click', () => {
    modal.classList.remove('show');
  });

  nextBtn.addEventListener('click', () => {
    step1.style.display = 'none';
    step2.style.display = 'block';
  });

  backBtn.addEventListener('click', () => {
    step2.style.display = 'none';
    step1.style.display = 'block';
  });

  submitBtn.addEventListener('click', (e) => {
    e.preventDefault();

    const form = document.getElementById('add-project-form');
    const formData = new FormData(form);

    fetch('/add-project/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCSRFToken(),
      },
      body: formData
    })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          addCardToGrid(data.project);
          modal.classList.remove('show');
          form.reset(); // forma tozalansin
        } else {
          alert('Xatolik: ' + data.error);
        }
      });
  });

  function addCardToGrid(project) {
    const grid = document.querySelector('.project-grid');
    const card = document.createElement('div');
    card.classList.add('project-card');
    card.innerHTML = `
      <div class="category-badge">${project.category}</div>
      <h3>${project.title}</h3>
      <p>${project.description}</p>
      <p class="owner">👤 ${project.ism} ${project.familya}</p>
    `;
    grid.prepend(card);
  }

  function getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      const [k, v] = cookie.trim().split('=');
      if (k === name) return v;
    }
    return '';
  }
});
