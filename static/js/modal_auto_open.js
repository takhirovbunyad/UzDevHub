document.addEventListener('DOMContentLoaded', () => {
  const slug = document.body.getAttribute('data-modal-slug');
  if (!slug) return;

  const scriptTag = document.getElementById('project-json');
  if (!scriptTag) return;

  let projectsData;

  try {
    projectsData = JSON.parse(scriptTag.textContent);
    if (!Array.isArray(projectsData)) {
      console.error("❌ JSON parse bo‘ldi, lekin array emas:", projectsData);
      return;
    }
    console.log("✅ JSON array tayyor:", projectsData);
  } catch (err) {
    console.error("❌ JSON parse xatolik:", err);
    return;
  }

  const project = projectsData.find(p => p.slug === slug);
  if (project) {
    console.log("✅ Modal ochilyapti:", project);
    openModal(project.id, project.slug, project.publish || new Date().toISOString());
  } else {
    console.warn("❗ Modal ochilmadi, slug topilmadi:", slug);
  }
});
const copyBtn = document.getElementById('copy-link-btn');

function openModal(id, slug, publish) {
  if (!publish) publish = new Date().toISOString();
  const date = new Date(publish);
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();

  const url = `${window.location.origin}/${year}/${month}/${day}/${slug}/`;
  history.pushState(null, null, url);

  const modal = document.getElementById(`modal-${id}`);
  if (modal) {
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';

    // Nusxalash tugmasini ko‘rsatish va URL saqlash
    copyBtn.style.display = 'inline-block';
    copyBtn.setAttribute('data-url', url);
  }
}

function closeModal(id) {
  history.pushState(null, null, '/projects/');

  const modal = document.getElementById(`modal-${id}`);
  if (modal) {
    modal.classList.remove('show');
    document.body.style.overflow = '';
  }

  // Nusxalash tugmasini yashirish
  copyBtn.style.display = 'none';
}

// Tugma bosilganda URL ni nusxalash
copyBtn.addEventListener('click', () => {
  const url = copyBtn.getAttribute('data-url');
  navigator.clipboard.writeText(url).then(() => {
    copyBtn.textContent = '✅';
    setTimeout(() => {
      copyBtn.textContent = '🚀';
    }, 500);
  });
});
