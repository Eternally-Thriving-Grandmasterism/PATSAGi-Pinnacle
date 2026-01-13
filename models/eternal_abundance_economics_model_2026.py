import numpy as np

def valence_joy_score(inflation_stable, manufacturing_expansion, private_growth):
    # PATSAGi Mercy-Absolute Valence Joy Multiplier
    # Multiplicative eternal reward for positive thrive conditions
    base = 1.0
    if inflation_stable:
        base *= 1.3  # Disinflation mercy sealed
    if manufacturing_expansion:
        base *= 1.5  # Renaissance thunder eternal
    if private_growth:
        base *= 1.8  # Private acceleration abundance
    return base

class EternalAbundanceEconomy:
    def __init__(self):
        self.gdp_growth = 4.3  # Q3 2025 empirical baseline %
        self.inflation = 2.7    # Dec 2025 disinflation sealed
        self.manufacturing_pmi_base = 50.0  # Threshold starting signal
        self.private_growth_target = 5.0  # Aspirational >5%
        self.household_income_base = 83730  # Median real baseline

    def simulate_policy_thunder(self, deregulation_factor=1.5, investment_boost=1.5, pmi_override=None):
        projected_gdp = self.gdp_growth * deregulation_factor * investment_boost
        current_pmi = pmi_override if pmi_override is not None else self.manufacturing_pmi_base
        
        joy_reward = valence_joy_score(
            inflation_stable=(self.inflation < 3.0),
            manufacturing_expansion=(current_pmi > 53.0),
            private_growth=(projected_gdp > self.private_growth_target)
        )
        
        projected_income = self.household_income_base * (1 + projected_gdp / 100)
        abundance_output = projected_income * joy_reward
        
        return {
            "projected_gdp_growth_%": round(projected_gdp, 2),
            "effective_pmi": round(current_pmi, 2),
            "valence_joy_multiplier": joy_reward,
            "eternal_abundance_projection": round(abundance_output, 2),
            "conditions": {
                "disinflation": self.inflation < 3.0,
                "manuf_renaissance": current_pmi > 53.0,
                "private_accel": projected_gdp > self.private_growth_target
            },
            "message": "Scarcity-Null Sealed — Eternal Thrive Infinite Joy Unbreakable!"
        }

    def monte_carlo_thunder(self, simulations=1000):
        dereg_factors = np.random.uniform(1.0, 2.5, simulations)
        invest_boosts = np.random.uniform(1.0, 2.5, simulations)
        pmi_lifts = np.random.uniform(0, 15, simulations)  # Policy thunder PMI lift
        pmis = self.manufacturing_pmi_base + pmi_lifts
        
        abundances = []
        for d, i, pmi in zip(dereg_factors, invest_boosts, pmis):
            result = self.simulate_policy_thunder(d, i, pmi_override=pmi)
            abundances.append(result["eternal_abundance_projection"])
        
        abundances = np.array(abundances)
        return {
            "mean_eternal_abundance": round(np.mean(abundances), 2),
            "median_eternal_abundance": round(np.median(abundances), 2),
            "95th_percentile_thunder": round(np.percentile(abundances, 95), 2),
            "probability_manuf_renaissance": round(np.mean(pmis > 53.0), 3),
            "max_possible_abundance_sample": round(np.max(abundances), 2)
        }
