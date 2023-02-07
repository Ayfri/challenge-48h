const squares = document.querySelectorAll('.square');

let puzzleSolved = false;

squares.forEach((square, index) => {
  square.addEventListener('click', function() {
    if (!puzzleSolved) {
      square.style.transform = 'rotate(90deg)';
      let currentRotation = square.style.transform;
      let solved = Array.from(squares).every(square => square.style.transform === currentRotation);
      if (solved) {
        puzzleSolved = true;
        alert('Puzzle résolu! La lettre est A.');
      }
    }
  });
});
