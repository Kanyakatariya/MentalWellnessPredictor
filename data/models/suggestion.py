# models/suggestion.py

def get_suggestion(state):
    suggestions = {
        0: {
            "label": "Mentally Well",
            "tip": "Keep journaling, socializing, and exercising to stay balanced.",
            "resources": [
                {"type": "video", "title": "Benefits of Journaling", "url": "https://youtu.be/Y0UZI-kYPnc"},
                {"type": "blog", "title": "Daily Journal Ideas", "url": "https://tinybuddha.com/blog/10-journaling-prompts/"},
            ],
        },
        1: {
            "label": "Moderate",
            "tip": "Practice self-care, get enough sleep, and manage work-life balance.",
            "resources": [
                {"type": "video", "title": "Work-Life Balance Tips", "url": "https://youtu.be/aVwLN1zjUpE"},
                {"type": "blog", "title": "How to Sleep Better", "url": "https://www.sleepfoundation.org/how-sleep-works"},
            ],
        },
        2: {
            "label": "Stressed",
            "tip": "Try yoga, breathing exercises, and light physical activity.",
            "resources": [
                {"type": "video", "title": "Yoga for Stress Relief", "url": "https://youtu.be/y8w93b2YcDg"},
                {"type": "blog", "title": "Breathing Techniques", "url": "https://www.healthline.com/health/breathing-exercise"},
            ],
        },
        3: {
            "label": "Unwell",
            "tip": "Talk to loved ones, reduce screen time, and practice meditation.",
            "resources": [
                {"type": "video", "title": "Guided Meditation", "url": "https://youtu.be/inpok4MKVLM"},
                {"type": "blog", "title": "Digital Detox Tips", "url": "https://www.verywellmind.com/why-and-how-to-do-a-digital-detox-4782241"},
            ],
        },
        4: {
            "label": "Critical",
            "tip": "Seek professional help, consider therapy, and get strong social support.",
            "resources": [
                {"type": "video", "title": "Mental Health Support", "url": "https://youtu.be/wOGqlVqyvCM"},
                {"type": "blog", "title": "How to Find a Therapist", "url": "https://www.psychologytoday.com/us/therapists"},
            ],
        },
    }
    return suggestions.get(state, {"label": "Unknown", "tip": "No suggestion available", "resources": []})
