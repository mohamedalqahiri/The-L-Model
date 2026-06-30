### 1. Table of Equations - The L Model Core

| Equation | Value range & unit | Role/source |
| :--- | :--- | :--- |
| $$L_t = L_0 \cdot (1 + n)^t$$ | $0.0 < L_0 \leq 0.50$ | Labor force.<br>$L_0$ = Initial population ratio |
| $$n = 0.015 \cdot \left(\frac{r_t}{f_t} + 1\right)$$ | $n \geq 0.015$ | Growth rate,<br>augmented by synergy with AI |
| $$\langle 1 \rangle$$ | Constant = 1 | Human constant<br>in exponent |
| $$\text{Sync}_t = f_t \cdot \left(1 + \ln\left(1 + \frac{f_t}{r_t}\right)\right)$$ | Max = 1.693 | Matter & Energy Input flow $f$<br>and Processing $r$ |
| $$f_t = \frac{1}{1 + 5.667 \cdot e^{-0.k \cdot t}}$$ | $0 \leq f_t \leq 1$ | Flow stock<br>sigmoid |
| $$r_t = \frac{1}{1 + 4 \cdot e^{-0.k \cdot t}}$$ | $0 \leq r_t \leq 1$ | Work Load<br>sigmoid |
|  | $k = 0.65$ | Accelerator growth rate<br>of robotics and AI |
| $$\text{Total Absorptions} = 1 + R + \sigma$$ | $\geq 1$ | System<br>capacity |
| $$R_t = \theta \cdot \frac{f_t}{r_t}$$ | $\theta = 0.24$ | Resource<br>coefficient |
| $$\sigma_t = 0.2 \cdot (1 + \text{Dsec}) \cdot E_{\text{inst}_t}$$ | $0.2 \leq \sigma_t$ | Entropy<br>coefficient |
| $$E_{\text{inst}_t} = e^{\lambda(1 - f_t) + c}$$ | $\lambda > 0$ | Institutional<br>energy |
| $$\text{Dsec}_t = (1 - f_t) \cdot \left[\tau \cdot \|2\rho - 1\|\right]$$ | $0 \leq \text{Dsec}_t$ | Dissipation<br>coefficient |
