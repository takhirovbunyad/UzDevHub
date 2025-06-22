document.addEventListener("DOMContentLoaded", () => {
  const toggleBtn = document.getElementById('dark-toggle');
  const body = document.body;

  if (!toggleBtn) {
    console.warn('Toggle button topilmadi');
    return;
  }

  if (localStorage.getItem('theme') === 'light') {
    body.classList.add('light-mode');
    toggleBtn.textContent = '🌙';
  } else {
    body.classList.remove('light-mode');
    toggleBtn.textContent = '☀️';
  }

  toggleBtn.addEventListener('click', () => {
    body.classList.toggle('light-mode');
    const isLight = body.classList.contains('light-mode');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
    toggleBtn.textContent = isLight ? '🌙' : '☀️';
  });
});
