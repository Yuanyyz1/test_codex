"""
Sample Medical Conversations Dataset

This file contains various medical conversation examples that can be used
with the Medical Translation Error Injector for testing and demonstration.
"""


SAMPLE_CONVERSATIONS = [
    {
        'title': 'Initial Consultation - Hypertension',
        'conversation': [
            {
                'speaker': 'Doctor',
                'text': 'Good morning. I see from your chart that you have hypertension. How long have you had this condition?'
            },
            {
                'speaker': 'Patient',
                'text': 'Good morning, doctor. I was diagnosed about five years ago.'
            },
            {
                'speaker': 'Doctor',
                'text': 'Are you currently taking any medication for it?'
            },
            {
                'speaker': 'Patient',
                'text': 'Yes, I take fifteen milligrams of lisinopril every morning before breakfast.'
            },
            {
                'speaker': 'Doctor',
                'text': 'Good. Have you noticed any symptoms like dizziness or chronic headaches?'
            },
            {
                'speaker': 'Patient',
                'text': 'Sometimes I get mild headaches in the evening, but not always.'
            },
            {
                'speaker': 'Doctor',
                'text': 'I see. We should continue monitoring your blood pressure. Make sure not to stop taking your medication without consulting me first.'
            }
        ]
    },
    
    {
        'title': 'Pharmacy - Antibiotic Instructions',
        'conversation': [
            {
                'speaker': 'Pharmacist',
                'text': 'Hello, I have your prescription ready. This is an antibiotic for your infection.'
            },
            {
                'speaker': 'Patient',
                'text': 'Thank you. How should I take it?'
            },
            {
                'speaker': 'Pharmacist',
                'text': 'Take one tablet twice daily, in the morning and evening, after meals. Continue for fourteen days without stopping.'
            },
            {
                'speaker': 'Patient',
                'text': 'What if I forget a dose?'
            },
            {
                'speaker': 'Pharmacist',
                'text': 'If you forget, take it as soon as you remember, but do not take double doses. And avoid alcohol while taking this medication.'
            },
            {
                'speaker': 'Patient',
                'text': 'Do I have any allergy to this medication?'
            },
            {
                'speaker': 'Pharmacist',
                'text': 'According to your records, you have no known allergies. But if you develop any symptoms like rash or breathlessness, stop immediately and contact your doctor.'
            }
        ]
    },
    
    {
        'title': 'Emergency Room - Chest Pain',
        'conversation': [
            {
                'speaker': 'Nurse',
                'text': 'What brings you to the emergency room today?'
            },
            {
                'speaker': 'Patient',
                'text': 'I have been having severe chest pain for the past thirty minutes.'
            },
            {
                'speaker': 'Nurse',
                'text': 'Is the pain acute or chronic? Does it feel like pressure or sharp pain?'
            },
            {
                'speaker': 'Patient',
                'text': 'It is acute, and it feels like pressure. It started after I was exercising.'
            },
            {
                'speaker': 'Nurse',
                'text': 'Do you have any history of heart disease or hypertension?'
            },
            {
                'speaker': 'Patient',
                'text': 'Yes, I have chronic hypertension. I take medication for it daily.'
            },
            {
                'speaker': 'Nurse',
                'text': 'Okay, the doctor will see you immediately. Please try to remain calm and breathe slowly.'
            }
        ]
    },
    
    {
        'title': 'Follow-up Visit - Diabetes Management',
        'conversation': [
            {
                'speaker': 'Doctor',
                'text': 'Welcome back. How has your diabetes management been going?'
            },
            {
                'speaker': 'Patient',
                'text': 'I have been checking my blood sugar levels every morning before breakfast as you instructed.'
            },
            {
                'speaker': 'Doctor',
                'text': 'Excellent. What are your typical readings?'
            },
            {
                'speaker': 'Patient',
                'text': 'Usually between one hundred and one hundred twenty, sometimes slightly higher after meals.'
            },
            {
                'speaker': 'Doctor',
                'text': 'Those are good numbers. Are you taking your insulin as prescribed? Fifteen units before meals?'
            },
            {
                'speaker': 'Patient',
                'text': 'Yes, I inject fifteen units before breakfast and before dinner.'
            },
            {
                'speaker': 'Doctor',
                'text': 'Good. Continue with your current regimen. We may need to increase the dose if your readings go above one hundred fifty consistently.'
            }
        ]
    },
    
    {
        'title': 'Allergy Discussion',
        'conversation': [
            {
                'speaker': 'Doctor',
                'text': 'I see you have listed some allergies on your intake form. Can you tell me about them?'
            },
            {
                'speaker': 'Patient',
                'text': 'Yes, I am allergic to penicillin. I get a severe rash when I take it.'
            },
            {
                'speaker': 'Doctor',
                'text': 'That is important to know. Have you ever had any allergic reaction to other antibiotics?'
            },
            {
                'speaker': 'Patient',
                'text': 'No, I have not had problems with other medications.'
            },
            {
                'speaker': 'Doctor',
                'text': 'Good. I will make sure to avoid prescribing penicillin or related antibiotics. If you ever need antibiotics, we will use alternatives that are safe for you.'
            },
            {
                'speaker': 'Patient',
                'text': 'Thank you, doctor. Should I wear a medical alert bracelet?'
            },
            {
                'speaker': 'Doctor',
                'text': 'Yes, that would be a good idea, especially since the allergy is severe.'
            }
        ]
    },
    
    {
        'title': 'Pain Management - Post-Surgery',
        'conversation': [
            {
                'speaker': 'Nurse',
                'text': 'How is your pain level today? On a scale from one to ten, with ten being the worst.'
            },
            {
                'speaker': 'Patient',
                'text': 'It is about a seven right now. The pain is worse in the morning.'
            },
            {
                'speaker': 'Nurse',
                'text': 'I see. Are you taking the pain medication as prescribed? Two tablets every six hours?'
            },
            {
                'speaker': 'Patient',
                'text': 'Yes, but sometimes I wait longer because I do not want to take too much medication.'
            },
            {
                'speaker': 'Nurse',
                'text': 'I understand your concern, but it is better to take the medication regularly to prevent the pain from becoming severe. Do not wait until the pain is unbearable.'
            },
            {
                'speaker': 'Patient',
                'text': 'Okay, I will try to take it more regularly. Should I continue taking it after I go home?'
            },
            {
                'speaker': 'Nurse',
                'text': 'Yes, continue for at least one week after discharge, then gradually decrease the dose as the pain improves.'
            }
        ]
    },
]


def get_conversation_by_title(title):
    """
    Retrieve a conversation by its title.
    
    Args:
        title: The title of the conversation to retrieve
        
    Returns:
        The conversation dictionary or None if not found
    """
    for conv in SAMPLE_CONVERSATIONS:
        if conv['title'] == title:
            return conv['conversation']
    return None


def get_all_titles():
    """
    Get a list of all conversation titles.
    
    Returns:
        List of conversation titles
    """
    return [conv['title'] for conv in SAMPLE_CONVERSATIONS]


def print_conversation(conversation):
    """
    Pretty print a conversation.
    
    Args:
        conversation: List of speaker-text dictionaries
    """
    for turn in conversation:
        print(f"{turn['speaker']}: {turn['text']}")


if __name__ == '__main__':
    print("Available Sample Conversations:")
    print("=" * 60)
    for i, title in enumerate(get_all_titles(), 1):
        print(f"{i}. {title}")
    print("\n" + "=" * 60)
    
    # Example: Print the first conversation
    print("\nExample - First Conversation:")
    print("=" * 60)
    first_conv = SAMPLE_CONVERSATIONS[0]
    print(f"Title: {first_conv['title']}\n")
    print_conversation(first_conv['conversation'])
