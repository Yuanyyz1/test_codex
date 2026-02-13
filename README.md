# Medical Translation Error Insertion

This repository provides tools for inserting natural and subtle translation errors into medical conversations. This is useful for:

- Training medical interpreters to detect translation errors
- Testing error detection systems
- Creating realistic datasets for machine learning models
- Educational purposes in medical interpretation courses

## Features

- **Natural Error Types**: Implements several types of realistic translation errors:
  - Medical term substitutions (e.g., hypertension ↔ hypotension)
  - Number confusions (e.g., fifteen ↔ fifty)
  - Qualifier omissions (e.g., omitting "not" or "no")
  - Temporal/directional confusions (e.g., before ↔ after)

- **Configurable Error Rate**: Adjust the probability of error insertion
- **Reproducible Results**: Use random seeds for consistent outputs
- **Detailed Error Tracking**: Get full information about what errors were introduced

## Installation

```bash
# Clone the repository
git clone https://github.com/Yuanyyz1/test_codex.git
cd test_codex

# No additional dependencies required (uses Python standard library only)
```

## Usage

### Basic Usage

```python
from medical_translation_errors import MedicalTranslationErrorInjector

# Create an injector with 15% error probability (default)
injector = MedicalTranslationErrorInjector(error_probability=0.15)

# Inject errors into a text
text = "The patient has hypertension and takes fifteen milligrams daily."
modified_text, errors = injector.inject_errors(text, seed=42)

print("Original:", text)
print("Modified:", modified_text)
print("Errors:", errors)
```

### Conversation Processing

```python
from medical_translation_errors import MedicalTranslationErrorInjector

# Create injector
injector = MedicalTranslationErrorInjector(error_probability=0.20)

# Define a conversation
conversation = [
    {
        'speaker': 'Doctor',
        'text': 'Do you have any allergies to medications?'
    },
    {
        'speaker': 'Patient',
        'text': 'Yes, I am allergic to penicillin.'
    }
]

# Inject errors
modified_conversation, errors = injector.inject_errors_in_conversation(
    conversation, seed=42
)

# Display results
for turn in modified_conversation:
    print(f"{turn['speaker']}: {turn['text']}")
```

### Running the Demo

```bash
python medical_translation_errors.py
```

This will run a demonstration showing:
- An original medical conversation
- The same conversation with injected errors
- A detailed list of all errors introduced

## Error Types

### 1. Medical Term Substitution
Replaces medical terms with similar-sounding but different terms:
- hypertension → hypotension
- infection → inflammation
- malignant → benign

### 2. Number Confusion
Confuses numbers that sound similar:
- fifteen → fifty
- thirteen → thirty
- 15 → 50

### 3. Qualifier Omission
Removes critical qualifiers that change meaning:
- "no symptoms" → "symptoms"
- "not allergic" → "allergic"

### 4. Temporal/Directional Confusion
Swaps temporal or directional terms:
- before → after
- morning → evening
- increase → decrease

## Customization

You can extend the error types by modifying the dictionaries in the `MedicalTranslationErrorInjector` class:

```python
injector = MedicalTranslationErrorInjector()

# Add custom medical term substitutions
injector.medical_substitutions['diabetes'] = ['diabetic']

# Add custom number confusions
injector.number_substitutions['100'] = '1000'

# Inject errors with custom dictionary
text = "The patient has diabetes."
modified_text, errors = injector.inject_errors(text)
```

## Parameters

### MedicalTranslationErrorInjector

**Constructor:**
- `error_probability` (float): Probability of introducing an error at each opportunity (0.0 to 1.0). Default: 0.15

**Methods:**

- `inject_errors(text, seed=None)`: Inject errors into a single text string
  - Returns: (modified_text, list_of_errors)

- `inject_errors_in_conversation(conversation, seed=None)`: Inject errors into a conversation
  - conversation: List of dicts with 'speaker' and 'text' keys
  - Returns: (modified_conversation, list_of_all_errors)

## Example Output

```
ORIGINAL CONVERSATION:
Doctor: Hello, I see from your chart that you have hypertension.
Patient: Yes, I take fifteen milligrams every morning.

CONVERSATION WITH TRANSLATION ERRORS:
Doctor: Hello, I see from your chart that you have hypotension.
Patient: Yes, I take fifty milligrams every morning.

ERRORS INTRODUCED:
1. Turn 0, Position 10
   Type: medical_substitution
   Original: 'hypertension.' → Modified: 'hypotension.'
2. Turn 1, Position 3
   Type: number_substitution
   Original: 'fifteen' → Modified: 'fifty'
```

## Use Cases

1. **Medical Interpreter Training**: Help interpreters practice identifying subtle translation errors
2. **Quality Assurance**: Test interpretation quality assurance systems
3. **Research**: Study the impact of translation errors on medical outcomes
4. **Education**: Teach medical students about the importance of accurate interpretation

## Contributing

Contributions are welcome! Feel free to:
- Add new error types
- Expand the medical terminology dictionaries
- Improve error detection algorithms
- Add more examples

## License

This project is open source and available for educational and research purposes.

## Disclaimer

This tool is for educational and research purposes only. Always use professional medical interpreters in real medical situations.
