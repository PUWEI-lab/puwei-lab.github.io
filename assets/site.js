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
  document.addEventListener('keydown', event => {
    const menu = document.querySelector('.mobile-menu[open]');
    if (event.key === 'Escape' && menu && !document.querySelector('dialog[open]')) {
      menu.open = false;
      menu.querySelector('summary').focus();
    }
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
  dialog.innerHTML = '<button class="lightbox-close" aria-label="關閉圖片">關閉 Close ×</button><button class="lightbox-prev" aria-label="上一張圖片">←</button><figure><img alt="" draggable="false"><p class="lightbox-status" role="status"></p><figcaption aria-live="polite"></figcaption><a class="lightbox-original" target="_blank" rel="noopener noreferrer">開啟圖片 ↗</a></figure><button class="lightbox-next" aria-label="下一張圖片">→</button>';
  document.body.append(dialog);
  const unique = [...new Map(links.map(link => [link.href, link])).values()];
  const picture = dialog.querySelector('img');
  const caption = dialog.querySelector('figcaption');
  const status = dialog.querySelector('.lightbox-status');
  const original = dialog.querySelector('.lightbox-original');
  function loaded() {
    picture.hidden = false;
    status.hidden = true;
  }
  picture.addEventListener('load', loaded);
  picture.addEventListener('error', () => {
    picture.hidden = true;
    status.hidden = false;
    status.textContent = '圖片暫時無法載入，請稍後再試，或點選下方連結開啟圖片。';
  });
  let current = 0;
  let opener = null;
  function show(index) {
    current = (index + unique.length) % unique.length;
    const link = unique[current];
    picture.hidden = true;
    status.hidden = false;
    status.textContent = '圖片載入中…';
    original.href = link.href;
    picture.src = link.href;
    picture.alt = link.querySelector('img')?.alt || '';
    const credit = link.closest('figure')?.querySelector('figcaption')?.textContent?.trim();
    caption.textContent = `${current + 1} / ${unique.length}${link.dataset.caption ? ' — ' + link.dataset.caption : ''}${credit ? '｜' + credit : ''}`;
    if (picture.complete && picture.naturalWidth > 0) loaded();
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
    status.hidden = true;
    opener?.focus({preventScroll: true});
  });
  let gesture = null;
  const frame = dialog.querySelector('figure');
  frame.addEventListener('pointerdown', event => {
    if (event.pointerType === 'touch' && event.isPrimary) {
      gesture = {id: event.pointerId, x: event.clientX, y: event.clientY};
    }
  });
  frame.addEventListener('pointercancel', () => { gesture = null; });
  frame.addEventListener('pointerup', event => {
    if (!gesture || event.pointerId !== gesture.id) return;
    const dx = event.clientX - gesture.x;
    const dy = event.clientY - gesture.y;
    gesture = null;
    if (unique.length > 1 && Math.abs(dx) >= 50 && Math.abs(dx) > Math.abs(dy) * 1.25) {
      show(current + (dx < 0 ? 1 : -1));
    }
  });
})();
