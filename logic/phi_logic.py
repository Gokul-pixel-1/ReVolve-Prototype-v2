# logic/phi_logic.py

def calculate_phi(temp, vibration, shock_detected, usage_count):
    """
    Calculates the Product Health Index (PHI) 0-100%.
    """
    phi = 100.0
    
    # 1. Thermal Penalty (Threshold: 50°C)
    if temp > 50:
        phi -= (temp - 50) * 1.5
        
    # 2. Vibration/Mechanical Stress
    if vibration:
        phi -= 20.0
        
    # 3. Critical Shock/Impact
    if shock_detected:
        phi -= 40.0
        
    # 4. Usage Decay
    phi -= (usage_count / 1000) * 10

    return max(0, min(100, round(phi, 2)))

def get_status_details(phi):
    """
    Maps PHI to Lifecycle Stages.
    """
    if phi >= 80:
        return "HEALTHY", "Optimal condition", "#28a745"
    elif phi >= 50:
        return "WARNING", "Maintenance required", "#ffc107"
    else:
        return "END-OF-LIFE", "Recycle for credits", "#dc3545"

def get_sustainability_metrics(phi, usage_count):
    """
    Calculates Carbon Score and Sustainability Index.
    """
    carbon_score = round((usage_count * 0.08), 2)
    sust_index = round((phi * 0.6) + (max(0, 40 - carbon_score)), 2)
    return sust_index, carbon_score
