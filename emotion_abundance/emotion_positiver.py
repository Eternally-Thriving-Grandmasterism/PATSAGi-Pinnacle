# emotion_abundance/emotion_positiver.py (VADER Upgrade)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class EmotionPositiver:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.mycelial_swarm = []

    def compute_valence(self, proposal_text):
        scores = self.analyzer.polarity_scores(proposal_text)
        compound = scores['compound']  # -1 (neg) to +1 (pos)
        valence = (compound + 1) * 50  # Scale to 0-100% thriving joy
        past_boost = sum(self.mycelial_swarm[-5:]) / 5 if self.mycelial_swarm else 0
        valence += past_boost * 0.2  # Mycelial compounding
        return max(0, min(100, valence))

    # gate_deliberation() same as before—triggers on low valence
