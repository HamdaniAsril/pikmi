// pikmi landing page: reads the catalog so the page follows whatever styles the repo ships.

const SKILL = 'skills/pikmi/';
const $ = (selector) => document.querySelector(selector);
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');

const MEDIA_NAMES = { ui: 'web', slides: 'slides', social: 'social', app: 'app' };
const LANGUAGE_NAMES = { en: 'english', id: 'indonesian' };
// filler words people type around a mood ("make it look like ...", "bikin kayak ...")
const FILLER = new Set(['a', 'an', 'and', 'the', 'it', 'its', 'make', 'like', 'look', 'looks', 'style', 'styles', 'with', 'for', 'of', 'to', 'in',
  'bikin', 'buat', 'kayak', 'ala', 'yang', 'dan', 'gaya', 'tampilan', 'desain', 'jadi', 'seperti']);

const state = { styles: [], current: -1, filter: 'all', query: '' };

// theme switch
const themeSwitch = $('#theme-switch');
function setTheme(dark) {
  if (dark) document.documentElement.dataset.theme = 'dark';
  else delete document.documentElement.dataset.theme;
  themeSwitch.setAttribute('aria-checked', String(dark));
}
setTheme(document.documentElement.dataset.theme === 'dark');
themeSwitch.addEventListener('click', () => {
  const dark = themeSwitch.getAttribute('aria-checked') !== 'true';
  setTheme(dark);
  try { localStorage.setItem('pikmi-theme', dark ? 'dark' : 'light'); } catch (e) {}
});

// copy keys
document.querySelectorAll('[data-copy]').forEach((button) => {
  const label = button.querySelector('.k-label');
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(button.dataset.copy);
      label.textContent = 'copied';
    } catch (e) {
      label.textContent = 'select it';
    }
    setTimeout(() => { label.textContent = 'copy'; }, 1600);
  });
});

// catalog
async function readCatalog() {
  const response = await fetch(SKILL + 'catalog.json');
  if (!response.ok) throw new Error(`catalog.json: ${response.status}`);
  const catalog = await response.json();
  return Promise.all(catalog.styles.map(async (style, i) => {
    const folder = SKILL + style.preview.replace(/[^/]*$/, '');
    let tokens = null;
    try {
      const r = await fetch(folder + 'tokens.json');
      if (r.ok) tokens = await r.json();
    } catch (e) {}
    const words = [style.name, style.id, style.summary, ...(style.keywords?.en ?? []), ...(style.keywords?.id ?? [])];
    return {
      ...style,
      number: String(i + 1).padStart(2, '0'),
      href: SKILL + style.preview,
      tokens,
      haystack: words.join(' ').toLowerCase(),
    };
  }));
}

function palette(style) {
  const theme = style.tokens?.themes?.[style.themes[0]];
  if (!theme) return [];
  return [['page', theme.page], ['text', theme.text], ['accent', theme.accent]].filter(([, hex]) => hex);
}

function fonts(style) {
  const families = Object.values(style.tokens?.fonts ?? {}).map((font) => font.family);
  return [...new Set(families)];
}

function el(tag, props = {}, children = []) {
  const node = Object.assign(document.createElement(tag), props);
  node.append(...children);
  return node;
}

function arrowIcon() {
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('viewBox', '0 0 10 10');
  svg.setAttribute('width', '8');
  svg.setAttribute('height', '8');
  svg.setAttribute('aria-hidden', 'true');
  svg.innerHTML = '<path d="M2 8l6-6m-4.5 0h4.5v4.5"/>';
  return svg;
}

// search and theme filter
function matches(style) {
  if (state.filter !== 'all' && !style.themes.includes(state.filter)) return false;
  const query = state.query.trim().toLowerCase();
  if (!query || style.haystack.includes(query)) return true;
  const words = query.split(/[\s,]+/).filter((w) => w.length > 1 && !FILLER.has(w));
  return words.some((w) => style.haystack.includes(w));
}

function visibleStyles() {
  return state.styles.map((style, index) => ({ style, index })).filter(({ style }) => matches(style));
}

// the picker device
const viewport = $('#viewport');
const frame = $('#preview-frame');
const screenMsg = $('#screen-msg');

function fitFrame() {
  const width = viewport.clientWidth;
  const base = width < 560 ? 480 : 1280;
  const scale = width / base;
  frame.style.width = `${base}px`;
  frame.style.height = `${viewport.clientHeight / scale}px`;
  frame.style.transform = `scale(${scale})`;
}
new ResizeObserver(fitFrame).observe(viewport);

function showMessage(big, small = '') {
  screenMsg.querySelector('.msg-big').textContent = big;
  screenMsg.querySelector('.msg-small').textContent = small;
  screenMsg.hidden = false;
}

function setStatus(text, live) {
  $('#status-text').textContent = text;
  $('#device-status .led').classList.toggle('on', live);
}

frame.addEventListener('load', () => {
  if (!frame.getAttribute('src')) return;
  // same origin: hide the preview's own scrollbar, it reads as noise at this scale
  try { frame.contentDocument.documentElement.style.scrollbarWidth = 'none'; } catch (e) {}
  screenMsg.hidden = true;
  setStatus('live preview', true);
});

function select(index) {
  const style = state.styles[index];
  if (!style || index === state.current) return;
  state.current = index;

  document.querySelectorAll('#device-keys .key[data-index]').forEach((k) => {
    k.setAttribute('aria-pressed', String(Number(k.dataset.index) === index));
  });

  $('#readout-num').textContent = style.number;
  $('#readout-of').textContent = `/${String(state.styles.length).padStart(2, '0')}`;
  $('#readout-name').textContent = style.name;
  $('#readout-themes').textContent = style.themes.join(' · ');
  const open = $('#open-preview');
  open.href = style.href;
  open.querySelector('.sr')?.remove();
  open.append(el('span', { className: 'sr', textContent: ` of ${style.name}` }));

  showMessage('loading', style.name);
  setStatus('loading', false);
  frame.title = `Preview of the ${style.name} style`;
  frame.src = style.href;

  // the offer card and marker in "how it works" follow the picked style
  $('#offer-name').textContent = style.name;
  $('#offer-themes').textContent = style.themes.join(', ');
  const colors = palette(style);
  $('#offer-palette').textContent = colors.length ? colors.map(([role, hex]) => `${hex.toUpperCase()} ${role}`).join(' · ') : 'see tokens.json';
  $('#offer-fonts').textContent = fonts(style).join(' / ') || 'see tokens.json';
  $('#marker').textContent = `/* pikmi: ${style.id} */`;
}

function randomFrom(indexes) {
  const pool = indexes.length > 1 ? indexes.filter((i) => i !== state.current) : indexes;
  return pool[Math.floor(Math.random() * pool.length)];
}

function showOnPanel(index) {
  select(index);
  $('#picker').scrollIntoView({ behavior: reduceMotion.matches ? 'auto' : 'smooth', block: 'start' });
}

function renderKeys() {
  const shown = visibleStyles();
  const keys = shown.map(({ style, index }) => {
    const key = el('button', { type: 'button', className: 'key skey' }, [
      el('span', { className: 'skey-top' }, [
        el('span', { textContent: style.number }),
        el('span', { textContent: style.themes.join(' · ') }),
      ]),
      el('span', { className: 'skey-name', textContent: style.name }),
    ]);
    key.dataset.index = index;
    key.setAttribute('aria-pressed', String(index === state.current));
    key.addEventListener('click', () => select(index));
    return key;
  });

  const random = el('button', { type: 'button', className: 'key alt skey' }, [
    el('span', { className: 'skey-top', textContent: '??' }),
    el('span', { className: 'skey-name', textContent: 'random' }),
  ]);
  random.setAttribute('aria-label', shown.length ? 'Random style from this list' : 'Random style');
  random.addEventListener('click', () => {
    const pool = shown.length ? shown.map(({ index }) => index) : state.styles.map((s, i) => i);
    select(randomFrom(pool));
  });

  const message = shown.length ? [] : [el('p', { className: 'grid-msg', textContent: `No style matches “${state.query.trim()}”. Try another mood, or press random.` })];
  $('#device-keys').replaceChildren(...keys, ...message, random);
  $('#result-count').textContent = `${shown.length} ${shown.length === 1 ? 'style' : 'styles'}`;
}

function renderCounts() {
  $('#count-all').textContent = state.styles.length;
  $('#count-light').textContent = state.styles.filter((s) => s.themes.includes('light')).length;
  $('#count-dark').textContent = state.styles.filter((s) => s.themes.includes('dark')).length;
}

function renderSpecs() {
  const media = [...new Set(state.styles.flatMap((s) => s.media))];
  const langs = [...new Set(state.styles.flatMap((s) => Object.keys(s.keywords ?? {})))];
  $('#spec-styles').textContent = state.styles.length;
  $('#spec-media').textContent = media.length;
  $('#spec-media-list').textContent = media.map((m) => MEDIA_NAMES[m] ?? m).join(' · ');
  if (!state.styles.every((s) => s.media.length === media.length)) {
    $('#spec-media').nextElementSibling.firstChild.textContent = 'media';
  }
  $('#spec-langs').textContent = langs.length;
  $('#spec-langs-list').textContent = langs.map((l) => LANGUAGE_NAMES[l] ?? l).join(' · ');
}

function renderCards() {
  const cards = state.styles.map((style, i) => {
    const colors = palette(style);
    const swatches = el('span', { className: 'palette' }, colors.map(([role, hex]) => {
      const chip = el('span', { title: `${hex.toUpperCase()} ${role}` });
      chip.style.background = hex;
      return chip;
    }));
    swatches.setAttribute('role', 'img');
    swatches.setAttribute('aria-label', 'Palette: ' + colors.map(([role, hex]) => `${role} ${hex}`).join(', '));

    const numberKey = el('button', { type: 'button', className: 'key num-key hit', textContent: style.number });
    numberKey.setAttribute('aria-label', `Show ${style.name} on the panel`);
    numberKey.addEventListener('click', () => showOnPanel(i));

    const themes = ['light', 'dark'].map((t) => {
      const on = style.themes.includes(t);
      return el('span', { className: on ? 'theme' : 'theme off' }, [
        el('span', { className: on ? 'led on' : 'led' }),
        el('span', { textContent: t }),
        el('span', { className: 'sr', textContent: on ? ' (included)' : ' (not included)' }),
      ]);
    });

    return el('li', { className: 'panel scard' }, [
      el('div', { className: 'scard-top' }, [numberKey, swatches]),
      el('h3', { textContent: style.name }),
      el('p', { textContent: style.summary }),
      el('div', { className: 'scard-foot' }, [
        el('span', { className: 'themes' }, themes),
        el('a', { className: 'scard-link', href: style.href, target: '_blank', rel: 'noopener', textContent: 'open preview' }, [
          el('span', { className: 'sr', textContent: ` of ${style.name}` }),
          arrowIcon(),
        ]),
      ]),
    ]);
  });

  const shuffle = el('button', { type: 'button', className: 'shuffle', textContent: 'shuffle →' });
  shuffle.setAttribute('aria-label', 'Show a random style on the panel');
  shuffle.addEventListener('click', () => showOnPanel(randomFrom(state.styles.map((s, i) => i))));
  const randomCard = el('li', { className: 'panel scard random-card' }, [
    el('p', { className: 'on-screen-label', textContent: 'can’t decide?' }),
    el('h3', { textContent: 'pick one at random' }),
    shuffle,
  ]);

  $('#style-cards').replaceChildren(...cards, randomCard);
}

// toolbar
$('#style-search').addEventListener('input', (event) => {
  state.query = event.target.value;
  renderKeys();
});
document.querySelectorAll('.pill[data-filter]').forEach((pill) => pill.addEventListener('click', () => {
  state.filter = pill.dataset.filter;
  document.querySelectorAll('.pill[data-filter]').forEach((p) => p.setAttribute('aria-pressed', String(p === pill)));
  renderKeys();
}));

function fail(error) {
  console.error(error);
  setStatus('no signal', false);
  $('#readout-name').textContent = 'catalog not found';
  showMessage('no signal', 'The style catalog could not be read. Serve this page over http from the repository root.');
  $('#result-count').textContent = '';
  $('#device-keys').replaceChildren(el('p', { className: 'grid-msg', textContent: 'The styles could not load.' }));
  $('#style-cards').replaceChildren(el('li', {
    className: 'list-msg',
    textContent: 'The style list could not load. Open this page through a web server from the repository root.',
  }));
}

readCatalog().then((styles) => {
  state.styles = styles;
  if (!styles.length) {
    setStatus('empty', false);
    $('#readout-name').textContent = 'no styles yet';
    showMessage('empty', 'The catalog has no styles yet.');
    $('#device-keys').replaceChildren(el('p', { className: 'grid-msg', textContent: 'No styles in the catalog yet.' }));
    $('#style-cards').replaceChildren(el('li', { className: 'list-msg', textContent: 'No styles in the catalog yet.' }));
    return;
  }
  renderCounts();
  renderSpecs();
  renderKeys();
  renderCards();
  // open on a random style other than the one this page wears
  const others = styles.map((s, i) => i).filter((i) => styles[i].id !== 'instrument-panel');
  select(others.length ? randomFrom(others) : 0);
}).catch(fail);
