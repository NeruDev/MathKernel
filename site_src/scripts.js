document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");

  // ===== CARGAR TEMA =====
  const savedTheme = localStorage.getItem("theme") || "light";
  document.documentElement.setAttribute("data-theme", savedTheme);

  updateIcon(savedTheme);

  // ===== SWITCH =====
  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      let currentTheme = document.documentElement.getAttribute("data-theme");
      let newTheme = currentTheme === "dark" ? "light" : "dark";

      document.documentElement.setAttribute("data-theme", newTheme);
      localStorage.setItem("theme", newTheme);

      updateIcon(newTheme);
    });
  }

  // ===== ICONO DINÁMICO =====
  function updateIcon(theme) {
    if (!themeToggle) return;

    if (theme === "dark") {
      themeToggle.textContent = "🌙";
    } else {
      themeToggle.textContent = "🌞";
    }
  }

  // ===== MARKDOWN DINÁMICO (tu código original) =====
  const mdContainer = document.getElementById("md-content");
  if (mdContainer) {
    const mdPath = "../../content/00_fundamentos/01_simbologia_matematica/simbologia_matematica.md";
    
    fetch(mdPath)
      .then(res => {
        if (!res.ok) throw new Error("No se pudo cargar el Markdown");
        return res.text();
      })
      .then(text => {
        mdContainer.innerHTML = marked.parse(text);

        if (window.MathJax) {
          MathJax.typesetPromise([mdContainer]).then(() => {
            console.log("MathJax renderizado");
          });
        }
      })
      .catch(err => {
        mdContainer.innerHTML = "<p style='color: var(--miku-fuchsia)'>⚠️ Error al cargar contenido. Usa Live Server en local.</p>";
        console.error(err);
      });
  }
});