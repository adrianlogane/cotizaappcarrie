# Cotizador de transporte CHLG

Página web que automatiza el costeo de la planilla "COSTEO PARA COTIZAR REGIONES" y el "TARIFARIO PREFERENCIAL 2026".

## Archivos

| Archivo | Qué es |
|---|---|
| `cotizador.html` | Página lista para usar. Se abre con doble clic en cualquier navegador; no necesita servidor. |
| `src/cotizador.template.html` | Código fuente (HTML, CSS y JavaScript) con el marcador `__DATA__` donde van las comunas. |
| `data/comunas_data.json` | 346 comunas con km por carretera desde Pudahuel, San Antonio, Valparaíso y aeropuerto. |
| `data/comunas.json` | Listado de comunas por región (fuente). |
| `data/geo.json` | Coordenadas de cada comuna (OpenStreetMap / Nominatim). |
| `data/routes.json` | Km y horas de ruta por origen (OSRM). |
| `scripts/geocode.py` | Obtiene coordenadas de las comunas. |
| `scripts/routes.py` | Calcula km por carretera desde cada origen. |
| `scripts/prepare.py` | Une coordenadas y rutas en `comunas_data.json`. |
| `scripts/build.py` | Inserta los datos en la plantilla y genera `cotizador.html`. |

## Formato de cada comuna en `comunas_data.json`

`[comuna, región, km Pudahuel, km San Antonio, km Valparaíso, km Aeropuerto, horas desde Pudahuel, marca, lat, lon]`

Marca: `isla` (sin acceso por carretera), `chacao` (Chiloé, suma cruce), `caso` (barcaza o ruta por Argentina), vacío (normal).

## Cómo se calcula (pestaña Regiones)

Igual que la planilla:

- Combustible = km ida × 2 ÷ rendimiento × precio diésel
- Por día de viaje: sueldo chofer (sueldo mensual ÷ 25), viático, leasing y desgaste (mensual ÷ 22)
- Hospedaje por noche, peajes, viaje conductor (desde 400 km, ciudad más cercana de la tabla), extras
- Exclusivo = costo + margen (40 % o 50 % según vehículo); consolidado = 65 % del exclusivo
- Rampa hidráulica se suma después del margen

Diferencias con la planilla:

- Camión 5.000: la planilla calculaba el sueldo del chofer con la celda del viático ($10.000/día). Aquí usa $40.000/día.
- Peajes: se estiman por km recorrido según vehículo (valores sacados de cotizaciones anteriores, incluyen el 20 %). Se pueden escribir a mano.
- Días de viaje = km ida ÷ 650, redondeado hacia arriba. Noches = días − 1.

Los valores editables están en `DEFAULTS` dentro del script de la plantilla, y también en la pestaña Parámetros (esos cambios se guardan solo en el navegador).

## Regenerar

```bash
python3 scripts/geocode.py data   # solo si cambia el listado de comunas (≈6 min)
python3 scripts/routes.py data    # recalcula km
python3 scripts/prepare.py data   # arma comunas_data.json
python3 scripts/build.py          # genera cotizador.html
```
