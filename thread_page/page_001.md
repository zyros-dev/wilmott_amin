# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 1 of 59** — Posts #1–#50

[Index](index.md) | [Next →](page_002.md)

---

### #1 — Amin (Topic Author)
*April 17, 2016, 12:24 PM*

**(broken latex: Unbalanced $$: 1)**

```latex
I will try to give wilmott friends an idea about my new research on stochastic differential equations and their
simulation. My formal research paper will be ready in a week but I will present some preview details about the research
for the friends for discussion.Let us write a simple stochastic differential equation in the general form with a finite
step here as$x(t)=\int _0^t\mu (x(t)) \text{dt}+\int _0^t\sigma (x(t)) \text{dz}(t)\text{     }\text{Eq (1)}$ When we
simulate the above stochastic differential equation, the simplest method is to freeze the drift and volatility
coefficients at their initial value, and multiply with dt and Normal(sqrt(t)) as
$x(t)=\mu (x(0)) \text{dt}+\sigma (x(0)) \text{sqrt}(t)z.$ Though many better techniques exist to simulate the
stochastic differential equations for a finite step or to find their density, most of them lack generalization and have
to be applied in special settings. We derive a generic new method that can simulate even non-linear stochastic
differential equations to arbitrary accuracy. The method is extremely simple and is based on the simple understanding of
how the non-linear coefficient functions are changing in time. I have tried to give some intuition about it in the
exposition below.Before, we embark on a full-fledged scheme for the above general SDE, we would like to give the reader
some crucial insights. To give the proper insights, we would like to start by taking a normal diffusion so that we could
proceed in a step by step manner$\text{dx}(s)=\sigma  \text{dz}(s)$ Eq(2)or$x(t)=x(0)+\int _0^t\sigma  \text{dz}(s)$
Eq(3)We would like to start by learning how to calculate the following time integral with extreme precision and
arbitrary accuracy$I(t)=\int _0^t\mu (x(s)) \text{ds}$ Eq(4)We would also like to explain how to calculate the following
stochastic integral with extreme precision and arbitrary accuracy$S(t)=\int _0^t\sigma (x(s)) \text{dz}(s)$ Eq(5)Since
we want to proceed step by step, we will first calculate these integrals for a normal brownian motion as given in Eq (2)
and after gaining intuition , we later generalize the SDE from Eq(2) to Eq(1) and calculate I(t) and S(t) with the most
general dynamics as given by Eq(1).We start by calculating I(t) as given by Eq(4) and Eq(2).
$\int _0^t\mu (x(s))\text{ds}=t \mu (x(t)) -\int _0^ts d[\mu (x(s))]$ Eq(6)Expanding the second term on RHS
$\int _0^ts d[\mu (x(s))]=\int _0^t \frac{\partial \mu (x(s))}{\partial x}s\sigma\text{dz}(s)+.5\int _0^t \frac{\partial ^2\mu (x(s))}{\partial x^2}s\sigma ^2 \text{ds}$
Eq(7)We know that$\frac{\partial \mu (x(s))}{\partial x}$ in first term of Eq(7) is a function of x(s) and we can apply
Ito Change of variable formula on this as
$\frac{\partial \mu (x(s))}{\partial x}=\frac{\partial \mu (x(0))}{\partial x}+\int _0^s \frac{\partial ^2\mu (x(u))}{\partial x^2}\sigma\text{dz}(u)+.5\int _0^s \frac{\partial ^3\mu (x(u))}{\partial x^3}\sigma ^2 \text{du}$
Eq(8)Now we come to the most important step towards understanding of this expansion. We expand the first noise term on
RHS of Eq(7) by substituting Eq(8) in it.
$\int _0^t \frac{\partial \mu (x(s))}{\partial x}s\sigma\text{dz}(s)=\int _0^t \frac{\partial \mu (x(0))}{\partial x}s\sigma\text{dz}(s)+\int _0^t s \sigma\text{dz}(s)\int _0^s \frac{\partial ^2\mu (x(u))}{\partial x^2}\sigma\text{dz}(u) +\int _0^t s\sigma\text{dz}(s)\int _0^s .5 \frac{\partial ^3\mu (x(u))}{\partial x^3}\sigma ^2 \text{du}\text{  }$
Eq(9)So we have a few nested integrals and we can easily deal with them. We could continue the expansions of
$\frac{\partial ^2\mu (x(u))}{\partial x^2}$ and$\frac{\partial ^3\mu (x(u))}{\partial x^3}$ to further order just by
following Eq(8) but we stop the order here for initial simplicity and explanation of the basic example. We freeze
$\frac{\partial ^2\mu (x(u))}{\partial x^2}$ and$\frac{\partial ^3\mu (x(u))}{\partial x^3}$ in the above equation to
their initial time zero values (we could have continued to expand them to desired accuracy if we wished) and write Eq(9)
as
$\int _0^t \frac{\partial \mu (x(s))}{\partial x}s\sigma\text{dz}(s)=\frac{\partial \mu (x(0))}{\partial x}\int _0^t s\sigma\text{dz}(s)+\frac{\partial ^2\mu (x(0))}{\partial x^2}\int _0^t s \sigma\text{dz}(s)\int _0^s \sigma\text{dz}(u) +.5 \frac{\partial ^3\mu (x(0))}{\partial x^3}\int _0^t s\sigma\text{dz}(s)\int _0^s \sigma ^2 \text{du}\text{  }$
Eq(10)Now we are left to evaluation of intgrals$\int _0^t \text{s}\sigma\text{dz}(s)$ Eq(11)and double nested integrals
$\int _0^t s \sigma\text{dz}(s)\int _0^s \sigma\text{dz}(u)=\int _0^t s \sigma ^2\text{  }(z(s)-z(0))\text{dz}(s)$
$\int _0^t s\sigma\text{dz}(s)\int _0^s \sigma ^2 \text{du}=\int _0^t s\sigma  \left(\left.\sigma ^2 s\right)\text{dz}(s)\right.$
None of the above nested integrals vanishes and their continuations do not go to zero. I have devised schemes in my
research that can calculate all different types of above integrals with arbitrary complexity of nesting to perfect
precision using very simple integral calculus in a form that is a function of only time t, and a unit gaussian.We would
similarly expand the second term of Eq(7) on RHS using Ito expansion of$\frac{\partial ^2\mu (x(s))}{\partial x^2}$ and
substituting it in Eq(7) . We will freeze the coefficients of above expansion at time zero like we did to get Eq(10) and
get different integrals like Eq(11-13). All these stochastic integrals can be trivially solved by scheme I have devised
in my research.To be continued tomorrow. Sorry, tired of writing more at the moment.
```

---

### #2 — list1
*April 17, 2016, 12:49 PM*

It might be you lost term x ( 0 ) on the right hand side (1). The simplest discrete scheme is Euler's one. You can find
a stepwise approximation of the solution of the nonlinear SDE. You can present$\Delta t$ order convergence of the
approximate to exact solution. Your scheme looks to be assigned to only first step on [ 0 ,$\Delta t$ ] interval. In
other words you should make first a stepwise recurrent continuation of the finite scheme on arbitrary interval [0 , T ].
Next it looks reasonable to present estimate$(\Delta t )^n$ of the convergence of the approximate solution to exact
solution.

---

### #3 — Amin (Topic Author)
*April 17, 2016, 12:55 PM*

QuoteOriginally posted by: list1It might be you lost term x ( 0 ) on the right hand side (1). Sorry it is a
mistake.Quote Your scheme looks to be assigned to only first step on [ 0 ,$\Delta t$ ] interval. In other words you
should make first a stepwise recurrent continuation of the finite scheme on arbitrary interval [0 , T ].No it is totally
general. Once you understand my logic, you can easily work out the mathematics.

---

### #4 — Cuchulainn
*April 17, 2016, 1:03 PM*

Quoteperfect precision There is no such thing as perfect precision in (numerical) mathematics. Accuracy is a polynomial
function of dt based on continuity of the unknown exact solution. Which is what @list has also said, when I look at it.
Is convergence monotonic?

---

### #5 — list1
*April 17, 2016, 2:25 PM*

QuoteOriginally posted by: AminQuoteOriginally posted by: list1It might be you lost term x ( 0 ) on the right hand side
(1). Sorry it is a mistake.Quote Your scheme looks to be assigned to only first step on [ 0 ,$\Delta t$ ] interval. In
other words you should make first a stepwise recurrent continuation of the finite scheme on arbitrary interval [0 , T
].No it is totally general. Once you understand my logic, you can easily work out the mathematics.In all equation s you
used 0 on the low bounds of the integral besides you used x ( 0 ) in eq (10). It suggests that you consider only first
step on finite time partition$ { t\,_k } $ of the arbitrary interval [ 0 , T ]. You should consider a partition of the [
0 , T ] and then to apply your method on each subinterval$ [\, t\,_k , t\,_{k + 1}\, ) $

---

### #6 — pcaspers
*April 17, 2016, 2:58 PM*

QuoteOriginally posted by: CuchulainnQuoteperfect precision There is no such thing as perfect precision in (numerical)
mathematics. Accuracy is a polynomial function of dt based on continuity of the unknown exact solution. Which is what
@list has also said, when I look at it. Is convergence monotonic?why do you put "numerical" in brackets, makes me
nervous

---

### #7 — Cuchulainn
*April 17, 2016, 3:08 PM*

QuoteOriginally posted by: pcaspersQuoteOriginally posted by: CuchulainnQuoteperfect precision There is no such thing as
perfect precision in (numerical) mathematics. Accuracy is a polynomial function of dt based on continuity of the unknown
exact solution. Which is what @list has also said, when I look at it. Is convergence monotonic?why do you put
"numerical" in brackets, makes me nervousGood point. I was thinking that someone gives a closed/exact solution which
they might think is perfectly precise until you want numbers:)

---

### #8 — Amin (Topic Author)
*April 19, 2016, 12:32 PM*

In the previous post, I mentioned a general technique of expanding stochastic integrals in a way that we can utilize
higher derivatives(than the two derivatives of stochastic integrals as is the current best practice) in evaluation of
stochastic integrals and in simulation . We can continue to take higher derivatives, and freeze the derivatives in the
tail at their zero value and later evaluate the stochastic integrals composed merely of z(t) and t and expand them in
powers of standard normal N(0,1) and a function of time and volatility.I will mention a caveat that in following
exposition normal SDE is$z(t)=z(0)+\int _0^t\sigma  \text{dz}(s)$ I will explain with some basic examples how nested
integrals mentioned in the previous post can be trivially simulated with perfect accuracy to any length of time. The
detailed evaluation methodology will follow in a later post.$\int _0^t \text{s}\sigma\text{dz}(s)$ Eq(11)can be
simulated as$\int _0^t \text{s}\sigma\text{dz}(s)=\frac{2.175}{\sqrt{2\text{Pi}}}\sigma  \frac{t^{1.5}}{1.5} N(0,1)$
where N(0,1) indicates a single standard normal draw in simulation.
$\int _0^t z(s)\text{ds}=z(0)t+\frac{2.175}{\sqrt{2\text{Pi}}}\sigma  \frac{t^{1.5}}{1.5} N(0,1)$ We give another
general simulation expansion as
$\int _0^t z(s)\sigma\text{dz}(s)=\frac{2.5}{\sqrt{2\text{Pi}}}z(0)\sigma \sqrt{t}N(0,1) +.5\frac{2.5}{\sqrt{2\text{Pi}}}\sigma ^2t\text{  }N(0,1)^2-.5\sigma ^2t $
The above simulation for the stochastic integral is valid for any length of time as is the case with simulation of all
other nested integrals that I will mention. For example, the above simulation equation can be simply verified by most
members of the forum by setting up a simulation in 5-10 minutes. Similarly taking Equation 12 in the first post, we have
a stepping technique that remains perfectly accurate for all time horizons.C1, C2, C3 in the below are fixed constants.
$\int _0^t s \sigma\text{dz}(s)\int _0^s \sigma\text{dz}(u)=\int _0^t s \sigma \text{  }(z(s)-z(0))\text{dz}(s)=.5 \text{C2} \sigma ^2\frac{t ^2}{2} N(0,1)^2-.5\sigma ^2\frac{t^2}{2}$
while the general version of above integral can be solved as
$\int _0^t s \sigma \text{  }z(s)\text{dz}(s)=\text{C1} z(0)\sigma  \frac{t^{1.5}}{1.5}N(0,1)+.5 \text{C2} \sigma ^2\frac{t ^2}{2} N(0,1)^2-.5\sigma ^2\frac{t^2}{2}$
I give the last integral for today here as
$\int _0^t s\sigma\text{dz}(s)\int _0^s \sigma ^2 \text{du}=\int _0^t s\sigma  \left(\left.\sigma ^2 s\right)\text{dz}(s)\right.$
Eq(13)which can be simulated as
$\int _0^t s\sigma\text{dz}(s)\int _0^s \sigma ^2 \text{du}=\int _0^t s\sigma  \left(\left.\sigma ^2 s\right)\text{dz}(s)=.5 \text{C3} \sigma ^3\frac{t^{2.5}}{2.5}N(0,1)\right.$
Most friends would have realized that in a complex simulation we can put together the coefficients of powers of standard
Normal and simply multiply those coefficients with the N(0,1) powers and add to get the result.

---

### #9 — list1
*April 19, 2016, 7:32 PM*

Amin , your formulas might make sense only for [ 0 , t ] where t is a small number. There are a large number of
approaches have been developed in the theory of SDEs for the construction of the DISCRETE time approximations of the
SDEs solutions. It might make sense to look through them and might be contact to some of the authors introducing yours
approach.

---

### #10 — Amin (Topic Author)
*April 20, 2016, 1:54 AM*

list1, please read what I have stated. These formulas are valid for all time. Please do not give any comments out of
your usual intuition. I will accept your comments if you have spent 5 minutes in setting up a small simulation to test
my formulas and then say something meaningful about the results you got. Now do not write a word here without setting up
the simulation. You will be most welcome to comment after you have actually done that.

---

### #11 — Cuchulainn
*April 20, 2016, 6:32 AM*

QuoteOriginally posted by: Aminlist1, please read what I have stated. These formulas are valid for all time. Please do
not give any comments out of your usual intuition. I will accept your comments if you have spent 5 minutes in setting up
a small simulation to test my formulas and then say something meaningful about the results you got. Now do not write a
word here without setting up the simulation. You will be most welcome to comment after you have actually done that.Wrong
answer IMO. Imagine if you said that at a training session. That's the way @Quantigic reacts.list has a point. It is up
to the author to prove the benefits of a new method, not the reader! All we see is a number of equations which (at least
for me) have to be taken on blind faith.Take a concrete case would be a good idea. And where can these formulae be
used?If the author spends 5 minutes => save the 90K forum members each spending 5 minutes.  Quotewe can put together the
coefficients of powers of standard Normal and simply multiply those coefficients with the N(0,1) powers and add to get
the result.I wonder how this pans out.   I smell a series..

---

### #12 — list1
*April 20, 2016, 7:44 AM*

It might be I am wrong but let check your approximation in a trivial case $\mu\,=\, 0\, , \, \sigma\,=\,1$ and t = 10.

---

### #13 — Amin (Topic Author)
*April 20, 2016, 8:29 AM*

Sorry about being a bit curt. Thank you cuch for your suggestion. I am quickly pasting the code for one example integral
zdz. Please copy it in your matlab editor or simply clone in any other language. As I have set up the simulation, you
can trivially modify the simple monte carlo using equations I gave in previous post vs how we traditionally do an
accurate short stepping monte carlo. Excuse any possible minor errors as I am not being formal. @Cuch and others, your
feedback is requested.
$\int _0^t z(s)\sigma\text{dz}(s)=\frac{2.5}{\sqrt{2\text{Pi}}}z(0)\sigma \sqrt{t}N(0,1) +.5\frac{2.5}{\sqrt{2\text{Pi}}}\sigma ^2t\text{  }N(0,1)^2-.5\sigma ^2t $
Here is the main function.function [] = SDE_Compare_Zintegrals_Infiniti_public( )s1 = RandStream('mt19937ar');
RandStream.setDefaultStream(s1); savedState = s1.State;
z0=1;%z0=10;%z0=.5;sigma0=0.710%sigma0=0.710/4%sigma0=0.710*4T_index=200; %T_index=2000; %T_index=20;
dt=.005/1.0;T=(T_index)*dt;paths=1000000; zz(1:paths)=z0; I2(1:paths)=0.0;%integral zdz over time by traditional short
stepped monte carlo.zzT(1:paths)=0.0;%One step integral zdz calculated by my method for nn=1:T_index %Loop over time.
t=(nn)*dt; t2=(nn-1)*dt; Random1=randn(size(zz)); RandTemp1=Random1.*sqrt(dt); I2=I2+(RandTemp1*sigma0).*(zz); zz = zz
+RandTemp1*sigma0; end %My One Step method calculation starts Random1=randn(size(zzT));
zzT=z0*sigma0.*Random1*T.^.5*2.5/sqrt(2*pi)+... %Excuse the coefficients 2.5/sqrt(2pi). It is unity. I followed as I
wrote on internet. Please modify. .5*sigma0.^2* Random1.^2.*T*2.5/sqrt(2*pi)-... .5*sigma0.^2.*T; I2_avg=sum(I2)./paths
zzT_avg=sum(zzT)./paths I2_avg2=sum(abs(I2))./paths zzT_avg2=sum(abs(zzT))./pathsBinSize=.05;%Here you can change the
resolution of monte carlo density. You might have to look at the graph and if it is jagged and noisy, increase the bin
sizeMaxCutOff=1000;%Max cut off is a value given to density generation program. [XDensity,IndexOutX,IndexMaxX] =
MakeDensityFromSimulation_Infiniti(I2,paths,BinSize,MaxCutOff );[XDensity2,IndexOutX2,IndexMaxX2] =
MakeDensityFromSimulation_Infiniti(zzT,paths,BinSize,MaxCutOff );
plot(IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'g',IndexOutX2(1:IndexMaxX2),XDensity2(1:IndexMaxX2),'r')
str=input('look at overlaid Graph comparison of traditional Monte carlo density of zdz(green line) with density of SDE
generated from one step monte carlo method(red line)>'); endHere is the helper function to graph from monte
carlofunction [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti(X,Paths,BinSize,MaxCutOff )%Processes
monte carlo paths to return a series Xdensity as a function of IndexOut. IndexMax is the maximum value of index.%
Xmin=0; Xmax=0; for p=1:Paths if(X(p)>MaxCutOff) X(p)=MaxCutOff; end if(Xmin>real(X(p))) Xmin=real(X(p)); end
if(XmaxIndexMax) index=IndexMax; end XDensity(index)=XDensity(index)+1.0/Paths/BinSize; end
IndexOut(1:IndexMax)=Xmin+(0:(IndexMax-1))*BinSize; end

---

### #14 — Cuchulainn
*April 20, 2016, 8:34 AM*

Amin,I would be interested in testing your formula in a 1-factor MC option pricer. if possible, could you delineate the
steps? Thx.

---

### #15 — Amin (Topic Author)
*April 20, 2016, 8:41 AM*

Yes, Cuch, I will post it here for a lognormal option pricer or CEV option pricer.  But please give me two or three days
since I am busy working out a few last details of the method and its derivation. I hope you do not mind a few days. In
the meantime, you could play around with the integrals I mentioned in the previous post using the matlab code I pasted.

---

### #16 — Cuchulainn
*April 20, 2016, 8:58 AM*

No problem.

---

### #17 — list1
*April 20, 2016, 10:23 AM*

QuoteOriginally posted by: list1It might be I am wrong but let check your approximation in a trivial case
$\mu\,=\, 0\, , \, \sigma\,=\,1$ and t = 10.Your eq eq should be of the type
$ x \,(\, 10\, ) \,=\,  x \,(\, 0\, ) \,+ \int_0^{10}\,dz\,(\,s\,)\,\,=\,\, x \,(\, 0\, ) \,+ \,z\,(\,10\,) $ Can we
apply your formulas to present approximation of the x ( 10 ) ?

---

### #18 — Cuchulainn
*April 20, 2016, 10:42 AM*

QuoteOriginally posted by: list1QuoteOriginally posted by: list1It might be I am wrong but let check your approximation
in a trivial case$\mu\,=\, 0\, , \, \sigma\,=\,1$ and t = 10.Your eq eq should be of the type
$ x \,(\, 10\, ) \,=\,  x \,(\, 0\, ) \,+ \int_0^{10}\,dz\,(\,s\,)\,\,=\,\, x \,(\, 0\, ) \,+ \,z\,(\,10\,) $ Can we
apply your formulas to present approximation of the x ( 10 ) ?How does this compare against solution using Ito formula?
====Kloeden and Platen have a bunch of explicitly solvable SDE pages 118-126.

---

### #19 — amike
*April 20, 2016, 10:43 AM*

For your example there is also a handy exact integral: $$\int_0^t z_t dz_t=\frac{1}{2}(z_t^2-t)$ $, so you may want to
explain how/if your result agrees with it...

---

### #20 — list1
*April 20, 2016, 1:32 PM*

QuoteOriginally posted by: list1QuoteOriginally posted by: list1It might be I am wrong but let check your approximation
in a trivial case$\mu\,=\, 0\, , \, \sigma\,=\,1$ and t = 10.Your eq eq should be of the type
$ x \,(\, 10\, ) \,=\,  x \,(\, 0\, ) \,+ \int_0^{10}\,dz\,(\,s\,)\,\,=\,\, x \,(\, 0\, ) \,+ \,z\,(\,10\,) $ Can we
apply your formulas to present approximation of the x ( 10 ) ?My idea was for the explicit exact function x ( 10 ) given
above to apply Amin's formulas. It should be first whether these formulas are correct. Second as Amin's formulas
contained z ( 0 ) that probably is equal to 0 if z is a Wiener process then the same type of approximation on [ 5 , 10 ]
with x ( 5 ) as initial data present better approximation of x ( 10 ) value of original eq (1). This observation
suggests that in case if formulas are correct to use partition of the [ 0 , T ] and apply Amin's formulas on each
subinterval. When the length of max interval tends to 0 we should arrive at exact solution. In original scheme formulas
are attached to the interval [ 0 , t ], t > 0. It is difficult to call it approximation as there is there is no
parameter which specifies convergence approximation to exact sde solution. Situation is similar to say y = sin x and y =
$x^3$ on [ - 1 , 1 ]. These are different functions though on a small interval [ - h , h ] one can be considered as an
approximation of other.

---

### #21 — Amin (Topic Author)
*April 20, 2016, 4:26 PM*

QuoteOriginally posted by: list1QuoteOriginally posted by: list1QuoteOriginally posted by: list1It might be I am wrong
but let check your approximation in a trivial case$\mu\,=\, 0\, , \, \sigma\,=\,1$ and t = 10.Your eq eq should be of
the type$ x \,(\, 10\, ) \,=\,  x \,(\, 0\, ) \,+ \int_0^{10}\,dz\,(\,s\,)\,\,=\,\, x \,(\, 0\, ) \,+ \,z\,(\,10\,) $
Can we apply your formulas to present approximation of the x ( 10 ) ?My idea was for the explicit exact function x ( 10
) given above to apply Amin's formulas. It should be first whether these formulas are correct. Second as Amin's formulas
contained z ( 0 ) that probably is equal to 0 if z is a Wiener process then the same type of approximation on [ 5 , 10 ]
with x ( 5 ) as initial data present better approximation of x ( 10 ) value of original eq (1). This observation
suggests that in case if formulas are correct to use partition of the [ 0 , T ] and apply Amin's formulas on each
subinterval. When the length of max interval tends to 0 we should arrive at exact solution. In original scheme formulas
are attached to the interval [ 0 , t ], t > 0. It is difficult to call it approximation as there is there is no
parameter which specifies convergence approximation to exact sde solution. Situation is similar to say y = sin x and y =
$x^3$ on [ - 1 , 1 ]. These are different functions though on a small interval [ - h , h ] one can be considered as an
approximation of other.I have presented a graphical comparison of two densities. One derived by short stepping monte
carlo and the other derived from one step monte carlo. I am a bit busy, so I cannot spare time to give anything better
at the moment. It should be enough to tell you, if you play with the program, how good my method is. If there is a
mismatch between densities, it is mostly due to problems with short-stepping traditional monte carlo. If you graph
densities of sin(x) and x3, you should be able to detect the difference if you are smart enough. As I said, this is the
best I can do today to set up a small simulation of two densities for you so you can compare for yourself.

---

### #22 — Amin (Topic Author)
*April 23, 2016, 4:29 PM*

For the interest of friends I will post slightly modified version of the previous program that computes the integral of
tzdz  or t(z-z0)dz by putting z0=0. If my one step method has a different shape, it is more accurate than the shape of
density from very short stepping method. You can look at mean and second moment numbers that they match very well. You
will need the helper matlab function from previous post to plot the density. I will be posting a full fledged simulation
of CEV model option pricing program in 2-4 days. function [] = SDE_Compare_Zintegrals_Infiniti_public02( )
s1 = RandStream('mt19937ar');RandStream.setDefaultStream(s1);savedState = s1.State;
z0=4;%z0=0;%z0=10;%z0=.5;sigma0=.710/2;%sigma0=0.710/4%sigma0=0.710*4T_index=400;%
00; %T_index=2000; %T_index=20;
dt=.005/1.0;T=(T_index)*dt;paths=1000000; zz(1:paths)=z0; I2(1:paths)=0.0;%integral tzdz                         over
time by traditional short stepped monte carlo.
zzT(1:paths)=0.0;%One step integral tzdz calculated by my method for nn=1:T_index %Loop over time.t=(nn)*dt;
t2=(nn-1)*dt; Random1=randn(size(zz)); RandTemp1=Random1.*sqrt(dt);I2=I2+t2*(RandTemp1*sigma0).*(zz);zz = zz
+RandTemp1*sigma0;end%My One Step method calculation startsRandom1=randn(size(zzT));
zzT=z0*sigma0.*Random1*T.^1.5*.5760+...sigma0.^2*
Random1.^2.*T.^2*sqrt(2).*(1/4)-....5*sigma0.^2.*T.^2*(1/2)*sqrt(2);I2_avg=sum(I2)./pathszzT_avg=sum(zzT)./pathsI2_avg2=sum(abs(I2))./pathszzT_avg2=sum(abs(zzT))./paths%%Below
are second moments. To see if both are matchedI2_var=sum(I2.^2)./pathszzT_var=sum(zzT.^2)./pathsBinSize=.01;%Here you
can change the resolution of monte carlo density. You might have to look at the graph and if it is jagged and noisy,
increase the bin sizeMaxCutOff=1000;%Max cut off is a value given to density generation program.
[XDensity,IndexOutX,IndexMaxX] = MakeDensityFromSimulation_Infiniti(I2,paths,BinSize,MaxCutOff
);[XDensity2,IndexOutX2,IndexMaxX2] = MakeDensityFromSimulation_Infiniti(zzT,paths,BinSize,MaxCutOff
);plot(IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'g',IndexOutX2(1:IndexMaxX2),XDensity2(1:IndexMaxX2),'r')str=input('look
at overlaid Graph comparison of traditional Monte carlo density of zdz(green line) with density of SDE generated from
one step monte carlo method(red line)>');end

---

### #23 — Amin (Topic Author)
*April 24, 2016, 4:04 AM*

Though I just gave a detailed scheme for a double nested dz integral, many intelligent and smart mathematicians would
have guessed that a doubly nested dz integral can be described in terms of hermite polynomials of degree up to 2 and
similarly the integrals with nesting degree 3 could be described in terms of hermite polynomials of degree three and
less and so on for higher degree of nesting.  Of course, you have to make adjustments due to volatility and time
multipliers that affect the total variance.

---

### #24 — Amin (Topic Author)
*April 24, 2016, 6:46 AM*

For a reference to above formulas with nested dz-integrals when you have calculated the appropriate variance, you can
calculate them by a slight modification after following the reference below."Brownian Motion and Stochastic Calculus" by
Karatzas and Shreve. You have to follow the Exercise 3.31 on page 167.

---

### #25 — Cuchulainn
*April 24, 2016, 10:40 AM*

QuoteOriginally posted by: AminFor a reference to above formulas with nested dz-integrals when you have calculated the
appropriate variance, you can calculate them by a slight modification after following the reference below."Brownian
Motion and Stochastic Calculus" by Karatzas and Shreve. You have to follow the Exercise 3.31 on page 167.This is a
well-known technique in engineering.. the book by Ghanem and Spanos expands on this topic.On a related topic, instead of
integral we can use Karhunen Loeve expansion and transform SDE into a random ODE. I have discretize eq (6) by hand
(predictor correct as in Kloeden+Platen) and using the Boost ODE solver in combination with Monte Carlo. I get results
that are better than the known FD schemes for SDE.RODEThe point is that the uncountable measure space has been replaced
by a countable(and then truncated) Fourier expansion in eqs. (2) and (26). N.B. we have to solve it as a Stratonovich
corrected drift function.

---

### #26 — Amin (Topic Author)
*April 24, 2016, 2:20 PM*

Cuch, you are right. How well known the techniques is in applied literature, I do not know but if you read my first post
in the thread, you will realize that we can do a much high order monte carlo than existing practices. Most of the
integrals involve simple and basic arithmetic with a minor application of integral calculus. If you take high enough
order in expansion of drift and volatility part of SDE, you could do a 5yr monte carlo with desired accuracy in just one
step. In the context of my first post, this technique has never been applied to monte carlo before. My upcoming paper
also has a portion devoted to very interesting applications of Girsanov theorem to non-linear SDEs with drift.

---

### #27 — Cuchulainn
*April 24, 2016, 2:44 PM*

QuoteOriginally posted by: AminCuch, you are right. How well known the techniques is in applied literature, I do not
know but if you read my first post in the thread, you will realize that we can do a much high order monte carlo than
existing practices. Most of the integrals involve simple and basic arithmetic with a minor application of integral
calculus. If you take high enough order in expansion of drift and volatility part of SDE, you could do a 5yr monte carlo
with desired accuracy in just one step. In the context of my first post, this technique has never been applied to monte
carlo before. My upcoming paper also has a portion devoted to very interesting applications of Girsanov theorem to
non-linear SDEs with drift.Amin,Unfortunately, I don't speak Matlab, so I will need to rely on a math/pseudo-code for
the algorithm. I would say write up the stuff _in detail_ so that we can all have a go (writing Matlab does not
count).thanks

---

### #28 — Amin (Topic Author)
*April 24, 2016, 4:01 PM*

Ok Cuch, I will try to write a C++ code for you because that is what I will do myself finally. A word of caution,
Karatzas and Shreve reference I mentioned will have to be slightly modified but you could see that different nested
integrals in our case remain orthogonal to each other which is probably the only requirement for a general application.

---

### #29 — Cuchulainn
*April 24, 2016, 4:09 PM*

Ok, but a precise description of the algorithm is enough.

---

### #30 — Amin (Topic Author)
*April 24, 2016, 4:59 PM*

QuoteOriginally posted by: CuchulainnOk, but a precise description of the algorithm is enough.Yes, I will try to explain
that in detail.QuoteOriginally posted by: AminA word of caution, Karatzas and Shreve reference I mentioned will have to
be slightly modified but you could see that different nested integrals in our case remain orthogonal to each other which
is probably the only requirement for a general application.Friends can notice that right hand side of multiple Ito
integral computation is independent of t1, t2, .., tn-1 and dMt1, dMt2, dMt3,.. and only depends on t and Mt. Our
integrals are also orthogonal. for example in the integral$\int _0^t s \sigma\text{dz}(s)\int _0^s \sigma\text{dz}(u)$
the part$s \sigma\text{dz}(s)$ is orthogonal to$ \int _0^s \sigma\text{dz}(u)$ and so on for any degree of nesting. Just
as dz(s) is orthogonal to z(s).

---

### #31 — Amin (Topic Author)
*April 25, 2016, 3:56 AM*

For the friends who would like to know how the further nested integrals can be calculated here is a small program for
third order nesting integral.$\int _0^t s \sigma\text{dz}(s)\int _0^s \sigma\text{dz}(u)\int _0^u \sigma\text{dz}(v)$
function [] = SDE_Compare_Zintegrals_Infiniti_public03( )s1 =
RandStream('mt19937ar');RandStream.setDefaultStream(s1);savedState = s1.State;
z0=0;sigma0=.710/2;%sigma0=0.710/4%sigma0=0.710*4T_index=1000;%T_index=2000; %T_index=20;
dt=.005/4.0;T=(T_index)*dt;paths=1000000; zz(1:paths)=z0; I2(1:paths)=0.0;%integral zdz0 over time by traditional short
stepped monte carlo.I1(1:paths)=0.0;zzT(1:paths)=0.0;%One step integral zdz calculated by my method for nn=1:T_index
%Loop over time.t=(nn)*dt; t2=(nn-1)*dt; Random1=randn(size(zz));
RandTemp1=Random1.*sqrt(dt);I2=I2+t2*(RandTemp1*sigma0).*I1; %Outer integral I1=I1+(RandTemp1*sigma0).*(zz); %Inner
integralzz = zz +RandTemp1*sigma0;end%My One Step method calculation startsRandom1=randn(size(zzT)); zzT=sigma0.^3*
Random1.^3.*T.^2.5*sqrt(6)/2.*(1/4/2.5)-...3*sigma0.^3.*T.^2.5*Random1.^1.*(1/4/2.5)*sqrt(6)/2;I2_avg=sum(I2)./pathszzT_avg=sum(zzT)./pathsI2_avg2=sum(abs(I2))./pathszzT_avg2=sum(abs(zzT))./paths%%Below
are second moments. To see if both are matchedI2_var=sum(I2.^2)./pathszzT_var=sum(zzT.^2)./pathsBinSize=.0001;%Here you
can change the resolution of monte carlo density. You might have to look at the graph and if it is jagged and noisy,
increase the bin sizeMaxCutOff=1000;%Max cut off is a value given to density generation program.
[XDensity,IndexOutX,IndexMaxX] = MakeDensityFromSimulation_Infiniti(I2,paths,BinSize,MaxCutOff
);[XDensity2,IndexOutX2,IndexMaxX2] = MakeDensityFromSimulation_Infiniti(zzT,paths,BinSize,MaxCutOff
);plot(IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'g',IndexOutX2(1:IndexMaxX2),XDensity2(1:IndexMaxX2),'r')str=input('look
at overlaid Graph comparison of traditional Monte carlo density of zdz(green line) with density of SDE generated from
one step monte carlo method(red line)>');end

---

### #32 — Amin (Topic Author)
*April 30, 2016, 1:12 PM*

I will take a few more days to complete the paper but here are a few formulas for friends. Here I give the general
algorithm for the type of integrals where only dz and dt integrals follow each other in any order. Like many other
possibilities, one four order repeated integral with two dz uncertainties could be
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\text{dv}\int _0^v\sigma  \text{dz}(w)$ The value of the above
kind of integrals, as long as there is no explicit t, does not depend upon the sequence order(whether dz integral comes
first or dt integral comes first does not change the value of the total integrals) so variance can be easily calculated
by Ito Isometry. The order of hermite polynomial depends upon the number of normal uncertainties so is equal to number
of dz integrals. Here is the simple formula to calculate the hermite polynomial representation of the integrals which
equals$ H_n(N)*\frac{\sqrt{\text{Variance}}}{\sqrt{n!}}$ here n, which is the order of hermite polynomials, equals the
number of normal uncertainties. I will give a few examples
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}=H_1(N)\frac{\sigma\text{t}^{1.5}}{\sqrt{1!}\sqrt{3}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)=H_2(N)\frac{\sigma ^2t}{\sqrt{2!}\sqrt{2}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\sigma\text{dz}(v)=\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\sigma\text{dz}(u)\int _0^u\sigma\text{dz}(v)=H_2(N)\frac{\sigma ^2t^2}{\sqrt{2!}\sqrt{12}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\sigma\text{dz}(u)\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\text{du}\int _0^u\sigma\text{dz}(v)=H_1(N)\frac{\sigma ^2t^{2.5}}{\sqrt{1!}\sqrt{20}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)\int _0^u\sigma\text{dz}(v)=H_3(N)\frac{\sigma ^3t^{1.5}}{\sqrt{3!}\sqrt{6}}$
Fourth order and higher integrals can be evaluated to perfect precision using this method so I am not giving examples
for that.

---

### #33 — Cuchulainn
*May 2, 2016, 10:44 AM*

QuoteOriginally posted by: AminI will take a few more days to complete the paper but here are a few formulas for
friends. Here I give the general algorithm for the type of integrals where only dz and dt integrals follow each other in
any order. Like many other possibilities, one four order repeated integral with two dz uncertainties could be
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\text{dv}\int _0^v\sigma  \text{dz}(w)$ The value of the above
kind of integrals, as long as there is no explicit t, does not depend upon the sequence order(whether dz integral comes
first or dt integral comes first does not change the value of the total integrals) so variance can be easily calculated
by Ito Isometry. The order of hermite polynomial depends upon the number of normal uncertainties so is equal to number
of dz integrals. Here is the simple formula to calculate the hermite polynomial representation of the integrals which
equals$ H_n(N)*\frac{\sqrt{\text{Variance}}}{\sqrt{n!}}$ here n, which is the order of hermite polynomials, equals the
number of normal uncertainties. I will give a few examples
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}=H_1(N)\frac{\sigma\text{t}^{1.5}}{\sqrt{1!}\sqrt{3}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)=H_2(N)\frac{\sigma ^2t}{\sqrt{2!}\sqrt{2}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\sigma\text{dz}(v)=\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\sigma\text{dz}(u)\int _0^u\sigma\text{dz}(v)=H_2(N)\frac{\sigma ^2t^2}{\sqrt{2!}\sqrt{12}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\sigma\text{dz}(u)\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\text{du}\int _0^u\sigma\text{dz}(v)=H_1(N)\frac{\sigma ^2t^{2.5}}{\sqrt{1!}\sqrt{20}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)\int _0^u\sigma\text{dz}(v)=H_3(N)\frac{\sigma ^3t^{1.5}}{\sqrt{3!}\sqrt{6}}$
Fourth order and higher integrals can be evaluated to perfect precision using this method so I am not giving examples
for that.what's N?I have having difficulty thinking how these formula can be used in applications.Is it not an idea to
write it up in an (SSRN?) scientific paper from beginning to end?

---

### #34 — Amin (Topic Author)
*May 2, 2016, 11:57 AM*

Quotewhat's N?N is standard Normal random draw in case of monte carlo and you could also replace it with normal density
for analytics.QuoteI have having difficulty thinking how these formula can be used in applications.I will be explaining
that very carefully in the next post.QuoteIs it not an idea to write it up in an (SSRN?) scientific paper from beginning
to end?Yes, I will be doing that in a few days. This is just preview.I will also be posting a small monte carlo program
in a day that will be second order accurate in T. order(T^2) and could be extended to higher orders using the algorithm
I describe here later today.

---

### #35 — Cuchulainn
*May 2, 2016, 12:09 PM*

QuoteN is standard Normal random draw ?? cdf, pdf, or something else?Shreve has Hermite H(x,y), but now it is H(N())
where N is cumulative normal? Did I miss something?  QuoteI will also be posting a small monte carlo program in a day
that will be second order accurate in T. order(T^2) what's T?

---

### #36 — Amin (Topic Author)
*May 2, 2016, 1:28 PM*

QuoteQuoteN is standard Normal random draw ?? cdf, pdf, or something else?as in simple monte carlo like from box muller
or any other normal rng. If you want to use analytics as I mentioned in my post you would have to use pdf.QuoteShreve
has Hermite H(x,y), but now it is H(N()) where N is cumulative normal? Did I miss something?  You could have used H(x,y)
but I think they become equivalent the way I wrote variance out of H(x,y) and used only H(x). I thought it was
simpler.QuoteQuoteI will also be posting a small monte carlo program in a day that will be second order accurate in T.
order(T^2) what's T?T is the time step or final time.

---

### #37 — Amin (Topic Author)
*May 2, 2016, 1:43 PM*

Cuch, here you could see why those integrals are helpful. I have tried to explain in simple terms.We take a general
stochastic differential equation.$x(t)=x(0)+\int _0^t\mu (x(s)) \text{ds}+\int _0^t\sigma (x(s)) \text{dz}(s)$
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
$=x(0)+\mu (x(0))\int _0^t\text{ds}+\frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\int _0^t\int _0^s \text{dvds}+\frac{\partial \mu (x(0))}{\partial x}\sigma (x(0))\int _0^t\int _0^s \text{dz}(v)\text{ds}+.5\frac{\partial ^2\mu (x(0))}{\partial x^2}\sigma ^2(x(0)) \int _0^t\int _0^s  \text{dv} \text{ds}$
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

### #38 — Cuchulainn
*May 3, 2016, 5:55 PM*

Amin,I take the classic SDE/FDM approach and then use it in the MC simulator. I do not have enough knowledge of the
integral approach to do MC with your formulae.I give the code in an attempt to possibly allow the Hermite stuff to be
used in the path evolver stuff. Do I plug in your drift and diffusion functions into my code?You see, I'm a white belt
here:)Thanks// Edited code. The loop is key!class SDE{ // Defines drift + diffusion + dataprivate:
std::shared_ptr data;   // The data for the optionpublic:       SDE(const OptionData& optionData) : data(new
OptionData(optionData)) {} double drift(double t, double S)        { // Drift term                 return (data->r -
data->D)*S; // r - D  }               double diffusion(double t, double S)    { // Diffusion term
return data->sig * S;   }};int main(){  std::cout > NT; // V2 mediator stuff    long NSIM = 50000;      std::cout >
NSIM;       double M = static_cast(NSIM);   double k = myOption.T / double (NT);    double sqrk = std::sqrt(k);     //
Normal random number double dW;      double price = 0.0;     // Option price double payoffT; double avgPayoffT = 0.0;
double squaredPayoff = 0.0;     double sumPriceT = 0.0; // Normal (0,1) rng     std::default_random_engine dre;
std::normal_distribution nor(0.0, 1.0); long coun = 0; // Number of times S hits origin for (long i = 1; i

---

### #39 — Amin (Topic Author)
*May 3, 2016, 7:58 PM*

**(broken latex: Unbalanced $$: 9)**

```latex
Daniel, I will do simple math behind the sde you are simulating. Here is the equation that we expanded just one level
more than traditional monte carlo. This is equation right after equation six in previous post. I will write it again.
$x(t)=x(0)+\mu (x(0))\int _0^t\text{ds}+\frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\int _0^t\int _0^s \text{dvds}+\frac{\partial \mu (x(0))}{\partial x}\sigma (x(0))\int _0^t\int _0^s \text{dz}(v)\text{ds}+.5\frac{\partial ^2\mu (x(0))}{\partial x^2}\sigma ^2(x(0)) \int _0^t\int _0^s  \text{dv} \text{ds}$
$+\sigma (x(0))\int _0^t\text{dz}(s)+\frac{\partial \sigma (x(0))}{\partial x}\mu (x(0))\int _0^t\int _0^s \text{dvdz}(s)+\frac{\partial \sigma (x(0))}{\partial x}\sigma (x(0))\int _0^t\int _0^s \text{dz}(v)\text{dz}(s)+.5\frac{\partial ^2\sigma (x(0))}{\partial x^2}\sigma ^2(x(0))\int _0^t\int _0^s\text{dv}\text{dz}(s)$
Eq(1)I have tried to use your notation.we use$\mu\text{(x(0))=(r-d)x(0)}$
$\frac{\partial \mu (x(0))}{\partial x}\text{=(r-d)}$$\frac{\partial ^2\mu (x(0))}{\partial x^2}\text{=0}$
$\sigma\text{(x(0))= sig x(0)}$$\frac{\partial \sigma (x(0))}{\partial x}\text{=sig}$
$\frac{\partial ^2\sigma (x(0))}{\partial x^2}\text{=0}$ substituting the above values in Eq(1), we get
$x(t)=x(0)+(r-d)x(0) \Delta\text{t}+(r-d)^2x(0)\frac{\Delta\text{t}^2}{2}+(r-d)\text{sig} x(0)\int _0^t\int _0^s \text{dz}(v)\text{ds}$
$+\text{sig} x(0)\text{nor}(0,1)\sqrt{\Delta\text{t}}+\text{sig} (r-d)x(0)\int _0^t\int _0^s \text{dvdz}(s)+\text{sig}^2 x(0)\int _0^t\int _0^s \text{dz}(v)\text{dz}(s)$
We use the identities
$\int _0^t\int _0^s \text{dz}(v)\text{ds}=\int _0^t\int _0^s \text{dvdz}(s)=\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$
and$\int _0^t\int _0^s \text{dz}(v)\text{dz}(s)=\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t}}{2}$ Now we can get
the monte carlo simulation scheme.
$x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)^2x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$
$+\text{sig}^2x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t}}{2}$ The above is order$\Delta\text{t}$ accurate
with some terms of higher order. Adding one more term that comes from further expansion will take the order to
$\Delta\text{t}$ ^1.5. The new better scheme would be
$x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)(r-d)x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2*\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$
$+\text{sig}^2*x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t} }{2}+\text{sig}^3*x(t)\left(\text{nor}(0,1)^3-3\text{nor}(0,1)\right)\frac{\Delta\text{t}^{1.5}}{6}$
```

---

### #40 — Cuchulainn
*May 4, 2016, 12:29 PM*

Thanks. Ahsan, that's pretty clear.Let me get my head around to get it into the MC framework and I'll hopefully get back
with some results and queries in a few days.

---

### #41 — Amin (Topic Author)
*May 5, 2016, 6:59 AM*

Thank you Daniel. We all Wilmotters await the results of your monte carlo work. I am looking forward to your analysis,
comments and questions.Though for mildly non-linear SDEs, we can take a quite large step, for many non-linear SDE
equations, a universally much longer step becomes difficult especially close to zero where derivatives change extremely
fast. I am presenting an improvement using Girsanov theorem so that a large enough step could be taken by even
non-linear equations. I will upload that program here on Wilmott in a day hopefully that could do monte carlo with
Girsanov theorem and we will be able to take large steps for non-linear SDEs.I had earlier said on the forum that we
would be able to take large steps of even 5-10 years in monte carlo or other density construction. I stand behind my
claim but that has to be done by using the concepts from my earlier work Stochastic Calculus of Standard Deviations. In
stochastic calculus of standard deviations, we divide the initial delta density into 100-400 normal standard deviation
subdivisions that preserve the mass in each subdivision and continue to advance ahead in time in the same normal
standard deviation line. We can effortlessly take step size of roughly .25 years and continue to update the SDE
derivatives of each subdivision in the direction of that particular normal SD. Unlike recombining tree, we move ahead in
a non-recombining tree where number of tree branches remain exactly the same through delta origin (start of SDE
simulation)  to the end of the simulation and complexity remains exactly the same as we advance the density into time.
It will be impossible for many non-linear SDEs to take the derivatives only at time zero and advance the solution till
several years since it may become too difficult and unefficient to keep on taking derivatives of drift and volatility
functions. However I am sure it can still be done extremely cheaply using the concepts from stochastic calculus of
standard deviations.

---

### #42 — Gambler
*May 5, 2016, 12:21 PM*

interesting

---

### #43 — Cuchulainn
*May 5, 2016, 7:19 PM*

Just  to make sure; your SDE is?dS = (r-d)Sdt + sig S dW?It has an exact solution.

---

### #44 — Amin (Topic Author)
*May 6, 2016, 12:20 AM*

Yes, of course, we all know the lognormal density solution after transformation to log coordinates but my scheme has no
knowledge of the exact solution. It is based on the naiive simulation technique used in your code and a comparison has
to be made how better it is as compared to scheme you used in code.

---

### #45 — Amin (Topic Author)
*May 6, 2016, 5:09 AM*

Sorry about a careless mistake in Eq(6) in the fourth post from the bottom on previous page. I took a second derivative
in the last term while I should have used Ito product rule. When I wrote the post in response to cuch's post, I was
going to sleep in the evening after staying awake for more than 24 hours but decided to answer his post first before I
sleep so I made the mistake. I think most forum members have a better mathematics than mine, so they would have
understood the mistake on their own but if you did not notice it, please substitute Ito product rule instead of simple
change of one variable Ito formula I carelessly used there.

---

### #46 — Cuchulainn
*May 6, 2016, 8:09 AM*

**(broken latex: Unbalanced $$: 1)**

```latex
QuoteAdding one more term that comes from further expansion will take the order to$\Delta\text{t}$ ^1.5. The new better
scheme would be
$x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)(r-d)x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2*\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$
$+\text{sig}^2*x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t} }{2}+\text{sig}^3*x(t)\left(\text{nor}(0,1)^3-3\text{nor}(0,1)\right)\frac{\Delta\text{t}^{1.5}}{6}$
OK, I have put this this into MC code. Looking at it I see that it is Euler plus extra terms of order O(dt) and
O(dt^3/2). Intuitively, accuracy will be similar to Euler, which is borne out on the example (put). If anything, Euler
is very very slightly more accurate.K = 10, S=5, r = 0.12, sig = 0.5, T = 1.I can try other use cases but at this stage
I am curious on how to proceed. // One thing I do miss is that all of a sudden the schemes no longer explicitly use
Hermite polynomials.
```

---

### #47 — Amin (Topic Author)
*May 6, 2016, 8:58 AM*

QuoteI can try other use cases but at this stage I am curious on how to proceed. One thing to check for will be how long
can your step get when you use a higher order scheme while you keep accuracy the same as that of scheme of order(dt^.5),
the benchmark accuracy. If your step is already small enough and accuracy is very good there may be very small advantage
of higher order scheme. However you can increase step size with higher order scheme so one thing to investigate would be
how long can the step get with higher order scheme as compared to the small step naiive dt^.5 order scheme while
accuracy could remain the same. Quote One thing I do miss is that all of a sudden the schemes no longer explicitly use
Hermite polynomials.nor(0,1)= x =H1(x)=H1(nor(0,1))nor(0,1)^2-1=x^2 - 1 = H2(x)=H2(nor(0,1))nor(0,1)^3-3nor(0,1)= x^3 -
3 x = H3(x) =H3(nor(0,1))If you wanted to be totally analytic, You could have replaced nor(0,1) with x and integrated
over a unit normal density f(x) to get the same one step monte carlo density analytically. We have replaced x with a
unit normal random draw in hermite polynomials as it is a numerical integration over unit normal density in monte carlo
sense since we are drawing random numbers from unit normal density.

---

### #48 — Cuchulainn
*May 6, 2016, 9:27 AM*

Let's try a 2-factor model e.g. basket, Heston.And a mean-reverting SDE.

---

### #49 — Amin (Topic Author)
*May 6, 2016, 10:02 AM*

Ok, I will write a scheme for 2D correlated heston with mean reverting volatility. Please give me a few hours so I could
work out the mathematics as Heston was not my favorite in research till now so I will have to do some new work alongwith
some other things. Might have to take a few hours before I could get back.

---

### #50 — Cuchulainn
*May 6, 2016, 10:24 AM*

QuoteOriginally posted by: AminOk, I will write a scheme for 2D correlated heston with mean reverting volatility. Please
give me a few hours so I could work out the mathematics as Heston was not my favorite in research till now so I will
have to do some new work alongwith some other things. Might have to take a few hours before I could get back.No problem
and no hurry.  I won't be able to look until early next week anyways.You can see Heston/CIR as a test of your new
approach and the ability to reproduce and improve the results.

---

[Index](index.md) | [Next →](page_002.md)
