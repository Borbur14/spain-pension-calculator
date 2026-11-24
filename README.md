# Calculadora de pensión de jubilación 2026 · Spain pension calculator

Free, open-source calculator for the **Spanish state retirement pension (pensión de jubilación contributiva) in 2026**: percentage by years contributed (*tabla de jubilación por años cotizados*), base reguladora, maximum and minimum pension. Python and JavaScript, no dependencies.

**Use it online (no code):** [Calculadora de pensión de jubilación 2026](https://borbur.net/es/herramientas/calculadora-pension-jubilacion/) · [Spain pension calculator (English)](https://borbur.net/tools/spain-pension-calculator/)

Made by [Borja Burguillos](https://borbur.net/about/), author of [Why Bitcoin Had to Exist](https://borbur.net/books/why-bitcoin-had-to-exist/) and [Stablecoins for a Better World](https://borbur.net/books/stablecoins-for-a-better-world/).

## Tabla de jubilación por años cotizados (2026)

Pensión mensual en 14 pagas con una base de cotización media constante (euros de hoy).

| Años cotizados | % en 2026 | % desde 2027 | Base 1.500 € | Base 2.000 € | Base 3.000 € |
|---|---|---|---|---|---|
| 15 | 50,0 % | 50,0 % | 642,86 € | 857,14 € | 1.285,71 € |
| 16 | 52,52 % | 52,28 % | 675,26 € | 900,34 € | 1.350,51 € |
| 17 | 55,04 % | 54,56 % | 707,66 € | 943,54 € | 1.415,31 € |
| 18 | 57,56 % | 56,84 % | 740,06 € | 986,74 € | 1.480,11 € |
| 19 | 60,08 % | 59,12 % | 772,46 € | 1.029,94 € | 1.544,91 € |
| 20 | 62,38 % | 61,4 % | 802,03 € | 1.069,37 € | 1.604,06 € |
| 22 | 66,94 % | 65,96 % | 860,66 € | 1.147,54 € | 1.721,31 € |
| 25 | 73,78 % | 72,8 % | 948,60 € | 1.264,80 € | 1.897,20 € |
| 27 | 78,34 % | 77,36 % | 1.007,23 € | 1.342,97 € | 2.014,46 € |
| 30 | 85,18 % | 84,2 % | 1.095,17 € | 1.460,23 € | 2.190,34 € |
| 33 | 92,02 % | 91,04 % | 1.183,11 € | 1.577,49 € | 2.366,23 € |
| 35 | 96,58 % | 95,6 % | 1.241,74 € | 1.655,66 € | 2.483,49 € |
| 36 | 98,86 % | 97,84 % | 1.271,06 € | 1.694,74 € | 2.542,11 € |
| 37 | 100,0 % | 100,0 % | 1.285,71 € | 1.714,29 € | 2.571,43 € |
| 38 | 100,0 % | 100,0 % | 1.285,71 € | 1.714,29 € | 2.571,43 € |
| 40 | 100,0 % | 100,0 % | 1.285,71 € | 1.714,29 € | 2.571,43 € |

Datos completos (15 a 40 años, también base máxima): [pension_table_2026.csv](pension_table_2026.csv). Una página por cada caso: [15](https://borbur.net/es/herramientas/calculadora-pension-jubilacion/15-anos-cotizados/), [20](https://borbur.net/es/herramientas/calculadora-pension-jubilacion/20-anos-cotizados/), [25](https://borbur.net/es/herramientas/calculadora-pension-jubilacion/25-anos-cotizados/), [30](https://borbur.net/es/herramientas/calculadora-pension-jubilacion/30-anos-cotizados/), [35](https://borbur.net/es/herramientas/calculadora-pension-jubilacion/35-anos-cotizados/) y [40 años cotizados](https://borbur.net/es/herramientas/calculadora-pension-jubilacion/40-anos-cotizados/); por base: [1.500 €](https://borbur.net/es/herramientas/calculadora-pension-jubilacion/base-1500-euros/), [2.000 €](https://borbur.net/es/herramientas/calculadora-pension-jubilacion/base-2000-euros/), [3.000 €](https://borbur.net/es/herramientas/calculadora-pension-jubilacion/base-3000-euros/).

## Rules (2026)

| Item | 2026 |
|---|---|
| Minimum contribution period | 15 years (50% of the base reguladora) |
| Percentage, retiring in 2026 | +0.21% a month for 49 months, then +0.19% a month; 100% at 36 years 6 months |
| Percentage, retiring from 2027 | +0.19% a month for 248 months, then +0.18% a month |
| Base reguladora | average monthly contribution base of the last 25 years x 300 / 350 |
| Maximum contribution base | €5,101.20 a month |
| Maximum pension | €3,359.60 a month in 14 payments |
| Minimum pension (single, 65+) | €936.20 a month (€1,256.60 with a dependent spouse) |
| Ordinary retirement age | 65 with 38 years 3 months or more; otherwise 66 years 10 months (2026) |

Simplifications: same base every month, no inflation update of old bases, no early-retirement cut, no delay incentive, no contribution gaps, Régimen General only. For an official figure use the Seguridad Social simulator (Tu Seguridad Social).

## Use

```python
from pension import pension
pension(2000, 25 * 12)   # {'base_reguladora': 1714.29, 'percentage': 73.78, 'pension': 1264.8, ...}
```

```js
import { pension } from "./pension.js";
pension(2000, 25 * 12);  // { baseReguladora: 1714.29, percentage: 73.78, pension: 1264.8, ... }
```

## More free tools by the same author

- [Spain net salary calculator 2026](https://borbur.net/tools/spain-net-salary-calculator/) · [Calculadora de sueldo neto](https://borbur.net/es/herramientas/calculadora-sueldo-neto/) (code: [spain-salary-calculator-2026](https://github.com/Borbur14/spain-salary-calculator-2026))
- [Beckham Law calculator](https://borbur.net/tools/beckham-law-calculator/) · [Calculadora Ley Beckham](https://borbur.net/es/herramientas/calculadora-ley-beckham/)
- [Salary tax in 20 countries, 2026](https://borbur.net/tools/salary-tax-comparator/)
- [UAE gratuity calculator](https://borbur.net/tools/uae-gratuity-calculator/)

## Licence

Code: MIT. Table and data: CC BY 4.0, credit "Borja Burguillos, borbur.net".
