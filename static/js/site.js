const initMobileMenu = () => {
  const mobileMenuButton = document.getElementById('mobileMenuButton');
  const mobileMenu = document.getElementById('mobileMenu');

  if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener('click', () => {
      const expanded = mobileMenuButton.getAttribute('aria-expanded') === 'true';
      mobileMenuButton.setAttribute('aria-expanded', String(!expanded));
      mobileMenu.classList.toggle('hidden');
    });
  }
};

const initCarousel = () => {
  const carousel = document.getElementById('heroCarousel');
  if (!carousel) return;

  const track = carousel.querySelector('.carousel-track');
  const slides = track ? Array.from(track.children) : [];
  const dots = Array.from(carousel.querySelectorAll('[data-carousel-dot]'));
  const prevBtn = carousel.querySelector('[data-carousel-prev]');
  const nextBtn = carousel.querySelector('[data-carousel-next]');

  if (!track || slides.length === 0) return;

  let current = 0;
  let timer = null;

  const goTo = (index) => {
    current = (index + slides.length) % slides.length;
    track.style.transform = `translateX(-${current * 100}%)`;
    dots.forEach((dot, dotIndex) => {
      dot.classList.toggle('is-active', dotIndex === current);
    });
  };

  const next = () => goTo(current + 1);
  const prev = () => goTo(current - 1);

  if (nextBtn) nextBtn.addEventListener('click', next);
  if (prevBtn) prevBtn.addEventListener('click', prev);

  dots.forEach((dot) => {
    dot.addEventListener('click', () => {
      const index = Number(dot.getAttribute('data-carousel-dot'));
      goTo(index);
    });
  });

  const startAutoplay = () => {
    if (timer) clearInterval(timer);
    timer = setInterval(next, 5500);
  };

  carousel.addEventListener('mouseenter', () => {
    if (timer) clearInterval(timer);
  });

  carousel.addEventListener('mouseleave', startAutoplay);

  goTo(0);
  startAutoplay();
};

const initRadarFilters = () => {
  const root = document.querySelector('[data-radar-filter-root]');
  if (!root) return;

  const cards = Array.from(root.querySelectorAll('[data-radar-card]'));
  const purposeInputs = Array.from(root.querySelectorAll('[data-radar-purpose]'));
  const architectureSelect = root.querySelector('[data-radar-architecture]');
  const resetButton = root.querySelector('[data-radar-reset]');
  const resultsCount = Array.from(root.querySelectorAll('[data-radar-results-count]'));
  const resultsSummary = root.querySelector('[data-radar-results-summary]');
  const emptyState = root.querySelector('[data-radar-empty-state]');
  const cardGrid = root.querySelector('[data-radar-card-grid]');
  const totalCount = cards.length;

  if (!cards.length || !architectureSelect || !purposeInputs.length) return;

  const getSelectedPurposes = () =>
    purposeInputs
      .filter((input) => input.checked)
      .map((input) => input.value.toLowerCase());

  const applyFilters = () => {
    const selectedPurposes = getSelectedPurposes();
    const selectedArchitecture = architectureSelect.value.toLowerCase();
    let visibleCount = 0;

    cards.forEach((card) => {
      const cardPurpose = (card.getAttribute('data-purpose') || '').toLowerCase();
      const cardArchitecture = (card.getAttribute('data-architecture') || '').toLowerCase();
      const matchesPurpose = selectedPurposes.includes(cardPurpose);
      const matchesArchitecture = selectedArchitecture === 'all' || cardArchitecture === selectedArchitecture;
      const isVisible = matchesPurpose && matchesArchitecture;

      card.classList.toggle('hidden', !isVisible);
      card.setAttribute('aria-hidden', String(!isVisible));

      if (isVisible) visibleCount += 1;
    });

    resultsCount.forEach((node) => {
      node.textContent = String(visibleCount);
    });

    if (resultsSummary) {
      const architectureLabel = selectedArchitecture === 'all'
        ? 'all architectures'
        : `architecture ${selectedArchitecture.toUpperCase()}`;

      if (selectedPurposes.length === 0) {
        resultsSummary.textContent = 'No detection type is selected. Enable at least one option to show matching models.';
      } else {
        const purposeLabel = selectedPurposes
          .map((value) => (value === 'g' ? 'ground target' : 'air target'))
          .join(' + ');
        resultsSummary.textContent = `Showing ${visibleCount} of ${totalCount} models for ${purposeLabel} and ${architectureLabel}.`;
      }
    }

    if (emptyState) {
      emptyState.classList.toggle('hidden', visibleCount !== 0);
    }

    if (cardGrid) {
      cardGrid.classList.toggle('hidden', visibleCount === 0);
    }
  };

  purposeInputs.forEach((input) => {
    input.addEventListener('change', applyFilters);
  });

  architectureSelect.addEventListener('change', applyFilters);

  if (resetButton) {
    resetButton.addEventListener('click', () => {
      purposeInputs.forEach((input) => {
        input.checked = true;
      });
      architectureSelect.value = 'all';
      applyFilters();
    });
  }

  applyFilters();
};

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();

  initCarousel();
  initRadarFilters();
});
