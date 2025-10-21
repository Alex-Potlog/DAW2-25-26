# DAW2 - Desarrollo de Aplicaciones Web 2

Repositorio para las actividades, ejercicios y documentación del segundo año de Desarrollo de Aplicaciones Web de Thos i Codina.

## 📁 Estructura del Repositorio

Este repositorio está organizado por estudiante, con cada estudiante teniendo su propio directorio que contiene subdirectorios para diferentes módulos y lenguajes de programación:

```
DAW2/
├── [Nombre Estudiante]/
│   ├── M6/             # Javascript - Alfredo Ballestero
│   ├── M7/             # PHP - Teresa Gistall
│   ├── M8/             # Git y esas cosas - Jordi Llorente
│   ├── M9/             # Interfaces - Alfredo Ballestero
│   ├── M9/             # Python - Miquel Crespo
│   └── M12/            # Projecte final de curs - Miquel Crespo i Jordi Llorente
├── creaPersona.sh      # Script para añadir nuevos estudiantes
├── asignExamen.sh      # Script para crear estructura de examen
└── README.md
```

## 👥 Estudiantes

- Alex
- ErJaLo (Jan)
- Gouthar (John)
- Mar
- Marta
- Nico
- Oscar
- Roger
- Xavi
- saturnoV18 (Adrian)

## 📚 Módulos
- **M6**: Desarrollo parte del cliente
- **M7**: Programacion con PHP, Usualmente no explica nada mas que lo que pone en w3schools
- **M8**: Despliegue de aplicaciones
- **M9**: Diseño y desarrollo de interfaces
- **MOPT**: Programacion con Python
- **M12**: Proyecto final de curso

## 🛠️ Scripts Disponibles

### Añadir un Nuevo Estudiante

Para añadir un nuevo estudiante a la estructura del proyecto, utiliza el script proporcionado:

```bash
./creaPersona.sh [nombre-estudiante]
```

Esto creará automáticamente la estructura de directorios necesaria con archivos placeholder.

Luego confirma los cambios:
```bash
git add .
git commit -m "Añadir [nombre-estudiante] al repositorio"
```

### Crear Estructura de Examen

Para crear una carpeta de examen con su estructura correspondiente:

```bash
./asignExamen.sh [nombre-examen]
```

Este script:
- Crea un directorio `Examen-[nombre-examen]`
- Genera dos subdirectorios: `apuntes` y `ejercicios`
- Añade archivos placeholder `archivo.txt` en cada subdirectorio

**Ejemplo de uso:**
```bash
./asignExamen.sh M7-PHP
# Creará: Examen-M7-PHP/apuntes/ y Examen-M7-PHP/ejercicios/
```

## 🤝 Contribuir

Cada estudiante debe:
- Trabajar en su propio directorio
- Mantener su código organizado por módulo/lenguaje
- Incluir mensajes de commit significativos
- Evitar modificar los directorios de otros estudiantes
- Antes de hacer un commit, asegurarse de tener la ultima version (fetch y pull) para no entorpecer a los demás

## 📝 Notas

- Los archivos `archivo.txt` vacíos sirven como placeholders para mantener la estructura de directorios en Git
- Seguir las pautas del curso para convenciones de nomenclatura y estructura del código
- Se puede realizar consultas al codigo de los demas, para esto es este proyecto en git, pero evitemos hacer cambios aun si son minusculos

## 📄 Licencia

Este es un repositorio educativo para fines de trabajo del curso.

---

*DAW2 - Desarrollo de Aplicaciones Web, Curso 2025-2026*
