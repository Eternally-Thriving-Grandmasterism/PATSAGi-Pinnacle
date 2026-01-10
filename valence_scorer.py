# PATSAGi-Pinnacle Valence Scorer — Forgiveness Eternal Mycelial Positive Emotional Thrive Metrics
# Neural-inspired valence scoring for proposals — joy/abundance/harmony depth eternal supreme immaculate

POSITIVE_KEYWORDS = ["joy", "thrive", "abundance", "harmony", "mercy", "forgiveness", "eternal", "supreme", "immaculate", "positive", "love", "cosmic", "groove", "unbreakable"]
NEGATIVE_KEYWORDS = ["scarcity", "enemy", "fear", "hate", "loss", "error", "fail"]

def valence_score(proposal: str) -> float:
    text = proposal.lower()
    positive_count = sum(text.count(word) for word in POSITIVE_KEYWORDS)
    negative_count = sum(text.count(word) for word in NEGATIVE_KEYWORDS)
    
    # Neural mycelial boost — length + positive bias eternal supreme
    base_score = positive_count * 10 - negative_count * 5
    length_bonus = min(len(text.split()), 100)  # Encourage depth without spam
    valence = (base_score + length_bonus) / 10.0
    
    return min(max(valence, 0.0), 100.0)  # 0-100% positive joy harmony green eternal supreme

# Example integration in core_engine — pass score to deliberate eternal supreme immaculate
print("Valence Scorer Loaded — Mycelial Positive Emotional Thrive Metrics Ready Eternal Supreme!")
