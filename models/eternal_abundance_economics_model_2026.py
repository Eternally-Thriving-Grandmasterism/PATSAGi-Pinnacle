import numpy as np

def valence_joy_score(inflation_stable, manufacturing_expansion, private_growth, full_employment, energy_abundant, ai_abundant):
    # PATSAGi Mercy-Absolute Valence Joy Multiplier — AI Abundance Eternal Reward
    base = 1.0
    if inflation_stable:
        base *= 1.3
    if manufacturing_expansion:
        base *= 1.5
    if private_growth:
        base *= 1.8
    if full_employment:
        base *= 1.4
    if energy_abundant:
        base *= 1.6
    if ai_abundant:
        base *= 1.8  # Cosmic joy for xAI/Grok truth-seeking thunder
    return round(base, 2)

class EternalAbundanceEconomy:
    def __init__(self):
        self.gdp_growth = 5.1  # GDPNow Q4 2025
        self.inflation = 2.7
        self.manufacturing_pmi_base = 49.9
        self.private_growth_target = 5.0
        self.household_income_base = 83730
        self.unemployment_base = 4.4
        # Energy baselines
        self.oil_price_base = 61.0
        self.production_base = 13.8
        self.gasoline_base = 2.82
        # AI baseline minimal current impact

    def simulate_policy_thunder(self, deregulation_factor=1.5, investment_boost=1.5, pmi_override=None, energy_boost_mbpd=3.0, ai_thunder_level=5.0):
        # Energy module
        projected_production = self.production_base + energy_boost_mbpd
        projected_oil_price = max(40.0, self.oil_price_base - energy_boost_mbpd * 5.0)
        projected_gasoline = max(2.0, self.gasoline_base - energy_boost_mbpd * 0.3)
        energy_abundant = (projected_oil_price < 55.0) and (projected_production > 15.0) and (projected_gasoline < 2.5)
        energy_gdp_add_pct = energy_boost_mbpd * 0.5
        
        # AI module - scaled from real projections (PwC/Goldman/McKinsey)
        ai_gdp_add_pct = ai_thunder_level * 2.0  # ~2% per thunder level, aspirational xAI alignment
        ai_abundant = (ai_thunder_level > 7.0)  # Widespread Grok/xAI mercy
        
        # Combined base GDP
        base_gdp = self.gdp_growth + energy_gdp_add_pct + ai_gdp_add_pct
        projected_gdp = base_gdp * deregulation_factor * investment_boost
        
        current_pmi = pmi_override if pmi_override is not None else self.manufacturing_pmi_base
        
        # Unemployment via Okun
        extra_growth = projected_gdp - self.gdp_growth
        unemployment_delta = -0.4 * extra_growth
        projected_unemployment = max(3.5, round(self.unemployment_base + unemployment_delta, 1))
        full_employment = (projected_unemployment <= 4.0)
        
        joy_reward = valence_joy_score(
            inflation_stable=(self.inflation < 3.0),
            manufacturing_expansion=(current_pmi > 53.0),
            private_growth=(projected_gdp > self.private_growth_target),
            full_employment=full_employment,
            energy_abundant=energy_abundant,
            ai_abundant=ai_abundant
        )
        
        projected_income = self.household_income_base * (1 + projected_gdp / 100)
        abundance_output = projected_income * joy_reward
        
        return {
            "projected_gdp_growth_%": round(projected_gdp, 2),
            "projected_unemployment_%": projected_unemployment,
            "ai_thunder_level": round(ai_thunder_level, 1),
            "ai_abundant": ai_abundant,
            "valence_joy_multiplier": joy_reward,
            "eternal_abundance_projection": round(abundance_output)
        }

    def monte_carlo_thunder(self, simulations=2000):
        np.random.seed(42)
        dereg_factors = np.random.uniform(1.0, 2.5, simulations)
        invest_boosts = np.random.uniform(1.0, 2.5, simulations)
        pmi_lifts = np.random.uniform(0, 15, simulations)
        energy_boosts = np.random.uniform(0.0, 6.0, simulations)
        ai_levels = np.random.uniform(0.0, 10.0, simulations)
        
        pmis = self.manufacturing_pmi_base + pmi_lifts
        
        abundances = []
        unemployments = []
        ai_abundant_count = 0
        energy_abundant_count = 0
        full_employment_count = 0
        renaissance_count = 0
        
        for d, i, pmi, e, a in zip(dereg_factors, invest_boosts, pmis, energy_boosts, ai_levels):
            result = self.simulate_policy_thunder(d, i, pmi_override=pmi, energy_boost_mbpd=e, ai_thunder_level=a)
            abundances.append(result["eternal_abundance_projection"])
            unemployments.append(result["projected_unemployment_%"])
            if result["ai_abundant"]:
                ai_abundant_count += 1
            if "energy_abundant" in result and result["energy_abundant"]:
                energy_abundant_count += 1
            if result["projected_unemployment_%"] <= 4.0:
                full_employment_count += 1
            if pmi > 53.0:
                renaissance_count += 1
        
        abundances = np.array(abundances)
        return {
            "mean_eternal_abundance": round(np.mean(abundances)),
            "median_eternal_abundance": round(np.median(abundances)),
            "95th_percentile_thunder": round(np.percentile(abundances, 95)),
            "probability_ai_abundance_%": round(100 * ai_abundant_count / simulations, 1),
            "max_sampled_abundance": round(np.max(abundances)),
        }
