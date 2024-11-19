# Proyecto FHIR - Gestión de Pacientes y Alergias

Este proyecto implementa el estándar **FHIR (Fast Healthcare Interoperability Resources)** para crear y gestionar recursos de salud, específicamente **pacientes** y **alergias/intolerancias**. El objetivo es crear y gestionar los recursos **Patient** y **AllergyIntolerance**.

### Descripción de los Archivos

- **base.py**: Contiene las funciones para interactuar con el servidor FHIR (enviar recursos y obtener recursos).
- **workflow.py**: Define el flujo de trabajo para crear un paciente y enviar el recurso **Patient** al servidor.
- **workflow_allergy.py**: Define el flujo de trabajo para crear una alergia/intolerancia y asociarla a un paciente.
- **patient.py**: Contiene la función para crear el recurso **Patient**.
- **allergyIntol.py**: Contiene la función para crear el recurso **AllergyIntolerance**.

---

## Requisitos

Para ejecutar este proyecto, necesitarás tener Python 3.x y los siguientes paquetes instalados:

1. **fhir.resources**: Paquete para manejar recursos FHIR en Python.
    ```bash
    pip install fhir.resources
    ```

2. **requests**: Paquete para hacer solicitudes HTTP.
    ```bash
    pip install requests
    ```

---

## Flujo de Trabajo

### `workflow.py` - Crear un paciente

Este archivo crea un recurso **Patient** con los siguientes parámetros:

- **family_name**: Apellido del paciente.
- **given_name**: Nombre del paciente.
- **birth_date**: Fecha de nacimiento.
- **gender**: Género.
- **phone**: Teléfono (opcional).
- **identifier**: Identificador único del paciente (por ejemplo, un número de seguro social).

Una vez creado el paciente, se envía al servidor FHIR y se obtiene el ID del paciente.

### `workflow_allergy.py` - Crear una alergia/intolerancia

Este archivo crea un recurso **AllergyIntolerance** y lo asocia a un paciente. Los parámetros incluyen:

- **patient_id**: ID del paciente.
- **medication_code**: Código del medicamento causante de la alergia.
- **reaction_code**: Código SNOMED CT de la reacción (por ejemplo, **Hives**).
- **date_recorded**: Fecha de registro de la alergia.
- **clinical_status**: Estado clínico de la alergia (activo/inactivo).
- **verification_status**: Estado de verificación (confirmado/no confirmado).
- **criticality**: Gravedad de la alergia (alta/baja).

Una vez creado el recurso **AllergyIntolerance**, se envía al servidor FHIR y se obtiene el ID de la alergia.

---

## Funciones en el Proyecto

### `base.py` - Funciones para interactuar con el servidor FHIR

Este archivo contiene las funciones necesarias para enviar y recuperar recursos FHIR desde el servidor público de FHIR. Se usan dos funciones principales:

- `send_resource_to_hapi_fhir`: Enviar un recurso al servidor FHIR.
- `get_resource_from_hapi_fhir`: Recuperar un recurso del servidor FHIR usando su ID.

### `patient.py` - Crear un paciente

Este archivo contiene la función para crear un recurso **Patient**. Los parámetros utilizados incluyen el nombre, la fecha de nacimiento, el género y el identificador del paciente.

### `allergyIntol.py` - Crear AllergyIntolerance

Este archivo contiene la función para crear el recurso **AllergyIntolerance**. Se asocia a un paciente y registra la alergia/intolerancia con información sobre el medicamento, la reacción y la gravedad.

---

## Uso

1. **Crear un paciente**: Para crear un paciente, simplemente ejecuta `workflow.py`, que creará el recurso **Patient** con los datos proporcionados (por ejemplo, nombre, fecha de nacimiento, etc.) y lo enviará al servidor FHIR.
   
2. **Crear una alergia/intolerancia**: Una vez que el paciente haya sido creado, puedes ejecutar `workflow_allergy.py` para crear un recurso **AllergyIntolerance**. Este recurso se asociará con el ID del paciente y registrará la alergia/intolerancia a un medicamento, junto con detalles como la reacción y la gravedad.

---

## Notas

- El servidor FHIR utilizado en este proyecto es el servidor público [SMART Health IT](https://launch.smarthealthit.org/), que proporciona un entorno para probar y trabajar con recursos FHIR de manera accesible.
- Los recursos **Patient** y **AllergyIntolerance** son ejemplos comunes de cómo se gestionan los datos de salud dentro del estándar FHIR, permitiendo una interoperabilidad efectiva en sistemas de salud.
