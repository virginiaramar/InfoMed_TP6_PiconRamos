import requests



# Enviar el recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource,resource_type):
    url = f"https://launch.smarthealthit.org/v/r4/fhir/{resource_type}"
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
    url = f"https://launch.smarthealthit.org/v/r4/fhir/{resource_type}/{resource_id}"
    
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())



def search_by_identifier(identifier):
    
    search_url = f"https://launch.smarthealthit.org/v/r4/fhir/Patient?identifier={identifier}"
    print(search_url)
    response = requests.get(search_url, headers={"Accept": "application/fhir+json"})
    
    
    if response.status_code == 200:
        patients = response.json()
        print(patients)
        if patients:
            print("Paciente encontrado:")
            for patient in patients:
                print(patient)
        else:
            print("No se encontró ningún paciente con ese identificador.")
    else:
        print(f"Error al buscar paciente por identificador: {response.status_code}")
        print(response.json())

