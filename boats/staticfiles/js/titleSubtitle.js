document.addEventListener("DOMContentLoaded", function () {
    const accordions = document.querySelectorAll(".accordion-btn");

    accordions.forEach((btn) => {
        btn.addEventListener("click", function () {
            const content = this.nextElementSibling;
            const icon = this.querySelector(".icon");

            if (content.style.maxHeight) {
                content.style.maxHeight = null;
                icon.textContent = "+";
            } else {
                document.querySelectorAll(".accordion-content").forEach((el) => {
                    el.style.maxHeight = null;
                    el.previousElementSibling.querySelector(".icon").textContent = "+";
                });

                content.style.maxHeight = content.scrollHeight + "px";
                icon.textContent = "−";
            }
        });
    });
});
