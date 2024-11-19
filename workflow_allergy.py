from allergyIntol import create_allergy_intolerance
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

if __name__ == "__main__":

    # ID del anterior paciente creado
    patient_id = "2594637"  
    # Código de Penicillin G
    medication_code = "7980"  
    # Código de Hives (ronchas) en SNOMED
    reaction_code = "247472004" 
    # fecha de registro 
    date_recorded = "2024-11-19"  
    # Estado clínico (puede ser "active" o "inactive")
    clinical_status = "active" 
    # Estado de verificación (puede ser "unconfirmed" o "confirmed") 
    verification_status = "unconfirmed"  
    # Criticalidad de la alergia (puede ser "high", "low", etc.)
    criticality = "high"  

   
    allergy = create_allergy_intolerance(patient_id=patient_id, medication_code=medication_code, reaction_code=reaction_code, date_recorded=date_recorded, clinical_status=clinical_status, verification_status=verification_status, criticality=criticality)


    allergy_id = send_resource_to_hapi_fhir(allergy, 'AllergyIntolerance')
    
  
    if allergy_id:
        get_resource_from_hapi_fhir(allergy_id, 'AllergyIntolerance')
