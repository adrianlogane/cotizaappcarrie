"""Arma cotizador.html insertando los datos de comunas en la plantilla.

Uso:  python3 scripts/build.py
Lee:  src/cotizador.template.html  y  data/comunas_data.json
Crea: cotizador.html
"""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
plantilla = (root / "src" / "cotizador.template.html").read_text(encoding="utf-8")
datos = (root / "data" / "comunas_data.json").read_text(encoding="utf-8")
(root / "cotizador.html").write_text(plantilla.replace("__DATA__", datos), encoding="utf-8")
print("cotizador.html generado")
