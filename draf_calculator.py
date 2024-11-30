# Dynamic Reward Allocation Formula (DRAF)

def calculate_reward(T_reward, token_holding, total_weighted_tokens, beta_min, beta_max, alpha_min, alpha_max, holding_time, max_holding_time, max_share):
    """
    Calculate individual reward R_i based on the DRAF formula.
    
    Parameters:
    T_reward (float): Total Reward Pool available for distribution.
    token_holding (float): Tokens held by the participant.
    total_weighted_tokens (float): Sum of all weighted tokens in the system.
    beta_min (float): Minimum progressive bonus.
    beta_max (float): Maximum progressive bonus.
    alpha_min (float): Minimum regressive penalty.
    alpha_max (float): Maximum regressive penalty.
    holding_time (float): Time tokens have been held by the participant.
    max_holding_time (float): Maximum time multiplier threshold.
    max_share (float): Maximum share of tokens a participant can hold.

    Returns:
    float: The reward allocated to the participant.
    """
    # Calculate participant's proportional share
    proportional_share = token_holding / max_share

    # Calculate progressive bonus (beta)
    beta = beta_min + (beta_max - beta_min) * (1 - proportional_share)

    # Calculate regressive penalty (alpha)
    alpha = alpha_min + (alpha_max - alpha_min) * proportional_share

    # Calculate holding time multiplier
    holding_multiplier = min(holding_time / max_holding_time, 1)

    # Weighted token calculation
    weighted_tokens = token_holding * (1 + beta - alpha) * (1 + holding_multiplier)

    # Reward calculation
    reward = T_reward * (weighted_tokens / total_weighted_tokens)

    return reward


# Example usage
if __name__ == "__main__":
    # Example parameters
    T_reward = 10000  # Total reward pool
    token_holding = 1000  # Participant's token holdings
    total_weighted_tokens = 50000  # Total weighted tokens in the system
    beta_min = 0.05
    beta_max = 0.15
    alpha_min = 0.02
    alpha_max = 0.10
    holding_time = 6  # Held for 6 months
    max_holding_time = 12  # Maximum holding time is 12 months
    max_share = 0.2  # Maximum share allowed (e.g., 20% of total tokens)

    # Calculate reward
    reward = calculate_reward(
        T_reward,
        token_holding,
        total_weighted_tokens,
        beta_min,
        beta_max,
        alpha_min,
        alpha_max,
        holding_time,
        max_holding_time,
        max_share
    )

    print(f"Reward for the participant: {reward:.2f}")
