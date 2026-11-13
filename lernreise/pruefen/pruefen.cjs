// Prüft die gebaute Lernreise (site/) in Chromium und WebKit. Aufruf: node lernreise/pruefen/pruefen.cjs
// Playwright kommt aus janrummel-eu/werkzeug; außerhalb der Sandbox starten (Chromium braucht Mach-Ports).
const os = require('os'), fs = require('fs'), path = require('path');
const { chromium, webkit, devices } = require(path.join(os.homedir(), 'Projects/janrummel-eu/werkzeug/node_modules/playwright'));
const SITE = path.join(__dirname, '..', '..', 'site');
const BASE = 'http://lr.test/ai-fluency/';
const typ = {'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.woff2':'font/woff2','.png':'image/png','.svg':'image/svg+xml','.pdf':'application/pdf','.xml':'application/xml','.txt':'text/plain'};
async function route(ctx){ await ctx.route('**/*', async r => { const u = new URL(r.request().url());
  if (u.host !== 'lr.test') return r.abort();
  let p = decodeURIComponent(u.pathname).replace(/^\/ai-fluency/, ''); if (p.endsWith('/')) p += 'index.html';
  const f = path.join(SITE, p);
  if (fs.existsSync(f) && fs.statSync(f).isFile()) return r.fulfill({status:200, body:fs.readFileSync(f), contentType:typ[path.extname(f)]||'application/octet-stream'});
  return r.fulfill({status:404, body:fs.readFileSync(path.join(SITE,'404.html')), contentType:typ['.html']}); }); }
const SEITEN = ['de/','de/karte/','de/etappe-1/aufgabe-waehlen/','de/etappe-1/konto-und-daten/','de/etappe-1/erste-anfrage/','de/etappe-2/anfrage-bauen/','de/etappe-2/dokument-pruefen/','de/etappe-2/in-runden/','de/etappe-3/gegen-die-quelle/','de/etappe-3/websuche/','de/etappe-3/gegenlesen/','de/etappe-4/daueranweisung/','de/etappe-4/projekte/','de/etappe-4/ablage-und-regeln/','de/etappe-5/ausblick-agenten/','en/','','de/l1-first-steps/01-what-is-ai/'];
(async () => { let fehler = 0;
 for (const [n, bt, o] of [['desktop', chromium, {viewport:{width:1280,height:900}}], ['iphone', webkit, devices['iPhone 13']], ['dunkel', chromium, {viewport:{width:1280,height:900}, colorScheme:'dark'}]]) {
  const b = await bt.launch();
  for (const s of SEITEN) { const ctx = await b.newContext(o); await route(ctx); const p = await ctx.newPage(); const e = [];
   p.on('pageerror', x => e.push('js:' + x.message));
   p.on('console', m => { if (m.type()==='error' && !/goatcounter|count\.js|ERR_FAILED|net::|404/.test(m.text())) e.push('console:' + m.text()); });
   await p.goto(BASE + s, {waitUntil:'load'}); await p.waitForTimeout(300);
   const ue = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
   if (ue > 0) e.push('Querüberlauf ' + ue + 'px');
   if (e.length) { fehler += e.length; console.log('FEHLER', n, s, e.join(' | ')); }
   await ctx.close(); }
  await b.close(); }
 // Werkzeugwahl wird gemerkt
 const b = await chromium.launch(); const ctx = await b.newContext(); await route(ctx); const p = await ctx.newPage();
 await p.goto(BASE + 'de/etappe-1/erste-anfrage/'); await p.click('#tab-4');
 await p.goto(BASE + 'de/etappe-4/daueranweisung/'); await p.waitForTimeout(200);
 const sel = await p.evaluate(() => [document.querySelector('#tab-4').getAttribute('aria-selected'), document.getElementById('panel-4').hidden, document.getElementById('panel-1').hidden]);
 const ok = sel[0]==='true' && sel[1]===false && sel[2]===true;
 console.log('Werkzeug gemerkt:', ok ? 'ja' : 'NEIN ' + JSON.stringify(sel)); if (!ok) fehler++;
 await b.close();
 console.log(fehler ? `ROT: ${fehler} Befunde` : 'GRÜN: 18 Adressen x 3 Ansichten, Werkzeugwahl gemerkt');
 process.exit(fehler ? 1 : 0); })();
