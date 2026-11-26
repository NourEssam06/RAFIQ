import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { expect, test } from '@playwright/test';

const preview = pathToFileURL(resolve('public/pen-fixture/index.html')).href;

test('keyboard navigation reaches the filters and returns from the dialog', async ({ page }) => {
  await page.goto(preview);
  await page.keyboard.press('Tab');
  await expect(page.getByRole('link', { name: 'Skip to content' })).toBeFocused();
  await page.keyboard.press('Enter');
  await expect(page.getByRole('main')).toBeFocused();
  const driverNav = page.getByRole('navigation', { name: 'Driver workspace' });
  await page.keyboard.press('Tab');
  await expect(driverNav.getByRole('link', { name: 'Sessions' })).toBeFocused();
  await page.keyboard.press('Tab');
  await expect(driverNav.getByRole('link', { name: 'Personal Overview' })).toBeFocused();
  await page.keyboard.press('Tab');
  await expect(page.getByRole('combobox', { name: 'Session period' })).toBeFocused();
  await page.keyboard.press('Tab');
  const refresh = page.getByRole('button', { name: 'Refresh summary' });
  await expect(refresh).toBeFocused();
  await expect(refresh).toHaveCSS('outline-style', 'solid');
  await expect(refresh).toHaveCSS('outline-width', '3px');

  await page.keyboard.press('Tab');
  const opener = page.getByRole('button', { name: 'Clear selection' });
  await expect(opener).toBeFocused();
  const dialog = page.getByRole('dialog', { name: 'Clear this selection?' });
  await page.keyboard.press('Enter');
  await expect(dialog.getByRole('button', { name: 'Cancel' })).toBeFocused();
  await page.keyboard.press('Escape');
  await expect(dialog).toBeHidden();
  await expect(opener).toBeFocused();

  await page.keyboard.press('Enter');
  await page.keyboard.press('Enter');
  await expect(dialog).toBeHidden();
  await expect(opener).toBeFocused();
});

test('a refresh exposes loading and completion without moving focus', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.clock.install();
  await page.clock.pauseAt(new Date(Date.now() + 60_000));
  await page.goto(preview);
  await page.getByLabel('Session period').selectOption('month');
  const refresh = page.getByRole('button', { name: 'Refresh summary' });
  await refresh.focus();
  await page.keyboard.press('Enter');
  const status = page.getByRole('status');
  await expect(status).toHaveText('Loading session summary for the last 30 days.');
  await expect(page.locator('#summary-icon')).toHaveCSS('animation-name', 'none');
  await expect(refresh).toBeFocused();

  await page.clock.runFor(1_200);
  await expect(status).toHaveText('Session summary ready for the last 30 days.');
  await expect(refresh).toBeFocused();
  const chart = page.getByRole('table', { name: 'Recorded warning counts by behavior' });
  await expect(chart.getByRole('row', { name: 'Drowsiness 9' })).toBeVisible();
  await expect(chart.getByRole('row', { name: 'Distraction 4' })).toBeVisible();
  await expect(chart.getByRole('progressbar')).toHaveCount(0);
  expect(await chart.locator('progress').evaluateAll(bars => bars.map(bar => bar.getAttribute('value')))).toEqual(['9', '4']);

  const clear = page.getByRole('button', { name: 'Clear selection' });
  await clear.click();
  await page.getByRole('dialog').getByRole('button', { name: 'Clear selection' }).click();
  await expect(page.getByLabel('Session period')).toHaveValue('week');
  await expect(clear).toBeFocused();
  await page.clock.runFor(1_200);
  await expect(status).toHaveText('Session summary ready for the last 7 days.');
});

for (const width of [1440, 640, 390, 320]) {
  test(`workspace and dialog reflow at ${width} CSS pixels`, async ({ page }) => {
    await page.setViewportSize({ width, height: 800 });
    await page.goto(preview);
    const sessions = page.getByRole('region', { name: 'Sessions', exact: true });
    const overview = page.getByRole('region', { name: 'Personal Overview' });
    const sessionsBounds = await sessions.boundingBox();
    const overviewBounds = await overview.boundingBox();
    expect(sessionsBounds).not.toBeNull();
    expect(overviewBounds).not.toBeNull();
    if (width === 1440) {
      expect(overviewBounds!.x).toBeGreaterThan(sessionsBounds!.x);
      expect(overviewBounds!.y).toBe(sessionsBounds!.y);
    } else {
      expect(overviewBounds!.y).toBeGreaterThanOrEqual(sessionsBounds!.y + sessionsBounds!.height);
    }
    expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(width);

    await page.getByRole('button', { name: 'Clear selection' }).click();
    const dialog = page.getByRole('dialog', { name: 'Clear this selection?' });
    await expect(dialog.getByRole('button', { name: 'Clear selection' })).toBeInViewport();
    expect(await dialog.evaluate(element => element.scrollWidth)).toBeLessThanOrEqual(
      await dialog.evaluate(element => element.clientWidth),
    );
  });
}
