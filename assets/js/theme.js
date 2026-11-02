// Runs in the head so the page does not flash the wrong theme.
let setTheme = (theme) => {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("theme", theme);
};

let toggleTheme = (theme) => setTheme(theme == "dark" ? "light" : "dark");

let saved = localStorage.getItem("theme");
let prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
setTheme(saved || (prefersDark ? "dark" : "light"));
