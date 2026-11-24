"""Spain state retirement pension calculator, 2026 rules (Régimen General).

Calculadora de pensión de jubilación 2026: porcentaje por años cotizados,
base reguladora, pensión máxima y mínima.

Source of the rules: Ley General de la Seguridad Social art. 209-210 and the
transitional schedule of Ley 27/2011; 2026 maximum and minimum pensions.
Live calculator: https://borbur.net/es/herramientas/calculadora-pension-jubilacion/
Author: Borja Burguillos (https://borbur.net). Code: MIT. Data: CC BY 4.0.
"""

MAX_BASE_2026 = 5101.20      # maximum monthly contribution base, €
MAX_PENSION_2026 = 3359.60   # maximum pension, € a month in 14 payments
MIN_PENSION_2026 = 936.20    # minimum pension, single, aged 65+
MIN_PENSION_SPOUSE_2026 = 1256.60  # minimum pension with a dependent spouse


def percentage(months, year=2026):
    """Share of the base reguladora earned by `months` of contributions.

    15 years (180 months) is the minimum and earns 50%.
    Retiring in 2026: +0.21% a month for the next 49 months, then +0.19%.
    Retiring from 2027: +0.19% a month for 248 months, then +0.18%.
    100% is reached with 36 years 6 months (438 months).
    Returns None below 15 years (no contributory pension).
    """
    x = months - 180
    if x < 0:
        return None
    if year <= 2026:
        p = 50 + min(x, 49) * 0.21 + max(x - 49, 0) * 0.19
    else:
        p = 50 + min(x, 248) * 0.19 + max(x - 248, 0) * 0.18
    return min(round(p, 2), 100.0)


def pension(base, months, year=2026):
    """Monthly pension (14 payments) for a steady monthly contribution base in today's euros.

    base reguladora = average base of the last 25 years x 300 / 350 (14 payments).
    Simplified: assumes the same base every month and no inflation adjustment,
    no early-retirement cut, no delay incentive and no gaps.
    """
    br = min(base, MAX_BASE_2026) * 300 / 350
    p = percentage(months, year) or 0
    raw = br * p / 100
    return {
        "base_reguladora": round(br, 2),
        "percentage": p,
        "pension": round(min(raw, MAX_PENSION_2026), 2),
        "capped_at_maximum": raw > MAX_PENSION_2026,
        "below_minimum": raw < MIN_PENSION_2026,
    }


if __name__ == "__main__":
    for years in (15, 20, 25, 30, 35, 37, 40):
        r = pension(2000, years * 12)
        print(f"{years} years, base €2,000: {r['percentage']}% -> €{r['pension']:.2f} a month")
