// Modalni ochish: id, slug va publish (sana) qabul qiladi
function openModal(id, slug, publish) {
  if (!publish) {
    publish = new Date().toISOString();  // fallback uchun hozirgi sana
  }
  const date = new Date(publish);
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();

  // URLni yangilaymiz
  history.pushState(null, null, `/${year}/${month}/${day}/${slug}/`);

  // Modalni topib ko‘rsatamiz
  const modal = document.getElementById(`modal-${id}`);
  if (modal) {
    modal.classList.add('show');
    // Scrollni oldini olish uchun bodyga overflow hidden qo‘yish mumkin
    document.body.style.overflow = 'hidden';
  }
}

// Modalni yopish: id qabul qiladi
function closeModal(id) {
  // URLni loyihalar ro‘yxatiga qaytarish
  history.pushState(null, null, `/projects/`);

  const modal = document.getElementById(`modal-${id}`);
  if (modal) {
    modal.classList.remove('show');
    document.body.style.overflow = ''; // scrollni tiklash
  }
}

// Sahifa yuklanganda URLdagi slugga qarab modalni avtomatik ochish
document.addEventListener('DOMContentLoaded', () => {
  const projectsData = JSON.parse(document.getElementById('project-json').textContent);
  const pathParts = window.location.pathname.split('/');

  // URL format: /year/month/day/slug/
  const slugFromUrl = pathParts.length >= 5 ? pathParts[4] : null;

  if (slugFromUrl) {
    const project = projectsData.find(p => p.slug === slugFromUrl);
    if (project) {
      openModal(project.id, project.slug, project.publish);
    }
  }
});

// Modal oynani tashqariga bosganda yopish uchun qo‘shimcha event
document.addEventListener('click', function(event) {
  // Agar click modalning orqa fonida bo‘lsa
  if (event.target.classList.contains('modal') && event.target.classList.contains('show')) {
    const id = event.target.id.split('-')[1];
    closeModal(id);
  }
});
