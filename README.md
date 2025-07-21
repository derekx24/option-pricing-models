# Option Pricing Models (Black-Scholes, Monte Carlo, Heston)

This project implements and compares three models for pricing European options:

- **Black-Scholes** 
- **Monte Carlo simulation**
- **Heston stochastic volatility model**

It evaluates model outputs against real-world market data (from `yfinance`) and explores pricing discrepancies.

## Models & Methodology

### Black-Scholes
- Assumes constant volatility.
- Closed-form analytical formula for call and put options.
- Used to compute Greeks.

### Monte Carlo Simulation
- Simulates thousands of asset price paths to compute expected payoff.
- Demonstrates convergence and path dependency.
- Highlights the tradeoff between accuracy and computational cost.

### Heston Model
- Models volatility as a stochastic process.
- Captures smile/skew not handled by Black-Scholes.
- Simulated using Euler-Maruyama discretization.

## Insights & Takeaways

- Pulled real AAPL call and put option chains using `yfinance` and compared them to prices from Black-Scholes and Heston models  
- Plotted the differences across strike prices to see where the models over price or under price options  
- Used Black-Scholes and Heston models to price European call options under risk-neutral assumptions  
- Reflected on how model assumptions affect pricing and where they might break down  
- connected the theory to real data and see how these models behave in the real world

## Setup

```bash
conda create -n options python=3.9
conda activate options
pip install -r requirements.txt
```