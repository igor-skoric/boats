document.addEventListener("DOMContentLoaded", () => {
    const dropdowns = [
        { button: "servicesBtn1", menu: "servicesMenu1" },
        { button: "servicesBtn", menu: "servicesMenu" }
    ];

    let activeMenu = null; // Drži referencu na trenutno otvoren meni

    dropdowns.forEach(({ button, menu }) => {
        const btn = document.getElementById(button);
        const menuElement = document.getElementById(menu);

        btn.addEventListener("click", (event) => {
            event.stopPropagation(); // Sprečava zatvaranje menija kada kliknemo na dugme

            if (activeMenu && activeMenu !== menuElement) {
                activeMenu.style.maxHeight = "0"; // Zatvori prethodni meni
            }

            if (menuElement.style.maxHeight === "0px" || !menuElement.style.maxHeight) {
                menuElement.style.maxHeight = menuElement.scrollHeight + "px"; // Otvori meni
                activeMenu = menuElement;
            } else {
                menuElement.style.maxHeight = "0"; // Zatvori meni ako je već otvoren
                activeMenu = null;
            }
        });
    });

    // Klik van menija zatvara otvoreni meni
    document.addEventListener("click", () => {
        if (activeMenu) {
            activeMenu.style.maxHeight = "0";
            activeMenu = null;
        }
    });

    // Sprečava zatvaranje kada kliknemo unutar menija
    dropdowns.forEach(({ menu }) => {
        document.getElementById(menu).addEventListener("click", (event) => {
            event.stopPropagation();
        });
    });


    // Na scroll dodaj boju header-u


    window.addEventListener('DOMContentLoaded', function () {
      const header = document.getElementById('main-header');

      // Provera da li smo na home page-u (putanja je "/")
      if (window.location.pathname === '/') {
        window.addEventListener('scroll', function () {
          if (window.scrollY > 50) {
            header.classList.remove('bg-transparent');
            header.classList.add('bg-gray-800', 'shadow-md');
          } else {
            header.classList.add('bg-transparent');
            header.classList.remove('bg-gray-800', 'shadow-md');
          }
        });
      } else {
        // Na drugim stranicama uvek tamna pozadina
        header.classList.remove('bg-transparent');
        header.classList.add('bg-gray-800', 'shadow-md');
      }
    });


});
