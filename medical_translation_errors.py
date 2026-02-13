"""
Medical Translation Error Insertion Module

This module provides functionality to insert natural and subtle translation errors
into medical conversations. The errors mimic common translation mistakes that occur
in real medical interpreting scenarios.
"""

import random
import re
from typing import List, Dict, Tuple, Optional


class MedicalTranslationErrorInjector:
    """
    Injects natural and subtle translation errors into medical conversations.
    
    Supports various error types:
    - Word substitution (similar sounding medical terms)
    - False friends (words that sound similar but mean different things)
    - Number confusion (dosage errors)
    - Omission of critical qualifiers
    - Tense/temporal confusion
    """
    
    def __init__(self, error_probability: float = 0.15):
        """
        Initialize the error injector.
        
        Args:
            error_probability: Probability of introducing an error (0.0 to 1.0)
        """
        self.error_probability = error_probability
        
        # Medical term substitutions (subtle errors)
        self.medical_substitutions = {
            'hypertension': ['hypotension', 'hyperextension'],
            'hypotension': ['hypertension'],
            'infection': ['inflammation', 'infusion'],
            'inflammation': ['infection'],
            'prescription': ['proscription', 'description'],
            'dose': ['does', 'dosage'],
            'tablet': ['capsule'],
            'capsule': ['tablet'],
            'chronic': ['acute'],
            'acute': ['chronic'],
            'malignant': ['benign'],
            'benign': ['malignant'],
            'symptom': ['syndrome'],
            'diagnosis': ['prognosis'],
            'prognosis': ['diagnosis'],
            'allergy': ['allergic'],
            'breathe': ['breath'],
            'breath': ['breathe'],
            'ingest': ['inject'],
            'inject': ['ingest'],
            'oral': ['aural'],
            'bacteria': ['virus'],
            'virus': ['bacteria'],
        }
        
        # Number substitutions (common mishearings)
        self.number_substitutions = {
            'fifteen': 'fifty',
            'fifty': 'fifteen',
            'thirteen': 'thirty',
            'thirty': 'thirteen',
            'fourteen': 'forty',
            'forty': 'fourteen',
            '15': '50',
            '50': '15',
            '13': '30',
            '30': '13',
            '14': '40',
            '40': '14',
        }
        
        # Common medical qualifiers that might be omitted
        self.omittable_qualifiers = [
            'not', 'no', 'without', 'never', 'rarely', 'sometimes', 
            'often', 'always', 'very', 'slightly', 'mildly', 'severely'
        ]
        
        # Temporal/tense markers that might be confused
        self.temporal_confusions = {
            'before': 'after',
            'after': 'before',
            'morning': 'evening',
            'evening': 'morning',
            'daily': 'weekly',
            'weekly': 'daily',
            'increase': 'decrease',
            'decrease': 'increase',
            'start': 'stop',
            'stop': 'start',
            'continue': 'discontinue',
            'discontinue': 'continue',
        }
    
    def inject_errors(self, text: str, seed: Optional[int] = None) -> Tuple[str, List[Dict]]:
        """
        Inject translation errors into the given text.
        
        Args:
            text: The original medical conversation text
            seed: Random seed for reproducibility (optional)
            
        Returns:
            Tuple of (modified_text, list_of_errors_introduced)
        """
        if seed is not None:
            random.seed(seed)
        
        errors_introduced = []
        words = text.split()
        modified_words = words.copy()
        
        for i, word in enumerate(words):
            if random.random() < self.error_probability:
                error = self._apply_random_error(word, i)
                if error:
                    modified_words[i] = error['new_word']
                    errors_introduced.append({
                        'position': i,
                        'original': error['original'],
                        'modified': error['new_word'],
                        'error_type': error['error_type']
                    })
        
        return ' '.join(modified_words), errors_introduced
    
    def _apply_random_error(self, word: str, position: int) -> Optional[Dict]:
        """
        Apply a random error type to a word.
        
        Args:
            word: The word to potentially modify
            position: Position of the word in the sentence
            
        Returns:
            Dictionary with error details or None if no error applied
        """
        # Clean the word (remove punctuation for matching)
        clean_word = re.sub(r'[^\w\s]', '', word).lower()
        
        # Try different error types
        error_types = [
            self._try_medical_substitution,
            self._try_number_substitution,
            self._try_qualifier_omission,
            self._try_temporal_confusion,
        ]
        
        random.shuffle(error_types)
        
        for error_func in error_types:
            error = error_func(word, clean_word)
            if error:
                return error
        
        return None
    
    def _try_medical_substitution(self, original_word: str, clean_word: str) -> Optional[Dict]:
        """Try to substitute a medical term."""
        if clean_word in self.medical_substitutions:
            substitutes = self.medical_substitutions[clean_word]
            new_word = random.choice(substitutes)
            
            # Preserve capitalization
            if original_word[0].isupper():
                new_word = new_word.capitalize()
            
            # Preserve punctuation
            punctuation = ''.join(c for c in original_word if not c.isalnum())
            if punctuation:
                new_word = new_word + punctuation
            
            return {
                'original': original_word,
                'new_word': new_word,
                'error_type': 'medical_substitution'
            }
        return None
    
    def _try_number_substitution(self, original_word: str, clean_word: str) -> Optional[Dict]:
        """Try to substitute a number."""
        if clean_word in self.number_substitutions:
            new_word = self.number_substitutions[clean_word]
            
            # Preserve punctuation
            punctuation = ''.join(c for c in original_word if not c.isalnum())
            if punctuation:
                new_word = new_word + punctuation
            
            return {
                'original': original_word,
                'new_word': new_word,
                'error_type': 'number_substitution'
            }
        return None
    
    def _try_qualifier_omission(self, original_word: str, clean_word: str) -> Optional[Dict]:
        """Try to omit a critical qualifier."""
        if clean_word in self.omittable_qualifiers:
            # 30% chance to actually omit if selected
            if random.random() < 0.3:
                return {
                    'original': original_word,
                    'new_word': '',  # Omit the word
                    'error_type': 'qualifier_omission'
                }
        return None
    
    def _try_temporal_confusion(self, original_word: str, clean_word: str) -> Optional[Dict]:
        """Try to confuse temporal/directional terms."""
        if clean_word in self.temporal_confusions:
            new_word = self.temporal_confusions[clean_word]
            
            # Preserve capitalization
            if original_word[0].isupper():
                new_word = new_word.capitalize()
            
            # Preserve punctuation
            punctuation = ''.join(c for c in original_word if not c.isalnum())
            if punctuation:
                new_word = new_word + punctuation
            
            return {
                'original': original_word,
                'new_word': new_word,
                'error_type': 'temporal_confusion'
            }
        return None
    
    def inject_errors_in_conversation(
        self, 
        conversation: List[Dict[str, str]], 
        seed: Optional[int] = None
    ) -> Tuple[List[Dict[str, str]], List[Dict]]:
        """
        Inject errors into a conversation (list of speaker-text pairs).
        
        Args:
            conversation: List of dicts with 'speaker' and 'text' keys
            seed: Random seed for reproducibility (optional)
            
        Returns:
            Tuple of (modified_conversation, all_errors_introduced)
        """
        if seed is not None:
            random.seed(seed)
        
        modified_conversation = []
        all_errors = []
        
        for turn_idx, turn in enumerate(conversation):
            modified_text, errors = self.inject_errors(turn['text'], seed=None)
            modified_conversation.append({
                'speaker': turn['speaker'],
                'text': modified_text
            })
            
            # Add turn index to errors
            for error in errors:
                error['turn_index'] = turn_idx
                all_errors.append(error)
        
        return modified_conversation, all_errors


def main():
    """Example usage of the medical translation error injector."""
    
    # Create an injector with 20% error probability
    injector = MedicalTranslationErrorInjector(error_probability=0.20)
    
    # Example medical conversation
    conversation = [
        {
            'speaker': 'Doctor',
            'text': 'Hello, I see from your chart that you have hypertension. Are you taking your medication daily?'
        },
        {
            'speaker': 'Patient',
            'text': 'Yes, I take fifteen milligrams every morning before breakfast.'
        },
        {
            'speaker': 'Doctor',
            'text': 'Good. Have you noticed any symptoms like infection or inflammation?'
        },
        {
            'speaker': 'Patient',
            'text': 'No, I have not had any symptoms. My chronic pain is better now.'
        },
        {
            'speaker': 'Doctor',
            'text': 'Excellent. Continue taking your medication and we will increase the dose if needed.'
        }
    ]
    
    print("=" * 80)
    print("ORIGINAL CONVERSATION:")
    print("=" * 80)
    for turn in conversation:
        print(f"{turn['speaker']}: {turn['text']}")
    
    print("\n" + "=" * 80)
    print("CONVERSATION WITH TRANSLATION ERRORS:")
    print("=" * 80)
    
    # Inject errors with a seed for reproducibility
    modified_conversation, errors = injector.inject_errors_in_conversation(
        conversation, seed=42
    )
    
    for turn in modified_conversation:
        print(f"{turn['speaker']}: {turn['text']}")
    
    print("\n" + "=" * 80)
    print("ERRORS INTRODUCED:")
    print("=" * 80)
    
    if errors:
        for i, error in enumerate(errors, 1):
            print(f"{i}. Turn {error['turn_index']}, Position {error['position']}")
            print(f"   Type: {error['error_type']}")
            print(f"   Original: '{error['original']}' → Modified: '{error['modified']}'")
    else:
        print("No errors were introduced in this run.")
    
    print("\n" + "=" * 80)


if __name__ == '__main__':
    main()
