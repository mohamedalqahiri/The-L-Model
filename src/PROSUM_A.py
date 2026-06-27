"""
Core System Engine applying the exact Sync_t logic from the verified table.
"""
import math
from parameters import calculate_flows, calculate_drag_and_absorption, L_0

def calculate_sync_t(t=0):
    """Sync_t = f_t * {1 + ln(1 + r_t / f_t)}"""
    f_t, r_t = calculate_flows(t)
    sync_t = f_t * (1 + math.log(1 + (r_t / f_t)))
    return sync_t

def calculate_prosum_a(t=0, AC_modifier=1.0):
    """
    PROSUM.A_t = L_t ^ {1 + (sync_t * AC_modifier / total_absorption)}
    AC_modifier represents the Algorithmic Complexity scaling layer from Github.
    """
    f_t, r_t = calculate_flows(t)
    sync_t = calculate_sync_t(t)
    total_absorption, R_t, sigma_t = calculate_drag_and_absorption(t)
    
    # Calculate L_t growth dynamic augmented by synergy with AI
    n = 0.015 * ((r_t / f_t) + 1)
    L_t = L_0 * math.pow((1 + n), t)
    
    # Injecting Algorithmic Complexity safely into the core Sync ratio
    # High AC scales the synergy potential against the drag denominator
    sync_ratio = (sync_t * AC_modifier) / total_absorption
    exponent = 1 + sync_ratio
    
    system_output = math.pow(L_t * 100, exponent) # Base scaled to 100 for visibility
    return system_output, sync_t, total_absorption
  
