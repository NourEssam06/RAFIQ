import { expect, test } from '@playwright/test';

test('an owner can submit and reload a single validated result', async ({ browser, page, request }) => {
  console.log(`Browser ${browser.browserType().name()} ${browser.version()}`);
  await page.goto('http://127.0.0.1:3000');
  await page.getByLabel('Synthetic identity').selectOption('driver-a');
  await page.getByRole('button', { name: 'Submit fixture' }).click();

  const fixtureId = page.getByTestId('fixture-id');
  await expect(fixtureId).toHaveText(/^[0-9a-f-]{36}$/);
  const id = await fixtureId.innerText();
  const result = page.getByText('3 samples · mean 4 · synthetic-mean-v1');
  await expect(result).toBeVisible({ timeout: 20_000 });
  await page.reload();
  await expect(result).toBeVisible();
  await expect(fixtureId).toHaveText(id);
  await page.getByRole('button', { name: 'Submit fixture' }).click();
  await expect(fixtureId).toHaveText(id);
  await expect(result).toBeVisible();

  const path = `http://127.0.0.1:8000/api/v1/local-fixtures/${id}`;
  const unauthenticated = await request.get(path);
  expect(unauthenticated.status()).toBe(401);
  expect(await unauthenticated.json()).toEqual({ detail: 'Synthetic identity required' });

  await page.getByLabel('Synthetic identity').selectOption('driver-b');
  await expect(page.getByText('No fixture has been submitted.')).toBeVisible();
  await expect(result).toHaveCount(0);
  const otherDriver = await request.get(path, {
    headers: { Authorization: 'Bearer local-driver-b' },
  });
  expect(otherDriver.status()).toBe(404);
  expect(await otherDriver.json()).toEqual({ detail: 'Fixture not found' });
});
