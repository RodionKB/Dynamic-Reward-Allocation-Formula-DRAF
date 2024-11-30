**Dynamic Reward Allocation Formula (DRAF)**
By RodionKB

The Dynamic Reward Allocation Formula (DRAF) is a cutting-edge reward distribution mechanism tailored for decentralized ecosystems. 
It combines fairness, scalability, and sustainability, ensuring an engaging experience for participants of all sizes. 
DRAF promotes inclusivity, long-term holding, and active engagement while balancing the influence of larger holders.


**Key Features**
Progressive Bonuses for Small Holders: Rewards smaller participants with additional bonuses to ensure inclusivity and fairness.

Regressive Penalties for Large Holders: Balances the system by slightly reducing rewards for larger participants to prevent dominance.

Dynamic Scalability: Automatically adjusts to transaction volume, holding time, and participant activity.

Holding Time Rewards: Long-term participants are incentivized through a holding time multiplier, encouraging ecosystem stability.

Sustainable Growth: The Reward Pool is dynamically funded through transaction contributions, creating a self-sustaining system.

Transparency and Trust: A deterministic formula enables participants to predict their rewards and fosters trust in the system.

**How It Works**
DRAF dynamically allocates rewards from the Reward Pool (𝑇reward) based on:
Token Holdings (𝑇𝑖Ti)
Progressive Bonuses (𝛽)
Regressive Penalties (𝛼)
Holding Time Multiplier (𝐻holding)

def calculate_reward(T_reward, T_i, total_weighted_tokens, beta, alpha, H_holding):
    """
    Calculate the reward for a participant based on the DRAF formula.
    
    Parameters:
    T_reward (float): Total reward pool available for distribution.
    T_i (float): Tokens held by the participant.
    total_weighted_tokens (float): Sum of all weighted tokens in the system.
    beta (float): Progressive bonus for the participant.
    alpha (float): Regressive penalty for the participant.
    H_holding (float): Holding time multiplier for the participant.

    Returns:
    float: Reward allocated to the participant.
    """
    # Weighted tokens for the participant
    weighted_tokens_i = T_i * (1 + beta - alpha) * (1 + H_holding)

    # Reward calculation
    reward = T_reward * (weighted_tokens_i / total_weighted_tokens)

    return reward


Example usage
if __name__ == "__main__":
    # Example parameters
    T_reward = 10000  # Total reward pool
    T_i = 1000  # Participant's token holdings
    total_weighted_tokens = 50000  # Total weighted tokens in the system
    beta = 0.10  # Progressive bonus
    alpha = 0.05  # Regressive penalty
    H_holding = 0.50  # Holding time multiplier (e.g., for 6 months)

    # Calculate reward
    reward = calculate_reward(
        T_reward,
        T_i,
        total_weighted_tokens,
        beta,
        alpha,
        H_holding
    )

    print(f"Reward for the participant: {reward:.2f}")


**Here’s a simple example of how to calculate rewards using DRAF:
from draf_calculator import calculate_reward**

Example parameters
T_reward = 10000
token_holding = 1000
total_weighted_tokens = 50000
beta_min = 0.05
beta_max = 0.15
alpha_min = 0.02
alpha_max = 0.10
holding_time = 6
max_holding_time = 12
max_share = 0.2

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



    
