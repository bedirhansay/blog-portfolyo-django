import $ from "jquery";

export default class Component {
  constructor() {
    $(".menu").on("click", () => {
      $(".navbar-sub").toggleClass("active");
      $(".dropdown").removeClass("active");
      this.changeText();
    });

    $(".profile").on("click", () => {
      $(".dropdown").toggleClass("active");
      $(".navbar-sub").removeClass("active");
      this.changeText();
    });

    this.startTextLoop();
  }

  changeText(textArray, currentIndex) {
    const midText = $(".mid-text");
    const nextIndex = (currentIndex + 1) % textArray.length;
    const nextText = textArray[nextIndex];

    midText.text("");
    this.typeEffect(midText, nextText, 0);
  }

  typeEffect(element, text, index) {
    if (index < text.length) {
      element.append(text[index]);
      setTimeout(() => {
        this.typeEffect(element, text, index + 1);
      }, 100);
    }
  }

  startTextLoop() {
    const textArray = ["Python", "Javascript", "React", "Next.js"];
    let currentIndex = 0;

    setInterval(() => {
      this.changeText(textArray, currentIndex);
      currentIndex = (currentIndex + 1) % textArray.length;
    }, 2000);
  }
}

new Component();
