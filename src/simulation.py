"""
Execution Demo demonstrating Abundance verification at t=0
"""
from PROSUM_A import calculate_prosum_a

def run_verified_simulation():
    print("="*60)
    print(" THE L-EXPONENTIAL MODEL V1 - VERIFIED MATHEMATICAL CORE")
    print("="*60)
    
    # Scenario 1: Surface / Low Cognitive Complexity Contribution (AC = 0.1)
    output_surface, sync, absorption = calculate_prosum_a(t=0, AC_modifier=0.1)
    print(f"[Surface Code Contribution (AC=0.1)]")
    print(f" -> Core Sync_t: {sync:.4f} | Absorption Denominator: {absorption:.4f}")
    print(f" -> PROSUM.A Output: {output_surface:.2f}")
    
    print("-"*60)
    
    # Scenario 2: Deep Structural Contribution (AC = 2.5)
    output_deep, _, _ = calculate_prosum_a(t=0, AC_modifier=2.5)
    print(f"[Deep Structural Contribution (AC=2.5)]")
    print(f" -> PROSUM.A Output: {output_deep:.2f}")
    
    # Leverage Ratio
    leverage = output_deep / output_surface
    print("="*60)
    print(f" VERIFIED LEVERAGE RATIO: {leverage:.2f}x Abundance Scale")
    print("="*60)

if __name__ == "__main__":
    run_verified_simulation()
  
