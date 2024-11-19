from fhir.resources.allergyintolerance import AllergyIntolerance, AllergyIntoleranceReaction
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.codeablereference import CodeableReference
from fhir.resources.reference import Reference
from datetime import date


def create_allergy_intolerance(patient_id=None, medication_code=None, reaction_code=None, date_recorded=None, clinical_status=None, verification_status=None, criticality=None):
    
    
    # Crear la referencia al paciente
    patient_reference = Reference(reference=f"Patient/{patient_id}")
    
    # Crear el recurso AllergyIntolerance 
    allergy = AllergyIntolerance(patient=patient_reference)
    
   
    if clinical_status:
        clinical_status_coding = Coding(
            system="http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical",
            code=clinical_status,
            display="Active" if clinical_status == "active" else "Inactive"
        )
        allergy.clinicalStatus = CodeableConcept(coding=[clinical_status_coding])
    
    
    if verification_status:
        verification_status_coding = Coding(
            system="http://terminology.hl7.org/CodeSystem/allergyintolerance-verification",
            code=verification_status,
            display="Unconfirmed" if verification_status == "unconfirmed" else "Confirmed"
        )
        allergy.verificationStatus = CodeableConcept(coding=[verification_status_coding])
    
    
    if criticality:
        allergy.criticality = criticality
    
    
    if medication_code:
        medication_coding = Coding(
            system="http://www.nlm.nih.gov/research/umls/rxnorm",
            code=medication_code,
            display="Penicillin G"  
        )
        allergy.code = CodeableConcept(coding=[medication_coding])
    
   
    if date_recorded:
        allergy.recordedDate = date.fromisoformat(date_recorded)
    
   
    if reaction_code:
        reaction_coding = Coding(
            system="http://snomed.info/sct",
            code=reaction_code,
            display="Hives"  
        )
        
        manifestation_concept = CodeableConcept(coding=[reaction_coding])
        manifestation_reference = CodeableReference(concept=manifestation_concept)
        reaction = AllergyIntoleranceReaction(manifestation=[manifestation_reference])
        allergy.reaction = [reaction]
    
    return allergy


