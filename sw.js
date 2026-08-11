/* Fatia — service worker.
   A app tem de abrir sem rede: o essencial fica em cache.
   A página em si vai primeiro à rede, para que uma versão nova apareça sem truques. */
const CACHE = 'fatia-1.3.0';
const SHELL = ['./', './index.html', './manifest.webmanifest',
               './icon-192.png', './icon-512.png', './fatia-logo.svg'];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => Promise.all(SHELL.map(u => c.add(u).catch(() => {}))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

const guarda = (req, res) => {
  const copia = res.clone();
  caches.open(CACHE).then(c => c.put(req, copia)).catch(() => {});
  return res;
};

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;   /* preço da eletricidade vai sempre à rede */
  if (url.pathname.startsWith('/api/')) {
    e.respondWith(fetch(req));
    return;
  }

  /* página e dados de mercado: rede primeiro, cache como rede de segurança */
  if (req.mode === 'navigate' || url.pathname.endsWith('.json') || url.pathname.endsWith('.webmanifest')) {
    e.respondWith(
      fetch(req).then(r => guarda(req, r))
                .catch(() => caches.match(req).then(r => r || caches.match('./index.html')))
    );
    return;
  }

  /* restantes ficheiros: cache primeiro */
  e.respondWith(
    caches.match(req).then(r => r || fetch(req).then(res => guarda(req, res)))
  );
});
