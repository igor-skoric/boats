document.addEventListener("DOMContentLoaded", () => {

    document.querySelector('.scroll-to-top').addEventListener('click', function (e) {
        e.preventDefault();
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      });

});