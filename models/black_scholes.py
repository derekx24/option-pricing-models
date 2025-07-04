import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Price a European option using the Black-Scholes formula.

    Parameters:
    S: Spot price
    K: Strike price
    T: Time to maturity (in years)
    r: Risk-free rate
    sigma: Volatility

    Returns:
    Option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

def delta(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    if option_type == "call":
        return norm.cdf(d1)
    elif option_type == "put":
        return norm.cdf(d1) - 1

def gamma(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    return S * norm.pdf(d1) * np.sqrt(T)

def theta(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    term1 = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    if option_type == "call":
        return term1 - r * K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return term1 + r * K * np.exp(-r * T) * norm.cdf(-d2)

def rho(S, K, T, r, sigma, option_type="call"):
    d2 = (np.log(S / K) + (r - 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    if option_type == "call":
        return K * T * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return -K * T * np.exp(-r * T) * norm.cdf(-d2)