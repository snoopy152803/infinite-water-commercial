// service-worker.js — minimal app-shell cache.
// A service worker is a technical requirement for browsers to consider a
// site "installable" (alongside the manifest). This one just caches the
// core files so the app still opens if you're offline.

const CACHE_NAME = 'eternalflow-v1';
const APP_SHELL = [
  '/',
  '/style.css',
  '/manifest.json',
  '/icon-192.png',
  '/icon-512.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(APP_SHELL))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((names) =>
      Promise.all(names.filter((n) => n !== CACHE_NAME).map((n) => caches.delete(n)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  // Cache-first for the app shell, network fallback for everything else.
  event.respondWith(
    caches.match(event.request).then((cached) => cached || fetch(event.request))
  );
});
