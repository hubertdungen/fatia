<p align="center">
  <img src="fatia-logo.svg" width="110" alt="Fatia">
</p>

<h1 align="center">Fatia</h1>

<p align="center">
  3D printing price calculator — built on your slicer's own estimate.<br>
  <b>English</b> · <a href="README_pt.md">Português</a>
</p>

---

Feed it what your slicer already tells you — grams, time, cost — and Fatia gives you the price, your real profit, and a quote ready to send. One HTML file, no server, no account — and installable as an app in one click.

**[▶ Open Fatia](https://hubertdungen.github.io/fatia/)**

*"Fatia" is Portuguese for slice — both the slicer's kind and your slice of the profit.*

## Why

Most 3D printing calculators add up filament and electricity and stop there. That isn't your cost, it's a fraction of it. Missing: machine depreciation, the fixed setup work every plate needs, waste, packaging, and above all printer time — which is where long jobs quietly stop being profitable.

Fatia computes both sides in parallel: **what it costs you** and **what you charge**. The gap between them is your profit, and it's always on screen.

## What it does

**Slicer-first.** Every plate takes weight, time and a cost in euros. Fill in the cost and it wins — the weight calculation is skipped. A correction factor adjusts the estimate, because slicers only count the spool price, not supplier shipping or waste.

**Post-print reconciliation.** After printing, enter the real figures. Fatia shows the deviation and, when it's large, offers to remember it as the typical drift for future estimates. This is what stops the calculator from silently going stale.

**The plate as the unit of work.** A fixed fee and setup minutes per plate — slicing, prepping the bed, popping parts off. None of it depends on how many parts fit, which is exactly why filling the plate pays. A density readout quantifies how much.

**Market positioning.** Three gauges: machine hourly rate, price per part, price per plate. Reference figures were gathered in August 2026 and age themselves forward using the Bank of Portugal's inflation forecast. You can also paste competitor quotes for the same job, and log which of your own quotes were accepted or rejected.

**Real shipping.** 16 services with current prices: CTT registered mail, parcel post T1/T2 with and without home delivery, air freight to Madeira and the Azores, InPost lockers in Portugal and InPost to eight European countries. Packaging weight counts toward the bracket, because that's what the carrier weighs.

**Printer database.** 17 models with price, average draw and service life. Star your favourites, add your own, edit anything.

**Several printers in one job.** Each plate picks its own machine. The hourly cost is that machine's, and the total is the time-weighted average across plates. Reconcile the real print time and every plate scales by the same ratio — plain rule of three. The panel shows each machine's €/h and the resulting average.

**Client quote.** A clean printable view with a spec box and not a single margin in sight. Optionally:

- **the printers used** — one master switch, plus a per-plate tick for which ones show;
- **your brand** — logo, billing name, tax number, contacts, address, an italic tagline and a highlighted note to the client;
- **QR codes** — off by default. The QR is generated from whatever address you type, with no network and no third-party service, and any of them can be replaced by your own PNG/JPEG.

**Presets and memory.** Save named configurations, export and import as JSON. Everything goes into the template: per-plate printers, logo, copy and QR codes. It remembers where you left off.

**Simple mode.** Hides everything you aren't using. Click any panel heading to fold it.

## Running it

Open `index.html` in a browser. That's it.

**Install it as an app.** Served over `http(s)` — GitHub Pages or a local server — Fatia is a PWA: an **⤓ Install app** button appears, or use the browser menu (Chrome/Edge: ⋮ → *Install Fatia*; mobile: share → *Add to Home Screen*). It then opens in its own window, with an icon, and works offline.

Two features need the page served over `http(s)`: live electricity spot pricing and the data update check. Opened from disk as `file://`, browsers block all outbound requests and there is no way around it. Use GitHub Pages, or a local server:

```bash
python3 -m http.server 8000     # then open http://localhost:8000
```

## Reference data sources

| What | Source | Date |
| --- | --- | --- |
| Machine and labour hourly rates | [LayerMath](https://layermath.com/blog/3d-printing-hourly-rate) | Jun 2026 |
| Price per part in Portugal | [Zaask](https://www.zaask.pt/quanto-custa/impressao-3d) | 2026 |
| Inflation forecast | [Banco de Portugal](https://www.bportugal.pt/comunicado/comunicado-do-banco-de-portugal-sobre-o-boletim-economico-de-junho-de-2026) | Jun 2026 |
| CTT shipping | [CTT](https://www.ctt.pt/particulares/enviar/para-portugal/encomenda-postal) | Aug 2026 |
| InPost shipping | [InPost](https://www.inpost.pt/faz-um-envio/nossas-tarifas-de-envio) | Aug 2026 |
| Electricity spot price | [energy-charts.info](https://api.energy-charts.info/) (OMIE / PT zone) | live |

These are **informational estimates, not quotations.** Verify them before relying on any figure in a real quote.

## Updating the bundled data

`dados.json` holds the market benchmark, carrier tariffs and printer list. The app fetches it on load when served over http(s), so editing that one file updates every deployed copy. Bump its `data` field when you change it.

## Licence

**Personal use — free.** Use, copy and modify it however you like for personal projects, learning and non-commercial work.

**Commercial use — by prior arrangement.** If you use Fatia to price work you sell:

| Monthly revenue | Fee |
| --- | --- |
| Up to €10,000 | €10/month |
| Above €10,000 | €100/month |

Contact **hubertkenobi@gmail.com** before you start. Full terms in [`LICENSE`](LICENSE); a Portuguese translation is in [`LICENCA.md`](LICENCA.md).

---

<p align="center">
  <i>Fatia — powered by <b>DL X</b></i><br>
  <sub><i>DL X is the research and product division of <b>DungenLabs</b>, an engineering lab in Lisbon —
  the half of the lab that builds for itself: experimental prototypes, in-house manufactured products
  (FDM extrusion, fibre-reinforced filament and resin casting), partnerships, and technology looking
  for a use.</i></sub><br>
  <sub><a href="https://dlx.dungenlabs.com">dlx.dungenlabs.com</a> · <a href="https://dungenlabs.com">dungenlabs.com</a></sub>
</p>
