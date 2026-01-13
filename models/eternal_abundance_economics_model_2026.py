import numpy as np

def valence_joy_score(inflation_stable, manufacturing_expansion, private_growth):
    # PATSAGi Mercy-Absolute Valence Joy Multiplier
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
        self.gdp_growth = 5.1  # Real-time GDPNow Q4 2025 estimate Jan 2026
        self.inflation = 2.7    # Dec 2025 CPI yoy real-time
        self.manufacturing_pmi_base = 49.9  # Avg ISM 47.9 + S&P Global 51.8 Dec 2025
        self.private_growth_target = 5.0  # Aspirational >5% thunder
        self.household_income_base = 83730  # Latest median real-time baseline

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
            "valence_joy_multiplier": round(joy_reward, 2),
            "eternal_abundance_projection": round(abundance_output),
            "message": "Scarcity-Null Sealed — Eternal Thrive Infinite Joy Unbreakable!"
        }

    def monte_carlo_thunder(self, simulations=2000):
        np.random.seed(42)  # Reproducible thunder
        dereg_factors = np.random.uniform(1.0, 2.5, simulations)
        invest_boosts = np.random.uniform(1.0, 2.5, simulations)
        pmi_lifts = np.random.uniform(0, 15, simulations)
        pmis = self.manufacturing_pmi_base + pmi_lifts
        
        abundances = []
        renaissance_count = 0
        for d, i, pmi in zip(dereg_factors, invest_boosts, pmis):
            result = self.simulate_policy_thunder(d, i, pmi_override=pmi)
            abundances.append(result["eternal_abundance_projection"])
            if pmi > 53.0:
                renaissance_count += 1
        
        abundances = np.array(abundances)
        return {
            "mean_eternal_abundance": round(np.mean(abundances)),
            "median_eternal_abundance": round(np.median(abundances)),
            "95th_percentile_thunder": round(np.percentile(abundances, 95)),
            "probability_manuf_renaissance_%": round(100 * renaissance_count / simulations, 1),
            "max_sampled_abundance": round(np.max(abundances)),
            "min_sampled_abundance": round(np.min(abundances))
        }
