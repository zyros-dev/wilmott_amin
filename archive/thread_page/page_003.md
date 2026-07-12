# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 3 of 59** — Posts #101–#150

[← Previous](page_002.md) | [Index](index.md) | [Next →](page_004.md)

---

### #101 — Amin (Topic Author)
*June 8, 2016, 3:28 PM*

I wrote this attempt at solution of general fokker planck PDE the day before yesterday on Latex. I have not numerically
verified it so I cannot be sure whether it is right or not. Since my research reaches some American institutions of
higher learning, I have decided to put it on internet otherwise I would have waited to verify it numerically.Let us
consider a general fokker planck equation stated as
$\frac{\partial p(x,t)}{\partial t}=-\frac{\partial [\mu (x)p(x,t)]}{\partial x}+\frac{.5\partial ^2\left[\sigma (x)^2p(x,t)\right]}{\partial x^2}$
Eq(1)Expanding the first order and second order derivatives on the right side of PDE in Eq(1), we get
$\frac{\partial p(x,t)}{\partial t}=-\mu (x)\frac{\partial p(x,t)]}{\partial x}-\frac{\partial \mu (x)}{\partial x}p(x,t)+\frac{\partial \sigma (x)}{\partial x}p(x,t)+2\sigma (x)\frac{\partial p(x,t)}{\partial x}+.5\sigma (x)^2\frac{\partial ^2p(x,t)}{\partial x^2}$
Eq(2)We divide the x-dimension in PDE into small subdivisions like we did in stochastic calculus of Standard deviations,
and we know that each standard deviation moves in a way that mass is preserved in each subdivision. We want to find a
local solution to this PDE for each subdivision. Let us fix some notations first. Each subdivision at time t starts at
coordinates given as$x_a(\text{t})$ and ends at coordinates$x_b(\text{t})$ . These are the limits of integration when we
integrate for the probability mass over each subdivision. We also set$x_0(\text{t})$ as the centre of the subdivision at
time t.$C_n$ is the probability mass in subdivision related to nth standard deviation of the normal. When we have to
deal with normal distribution after setting the equations, we replace normal distribution by appropriate arbitrary
standard deviation n and then solve the equations for each n separately. We want to try a time averaged form of normal
distribution as a solution in this pde. We try a solution where$\bar{\mu }$ and$\bar{\sigma }$ are time averaged values
of drift and volatility for the specific step size from$t_0$ to$t_1$ and subdivision limits$x_a(\text{t})$ to
$x_b(\text{t})$ and we use them as the local solution for that specific x and t discretisation. We try to present the
averaged local solution for each subdivision as a normal given by the equation
$g(x,t)=\frac{1}{\bar{\sigma }\sqrt{2\pi  t}}\exp \left(-.5\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right){}^2\right)$
Eq(3)We will like to emphasize that once the two ends of subdivisions$x_a(\text{t})$ and$x_b(\text{t})$ , or
alternatively mid of the subdivision$x_0(\text{t})$ , and drift and volatility parameters$\bar{\mu }$ and$\bar{\sigma }$
are given, we can find the ends of subdivisions at the next time step as
$x_a\left(t_1\right)=x_a\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)-.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)$
Eq(4)
$x_b\left(t_1\right)=x_b\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)+.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)$
Eq(5)We start by taking the appropriate derivatives of the equation before we put it in the Pde Eq(2). The derivatives
are given as$\frac{\partial g(x,t)}{\partial x}=-g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)$
Eq(6)
$\frac{\partial ^2g(x,t)}{\partial x^2}=g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right){}^2-\frac{g(x,t)}{\bar{\sigma }\sqrt{t}}$
Eq(7)
$\frac{\partial g(x,t)}{\partial t}=g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)\left(\frac{x-x_0-\bar{\mu }t}{2\bar{\sigma }t^{1,5}}+\frac{\bar{\mu }}{\bar{\sigma }\sqrt{t}}\right)$
Eq(8)We integrate both sides of the PDE in Eq(2) over time from$t_0$ to$t_1$ to find the change in probability mass and
then we integrate over each subdivision$x_a(\text{t_1})$ and$x_b(\text{t_1})$ to find the total probability mass in each
subdivision that is kept constant by supposition and is the same as the mass at the start in subdivision
$x_a(\text{t_0})$ and$x_b(\text{t_0})$ given by$C_n$ . We get two equations from both sides of the PDE and we solve them
to find the unknowns that are$\bar{\mu }$ and$\bar{\sigma }$ , the time averaged values of drift and volatility for the
specific step size from$t_0$ to$t_1$ and subdivision limits$x_a(\text{t_1})$ to$x_b(\text{t_1})$ We put Eq(6) in LHS of
PDE in Eq(2) and do this as
$\int _{x_a(\text{t1})}^{x_{b(\text{t1})}}\int _{t_0}^{t_1}\frac{\partial p(x, t)}{\partial t} \text{dt} \text{dx}=C_n$
Eq(8)
$\int _{x_a(\text{t1})}^{x_b(\text{t1})}\int _{t_0}^{t_1}g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)\left(\frac{x-x_0-\bar{\mu }t}{2\bar{\sigma }t^{1,5}}+\frac{\bar{\mu }}{\bar{\sigma }\sqrt{t}}\right)\text{dt} \text{dx}=C_n$
Eq(9)We replace normal function g(x,t) by specific standard deviation 'n' for which we are solving the PDE. We know
standard deviations are units of normal. We will have to solve the equation for each different n using the same
algorithm.
$\int _{x_a(\text{t1})}^{x_b(\text{t1})}\int _{t_0}^{t_1}n\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)\left(\frac{x-x_0-\bar{\mu }t}{2\bar{\sigma }t^{1,5}}+\frac{\bar{\mu }}{\bar{\sigma }\sqrt{t}}\right)\text{dt} \text{dx}=C_n$
Eq(10)using Eq(4) and Eq(5) given again as
$x_a\left(t_1\right)=x_a\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)-.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)$
Eq(4)
$x_b\left(t_1\right)=x_b\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)+.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)$
Eq(5)and putting them as limits of integration for each subdivision, we get
$\int _{x_a\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)-.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)}^{x_b\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)+.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)}\int _{t_0}^{t_1}n\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)\left(\frac{x-x_0-\bar{\mu }t}{2\bar{\sigma }t^{1,5}}+\frac{\bar{\mu }}{\bar{\sigma }\sqrt{t}}\right)\text{dt} \text{dx}=C_n$
Eq(11)We put Eq(7) and Eq(8) in RHS of PDE (2) and just Similar to what we did for the left hand side of the PDE as
$\int _{x_a\left(t_1\right)}^{x_b\left(t_1\right)}\int _{t_0}^{t_1}\left(-\frac{\partial [\mu (x)p(x,t)]}{\partial x}+\frac{.5\partial ^2\left[\sigma (x)^2p(x,t)\right]}{\partial x^2}\right) \text{dt} \text{dx}=C_n$
Eq(12)
$\int _{x_a\left(t_1\right)}^{x_b\left(t_1\right)}\int _{t_0}^{t_1}\left(-\mu (x)\frac{\partial p(x,t)]}{\partial x}-\frac{\partial \mu (x)}{\partial x}p(x,t)+\frac{\partial \sigma (x)}{\partial x}p(x,t)+2\sigma (x)\frac{\partial p(x,t)}{\partial x}+.5\sigma (x)^2\frac{\partial ^2p(x,t)}{\partial x^2}\right) \text{dt} \text{dx}=C_n$
Eq(13)
$\int _{x_a\left(t_1\right)}^{x_b\left(t_1\right)}\int _{t_0}^{t_1}\left(\mu (x)g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)-\frac{\partial \mu (x)}{\partial x}g(x,t)+\frac{\partial \sigma (x)}{\partial x}g(x,t)-2\sigma (x)g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)+.5\sigma (x)^2\left(g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right){}^2-\frac{g(x,t)}{\bar{\sigma }\sqrt{t}}\right)\right) \text{dt} \text{dx}=C_n$
Eq(14)We replace normal function g(x,t) by specific standard deviation 'n' for which we are solving the PDE. We know
standard deviations are units of normal. We will have to solve the equation for each different n using the same
algorithm.
$\int _{x_a\left(t_1\right)}^{x_b\left(t_1\right)}\int _{t_0}^{t_1}n\left(+\mu (x)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)-\frac{\partial \mu (x)}{\partial x}+\frac{\partial \sigma (x)}{\partial x}-2\sigma (x)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)+.5\sigma (x)^2\left(\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right){}^2-\frac{1}{\bar{\sigma }\sqrt{t}}\right)\right) \text{dt} \text{dx}=C_n$
Eq(15)using Eq(4) and Eq(5) and replacing the ends of the subdivisions in the integration limits as
$\int _{x_a\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)-.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)}^{x_b\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)+.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)}\int _{t_0}^{t_1}n\left(\mu (x)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)-\frac{\partial \mu (x)}{\partial x}+\frac{\partial \sigma (x)}{\partial x}-2\sigma (x)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)+.5\sigma (x)^2\left(\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right){}^2-\frac{1}{\bar{\sigma }\sqrt{t}}\right)\right) \text{dt} \text{dx}=C_n$
Eq(16)Now we have two equations in two unknowns that are$\bar{\mu }$ and$\bar{\sigma }$ , the local time averaged values
of drift and volatility for the specific step size from$t_0$ to$t_1$ and subdivision limits$x_a(\text{t_1})$ to
$x_b(\text{t_1})$ and we have two equations Eq(11) and Eq(16) that we can solve together for each value of standard
deviation n to find the two unknowns. EDIT: I changed Eqs (4) and 5 slightly. Limits in dependent equations also
changed.EDIT2: Some signs were wrong in FP equation when I expanded the derivatives. Corrected them.

---

### #102 — Amin (Topic Author)
*July 2, 2016, 3:21 PM*

QuoteOriginally posted by: AminI wrote this attempt at solution of general fokker planck PDE the day before yesterday on
Latex. I have not numerically verified it so I cannot be sure whether it is right or not. Since my research reaches some
American institutions of higher learning, I have decided to put it on internet otherwise I would have waited to verify
it numerically.Let us consider a general fokker planck equation stated as
$\frac{\partial p(x,t)}{\partial t}=-\frac{\partial [\mu (x)p(x,t)]}{\partial x}+\frac{.5\partial ^2\left[\sigma (x)^2p(x,t)\right]}{\partial x^2}$
Eq(1)Expanding the first order and second order derivatives on the right side of PDE in Eq(1), we get
$\frac{\partial p(x,t)}{\partial t}=-\mu (x)\frac{\partial p(x,t)]}{\partial x}-\frac{\partial \mu (x)}{\partial x}p(x,t)+\frac{\partial \sigma (x)}{\partial x}p(x,t)+2\sigma (x)\frac{\partial p(x,t)}{\partial x}+.5\sigma (x)^2\frac{\partial ^2p(x,t)}{\partial x^2}$
Eq(2)We divide the x-dimension in PDE into small subdivisions like we did in stochastic calculus of Standard deviations,
and we know that each standard deviation moves in a way that mass is preserved in each subdivision. We want to find a
local solution to this PDE for each subdivision. Let us fix some notations first. Each subdivision at time t starts at
coordinates given as$x_a(\text{t})$ and ends at coordinates$x_b(\text{t})$ . These are the limits of integration when we
integrate for the probability mass over each subdivision. We also set$x_0(\text{t})$ as the centre of the subdivision at
time t.$C_n$ is the probability mass in subdivision related to nth standard deviation of the normal. When we have to
deal with normal distribution after setting the equations, we replace normal distribution by appropriate arbitrary
standard deviation n and then solve the equations for each n separately. We want to try a time averaged form of normal
distribution as a solution in this pde. We try a solution where$\bar{\mu }$ and$\bar{\sigma }$ are time averaged values
of drift and volatility for the specific step size from$t_0$ to$t_1$ and subdivision limits$x_a(\text{t})$ to
$x_b(\text{t})$ and we use them as the local solution for that specific x and t discretisation. We try to present the
averaged local solution for each subdivision as a normal given by the equation
$g(x,t)=\frac{1}{\bar{\sigma }\sqrt{2\pi  t}}\exp \left(-.5\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right){}^2\right)$
Eq(3)We will like to emphasize that once the two ends of subdivisions$x_a(\text{t})$ and$x_b(\text{t})$ , or
alternatively mid of the subdivision$x_0(\text{t})$ , and drift and volatility parameters$\bar{\mu }$ and$\bar{\sigma }$
are given, we can find the ends of subdivisions at the next time step as
$x_a\left(t_1\right)=x_a\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)-.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)$
Eq(4)
$x_b\left(t_1\right)=x_b\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)+.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)$
Eq(5)We start by taking the appropriate derivatives of the equation before we put it in the Pde Eq(2). The derivatives
are given as$\frac{\partial g(x,t)}{\partial x}=-g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)$
Eq(6)
$\frac{\partial ^2g(x,t)}{\partial x^2}=g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right){}^2-\frac{g(x,t)}{\bar{\sigma }\sqrt{t}}$
Eq(7)
$\frac{\partial g(x,t)}{\partial t}=g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)\left(\frac{x-x_0-\bar{\mu }t}{2\bar{\sigma }t^{1,5}}+\frac{\bar{\mu }}{\bar{\sigma }\sqrt{t}}\right)$
Eq(8)We integrate both sides of the PDE in Eq(2) over time from$t_0$ to$t_1$ to find the change in probability mass and
then we integrate over each subdivision$x_a(\text{t_1})$ and$x_b(\text{t_1})$ to find the total probability mass in each
subdivision that is kept constant by supposition and is the same as the mass at the start in subdivision
$x_a(\text{t_0})$ and$x_b(\text{t_0})$ given by$C_n$ . We get two equations from both sides of the PDE and we solve them
to find the unknowns that are$\bar{\mu }$ and$\bar{\sigma }$ , the time averaged values of drift and volatility for the
specific step size from$t_0$ to$t_1$ and subdivision limits$x_a(\text{t_1})$ to$x_b(\text{t_1})$ We put Eq(6) in LHS of
PDE in Eq(2) and do this as
$\int _{x_a(\text{t1})}^{x_{b(\text{t1})}}\int _{t_0}^{t_1}\frac{\partial p(x, t)}{\partial t} \text{dt} \text{dx}=C_n$
Eq(8)
$\int _{x_a(\text{t1})}^{x_b(\text{t1})}\int _{t_0}^{t_1}g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)\left(\frac{x-x_0-\bar{\mu }t}{2\bar{\sigma }t^{1,5}}+\frac{\bar{\mu }}{\bar{\sigma }\sqrt{t}}\right)\text{dt} \text{dx}=C_n$
Eq(9)We replace normal function g(x,t) by specific standard deviation 'n' for which we are solving the PDE. We know
standard deviations are units of normal. We will have to solve the equation for each different n using the same
algorithm.
$\int _{x_a(\text{t1})}^{x_b(\text{t1})}\int _{t_0}^{t_1}n\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)\left(\frac{x-x_0-\bar{\mu }t}{2\bar{\sigma }t^{1,5}}+\frac{\bar{\mu }}{\bar{\sigma }\sqrt{t}}\right)\text{dt} \text{dx}=C_n$
Eq(10)using Eq(4) and Eq(5) given again as
$x_a\left(t_1\right)=x_a\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)-.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)$
Eq(4)
$x_b\left(t_1\right)=x_b\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)+.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)$
Eq(5)and putting them as limits of integration for each subdivision, we get
$\int _{x_a\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)-.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)}^{x_b\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)+.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)}\int _{t_0}^{t_1}n\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)\left(\frac{x-x_0-\bar{\mu }t}{2\bar{\sigma }t^{1,5}}+\frac{\bar{\mu }}{\bar{\sigma }\sqrt{t}}\right)\text{dt} \text{dx}=C_n$
Eq(11)We put Eq(7) and Eq(8) in RHS of PDE (2) and just Similar to what we did for the left hand side of the PDE as
$\int _{x_a\left(t_1\right)}^{x_b\left(t_1\right)}\int _{t_0}^{t_1}\left(-\frac{\partial [\mu (x)p(x,t)]}{\partial x}+\frac{.5\partial ^2\left[\sigma (x)^2p(x,t)\right]}{\partial x^2}\right) \text{dt} \text{dx}=C_n$
Eq(12)
$\int _{x_a\left(t_1\right)}^{x_b\left(t_1\right)}\int _{t_0}^{t_1}\left(-\mu (x)\frac{\partial p(x,t)]}{\partial x}-\frac{\partial \mu (x)}{\partial x}p(x,t)+\frac{\partial \sigma (x)}{\partial x}p(x,t)+2\sigma (x)\frac{\partial p(x,t)}{\partial x}+.5\sigma (x)^2\frac{\partial ^2p(x,t)}{\partial x^2}\right) \text{dt} \text{dx}=C_n$
Eq(13)
$\int _{x_a\left(t_1\right)}^{x_b\left(t_1\right)}\int _{t_0}^{t_1}\left(\mu (x)g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)-\frac{\partial \mu (x)}{\partial x}g(x,t)+\frac{\partial \sigma (x)}{\partial x}g(x,t)-2\sigma (x)g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)+.5\sigma (x)^2\left(g(x,t)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right){}^2-\frac{g(x,t)}{\bar{\sigma }\sqrt{t}}\right)\right) \text{dt} \text{dx}=C_n$
Eq(14)We replace normal function g(x,t) by specific standard deviation 'n' for which we are solving the PDE. We know
standard deviations are units of normal. We will have to solve the equation for each different n using the same
algorithm.
$\int _{x_a\left(t_1\right)}^{x_b\left(t_1\right)}\int _{t_0}^{t_1}n\left(+\mu (x)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)-\frac{\partial \mu (x)}{\partial x}+\frac{\partial \sigma (x)}{\partial x}-2\sigma (x)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)+.5\sigma (x)^2\left(\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right){}^2-\frac{1}{\bar{\sigma }\sqrt{t}}\right)\right) \text{dt} \text{dx}=C_n$
Eq(15)using Eq(4) and Eq(5) and replacing the ends of the subdivisions in the integration limits as
$\int _{x_a\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)-.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)}^{x_b\left(t_0\right)+\bar{\mu }\left(t_1-t_0\right)+.5\bar{\sigma }\left(\sqrt{t_1}-\sqrt{t_0}\right)}\int _{t_0}^{t_1}n\left(\mu (x)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)-\frac{\partial \mu (x)}{\partial x}+\frac{\partial \sigma (x)}{\partial x}-2\sigma (x)\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right)+.5\sigma (x)^2\left(\left(\frac{x-x_0-\bar{\mu }t}{\bar{\sigma }\sqrt{t}}\right){}^2-\frac{1}{\bar{\sigma }\sqrt{t}}\right)\right) \text{dt} \text{dx}=C_n$
Eq(16)Now we have two equations in two unknowns that are$\bar{\mu }$ and$\bar{\sigma }$ , the local time averaged values
of drift and volatility for the specific step size from$t_0$ to$t_1$ and subdivision limits$x_a(\text{t_1})$ to
$x_b(\text{t_1})$ and we have two equations Eq(11) and Eq(16) that we can solve together for each value of standard
deviation n to find the two unknowns. EDIT: I changed Eqs (4) and 5 slightly. Limits in dependent equations also
changed.EDIT2: Some signs were wrong in FP equation when I expanded the derivatives. Corrected them.I had learnt of the
mistakes in my derivation in the following days when I wrote this post but since so many things were happening I could
not come back to correcting the mistakes. I am more peaceful now so I decided to write again to make amends in the
procedure I suggested to find the local time averaged values of mean and volatility for each subdivision.QuoteWe
integrate both sides of the PDE in Eq(2) over time from$t_0$ to$t_1$ to find the change in probability mass and then we
integrate over each subdivision$x_a(\text{t_1})$ and$x_b(\text{t_1})$ to find the total probability mass in each
subdivision that is kept constant by supposition and is the same as the mass at the start in subdivision
$x_a(\text{t_0})$ and$x_b(\text{t_0})$ given by$C_n$ . We get two equations from both sides of the PDE and we solve them
to find the unknowns that are$\bar{\mu }$ and$\bar{\sigma }$ , the time averaged values of drift and volatility for the
specific step size from$t_0$ to$t_1$ and subdivision limits$x_a(\text{t_1})$ to$x_b(\text{t_1})$ The above argument has
a serious error that mass in a local Gaussian diffusion of the form that we have supposed cannot remain constant and a
lot of it leaks out of the boundaries and continues to diffuse to +infinity on one side and -infinity on the other side.
If the mass at the start at time$t_0$ in some nth subdivision is$C_n$ , it can never be$C_n$ at time$t_1$ in the
presence of a finite diffusion because some mass will leak out of both boundaries. Second error was that I replaced
normal distribution function with n everywhere which was wrong in the current context.Here are the amends to the
procedure to get the right local distribution for every subdivision. We follow a two step procedure.1. We know that mean
in each subdivision follows an ordinary differential equation. In a small subdivision, we can start an ODE from the mean
of the starting subdivision at time$t_0$ and find the mean of the subdivision at time$t_1$ This should be fairly simple.
We will have to make small amends to it for perfect accuracy but for small subdivisions it should work well enough.2.
Now we are left to calculate only local value of volatility for each subdivision. In order to do that we equate equation
(11) and equation (16) with time averaged value of mean$\bar{\mu }$ known. The normal function, that I erroneously
replaced with 'n' in above derivations in the previous post, would simply cancel out on both sides of equation with
equation(11) on LHS and equation (16) on RHS. Now we have a relatively simple equation to solve to calculate the value
of time averaged volatility$\bar{\sigma }$ . I am sure this can easily be done using mathematica with eq (11) and eq
(16) on LHS and RHS and$\bar{\mu }$ known.

---

### #103 — Amin (Topic Author)
*July 2, 2016, 4:23 PM*

I would like to mention that the above solution was just an exercise to find a different way to solve the Fokker planck
equation. The preferred method remains the stochastic calculus of standard deviations. I know now that using SCSD, we
can have a perfect accuracy for all different diffusions even close to zero. I clearly know how to tackle it even very
close to zero now. We can tackle diffusions with various kinds of drifts very seamlessly.

---

### #104 — Amin (Topic Author)
*July 3, 2016, 3:07 AM*

Ok, we were very close in stochastic  calculus of standard deviations but some improvement was required in the method.
We know how to tackle parts involving time and gaussian dependent terms g(z,t). Let us consider one step advance of the
densityX(t+1)=X(t)+f_1(X(t))g_1(z , t)+f_2(X(t))g_2(z,t)+..f_k(X(t))g_k(z,t);where f_n(X) is evaluated at X=X_0 i.e
centre of each of the subdivisions at time t.The terms of type f(X) are sometimes very non-linear and especially close
to zero they may become extremely non-linear. On top of that probability density may be very non-linear close to zero
and mid point evaluated value f(X_0) may not capture steep change in probability density. We have to take a value of
each f(X) term which is representative of the value(effective value) in the particular subdivision interval and we
cannot freely choose it to be f(X_0) which can however work well if the subdivisions are very small and
representative/effective value and value at centre become very close.Representative/effective value can easily be
calculated using the conditional Bayes law by taking an integral of  f(X)p(X)dX evaluated over the particular
subdivision divided by the integral of p(X)dX evaluated over the same subdivision interval. If the interval is very
small or the shape of pdf is so that we can suppose p(X) is a level surface in that interval (meaning non-linearity
comes only from f(X) term), we can take  integral of f(X)dX in numerator and integral of dX in denominator and this
could work decently well. Here p(X) is used to denote probability density.

---

### #105 — Amin (Topic Author)
*July 31, 2016, 9:14 AM*

Please check this attached program for simulation of CEV noise using SCSD technology.

![](./images/upload_icons/zip.gif)
[SDEXticsInfinitiTechnologiesCEVNoise02_Public.zip](./download/file.php?id=7418&sid=d0e37a29157ea47e520e988888970b37)
(1.99 KiB) Downloaded 176 times

In case you cannot download it. Here is the code.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [] = SDEXticsInfinitiTechnologiesCEVNoise02_Public( )

X0_max=800;%Total number of SD Fractions.

X0_mid=400.5;%Mid of the SD Grid. Lies at z0 by definition.

X0_mid0=400;

X0_start=1;

dX0=.0125;%*8.0;%Width of SD cells in terms of Standard Deviations.

T_index=100*1;

dt=.01/1.0;

epsilon=0.70

gamma=.650;

z0=1;

dz_integral2(1:X0_max)=z0;

iivector(1:X0_max)=1:X0_max;

paths=1000000; %No. of Paths for creation of Monte Carlo density by simulating z, F(z);

zz4(1:paths)=z0;

const=.398942*exp(-dX0^2.*(.25+(iivector-X0_mid).^2)).*(-exp(.5*dX0^2.*(-.5+(iivector-X0_mid)).^2)+exp(.5*dX0^2.*(.5+(iivector-X0_mid)).^2));;

const2=.398942*(dX0.*exp(-.5*dX0^2.*(.5+(iivector-X0_mid)).^2).*(-.5-(iivector-X0_mid))+...

dX0.*exp(-.5*dX0^2.*(-.5+(iivector-X0_mid)).^2).*(-.5+(iivector-X0_mid))-...

1.25331*erf(dX0.*(-.353553+.707107*(iivector-X0_mid)))+...

1.25331*erf(dX0.*(.353553+.707107*(iivector-X0_mid))));

const3=.398942.^1*(exp(-.5*dX0^2.*(-.5+(iivector-X0_mid)).^2).*(2+(.5-(iivector-X0_mid)).^2.*dX0^2)+...

exp(-.5*dX0^2.*(.5+(iivector-X0_mid)).^2).*(-2-(.5+(iivector-X0_mid)).^2*dX0^2));

const4=.398942.^1*(exp(-.5*dX0^2.*(.5+(iivector-X0_mid)).^2).*dX0.*(-1.5-3*(iivector-X0_mid)+(-.5-(iivector-X0_mid)).^3.*dX0^2)+...

    exp(-.5*dX0^2.*(-.5+(iivector-X0_mid)).^2).*dX0.*(-1.5+3*(iivector-X0_mid)+(-.5+(iivector-X0_mid)).^3.*dX0^2)-...

    3.75994*erf(dX0.*(-.353553+.707107*(iivector-X0_mid)))+...

    3.75994*erf(dX0.*(.353553+.707107*(iivector-X0_mid))));

prob2=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)*dX0;

prob2=normcdf(((iivector-X0_mid).*dX0)+.5*dX0)-normcdf(((iivector-X0_mid).*dX0)-.5*dX0);

%
plot((1:X0_max),const(1:X0_max),'g',(1:X0_max),const2(1:X0_max),'r',(1:X0_max),const3(1:X0_max),'b',(1:X0_max),const4(1:X0_max),'y')

% str=input('enter a key');

%

%
plot((1:X0_max),const(1:X0_max)./prob2(1:X0_max),'g',(1:X0_max),const2(1:X0_max)./prob2(1:X0_max),'r',(1:X0_max),const3(1:X0_max)./prob2(1:X0_max),'b',(1:X0_max),const4(1:X0_max)./prob2(1:X0_max),'y')

% str=input('enter a key');

for nn=1:T_index %Loop over time.

t=(nn)*dt;

t0=(nn-1)*dt;

prob=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)/(sqrt(t)*epsilon); %Probability in each SD Grid cell.

dt=t-t0;

dz_integral2=dz_integral2+...

epsilon.*dz_integral2.^gamma.*(sqrt(t)-sqrt(t0)).*(const./prob2)...

+1.0*epsilon.*gamma.*dz_integral2.^(gamma-1).*(epsilon.*dz_integral2.^(gamma)).*(t-t0)/2.0.*(((const2)-1))...

+epsilon.^3.*((gamma*(gamma-1).*dz_integral2.^(gamma-2+2*gamma))+gamma.^2.*dz_integral2.^(2*gamma-2+gamma)).*(t.^1.5-t0.^1.5)./6.*((const3)-const.*3)...

+0*epsilon.^4.*(gamma*(gamma-1)*(gamma-2).*dz_integral2.^(gamma-3+3*gamma)+4*gamma.^2*(gamma-1).*dz_integral2.^(gamma-2+gamma-1+2*gamma)+...

gamma.^3*dz_integral2.^(3*gamma-3+gamma)).*(t.^2-t0.^2)./24.*(const4-6*const2+3)+...

+.5*(epsilon.^3.*(gamma*(gamma-1).*dz_integral2.^(gamma-2+2*gamma))).*(t.^1.5/1.5-t0.^.5*t+.5*t0.^1.5/1.5).*(const);

% CONST0=epsilon.*Z_power1.*(sqrt(t)-sqrt(t0)).*(const./prob2);

% CONST1=epsilon.*dz_integral2.^gamma.*(sqrt(t)-sqrt(t0)).*(const./prob2);

% CONST2=epsilon.*gamma.*dz_integral2.^(gamma-1).*(epsilon.*dz_integral2.^(gamma)).*(t-t0)/2.0.*(((const2)-1));

%
CONST3=epsilon.^3.*((gamma*(gamma-1).*dz_integral2.^(gamma-2+2*gamma))+gamma.^2.*dz_integral2.^(2*gamma-2+gamma)).*(t.^1.5-t0.^1.5)./6.*((const3)-const.*3);

%
CONST4=epsilon.^4.*(gamma*(gamma-1)*(gamma-2).*dz_integral2.^(gamma-3+3*gamma)+4*gamma.^2*(gamma-1).*dz_integral2.^(gamma-2+gamma-1+2*gamma)+...

% gamma.^3*dz_integral2.^(3*gamma-3+gamma)).*(t.^2-t0.^2)./24.*(const4-6*const2+3);

%

% CONST4=.5*(epsilon.^3.*(gamma*(gamma-1).*dz_integral2.^(gamma-2+2*gamma))).*(t.^.5-t0.^.5).*sqrt(dt).*(const./prob2);

%

%plot(dz_integral2(1:X0_max),CONST0(1:X0_max),'k',dz_integral2(1:X0_max),CONST1(1:X0_max),'g',dz_integral2(1:X0_max),CONST2(1:X0_max),'r',dz_integral2(1:X0_max),CONST3(1:X0_max),'b',dz_integral2(1:X0_max),CONST4(1:X0_max),'y')

%str=input('enter a key');

%Naive brute force Monte carlo part follows. Since the steps are extremely

%short the monte carlo is uite close to the right density for most of the cases

%but may be off for a very small number of cases but it is a good initial

%check on our analytic density

Random1=randn(size(zz4));

RandTemp1=Random1.*sqrt(dt);

zz4 =zz4+zz4.^gamma.*RandTemp1*epsilon;

%dz_integral2(dz_integral2');

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

---

### #106 — Amin (Topic Author)
*July 31, 2016, 3:26 PM*

Here are some quick notes about the previous program.

The diffusion I am analytically simulating is dX=epsilon X^gamma dz(t).

The results are very encouraging. However the accuracy sharply deteriorates when significant mass of the diffusion gets
absorbed in zero. If diffusion reaches zero but significant mass does not get absorbed in zero, the results are still
very good. The reason is that we have divided the total density into standard deviation fractions. The most negative
standard deviations expand the fastest in negative direction and the most positive standard deviation expand fastest in
the positive direction at a rate proportional to standard deviation count and so on for intermediate values. When
significant mass is absorbed at zero, a large fraction  of the negative standard deviations is absorbed in zero but
remaining more positive standard deviation fractions continue to advance. By contrast, when we simulate by monte carlo,
the mass that is away from zero contains all standard deviations  and hence a method that mimicks Gaussian must contain
all standard deviations. Our analytic method works by advancing all standard deviations independently. When significant
standard deviation fractions are absorbed at zero, we must re-assign standard deviation fractions to all the probability
mass that has not reached zero so that it contains all standard deviation fractions. This is however not very simple or
straightforward to do and would require an algorithmic effort to do it. Another way to approach the problem would be to
reflect the negative standard deviation fractions that reach zero back into positive domain with negative amplitude that
cancels the increased amplitude due to lack of negative standard deviation. This will also require some effort and I
have not worked on it. Close vicinity of zero is not a problem for the algorithm. The only problem is that negative
standard deviation fractions that get absorbed in zero are lacked in the positive body/domain of the noise diffusion
where all standard deviation  fractions must be present for a perfectly Gaussian algorithm. Some way around it can be
worked out with a bit of effort.

After a few years (>1-4)the accuracy starts to decrease. Here I will like to mention that my estimate of mean is only
based on a rough summation so you will have to write your own integration routine on subdivisions each with different
width if you want perfect precision.

Here I would like to remind readers of my density correction technique that changes the density so as to make its mean
equal to a given number while keeping the mass equal to unity. I presented it in an old program in which I calculated
transition densities with Girsanov. I will find that out again and explain it here in a day or two. That routine can be
very handy for removing small biases in the density in a way that density moves in the desired direction and its mass
remains unity and average over the density becomes equal to the desired average. With the help of that small density
correction routine, you can freely use the above method even where large accuracy is required for the CEV noises where
significant mass is not absorbed at zero for short to medium time horizons. I will explain that routine here probably in
my next post.

---

### #107 — Amin (Topic Author)
*August 15, 2016, 11:16 AM*

I have been thinking if we can solve a general Pde by using techniques similar to stochastic calculus of standard
deviations. Yesterday, I had some ideas so I thought I would share them with friends here. I am extremely confident that
something can be developed based on these ideas. I have enough clarity here.

The idea here is to divide the PDE domain into small subdivisions. We set the change in PDE variable equal to zero as we
march into time. We take Laplace transform locally for each subdivision. From this local Laplace transform, we can find
the moments of movement in the PDE variable that can be used with some appropriate orthogonal polynomial to move and/or
expand the small subdivision so that some quantities related to PDE variable remains constant in time.

We try to find the local solution of a simple PDE of the form

$\frac{\partial f}{\partial t}=\mu (x)\frac{\partial f}{\partial x}+.5 \sigma ^2(x)\frac{\partial ^2f}{\partial x^2}$

At the start I would like to recall the integration technique I mentioned earlier in this thread.

$\int_a^b f(x) \, dx=f\left(x_0\right)\left(\int _a^{x_0}dx+\int _{x_0}^bdx\right)+\frac{\partial f}{\partial x}\left(x_0\right)\left(\int _a^{x_0}\int_a^{x_0} dx \, dx+\int _{x_0}^b\int_{x_0}^b dx \, dx\right)$

$+\frac{\partial ^2f}{\partial x^2}\left(x_0\right)\left(\int _a^{x_0}\int _a^{x_0}\int _a^{x_0}dxdxdx+\int _{x_0}^b\int _{x_0}^b\int _{x_0}^bdxdxdx\right)$

where $x_0=\frac{a+b}{2}$ is the middle of the subdivision

We would now show how to apply it to taking the Laplace transform of the second order term in the PDE

$\int _a^be^{-s x}\sigma ^2(x)\frac{\partial ^2f}{\partial x^2}dx=\left(e^{-s x}\sigma ^2(x)\frac{\partial ^2f}{\partial x^2}\right){}_{x=x_0} \left( \int_a^{x_0} dx +\int_{x_0}^b dx \right)$

$+\frac{\partial }{\partial x}\left(e^{-s x}\sigma ^2(x)\frac{\partial ^2f}{\partial x^2}\right) {}_{x=x_0\text{  }}\left(\int _a^{x_0}\int_a^{x_0} dx \, dx+\int _{x_0}^b\int_{x_0}^b dx \, dx\right)$

$+\frac{\partial ^2}{\partial x^2}\left(e^{-s x}\sigma ^2(x)\frac{\partial ^2f}{\partial x^2}\right) {}_{x=x_0\text{  }}\left(\int _a^{x_0}\int _a^{x_0}\int _a^{x_0}dxdxdx+\int _{x_0}^b\int _{x_0}^b\int _{x_0}^bdxdxdx\right)$
Equation(A)

coming back to the PDE

$\frac{\partial f}{\partial t}=\mu (x)\frac{\partial f}{\partial x}+.5 \sigma ^2(x)\frac{\partial ^2f}{\partial x^2}$

We equate the time derivative to zero so as to find the curve where PDE variable does not change as time passes.

$0=\mu (x)\frac{\partial f}{\partial x}+.5 \sigma ^2(x)\frac{\partial ^2f}{\partial x^2}$

Taking the Laplace transform of the above PDE

$F(s)=\int _a^b\left(\mu (x)\frac{\partial f}{\partial x}+.5 \sigma ^2(x)\frac{\partial ^2f}{\partial x^2}\right)e^{-s x}dx$

If the initial data is given in analytic form or we can find its appropriate numerical derivatives, the terms above can
be calculated by the integration technique shown at the start in Equation(A) and we will get an analytic expression in
Laplace transform variable 's'. This expression can be repeatedly differentiated and setting s=0, we can find the values
of various moments.

F(0) = mass

$\frac{\partial F}{\partial s}(0)=$ 1st moment.

$\frac{\partial ^2F}{\partial s^2}(0)=$ 2nd moment

These local moments can be turned into cumulants and used with some orthogonal polynomials to march the PDE into time
like I did in stochastic calculus of standard deviations. When PDE has growth/killing terms or forcing terms, we can
integrate them along the trajectory of PDE variable and add them to the result.

---

### #108 — Amin (Topic Author)
*August 24, 2016, 5:56 PM*

I started a new thread about proposal for a paid commercial project or open source code or collaboration with researchers at some good university related to research on this thread here. [viewtopic.php?f=3&t=100096](https://forum.wilmott.com/viewtopic.php?f=3&t=100096) You can see there are large advantages to this new technique and it can be used in limitless ways in derivatives pricing and risk management. If you would be interested, please email me at anan2999(at)yahoo.com

---

### #109 — Amin (Topic Author)
*September 20, 2016, 7:25 AM*

Those friends who downloaded and played with the program for simulation of CEV noise in post 105 would have noticed that
the program has good accuracy. I am now working on basis point accuracy in simulation of CEV noise.

Those researchers who extrapolated the method directly to SDEs with varaible drift would have realized that the method
lacks accuracy especially when there is strong mean reversion and other similar extreme variations in drift across the
density. The reason is that when drift is variable it affects every point in density differently and hence contributes
to local variance everywhere. To get accuracy in simulations of SDEs with variable (possibly mean reversion) drift, I
have introduced the concept of variance time that is local to every subdivision(different for each part of the density).
For example when mean reversion drift contracts a density, there is a negative contribution to variance different
everywhere locally for each subdivision and hence local variance time is smaller than actual time depending upon the
degree of local contraction in the density. With this new work, we will have great insights into how variable drift and
volatility shape and alter the variance of the distribution of an SDE together and their interactions.

Though I have been away from the work for some time, I have decided to write a formal paper that would be ready in a few
weeks. However, I will upload a program on this thread for the simulation of densities of SDEs with variable drift and
mean reversion in a week. The program will also calculate various stochastic integrals of SDEs with variable drift.

---

### #110 — Amin (Topic Author)
*October 1, 2016, 5:07 PM*

It may be a few more days to get a full-fledged program for mean reversion SDEs. The technique I have used worked
perfectly well for SDEs with non-state dependent(or constant) diffusion coefficient. It also works on most cases with
state dependent vol but I have to work out some of the things in a few days. There are other interesting results like
change of measure with Girsanov in our setting which is analogous to how we add a drift integral to dz(t) to get a
brownain motion on a different measure.

---

### #111 — Amin (Topic Author)
*October 4, 2016, 10:14 AM*

The work is done and I hope to post a matlab program with my reference explanation notes in latex tomorrow. I have tried
my program mostly on SDEs with mean reversion but I am sure it would be applicable to all SDEs with state dependent
drift and volatility.

---

### #112 — Amin (Topic Author)
*October 5, 2016, 8:46 AM*

Edit: Sorry, I have removed the program. There was some error in my stochastic integrals calculation. I will post a new
program tomorrow.

---

### #113 — Amin (Topic Author)
*October 5, 2016, 8:52 AM*

The above program is solution to mean reverting SDE   dX=kappa*(theta-X) dt + X^gamma dz(t). I will follow with detailed
notes in a few hours. I will also follow with another program with Girsanov simulation that is slightly more exact.

The code is really not optimized and there is a large room for speed optimization. I have still not done analysis of
contribution of integrals to accuracy and some of higher order integrals might be redundant.

IF you run the above code, the mean of mean reverting density will show on screen as dz_integral2_avg=.379867626XXX and
true mean as .38033XXXX.

Another caveat, many friends would notice that the integral denoted as dzdt in the current program that appears in
quadratic variation term is different from the one I used in quadratic variations of the older program in post 105. That
integral was wrong and was slightly contributing to errors and has to be replaced by dzdt term in the current program.

---

### #114 — Amin (Topic Author)
*October 7, 2016, 6:25 AM*

function [] = SDEXticsInfinitiTechnologiesCEVNoise05_Public( )

X0_max=800;%Total number of SD Fractions.End of the SD gird Index.

X0_mid=400+.5;%Mid of the SD Grid.Always Median of density.

X0_mid0=400;%Median-.5*dX0, so Grid index 401=Median+.5*dX0;Grid cells 400 and 401 are on both sides of median.

X0_start=1; %Start of the  SD Grid Index.

dX0=.0125;%Width of SD cells in terms of Standard Deviations.

iivector(1:X0_max)=(1:X0_max);

T_index=100*4;%

dt=.01/8.0;%Needs to be smaller if you want to start the density from close to zero.

epsilon=.3

gamma=1;

kappa=3.50;

theta=0.250;%.25;

z0=1;

dz_integral2(1:X0_max)=z0;

paths=100000; %No. of Paths for creation of Monte Carlo density by simulating z, F(z);

zz4(1:paths)=z0;

const=.398942*exp(-dX0^2.*(.25+(iivector-X0_mid).^2)).*(-exp(.5*dX0^2.*(-.5+(iivector-X0_mid)).^2)+exp(.5*dX0^2.*(.5+(iivector-X0_mid)).^2));;

const2=.398942*(dX0.*exp(-.5*dX0^2.*(.5+(iivector-X0_mid)).^2).*(-.5-(iivector-X0_mid))+...

    dX0.*exp(-.5*dX0^2.*(-.5+(iivector-X0_mid)).^2).*(-.5+(iivector-X0_mid))-...

    1.25331*erf(dX0.*(-.353553+.707107*(iivector-X0_mid)))+...

    1.25331*erf(dX0.*(.353553+.707107*(iivector-X0_mid))));

const3=.398942.^1*(exp(-.5*dX0^2.*(-.5+(iivector-X0_mid)).^2).*(2+(.5-(iivector-X0_mid)).^2.*dX0^2)+...

    exp(-.5*dX0^2.*(.5+(iivector-X0_mid)).^2).*(-2-(.5+(iivector-X0_mid)).^2*dX0^2));

%const4=.398942.^1*(exp(-.5*dX0^2.*(.5+(iivector-X0_mid)).^2).*dX0.*(-1.5-3*(iivector-X0_mid)+(-.5-(iivector-X0_mid)).^3.*dX0^2)+...

%    exp(-.5*dX0^2.*(-.5+(iivector-X0_mid)).^2).*dX0.*(-1.5+3*(iivector-X0_mid)+(-.5+(iivector-X0_mid)).^3.*dX0^2)-...

%    3.75994*erf(dX0.*(-.353553+.707107*(iivector-X0_mid)))+...

%    3.75994*erf(dX0.*(.353553+.707107*(iivector-X0_mid))));

prob2=normcdf(((iivector-X0_mid).*dX0)+.5*dX0)-normcdf(((iivector-X0_mid).*dX0)-.5*dX0);

tt(1:X0_max)=dt;%%tt is variance time

tt0(1:X0_max)=0;

ttOld(1:X0_max)=dt;

for nn=1:T_index %Loop over time.

    t=(nn)*dt;%t is true time.

    t0=(nn-1)*dt; %t-dt;

    dt=t-t0;

    prob=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)/(sqrt(t)*epsilon);

    vol0=epsilon.*dz_integral2.^gamma;

    vol02=vol0.*vol0;

    d_vol0_=epsilon*gamma*dz_integral2.^(gamma-1);

    %d2_vol0_=epsilon*gamma*(gamma-1)*dz_integral2.^(gamma-2);

    mu0=kappa*(theta-dz_integral2);

    d_mux0_=-kappa;

    d_mux0_mu0=-kappa*mu0;

    d_mux0_vol0=-kappa*vol0;

    d__mux0_mu0_mu0=kappa.^2.*mu0;

    d__mux0_mu0_mu0_mu0=-kappa.^3.*mu0;

    %d__mux0_mu0_vol0=kappa.^2.*vol0;

    %d__mux0_vol0_mu0=-kappa*d_vol0_.*mu0;

    d__mux0_vol0_vol0=-kappa*d_vol0_.*vol0;

    d_volx0_mu0=d_vol0_.*mu0;

    d_volx0_vol0=d_vol0_.*vol0;

   
%d__volx0_mu0_mu0=(kappa.*epsilon*gamma*(gamma-1)*theta*dz_integral2.^(gamma-2)-kappa*epsilon*gamma.^2*dz_integral2.^(gamma-1)).*mu0;

   
d__volx0_mu0_vol0=(kappa.*epsilon*gamma*(gamma-1)*theta*dz_integral2.^(gamma-2)-kappa*epsilon*gamma.^2*dz_integral2.^(gamma-1)).*vol0;

    d__vol0_vol0_mu0=epsilon.^2*gamma*(2*gamma-1).*dz_integral2.^(2*gamma-2).*mu0;

    d__vol0_vol0_vol0=epsilon.^2*gamma*(2*gamma-1).*dz_integral2.^(2*gamma-2).*vol0;

    dzdt=(sqrt(tt.^3/3-tt0.^3/3)-sqrt(tt.*tt0.^2-tt0.^3));

    dzdzdt=(sqrt(tt.^4.0/12-tt0.^4./12-tt.*tt0.^3/3+tt0.^4/3)-sqrt(tt.^2.*tt0.^2/2-tt0.^4/2-tt0.^3.*tt+tt0.^4));

    dz_integral2=dz_integral2+...

        mu0*dt+d_mux0_mu0*dt.^2/2+d__mux0_mu0_mu0*dt.^3/6+...

        d_mux0_vol0.*const.*(dzdt)+...

        d__mux0_vol0_vol0.*(const2-1)/sqrt(2).*(dzdzdt)+...

        vol0.*const./prob2.*(tt.^.5-tt0.^.5)+...

        d_volx0_mu0.*const.*(dzdt)+...

        d_volx0_vol0.*(const2-1).*(tt-tt0)./2.0+...

        d__volx0_mu0_vol0.*(const2-1)/sqrt(2).*(dzdzdt)+...

        d__vol0_vol0_mu0.*(const2-1)/sqrt(2).*(dzdzdt)+...

        d__vol0_vol0_vol0.*(const3-3*const).*(tt.^1.5-tt0.^1.5)/6.0+...

        .5*gamma*(gamma-1)*dz_integral2.^(gamma-2+2*gamma)*epsilon.^3.*const.*(dzdt);

        %Following block. Line 78-83 is varaince time adjustment.

       
 %dMuVarG=(mu0./vol0*dt+d_mux0_.*mu0./vol0.*dt.^2/2+d_mux0_.*(sqrt(tt.^3/3-0*tt0.*tt.^2+0*tt0.^2.*tt)-sqrt(tt0.^3/3))-...

         %  
 mu0./vol02.*d_vol0_.*mu0.*dt.^2/2-mu0./vol0.*d_vol0_.*(sqrt(tt.^3/3-tt0.*tt.^2+tt0.^2.*tt)-sqrt(tt0.^3/3)));

         dMuVarG=mu0./vol0*dt+0*d_mux0_.*mu0./vol0.*dt.^2/2+d_mux0_.*const.*(dzdt)-...

             0*mu0./vol02.*d_vol0_.*mu0.*dt.^2/2-mu0./vol02.*d_vol0_.*vol0.*const.*(dzdt);

         SqrtDiff=sqrt(tt)+...

             (dMuVarG-(.5*dMuVarG(X0_mid0)+.5*dMuVarG(X0_mid0+1)))./(const./prob2);%This line is variance time
adjustment.If it is zero, tt0=tt;

         tt0=SqrtDiff.^2;

         tt=tt0+dt;

         tt0_avg=sum(tt0)/X0_max

         tt_avg=sum(tt)/X0_max

         true_time=t

%     ttDiffOld=tt-(ttOld+dt);

%     ttOld=tt;

%     ttDiffOld

%     tt

     nn

    %Naive brute force Monte carlo part follows. Since the steps are extremely

    %short the monte carlo is quite close to the right density for most of the cases

    %but may be off for a very small number of cases but it is a good initial

    %check on our analytic density

    NNNN=1;

    for nnnn=1:NNNN

        Random1=randn(size(zz4));

       
zz4=theta+(zz4-theta).*exp(-kappa*dt/NNNN)+epsilon.*zz4.^gamma.*sqrt(.5/kappa.*(1-exp(-2*kappa*dt/NNNN))).*Random1;

        zz4(zz4');

end

---

### #115 — Amin (Topic Author)
*October 7, 2016, 6:37 AM*

I have posted new matlab program in post 114 above for simulation of  mean reverting SDE   dX=kappa*(theta-X) dt +
X^gamma dz(t). I will follow with detailed notes on the weekend. I will also follow with another program with Girsanov
simulation that is slightly more exact. The purpose of this part of work was to make the method work when there is state
dependent drift that strongly increases or decreases variance otherwise we could only use this new method mostly on
different forms of noise.

The above program needs a graphing matlab routine that I have posted on the thread earlier.

The issue of perfect accuracy still remains and I have very good ideas how to achieve basis point accuracy and I plan to
continue work towards that in next few weeks. The above program runtime also includes a very short stepping monte carlo
that is done to make a graphical comparison of monte carlo density with our density. The true run time will change even
further because the final plan is to have 40-50 subdivisions only as opposed to 800 subdivisions in the current program.

During Next week, I will release another version that will tackle problems at zero.

More about variance time correction in my notes that I plan to post on the weekend.

---

### #116 — Amin (Topic Author)
*October 10, 2016, 8:13 AM*

The logic of variance time adjustment is very simple. I have given a heuristic derivation. Without a drift, we have to
principal order the following equation for volatility term.

$\sigma (x)\text{dz}(t)=\sigma (x) n \Delta\text{X0} \left(\sqrt{t_1}- \sqrt{t_0}\right)$

We have to map the above integral (starting with principal order) to change in time. Obviously we see

$\sigma (x) n \Delta\text{X0} \left(\sqrt{t_1}- \sqrt{t_0}\right) \propto  \left(\sqrt{t_1}- \sqrt{t_0}\right)$

When we want to find the time adjustment for any other integral (integral of u(x) dt for example) for a very short time
period, we can directly apply the proportionality as

$\frac{\mu (x) \text{dt} }{\sigma (x) n \Delta\text{X0} \left(\sqrt{t_1}- \sqrt{t_0}\right)}\left(\sqrt{t_1}- \sqrt{t_0}\right)=\frac{\mu (x) \text{dt} }{\sigma (x) n \Delta\text{X0}}$

$=\frac{1}{n \Delta\text{X0}}\frac{\mu (x) \text{dt} }{\sigma (x) }$

which is the calculation for principal order. In my program$n \Delta\text{X0}$ is equal to const/prob2. Rest of the
calculations follow.

I had not done extremely thorough analysis of some of the integrals and I am afraid some integrals still have a slack
and have minor errors and I would be reviewing them in next few days. I plan to post a new program in 3-4 days which
will be definitive about all the integrals. I hope that some of the errors in probability density of mean reversion SDEs
in the current program would decrease in the new program.

---

### #117 — Amin (Topic Author)
*October 11, 2016, 2:55 PM*

Here is a rough analysis of why we have extra problems in the simulation of SDEs with strongly state dependent drift. I
also give suggestions for the solution to the problem. Consider a general SDE with state dependent drift

$\text{dX}=\mu (X) \text{dt} + \sigma (X) \text{dz}(t)$

Representing the density in the form of a normal density, we can write the exponential part without normalization as

$\text{EXP}\left[\frac{-.5\left(X-X_0-\int_{t_0}^{t_1} \mu (X) \, dt\right){}^2}{\int_{t_0}^{t_1} \sigma (X)^2 \, dt}\right]=\text{EXP}\left[-.5\frac{\left(X-X_0\right){}^2+\left(\int_{t_0}^{t_1} \mu (X) \, dt\right){}^2-2\left(X-X_0\right)\left(\int_{t_0}^{t_1} \mu (X) \, dt\right)}{\int_{t_0}^{t_1} \sigma (X)^2 \, dt}\right]$

The density appears as a square of sum of stochastic variables on the exponential in the normal. We know when we square
a sum of stochastic variables, We have to account for covariances in addition to individual variances. When there is a
drift, the analysis of these covariances is very important since these introduce extra terms in simulation and these
extra terms are not directly known from the SDE. To analyze covariances, we look at the volatility of various parts of
the last term on exponential

$\left(X-X_0\right)\left(\int_{t_0}^{t_1} \mu (X) \, dt\right)$

Looking at vols of each part, the highest order volatility integral of  first part

$\text{Vol}\left(X-X_0\right)=\int_{t_0}^{t_1} \sigma (X) \, dz(t)$

and volatility integral of the second part is given as

$\text{Vol}\left(\int_{t_0}^{t_1} \mu (X) \, dt\right)=\int dt\int _{t_0}^{t_1}\frac{d \mu (X)}{\text{dX}}\sigma (X)dz(t)$

We see right away that dz(t) and dz(t) terms in the two Vol terms should correlate to dt. We can see that there is
covariance between dz(t) and dz(t) dt terms and their covariance is of the order of dt*dt. We can see that a dt^2 term
in the square on normal translates roughly into a dt term in SDE dynamics which is almost never negligible to be
neglected.  heuristically, we can say that the covariance is roughly of the order of

$\left.\text{Cov}\left(\left(X-X_0\right),\left(\int_{t_0}^{t_1} \mu (X) \, dt\right)\right)=\int dt\int _{t_0}^{t_1}\frac{d \mu (X)}{\text{dX}}\sigma ^2(X)dt\right)$

This term cannot be safely neglected in either monte carlo or other types of simulations of the SDE with state dependent
drift. Since we never knew and always neglected this term in our simulation of density of mean reversion SDEs, we were
getting rough results. I will be posting a new program on Wilmott with careful analysis of this covaraince term and much
better simulation of mean reversion and other SDEs in a few days. I have not done any analysis but I do believe that
this term has to be added to monte carlo of nonlinear highly state dependent SDEs to get accurate results. So when we
are simulating an SDE with strongly state dependent drift, we have to know that extra terms are introduced in simulation
because of the covariance between normal state dependent drift and other terms and these covariance terms are not known
from the SDE directly.

---

### #118 — Amin (Topic Author)
*October 12, 2016, 7:32 AM*

Here is a better, more clear and corrected re-statement of what I described in the earlier post. The right statement is
that total variance of a system of two stochastic variables includes their covariance in addition to their individual
variances. In my simulation of density without any random numbers, I had not included covariance term that is of order
dt in context of standard deviations and this was adding to inaccuracy. However, in monte carlo we simulate using random
draws of normal so most covariances would automatically be accounted and my statement might have no relevance to
accurate monte carlo which accounts properly for individual variances and correlations.

---

### #119 — Amin (Topic Author)
*October 13, 2016, 12:23 PM*

I will be posting a new program on coming Monday for density simulation of mean reverting SDEs. I have much better
accuracy now due to new and improved second order accurate variance time adjustment.

Edit: Sorry as it will take a few more days since I have to take care of some numerical instabilities.

---

### #120 — Amin (Topic Author)
*October 21, 2016, 6:27 PM*

I improved the algorithm for variance time adjustment but there are still substantial problems in the algorithm. I am
working on a better algorithm that takes some inspiration from Girsanov. For a diffusion

dX(t)=mu(X(t)) dt + sigma(X(t)) dz(t)

Earlier I was using a zero mean brownian motion as the base that was evolving in time which was used for calculation of
change in the values of hermite polynomials in each density subdivision and these constants were used for the
calculation of new density.

The improved strategy goes like this. I am using a normal y with constant variance but variable drift  where z is
standard brownian motion as        dy(t)=dz(t)+mu(X(t))/sigma(X(t))dt. This is again another normal with a different
mean and different variance(as compared to standard brownian motion) since volatility is not variable and state
dependent drift makes a variance change. We can calculate this very easily.

And then I calculate integrated constants as difference between hermite polynomials based on change in y after and
before each time simulation interval. Then I use the equation as  dX(t)=sigma(X(t))dy(t) where I have used
dy(t)=dz(t)+mu(X(t))/sigma(X(t))dt. I really think this two stage evolution would help calculate all the joint effects
of change in drift and volatility with precision without significant overhead of calculations.

I hope to have results and a program ready sometime next week.

---

### #121 — Amin (Topic Author)
*October 24, 2016, 5:31 PM*

In this post I try to heuristicaly relate standard deviations calculus method of evolution of density of a stochastic
differential equation to Fokker Planck equation. For the sake of simplicity I do not consider drift and only consider a
diffusion with state dependent volatility and then heuristically relate new method to the Fokker Planck PDE. Let us
consider the diffusion

$\text{dX}(t)=\sigma (X(t))\text{dz}(t) $  Equation 1.

The corresponding Fokker Planck goes as

$\frac{\partial p}{\partial t}=.5\frac{\partial ^2\left(\sigma ^2(x)p\right)}{\partial x^2}$

Expanding the derivative on the right, we get

$\frac{\partial p}{\partial t}=.5\sigma ^2(x)\frac{\partial ^2p}{\partial x^2}+2\sigma (x)\frac{\partial \sigma (x)}{\partial x}\frac{\partial p}{\partial x}+(\left(\frac{\partial \sigma (x)}{\partial x}\right)^2+\sigma (x)\frac{\partial ^2\sigma (x)}{\partial x^2})p$
Equation (2)

In our method, we take local values of volatility$\sigma\text{(x)}$ in each subdivision. We start with the highest
derivative which is the second order derivative in our case and find its local solution as a brownian motion density
which is again scaled by local value of volatility$\sigma\text{(x)}$ Let us write this solution as f(x) which indicates
normal as brownian motion density here. Within each subdivision, the density will evolve according to normal brownian
motion evolution scaled by local value of volatility. We will take expectations of other terms on right hand side with
respect to This brownian motion density.

Taking the second term on right hand side of equation 2. Since we divide the density into large number of small
subdivisions to find a local solution in each of them, we have to write for the first derivative of probability within
each subdivision with boundaries$x_a$ and$x_b$

$\frac{\partial p\left(x_b\right)}{\partial x}-\frac{\partial p\left(x_a\right)}{\partial x}=\frac{\partial f\left(x_b\right)}{\partial x}-\frac{\partial f\left(x_a\right)}{\partial x}=\int_{x_a}^{x_b} \frac{\partial ^2f(x)}{\partial x^2} \, dx$
Equation (3)

Taking the last term and expanding further

$\int_{x_a}^{x_b} \frac{\partial ^2f(x)}{\partial x^2} \, dx=\int _{x_a}^{x_b}\left.(\left.\frac{\partial ^2f(x)}{\partial x^2}\right/f(x) \right)f(x)dx=E [\text{H2}(x)]$
Equation (4)

where the last term denotes expectation of second hermite polynomial over the subdivision heuristically recognized as
expectation of the ratio of the second derivative of the density with respect to the density itself within the
subdivision boundaries. I have written equations without normalizations and related coefficients.

Now considering the last term on right hand side of equation 2, we have for probability mass within each subdivision
with boundaries$x_a$ and$x_b$

$p\left(x_b\right)-p\left(x_a\right)=f\left(x_b\right)-f\left(x_a\right)=\int_{x_a}^{x_b} \frac{\partial f(x)}{\partial x} \, dx$
Equation(5)

Taking the last term and expanding further

$\int_{x_a}^{x_b} \frac{\partial f(x)}{\partial x} \, dx=\int _{x_a}^{x_b}\left.(\left.\frac{\partial f(x)}{\partial x}\right/f(x) \right)f(x)dx=E [\text{H1}(x)]$
Equation(6)

where the last term denotes expectation of first order hermite polynomial over the subdivision heuristically recognized
as expectation of the ratio of the first derivative of the density of brownain motion with respect to the density itself
within the subdivision boundaries.

Our method now heuristically goes like this. We start with the highest derivative which is the second order derivative
in our case and find its local solution as a brownian motion density scaled by local value of variance$\sigma\text{(x)}$

We expand the density on standard deviations just like normal brownian motion density scaled locally in each subdivision
by the coefficient of the second order derivative. Then we add the following terms. The first term goes as

$2\sigma \left(x\left(t_0\right)\right)\frac{\partial \sigma \left(x\left(t_0\right)\right)}{\partial x}\int _{t_0}^{t_1}\frac{\partial p}{\partial x}dt$

$=2\sigma \left(x\left(t_0\right)\right)\frac{\partial \sigma \left(x\left(t_0\right)\right)}{\partial x}\int _{t_0}^{t_1}\int _{x_a}^{x_b}(\left.\frac{\partial ^2f(x)}{\partial x^2}\right/f(x) )f(x)dxdt$

$=2\sigma \left(x\left(t_0\right)\right)\frac{\partial \sigma \left(x\left(t_0\right)\right)}{\partial x}\int _{t_0}^{t_1}E[\text{H2}(x)]dt$
Equation(7)

The second term we add goes as

$(\left(\frac{\partial \sigma \left(x\left(t_0\right)\right)}{\partial x}\right){}^2+\sigma \left(x\left(t_0\right)\right)\frac{\partial ^2\sigma \left(x\left(t_0\right)\right)}{\partial x^2})\int_{t_0}^{t_1} p \, dt$

$=(\left(\frac{\partial \sigma \left(x\left(t_0\right)\right)}{\partial x}\right){}^2+\sigma \left(x\left(t_0\right)\right)\frac{\partial ^2\sigma \left(x\left(t_0\right)\right)}{\partial x^2})\int _{t_0}^{t_1}\int _{x_a}^{x_b}(\left.\frac{\partial f(x)}{\partial x}\right/f(x) )f(x)dxdt$

$=(\left(\frac{\partial \sigma \left(x\left(t_0\right)\right)}{\partial x}\right){}^2+\sigma \left(x\left(t_0\right)\right)\frac{\partial ^2\sigma \left(x\left(t_0\right)\right)}{\partial x^2})\int _{t_0}^{t_1}E[\text{H1}(x)]dt$
Equation(8)

Sorry for ambiguity but Here I want to indicate that in equation 8(and similarly for equation 7), instead of integral

$\int _{t_0}^{t_1}E[\text{H1}(x)]dt$

I have used the following solution

$E[\text{H1}(x(t_1))]-E[\text{H1}(x(t_0))]$

My constants in the programs I uploaded were based on difference in the expectations of hermite polynomials associated
with brownian motion for evolution from each simulation interval starting time to simulation interval end time
associated with each probability mass subdivision.

I will like to mention that this second term as given by equation (8) was missing from the solution of CEV density
program I posted on this thread earlier and that is why we probably had to take very small steps to maintain accuracy.

It will be a few days before I post a detailed program for SDEs with drift. I will also be posting a new revised matlab
program for CEV diffusions within a few days.

---

### #122 — Amin (Topic Author)
*October 26, 2016, 9:25 AM*

I do not know if I had extended heuristics too far in the previous post in search for the right solution but we all know
that for a general parabolic equation of the Fokker Planck Form, the general solution that exists for constant
coefficients is well known.

According to book by Andrei D. Polyanin and Vladimir E. Nazaiknskii p. 284-285, for constant coefficients PDE of the
form

$\frac{\partial p}{\partial t}=A\frac{\partial ^2p}{\partial x^2}+B\frac{\partial p}{\partial x}+C p$

The above constant coefficients PDE takes the fundamental solution

$p(x,t)=\frac{1}{2\sqrt{\pi  A t}}\text{Exp}\left[-\frac{(x + B t) }{4 A t }+C t\right]$

We could replace state dependent coefficients instead of constant coefficients and the solution would be applicable in
the immediate neighborhood where we calculated the values of state dependent coefficients.

$A=.5\sigma ^2(x)$

$B=2\sigma (x)\frac{\partial \sigma (x)}{\partial x}$

$C=(\left(\frac{\partial \sigma (x)}{\partial x}\right)^2+\sigma (x)\frac{\partial ^2\sigma (x)}{\partial x^2})$

---

### #123 — Amin (Topic Author)
*October 31, 2016, 10:07 AM*

The Hermite polynomials are given by the exponential generating function

$\text{Exp}\left[z t -.5 t^2\right]=\sum _{n=0}^{\infty } \text{He}_n(z) \frac{t^n}{n!}$

By comparison with the exponential generating function, Girsanov exponential finds a direct expansion in terms of
hermite polynomials.

Consider a general SDE with state dependent drift.

$\text{dX}=\mu (x) \text{dt} + \sigma (x) \text{dz}(t)$

The Girsanov exponential associated with the SDE is given as

$G(X)=\text{Exp}\left[\frac{\mu (x)}{\sigma (x)}\text{dz}(t)-.5\left(\frac{\mu (x)}{\sigma (x)}\right)^2\text{dt}\right]$

and can be directly expanded everywhere locally in the form of hermite polynomials. This is the right way in order to
get precise dynamics when drift is added to the SDE. In order to get the density of the above SDE with state dependent
drift, when we expand the product of density without drift and Girsanov exponential, we get the original density without
drift(zero order polynomial) and local expectations of higher order hermite polynomials based on Girsanov exponential.

---

### #124 — Amin (Topic Author)
*November 17, 2016, 8:46 AM*

Tomorrow, I will be posting my paper on SSRN for solution of initial value problems related to ODEs of first, second and
higher orders. The method is extremely general and requires no restrictions on linearity of coefficients or most of the
other special restrictions. The solution method is completely based on my method of iterated integrals that I proposed
on this thread earlier. In the paper, I have tried to explain the method with a good range of examples.

I will give the link tomorrow.

---

### #125 — list1
*November 17, 2016, 5:13 PM*

Amin, let start with Sun Apr 17 2016 12,24 pm message. In eq(1) and (3) you used the same notation x ( t ) though they
are different and next it might confuse which x ( t ) do you mean. Whether the in (2) , (3) ... mu and sigma are with
freezed x or not. If my feeling correct you talk about eq with frozen coefficients which defines gaussian x ( t ).
Frozen coefficients define construction on the first small interval. x ( t ) is gaussian process which mean and variance
easy to calculate at each moment t. I did not see next step from$[ 0 , t _1 ] $ to$ [  t _1 , t_2 ] $ and so on Then we
probably need to go closer to the solution of (1) from discrete time ?

---

### #126 — Amin (Topic Author)
*November 17, 2016, 9:52 PM*

List, I will answer your question on the weekend.

---

### #127 — Amin (Topic Author)
*November 17, 2016, 9:53 PM*

Here is a simple description of method of iterated integrals as I have written in my paper coming in a day.

Ordinary differential equations define a differential relationship which is usually a low order derivative between the
independent variable and the dependent variable. This differential relationship is usually a function that can possibly
take a large number of derivatives with respect to both variables. In an initial value problem, in general, when we take
step in independent variable, this differential relationship has to be integrated along the independent variable to find
the change in the dependent variable and a perfect integration would require the knowledge of higher total derivatives
of differential function with respect to independent variable. Previously, in context of SDEs and ODEs there were no
general ways to relate higher total derivatives of the differential function to the variation of the independent
variable and many times order of the differential function/equation would limit the useful knowledge when integrating
the differential function/equation with respect to the independent variable. In  method of iterated integrals, we add
consecutive terms in which we differentiate the previous total derivative with respect to dependent variable and convert
 it to higher derivative with respect to the independent variable through chain rule derivative usually described by the
differential function/equation itself. Since we do not include derivatives of the differential function with respect to
independent variable,, by saying ‘total derivative’, the purpose is to merely emphasize the indirect dependence of
differential equation/function on independent variable through chain rule linking the derivatives of differential
equation due to dependent variable into variation due to independent variable. In fact, mostly independent variable
could be directly integrated in the differential equation/function and we would not need derivatives of differential
equation with respect to independent variable. However if this direct integration with respect to independent variable
could not be carried out, we would in fact need total derivatives in the formal sense to integrate the differential
function.

Many people would like to think of method of iterated integrals as a dependent variable analog of Taylor series where
moments of variation in the independent variable are mapped on the change in dependent variable through appropriately
calculated higher derivatives of the differential function. Each iterated integral term in the series calculates the
correction of one higher order derivative to the integral of differential function as the independent variable moves
from one point to another.

---

### #128 — Amin (Topic Author)
*November 19, 2016, 8:54 AM*

Here you can download my paper. [https://papers.ssrn.com/sol3/papers.cfm ... id=2872598](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598) I will improve it over next few days but interesting how so many second order ODEs can be so easily solved.

---

### #129 — Amin (Topic Author)
*November 20, 2016, 2:26 AM*

It is interesting that SSRN screen I see for my paper shows me exactly my activity. I have given the link on several
other places but there is not even a single abstract view other than my activity. Are they routing me a different web
site and a different web site for others. I do not know but not even a single abstract view by any one else makes me
feel something is very wrong.

---

### #130 — Amin (Topic Author)
*November 20, 2016, 2:59 AM*

I have written to SSRN to ensure the sanctity of my research. Let us see what they got to say. This is not a frivolous
issue.

---

### #131 — Amin (Topic Author)
*November 21, 2016, 7:20 AM*

In the next post I am copying page 12 to page 15 of my paper. It is about the solution to second order ODEs. Let us hope
it goes to the readers in the same exact format as I am writing.

---

### #132 — Amin (Topic Author)
*November 21, 2016, 8:17 AM*

Page 12 starts.

Solution to Second Order ODEs

We find the solution to General second order Ordinary Differential Equations given as

$\frac{d^2y}{dt^2}=f\left(t,y,y'\right)$,   $t\geq 0$,        $y\left(t_0\right)=y_0$,    $y'\left(t_0\right)=y'_0$

Equation (18)

We suppose that function f in the equation above is sufficiently well behaved and satisfies the usual regularity
conditions.

Integrating Equation (18), we get the solution

$y(t)=y\left(t_0\right)+y'\left(t_0\right)\left(t-t_0\right)$

$+\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y(\tau ),y'(\tau )\right)d\tau ds$

Equation (19)

The differential function in the second order ODE takes three arguments in general. In a direct integration, the
independent variable would likely get integrated but we have to take partial derivatives of differeential function with
respect to both dependent arguments and convert them to indirect derivatives with respect to independent variable using
the chain rule and given initial values of the arguments and the differential function/equation itself. We would call
the sum of these indirect derivatives on nth order as indirect total derivative of (that) nth order order.

Here we expand the double integral in Equation (19) by terms required to take one indirect total derivative

Page 13 starts

$\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y(\tau ),y'(\tau )\right)d\tau ds$

$=\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y\left(t_0\right),y'\left(t_0\right)\right)d\tau ds$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]\frac{dy\left(u,y,y'\right)}{dt} dud\tau ds\right.$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]\frac{dy'\left(u,y,y'\right)}{dt} dud\tau ds$

Equation (20)

The above expression would be exact if we could somehow perfectly evaluate it(third order integrals in the eqution). In
general, however, we substitute the initial values of dependent arguments and take the expansion to next level by taking
another indirect total derivative. Whenever we take the expansion to next indirect total derivative, we have to find
partial derivatives of previous total derivative expression with respect to all dependent variables and convert them to
indirect derivative using the chain rule.

Using Initial values$\frac{dy}{dt}=y'\left(t_0\right)=y'_0$ and
$\frac{dy'}{dt}=\frac{d^2y}{dt^2}=f\left(t_0,y_0,y'_0\right)$

Substituring above initial values and also expanding one level further, we get the expression

$\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y(\tau ),y'(\tau )\right)d\tau ds$

$=\int _{t_0}^t\int _{t_0}^sf\left(t_0,y_0,y'_0\right)d\tau ds$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0 dud\tau ds$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right) dud\tau ds$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]\frac{dy(u)}{du}\right.$

$\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]\frac{dy'(u)}{du}\right]\frac{dy(v)}{dv}dv dud\tau ds$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]\frac{dy(u)}{du}\right.$

$\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]\frac{dy'(u)}{du}\right]\frac{dy'(v)}{dv}dv dud\tau ds$

 Equation (21)

Page 14 starts

 Using Equations 19, 20 and 21, we can write the first few terms of the general solution of the 2nd order differential
equations problem as

$y(t)=y\left(t_0\right)+y'\left(t_0\right)\left(t-t_0\right)$

$+\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y\left(t_0\right),y'\left(t_0\right)\right)d\tau ds$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0 \right.$

$\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right) \right]dud\tau ds$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0\right.\right.$

$+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)f\left(u,y_0,y'_0\right)\right]y'_0$

$\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]y'_0\right.$

$\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]f\left(u,y_0,y'_0\right)\right]$

$\left.f\left(v,y_0,y'_0\right)\right]dv dud\tau ds$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)f\left(u,y_0,y'_0\right)\right]y'_0\right.\right.$

$\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]y'_0\right.$

$\left.\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]y_0$

$+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0\right.\right.$

$+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)f\left(u,y_0,y'_0\right)\right]y'_0$

$+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]y'_0\right.$

$\left.\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]$

$\left.f\left(w,y_0,y'_0\right)\right]dwdv dud\tau ds$

Equation (22)

Page 15 Starts

Example 4

Consider the 2nd order initial value problem given as

$y''=f\left(\tau ,y(\tau ),y'(\tau )\right)=-2y'-y$,       $y'(0)=y'_0=1$  $y(0)=y_0=1$

using Equation (22), we calculate the values of the coefficients in terms of initial values as

$\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y\left(t_0\right),y'\left(t_0\right)\right)d\tau ds$

$=\left(-2y'_0-y_0\right)\frac{ t^2}{2}=-3\frac{ t^2}{2}$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0 +\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right) \right]dud\tau ds$

$=-y_0\frac{ t^3}{6}-2\left(-2y'_0-y_0\right)\frac{ t^3}{6}=4\frac{ t^3}{3}$

$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)f\left(u,y_0,y'_0\right)\right]y'_0\right.\right.$

$\left.+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]dv dud\tau ds$

$=0+2y'_0\frac{ t^4}{24}-\left(-2y'_0-y_0\right)\frac{ t^4}{24}+4\left(-2y'_0-y_0\right)\frac{ t^4}{24}=-7\frac{ t^4}{24}$

We get the new solution as

$y(t)=1+t-3\frac{ t^2}{2}+4\frac{ t^3}{3}-7\frac{ t^4}{24}+\text{...}$

---

### #133 — Paul
*November 21, 2016, 8:35 AM*

Why are you taking many many pages to do something that can be explained in two sentences and done in practice almost in
your head?

P

---

### #134 — outrun
*November 21, 2016, 8:59 AM*

>  Let us hope it goes to the readers in the same exact format as I am writing.
are you copying the content of the paper here because nobody is downloading it and you think someone is preventing
people to do so? I can download it if you want.

I see no reason why it would be in a different format to me as a reader compared to you as a writer. You can always fix
typos by editing your post.

---

### #135 — Amin (Topic Author)
*November 21, 2016, 9:05 AM*

For Paul,

I am still editing the equations when I saw your post. But I really do not know why nobody ever did it before and never
used it before. It make non-linear 2nd order and higher ODEs a joke in simple algebra and calculus.

.

I will like you to explain that.

When somebody has done it, it becomes simple for everyone. Besides, not everybody is as smart as you are, so let me
explain it in detail.

---

### #136 — Cuchulainn
*November 21, 2016, 9:29 AM*

I get the impression that OP is ignorant of the theoretical and numerical aspects of ODEs which were developed by Runge,
Kutta and many others. Your approach is cumbersome. The  approach is over-engineered.

The standard way is to write the 2nd order ODE as a 2X2 systems of 1st order ODEs in y and v == dy/dt to get

$dw/dt = Aw, w = (y,v)$ and $A$ is a 2.x2 matrix. The solution is

$w(t) = exp(At)$ (exponential of a matrix, now where did we see that before?). And you can compute it almost by hand.

*But I really do not know why nobody ever did it before and never used it before.*

Yes, they have.I would advise learning ODE theory instead of looks like an osmotic process To be frank it is would I
expect in 1st undergrad maths..

On positive side, the results will be more elegant and compact if you take this approach. It can even be directly
plugged into C++.

---

### #137 — Amin (Topic Author)
*November 21, 2016, 9:35 AM*

Cuch, please. I did not expect such an ignorant post from you. I gave a simple linear example in order to understand and
compare. The paper has more examples. My method will run, where your Runge-Kutta becomes totally hopeless.

---

### #138 — Cuchulainn
*November 21, 2016, 9:39 AM*

Amin,

'Which part of my post was ignorant? I played the ball, not the man.

*My method will run, where your Runge-Kutta becomes totally hopeless.*

I said Runge, Kutta and others (note the komma!), not Runge-Kutta. Subtle difference. I was not necessarily talking
numeric. I think you missed the point of my solution.

---

### #139 — outrun
*November 21, 2016, 9:39 AM*

Lol "RK4 is totale hopeless", how can you say that if you haven't even heard about it? And was is your region of
stability then?

---

### #140 — Amin (Topic Author)
*November 21, 2016, 9:40 AM*

I want to warn there are some minor errors in the Equation(22) about bracket placement. I continued to try to fix it but
gave up after external controls on my computer made me helpless and did not let me fix it. As Paul made the observation,
the method is extremely simple and most mathematicians would easily follow it. More in the paper.

---

### #141 — Cuchulainn
*November 21, 2016, 10:14 AM*

> I want to warn there are some minor errors in the Equation(22) about bracket placement. I continued to try to fix it
but gave up after external controls on my computer made me helpless and did not let me fix it. As Paul made the
observation, the method is extremely simple and most mathematicians would easily follow it. More in the paper.
I checked Example 4 solution but I don't get the answer that is claimed.

BTW Variation of parameters not good?

https://en.wikipedia.org/wiki/Variation_of_parameters

---

### #142 — outrun
*November 21, 2016, 10:19 AM*

Here is a plot of stability regions of classical methods. Do you understand this?

![Image](http://vmm.math.uci.edu/ODEandCM/ii/absolute_stability_regions.png)

---

### #143 — Paul
*November 21, 2016, 10:45 AM*

Isn't this all first-year undergrad stuff?

P

---

### #144 — Cuchulainn
*November 21, 2016, 12:53 PM*

> Lol "RK4 is totale hopeless", how can you say that if you haven't even heard about it? And was is your region of
stability then?
Indeed.

Let's put things straight RK is extremely **robust. **But it can be a bit slow.

---

### #145 — Amin (Topic Author)
*November 21, 2016, 4:59 PM*

Please do not distort what I said. I never said RK is always hopeless. I said where RK would be hopeless, my method
would still work great. RK and other good methods are not adapted to specific ODEs especially when ODEs are
non-linear.For Non-linear ODEs, you would continue Newton iterations forever for any stable implicit method but my
method would be explicit, robust and fast and will usually require only high school calculus and algebra. All these
iterated integrals can be very easily solved though in some cases you might need symbolic computation packages but for
every given ODE, you will get an explicit series solution in terms of arbitrary initial values and independent variable
once for all that would usually be lightning fast as opposed to forever long Newton loops in RK for every step. You
could make effort to find general series solution of any ODE and then use it forever.

As Paul said most of the stuff you guys are discussing can be found in undergraduate books. Only thing you will not find
is my method and I challenge everyone to give a reference to any book, paper or some other academic work that has
presented it before.

---

### #146 — Amin (Topic Author)
*November 21, 2016, 5:08 PM*

In my paper I have given an example 5 on page 16 for 2nd order non-linear ODEs that I have not copied in my first post
today and the example shows how 2nd order non-linear ODEs become so extremely simple to solve by the new method while
none of the classical method can easily solve that ODE.

---

### #147 — Cuchulainn
*November 21, 2016, 9:35 PM*

> Page 12 starts.
>
> Solution to Second Order ODEs
>
>
>
> We find the solution to General second order Ordinary Differential Equations given as
>
> $\frac{d^2y}{dt^2}=f\left(t,y,y'\right)$,   $t\geq 0$,        $y\left(t_0\right)=y_0$,    $y'\left(t_0\right)=y'_0$
>
> Equation (18)
>
> We suppose that function f in the equation above is sufficiently well behaved and satisfies the usual regularity
conditions.
>
> Integrating Equation (18), we get the solution
>
> $y(t)=y\left(t_0\right)+y'\left(t_0\right)\left(t-t_0\right)$
>
> $+\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y(\tau ),y'(\tau )\right)d\tau ds$
>
> Equation (19)
>
> The differential function in the second order ODE takes three arguments in general. In a direct integration, the
independent variable would likely get integrated but we have to take partial derivatives of differeential function with
respect to both dependent arguments and convert them to indirect derivatives with respect to independent variable using
the chain rule and given initial values of the arguments and the differential function/equation itself. We would call
the sum of these indirect derivatives on nth order as indirect total derivative of (that) nth order order.
>
>
>
> Here we expand the double integral in Equation (19) by terms required to take one indirect total derivative
>
>
>
> Page 13 starts
>
> $\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y(\tau ),y'(\tau )\right)d\tau ds$
>
> $=\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y\left(t_0\right),y'\left(t_0\right)\right)d\tau ds$
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]\frac{dy\left(u,y,y'\right)}{dt} dud\tau ds\right.$
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]\frac{dy'\left(u,y,y'\right)}{dt} dud\tau ds$
>
> Equation (20)
>
> The above expression would be exact if we could somehow perfectly evaluate it(third order integrals in the eqution).
In general, however, we substitute the initial values of dependent arguments and take the expansion to next level by
taking another indirect total derivative. Whenever we take the expansion to next indirect total derivative, we have to
find partial derivatives of previous total derivative expression with respect to all dependent variables and convert
them to indirect derivative using the chain rule.
>
> Using Initial values$\frac{dy}{dt}=y'\left(t_0\right)=y'_0$ and
$\frac{dy'}{dt}=\frac{d^2y}{dt^2}=f\left(t_0,y_0,y'_0\right)$
>
>
>
> Substituring above initial values and also expanding one level further, we get the expression
>
>
>
> $\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y(\tau ),y'(\tau )\right)d\tau ds$
>
> $=\int _{t_0}^t\int _{t_0}^sf\left(t_0,y_0,y'_0\right)d\tau ds$
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0 dud\tau ds$
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right) dud\tau ds$
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]\frac{dy(u)}{du}\right.$
>
>
$\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]\frac{dy'(u)}{du}\right]\frac{dy(v)}{dv}dv dud\tau ds$
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]\frac{dy(u)}{du}\right.$
>
>
$\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]\frac{dy'(u)}{du}\right]\frac{dy'(v)}{dv}dv dud\tau ds$
>
>  Equation (21)
>
>
>
> Page 14 starts
>
>  Using Equations 19, 20 and 21, we can write the first few terms of the general solution of the 2nd order differential
equations problem as
>
>
>
> $y(t)=y\left(t_0\right)+y'\left(t_0\right)\left(t-t_0\right)$
>
> $+\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y\left(t_0\right),y'\left(t_0\right)\right)d\tau ds$
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0 \right.$
>
>
$\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right) \right]dud\tau ds$
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0\right.\right.$
>
> $+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)f\left(u,y_0,y'_0\right)\right]y'_0$
>
> $\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]y'_0\right.$
>
> $\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]f\left(u,y_0,y'_0\right)\right]$
>
> $\left.f\left(v,y_0,y'_0\right)\right]dv dud\tau ds$
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)f\left(u,y_0,y'_0\right)\right]y'_0\right.\right.$
>
> $\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]y'_0\right.$
>
>
$\left.\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]y_0$
>
>
$+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0\right.\right.$
>
> $+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)f\left(u,y_0,y'_0\right)\right]y'_0$
>
> $+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]y'_0\right.$
>
>
$\left.\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]$
>
> $\left.f\left(w,y_0,y'_0\right)\right]dwdv dud\tau ds$
>
>
>
> Equation (22)
>
>
>
> Page 15 Starts
>
> Example 4
>
> Consider the 2nd order initial value problem given as
>
>
>
> $y''=f\left(\tau ,y(\tau ),y'(\tau )\right)=-2y'-y$,       $y'(0)=y'_0=1$  $y(0)=y_0=1$
>
>
>
> using Equation (22), we calculate the values of the coefficients in terms of initial values as
>
> $\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y\left(t_0\right),y'\left(t_0\right)\right)d\tau ds$
>
> $=\left(-2y'_0-y_0\right)\frac{ t^2}{2}=-3\frac{ t^2}{2}$
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0 +\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right) \right]dud\tau ds$
>
> $=-y_0\frac{ t^3}{6}-2\left(-2y'_0-y_0\right)\frac{ t^3}{6}=4\frac{ t^3}{3}$
>
>
>
>
$+\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)f\left(u,y_0,y'_0\right)\right]y'_0\right.\right.$
>
>
$\left.+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y,y'\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y,y'\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]dv dud\tau ds$
>
>
$=0+2y'_0\frac{ t^4}{24}-\left(-2y'_0-y_0\right)\frac{ t^4}{24}+4\left(-2y'_0-y_0\right)\frac{ t^4}{24}=-7\frac{ t^4}{24}$
>
>
>
> We get the new solution as
>
>
>
> $y(t)=1+t-3\frac{ t^2}{2}+4\frac{ t^3}{3}-7\frac{ t^4}{24}+\text{...}$
For the linear test case I get $y(t) = (1 - t) e^{-t}$.

You see it satisfies bespoke IVP.

---

### #148 — Cuchulainn
*November 21, 2016, 9:47 PM*

*All these iterated integrals can be very easily solved though in some cases you might need symbolic computation
packages but for every given ODE, you will get an explicit series solution in terms of arbitrary initial values and
independent variable once for all that would usually be lightning fast as opposed to forever long Newton loops in RK for
every step.*

1. Nobody really does symbolic calculus.

2. The approach becomes difficult for nth order ODE ==> n nested integrals.

3. OK you might get a series but does it converge? Compare $y(t) = (1-t)e^{-t}$.

4. A numerical solution - even if desired - will be almost impossible.

5. I would reduce it to a system of 1st order ODEs, so we can stand of shoulders of giants.

6. "*forever long Newton loops in RK for every step."*  That's a bit silly remark.

7. No mention of Picard theory of ODEs (existence and uniqueness, old sport).  Big risk is solving problems that don't
have a solution in an interval. This is basic undergrad maths.

Here a quiz to solve using this method (it is nonlinear)

$y' = p y^2 + q y + r$

or

$f' = f(1-f), f(0) = 1/2$

---

### #149 — Amin (Topic Author)
*November 22, 2016, 3:23 AM*

Yes, I do see a possible algebra error in the shown example. You know when I was writing the last day, I would correct
the errors and they would make them wrong again at places since they have controls on my computer. For most people it
would be impossible to do any work in such a case.

Just solve the examples on your own and expand the actual solution in series and it would be the same.

@cuch.

Yes, I will like to solve your proposed examples. They are a very simple case. But give me a few hours since at the
moment I have some other things to do.

---

### #150 — Amin (Topic Author)
*November 22, 2016, 11:10 AM*

This is example from my paper page 16-17. The example below is borrowed from the book Non Linear Ordinary Differential
Equations by Martin Hermann and Masoud Saravi. Example 2.7, page 50.

Page 16 starts.

Example 5

Consider the 2nd order initial value problem given as

$y''=f\left(\tau ,y(\tau ),y'(\tau )\right)=-2 y y'$       $y(0)=y_0=0$      $y'(0)=y'_0=1$

From the general solution expansion given in Equation (22), we calculate the coefficients of the first few terms as

$\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y\left(t_0\right),y'\left(t_0\right)\right)d\tau ds=\left(-2y'_0y_0\right)\frac{t^2}{2}=0$

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0 +\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right) \right]dud\tau ds$

$=\left(-2y'_0{}^2\right)\frac{t^3}{6}+\left(-2y_0\left(-2y'_0y_0\right)\frac{t^3}{6}=-\frac{t^3}{3}\right.$

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]y'_0\right.$

$\left.+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]dv dud\tau ds$

$=0+\left(8y_0 y'_0{}^2\right)\frac{t^4}{24}+\left(8y_0 y'_0{}^2\right)\frac{t^4}{24}+\left(-8y_0{}^3y'_0\right)\frac{t^4}{24}=0$

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\int _{t_0}^v\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0\right.\right.\right.$

$\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]y'_0$

$+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0\right.$

$\left.\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]y'_0$

$+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]y'_0\right.$

$+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0\right.$

$\left.\left.\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]f\left(w,y_0,y'_0\right)\right]dwdv dud\tau ds$

$\left.=0+\left(8y'_0{}^3\right)\frac{t^5}{120}+\left(8y'_0{}^3\right)\frac{t^5}{120}+\left(-24y_0{}^2y'_0{}^2\right)\right)\frac{t^5}{120}+0+$

$\left(16 y_0y'_0\left(-2y_0y'_0\right)\right)\frac{t^5}{120}+\left(16 y_0y'_0\left(-2y_0y'_0\right)\right)\frac{t^5}{120}-\left(8y_0{}^3\left(-2y_0y'_0\right)\right)\frac{t^5}{120}=\frac{2t^5}{15}$

By continuing the expansion for another two terms, we can verify the next term in expansion as $\frac{-17t^7}{315}$

And we get the first significant terms of the solution as

$y(t)=t-\frac{t^3}{3}+\frac{2t^5}{15}-\frac{17t^7}{315}+\text{...}.$

I never gave the last term of expansion but I did verify it. You can compare the solution with the one given in the book
page 50.

---

[← Previous](page_002.md) | [Index](index.md) | [Next →](page_004.md)
