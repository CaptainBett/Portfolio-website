/*-- default-swiper --*/

var swiper = new Swiper('#default-swiper', {
  slidesPerView: 3,
  spaceBetween: 15,
  loop: true,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  breakpoints: {
    '@0.25': {
      slidesPerView: 1,
    },
    '@0.5': {
      slidesPerView: 2,
    },
    '@1.00': {
      slidesPerView: 3,
    },
  }
});



/*-- logo-swiper --*/

var swiper = new Swiper('#logo-swiper', {
  slidesPerView: 5,
  spaceBetween: 60,
  loop: true,
  speed: 1200,
  pagination: false,
  autoplay: {
    delay: 3500,
    disableOnInteraction: false,
  },
  breakpoints: {
    '@0.25': {
      slidesPerView: 2,
    },
    '@0.5': {
      slidesPerView: 3,
    },
    '@1.00': {
      slidesPerView: 5,
    },
  }
});



/*-- fullwidth-swiper --*/

var swiper = new Swiper('#fullwidth-swiper', {
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  keyboard: true,
});



/*-- fullwidth-nav-swiper --*/

var swiper = new Swiper('#fullwidth-nav-swiper', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  keyboard: true,
});



/*-- flow-swiper --*/

var swiper = new Swiper('#flow-swiper', {
  effect: 'coverflow',
  grabCursor: true,
  loop: true,
  coverflowEffect: {
    rotate: 50,
    stretch: 0,
    depth: 100,
    modifier: 1,
    slideShadows: true,
  },
  breakpoints: {
    '@0.25': {
      centeredSlides: true,
      slidesPerView: "auto",
    },
    '@0.75': {
      centeredSlides: false,
      slidesPerView: 3,
    },
  },
  pagination: {
    el: '.swiper-pagination',
  },
});



/*-- vertical-swiper --*/

var swiper = new Swiper('#vertical-swiper', {
  direction: 'vertical',
  slidesPerView: 1,
  mousewheel: true,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
});



/*-- product-swiper --*/

var swiper = new Swiper('#product-swiper', {
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  keyboard: true,
});