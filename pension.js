// Spain state retirement pension calculator, 2026 rules (Régimen General).
// Calculadora de pensión de jubilación 2026. Live: https://borbur.net/es/herramientas/calculadora-pension-jubilacion/
// Author: Borja Burguillos (https://borbur.net). MIT licence.
export const MAX_BASE_2026 = 5101.2, MAX_PENSION_2026 = 3359.6, MIN_PENSION_2026 = 936.2;

export function percentage(months, year = 2026) {
  const x = months - 180;
  if (x < 0) return null;
  const p = year <= 2026
    ? 50 + Math.min(x, 49) * 0.21 + Math.max(x - 49, 0) * 0.19
    : 50 + Math.min(x, 248) * 0.19 + Math.max(x - 248, 0) * 0.18;
  return Math.min(Math.round(p * 100) / 100, 100);
}

export function pension(base, months, year = 2026) {
  const br = Math.min(base, MAX_BASE_2026) * 300 / 350;
  const p = percentage(months, year) ?? 0;
  const raw = br * p / 100;
  return { baseReguladora: +br.toFixed(2), percentage: p, pension: +Math.min(raw, MAX_PENSION_2026).toFixed(2),
           cappedAtMaximum: raw > MAX_PENSION_2026, belowMinimum: raw < MIN_PENSION_2026 };
}
