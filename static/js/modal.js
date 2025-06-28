function openModal(id, slug, publish) {
  if (!publish) {
    publish = new Date().toISOString();
  }
  const date = new Date(publish);
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();

  // URLni yangilash
  history.pushState(null, null, `/${year}/${month}/${day}/${slug}/`);

  const modal = document.getElementById(`modal-${id}`);
  if (modal) {
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(id) {
  history.pushState(null, null, `/projects/`);

  const modal = document.getElementById(`modal-${id}`);
  if (modal) {
    modal.classList.remove('show');
    document.body.style.overflow = '';
  }
}

// Modal tashqarisiga bosilganda yopish
document.addEventListener('click', function(event) {
  if (event.target.classList.contains('modal') && event.target.classList.contains('show')) {
    const id = event.target.id.split('-')[1];
    closeModal(id);
  }
});

function openModal(id, slug, publish) {
  if (!publish) {
    publish = new Date().toISOString();
  }
  const date = new Date(publish);
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();

  history.pushState(null, null, `/${year}/${month}/${day}/${slug}/`);

  const modal = document.getElementById(`modal-${id}`);
  if (modal) {
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(id) {
  history.pushState(null, null, '/projects/');

  const modal = document.getElementById(`modal-${id}`);
  if (modal) {
    modal.classList.remove('show');
    document.body.style.overflow = '';
  }
}
