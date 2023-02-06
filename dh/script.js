const playButton = document.getElementById("play");
const result = document.getElementById("result");

playButton.addEventListener("click", function() {
  const pile = document.getElementById("pile").checked;
  const face = document.getElementById("face").checked;

  if (!pile && !face) {
    result.textContent = "Veuillez choisir Pile ou Face";
  } else {
    const random = Math.random() < 0.5;
    if (random && pile || !random && face) {
      result.textContent = "Vous avez gagné la lettre est P";
    } else {
      result.textContent = "Vous avez perdu.";
    }
  }
});
