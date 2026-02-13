"""
Comprehensive Demo: Medical Translation Error Insertion

This script demonstrates the full capabilities of the Medical Translation Error 
Injector using the sample conversations dataset.
"""

from medical_translation_errors import MedicalTranslationErrorInjector
from sample_conversations import SAMPLE_CONVERSATIONS, get_all_titles


def demo_with_sample_conversations():
    """Run the error injector on all sample conversations."""
    
    print("\n" + "=" * 80)
    print("MEDICAL TRANSLATION ERROR INJECTION - COMPREHENSIVE DEMO")
    print("=" * 80)
    
    # Create injector with moderate error probability
    injector = MedicalTranslationErrorInjector(error_probability=0.18)
    
    # Process each sample conversation
    for idx, sample in enumerate(SAMPLE_CONVERSATIONS, 1):
        print(f"\n{'=' * 80}")
        print(f"SAMPLE {idx}: {sample['title']}")
        print("=" * 80)
        
        conversation = sample['conversation']
        
        # Show original
        print("\n--- ORIGINAL CONVERSATION ---")
        for turn in conversation:
            print(f"{turn['speaker']:12s}: {turn['text']}")
        
        # Inject errors with a unique seed for each conversation
        modified_conversation, errors = injector.inject_errors_in_conversation(
            conversation, seed=100 + idx
        )
        
        # Show modified version
        print("\n--- WITH TRANSLATION ERRORS ---")
        for turn in modified_conversation:
            print(f"{turn['speaker']:12s}: {turn['text']}")
        
        # Show error details
        print(f"\n--- ERROR ANALYSIS ---")
        if errors:
            print(f"Total errors introduced: {len(errors)}")
            
            # Group errors by type
            error_by_type = {}
            for error in errors:
                error_type = error['error_type']
                if error_type not in error_by_type:
                    error_by_type[error_type] = []
                error_by_type[error_type].append(error)
            
            print("\nErrors by type:")
            for error_type, error_list in error_by_type.items():
                print(f"  - {error_type}: {len(error_list)}")
            
            print("\nDetailed error list:")
            for i, error in enumerate(errors, 1):
                print(f"  {i}. Turn {error['turn_index']}, Position {error['position']}")
                print(f"     '{error['original']}' → '{error['modified']}'")
                print(f"     Type: {error['error_type']}")
                
                # Flag critical errors
                if error['error_type'] in ['number_substitution', 'qualifier_omission']:
                    print(f"     ⚠️  CRITICAL: This error could affect patient safety!")
        else:
            print("No errors were introduced in this conversation.")
    
    print("\n" + "=" * 80)
    print("DEMO COMPLETED")
    print("=" * 80)


def demo_error_severity_analysis():
    """Demonstrate how to analyze error severity."""
    
    print("\n" + "=" * 80)
    print("ERROR SEVERITY ANALYSIS")
    print("=" * 80)
    
    injector = MedicalTranslationErrorInjector(error_probability=0.25)
    
    # Use the diabetes management conversation
    conversation = SAMPLE_CONVERSATIONS[3]['conversation']
    
    print(f"\nAnalyzing: {SAMPLE_CONVERSATIONS[3]['title']}")
    print("-" * 80)
    
    # Run multiple times to get statistics
    num_runs = 10
    critical_errors_per_run = []
    total_errors_per_run = []
    
    for run in range(num_runs):
        modified_conversation, errors = injector.inject_errors_in_conversation(
            conversation, seed=200 + run
        )
        
        total_errors = len(errors)
        critical_errors = sum(
            1 for e in errors 
            if e['error_type'] in ['number_substitution', 'qualifier_omission']
        )
        
        total_errors_per_run.append(total_errors)
        critical_errors_per_run.append(critical_errors)
    
    print(f"\nStatistics from {num_runs} runs:")
    print(f"  Average total errors: {sum(total_errors_per_run) / num_runs:.1f}")
    print(f"  Average critical errors: {sum(critical_errors_per_run) / num_runs:.1f}")
    print(f"  Max errors in a run: {max(total_errors_per_run)}")
    print(f"  Min errors in a run: {min(total_errors_per_run)}")
    
    # Show one example with errors
    print(f"\n--- Example run with errors ---")
    for run in range(num_runs):
        modified_conversation, errors = injector.inject_errors_in_conversation(
            conversation, seed=200 + run
        )
        if errors:
            print(f"\nRun {run + 1} (seed={200 + run}):")
            for error in errors:
                severity = "CRITICAL" if error['error_type'] in ['number_substitution', 'qualifier_omission'] else "Minor"
                print(f"  [{severity:8s}] '{error['original']}' → '{error['modified']}' ({error['error_type']})")
            break


def demo_customization():
    """Demonstrate how to customize the error injector."""
    
    print("\n" + "=" * 80)
    print("CUSTOMIZATION DEMO")
    print("=" * 80)
    
    # Create a custom injector
    injector = MedicalTranslationErrorInjector(error_probability=0.20)
    
    # Add custom medical term substitutions
    print("\nAdding custom medical terms...")
    injector.medical_substitutions['asthma'] = ['anemia']
    injector.medical_substitutions['anemia'] = ['asthma']
    injector.medical_substitutions['diabetes'] = ['dialysis']
    
    # Add custom number confusions
    print("Adding custom number confusions...")
    injector.number_substitutions['100'] = '1000'
    injector.number_substitutions['1000'] = '100'
    
    # Test with custom text
    text = "The patient has asthma and diabetes. Blood glucose is 100 mg/dL."
    
    print(f"\nOriginal text:")
    print(f"  {text}")
    
    # Try multiple seeds to show custom substitutions
    print(f"\nTesting custom substitutions (5 runs):")
    for seed in range(300, 305):
        modified_text, errors = injector.inject_errors(text, seed=seed)
        if errors:
            print(f"\n  Seed {seed}:")
            print(f"    Result: {modified_text}")
            print(f"    Errors: {', '.join([f'{e['original']}→{e['modified']}' for e in errors])}")


def main():
    """Run all demos."""
    
    # Main demo with all conversations
    demo_with_sample_conversations()
    
    # Error severity analysis
    demo_error_severity_analysis()
    
    # Customization demo
    demo_customization()
    
    print("\n" + "=" * 80)
    print("ALL DEMOS COMPLETED SUCCESSFULLY!")
    print("=" * 80)
    print("\nKey Takeaways:")
    print("  • The error injector produces natural and subtle translation errors")
    print("  • Errors include medical term confusion, number mistakes, and qualifier omissions")
    print("  • Critical errors (numbers, qualifiers) are flagged for patient safety")
    print("  • The system is customizable and reproducible with seeds")
    print("  • Useful for training, testing, and research in medical interpretation")
    print("=" * 80 + "\n")


if __name__ == '__main__':
    main()
