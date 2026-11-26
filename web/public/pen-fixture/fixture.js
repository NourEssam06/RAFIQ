'use strict';

const filters = document.querySelector('#session-filters');
const period = document.querySelector('#session-period');
const refresh = filters.querySelector('[type="submit"]');
const status = document.querySelector('#summary-status');
const icon = document.querySelector('#summary-icon');
const scope = document.querySelector('#chart-scope');
const dialog = document.querySelector('#clear-dialog');
const opener = document.querySelector('#open-clear');
const summaries = {
  week: { days: 7, sessions: 5, warnings: { drowsiness: 3, distraction: 1 } },
  month: { days: 30, sessions: 16, warnings: { drowsiness: 9, distraction: 4 } },
};
let refreshTimer;

function refreshSummary() {
  clearTimeout(refreshTimer);
  const summary = summaries[period.value];
  refresh.setAttribute('aria-disabled', 'true');
  status.textContent = `Loading session summary for the last ${summary.days} days.`;
  icon.className = 'status-icon is-loading';
  icon.textContent = '◷';

  refreshTimer = setTimeout(() => {
    scope.textContent = `Last ${summary.days} days · ${summary.sessions} synthetic sessions`;
    for (const [behavior, count] of Object.entries(summary.warnings)) {
      const row = document.getElementById(behavior);
      row.querySelector('span').textContent = count;
      row.querySelector('progress').value = count;
    }
    icon.className = 'status-icon is-ready';
    icon.textContent = '✓';
    refresh.removeAttribute('aria-disabled');
    refreshTimer = undefined;
    status.textContent = `Session summary ready for the last ${summary.days} days.`;
  }, 1200);
}

filters.addEventListener('submit', (event) => {
  event.preventDefault();
  if (refreshTimer === undefined) refreshSummary();
});

opener.addEventListener('click', () => {
  dialog.returnValue = '';
  dialog.showModal();
});

dialog.addEventListener('close', () => {
  if (dialog.returnValue === 'clear') {
    filters.reset();
    refreshSummary();
  }
  opener.focus();
});
