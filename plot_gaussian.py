import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, cauchy

# Define range of x values
x = np.linspace(-10, 10, 500)

# Calculate PDFs
gaussian_pdf = norm.pdf(x, loc=0, scale=1)
cauchy_pdf = cauchy.pdf(x, loc=0, scale=1)

# Calculate negative log-likelihoods
gaussian_nll = -np.log(gaussian_pdf)
cauchy_nll = -np.log(cauchy_pdf)

# Plot
fig, axs = plt.subplots(2, 1, figsize=(6, 8), sharex=True)

# Top plot: PDFs
axs[0].plot(x, gaussian_pdf, 'k-', label='Gaussian PDF')
axs[0].plot(x, cauchy_pdf, 'k--', label='Cauchy PDF')
axs[0].set_ylabel('Probability Density')
axs[0].legend(loc='upper right')
axs[0].grid(True)

# Bottom plot: Negative Log-Likelihoods
axs[1].plot(x, gaussian_nll, 'k-', label='Gaussian -log likelihood')
axs[1].plot(x, cauchy_nll, 'k--', label='Cauchy -log likelihood')
axs[1].set_ylabel('-log likelihood')
axs[1].set_xlabel('x')
axs[1].legend(loc='upper right')
axs[1].grid(True)

plt.tight_layout()
plt.show()
