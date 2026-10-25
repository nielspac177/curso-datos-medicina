# Semana 2 · Describir datos

Tipos de variables; media, mediana y dispersión; la tabla 1 · Práctica: ENDES

**Materiales:** <https://nielspac177.github.io/curso-datos-medicina/materiales/#s2>

El hilo de la clase es la anemia en niñas y niños de 6 a 59 meses (ENDES 2024, INEI). El cuaderno termina
reproduciendo la cifra oficial: 43.7 % de anemia de 6 a 35 meses (40.2 % urbano, 51.9 % rural).

## Archivos

| Archivo | Para quién | Qué es |
|---|---|---|
| [`diapositivas/index.html`](diapositivas/index.html) | Clase | 40 diapositivas interactivas. Flechas para avanzar, **N** para las notas del orador, **F** para pantalla completa. |
| [`diapositivas/semana02_describir_datos.pdf`](diapositivas/semana02_describir_datos.pdf) | Alumnos | Las mismas diapositivas en PDF, con todos los pasos visibles. |
| [`cuadernos/02_describir_datos_ALUMNO.ipynb`](cuadernos/02_describir_datos_ALUMNO.ipynb) | Alumnos | Cuaderno de Colab con 10 ejercicios para completar. Es el que enlaza la página de materiales. |
| [`cuadernos/02_describir_datos_DOCENTE.ipynb`](cuadernos/02_describir_datos_DOCENTE.ipynb) | Docente | El mismo cuaderno ejecutado, con soluciones, la lectura de cada resultado y notas de tiempo. |

## Plan de las dos horas

| Minutos | Qué | Material |
|---|---|---|
| 0 a 35 | Qué es una fila, el 999, tipos de variables, centro y dispersión | Diapositivas 1 a 26 |
| 35 a 75 | Partes 0 a 5 del cuaderno | Ejercicios 1 a 6 |
| 75 a 90 | La tabla 1, valores p, pesos de muestreo | Diapositivas 27 a 33 |
| 90 a 115 | Partes 6 a 8 del cuaderno | Ejercicios 7 a 10 |
| 115 a 120 | Herramientas y cierre | Diapositivas 34 a 40 |

## Cómo regenerar

Los dos cuadernos salen de un solo guion, así que no se editan a mano:

```bash
pip install pandas numpy scipy seaborn tableone requests nbformat nbclient ipykernel pytest
python -m pytest -q                              # pruebas de las funciones de la tabla 1
python scripts/construir_semana02.py --ejecutar  # escribe ALUMNO y ejecuta DOCENTE (baja ~16 MB del INEI)
```

- Las funciones (`codigos_a_nan`, `tabla1`, `media_ponderada`...) viven en `scripts/semana02_funciones.py` y se copian tal cual a los cuadernos.
- El PDF se exporta abriendo `diapositivas/index.html?print` y usando "Imprimir → Guardar como PDF" (o Chrome sin interfaz con `--print-to-pdf`).
- Los datos no se guardan en el repositorio: el cuaderno los baja del INEI (módulos 1629, 1630 y 1638 de la ENDES 2024).
