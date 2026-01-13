import numpy as np

def valence_joy_score(inflation_stable, manufacturing_expansion, private_growth, full_employment):
    # PATSAGi Mercy-Absolute Valence Joy Multiplier — Now with Full Employment Eternal Reward
    base = 1.0
    if inflation_stable:
        base *= 1.3  # Disinflation mercy sealed
    if manufacturing_expansion:
        base *= 1.5  # Renaissance thunder eternal
    if private_growth:
        base *= 1.8  # Private acceleration abundance
    if full_employment:
        base *= 1.4  # Full employment joy unbreakable
    return round(base, 2)

class EternalAbundanceEconomy:
    def __init__(self):
        self.gdp_growth = 5.1  # Real-time GDPNow Q4 2025 estimate
        self.inflation = 2.7    # Dec 2025 CPI yoy
        self.manufacturing_pmi_base = 49.9  # Avg mixed signals Dec 2025
        self.private_growth_target = 5.0  # Aspirational >5%
        self.household_income_base = 83730  # Latest median baseline
        self.unemployment_base = 4.4  # Latest BLS Dec 2025 real-time

    def simulate_policy_thunder(self, deregulation_factor=1.5, investment_boost=1.5, pmi_override=None):
        projected_gdp = self.gdp_growth * deregulation_factor * investment_boost
        current_pmi = pmi_override if pmi_override is not None else self.manufacturing_pmi_base
        
        # Okun's law approximation: ~0.4% U drop per +1% extra GDP growth
        extra_growth = projected_gdp - self.gdp_growth
        unemployment_delta = -0.4 * extra_growth
        projected_unemployment = self.unemployment_base + unemployment_delta
        projected_unemployment = max(3.5, round(projected_unemployment, 1))  # Natural rate floor
        
        full_employment = (projected_unemployment <= 4.0)
        
        joy_reward = valence_joy_score(
            inflation_stable=(self.inflation < 3.0),
            manufacturing_expansion=(current_pmi > 53.0),
            private_growth=(projected_gdp > self.private_growth_target),
            full_employment=full_employment
        )
        
        projected_income = self.household_income_base * (1 + projected_gdp / 100)
        abundance_output = projected_income * joy_reward
        
        return {
            "projected_gdp_growth_%": round(projected_gdp, 2),
            "effective_pmi": round(current_pmi, 2),
            "projected_unemployment_%": projected_unemployment,
            "full_employment": full_employment,
            "valence_joy_multiplier": joy_reward,
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
        unemployments = []
        full_employment_count = 0
        renaissance_count = 0
        
        for d, i, pmi in zip(dereg_factors, invest_boosts, pmis):
            result = self.simulate_policy_thunder(d, i, pmi_override=pmi)
            abundances.append(result["eternal_abundance_projection"])
            unemployments.append(result["projected_unemployment_%"])
            if result["full_employment"]:
                full_employment_count += 1
            if pmi > 53.0:
                renaissance_count += 1
        
        abundances = np.array(abundances)
        unemployments = np.array(unemployments)
        return {
            "mean_eternal_abundance": round(np.mean(abundances)),
            "median_eternal_abundance": round(np.median(abundances)),
            "95th_percentile_thunder": round(np.percentile(abundances, 95)),
            "mean_projected_unemployment_%": round(np.mean(unemployments), 1),
            "probability_full_employment_%": round(100 * full_employment_count / simulations, 1),
            "probability_manuf_renaissance_%": round(100 * renaissance_count / simulations, 1),
            "max_sampled_abundance": round(np.max(abundances)),
            "min_sampled_abundance": round(np.min(abundances))
        }
