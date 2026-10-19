// All content and work details are accessible without JavaScript.
document.getElementById('year').textContent = new Date().getFullYear();
function updateNavigation() {
  document.querySelectorAll('nav a').forEach(link => {
    const active = link.hash === location.hash || (link.hash === '#works' && location.hash.startsWith('#work-'));
    if (active) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
}
window.addEventListener('hashchange', updateNavigation);
updateNavigation();
