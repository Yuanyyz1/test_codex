# Quick Start Guide

## Medical Translation Error Injector

### Installation
```bash
git clone https://github.com/Yuanyyz1/test_codex.git
cd test_codex
```

No dependencies required - uses Python standard library only!

### Quick Usage

#### 1. Basic Example (Single Text)
```python
from medical_translation_errors import MedicalTranslationErrorInjector

injector = MedicalTranslationErrorInjector(error_probability=0.15)
text = "The patient has hypertension and takes fifteen milligrams daily."
modified_text, errors = injector.inject_errors(text, seed=42)

print("Original:", text)
print("Modified:", modified_text)
```

#### 2. Conversation Example
```python
conversation = [
    {'speaker': 'Doctor', 'text': 'Do you have any allergies?'},
    {'speaker': 'Patient', 'text': 'Yes, I am allergic to penicillin.'}
]

modified_conv, errors = injector.inject_errors_in_conversation(conversation, seed=42)
```

#### 3. Run Demo Scripts
```bash
# Basic demo with one conversation
python medical_translation_errors.py

# Multiple example scenarios
python examples.py

# Comprehensive demo with all sample conversations
python comprehensive_demo.py
```

#### 4. Run Tests
```bash
python test_medical_translation_errors.py
```

### Error Types

The injector creates 4 types of realistic translation errors:

1. **Medical Term Substitutions** - Similar-sounding medical terms
   - `hypertension` ↔ `hypotension`
   - `infection` ↔ `inflammation`

2. **Number Confusions** - Common number mishearings
   - `fifteen` ↔ `fifty`
   - `13` ↔ `30`

3. **Qualifier Omissions** - Removed critical qualifiers
   - `not` → (omitted)
   - `no` → (omitted)

4. **Temporal Confusions** - Reversed time/direction
   - `before` ↔ `after`
   - `increase` ↔ `decrease`

### Customization

Add your own error patterns:
```python
injector = MedicalTranslationErrorInjector()
injector.medical_substitutions['asthma'] = ['anemia']
injector.number_substitutions['100'] = '1000'
```

### Sample Conversations Included

The repository includes 6 realistic medical conversations:
1. Initial Consultation - Hypertension
2. Pharmacy - Antibiotic Instructions
3. Emergency Room - Chest Pain
4. Follow-up Visit - Diabetes Management
5. Allergy Discussion
6. Pain Management - Post-Surgery

Access them with:
```python
from sample_conversations import SAMPLE_CONVERSATIONS
conversation = SAMPLE_CONVERSATIONS[0]['conversation']
```

### Parameters

**MedicalTranslationErrorInjector(error_probability=0.15)**
- `error_probability`: Probability of introducing an error (0.0 to 1.0)

**Methods:**
- `inject_errors(text, seed=None)` - Inject errors into text
- `inject_errors_in_conversation(conversation, seed=None)` - Inject errors into conversation

**Returns:**
- `(modified_text, list_of_errors)` with detailed error information

### Tips

1. **Use seeds for reproducibility**: Same seed = same errors
2. **Adjust error_probability**: Lower for subtle errors, higher for testing
3. **Check error types**: Flag critical errors (numbers, qualifiers)
4. **Extend dictionaries**: Add domain-specific medical terms

### Support

For issues or questions, please open an issue on GitHub.
