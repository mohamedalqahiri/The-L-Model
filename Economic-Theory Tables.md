###  The L Model Core

### Table of Equations

| Equation | Value range & unit | Role/source |
| :--- | :--- | :--- |
| $\text{PROSUM.A}_t = L_t^(1 + \frac{\text{sync}(r_t / f_t)}{1 + R + \sigma}\right)$ | | System output at time $t$ |
| $L_t = L_0 \cdot (1 + n)^t$ | $0.0 < L_0 \leq 0.50 \ (0.27)$ | Active human innovation factor as % of total population. |
| $n = 0.015 \cdot \left(\frac{r_t}{f_t} + 1\right)$ | $n : 3.5\% \rightarrow 3\%$ | Natural growth rate of innovators augmented by synergy with AI. |
| $\langle 1 \rangle$ in the exponent = Constant. | | Human Inherent Cognitive. |
|$$\text{Sync}_t = f_t \cdot \left(1 + \ln\left(1 + \frac{f_t}{r_t}\right)\right)$$|with r= f=1, sync = 1.693 |Matter & Energy Input flow \'$f$\' and Processing Robotic \'$r$\' sync. ensuring system vitality. |
| $f_t = \frac{1}{1 + 5.667 \cdot e^{-0.k \cdot t}}$ | $f : 0.15 \rightarrow 1.0$ | Inputs Flow/Total inputs (flow+stock). |
| $r_t = \frac{1}{1 + 4 \cdot e^{-0.k \cdot t}}$ | $r : 0.2 \rightarrow 1.0$ | Robotized Processing/Total Processing Work Load |
| | $k = 0.65$ | Accelerator growth rate of robotics and inputs flow in high tech ecosystem. |
| Total Absorptions $= 1 + R + \sigma$ | | |
| $R_t = \theta \cdot \frac{f_t}{r_t}$ | $\theta = 0.28 (mid-point of 0.24 , 0.32$ | Responsiveness Development Vector |
| $\sigma_t = 0.2 \cdot (1 + \text{Dsec}) \cdot E_{\text{inst}}$ | $0.2$ drag base | Institutional and sectoral drag coefficient |
| $E_{\text{inst}_t} = e^{\lambda(1 - f_t) + c}$| $\lambda : 0.3 \rightarrow 0$ | Institutional drag coefficient |
| $\text{Dsec}_t = (1 - f_t) \cdot (\tau \cdot abs(2\rho - 1) + \mu \cdot\text{d.cagr}(t) )$ |d_cagr = 0.0425 | Sectoral drag coefficient |

### Parameters Table

| Parameters | Value range and unit | Role/source |
| :--- | :--- | :--- |
| $R \text{ Distrib.} = a_{IQ} + a_{\text{Phi}} + a_{\text{Ser}} + a_{\text{infra}}$ | | //Calibrated based on US, Germany and China data. |
| As % $R_t$ : $IQ_t =$ | $31.0\%$ | - Human-Core Development. |
| $Phi_t =$ | $12.5\%$ | - Extra-Terrestrial Infrastructure. |
| $Ser =$ | $18.75\%$ | - Cyber-Protection. |
| $infra =$ | $37.5\%$ | - Infrastructure & Energy. |
| | | |
| $G = G = \text{Subsidies} / \text{Total GDP}$ | $0.25$ | Government subsidies to primary sector // World Bank, IMF. |
| $\gamma =$ | $0.2$ | Direct impact weight of subsidies // US Federal Reserve. |
| $c = G × $gamma$ | $0.05$ | Policy impact // OECD |
| $\tau$ | $0.15$ | Size variance weight // World Bank Sector Data. |
| $\mu$ | $0.5$ | Growth variance weight // IMF Growth Reports |
| $\rho = GDP {h-tech}/Total GDP$ | $0.35$ | Relative high-tech sector volume // UNCTAD, BIS. |
| $\text{d.cagr}(t) = 0.07e^{-0.1t}$ | $0.07 \sim 0$ | Sectors growth rate differential $d_cagr$ // Calibrated on US, Germany, China data. |

### Numerical Examples

$t = 5; \ L_0 = 100; \ c = 0.05; \ \tau = 0.15; \ \mu = 0.5; \ \rho = 0.35:$

| | |
| :--- | :--- |
| $\text{PROSUM.A} = 116.67^{(1 + 1.411 / (1 + 0.303 + 0.224))} =$ | **9,482.511** |
| $L_5 = 27 \cdot \text{EXP}(1)^{(0.0303 \cdot 5)} =$ | 116.673 |
| $n(5) = 0.015 \cdot (0.866 / 0.82 + 1) =$ | 0.031 |
| $\text{Sync}(5) = 0.820 \cdot (1 + \text{LN}(1 + 0.866 / 0.82)) =$ | 1.411 |
| $f_5 = 1 / (1 + 5.667 \cdot \text{EXP}(1)^{(-0.65 \cdot 5)}) =$ | 0.820 |
| $r_5 = 1 / (1 + 4 \cdot \text{EXP}(1)^{(-0.65 \cdot 5)}) =$ | 0.866 |
| $R(5) = 0.32 \cdot (0.82 / 0.866) =$ | 0.303 |
| $\sigma(5) = 0.2 \cdot (1 + 0.0075) \cdot 1.11 =$ | 0.224 |
| $E_{\text{inst}}(5) = \text{EXP}(1)^{(0.3 \cdot (1 - 0.82) + 0.05)} =$ | 1.110 |
| $\text{Dsec}(5) = (1 - 0.82) \cdot (0.15 \cdot \text{ABS}((2 \cdot 0.35 - 1) + 0.5 \cdot 0.0425)) =$ | 0.008 |
| $d_{\text{cagr}}(5) = 0.07 \cdot \text{EXP}(1)^{(-0.1 \cdot 5)} =$ | 0.0425 |
