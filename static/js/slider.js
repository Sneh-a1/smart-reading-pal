const sliders = {};

function getPerPage() {
  const width = window.innerWidth;
  if (width >= 1024) return 6;
  if (width >= 768) return 4;
  return 2;
}

function slideRight(id) {
  const slider = document.getElementById(`slider-${id}`);
  const items = slider.children;
  const perPage = getPerPage();

  if (!sliders[id]) sliders[id] = 0;

  const maxSlide = Math.ceil(items.length / perPage) - 1;

  if (sliders[id] < maxSlide) {
    sliders[id]++;
    updateSlider(slider, sliders[id], perPage);
  }
}

function slideLeft(id) {
  const slider = document.getElementById(`slider-${id}`);
  const perPage = getPerPage();

  if (!sliders[id]) sliders[id] = 0;

  if (sliders[id] > 0) {
    sliders[id]--;
    updateSlider(slider, sliders[id], perPage);
  }
}

function updateSlider(slider, index, perPage) {
  const percentage = 100 / perPage;
  slider.style.transform = `translateX(-${index * percentage}%)`;
}

window.addEventListener('resize', () => {
  for (let id in sliders) {
    sliders[id] = 0;
    const slider = document.getElementById(`slider-${id}`);
    if (slider) slider.style.transform = 'translateX(0)';
  }
});
