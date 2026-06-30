### 1. Table of Equations - Model L Core

| Equation | Value range & unit | Role/source |
| :--- | :--- | :--- |
| $$\text{PROSUM.A}_t = L_t \cdot \left(1 + \frac{\text{Sync}_t}{t}\right)$$ | Unitless | Productivity output at time t |
| $$L_t = L_0 \cdot (1 + n)^t$$ | $0.0 < L_0 \leq 0.50$ | Labor force. $L_0$ = initial population ratio |
| $$n = 0.015 \cdot \left(\frac{r_t}{f_t} + 1\right)$$ | $n \geq 0.015$ | Growth rate, augmented by synergy with AI |
| $$\langle 1 \rangle$$ | Constant = 1 | Human constant in exponent |
| $$\text{Sync}_t = f_t \cdot \left\{1 + \ln\left(1 + \frac{f_t}{r_t}\right)\right\}$$ | Max = 1.693 | Matter & Energy Input flow $f$ and Processing $r$ |
| $$f_t = \frac{1}{1 + 5.667 \cdot e^{-0.k \cdot t}}$$ | $0 \leq f_t \leq 1$ | Flow stock sigmoid |
| $$r_t = \frac{1}{1 + 4 \cdot e^{-0.k \cdot t}}$$ | $0 \leq r_t \leq 1$ | Work Load sigmoid |
|  | $k = 0.65$ | Accelerator growth rate of robotics and AI |
| $$\text{Total Absorptions} = 1 + R + \sigma$$ | $\geq 1$ | System capacity |
| $$R_t = \theta \cdot \frac{f_t}{r_t}$$ | $\theta = 0.24$ | Resource coefficient |
| $$\sigma_t = 0.2 \cdot (1 + \text{Dsec}) \cdot E_{\text{inst}_t}$$ | $0.2 \leq \sigma_t$ | Entropy coefficient |
| $$E_{\text{inst}_t} = e^{\lambda(1 - f_t) + c}$$ | $\lambda > 0$ | Institutional energy |
| $$\text{Dsec}_t = (1 - f_t) \cdot [\tau \cdot |2\rho - 1|]$$ | $0 \leq \text{Dsec}_t$ | Dissipation coefficient |

### 2. Table of Parameters
| Symbol | Value | Description | Unit |
| :--- | :--- | :--- | :--- |
| $L_0$ | $0.1 - 0.5$ | Initial labor ratio | Ratio |
| $n$ | $\geq 0.015$ | AI-augmented growth | 1/year |
| $k$ | $0.65$ | Robotics accelerator | 1/year |
| $\theta$ | $0.24$ | Resource scaling | Unitless |
| $\lambda$ | $> 0$ | Institutional decay | 1/year |

### 3. Numerical Example
| Variable | Input Value | Output | Note |
| :--- | :--- | :--- | :--- |
| $L_0$ | $0.30$ | - | 30% population active |
| $t$ | $10$ | - | 10 years |
| $f_{10}$ | - | $0.82$ | From sigmoid eq |
| $r_{10}$ | - | $0.71$ | From sigmoid eq |
| $\text{PROSUM.A}_{10}$ | - | $1.43$ | 43% productivity gain |
