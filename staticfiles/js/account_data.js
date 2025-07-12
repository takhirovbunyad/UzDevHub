document.addEventListener('DOMContentLoaded', () => {
  const userInfoBtn = document.getElementById('user-info-btn');
  const userInfoModal = document.getElementById('user-info-modal');
  const closeUserInfo = document.getElementById('close-user-info');

  if (userInfoBtn) {
    userInfoBtn.addEventListener('click', () => {
      userInfoModal.style.display = 'flex'; // yoki classList.add('show')
    });
  }

  if (closeUserInfo) {
    closeUserInfo.addEventListener('click', () => {
      userInfoModal.style.display = 'none'; // yoki classList.remove('show')
    });
  }

  window.addEventListener('click', (e) => {
    if (e.target === userInfoModal) {
      userInfoModal.style.display = 'none';
    }
  });
});
