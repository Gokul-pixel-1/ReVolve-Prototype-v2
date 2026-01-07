def calculate_phi(temperature, vibration, usage_cycles):
    """
    Calculate Product Health Index (PHI)

    Returns:
    - phi (0–100)
    - penalties (list)
    - lifecycle_stage
    - remaining_life
    """

    phi = 100
    penalties = []

    # Temperature impact
    if temperature > 60:
        phi -= 30
        penalties.append("High temperature (>60°C)")
    elif temperature > 40:
        phi -= 15
        penalties.append("Moderate temperature (>40°C)")

    # Vibration impact
    if vibration == 1:
        phi -= 20
        penalties.append("Vibration detected")

    # Usage cycle impact
    if usage_cycles > 80:
        phi -= 40
        penalties.append("Very high usage cycles (>80)")
    elif usage_cycles > 40:
        phi -= 20
        penalties.append("Moderate usage cycles (>40)")

    # Clamp PHI
    phi = max(0, min(100, phi))

    # Lifecycle stage
    if usage_cycles <= 20:
        stage = "New"
    elif usage_cycles <= 50:
        stage = "Active"
    elif usage_cycles <= 80:
        stage = "Aging"
    else:
        stage = "Retired"

    # Remaining useful life
    max_cycles = 100
    remaining_life = max(0, max_cycles - usage_cycles)

    return phi, penalties, stage, remaining_life
