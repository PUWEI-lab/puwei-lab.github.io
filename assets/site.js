// Text navigation works without JavaScript; enhance active in-page links.
(() => {
  function updateLocation() {
    const id = location.hash.slice(1);
    document.querySelectorAll('[data-work-anchor]').forEach(link => {
      const target = new URL(link.href);
      if (target.pathname !== location.pathname) return;
      const selected = id && link.dataset.workAnchor === id;
      if (selected) {
        link.setAttribute('aria-current', 'location');
        for (let parent = link.parentElement; parent; parent = parent.parentElement) {
          if (parent.matches('.section-nav, .series-nav')) parent.open = true;
        }
      } else link.removeAttribute('aria-current');
    });
  }
  updateLocation();
  window.addEventListener('hashchange', updateLocation);
  document.querySelectorAll('.mobile-menu a').forEach(link => {
    link.addEventListener('click', () => { link.closest('.mobile-menu').open = false; });
  });
})();

// Every page and full-size image link works without JavaScript.
// This optional viewer adds keyboard navigation and focus restoration.
(() => {
  const links = [...document.querySelectorAll('a[data-lightbox]')];
  if (!links.length || typeof HTMLDialogElement === 'undefined') return;
  const dialog = document.createElement('dialog');
  dialog.className = 'lightbox';
  dialog.setAttribute('aria-label', '作品圖片檢視');
  dialog.innerHTML = '<button class="lightbox-close" aria-label="關閉圖片">關閉 Close ×</button><button class="lightbox-prev" aria-label="上一張圖片">←</button><figure><img alt=""><figcaption aria-live="polite"></figcaption></figure><button class="lightbox-next" aria-label="下一張圖片">→</button>';
  document.body.append(dialog);
  const unique = [...new Map(links.map(link => [link.href, link])).values()];
  const picture = dialog.querySelector('img');
  const caption = dialog.querySelector('figcaption');
  let current = 0;
  let opener = null;
  function show(index) {
    current = (index + unique.length) % unique.length;
    const link = unique[current];
    picture.src = link.href;
    picture.alt = link.querySelector('img')?.alt || '';
    caption.textContent = `${current + 1} / ${unique.length}${link.dataset.caption ? ' — ' + link.dataset.caption : ''}`;
    dialog.querySelector('.lightbox-prev').hidden = unique.length < 2;
    dialog.querySelector('.lightbox-next').hidden = unique.length < 2;
  }
  links.forEach(link => link.addEventListener('click', event => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    opener = link;
    show(unique.findIndex(item => item.href === link.href));
    dialog.showModal();
    document.body.classList.add('modal-open');
  }));
  dialog.querySelector('.lightbox-close').addEventListener('click', () => dialog.close());
  dialog.querySelector('.lightbox-prev').addEventListener('click', () => show(current - 1));
  dialog.querySelector('.lightbox-next').addEventListener('click', () => show(current + 1));
  dialog.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft') { event.preventDefault(); show(current - 1); }
    if (event.key === 'ArrowRight') { event.preventDefault(); show(current + 1); }
  });
  dialog.addEventListener('close', () => {
    document.body.classList.remove('modal-open');
    picture.removeAttribute('src');
    opener?.focus({preventScroll: true});
  });
})();
