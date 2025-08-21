document.addEventListener('DOMContentLoaded', () => {
  const addBtn = document.getElementById('open-add-modal');
  const modal = document.getElementById('add-modal');
  const step1 = document.getElementById('form-step-1');
  const step2 = document.getElementById('form-step-2');
  const nextBtn = document.getElementById('next-btn');
  const backBtn = document.getElementById('back-btn');
  const submitBtn = document.getElementById('submit-btn');
  const closeBtn = document.getElementById('close-modal');

  // Modalni ochish
  addBtn.addEventListener('click', () => {
    closeAllModals();
    modal.classList.add('show');
    step1.style.display = 'block';
    step2.style.display = 'none';
  });

  // Modalni yopish
  closeBtn.addEventListener('click', () => {
    modal.classList.remove('show');
    step1.style.display = 'block';
    step2.style.display = 'none';
  });

  // Keyingi bosqichga o‘tish
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

  // Orqaga qaytish
  backBtn.addEventListener('click', () => {
    step2.style.display = 'none';
    step1.style.display = 'block';
  });

  // Formani yuborish
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
    })
    .catch(() => {
      alert('Server bilan bog‘lanishda xatolik yuz berdi.');
    });
  });

  // Yangi loyiha kartasini sahifaga qo‘shish
  function addCardToGrid(project) {
    const grid = document.querySelector('.project-grid');
    const card = document.createElement('div');
    card.classList.add('project-card');

    const badge = project.category ? `<div class="category-badge">🏷️ ${project.category}</div>` : "";

    card.innerHTML = `
      ${badge}
      <h3>${escapeHtml(project.title)}</h3>
      <p>${escapeHtml(project.description)}</p>
      <p class="owner">👤 ${escapeHtml(project.owner_name)} ${escapeHtml(project.owner_last_name)}</p>
    `;

    // Modal ochish funksiyasini chaqirish uchun onclick qo‘shish
    card.setAttribute('onclick', `openModal('${project.id}', '${project.slug}', '${project.publish}')`);

    grid.prepend(card);
  }

  // XSS oldini olish uchun escape qilish
  function escapeHtml(text) {
    if (!text) return '';
    return text.replace(/[&<>"'`=\/]/g, function(s) {
      return ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
        '`': '&#96;',
        '=': '&#61;',
        '/': '&#47;'
      })[s];
    });
  }

  // CSRF tokenni olish
  function getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      const [k, v] = cookie.trim().split('=');
      if (k === name) return v;
    }
    return '';
  }

  // Boshqa modalni yopish (agar ochiq bo‘lsa)
  function closeAllModals() {
    document.querySelectorAll('.modal').forEach(modal => {
      modal.classList.remove('show');
    });
  }
});
