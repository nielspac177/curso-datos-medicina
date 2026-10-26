"""Funciones de la semana 2 (Describir datos).

Son la única fuente de verdad: construir_semana02.py copia su código a los
cuadernos de Colab y tests/test_semana02.py las prueba.
"""
import numpy as np
import pandas as pd


def codigos_a_nan(x, desde, escala=1):
    """Convierte en NaN los códigos de "no sabe / no medido" (valores >= desde) y aplica la escala."""
    return x.where(x < desde) / escala


def resumir_numerica(x, tipo="media"):
    """'media' -> "media (DE)"; 'mediana' -> "mediana [P25, P75]". Ignora faltantes."""
    x = x.dropna()
    if tipo == "media":
        return f"{x.mean():.1f} ({x.std():.1f})"
    if tipo == "mediana":
        p25, p50, p75 = x.quantile([0.25, 0.50, 0.75])
        return f"{p50:.1f} [{p25:.1f}, {p75:.1f}]"
    raise ValueError("tipo debe ser 'media' o 'mediana'")


def resumir_categorica(x):
    """Devuelve {categoría: "n (%)"}; el % se calcula sobre los valores no faltantes."""
    conteo = x.value_counts(sort=False)
    if not isinstance(x.dtype, pd.CategoricalDtype):
        conteo = conteo.sort_index()
    total = conteo.sum()
    return {nivel: f"{n} ({100 * n / total:.1f})" for nivel, n in conteo.items()}


def media_ponderada(x, pesos):
    """Media de x usando pesos de muestreo; descarta las filas con x faltante."""
    ok = x.notna()
    return float(np.sum(x[ok] * pesos[ok]) / np.sum(pesos[ok]))


def tabla1(df, grupo=None, normales=(), asimetricas=(), categoricas=()):
    """Tabla 1 de un estudio: una columna Total, una por grupo y una de faltantes."""
    columnas = {"Total": df}
    if grupo is not None:
        for nivel, sub in df.groupby(grupo, observed=False):
            columnas[str(nivel)] = sub

    filas = {("n", ""): {c: str(len(sub)) for c, sub in columnas.items()}}

    def faltantes(var):
        n = df[var].isna().sum()
        return f"{n} ({100 * n / len(df):.1f})"

    for var in normales:
        fila = {c: resumir_numerica(sub[var], "media") for c, sub in columnas.items()}
        filas[(f"{var}, media (DE)", "")] = {**fila, "Faltantes, n (%)": faltantes(var)}
    for var in asimetricas:
        fila = {c: resumir_numerica(sub[var], "mediana") for c, sub in columnas.items()}
        filas[(f"{var}, mediana [RIC]", "")] = {**fila, "Faltantes, n (%)": faltantes(var)}
    for var in categoricas:
        por_columna = {c: resumir_categorica(sub[var]) for c, sub in columnas.items()}
        for i, nivel in enumerate(por_columna["Total"]):
            fila = {c: por_columna[c].get(nivel, "0 (0.0)") for c in columnas}
            fila["Faltantes, n (%)"] = faltantes(var) if i == 0 else ""
            filas[(f"{var}, n (%)", str(nivel))] = fila

    tabla = pd.DataFrame.from_dict(filas, orient="index")
    tabla.index = pd.MultiIndex.from_tuples(tabla.index, names=["Variable", "Nivel"])
    return tabla.fillna("")[list(columnas) + ["Faltantes, n (%)"]]
