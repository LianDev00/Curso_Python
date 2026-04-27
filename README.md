# Curso de Python

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/status-en%20progreso-brightgreen)

Repositorio personal donde documento mi aprendizaje de **Python** desde cero, con notebooks de Jupyter organizados por tema, ejercicios resueltos y prácticas adicionales.

---

## Sobre mí
Estoy aprendiendo Python con un enfoque práctico: cada tema lo cubro con teoría breve y bastantes ejercicios para reforzar la idea. Mi objetivo a mediano plazo es usar Python para **automatización** y **análisis de datos**.

---

## Ruta de aprendizaje

| Nº | Notebook | Tema | Conceptos clave |
|----|----------|------|-----------------|
| 1  | `1_cadenas.ipynb` | Cadenas | `str`, métodos, formateo, f-strings |
| 3  | `3_slicing.ipynb` | Slicing | Índices, rangos, paso negativo |
| 4  | `4_condicionales.ipynb` | Condicionales | `if`, `elif`, `else`, operadores lógicos |
| 5  | `5_for.ipynb` | Bucles `for` | Iteración, `range`, `enumerate` |
| 6  | `6_while.ipynb` | Bucles `while` | Condiciones, `break`, `continue` |
| 7  | `7_Estructura_datos.ipynb` | Estructuras de datos | Listas, tuplas, diccionarios, sets |
| 8  | `8_funciones.ipynb` | Funciones | Parámetros, `return`, scope, desafíos |
| 9  | `9_try_except.ipynb` | Manejo de errores | `try/except`, `raise`, validación |
| 10 | `10_list_comprehensions.ipynb` | List comprehensions | Sintaxis compacta, filtros, anidadas |
| 11 | `11_modulos.ipynb` | Módulos estándar | `random`, `datetime`, `os`, `string` |
| 12 | `12_archivos.ipynb` | Archivos | Lectura, escritura, `with`, CSV |
| 13 | `13_POO.ipynb` | POO (teoría) | Clases, `__init__`, herencia, `super`, encapsulación, dunder methods |
| 14 | `14_POO_Ejercicios.ipynb` | POO — ejercicios | 10 ejercicios graduados (fáciles → difíciles) |
| 15 | `15_POO_Practica.ipynb` | POO + validación | Combina clases con `try/except` y `raise` |
| 16 | `16_POO_Practica.ipynb` | POO + módulos/archivos | Integra clases con `random`, `datetime`, archivos |

### Repasos y fases

- `fase1.ipynb` — Ejercicios integradores de la **Fase 1** (fundamentos)
- `fase2.ipynb` — Ejercicios complejos de la **Fase 2**
- `loops.ipynb` — Práctica adicional de bucles y strings

---

## CS50P — Harvard

En paralelo estoy resolviendo los problem sets del curso **[CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)**:

- `CS50_01_str_func.ipynb` — Strings y funciones
- `CS50_02_condicionales.ipynb` — Condicionales
- `CS50_03_loops.ipynb` — Bucles

---

## Recursos extra

- **`Libro_Python/`** — Apuntes en HTML por tema (teoría organizada como un mini-libro de consulta).
- **`Practicas/`** — Scripts independientes:
  - `Adivinar_numero.py` — juego de adivinar números
  - `Generar_password.py` — generador de contraseñas seguras

---

## Cómo ejecutar los notebooks

### Requisitos
- Python 3.10 o superior
- Jupyter Notebook o VS Code con la extensión de Jupyter

### Instalación rápida

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd Curso_Python

# (Opcional) crear entorno virtual
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# Instalar Jupyter
pip install jupyter

# Abrir
jupyter notebook
```

O simplemente abre la carpeta en **VS Code** y haz clic en cualquier `.ipynb`.

---

## Próximos temas

Una vez consolidada la base, la ruta de aprendizaje continúa hacia automatización y análisis de datos:

1. **`requests` + APIs** — consumir servicios externos (clima, GitHub, criptomonedas)
2. **`sqlite3`** — persistencia de datos en bases ligeras
3. **Pandas** — análisis y manipulación de datos
4. **Matplotlib** — visualización
5. **NumPy** — cálculo numérico

---

## Licencia

Repositorio de uso personal con fines educativos.
