import requests
from patient import create_patient_resource


# Enviar el recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource,resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        
        # Devolver el ID del recurso creado
        return response.json()['id']
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None

# Buscar el recurso por ID 
def get_resource_from_hapi_fhir(resource_id, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    family_name = "Doe"
    given_name = "John"
    birth_date = "1990-01-01"
    gender = "male"
    phone = None 

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    # Ver el recurso de paciente creado
    if patient_id:
        get_resource_from_hapi_fhir(patient_id,'Patient')