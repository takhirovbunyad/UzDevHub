document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("search-input");
  const projectCards = document.querySelectorAll(".project-card");

  // Normalizatsiya qilish (katta-kichik harfni farqlamaslik uchun)
  function normalizeText(text) {
    return text.toLowerCase().replace(/\s+/g, "");
  }

  searchInput.addEventListener("input", function () {
    const query = normalizeText(searchInput.value);

    projectCards.forEach(card => {
      const title = normalizeText(card.querySelector("h3")?.textContent || "");
      const desc = normalizeText(card.querySelector("p")?.textContent || "");
      const owner = normalizeText(card.querySelector(".owner")?.textContent || "");
      const category = normalizeText(card.querySelector(".category-badge")?.textContent || "");
      const tags = normalizeText(card.getAttribute("data-tags") || ""); // data-tags attribute qo‘shamiz

      const matches = (
        title.includes(query) ||
        desc.includes(query) ||
        owner.includes(query) ||
        category.includes(query) ||
        tags.includes(query)
      );

      card.style.display = matches ? "flex" : "none";
    });
  });
});
