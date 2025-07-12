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
    step1.style.display = 'block';
    step2.style.display = 'none';
  });

  nextBtn.addEventListener('click', () => {
    const title = document.querySelector("input[name='title']").value.trim();
    const description = document.querySelector("textarea[name='description']").value.trim();
    if (!title || !description) {
      alert("Iltimos, sarlavha va izohni to‘ldiring.");
      return;
    }
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
        form.reset();
        step1.style.display = 'block';
        step2.style.display = 'none';
      } else {
        alert('Xatolik: ' + data.error);
      }
    });
  });

  function addCardToGrid(project) {
    const grid = document.querySelector('.project-grid');
    const card = document.createElement('div');
    card.classList.add('project-card');

    const badge = project.category ? `<div class="category-badge">🏷️ ${project.category}</div>` : "";

    card.innerHTML = `
      ${badge}
      <h3>${project.title}</h3>
      <p>${project.description}</p>
      <p class="owner">👤 ${project.owner_name} ${project.owner_last_name}</p>
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
