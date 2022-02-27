// slider

function sliderPluggin(activeslide = 0) {
  const slides = document.querySelectorAll(".slide");

  slides[activeslide].classList.add("active");

  function clearActiveClasses() {
    slides.forEach((slide) => {
      slide.classList.remove("active");
    });
  }

  for (const slide of slides) {
    slide.addEventListener("click", () => {
      clearActiveClasses();
      slide.classList.add("active");
    });
  }
}

sliderPluggin(0);

// counter

// function animateValue(obj, start, end, duration) {
//   let startTimestamp = null;
//   const step = (timestamp) => {
//     if (!startTimestamp) startTimestamp = timestamp;
//     const progress = Math.min((timestamp - startTimestamp) / duration, 1);
//     obj.innerHTML = Math.floor(progress * (end - start) + start);
//     if (progress < 1) {
//       window.requestAnimationFrame(step);
//     }
//   };
//   window.requestAnimationFrame(step);
// }

// const purecounters = $(".purecounter");

// for (const counteritem of purecounters) {
//   animateValue(
//     counteritem,
//     counteritem.data("purecounter-end"),
//     counteritem.data("purecounter-start"),
//     5000
//   );
// }
