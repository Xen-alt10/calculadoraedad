# Proyecto: Calculadora de Edad — LPR 2026

**Escuela de Educación Secundaria Técnica N° 1 — Vicente López**  
**Curso:** 5° Año — Especialidad Computación / Programación  
**Materia:** Laboratorio de Programación (LPR)  
**Profesor:** Prof. York Mansilla Muñoz  
**Estudiante:** Alexander Luca Veit

## 📌 Descripción de la Actividad

Este proyecto es una actividad de diagnóstico y nivelación. Consiste en desarrollar un programa que calcule la edad exacta de una persona comparando su fecha de nacimiento con la fecha actual, validando que los datos existen en el calendario real (controlando años bisiestos y días de cada mes).

El objetivo principal es comparar la lógica y la sintaxis de dos paradigmas diferentes:

- **C++ ANSI estándar:** Lenguaje estructurado, de tipado estático y bajo nivel.
- **Python 3:** Lenguaje multiparadigma, de tipado dinámico y alto nivel.

## 🗂 Estructura del Repositorio

```text
calculadoraedad/
├── proyecto_cpp/
│   └── main.cpp        # Implementación en C++
├── proyecto_python/
│   └── main.py         # Implementación en Python
├── docs/
│   └── InformeProyectoCalculadoraEdad.pdf  # Informe del proyecto
├── .gitignore
├── LICENSE             # Licencia MIT
└── README.md
```

## 💻 Implementaciones

### 1) C++ (`proyecto_cpp/main.cpp`)

- **Validación de fecha:** Verifica rango de años (1900-2026), meses (1-12), días (1-31). Controla meses con 30 días (abril, junio, septiembre, noviembre) y febrero según año bisiesto.
- **Cálculo de edad:** Calcula la edad en años tomando como referencia la fecha actual fija en el código (`08/07/2026`). Si aún no cumplió años en el año actual, resta 1.
- **Salida:** Muestra la fecha de hoy, la edad calculada en años y una cabecera personalizada.

**Nota:** En la cabecera aparece "Alexander Veit". Según la consigna, se debe reemplazar por el nombre y apellido real del estudiante al ejecutar/editar.

### 2) Python (`proyecto_python/main.py`)

- **Ingreso validado:** Función `pedir_fecha()` que solicita día/mes/año, valida con `datetime.date`, rechaza fechas futuras, años menores a 1900 e ingresos inválidos (no numéricos o fechas inexistentes).
- **Cálculo de edad exacta:** Función `calcular_edad()` que obtiene la edad en años, meses, semanas, días y el total de días vividos. Utiliza el cálculo por cumpleaños (comparando mes/día) y operaciones con fechas para obtener los valores restantes con precisión (incluye años bisiestos automáticamente).
- **Salida:** Muestra la edad exacta desglosada y el total de días vividos.

## 🛠️ Requisitos e Instalación

Para ejecutar y colaborar en este proyecto necesitas:

- **Python 3.12+** (marcar "Add python.exe to PATH" durante la instalación).
- **Compilador G++ / GCC** (instalado mediante MinGW en Windows 10/11).
- **Git** (configurado con rama por defecto `main`).
- **IDE recomendado:** Visual Studio Code (con extensiones como "Code Runner" para facilitar la ejecución).

### Clonar el repositorio

```bash
git clone https://github.com/Xen-alt10/calculadoraedad.git
cd calculadoraedad
```

## ▶️ Cómo ejecutar

### En C++

Desde la carpeta `proyecto_cpp/`:

```bash
g++ -o calculadoraedad main.cpp
./calculadoraedad
```

O ejecutar directamente con Code Runner desde VS Code.

### En Python

Desde la carpeta `proyecto_python/`:

```bash
python main.py
```

O ejecutar directamente con Code Runner desde VS Code.

## 🧪 Funcionalidades destacadas

- **Validación robusta** (fechas inexistentes, años bisiestos, límites razonables).
- **Cálculo preciso** en Python (desglose en años/meses/semanas/días y total de días vividos).
- **Comparativa entre paradigmas** (estructurado C++ vs multiparadigma Python).
- **Documentación**: informe académico en `docs/` siguiendo lineamientos APA 7ª edición.

## 👤 Autor

- **Alexander Luca Veit** — Programador / Estudiante  
  GitHub: [Xen-alt10](https://github.com/Xen-alt10)  
  Repositorio: [calculadoraedad](https://github.com/Xen-alt10/calculadoraedad)

## 📄 Licencia

Este proyecto está bajo licencia [MIT](LICENSE). Copyright (c) 2026 Xen-alt10.
