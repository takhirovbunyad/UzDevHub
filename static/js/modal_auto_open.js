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
