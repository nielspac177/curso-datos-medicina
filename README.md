# Estadística y Machine Learning para Estudiantes de Medicina

Curso en vivo de 16 semanas, sin fines de lucro, con bases de datos abiertas de salud. Dr. Niels Pacheco-Barrios.

- **Materiales (diapositivas y cuadernos de Colab):** https://nielspac177.github.io/curso-datos-medicina/materiales/
- **Página del curso e inscripción:** https://nielspac177.github.io/curso-datos-medicina/
- **Syllabus:** [syllabus.pdf](syllabus.pdf)

## Contenido

| # | Tema | Contenido |
|---|---|---|
| 0 | [Módulo 0 · Nivelación (opcional)](semanas/00-nivelacion/) | Notación y funciones; logaritmos y odds; vectores y matrices como tablas; probabilidad básica |
| 1 | [El médico y los datos](semanas/01-el-medico-y-los-datos/) | Por qué analizar datos; primeros pasos en Google Colab y Python |
| 2 | [Describir datos](semanas/02-describir-datos/) | Tipos de variables; media, mediana y dispersión; la tabla 1 |
| 3 | [Visualizar datos](semanas/03-visualizar-datos/) | Principios de una buena figura; histogramas, cajas y dispersión |
| 4 | [Probabilidad y distribuciones](semanas/04-probabilidad-y-distribuciones/) | Probabilidad para médicos; normal y binomial; teorema del límite central |
| 5 | [Estimar con confianza](semanas/05-estimar-con-confianza/) | Error estándar; intervalos de confianza; bootstrap |
| 6 | [El valor p](semanas/06-el-valor-p/) | Hipótesis nula; qué significa (y qué no) un valor p; poder y tamaño de muestra |
| 7 | [Pruebas estadísticas](semanas/07-pruebas-estadisticas/) | t de Student, Mann-Whitney, chi cuadrado; comparaciones múltiples y FDR |
| 8 | [Correlación y regresión lineal](semanas/08-correlacion-y-regresion-lineal/) | Correlación no es causalidad; mínimos cuadrados; R² |
| 9 | [Regresión logística](semanas/09-regresion-logistica/) | Odds y odds ratio; el modelo logístico |
| 10 | [Confusión y ajuste](semanas/10-confusion-y-ajuste/) | Confusores y regresión múltiple; grafos causales (DAGs) |
| 11 | [Del modelo al machine learning](semanas/11-del-modelo-al-machine-learning/) | Inferencia vs. predicción; sesgo y varianza; validación cruzada |
| 12 | [Árboles y bosques](semanas/12-arboles-y-bosques/) | Árboles de decisión; random forest; importancia de variables |
| 13 | [Gradient boosting y evaluación](semanas/13-gradient-boosting-y-evaluacion/) | XGBoost en intuición; sensibilidad, especificidad, ROC, calibración |
| 14 | [Redes neuronales](semanas/14-redes-neuronales/) | La neurona artificial; capas y retropropagación; cuándo usarlas (y cuándo no) en salud |
| 15 | [Taller de proyecto](semanas/15-taller-de-proyecto/) | Trabajo en pods con asesoría; análisis y armado de la presentación |
| 16 | [Presentaciones finales](semanas/16-presentaciones-finales/) | Presentación en formato de congreso; la ruta hacia la publicación |

## Estructura del repositorio

```
index.html              página del curso (GitHub Pages)
materiales/
  index.html            página de materiales
  semanas.json          lista de materiales por semana (edite este archivo)
semanas/NN-tema/
  diapositivas/         PDF de la clase
  cuadernos/            cuadernos .ipynb para Google Colab
datos/README.md         dónde conseguir cada base de datos (aquí no se guardan datos)
scripts/                validación de semanas.json
```

## Publicar los materiales de una semana

1. Copie los archivos a la carpeta de la semana, por ejemplo `semanas/01-el-medico-y-los-datos/cuadernos/01_nhanes.ipynb` y `semanas/01-el-medico-y-los-datos/diapositivas/01_clase.pdf`.
2. En `materiales/semanas.json`, complete la entrada de esa semana:

   ```json
   "fecha": "2026-10-04",
   "slides": "semanas/01-el-medico-y-los-datos/diapositivas/01_clase.pdf",
   "cuadernos": [
     { "titulo": "NHANES: primera exploración", "title": "NHANES: first look",
       "ruta": "semanas/01-el-medico-y-los-datos/cuadernos/01_nhanes.ipynb" }
   ],
   "video": "https://youtu.be/...",
   "grabacion": "https://..."
   ```

   `slides` acepta una ruta del repositorio (PDF) o un enlace completo (Google Slides, Canva). El botón **Abrir en Colab** se genera solo a partir de `ruta`.
3. Revise y suba:

   ```bash
   python scripts/validar_materiales.py
   git add . && git commit -m "Materiales de la semana 1" && git push
   ```

La página se actualiza en uno o dos minutos. Con `fecha` completa, la semana en curso aparece resaltada.

**Antes de subir un cuaderno**, borre las salidas que muestren filas de MIMIC-IV o PPMI (en Colab: *Editar → Borrar todas las salidas*). Ver [datos/README.md](datos/README.md).

## Configuración del sitio

- **Formulario de inscripción:** en `index.html`, busque `var FORM_URL = "";` y pegue el enlace del formulario. Mientras esté vacío, el botón de inscripción lleva a WhatsApp.
- **Syllabus:** reemplace `syllabus.pdf` por la nueva versión con el mismo nombre.
