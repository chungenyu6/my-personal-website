const copyButtons = document.querySelectorAll("[data-email]");
const copyStatus = document.querySelector(".copy-status");
let statusTimer;

async function copyText(text) {
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(text);
    return;
  }

  const textArea = document.createElement("textarea");
  textArea.value = text;
  textArea.setAttribute("readonly", "");
  textArea.style.position = "fixed";
  textArea.style.opacity = "0";
  document.body.append(textArea);
  textArea.select();
  const copied = document.execCommand("copy");
  textArea.remove();

  if (!copied) {
    throw new Error("Copy command failed");
  }
}

function showCopyStatus(message) {
  if (!copyStatus) return;

  window.clearTimeout(statusTimer);
  copyStatus.textContent = message;
  copyStatus.classList.add("is-visible");
  statusTimer = window.setTimeout(() => {
    copyStatus.classList.remove("is-visible");
  }, 2200);
}

copyButtons.forEach((button) => {
  button.addEventListener("click", async () => {
    try {
      await copyText(button.dataset.email);
      showCopyStatus("Email copied");
    } catch {
      showCopyStatus("Could not copy email");
    }
  });
});
