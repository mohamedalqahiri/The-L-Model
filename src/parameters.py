"""
The L-Exponential Model V1 - Calibrated Strategic Parameters
Directly derived from the formal verified equations table (2026).
"""
import math

# Baseline Parameters (t=0)
k = 0.65          # Accelerator growth rate of robotics and input flow
L_0 = 0.27        # Active human innovation factor (Baseline 0.27)
theta = 0.28      # Responsiveness Development Vector (Mid-point of 0.24 -> 0.32)

# Institutional and Sectoral Drag Coefficients
G = 0.25          # Government subsidies to primary sector / Total GDP
gamma = 0.20      # Direct impact weight of subsidies
c = 0.05          # Policy impact
lambda_val = 0.30 # Institutional drag coefficient (Initial baseline)
tau = 0.15        # Size variance weight
mu = 0.50         # Growth variance weight
rho = 0.35        # Relative high-tech sector volume (GDP_h-tech/Total GDP)

def calculate_flows(t=0):
    """Calculates f_t (input flow) and r_t (robotized processing) at time t"""
    f_t = 1 / (1 + 5.667 * math.exp(-k * t))
    r_t = 1 / (1 + 4 * math.exp(-k * t))
    return f_t, r_t

def calculate_drag_and_absorption(t=0):
    """
    Computes Total Absorptions = 1 + R + sigma
    Based strictly on Sectoral (Dsec) and Institutional (Einst) drag equations.
    """
    f_t, r_t = calculate_flows(t)
    
    # 1. Calculate R_t
    R_t = theta * (f_t / r_t)
    
    # 2. Calculate Sectoral Drag (Dsec_t)
    # d_cagr at t=0 is 0.07 * e^(0) = 0.07
    d_cagr_t = 0.07 * math.exp(-0.1 * t)
    Dsec_t = (1 - f_t) * (tau * abs(2 * rho - 1) + mu * d_cagr_t)
    
    # 3. Calculate Institutional Drag (E_inst_t)
    E_inst_t = math.exp(lambda_val * (1 - f_t) + c)
    
    # 4. Calculate Net Drag Coefficient (sigma_t)
    sigma_t = 0.2 * (1 + Dsec_t) * E_inst_t
    
    # Total Absorptions
    total_absorption = 1 + R_t + sigma_t
    return total_absorption, R_t, sigma_t
  
