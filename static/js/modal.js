// Slugga asoslangan modalni ochish
function openModal(id, slug) {
  history.pushState(null, null, `/projects/${slug}/`);
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
  const slugFromUrl = pathParts.length >= 3 ? pathParts[2] : null;

  if (slugFromUrl) {
    const project = projectsData.find(p => p.slug === slugFromUrl);
    if (project) {
      openModal(project.id, project.slug);
    }
  }
});
