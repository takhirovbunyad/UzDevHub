// Slugga asoslangan modalni ochish
function openModal(id, slug, publish) {
  if (!publish) {
    publish = new Date().toISOString();  // fallback uchun hozirgi sana
  }
  const date = new Date(publish);
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();
  history.pushState(null, null, `/${year}/${month}/${day}/${slug}/`);

  const modal = document.getElementById(`modal-${id}`);
  if (modal) {
    modal.classList.add('show');
  }
}

// Modalni yopish
function closeModal(id) {
  history.pushState(null, null, `/projects/`);
  const modal = document.getElementById(`modal-${id}`);
  if (modal) {
    modal.classList.remove('show');
  }
}

// Sahifa yuklanganda URLdagi slug asosida modalni avtomatik ochish
document.addEventListener('DOMContentLoaded', function () {
  const projectsData = JSON.parse(document.getElementById('project-json').textContent);
  const pathParts = window.location.pathname.split('/');

  // /2025/6/28/slug/ formatdagi URLdan slugni olish
  const slugFromUrl = pathParts.length >= 5 ? pathParts[4] : null;

  if (slugFromUrl) {
    const project = projectsData.find(p => p.slug === slugFromUrl);
    if (project) {
      openModal(project.id, project.slug, project.publish);
    }
  }
});
