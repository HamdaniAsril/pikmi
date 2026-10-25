// pikmi landing page: reads the catalog so the page follows whatever styles the repo ships.

const SKILL = '../skills/pikmi/';
const $ = (selector) => document.querySelector(selector);

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

function el(tag, props = {}, children = []) {
  const node = Object.assign(document.createElement(tag), props);
  node.append(...children);
  return node;
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

  document.querySelectorAll('#device-keys .srow[data-index]').forEach((row) => {
    const on = Number(row.dataset.index) === index;
    row.setAttribute('aria-pressed', String(on));
    if (on) keepInList(row);
  });

  $('#readout-num').textContent = style.number;
  $('#readout-of').textContent = `/${String(state.styles.length).padStart(2, '0')}`;
  $('#readout-name').textContent = style.name;
  $('#readout-summary').textContent = style.summary;
  const open = $('#open-preview');
  open.href = style.href;
  open.querySelector('.sr')?.remove();
  open.append(el('span', { className: 'sr', textContent: ` of ${style.name}` }));

  showMessage('loading', style.name);
  setStatus('loading', false);
  frame.title = `Preview of the ${style.name} style`;
  frame.src = style.href;
}

function randomFrom(indexes) {
  const pool = indexes.length > 1 ? indexes.filter((i) => i !== state.current) : indexes;
  return pool[Math.floor(Math.random() * pool.length)];
}

// scroll the list itself, not the page, so a row picked elsewhere stays visible
function keepInList(row) {
  const list = $('#device-keys');
  const top = row.offsetTop;
  if (top < list.scrollTop) list.scrollTop = top;
  else if (top + row.offsetHeight > list.scrollTop + list.clientHeight) list.scrollTop = top + row.offsetHeight - list.clientHeight;
}

function swatches(style) {
  const colors = palette(style);
  const chips = el('span', { className: 'palette' }, colors.map(([role, hex]) => {
    const chip = el('span', { title: `${hex.toUpperCase()} ${role}` });
    chip.style.background = hex;
    return chip;
  }));
  chips.setAttribute('role', 'img');
  chips.setAttribute('aria-label', 'Palette: ' + colors.map(([role, hex]) => `${role} ${hex}`).join(', '));
  return chips;
}

function renderKeys() {
  const shown = visibleStyles();
  const rows = shown.map(({ style, index }) => {
    const row = el('button', { type: 'button', className: 'srow' }, [
      el('span', { className: 'srow-num', textContent: style.number }),
      el('span', { className: 'srow-name', textContent: style.name }),
      el('span', { className: 'srow-meta' }, [swatches(style), el('span', { textContent: style.themes.join(' · ') })]),
    ]);
    row.dataset.index = index;
    row.setAttribute('aria-pressed', String(index === state.current));
    row.addEventListener('click', () => select(index));
    return row;
  });

  const random = el('button', { type: 'button', className: 'srow random' }, [
    el('span', { className: 'srow-num', textContent: '??' }),
    el('span', { className: 'srow-name', textContent: 'random' }),
    el('span', { className: 'srow-meta', textContent: 'surprise me' }),
  ]);
  random.setAttribute('aria-label', shown.length ? 'Random style from this list' : 'Random style');
  random.addEventListener('click', () => {
    const pool = shown.length ? shown.map(({ index }) => index) : state.styles.map((s, i) => i);
    select(randomFrom(pool));
  });

  const message = shown.length ? [] : [el('p', { className: 'grid-msg', textContent: `No style matches “${state.query.trim()}”. Try another mood, or press random.` })];
  $('#device-keys').replaceChildren(...rows, ...message, random);
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

// how it works: drawn bars, and catalog numbers on the "pick one of three" screen
const WAVE = [4, 10, 18, 8, 26, 14, 6, 20, 30, 12, 22, 8, 16, 4, 12, 24, 10, 6, 18, 8, 14, 28, 10, 4, 16, 8];
$('#wave').replaceChildren(...WAVE.map((h, i) => {
  const bar = el('span', { className: i < 12 ? '' : 'quiet' });
  bar.style.height = `${h}px`;
  return bar;
}));
const METER = [4, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 11, 12, 12, 13, 13, 14, 14];
$('#meter').replaceChildren(...METER.map((h, i) => {
  const seg = el('span', { className: i < 22 ? '' : 'off' });
  seg.style.height = `${h}px`;
  return seg;
}));

function renderStory() {
  const rows = [...document.querySelectorAll('.lcd-option[data-style]')];
  rows.forEach((row) => {
    const style = state.styles.find((s) => s.id === row.dataset.style);
    if (style) row.querySelector('.lcd-num').textContent = style.number;
    else row.remove();
  });
  const left = document.querySelectorAll('.lcd-option[data-style]').length;
  $('#sel-title').textContent = `sel · ${left} ${left === 1 ? 'match' : 'matches'}`;
  $('#sel-state').textContent = `1/${left}`;
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
}

readCatalog().then((styles) => {
  state.styles = styles;
  if (!styles.length) {
    setStatus('empty', false);
    $('#readout-name').textContent = 'no styles yet';
    showMessage('empty', 'The catalog has no styles yet.');
    $('#device-keys').replaceChildren(el('p', { className: 'grid-msg', textContent: 'No styles in the catalog yet.' }));
    return;
  }
  renderCounts();
  renderSpecs();
  renderKeys();
  renderStory();
  // open on a random style other than the one this page wears
  const others = styles.map((s, i) => i).filter((i) => styles[i].id !== 'instrument-panel');
  select(others.length ? randomFrom(others) : 0);
}).catch(fail);
