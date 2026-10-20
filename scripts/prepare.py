"""Une comunas.json + geo.json + routes.json en comunas_data.json (formato compacto que usa la página).

Uso: python3 scripts/prepare.py data
"""
import json, sys

D = sys.argv[1]
src = json.load(open(D + "/comunas.json", encoding="utf-8"))
r = json.load(open(D + "/routes.json", encoding="utf-8"))
g = json.load(open(D + "/geo.json", encoding="utf-8"))

short = {
    "Arica y Parinacota": "Arica y Parinacota", "Tarapacá": "Tarapacá", "Antofagasta": "Antofagasta",
    "Atacama": "Atacama", "Coquimbo": "Coquimbo", "Valparaíso": "Valparaíso",
    "Región del Libertador Gral. Bernardo O’Higgins": "O'Higgins", "Región del Maule": "Maule",
    "Región de Ñuble": "Ñuble", "Región del Biobío": "Biobío", "Región de la Araucanía": "Araucanía",
    "Región de Los Ríos": "Los Ríos", "Región de Los Lagos": "Los Lagos",
    "Región Aisén del Gral. Carlos Ibáñez del Campo": "Aysén",
    "Región de Magallanes y de la Antártica Chilena": "Magallanes",
    "Región Metropolitana de Santiago": "Metropolitana",
}
chiloe = {"Ancud", "Castro", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao"}
isla = {"Juan Fernández", "Isla de Pascua", "Antártica", "Cabo de Hornos (Ex Navarino)"}
caso = {"Chaitén", "Futaleufú", "Palena", "Hualaihué", "Cochamó", "Porvenir", "Primavera", "Timaukel"}

out = []
for reg in src["regiones"]:
    for c in reg["comunas"]:
        k = reg["region"] + "|" + c
        rr, gg, rs = r[k], g[k], short[reg["region"]]
        flag = ("isla" if c in isla else "chacao" if c in chiloe
                else "caso" if (c in caso or rs in ("Aysén", "Magallanes")) else "")
        km = lambda o: None if flag == "isla" or rr[o] is None else rr[o][0]
        h = None if flag == "isla" or rr["PUD"] is None else rr["PUD"][1]
        out.append([c.replace(" (Ex Navarino)", ""), rs, km("PUD"), km("SAI"), km("VAP"), km("AMB"),
                    h, flag, round(gg["lat"], 3), round(gg["lon"], 3)])

json.dump(out, open(D + "/comunas_data.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(out), "comunas")
