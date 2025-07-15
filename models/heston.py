import numpy as np

def heston_sim(S0, v0, r, kappa, theta, sigma_v, rho, T, N, M):
    """
    S0: Initial stock price
    v0: Initial variance
    r: Risk-free rate
    kappa: Mean reversion speed of variance
    theta: Long-run variance
    sigma_v: Volatility of volatility
    rho: Correlation between asset and variance
    T: Time to maturity (in years)
    N: Number of time N
    M: Number of simulated M

    Returns:
    S: Simulated asset prices (M x N+1)
    v: Simulated variances (M x N+1)
    """
    dt = T / N

    # containers for all simulated M
    S = np.zeros((M, N + 1))
    v = np.zeros((M, N + 1))

    # starting values
    S[:, 0] = S0
    v[:, 0] = v0

    for t in range(1, N + 1):
        z1 = np.random.randn(M)
        z2 = np.random.randn(M)
        w1 = z1
        w2 = rho * z1 + np.sqrt(1 - rho ** 2) * z2

        v_prev = v[:, t - 1]
        v[:, t] = np.maximum(
            v_prev + kappa * (theta - v_prev) * dt + sigma_v * np.sqrt(np.maximum(v_prev, 0)) * np.sqrt(dt) * w2,
            0.0
        )

        S[:, t] = S[:, t - 1] * np.exp(
            (r - 0.5 * v_prev) * dt + np.sqrt(np.maximum(v_prev, 0)) * np.sqrt(dt) * w1
        )

    return S, v
