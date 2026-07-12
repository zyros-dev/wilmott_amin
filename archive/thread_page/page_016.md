# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 16 of 65** — Posts #751–#800

[← Previous](page_015.md) | [Index](index.md) | [Next →](page_017.md)

---

### #751 — Amin (Topic Author)
*August 16, 2018, 9:51 PM*

Sorry in the previous program, In the training one step ahead simulation step, I needed to advance just one subdivision
of the density to make a variance comparison. Actually, it could take three consecutive subdivisions.

Obviously in the variants of the program when we do not know the generating SDE and when there could be uncertainty that
is not coming off a single SDE, we will have to advance all the density subdivisions and make a different existing to
one step ahead variance comparison for all of the subdivisions and use different variance scaling in hermite polynomials
associated with each density subdivision.

---

### #752 — Amin (Topic Author)
*August 18, 2018, 10:52 AM*

When I calculated ratio of variance(or standard deviation to be precise) in my program, I used an approximate value for
the subdivision ends. What I used is given here

              y0h=X(81)+(X(82)-X(81))/2.0; //higher ending point of subdivision 81

              y0l=X(81)-(X(81)-X(80))/2.0;  //lower ending point of subdivision 81

dividing the difference between centres of consecutive subdivisions by two is only approximate but works reasonably well
at most places in the density. I want to point out again that these subdivision endpoints were calculated on a
non-normal density before the transformation that converts it into a normal density. But I am sure there will be
extensions that will calculate subdivision ends employing higher derivatives that will make a sharply precise
calculation of subdivision end points and the ratio of standard deviations of existing and one step ahead simulation
density.

My calculated value of subdivision ends is only rough but accurate enough and the ratio of standard deviations
calculated do change slightly across the density and actually become very inaccurate at start of the density. I believe
it is due to the fact that I have made a very rough calculation of subdivision ends.

---

### #753 — Amin (Topic Author)
*August 18, 2018, 7:39 PM*

Sorry bad post.

---

### #754 — Amin (Topic Author)
*August 19, 2018, 2:21 PM*

When we simulate a simple SDE of the form

$dX(t)=\sigma(t) dz(t)$

for two steps with volatility for individual steps given as $\sigma(t_1)$  and $\sigma(t_2)$

The true integrated variance over time is known obviously as ${\sigma(t_1)}^2 \Delta(t_1) + \sigma(t_2)^2 \Delta(t_2) $

But in the Ito-Taylor density simulation method, the integrated variance is correlated with previous time steps for each
time step in time evolution and when we use a hermite polynomial with unit variance for two step simulation, the
integrated variance of the density with two step evolution is given as

${\sigma(t_1)}^2 \Delta(t_1) + 2 \sigma(t_1) \sqrt{\Delta(t_1)} \sigma(t_2) \sqrt{\Delta(t_2)} +{\sigma(t_2)}^2 \Delta(t_2)$

Now all friends can see why in the Ito-Taylor density simulation method programs I posted for various SDEs with time
homogeneous variance structure and for T step simulation when I used$\frac{1}{\sqrt{T}}$ , my variance was matching with
true variance since it divided the correlated integrated variance (of the Ito-Taylor density simulation method) by a
factor of T and brought it equal to true uncorrelated integrated variance in time.

So we have to design all Ito-Taylor density simulation methods considering that unlike monte carlo integrated variance
is no-longer uncorrelated in time in this Ito-Taylor density simulation method and we would have to match integrated
variance on each step of the density evolution. This is just the beginning and start of the method but I am sure there
would be large contributions from many other people and hopefully this will become method of choice for densities
simulation because it is so fast.

And sorry there were some errors in the latest program I posted and I would be posting another corrected program in two
to three days.

---

### #755 — Amin (Topic Author)
*August 20, 2018, 5:57 PM*

I am sharing this program and this could be a possible starting point for more advanced and precise algorithms. The
program works for simple SDEs that do not take auto-correlation structure in integrated variance and you would have to
make modifications in this program if you want to simulate mean-reverting or other SDE that take auto-correlation in
time though this modification can be easily done. I am sure you would have to modify it for many other SDEs but I hope
that it would be useful as a good starting point.

I have simulated the SDE given as

$dX(t)=\mu(t) X(t) dt + \sigma(t) X(t) dz(t)$

The program can take any term structure of volatilities and variable simulation steps. But it simulates one single
unique SDE and you would have to make some changes in the program if you want to change the SDE half way along the
simulation.

I have used the following simple algorithm to calculate the variance scaling of hermite polynomials.

I have equated the Ito-Taylor simulation method correlated integrated variance with a scaling factor for simulation
standard deviation and equated it with uncorrelated true variance of the SDE evolution by altering the scaling factor
that makes both sides of the equations equal i.e. this scaling factor equates the integrated variance of the Ito-Taylor
density simulation method with the true integrated variance. This is the scaling that is applied to hermite polynomials.
In case of auto-correlation in true variance evolution, you would have to account for the autocorrelation effect that I
have not done. Here are the equations

if$\sigma_0^2$ is the variance of existing density and$\sigma_1^2$ is the variance of simulation step. Integrated
variance of uncorrelated true SDE evolution is on the RHS of the equation below. And Ito-Taylor density simulation
method integrated variance is on the LHS of equation below. To the LHS of the equation which is Ito-Taylor density
integrated variance, I have applied a scaling denoted by$\rho$ to the simulation step variance (its squre-root)
$\sigma_1$ which would equate both sides of the equation.

${\sigma_0}^2 + 2 \sigma_0 (\rho \sigma_1) + {(\rho \sigma_1)}^2 = {\sigma_0}^2 + {\sigma_1}^2 $

so we get the equation for rho as

${\rho}^2 +  \frac{2 \sigma_0}{\sigma_1}  \rho -1=0$

Though we could also calculate absolute variances in normal terms but we just need to find the ratio of standard
deviations(meaning square roots of variances) which is done by transforming the densities into normal terms and taking
the ratios of both transformed existing density and transformed simulation density subdivision interval.

$\rho = \frac{-b + \sqrt{b^2 +4}}{2}$ where $ b= \frac{2 \sigma_0}{\sigma_1}$

rho is the scaling of hermite polynomials that is needed to match the Ito-Taylor simulation method density with true
density on each simulation step in time. Again here$\sigma_0$ is square root of variance associated with existing
density and$\sigma_1$ is square root of variance associated with simulation step. And this ratio is calculated in
"transformed normal density terms" and I would like to compare the normal density transformation as
dimensionless-coordinates.

This is b in the above equation where we need to find the ratio of standard deviations.

Here is the matlab program. This is the first quick version and I hope to update it with a better program in a few days.

```
function [] = ItoTaylorNewWilmottQuadratic03ANew()
%This program simultes the density by making a comparison of
%existing variance of the density and variance to be simulated.
%The Ito-Taylro Density Simulaiton method adjusts the variance
%of hermite polynomials so that simulated variance matches
%with the true integrated variance of the SDE.
%The current program works in the case of SDEs with little
%auto-correlation strucutre across time. So In the case
%of mean-reverting stochastic volatility models or other
%similar models where auto-correlation exists in time,
%the method has to be appropriately modified.
%The first time step is directly simulated
%But for all later steps the variance of hermite
%polynomials is altered so that Ito-Taylor simulation
%method's integrated variance matches the true integrated variance
%The variance is matched by solution of the equation
% sigma1^2 + 2 * sigma1 *(r * sigma2)+ (r * sigma2)^2
%=sigma1^2 + 2 * sigma1 *sigma2+ sigma2^2
%The LHS of the equation is correlated variance
%equation with r which is the scaling factor.
%The RHS of the equation is uncorrelated variance
%evolution which will have to be altered in the
%case of SDEs that take auto-correlation.
% r is the scaling factor that is adjusted so
%that the variance of both sides of the equations are equal
%and this is the scalingfactor that adjusts the
%hermite polynomials's variance
Nn=161;    % No of normal density subdivisions
dNn=.05;   % Normal density width. would change with number of subdivisions
Tt=20;      %No of total simulation time steps;
x0=1.0;   % starting value of SDE
X(1:Nn)=x0; %Initialize the density subdivisions with initial value.
beta1=.55;   % the first drift term power.
gamma=.850;   % volatility power.
mu0=.26;   % first drift coefficient.
dt(1)=.05; %I have kept the time steps the same but you can freely change them.
dt(2)=.05;
dt(3)=.05;
dt(4:Tt)=.065
sigma0(1)=.85;
sigma0(2)=.65;
sigma0(3)=.75;
sigma0(4)=.85;
sigma0(5)=.85;
sigma0(6)=.25;
sigma0(7)=.55;
sigma0(8)=.65;
sigma0(9)=.75;
sigma0(10:Tt)=.95;
T1=1.0;%Hermite polynomials have unit varaince for first step.
for tt=1:Tt

     if(tt>1)
      tt
      NnMid=81; %This is the subdivision used for calculation
      %of ratio of standard deviations.
        for nn=NnMid-1:NnMid+1
             Zn(nn)=((nn-1)*dNn - 4.0);
             %This is a training step to calculate a ratio of
             %one simulation step volatility of the density and
             %volatility of exising density.
             %Volatility in above line to be understood as square root of variance
             %One step simulation density  is calculated using a
             %single starting point of x0
             %but you can freely choose any other starting
             %point since the variance of transformed normal
             %density is independent of the starting coordinates
             %though there could be some better starting points
             % from the point of view of accuracy.
             %This simulation step uses hermite polynomial with standard variance.
             %This simulation step is re-started from time zero
             %and not on top of existing density. This is just
             %to calculate one step variance(or its square root)
             %It works since we are calculating the density in
             %normal or "dimensionless" coordinates.

            X1(nn)=x0+ ...
             mu0* x0.^beta1 * dt(tt) + ...
             mu0^2 * beta1* x0.^(2*beta1-1) * dt(tt).^2/2.0 + ...
            (sigma0(tt) * x0.^gamma *sqrt(dt(tt)) + ...
             sigma0(tt) * mu0 * beta1 * x0.^(beta1 + gamma -1) *(1 - 1 / sqrt(3)) * dt(tt).^1.5 + ...
             sigma0(tt) * mu0 * gamma * x0.^(beta1 + gamma -1) * 1 / sqrt(3) * dt(tt)^1.5) * Zn(nn) + ...
             sigma0(tt).^2 *gamma* x0.^(2*gamma -1 ) .* dt(tt)/2 .* ( Zn(nn).^2 - 1 );

        end

        %Calculate the start and ends of mid density subdivisions
        %y0h and y0l are start and end of mid of existing density
        %before the simulation
        y0h=X(NnMid)+(X(NnMid+1)-X(NnMid))/2.0;
        y0l=X(NnMid)-(X(NnMid)-X(NnMid-1))/2.0;

        %y1h and y1l are start and end of mid of density that has been
        %simulated to calculate the variance after the simulation
        y1h=X1(NnMid)+(X1(NnMid+1)-X1(NnMid))/2.0;
        y1l=X1(NnMid)-(X1(NnMid)-X1(NnMid-1))/2.0;

        % We calculate the standard deviation ratio after converting both
        % densities to normal density after transformation.
        % For a single unique SDE, we need to compare just one density subdivison
        % and we just compare the ratio of varaince of middle subdivisions
        % of existing and simulated training density

        SigmaRatio=(2)*(y0h^(1-gamma)-y0l^(1-gamma))/(y1h^(1-gamma)-y1l^(1-gamma))

        rho= (-SigmaRatio + sqrt(SigmaRatio^2 + 4))/2.0;
        %This rho is scaling of hermite polynomials.

       T1=rho^2*(1);
     end
    for nn=1:Nn
        Z(nn)=((nn-1)*dNn-4.0)*sqrt(T1);

        HermiteP(1,nn)=1;
        HermiteP(2,nn)=Z(nn);
        HermiteP(3,nn)=(Z(nn)^2-1);
        HermiteP(4,nn)=Z(nn)^3-3*Z(nn);
        HermiteP(5,nn)=Z(nn)^4-6*Z(nn)^2+3;

    end
    for nn=1:Nn
        X(nn)=X(nn)+ ...
            mu0* X(nn).^beta1 * dt(tt) + ...
            mu0^2 * beta1* X(nn).^(2*beta1-1) * dt(tt)^2/2.0 + ...
           (sigma0(tt) * X(nn)^gamma *sqrt(dt(tt)) + ...
            sigma0(tt) * mu0 * beta1 * X(nn).^(beta1 + gamma -1) *(1 - 1 / sqrt(3)) * dt(tt)^1.5 + ...
            sigma0(tt) * mu0 * gamma * X(nn).^(beta1 + gamma -1) * 1 / sqrt(3) * dt(tt)^1.5) * HermiteP(2,nn) + ...
            sigma0(tt).^2 *gamma* X(nn).^(2*gamma -1 ) * dt(tt)/2 * HermiteP(3,nn);
    end

end
for nn=1:Nn
    B(nn)=((nn-1)*dNn-4.0);
end
for nn=2:Nn-1
    DfX(nn) = (X(nn + 1) - X(nn - 1))/(B(nn + 1) - B(nn - 1));
end
fX(1:Nn)=0;
for nn = 2:Nn-1
    fX(nn) = normpdf(B(nn),0, 1)/abs(DfX(nn));
end
%Monte carlo simulation follows for comparison of our simulated desnsity and
% monte carlo density.
paths=100000;
X2(1:paths)=x0;
Random1(1:paths)=0;
sigma00(1:Tt)=sigma0(1:Tt);
for tt=1:Tt
    dt0=dt(tt);
    Random1=randn(size(Random1));
    X2(1:paths)=X2(1:paths)+ mu0* X2(1:paths).^beta1 *dt0 + ...
        sigma00(tt) * X2(1:paths).^gamma .* Random1(1:paths) *sqrt(dt0) + ...
        mu0^2 * beta1* X2(1:paths).^(2*beta1-1) *  dt0^2/2.0 + ...
        sigma00(tt)^2 * gamma * X2(1:paths).^(2*gamma-1) .* dt0/2.0 .* (Random1(1:paths).^2-1) + ...
        mu0 * sigma00(tt) *gamma* X2(1:paths).^(beta1+gamma-1) .* sqrt(1/3) .* dt0^1.5 .* Random1(1:paths) + ...
        sigma00(tt) * mu0 *beta1* X2(1:paths).^(beta1+gamma-1) .* (1-sqrt(1/3)) .* dt0^1.5 .* Random1(1:paths);
end
sum(X2(:))/paths   %monte carlo average
BinSize=.0075;
MaxCutOff=20;
[XDensity,IndexOutX,IndexMaxX] = MakeDensityFromSimulation_Infiniti(X2,paths,BinSize,MaxCutOff);
plot(X(3:Nn-2),fX(3:Nn-2),'r',IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'g');
end

```

---

### #756 — Amin (Topic Author)
*August 20, 2018, 9:36 PM*

Just a warning that for some SDEs and for specific parameters there, the step size that I have used in the above matlab
program sometimes might be too large since I am using only two hermite polynomials in the Ito-Taylor density simulation
method. It was very easy to write a simple two polynomial simulation program.

---

### #757 — Amin (Topic Author)
*August 26, 2018, 8:42 PM*

I hope to present a new program in a few days(3-4) based on evolution of the SDEs in transformed coordinates. And here
are the key features of the idea behind the new program.

1. Compare the variance by simulating the median of the transformed SDE. Here Z=0 will be used in the simulation and
though there will be contributions from the second and fourth hermite polynomials, it will become an ODE like evolution
for the median.

2. For appropriate calculation of the variance, I plan to calculate the change of density derivative with respect to Z
analytically instead of using finite-differences. Especially at the median, since Z=0, there will only be contribution
to this calculated volatility (square-root of variance) only from the terms that take the first power of Z coming from
first and third hermite polynomials.

I hope that I will be able to calculate a very good estimate of the variance of the transformed density in new
coordinates since a lot of the error that comes from inaccuracies in the numerical method will be controlled when most
calculations are analytic and are done using the above features.

---

### #758 — Amin (Topic Author)
*August 27, 2018, 11:50 AM*

In some of my first Ito-Taylor programs, I calculated the density of SDEs using a change of variable derivative with a
standard gaussian density and this change of variable derivative was calculated analytically but later in my programs, I
calculated it with finite-differences. Since this derivative is calculated with respect to a standard gaussian variable,
it is also directly related with variance.

If the one step second order Ito-Taylor expansion of X(n) which is nth subdivision of the density of X and is given as

$X(n)= a(X_0(n),\Delta t) + b(X_0(n),\Delta t) Z(n) + c(X_0(n),\Delta t) ({Z(n)}^2-1) $

In that case, the local derivative of nth subdivision with respect to Z(n) can be found as

$\frac{dX(n)}{dZ(n)} = b(X_0(n),\Delta t) + 2 c(X_0(n),\Delta t)  Z(n) $

And then I calculated the density of X which has been expanded by Ito-Taylor by change of variable with respect to
Standard Gaussian density as

$f(X(n)) = f(Z(n))   |\frac{dZ(n)}{dX(n)} | $

but in my later programs, I simply calculated this derivative using finite differences. This derivative is directly
related with the variance of the density of the SDE and really should be calculated analytically. In addition to giving
us insight about evolution of variance for each subdivision and existing variance for each subdivision, if we calculate
this derivative analytically, we will have more precision than using finite-differences version of this derivative.
Though obviously, for the calculation of existing variance when dynamics of the evolution are not known or are too
complex, we will like to calculate this derivative using finite-differences.

---

### #759 — Amin (Topic Author)
*August 27, 2018, 7:43 PM*

I think there could be many many new things in stochastics due to new Ito-Taylor related research. Here are a few new
opportunities as I can foresee and brainstorming ideas.

1. For modelling and solution of stochastic differential equations, We can very easily modify the existing Ito-Taylor
density simulation method to have new stochastic differential equations with time scaling applied to gaussian random
variable in the SDE that is different from the time scaling of Brownian motion. This could be very helpful in many
stochastic applications.

2. We could easily extend the method and try non-linear version of SDEs where non-linear Guassian noise can for example
take a differential of square of Brownian motion, or cube of Brownian motion in the SDE. This is really no more
difficult and we can do it just by expanding the non-linear noise in the SDE using Ito formula and then representing
every resulting integral in terms of integrals of hermite polynomials and then further expand those integrals using
Ito-Taylor logic. Here is a relevant earlier post that I made in which I tried to show how integrals containing powers
of Brownian motion can easily be represented in terms of hermite polynomials.

>
> Amin:
> Here I have latexed the update formulas for stochastic integrals
>
> $\int_0^t s^m H_{n}(z(s)) ds = \frac {t^{m+1} H_{n}(z(t))}{(m+1)} (1 - \frac {\sqrt{n}}{\sqrt{(2m+n+2)}}) $
>
> $\int_0^t s^m H_{n}(z(s)) dz(s)= \frac {t^m H_{n+1}(z(t))}{ \sqrt{(n+1)} \sqrt{(2m+n+1)}} $
As I suggested, we can calculate most stochastic integrals using this update. Let us suppose, we want to calculate

$\int_0^t z(s)^4 ds$  Equation(1)

Here is the way to go. We have to do it in terms of hermite polynomials.

fourth hermite polynomial representation of Brownian motion goes like

$H_4(z(t)) = z(t)^4 -6 t z(t)^2 +3 t^2 $  Eq(2)

and second hermite polynomial is

$H_2(z(t)) = z(t)^2 - t $  Eq(3)

and we know from the quoted post

$\int_0^t H_4(z(s)) ds = t H_4(z(t)) (1- \frac{2}{\sqrt{6}} ) $  Eq(4)

so from Eq(2) and Eq(4)

$\int_0^t z(s)^4 ds = t H_4(z(t)) (1 - \frac{2}{\sqrt{6}} ) + 6 \int_0^t s z(s)^2 ds - 3 \int_0^t s^2 ds $ Eq(5)

In order to solve the second term, we take the second hermite polynomial and use the formula in quotes to calculate that

$\int_0^t s H_2(z(s)) ds = \frac{t^2 H_2(z(t))}{2} (1 - \frac{\sqrt{2}}{\sqrt{6}} ) $  Eq(6)

so

$\int_0^t s z(s)^2 ds = \frac{t^2 H_2(z(t))}{2} ( 1 - \frac{\sqrt{2}}{\sqrt{6}} ) + \int_0^t s^2 ds $  Eq(7)

and we substitute Eq(7) in Eq(5) to get

$\int_0^t z(s)^4 ds = t H_4(z(t)) ( 1 - \frac{2}{\sqrt{6}} ) + 3 t^2 H_2(z(t)) ( 1 - \frac{\sqrt{2}}{\sqrt{6}} ) + 3 \int_0^t s^2 ds $

so

$\int_0^t z(s)^4 ds = t H_4(z(t)) (1- \frac{2}{\sqrt{6}} ) + 3 t^2 H_2(z(t)) ( 1 - \frac{\sqrt{2}}{\sqrt{6}} ) + t^3 $

and we could take$t^3$ common and have a representation in terms of standard normal. And then you can easily simulate
the density of$\int_0^t z(s)^4 ds$ or analytically calculate and plot its density.
3. It would also be interesting how we could solve Jump-diffusion SDEs by calculating the variance of Jump parts of the
SDEs and adding it to Ito-Taylor density simulation method on every step.

4. We could try other noises different from Gaussian noise. Very simple starting point could be noises for whose
densities we already know other orthogonal polynomials just like hermite polynomials are orthogonal with respect to
Gaussian density.

So I really believe there would be huge new avenues for people doing research in stochastics and their applications and
we would be able to apply stochastics to model many complex phenomenon more easily.

---

### #760 — Amin (Topic Author)
*August 27, 2018, 8:28 PM*

I would like to mention for friends again that Ito-Taylor expansion theory of SDEs was originally developed by Dr.
Eckhard Platen and Dr. Wolfgang Wagner. Here are two first original papers in this area.

1. A Generalized Taylor Formula for Solutions of Stochastic Equations. By Eckhard Platen.

2. On a Taylor Formula for a Class of Ito Processes. By Eckhard Platen and Wolfgang Wagner.

Though it is popularly called Ito-Taylor expansion, it has also been called Platen and Wagner formula at many places in
the literature acknowledging the original work of Platen and Wagner.

---

### #761 — Amin (Topic Author)
*September 13, 2018, 7:51 AM*

> When we simulate a simple SDE of the form
>
> $dX(t)=\sigma(t) dz(t)$
>
> for two steps with volatility for individual steps given as $\sigma(t_1)$  and $\sigma(t_2)$
>
> The true integrated variance over time is known obviously as${\sigma(t_1)}^2 \Delta(t_1) + \sigma(t_2)^2 \Delta(t_2) $
>
> But in the Ito-Taylor density simulation method, the integrated variance is correlated with previous time steps for
each time step in time evolution and when we use a hermite polynomial with unit variance for two step simulation, the
integrated variance of the density with two step evolution is given as
>
>
${\sigma(t_1)}^2 \Delta(t_1) + 2 \sigma(t_1) \sqrt{\Delta(t_1)} \sigma(t_2) \sqrt{\Delta(t_2)} +{\sigma(t_2)}^2 \Delta(t_2)$
>
> Now all friends can see why in the Ito-Taylor density simulation method programs I posted for various SDEs with time
homogeneous variance structure and for T step simulation when I used$\frac{1}{\sqrt{T}}$ , my variance was matching with
true variance since it divided the correlated integrated variance (of the Ito-Taylor density simulation method) by a
factor of T and brought it equal to true uncorrelated integrated variance in time.
>
> So we have to design all Ito-Taylor density simulation methods considering that unlike monte carlo integrated variance
is no-longer uncorrelated in time in this Ito-Taylor density simulation method and we would have to match integrated
variance on each step of the density evolution. This is just the beginning and start of the method but I am sure there
would be large contributions from many other people and hopefully this will become method of choice for densities
simulation because it is so fast.
>
>
>
> And sorry there were some errors in the latest program I posted and I would be posting another corrected program in
two to three days.

I believe that the statement made in the above post is true only when first hermite polynomials are involved. And the
density simulation laws over the time grid would be different and more complex as we add higher hermite polynomials in
Ito-Taylor density simulation algorithm. And since the above holds for only first hermite polynomials and that is one
reason when we convert the SDE into gaussian-like coordinates and most of the variance is explained by the first hermite
polynomial in transformed coordinates, we can easily use the hermite polynomial variance scaling formula that is based
on the above post. But I am sure we are not limited to using that formula based on gaussian-like coordinates and I would
soon be posting a new program for SDE evolution that would advance the density using original coordinates and that would
be based on how higher hermite polynomials interact when we use Ito-Taylor desnity evolution algorithm though I am
afraid that some equations that would have to be solved would be more difficult than the simple quadratic equation we
needed to solve when we made the variance calculations in the gaussian-like transformed coordinates.

---

### #762 — Amin (Topic Author)
*September 17, 2018, 2:05 PM*

In the old program that I shared that demonstrated that the new method is indeed useful, I simply took a transformation
of the SDE variable and compared existing and new variances by taking a ratio of subdivision widths in transformed
variables. This was a quick hack and works remarkably well. But has problems when SDEs become non-linear like
stochastic  volatility SDEs and when diffusion starts too close to zero. In an ideal sense, the existing and new
variances of transformed variables have to be compared in terms of variance of Bessel process. I am working on it but
since the process has to be fast, it would require a bit of effort as we do not want any large calculations that would
slow down the method. We have to match existing variance with the variance of Bessel process for the same probability
quantile and same for the new variance. I hope that I would be able to complete this in next few days and post a simple
routine here on Wilmott technical forum.

---

### #763 — Amin (Topic Author)
*September 21, 2018, 4:14 PM*

Sorry bad post.

---

### #764 — Amin (Topic Author)
*September 27, 2018, 5:05 PM*

OK here is my initial strategy to map the volatility on a CEV type diffusion. Sankaran's approximation maps the CDF of
CEV variable on the CDF of normal variable. This is very similar to CDF subdivisions we have in our method. Using
Sankaran's approximation, we can easily numerically calculate the value of$\frac{\partial F}{\partial Z}$ and by
perturbing these derivatives, we can calculate the values of
$\frac{\partial \frac{\partial F}{\partial Z}}{\partial \big[{\sigma}^2 t \big]}$ . In fact
$\frac{\partial F}{\partial Z}$ is an even cheaper and better proxy for the width of the subdivisions and is found by
finite differences on subdivision centers. And we will have to do a newton type iteration to match and find a pair of
$\frac{\partial F}{\partial Z}$ and${\sigma}^2 t$ from the Sankaran formula to find the variance in driftless CEV units.
This should be fairly easy. I have not done this yet but I will be playing with it in next few days. And if it goes
well, something faster might possibly be worked out. I believe we could map different subdivisions of non-linear SDEs on
respective sub divisions of CEV process to find the variance of various subdivisions of non-linear subdivisions in
driftless CEV units. Again I have not done this so I would request friends to take this with a grain of salt.

Word of caution is that this is for researchers only and not everybody is advised to start working with this until there
is a completely clear recipe to follow.

---

### #765 — Amin (Topic Author)
*September 30, 2018, 11:31 AM*

> I am sharing this program and this could be a possible starting point for more advanced and precise algorithms. The
program works for simple SDEs that do not take auto-correlation structure in integrated variance and you would have to
make modifications in this program if you want to simulate mean-reverting or other SDE that take auto-correlation in
time though this modification can be easily done. I am sure you would have to modify it for many other SDEs but I hope
that it would be useful as a good starting point.
>
> I have simulated the SDE given as
>
> $dX(t)=\mu(t) X(t) dt + \sigma(t) X(t) dz(t)$
>
> The program can take any term structure of volatilities and variable simulation steps. But it simulates one single
unique SDE and you would have to make some changes in the program if you want to change the SDE half way along the
simulation.
>
> I have used the following simple algorithm to calculate the variance scaling of hermite polynomials.
>
>
>
> I have equated the Ito-Taylor simulation method correlated integrated variance with a scaling factor for simulation
standard deviation and equated it with uncorrelated true variance of the SDE evolution by altering the scaling factor
that makes both sides of the equations equal i.e. this scaling factor equates the integrated variance of the Ito-Taylor
density simulation method with the true integrated variance. This is the scaling that is applied to hermite polynomials.
In case of auto-correlation in true variance evolution, you would have to account for the autocorrelation effect that I
have not done. Here are the equations
>
> if$\sigma_0^2$ is the variance of existing density and$\sigma_1^2$ is the variance of simulation step. Integrated
variance of uncorrelated true SDE evolution is on the RHS of the equation below. And Ito-Taylor density simulation
method integrated variance is on the LHS of equation below. To the LHS of the equation which is Ito-Taylor density
integrated variance, I have applied a scaling denoted by$\rho$ to the simulation step variance (its squre-root)
$\sigma_1$ which would equate both sides of the equation.
>
> ${\sigma_0}^2 + 2 \sigma_0 (\rho \sigma_1) + {(\rho \sigma_1)}^2 = {\sigma_0}^2 + {\sigma_1}^2 $
>
> so we get the equation for rho as
>
> ${\rho}^2 +  \frac{2 \sigma_0}{\sigma_1}  \rho -1=0$
>
> Though we could also calculate absolute variances in normal terms but we just need to find the ratio of standard
deviations(meaning square roots of variances) which is done by transforming the densities into normal terms and taking
the ratios of both transformed existing density and transformed simulation density subdivision interval.
>
> $\rho = \frac{-b + \sqrt{b^2 +4}}{2}$ where $ b= \frac{2 \sigma_0}{\sigma_1}$
>
> rho is the scaling of hermite polynomials that is needed to match the Ito-Taylor simulation method density with true
density on each simulation step in time. Again here$\sigma_0$ is square root of variance associated with existing
density and$\sigma_1$ is square root of variance associated with simulation step. And this ratio is calculated in
"transformed normal density terms" and I would like to compare the normal density transformation as
dimensionless-coordinates.
>
> This is b in the above equation where we need to find the ratio of standard deviations.
In many non-linear equations, it might not be possible to assign a single scaling$\rho$ to the variance along all
subdivisions for a single SDE. And we could have a different scaling applied to hermite polynomials$\rho(n)$ for nth
subdivision. Another simple way for finding$b(n)=\frac{ 2 \sigma_0(n)}{\sigma_1(n)}$ would be to simply use the basic
formula of variance and use the formula$b(n)=\frac{2 (x_n(t)-\mu(t))}{(x_n(t,t+1)-\mu(t,t+1)}$ . Here$x_n(t)$ is the
center of the nth subdivision on the existing density and$\mu(t)$ is the mean of the existing density while$x_n(t,t+1)$
is the center of nth subdivision on one step evolved density that is evolved from the mean$\mu(t)$ of the existing
density and$\mu(t,t+1)$ is the mean of the new one step evolved density.

I wanted to post a program with this formula but there was a problem that close to the means in the equation for$b(n)$ ,
the values become unstable or off and I have to account for this instability and fix it otherwise this formula works
remarkably well once a bit away from the means. Again this formula has to be applied to transformed coordinates as I did
in the first program.

---

### #766 — Amin (Topic Author)
*October 12, 2018, 1:19 PM*

Here are some interesting things that have come up in my research. suppose there is an SDE of the form
$dX(t)=\mu(t) X^{\beta}(t) dt + \sigma(t) X^{\gamma}(t) dz(t)$ that we want to simulate with this new Ito-Taylor density
simulation method. We noticed that a lot of SDEs of this form could easily be simulated with this method after
transformation into Bessel coordinates. While some non-linear SDEs like stochastic volatility SDEs could not be
simulated in a satisfactory manner. Here I try to explain this anomaly and I will like to state a few observations.

When we transformed SDEs of the type given above in SDE equation into Bessel coordinates, the numerically calculated
first derivative of transformed density with respect to normal variable$\frac{\partial Y}{\partial Z}$ when calculated
from density mass equality, remains almost constant and does not take a significant second derivative. Here Y represents
Bessel transformed variable from SDE variable X. For all those SDEs that become linear after converting to Bessel
coordinates, we can use several methods including the method in my original program. Here the criteria for linearity is
that$\frac{\partial Y}{\partial Z}$ is almost constant and$\frac{{\partial}^{2} Y}{\partial {Z}^2}$ is almost
negligible. In the equations that are non-linear like stochastic volatility equation that takes a non-negligible second
derivative with normal variable, we need to use this numerically calculated second or higher derivatives with possibly
hermite polynomials to appropriately calculate existing variance and innovations(I earlier called it simulation
variance) variance and their ratios. We cannot easily use the original coordinates since in the original coordinates,
the SDE variable continues to take many higher derivatives with normal. I am sure with a slightly better understanding
of the method, we could also use original coordinates for density simulation as well. again the reason for my being able
to successfully simulate the densities of many simpler linear processes was that when I converted them into transformed
coordinates, all higher derivatives with respect to normal variable disappeared and only the first derivative remained.
In general, after the appropriate transformations, the number of significant higher derivatives with respect to normal
variable sharply decreases. I believe that these numerically calculated higher derivatives of transformed densities with
normal variable have to be used with variance of hermite polynomials to satisfactorily calculate the existing and
innovations variance.

---

### #767 — Amin (Topic Author)
*October 14, 2018, 5:30 PM*

Suppose we have an SDE for X and we have calculated its existing density at a certain time. We suppose that we have
divided the density of X into subdivisions that have the same mass as linear subdivisions of the normal density. We want
to calculate local variance for each subdivision. In order to do that we numerically calculate the derivatives
$\frac{\partial X}{\partial Z}$ and$\frac{\partial^2 X}{\partial Z^2}$ where Z is a standard normal variable and these
derivatives are calculated with probability mass equality for each subdivision of X. For now we limit ourselves to first
two derivatives. We can expand X as a function of Z around the center of nth subdivision,$x_n$ as

$X(Z)=x_n + \frac{\partial X}{\partial Z} Z + .5 \frac{\partial^2 X}{\partial Z^2} Z^2$

Using the variance for standard normal and its powers, we can easily calculate the local variance of X at the nth
subdivision.

The only problem is that Z is perfectly correlated across time in our Ito-Taylor density simulation method while it is
totally uncorrelated across time in reality so we have to make an adjustment in the value of Z that we use for
simulation of Ito-Taylor density simulation method.

if$X_0$ denotes the existing density variable and$X_1$ denotes the innovations density variable, the true variance that
is the right variance at the certain subdivision after taking the innovation simulation step should be

$(\frac{\partial X_0}{\partial Z})^2 + (\frac{\partial X_1}{\partial Z})^2+.5 (\frac{\partial^2 X_0}{\partial Z^2} )^2  +.5 ( \frac{\partial^2 X_1}{\partial Z^2})^2 $

while Ito-Taylor simulation assumes complete correlation for the Z's across time and their variance without any
adjustment turns out to be far greater. This variance can also be very easily calculated.

Again we have to make sure that Ito-Taylor simulation method variance matches with the true variance of the SDE at that
particular subdivision. This can also be easily done. This is not much more difficult than what we did for one
derivative case and requires slightly altering the analysis on the same lines. And then we will advance the SDE density
with different local scaling of hermite polynomials on each subdivision so that local variance simulated with Ito-Taylor
density simulation method matches with the true simulation variance.

I hope to post a full-fledged program that calculates the true density with Ito-Taylor density simulation method in a
few days.

I am travelling tomorrow so will post more details on Tuesday.

---

### #768 — Amin (Topic Author)
*October 17, 2018, 12:33 PM*

Here is the correlated sum of existing variance and innovation/simulation variance of Ito-Taylor density simulation
method in terms of original Z's. We will weight$Z_1$ with$\rho$ in LHS which is the correlated evolution and take
expectations and equate with true uncorrelated (and unweighted) sum of existing and innovation/simulation variance on
RHS and solve this quartic equation for$\rho$ and this calculated$\rho$ will be used for scaling the Z's in hermite
polynomials in Ito-Taylor density simulation method. I am writing the correlated sum of existing and innovation variance
with$Z_1$ weighted with$\rho$ in RHS and true variance after one step evolution in RHS. After taking expectations for Z,
we will solve these resulting quartic equation in$\rho$ and it is$\rho$ that will scale the Z's in hermite polynomials
in the density simulation method. In the first part of the equation or LHS, both$Z_0$ and$Z_1$ are perfectly correlated
when they appear as a product but otherwise they are standard normal with unit variance and$\rho$ is simply a scalar
multiplier.

$(\frac{\partial X_0}{\partial Z_0})^2 E(Z_0 )^2+ (\frac{\partial X_1}{\partial Z_1})^2 E(\rho Z_1)^2 + 2 \frac{\partial X_0}{\partial Z_0} \frac{\partial X_1}{\partial Z_1} E[Z_0 (\rho Z_1)]$

$+ .25 (\frac{\partial^2 X_0}{ \partial {Z_0}^2})^2  E (Z_0)^4-.25 (\frac{\partial^2 X_0}{\partial {Z_0}^2})^2  ({E(Z_0)}^2)^2 $

$ +.25 (\frac{\partial^2 X_1}{ \partial {Z_1}^2})^2  E (\rho Z_1)^4-.25 (\frac{\partial^2 X_1}{\partial {Z_1}^2})^2  ({E(\rho Z_1)}^2)^2 $

$+.5 \frac{\partial^2 X_0}{\partial {Z_0}^2} \frac{\partial^2 X_1}{\partial {Z_1}^2} E[{Z_0}^2 (\rho Z_1)^2] -.5 \frac{\partial^2 X_0}{\partial {Z_0}^2} \frac{\partial^2 X_1}{\partial {Z_1}^2} (E[ Z_0 (\rho Z_1)])^2$

=$(\frac{\partial X_0}{\partial Z_0})^2 E(Z_0 )^2+ (\frac{\partial X_1}{\partial Z_1})^2 E( Z_1)^2 $

$+ .25 (\frac{\partial^2 X_0}{ \partial {Z_0}^2})^2  E (Z_0)^4-.25 (\frac{\partial^2 X_0}{\partial {Z_0}^2})^2  ({E(Z_0)}^2)^2 $

$ +.25 (\frac{\partial^2 X_1}{ \partial {Z_1}^2})^2  E ( Z_1)^4-.25 (\frac{\partial^2 X_1}{\partial {Z_1}^2})^2  ({E( Z_1)}^2)^2 $

---

### #769 — Amin (Topic Author)
*October 18, 2018, 7:15 PM*

OK friends, I tried the above with explicit solution of quartic equation and applied it to stochastic volatility type
SDEs. My fit was generally remarkably better than before but I could see some minor discrepancy in the right tail of the
stoch  vol SDEs. Since in asset pricing, we want to be precise, so more care has to be taken. I am very sure any
discrepancy in the right tail in the skew is due to small amount of third derivative that my analysis till 2nd order did
not cover. Only problem is that sextic equation may not have a closed form solution. I will redo the above analysis till
fourth order and then write a program that does Newton iteration to solve the eighth order polynomial equation for the
scaling factor. I Am sure we can get away with around hundred points in the SDE density and then take a quarter year
time step and do all newton iterations for the whole 100 point grid to get the solution of eighth order polynomial in
parallel. I hope I will complete all of that in 7-10 days and post a new program here after that.

I am hundred percent certain after looking at the results of stoch vol SDEs densities that above analysis works
perfectly fine since there was a remarkably marked improvement in results from first order analysis. Anyway, for
researchers interested in looking at it on their own, I hope to post a matlab program with just 2nd order solution from
analysis in previous post in next 2-3 days. I hope this program will be helpful for many interested friends to do
experiments on their own.

---

### #770 — Amin (Topic Author)
*October 25, 2018, 6:10 PM*

This is something interesting so I thought I will share it. I was thinking of the relationship between derivatives of
the SDE variable X with respect to Z and the coefficients of hermite polynomials and I set up a small experiment in
which I constructed a random variable X from hermite polynomials along a density evolution using Ito-Taylor density
evolution method.

if $X(t+1)=c_1(X(t)) H_1(Z) + c_2(X(t)) H_2(Z) + c_3(X(t)) H_3(Z) $

If we differentiate$X(t+1)$ with respect to Z using density mass equality, we get that first derivative of X with
respect to Z equals the coefficient$c_1(X(t))$ of first hermite polynomial i.e.$ \frac{dX(t+1)}{dZ} = c_1(X(t))$ and
second derivative follows the relationship$.5 \frac{d^2 X(t+1)}{dZ^2}=c_2(X(t))$

and the third derivative followed $-\frac{1}{6}  \frac{d^3 X(t+1)}{dZ^3} =c_3(X(t))$

so these weighted derivatives with respect to standard normal density (that are coefficients of Taylor expansion of X
with respect to Z) have a direct interpretation as coefficients of hermite polynomials. This should hold when X is a
continuous random variable like we have in the density of SDEs.

To give a concrete idea, 1st derivative of X with respect to Z at nth point on the grid is simply calculated by finite
differences as$\frac{X(n+1)-X(n-1)}{Z(n+1)-Z(n-1)}$ on the Ito-Taylor density grid (to 2nd order accuracy).

---

### #771 — Amin (Topic Author)
*October 27, 2018, 6:13 PM*

sorry for being so wrong as I have been in the last post. But here I re-did my analysis for the relationship between
derivatives of X with respect to Z and the coefficients of hermite polynomials.

1st four hermite polynomials are

$H_1(Z)=Z$

$H_2(Z)=Z^2-1$

$H_3(Z)=Z^3-3Z$

$H_4(Z)=Z^4-6Z^2+3$

We suppose we have a function/variable that is composed of first four hermite polynomials and given as

$X(Z)=c_1 H_1(Z) + c_2 H_2(Z)+c_3 H_3(Z) + c_4 H_4(Z)$

differentiating the above appropriately, we get

$\frac{\partial^4 X}{\partial Z^4}=24 c_4$

$\frac{\partial^3 X}{\partial Z^3}=6 c_3+ 24 c_4 Z$

$\frac{\partial^2 X}{\partial Z^2}=2 c_2+6 c_3 Z + c_4(12 Z^2 -12)$

$\frac{\partial X}{\partial Z}=c_1 + 2 c_2 Z + c_3 (3 Z^2-3) + c_4 (4 Z^3-12 Z)$

Above equations can easily be solved but at Z=0, these equations are particularly easy to solve and we get

$\frac{\partial^4 X}{\partial Z^4}=24 c_4$

$\frac{\partial^3 X}{\partial Z^3}=6 c_3$

$\frac{\partial^2 X}{\partial Z^2}=2 c_2-12 c_4$

$\frac{\partial X}{\partial Z}=c_1 -3 c_3$

So we are making a slow but steady progress.

---

### #772 — Amin (Topic Author)
*November 3, 2018, 8:22 PM*

On this weekend I will post a new program for simulation. Currently, it has small instabilities but I am sure numerical
analysis experts and many other intelligent people could easily overcome them. The logic is very simple: I add drift in
a linear fashion and volatility term in an orthogonal fashion (square root of squared sum with previous increment from
the mean). It turns out to be very simple and there is just very basic mathematics in it. Though there might still be
cases with problems but I hope this will be very helpful. And again there are minor instabilities that grow with time
and some way still have to be worked out how to tackle them but I still decided to post the program. I will be posting
it tomorrow or on Sunday after writing explanations on the program.

---

### #773 — Amin (Topic Author)
*November 4, 2018, 6:34 PM*

Here is the new matlab program.In this program, I am simulating the SDE given as

       dy(t)=kappa*(theta-y(t))*dt + y(t)^gamma * dz(t);

I have not directly simulated the SDE but simulated the transformed Bessel process version of the SDE and then changed
coordinates to retrieve the SDE in original coordinates. The present program will directly simulate only the Bessel
Process version of the SDE in transformed coordinates.

The program has instability in 3-4 subdivisions in the mid of the density and I will be releasing a program in another
few days taking care of that and fixing the problem. You can do it on your own as well.

In this program, We are not taking any cross terms for the drift and volatility and have just added one constant
volatility term that occurs in the Bessel transformed SDE. The only volatility term is sigma0 *sqrt(t)*H1(N).

Here is the program. Sorry that I have not optimized the code in any way and this is just to demonstrate the idea of the
program. Will post a complete worked out program in a few days with complete optimizations.

```
function [] = ItoTaylorDensityWilmottSimplev1()
%Copyright Ahsan Amin. Infiniti derivatives Technologies.
%Please fell free to connect on linkedin: linkedin.com/in/ahsan-amin-0a53334
%or skype ahsan.amin2999
%In this program, I am simulating the SDE given as
%dy(t)=kappa(theta-y(t))*dt + y(t)^gamma dz(t);
%I have not directly simulated the SDE but simulated the transformed
%Bessel process version of the SDE and then changed coordinates to retreive
%the SDE in original coordinates.
%The present program will directly simulate only the Bessel Process version of the
%SDE in transformed coordinates.
%The program has instability in 3-4 subdivisions in the mid of the density
%and I will be relasing a program in another few days taking care of that
%and fixing the problem. You can do it on your own as well.
dt=.125/2;   % Simulation time interval.
Tt=8;     % Number of simulation levels. Terminal time= Tt*dt;
OrderA=4;  %expansion order for the analytic SDE.
OrderM=4;  %expansion order for the monte carlo simulation.
dNn=.05/1;   % Normal density width. would change with number of subdivisions
Nn=161;  % No of normal density subdivisions
NnMidn=81;%Median cell/subdivision.
NnMid=4.0;
x0=.30;   % starting value of SDE
beta1=0.0;   % the first drift term power.
beta2=1.0;   % Second drift term power.
gamma=.950;   % volatility power. Before you change this to values where
            %diffusion goes to zero, you will have to change the
            %calculation of the mean of the density in the body of the program
            %do not decrease it more than .75 before changing that.
kappa=1.0;   %mean reversion parameter.
theta=.2;   %mean reversion target
mu1=theta*kappa;   % first drift coefficient.
mu2=-1*kappa;    % Second drift coefficient.
sigma0=1.0;%Volatility value
alpha=1.0;% x^alpha is being expanded
alpha1=1-gamma;%For the expansion in transformed coordinates.

for nn=1:Nn
    x(nn)=x0^(1-gamma)/(1-gamma); %Initial value is assigned to each
                                  %subdivision in transformed coordinates.
end
%Please read notes at the end of the program for understanding of what is
%Y(l1,l2,l3,l4) and what are l1,l2, l3 and l4. In the ItoTaylor expansion
%l1 is first drift term expansion order index, l2 is for the second drift
%term, l3 is for quadratic variation drift term index and l4 is the
%volatility expansion order index.
%These sigma11, mu11, mu22, sigma22 can be lumped with Y(l1,l2,l3,l4) but I
%kept them separate for a general program where these values could change
%on every step while exponents on x in each term would remain same in
%pre-calcualted Y(l1,l2,l3,l4)
sigma11(1:OrderA+1)=0;
mu11(1:OrderA+1)=0;
mu22(1:OrderA+1)=0;
sigma22(1:OrderA+1)=0;
% index 1 correponds to zero level since matlab indexing starts at one.
sigma11(1)=1;
mu11(1)=1;
mu22(1)=1;
sigma22(1)=1;

for k=1:(OrderA+1)
    if sigma0~=0
        sigma11(k)=sigma0^(k-1);
    end
    if mu1 ~= 0
        mu11(k)=mu1^(k-1);
    end
    if mu2 ~= 0
        mu22(k)=mu2^(k-1);
    end
    if sigma0~=0
        sigma22(k)=sigma0^(2*(k-1));
    end
end
Ft(1:Tt+1,1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;
Fp(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;
Fp1(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;
%Pre-compute the time and power exponent values in small multi-dimensional arrays
for k = 0 : (OrderA)
    for m = 0:k
        l4 = k - m + 1;
        for n = 0 : m
            l3 = m - n + 1;
            for j = 0:n
                l2 = n - j + 1;
                l1 = j + 1;
                Ft(l1,l2,l3,l4) = dt^((l1-1) + (l2-1) + (l3-1) + .5* (l4-1));
                Fp(l1,l2,l3,l4) = (alpha + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
                Fp1(l1,l2,l3,l4) = (alpha1 + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
            end
        end
    end
end

for nn=1:Nn
    Z(nn)=((nn-1)*dNn-NnMid);
end

ZProb(1)=normcdf(.5*Z(1)+.5*Z(2),0,1);
ZProb(Nn)=1-normcdf(.5*Z(Nn)+.5*Z(Nn-1),0,1);
for nn=2:Nn-1
    ZProb(nn)=normcdf(.5*Z(nn)+.5*Z(nn+1),0,1)-normcdf(.5*Z(nn)+.5*Z(nn-1),0,1);
end
%Below call the program that calculates the Ito-Taylor coeffs.
YCoeff = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma);
%The routine below calls the Ito-Taylor Coeffs in transformed coordinates
%and uses alpha1 as the power where alpha1=1-gamma.
Yq=ItoTaylorCoeffsNew(alpha1,beta1,beta2,gamma);
YqCoeff=Yq/(1-gamma);%These coordinates are divided by (1-gamma)
Y(1,1,1,1)=0;
for nn=1:Nn
    Z(nn)=((nn-1)*dNn-NnMid);%*Rho1(nn);
    HermiteP(1,nn)=0;
    HermiteP(2,nn)=Z(nn);%rho1(nn)
    HermiteP(3,nn)=(Z(nn)^2-1);%rho2(nn)
    HermiteP(4,nn)=(Z(nn)^3-3*Z(nn));
    HermiteP(5,nn)=(Z(nn)^4-6*Z(nn)^2+3);
end
for tt=1:Tt
    for nn=1:Nn
        x1(nn)=x(nn);
        x_mean(nn)=0;
        for k = 0 : OrderA
            for m = 0:k
                l4 = k - m + 1;
                for n = 0 : m
                    l3 = m - n + 1;
                    for j = 0:n
                        l2 = n - j + 1;
                        l1 = j + 1;
                        if(l41)  %For first step when starting from delta origin, we do not
              %want squared orthogonal addition for volatility.
        MeanPrev=sum(ZProb(1:Nn).*x(1:Nn));%Mean of the ODE from previous step
        %Please be careful, when working with diffusion exponents that go
        %negative, this simple calculation of the mean will corrupt the
        %whole program when all sort of negative and imaginary values are
        %used to calculate the mean. For that case, you will have to
        %carefully take the mean with only values that are on positive real
        %axis.
        for nn=1:Nn
            if(x(nn)>MeanPrev)
                x(nn)=MeanPrev+x_mean(nn)+sqrt((x(nn)-MeanPrev).^2+dx(nn)^2);
                %Add the orthogonal increment in a squared fashion if above
                %the mean and add. x_mean is drift increment and is linearly added.
            elseif (x(nn)<MeanPrev)
                x(nn)=MeanPrev+x_mean(nn)-sqrt((x(nn)-MeanPrev).^2+dx(nn)^2);
                %Add the orthogonal increment to already negative value and
                %subtract.
            end
        end
    else
        x(1:Nn)=x(1:Nn)+x_mean(1:Nn)+dx(1:Nn); %This is linear addition in
                                %first time step when starting from delta origin.
    end
end
x(NnMidn)=(x(NnMidn+1)+x(NnMidn-1))/2;  %I just made this very quick and bad fix for the
                                %unstable value in the mid. Mid three or
                                %four subdivisions have instability.
for nn=1:Nn
    y_x(nn) = ((1-gamma)*x(nn)).^(1/(1-gamma)); %Convert to original coordinates
end
for nn=2:Nn-1
    Dfx(nn) = (x(nn + 1) - x(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    Dfy_x(nn) = (y_x(nn + 1) - y_x(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    %Change of variable derivative for densities
end

fx(1:Nn)=0;
fy_x(1:Nn)=0;
for nn = 2:Nn-1
    fx(nn) = normpdf(Z(nn),0, 1)/abs(Dfx(nn)); %Bessel process density
    fy_x(nn) = normpdf(Z(nn),0, 1)/abs(Dfy_x(nn));%Origianl coordinates density
end
str=input('Analytic Values Calculated. Press a key to start Monte Carlo');
%Calculate the density with monte carlo below.
rng(85109634, 'twister')
paths=100000;
X(1:paths)=x0^(1-gamma)/(1-gamma); %Bessel process Monte carlo
YY(1:paths)=x0;  %Original process monte carlo.
Random1(1:paths)=0;
for tt=1:Tt
    Random1=randn(size(Random1));
    HermiteP1(1,1:paths)=1;
    HermiteP1(2,1:paths)=Random1(1:paths);
    HermiteP1(3,1:paths)=Random1(1:paths).^2-1;
    HermiteP1(4,1:paths)=Random1(1:paths).^3-3*Random1(1:paths);
    HermiteP1(5,1:paths)=Random1(1:paths).^4-6*Random1(1:paths).^2+3;
    %HermiteP1(6,1:paths)=Random1(1:paths).^5-10*Random1(1:paths).^3+15*Random1(1:paths);
    %HermiteP1(7,1:paths)=Random1(1:paths).^6-15*Random1(1:paths).^4+45*Random1(1:paths).^2-15;
    XX0=X;
    YY0=YY;
    for k = 0 : OrderM
        for m = 0:k
            l4 = k - m + 1;
            for n = 0 : m
                l3 = m - n + 1;
                for j = 0:n
                    l2 = n - j + 1;
                    l1 = j + 1;
                    if(l4<=5)
                    X(1:paths)=X(1:paths) + YqCoeff(l1,l2,l3,l4) * ...
                    mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                    ((1-gamma)*XX0(1:paths)).^(Fp1(l1,l2,l3,l4)/(1-gamma)) .* ...
                    HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);

                %Above is bessel process monte carlo equation.

                    YY(1:paths)=YY(1:paths) + YCoeff(l1,l2,l3,l4) * ...
                    mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                    YY0(1:paths).^Fp(l1,l2,l3,l4) .* HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);
                %Above is original coordinates monte carlo equation.
                    end
                end
            end
        end
    end
end

X(X<0)=0;
sum(X(:))/paths   %monte carlo average for bessel coordinates
sum(x(2:Nn-1).*ZProb(2:Nn-1))  % Ito-Taylor density average for bessel coordinates
sum(y_x(2:Nn-1).*ZProb(2:Nn-1)) %Original process average from coordinates
                                %derived from bessel process
theta+(x0-theta)*exp(-kappa*dt*Tt)%Mean reverting SDE original variable true average

BinSize=.0075;
MaxCutOff=30;
[XDensity,IndexOutX,IndexMaxX] = MakeDensityFromSimulation_Infiniti(X,paths,BinSize,MaxCutOff);
plot(x(2:Nn-1),fx(2:Nn-1),'r',IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'g');
str=input('Look at Bessel graphs comparison between monte carlo density and analytic density');
[YDensity,IndexOutY,IndexMaxY] = MakeDensityFromSimulation_Infiniti(YY,paths,BinSize,MaxCutOff);
plot(y_x(2:Nn-1),fy_x(2:Nn-1),'r',IndexOutY(1:IndexMaxY),YDensity(1:IndexMaxY),'g');
str=input('Look at Original variable graphs comparison between monte carlo and analytic density');
end

% In the expansion of X^alpha
% With SDE
% dX(t)=mu1 * X(t)^beta1 dt + mu2* X(t)^beta2 dt + sigma * X(t)^gamma dz(t)
% The first order expansion of X^alpha with the above SDE is
% X(t+1)^alpha= X(t)^alpha +alpha* X(t)^(alpha-1) * mu1 * X(t)^beta1 *dt
% +alpha* X(t)^(alpha-1) * mu2 * X(t)^beta2 *dt
% + .5* alpha *(alpha-1)* X(t)^(alpha-2) * sigma^2 * X(t)^(2*gamma) *dt
% + alpha * X(t)^(alpha-1) * sigma * X(t)^gamma *dz(t)
% In my program, for the above four term expansion, I use a four dimensional
%array notation that shows the order of differentiation on each of these
%four types of terms. So if l1 represents drift one, l2 represents drift
%two and l3 represents quadratic variation term and l4 represents
%volatility term, we can use the notation Y(l1,l2,l3,l4) for the
%coefficients of expansion of the above term. So in the above first order expansion
% Y(1,0,0,0)= alpha * mu1
% Y(0,1,0,0)=alpha *mu2
% Y(0,0,1,0)= .5* alpha *(alpha-1)* sigma^2
% Y(0,0,0,1)= alpha * sigma
%
% For higher orders of expansion, we will have to carefully compute the
%coefficients separately based on path dependence and then lump them
%together in Y according to array indices. Once we have done that,
%we can write one term of the general expansion as
% Y(l1,l2,l3,l4) * x^(alpha+l1 * beta1 +l2* beta2 +l3* 2* gamma +l4 * gamma
%  - l1 -l2 - 2*l3 -l4) * HermiteP(l4) * dt^(l1 + l2 +l3 + .5*l4);
%
% In my program, since matlab does not take indices starting from zero,
%I have slightly adjusted the above notation.
%In the density simulation program, we pre-compute all coefficients and values
%needed in simulation but we have to calculate the part of above
%expression where power of x is evaluated.
% If we have four terms in Ito-hermite SDE expansion at first order,
%In every next level, each of the four terms would take four descendent
%terms and there will be sixteen terms on second level, and on third level
%there will be 64 descendent terms and 256 descendent terms on fourth level.
%However we can reduce the number of terms in Ito-hermite expansion to
%number of terms in polynomial expansion. For example Ito-hermite expansion
%of SDE with four terms on first order can be reduced to the number of
%terms in expansion of a polynomial with four terms on each level.
%To do this, we will have to pre-calculate the Coefficients carefully and
%the lump them together as in a polynomial like expansion.
% Again the above array Y(l1,l2,l3,l4) is relatively sparse and
%does not take all possible indices. Just like in polynomial expansion,
%on a certain expansion order, it takes only indices so that sum of indices
%goes to expansion order. For example on second order, only those indices
%could be found such that l1+l2+l3+l4=2. And similarly for third ito-hermite
%expansion level only those indices would be populated such that l1+l2+l3+l4=3.
% In order to do that I have done simple loops in a fashion shown below
%
% for k = 0 : (Order4)
%     for m = 0:k
%         l4 = k - m;
%         for n = 0 : m
%             l3 = m - n;
%             for j = 0:n
%                 l2 = n - j;
%                 l1 = j;
% First loop variable is for expansion order. And then rest of the loop
%variables take values such that their sum equals the expansion order.
%When we would add a fifth term in the SDE expansion for example,
%we will have to add another loop variable with the same logic that
%sum of loop variables equal to expansion order. In my matlab program,
%I have given offset to l4, l2,l3, l1 since array indices cannot start at zero.

```

---

### #774 — Amin (Topic Author)
*November 4, 2018, 6:55 PM*

This is how you will see the final graph comparison of the stochastic volatility SDE with monte carlo in green and
analytic density in red. Parameters are

x0=.3, theta=.2,kappa=1.0, gamma=.95,sigma=1.0; and T=.5 years. You can see the slight instability in the middle that
affects middle 3-4 subdivisions.

[![Image](../images/i.postimg.cc/2SSGDFZs/Stoch-Vol-Post-Graph.png)](https://postimages.org/)

---

### #775 — Amin (Topic Author)
*November 4, 2018, 7:48 PM*

Sorry, I missed many supporting matlab files for the program in post 773. I am posting them here.

```
function [Y] = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma)

%In the coefficient calculation program which calculates Y(l1,l2,l3,l4),
%I have used four levels of looping each for relevant expansion order.
%The first loop takes four values and second loop takes 16 values and
%third loop takes 64 values and so on. And then each coefficient
%term can be individually calculated while carefully accounting
%for path dependence.
%So for example in a nested loop structure
%m1= 1:mDim
%  m2=1:mDim
%  m3=1:mDim
%    l(m1)=l(m1)+1;
%    l(m2)=l(m2)+1;
%    l(m3)=l(m3)+1;
%in the above looping loop takes values from one to four with one
%indicating the first drift term, two indicating the second drift term
%and three indicating quadratic variation term and
%four indicating the volatility term. And with this looping structure
%we can So in the above looping m1=1 would mean that all terms are
%descendent of first drift term and m2=4 would mean that all terms are
%descendent of first drift term on first expansion order and descendent
%of volatility term on the second order and so we can keep track of path
%dependence perfectly.
%And on each level, we individually calculate the descendent terms. While
%keeping track of path dependence and calculating the coefficients with
%careful path dependence consideration, we update the appropriate element
%in our polynomial like expansion coefficient array
%explaining the part of code
%m1= 1:mDim
% m2=1:mDim
%  m3=1:mDim
%    l(m1)=l(m1)+1;
%    l(m2)=l(m2)+1;
%    l(m3)=l(m3)+1;
%Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,1,2);
%Here l(1) denotes l1 but written as l(1) so it can be conveniently
%updated with the loop variable when the loop variable takes value one
%indicating first drift term . And l(2) could be conveniently updated when
%the loop variable takes value equal to two indicating second
%drift term and so on.
%Here is the part of code snippet for that
%for m1=1:mDim
%    l(1)=1;
%    l(2)=1;
%    l(3)=1;
%    l(4)=1;
%    l(m1)=l(m1)+1;
%CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma - (l(1)-1) - (l(2)-1) -
2*(l(3)-1) - (l(4)-1);
%    CoeffDX2 = CoeffDX1 - 1;
%    ArrIndex0=m1;
%    ArrIndex=(m1-1)*mDim;
%    Coeff1st=Y1(ArrIndex0)*CoeffDX1;
%    Coeff2nd=Y1(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
%    Y2(1+ArrIndex)=Coeff1st;
%    Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
%    Y2(2+ArrIndex)=Coeff1st;
%    Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
%    Y2(3+ArrIndex)=Coeff2nd;
%    Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,1,2,n1(m1));
%    Y2(4+ArrIndex)=Coeff1st;
%    Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,1,3,n1(m1));

%The first four lines update the array indices according to the parent term.
%And then CoeffDX1 and CoeffDX2 are calculated according to algebraic exponents on parent terms.
%ArrIndex0=m1; calculates the array index of the parent term
%And ArrIndex=(m1-1)*mDim; calculates the array index of the descendent terms
%And coefficient of the drift and volatility descendent terms is
%calculated by multiplying the coefficient of the parent term by
%Coeff1st=Y1(ArrIndex0)*CoeffDX1;
%And coefficient of the quadratic variation descendent terms is
%calculated by multiplying the coefficient of the parent term by
%Coeff2nd=Y1(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
%And then each of the four descendent terms are updated with Coeff1st
%if they are drift or volatility descendent terms or Coeff2nd if
%they are quadratic variation descendent terms.
%Here Y1 indicates the temporary coefficient array with parent terms on
%first level. And Y2 denotes temporary coefficient array with parent terms
%on second level and Y3 indicates temporary coefficient array with parent terms on third level.
[IntegralCoeff,IntegralCoeffdt,IntegralCoeffdz] = ComputeIntegralCoeffs();
n1(1)=2;
n1(2)=2;
n1(3)=2;
n1(4)=3;
%n1(1), n1(2), n1(3) are drift and quadratic variation term variables
%and take a value equal to 2 indicating a dt integral.
%n1(4) is volatility term variable and indicates a dz-integral by taking a
%value of 3.
mDim=4; % four descendent terms in each expansion
Y(1:5,1:5,1:5,1:5)=0;
Y1(1:mDim)=0;
Y2(1:mDim*mDim)=0;
Y3(1:mDim*mDim*mDim)=0;

%First Ito-hermite expansion level starts here. No loops but four
%descendent terms.
l(1)=1;
l(2)=1;
l(3)=1;
l(4)=1;
CoeffDX1 = alpha;
CoeffDX2 = CoeffDX1 - 1;
Coeff1st=CoeffDX1;
Coeff2nd=.5*CoeffDX1*CoeffDX2;
Y1(1)=Coeff1st;
Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,1,2);
Y1(2)=Coeff1st;
Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,1,1,2);
Y1(3)=Coeff2nd;
Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,1,1,2);
Y1(4)=Coeff1st;
Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,1,1,3);
%Second Ito-hermite expansion level starts. It has a loop over four parent
%terms and there are four descendent terms for each parent term.
%The coefficient terms are then lumped in a polynomial-like expansion
%array of coefficients.
for m1=1:mDim
    l(1)=1;
    l(2)=1;
    l(3)=1;
    l(4)=1;
    l(m1)=l(m1)+1;
    CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma ...
                        - (l(1)-1) - (l(2)-1) - 2*(l(3)-1) - (l(4)-1);
    CoeffDX2 = CoeffDX1 - 1;
    ArrIndex0=m1;
    ArrIndex=(m1-1)*mDim;
    Coeff1st=Y1(ArrIndex0)*CoeffDX1;
    Coeff2nd=Y1(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
    Y2(1+ArrIndex)=Coeff1st;
    Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
    Y2(2+ArrIndex)=Coeff1st;
    Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
    Y2(3+ArrIndex)=Coeff2nd;
    Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,1,2,n1(m1));
    Y2(4+ArrIndex)=Coeff1st;
    Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,1,3,n1(m1));
    %Third Ito-hermite expansion level starts and it is a nested loop with
    %a total of sixteen parents and each parent takes four descendent
    %terms.
    for m2=1:mDim
        l(1)=1;
        l(2)=1;
        l(3)=1;
        l(4)=1;
        l(m1)=l(m1)+1;
        l(m2)=l(m2)+1;
        CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma ...
                        - (l(1)-1) - (l(2)-1) - 2*(l(3)-1) - (l(4)-1);
        CoeffDX2=CoeffDX1-1;
        ArrIndex0=(m1-1)*mDim+m2;
        ArrIndex=((m1-1)*mDim+(m2-1))*mDim;
        Coeff1st=Y2(ArrIndex0)*CoeffDX1;
        Coeff2nd=Y2(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
        Y3(1+ArrIndex)=Coeff1st;
        Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,2,n1(m2),n1(m1));
        Y3(2+ArrIndex)=Coeff1st;
        Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,2,n1(m2),n1(m1));
        Y3(3+ArrIndex)=Coeff2nd;
        Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,2,n1(m2),n1(m1));
        Y3(4+ArrIndex)=Coeff1st;
        Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,3,n1(m2),n1(m1));
        %fourht Ito-hermite expansion level starts and it is a triply-nested loop with
        %a total of sixteen parents and each parent takes four descendent
        %terms. We then lump the terms in a relatively sparse polynomial
        %like expansion coefficient array that has smaller number of
        %non-zero terms.
        for m3=1:mDim
            l(1)=1;
            l(2)=1;
            l(3)=1;
            l(4)=1;
            l(m1)=l(m1)+1;
            l(m2)=l(m2)+1;
            l(m3)=l(m3)+1;
            CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma ...
                        - (l(1)-1) - (l(2)-1) - 2*(l(3)-1) - (l(4)-1);
            CoeffDX2=CoeffDX1-1;
            ArrIndex0=((m1-1)*mDim+(m2-1))*mDim+m3;
            %ArrIndex=(((m1-1)*mDim+(m2-1))*mDim+(m3-1))*mDim;
            Coeff1st=Y3(ArrIndex0)*CoeffDX1;
            Coeff2nd=Y3(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
            %Y4(1+ArrIndex)=Coeff1st;
            Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(2,n1(m3),n1(m2),n1(m1));
            %Y4(2+ArrIndex)=Coeff1st;
            Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(2,n1(m3),n1(m2),n1(m1));
            %Y4(3+ArrIndex)=Coeff2nd;
            Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(2,n1(m3),n1(m2),n1(m1));
            %Y4(4+ArrIndex)=Coeff1st;
            Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(3,n1(m3),n1(m2),n1(m1));
         end
    end
end

end

```

Here is the second supporting file.

```
function [IntegralCoeff0,IntegralCoeffdt,IntegralCoeffdz] = ComputeIntegralCoeffs()

IntegralCoeff(1:3,1:3,1:3,1:3)=0;
IntegralCoeffdt(1:3,1:3,1:3,1:3)=0;
IntegralCoeffdz(1:3,1:3,1:3,1:3)=0;
IntegralCoeff0(1:3,1:3,1:3,1:3)=0;
IntegralCoeff0(1,1,1,2)=1;
IntegralCoeff0(1,1,1,3)=1;
IntegralCoeff0(1,1,2,2)=1/2;
IntegralCoeff0(1,1,3,2)=1-1/sqrt(3);
IntegralCoeff0(1,1,2,3)=1/sqrt(3);
IntegralCoeff0(1,1,3,3)=1/2;
IntegralCoeff0(1,2,2,2)=1/6;
IntegralCoeff0(1,3,2,2)=(1-1/sqrt(3))*1/2*(1-1/sqrt(5));
IntegralCoeff0(1,2,3,2)=1/sqrt(3)/2*(1-1/sqrt(5));
IntegralCoeff0(1,3,3,2)=1/2*(1-sqrt(2)/2);
IntegralCoeff0(1,2,2,3)=1/2*1/sqrt(5);
IntegralCoeff0(1,3,2,3)=(1-1/sqrt(3))*1/sqrt(2)*1/2;
IntegralCoeff0(1,2,3,3)=1/sqrt(3)/sqrt(2)*1/(2);
IntegralCoeff0(1,3,3,3)=1/6;
IntegralCoeff0(2,2,2,2)=1/24;
IntegralCoeff0(2,2,3,2)=1/2*1/sqrt(5)*1/3*(1-1/sqrt(7));
IntegralCoeff0(2,3,2,2)=1/sqrt(3)*1/2*(1-1/sqrt(5))*1/3*(1-1/sqrt(7));
IntegralCoeff0(3,2,2,2)=(1-1/sqrt(3))*1/2*(1-1/sqrt(5))*1/3*(1-1/sqrt(7));
IntegralCoeff0(3,3,2,2)=1/2*(1-sqrt(2)/2)*1/2*(1-sqrt(2)/sqrt(6));
IntegralCoeff0(2,3,3,2)=1/sqrt(3)*1/sqrt(2)*1/2*1/2*(1-sqrt(2)/sqrt(6));
IntegralCoeff0(3,2,3,2)=(1-1/sqrt(3))*1/sqrt(2)*1/2*1/2*(1-sqrt(2)/sqrt(6));
IntegralCoeff0(3,3,3,2)=1/6*(1-sqrt(3)/sqrt(5));
IntegralCoeff0(2,2,2,3)=1/6*1/sqrt(7);
IntegralCoeff0(2,2,3,3)=1/2*1/sqrt(5)*1/sqrt(2)*1/sqrt(6);
IntegralCoeff0(2,3,2,3)=1/sqrt(3)*1/2*(1-1/sqrt(5))*1/sqrt(2)*1/sqrt(6);
IntegralCoeff0(3,2,2,3)=(1-1/sqrt(3))*1/2*(1-1/sqrt(5))*1/sqrt(2)*1/sqrt(6);
IntegralCoeff0(3,3,2,3)=1/2*(1-sqrt(2)/2)*1/sqrt(3)*1/sqrt(5);
IntegralCoeff0(2,3,3,3)=1/sqrt(3)*1/sqrt(2)*1/sqrt(4)*1/sqrt(3)*(1/sqrt(5));
IntegralCoeff0(3,2,3,3)=(1-1/sqrt(3))*1/sqrt(2)*1/2*1/sqrt(3)*1/sqrt(5);
IntegralCoeff0(3,3,3,3)=1/24;

%Can also be calculated with algorithm below.
%here IntegralCoeffdt indicates the coefficients of a dt-integral.
%This dt-integral means that you are calculating the Ito-hermite expansion
%of  Integral X(t)^alpha dt with X(t) dynamics given by the SDE
%here IntegralCoeffdz indicates the coefficients of a dz-integral.
%This dz-integral means that you are calculating the Ito-hermite expansion
%of  Integral X(t)^alpha dz(t) with X(t) dynamics given by the SDE
%IntegralCoeff is is associated with expansion of X(t)^alpha.
%IntegralCoeff below is not returned and IntegralCoeff0 manually calculated
%above is returned but both are the same.
l0(1:2)=1;
for m4=1:2
    l0(1)=1;
    l0(2)=1;

    %IntegralCoeff4(m4,1,1,1)=1;
    %IntegralCoeff4(m4,1,1,1)=1;
    %1 is added to m4 since index 1 stands for zero, 2 for one and three
    %for two.
    IntegralCoeff(1,1,1,m4+1)=1;
    l0(m4)=l0(m4)+1;
    IntegralCoeffdt(1,1,1,m4+1)=IntegralCoeff(1,1,1,m4+1)* ...
        1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
    IntegralCoeffdz(1,1,1,m4+1)= IntegralCoeff(1,1,1,m4+1)* ...
        1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
    for m3=1:2
        l0(1)=1;
        l0(2)=1;
        l0(m4)=l0(m4)+1;

        if(m3==1)
            IntegralCoeff(1,1,m4+1,m3+1)=1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
        end
        if(m3==2)
            IntegralCoeff(1,1,m4+1,m3+1)= 1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
        end
        l0(m3)=l0(m3)+1;
        %IntegralCoeff(1,1,m4+1,m3+1)=IntegralCoeff4(m4,m3,1,1);
        IntegralCoeffdt(1,1,m4+1,m3+1)=IntegralCoeff(1,1,m4+1,m3+1)* ...
            1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
        IntegralCoeffdz(1,1,m4+1,m3+1)= IntegralCoeff(1,1,m4+1,m3+1)* ...
            1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
        for m2=1:2
            l0(1)=1;
            l0(2)=1;
            l0(m4)=l0(m4)+1;
            l0(m3)=l0(m3)+1;

            if(m2==1)
               
IntegralCoeff(1,m4+1,m3+1,m2+1)=IntegralCoeff(1,1,m4+1,m3+1)*1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
            end
            if(m2==2)
                IntegralCoeff(1,m4+1,m3+1,m2+1)=
IntegralCoeff(1,1,m4+1,m3+1)*1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
            end
            l0(m2)=l0(m2)+1;
            %IntegralCoeff(1,m4+1,m3+1,m2+1)=IntegralCoeff4(m4,m3,m2,1);
            IntegralCoeffdt(1,m4+1,m3+1,m2+1)=IntegralCoeff(1,m4+1,m3+1,m2+1)* ...
                1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
            IntegralCoeffdz(1,m4+1,m3+1,m2+1)= IntegralCoeff(1,m4+1,m3+1,m2+1)* ...
                1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
            for m1=1:2
                l0(1)=1;
                l0(2)=1;
                l0(m4)=l0(m4)+1;
                l0(m3)=l0(m3)+1;
                l0(m2)=l0(m2)+1;
                if(m1==1)
                   
IntegralCoeff(m4+1,m3+1,m2+1,m1+1)=IntegralCoeff(1,m4+1,m3+1,m2+1)*1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
                end
                if(m1==2)
                    IntegralCoeff(m4+1,m3+1,m2+1,m1+1)=
IntegralCoeff(1,m4+1,m3+1,m2+1)*1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
                end
                l0(m1)=l0(m1)+1;
                %IntegralCoeff(m4+1,m3+1,m2+1,m1+1)=IntegralCoeff4(m4,m3,m2,m1);
                IntegralCoeffdt(m4+1,m3+1,m2+1,m1+1)=IntegralCoeff(m4+1,m3+1,m2+1,m1+1)* ...
                    1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
                IntegralCoeffdz(m4+1,m3+1,m2+1,m1+1)= IntegralCoeff(m4+1,m3+1,m2+1,m1+1)* ...
                    1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
            end
        end
    end
end
end
```

And here is the graphing from monte carlo file.

```
function [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti(X,Paths,BinSize,MaxCutOff )
%Processes monte carlo paths to return a series Xdensity as a function of IndexOut. IndexMax is the maximum value of
index.
%

Xmin=0;
Xmax=0;
for p=1:Paths
if(X(p)>MaxCutOff)
X(p)=MaxCutOff;
end
if(X(p)real(X(p)))
Xmin=real(X(p));
end
if(XmaxIndexMax)
index=IndexMax;
end
XDensity(index)=XDensity(index)+1.0/Paths/BinSize;
end
IndexOut(1:IndexMax)=Xmin+(0:(IndexMax-1))*BinSize;
end

```

---

### #776 — Amin (Topic Author)
*November 7, 2018, 11:07 AM*

I am posting a new version of the program which is quite better than the first version. It still suffers from the
instability issue but to a lesser degree. I have slightly changed the framework and my purpose for posting new code is
that anybody who wants to totally finesse the program and remove any instability will have a far better starting
version. One reminder is that you can easily simulate any SDE of the form

dx(t)=mu1 X(t)^beta1 dt + mu2 X(t)^beta2 dt+ sigma dz(t);

I have simulated the Bessel transformed form of the above SDE and the program automatically converts the above SDE to
original coordinates after simulating the Bessel process.

Here is the code.

```
function [] = ItoTaylorDensityWilmottSimplev3()
%Copyright Ahsan Amin. Infiniti derivatives Technologies.
%Please fell free to connect on linkedin: linkedin.com/in/ahsan-amin-0a53334
%or skype ahsan.amin2999
%In this program, I am simulating the SDE given as
%dy(t)=kappa(theta-y(t))*dt + y(t)^gamma dz(t);
%I have not directly simulated the SDE but simulated the transformed
%Bessel process version of the SDE and then changed coordinates to retreive
%the SDE in original coordinates.
%The present program will directly simulate only the Bessel Process version of the
%SDE in transformed coordinates.
%The program has instability in 3-4 subdivisions in the mid of the density
%and I will be relasing a program in another few days taking care of that
%and fixing the problem. You can do it on your own as well.
dt=.125/2;   % Simulation time interval.
Tt=8;     % Number of simulation levels. Terminal time= Tt*dt;
OrderA=4;  %expansion order for the analytic SDE.
OrderM=4;  %expansion order for the monte carlo simulation.
dNn=.1/1;   % Normal density width. would change with number of subdivisions
Nn=80;  % No of normal density subdivisions
%NnMidn=81;%Median cell/subdivision.
NnMidl=40;
NnMidh=41;
NnMid=4.0;
x0=.250;   % starting value of SDE
beta1=0.0;   % the first drift term power.
beta2=1.0;   % Second drift term power.
gamma=.950;   % volatility power. Before you change this to values where
            %diffusion goes to zero, you will have to change the
            %calculation of the mean of the density in the body of the program
            %do not decrease it more than .75 before changing that.
kappa=.750;   %mean reversion parameter.
theta=.150;   %mean reversion target
mu1=1*theta*kappa;   % first drift coefficient.
mu2=-1*kappa;    % Second drift coefficient.
sigma0=1.0;%Volatility value
alpha=1.0;% x^alpha is being expanded
alpha1=1-gamma;%For the expansion in transformed coordinates.

for nn=1:Nn
    x(nn)=x0^(1-gamma)/(1-gamma); %Initial value is assigned to each
                                  %subdivision in transformed coordinates.
end
%Please read notes at the end of the program for understanding of what is
%Y(l1,l2,l3,l4) and what are l1,l2, l3 and l4. In the ItoTaylor expansion
%l1 is first drift term expansion order index, l2 is for the second drift
%term, l3 is for quadratic variation drift term index and l4 is the
%volatility expansion order index.
%These sigma11, mu11, mu22, sigma22 can be lumped with Y(l1,l2,l3,l4) but I
%kept them separate for a general program where these values could change
%on every step while exponents on x in each term would remain same in
%pre-calcualted Y(l1,l2,l3,l4)
sigma11(1:OrderA+1)=0;
mu11(1:OrderA+1)=0;
mu22(1:OrderA+1)=0;
sigma22(1:OrderA+1)=0;
% index 1 correponds to zero level since matlab indexing starts at one.
sigma11(1)=1;
mu11(1)=1;
mu22(1)=1;
sigma22(1)=1;

for k=1:(OrderA+1)
    if sigma0~=0
        sigma11(k)=sigma0^(k-1);
    end
    if mu1 ~= 0
        mu11(k)=mu1^(k-1);
    end
    if mu2 ~= 0
        mu22(k)=mu2^(k-1);
    end
    if sigma0~=0
        sigma22(k)=sigma0^(2*(k-1));
    end
end
Ft(1:Tt+1,1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;
Fp(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;
Fp1(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;
%Pre-compute the time and power exponent values in small multi-dimensional arrays
for k = 0 : (OrderA)
    for m = 0:k
        l4 = k - m + 1;
        for n = 0 : m
            l3 = m - n + 1;
            for j = 0:n
                l2 = n - j + 1;
                l1 = j + 1;
                Ft(l1,l2,l3,l4) = dt^((l1-1) + (l2-1) + (l3-1) + .5* (l4-1));
                Fp(l1,l2,l3,l4) = (alpha + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
                Fp1(l1,l2,l3,l4) = (alpha1 + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
            end
        end
    end
end

for nn=1:Nn
    Z(nn)=((nn-.5)*dNn-NnMid);
end
%Z
%str=input('Show Z');
ZProb(1)=normcdf(.5*Z(1)+.5*Z(2),0,1);
ZProb(Nn)=1-normcdf(.5*Z(Nn)+.5*Z(Nn-1),0,1);
for nn=2:Nn-1
    ZProb(nn)=normcdf(.5*Z(nn)+.5*Z(nn+1),0,1)-normcdf(.5*Z(nn)+.5*Z(nn-1),0,1);
end
%Below call the program that calculates the Ito-Taylor coeffs.
YCoeff = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma);
%The routine below calls the Ito-Taylor Coeffs in transformed coordinates
%and uses alpha1 as the power where alpha1=1-gamma.
Yq=ItoTaylorCoeffsNew(alpha1,beta1,beta2,gamma);
YqCoeff=Yq/(1-gamma);%These coordinates are divided by (1-gamma)
Y(1,1,1,1)=0;
CC(1:Nn)=0;
for nn=1:Nn
    Z(nn)=((nn-.5)*dNn-NnMid);%*Rho1(nn);
    HermiteP(1,nn)=0;
    HermiteP(2,nn)=Z(nn);%rho1(nn)
    HermiteP(3,nn)=(Z(nn)^2-1);%rho2(nn)
    HermiteP(4,nn)=(Z(nn)^3-3*Z(nn));
    HermiteP(5,nn)=(Z(nn)^4-6*Z(nn)^2+3);
end
for tt=1:Tt
    for nn=1:Nn
        x1(nn)=x(nn);
        x_mean(nn)=0;
        for m = 0 : OrderA
           for n = 0 : m
               l3 = m - n + 1;
               for j = 0:n
                   l2 = n - j + 1;
                   l1 = j + 1;
                   x_mean(nn)=x_mean(nn) + YqCoeff(l1,l2,l3,l4) .* ...
                        mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4).* ...
                        ((1-gamma)*x(nn)).^(Fp1(l1,l2,l3,l4)/(1-gamma)) .* Ft(l1,l2,l3,l4);
                        %x_mean calculates the total drift from combination
                        %of three drift terms in their Ito-Taylor
                        %expansion.
                        %((1-gamma)*x(nn)).^(Fp1(l1,l2,l3,l4)/(1-gamma)) is
                        %term for the original untransformed SDE variable.
                        %This is basically ODE for each subdivision where
                        %initial value of ODE is reset at each time level
                        %after addition of diffusion increment fro previous
                        %time levelthat is different for each subdivision.
                  %      end
               end
           end
        end
        dx(nn)= +sigma0*HermiteP(2,nn)*sqrt(dt);
                        %We are not taking any cross terms for the drift
                        %and volatility and have just added one constant
                        %volatility terms that occurs in the Bessel
                        %transformed SDE.

    end
    if(tt>1)

        %For first step when starting from delta origin, we do not
              %want squared orthogonal addition for volatility.
        MeanPrev=sum(ZProb(1:Nn).*x(1:Nn));%Mean of the ODE from previous step
        x_meanAvg=sum(ZProb(1:Nn).*x_mean(1:Nn));
        %MeanPrev=.5*x(NnMidl)+.5*x(NnMidh);
        %MeanPrev=.5*MeanPrev+.5*MeanPrev0;
        %Please be careful, when working with diffusion exponents that go
        %negative, this simple calculation of the mean will corrupt the
        %whole program when all sort of negative and imaginary values are
        %used to calculate the mean. For that case, you will have to
        %carefully take the mean with only values that are on positive real
        %axis.
        MeanPrev=sum(ZProb(1:Nn).*x(1:Nn));

        %MeanPrev
        for nn=1:Nn
            if(x(nn)>=MeanPrev)
                sign_x(nn)=1;
            else
                sign_x(nn)=-1;
            end
            if(dx(nn)>=0.0)
                sign_dx(nn)=1;
            else
                sign_dx(nn)=-1;
            end
            if(x_mean(nn)>=x_meanAvg)
                sign_x_mean(nn)=1;
            else
                sign_x_mean(nn)=-1;
            end
            if((x(nn)-MeanPrev)+dx(nn)>=0)
                sign_Sum(nn)=+1;
            else
                sign_Sum(nn)=-1;
            end
            sign_Sum(nn)=sign_x(nn);
        end

        x_0(1:Nn)=x(1:Nn);
        for nn=1:Nn
            %This is the squared addition for t>1 time steps.
            x(nn)=MeanPrev+x_mean(nn)+sign_Sum(nn).*sqrt(abs(sign_x(nn)*  ...
                (x(nn)-MeanPrev).^2+sign_dx(nn).*dx(nn).^2));
        end

    else
        x(1:Nn)=x(1:Nn)+x_mean(1:Nn)+dx(1:Nn); %This is linear addition in
                                %first time step when starting from delta origin.
    end
end
%x(NnMidn)=(x(NnMidn+1)+x(NnMidn-1))/2;  %I just made this very quick and bad fix for the
                                %unstable value in the mid. Mid three or
                                %four subdivisions have instability.
for nn=1:Nn
    y_x(nn) = ((1-gamma)*x(nn)).^(1/(1-gamma)); %Convert to original coordinates
end
for nn=2:Nn-1
    Dfx(nn) = (x(nn + 1) - x(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    Dfy_x(nn) = (y_x(nn + 1) - y_x(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    %Change of variable derivative for densities
end

fx(1:Nn)=0;
fy_x(1:Nn)=0;
for nn = 2:Nn-1
    fx(nn) = normpdf(Z(nn),0, 1)/abs(Dfx(nn)); %Bessel process density
    fy_x(nn) = normpdf(Z(nn),0, 1)/abs(Dfy_x(nn));%Origianl coordinates density
end
str=input('Analytic Values Calculated. Press a key to start Monte Carlo');
%Calculate the density with monte carlo below.
rng(85109634, 'twister')
paths=100000;
X(1:paths)=x0^(1-gamma)/(1-gamma); %Bessel process Monte carlo
YY(1:paths)=x0;  %Original process monte carlo.
Random1(1:paths)=0;
for tt=1:Tt
    Random1=randn(size(Random1));
    HermiteP1(1,1:paths)=1;
    HermiteP1(2,1:paths)=Random1(1:paths);
    HermiteP1(3,1:paths)=Random1(1:paths).^2-1;
    HermiteP1(4,1:paths)=Random1(1:paths).^3-3*Random1(1:paths);
    HermiteP1(5,1:paths)=Random1(1:paths).^4-6*Random1(1:paths).^2+3;
    %HermiteP1(6,1:paths)=Random1(1:paths).^5-10*Random1(1:paths).^3+15*Random1(1:paths);
    %HermiteP1(7,1:paths)=Random1(1:paths).^6-15*Random1(1:paths).^4+45*Random1(1:paths).^2-15;
    XX0=X;
    YY0=YY;
    for k = 0 : OrderM
        for m = 0:k
            l4 = k - m + 1;
            for n = 0 : m
                l3 = m - n + 1;
                for j = 0:n
                    l2 = n - j + 1;
                    l1 = j + 1;
                    if(l4<=5)
                    X(1:paths)=X(1:paths) + YqCoeff(l1,l2,l3,l4) * ...
                    mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                    ((1-gamma)*XX0(1:paths)).^(Fp1(l1,l2,l3,l4)/(1-gamma)) .* ...
                    HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);

                %Above is bessel process monte carlo equation.

                    YY(1:paths)=YY(1:paths) + YCoeff(l1,l2,l3,l4) * ...
                    mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                    YY0(1:paths).^Fp(l1,l2,l3,l4) .* HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);
                %Above is original coordinates monte carlo equation.
                    end
                end
            end
        end
    end
end

X(X<0)=0;
sum(X(:))/paths   %monte carlo average for bessel coordinates
sum(x(2:Nn-1).*ZProb(2:Nn-1))  % Ito-Taylor density average for bessel coordinates
sum(y_x(2:Nn-1).*ZProb(2:Nn-1)) %Original process average from coordinates
                                %derived from bessel process
theta+(x0-theta)*exp(-kappa*dt*Tt)%Mean reverting SDE original variable true average

BinSize=.0075;
MaxCutOff=30;
[XDensity,IndexOutX,IndexMaxX] = MakeDensityFromSimulation_Infiniti(X,paths,BinSize,MaxCutOff);
plot(x(2:Nn-1),fx(2:Nn-1),'r',IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'g');
str=input('Look at Bessel graphs comparison between monte carlo density and analytic density');
[YDensity,IndexOutY,IndexMaxY] = MakeDensityFromSimulation_Infiniti(YY,paths,BinSize,MaxCutOff);
plot(y_x(2:Nn-1),fy_x(2:Nn-1),'r',IndexOutY(1:IndexMaxY),YDensity(1:IndexMaxY),'g');
str=input('Look at Original variable graphs comparison between monte carlo and analytic density');
end

% In the expansion of X^alpha
% With SDE
% dX(t)=mu1 * X(t)^beta1 dt + mu2* X(t)^beta2 dt + sigma * X(t)^gamma dz(t)
% The first order expansion of X^alpha with the above SDE is
% X(t+1)^alpha= X(t)^alpha +alpha* X(t)^(alpha-1) * mu1 * X(t)^beta1 *dt
% +alpha* X(t)^(alpha-1) * mu2 * X(t)^beta2 *dt
% + .5* alpha *(alpha-1)* X(t)^(alpha-2) * sigma^2 * X(t)^(2*gamma) *dt
% + alpha * X(t)^(alpha-1) * sigma * X(t)^gamma *dz(t)
% In my program, for the above four term expansion, I use a four dimensional
%array notation that shows the order of differentiation on each of these
%four types of terms. So if l1 represents drift one, l2 represents drift
%two and l3 represents quadratic variation term and l4 represents
%volatility term, we can use the notation Y(l1,l2,l3,l4) for the
%coefficients of expansion of the above term. So in the above first order expansion
% Y(1,0,0,0)= alpha * mu1
% Y(0,1,0,0)=alpha *mu2
% Y(0,0,1,0)= .5* alpha *(alpha-1)* sigma^2
% Y(0,0,0,1)= alpha * sigma
%
% For higher orders of expansion, we will have to carefully compute the
%coefficients separately based on path dependence and then lump them
%together in Y according to array indices. Once we have done that,
%we can write one term of the general expansion as
% Y(l1,l2,l3,l4) * x^(alpha+l1 * beta1 +l2* beta2 +l3* 2* gamma +l4 * gamma
%  - l1 -l2 - 2*l3 -l4) * HermiteP(l4) * dt^(l1 + l2 +l3 + .5*l4);
%
% In my program, since matlab does not take indices starting from zero,
%I have slightly adjusted the above notation.
%In the density simulation program, we pre-compute all coefficients and values
%needed in simulation but we have to calculate the part of above
%expression where power of x is evaluated.
% If we have four terms in Ito-hermite SDE expansion at first order,
%In every next level, each of the four terms would take four descendent
%terms and there will be sixteen terms on second level, and on third level
%there will be 64 descendent terms and 256 descendent terms on fourth level.
%However we can reduce the number of terms in Ito-hermite expansion to
%number of terms in polynomial expansion. For example Ito-hermite expansion
%of SDE with four terms on first order can be reduced to the number of
%terms in expansion of a polynomial with four terms on each level.
%To do this, we will have to pre-calculate the Coefficients carefully and
%the lump them together as in a polynomial like expansion.
% Again the above array Y(l1,l2,l3,l4) is relatively sparse and
%does not take all possible indices. Just like in polynomial expansion,
%on a certain expansion order, it takes only indices so that sum of indices
%goes to expansion order. For example on second order, only those indices
%could be found such that l1+l2+l3+l4=2. And similarly for third ito-hermite
%expansion level only those indices would be populated such that l1+l2+l3+l4=3.
% In order to do that I have done simple loops in a fashion shown below
%
% for k = 0 : (Order4)
%     for m = 0:k
%         l4 = k - m;
%         for n = 0 : m
%             l3 = m - n;
%             for j = 0:n
%                 l2 = n - j;
%                 l1 = j;
% First loop variable is for expansion order. And then rest of the loop
%variables take values such that their sum equals the expansion order.
%When we would add a fifth term in the SDE expansion for example,
%we will have to add another loop variable with the same logic that
%sum of loop variables equal to expansion order. In my matlab program,
%I have given offset to l4, l2,l3, l1 since array indices cannot start at zero.

```

---

### #777 — Amin (Topic Author)
*December 11, 2018, 7:43 PM*

Sorry Bad post.

---

### #778 — Amin (Topic Author)
*January 14, 2019, 10:06 PM*

We know that normal distribution and its transformations are known by Normal distribution's standard deviations. We can
find CDF of any transformation of normal density by knowing the associated standard deviation.

We have that

                    Standard deviations=$Z(x,t)=\frac{x-\int_{t_0}^{t} \mu(x) dt}{\sqrt{\int_{t_0}^t {\sigma(x)}^2 dt}}$

When we are moving on a particular standard deviation line we have

                                                    $\Delta Z(x,t)=0$

For that to happen, we must have

$\Delta Z(x,t)=\frac{\partial Z}{\partial x} \Delta x + \frac{\partial Z}{\partial t} \Delta t=0$

or in order to remain on the same standard deviation line, we can move in x direction in time$\Delta t$ by magnitude
given as

$\frac{\Delta x}{\Delta t}=-\frac{\frac{\partial Z}{\partial t}}{\frac{\partial Z}{\partial x}}$

where

$\frac{\partial Z}{\partial x}=\frac{1-\frac{\partial \int_{t_0}^{t} \mu(x) dt}{\partial x}}{\sqrt{\int_{t_0}^t {\sigma(x)}^2 dt}}-(\frac{x-\int_{t_0}^{t} \mu(x) dt}{({\int_{t_0}^t {\sigma(x)}^2 dt})^{(-3/2)}}) \frac{\partial {\int_{t_0}^{t} {\sigma(x)}^2 dt}}{\partial x}$

and

$\frac{\partial Z}{\partial t}=\frac{-\frac{\partial \int_{t_0}^{t} \mu(x) dt}{\partial t}}{\sqrt{\int_{t_0}^t {\sigma(x)}^2 dt}}-(\frac{x-\int_{t_0}^{t} \mu(x) dt}{({\int_{t_0}^t {\sigma(x)}^2 dt})^{(-3/2)}})\frac{\partial {\int_{t_0}^{t} {\sigma(x)}^2 dt}}{\partial t}$

all the integrals of the type$\frac{\partial \int_{t_0}^{t} \mu(x) dt}{\partial x}$ ,
$\frac{\partial \int_{t_0}^{t} \mu(x) dt}{\partial t}$ ,$ \frac{\partial {\int_{t_0}^{t} {\sigma(x)}^2 dt}}{\partial x}$
and$ \frac{\partial {\int_{t_0}^{t} {\sigma(x)}^2 dt}}{\partial t}$

can be calculated from previous stochastic analysis.

Soon I hope to post a program based on the above analysis.

---

### #779 — Amin (Topic Author)
*January 21, 2019, 7:18 PM*

Here is derivation of an interesting density simulation scheme for simpler SDEs. In this scheme we continue to calculate
drift and integrated vol on Standard deviation or constant CDF lines and continue to project the density into time. Ok
here we go

On a certain constant CDF line, we have

$Z=\frac{x_2-\int_{0}^{t_2} \mu(x,t) dt - x_0}{\sqrt{\int_0^{t_2} \sigma(x,t)^2 dt}}$                 Eq(1)

suppose $x_1$ is another point that lies on the same constant CDF line at time $t_1$ so we must also have

$Z=\frac{x_1-\int_0^{t_1} \mu(x,t) dt -x_0}{\sqrt{\int_0^{t_1} \sigma(x,t)^2 dt}}$                     Eq(2)

From Eq(1), we do some algebra and we have that Eq(1) can also be written as

$Z=\frac{x_2-\int_0^{t_1} \mu(x,t) dt - \int_{t_1}^{t_2}\mu(x,t) dt + x_1 -x_1 -x_0}{\sqrt{\int_{0}^{t_2} \sigma(x,t)^2 dt}}$

We can further write the above expression as

$\frac{x_2-\int_{t_1}^{t_2} mu(x,t) dt}{\sqrt{\int_0^{t_2}\sigma(x,t)^2 dt}} - \frac{x_1-\int_0^{t_1} mu(x,t) dt -x_0}{\sqrt{\int_0^{t_2}\sigma(x,t)^2 dt}} =Z$

We divide the numerator and denominator of second term both by$\sqrt{\int_0^{t_1} \sigma(x,t)^2 dt}$ and multiply both
sides of the total equation by$\sqrt{\int_0^{t_2} \sigma(x,t)^2 dt}$ to get the expression

$x_2-\int_{t_1}^{t_2} \mu(x,t) dt -x_1 + \sqrt{\int_0^{t_1} \sigma(x,t)^2 dt} \frac{x_1-\int_0^{t_1} \mu(x,t) dt -x_0}{\sqrt{\int_0^{t_1} \sigma(x,t)^2 dt}} =\sqrt{\int_0^{t_2}\sigma(x,t)^2 dt}  Z$

but from Eq(2) we also have

$x_2 -\int_{t_1}^{t_2} \mu(x,t) dt -x_1 + \sqrt{\int_0^{t_1} \sigma(x,t)^2 dt } Z = \sqrt{\int_0^{t_2} \sigma(x,t)^2 dt } Z$

So our density simulation scheme becomes along a particular CDF line Z(n), we have after a minor change of notation

$x(t_2)=x(t_1) + \int_{t_1}^{t_2} \mu(x,t) dt - \sqrt{\int_0^{t_1} \sigma(x,t)^2 dt } Z(n) + \sqrt{\int_0^{t_2} \sigma(x,t)^2 dt } Z(n)$

This is very handy since we can continue to travel along the nth CDF line and continue to calculate drift and integrated
volatility on the same line and continue to evolve into time. In higher dimensions, this just needs integrated
volatility net of correlations so very simple to evolve density in higher dimensions as well.

---

### #780 — Amin (Topic Author)
*January 22, 2019, 3:07 PM*

What I have posted in the previous message seems to hold true in Bessel Coordinates for diffusions that do not have
extreme non-linearities like mean-reverting SDEs and other non-linear SDEs. It does work for non-linear mean-reverting
diffusions for smaller times but then starts to lose accuracy with increasing time. It does not seem to hold in the
original coordinates for CEV type diffusions. I will soon be posting a program that will give a better idea for friends
interested in this.

---

### #781 — Amin (Topic Author)
*January 28, 2019, 2:44 PM*

I am testing two methods in this program.1. Integral of the squared vol method.

2. Squared orthogonal increments method.

Second method is far more accurate but suffers from instability in the mid of the SDE density. I have ideas how to fix
it and will soon be uploading

a better version of this. I have earlier posted dependencies of this program but will post them again in a few hours.

```
function [] = ItoTaylorDensityWilmottSimplev12()
%Copyright Ahsan Amin. Infiniti derivatives Technologies.
%Please fell free to connect on linkedin: linkedin.com/in/ahsan-amin-0a53334
%or skype ahsan.amin2999
%In this program, I am simulating the SDE given as
%dy(t)=mu1 x(t)^beta1 dt + mu2 x(t)^beta2 dt +sigma x(t)^gamma dz(t)
%I have not directly simulated the SDE but simulated the transformed
%Bessel process version of the SDE and then changed coordinates to retreive
%the SDE in original coordinates.
%The present program will directly simulate only the Bessel Process version of the
%SDE in transformed coordinates.
%The program has instability in 3-4 subdivisions in the mid of the density
%and I will be relasing a program in another few days taking care of that
%and fixing the problem. You can do it on your own as well.
% I am testing two methods.1. Integral of the squared vol method.
% 2. Squared orthogonal increments method.
%Second method is far more accurate but suffers from instability in the mid
%of the SDE density. I have ideas how to fix it and will soon be uploading
%a better version of this.
dt=.125/4;   % Simulation time interval.
Tt=32;     % Number of simulation levels. Terminal time= Tt*dt;
OrderA=4;  %expansion order for the analytic SDE.
OrderM=4;  %expansion order for the monte carlo simulation.
%Due to variable declaration constrint is that orderA>=OrderM.
%Current max expansion order is 4.
dNn=.1/1;   % Normal density width. would change with number of subdivisions
Nn=80;  % No of normal density subdivisions
%NnMidn=81;%Median cell/subdivision.
NnMidl=40;
NnMidh=41;

NnMid=4.0;
x0=1.0;   % starting value of SDE

beta1=0.0;   % the first drift term power.
beta2=1.0;   % Second drift term power.
gamma=.550;   % volatility power.
kappa=.80;   %mean reversion parameter.
theta=1.0;   %mean reversion target
%Below you can get rid of kappa and theta and freely choose your own values
%for both drift coefficients.
mu1=0*theta*kappa;   % first drift coefficient.
mu2=-1*kappa;    % Second drift coefficient.
sigma0=.650;%Volatility value
alpha=1;% x^alpha is being expanded
alpha1=1-gamma;%For the expansion in transformed coordinates.

for nn=1:Nn
    x(nn)=x0^(1-gamma)/(1-gamma); %Initial value is assigned to each
                                  %subdivision in transformed bessel
                                  %coordinates.
    y(nn)=x0;
    w(nn)=x0^(1-gamma)/(1-gamma);
end
%Please read notes at the end of the program for understanding of what is
%Y(l1,l2,l3,l4) and what are l1,l2, l3 and l4. In the ItoTaylor expansion
%l1 is first drift term expansion order index, l2 is for the second drift
%term, l3 is for quadratic variation drift term index and l4 is the
%volatility expansion order index.
%These sigma11, mu11, mu22, sigma22 can be lumped with Y(l1,l2,l3,l4) but I
%kept them separate for a general program where these values could change
%on every step while exponents on x in each term would remain same in
%pre-calcualted Y(l1,l2,l3,l4)
sigma11(1:OrderA+1)=0;
mu11(1:OrderA+1)=0;
mu22(1:OrderA+1)=0;
sigma22(1:OrderA+1)=0;
% index 1 correponds to zero level since matlab indexing starts at one.
sigma11(1)=1;
mu11(1)=1;
mu22(1)=1;
sigma22(1)=1;

for k=1:(OrderA+1)
    if sigma0~=0
        sigma11(k)=sigma0^(k-1);
    end
    if mu1 ~= 0
        mu11(k)=mu1^(k-1);
    end
    if mu2 ~= 0
        mu22(k)=mu2^(k-1);
    end
    if sigma0~=0
        sigma22(k)=sigma0^(2*(k-1));
    end
end
Ft(1:Tt+1,1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0; %General time powers on hermite polynomials
Fp(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers on coefficients of hermite polynomials.
Fp1(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers for bessel transformed coordinates.
%Pre-compute the time and power exponent values in small multi-dimensional arrays
for k = 0 : (OrderA+1)
    for m = 0:k
        l4 = k - m + 1;
        for n = 0 : m
            l3 = m - n + 1;
            for j = 0:n
                l2 = n - j + 1;
                l1 = j + 1;
                Ft(l1,l2,l3,l4) = dt^((l1-1) + (l2-1) + (l3-1) + .5* (l4-1));
                Fp(l1,l2,l3,l4) = (alpha + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
                %Below power uses alpha1 associated with bessel
                %coordinates. alpha1 is initial power being expanded. It will be further divided by (1-gamma)
                %When used in the body of the program.
                Fp1(l1,l2,l3,l4) = (alpha1 + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
            end
        end
    end
end

for nn=1:Nn
    Z(nn)=((nn-.5)*dNn-NnMid);
end
%Z
%str=input('Show Z');
ZProb(1)=normcdf(.5*Z(1)+.5*Z(2),0,1);
ZProb(Nn)=1-normcdf(.5*Z(Nn)+.5*Z(Nn-1),0,1);
for nn=2:Nn-1
    ZProb(nn)=normcdf(.5*Z(nn)+.5*Z(nn+1),0,1)-normcdf(.5*Z(nn)+.5*Z(nn-1),0,1);
    %Above calculate probability mass in each probability subdivision.
end
%Below call the program that calculates the Ito-Taylor coeffs.
YCoeff = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma);
%The routine below calls the Ito-Taylor Coeffs in transformed coordinates
%and uses alpha1 as the power where alpha1=1-gamma.
Yq=ItoTaylorCoeffsNew(alpha1,beta1,beta2,gamma);
YqCoeff=Yq/(1-gamma);%These coordinates are divided by (1-gamma)

for nn=1:Nn
    Z(nn)=((nn-.5)*dNn-NnMid);%*Rho1(nn);
    HermiteP(1,nn)=0;
    HermiteP(2,nn)=Z(nn);%rho1(nn)
    HermiteP(3,nn)=(Z(nn)^2-1);%rho2(nn)
    HermiteP(4,nn)=(Z(nn)^3-3*Z(nn));
    HermiteP(5,nn)=(Z(nn)^4-6*Z(nn)^2+3);

end
    HermiteVar(1)=0;
    HermiteVar(2)=1;%rho1(nn)
    HermiteVar(3)=2;%rho2(nn)
    HermiteVar(4)=6;
    HermiteVar(5)=24;
    HermiteVar(6)=120;
    HermiteVar(7)=720;
    HermiteVar(8)=720*7;
    HermiteVar(9)=720*7*8;
nStart=1;
wnStart=1;

for tt=1:Tt
    for nn=1:Nn
        x1(nn)=x(nn);
        if(tt==1)
        Sigma2dt(nn)=0.0;
        Sigma22dt(nn)=0.0;
        Sigma2dtPrev(nn)=0.0;
        end
         Mu0dt(nn)=0.0;

         wMu0dt(nn)=0.0;

        Sigma2dtPrev(nn)=.5*Sigma2dt(nn)+.5*Sigma22dt(nn);
        for k = 0 : OrderA
            for m = 0:k
                l4 = k - m + 1;
                for n = 0 : m
                    l3 = m - n + 1;
                    for j = 0:n
                        l2 = n - j + 1;
                        l1 = j + 1;
                        if(l4=2)

                        %%Sigma2dt integrates over time. It is squared vol
                        %%associated with bessel rpocess and used for
                        %%integral of vol method.
                        Sigma2dt(nn)=Sigma2dt(nn) + YqCoeff(l1,l2,l3,l4).^2 .* ...
                            (mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)).^2.* ...
                            ((1-gamma)*x(nn)).^(2*Fp1(l1,l2,l3,l4)/(1-gamma)) .* ...
                            HermiteVar(l4) .* Ft(l1,l2,l3,l4).^2;

                        end
                    end
                end
            end
        end
        dw(nn)=sigma0*sqrt(dt)*Z(nn);

%Below are intermediate calculations for integral of vol method.
   if(tt==1)
       x2(nn)=x0^(1-gamma)/(1-gamma)+ Mu0dt(nn) + sqrt(Sigma2dt(nn))*Z(nn);

   end
   if(tt>1)
       x2(nn)=x1(nn)+ Mu0dt(nn) + (sqrt(Sigma2dt(nn))-sqrt(Sigma2dtPrev(nn)))*Z(nn);
   end
 %Below I tried some sort of predictor corrector but it does not seem to
 %have much benefit.

   Mu2dt(nn)=0.0;
   %Sigma22dt(nn)=0.0;
         for k = 0 : OrderA
             for m = 0:k
                 l4 = k - m + 1;
                 for n = 0 : m
                     l3 = m - n + 1;
                     for j = 0:n
                         l2 = n - j + 1;
                         l1 = j + 1;
                         if(l4=2)

                        %%Sigma2dt integrates over time
                        Sigma22dt(nn)=Sigma22dt(nn) + YqCoeff(l1,l2,l3,l4).^2 .* ...
                            (mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)).^2.* ...
                            ((1-gamma)*x2(nn)).^(2*Fp1(l1,l2,l3,l4)/(1-gamma)) .* ...
                            HermiteVar(l4) .* Ft(l1,l2,l3,l4).^2;

                        end
                    end
                end
            end
        end
   %Below I have advanced the value of bessel cooridinates variable in
   %squared vol method.
   if(tt==1)
       x(nn)=x0^(1-gamma)/(1-gamma)+ .5*(Mu0dt(nn)+Mu2dt(nn)) + sqrt(Sigma2dt(nn))*Z(nn);
   end
   if(tt>1)
       x(nn)=x1(nn)+.5* (Mu2dt(nn)+Mu0dt(nn)) + (sqrt(.5*Sigma2dt(nn)+.5*Sigma22dt(nn))-sqrt(Sigma2dtPrev(nn)))*Z(nn);
   end

    end
    EnterLoop1=1;
    EnterLoop2=1;
    for nn=Nn-1:-1:nStart
        %First loop makes sure that values are monotonic and the values
        %very close to zero that become unbounded are turned to zero.
        if((x(nn)>x(nn+1))&&(EnterLoop1==1))
            x(1:nn)=0;
            nStart=nn+1;
            EnterLoop1=0;
        end
        %Second loop makes sure that values smaller than zero that would
        %become complex are turned to zero.
        if((x(nn)0)
        w(isnan(w)==1)=0;
        wMu0dt(isnan(wMu0dt)==1)=0;
        wMeanPrev=sum(ZProb(wnStart:Nn).*w(wnStart:Nn));%Calculate the mean.

        for nn=wnStart:Nn
            if(w(nn)>=wMeanPrev)
                sign_w(nn)=1;
            else
                sign_w(nn)=-1;
            end

            if(dw(nn)>=0.0)
                sign_dw(nn)=1;
            else
                sign_dw(nn)=-1;
            end
            if((w(nn)-wMeanPrev)+dw(nn)>=0)
                sign_Sum(nn)=+1;
            else
                sign_Sum(nn)=-1;
            end

        end

        for nn=wnStart:Nn
            %This is the squared addition for t>0 time steps.
            w(nn)=wMeanPrev+wMu0dt(nn)+sign_Sum(nn).*sqrt(abs(sign_w(nn)*  ...
                (w(nn)-wMeanPrev).^2+sign_dw(nn).*dw(nn).^2));

        end

    EnterLoop1=1;
    EnterLoop2=1;
    for nn=Nn-1:-1:wnStart
        %Makes sure values decrease monotonically close to zero.
        if((w(nn)>w(nn+1))&&(EnterLoop1==1))
            w(1:nn)=0;
            wnStart=nn+1;
            EnterLoop1=0;
        end
        %Makes sure values are not smaller than zero.
        if((w(nn)<0)&&(EnterLoop2==1))
            w(1:nn)=0.0;
            wnStart=nn+1;
            EnterLoop2=0;
        end
    end

    end

end
%x(x<0)=0.0;
for nn=nStart+1:Nn
    y_x(nn) = ((1-gamma)*x(nn)).^(1/(1-gamma)); %Convert squared vol values
    %from bessel to original coordinates
    y_w(nn) = ((1-gamma)*w(nn)).^(1/(1-gamma)); %Convert squared orthogonal
    %increment method values from bessel to original coordinates
end
for nn=2:Nn-1
    Dfx(nn) = (x(nn + 1) - x(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    Dfw(nn) = (w(nn + 1) - w(nn - 1))/(Z(nn + 1) - Z(nn - 1));

    Dfy_x(nn) = (y_x(nn + 1) - y_x(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    Dfy_w(nn) = (y_w(nn + 1) - y_w(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    %Change of variable derivative for densities
end

fw(1:Nn)=0;
fx(1:Nn)=0;
fy_x(1:Nn)=0;
for nn = 2:Nn-1
    fx(nn) = normpdf(Z(nn),0, 1)/abs(Dfx(nn)); %Bessel process density
    fw(nn) = normpdf(Z(nn),0, 1)/abs(Dfw(nn)); %Bessel process density

    fy_x(nn) = normpdf(Z(nn),0, 1)/abs(Dfy_x(nn));%Origianl coordinates density
    fy_w(nn) = normpdf(Z(nn),0, 1)/abs(Dfy_w(nn));%Origianl coordinates density
end
str=input('Analytic Values Calculated. Press a key to start Monte Carlo');
%Calculate the density with monte carlo below.
rng(85109634, 'twister')
paths=100000;
X(1:paths)=x0^(1-gamma)/(1-gamma); %Bessel process Monte carlo
YY(1:paths)=x0;  %Original process monte carlo.
Random1(1:paths)=0;
for tt=1:Tt
    Random1=randn(size(Random1));
    HermiteP1(1,1:paths)=1;
    HermiteP1(2,1:paths)=Random1(1:paths);
    HermiteP1(3,1:paths)=Random1(1:paths).^2-1;
    HermiteP1(4,1:paths)=Random1(1:paths).^3-3*Random1(1:paths);
    HermiteP1(5,1:paths)=Random1(1:paths).^4-6*Random1(1:paths).^2+3;
    %HermiteP1(6,1:paths)=Random1(1:paths).^5-10*Random1(1:paths).^3+15*Random1(1:paths);
    %HermiteP1(7,1:paths)=Random1(1:paths).^6-15*Random1(1:paths).^4+45*Random1(1:paths).^2-15;
    XX0=X;
    YY0=YY;
    for k = 0 : OrderM
        for m = 0:k
            l4 = k - m + 1;
            for n = 0 : m
                l3 = m - n + 1;
                for j = 0:n
                    l2 = n - j + 1;
                    l1 = j + 1;
                    if(l4<=5)
                    X(1:paths)=X(1:paths) + YqCoeff(l1,l2,l3,l4) * ...
                    mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                    ((1-gamma)*XX0(1:paths)).^(Fp1(l1,l2,l3,l4)/(1-gamma)) .* ...
                    HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);

                %Above is bessel process monte carlo equation.

                    YY(1:paths)=YY(1:paths) + YCoeff(l1,l2,l3,l4) * ...
                    mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                    YY0(1:paths).^Fp(l1,l2,l3,l4) .* HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);
                %Above is original coordinates monte carlo equation.
                    end
                end
            end
        end
    end
end

X(X<0)=0;
sum(X(:))/paths   %monte carlo average for bessel coordinates
sum(x(nStart:Nn-1).*ZProb(nStart:Nn-1))  % Ito-Taylor density average for bessel coordinates
sum(w(wnStart:Nn-1).*ZProb(wnStart:Nn-1))% Ito-Taylor density average for
%with squared orthogoanl increments in bessel coordinates
YY(YY<0)=0;
sum(YY(:))/paths %origianl coordinates monte carlo average.
sum(y_x(nStart:Nn-1).*ZProb(nStart:Nn-1)) %Original process average from coordinates
sum(y_w(wnStart:Nn-1).*ZProb(wnStart:Nn-1))   %derived from bessel process
theta+(x0-theta)*exp(-kappa*dt*Tt)%Mean reverting SDE original variable true average

BinSize=.0075;%Please change this bin size accordingly. When data range is too small decrease it.
%When density range is too large increase it.
MaxCutOff=30;
[XDensity,IndexOutX,IndexMaxX] = MakeDensityFromSimulation_Infiniti(X,paths,BinSize,MaxCutOff);
plot(w(wnStart:Nn-1),fw(wnStart:Nn-1),'b',x(nStart:Nn-1),fx(nStart:Nn-1),'r',IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'g');
str=input('Look at Bessel graphs comparison between monte carlo density and analytic density.Blue graph is from squared
orthogonal incrments method and red is from squared volatility, green is monte carlo.');

[YDensity,IndexOutY,IndexMaxY] = MakeDensityFromSimulation_Infiniti(YY,paths,BinSize,MaxCutOff);
plot(y_w(wnStart+1:Nn-1),fy_w(wnStart+1:Nn-1),'b',y_x(nStart+1:Nn-1),fy_x(nStart+1:Nn-1),'r',IndexOutY(1:IndexMaxY),YDensity(1:IndexMaxY),'g');
str=input('Look at Original variable graphs comparison between monte carlo and analytic density');
str=input('Blue graph is from squared orthogonal incrments method and red is from squared volatility, green is monte
carlo.');
end

% In the expansion of X^alpha
% With SDE
% dX(t)=mu1 * X(t)^beta1 dt + mu2* X(t)^beta2 dt + sigma * X(t)^gamma dz(t)
% The first order expansion of X^alpha with the above SDE is
% X(t+1)^alpha= X(t)^alpha +alpha* X(t)^(alpha-1) * mu1 * X(t)^beta1 *dt
% +alpha* X(t)^(alpha-1) * mu2 * X(t)^beta2 *dt
% + .5* alpha *(alpha-1)* X(t)^(alpha-2) * sigma^2 * X(t)^(2*gamma) *dt
% + alpha * X(t)^(alpha-1) * sigma * X(t)^gamma *dz(t)
% In my program, for the above four term expansion, I use a four dimensional
%array notation that shows the order of differentiation on each of these
%four types of terms. So if l1 represents drift one, l2 represents drift
%two and l3 represents quadratic variation term and l4 represents
%volatility term, we can use the notation Y(l1,l2,l3,l4) for the
%coefficients of expansion of the above term. So in the above first order expansion
% Y(1,0,0,0)= alpha * mu1
% Y(0,1,0,0)=alpha *mu2
% Y(0,0,1,0)= .5* alpha *(alpha-1)* sigma^2
% Y(0,0,0,1)= alpha * sigma
%
% For higher orders of expansion, we will have to carefully compute the
%coefficients separately based on path dependence and then lump them
%together in Y according to array indices. Once we have done that,
%we can write one term of the general expansion as
% Y(l1,l2,l3,l4) * x^(alpha+l1 * beta1 +l2* beta2 +l3* 2* gamma +l4 * gamma
%  - l1 -l2 - 2*l3 -l4) * HermiteP(l4) * dt^(l1 + l2 +l3 + .5*l4);
%
% In my program, since matlab does not take indices starting from zero,
%I have slightly adjusted the above notation.
%In the density simulation program, we pre-compute all coefficients and values
%needed in simulation but we have to calculate the part of above
%expression where power of x is evaluated.
% If we have four terms in Ito-hermite SDE expansion at first order,
%In every next level, each of the four terms would take four descendent
%terms and there will be sixteen terms on second level, and on third level
%there will be 64 descendent terms and 256 descendent terms on fourth level.
%However we can reduce the number of terms in Ito-hermite expansion to
%number of terms in polynomial expansion. For example Ito-hermite expansion
%of SDE with four terms on first order can be reduced to the number of
%terms in expansion of a polynomial with four terms on each level.
%To do this, we will have to pre-calculate the Coefficients carefully and
%the lump them together as in a polynomial like expansion.
% Again the above array Y(l1,l2,l3,l4) is relatively sparse and
%does not take all possible indices. Just like in polynomial expansion,
%on a certain expansion order, it takes only indices so that sum of indices
%goes to expansion order. For example on second order, only those indices
%could be found such that l1+l2+l3+l4=2. And similarly for third ito-hermite
%expansion level only those indices would be populated such that l1+l2+l3+l4=3.
% In order to do that I have done simple loops in a fashion shown below
%
% for k = 0 : (Order4)
%     for m = 0:k
%         l4 = k - m;
%         for n = 0 : m
%             l3 = m - n;
%             for j = 0:n
%                 l2 = n - j;
%                 l1 = j;
% First loop variable is for expansion order. And then rest of the loop
%variables take values such that their sum equals the expansion order.
%When we would add a fifth term in the SDE expansion for example,
%we will have to add another loop variable with the same logic that
%sum of loop variables equal to expansion order. In my matlab program,
%I have given offset to l4, l2,l3, l1 since array indices cannot start at zero.

%
%
% % In the expansion of X^alpha
% % With SDE
% % dX(t)=mu1 * X(t)^beta1 dt + mu2* X(t)^beta2 dt + sigma * X(t)^gamma dz(t)
% % The first order expansion of X^alpha with the above SDE is
% % X(t+1)^alpha= X(t)^alpha +alpha* X(t)^(alpha-1) * mu1 * X(t)^beta1 *dt
% % +alpha* X(t)^(alpha-1) * mu2 * X(t)^beta2 *dt
% % + .5* alpha *(alpha-1)* X(t)^(alpha-2) * sigma^2 * X(t)^(2*gamma) *dt
% % + alpha * X(t)^(alpha-1) * sigma * X(t)^gamma *dz(t)
% % In my program, for the above four term expansion, I use a four dimensional
% %array notation that shows the order of differentiation on each of these
% %four types of terms. So if l1 represents drift one, l2 represents drift
% %two and l3 represents quadratic variation term and l4 represents
% %volatility term, we can use the notation Y(l1,l2,l3,l4) for the
% %coefficients of expansion of the above term. So in the above first order expansion
% % Y(1,0,0,0)= alpha * mu1
% % Y(0,1,0,0)=alpha *mu2
% % Y(0,0,1,0)= .5* alpha *(alpha-1)* sigma^2
% % Y(0,0,0,1)= alpha * sigma
% %
% % For higher orders of expansion, we will have to carefully compute the
% %coefficients separately based on path dependence and then lump them
% %together in Y according to array indices. Once we have done that,
% %we can write one term of the general expansion as
% % Y(l1,l2,l3,l4) * x^(alpha+l1 * beta1 +l2* beta2 +l3* 2* gamma +l4 * gamma
% %  - l1 -l2 - 2*l3 -l4) * HermiteP(l4) * dt^(l1 + l2 +l3 + .5*l4);
% %
% % In my program, since matlab does not take indices starting from zero,
% %I have slightly adjusted the above notation.
% %In the density simulation program, we pre-compute all coefficients and values
% %needed in simulation but we have to calculate the part of above
% %expression where power of x is evaluated.
% % If we have four terms in Ito-hermite SDE expansion at first order,
% %In every next level, each of the four terms would take four descendent
% %terms and there will be sixteen terms on second level, and on third level
% %there will be 64 descendent terms and 256 descendent terms on fourth level.
% %However we can reduce the number of terms in Ito-hermite expansion to
% %number of terms in polynomial expansion. For example Ito-hermite expansion
% %of SDE with four terms on first order can be reduced to the number of
% %terms in expansion of a polynomial with four terms on each level.
% %To do this, we will have to pre-calculate the Coefficients carefully and
% %the lump them together as in a polynomial like expansion.
% % Again the above array Y(l1,l2,l3,l4) is relatively sparse and
% %does not take all possible indices. Just like in polynomial expansion,
% %on a certain expansion order, it takes only indices so that sum of indices
% %goes to expansion order. For example on second order, only those indices
% %could be found such that l1+l2+l3+l4=2. And similarly for third ito-hermite
% %expansion level only those indices would be populated such that l1+l2+l3+l4=3.
% % In order to do that I have done simple loops in a fashion shown below
% %
% % for k = 0 : (Order4)
% %     for m = 0:k
% %         l4 = k - m;
% %         for n = 0 : m
% %             l3 = m - n;
% %             for j = 0:n
% %                 l2 = n - j;
% %                 l1 = j;
% % First loop variable is for expansion order. And then rest of the loop
% %variables take values such that their sum equals the expansion order.
% %When we would add a fifth term in the SDE expansion for example,
% %we will have to add another loop variable with the same logic that
% %sum of loop variables equal to expansion order. In my matlab program,
% %I have given offset to l4, l2,l3, l1 since array indices cannot start at zero.
```

---

### #782 — Amin (Topic Author)
*January 28, 2019, 2:49 PM*

Here are the dependencies of the above program.

```
function [Y] = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma)

%In the coefficient calculation program which calculates Y(l1,l2,l3,l4),
%I have used four levels of looping each for relevant expansion order.
%The first loop takes four values and second loop takes 16 values and
%third loop takes 64 values and so on. And then each coefficient
%term can be individually calculated while carefully accounting
%for path dependence.
%So for example in a nested loop structure
%m1= 1:mDim
% 	m2=1:mDim
%		m3=1:mDim
%    l(m1)=l(m1)+1;
%    l(m2)=l(m2)+1;
%    l(m3)=l(m3)+1;

%in the above looping loop takes values from one to four with one
%indicating the first drift term, two indicating the second drift term
%and three indicating quadratic variation term and
%four indicating the volatility term. And with this looping structure
%we can So in the above looping m1=1 would mean that all terms are
%descendent of first drift term and m2=4 would mean that all terms are
%descendent of first drift term on first expansion order and descendent
%of volatility term on the second order and so we can keep track of path
%dependence perfectly.
%And on each level, we individually calculate the descendent terms. While
%keeping track of path dependence and calculating the coefficients with
%careful path dependence consideration, we update the appropriate element
%in our polynomial like expansion coefficient array

%explaining the part of code
%m1= 1:mDim
%	m2=1:mDim
%		m3=1:mDim
%    l(m1)=l(m1)+1;
%    l(m2)=l(m2)+1;
%    l(m3)=l(m3)+1;
%Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,1,2);

%Here l(1) denotes l1 but written as l(1) so it can be conveniently
%updated with the loop variable when the loop variable takes value one
%indicating first drift term . And l(2) could be conveniently updated when
%the loop variable takes value equal to two indicating second
%drift term and so on.
%Here is the part of code snippet for that

%for m1=1:mDim
%    l(1)=1;
%    l(2)=1;
%    l(3)=1;
%    l(4)=1;
%    l(m1)=l(m1)+1;
%CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma - (l(1)-1) - (l(2)-1) -
2*(l(3)-1) - (l(4)-1);
%    CoeffDX2 = CoeffDX1 - 1;
%    ArrIndex0=m1;
%    ArrIndex=(m1-1)*mDim;
%    Coeff1st=Y1(ArrIndex0)*CoeffDX1;
%    Coeff2nd=Y1(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
%    Y2(1+ArrIndex)=Coeff1st;
%    Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
%    Y2(2+ArrIndex)=Coeff1st;
%    Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
%    Y2(3+ArrIndex)=Coeff2nd;
%    Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,1,2,n1(m1));
%    Y2(4+ArrIndex)=Coeff1st;
%    Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,1,3,n1(m1));

%The first four lines update the array indices according to the parent term.
%And then CoeffDX1 and CoeffDX2 are calculated according to algebraic exponents on parent terms.
%ArrIndex0=m1; calculates the array index of the parent term
%And ArrIndex=(m1-1)*mDim; calculates the array index of the descendent terms
%And coefficient of the drift and volatility descendent terms is
%calculated by multiplying the coefficient of the parent term by
%Coeff1st=Y1(ArrIndex0)*CoeffDX1;
%And coefficient of the quadratic variation descendent terms is
%calculated by multiplying the coefficient of the parent term by
%Coeff2nd=Y1(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
%And then each of the four descendent terms are updated with Coeff1st
%if they are drift or volatility descendent terms or Coeff2nd if
%they are quadratic variation descendent terms.
%Here Y1 indicates the temporary coefficient array with parent terms on
%first level. And Y2 denotes temporary coefficient array with parent terms
%on second level and Y3 indicates temporary coefficient array with parent terms on third level.

[IntegralCoeff,IntegralCoeffdt,IntegralCoeffdz] = ComputeIntegralCoeffs();

n1(1)=2;
n1(2)=2;
n1(3)=2;
n1(4)=3;
%n1(1), n1(2), n1(3) are drift and quadratic variation term variables
%and take a value equal to 2 indicating a dt integral.
%n1(4) is volatility term variable and indicates a dz-integral by taking a
%value of 3.

mDim=4; % four descendent terms in each expansion
Y(1:5,1:5,1:5,1:5)=0;
Y1(1:mDim)=0;
Y2(1:mDim*mDim)=0;
Y3(1:mDim*mDim*mDim)=0;

%First Ito-hermite expansion level starts here. No loops but four
%descendent terms.
l(1)=1;
l(2)=1;
l(3)=1;
l(4)=1;
CoeffDX1 = alpha;
CoeffDX2 = CoeffDX1 - 1;
Coeff1st=CoeffDX1;
Coeff2nd=.5*CoeffDX1*CoeffDX2;

Y1(1)=Coeff1st;
Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,1,2);
Y1(2)=Coeff1st;
Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,1,1,2);
Y1(3)=Coeff2nd;
Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,1,1,2);
Y1(4)=Coeff1st;
Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,1,1,3);

%Second Ito-hermite expansion level starts. It has a loop over four parent
%terms and there are four descendent terms for each parent term.
%The coefficient terms are then lumped in a polynomial-like expansion
%array of coefficients.
for m1=1:mDim
    l(1)=1;
    l(2)=1;
    l(3)=1;
    l(4)=1;
    l(m1)=l(m1)+1;
    CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma ...
                        - (l(1)-1) - (l(2)-1) - 2*(l(3)-1) - (l(4)-1);
    CoeffDX2 = CoeffDX1 - 1;
    ArrIndex0=m1;
    ArrIndex=(m1-1)*mDim;
    Coeff1st=Y1(ArrIndex0)*CoeffDX1;
    Coeff2nd=Y1(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
    Y2(1+ArrIndex)=Coeff1st;
    Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
    Y2(2+ArrIndex)=Coeff1st;
    Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
    Y2(3+ArrIndex)=Coeff2nd;
    Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,1,2,n1(m1));
    Y2(4+ArrIndex)=Coeff1st;
    Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,1,3,n1(m1));
    %Third Ito-hermite expansion level starts and it is a nested loop with
    %a total of sixteen parents and each parent takes four descendent
    %terms.
    for m2=1:mDim
        l(1)=1;
        l(2)=1;
        l(3)=1;
        l(4)=1;
        l(m1)=l(m1)+1;
        l(m2)=l(m2)+1;
        CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma ...
                        - (l(1)-1) - (l(2)-1) - 2*(l(3)-1) - (l(4)-1);
        CoeffDX2=CoeffDX1-1;
        ArrIndex0=(m1-1)*mDim+m2;
        ArrIndex=((m1-1)*mDim+(m2-1))*mDim;
        Coeff1st=Y2(ArrIndex0)*CoeffDX1;
        Coeff2nd=Y2(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
        Y3(1+ArrIndex)=Coeff1st;
        Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,2,n1(m2),n1(m1));
        Y3(2+ArrIndex)=Coeff1st;
        Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,2,n1(m2),n1(m1));
        Y3(3+ArrIndex)=Coeff2nd;
        Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,2,n1(m2),n1(m1));
        Y3(4+ArrIndex)=Coeff1st;
        Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,3,n1(m2),n1(m1));
        %fourht Ito-hermite expansion level starts and it is a triply-nested loop with
        %a total of sixteen parents and each parent takes four descendent
        %terms. We then lump the terms in a relatively sparse polynomial
        %like expansion coefficient array that has smaller number of
        %non-zero terms.

        for m3=1:mDim
            l(1)=1;
            l(2)=1;
            l(3)=1;
            l(4)=1;
            l(m1)=l(m1)+1;
            l(m2)=l(m2)+1;
            l(m3)=l(m3)+1;
            CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma ...
                        - (l(1)-1) - (l(2)-1) - 2*(l(3)-1) - (l(4)-1);
            CoeffDX2=CoeffDX1-1;
            ArrIndex0=((m1-1)*mDim+(m2-1))*mDim+m3;
            %ArrIndex=(((m1-1)*mDim+(m2-1))*mDim+(m3-1))*mDim;
            Coeff1st=Y3(ArrIndex0)*CoeffDX1;
            Coeff2nd=Y3(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
            %Y4(1+ArrIndex)=Coeff1st;
            Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(2,n1(m3),n1(m2),n1(m1));
            %Y4(2+ArrIndex)=Coeff1st;
            Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(2,n1(m3),n1(m2),n1(m1));
            %Y4(3+ArrIndex)=Coeff2nd;
            Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(2,n1(m3),n1(m2),n1(m1));
            %Y4(4+ArrIndex)=Coeff1st;
            Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(3,n1(m3),n1(m2),n1(m1));
         end
    end
end

end

```

and

```
function [IntegralCoeff0,IntegralCoeffdt,IntegralCoeffdz] = ComputeIntegralCoeffs()

IntegralCoeff(1:3,1:3,1:3,1:3)=0;
IntegralCoeffdt(1:3,1:3,1:3,1:3)=0;
IntegralCoeffdz(1:3,1:3,1:3,1:3)=0;

IntegralCoeff0(1:3,1:3,1:3,1:3)=0;

IntegralCoeff0(1,1,1,2)=1;
IntegralCoeff0(1,1,1,3)=1;

IntegralCoeff0(1,1,2,2)=1/2;
IntegralCoeff0(1,1,3,2)=1-1/sqrt(3);
IntegralCoeff0(1,1,2,3)=1/sqrt(3);
IntegralCoeff0(1,1,3,3)=1/2;

IntegralCoeff0(1,2,2,2)=1/6;
IntegralCoeff0(1,3,2,2)=(1-1/sqrt(3))*1/2*(1-1/sqrt(5));
IntegralCoeff0(1,2,3,2)=1/sqrt(3)/2*(1-1/sqrt(5));
IntegralCoeff0(1,3,3,2)=1/2*(1-sqrt(2)/2);
IntegralCoeff0(1,2,2,3)=1/2*1/sqrt(5);
IntegralCoeff0(1,3,2,3)=(1-1/sqrt(3))*1/sqrt(2)*1/2;
IntegralCoeff0(1,2,3,3)=1/sqrt(3)/sqrt(2)*1/(2);
IntegralCoeff0(1,3,3,3)=1/6;

IntegralCoeff0(2,2,2,2)=1/24;
IntegralCoeff0(2,2,3,2)=1/2*1/sqrt(5)*1/3*(1-1/sqrt(7));
IntegralCoeff0(2,3,2,2)=1/sqrt(3)*1/2*(1-1/sqrt(5))*1/3*(1-1/sqrt(7));
IntegralCoeff0(3,2,2,2)=(1-1/sqrt(3))*1/2*(1-1/sqrt(5))*1/3*(1-1/sqrt(7));
IntegralCoeff0(3,3,2,2)=1/2*(1-sqrt(2)/2)*1/2*(1-sqrt(2)/sqrt(6));
IntegralCoeff0(2,3,3,2)=1/sqrt(3)*1/sqrt(2)*1/2*1/2*(1-sqrt(2)/sqrt(6));
IntegralCoeff0(3,2,3,2)=(1-1/sqrt(3))*1/sqrt(2)*1/2*1/2*(1-sqrt(2)/sqrt(6));
IntegralCoeff0(3,3,3,2)=1/6*(1-sqrt(3)/sqrt(5));

IntegralCoeff0(2,2,2,3)=1/6*1/sqrt(7);
IntegralCoeff0(2,2,3,3)=1/2*1/sqrt(5)*1/sqrt(2)*1/sqrt(6);
IntegralCoeff0(2,3,2,3)=1/sqrt(3)*1/2*(1-1/sqrt(5))*1/sqrt(2)*1/sqrt(6);
IntegralCoeff0(3,2,2,3)=(1-1/sqrt(3))*1/2*(1-1/sqrt(5))*1/sqrt(2)*1/sqrt(6);
IntegralCoeff0(3,3,2,3)=1/2*(1-sqrt(2)/2)*1/sqrt(3)*1/sqrt(5);
IntegralCoeff0(2,3,3,3)=1/sqrt(3)*1/sqrt(2)*1/sqrt(4)*1/sqrt(3)*(1/sqrt(5));
IntegralCoeff0(3,2,3,3)=(1-1/sqrt(3))*1/sqrt(2)*1/2*1/sqrt(3)*1/sqrt(5);
IntegralCoeff0(3,3,3,3)=1/24;

%Can also be calculated with algorithm below.
%here IntegralCoeffdt indicates the coefficients of a dt-integral.
%This dt-integral means that you are calculating the Ito-hermite expansion
%of  Integral X(t)^alpha dt with X(t) dynamics given by the SDE
%here IntegralCoeffdz indicates the coefficients of a dz-integral.
%This dz-integral means that you are calculating the Ito-hermite expansion
%of  Integral X(t)^alpha dz(t) with X(t) dynamics given by the SDE

%IntegralCoeff is is associated with expansion of X(t)^alpha.
%IntegralCoeff below is not returned and IntegralCoeff0 manually calculated
%above is returned but both are the same.

l0(1:2)=1;

for m4=1:2
    l0(1)=1;
    l0(2)=1;

    %IntegralCoeff4(m4,1,1,1)=1;
    %IntegralCoeff4(m4,1,1,1)=1;
    %1 is added to m4 since index 1 stands for zero, 2 for one and three
    %for two.
    IntegralCoeff(1,1,1,m4+1)=1;
    l0(m4)=l0(m4)+1;
    IntegralCoeffdt(1,1,1,m4+1)=IntegralCoeff(1,1,1,m4+1)* ...
        1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
    IntegralCoeffdz(1,1,1,m4+1)= IntegralCoeff(1,1,1,m4+1)* ...
        1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
    for m3=1:2
        l0(1)=1;
        l0(2)=1;
        l0(m4)=l0(m4)+1;

        if(m3==1)
            IntegralCoeff(1,1,m4+1,m3+1)=1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
        end
        if(m3==2)
            IntegralCoeff(1,1,m4+1,m3+1)= 1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
        end
        l0(m3)=l0(m3)+1;
        %IntegralCoeff(1,1,m4+1,m3+1)=IntegralCoeff4(m4,m3,1,1);
        IntegralCoeffdt(1,1,m4+1,m3+1)=IntegralCoeff(1,1,m4+1,m3+1)* ...
            1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
        IntegralCoeffdz(1,1,m4+1,m3+1)= IntegralCoeff(1,1,m4+1,m3+1)* ...
            1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
        for m2=1:2
            l0(1)=1;
            l0(2)=1;
            l0(m4)=l0(m4)+1;
            l0(m3)=l0(m3)+1;

            if(m2==1)
               
IntegralCoeff(1,m4+1,m3+1,m2+1)=IntegralCoeff(1,1,m4+1,m3+1)*1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
            end
            if(m2==2)
                IntegralCoeff(1,m4+1,m3+1,m2+1)=
IntegralCoeff(1,1,m4+1,m3+1)*1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
            end
            l0(m2)=l0(m2)+1;
            %IntegralCoeff(1,m4+1,m3+1,m2+1)=IntegralCoeff4(m4,m3,m2,1);
            IntegralCoeffdt(1,m4+1,m3+1,m2+1)=IntegralCoeff(1,m4+1,m3+1,m2+1)* ...
                1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
            IntegralCoeffdz(1,m4+1,m3+1,m2+1)= IntegralCoeff(1,m4+1,m3+1,m2+1)* ...
                1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);

            for m1=1:2
                l0(1)=1;
                l0(2)=1;
                l0(m4)=l0(m4)+1;
                l0(m3)=l0(m3)+1;
                l0(m2)=l0(m2)+1;
                if(m1==1)
                   
IntegralCoeff(m4+1,m3+1,m2+1,m1+1)=IntegralCoeff(1,m4+1,m3+1,m2+1)*1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
                end
                if(m1==2)
                    IntegralCoeff(m4+1,m3+1,m2+1,m1+1)=
IntegralCoeff(1,m4+1,m3+1,m2+1)*1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
                end
                l0(m1)=l0(m1)+1;
                %IntegralCoeff(m4+1,m3+1,m2+1,m1+1)=IntegralCoeff4(m4,m3,m2,m1);
                IntegralCoeffdt(m4+1,m3+1,m2+1,m1+1)=IntegralCoeff(m4+1,m3+1,m2+1,m1+1)* ...
                    1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
                IntegralCoeffdz(m4+1,m3+1,m2+1,m1+1)= IntegralCoeff(m4+1,m3+1,m2+1,m1+1)* ...
                    1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
            end
        end
    end
end

end
```

And the graphing of simulation file is here.

```
function [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti(X,Paths,BinSize,MaxCutOff )
%Processes monte carlo paths to return a series Xdensity as a function of IndexOut. IndexMax is the maximum value of
index.
%

Xmin=0;
Xmax=0;
for p=1:Paths
if(X(p)>MaxCutOff)
X(p)=MaxCutOff;
end
%if(X(p)real(X(p)))
Xmin=real(X(p));
end
if(XmaxIndexMax)
index=IndexMax;
end

XDensity(index)=XDensity(index)+1.0/Paths/BinSize;

end

IndexOut(1:IndexMax)=Xmin+(0:(IndexMax-1))*BinSize;

end

```

---

### #783 — Amin (Topic Author)
*January 28, 2019, 3:39 PM*

I posted this on internet about my latest research. I will continue to post my research and programs on parameter
estimation of SDEs and state-space processes and related filtering on Wilmott forum. And then further continue with 
posting research on AI + Bayesian methods on this forum. Here is my post on linkedin about my research.

[https://www.linkedin.com/pulse/introduc ... hsan-amin/](https://www.linkedin.com/pulse/introduction-newly-developed-research-infiniti-derivatives-ahsan-amin/)

Introduction to Newly Developed Research at Infiniti Derivatives Technologies.

Fast and Accurate Monte Carlo Simulation.

Due to recently developed research at Infiniti Derivatives Technologies, we can do accurate monte carlo simulations of
almost any stochastic differential equation. This includes arbitrary stochastic volatility SDEs and their related greeks
SDEs. We challenge you to throw examples of difficult SDEs that we would solve with our newly developed technology.

Discovery of a new SDE Density Simulation Framework.

We have developed a new SDE density simulation framework that is very fast and reasonably robust. Here are some examples
of the applications of this technology

Fast Calibration of derivatives models and calculation of their greeks.
New innovative models. For example you could now have a SV SABR model in which volatility is governed by a CEV process
of arbitrary quotient. We could for example help you simulate, calibrate and risk manage a SV Libor Market Model
framework in which SABR vol is given by a CEV process.
Formation of alpha generation strategies with options. Our density simulation framework can allow you to calculate the
right distribution of the underlying asset and you could then trade options according to mispricing with respect to
implied vol in the market.
Modeling of mean-reverting densities for statistical arbitrage in pairs trading.
 The method is ideal for calibration of volatility surfaces and can very easily be enhanced to calibrate and simulate
the local volatility and LSV models.
""

""

Filtering and Parameter Estimation:

Our research on SDEs has ramifications for non- linear Bayesian filtering and parameters estimation in the area of SDEs
and state-space models. Using this new research, we can do on-line parameter optimization and tuning for the parameters
of the SDE or the state space process. It can also be possible to use slowly varying parameters framework for filtering
of the SDE or the state space process. I have also done research work that obviates the need for expensive integrations
in non-linear Bayesian filtering and the whole work can be done in transition probabilities framework. This makes the
process both faster and more accurate. With this new research, we can do non-linear filtering for non-linear state-space
models where efficient filtering was earlier not possible. These are interesting developments in filtering and parameter
estimation using my research on stochastic processes. This can have huge applications within and out of the context of
quantitative finance. Here are some applications in quantitative finance:

We can find the true distribution of financial data generation process using filtering and parameter estimation
techniques. We can also find out how volatility mean reverts after using filtering and calculating the data distribution
of data generating process on several scales. This will give us true data generating process and tell us about the true
mean reversion in the data as opposed to blindly following the implied distributions backed out from the option pricing
data. We can for example find out what is the true data generating process for sixty dimensional LIBOR rate process used
in LIBOR market model and what is the structure of their daily volatility and how this structure scales to weekly,
monthly and quarterly volatility and how future volatility changes. This can be a very exciting application of our
parameter estimation algorithm and will help outline the true LIBOR volatilities which can then be compared to LIBORs
implied volatility for statistical arbitrage purposes.
filtering of financial data can be used in the context of quantitative trading.
We can use filtering in the context of pairs trading where the mean reverting parameter can be calculated online and can
also be modeled as a slowly varying parameter. Its intensity could tell about the mean reversion speed of the pair in
pairs trading.
I wish to work with your company as a consulting partner to implement some of these new technologies. If you have any
questions or you would like me to work for you on these projects for your company, please email me at
[[email protected]](/cdn-cgi/l/email-protection#d7b6b9b6b9e5eeeeee97aeb6bfb8b8f9b4b8ba)

---

### #784 — ppauper
*January 28, 2019, 8:32 PM*

>
> I will continue to post my research and programs on parameter estimation of SDEs and state-space processes and related
filtering on Wilmott forum. And then further continue with  posting research on AI + Bayesian methods on this forum.
>
thanks

I for one always look forward to your posts

---

### #785 — Amin (Topic Author)
*January 29, 2019, 2:38 PM*

Thank you Peter for your kind words. Yes, I hope to continue putting interesting stuff on Wilmott here. I wish everybody
likes this knowledge sharing. Thank you again.

---

### #786 — Amin (Topic Author)
*February 7, 2019, 9:09 PM*

OK friends, I am excited as there is another major breakthrough in the Ito-Taylor density simulation method. I had done
a paper last year in which I had claimed that transition probabilities between different CDF subdivisions during the
evolution of an SDE can be mapped and are the same as the transition probabilities between different CDF subdivisions of
a brownian motion with the same volatility. Using the ideas from that paper, I have worked out a new method in which
works well even in original coordinates and can also be used for evolution of dt-integrals and dz-integrals of the SDE.
This is a major breakthrough. We noticed that in Ito Taylor method density is mapped on a normal density at each step. I
mapped the simulation density before simulation step on a corresponding Brownian motion and then simulated the brownian
motion with the same volatility as the SDE and found out what is the transition value of gaussian Z that is required to
move from nth CDF interval at time t-1 to nth CDF interval at time t on the brownian motion density. I used the same
transition value of gaussian Z in hermite polynomials for the simulation of  SDE and it can be done in the original
coordinates as well. I am uploading a very simple program that shows how it is done. I have just simulated CEV noise
using the density but it can also be very easily used with SDEs with linear and non-linear drifts. Here is the simple
program. I will come up with a very detailed program very soon. Here is the simple program that simulates an SDE by
mapping it on Brownian motion and using transition Z from the brownian motion transition values.

```
function [] = ItoTaylorDensityRecombining()
%In this quick program, I am simulating the driftless noise SDE
%dX(t)=sigma * X(t)^gamma * dz(t)
dt=.125/4;   % Simulation time interval.
Tt=16;       % Number of simulation levels. Terminal time= Tt*dt;
dNn=.1/1;    % Normal density width. would change with number of subdivisions
Nn=80;       % No of normal density subdivisions
NnMidl=40;
NnMidh=41;
NnMid=4.0;
x0=1.0;      % starting value of SDE
gamma=.50;   %volatility power exponent
sigma0=1.0;   %Volatility value

y(1:Nn)=x0;  %SDE variable
for nn=1:Nn
    Z(nn)=((nn-.5)*dNn-NnMid);
end
ZProb(1)=normcdf(.5*Z(1)+.5*Z(2),0,1);
ZProb(Nn)=1-normcdf(.5*Z(Nn)+.5*Z(Nn-1),0,1);
for nn=2:Nn-1
    ZProb(nn)=normcdf(.5*Z(nn)+.5*Z(nn+1),0,1)-normcdf(.5*Z(nn)+.5*Z(nn-1),0,1);
end

for tt=1:Tt
    for nn=1:Nn
        x1(nn)=x0+sigma0*sqrt((tt-1)*dt)*Z(nn);%Simulate brownian motion
        %to the last date
    end
    for nn=1:Nn
        x2(nn)=x0+sigma0*sqrt(tt*dt)*Z(nn);%Simulate brownian motion to
        %the next date
    end
    for nn=1:Nn
        Zt(nn,nn)=(x2(nn)-x1(nn))/sigma0/sqrt(dt);%Get the transition value
        %of Z that is required to go from nth CDF subdivision of brownain
        %motion at time t-1 to nth CDF subdivision of brownian motion
        %at time t.
        %use the same transition value of Z to generate hermite
        %polynomials.
        HermiteP(1,nn)=0;
        HermiteP(2,nn)=Zt(nn,nn);%rho1(nn)
        HermiteP(3,nn)=(Zt(nn,nn)^2-1);%rho2(nn)
        HermiteP(4,nn)=(Zt(nn,nn)^3-3*Zt(nn,nn));
        HermiteP(5,nn)=(Zt(nn,nn)^4-6*Zt(nn,nn)^2+3);
    end
    for nn=1:Nn
        y(nn)=y(nn)+sigma0*sqrt(dt)*y(nn)^gamma.*HermiteP(2,nn) ...
             +sigma0^2*gamma*y(nn)^(2*gamma-1)*dt.*HermiteP(3,nn)/2 ...
             +sigma0^3*gamma*(2*gamma-1)*y(nn).^(3*gamma-2)*dt^1.5.*(HermiteP(4,nn))/6 ...
             +sigma0^4*gamma*(2*gamma-1)*(3*gamma-2).*y(nn).^(4*gamma-3)*dt^2.0.*(HermiteP(5,nn))/24;
    end
end

for nn=2:Nn-1
    Dfy(nn) = (y(nn + 1) - y(nn - 1))/(Z(nn + 1) - Z(nn - 1));
end
fy(1:Nn)=0;
for nn = 2:Nn-1
    fy(nn) = normpdf(Z(nn),0, 1)/abs(Dfy(nn));%Origianl coordinates density
end

str=input('Analytic Values Calculated. Press a key to start Monte Carlo');
rng(85109634, 'twister')
paths=100000;
Y(1:paths)=x0;  %Original process monte carlo.
Random1(1:paths)=0;
for tt=1:Tt
    Random1=randn(size(Random1));
    HermiteP1(1,1:paths)=1;
    HermiteP1(2,1:paths)=Random1(1:paths);
    HermiteP1(3,1:paths)=Random1(1:paths).^2-1;
    HermiteP1(4,1:paths)=Random1(1:paths).^3-3*Random1(1:paths);
    HermiteP1(5,1:paths)=Random1(1:paths).^4-6*Random1(1:paths).^2+3;
    Y0=Y;

    Y(1:paths)=Y(1:paths)+sigma0*sqrt(dt).*Y0(1:paths).^gamma.*HermiteP1(2,1:paths) ...
    +sigma0^2*gamma*Y0(1:paths).^(2*gamma-1).*dt.*HermiteP1(3,1:paths)/2.0 ...
    +sigma0^3*gamma*(2*gamma-1)*Y0(1:paths).^(3*gamma-2).*dt^1.5.*HermiteP1(4,1:paths)/6.0 ...
    +sigma0^4*gamma*(2*gamma-1)*(3*gamma-2).*Y0(1:paths).^(4*gamma-3)*dt^2.0.*HermiteP1(5,1:paths)/24;
end
sum(y(2:Nn-1).*ZProb(2:Nn-1))
Y(Y<0)=0;
sum(Y(:))/paths
BinSize=.0275;
MaxCutOff=30;
[YDensity,IndexOutY,IndexMaxY] = MakeDensityFromSimulation_Infiniti(Y,paths,BinSize,MaxCutOff);
plot(y(2:Nn-1),fy(2:Nn-1),'r',IndexOutY(1:IndexMaxY),YDensity(1:IndexMaxY),'g');

end
```

Though the above program works with driftless CEV SDEs, I will be uploading a detailed program in a day or two that
would simulate every SDE and its dt-integrals and its dz-integrals. This has become possible with the new discovery.

---

### #787 — Amin (Topic Author)
*February 22, 2019, 6:36 PM*

Sorry that I have been away working on my market trading project. But for next few days, I will work on my Ito-Taylor
SDE simulation methods research. Here is the agenda for next few days. OK, one more thing that we have been working with
Ito-Taylor density simulation part and we have neglected the Ito-Taylor monte carlo simulation. In the next post, I will
be putting here a program that will take an arbitrary dimensional correlated system of SDEs of the kinds that appear in
mathematical finance and we will be able to do monte carlo simulation up to 2nd or 4th order accuracy as suggested by
the user. Then I will upload another example code that will simulate correlated three factor SV LIBOR market model SDEs
to 2nd or 4th order accuracy as suggested by the user. So there are going to be interesting examples. On the Ito-Taylor
density simulation side, I have also almost completed work on squared orthogonal increments density simulation scheme to
take care of the instability and I will also be posting that here before I go underground again to start working on
market trading. Hope to have an exciting week ahead.

---

### #788 — Amin (Topic Author)
*July 2, 2019, 4:26 PM*

Very sorry for remaining away for such a long time even before my research was taken to conclusion. I have been working
with market trading based on analytics with limit order book dynamics but two weeks ago I returned to the problem of
simulation of stochastic differential equations and their stochastic integrals. I would like to take the research to
conclusion since I spent more than two years working on the problem. And now I believe that I am extremely close to the
solution of the problem and expect that I would be able to present a completely worked out matlab program within a week
to ten days. OK during my research I came across some interesting equations that I would like to share since there is a
possibility they could be solved by analytical means by experts. One benchmark of my research has been stochastic
volatility type equations take two non-linear terms in their drift. These represent enough generality and are also
difficult enough. Ok, let us consider the following SDE.

$dX_s= \mu_1 X_s^{\beta_1} ds + \mu_2 X_s^{\beta_2} ds + \sigma X_s^{\gamma} dz(s)$   Eq(1)

I have been working with bessel coordinates where the SDE can be transformed into bessel variable
$Y_s=\frac{{X_s}^{(1-\gamma)}}{(1-\gamma)}$ as (after the application of Ito formula)

$d[\frac{{X_s}^{(1-\gamma)}}{(1-\gamma)}] = \mu_1 X_s^{(\beta_1-\gamma)} ds + \mu_2 X_s^{(\beta_2-\gamma)} ds + .5 \sigma^2 (-\gamma) X_s^{(\gamma-1)} ds + \sigma dz(s)$
Eq(2)

I had been trying to use Feynman exponential on this SDE. When we write the Fokker planck of the SDE, there is killing
term in the FP PDE that correponds to Feynman exponential. Since there are no random numbers in my deterministic density
evolution, it has to learn from the Fokker planck in addition to following the SDE. Drift and diffusion terms would
remain the same but Feynman exponential slightly shifts the underlying distribution and the density of the mean
reverting SDEs (at 100% vols) start to go off after six or nine months. I believe that this is due to not accounting the
Feynman exponential. While I was working on this, I found something interesting.

If we pick an exponential intelligently and multiply it with Bessel form of the SDE and apply Ito formula, we can cancel
the drift terms in the Bessel form with the exponential multiplying the Gaussian directly. I could easily solve such a
form in my framework but there could possibly be analytic solutions of such forms as well. Here is my choice of
exponential and I apply it to bessel transformation and use Ito here

$d[\exp(\int_0^s[-\mu_1(1-\gamma)X_v^{\beta_1-1}dv-\mu_2(1-\gamma)X_v^{\beta_2-1}dv-.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv])$

$ \frac{X_s^{(1-\gamma)}}{(1-\gamma)}]$  Eq(3)

In the above stochastic product to be solved by Ito, the terms in the exponential have been so chosen that after the
application of Ito dt-terms in the first part of Ito expansion that appear from the differential of the integral
multiplied by bessel variable would cancel the drift terms in the second part from differential of the bessel variable.
These drift terms in second part are from the bessel SDE form given in equation two. The above differential is expanded
by Ito as

$d[\exp(\int_0^s[-\mu_1(1-\gamma)X_v^{\beta_1-1}dv-\mu_2(1-\gamma)X_v^{\beta_2-1}dv-.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv]) \frac{X_s^{(1-\gamma)}}{(1-\gamma)}]$

$=\exp(\int_0^s[-\mu_1(1-\gamma)X_v^{\beta_1-1}dv-\mu_2(1-\gamma)X_v^{\beta_2-1}dv-.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv])$

$* (-\mu_1(1-\gamma)X_s^{\beta_1-1}ds-\mu_2(1-\gamma)X_s^{\beta_2-1}ds-.5\sigma^2(-\gamma)(1-\gamma)X_s^{2\gamma-2}ds) * \frac{X_s^{(1-\gamma)}}{(1-\gamma)}$

$+\exp(\int_0^s[-\mu_1(1-\gamma)X_v^{\beta_1-1}dv-\mu_2(1-\gamma)X_v^{\beta_2-1}dv-.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv])$

$*( \mu_1 X_s^{(\beta_1-\gamma)} ds + \mu_2 X_s^{(\beta_2-\gamma)} ds + .5 \sigma^2 (-\gamma) X_s^{(\gamma-1)} ds + \sigma dz(s))$

After algebra, the above simplifies to

$d[\exp(\int_0^s[-\mu_1(1-\gamma)X_v^{\beta_1-1}dv-\mu_2(1-\gamma)X_v^{\beta_2-1}dv-.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv]) \frac{X_s^{(1-\gamma)}}{(1-\gamma)}]$

$=\exp(\int_0^s[-\mu_1(1-\gamma)X_v^{\beta_1-1}dv-\mu_2(1-\gamma)X_v^{\beta_2-1}dv-.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv])\sigma dz(s))$

After taking integrals on both sides, we get

$\exp(\int_0^t[-\mu_1(1-\gamma)X_v^{\beta_1-1}dv-\mu_2(1-\gamma)X_v^{\beta_2-1}dv-.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv]) \frac{X_t^{(1-\gamma)}}{(1-\gamma)}$

$=\frac{X_0^{(1-\gamma)}}{(1-\gamma)} + \int_0^t \exp(\int_0^s[-\mu_1(1-\gamma)X_v^{\beta_1-1}dv-\mu_2(1-\gamma)X_v^{\beta_2-1}dv-.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv])\sigma dz(s))$

From where we get the solution as

$\frac{X_t^{(1-\gamma)}}{(1-\gamma)}=\frac{X_0^{(1-\gamma)}}{(1-\gamma)}*\exp(\int_0^t[+\mu_1(1-\gamma)X_v^{\beta_1-1}dv+\mu_2(1-\gamma)X_v^{\beta_2-1}dv+.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv]) $

$+\exp(\int_0^t[+\mu_1(1-\gamma)X_v^{\beta_1-1}dv+\mu_2(1-\gamma)X_v^{\beta_2-1}dv+.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv])$

$*\int_0^t \exp(\int_0^s[-\mu_1(1-\gamma)X_v^{\beta_1-1}dv-\mu_2(1-\gamma)X_v^{\beta_2-1}dv-.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}dv])\sigma dz(s))$

writing the integral in a simplified form, the above expression becomes

$\frac{X_t^{(1-\gamma)}}{(1-\gamma)}=\frac{X_0^{(1-\gamma)}}{(1-\gamma)}*\exp(\int_0^t K(X_v)dv) $

$+ \exp(\int_0^t K(X_v)dv)  \int_0^t \exp( \int_0^s -K(X_v)dv ) \sigma dz(s) $

where
$K(X_v)=+\mu_1(1-\gamma)X_v^{\beta_1-1}+\mu_2(1-\gamma)X_v^{\beta_2-1}+.5\sigma^2(-\gamma)(1-\gamma)X_v^{2\gamma-2}$

I can solve the integrals in my framework but the question is if there is a clever analytical method to solve these
integrals.

I will be coming back with more posts in next few days. I hope to conclusively solve the problem now.

---

### #789 — Amin (Topic Author)
*July 12, 2019, 11:38 AM*

Here is the new improved program for simulation of densities using Ito-Taylor density Simulation method I have worked
on. It works quite well. But it is still not perfect for large terminal time with very high volatilities in the SDE. I
have worked with squared orthogonal increments method and removed instabilities in the earlier versions and made the
algorithm more accurate. Here is the program. It computes the density analytically and then makes a comparison with
monte carlo density.

```
function [] = ItoTaylorDensityMRRecombining07()
%Copyright Ahsan Amin. Infiniti derivatives Technologies.
%Please fell free to connect on linkedin: linkedin.com/in/ahsan-amin-0a53334
%or skype ahsan.amin2999
%In this program, I am simulating the SDE given as
%dy(t)=mu1 x(t)^beta1 dt + mu2 x(t)^beta2 dt +sigma x(t)^gamma dz(t)
%I have not directly simulated the SDE but simulated the transformed
%Bessel process version of the SDE and then changed coordinates to retreive
%the SDE in original coordinates.
%The present program will directly simulate only the Bessel Process version of the
%SDE in transformed coordinates.
dt=.125/8;   % Simulation time interval.%For diffusions close to zero
             %decrease dt for accuracy.
Tt=8*4;     % Number of simulation levels. Terminal time= Tt*dt; //.125/8*8*8=1 year;
OrderA=2;  %Keep at two.
OrderM=2;  %Keep at two.
dNn=.2/1;   % Normal density subdivisions width. would change with number of subdivisions
Nn=40;  % No of normal density subdivisions
NnMidl=20;%One half left from mid of normal density
NnMidh=21;%One half right from the mid of normal density
NnMid=4.0;
x0=1.0;   % starting value of SDE
beta1=0.0;   % the first drift term power.
beta2=1.0;   % Second drift term power.
gamma=.550;   % volatility power.
kappa=.750;   %mean reversion parameter.
theta=1.0;   %mean reversion target
%Below you can get rid of kappa and theta and freely choose your own values
%for both drift coefficients.
mu1=1*theta*kappa;   % first drift coefficient.
mu2=-1*kappa;    % Second drift coefficient.
sigma0=.750;%Volatility value
alpha=1;% x^alpha is being expanded. This is currently for monte carlo only.
    y(1:Nn)=x0;
    w(1:Nn)=x0^(1-gamma)/(1-gamma);
Z(1:Nn)=(((1:Nn)-.5)*dNn-NnMid);

ZProb(1)=normcdf(.5*Z(1)+.5*Z(2),0,1);
ZProb(Nn)=1-normcdf(.5*Z(Nn)+.5*Z(Nn-1),0,1);
for nn=2:Nn-1
    ZProb(nn)=normcdf(.5*Z(nn)+.5*Z(nn+1),0,1)-normcdf(.5*Z(nn)+.5*Z(nn-1),0,1);
    %Above calculate probability mass in each probability subdivision.
end

 dt2=dt^2/2;
 dtsqrt=sqrt(dt);
 dtonehalf=dt.^1.5;

wnStart=1;

tic

for tt=1:Tt

    yy(wnStart:Nn)=((1-gamma)*w(wnStart:Nn)).^(1/(1-gamma));

    theta1=mu1;
    theta2=mu2;
    theta3=.5*sigma0^2*(-gamma);
    omega1=beta1-gamma;
    omega2=beta2-gamma;
    omega3=gamma-1;

    GG(wnStart:Nn)=theta1*yy(wnStart:Nn).^omega1+theta2*yy(wnStart:Nn).^omega2+theta3*yy(wnStart:Nn).^omega3;
    dGG(wnStart:Nn)=omega1*theta1*yy(wnStart:Nn).^(omega1-1)+omega2*theta2*yy(wnStart:Nn).^(omega2-1)+ ...
        omega3*theta3*yy(wnStart:Nn).^(omega3-1);
    DD(wnStart:Nn)=mu1*yy(wnStart:Nn).^beta1+mu2*yy(wnStart:Nn).^beta2;
    dGG2(wnStart:Nn)=theta1*omega1*(omega1-1).*yy(wnStart:Nn).^(omega1-2)+ ...
        theta2*omega2*(omega2-1).*yy(wnStart:Nn).^(omega2-2)+ ...
        theta3*omega3*(omega3-1).*yy(wnStart:Nn).^(omega3-2);
    QQ(wnStart:Nn)=sigma0^2*yy(wnStart:Nn).^(2*gamma);
    VV(wnStart:Nn)=sigma0.*yy(wnStart:Nn).^gamma;
%        d2GGVV(nn)=omega1*theta1*sigma0.*(omega1+gamma-1).*yy(nn).^(omega1+gamma-2)+ ...
%            omega2*theta2*sigma0.*(omega2+gamma-1).*yy(nn).^(omega2+gamma-2)+ ...
%            omega3*theta3*sigma0.*(omega3+gamma-1).*yy(nn).^(omega3+gamma-2);

    wMu0dt(wnStart:Nn)=GG(wnStart:Nn)*dt + dGG(wnStart:Nn).*DD(wnStart:Nn).*dt2 + ...
        .5*dGG2(wnStart:Nn).*QQ(wnStart:Nn).*dt2;

    dw(wnStart:Nn)=sigma0*Z(wnStart:Nn).*dtsqrt+ ...
        dGG(wnStart:Nn).*VV(wnStart:Nn).*(1-1/sqrt(3.0)).*Z(wnStart:Nn).*dtonehalf;%+ ...
        %0*d2GGVV(nn).*VV(nn).*(1/sqrt(2.0).*(1-sqrt(2.0)/2.0)).*dt.^2.0.*(Z(nn).^2-1);

    if(tt>0)
        w(isnan(w)==1)=0;
        wMu0dt(isnan(wMu0dt)==1)=0;
        wPrev=w;
        wMeanPrev=sum(ZProb(wnStart:Nn).*w(wnStart:Nn));%Calculate the mean.
        w(wnStart:Nn)=wMeanPrev+wMu0dt(wnStart:Nn)+ ...
           
sign(w(wnStart:Nn)-wMeanPrev+dw(wnStart:Nn)).*sqrt(abs(sign(w(wnStart:Nn)-wMeanPrev).*(w(wnStart:Nn)-wMeanPrev).^2+ ...
            sign(dw(wnStart:Nn)).*(dw(wnStart:Nn).^2)));

        D1wl=(11/6*w(NnMidl-2)-3*w(NnMidl-3)+3/2*w(NnMidl-4)-1/3*w(NnMidl-5))/dNn;
        D2wl=(35/12*w(NnMidl-2) -26/3*w(NnMidl-3)+ 19/2*w(NnMidl-4)-14/3*w(NnMidl-5)+11/12*w(NnMidl-6))/dNn.^2;
        DeltaD1w=(w(NnMidh+2)-w(NnMidl-2)-5*D1wl*dNn-5.0*D2wl*dNn.^2.0/1.0)/12.50/dNn;

        w(NnMidl-1)=w(NnMidl-2)+(.5*(D1wl+D2wl*dNn/1)+.5*(D1wl+D2wl*dNn/1+DeltaD1w))*dNn;
        w(NnMidl)=w(NnMidl-1)+(.5*(D1wl+D2wl*dNn/1+DeltaD1w)+.5*(D1wl+D2wl*dNn/1+2*DeltaD1w))*dNn;
        w(NnMidh)=w(NnMidl)+(.5*(D1wl+D2wl*dNn/1+2*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+3*DeltaD1w))*dNn;
        w(NnMidh+1)=w(NnMidh)+(.5*(D1wl+D2wl*dNn/1+3*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+4*DeltaD1w))*dNn;

        w1(1:Nn-1)=w(1:Nn-1);
        w2(1:Nn-1)=w(2:Nn);
        w(w1(:)>w2(:))=0;%Be careful;might not universally hold;

        w(ww(nn+1))&&(EnterLoop1==1))
%            w(1:nn)=0;
%            wnStart=nn+1;
%            EnterLoop1=0;
%        end
%        %Makes sure values are not smaller than zero.
%        if((w(nn)<0)&&(EnterLoop2==1))
%            w(1:nn)=0.0;
%            wnStart=nn+1;
%            EnterLoop2=0;
%        end
%    end
    end

end

y_w(1:Nn)=0;
y_w(wnStart:Nn) = ((1-gamma)*w(wnStart:Nn)).^(1/(1-gamma));
Dfy_w(wnStart:Nn)=0;
for nn=wnStart+1:Nn-1
    Dfy_w(nn) = (y_w(nn + 1) - y_w(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    %Change of variable derivative for densities
end
fy_w(1:Nn)=0;
for nn = wnStart:Nn-1
    fy_w(nn) = (normpdf(Z(nn),0, 1))/abs(Dfy_w(nn));%Origianl coordinates density
end

toc
str=input('Analytic Values calcuated; Press a key to start monte carlo');

sigma11(1:OrderA+1)=0;
mu11(1:OrderA+1)=0;
mu22(1:OrderA+1)=0;
sigma22(1:OrderA+1)=0;
% index 1 correponds to zero level since matlab indexing starts at one.
sigma11(1)=1;
mu11(1)=1;
mu22(1)=1;
sigma22(1)=1;

for k=1:(OrderA+1)
    if sigma0~=0
        sigma11(k)=sigma0^(k-1);
    end
    if mu1 ~= 0
        mu11(k)=mu1^(k-1);
    end
    if mu2 ~= 0
        mu22(k)=mu2^(k-1);
    end
    if sigma0~=0
        sigma22(k)=sigma0^(2*(k-1));
    end
end
Ft(1:Tt+1,1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0; %General time powers on hermite polynomials
Fp(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers on coefficients of hermite polynomials.
%Fp1(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers for bessel transformed coordinates.
%Pre-compute the time and power exponent values in small multi-dimensional arrays
for k = 0 : (OrderA+1)
    for m = 0:k
        l4 = k - m + 1;
        for n = 0 : m
            l3 = m - n + 1;
            for j = 0:n
                l2 = n - j + 1;
                l1 = j + 1;
                Ft(l1,l2,l3,l4) = dt^((l1-1) + (l2-1) + (l3-1) + .5* (l4-1));
                Fp(l1,l2,l3,l4) = (alpha + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
            end
        end
    end
end
%Below call the program that calculates the Ito-Taylor coeffs.
YCoeff = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma);
 %Calculate the density with monte carlo below.
 rng(85109634, 'twister')
 paths=100000;
 YY(1:paths)=x0;  %Original process monte carlo.
 Random1(1:paths)=0;
 for tt=1:Tt
     Random1=randn(size(Random1));
     HermiteP1(1,1:paths)=1;
     HermiteP1(2,1:paths)=Random1(1:paths);
     HermiteP1(3,1:paths)=Random1(1:paths).^2-1;
     YY0=YY;
     for k = 0 : OrderM
         for m = 0:k
             l4 = k - m + 1;
             for n = 0 : m
                 l3 = m - n + 1;
                 for j = 0:n
                     l2 = n - j + 1;
                     l1 = j + 1;
                     if(l4<=5)

                     YY(1:paths)=YY(1:paths) + YCoeff(l1,l2,l3,l4) * ...
                     mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                     YY0(1:paths).^Fp(l1,l2,l3,l4) .* HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);
                 %Above is original coordinates monte carlo equation.
                     end
                 end
             end
         end
     end
 end
 YY(YY<0)=0;
 sum(YY(:))/paths %origianl coordinates monte carlo average.
 sum(y_w(wnStart+1:Nn-1).*ZProb(wnStart+1:Nn-1)) %Original process average from coordinates
 theta+(x0-theta)*exp(-kappa*dt*Tt)%Mean reverting SDE original variable true average

 BinSize=.0075/2;%Please change this bin size accordingly. When data range is too small decrease it.
 %When density range is too large increase it.
 MaxCutOff=30;
 [YDensity,IndexOutY,IndexMaxY] = MakeDensityFromSimulation_Infiniti(YY,paths,BinSize,MaxCutOff);
 plot(y_w(wnStart+1:Nn-1),fy_w(wnStart+1:Nn-1),'r',IndexOutY(1:IndexMaxY),YDensity(1:IndexMaxY),'g');
 str=input('Blue graph is from squared orthogonal incrments method and red is from squared volatility, green is monte
carlo.');

end
```

---

### #790 — Amin (Topic Author)
*July 13, 2019, 8:49 AM*

As the friends would notice that the above program is quite accurate for reasonable volatilities but for very high
volatilities, the results start to deteriorate after a year and more. On the other hand, well written PDEs give precise
results even for extremely high volatilities. Therefore I decided to add PDEs to my existing research repertoire and
substitute numerical solution of Fokker Planck where it is easily available and continue with the analytics. Once a
precisely calculated density on a grid is available, it does not matter for further analytics if we obtained the grid
from Ito-Taylor density generation method or from numerical solution of a PDE. I will continue to try to make the
results of my Ito-Taylor density method sharply precise for extreme volatilities but in the mean time would also would
do analytics with numerical solution of forward Fokker-Planck PDEs. Here is a post I made on Linkedin that elaborates on
this idea.

https://www.linkedin.com/pulse/introducing-new-technologies-mathematical-finance-discipline-amin/

Introducing New Technologies in Mathematical Finance Discipline. A Totally New Paradigm.

I want to mention some interesting research achievements at Infiniti Derivatives Technologies in the area of stochastics
leading to huge improvements in mathematical methods of derivatives valuation, hedging, trading and risk management.

1.      Valuation of Path Dependent Stochastic Integrals on a PDE Grid.

It has been common historical wisdom that path dependent stochastic integrals cannot be calculated on a PDE grid. In our
new research, we debunk these past notions and show that there are methods of introducing path dependence on a PDE grid.
We have introduced new technologies that can calculate any stochastic path integral on a one or more dimensional PDE
grid in fraction of a second after the PDE has been solved. Of course calculating path integrals on higher dimensional
PDEs would require larger time but the time required to solve stochastic path integrals would strictly be far lesser
than required to solve the PDE itself. Some of these stochastic integrals could be for example conditional value of path
integral of squared volatility on the PDE grid for valuation of derivatives with stochastic volatility. Once the PDE has
been solved conditional backward stochastic integrals like exponential of path integral of interest rates representing
conditional bond prices or discount factor could also be calculated on the same PDE grid. From the PDE of interest
rates, you could calculate the backward evolution of difficult stochastic path integrals depending on interest rates of
whose PDE cannot be written easily. For Asian options, you could find the path integral of underlying as a forward
stochastic integral on the Fokker planck equation solved by a one dimensional PDE or on a two dimensional PDE with
stochastic volatility. The conditional values of these stochastic path integrals are available anywhere on the PDE grid
along the backward or forward evolution of the PDE. PDE methods can only calculate backward evolution of payoffs whose
explicit PDE has been written with arbitrary final data but we can calculate backward dynamic programming valuation of
far more complex stochastic integrals dependent on PDE underlying of whose explicit PDE is not available but conditional
of the value of the underlying as calculated in the forward PDE. We do not use any simulation or random numbers and only
rely on fast analytics to achieve the above mentioned goals.

2.      Calculation of Optimal Quantizers for Monte Carlo Simulations.

Once a Fokker planck PDE has been solved, we can calculate optimal quantizers in one or two dimensions in fraction of a
second. You could use these optimal quantizer schemes for forward evolution of stochastic integrals or backward dynamic
programming in a monte carlo setting. As opposed to existing optimal quantizer methods that are based on monte carlo
discretization schemes coupled with optimization techniques, we take a Fokker planck PDE solution as a starting point
which is more cheaply available and simply use very fast proprietary analytics to generate optimal quantizer grid that
can later be used for extremely fast monte carlo simulations and backward dynamic programming.

If you find any of this interesting and would like to implement this solution at your institution, you can email me at [[email protected]](http://mailto:anan2999@yahoo.com/) for further information and discussions. I want to mention again that none of these new technologies are in public domain.

---

### #791 — Amin (Topic Author)
*August 1, 2019, 8:19 AM*

Over the weekend, I will be writing two posts. First would explain the algorithm I used to remove instability from the
middle subdivisions in the density generation method and give a perfectly smooth output. This is important since many
friends would like to alter the program in their own fashion and would like to know how to remove the instability later
as the current method to remove instability is tailored to the grid I used and may fail on other grids. Once the basics
of the method are known, friends would be able to fix any grid with this method to remove instability.

Second post will give another algorithm that will be used if you have a probability distribution that is very close to
true distribution but the mean is slightly off. The algorithm would alter the probability distribution in a way that new
probability distribution is a valid distribution that it integrates to one and its mean integrates to true mean. I will
be doing both these things over the weekend.

---

### #792 — Amin (Topic Author)
*August 1, 2019, 8:36 AM*

I have decided to write a formal paper on the work I have done on this new density generation method for the
diffusions/SDEs. The paper will also show how to calculate stochastic integrals of the SDEs on the same grid used to
calculate the density in the first place. The paper will also show how to calculate the moments of these stochastic
integrals on the same grid. For example these mth moments can be written as

$E[ [ \int_0^T f(x) dt ]^m] $ and$E[ [ \int_0^T g(x) dz ]^m] $ where we are given the SDE of x(t) and we will first
evolve this SDE using our method and then calculate the stochastic integrals and then calculate moments of the same
stochastic integrals. This will be a very interesting paper and I hope that it will take no more than a month to
complete it and put it on SSRN. I might also add a section on backward dynamic programming for American options with
non-linear payoffs.

I will be posting many more programs here on Wilmott in coming weeks.

Though the method is not perfect with mean reverting equations with very high volatility and high mean reversions, I do
find solace in the fact that it works very well for a lot of other simpler SDEs. When we think of monte carlo
simulations, we know that monte carlo has been there for more than half a century but we have been able to take care of
nonlinear mean reversion SDE equations with monte carlo only very recently. So hopefully, other intelligent people will
make more interesting contributions to solve non-linear mean reverting SDEs in a few years.

---

### #793 — Amin (Topic Author)
*August 4, 2019, 6:36 PM*

In this new version of the program, I have also simulated the dt-integral given as $\int_0^t x(s)^{mp} ds$

for this I used the traditional formula given as

$\int_{t0}^{t1} x(s)^{mp} ds$

$=t1* x(t1)^{mp}- t0* x(t0)^{mp}$

$- mp * x(t0)^{(mp-1)}*(mu1*x(t0)^{beta1} + mu2*x(t0)^{beta2}) *(t1^2-t0^2)/2$

$-mp * x(t0)^{(mp-1)}*(sigma0 *x(t0)^{gamma})* N * (t1^{1.5}-t0^{1.5})/sqrt(3)$

$ -.5*mp*(mp-1)*sigma0^2*x(t0)^{(mp+2*gamma-2)}*(t1^2-t0^2)/2.0$

where SDE for the evolution of x(t) is given as

$dx(t)=mu1* x(t)^{beta1} dt + mu2* x(t)^{beta2} dt +sigma0* x(t)^{gamma} dz(t)$

I have used the same dt-integral simulation formula in monte carlo and my transition probabilities framework. I have
used original coordinates both in monte carlo and transition probabilities framework for calculation of dt-integrals.

Reference for the method for path-integrals/dt-integral I used in my program is my paper on SSRN titled "Solution of
Stochastic Volatility Models Using Variance Transition Probabilities and Path Integrals"

https://ssrn.com/abstract=2149231 or

[http://dx.doi.org/10.2139/ssrn.2149231](https://dx.doi.org/10.2139/ssrn.2149231)

For diffusions going into zero, you may see instabilities, I have not corrected for that yet in this initial version.

```
function [] = ItoTaylorDensityMRRecombining14A()
%Copyright Ahsan Amin. Infiniti derivatives Technologies.
%Please fell free to connect on linkedin: linkedin.com/in/ahsan-amin-0a53334
%or skype ahsan.amin2999
%In this program, I am simulating the SDE given as
%dy(t)=mu1 x(t)^beta1 dt + mu2 x(t)^beta2 dt +sigma x(t)^gamma dz(t)
%I have not directly simulated the SDE but simulated the transformed
%Bessel process version of the SDE and then changed coordinates to retreive
%the SDE in original coordinates.
%The present program will directly simulate only the Bessel Process version of the
%SDE in transformed coordinates.

%I have also simulated the dt-integral given as
% \int_0^t x(s)^mp ds  %%%here mp is power on x(s)
%for this I used the traditional formula given as
%\int_t0^t1 x(s)^mp ds=t1* x(t1)^mp- t0* x(t0)^mp - ...
% mp * x(t0)^(mp-1)*(mu1*x(t0)^beta1 + mu2*x(t0)^beta2) *(t1^2-t0^2)/2 -...
% mp * x(t0)^(mp-1)*(sigma0 *x(t0)^gamma)* N * (t1^1.5-t0^1.5)/sqrt(3) -...
%.5*mp*(mp-1)*sigma0^2*x(t0)^(mp+2*gamma-2)*(t1^2-t0^2)/2.0;

%I have used the same simulation formula in monte carlo and my
%transition probabilities framework. I have used original coordinates
%both in monte carlo and transition probabilities framework for calculation
% of dt-integrals.
% REference for the method for path-integrals/dt-integral I used in my
%program is my paper on
% SSRN titled "Solution of Stochastic Volatility Models Using Variance
%Transition Probabilities and Path Integrals"
%https://ssrn.com/abstract=2149231 or
%http://dx.doi.org/10.2139/ssrn.2149231
%For diffusions going into zero, you may see instabilities, I have not
%corrected for that yet in this initial version.
dt=.125/8;   % Simulation time interval.%For diffusions close to zero
             %decrease dt for accuracy.
Tt=8*8;     % Number of simulation levels. Terminal time= Tt*dt; //.125/8*8*8=1 year;
OrderA=2;  %Keep at two.
OrderM=2;  %Keep at two.
dNn=.2/1;   % Normal density subdivisions width. would change with number of subdivisions
Nn=40;  % No of normal density subdivisions
NnMidl=20;%One half left from mid of normal density
NnMidh=21;%One half right from the mid of normal density
NnMid=4.0;
x0=1.0;   % starting value of SDE
beta1=0.0;   % the first drift term power.
beta2=1.0;   % Second drift term power.
gamma=.850;   % volatility power.
kappa=.950;   %mean reversion parameter.
theta=1.0;   %mean reversion target
%Below you can get rid of kappa and theta and freely choose your own values
%for both drift coefficients.
mu1=0*theta*kappa;   % first drift coefficient.
mu2=-0*kappa;    % Second drift coefficient.
sigma0=.450;%Volatility value
mp=.5; %power on x(t) in dt-integral. I have tested powers .5,1, and 2.0
%may fail for extrme high or low powers.
alpha=1;% x^alpha is being expanded. This is currently for monte carlo only.
y(1:Nn)=x0;
w(1:Nn)=x0^(1-gamma)/(1-gamma);
x2dt0(1:Nn)=0.0;
x2dt(1:Nn,1:Tt)=0.0;
Z(1:Nn)=(((1:Nn)-.5)*dNn-NnMid);

ZProb(1)=normcdf(.5*Z(1)+.5*Z(2),0,1);
ZProb(Nn)=1-normcdf(.5*Z(Nn)+.5*Z(Nn-1),0,1);
for nn=2:Nn-1
    ZProb(nn)=normcdf(.5*Z(nn)+.5*Z(nn+1),0,1)-normcdf(.5*Z(nn)+.5*Z(nn-1),0,1);
    %Above calculate probability mass in each probability subdivision.
end

 dt2=dt^2/2;
 dtsqrt=sqrt(dt);
 dtonehalf=dt.^1.5;

wnStart=1;
tic
Zt(1:Nn,1:Nn)=0.0;

for tt=1:Tt

    t0=(tt-1)*dt;
    t1=tt*dt;
    yy(wnStart:Nn)=((1-gamma)*w(wnStart:Nn)).^(1/(1-gamma));

    theta1=mu1;
    theta2=mu2;
    theta3=.5*sigma0^2*(-gamma);
    omega1=beta1-gamma;
    omega2=beta2-gamma;
    omega3=gamma-1;

    GG(wnStart:Nn)=theta1*yy(wnStart:Nn).^omega1+theta2*yy(wnStart:Nn).^omega2+theta3*yy(wnStart:Nn).^omega3;
    dGG(wnStart:Nn)=omega1*theta1*yy(wnStart:Nn).^(omega1-1)+omega2*theta2*yy(wnStart:Nn).^(omega2-1)+ ...
        omega3*theta3*yy(wnStart:Nn).^(omega3-1);
    DD(wnStart:Nn)=mu1*yy(wnStart:Nn).^beta1+mu2*yy(wnStart:Nn).^beta2;
    dGG2(wnStart:Nn)=theta1*omega1*(omega1-1).*yy(wnStart:Nn).^(omega1-2)+ ...
        theta2*omega2*(omega2-1).*yy(wnStart:Nn).^(omega2-2)+ ...
        theta3*omega3*(omega3-1).*yy(wnStart:Nn).^(omega3-2);
    QQ(wnStart:Nn)=sigma0^2*yy(wnStart:Nn).^(2*gamma);
    VV(wnStart:Nn)=sigma0.*yy(wnStart:Nn).^gamma;
    d_dGG_VV_dyy(wnStart:Nn)= ...
        sigma0.*omega1.*theta1.*(omega1+gamma-1).*yy(wnStart:Nn).^(omega1+gamma-2) + ...
        sigma0.*omega2.*theta2.*(omega2+gamma-1).*yy(wnStart:Nn).^(omega2+gamma-2) + ...
        sigma0.*omega3.*theta3.*(omega3+gamma-1).*yy(wnStart:Nn).^(omega3+gamma-2);

    wMu0dt(wnStart:Nn)=GG(wnStart:Nn)*dt + dGG(wnStart:Nn).*DD(wnStart:Nn).*dt2 + ...
        .5*dGG2(wnStart:Nn).*QQ(wnStart:Nn).*dt2;%

    dw(wnStart:Nn)=(sigma0.*Z(wnStart:Nn).^1.*dtsqrt+ ...
        dGG(wnStart:Nn).*VV(wnStart:Nn).*(1-1/sqrt(3.0)).*Z(wnStart:Nn).^1.*dtonehalf + ... %;%+ ...
        d_dGG_VV_dyy(wnStart:Nn).*VV(wnStart:Nn).*(1/sqrt(2.0).*(1-sqrt(2.0)/2.0)).*dt.^2.0.*(Z(wnStart:Nn).^2-1));
    %I have added an extr term in above dw

    w(isnan(w)==1)=0;
    wMu0dt(isnan(wMu0dt)==1)=0;
    wMeanPrev=sum(ZProb(wnStart:Nn).*w(wnStart:Nn));%Calculate the mean.

    w(wnStart:Nn)=wMeanPrev+wMu0dt(wnStart:Nn)+ ...
        sign(w(wnStart:Nn)-wMeanPrev+dw(wnStart:Nn)).* ...
        sqrt(abs(sign(w(wnStart:Nn)-wMeanPrev).*(w(wnStart:Nn)-wMeanPrev).^2+ ...
        sign(dw(wnStart:Nn)).*((dw(wnStart:Nn)).^2)));

%Calculation of dt-integral starts
    yyPrev(wnStart:Nn)=yy(wnStart:Nn);
    yy(wnStart:Nn)=((1-gamma)*w(wnStart:Nn)).^(1/(1-gamma));
%Below we calculate transition probabilities between the process in
%original coordinates based on brownian motion transition probabilities.
%Below b1 is brownian motion subdivisions at time t0 and b2 are brownian
%motion subdivisions at time t1=t0+dt;
    b1(1:Nn)=x0+sigma0*sqrt((tt-1)*dt)*Z(1:Nn);%Simulate brownian motion
        %to the last date
    b2(1:Nn)=x0+sigma0*sqrt(tt*dt)*Z(1:Nn);%Simulate brownian motion to
    %recent date
   for mm=1:Nn
    Zt(mm,1:Nn)=(b2(1:Nn)-b1(mm))/sigma0/sqrt(dt);%Get the transition value
   end
   %Zt is the normal random number value which is used to mth subdivision
   %of b1 at t0 to nth subdivision of b2 at t1. This will remain same for
   %all the diffusions with volatility sigma0. And we later use the same
   % normal random number value for our calculations of evolution of
   %dt-integrals.

   %dZ2(2:Nn-1)=(b2(3:Nn)-b2(1:Nn-2))/2.0;
   %dZ2(1)=(b2(2)-b2(1));
   %dZ2(Nn)=(b2(Nn)-b2(Nn-1));

   dZ2(1:Nn)=sigma0*sqrt(t1)*dNn;

   %Above dZ2 are subdivision widths. they are also equal to
   %sigma0*sqrt(t1)*dNn. They are used to calculate integrated transition
   %probability mass that arrives into a certain subdivision of b2 at time
   %t1

   Mm=Nn;
   for nn=1:Nn
   pt(nn,1:Mm)=exp(-.5* ((b2(1:Mm)-b1(nn))/(sigma0*sqrt(dt))).^2)./sqrt(2*pi*sigma0^2*dt).* ...
       (dZ2(1:Mm));
   %above pt is transition probability
   end

   %for nn=1:Nn
   %Sumpt(nn)=sum(pt(nn,:));
   %end
   %Sumpt
   if(tt==1)
       pt0(1:Nn)=ZProb(1:Nn);
   end

    for mm1=1:Nn
        for mm0=1:Nn

            if(tt==1)
                x2dt(mm1,tt)=x2dt(mm1,tt)+x2dt0(mm0).*pt0(mm1)+ ...
                    (yy(mm1).^mp*t1-yyPrev(mm0).^mp*t0- ...
                    (yy(mm1)^mp-yyPrev(mm0).^mp)*t0).*pt(mm0,mm1).*ZProb(mm0);
            end
            if(tt>1)

            x2dt(mm1,tt)=x2dt(mm1,tt)+x2dt(mm0,tt-1).*pt(mm0,mm1)+ ...
                (yy(mm1).^mp*t1-yyPrev(mm0).^mp*t0- ...
                mp*(mu1*yyPrev(mm0).^(mp+beta1-1)+mu2*yyPrev(mm0).^(mp+beta2-1)).*(t1^2-t0^2)/2 - ...
                .5*mp*(mp-1).*sigma0^2*yyPrev(mm0).^(mp+2*gamma-2).*(t1^2-t0^2)/2 - ...
                mp*sigma0*yyPrev(mm0).^(mp+gamma-1) .*Zt(mm0,mm1).*(t1^1.5-t0^1.5)/sqrt(3)) .* ...
                pt(mm0,mm1).*ZProb(mm0);

            %This calculates the dt-integral using transition probabilities
            %framework
            end
        end
    end

    D1wl=(11/6*w(NnMidl-2)-3*w(NnMidl-3)+3/2*w(NnMidl-4)-1/3*w(NnMidl-5))/dNn;
    D2wl=(35/12*w(NnMidl-2) -26/3*w(NnMidl-3)+ 19/2*w(NnMidl-4)-14/3*w(NnMidl-5)+11/12*w(NnMidl-6))/dNn.^2;
    DeltaD1w=(w(NnMidh+2)-w(NnMidl-2)-5*D1wl*dNn-5.0*D2wl*dNn.^2.0/1.0)/12.50/dNn;

    wll(NnMidl-1)=w(NnMidl-2)+(.5*(D1wl+D2wl*dNn/1)+.5*(D1wl+D2wl*dNn/1+DeltaD1w))*dNn;
    wll(NnMidl)=wll(NnMidl-1)+(.5*(D1wl+D2wl*dNn/1+1.0*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+2.0*DeltaD1w))*dNn;
    wll(NnMidh)=wll(NnMidl)+(.5*(D1wl+D2wl*dNn/1+2.0*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+3.0*DeltaD1w))*dNn;
    wll(NnMidh+1)=wll(NnMidh)+(.5*(D1wl+D2wl*dNn/1+3.0*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+4.0*DeltaD1w))*dNn;

%
    D1wh=(-11/6*w(NnMidh+2)+3*w(NnMidh+3)-3/2*w(NnMidh+4)+1/3*w(NnMidh+5))/dNn;
    D2wh=(35/12*w(NnMidh+2) -26/3*w(NnMidh+3)+ 19/2*w(NnMidh+4)-14/3*w(NnMidh+5)+11/12*w(NnMidh+6))/dNn.^2;
    DeltaD1w=(w(NnMidh+2)-w(NnMidl-2)-5*D1wh*dNn-5.0*D2wh*dNn.^2.0/1.0)/12.50/dNn;
%
    whh(NnMidh+1)=w(NnMidh+2)-(.5*(D1wh+D2wh*dNn/1)+.5*(D1wh+D2wh*dNn/1+DeltaD1w))*dNn;
    whh(NnMidh)=whh(NnMidh+1)-(.5*(D1wh+D2wh*dNn/1+1*DeltaD1w)+.5*(D1wh+D2wh*dNn/1+2.0*DeltaD1w))*dNn;
    whh(NnMidl)=whh(NnMidh)-(.5*(D1wh+D2wh*dNn/1+2.0*DeltaD1w)+.5*(D1wh+D2wh*dNn/1+3.0*DeltaD1w))*dNn;
    whh(NnMidl-1)=whh(NnMidl)-(.5*(D1wh+D2wh*dNn/1+3.0*DeltaD1w)+.5*(D1wh+D2wh*dNn/1+4.0*DeltaD1w))*dNn;

    w(NnMidh+1)=.5*whh(NnMidh+1)+.5*wll(NnMidh+1);
    w(NnMidh)=.5*whh(NnMidh)+.5*wll(NnMidh);
    w(NnMidl)=.5*whh(NnMidl)+.5*wll(NnMidl);
    w(NnMidl-1)=.5*whh(NnMidl-1)+.5*wll(NnMidl-1);

        w1(1:Nn-1)=w(1:Nn-1);
        w2(1:Nn-1)=w(2:Nn);
        w(w1(:)>w2(:))=0;%Be careful;might not universally hold;

        w(w<0)=0.0;
        for nn=1:Nn
            if(w(nn)<=0)
                wnStart=nn+1;
            end
        end
    end

xx2dt(1:Nn)=0.0;
xx2dt(1:Nn)=x2dt(1:Nn,Tt);%./ZProb(1:Nn);
xx2dt(1:Nn)=xx2dt(1:Nn)./ZProb(1:Nn); %We have to remove probability from
%the variable x2dt. In calculations, we had x2dt equal to
% dt-integral *probability of being in the particular subdivision.
y_w(1:Nn)=0;
y_w(wnStart:Nn) = ((1-gamma)*w(wnStart:Nn)).^(1/(1-gamma));
Dfy_w(wnStart:Nn)=0;
Dfx2dt(1:Nn)=0;
for nn=2:Nn-1
    Dfx2dt(nn) = (xx2dt(nn + 1) - xx2dt(nn - 1))/(Z(nn + 1) - Z(nn - 1));
end

fx2dt(1:Nn)=0;
for nn = 2:Nn-1
    fx2dt(nn) = (normpdf(Z(nn),0, 1))/abs(Dfx2dt(nn));%Origianl coordinates density
end
fx2dt
for nn=wnStart+1:Nn-1
    Dfy_w(nn) = (y_w(nn + 1) - y_w(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    %Change of variable derivative for densities
end
fy_w(1:Nn)=0;
for nn = wnStart:Nn-1
    fy_w(nn) = (normpdf(Z(nn),0, 1))/abs(Dfy_w(nn));%Origianl coordinates density
end

toc
str=input('Analytic Values calcuated; Press a key to start monte carlo');

sigma11(1:OrderA+1)=0;
mu11(1:OrderA+1)=0;
mu22(1:OrderA+1)=0;
sigma22(1:OrderA+1)=0;
% index 1 correponds to zero level since matlab indexing starts at one.
sigma11(1)=1;
mu11(1)=1;
mu22(1)=1;
sigma22(1)=1;

for k=1:(OrderA+1)
    if sigma0~=0
        sigma11(k)=sigma0^(k-1);
    end
    if mu1 ~= 0
        mu11(k)=mu1^(k-1);
    end
    if mu2 ~= 0
        mu22(k)=mu2^(k-1);
    end
    if sigma0~=0
        sigma22(k)=sigma0^(2*(k-1));
    end
end
Ft(1:Tt+1,1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0; %General time powers on hermite polynomials
Fp(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers on coefficients of hermite polynomials.
%Fp1(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers for bessel transformed coordinates.
%Pre-compute the time and power exponent values in small multi-dimensional arrays
for k = 0 : (OrderA+1)
    for m = 0:k
        l4 = k - m + 1;
        for n = 0 : m
            l3 = m - n + 1;
            for j = 0:n
                l2 = n - j + 1;
                l1 = j + 1;
                Ft(l1,l2,l3,l4) = dt^((l1-1) + (l2-1) + (l3-1) + .5* (l4-1));
                Fp(l1,l2,l3,l4) = (alpha + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
            end
        end
    end
end
%Below call the program that calculates the Ito-Taylor coeffs.
YCoeff = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma);
 %Calculate the density with monte carlo below.
 rng(85109634, 'twister')
 paths=200000;
 YY(1:paths)=x0;  %Original process monte carlo.
 YY2dt(1:paths)=0.0;
 Random1(1:paths)=0;
 for tt=1:Tt
     t1=tt*dt;
     t0=(tt-1)*dt;
     Random1=randn(size(Random1));
     HermiteP1(1,1:paths)=1;
     HermiteP1(2,1:paths)=Random1(1:paths);
     HermiteP1(3,1:paths)=Random1(1:paths).^2-1;
     YY0=YY;
     YYPrev=YY;
     for k = 0 : OrderM
         for m = 0:k
             l4 = k - m + 1;
             for n = 0 : m
                 l3 = m - n + 1;
                 for j = 0:n
                     l2 = n - j + 1;
                     l1 = j + 1;
                     if(l4<=5)

                     YY(1:paths)=YY(1:paths) + YCoeff(l1,l2,l3,l4) * ...
                     mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                     YY0(1:paths).^Fp(l1,l2,l3,l4) .* HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);
                 %Above is original coordinates monte carlo equation.
                     end
                 end
             end
         end
     end
     YY2dt(1:paths)=YY2dt(1:paths)+t1*YY(1:paths).^mp-t0*YYPrev(1:paths).^mp- ...
         mp.*(mu1*YYPrev(1:paths).^(mp+beta1-1)+mu2*YYPrev(1:paths).^(mp+beta2-1)).*(t1^2-t0^2)/2.0 - ...
         .5*mp*(mp-1).*sigma0^2*YYPrev(1:paths).^(mp+2*gamma-2).*(t1^2-t0^2)/2 - ...
         mp*sigma0*YYPrev(1:paths).^(mp+gamma-1) .*HermiteP1(2,1:paths).*(t1^1.5-t0^1.5)/sqrt(3);
 end
 YY(YY<0)=0;

 sum(YY2dt(:))/paths   %dt-integral average from monte carlo
 sum(xx2dt(2:Nn-1).*ZProb(2:Nn-1)) %dt-integral from transition
 %probabilities framework.

 sum(YY(:))/paths %origianl coordinates monte carlo average.
 sum(y_w(wnStart+1:Nn-1).*ZProb(wnStart+1:Nn-1)) %Original process average from coordinates
 theta+(x0-theta)*exp(-kappa*dt*Tt)%Mean reverting SDE original variable true average

 BinSize=.0075*2;%Please change this bin size accordingly. When data range is too small decrease it.
 %When density range is too large increase it.
 MaxCutOff=30;
 [Y2dtDensity,IndexOutY2dt,IndexMaxY2dt] = MakeDensityFromSimulation_Infiniti(YY2dt,paths,BinSize,MaxCutOff);
 plot(xx2dt(2:Nn-1),fx2dt(2:Nn-1),'r',IndexOutY2dt(1:IndexMaxY2dt),Y2dtDensity(1:IndexMaxY2dt),'g');
 str=input('red line is dt-integral from transition probability framework , green is monte carlo.');

 BinSize=.0075/1;%Please change this bin size accordingly. When data range is too small decrease it.
 %When density range is too large increase it.
 MaxCutOff=30;
 [YDensity,IndexOutY,IndexMaxY] = MakeDensityFromSimulation_Infiniti(YY,paths,BinSize,MaxCutOff);
 plot(y_w(wnStart+1:Nn-1),fy_w(wnStart+1:Nn-1),'r',IndexOutY(1:IndexMaxY),YDensity(1:IndexMaxY),'g');
 str=input('red line is density of SDE from squared orthogonal incrments method, green is monte carlo.');

end
```

In a day or two, I will also post algorithm for removing instability from my programs as I promised.

Please note that transition probabilities dt-integral/Ito-integral density calculation program posted only works when
diffusion remains strictly positive. This is a programming problem and a limitation only in the introductory version and
in later versions, I will fix this problem and remove the restriction.  The part of the program that calculates the
density of SDE works in almost all cases even when the density hits zero, it is only the new transition probabilities
Ito-Integral part that is is currently limited to positive domain.  The algorithm to calculate the density of SDEs is
99.999% perfect when the diffusion takes just one term in the drift. Only when a second term is introduced in the drift
and there are non-linear dynamics that the program has problems for highly non-linear equations.

---

### #794 — Amin (Topic Author)
*August 23, 2019, 12:16 PM*

I have been able to alter the new method to find solution to densities of mean reverting SDEs with very high volatility
and very high mean reversions to perfect precision. I will be posting the matlab program over the weekend after properly
fromatting the program and making notes/comments. I Was able to add second order effect from the existing volatility.
After addition of second order volatility effect, we get perfect fit to shape of the monte carlo overlaid density and
the mean is remarkably exact to within a few basis points from the true mean. I will be posting the program over the
weekend. This is a very remarkable discovery and I am sure friends would love the new program.

---

### #795 — Amin (Topic Author)
*August 25, 2019, 5:29 PM*

Sorry Double Post. Deleted.

---

### #796 — Amin (Topic Author)
*August 25, 2019, 5:40 PM*

My second order correction to evolution of density of non-linear mean-reverting SDEs is only approximate but is a huge
improvement on first order and gives a very good idea about structure of the optimal correction. Please go ahead and try
to think of a better correction but please do not forget to give me credit for this work.

In this program, I am simulating the SDE given as    dy(t)=mu1 x(t)^beta1 dt + mu2 x(t)^beta2 dt +sigma x(t)^gamma dz(t)

where mu1=kappa*theta and mu2=-kappa with  beta1=0 and beta2=1;

I have not directly simulated the SDE but simulated the transformed  Bessel process version of the SDE and then changed
coordinates to retreive

the SDE in original coordinates. The present program will analytically evolve only the Bessel Process version of the

SDE in transformed coordinates. The present program is meant for mean-reversion SDEs that take two terms in non-linear
drift. It will work for simpler SDEs but for that you will  have to turn SecondOC variable, second order correction
variable to zero.

For diffusions going into zero, you may see instabilities, I have not corrected for that yet in this initial
version. Heston is still not good as substantial density goes into zero at practically realistic vol. Heston when
density does not hit zero will work perfectly.

I try volatility-power=gamma above .65 or .70; gamma=.95 is proxy for lognormal, the best and coveted SV model but not
used due to lack of tractibility.

Heston and even smaller gamma will work far better when x0=1 and theta=1 as in Interest rate LMM like models with local
volatility.

Very close to zero, heston density simulation does not work very well with this program. Whenever substantial  density
goes into zero, performance of the current program deteriorates.

---

### #797 — Amin (Topic Author)
*August 26, 2019, 5:34 PM*

I have removed the previous program that I posted yesterday as it was very suboptimal compared to the corrected version.
I am posting a new good program now that works excellently. Now Heston is also working with my new program in many many
cases even on higher volatilities. I am sure friends would love this program. Though there is need for more theoretical
research, I doubt if the program below can altered significantly now since it is already working very well. Here is the
only line of code with the second order correction that I newly added to the  existing program

SecondOC(wnStart:Nn)=-.0027*((tt-1)*dt).*dt./gamma^(2*gamma-1).*sigma0^4./(w(wnStart:Nn)*(1-gamma)).*(Z(wnStart:Nn).^2-1);

Here is the new  code. Most diffusions going into zero are working perfectly fine now. I will be posting some graphs
produced with this code tomorrow.

```
function [] = ItoTaylorDensityMRRecombining14F2Wilmott()
%Copyright Ahsan Amin. Infiniti derivatives Technologies.
%Please fell free to connect on linkedin: linkedin.com/in/ahsan-amin-0a53334
%or skype ahsan.amin2999
%In this program, I am simulating the SDE given as
%dy(t)=mu1 x(t)^beta1 dt + mu2 x(t)^beta2 dt +sigma x(t)^gamma dz(t)
%where mu1=kappa*theta and mu2=-kappa with
%beta1=0 and beta2=1;
%I have not directly simulated the SDE but simulated the transformed
%Bessel process version of the SDE and then changed coordinates to retreive
%the SDE in original coordinates.
%The present program will analytically evolve only the Bessel Process version of the
%SDE in transformed coordinates.
%The present program is meant for mean-reversion SDEs that take two terms
%in non-linear drift. It will work for simpler SDEs but for that you will
%have to turn SecondOC variable, second order correction variable to zero.
%
%For diffusions going into zero, you may see instabilities, I have not
%corrected for that yet in this initial version.
%Heston is still not good as substantial density goes into zero at
%practically realistic vol.
%Heston when density does not hit zero will work perfectly.
%I try volatility power/gamma above .65 0r .70
%gamma=.95 is proxy for lognormal, the best and coveted SV model but
%not used due to lack of tractibility.
%HEston and even smaller gamma will work far better when
%x0=1 and theta=1 as in Interest rate LMM like models with local volatility.
%Very close to zero, heston does not work very well. Whenever substantial
%density goes into zero, model performance deteriorates.
dt=.125/32;   % Simulation time interval.%For diffusions close to zero
             %decrease dt for accuracy.
Tt=32*8;     % Number of simulation levels. Terminal time= Tt*dt; //.125/32*32*16=2 year;
OrderA=2;  %Keep at two.
OrderM=2;  %Keep at two.
dtM=.125/4;%Monte carlo time interval size dtM.
TtM=4*8;%Monte carlo number of simulation intervals.

dNn=.2/1;   % Normal density subdivisions width. would change with number of subdivisions
Nn=46;  % No of normal density subdivisions
NnMidl=23;%One half left from mid of normal density(low)
NnMidh=24;%One half right from the mid of normal density(high)
NnMid=4.0;

x0=.25;   % starting value of SDE
beta1=0.0;   % the first drift term power.
beta2=1.0;   % Second drift term power.
gamma=.95;   % volatility power.
kappa=.950;   %mean reversion parameter.
theta=.10;   %mean reversion target

mu1=1*theta*kappa;   %first drift coefficient.
mu2=-1*kappa;    % Second drift coefficient.
sigma0=.90;%Volatility value
alpha=1;% x^alpha is being expanded. This is currently for monte carlo only.
alpha1=1-gamma;
y(1:Nn)=x0;
w(1:Nn)=x0^(1-gamma)/(1-gamma);
Z(1:Nn)=(((1:Nn)-3.5)*dNn-NnMid);

ZProb(1)=normcdf(.5*Z(1)+.5*Z(2),0,1)-normcdf(.5*Z(1)+.5*Z(2)-dNn,0,1);
ZProb(Nn)=normcdf(.5*Z(Nn)+.5*Z(Nn-1)+dNn,0,1)-normcdf(.5*Z(Nn)+.5*Z(Nn-1),0,1);

for nn=2:Nn-1
    ZProb(nn)=normcdf(.5*Z(nn)+.5*Z(nn+1),0,1)-normcdf(.5*Z(nn)+.5*Z(nn-1),0,1);
    %Above calculate probability mass in each probability subdivision.
end

 dt2=dt^2/2;
 dt3=dt^3/6.0;
 dtsqrt=sqrt(dt);
 dtonehalf=dt.^1.5;

wnStart=1;
tic

for tt=1:Tt

    yy(wnStart:Nn)=((1-gamma)*w(wnStart:Nn)).^(1/(1-gamma));

    theta1=mu1;
    theta2=mu2;
    theta3=.5*sigma0^2*(-gamma);
    omega1=beta1-gamma;
    omega2=beta2-gamma;
    omega3=gamma-1;

    GG(wnStart:Nn)=theta1*yy(wnStart:Nn).^omega1+theta2*yy(wnStart:Nn).^omega2+theta3*yy(wnStart:Nn).^omega3;
    dGG(wnStart:Nn)=omega1*theta1*yy(wnStart:Nn).^(omega1-1)+omega2*theta2*yy(wnStart:Nn).^(omega2-1)+ ...
        omega3*theta3*yy(wnStart:Nn).^(omega3-1);
    DD(wnStart:Nn)=mu1*yy(wnStart:Nn).^beta1+mu2*yy(wnStart:Nn).^beta2;
    dGG2(wnStart:Nn)=theta1*omega1*(omega1-1).*yy(wnStart:Nn).^(omega1-2)+ ...
        theta2*omega2*(omega2-1).*yy(wnStart:Nn).^(omega2-2)+ ...
        theta3*omega3*(omega3-1).*yy(wnStart:Nn).^(omega3-2);
    QQ(wnStart:Nn)=sigma0^2*yy(wnStart:Nn).^(2*gamma);
    ddGGDD(wnStart:Nn)=mu1*omega1*theta1*(omega1+beta1-1).*yy(wnStart:Nn).^(omega1+beta1-2)+ ...
        mu1*omega2*theta2*(omega2+beta1-1).*yy(wnStart:Nn).^(omega2+beta1-2)+ ...
        mu1*omega3*theta3*(omega3+beta1-1).*yy(wnStart:Nn).^(omega3+beta1-2)+ ...
        mu2*omega1*theta1*(omega1+beta2-1).*yy(wnStart:Nn).^(omega1+beta2-2)+ ...
        mu2*omega2*theta2*(omega2+beta2-1).*yy(wnStart:Nn).^(omega2+beta2-2)+ ...
        mu2*omega3*theta3*(omega3+beta2-1).*yy(wnStart:Nn).^(omega3+beta2-2);
    d2dGGDD(wnStart:Nn)=mu1*omega1*theta1*(omega1+beta1-1).*(omega1+beta1-2).*yy(wnStart:Nn).^(omega1+beta1-3)+ ...
        mu1*omega2*theta2*(omega2+beta1-1).*(omega2+beta1-2).*yy(wnStart:Nn).^(omega2+beta1-3)+ ...
        mu1*omega3*theta3*(omega3+beta1-1).*(omega3+beta1-2).*yy(wnStart:Nn).^(omega3+beta1-3)+ ...
        mu2*omega1*theta1*(omega1+beta2-1).*(omega1+beta2-2).*yy(wnStart:Nn).^(omega1+beta2-3)+ ...
        mu2*omega2*theta2*(omega2+beta2-1).*(omega2+beta2-2).*yy(wnStart:Nn).^(omega2+beta2-3)+ ...
        mu2*omega3*theta3*(omega3+beta2-1).*(omega3+beta2-2).*yy(wnStart:Nn).^(omega3+beta2-3);
    ddGG2QQ(wnStart:Nn)=theta1*sigma0^2.*omega1*(omega1-1).*(omega1+2*gamma-2).*yy(wnStart:Nn).^(omega1+2*gamma-3)+ ...
        sigma0^2*theta2*omega2*(omega2-1).*(omega2+2*gamma-2).*yy(wnStart:Nn).^(omega2+2*gamma-3)+ ...
        sigma0^2*theta3*omega3*(omega3-1).*(omega3+2*gamma-2).*yy(wnStart:Nn).^(omega3+2*gamma-3);
   
d2dGG2QQ(wnStart:Nn)=theta1*sigma0^2.*omega1*(omega1-1).*(omega1+2*gamma-2).*(omega1+2*gamma-3).*yy(wnStart:Nn).^(omega1+2*gamma-4)+
...
        sigma0^2*theta2*omega2*(omega2-1).*(omega2+2*gamma-2).*(omega2+2*gamma-3).*yy(wnStart:Nn).^(omega2+2*gamma-4)+
...
        sigma0^2*theta3*omega3*(omega3-1).*(omega3+2*gamma-2).*(omega3+2*gamma-3).*yy(wnStart:Nn).^(omega3+2*gamma-4);

    VV(wnStart:Nn)=sigma0.*yy(wnStart:Nn).^gamma;
    d_dGG_VV_dyy(wnStart:Nn)= ...
        sigma0.*omega1.*theta1.*(omega1+gamma-1).*yy(wnStart:Nn).^(omega1+gamma-2) + ...
        sigma0.*omega2.*theta2.*(omega2+gamma-1).*yy(wnStart:Nn).^(omega2+gamma-2) + ...
        sigma0.*omega3.*theta3.*(omega3+gamma-1).*yy(wnStart:Nn).^(omega3+gamma-2);

    wMu0dt(wnStart:Nn)=GG(wnStart:Nn)*dt + dGG(wnStart:Nn).*DD(wnStart:Nn).*dt2 + ...
        .5*dGG2(wnStart:Nn).*QQ(wnStart:Nn).*dt2 + ...
        ddGGDD(wnStart:Nn).*DD(wnStart:Nn).*dt3 + ...
        .5*ddGG2QQ(wnStart:Nn).*DD(wnStart:Nn).*dt3 + ...
        .5*d2dGGDD(wnStart:Nn).*QQ(wnStart:Nn).*dt3 + ...
        .25*d2dGG2QQ(wnStart:Nn).*QQ(wnStart:Nn).*dt3;
%    c0(wnStart:Nn)=-1*d_dGG_VV_dyy(wnStart:Nn).*VV(wnStart:Nn).*(1/sqrt(2.0).*(1-sqrt(2.0)/2.0)).*dt.^2.0;
    c1(wnStart:Nn)=sigma0.*dtsqrt+dGG(wnStart:Nn).*VV(wnStart:Nn).*(1-1/sqrt(3.0)).*dtonehalf ;
    c2(wnStart:Nn)=d_dGG_VV_dyy(wnStart:Nn).*VV(wnStart:Nn).*(1/sqrt(2.0).*(1-sqrt(2.0)/2.0)).*dt.^2.0;
%    dw0(wnStart:Nn)=(sigma0.*Z(wnStart:Nn).^1.*dtsqrt+ ...
%        dGG(wnStart:Nn).*VV(wnStart:Nn).*(1-1/sqrt(3.0)).*Z(wnStart:Nn).^1.*dtonehalf + ... %;%+ ...
%        1*d_dGG_VV_dyy(wnStart:Nn).*VV(wnStart:Nn).*(1/sqrt(2.0).*(1-sqrt(2.0)/2.0)).*dt.^2.0.*(Z(wnStart:Nn).^2-1));
    dw(wnStart:Nn)=c1(wnStart:Nn).*Z(wnStart:Nn) + ...
        c2(wnStart:Nn).*(Z(wnStart:Nn).^2-1);
   dw2(wnStart:Nn)=c1(wnStart:Nn).^2.0.*Z(wnStart:Nn).^2 + ...
        c2(wnStart:Nn).^2.*(Z(wnStart:Nn).^4-2*Z(wnStart:Nn).^2+1);

    w(isnan(w)==1)=0;

    wMu0dt(isnan(wMu0dt)==1)=0;

    wMeanPrev=sum(ZProb(wnStart:Nn).*w(wnStart:Nn));%Calculate the mean.

    %Below is second order correction.Uses second hermite polynomial
    SecondOC(wnStart:Nn)=-0.027*((tt-1)*dt).* ...
        (dt)./gamma^(2*gamma-1).* ...
        sigma0^4./(w(wnStart:Nn)*(1-gamma)).*(Z(wnStart:Nn).^2-1);%sqrt(dt)changed to dt.

 %   plot((wnStart:Nn),SecondOC(wnStart:Nn),'g')

 %   str=input('Look at plots');

    w(wnStart:Nn)=wMeanPrev+wMu0dt(wnStart:Nn)+  ...
        SecondOC(wnStart:Nn) + ...
        sign(w(wnStart:Nn)-wMeanPrev+dw(wnStart:Nn)).* ...
        sqrt(abs(sign(w(wnStart:Nn)-wMeanPrev).*(w(wnStart:Nn)-wMeanPrev).^2+ ...
        sign(dw(wnStart:Nn)).*dw2(wnStart:Nn)));

%Calculation of dt-integral starts
D1wl=(11/6*w(NnMidl-2)-3*w(NnMidl-3)+3/2*w(NnMidl-4)-1/3*w(NnMidl-5))/dNn;
    D2wl=(35/12*w(NnMidl-2)	-26/3*w(NnMidl-3)+	19/2*w(NnMidl-4)-14/3*w(NnMidl-5)+11/12*w(NnMidl-6))/dNn.^2;
    DeltaD1w=(w(NnMidh+2)-w(NnMidl-2)-5*D1wl*dNn-5.0*D2wl*dNn.^2.0/1.0)/12.50/dNn;

    wll(NnMidl-1)=w(NnMidl-2)+(.5*(D1wl+D2wl*dNn/1)+.5*(D1wl+D2wl*dNn/1+DeltaD1w))*dNn;
    wll(NnMidl)=wll(NnMidl-1)+(.5*(D1wl+D2wl*dNn/1+1.0*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+2.0*DeltaD1w))*dNn;
    wll(NnMidh)=wll(NnMidl)+(.5*(D1wl+D2wl*dNn/1+2.0*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+3.0*DeltaD1w))*dNn;
    wll(NnMidh+1)=wll(NnMidh)+(.5*(D1wl+D2wl*dNn/1+3.0*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+4.0*DeltaD1w))*dNn;

%
    D1wh=(-11/6*w(NnMidh+2)+3*w(NnMidh+3)-3/2*w(NnMidh+4)+1/3*w(NnMidh+5))/dNn;
    D2wh=(35/12*w(NnMidh+2)	-26/3*w(NnMidh+3)+	19/2*w(NnMidh+4)-14/3*w(NnMidh+5)+11/12*w(NnMidh+6))/dNn.^2;
    DeltaD1w=(w(NnMidh+2)-w(NnMidl-2)-5*D1wh*dNn-5.0*D2wh*dNn.^2.0/1.0)/12.50/dNn;
%

    whh(NnMidh+1)=w(NnMidh+2)-(.5*(D1wh+D2wh*dNn/1)+.5*(D1wh+D2wh*dNn/1+DeltaD1w))*dNn;
    whh(NnMidh)=whh(NnMidh+1)-(.5*(D1wh+D2wh*dNn/1+1*DeltaD1w)+.5*(D1wh+D2wh*dNn/1+2.0*DeltaD1w))*dNn;
    whh(NnMidl)=whh(NnMidh)-(.5*(D1wh+D2wh*dNn/1+2.0*DeltaD1w)+.5*(D1wh+D2wh*dNn/1+3.0*DeltaD1w))*dNn;
    whh(NnMidl-1)=whh(NnMidl)-(.5*(D1wh+D2wh*dNn/1+3.0*DeltaD1w)+.5*(D1wh+D2wh*dNn/1+4.0*DeltaD1w))*dNn;

    w(NnMidh+1)=.5*whh(NnMidh+1)+.5*wll(NnMidh+1);
    w(NnMidh)=.5*whh(NnMidh)+.5*wll(NnMidh);
    w(NnMidl)=.5*whh(NnMidl)+.5*wll(NnMidl);
    w(NnMidl-1)=.5*whh(NnMidl-1)+.5*wll(NnMidl-1);

        w1(1:Nn-1)=w(1:Nn-1);
        w2(1:Nn-1)=w(2:Nn);
        w(w1(:)>w2(:))=0;%Be careful;might not universally hold;

        w(w<0)=0.0;
        for nn=1:Nn
            if(w(nn)<=0)
                wnStart=nn+1;
           end
       end
end

 y_w(1:Nn)=0;
 y_w(wnStart:Nn) = ((1-gamma)*w(wnStart:Nn)).^(1/(1-gamma));
 Dfy_w(wnStart:Nn)=0;
 Dfw(wnStart:Nn)=0;
for nn=wnStart+1:Nn-1
    Dfy_w(nn) = (y_w(nn + 1) - y_w(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    Dfw(nn) = (w(nn + 1) - w(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    %Change of variable derivative for densities
end
fy_w(1:Nn)=0;
fw(1:Nn)=0;
for nn = wnStart:Nn-1
    fy_w(nn) = (normpdf(Z(nn),0, 1))/abs(Dfy_w(nn));%Origianl coordinates density
    fw(nn) = (normpdf(Z(nn),0, 1))/abs(Dfw(nn));
end

toc
str=input('Analytic Values calculated; Press a key to start monte carlo');

sigma11(1:OrderA+1)=0;
mu11(1:OrderA+1)=0;
mu22(1:OrderA+1)=0;
sigma22(1:OrderA+1)=0;
% index 1 correponds to zero level since matlab indexing starts at one.
sigma11(1)=1;
mu11(1)=1;
mu22(1)=1;
sigma22(1)=1;

for k=1:(OrderA+1)
    if sigma0~=0
        sigma11(k)=sigma0^(k-1);
    end
    if mu1 ~= 0
        mu11(k)=mu1^(k-1);
    end
    if mu2 ~= 0
        mu22(k)=mu2^(k-1);
    end
    if sigma0~=0
        sigma22(k)=sigma0^(2*(k-1));
    end
end
Ft(1:TtM+1,1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0; %General time powers on hermite polynomials
Fp(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers on coefficients of hermite polynomials.
Fp1(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers for bessel transformed coordinates.
%Pre-compute the time and power exponent values in small multi-dimensional arrays
for k = 0 : (OrderA+1)
    for m = 0:k
        l4 = k - m + 1;
        for n = 0 : m
            l3 = m - n + 1;
            for j = 0:n
                l2 = n - j + 1;
                l1 = j + 1;
                Ft(l1,l2,l3,l4) = dtM^((l1-1) + (l2-1) + (l3-1) + .5* (l4-1));
                Fp(l1,l2,l3,l4) = (alpha + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
                Fp1(l1,l2,l3,l4) = (alpha1 + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));

            end
        end
    end
end
%Below call the program that calculates the Ito-Taylor coeffs.
YCoeff = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma);
Yq=ItoTaylorCoeffsNew(alpha1,beta1,beta2,gamma);
YqCoeff=Yq/(1-gamma);%These coordinates are divided by (1-gamma)
 %Calculate the density with monte carlo below.
 rng(85109634, 'twister')
 paths=200000;
 YY(1:paths)=x0;  %Original process monte carlo.
 YY2dt(1:paths)=0.0;
 %YY4dt(1:paths)=0.0;
 X(1:paths)=x0^(1-gamma)/(1-gamma);
 Random1(1:paths)=0;
 for tt=1:TtM
     t1=tt*dtM;
     t0=(tt-1)*dtM;
     Random1=randn(size(Random1));
     HermiteP1(1,1:paths)=1;
     HermiteP1(2,1:paths)=Random1(1:paths);
     HermiteP1(3,1:paths)=Random1(1:paths).^2-1;
     YY0=YY;
     YYPrev=YY;
     XX0=X;

     for k = 0 : OrderM
         for m = 0:k
             l4 = k - m + 1;
             for n = 0 : m
                 l3 = m - n + 1;
                 for j = 0:n
                     l2 = n - j + 1;
                     l1 = j + 1;
                     if(l4<=5)

                      X(1:paths)=X(1:paths) + YqCoeff(l1,l2,l3,l4) * ...
                     mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                     ((1-gamma)*XX0(1:paths)).^(Fp1(l1,l2,l3,l4)/(1-gamma)) .* ...
                     HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);

                     YY(1:paths)=YY(1:paths) + YCoeff(l1,l2,l3,l4) * ...
                     mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                     YY0(1:paths).^Fp(l1,l2,l3,l4) .* HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);
                 %Above is original coordinates monte carlo equation.
                     end
                 end
             end
         end
     end
 end
 YY(YY<0)=0;
 X(X<0)=0;

 sum(YY(:))/paths %origianl coordinates monte carlo average.
 sum(y_w(wnStart+1:Nn-1).*ZProb(wnStart+1:Nn-1)) %Original process average from coordinates
 theta+(x0-theta)*exp(-kappa*dt*Tt)%Mean reverting SDE original variable true average

 BinSize=.0075/4;%Please change this bin size accordingly. When data range is too small decrease it.
 %When density range is too large increase it.Roughly, When starting point of SDE is
 %1, set at .0075*2; when starting point is x0=.1, set at .0075/4.0;
 MaxCutOff=30;
 [YDensity,IndexOutY,IndexMaxY] = MakeDensityFromSimulation_Infiniti(YY,paths,BinSize,MaxCutOff);
 plot(y_w(wnStart+1:Nn-1),fy_w(wnStart+1:Nn-1),'r',IndexOutY(1:IndexMaxY),YDensity(1:IndexMaxY),'g');
 str=input('red line is density of SDE from orthogonal incrments method, green is monte carlo.');

end
```

Dependencies of the code have already been uploaded in previous posts on this thread.

---

### #798 — Amin (Topic Author)
*August 28, 2019, 6:09 PM*

Post Deleted.

---

### #799 — Amin (Topic Author)
*August 29, 2019, 5:21 AM*

In my previous post I talked about the second term of taylor expansion of the existing distribution variable. The total
Taylor expansion approximately would go as

$X_0+\frac{\partial X}{\partial Z} H_1(Z)+ .5 \frac{{\partial}^2 X}{{\partial Z}^2} H_2(Z) +\frac{1}{6} \frac{{\partial}^3 X}{{\partial Z}^3} H_3(Z)+ H.O.T $

I believe the solution term we calculated in previous post is only an approximate proxy for
$\frac{{\partial}^2 X}{{\partial Z}^2}$ that takes into account one step evolution of the distribution variable and
works well only because of the high relative linearity of the Lamperti transformed variable. And the These calculations
would not be so straightforward for non-transformed SDE variables. I am sure once there is more research and there is a
better understanding of these phenomenon, we would be evolving difficult SDEs without taking their Lamperti transform.

The first term in above taylor expansion is linear variance that I have calculated by adding increments in a squared
fashion and multiplies with Z which is the first hermite polynomial. Friends would have noticed that I did not add the
second term of the Taylor expansion in a squared fashion to first term and added it separately to first term because it
is a different distinct term in Taylor expansion. Obviously higher order terms, if somewhere needed, would have to be
added separately and not in a squared fashion to previous terms. So linear variance and higher order variance is not to
be mixed up.

---

### #800 — Amin (Topic Author)
*August 31, 2019, 3:47 PM*

I am posting a new and improved version of the program. I have changed the methodology for dealing with second
derivative altogether and the results are extremely good. My program posted in previous post was just alright and had
some problems since long term after six or seven years became very poor and there were also suboptimalities in between
for smaller maturities. This program is simply excellent and I have tried it for ten years in the code I am posting with
superb results. It is a great improvement after I made changes to my methodology. Here is the code. I will explain the
changes and new methodology further with equations in next post in just a few hours. For ten years, for example the
difference in mean of the density in the code posted is just three basis points with quite high volatility and mean
reversion. Please enjoy the new program.

```
function [] = ItoTaylorDensityMRRecombining14F4Wilmott()
%Copyright Ahsan Amin. Infiniti derivatives Technologies.
%Please fell free to connect on linkedin: linkedin.com/in/ahsan-amin-0a53334
%or skype ahsan.amin2999
%In this program, I am simulating the SDE given as
%dy(t)=mu1 x(t)^beta1 dt + mu2 x(t)^beta2 dt +sigma x(t)^gamma dz(t)
%where mu1=kappa*theta and mu2=-kappa with
%beta1=0 and beta2=1;
%I have not directly simulated the SDE but simulated the transformed
%Bessel process version of the SDE and then changed coordinates to retreive
%the SDE in original coordinates.
%The present program will analytically evolve only the Bessel Process version of the
%SDE in transformed coordinates.
%The present program is meant for mean-reversion SDEs that take two terms
%in non-linear drift. It will work for simpler SDEs but for that you will
%have to turn SecondOC variable, second order correction variable to zero.
%
%For diffusions going into zero, you may see instabilities, I have not
%corrected for that yet in this initial version.
%Heston is still not good as substantial density goes into zero at
%practically realistic vol.
%Heston when density does not hit zero will work perfectly.
%I try volatility power/gamma above .65 0r .70
%gamma=.95 is proxy for lognormal, the best and coveted SV model but
%not used due to lack of tractibility.
%HEston and even smaller gamma will work far better when
%x0=1 and theta=1 as in Interest rate LMM like models with local volatility.
%Very close to zero, heston does not work very well. Whenever substantial
%density goes into zero, model performance deteriorates.
dt=.125/32;   % Simulation time interval.%For diffusions close to zero
             %decrease dt for accuracy.
Tt=32*80;     % Number of simulation levels. Terminal time= Tt*dt; //.125/32*32*16=2 year;
OrderA=2;  %Keep at two.
OrderM=2;  %Keep at two.
dtM=.125/4;%Monte carlo time interval size dtM.
TtM=4*80;%Monte carlo number of simulation intervals.

dNn=.2/1;   % Normal density subdivisions width. would change with number of subdivisions
Nn=46;  % No of normal density subdivisions
NnMidl=23;%One half left from mid of normal density(low)
NnMidh=24;%One half right from the mid of normal density(high)
NnMid=4.0;

x0=.25;   % starting value of SDE
beta1=0.0;   % the first drift term power.
beta2=1.0;   % Second drift term power.
gamma=.95;   % volatility power.
kappa=.90;   %mean reversion parameter.
theta=.10;   %mean reversion target

mu1=1*theta*kappa;   %first drift coefficient.
mu2=-1*kappa;    % Second drift coefficient.
sigma0=.80;%Volatility value
alpha=1;% x^alpha is being expanded. This is currently for monte carlo only.
alpha1=1-gamma;
y(1:Nn)=x0;
w(1:Nn)=x0^(1-gamma)/(1-gamma);
Z(1:Nn)=(((1:Nn)-3.5)*dNn-NnMid);
H4(1:Nn)=Z(1:Nn).^4-6*Z(1:Nn)+3;

ZProb(1)=normcdf(.5*Z(1)+.5*Z(2),0,1)-normcdf(.5*Z(1)+.5*Z(2)-dNn,0,1);
ZProb(Nn)=normcdf(.5*Z(Nn)+.5*Z(Nn-1)+dNn,0,1)-normcdf(.5*Z(Nn)+.5*Z(Nn-1),0,1);

for nn=2:Nn-1
    ZProb(nn)=normcdf(.5*Z(nn)+.5*Z(nn+1),0,1)-normcdf(.5*Z(nn)+.5*Z(nn-1),0,1);
    %Above calculate probability mass in each probability subdivision.
end

 dt2=dt^2/2;
 dt3=dt^3/6.0;
 dtsqrt=sqrt(dt);
 dtonehalf=dt.^1.5;

wnStart=1;
SecondOC(1:Nn)=0;
SecondD(1:Nn)=0.0;
tic

for tt=1:Tt

    yy(wnStart:Nn)=((1-gamma)*w(wnStart:Nn)).^(1/(1-gamma));

    theta1=mu1;
    theta2=mu2;
    theta3=.5*sigma0^2*(-gamma);
    omega1=beta1-gamma;
    omega2=beta2-gamma;
    omega3=gamma-1;

    GG(wnStart:Nn)=theta1*yy(wnStart:Nn).^omega1+theta2*yy(wnStart:Nn).^omega2+theta3*yy(wnStart:Nn).^omega3;
    dGG(wnStart:Nn)=omega1*theta1*yy(wnStart:Nn).^(omega1-1)+omega2*theta2*yy(wnStart:Nn).^(omega2-1)+ ...
        omega3*theta3*yy(wnStart:Nn).^(omega3-1);
    DD(wnStart:Nn)=mu1*yy(wnStart:Nn).^beta1+mu2*yy(wnStart:Nn).^beta2;
    dGG2(wnStart:Nn)=theta1*omega1*(omega1-1).*yy(wnStart:Nn).^(omega1-2)+ ...
        theta2*omega2*(omega2-1).*yy(wnStart:Nn).^(omega2-2)+ ...
        theta3*omega3*(omega3-1).*yy(wnStart:Nn).^(omega3-2);
    QQ(wnStart:Nn)=sigma0^2*yy(wnStart:Nn).^(2*gamma);
    ddGGDD(wnStart:Nn)=mu1*omega1*theta1*(omega1+beta1-1).*yy(wnStart:Nn).^(omega1+beta1-2)+ ...
        mu1*omega2*theta2*(omega2+beta1-1).*yy(wnStart:Nn).^(omega2+beta1-2)+ ...
        mu1*omega3*theta3*(omega3+beta1-1).*yy(wnStart:Nn).^(omega3+beta1-2)+ ...
        mu2*omega1*theta1*(omega1+beta2-1).*yy(wnStart:Nn).^(omega1+beta2-2)+ ...
        mu2*omega2*theta2*(omega2+beta2-1).*yy(wnStart:Nn).^(omega2+beta2-2)+ ...
        mu2*omega3*theta3*(omega3+beta2-1).*yy(wnStart:Nn).^(omega3+beta2-2);
    d2dGGDD(wnStart:Nn)=mu1*omega1*theta1*(omega1+beta1-1).*(omega1+beta1-2).*yy(wnStart:Nn).^(omega1+beta1-3)+ ...
        mu1*omega2*theta2*(omega2+beta1-1).*(omega2+beta1-2).*yy(wnStart:Nn).^(omega2+beta1-3)+ ...
        mu1*omega3*theta3*(omega3+beta1-1).*(omega3+beta1-2).*yy(wnStart:Nn).^(omega3+beta1-3)+ ...
        mu2*omega1*theta1*(omega1+beta2-1).*(omega1+beta2-2).*yy(wnStart:Nn).^(omega1+beta2-3)+ ...
        mu2*omega2*theta2*(omega2+beta2-1).*(omega2+beta2-2).*yy(wnStart:Nn).^(omega2+beta2-3)+ ...
        mu2*omega3*theta3*(omega3+beta2-1).*(omega3+beta2-2).*yy(wnStart:Nn).^(omega3+beta2-3);
    ddGG2QQ(wnStart:Nn)=theta1*sigma0^2.*omega1*(omega1-1).*(omega1+2*gamma-2).*yy(wnStart:Nn).^(omega1+2*gamma-3)+ ...
        sigma0^2*theta2*omega2*(omega2-1).*(omega2+2*gamma-2).*yy(wnStart:Nn).^(omega2+2*gamma-3)+ ...
        sigma0^2*theta3*omega3*(omega3-1).*(omega3+2*gamma-2).*yy(wnStart:Nn).^(omega3+2*gamma-3);
   
d2dGG2QQ(wnStart:Nn)=theta1*sigma0^2.*omega1*(omega1-1).*(omega1+2*gamma-2).*(omega1+2*gamma-3).*yy(wnStart:Nn).^(omega1+2*gamma-4)+
...
        sigma0^2*theta2*omega2*(omega2-1).*(omega2+2*gamma-2).*(omega2+2*gamma-3).*yy(wnStart:Nn).^(omega2+2*gamma-4)+
...
        sigma0^2*theta3*omega3*(omega3-1).*(omega3+2*gamma-2).*(omega3+2*gamma-3).*yy(wnStart:Nn).^(omega3+2*gamma-4);

    VV(wnStart:Nn)=sigma0.*yy(wnStart:Nn).^gamma;
    d_dGG_VV_dyy(wnStart:Nn)= ...
        sigma0.*omega1.*theta1.*(omega1+gamma-1).*yy(wnStart:Nn).^(omega1+gamma-2) + ...
        sigma0.*omega2.*theta2.*(omega2+gamma-1).*yy(wnStart:Nn).^(omega2+gamma-2) + ...
        sigma0.*omega3.*theta3.*(omega3+gamma-1).*yy(wnStart:Nn).^(omega3+gamma-2);

    wMu0dt(wnStart:Nn)=GG(wnStart:Nn)*dt + dGG(wnStart:Nn).*DD(wnStart:Nn).*dt2 + ...
        .5*dGG2(wnStart:Nn).*QQ(wnStart:Nn).*dt2 + ...
        ddGGDD(wnStart:Nn).*DD(wnStart:Nn).*dt3 + ...
        .5*ddGG2QQ(wnStart:Nn).*DD(wnStart:Nn).*dt3 + ...
        .5*d2dGGDD(wnStart:Nn).*QQ(wnStart:Nn).*dt3 + ...
        .25*d2dGG2QQ(wnStart:Nn).*QQ(wnStart:Nn).*dt3;
%    c0(wnStart:Nn)=-1*d_dGG_VV_dyy(wnStart:Nn).*VV(wnStart:Nn).*(1/sqrt(2.0).*(1-sqrt(2.0)/2.0)).*dt.^2.0;
    c1(wnStart:Nn)=sigma0.*dtsqrt+dGG(wnStart:Nn).*VV(wnStart:Nn).*(1-1/sqrt(3.0)).*dtonehalf ;
    c2(wnStart:Nn)=d_dGG_VV_dyy(wnStart:Nn).*VV(wnStart:Nn).*(1/sqrt(2.0).*(1-sqrt(2.0)/2.0)).*dt.^2.0;
%    dw0(wnStart:Nn)=(sigma0.*Z(wnStart:Nn).^1.*dtsqrt+ ...
%        dGG(wnStart:Nn).*VV(wnStart:Nn).*(1-1/sqrt(3.0)).*Z(wnStart:Nn).^1.*dtonehalf + ... %;%+ ...
%        1*d_dGG_VV_dyy(wnStart:Nn).*VV(wnStart:Nn).*(1/sqrt(2.0).*(1-sqrt(2.0)/2.0)).*dt.^2.0.*(Z(wnStart:Nn).^2-1));
    dw(wnStart:Nn)=c1(wnStart:Nn).*Z(wnStart:Nn);% + ...
    d2w(wnStart:Nn)=c2(wnStart:Nn).*(Z(wnStart:Nn).^2-1);
   dw2(wnStart:Nn)=c1(wnStart:Nn).^2.0.*Z(wnStart:Nn).^2;% + ...
   d2w2(wnStart:Nn)= c2(wnStart:Nn).^2.*(Z(wnStart:Nn).^4-2*Z(wnStart:Nn).^2+1);

    w(isnan(w)==1)=0;

    wMu0dt(isnan(wMu0dt)==1)=0;

    wMeanPrev=sum(ZProb(wnStart:Nn).*w(wnStart:Nn));%Calculate the mean.
    w2MeanPrev=sum(ZProb(wnStart:Nn).*(w(wnStart:Nn)-wMeanPrev).^2);
    w(wnStart:Nn)=wMeanPrev+wMu0dt(wnStart:Nn)-  ...
        1/sqrt(2*pi)*.5*(sign((w(wnStart:Nn)-wMeanPrev).^2-w2MeanPrev+d2w(wnStart:Nn))).*...
        sqrt(abs(sign((w(wnStart:Nn)-wMeanPrev).^2-w2MeanPrev).*((w(wnStart:Nn)-wMeanPrev).^2-w2MeanPrev).^2+ ...
        sign(d2w(wnStart:Nn)).*d2w2(wnStart:Nn))).*sigma0^2*dt/2+ ...
        sign(w(wnStart:Nn)-wMeanPrev+dw(wnStart:Nn)).* ...
        sqrt(abs(sign(w(wnStart:Nn)-wMeanPrev).*(w(wnStart:Nn)-wMeanPrev).^2+ ...
        sign(dw(wnStart:Nn)).*dw2(wnStart:Nn)));

%Calculation of dt-integral starts
D1wl=(11/6*w(NnMidl-2)-3*w(NnMidl-3)+3/2*w(NnMidl-4)-1/3*w(NnMidl-5))/dNn;
    D2wl=(35/12*w(NnMidl-2) -26/3*w(NnMidl-3)+ 19/2*w(NnMidl-4)-14/3*w(NnMidl-5)+11/12*w(NnMidl-6))/dNn.^2;
    DeltaD1w=(w(NnMidh+2)-w(NnMidl-2)-5*D1wl*dNn-5.0*D2wl*dNn.^2.0/1.0)/12.50/dNn;

    wll(NnMidl-1)=w(NnMidl-2)+(.5*(D1wl+D2wl*dNn/1)+.5*(D1wl+D2wl*dNn/1+DeltaD1w))*dNn;
    wll(NnMidl)=wll(NnMidl-1)+(.5*(D1wl+D2wl*dNn/1+1.0*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+2.0*DeltaD1w))*dNn;
    wll(NnMidh)=wll(NnMidl)+(.5*(D1wl+D2wl*dNn/1+2.0*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+3.0*DeltaD1w))*dNn;
    wll(NnMidh+1)=wll(NnMidh)+(.5*(D1wl+D2wl*dNn/1+3.0*DeltaD1w)+.5*(D1wl+D2wl*dNn/1+4.0*DeltaD1w))*dNn;

%
    D1wh=(-11/6*w(NnMidh+2)+3*w(NnMidh+3)-3/2*w(NnMidh+4)+1/3*w(NnMidh+5))/dNn;
    D2wh=(35/12*w(NnMidh+2) -26/3*w(NnMidh+3)+ 19/2*w(NnMidh+4)-14/3*w(NnMidh+5)+11/12*w(NnMidh+6))/dNn.^2;
    DeltaD1w=(w(NnMidh+2)-w(NnMidl-2)-5*D1wh*dNn-5.0*D2wh*dNn.^2.0/1.0)/12.50/dNn;
%

    whh(NnMidh+1)=w(NnMidh+2)-(.5*(D1wh+D2wh*dNn/1)+.5*(D1wh+D2wh*dNn/1+DeltaD1w))*dNn;
    whh(NnMidh)=whh(NnMidh+1)-(.5*(D1wh+D2wh*dNn/1+1*DeltaD1w)+.5*(D1wh+D2wh*dNn/1+2.0*DeltaD1w))*dNn;
    whh(NnMidl)=whh(NnMidh)-(.5*(D1wh+D2wh*dNn/1+2.0*DeltaD1w)+.5*(D1wh+D2wh*dNn/1+3.0*DeltaD1w))*dNn;
    whh(NnMidl-1)=whh(NnMidl)-(.5*(D1wh+D2wh*dNn/1+3.0*DeltaD1w)+.5*(D1wh+D2wh*dNn/1+4.0*DeltaD1w))*dNn;

    w(NnMidh+1)=.5*whh(NnMidh+1)+.5*wll(NnMidh+1);
    w(NnMidh)=.5*whh(NnMidh)+.5*wll(NnMidh);
    w(NnMidl)=.5*whh(NnMidl)+.5*wll(NnMidl);
    w(NnMidl-1)=.5*whh(NnMidl-1)+.5*wll(NnMidl-1);

        w1(1:Nn-1)=w(1:Nn-1);
        w2(1:Nn-1)=w(2:Nn);
        w(w1(:)>w2(:))=0;%Be careful;might not universally hold;

        w(w<0)=0.0;
        for nn=1:Nn
            if(w(nn)<=0)
                wnStart=nn+1;
           end
       end
end

 y_w(1:Nn)=0;
 y_w(wnStart:Nn) = ((1-gamma)*w(wnStart:Nn)).^(1/(1-gamma));
 Dfy_w(wnStart:Nn)=0;
 Dfw(wnStart:Nn)=0;
for nn=wnStart+1:Nn-1
    Dfy_w(nn) = (y_w(nn + 1) - y_w(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    Dfw(nn) = (w(nn + 1) - w(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    %Change of variable derivative for densities
end
fy_w(1:Nn)=0;
fw(1:Nn)=0;
for nn = wnStart:Nn-1
    fy_w(nn) = (normpdf(Z(nn),0, 1))/abs(Dfy_w(nn));%Origianl coordinates density
    fw(nn) = (normpdf(Z(nn),0, 1))/abs(Dfw(nn));
end

toc
str=input('Analytic Values calculated; Press a key to start monte carlo');

sigma11(1:OrderA+1)=0;
mu11(1:OrderA+1)=0;
mu22(1:OrderA+1)=0;
sigma22(1:OrderA+1)=0;
% index 1 correponds to zero level since matlab indexing starts at one.
sigma11(1)=1;
mu11(1)=1;
mu22(1)=1;
sigma22(1)=1;

for k=1:(OrderA+1)
    if sigma0~=0
        sigma11(k)=sigma0^(k-1);
    end
    if mu1 ~= 0
        mu11(k)=mu1^(k-1);
    end
    if mu2 ~= 0
        mu22(k)=mu2^(k-1);
    end
    if sigma0~=0
        sigma22(k)=sigma0^(2*(k-1));
    end
end
Ft(1:TtM+1,1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0; %General time powers on hermite polynomials
Fp(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers on coefficients of hermite polynomials.
Fp1(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers for bessel transformed coordinates.
%Pre-compute the time and power exponent values in small multi-dimensional arrays
for k = 0 : (OrderA+1)
    for m = 0:k
        l4 = k - m + 1;
        for n = 0 : m
            l3 = m - n + 1;
            for j = 0:n
                l2 = n - j + 1;
                l1 = j + 1;
                Ft(l1,l2,l3,l4) = dtM^((l1-1) + (l2-1) + (l3-1) + .5* (l4-1));
                Fp(l1,l2,l3,l4) = (alpha + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
                Fp1(l1,l2,l3,l4) = (alpha1 + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));

            end
        end
    end
end
%Below call the program that calculates the Ito-Taylor coeffs.
YCoeff = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma);
Yq=ItoTaylorCoeffsNew(alpha1,beta1,beta2,gamma);
YqCoeff=Yq/(1-gamma);%These coordinates are divided by (1-gamma)
 %Calculate the density with monte carlo below.
 rng(85109634, 'twister')
 paths=200000;
 YY(1:paths)=x0;  %Original process monte carlo.
 YY2dt(1:paths)=0.0;
 %YY4dt(1:paths)=0.0;
 X(1:paths)=x0^(1-gamma)/(1-gamma);
 Random1(1:paths)=0;
 for tt=1:TtM
     t1=tt*dtM;
     t0=(tt-1)*dtM;
     Random1=randn(size(Random1));
     HermiteP1(1,1:paths)=1;
     HermiteP1(2,1:paths)=Random1(1:paths);
     HermiteP1(3,1:paths)=Random1(1:paths).^2-1;
     YY0=YY;
     YYPrev=YY;
     XX0=X;

     for k = 0 : OrderM
         for m = 0:k
             l4 = k - m + 1;
             for n = 0 : m
                 l3 = m - n + 1;
                 for j = 0:n
                     l2 = n - j + 1;
                     l1 = j + 1;
                     if(l4<=5)

                      X(1:paths)=X(1:paths) + YqCoeff(l1,l2,l3,l4) * ...
                     mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                     ((1-gamma)*XX0(1:paths)).^(Fp1(l1,l2,l3,l4)/(1-gamma)) .* ...
                     HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);

                     YY(1:paths)=YY(1:paths) + YCoeff(l1,l2,l3,l4) * ...
                     mu11(l1)*mu22(l2)*sigma22(l3)*sigma11(l4)* ...
                     YY0(1:paths).^Fp(l1,l2,l3,l4) .* HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);
                 %Above is original coordinates monte carlo equation.
                     end
                 end
             end
         end
     end
 end
 YY(YY<0)=0;
 X(X<0)=0;

 sum(YY(:))/paths %origianl coordinates monte carlo average.
 sum(y_w(wnStart+1:Nn-1).*ZProb(wnStart+1:Nn-1)) %Original process average from coordinates
 theta+(x0-theta)*exp(-kappa*dt*Tt)%Mean reverting SDE original variable true average

 BinSize=.0075/4;%Please change this bin size accordingly. When data range is too small decrease it.
 %When density range is too large increase it.Roughly, When starting point of SDE is
 %1, set at .0075*2; when starting point is x0=.1, set at .0075/4.0;
 MaxCutOff=30;
 [YDensity,IndexOutY,IndexMaxY] = MakeDensityFromSimulation_Infiniti(YY,paths,BinSize,MaxCutOff);
 plot(y_w(wnStart+1:Nn-1),fy_w(wnStart+1:Nn-1),'r',IndexOutY(1:IndexMaxY),YDensity(1:IndexMaxY),'g');
 str=input('red line is density of SDE from orthogonal incrments method, green is monte carlo.');

end
```

The above program was tried for volatility exponents upwards of .65. It will not work for heston due to other technical
reasons in the program and I will fix them in a few days and assure friends that same "main algorithm" will work
perfectly fine for heston as well.

---

[← Previous](page_015.md) | [Index](index.md) | [Next →](page_017.md)
