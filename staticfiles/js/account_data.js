// account_data.js (tozalangan)
document.addEventListener('DOMContentLoaded', () => {
  const userInfoBtn   = document.getElementById('user-info-btn');
  const userInfoModal = document.getElementById('user-info-modal');
  const closeUserInfo = document.getElementById('close-user-info');

  // Info tugmasi bosilganda
  if (userInfoBtn) {
    userInfoBtn.addEventListener('click', () => {
      closeAllModals();
      userInfoModal.classList.add('show');
    });
  }

  // Yopish tugmasi
  if (closeUserInfo) {
    closeUserInfo.addEventListener('click', () => {
      userInfoModal.classList.remove('show');
    });
  }

  // Modal tashqarisiga bosilsa yopilsin
  window.addEventListener('click', (e) => {
    if (e.target === userInfoModal) {
      userInfoModal.classList.remove('show');
    }
  });

  // Boshqa modallarni yopish funksiyasi
  function closeAllModals() {
    document.querySelectorAll('.modal').forEach(modal => {
      modal.classList.remove('show');
    });
  }
});
