document.addEventListener("DOMContentLoaded", () => {

    /* ============================================
       BUTTON LOADING
    ============================================ */

    const form = document.querySelector("form");
    const runBtn = document.getElementById("runBtn");
    const btnText = document.getElementById("btnText");
    const spinner = document.getElementById("loadingSpinner");

    if (form) {

        form.addEventListener("submit", () => {

            if (runBtn) {

                runBtn.disabled = true;

                runBtn.classList.add("disabled");

            }

            if (spinner) {

                spinner.classList.remove("d-none");

            }

            if (btnText) {

                btnText.innerHTML =
                    '<i class="bi bi-cpu-fill"></i> Running Quantum Simulation...';

            }

        });

    }

    /* ============================================
       ATTACK PROGRESS BAR
    ============================================ */

    const progress = document.querySelector(".attack-detection-progress");

    if (progress) {

        const attack = Number(progress.dataset.attackPercentage || 0);

        progress.style.width = "0%";

        setTimeout(() => {

            progress.style.width = attack + "%";

        }, 300);

    }

    /* ============================================
       ANIMATED COUNTERS
    ============================================ */

    function animateCounter(element) {

        const target = parseFloat(
            element.textContent.replace("%", "")
        );

        if (isNaN(target)) return;

        let current = 0;

        const duration = 1200;

        const increment = target / (duration / 20);

        const timer = setInterval(() => {

            current += increment;

            if (current >= target) {

                current = target;

                clearInterval(timer);

            }

            if (element.textContent.includes("%")) {

                element.textContent = current.toFixed(1) + "%";

            } else {

                element.textContent = Math.round(current);

            }

        }, 20);

    }

    document.querySelectorAll(".metric-card h2,.metric-card h3").forEach(el => {

        animateCounter(el);

    });

    /* ============================================
       FLOATING METRIC CARDS
    ============================================ */

    document.querySelectorAll(".metric-card").forEach((card, index) => {

        card.style.animationDelay = `${index * 0.2}s`;

    });

    /* ============================================
       CARD HOVER EFFECT
    ============================================ */

    document.querySelectorAll(".card").forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-8px)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "";

        });

    });

    /* ============================================
       GRAPH FADE-IN
    ============================================ */

    const graphImages = document.querySelectorAll(".graph-card img");

    graphImages.forEach((img, index) => {

        img.style.opacity = "0";

        img.style.transform = "translateY(20px)";

        img.style.transition = ".7s";

        setTimeout(() => {

            img.style.opacity = "1";

            img.style.transform = "translateY(0px)";

        }, 300 + (index * 150));

    });

    /* ============================================
       HERO FADE
    ============================================ */

    const hero = document.querySelector(".hero");

    if (hero) {

        hero.style.opacity = "0";

        hero.style.transform = "translateY(25px)";

        hero.style.transition = ".8s";

        setTimeout(() => {

            hero.style.opacity = "1";

            hero.style.transform = "translateY(0px)";

        }, 100);

    }

    /* ============================================
       NODE GLOW
    ============================================ */

    document.querySelectorAll(".quantum-node").forEach(node => {

        node.addEventListener("mouseenter", () => {

            node.style.boxShadow =
                "0 0 30px rgba(0,217,255,.45)";

        });

        node.addEventListener("mouseleave", () => {

            node.style.boxShadow = "";

        });

    });

    /* ============================================
       SCROLL ANIMATION
    ============================================ */

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.style.opacity = "1";

                entry.target.style.transform = "translateY(0px)";

            }

        });

    }, {

        threshold: 0.15

    });

    document.querySelectorAll(".card").forEach(card => {

        card.style.opacity = "0";

        card.style.transform = "translateY(30px)";

        card.style.transition = ".7s";

        observer.observe(card);

    });

    /* ============================================
       LIVE CLOCK
    ============================================ */

    function updateClock() {

        const clock = document.getElementById("liveClock");

        if (!clock) return;

        const now = new Date();

        clock.innerHTML = now.toLocaleTimeString();

    }

    updateClock();

    setInterval(updateClock, 1000);

    /* ============================================
       RANDOM GLOW PULSE
    ============================================ */

    setInterval(() => {

        document.querySelectorAll(".metric-icon").forEach(icon => {

            icon.style.transform = "scale(1.1)";

            setTimeout(() => {

                icon.style.transform = "scale(1)";

            }, 350);

        });

    }, 3000);

    /* ============================================
       BUTTON RIPPLE
    ============================================ */

    document.querySelectorAll(".btn").forEach(button => {

        button.addEventListener("mouseenter", () => {

            button.style.transform = "translateY(-2px)";

        });

        button.addEventListener("mouseleave", () => {

            button.style.transform = "";

        });

    });

});
