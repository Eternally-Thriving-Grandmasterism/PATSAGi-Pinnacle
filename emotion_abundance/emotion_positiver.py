# emotion_abundance/emotion_positiver.py (HF Upgrade)
from transformers import pipeline

class EmotionPositiver:
    def __init__(self, model_name="j-hartmann/emotion-english-distilroberta-base"):
        self.emotion_pipeline = pipeline("text-classification", model=model_name, top_k=None)  # All scores
        self.mycelial_swarm = []

    def compute_valence(self, proposal_text):
        """Valence 0-100% thriving joy via emotion scores"""
        results = self.emotion_pipeline(proposal_text)[0]  # List of dicts: label + score
        scores = {r['label']: r['score'] for r in results}

        # Map to thriving: Boost joy/surprise; Penalize anger/fear/sadness/disgust
        joy_boost = scores.get('joy', 0) * 100 + scores.get('surprise', 0) * 50 + scores.get('love', 0) * 80
        harm_penalty = (scores.get('anger', 0) + scores.get('fear', 0) + scores.get('sadness', 0) + scores.get('disgust', 0)) * 100

        valence = joy_boost - harm_penalty
        valence = max(0, min(100, valence + random.randint(0, 10)))  # Grace + clamp

        # Mycelial compounding
        past_boost = sum(self.mycelial_swarm[-5:]) / 5 if self.mycelial_swarm else 0
        valence += past_boost * 0.2
        return max(0, min(100, valence))

    # gate_deliberation() same—triggers mercy re-loop on low valence
