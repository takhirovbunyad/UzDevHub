    document.addEventListener("DOMContentLoaded", function () {
      const loadBtn = document.getElementById("load-btn");
      const cardContainer = document.getElementById("card-container");

      if (loadBtn) {
        loadBtn.addEventListener("click", function () {
          const page = parseInt(loadBtn.dataset.page);

          fetch(`/load_more_cards/?page=${page}`)
            .then((res) => res.json())
            .then((data) => {
              data.cards.forEach((item) => {
                const card = document.createElement("div");
                card.classList.add("card");
                card.innerHTML = `
                  <img src="${item.preview}" alt="${item.title}">
                  <div class="card-body">
                    <h3>${item.title}</h3>
                    <p>${item.description}</p>
                    <a href="${item.url}" target="_blank" rel="noopener noreferrer">Batafsil o‘qish</a>
                    <small>Manba: ${item.source}</small>
                  </div>
                `;
                cardContainer.appendChild(card);
              });

              if (data.has_next) {
                loadBtn.dataset.page = page + 1;
              } else {
                loadBtn.style.display = "none";
              }
            })
            .catch((err) => {
              console.error("Xatolik:", err);
            });
        });
      }
    });
