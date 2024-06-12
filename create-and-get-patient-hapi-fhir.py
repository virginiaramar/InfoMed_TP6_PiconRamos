import requests
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint

# Crear el recurso FHIR de paciente con parámetros opcionales
def create_patient_resource(family_name=None, given_name=None, birth_date=None, gender=None, phone=None):
    patient = Patient()
    
    # Agregar el nombre del paciente si está disponible
    if family_name or given_name:
        name = HumanName()
        if family_name:
            name.family = family_name
        if given_name:
            name.given = [given_name]
        patient.name = [name]
    
    # Agregar la fecha de nacimiento si está disponible
    if birth_date:
        patient.birthDate = birth_date

    # Agregar el género si está disponible
    if gender:
        patient.gender = gender

    # Agregar información de contacto si está disponible
    if phone:
        contact = ContactPoint()
        contact.system = "phone"
        contact.value = phone
        contact.use = "mobile"
        patient.telecom = [contact]

    return patient

# Enviar el recurso FHIR al servidor HAPI FHIR
def send_patient_to_hapi_fhir(patient):
    url = "http://hapi.fhir.org/baseR4/Patient"
    headers = {"Content-Type": "application/fhir+json"}
    patient_json = patient.json()

    response = requests.post(url, headers=headers, data=patient_json)

    if response.status_code == 201:
        print("Paciente creado exitosamente")
        # Imprimir toda la respuesta para depuración
        #print("Response Headers:", response.headers)
        #print("Response JSON:", response.json())
        
        # Devolver el ID del paciente creado
        location_header = response.headers.get('Location')
        if location_header and "Patient" in location_header:
            patient_id = location_header.split('/')[-1]
            return response.json()['id']
        else:
            print("El recurso creado no es un paciente o el ID no se pudo obtener correctamente.")
            return None
    else:
        print(f"Error al crear el paciente: {response.status_code}")
        print(response.json())
        return None

# Ver el recurso FHIR de paciente por ID
def get_patient_from_hapi_fhir(patient_id):
    url = f"http://hapi.fhir.org/baseR4/Patient/{patient_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        patient = Patient.parse_obj(response.json())
        print(patient.json(indent=2))
    else:
        print(f"Error al obtener el paciente: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    # Parámetros del paciente (puedes dejar algunos vacíos)
    family_name = "Doe"
    given_name = "John"
    birth_date = "1990-01-01"
    gender = "male"
    phone = None  # Este parámetro se deja vacío

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone)
    patient_id = send_patient_to_hapi_fhir(patient)

    # Ver el recurso de paciente creado
    if patient_id:
        get_patient_from_hapi_fhir(patient_id)