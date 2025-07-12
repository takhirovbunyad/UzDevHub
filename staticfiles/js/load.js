document.addEventListener('DOMContentLoaded', function () {
  const loadBtn = document.getElementById('load-btn');
  const projectContainer = document.getElementById('project-container');

  if (loadBtn) {
    loadBtn.addEventListener('click', function () {
      const page = this.getAttribute('data-page');

      fetch(`/load-more-projects/?page=${page}`)
        .then(response => response.text())
        .then(data => {
          if (data.trim()) {
            projectContainer.insertAdjacentHTML('beforeend', data);

            // Modal ochish funksiyasini yangilangan cardlarga qo‘llash
            const newCards = projectContainer.querySelectorAll('.project-card');
            newCards.forEach(card => {
              card.onclick = function () {
                const id = this.getAttribute('onclick').match(/'(\d+)'/)[1];
                openModal(id);
              };
            });

            const nextPage = parseInt(page) + 1;
            loadBtn.setAttribute('data-page', nextPage);
          } else {
            loadBtn.remove(); // Boshqa sahifa yo‘q bo‘lsa tugmani o‘chir
          }
        });
    });
  }
});
