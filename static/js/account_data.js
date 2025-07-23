document.addEventListener('DOMContentLoaded', () => {
  const userInfoBtn = document.getElementById('user-info-btn');
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

  // ✅ FUNKSIYA: Muallif ma'lumotlarini ko‘rsatish
  window.showAuthorInfo = function (userId) {
    if (!userId) {
      console.error("❌ userId yo‘q!");
      return;
    }

    fetch(`/accounts/user-info/${userId}/`)
      .then(res => {
        if (!res.ok) {
          throw new Error("Server error");
        }
        return res.json();
      })
      .then(data => {
        console.log("✅ User info:", data);

        // Modalga ma'lumot joylash
        document.getElementById("author-fullname").innerText = `${data.first_name} ${data.last_name}`;
        document.getElementById("author-bio").innerText = data.bio || "Bio mavjud emas";
        document.getElementById("author-location").innerText = data.location || "Manzil yo‘q";

        // Modalni ko‘rsat
        document.getElementById("author-modal").style.display = "block";
      })
      .catch(error => {
        console.error("❌ Error fetching user info:", error);
      });
  }

  // Muallif modalni yopish
  const closeBtn = document.getElementById("close-author-modal");
  if (closeBtn) {
    closeBtn.addEventListener("click", function () {
      document.getElementById("author-modal").style.display = "none";
    });
  }
});
