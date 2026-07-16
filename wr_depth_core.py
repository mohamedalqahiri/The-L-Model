import math

def calculate_potential_value(ac, engagements, max_engagement):
    """
    Calculates the Potential Value (Lp) based on Algorithmic Complexity (AC) 
    and social engagement using a geometric mean to prevent viral bias.
    """
    if not engagements:
        return ac
        
    # Geometric mean of social engagements (likes, shares, ratings, etc.)
    product = 1.0
    for r in engagements:
        product *= max(r, 1) # Prevent zero multiplication
    geomean = product ** (1.0 / len(engagements))
    
    # Lp = Max(AC, AC * (1 + Geomean (R_i)/ R_max))
    lp_scaled = ac * (1.0 + (geomean (R_i)/ max_engagement))
    return max(ac, lp_scaled)

def calculate_rawlsian_weight(ac, ac_bar, lp):
    """
    Calculates the Rawlsian Weight (Wr) using a logistic expansion function
    to dynamically scale and protect high-complexity, low-reach content.
    """
    complexity_delta = ac - ac_bar
    # Wr = Lp / (1 + e^-(AC - AC_bar))
    try:
        denominator = 1.0 + math.exp(-complexity_delta)
        wr = lp / denominator
    except OverflowError:
        # Safeguard for extreme values
        wr = 0.0 if complexity_delta < 0 else lp
        
    return wr

# --- Quick Test / Demonstration ---
if __name__ == "__main__":
    # Benchmark average complexity on the platform
    platform_ac_bar = 0.4 
    
    print("--- SCENARIO A: Deep Content (High Complexity, Low Engagement) ---")
    ac_a = 0.85          # Highly academic/insightful post
    likes_a = [12, 15]   # Very few likes
    lp_a = calculate_potential_value(ac_a, likes_a, max_engagement=10000)
    wr_a = calculate_rawlsian_weight(ac_a, platform_ac_bar, lp_a)
    print(f"Complexity (AC): {ac_a} | Potential Value (Lp): {lp_a:.4f} | Rawlsian Weight (Wr): {wr_a:.4f}\n")

    print("--- SCENARIO B: Viral Content (Low Complexity, High Engagement) ---")
    ac_b = 0.15          # Low-effort meme/clickbait
    likes_b = [8500, 9000] # Massive viral reach
    lp_b = calculate_potential_value(ac_b, likes_b, max_engagement=10000)
    wr_b = calculate_rawlsian_weight(ac_b, platform_ac_bar, lp_b)
    print(f"Complexity (AC): {ac_b} | Potential Value (Lp): {lp_b:.4f} | Rawlsian Weight (Wr): {wr_b:.4f}\n")
  
