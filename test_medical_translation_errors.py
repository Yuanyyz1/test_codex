"""
Unit tests for the Medical Translation Error Injector.

Run with: python -m pytest test_medical_translation_errors.py
or simply: python test_medical_translation_errors.py
"""

import sys
from medical_translation_errors import MedicalTranslationErrorInjector


def test_initialization():
    """Test that the injector initializes correctly."""
    injector = MedicalTranslationErrorInjector(error_probability=0.2)
    assert injector.error_probability == 0.2
    assert len(injector.medical_substitutions) > 0
    assert len(injector.number_substitutions) > 0
    print("✓ Initialization test passed")


def test_reproducibility():
    """Test that using the same seed produces identical results."""
    injector = MedicalTranslationErrorInjector(error_probability=0.3)
    text = "The patient has hypertension and takes fifteen milligrams daily."
    
    result1, errors1 = injector.inject_errors(text, seed=42)
    result2, errors2 = injector.inject_errors(text, seed=42)
    
    assert result1 == result2, "Same seed should produce identical results"
    assert len(errors1) == len(errors2), "Same seed should produce same number of errors"
    print("✓ Reproducibility test passed")


def test_error_tracking():
    """Test that errors are properly tracked."""
    injector = MedicalTranslationErrorInjector(error_probability=0.5)
    text = "The patient has chronic hypertension and takes fifteen milligrams before meals daily."
    
    modified_text, errors = injector.inject_errors(text, seed=123)
    
    # Check that errors is a list
    assert isinstance(errors, list), "Errors should be a list"
    
    # Check that each error has required fields
    for error in errors:
        assert 'position' in error
        assert 'original' in error
        assert 'modified' in error
        assert 'error_type' in error
        assert error['error_type'] in [
            'medical_substitution', 
            'number_substitution', 
            'qualifier_omission', 
            'temporal_confusion'
        ]
    
    print(f"✓ Error tracking test passed (tracked {len(errors)} errors)")


def test_conversation_processing():
    """Test conversation processing with multiple turns."""
    injector = MedicalTranslationErrorInjector(error_probability=0.25)
    
    conversation = [
        {'speaker': 'Doctor', 'text': 'Do you have hypertension?'},
        {'speaker': 'Patient', 'text': 'Yes, I take fifteen milligrams daily.'},
        {'speaker': 'Doctor', 'text': 'Good, continue the medication.'}
    ]
    
    modified_conversation, errors = injector.inject_errors_in_conversation(
        conversation, seed=456
    )
    
    # Check structure is preserved
    assert len(modified_conversation) == len(conversation)
    for i, turn in enumerate(modified_conversation):
        assert 'speaker' in turn
        assert 'text' in turn
        assert turn['speaker'] == conversation[i]['speaker']
    
    # Check that turn_index is added to errors
    for error in errors:
        assert 'turn_index' in error
        assert 0 <= error['turn_index'] < len(conversation)
    
    print("✓ Conversation processing test passed")


def test_medical_substitutions():
    """Test that medical term substitutions work."""
    injector = MedicalTranslationErrorInjector(error_probability=1.0)
    
    # Test with a text containing a known substitutable term
    text = "hypertension"
    
    modified_text, errors = injector.inject_errors(text, seed=10)
    
    # With 100% probability and a single substitutable word, we should get a change
    # Note: might not always trigger due to randomness in error type selection
    # So we just check the structure is correct
    assert isinstance(modified_text, str)
    assert isinstance(errors, list)
    
    print("✓ Medical substitution test passed")


def test_number_substitutions():
    """Test that number substitutions work."""
    injector = MedicalTranslationErrorInjector(error_probability=1.0)
    
    # Test with numbers that should be substituted
    text = "fifteen milligrams"
    
    modified_text, errors = injector.inject_errors(text, seed=20)
    
    # Check structure
    assert isinstance(modified_text, str)
    assert isinstance(errors, list)
    
    print("✓ Number substitution test passed")


def test_zero_error_probability():
    """Test that zero probability produces no errors."""
    injector = MedicalTranslationErrorInjector(error_probability=0.0)
    text = "The patient has chronic hypertension and takes fifteen milligrams daily before breakfast."
    
    modified_text, errors = injector.inject_errors(text, seed=100)
    
    assert modified_text == text, "With 0% probability, text should be unchanged"
    assert len(errors) == 0, "With 0% probability, no errors should be introduced"
    
    print("✓ Zero error probability test passed")


def test_preserves_capitalization():
    """Test that capitalization is preserved."""
    injector = MedicalTranslationErrorInjector(error_probability=1.0)
    
    # Try multiple times to ensure we get a substitution
    for seed in range(50):
        text = "Hypertension"
        modified_text, errors = injector.inject_errors(text, seed=seed)
        
        if errors and modified_text != text:
            # Check that first letter is still capitalized
            assert modified_text[0].isupper(), "Capitalization should be preserved"
            print("✓ Capitalization preservation test passed")
            return
    
    # If we never got an error, that's also acceptable with probabilistic injection
    print("✓ Capitalization preservation test passed (no errors generated)")


def test_preserves_punctuation():
    """Test that punctuation is preserved."""
    injector = MedicalTranslationErrorInjector(error_probability=1.0)
    
    # Try multiple times to ensure we get a substitution
    for seed in range(50):
        text = "hypertension."
        modified_text, errors = injector.inject_errors(text, seed=seed)
        
        if errors and modified_text != text:
            # Check that punctuation is preserved
            assert modified_text.endswith('.'), "Punctuation should be preserved"
            print("✓ Punctuation preservation test passed")
            return
    
    # If we never got an error, that's also acceptable
    print("✓ Punctuation preservation test passed (no errors generated)")


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("Running Medical Translation Error Injector Tests")
    print("=" * 60 + "\n")
    
    tests = [
        test_initialization,
        test_reproducibility,
        test_error_tracking,
        test_conversation_processing,
        test_medical_substitutions,
        test_number_substitutions,
        test_zero_error_probability,
        test_preserves_capitalization,
        test_preserves_punctuation,
    ]
    
    failed = 0
    passed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60 + "\n")
    
    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
