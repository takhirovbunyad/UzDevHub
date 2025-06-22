// static/js/modal.js

function openModal(projectId) {
    const data = JSON.parse(document.getElementById('project-json').textContent);
    const project = data.find(p => p.id === projectId);

    if (!project) return;

    // Modal elementlari
    document.getElementById('modalTitle').textContent = project.title;
    document.getElementById('modalDesc').textContent = project.description;
    document.getElementById('modalOwner').textContent = `${project.owner_name} ${project.owner_last_name}`;

    // Fayl tugmasi
    const fileBtn = document.getElementById('modalFile');
    if (project.file) {
        fileBtn.href = project.file;
        fileBtn.style.display = 'inline-block';
    } else {
        fileBtn.style.display = 'none';
    }

    // URL tugmasi
    const urlBtn = document.getElementById('modalUrl');
    if (project.url) {
        urlBtn.href = project.url;
        urlBtn.style.display = 'inline-block';
    } else {
        urlBtn.style.display = 'none';
    }

    // Modalni ko‘rsatish
    document.getElementById('projectModal').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('projectModal').classList.add('hidden');
}
