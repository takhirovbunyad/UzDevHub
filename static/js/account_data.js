document.addEventListener('DOMContentLoaded', () => {
  const userInfoBtn = document.getElementById('user-info-btn');
  const userInfoModal = document.getElementById('user-info-modal');
  const closeUserInfo = document.getElementById('close-user-info');

  if (userInfoBtn) {
    userInfoBtn.addEventListener('click', () => {
      closeAllModals();
      userInfoModal.classList.add('show');
    });
  }

  if (closeUserInfo) {
    closeUserInfo.addEventListener('click', () => {
      userInfoModal.classList.remove('show');
    });
  }

  window.addEventListener('click', (e) => {
    if (e.target === userInfoModal) {
      userInfoModal.classList.remove('show');
    }
  });

  function closeAllModals() {
    document.querySelectorAll('.modal').forEach(modal => {
      modal.classList.remove('show');
    });
  }
});
