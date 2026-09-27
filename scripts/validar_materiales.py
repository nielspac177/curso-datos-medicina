"""Revisa que cada archivo citado en materiales/semanas.json exista en el repositorio.

Uso: python scripts/validar_materiales.py
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def main():
    manifiesto = json.loads((RAIZ / "materiales" / "semanas.json").read_text(encoding="utf-8"))
    errores = []

    for s in manifiesto["semanas"]:
        etiqueta = f"Semana {s['n']}"
        if not (RAIZ / s["carpeta"]).is_dir():
            errores.append(f"{etiqueta}: no existe la carpeta {s['carpeta']}")
        if s["slides"] and not s["slides"].startswith("http") and not (RAIZ / s["slides"]).is_file():
            errores.append(f"{etiqueta}: no existe {s['slides']}")
        for c in s["cuadernos"]:
            ruta = RAIZ / c["ruta"]
            if not ruta.is_file():
                errores.append(f"{etiqueta}: no existe {c['ruta']}")
                continue
            try:
                json.loads(ruta.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                errores.append(f"{etiqueta}: {c['ruta']} no es un cuaderno válido ({e})")

    if errores:
        print("\n".join(errores))
        sys.exit(1)
    print(f"OK: {len(manifiesto['semanas'])} semanas revisadas.")


if __name__ == "__main__":
    main()
