"""Arma el cotizador insertando los datos de comunas en la plantilla.

Uso:  python3 scripts/build.py
Lee:  src/cotizador.template.html  y  data/comunas_data.json
Crea: cotizador.html         -> página completa para abrir o subir a cualquier hosting (iPhone incluido)
      dist/artifact.html     -> solo el contenido, para publicar como artifact en claude.ai
"""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
plantilla = (root / "src" / "cotizador.template.html").read_text(encoding="utf-8")
datos = (root / "data" / "comunas_data.json").read_text(encoding="utf-8")
cuerpo = plantilla.replace("__DATA__", datos)

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Cotizador">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="format-detection" content="telephone=no">
<meta name="theme-color" content="#EEF1F5" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0B111A" media="(prefers-color-scheme: dark)">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;-webkit-text-size-adjust:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""

(root / "cotizador.html").write_text(HEAD + cuerpo + "\n</body>\n</html>\n", encoding="utf-8")
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "artifact.html").write_text(cuerpo, encoding="utf-8")
print("cotizador.html y dist/artifact.html generados")
