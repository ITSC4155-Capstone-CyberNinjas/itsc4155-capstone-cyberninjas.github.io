  function makeItRain() {
    document.getElementById("makeItRain").disabled = true;
    var end = Date.now() + (2 * 1000);
  

  var colors = ['#00703C', '#F0CB00', '#66cdaa'];
  
  function frame() {
    confetti({
      particleCount: 2,
      angle: 50,
      spread: 65,
      origin: { x: 0 },
      colors: colors
    });
    confetti({
      particleCount: 4,
      angle: 120,
      spread: 75,
      origin: { x: 1 },
      colors: colors
    });
  
    if (Date.now() < end) {
      requestAnimationFrame(frame);
    }
    else {
      document.getElementById("makeItRain").disabled = false;
    }
  };
    frame();
  }
  
  function randomInRange(min, max) {
    return Math.random() * (max - min) + min;
  }