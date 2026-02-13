"""
Example usage scenarios for the Medical Translation Error Injector.

This script demonstrates various ways to use the error injection tool
for different medical conversation scenarios.
"""

from medical_translation_errors import MedicalTranslationErrorInjector


def example_1_basic_usage():
    """Basic usage: single sentence error injection."""
    print("=" * 80)
    print("EXAMPLE 1: Basic Usage - Single Sentence")
    print("=" * 80)
    
    injector = MedicalTranslationErrorInjector(error_probability=0.25)
    
    text = "The patient has chronic hypertension and should take fifteen milligrams before breakfast daily."
    
    modified_text, errors = injector.inject_errors(text, seed=123)
    
    print(f"\nOriginal:  {text}")
    print(f"Modified:  {modified_text}")
    print(f"\nErrors introduced: {len(errors)}")
    for error in errors:
        print(f"  - '{error['original']}' → '{error['modified']}' ({error['error_type']})")
    print()


def example_2_doctor_patient_conversation():
    """Realistic doctor-patient conversation with errors."""
    print("=" * 80)
    print("EXAMPLE 2: Doctor-Patient Consultation")
    print("=" * 80)
    
    injector = MedicalTranslationErrorInjector(error_probability=0.18)
    
    conversation = [
        {
            'speaker': 'Doctor',
            'text': 'Good morning. How are you feeling today?'
        },
        {
            'speaker': 'Patient',
            'text': 'Not very well. I have been having chronic pain in my chest.'
        },
        {
            'speaker': 'Doctor',
            'text': 'I see. Have you noticed any symptoms like breathlessness or inflammation?'
        },
        {
            'speaker': 'Patient',
            'text': 'Yes, sometimes after exercise, but not always.'
        },
        {
            'speaker': 'Doctor',
            'text': 'Are you taking your hypertension medication? The dose is fifteen milligrams daily, correct?'
        },
        {
            'speaker': 'Patient',
            'text': 'Yes, I take it every morning before breakfast without fail.'
        },
        {
            'speaker': 'Doctor',
            'text': 'Good. We may need to increase the dose and add another medication. Do you have any allergy to antibiotics?'
        },
        {
            'speaker': 'Patient',
            'text': 'No, I have no allergies.'
        },
    ]
    
    modified_conversation, errors = injector.inject_errors_in_conversation(
        conversation, seed=456
    )
    
    print("\n--- ORIGINAL ---")
    for turn in conversation:
        print(f"{turn['speaker']}: {turn['text']}")
    
    print("\n--- WITH TRANSLATION ERRORS ---")
    for turn in modified_conversation:
        print(f"{turn['speaker']}: {turn['text']}")
    
    print(f"\n--- ERRORS SUMMARY ---")
    print(f"Total errors introduced: {len(errors)}")
    for i, error in enumerate(errors, 1):
        print(f"{i}. Turn {error['turn_index']}: '{error['original']}' → '{error['modified']}' ({error['error_type']})")
    print()


def example_3_medication_instructions():
    """Medication instruction scenario with dosage errors."""
    print("=" * 80)
    print("EXAMPLE 3: Medication Instructions (Critical Dosage Info)")
    print("=" * 80)
    
    injector = MedicalTranslationErrorInjector(error_probability=0.30)
    
    conversation = [
        {
            'speaker': 'Pharmacist',
            'text': 'Take this tablet twice daily, fifteen milligrams in the morning and fifteen milligrams in the evening.'
        },
        {
            'speaker': 'Patient',
            'text': 'Should I take it before or after meals?'
        },
        {
            'speaker': 'Pharmacist',
            'text': 'Take it after meals, not before. And never stop taking it without consulting your doctor.'
        },
        {
            'speaker': 'Patient',
            'text': 'What if I forget a dose?'
        },
        {
            'speaker': 'Pharmacist',
            'text': 'If you forget, take it as soon as you remember, but do not take double doses.'
        }
    ]
    
    modified_conversation, errors = injector.inject_errors_in_conversation(
        conversation, seed=789
    )
    
    print("\n--- ORIGINAL INSTRUCTIONS ---")
    for turn in conversation:
        print(f"{turn['speaker']}: {turn['text']}")
    
    print("\n--- TRANSLATED INSTRUCTIONS (with errors) ---")
    for turn in modified_conversation:
        print(f"{turn['speaker']}: {turn['text']}")
    
    print(f"\n--- CRITICAL ERRORS ---")
    critical_types = ['number_substitution', 'temporal_confusion', 'qualifier_omission']
    critical_errors = [e for e in errors if e['error_type'] in critical_types]
    
    if critical_errors:
        print(f"⚠️  Found {len(critical_errors)} critical errors that could affect patient safety:")
        for error in critical_errors:
            print(f"  - Turn {error['turn_index']}: '{error['original']}' → '{error['modified']}'")
            print(f"    Type: {error['error_type']}")
    else:
        print("No critical errors in this run.")
    print()


def example_4_reproducibility():
    """Demonstrate reproducibility with seeds."""
    print("=" * 80)
    print("EXAMPLE 4: Reproducibility with Random Seeds")
    print("=" * 80)
    
    injector = MedicalTranslationErrorInjector(error_probability=0.20)
    
    text = "The patient has acute infection and needs to start antibiotics immediately after breakfast."
    
    print(f"\nOriginal text: {text}\n")
    
    # Run 1 with seed
    print("Run 1 (seed=100):")
    modified_1, errors_1 = injector.inject_errors(text, seed=100)
    print(f"  Result: {modified_1}")
    print(f"  Errors: {len(errors_1)}")
    
    # Run 2 with same seed
    print("\nRun 2 (seed=100):")
    modified_2, errors_2 = injector.inject_errors(text, seed=100)
    print(f"  Result: {modified_2}")
    print(f"  Errors: {len(errors_2)}")
    
    # Verify reproducibility
    print(f"\nResults identical: {modified_1 == modified_2}")
    
    # Run 3 with different seed
    print("\nRun 3 (seed=200):")
    modified_3, errors_3 = injector.inject_errors(text, seed=200)
    print(f"  Result: {modified_3}")
    print(f"  Errors: {len(errors_3)}")
    
    print(f"\nResults different from Run 1: {modified_1 != modified_3}")
    print()


def example_5_custom_error_probability():
    """Show effect of different error probabilities."""
    print("=" * 80)
    print("EXAMPLE 5: Effect of Different Error Probabilities")
    print("=" * 80)
    
    text = "The patient with chronic hypertension should take fifteen milligrams daily before breakfast and avoid infection."
    
    print(f"\nOriginal: {text}\n")
    
    probabilities = [0.05, 0.15, 0.30, 0.50]
    
    for prob in probabilities:
        injector = MedicalTranslationErrorInjector(error_probability=prob)
        modified_text, errors = injector.inject_errors(text, seed=999)
        
        print(f"Error probability: {prob:.0%}")
        print(f"  Modified: {modified_text}")
        print(f"  Errors introduced: {len(errors)}")
        print()


def main():
    """Run all examples."""
    print("\n" + "=" * 80)
    print("MEDICAL TRANSLATION ERROR INJECTOR - EXAMPLE SCENARIOS")
    print("=" * 80 + "\n")
    
    example_1_basic_usage()
    example_2_doctor_patient_conversation()
    example_3_medication_instructions()
    example_4_reproducibility()
    example_5_custom_error_probability()
    
    print("=" * 80)
    print("All examples completed successfully!")
    print("=" * 80)


if __name__ == '__main__':
    main()
