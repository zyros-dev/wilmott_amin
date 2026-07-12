# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 12 of 59** — Posts #551–#600

[← Previous](page_011.md) | [Index](index.md) | [Next →](page_013.md)

---

### #551 — outrun
*May 26, 2017, 8:49 AM*

> I reckon it's an optimal flow algorithm to determine the largest daily flow the system will meet. And the associated
cost in delivery of the water supply.It could be a linear programming model.
>
> These kinds of models have greater applicability than just water slushing in pipes. Very useful stuff IMO.
Yes, dynamic programming.

It's like a large bucket where people take out water and which you have to fill to ensure it doesn't run empty.
The inflow rate schedule is the thing you optimize and the cost is typically non-constant. The cost could be
deterministic (e.g. you have a 3 year contract where the "office hour electricity prices" are always X and "nighttime
prices" are always Y) or dynamic/stochastic. Dynamic comes in two flavors: the price can be a stochastic spot price,
or you can have a forward market. If it's dynamic then you end up with option type of models.

The inflow rate you need to optimize also has an upperbound, and so does the bucket volume.

There storage models show up in various places. This was clean water production, but I've also build gas storage models
where companies would buy and store gas when the market prices are low, and extract and sell it when the prices are
high. A power plant that's used fuel to generate electricity is also very similar. All are almost the same thing!

---

### #552 — Cuchulainn
*May 26, 2017, 12:45 PM*

Thinking out loud: can we model the physical components (also save their historical behaviour) using some kind of
distribution (beta, triangle)? The network wil have spike no doubt but a lot will be mean-reverting?

---

### #553 — outrun
*May 26, 2017, 1:08 PM*

I didn't look at the network. They told me if the water buffer ever got empty then pressure would suddenly drop form 70
bar to 0. That would send a shockwave through the networks, possible breaking every pipe fitting underground. To fix it
they would have to open up *all* streets in the cities in their supply region.

My goal what to use more of the optionality the water buffer provided. E.g. let it *almost* run dry when production
costs (electricity prices) are high, fill it to the rim when electricity is very cheap.

With all the renewable energy getting on-line, electricity production becomes more stochastic, and that calls for energy
buffers to even out (temporal) mismatches between production and demand. So storage models are very popular nowadays.

---

### #554 — MaxwellSheffield
*June 16, 2017, 2:36 PM*

I am tired of these rubbish posts/tuto about how to build those C++/Excel Interface, never clear to me !  Sounds like
one of you is doing something about it, is it going to be a complete book that will cover all aspects ?When is it going
to be release ?  I cannot wait as I am tired of googling each of my issue, and never find what I want !  And yeah, not
the right the place..

---

### #555 — outrun
*June 16, 2017, 3:04 PM*

Buy propper books, Google for "good c+ books" and take time to learn. Or hire an expensive consultant. Or python.

Excel is for creating jobs and stability problems

---

### #556 — Amin (Topic Author)
*August 20, 2017, 7:36 AM*

I have definitively solved the simulation o stochastic differential equations using my method of Stochastic Calculus of
Standard Deviations(SCSD). I am getting high accuracy to a few basis points with extreme volatility out to 5-10 years.
The method is basically analogue of the method of iterated integrals that I used for solution of ordinary differential
equations adapted to stochastic differential equations. Might possibly post the programs in a week.

---

### #557 — tags
*August 20, 2017, 8:30 AM*

That googling "good c++ books justin london" returns anything finished to convince me that Google search is
untrustworthy.

---

### #558 — Amin (Topic Author)
*October 16, 2017, 2:30 PM*

Since this post in off-topic is relevant to this thread, I have copied it here for reference. Here is the link to the paper.[https://papers.ssrn.com/sol3/papers.cfm ... id=2872598](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598)

> I had a quick look at the SSRN article. It seems you did a lot of improvement compared to the initial try outs.
>
>
>
> in theory it is important that is works to crunch numbers as well as doing symbolic maths.
>
Daniel, I have given three mathematica code listings in the paper each for first Order Odes, nth order ODEs and Systems
of ODEs. Mathematica is used for different differentials and integrals that are messy to calculate by hand. You could
for example  change the mathematica line that specifies the ODEs and run the rest of the code as such. Again all you
need to do is to change the specification of ODE or system of ODEs and rest of the mathematica code will solve the
problem to give the right answer. Solution of ODEs that follow from the method is series solution of the closed form
answer.

Method of iterated integral that I have used for solution of ODEs has far larger applications. You can for example solve
non-linear transforms using this method. It could be used for the solution of SDEs and more. This method is a cousin of
Taylor series.

---

### #559 — Cuchulainn
*October 22, 2017, 9:52 AM*

Indeed, the second revision is more readable and structured, but there is some way to go (depending on what your
requirements are) as the article is more of a engineering/methods/recipe type article (nothing wrong with that) without
the mathematical foundations yet.

Some constructive remarks. To reduce the scope, I only examined first-order scalar IVP case:

1. The 'iterated integral trick' (your words) seems to have been plucked from thin air. In particular, I got stuck at
equations (3) and (4). The maths is informal. In practice it might be OK but it has to be proved in *theory*.

2. The compelling reason for iterated integral is not clear to me I examined equations (13) (BTW you can mention is$e^t$
) and (14)$tan( t)$ and I get *exactly* the same answers as Picard iteration using a **much simpler **single integral.

3. For (14) the series explodes at multiples of$t = \pi / 2$ On a follow-on, what is needed is a result stating the
interval in which a solution of the IVP exists and is nice and smooth (for a counterexample, take a ODE with a
discontinuous right hand side). BTW how to prove existence and uniqueness results is well known.

4. page 23: How do we 'use' the formula for $Y(t)$? For number crunching at least, just use an ODE solver.

5. Have you had a shot at the Riccati ODE which crops up here and there?

Some of these remarks have already been aired by @amike and myself.

---

### #560 — Amin (Topic Author)
*November 2, 2017, 1:48 PM*

Very constructive comments. Sorry for not being prompt to answer. Will get back in a day or two and try to answer most
of your points. Thanks again for constructive discussion.

---

### #561 — Cuchulainn
*November 2, 2017, 2:54 PM*

You're welcome, Mr. Amin.

---

### #562 — Amin (Topic Author)
*November 3, 2017, 3:33 PM*

Sorry again for coming back to you so late.

OK I explain equations 3-4 here that are the basics and foundation of of iterated integral.

For one variable, we can have the following equation which is very straightforward for one variable calculus.

$y(\tau)  =y(t_0) +\int_{t_0}^{\tau } \frac{\partial y(s)}{\partial s} \, ds$  Equation(1)

In the following two variable function, we apply the logic of above equation(1) to only the second variable and keep the
first variable exactly the same untouched.

$f(\tau , y(\tau))=f\left(\tau , y(t_0)\right)+\int_{t_0}^{\tau } \frac{\partial f(\tau , y(s))}{\partial s} \, ds$
Equation(2)

From the chain rule for partial derivatives, we have

$\frac{\partial f(\tau , y(s))}{\partial s}=\frac{\partial f(\tau ,y(s))}{\partial y}\frac{\partial y(s))}{\partial s}$
Equation (3)

Integrating both sides, we get

$\int_{t_0}^{\tau } \frac{\partial f(\tau , y(s))}{\partial s} \, ds=\int _{t_0}^{\tau }\frac{\partial f(\tau ,y(s))}{\partial s}\frac{\partial y(s))}{\partial s}ds$
Equation(4)

substituting Equation(4) in equation(2), we get

$f(\tau ,  y(\tau))=f\left(\tau , y(t_0)\right)+\int _{t_0}^{\tau }\frac{\partial f(\tau , y(s))}{\partial s}\frac{\partial y(s))}{\partial s}ds$
Equation(5)

However, we know from the original ODE

$\frac{\partial y(s))}{\partial s}=f(s,y(s))$ Equation(6)

We substitute Equation(6) in equation(5) to get

$f(\tau ,  y(\tau))=f\left(\tau ,y(t_0) \right)+\int _{t_0}^{\tau }\frac{\partial f(\tau , y(s))}{\partial s}f(s, y(s))ds$
Equation(7)

Above Equation(5) is equation(3) in my paper and Equation(7) is equation(4) in my paper. If something is unclear, please
let me know and I will try to explain. The iterated integral logic is repeated application of the above logic to higher
derivatives.

I will come back to other comments but please let me know if you understand the logic and if the above explanation is
good enough for that.

---

### #563 — Amin (Topic Author)
*November 10, 2017, 5:15 PM*

Here I explain the complete logic behind Iterated Integrals solution to ODEs a bit more in detail. In the next post, I
will extend the iterated Integrals logic for SDEs and monte carlo.

We are given a general first order ODE

$\frac{\text{dy}(t)}{\text{dt}}=f(t, y(t)),t\geq t_0,\ y(t_0)=y_0$   Equation(1)

$y(t)=y(t_0)+\int_{t_0}^t \frac{dy(\tau)}{d\tau} \, d\tau$   Equation(2)

Below is the formal solution of the ODE

$= y(t_0)+\int _{t_0}^t f(\tau, y(\tau))d\tau$    Equation(3)

For one variable, we can have the following equation which is very straightforward for one variable calculus.

$y(\tau)  =y(t_0) +\int_{t_0}^{\tau } \frac{d y(s)}{d s} \, ds$  Equation(4)

In the following two variable function, we apply the logic of above equation(4) to only the second variable and keep the
first variable exactly the same untouched. As we are finding change for only one of the variables, we switch to partial
derivatives in this equation.

$f(\tau , y(\tau))=f\left(\tau , y(t_0)\right)+\int_{t_0}^{\tau } \frac{\partial f(\tau , y(s))}{\partial s} \, ds$
Equation(5)

From the chain rule for partial derivatives, we have

$\frac{\partial f(\tau , y(s))}{\partial s}=\frac{\partial f(\tau ,y(s))}{\partial y}\frac{d y(s))}{d s}$ Equation (6)

Integrating both sides, we get

$\int_{t_0}^{\tau } \frac{\partial f(\tau , y(s))}{\partial s} \, ds=\int _{t_0}^{\tau }\frac{\partial f(\tau ,y(s))}{\partial y}\frac{d y(s))}{d s}ds$
Equation(7)

substituting Equation(7) in equation(5), we get

$f(\tau ,  y(\tau))=f\left(\tau , y(t_0)\right)+\int _{t_0}^{\tau }\frac{\partial f(\tau , y(s))}{\partial y}\frac{d y(s))}{d s}ds$
Equation(8)

However, we know from the original ODE

$\frac{d y(s))}{d s}=f(s,y(s))$ Equation(9)

We substitute Equation(9) in equation(8) to get

$f(\tau ,  y(\tau))=f\left(\tau ,y(t_0) \right)+\int _{t_0}^{\tau }\frac{\partial f(\tau , y(s))}{\partial y}f(s, y(s))ds$
Equation(10)

Integrating  the above equation (10) on both sides to match the equation(3), we get first order solution to our ODE

$y(t_0)+\int _{t_0}^t f(\tau, y(\tau))d\tau$

$=y(t_0)+\int _{t_0}^t f(\tau, y(t_0))d\tau+\int_{t_0}^t \int_{t_0}^{\tau } \frac{\partial f(\tau , y(s))}{\partial y}f(s, y(s))ds d\tau$
Equation(11)

Similarly taking the expansion to next order applying the same logic again yields the new higher order solution equation

$=y(t_0)+\int _{t_0}^t f(\tau, y(t_0))d\tau+\int_{t_0}^t \int_{t_0}^{\tau } \frac{\partial f(\tau , y(t_0))}{\partial y}f(s, y(t_0))ds d\tau$

$+\left.\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial f(\tau , y(v))}{\partial y}f(s, y(v)\right.\right]f(v, y(v))dvdsd\tau$
Equation(12)

In the next post, I will extend the logic of iterated integrals to monte carlo simulation of the SDEs so that highly
non-linear stochastic differential equations could be tackled easily by higher order monte carlo with larger monte carlo
step size.

---

### #564 — Amin (Topic Author)
*November 23, 2017, 10:48 AM*

Suppose we want to solve the following general SDE

$\text{dX} (\tau) = \mu  (X(\tau)) \text{d}\tau+ \sigma(X(\tau))  \text{dz}( \tau)  $  Equation(1)

The formal solution of the above SDE is given as

$X(t)=X(t_0)+\int_{t_0}^t \mu (X(\tau)) \, d\tau+\int _{t_0}^t\sigma(X(\tau))  dz(\tau )$  Equation(2)

We want to solve both integrand terms in above equation as

$ \mu (X(\tau))=\mu (X(t_0))+\int_{t_0}^\tau d\mu (X(s))$   Equation(3)

and

$ \sigma (X(\tau))=\sigma (X(t_0))+\int_{t_0}^\tau d\sigma (X(s))$  Equation(4)

When we substitute above equation(3) and equation(4) in equation(2), we get

$X(t)=X(t_0)+\int_{t_0}^t \mu (X(t_0)) \, d\tau+\int_{t_0}^t \int_{t_0}^\tau d\mu (X(s)) d\tau $

$+\int _{t_0}^t\sigma(X(t_0))  dz(\tau )+\int _{t_0}^t \int_{t_0}^\tau d\sigma (X(s)) dz(\tau )$  Equation(5)

From Ito expansion of $d\mu (X(s)) $ and $d\sigma (X(s)) $, we know that

$d\mu  (X(s))=\frac{\partial }{\partial X}[\mu ( X(s))]\mu (X(s)) \text{ds}+\frac{\partial }{\partial X}[\mu  (X(s))]\sigma (X(s)) \text{dz(s)}$

$+0.5 \frac{\partial ^2[\mu  ( X(s))]}{\partial X^2} \sigma ( X(s))^2\text{ds}$ Equation(6)

and

$d\sigma ( X(s))=\frac{\partial }{\partial X}[\sigma ( X(s))]\mu (X(s)) \text{ds}+\frac{\partial }{\partial X}[\sigma  (X(s))]\sigma (X(s)) \text{dz(s)}$

$+0.5 \frac{\partial ^2[\sigma  ( X(s))]}{\partial X^2} \sigma ( X(s))^2\text{ds}$  Equation(7)

We substitute equation (6) and Equation(7) in equation(5)

$X(t)=X(t_0)+\int_{t_0}^t \mu (X(t_0)) \, d\tau$

$+\int_{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\mu ( X(s))]\mu (X(s)) \text{ds} d\tau+\int_{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\mu  (X(s))]\sigma (X(s)) \text{dz(s)} d\tau$

$+\int_{t_0}^t \int_{t_0}^\tau 0.5 \frac{\partial ^2[\mu ( X(s))]}{\partial X^2} \sigma ( X(s))^2\text{ds} d\tau$

$+\int _{t_0}^t\sigma(X(t_0))  dz(\tau )$

$+\int _{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\sigma ( X(s))]\mu (X(s)) \text{ds} dz(\tau )$

$+\int _{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\sigma ( X(s))]\sigma (X(s)) dz(s ) dz(\tau )$

$+\int_{t_0}^t \int_{t_0}^\tau 0.5 \frac{\partial ^2[\sigma ( X(s))]}{\partial X^2} \sigma ( X(s))^2\text{ds} dz(\tau )$
Equation(8)

In a further order expansion, we evaluate terms at time 's' at$t_0$ and add a third order integral. I am not showing the
third order integral but up to second order, we will have

$X(t)=X(t_0)+\int_{t_0}^t \mu (X(t_0)) \, d\tau$

$+\int_{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\mu ( X(t_0))]\mu (X(t_0)) \text{ds} d\tau+\int_{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\mu  (X(t_0))]\sigma (X(t_0)) \text{dz(s)} d\tau$

$+\int_{t_0}^t \int_{t_0}^\tau 0.5 \frac{\partial ^2[\mu ( X(t_0))]}{\partial X^2} \sigma ( X(t_0))^2\text{ds} d\tau$

$+\int _{t_0}^t\sigma(X(t_0))  dz(\tau )$

$+\int _{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\sigma ( X(t_0))]\mu (X(t_0)) \text{ds} dz(\tau )$

$+\int _{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\sigma ( X(t_0))]\sigma (X(t_0)) dz(s ) dz(\tau )$

$+\int_{t_0}^t \int_{t_0}^\tau 0.5 \frac{\partial ^2[\sigma ( X(t_0))]}{\partial X^2} \sigma ( X(t_0))^2\text{ds} dz(\tau )$
Equation(9)

Since all the terms are evaluated at $t_0$, they are constants and we can write the above integrals as

$X(t)=X(t_0)+\mu (X(t_0)) \int_{t_0}^t   d\tau$

$+\frac{\partial }{\partial X}[\mu ( X(t_0))]\mu (X(t_0)) \int_{t_0}^t \int_{t_0}^\tau  \text{ds} d\tau$

$+ \frac{\partial }{\partial X}[\mu  (X(t_0))]\sigma (X(t_0)) \int_{t_0}^t \int_{t_0}^\tau \text{dz(s)} d\tau$

$+0.5 \frac{\partial ^2[\mu ( X(t_0))]}{\partial X^2} \sigma ( X(t_0))^2 \int_{t_0}^t \int_{t_0}^\tau \text{ds} d\tau$

$+\sigma(X(t_0))  \int _{t_0}^t dz(\tau )$

$+\frac{\partial }{\partial X}[\sigma ( X(t_0))]\mu (X(t_0)) \int _{t_0}^t \int_{t_0}^\tau  \text{ds} dz(\tau )$

$+\frac{\partial }{\partial X}[\sigma ( X(t_0))]\sigma (X(t_0))\int _{t_0}^t \int_{t_0}^\tau  dz(s ) dz(\tau )$

$+0.5 \frac{\partial ^2[\sigma ( X(t_0))]}{\partial X^2} \sigma ( X(t_0))^2\int_{t_0}^t \int_{t_0}^\tau  \text{ds} dz(\tau )$
Equation(10)

The integrals of the kind$\int_{t_0}^t \int_{t_0}^\tau  \text{ds} d\tau$ ,
$\int_{t_0}^t \int_{t_0}^\tau \text{dz(s)} d\tau$ and$\int _{t_0}^t \int_{t_0}^\tau  dz(s ) dz(\tau )$ and other higher
order integrals can be very easily analytically solved for monte carlo. These integrals also commute. I will post a
monte carlo simulation code for CEV and lognormal process based on the above logic in a few days.

If you like my above posts, I am looking for consulting and contract work and you could contact me for that at my email
anan2999(at)yahoo(dot)com

---

### #565 — Amin (Topic Author)
*December 5, 2017, 3:15 PM*

Very sorry for delay in posting the code for simulation based on above higher order monte carlo schemes. I will post
full code in a few days but here is the solution to stochastic integrals that need to be specified for monte carlo. Here
is the solution to those integrals.

In the equations below in the context of monte carlo t is the  step size in time.

$\int _0^t dz(\tau )=\sqrt{\text{t}} Z$   Equation(1)

$\int _0^t\int _0^{\tau }  dz(s) dz(\tau) =\frac{\text{t}  \left(Z^2-1\right)}{2}$    Equation(2)

$\int _0^t\int _0^{\tau }  ds dz(\tau )=\frac{\text{t}^{1.5} Z}{\sqrt{3}}$    Equation(3)

$\int _0^t\int_0^{\tau } dz(s) d\tau =\frac{\text{t}^{1.5} Z}{\sqrt{3}}$   Equation(4)

$\int _0^t\int _0^{\tau } dsd\tau =\frac{\text{t}^2}{2}$     Equation(5)

All the stochastic integrals share the same standard normal Z that we use in Equation(1). The above stochastic integrals
are given in terms of one standard normal draw for each monte carlo path. When they start from zero, as in monte carlo
in which all increments start over as if from time zero, all these double and higher order integrals commute.

I will soon post a full fledged matlab program for simulation using higher order monte carlo. For all those who wants to
do it themselves, you have to use solution of above stochastic integrals Eq(1)-Eq(5) in Equation(10) of previous post.

---

### #566 — Amin (Topic Author)
*December 6, 2017, 5:13 PM*

Here is a matlab program that simulates higher order iterated integral monte carlo of lognormal diffusion with drift and
compares it with traditional Euler method and also with exact analytic solution.

function [] = SVMonteCarloHigherOrderInfiniti( )

%SDE being discretized is

%dX(t)=mu0*X(t)*dt+simga0*X(t)*dz(t)

T_index=8; %No. of Simulation time steps

dt=.125/1.0; % Discretization spacing

TT=T_index*dt;%%Terminal Time

mu0=.40; %drift

sigma0=1.0;%volatility

X_0=1.0; %Starting Value of the lognormal diffusion

paths=1000000; %No Of Paths.

X(1:paths)=X_0; %Traditional Monte Carlo Variable

X1(1:paths)=X_0;%Iterated Integral Monte Carlo Variable

for nn=1:T_index %Loop over time.

    Random0=randn(size(X));

    %Stochastic integrals follow

    dZn=Random0*sqrt(dt);

    dZndt(1:paths)=dt.^1.5/sqrt(3)*Random0;

    dtdZn(1:paths)=dt.^1.5/sqrt(3)*Random0;

    dZndZn(1:paths)=dt/2.0.*(Random0.^2-1);

    dtdt=dt.^2.0/2.0;

    X=X+mu0.*X*dt+sigma0*X.*dZn; %Discretization of traditional Monte Carlo

    X1=X1+mu0.*X1*dt+sigma0*X1.*dZn ... %%Discretization of Iterated Integral

        +mu0.*mu0.*X1.*dtdt ...         %% Monte Carlo

        +mu0.*sigma0.*X1.*dZndt ...

        +sigma0.*mu0.*X1.*dtdZn ...

        +sigma0.*sigma0.*X1.*dZndZn;

end

%Following block is the analytic solution of lognormal SDE with drift.

n=0;

for n=1:2000

    n=n+1

    Z(n)=n*.005;

    Logf(n)=1.0/sqrt(2*pi)/Z(n)./(sigma0*sqrt(TT)).* ...

    exp(-.5*(log(Z(n))-log(X_0)-(mu0-.5*sigma0.^2)*TT).^2./(sigma0.^2*TT));

end

%The next block turns monte carlo diffusion into density.

MaxCutOff=50;

BinSize=.01;

[XDensity,IndexOutX,IndexMaxX] = MakeDensityFromSimulation_Infiniti(X,paths,BinSize,MaxCutOff );

[XDensity1,IndexOutX1,IndexMaxX1] = MakeDensityFromSimulation_Infiniti(X1,paths,BinSize,MaxCutOff );

plot(IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'r',IndexOutX1(1:IndexMaxX1),XDensity1(1:IndexMaxX1),'g', ...

 Z(1:2000),Logf(1:2000),'k')

%In the graph red line is traditional monte carlo with Euler method.

%green line is iterated integral monte carlo

%black line is analytic solution

str=input('look at overlaid Graph comparison of Monte carlo density of SDE using iterated integral(green line) with
density of SDE generated from analytic method(black line)>');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

Below is another function that is used for graphing the monte carlo diffusion and is called in the above program.

function [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti(X,Paths,BinSize,MaxCutOff )

%Processes monte carlo paths to return a series Xdensity as a function of IndexOut. IndexMax is the %maximum value of
index.

%

Xmin=0;

Xmax=0;

for p=1:Paths

if(X(p)>MaxCutOff)

X(p)=MaxCutOff;

end

if(Xmin>real(X(p)))

Xmin=real(X(p));

end

if(XmaxIndexMax)

index=IndexMax;

end

XDensity(index)=XDensity(index)+1.0/Paths/BinSize;

end

IndexOut(1:IndexMax)=Xmin+(0:(IndexMax-1))*BinSize;

end

---

### #567 — Amin (Topic Author)
*December 10, 2017, 8:58 AM*

Here is post 32 in this thread made on Sat Apr 30, 2016 1:12 pm in which I have given systematic solution to stochastic
integrals required for higher order monte carlo.

> *Amin:*I will take a few more days to complete the paper but here are a few formulas for friends. Here I give the
general algorithm for the type of integrals where only dz and dt integrals follow each other in any order. Like many
other possibilities, one four order repeated integral with two dz uncertainties could be
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\text{dv}\int _0^v\sigma  \text{dz}(w)$ The value of the above
kind of integrals, as long as there is no explicit t, does not depend upon the sequence order(whether dz integral comes
first or dt integral comes first does not change the value of the total integrals) so variance can be easily calculated
by Ito Isometry. The order of hermite polynomial depends upon the number of normal uncertainties so is equal to number
of dz integrals. Here is the simple formula to calculate the hermite polynomial representation of the integrals which
equals$ H_n(N)*\frac{\sqrt{\text{Variance}}}{\sqrt{n!}}$ here n, which is the order of hermite polynomials, equals the
number of normal uncertainties. I will give a few examples
>
> $\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}=H_1(N)\frac{\sigma\text{t}^{1.5}}{\sqrt{1!}\sqrt{3}}$
>
> $\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)=H_2(N)\frac{\sigma ^2t}{\sqrt{2!}\sqrt{2}}$
>
>
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\sigma\text{dz}(v)=\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\sigma\text{dz}(u)\int _0^u\sigma\text{dz}(v)=H_2(N)\frac{\sigma ^2t^2}{\sqrt{2!}\sqrt{12}}$
>
>
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\sigma\text{dz}(u)\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\text{du}\int _0^u\sigma\text{dz}(v)=H_1(N)\frac{\sigma ^2t^{2.5}}{\sqrt{1!}\sqrt{20}}$
>
>
$\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)\int _0^u\sigma\text{dz}(v)=H_3(N)\frac{\sigma ^3t^{1.5}}{\sqrt{3!}\sqrt{6}}$
>
> Fourth order and higher integrals can be evaluated to perfect precision using this method so I am not giving examples
for that.

Here is Post 37 in this thread where I have explained higher order monte carlo written on Mon May 02, 2016 1:43 pm

> *Amin:*Cuch, here you could see why those integrals are helpful. I have tried to explain in simple terms.We take a
general stochastic differential equation.$x(t)=x(0)+\int _0^t\mu (x(s)) \text{ds}+\int _0^t\sigma (x(s)) \text{dz}(s)$
Eq(1)Where$\mu\text{(x(s))}$ and$\text{ }\sigma\text{(x(s))}$ are x dependent functions and are stochastic due to
stochastic nature of x. It is unfortunate that when we use the above notation, we always substitute$\mu\text{(x(0))}$
for$\mu\text{(x(s))}$ and$\text{ }\sigma\text{(x(0))}$ for$\text{ }\sigma\text{(x(s))}$ as is standard in monte carlo
and other numerical analysis and little effort has been made to understand the time dependent nature and evolution of
$\mu\text{(x(s))}$ and$\text{ }\sigma\text{(x(s))}$ in between the simulation intervals. As I earlier said that
\mu\text{(x(s))} and$\text{ }\sigma\text{(x(s))}$ are functions that depend on x and are stochastic due to stochastic
nature of x. We define the evolution of these functions as
$\mu (x(s))=\mu (x(0))+\int _0^s \frac{\partial \mu (x(v))}{\partial x}\mu (x(v))\text{dv}+\int _0^s \frac{\partial \mu (x(v))}{\partial x}\sigma (x(v))\text{dz}(v)+.5\int _0^s \frac{\partial ^2\mu (x(v))}{\partial x^2}\sigma ^2(x(v)) \text{dv}$
Eq(2)
$\sigma (x(s))=\sigma (x(0))+\int _0^s \frac{\partial \sigma (x(v))}{\partial x}\mu (x(v))\text{dv}+\int _0^s \frac{\partial \sigma (x(v))}{\partial x}\sigma (x(v))\text{dz}(v)+.5\int _0^s \frac{\partial ^2\sigma (x(v))}{\partial x^2}\sigma ^2(x(v)) \text{dv}$
Eq(3)We can easily make the observation that x dependent terms in the above integrals from 0 to s could be expanded by
application of Ito formula into a time zero term and several other time dependent terms. We substitute equations 2 and 3
in Eq(1) to get
$x(t)=x(0)+\int _0^t\left(\mu (x(0))+\int _0^s \frac{\partial \mu (x(v))}{\partial x}\mu (x(v))\text{dv}+\int _0^s \frac{\partial \mu (x(v))}{\partial x}\sigma (x(v))\text{dz}(v)+.5\int _0^s \frac{\partial ^2\mu (x(v))}{\partial x^2}.\sigma ^2(x(v)) \text{dv}\right) \text{ds}+$
$\int _0^t\left(\sigma (x(0))+\int _0^s \frac{\partial \sigma (x(v))}{\partial x}\mu (x(v))\text{dv}+\int _0^s \frac{\partial \sigma (x(v))}{\partial x}\sigma (x(v))\text{dz}(v)+.5\int _0^s \frac{\partial ^2\sigma (x(v))}{\partial x^2}\sigma ^2(x(v)) \text{dv}\right) \text{dz}(s)$
Eq(4)Simplifying, we get
$x(t)=x(0)+\int _0^t\mu (x(0))\text{ds}+\int _0^t\int _0^s \frac{\partial \mu (x(v))}{\partial x}\mu (x(v))\text{dvds}+\int _0^t\int _0^s \frac{\partial \mu (x(v))}{\partial x}\sigma (x(v))\text{dz}(v)\text{ds}+.5\int _0^t\int _0^s \frac{\partial ^2\mu (x(v))}{\partial x^2}\left.\sigma ^2(x(v)) \text{dv}\right) \text{ds}+\int _0^t\sigma (x(0))\text{dz}(s)+\int _0^t\int _0^s \frac{\partial \sigma (x(v))}{\partial x}\mu (x(v))\text{dvdz}(s)$
$+\int _0^t\int _0^s \frac{\partial \sigma (x(v))}{\partial x}\sigma (x(v))\text{dz}(v)\text{dz}(s)+.5\int _0^t\int _0^s \frac{\partial ^2\sigma (x(v))}{\partial x^2}\sigma ^2(x(v)) \text{dv}\text{dz}(s)$
Eq(5) In the expression above only two single integrals$\int _0^t\mu (x(0))\text{ds}$ and
$\int _0^t\sigma (x(0))\text{dz}(s)$ depend upon time zero value of x and the rest of the double integrals all depend
upon forward time dependent values and have to be expanded again similarly and this process could continue until
derivatives existed(though we would generally always stop at third or fourth level if we could atain desired precision).
We expand just the first double integral in Eq(5) further as an example
$\int _0^t\int _0^s \frac{\partial \mu (x(v))}{\partial x}\mu (x(v))\text{dvds}=\int _0^t\int _0^s \frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\text{dvds}+\int _0^t\int _0^s\int _0^v\frac{\partial }{\partial x} \left[\frac{\partial \mu (x(u))}{\partial x}\mu (x(u))\right]\mu (x(u))\text{dudvds}$
$+\int _0^t\int _0^s\int _0^v\frac{\partial }{\partial x} \left[\frac{\partial \mu (x(u))}{\partial x}\mu (x(u))\right]\sigma (x(u))\text{dz}(u)\text{dvds}+\int _0^t\int _0^s\int _0^v.5\frac{\partial ^2}{\partial x^2} \left[\frac{\partial \mu (x(u))}{\partial x}\mu (x(u))\right]\sigma ^2(x(u))\text{dudvds}$
Eq(6)We could continue further but if further derivatives continue to exist, we have to ultimately truncate the
expansion at some level and we could simply substitute time zero values of drift and volatility for forward time
dependent values of drift and volatility. If we decide to stop the expansion at second level, we could write from Eq(5)
(Please notice that 2nd equality in equation below is approximate equality)
$x(t)=x(0)+\int _0^t\mu (x(0))\text{ds}+\int _0^t\int _0^s \frac{\partial \mu (x(v))}{\partial x}\mu (x(v))\text{dvds}+\int _0^t\int _0^s \frac{\partial \mu (x(v))}{\partial x}\sigma (x(v))\text{dz}(v)\text{ds}+.5\int _0^t\int _0^s \frac{\partial ^2\mu (x(v))}{\partial x^2}\left.\sigma ^2(x(v)) \text{dv}\right) \text{ds}$
$+\int _0^t\sigma (x(0))\text{dz}(s)+\int _0^t\int _0^s \frac{\partial \sigma (x(v))}{\partial x}\mu (x(v))\text{dvdz}(s)+\int _0^t\int _0^s \frac{\partial \sigma (x(v))}{\partial x}\sigma (x(v))\text{dz}(v)\text{dz}(s)+.5\int _0^t\int _0^s \frac{\partial ^2\sigma (x(v))}{\partial x^2}\sigma ^2(x(v)) \text{dv}\text{dz}(s)$
$=x(0)+\int _0^t\mu (x(0))\text{ds}+\int _0^t\int _0^s \frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\text{dvds}+\int _0^t\int _0^s \frac{\partial \mu (x(0))}{\partial x}\sigma (x(0))\text{dz}(v)\text{ds}+.5\int _0^t\int _0^s \frac{\partial ^2\mu (x(0))}{\partial x^2}\left.\sigma ^2(x(0)) \text{dv}\right) \text{ds}$
$+\int _0^t\sigma (x(0))\text{dz}(s)+\int _0^t\int _0^s \frac{\partial \sigma (x(0))}{\partial x}\mu (x(0))\text{dvdz}(s)+\int _0^t\int _0^s \frac{\partial \sigma (x(0))}{\partial x}\sigma (x(0))\text{dz}(v)\text{dz}(s)+.5\int _0^t\int _0^s \frac{\partial ^2\sigma (x(0))}{\partial x^2}\sigma ^2(x(0)) \text{dv}\text{dz}(s)$
$=x(0)+\mu (x(0))\int _0^t\text{ds}+\frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\int _0^t\int _0^s \text{dvds}+\frac{\partial \mu (x(0))}{\partial x}\sigma (x(0))\int _0^t\int _0^s \text{dz}(v)\text{ds}+.5\frac{\partial ^2\mu (x(0))}{\partial x^2}\sigma ^2(x(0)) \int _0^t\int _0^s  \text{dv} \text{ds}$
$+\sigma (x(0))\int _0^t\text{dz}(s)+\frac{\partial \sigma (x(0))}{\partial x}\mu (x(0))\int _0^t\int _0^s \text{dvdz}(s)+\frac{\partial \sigma (x(0))}{\partial x}\sigma (x(0))\int _0^t\int _0^s \text{dz}(v)\text{dz}(s)+.5\frac{\partial ^2\sigma (x(0))}{\partial x^2}\sigma ^2(x(0))\int _0^t\int _0^s\text{dv}\text{dz}(s)$
In case we wanted to go to fourth or hififth or even higher level, we could have continued the repeated expansion and
finally replaced forward values at their time zero values but If we only wanted to continue to third level, we could
have truncated the further series and replaced forward values by their time zero values and could have included
integrals of the kind from Eq(6). Please recall that when we wrote Eq(6), we expanded just one integral and other
integral terms have to be similarly expanded.(Please notice that 2nd equality in equation below is approximate equality)
$\int _0^t\int _0^s \frac{\partial \mu (x(v))}{\partial x}\mu (x(v))\text{dvds}$
$=\int _0^t\int _0^s \frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\text{dvds}+\int _0^t\int _0^s\int _0^v\frac{\partial }{\partial x} \left[\frac{\partial \mu (x(u))}{\partial x}\mu (x(u))\right]\mu (x(u))\text{dudvds}+\int _0^t\int _0^s\int _0^v\frac{\partial }{\partial x} \left[\frac{\partial \mu (x(u))}{\partial x}\mu (x(u))\right]\sigma (x(u))\text{dz}(u)\text{dvds}+\int _0^t\int _0^s\int _0^v.5\frac{\partial ^2}{\partial x^2} \left[\frac{\partial \mu (x(u))}{\partial x}\mu (x(u))\right]\sigma ^2(x(u))\text{dudvds}$
$=\frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\int _0^t\int _0^s \text{dvds}+\frac{\partial }{\partial x} \left[\frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\right]\mu (x(0))\int _0^t\int _0^s\int _0^v\text{dudvds}+\frac{\partial }{\partial x} \left[\frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\right]\sigma (x(0))\int _0^t\int _0^s\int _0^v\text{dz}(u)\text{dvds}+.5\frac{\partial ^2}{\partial x^2} \left[\frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\right]\sigma ^2(x(0))\int _0^t\int _0^s\int _0^v\text{dudvds}$
Cuch, here is the answer to your question in an earlier post why these integrals are helpful. As you can see in the
above equation, once we have taken initial time zero values of x dependent coefficients, the integrals to be evaluated
are of the kind$\int _0^t\int _0^s\int _0^v\text{dudvds}$ ,$\int _0^t\int _0^s\int _0^v\text{dz}(u)\text{dvds}$ ,
$\int _0^t\int _0^s\int _0^v\text{dz}(u)\text{dz}(v)\text{ds}$ and
$\int _0^t\int _0^s\int _0^v\text{dz}(u)\text{dz}(v)\text{dz}(s)$ which I mentioned how to evaluate in a previous post
using ito isometry and simple hermite polynomials.

---

### #568 — Amin (Topic Author)
*December 10, 2017, 9:05 AM*

In light of post 32 and post 37 of this thread copied in the last post 567, I want to mention that I had fully specified
the method of iterated integrals solution to SDEs as early as May 2016. Though I have written a formal paper on iterated
integrals solution to ODEs, I have not written a formal paper on iterated integrals solution to SDEs. If any friend
wants to do further research and discover new things using method of iterated integrals beyond what I have done or
include method of iterated integrals in a book, I would request them to please give reference to my research that I
deserve. I would be very thankful to friends who would give me credit that I deserve due to my original research.

I just noticed that latex in the above copied posts 35 and 37 of this thread is problematic despite that I copied it from there. Please refer to original post 32 and 37 on this thread here [viewtopic.php?f=4&t=99702&start=30](https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=30)

---

### #569 — Amin (Topic Author)
*December 29, 2017, 7:00 PM*

On 1st of next year, I will post matlab code for simulation with stochastic calculus of standard deviations. This is
different from what I have been doing like monte carlo simulation of SDEs with method of iterated integrals but method
of iterated integrals is still used for the solution of Fokker planck with stochastic calculus of standard deviations.
We could later solve for two dimensional distributions of the kind that arise in stochastic volatility models. Very
exciting stuff and very innovative research on probability distributions and solution of Fokker planck equations.

---

### #570 — Amin (Topic Author)
*January 1, 2018, 5:09 PM*

Sorry Friends. It will be another day or two before I could post everything. This new version is very close to something
people could use in a commercial industrial setting. I want to explain everything so people could understand it and be
able to extend it on their own and do more research. It will still take two to three days before I could post an easily
accessible explanation of the method and its underlying principles. I want to link every equation in my explanation to
the ones in the code so people could easily change it on their own and do more research. It is promised to be very
different and exciting for people in stochastics. I am sure in a few months, people would start doing all sort of new
things like calibrations of SV models and backward monte carlo of derivatives in this new setting I have proposed.

---

### #571 — Amin (Topic Author)
*January 3, 2018, 1:56 PM*

Here is the small matlab program for comparison of density with SCSD method and true density.

%If you share interests in Mathematical Finance and Statistics I invite you

%to connect on skype using Skype ID: ahsan.amin2999

%I also invite you to connect on linkedin using
email:[[email protected]](/cdn-cgi/l/email-protection#3a5b545b54080303037a435b52555514595557)

%This program is only initial demonstration of Stochastic Calculus of

%Standard Deviations technology.

%A new and more comprehensive program will appear on

%Wilmott.com web site after the research paper is complete on SSRN.

% The SDE whose probability distribution is calculated

% is CEV noise SDE.

%dX(t)=epsilon*X(t)^gamma*dz(t) with X(0)=x0;

%For consulting and innovative work related to this new technology

%Please feel free to email me.

%In the program

%1st hermite polynomial is const/prob2;

%2nd hermite polynomial is (const2/prob2-1);

%third hermite polynomial is (const3/prob2-3*const/prob2);

%These are calculated using normal density.

Program starts below.

function [] = SDEXticsInfinitiTechnologiesCEVNEWSerialX( )

X0_max=800;%Total number of SD Fractions.

X0_mid=400.5;%Mid of the SD Grid. Lies at z0 by definition.

X0_mid0=400;

X0_start=1;

dX0=.01;%*8.0;%Width of SD cells in terms of Standard Deviations.

T_index=600;

dt=1/12.0/100;%hundredth of a month

t_T=600/12/100;%%=.5

epsilon=0.650;

gamma=.650;

x0=1.0;

X(1:X0_max)=x0;

z_t(1:X0_max)=0;

z_t0(1:X0_max)=0;

iivector(1:X0_max)=1:X0_max;

H11_1(1:X0_max)=0;

H11_2(1:X0_max)=0;

H11_3(1:X0_max)=0;

H11_4(1:X0_max)=0;

H22_1(1:X0_max)=0;

H22_2(1:X0_max)=0;

H22_3(1:X0_max)=0;

H22_4(1:X0_max)=0;

H33_1(1:X0_max)=0;

H33_2(1:X0_max)=0;

H33_3(1:X0_max)=0;

H33_4(1:X0_max)=0;

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

%prob2=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)*dX0;

prob2=normcdf(((iivector-X0_mid).*dX0)+.5*dX0)-normcdf(((iivector-X0_mid).*dX0)-.5*dX0);

prob0=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0);

for nn=1:T_index %Loop over time.

    t=(nn)*dt;

    t0=(nn-1)*dt;

    prob=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)/(sqrt(t)*epsilon); %Probability in each SD Grid cell.

    dt=t-t0;

    for mm=1:X0_max

        z_t0(mm)=sqrt(t0).*(const(mm)./prob2(mm));

        z_t(mm)=sqrt(t).*(const(mm)./prob2(mm));

        H33_1(mm)=(const2(mm)./prob2(mm)-1.0)./sqrt(24.0).*(t.^2-t0.^2);

        H33_3(mm)=-(const2(mm)./prob2(mm)-1.0).*(t-t0)/2.0.*t0;

        H33_2(mm)=-(const(mm)./prob2(mm)).*(t0.^1.5)/sqrt(3).*(z_t(mm)-z_t0(mm));

        H33_4(mm)=(z_t(mm)-z_t0(mm)).*t0.*z_t0(mm);

        H22_1(mm)=(const2(mm)./prob2(mm)-1.0)./sqrt(24.0).*(t.^2-t0.^2);

        H22_2(mm)=-(const(mm)./prob2(mm)).*(t.^1.5-t0.^1.5)/sqrt(3).*z_t0(mm);

        H22_3(mm)=-(const(mm)./prob2(mm)).*(t0.^1.5)/sqrt(3).*(z_t(mm)-z_t0(mm));

        H22_4(mm)=(z_t(mm)-z_t0(mm)).*t0.*z_t0(mm);

        H11_1(mm)=(t.^1.5-t0.^1.5)/6.0.*(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm));

        H11_2(mm)=-(z_t(mm)-z_t0(mm)).*.5.*t0.*(const2(mm)./prob2(mm)-1.0);

        H11_3(mm)=-(z_t0(mm)).*.5.*(t-t0).*(const2(mm)./prob2(mm)-1.0);

        H11_4(mm)=(z_t(mm)-z_t0(mm)).*z_t0(mm).*z_t0(mm);

        if(X(mm)>0.0)

            X(mm)=X(mm)+...

             epsilon.^1.*X(mm).^gamma.*(z_t(mm)-z_t0(mm)) ...

             +(1.0.*gamma.*X(mm).^(2*gamma-1)).* ...

            (((const2(mm)./prob2(mm)-1).*epsilon.^2.*(t-t0)*.5)- ...

              epsilon.^2.*z_t0(mm).*(z_t(mm)-z_t0(mm)))...

             +1.0.*gamma.*(2*gamma-1).*X(mm).^(3*gamma-2) ...

             .*(epsilon.^3.*H11_1(mm)+epsilon.^3.*H11_2(mm)+epsilon.^3*H11_3(mm)+epsilon.^3.0.*H11_4(mm)) ...

              +.5/1.0*gamma.*(gamma-1).*X(mm).^(3*gamma-2).*(epsilon.^3.*(t^1.5-t0^1.5)/sqrt(3).*const(mm)./prob2(mm)
...

              -epsilon.^3.*t0.*(z_t(mm)-z_t0(mm))) ...  %...

            +.5*.5*gamma.*(gamma-1).*(3*gamma-2).*X(mm).^(4*gamma-3).* ...

                (epsilon.^4.0.*H22_1(mm)+epsilon.^4.*H22_2(mm)+epsilon.^4.*H22_3(mm)+epsilon.^4.0.*H22_4(mm)) ...

            +.5/1*gamma.^2.0.*(gamma-1).*X(mm).^(4*gamma-3.0).* ...

            (epsilon.^4.0.*H33_1(mm)+epsilon.^4.0.*H33_2(mm)+epsilon.^4.0.*H33_3(mm)+epsilon.^4.0.*H33_4(mm));

        end

        if(X(mm)=.5)

        P(:)=1-ncx2cdf(a,b,c(:));%Numerically generate driftless CEV CDF

    else

        P(:)=ncx2cdf(c(:),2-b,a);%Numerically generate driftless CEV CDF

    end

    for n=1:N-1

        if(n==1)

            p(n)=P(n)./dG_n(n);%CEV transition probability for first grid point

        end

        if(n>=2)

            p(n)=(P(n)-P(n-1))./dG_n(n);%CEV transition probability on grid point n>=2

        end

    end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

X_avg=sum(X.*prob2)

X_avg0=sum(X.*prob0.*dX0)

plot(G(1:N-1),p(1:N-1),'g',(X(X0_start+2:X0_max-2)),prob(X0_start+2:X0_max-2).*Jacobian_X(X0_start+2:X0_max-2),'r')

str=input('look at overlaid Graph comparison of true density of SDE(green line) with density of SDE generated from SCSD
analytic method(red line)>');

end

---

### #572 — Amin (Topic Author)
*January 3, 2018, 2:04 PM*

I will follow with complete details in a few hours but just for a check, the current program when it will run in matlab,
it will give the result in long display format as given below.

X_avg =

   0.999856578196410

X_avg0 =

   0.999654860791792

I will follow with Complete theoretical detail with equations. The program is quite satisfactory but it needs to be
improved very close to zero. I believe adding higher derivatives will help remove this problem.

---

### #573 — Amin (Topic Author)
*January 3, 2018, 3:16 PM*

The evolution equation of nth subdivision of SDE Variable$X_n(t)$ associated with nth Gaussian standard deviation is
given below

$X_n(t)=X_n\left(t_0\right)+\epsilon\text{X}_n\left(t_0\right)\int _{t_0}^tdz_n(s)$          Integral(1)

$+\epsilon ^2 \gamma  X_n\left(t_0\right){}^{2\gamma -1}\int_{t_0}^t\int _{t_0}^sdz_n(v)dz_n(s)$           Integral(2)

$+.5\epsilon ^3 \gamma (\gamma -1) X_n\left(t_0\right){}^{3\gamma -2}\int _{t_0}^t\int _{t_0}^sdvdz_n(s)$ Integral(3)

$+\epsilon ^3 \gamma (2\gamma -1) X_n\left(t_0\right){}^{3\gamma -2}\int _{t_0}^t\int _{t_0}^s\int _{t_0}^vdz_n(u)dz_n(v)dz_n(s)$
Integral(4)

$+.5\epsilon ^4 \gamma (\gamma -1) (3\gamma -2)X_n\left(t_0\right){}^{4\gamma -3}\int _{t_0}^t\int _{t_0}^s\int _{t_0}^v dz_n(u)dvdz_n(s)$
Integral(5)

$+\epsilon ^4 \gamma ^2(\gamma -1) X_n\left(t_0\right){}^{4\gamma -3}\int _{t_0}^t\int _{t_0}^s\int _{t_0}^v du dz_n(v)dz_n(s)$
Integral(6)

To calculate these iterated integrals, we rewrite the integrals as some of integrals starting from lower integral limits
as zero so we could easily calculate them using ito isometry. here H1(n), H2(n) and H3(n) are hermite polynomials of
1st, 2nd and 3rd order associated with nth subdivision of standard normal density. In the accompanying program 1st
hermite polynomial is const/prob2; 2nd hermite polynomial is (const2/prob2-1); third hermite polynomial is
(const3/prob2-3*const/prob2);These are calculated using standard normal density.

Solution to integral (1)

$\int _{t_0}^tdz_n(s)=z_n(t)-z_n\left(t_0\right)$

Solution to integral (2)

$\int _{t_0}^t\int _{t_0}^sdz_n(v)dz_n(s)=\int _{t_0}^t\int _0^sdz_n(v)dz_n(s)-\int _{t_0}^t\int _0^{t_0}dz_n(v)dz_n(s)$

$=\int _0^t\int _0^sdz_n(v)dz_n(s)-\int _0^{t_0}\int _0^sdz_n(v)dz_n(s)-\int _0^t\int _0^{t_0}dz_n(v)dz_n(s)+$

$\int _0^{t_0}\int _0^{t_0}dz_n(v)dz_n(s)$

$=.5t \text{H2}(n)-.5t_0\text{H2}(n)-z_n(t_0) z_n(t)+z_n(t_0)z_n(t_0)$

Solution to integral (3)

$\int _{t_0}^t\int _{t_0}^sdvdz_n(s)=\int _{t_0}^t\int _0^sdvdz_n(s)-\int _{t_0}^t\int _0^{t_0}dv dz_n(s)$

$=\int _0^t\int _0^sdvdz_n(s)-\int _0^{t_0}\int _0^sdvdz_n(s)-\int _0^t\int _0^{t_0}dvdz_n(s)+\int _0^{t_0}\int _0^{t_0}dvdz_n(s)$

$=\frac{t^{1.5}}{\sqrt{3}} \text{H1}(n)-\frac{t_0{}^{1.5}}{\sqrt{3}} \text{H1}(n)-t_0 z_n(t)+t_0z_n\left(t_0\right)$

Solution to integral (4)

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^vdz_n(u)dz_n(v)dz_n(s)$

$=\int _{t_0}^t\int _{t_0}^s\int _0^vdz_n(u)dz_n(v)dz_n(s)-\int _{t_0}^t\int _{t_0}^s\int _0^{t_0}dz_n(u)dz_n(v)dz_n(s)$

$=\int _{t_0}^t\int _0^s\int _0^vdz_n(u)dz_n(v)dz_n(s)-\int _{t_0}^t\int _0^{t_0}\int _0^vdz_n(u)dz_n(v)dz_n(s)$

$-\int _{t_0}^t\int _0^s\int _0^{t_0}dz_n(u)dz_n(v)dz_n(s)+\int _{t_0}^t\int _0^{t_0}\int _0^{t_0}dz_n(u)dz_n(v)dz_n(s)$

$=\int _0^t\int _0^s\int _0^vdz_n(u)dz_n(v)dz_n(s)-\int _0^{t_0}\int _0^s\int _0^vdz_n(u)dz_n(v)dz_n(s)$

$-\int _0^t\int _0^{t_0}\int _0^vdz_n(u)dz_n(v)dz_n(s)+\int _0^{t_0}\int _0^{t_0}\int _0^vdz_n(u)dz_n(v)dz_n(s)$

$-\int _0^t\int _0^s\int _0^{t_0}dz_n(u)dz_n(v)dz_n(s)+\int _0^{t_0}\int _0^s\int _0^{t_0}dz_n(u)dz_n(v)dz_n(s)$

$+\int _0^t\int _0^{t_0}\int _0^{t_0}dz_n(u)dz_n(v)dz_n(s)-\int _0^{t_0}\int _0^{t_0}\int _0^{t_0}dz_n(u)dz_n(v)dz_n(s)$

$={H3}(n)\frac{t^{1.5}}{6}-\text{H3}(n)\frac{t_0{}^{1.5}}{6}$

$-{H2}(n)\frac{t_0}{2}+z_n\left(t_0\right)\text{H2}(n)\frac{t_0}{2}$

$-\text{H2}(n)\frac{t}{2}z_n\left(t_0\right)+\text{H2}(n)\frac{t_0}{2}z_n\left(t_0\right)$

$+z_n(t)z_n\left(t_0\right)z\left(t_0\right)-z_n\left(t_0\right)z_n\left(t_0\right)z_n\left(t_0\right)$

Solution to integral (5)

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^vdz_n(u)dvdz_n(s)$

$=\int _0^t\int _0^s\int _0^vdz_n(u)dvdz_n(s)-\int _0^{t_0}\int _0^s\int _0^vdz_n(u)dvdz_n(s)$

$-\int _0^t\int _0^{t_0}\int _0^vdz_n(u)dvdz_n(s)+\int _0^{t_0}\int _0^{t_0}\int _0^vdz_n(u)dvdz_n(s)$

$-\int _0^t\int _0^s\int _0^{t_0}dz_n(u)dvdz_n(s)+\int _0^{t_0}\int _0^s\int _0^{t_0}dz_n(u)dvdz_n(s)$

$+\int _0^t\int _0^{t_0}\int _0^{t_0}dz_n(u)dvdz_n(s)-\int _0^{t_0}\int _0^{t_0}\int _0^{t_0}dz_n(u)dvdz_n(s)$

$=\text{H2}(n)\frac{t^2}{24}-\text{H2}(n)\frac{t_0{}^2}{24}$

$-z(t)\text{H1}(n)\frac{t_0{}^{1.5}}{\sqrt{3}}+z_n\left(t_0\right)\text{H1}(n)\frac{t_0{}^{1.5}}{\sqrt{3}}$

$-z_n\left(t_0\right)\text{H1}(n)\frac{t^{1.5}}{\sqrt{3}}+z_n\left(t_0\right)\text{H1}(n)\frac{t_0{}^{1.5}}{\sqrt{3}}$

$+z_n\left(t_0\right)t_0z_n(t)-z_n\left(t_0\right)t_0z_n\left(t_0\right)$

Solution to integral (6)

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^vdudz(v)dz(s)$

$=\int _0^t\int _0^s\int _0^vdudz_n(v)dz_n(s)-\int _0^{t_0}\int _0^s\int _0^vdud_nz(v)dz_n(s)$

$-\int _0^t\int _0^{t_0}\int _0^vdudz_n(v)dz_n(s)+\int _0^{t_0}\int _0^{t_0}\int _0^vdudz_n(v)dz_n(s)$

$-\int _0^t\int _0^s\int _0^{t_0}dudz_n(v)dz_n(s)+\int _0^{t_0}\int _0^s\int _0^{t_0}dudz_n(v)dz_n(s)$

$+\int _0^t\int _0^{t_0}\int _0^{t_0}dudz_n(v)dz_n(s)-\int _0^{t_0}\int _0^{t_0}\int _0^{t_0}dudz_n(v)dz_n(s)$

$=\text{H2}(n)\frac{t^2}{24}-\text{H2}(n)\frac{t_0{}^2}{24}$

$-z(t)\text{H1}(n)\frac{t_0{}^{1.5}}{\sqrt{3}}+z_n\left(t_0\right)\text{H1}(n)\frac{t_0{}^{1.5}}{\sqrt{3}}$

$-t_0\text{H2}(n)\frac{t}{2}+t_0\text{H2}(n)\frac{t_0}{2}$

$+t_0z\left(t_0\right)z_n(t)-t_0z_n\left(t_0\right)z_n\left(t_0\right)$

Please ask any question and let me know how I could explain better.

---

### #574 — Amin (Topic Author)
*January 3, 2018, 3:27 PM*

We have introduced a new numerical method in stochastics that simulates the evolution of the density of a stochastic
differential equation. This is a new method that takes a starting density (possibly a delta density) and evolves it in
time using an explicit algorithm that updates the density according to given SDE dynamics over time. It is like the
solution of a Fokker Planck equation in time but obtained far more cheaply and in a way that transition probabilities of
the density are exactly known between any two points in time and space.

Here is a link to a small document that I had written about some of the possibilities about what we can do with this new technology. [https://drive.google.com/file/d/0B1UoJb ... sp=sharing](https://drive.google.com/file/d/0B1UoJb9Zaj22WmxkSDZHcUt6TE0/view?usp=sharing)

---

### #575 — Cuchulainn
*January 3, 2018, 3:50 PM*

*Please ask any question and let me know how I could explain better.*

These formulae are mind-boggling.

---

### #576 — Amin (Topic Author)
*January 3, 2018, 5:52 PM*

**(broken latex: Unbalanced $$: 3)**

```latex
Sorry I failed to explain properly. Once you know how I solved these integrals, you would know that this is in fact very
easy to do that. I try to explain one third order integral again in better detail. These integrals start from$t_0$ and
it is not straightforward how to solve them with$t_0$ limit. However if we can convert lower limits to zero, we can
easily solve them with Ito isometry. Here is the integral under consideration. Please note that I have removed subscript
n from$z_n(t)$ for the sake of simplicity here.

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^vdz(u)dz(v)dz(s)$  equation 1.

We take the inner most integral.

$\int _{t_0}^vdz(u)$       integral 2

This integral has limits$t_0$ to v. We divide it into two integrals. The first is zero to v and we subtract the integral
from zero to$t_0$ so that both new integrals have lower limit from zero and they sum up to integral 2.

$\int _{t_0}^vdz(u)=\int _0^vdz(u)-\int _0^{t_0}dz(u)$  equation(3)

We have divided the innermost integral in equation 1 into two integrals that both have lower limit at zero. Now we add
the middle integral in equation 1 and we have that

$\int _{t_0}^s\int _{t_0}^vdz(u)dz(v)$  equation(4)

applying equation 3 to inner integral in above equation(4), we get

$\int _{t_0}^s\int _{t_0}^vdz(u)dz(v)=\int _{t_0}^s\int _0^vdz(u)dz(v)-\int _{t_0}^s\int _0^{t_0}dz(u)dz(v)$ Equation(5)

Now we apply the same change of lower limits to zero for 1st integral in RHS of equation (5) and divide outer integral
from$t_0$ to s into two integrals with limits zero to s minus zero to$t_0$

$\int _{t_0}^s\int _0^vdz(u)dz(v)=\int _{0}^s\int _0^vdz(u)dz(v)-\int _0^{t_0}\int _0^vdz(u)dz(v)$  Equation(6)

similarly for the second integral in RHS of equation(5)

$\int _{t_0}^s\int _0^{t_0}dz(u)dz(v)$

$=\int _0^s\int _0^{t_0}dz(u)dz(v)$$-\int _0^{t_0}\int _0^{t_0}dz(u)dz(v)$   Equation(7)

We substitute equations 6 and 7 in the RHS of Equation(5) to get

$\int _{t_0}^s\int _{t_0}^vdz(u)dz(v)$

$=\int _{0}^s\int _0^vdz(u)dz(v)-\int _0^{t_0}\int _0^vdz(u)dz(v)$

$-\int _0^s\int _0^{t_0}dz(u)dz(v)$$+\int _0^{t_0}\int _0^{t_0}dz(u)dz(v)$   Equation(8)

Equation(8) is the solution to two inner integrals in equation(1). We substitute it inside equation(1) to get

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^vdz(u)dz(v)dz(s)$

$=\int _{t_0}^t\int _{0}^s\int _0^vdz(u)dz(v)dz(s)-\int _{t_0}^t\int _0^{t_0}\int _0^vdz(u)dz(v)dz(s)$

$-\int _{t_0}^t\int _0^s\int _0^{t_0}dz(u)dz(v)dz(s)$$+\int _{t_0}^t\int _0^{t_0}\int _0^{t_0}dz(u)dz(v)dz(s)$
Equation(9)

All the inner integrals have lower limit at zero. We repeat the previous technique with outer integral and divide it
into two integrals such that both have a zerl lower limit. Taking the first third order integral in RHS of equation(9),
we get

$\int _{t_0}^t\int _{0}^s\int _0^vdz(u)dz(v)dz(s)=\int _0^t\int _{0}^s\int _0^vdz(u)dz(v)dz(s)-\int _0^{t_0}\int _{0}^s\int _0^vdz(u)dz(v)dz(s)$
Equation(10)

Similalry for other three integrals in the RHS of equation 9 to get the answer

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^vdz(u)dz(v)dz(s)$

$=\int _0^t\int _0^s\int _0^vdz(u)dz(v)dz(s)-\int _0^{t_0}\int _0^s\int _0^vdz(u)dz(v)dz(s)$

$-\int _0^t\int _0^{t_0}\int _0^vdz(u)dz(v)dz(s)+\int _0^{t_0}\int _0^{t_0}\int _0^vdz(u)dz(v)dz(s)$

$-\int _0^t\int _0^s\int _0^{t_0}dz(u)dz(v)dz(s)+\int _0^{t_0}\int _0^s\int _0^{t_0}dz(u)dz(v)dz(s)$

$+\int _0^t\int _0^{t_0}\int _0^{t_0}dz(u)dz(v)dz(s)-\int _0^{t_0}\int _0^{t_0}\int _0^{t_0}dz(u)dz(v)dz(s)$
Equation(11)

Basically all of the above is extremely simple and only play with the limits of integrals.

Now using ito isometry with stochastic integrals, we get the answer as

$=\text{H3}(n)\frac{t^{1.5}}{6}-\text{H3}(n)\frac{t_0{}^{1.5}}{6}$

$-z(t)\text{H2}(n)\frac{t_0}{2}+z\left(t_0\right)\text{H2}(n)\frac{t_0}{2}$

$-\text{H2}(n)\frac{t}{2}z\left(t_0\right)+\text{H2}(n)\frac{t_0}{2}z\left(t_0\right)$

$+z(t)z\left(t_0\right)z\left(t_0\right)-z\left(t_0\right)z\left(t_0\right)z\left(t_0\right)$

```

---

### #577 — Cuchulainn
*January 4, 2018, 7:41 PM*

> Suppose we want to solve the following general SDE
>
>
>
> $\text{dX} (\tau) = \mu  (X(\tau)) \text{d}\tau+ \sigma(X(\tau))  \text{dz}( \tau)  $  Equation(1)
>
>
>
> The formal solution of the above SDE is given as
>
> $X(t)=X(t_0)+\int_{t_0}^t \mu (X(\tau)) \, d\tau+\int _{t_0}^t\sigma(X(\tau))  dz(\tau )$  Equation(2)
>
>
>
> We want to solve both integrand terms in above equation as
>
> $ \mu (X(\tau))=\mu (X(t_0))+\int_{t_0}^\tau d\mu (X(s))$   Equation(3)
>
> and
>
> $ \sigma (X(\tau))=\sigma (X(t_0))+\int_{t_0}^\tau d\sigma (X(s))$  Equation(4)
>
> When we substitute above equation(3) and equation(4) in equation(2), we get
>
>
>
> $X(t)=X(t_0)+\int_{t_0}^t \mu (X(t_0)) \, d\tau+\int_{t_0}^t \int_{t_0}^\tau d\mu (X(s)) d\tau $
>
> $+\int _{t_0}^t\sigma(X(t_0))  dz(\tau )+\int _{t_0}^t \int_{t_0}^\tau d\sigma (X(s)) dz(\tau )$  Equation(5)
>
>
>
> From Ito expansion of $d\mu (X(s)) $ and $d\sigma (X(s)) $, we know that
>
>
$d\mu  (X(s))=\frac{\partial }{\partial X}[\mu ( X(s))]\mu (X(s)) \text{ds}+\frac{\partial }{\partial X}[\mu  (X(s))]\sigma (X(s)) \text{dz(s)}$
>
> $+0.5 \frac{\partial ^2[\mu  ( X(s))]}{\partial X^2} \sigma ( X(s))^2\text{ds}$ Equation(6)
>
>
>
> and
>
>
$d\sigma ( X(s))=\frac{\partial }{\partial X}[\sigma ( X(s))]\mu (X(s)) \text{ds}+\frac{\partial }{\partial X}[\sigma  (X(s))]\sigma (X(s)) \text{dz(s)}$
>
> $+0.5 \frac{\partial ^2[\sigma  ( X(s))]}{\partial X^2} \sigma ( X(s))^2\text{ds}$  Equation(7)
>
>
>
> We substitute equation (6) and Equation(7) in equation(5)
>
>
>
> $X(t)=X(t_0)+\int_{t_0}^t \mu (X(t_0)) \, d\tau$
>
>
$+\int_{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\mu ( X(s))]\mu (X(s)) \text{ds} d\tau+\int_{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\mu  (X(s))]\sigma (X(s)) \text{dz(s)} d\tau$
>
> $+\int_{t_0}^t \int_{t_0}^\tau 0.5 \frac{\partial ^2[\mu ( X(s))]}{\partial X^2} \sigma ( X(s))^2\text{ds} d\tau$
>
> $+\int _{t_0}^t\sigma(X(t_0))  dz(\tau )$
>
> $+\int _{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\sigma ( X(s))]\mu (X(s)) \text{ds} dz(\tau )$
>
> $+\int _{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\sigma ( X(s))]\sigma (X(s)) dz(s ) dz(\tau )$
>
>
$+\int_{t_0}^t \int_{t_0}^\tau 0.5 \frac{\partial ^2[\sigma ( X(s))]}{\partial X^2} \sigma ( X(s))^2\text{ds} dz(\tau )$
Equation(8)
>
> In a further order expansion, we evaluate terms at time 's' at$t_0$ and add a third order integral. I am not showing
the third order integral but up to second order, we will have
>
>
>
> $X(t)=X(t_0)+\int_{t_0}^t \mu (X(t_0)) \, d\tau$
>
>
$+\int_{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\mu ( X(t_0))]\mu (X(t_0)) \text{ds} d\tau+\int_{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\mu  (X(t_0))]\sigma (X(t_0)) \text{dz(s)} d\tau$
>
> $+\int_{t_0}^t \int_{t_0}^\tau 0.5 \frac{\partial ^2[\mu ( X(t_0))]}{\partial X^2} \sigma ( X(t_0))^2\text{ds} d\tau$
>
> $+\int _{t_0}^t\sigma(X(t_0))  dz(\tau )$
>
> $+\int _{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\sigma ( X(t_0))]\mu (X(t_0)) \text{ds} dz(\tau )$
>
> $+\int _{t_0}^t \int_{t_0}^\tau \frac{\partial }{\partial X}[\sigma ( X(t_0))]\sigma (X(t_0)) dz(s ) dz(\tau )$
>
>
$+\int_{t_0}^t \int_{t_0}^\tau 0.5 \frac{\partial ^2[\sigma ( X(t_0))]}{\partial X^2} \sigma ( X(t_0))^2\text{ds} dz(\tau )$
Equation(9)
>
>
>
> Since all the terms are evaluated at $t_0$, they are constants and we can write the above integrals as
>
> $X(t)=X(t_0)+\mu (X(t_0)) \int_{t_0}^t   d\tau$
>
> $+\frac{\partial }{\partial X}[\mu ( X(t_0))]\mu (X(t_0)) \int_{t_0}^t \int_{t_0}^\tau  \text{ds} d\tau$
>
> $+ \frac{\partial }{\partial X}[\mu  (X(t_0))]\sigma (X(t_0)) \int_{t_0}^t \int_{t_0}^\tau \text{dz(s)} d\tau$
>
> $+0.5 \frac{\partial ^2[\mu ( X(t_0))]}{\partial X^2} \sigma ( X(t_0))^2 \int_{t_0}^t \int_{t_0}^\tau \text{ds} d\tau$
>
> $+\sigma(X(t_0))  \int _{t_0}^t dz(\tau )$
>
> $+\frac{\partial }{\partial X}[\sigma ( X(t_0))]\mu (X(t_0)) \int _{t_0}^t \int_{t_0}^\tau  \text{ds} dz(\tau )$
>
> $+\frac{\partial }{\partial X}[\sigma ( X(t_0))]\sigma (X(t_0))\int _{t_0}^t \int_{t_0}^\tau  dz(s ) dz(\tau )$
>
>
$+0.5 \frac{\partial ^2[\sigma ( X(t_0))]}{\partial X^2} \sigma ( X(t_0))^2\int_{t_0}^t \int_{t_0}^\tau  \text{ds} dz(\tau )$
Equation(10)
>
>
>
> The integrals of the kind$\int_{t_0}^t \int_{t_0}^\tau  \text{ds} d\tau$ ,
$\int_{t_0}^t \int_{t_0}^\tau \text{dz(s)} d\tau$ and$\int _{t_0}^t \int_{t_0}^\tau  dz(s ) dz(\tau )$ and other higher
order integrals can be very easily analytically solved for monte carlo. These integrals also commute. I will post a
monte carlo simulation code for CEV and lognormal process based on the above logic in a few days.
>
>
>
> If you like my above posts, I am looking for consulting and contract work and you could contact me for that at my
email anan2999(at)yahoo(dot)com
Take special case of (1) i.e. GBM SDE. Can you reproduce its analytic solution? It's a litmus test.

---

### #578 — Amin (Topic Author)
*January 5, 2018, 9:58 AM*

Here are a few(six) graphs for the CEV SDE dX(t)=epsilon X(t).^gamma dz(t) at time T years starting from X(0)=x0. These
graphs show the comparison of stochastic calculus of standard deviations(SCSD) density and the true density. I welcome
comments. I have used a predictor corrector version of my earlier post explaining the evolution of density in stochastic
calculus of standard deviations(SCSD)  method. In most of the graphs lines with true and SCSD method are so close that
it is difficult to see the green line.

![Image](https://s6.postimg.org/qicpsj3ch/Graph01.png)![Image](https://s6.postimg.org/gxt35ntg1/Graph02.png)![Image](https://s6.postimg.org/pstxg6py9/Graph03.png)![Image](https://s6.postimg.org/bz5kr552p/Graph04.png)![Image](https://s6.postimg.org/b9msesc8x/Graph05.png)![Image](https://s6.postimg.org/g8aatbvhd/Graph06.png)

---

### #579 — Amin (Topic Author)
*January 5, 2018, 10:09 AM*

> Take special case of (1) i.e. GBM SDE. Can you reproduce its analytic solution? It's a litmus test.
Daniel I posted a matlab program in post 566 that does exactly that. It makes a comparison of three densities. 1. true
density 2. method of iterated integrals density 3. Simple Euler method density. And I gave a large drift and large
volatility and people can see that 1st and 2nd densities are indistinguishable. For your review, I will soon be posting
a graphical comparison of the densities on this forum..

---

### #580 — Cuchulainn
*January 5, 2018, 12:21 PM*

> Take special case of (1) i.e. GBM SDE. Can you reproduce its analytic solution? It's a litmus test.
Daniel I posted a matlab program in post 566 that does exactly that. It makes a comparison of three densities. 1. true
density 2. method of iterated integrals density 3. Simple Euler method density. And I gave a large drift and large
volatility and people can see that 1st and 2nd densities are indistinguishable. For your review, I will soon be posting
a graphical comparison of the densities on this forum..
Thanks. I qualify: can your method  produce an **analytical solution** for GBM SDE as easily as the other approaches?

Reading MATLAB code gives me a headache. There is a insert code option ... use ...  in the tab bar.

That predictor-corrector.. how does it look like in **Latex algorithmic form**?

---

### #581 — Amin (Topic Author)
*January 5, 2018, 2:40 PM*

> Thanks. I qualify: can your method  produce an **analytical solution** for GBM SDE as easily as the other approaches?
>
>
As far as method of iterated integrals for SDEs is concerned, it is meant for monte carlo and not for analytic solution
though you could try analytical solution with a large number of iterated integral terms. It helps with monte carlo of
nonlinear equations where other methods do not work well. It handles non-linearity well.
> Reading MATLAB code gives me a headache. There is a insert code option ... use ...  in the tab bar.
>
>
>
> That predictor-corrector.. how does it look like in **Latex algorithmic form**?
I will soon be posting predictor-corrector version with the insert code option. Thank you for mentioning this.

---

### #582 — Cuchulainn
*January 5, 2018, 2:50 PM*

```
 P(1:N-1)=1;
[font=-apple-system, Helvetica Neue, Helvetica, sans-serif]    a=S0.^(2*(1-gamma))/((1-gamma).^2*epsilon.^2*t);[/font]
[font=-apple-system, Helvetica Neue, Helvetica, sans-serif]    b=1/(1-gamma);[/font]
[font=-apple-system, Helvetica Neue, Helvetica, sans-serif]   
c(1:N-1)=(.5*G(1:N-1)+.5*G(2:N)).^(2*(1-gamma))/((1-gamma).^2*epsilon.^2*t);[/font]
[font=-apple-system, Helvetica Neue, Helvetica, sans-serif]    if(gamma>=.5)[/font]
[font=-apple-system, Helvetica Neue, Helvetica, sans-serif]        P(:)=1-ncx2cdf(a,b,c(:));%Numerically generate
driftless CEV CDF[/font]
[font=-apple-system, Helvetica Neue, Helvetica, sans-serif]    else[/font]
[font=-apple-system, Helvetica Neue, Helvetica, sans-serif]        P(:)=ncx2cdf(c(:),2-b,a);%Numerically generate
driftless CEV CDF[/font]
[font=-apple-system, Helvetica Neue, Helvetica, sans-serif]    end[/font]
[font=-apple-system, Helvetica Neue, Helvetica, sans-serif]    for n=1:N-1[/font]

```

and then w/o generated font stuff

---

### #583 — Cuchulainn
*January 5, 2018, 2:58 PM*

```
P(1:N - 1) = 1;
a = S0. ^ (2 * (1 - gamma)) / ((1 - gamma). ^ 2 * epsilon. ^ 2 * t);
b = 1 / (1 - gamma);
c(1:N - 1) = (.5*G(1:N - 1) + .5*G(2:N)). ^ (2 * (1 - gamma)) / ((1 - gamma). ^ 2 * epsilon. ^ 2 * t);
if (gamma >= .5)
P(:) = 1 - ncx2cdf(a, b, c(:)); %Numerically generate driftless CEV CDF
else
P(:) = ncx2cdf(c(:), 2 - b, a); %Numerically generate driftless CEV CDF
end
for n = 1:N - 1
```

Imported via Visual Studio..

---

### #584 — Cuchulainn
*January 5, 2018, 3:12 PM*

*I will soon be posting predictor-corrector version with the insert code option*

In TEX is more readable. It has more added value for your cause.

BTW are you using the drift-corrected PC version?  I hope.

---

### #585 — Amin (Topic Author)
*January 8, 2018, 11:09 AM*

I would like to mention that the method also calculates the path integrals of functions of the diffusion on the same one
dimensional grid. So we could do Asian or Bermudan/American Asian options on one dimensional grid. It would also work
great for the derivatives that depend on path integrals of variance and other related variables.

If the diffusion is

dX(t)=mu(X(t)) dt +epsilon(X(t)) dz(t) Equation(1)

then we can easily on the same one dimensional grid calculate  the integrals of the kind

$\int _0^t f(X(t)) ds$   Equation(2)

$\int _0^t g(X(t))dz(s)$  Equation(3)

where f(.) and g(.) are two well behaved functions.

We can see that the integrals of the kind in equation (2) are very useful in calculating the derivatives that depend on
path integrals of some kind.

If somebody would want to offer a consulting project, I could help calculate all the above integrals that can be used
almost everywhere in computational finance. Please email me at anan2999(at)yahoo(dot)com

---

### #586 — Amin (Topic Author)
*January 10, 2018, 6:04 PM*

I will be posting a code for path integrals of diffusions with Asian options in a lognormal model as an example. I hope
to post the code some time over this weekend. This is very interesting and I am sure many friends would absolutely like
this new technique.

---

### #587 — Amin (Topic Author)
*January 15, 2018, 3:34 PM*

```
%Copyright Infiniti Derivatives Technologies, Lahore, Pakistan.
%www.infinitiderivatives.com
%Phone:+92-336-2602125
%email:[email protected], [email protected],
%[email protected]
%If you share interests in Mathematical Finance and Statistics I invite you
%to connect on skype using Skype ID: ahsan.amin2999
%I also invite you to connect on linkedin using email:[email protected]
%This program is only initial demonstration of Stochastic Calculus of
%Standard Deviations technology.
%A new and more comprehensive program will appear on
%Wilmott.com web site after the research paper is complete on SSRN.
% The SDE whose probability distribution is calculated
% is lognormal noise SDE.
%dX(t)=epsilon*X(t)*dz(t) with X(0)=x0;
%Xdt is the path integral of the above lognormal diffusion.
%For consulting and innovative work related to this new technology
%Please feel free to email me.
%In the program
%1st hermite polynomial is const/prob2;
%2nd hermite polynomial is (const2/prob2-1);
%third hermite polynomial is (const3/prob2-3*const/prob2);
%These are calculated using normal density.
%For accuracy with very high volatility and very long time frames, you will
%need to add another term in path integral SCSD analytics.
function [] = SDEXticsInfinitiTechnologiesLNAsian( )
X0_max=1000;%Total number of SD Fractions.
X0_mid=500.5;%Mid of the SD Grid. Lies at z0 by definition.
X0_mid0=500;
X0_start=1;
dX0=.01;%*8.0;%Width of SD cells in terms of Standard Deviations.
T_index=1200*1; %For 2 years.
dt=1/12.0/50;%hundredth of a month
t_T=1200/12/50;%%=2.0
epsilon=0.450;
gamma=1.0;
x0=1.0;
X(1:X0_max)=x0; %These are centres of lognormal diffusion subdivisions.
Xdt(1:X0_max)=0.0;%these are centres of path-integrals of lognormal diffusion.
z_t(1:X0_max)=0;
z_t0(1:X0_max)=0;
iivector(1:X0_max)=1:X0_max;
H11_1(1:X0_max)=0;
H11_2(1:X0_max)=0;
H11_3(1:X0_max)=0;
H11_4(1:X0_max)=0;
H5_1(1:X0_max)=0.0;
H5_2(1:X0_max)=0.0;
H5_3(1:X0_max)=0.0;
H5_4(1:X0_max)=0.0;
H5_5(1:X0_max)=0.0;
H5_6(1:X0_max)=0.0;
H5_7(1:X0_max)=0.0;
H5_8(1:X0_max)=0.0;
H6_1(1:X0_max)=0.0;
H6_2(1:X0_max)=0.0;
H6_3(1:X0_max)=0.0;
H6_4(1:X0_max)=0.0;
H6_5(1:X0_max)=0.0;
H6_6(1:X0_max)=0.0;
H6_7(1:X0_max)=0.0;
H6_8(1:X0_max)=0.0;
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
%prob2=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)*dX0;
prob2=normcdf(((iivector-X0_mid).*dX0)+.5*dX0)-normcdf(((iivector-X0_mid).*dX0)-.5*dX0);
prob0=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0);
for nn=1:T_index %Loop over time.
    t=(nn)*dt;
    t0=(nn-1)*dt;
    prob=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)/(sqrt(t)*epsilon); %Probability in each SD Grid cell.
    dt=t-t0;
    for mm=1:X0_max
        z_t0(mm)=sqrt(t0).*(const(mm)./prob2(mm));
        z_t(mm)=sqrt(t).*(const(mm)./prob2(mm));

        H11_1(mm)=(t.^1.5-t0.^1.5)/6.0.*(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm));
        H11_2(mm)=-(z_t(mm)-z_t0(mm)).*.5.*t0.*(const2(mm)./prob2(mm)-1.0);
        H11_3(mm)=-(z_t0(mm)).*.5.*(t-t0).*(const2(mm)./prob2(mm)-1.0);
        H11_4(mm)=(z_t(mm)-z_t0(mm)).*z_t0(mm).*z_t0(mm);

        H5_1(mm)=(const4(mm)./prob2(mm)-6*const2(mm)./prob2(mm)+3.0)./24*(t.^2.0-t0.^2.0);
        H5_2(mm)=-z_t0(mm).*(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm))*(t.^1.5-t0.^1.5)/6.0;
        H5_3(mm)=-(const2(mm)./prob2(mm)-1).*(const2(mm)./prob2(mm)-1).*t0/2.0.*(t-t0)/2.0;
        H5_4(mm)=z_t0(mm).^2.0.*(const2(mm)./prob2(mm)-1).*(t-t0)/2.0;
        H5_5(mm)=-(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm)).*t0.^1.5/6.0.*(z_t(mm)-z_t0(mm));
        H5_6(mm)=(const2(mm)./prob2(mm)-1).*t0/2.0.*z_t0(mm).*(z_t(mm)-z_t0(mm));
        H5_7(mm)=(const2(mm)./prob2(mm)-1).*t0/2.0.*z_t0(mm).*(z_t(mm)-z_t0(mm));
        H5_8(mm)=-(z_t(mm)-z_t0(mm)).*z_t0(mm).^3.0;

        H6_1(mm)=(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm))./sqrt(6*60).*(t.^2.5-t0.^2.5);
        H6_2(mm)=-z_t0(mm).*(const2(mm)./prob2(mm)-1)*(t.^2.0-t0.^2.0)/sqrt(24.0);
        H6_3(mm)=-(const2(mm)./prob2(mm)-1).*(const(mm)./prob2(mm)).*t0/2.0.*(t.^1.5-t0.^1.5)/sqrt(3.0);
        H6_4(mm)=z_t0(mm).^2.0.*(const(mm)./prob2(mm)).*(t.^1.5-t0.^1.5)/sqrt(3.0);
        H6_5(mm)=-(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm)).*t0.^1.5/6.0.*(t-t0);
        H6_6(mm)=(const2(mm)./prob2(mm)-1).*t0/2.0.*z_t0(mm).*(t-t0);
        H6_7(mm)=(const2(mm)./prob2(mm)-1).*t0/2.0.*z_t0(mm).*(t-t0);
        H6_8(mm)=-(t-t0).*z_t0(mm).^3.0;

        if(X(mm)>0.0)

            Xdt(mm)=Xdt(mm)+ ...
            X(mm).*dt+ ...
            X(mm).*epsilon.*(const(mm)./prob2(mm).*((t.^1.5-t0.^1.5)/sqrt(3)) +...
            -z_t0(mm).*(t-t0))+ ...
            X(mm)/1.0.*epsilon.^2.0.*( ...
            (const2(mm)./prob2(mm)-1).*(t.^2-t0.^2)/sqrt(24.0) ...
            -(const2(mm)./prob2(mm)-1).*(t0)/2.0.*(t-t0) ...
            -z_t0(mm).*const(mm)./prob2(mm).*(t.^1.5-t0.^1.5)/sqrt(3) ...
            +z_t0(mm).*z_t0(mm).*(t-t0))+ ...
           .5.*X(mm)/1.0.*epsilon.^3.0.*( ...
            (H6_1(mm)+H6_2(mm)+H6_3(mm)+H6_4(mm)+H6_5(mm)+H6_6(mm)+H6_7(mm)+H6_8(mm)));

            X(mm)=X(mm)+...
             epsilon.^1.*X(mm).^gamma.*(z_t(mm)-z_t0(mm)) ...
             +(1.0.*gamma.*X(mm).^(2*gamma-1)).* ...
            (((const2(mm)./prob2(mm)-1).*epsilon.^2.*(t-t0)*.5)- ...
              epsilon.^2.*z_t0(mm).*(z_t(mm)-z_t0(mm)))...
             +1.0.*gamma.*(2*gamma-1).*X(mm).^(3*gamma-2) ...
             .*(epsilon.^3.*H11_1(mm)+epsilon.^3.*H11_2(mm)+epsilon.^3*H11_3(mm)+epsilon.^3.0.*H11_4(mm)) ...
              +1*(6*gamma.^3-7*gamma.^2+2*gamma).*X(mm).^(4*gamma-3).*epsilon.^4.0 ...
              .*(H5_1(mm)+H5_2(mm)+H5_3(mm)+H5_4(mm)+H5_5(mm)+H5_6(mm)+H5_7(mm)+H5_8(mm));

        else
            X(mm)=0.0;
            for mmm=1:mm
                X(mmm)=0.0;
            end
        end

    end
end

effective_sigma=epsilon;
X(X0.0)
        %Jacobian_X(ii)=((X(ii-2))-8*(X(ii-1))+8*(X(ii+1))-(X(ii+2)))/(12*dX0*sqrt((T_index-1+1)*dt)*effective_sigma);
        Jacobian_X(ii)=((X(ii+1))-(X(ii-1)))/(2*dX0*sqrt((T_index)*dt)*effective_sigma);
        if(Jacobian_X(ii)~=0.0)
            Jacobian_X(ii)=abs(1/Jacobian_X(ii));
        end
    else
        Jacobian_X(ii)=0.0;
    end
%    if(Xdt(ii-1)>0.0)
            Jacobian_Xdt(ii)=((Xdt(ii+1))-(Xdt(ii-1)))/(2*dX0*sqrt((T_index)*dt)*effective_sigma);
        if(Jacobian_Xdt(ii)~=0.0)
            Jacobian_Xdt(ii)=abs(1/Jacobian_Xdt(ii));

        else
            Jacobian_Xdt(ii)=0.0;
        end
%        Jacobian_Xdt(ii)=0.0;
%    end
end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Calculation of Analytic lognormal density below
n=0;
N=1000;
TT=T_index*dt;
sigma0=epsilon;
X_0=x0;
mu0=0.0;
for n=1:N
    n=n+1
    Z(n)=n*.01;
    Logf(n)=1.0/sqrt(2*pi)/Z(n)./(sigma0*sqrt(TT)).* ...
    exp(-.5*(log(Z(n))-log(X_0)-(mu0-.5*sigma0.^2)*TT).^2./(sigma0.^2*TT));
end
% Monte Carlo Follows for the calculation of lognormal SDE and its path integral.
% the density of this monte carlo path integral is later graphically compared with
% SCSD path integral.
paths=1000000;
Y1(1:paths)=x0;
Y1dt(1:paths)=0.0;
T_index0=T_index/10;
dt0=dt*10;
for nn=1:T_index0 %Loop over time.
    Random0=randn(size(Y1));
    %Stochastic integrals follow
    dZn=Random0*sqrt(dt0);
    dZndZn(1:paths)=dt0/2.0.*(Random0.^2-1);

    %Y=Y+mu0.*Y*dt+sigma0*Y.*dZn; %Discretization of traditional Monte Carlo
    Y1dt=Y1dt+.5*Y1.*dt0;

    Y1=Y1+sigma0*Y1.*dZn ... %%Discretization of Iterated Integral
    +sigma0.*sigma0.*Y1.*dZndZn;
    Y1dt=Y1dt+.5*Y1.*dt0;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
MaxCutOff=15;
BinSize=.01;
[Y1dtDensity,IndexOutY1dt,IndexMaxY1dt] = MakeDensityFromSimulation_Infiniti(Y1dt,paths,BinSize,MaxCutOff );
%[XDensity1,IndexOutX1,IndexMaxX1] = MakeDensityFromSimulation_Infiniti(X1,paths,BinSize,MaxCutOff );

plot(IndexOutY1dt(1:IndexMaxY1dt),Y1dtDensity(1:IndexMaxY1dt),'g', ...
    (Xdt(X0_start+2:X0_max-2)),prob(X0_start+2:X0_max-2).*Jacobian_Xdt(X0_start+2:X0_max-2),'r');
title('Graph of path integral of lognormal diffusion')
ylabel('Density of Path integral')
legend('Green Line=Monte Carlo Density','Red Line = SCSD density')

%Xdt array contains centres of path integral density subdivisions.
% Z(1:2000),Logf(1:2000),'k')
%Xdt
Xdt_avg=sum(Xdt.*prob2)  %mean of SCSD path integral density
Y1dt_avg=sum(Y1dt)/paths %mean of numerically calculated path integral density
%Jacobian_Xdt
str=input('look at overlaid Graph comparison of true density of path integral of SDE(green line) with density of SDE
path integral generated from SCSD analytic method(red line)>');

X_avg=sum(X.*prob2) % mean of lognomral SDE
X_avg0=sum(X.*prob0.*dX0)% mean of lognomral SDE

%ylabel('Change in Asset Price')
plot(Z(1:N-1),Logf(1:N-1),'g',(X(X0_start+2:X0_max-2)),prob(X0_start+2:X0_max-2).*Jacobian_X(X0_start+2:X0_max-2),'r')
%X array contains centres of SDE density subdivisions.
title('Graph of lognormal density')
ylabel('Density of lognormal SDE Process')
legend('Green Line=Analytic Density','Red Line = SCSD density')
str=input('look at overlaid Graph comparison of true density of SDE(green line) with density of SDE generated from SCSD
analytic method(red line)>');
end

```

I have posted the code for density of path integral of lognormal distribution and compared it with density of path
integral calculated using monte carlo. The program has not been optimized in anyway and careful optimization will make
it an order of magnitude faster. Please note that present run time also includes brute force monte carlo. Here is
another code for function that you will need for above function.

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
if(Xmin>real(X(p)))
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

When you run the program, you will get the following 1st output.

Xdt_avg =

   1.999825915399553

Y1dt_avg =

   1.999747705398276

---

### #588 — Amin (Topic Author)
*January 20, 2018, 4:52 PM*

In the previous post, I gave a graphical comparison of path integrals of lognormal diffusion with Monte carlo and my new
method. I did not explicitly price the Asian options. Here I post a new program in which I have explicitly priced Asian
options and compared the new method Asian option price with monte carlo price. Here is the code for that

```
%Copyright Infiniti Derivatives Technologies, Lahore, Pakistan.
%www.infinitiderivatives.com
%Phone:+92-336-2602125
%email:[email protected], [email protected],
%[email protected]
%If you share interests in Mathematical Finance and Statistics I invite you
%to connect on skype using Skype ID: ahsan.amin2999
%I also invite you to connect on linkedin using email:[email protected]
%This program is only initial demonstration of Stochastic Calculus of
%Standard Deviations technology.
%A new and more comprehensive program will appear on
%Wilmott.com web site after the research paper is complete on SSRN.
% The SDE whose probability distribution is calculated
% is lognormal noise SDE.
%dX(t)=epsilon*X(t)*dz(t) with X(0)=x0;
%Xdt is the path integral of the above lognormal diffusion.
%For consulting and innovative work related to this new technology
%Please feel free to email me.
%In the program
%1st hermite polynomial is const/prob2;
%2nd hermite polynomial is (const2/prob2-1);
%third hermite polynomial is (const3/prob2-3*const/prob2);
%These are calculated using normal density.
%For accuracy with very high volatility and very long time frames, you will
%need to add another term in path integral SCSD analytics.
function [] = SDEXticsInfinitiTechnologiesLNAsian02( )
X0_max=1000;%Total number of SD Fractions.
X0_mid=500.5;%Mid of the SD Grid. Lies at z0 by definition.
X0_mid0=500;
X0_start=1;
dX0=.01;%*8.0;%Width of SD cells in terms of Standard Deviations.
T_index=1200*1; %For 2 years.
dt=1/12.0/50;%hundredth of a month
Tt=1200/12/50;%%=2.0
epsilon=0.450;
gamma=1.0;

x0=1.0;
AsianStrike=x0;
X(1:X0_max)=x0; %These are centres of lognormal diffusion subdivisions.
Xdt(1:X0_max)=0.0;%these are centres of path-integrals of lognormal diffusion.
z_t(1:X0_max)=0;
z_t0(1:X0_max)=0;
iivector(1:X0_max)=1:X0_max;
H11_1(1:X0_max)=0;
H11_2(1:X0_max)=0;
H11_3(1:X0_max)=0;
H11_4(1:X0_max)=0;
H5_1(1:X0_max)=0.0;
H5_2(1:X0_max)=0.0;
H5_3(1:X0_max)=0.0;
H5_4(1:X0_max)=0.0;
H5_5(1:X0_max)=0.0;
H5_6(1:X0_max)=0.0;
H5_7(1:X0_max)=0.0;
H5_8(1:X0_max)=0.0;
H6_1(1:X0_max)=0.0;
H6_2(1:X0_max)=0.0;
H6_3(1:X0_max)=0.0;
H6_4(1:X0_max)=0.0;
H6_5(1:X0_max)=0.0;
H6_6(1:X0_max)=0.0;
H6_7(1:X0_max)=0.0;
H6_8(1:X0_max)=0.0;
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
%prob2=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)*dX0;
prob2=normcdf(((iivector-X0_mid).*dX0)+.5*dX0)-normcdf(((iivector-X0_mid).*dX0)-.5*dX0);
prob0=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0);
for nn=1:T_index %Loop over time.
    t=(nn)*dt;
    t0=(nn-1)*dt;
    prob=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)/(sqrt(t)*epsilon); %Probability in each SD Grid cell.
    dt=t-t0;
    for mm=1:X0_max
        z_t0(mm)=sqrt(t0).*(const(mm)./prob2(mm));
        z_t(mm)=sqrt(t).*(const(mm)./prob2(mm));
        H11_1(mm)=(t.^1.5-t0.^1.5)/6.0.*(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm));
        H11_2(mm)=-(z_t(mm)-z_t0(mm)).*.5.*t0.*(const2(mm)./prob2(mm)-1.0);
        H11_3(mm)=-(z_t0(mm)).*.5.*(t-t0).*(const2(mm)./prob2(mm)-1.0);
        H11_4(mm)=(z_t(mm)-z_t0(mm)).*z_t0(mm).*z_t0(mm);

        H5_1(mm)=(const4(mm)./prob2(mm)-6*const2(mm)./prob2(mm)+3.0)./24*(t.^2.0-t0.^2.0);
        H5_2(mm)=-z_t0(mm).*(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm))*(t.^1.5-t0.^1.5)/6.0;
        H5_3(mm)=-(const2(mm)./prob2(mm)-1).*(const2(mm)./prob2(mm)-1).*t0/2.0.*(t-t0)/2.0;
        H5_4(mm)=z_t0(mm).^2.0.*(const2(mm)./prob2(mm)-1).*(t-t0)/2.0;
        H5_5(mm)=-(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm)).*t0.^1.5/6.0.*(z_t(mm)-z_t0(mm));
        H5_6(mm)=(const2(mm)./prob2(mm)-1).*t0/2.0.*z_t0(mm).*(z_t(mm)-z_t0(mm));
        H5_7(mm)=(const2(mm)./prob2(mm)-1).*t0/2.0.*z_t0(mm).*(z_t(mm)-z_t0(mm));
        H5_8(mm)=-(z_t(mm)-z_t0(mm)).*z_t0(mm).^3.0;

        H6_1(mm)=(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm))./sqrt(6*60).*(t.^2.5-t0.^2.5);
        H6_2(mm)=-z_t0(mm).*(const2(mm)./prob2(mm)-1)*(t.^2.0-t0.^2.0)/sqrt(24.0);
        H6_3(mm)=-(const2(mm)./prob2(mm)-1).*(const(mm)./prob2(mm)).*t0/2.0.*(t.^1.5-t0.^1.5)/sqrt(3.0);
        H6_4(mm)=z_t0(mm).^2.0.*(const(mm)./prob2(mm)).*(t.^1.5-t0.^1.5)/sqrt(3.0);
        H6_5(mm)=-(const3(mm)./prob2(mm)-3*const(mm)./prob2(mm)).*t0.^1.5/6.0.*(t-t0);
        H6_6(mm)=(const2(mm)./prob2(mm)-1).*t0/2.0.*z_t0(mm).*(t-t0);
        H6_7(mm)=(const2(mm)./prob2(mm)-1).*t0/2.0.*z_t0(mm).*(t-t0);
        H6_8(mm)=-(t-t0).*z_t0(mm).^3.0;
        if(X(mm)>0.0)
            Xdt(mm)=Xdt(mm)+ ...
            X(mm).*dt+ ...
            X(mm).*epsilon.*(const(mm)./prob2(mm).*((t.^1.5-t0.^1.5)/sqrt(3)) +...
            -z_t0(mm).*(t-t0))+ ...
            X(mm)/1.0.*epsilon.^2.0.*( ...
            (const2(mm)./prob2(mm)-1).*(t.^2-t0.^2)/sqrt(24.0) ...
            -(const2(mm)./prob2(mm)-1).*(t0)/2.0.*(t-t0) ...
            -z_t0(mm).*const(mm)./prob2(mm).*(t.^1.5-t0.^1.5)/sqrt(3) ...
            +z_t0(mm).*z_t0(mm).*(t-t0))+ ...
           1*.5.*X(mm)/1.0.*epsilon.^3.0.*( ...
            (H6_1(mm)+H6_2(mm)+H6_3(mm)+H6_4(mm)+H6_5(mm)+H6_6(mm)+H6_7(mm)+H6_8(mm)));

            X(mm)=X(mm)+...
             epsilon.^1.*X(mm).^gamma.*(z_t(mm)-z_t0(mm)) ...
             +(1.0.*gamma.*X(mm).^(2*gamma-1)).* ...
            (((const2(mm)./prob2(mm)-1).*epsilon.^2.*(t-t0)*.5)- ...
              epsilon.^2.*z_t0(mm).*(z_t(mm)-z_t0(mm)))...
             +1.0.*gamma.*(2*gamma-1).*X(mm).^(3*gamma-2) ...
             .*(epsilon.^3.*H11_1(mm)+epsilon.^3.*H11_2(mm)+epsilon.^3*H11_3(mm)+epsilon.^3.0.*H11_4(mm)) ...
              +1*(6*gamma.^3-7*gamma.^2+2*gamma).*X(mm).^(4*gamma-3).*epsilon.^4.0 ...
              .*(H5_1(mm)+H5_2(mm)+H5_3(mm)+H5_4(mm)+H5_5(mm)+H5_6(mm)+H5_7(mm)+H5_8(mm));
        else
            X(mm)=0.0;
            for mmm=1:mm
                X(mmm)=0.0;
            end
        end
    end
end
effective_sigma=epsilon;
X(X0.0)
        %Jacobian_X(ii)=((X(ii-2))-8*(X(ii-1))+8*(X(ii+1))-(X(ii+2)))/(12*dX0*sqrt((T_index-1+1)*dt)*effective_sigma);
        Jacobian_X(ii)=((X(ii+1))-(X(ii-1)))/(2*dX0*sqrt((T_index)*dt)*effective_sigma);
        if(Jacobian_X(ii)~=0.0)
            Jacobian_X(ii)=abs(1/Jacobian_X(ii));
        end
         Jacobian_XAsian(ii)=((Xdt(ii+1)-Xdt(ii-1))/Tt)/(2*dX0*sqrt((T_index)*dt)*effective_sigma);
         if(Jacobian_XAsian(ii)~=0.0)
             Jacobian_XAsian(ii)=abs(1/Jacobian_XAsian(ii));
         end
    else
        Jacobian_X(ii)=0.0;
    end
%    if(Xdt(ii-1)>0.0)
            Jacobian_Xdt(ii)=((Xdt(ii+1))-(Xdt(ii-1)))/(2*dX0*sqrt((T_index)*dt)*effective_sigma);
        if(Jacobian_Xdt(ii)~=0.0)
            Jacobian_Xdt(ii)=abs(1/Jacobian_Xdt(ii));
        else
            Jacobian_Xdt(ii)=0.0;
        end
%        Jacobian_Xdt(ii)=0.0;
%    end
end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Calculation of Analytic lognormal density below
n=0;
N=1000;
TT=T_index*dt;
sigma0=epsilon;
X_0=x0;
mu0=0.0;
for n=1:N
    n=n+1
    Z(n)=n*.01;
    Logf(n)=1.0/sqrt(2*pi)/Z(n)./(sigma0*sqrt(TT)).* ...
    exp(-.5*(log(Z(n))-log(X_0)-(mu0-.5*sigma0.^2)*TT).^2./(sigma0.^2*TT));
end
% Monte Carlo Follows for the calculation of lognormal SDE and its path integral.
% the density of this monte carlo path integral is later graphically compared with
% SCSD path integral.
paths=10000000;
Y1(1:paths)=x0;
Y1dt(1:paths)=0.0;
T_index0=T_index/10;
dt0=dt*10;
Tt=T_index0*dt0;
for nn=1:T_index0 %Loop over time.
    Random0=randn(size(Y1));
    %Stochastic integrals follow
    dZn=Random0*sqrt(dt0);
    dZndZn(1:paths)=dt0/2.0.*(Random0.^2-1);
    Y1dt=Y1dt+.5*Y1.*dt0;
    Y1=Y1+sigma0*Y1.*dZn ... %%Discretization of Iterated Integral
    +sigma0.*sigma0.*Y1.*dZndZn;
    Y1dt=Y1dt+.5*Y1.*dt0;
end
AsianPriceMC=0.0;
for pp=1:paths
    if(Y1dt(pp)/Tt>AsianStrike)
        AsianPriceMC=AsianPriceMC+(Y1dt(pp)/Tt-AsianStrike)/paths;
    end
end
    probXAsian(1:X0_max)=0.0;
    XAsianSubDivStart(1:X0_max)=0.0;
    XAsianSubDivEnd(1:X0_max)=0.0;
 AsianPriceX=0.0;
for ii=2:X0_max-2
    probXAsian(ii)=prob(ii).*Jacobian_XAsian(ii);
    XAsianSubDivStart(ii)=.5*(Xdt(ii)+Xdt(ii-1))./Tt;
    XAsianSubDivEnd(ii)=.5*(Xdt(ii)+Xdt(ii+1))./Tt;
    if((XAsianSubDivStart(ii)=AsianStrike))

       AsianPriceX=AsianPriceX+1*probXAsian(ii).*(XAsianSubDivEnd(ii)-AsianStrike) ...
           .*(.5*XAsianSubDivEnd(ii)+.5*AsianStrike-AsianStrike);
    end
    if((XAsianSubDivStart(ii)>=AsianStrike)&&(XAsianSubDivEnd(ii)>AsianStrike))
        AsianPriceX=AsianPriceX+(Xdt(ii)/Tt-AsianStrike) ...
            .*probXAsian(ii).*(XAsianSubDivEnd(ii)-XAsianSubDivStart(ii));
    end
end
%Tt
%sum(prob2)
AsianPriceX
AsianPriceMC
str=input('look at Asian Price from monte carlo (AsianPriceMC) and Asian Price from our method (AsianPriceX)>');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
MaxCutOff=15;
BinSize=.01;
[Y1dtDensity,IndexOutY1dt,IndexMaxY1dt] = MakeDensityFromSimulation_Infiniti(Y1dt,paths,BinSize,MaxCutOff );
%[XDensity1,IndexOutX1,IndexMaxX1] = MakeDensityFromSimulation_Infiniti(X1,paths,BinSize,MaxCutOff );
    plot(IndexOutY1dt(1:IndexMaxY1dt),Y1dtDensity(1:IndexMaxY1dt),'g', ...
    (Xdt(X0_start+2:X0_max-2)),prob(X0_start+2:X0_max-2).*Jacobian_Xdt(X0_start+2:X0_max-2),'r');
title('Graph of path integral of lognormal diffusion')
ylabel('Density of Path integral')
legend('Green Line=Monte Carlo Density','Red Line = SCSD density')
%Xdt array contains centres of path integral density subdivisions.
% Z(1:2000),Logf(1:2000),'k')
%Xdt
Xdt_avg=sum(Xdt.*prob2)  %mean of SCSD path integral density
Y1dt_avg=sum(Y1dt)/paths %mean of numerically calculated path integral density
%Jacobian_Xdt
str=input('look at overlaid Graph comparison of true density of path integral of SDE(green line) with density of SDE
path integral generated from SCSD analytic method(red line)>');
X_avg=sum(X.*prob2) % mean of lognomral SDE
X_avg0=sum(X.*prob0.*dX0)% mean of lognomral SDE
%ylabel('Change in Asset Price')
plot(Z(1:N-1),Logf(1:N-1),'g',(X(X0_start+2:X0_max-2)),prob(X0_start+2:X0_max-2).*Jacobian_X(X0_start+2:X0_max-2),'r')
%X array contains centres of SDE density subdivisions.
title('Graph of lognormal density')
ylabel('Density of lognormal SDE Process')
legend('Green Line=Analytic Density','Red Line = SCSD density')
str=input('look at overlaid Graph comparison of true density of SDE(green line) with density of SDE generated from SCSD
analytic method(red line)>');
end

```

Here is the first output from the above program.

AsianPriceX =

   0.146180152855722

AsianPriceMC =

   0.145136738204934

---

### #589 — Cuchulainn
*January 21, 2018, 3:31 PM*

Comparing your solution to the MC price may be less convincing to comparison against (quasi) exact solutions. Haug 2007
has a number of examples.

---

### #590 — Billy7
*January 21, 2018, 4:36 PM*

I could give an "exact" solution to this, if I understood the inputs. Is it supposed to be continuous averaging, or
discrete with 120, or 1200 averaging fixings? Either way both prices above seem approximately correct. The question is
how long does it take.

---

### #591 — Cuchulainn
*January 21, 2018, 4:51 PM*

> I could give an "exact" solution to this, if I understood the inputs. Is it supposed to be continuous averaging, or
discrete with 120, or 1200 averaging fixings? Either way both prices above seem approximately correct. The question is
how long does it take.
Very god suggestion.

An interesting project is automatic stress testing for a range of randomly generated input parameters (to remove
cognitive bias).

---

### #592 — Amin (Topic Author)
*January 21, 2018, 6:54 PM*

I am not actively working on this research project and spend a few hours every weekend on this. As I had earlier
mentioned that I did not optimize the matlab routine at all. Once it is optimized for speed, it would be very fast. In
my code example, I have given the solution to the simplest path integral possible. The method can tackle some of the
most difficult path integrals that we encounter in mathematics and physics and which could not be easily calculated
earlier.

I am working most of the time on algorithmic trading as my attempts at getting some consulting opportunity related to
this research have not succeeded.

---

### #593 — Billy7
*January 21, 2018, 7:11 PM*

Well, if I were you I would try to sell it like this: Go into the trouble of optimizing simple examples like that and
then say: "My method calculates the price of an Asian option in 10ms, whereas a PDE method takes 200ms, MC takes 1 sec,
a tree takes 100 ms for the same accuracy."  And do it as Cuchulainn says for a wide range of inputs. You need to give
concrete examples showing your method is at least as efficient (and robust) as the existing ones. Either for simple
problems like this one, or for more complicated ones. That may get people interested.

---

### #594 — Cuchulainn
*January 21, 2018, 8:19 PM*

And documenting it in standardised format (begin=midele-end). etc. etc.

random e.g.

http://www.math.ku.dk/~rolf/KlassenBinomial.pdf

Make it easy for people.

---

### #595 — Amin (Topic Author)
*January 21, 2018, 8:25 PM*

Here is a quickly optimized version of the matlab program for calculating path integrals of lognormal model.

```
%Copyright Infiniti Derivatives Technologies, Lahore, Pakistan.
%www.infinitiderivatives.com
%Phone:+92-336-2602125
%email:[email protected], [email protected],
%[email protected]
%If you share interests in Mathematical Finance and Statistics I invite you
%to connect on skype using Skype ID: ahsan.amin2999
%I also invite you to connect on linkedin using email:[email protected]
%This program is only initial demonstration of Stochastic Calculus of
%Standard Deviations technology.
%A new and more comprehensive program will appear on
%Wilmott.com web site after the research paper is complete on SSRN.
% The SDE whose probability distribution is calculated
% is lognormal noise SDE.
%dX(t)=epsilon*X(t)*dz(t) with X(0)=x0;
%Xdt is the path integral of the above lognormal diffusion.
%For consulting and innovative work related to this new technology
%Please feel free to email me.
%In the program
%1st hermite polynomial is const/prob2;
%2nd hermite polynomial is (const2/prob2-1);
%third hermite polynomial is (const3/prob2-3*const/prob2);
%These are calculated using normal density.
%For accuracy with very high volatility and very long time frames, you will
%need to add another term in path integral SCSD analytics.
function [] = SDEXticsInfinitiTechnologiesLNAsian02( )

tic
X0_max=500;%Total number of SD Fractions.
X0_mid=250.5;%Mid of the SD Grid. Lies at z0 by definition.
X0_mid0=250;
X0_start=1;
dX0=.01*5.0/2.50;%*8.0;%Width of SD cells in terms of Standard Deviations.
T_index=300*1; %For 2 years.
dt=1/12.0/25;%hundredth of a month
Tt=300/12/25;%%=2.0
epsilon=0.450;
gamma=1.0;

x0=1.0;
AsianStrike=x0;
X(1:X0_max)=x0; %These are centres of lognormal diffusion subdivisions.
Xdt(1:X0_max)=0.0;%these are centres of path-integrals of lognormal diffusion.
z_t(1:X0_max)=0;
z_t0(1:X0_max)=0;
iivector(1:X0_max)=1:X0_max;
H11_1(1:X0_max)=0;
H11_2(1:X0_max)=0;
H11_3(1:X0_max)=0;
H11_4(1:X0_max)=0;
H5_1(1:X0_max)=0.0;
H5_2(1:X0_max)=0.0;
H5_3(1:X0_max)=0.0;
H5_4(1:X0_max)=0.0;
H5_5(1:X0_max)=0.0;
H5_6(1:X0_max)=0.0;
H5_7(1:X0_max)=0.0;
H5_8(1:X0_max)=0.0;
H6_1(1:X0_max)=0.0;
H6_2(1:X0_max)=0.0;
H6_3(1:X0_max)=0.0;
H6_4(1:X0_max)=0.0;
H6_5(1:X0_max)=0.0;
H6_6(1:X0_max)=0.0;
H6_7(1:X0_max)=0.0;
H6_8(1:X0_max)=0.0;
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
%prob2=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)*dX0;
prob2=normcdf(((iivector-X0_mid).*dX0)+.5*dX0)-normcdf(((iivector-X0_mid).*dX0)-.5*dX0);
prob0=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0);
Q1=const./prob2;
Q2=(const2./prob2-1);
Q3=(const3./prob2-3.*const./prob2);
Q4=(const4./prob2-6*const2./prob2+3.0);
for nn=1:T_index %Loop over time.
    t=(nn)*dt;
    t0=(nn-1)*dt;
    prob=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)/(sqrt(t)*epsilon); %Probability in each SD Grid cell.
    dt=t-t0;
    t_sqrt=sqrt(t);
    t0_sqrt=sqrt(t0);
    t0_15=t0.^1.5;
    t_15=t.^1.5;
    t0_20=t0.^2.0;
    t_20=t.^2.0;
    t0_25=t0.^2.5;
    t_25=t.^2.5;
    epsilon_2=epsilon.*epsilon;
    epsilon_3=epsilon_2.*epsilon;
    epsilon_4=epsilon_3.*epsilon;
    for mm=1:X0_max
        z_t0(mm)= t0_sqrt.*Q1(mm);
        z_t(mm)=t_sqrt.*Q1(mm);
        H11_1(mm)=(t_15-t0_15)/6.0.*Q3(mm);
        H11_2(mm)=-(z_t(mm)-z_t0(mm)).*.5.*t0.*Q2(mm);
        H11_3(mm)=-(z_t0(mm)).*.5.*(dt).*(Q2(mm));
        H11_4(mm)=(z_t(mm)-z_t0(mm)).*z_t0(mm).*z_t0(mm);

        H5_1(mm)=Q4(mm)./24*(t_20-t0_20);
        H5_2(mm)=-z_t0(mm).*(Q3(mm))*(t_15-t0_15)/6.0;
        H5_3(mm)=-(Q2(mm)).*(Q2(mm)).*t0/2.0.*(dt)/2.0;
        H5_4(mm)=z_t0(mm).^2.0.*(Q2(mm)).*(dt)/2.0;
        H5_5(mm)=-(Q3(mm)).*t0_15/6.0.*(z_t(mm)-z_t0(mm));
        H5_6(mm)=(Q2(mm)).*t0/2.0.*z_t0(mm).*(z_t(mm)-z_t0(mm));
        H5_7(mm)=(Q2(mm)).*t0/2.0.*z_t0(mm).*(z_t(mm)-z_t0(mm));
        H5_8(mm)=-(z_t(mm)-z_t0(mm)).*z_t0(mm).^3.0;

        H6_1(mm)=(Q3(mm))./sqrt(6*60).*(t_25-t0_25);
        H6_2(mm)=-z_t0(mm).*(Q2(mm))*(t_20-t0_20)/sqrt(24.0);
        H6_3(mm)=-(Q2(mm)).*(Q1(mm)).*t0/2.0.*(t_15-t0_15)/sqrt(3.0);
        H6_4(mm)=z_t0(mm).^2.0.*(Q1(mm)).*(t_15-t0_15)/sqrt(3.0);
        H6_5(mm)=-(Q3(mm)).*t0_15/6.0.*(dt);
        H6_6(mm)=(Q2(mm)).*t0/2.0.*z_t0(mm).*(dt);
        H6_7(mm)=(Q2(mm)).*t0/2.0.*z_t0(mm).*(dt);
        H6_8(mm)=-(dt).*z_t0(mm).^3.0;
        if(X(mm)>0.0)
            Xdt(mm)=Xdt(mm)+ ...
            X(mm).*dt+ ...
            X(mm).*epsilon.*(Q1(mm).*((t_15-t0_15)/sqrt(3)) +...
            -z_t0(mm).*(dt))+ ...
            X(mm)/1.0.*epsilon_2.*( ...
            Q2(mm).*(t_20-t0_20)/sqrt(24.0) ...
            -(Q2(mm)).*(t0)/2.0.*(dt) ...
            -z_t0(mm).*const(mm)./prob2(mm).*(t_15-t0_15)/sqrt(3) ...
            +z_t0(mm).*z_t0(mm).*(dt))+ ...
           1*.5.*X(mm)/1.0.*epsilon_3.*( ...
            (H6_1(mm)+H6_2(mm)+H6_3(mm)+H6_4(mm)+H6_5(mm)+H6_6(mm)+H6_7(mm)+H6_8(mm)));

            X(mm)=X(mm)+...
             epsilon.*X(mm).^gamma.*(z_t(mm)-z_t0(mm)) ...
             +(1.0.*gamma.*X(mm).^(2*gamma-1)).* ...
            (((Q2(mm)).*epsilon_2.*(dt)*.5)- ...
              epsilon_2.*z_t0(mm).*(z_t(mm)-z_t0(mm)))...
             +1.0.*gamma.*(2*gamma-1).*X(mm).^(3*gamma-2) ...
             .*epsilon_3.*(H11_1(mm)+H11_2(mm)+H11_3(mm)+H11_4(mm)) ...
              +1*(6*gamma.^3-7*gamma.^2+2*gamma).*X(mm).^(4*gamma-3).*epsilon_4 ...
              .*(H5_1(mm)+H5_2(mm)+H5_3(mm)+H5_4(mm)+H5_5(mm)+H5_6(mm)+H5_7(mm)+H5_8(mm));
        else
            X(mm)=0.0;
            for mmm=1:mm
                X(mmm)=0.0;
            end
        end
    end
end

%str=input('look at Elapsed time');
effective_sigma=epsilon;
X(X0.0)
        %Jacobian_X(ii)=((X(ii-2))-8*(X(ii-1))+8*(X(ii+1))-(X(ii+2)))/(12*dX0*sqrt((T_index-1+1)*dt)*effective_sigma);
        Jacobian_X(ii)=((X(ii+1))-(X(ii-1)))/(2*dX0*sqrt((T_index)*dt)*effective_sigma);
        if(Jacobian_X(ii)~=0.0)
            Jacobian_X(ii)=abs(1/Jacobian_X(ii));
        end
         Jacobian_XAsian(ii)=((Xdt(ii+1)-Xdt(ii-1))/Tt)/(2*dX0*sqrt((T_index)*dt)*effective_sigma);
         if(Jacobian_XAsian(ii)~=0.0)
             Jacobian_XAsian(ii)=abs(1/Jacobian_XAsian(ii));
         end
    else
        Jacobian_X(ii)=0.0;
    end
%    if(Xdt(ii-1)>0.0)
            Jacobian_Xdt(ii)=((Xdt(ii+1))-(Xdt(ii-1)))/(2*dX0*sqrt((T_index)*dt)*effective_sigma);
        if(Jacobian_Xdt(ii)~=0.0)
            Jacobian_Xdt(ii)=abs(1/Jacobian_Xdt(ii));
        else
            Jacobian_Xdt(ii)=0.0;
        end
%        Jacobian_Xdt(ii)=0.0;
%    end
end
AsianPriceMC=0.0;
    probXAsian(1:X0_max)=0.0;
    XAsianSubDivStart(1:X0_max)=0.0;
    XAsianSubDivEnd(1:X0_max)=0.0;
 AsianPriceX=0.0;
for ii=2:X0_max-2
    probXAsian(ii)=prob(ii).*Jacobian_XAsian(ii);
    XAsianSubDivStart(ii)=.5*(Xdt(ii)+Xdt(ii-1))./Tt;
    XAsianSubDivEnd(ii)=.5*(Xdt(ii)+Xdt(ii+1))./Tt;
    if((XAsianSubDivStart(ii)=AsianStrike))

       AsianPriceX=AsianPriceX+1*probXAsian(ii).*(XAsianSubDivEnd(ii)-AsianStrike) ...
           .*(.5*XAsianSubDivEnd(ii)+.5*AsianStrike-AsianStrike);
       AsianPriceX=AsianPriceX+1*probXAsian(ii).*(XAsianSubDivEnd(ii)-AsianStrike) ...
           .*(.5*XAsianSubDivEnd(ii)+.5*AsianStrike-AsianStrike);
    end
    if((XAsianSubDivStart(ii)>=AsianStrike)&&(XAsianSubDivEnd(ii)>AsianStrike))
        AsianPriceX=AsianPriceX+(Xdt(ii)/Tt-AsianStrike) ...
            .*probXAsian(ii).*(XAsianSubDivEnd(ii)-XAsianSubDivStart(ii));
    end
end
toc
str=input('look at Elapsed time');
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Calculation of Analytic lognormal density below
n=0;
N=1000;
TT=T_index*dt;
sigma0=epsilon;
X_0=x0;
mu0=0.0;
for n=1:N
    n=n+1
    Z(n)=n*.01;
    Logf(n)=1.0/sqrt(2*pi)/Z(n)./(sigma0*sqrt(TT)).* ...
    exp(-.5*(log(Z(n))-log(X_0)-(mu0-.5*sigma0.^2)*TT).^2./(sigma0.^2*TT));
end
% Monte Carlo Follows for the calculation of lognormal SDE and its path integral.
% the density of this monte carlo path integral is later graphically compared with
% SCSD path integral.
paths=1000000;
Y1(1:paths)=x0;
Y1dt(1:paths)=0.0;
T_index0=T_index/1;
dt0=dt*1;
Tt=T_index0*dt0;
for nn=1:T_index0 %Loop over time.
    Random0=randn(size(Y1));
    %Stochastic integrals follow
    dZn=Random0*sqrt(dt0);
    dZndZn(1:paths)=dt0/2.0.*(Random0.^2-1);
    Y1dt=Y1dt+.5*Y1.*dt0;
    Y1=Y1+sigma0*Y1.*dZn ... %%Discretization of Iterated Integral
    +sigma0.*sigma0.*Y1.*dZndZn;
    Y1dt=Y1dt+.5*Y1.*dt0;
end
for pp=1:paths
    if(Y1dt(pp)/Tt>AsianStrike)
        AsianPriceMC=AsianPriceMC+(Y1dt(pp)/Tt-AsianStrike)/paths;
    end
end

%Tt
%sum(prob2)
AsianPriceX
AsianPriceMC
str=input('look at Asian Price from monte carlo (AsianPriceMC) and Asian Price from our method (AsianPriceX)>');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
MaxCutOff=15;
BinSize=.01;
[Y1dtDensity,IndexOutY1dt,IndexMaxY1dt] = MakeDensityFromSimulation_Infiniti(Y1dt,paths,BinSize,MaxCutOff );
%[XDensity1,IndexOutX1,IndexMaxX1] = MakeDensityFromSimulation_Infiniti(X1,paths,BinSize,MaxCutOff );
    plot(IndexOutY1dt(1:IndexMaxY1dt),Y1dtDensity(1:IndexMaxY1dt),'g', ...
    (Xdt(X0_start+2:X0_max-2)),prob(X0_start+2:X0_max-2).*Jacobian_Xdt(X0_start+2:X0_max-2),'r');
title('Graph of path integral of lognormal diffusion')
ylabel('Density of Path integral')
legend('Green Line=Monte Carlo Density','Red Line = SCSD density')
%Xdt array contains centres of path integral density subdivisions.
% Z(1:2000),Logf(1:2000),'k')
%Xdt
Xdt_avg=sum(Xdt.*prob2)  %mean of SCSD path integral density
Y1dt_avg=sum(Y1dt)/paths %mean of numerically calculated path integral density
%Jacobian_Xdt
str=input('look at overlaid Graph comparison of true density of path integral of SDE(green line) with density of SDE
path integral generated from SCSD analytic method(red line)>');
X_avg=sum(X.*prob2) % mean of lognomral SDE
X_avg0=sum(X.*prob0.*dX0)% mean of lognomral SDE
%ylabel('Change in Asset Price')
plot(Z(1:N-1),Logf(1:N-1),'g',(X(X0_start+2:X0_max-2)),prob(X0_start+2:X0_max-2).*Jacobian_X(X0_start+2:X0_max-2),'r')
%X array contains centres of SDE density subdivisions.
title('Graph of lognormal density')
ylabel('Density of lognormal SDE Process')
legend('Green Line=Analytic Density','Red Line = SCSD density')
str=input('look at overlaid Graph comparison of true density of SDE(green line) with density of SDE generated from SCSD
analytic method(red line)>');
end

```

In matlab when I have not used any vector format for loops and made all loops serial, the program takes .15 seconds for
one year Asian option. Matlab is known to be slow for loops when serial calculations are used. Written in C++, it would
be far faster by about 5 to ten times..

---

### #596 — Billy7
*January 21, 2018, 9:09 PM*

Well, that's more info but I still don't know if that's for continuous monitoring or discrete. Can the method do both
easily? For example in Monte Carlo you cannot directly find the continuous monitored price (as far as I know), but you
can run one with say 50 averaging dates, then one with 100 and extrapolate. Doing that using Sobol sequences I get an
extrapolated price of 0.14513 in 0.15secs (65K+65K paths), 0.14516 in  0.3 secs (131K+131K paths) . This is parallelized
but the PC is 9 yrs old. The correct cont.monitored price is 0.145199. Can it do American exercise? How long would that
take? People would need to see a few test cases like that well presented.

---

### #597 — Amin (Topic Author)
*January 22, 2018, 4:45 PM*

1. It is like continuous monitoring. 240 averaging dates per year.

2. It can easily handle larger discrete monitoring dates.

3. The method is parallelizable.

4. can easily handle American options.

5. You can find transition probability between any two points in time in the asset space and also in the path integral
space.

6. You can easily calculate the greeks on the same grid.

7. You can easily specify the term structure of volatility.

8. You can handle barriers. Or barriers with American option.

On the negative side

1. There is an error of around 10bp in two year continuously monitored Asian option with 45% vol. I get .1462 for the
two year option for which your value is: 1451. Since this error is more or less constant and would scale with vol, you
could have a good idea about such biases for a particular date. You could easily correct for it.

2. We might not be able to price options with maturity greater than 5 years because of increasing error.

---

### #598 — Cuchulainn
*January 22, 2018, 7:31 PM*

You use 'can'; what does it mean exactly?

e.g. getting (4) into an ODE! How does it go? A few lines to explain. I have no idea how to shove a free boundary into
an ODE.

---

### #599 — Amin (Topic Author)
*January 22, 2018, 7:45 PM*

I have not priced American options but I am very sure that they can be handled with a bit of hack. The reason is that
transition probabilities are exactly known and a backward algorithm can easily be implemented on the same grid on which
we have calculated  the forward evolution of the probability density.

---

### #600 — Cuchulainn
*January 22, 2018, 7:55 PM*

> I have not priced American options but I am very sure that they can be handled with a bit of hack.
How?

4. can easily handle American options.

??? throw us some crumbs to give us an idea.

---

[← Previous](page_011.md) | [Index](index.md) | [Next →](page_013.md)
