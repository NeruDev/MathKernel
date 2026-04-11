
document.addEventListener("DOMContentLoaded", () => {
  const currentTheme = localStorage.getItem("theme") || "light";
  document.documentElement.setAttribute("data-theme", currentTheme);
  
  const themeToggle = document.getElementById("theme-toggle");
  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      let theme = document.documentElement.getAttribute("data-theme");
      let newTheme = theme === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", newTheme);
      localStorage.setItem("theme", newTheme);
    });
  }

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
        mdContainer.innerHTML = "<p style='color: var(--miku-fuchsia)'>⚠️ Hubo un error al cargar el contenido de la simbología. Para verlo localmente, recuerda usar 'Live Server' por bloqueos CORS.</p>";
        console.error(err);
      });
  }
});
