from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, search_by_identifier

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    id_provisional = "builder"
    family_name = "López"
    given_name = "Juan"
    birth_date = "1986-06-29"
    gender = "male"
    phone = None 
    identifier = "1226548"

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(id_provisional, identifier, family_name, given_name, birth_date, gender, phone)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')
    

    # Ver el recurso de paciente creado
    if patient_id:
        get_resource_from_hapi_fhir(patient_id,'Patient')
    
    search_patient=search_by_identifier(identifier)