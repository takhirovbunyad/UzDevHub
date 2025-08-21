document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("public-user-info-modal");
  const closeBtn = document.getElementById("public-user-info-close");

  function openModal() {
    modal.classList.add("show");
    document.body.style.overflow = "hidden"; // Scroll lock
  }

  function closeModal() {
    modal.classList.remove("show");
    document.body.style.overflow = "";
  }

  function clearModal() {
    const fields = [
      "fullname", "email", "profession", "bio", "address",
      "workplace", "phone", "telegram", "github", "linkedin", "website"
    ];
    fields.forEach(f => {
      const el = document.getElementById(`public-user-${f}`);
      if (el) {
        if (el.tagName === "A") {
          el.href = "#";
        }
        el.textContent = "";
      }
    });

    const img = document.getElementById("public-user-profile-image");
    if (img) {
      img.style.display = "none";
      img.src = "";
    }
  }

  // Author info ochish
  window.showAuthorInfo = async function (username) {
    clearModal(); // har safar ochishda tozalash
    try {
      const res = await fetch(`/accounts/user-info/${username}/`);
      if (!res.ok) throw new Error("Ma'lumot topilmadi");
      const data = await res.json();

      document.getElementById("public-user-fullname").textContent =
        `${data.first_name || ""} ${data.last_name || ""}`.trim() || "Ko‘rsatilmagan";
      document.getElementById("public-user-email").textContent = data.email || "Ko‘rsatilmagan";
      document.getElementById("public-user-profession").textContent = data.profession || "Ko‘rsatilmagan";
      document.getElementById("public-user-bio").textContent = data.bio || "Ko‘rsatilmagan";
      document.getElementById("public-user-address").textContent = data.address || "Ko‘rsatilmagan";
      document.getElementById("public-user-workplace").textContent = data.workplace || "Ko‘rsatilmagan";
      document.getElementById("public-user-phone").textContent = data.phone_number || "Ko‘rsatilmagan";

      ["telegram", "github", "linkedin", "website"].forEach(link => {
        const el = document.getElementById(`public-user-${link}`);
        if (data[link]) {
          el.href = data[link];
          el.textContent = data[link];
        } else {
          el.textContent = "Ko‘rsatilmagan";
          el.removeAttribute("href");
        }
      });

      if (data.profile_image_url) {
        const img = document.getElementById("public-user-profile-image");
        img.src = data.profile_image_url;
        img.style.display = "block";
      }

      openModal(); // har safar modal ochiladi
    } catch (err) {
      console.error(err);
      alert("Foydalanuvchi ma'lumotlarini olishda xatolik yuz berdi.");
    }
  };

  // Modalni yopish tugmasi
  closeBtn?.addEventListener("click", closeModal);

  // Overlay bosilganda yopish
  modal.addEventListener("click", (e) => {
    if (e.target === modal) closeModal();
  });

  // ESC tugmasi
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
  });
});
python -m venv venv
