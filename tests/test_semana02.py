"""Pruebas de las funciones que usan los cuadernos de la semana 2.

Uso: python -m pytest -q
"""
import numpy as np
import pandas as pd
import pytest

from semana02_funciones import (
    codigos_a_nan,
    media_ponderada,
    resumir_categorica,
    resumir_numerica,
    tabla1,
)


def test_codigos_a_nan_reemplaza_solo_los_codigos():
    x = pd.Series([112, 999, 121, 999])
    limpio = codigos_a_nan(x, desde=999)
    assert limpio.isna().sum() == 2
    assert limpio.dropna().tolist() == [112, 121]


def test_codigos_a_nan_con_escala():
    x = pd.Series([-152, 9996, -13, 9999])
    limpio = codigos_a_nan(x, desde=9996, escala=100)
    assert limpio.dropna().tolist() == [-1.52, -0.13]


def test_resumir_numerica_media_de():
    x = pd.Series([10.0, 12.0, 14.0, np.nan])
    assert resumir_numerica(x, "media") == "12.0 (2.0)"


def test_resumir_numerica_mediana_ric():
    x = pd.Series([1, 2, 3, 4, 100])
    assert resumir_numerica(x, "mediana") == "3.0 [2.0, 4.0]"


def test_resumir_numerica_rechaza_tipo_desconocido():
    with pytest.raises(ValueError):
        resumir_numerica(pd.Series([1, 2]), "moda")


def test_resumir_categorica_porcentaje_sobre_no_faltantes():
    x = pd.Series(["a", "a", "b", None])
    assert resumir_categorica(x) == {"a": "2 (66.7)", "b": "1 (33.3)"}


def test_resumir_categorica_respeta_el_orden_de_las_categorias():
    x = pd.Series(pd.Categorical(["alto", "bajo"], categories=["bajo", "medio", "alto"], ordered=True))
    assert list(resumir_categorica(x)) == ["bajo", "medio", "alto"]
    assert resumir_categorica(x)["medio"] == "0 (0.0)"


def test_media_ponderada():
    assert media_ponderada(pd.Series([1, 0]), pd.Series([3, 1])) == pytest.approx(0.75)
    assert media_ponderada(pd.Series([1, np.nan, 0]), pd.Series([3, 5, 1])) == pytest.approx(0.75)


@pytest.fixture
def pacientes():
    return pd.DataFrame({
        "grupo": ["sí", "sí", "no", "no", "no"],
        "edad": [30, 40, 20, 30, np.nan],
        "sexo": ["M", "F", "F", "F", "M"],
    })


def test_tabla1_columnas_y_n(pacientes):
    t = tabla1(pacientes, "grupo", normales=["edad"], categoricas=["sexo"])
    assert list(t.columns) == ["Total", "no", "sí", "Faltantes, n (%)"]
    assert t.loc[("n", ""), "Total"] == "5"
    assert t.loc[("n", ""), "no"] == "3"


def test_tabla1_resume_por_grupo(pacientes):
    t = tabla1(pacientes, "grupo", normales=["edad"], categoricas=["sexo"])
    assert t.loc[("edad, media (DE)", ""), "sí"] == "35.0 (7.1)"
    assert t.loc[("sexo, n (%)", "F"), "no"] == "2 (66.7)"
    assert t.loc[("edad, media (DE)", ""), "Faltantes, n (%)"] == "1 (20.0)"


def test_tabla1_sin_grupo_solo_total(pacientes):
    t = tabla1(pacientes, None, asimetricas=["edad"])
    assert list(t.columns) == ["Total", "Faltantes, n (%)"]
    assert t.loc[("edad, mediana [RIC]", ""), "Total"] == "30.0 [27.5, 32.5]"
