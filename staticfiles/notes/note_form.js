(function () {
  const textarea = document.getElementById("id_content");
  const countEl = document.getElementById("content-char-count");
  if (!textarea || !countEl) return;

  function update() {
    countEl.textContent = String(textarea.value.length);
  }

  textarea.addEventListener("input", update);
  update();
})();
