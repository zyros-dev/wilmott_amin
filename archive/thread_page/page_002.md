# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 2 of 65** — Posts #51–#100

[← Previous](page_001.md) | [Index](index.md) | [Next →](page_003.md)

---

### #51 — Cuchulainn
*May 8, 2016, 10:12 AM*

Feedback on GBM:I ran MC for low/zero/high values of r,d and sig. The results are almost identical to those produced by
Euler. In any case, convergence O(dt^3/2) does not seem to hold, based on inspecting the output. And it is more
computationally intensive.The first few terms of your scheme is Euler so my feeling is all the extra terms cannot bump
up the accuracy.

---

### #52 — Amin (Topic Author)
*May 8, 2016, 11:48 AM*

Daniel, you have to alter the step size. At a very small step size, if the equation is not very non-linear, there are
little gains from better scheme since it is the sqrt(dt) term that dominates everything. Please increase the step size
by for example by ten times the step size you are using for Euler monte carlo and you will see that larger step size
will give you one step dynamics quite different from normal density and very close to original distribution in a way
traditional Euler monte carlo can never capture. If you used matlab, I would have posted a program for you that could do
it in matlab and you could visually compare the graphs of densities from Euler and using this new method with 10X step,
20X step or 50X step in time as compares to Euler monte carlo step of 1X with same final time.I will be posting a two
dimensional correlated CEV diffusion monte carlo today but that program would be in matlab. Friends would be able to
view the resulting densities as overlaid graphs to make a comparison of the accuracy of the method for themselves. I
will give a pseudo code and equations in Latex as well.

---

### #53 — Cuchulainn
*May 8, 2016, 12:34 PM*

I took NT = 100, 1000, 500 and I could see no difference. This is at odds with the previous post. Can you give parameter
values for r, d, ... and dt?One exampleK = 10S = 5r = 0.12sig = 0.5T = 1With NT, NSIM100,10001000,100000500, 5000001000,
100000What prices do you get? // For me personally, Matlab code is not insightful at the moment.

---

### #54 — Amin (Topic Author)
*May 9, 2016, 3:17 AM*

I will be able to give the numbers later today but there is something I would like to mention before that.Compare these
two.New method with NT=10.Euler with NT=100. Keep NSIM the same for both.Better calculate a precise benchmark with Euler
NT=1000, NSIM=large.Then see what is new method with NT=8, NT=16, NT=10, NT=20. and compare with Euler.For several
non-linear equations if you take  a step as small  as dt=.0001, you still do not get one step density right in Euler
monte carlo. The density simply does not match the analytic density. But this new method has the ability to give precise
density even when steps are increased by a multiple of 10 to 20 or sometimes even more for such equations. I wish you
could clone my matlab monte carlo density graphing program in python or some other language you like to use, and then
you could see how the density changes with step instead of relying only on the option pricing numbers.

---

### #55 — Cuchulainn
*May 9, 2016, 7:06 AM*

I think it is better if you post these results to see if I can reproduce them . In this way I can see my code is running
properly because I don't see a lot of difference between the two methods at this stage.Your numbers are more interesting
than mine:) QuoteI wish you could clone my matlab monte carlo density graphing program in python or some other language
you like to use, and then you could see how the density changes with step instead of relying only on the option pricing
numbers. This is not a show-stopper. We can use the language of numerical analysis. I avoid Matlab and Python (Even tho'
it was invented in Amsterdam) like the plague.[

---

### #56 — Cuchulainn
*May 10, 2016, 9:56 AM*

[This post has been deleted or contains no text content]

---

### #57 — Cuchulainn
*May 10, 2016, 2:42 PM*

Same example.NT,NSIM, Euler classic, A. Amin method========================2000, 1000000, 4.07306, 4.073062000, 2000000,
4.07426, 4.07426

---

### #58 — Amin (Topic Author)
*May 10, 2016, 6:14 PM*

Daniel, thank you for your effort. It is much appreciated. I guess, you used the second supposedly more accurate scheme.
I would request you to compare the Euler with smaller order scheme I had derived. When I wrote the supposedly more
accurate scheme I added one term on the fly from higher level. However I realize that when we go from lower level to
higher level of derivatives, all the terms have to be taken to higher level unless you have done some special analysis
particular to SDE. I added one term and missed many others something which might be causing biases. I would request you
to do your numerical accuracy analysis on scheme I mentioned as order(dt)  or order delta_t. Once this scheme is proven
better, I will write detailed order(dt)^1.5 scheme with all terms included. Let us see what your results are?

---

### #59 — Cuchulainn
*May 10, 2016, 6:17 PM*

QuoteOriginally posted by: AminDaniel, thank you for your effort. It is much appreciated. I guess, you used the second
supposedly more accurate scheme. I would request you to compare the Euler with less accurate scheme I had derived. When
I wrote the supposedly more accurate scheme I added one term on the fly from higher level. However I realize that when
we go from lower level to higher level of derivatives, all the terms have to be taken to higher level unless you have
done some special analysis particular to SDE. I added one term and missed many others something which might be causing
biases. I would request you to do your numerical accuracy analysis on scheme I mentioned as order(dt)  or order delta_t.
Once this scheme is proven better, I will write detailed order(dt)^1.5 scheme with all terms included. Let us see what
your results are?I am counting on a bug-free formula. Your formula was wrong, thus? I'm wasting my time like this.
Meshuggah.==Anyways, let's look ahead :)The first scheme does not put any 'sods on the dyke" (Dutch phrase) i.e. it
makes no difference. Results is the same. Unfortunately, I think it's back to the drawing board???Even looking at the
schemes gut feeling says it is no better than Euler. It' Euler with terms tagged on.Did you do MC pricing at all with
these schemes?  Unless I have made a huge computing error??

---

### #60 — Amin (Topic Author)
*May 10, 2016, 8:10 PM*

Daniel, as I said, I added a higher order term quickly thinking it might add to accuracy. I will appreciate if you could
quickly give us a table of values from O(dt) scheme just like you gave for supposedly higher order scheme. You already
have the program and it will take you 5-10 minutes. Hope you would be willing to do this considering I spent hours
writing latex formulas here.

---

### #61 — Cuchulainn
*May 10, 2016, 8:49 PM*

**(broken latex: Unbalanced $$: 9)**

```latex
QuoteOriginally posted by: AminDaniel, I will do simple math behind the sde you are simulating. Here is the equation
that we expanded just one level more than traditional monte carlo. This is equation right after equation six in previous
post. I will write it again.
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
Neither scheme is an improvement on Euler in any way.. Believe me. I won't be posting numbers because they all the same.
The schemes fall short for MC simulation. Most disconcerting is that convergence is erratic and not monotone.QuoteI
added a higher order term quickly thinking it might add to accuracyAnd it might not.
```

---

### #62 — Amin (Topic Author)
*May 11, 2016, 12:25 AM*

QuoteNeither scheme is an improvement on Euler in any way.. Believe me. I won't be posting numbers because they all the
same. The schemes fall short for MC simulation. Please post numbers since they would be very helpful to see what they
are. They might be off as you have suggested but only numbers you posted were from a bad scheme. I am not asking you to
do something that is worthless.QuoteQuoteI added a higher order term quickly thinking it might add to accuracyAnd it
might not.QuoteAs I already explained, when we go to higher order all terms have to be taken to higher order otherwise
there are biases. I was not so deeply aware when I wrote the scheme. Please post numbers from good scheme and I can see
what is wrong and how wrong it is and many other things.

---

### #63 — Cuchulainn
*May 11, 2016, 4:30 AM*

QuoteOriginally posted by: AminQuoteNeither scheme is an improvement on Euler in any way.. Believe me. I won't be
posting numbers because they all the same. The schemes fall short for MC simulation. Please post numbers since they
would be very helpful to see what they are. They might be off as you have suggested but only numbers you posted were
from a bad scheme. I am not asking you to do something that is worthless.QuoteQuoteI added a higher order term quickly
thinking it might add to accuracyAnd it might not.QuoteAs I already explained, when we go to higher order all terms have
to be taken to higher order otherwise there are biases. I was not so deeply aware when I wrote the scheme. Please post
numbers from good scheme and I can see what is wrong and how wrong it is and many other things.This is not the way to
proceed. So, I'm out until you post a correct scheme.

---

### #64 — Cuchulainn
*May 11, 2016, 4:31 AM*

QuoteOriginally posted by: AminQuoteNeither scheme is an improvement on Euler in any way.. Believe me. I won't be
posting numbers because they all the same. The schemes fall short for MC simulation. Please post numbers since they
would be very helpful to see what they are. They might be off as you have suggested but only numbers you posted were
from a bad scheme. I am not asking you to do something that is worthless.QuoteQuoteI added a higher order term quickly
thinking it might add to accuracyAnd it might not.QuoteAs I already explained, when we go to higher order all terms have
to be taken to higher order otherwise there are biases. I was not so deeply aware when I wrote the scheme. Please post
numbers from good scheme and I can see what is wrong and how wrong it is and many other things.This is not the way to
proceed. So, I'm out.

---

### #65 — Cuchulainn
*May 11, 2016, 6:30 AM*

QuoteOriginally posted by: amikeFor your example there is also a handy exact integral: $
$\int_0^t z_t dz_t=\frac{1}{2}(z_t^2-t)$ $, so you may want to explain how/if your result agrees with it...I agree.This
is still an open question here. I think a yes/no should be given to clear up the misunderstandings.

---

### #66 — Amin (Topic Author)
*May 11, 2016, 7:01 AM*

Sorry Daniel for the delay in posting my results. I would request you to rejoin the discussion if you like, please. OK,
I tested the right O(dt) scheme and it gives far better results, at least on my computer, for longer step sizes and the
difference becomes especially obvious when step size becomes greater than .05 years. I will be posting my results like
you did in an hour.I would politely say that what you call open question in your previous post has been definitively and
rightly answered by me on this thread. I claim the answer I gave is the only right answer. In fact I am not the first
one who gave this answer especially when there are only dz-integrals the answer was well known to many stochastic
calculus experts. I do not know whether anybody had done both a combination of dt-and dz-integrals before like I posted
on this thread. Many experts in stochastic calculus will like to tell you that my answer is exactly the right answer.In
order to clear any misconception, I will post my matlab program for the problem Daniel posted so people can see for
themselves how my method performs. Daniel, I hope you could be able to look at equations in the matlab program and clone
in C++.Sorry I was unable to post my programs before like I continued to say. I dug up a six year old damaged laptop,
removed all wifi devices, attached it to an external monitor and I am back to work.

---

### #67 — Amin (Topic Author)
*May 11, 2016, 7:59 AM*

Here is my table of Results. I quickly did some quick simulations.NT             NSIM                  Euler
A.Amin1               10^6                 3.94247                   4.05782               10^6                 3.98663
4.07155               10^6                 4.04323                   4.078810             10^6                 4.05666
4.0746320             10^6                 4.06806                   4.0765950             10^6                 4.07302
4.07637100           10^6                 4.0691                     4.0707Exact answer suggested by Daniel is 4.07326.
We can see that both methods have enough monte carlo variance. Only NT=2 can get my method in the approximate right
territory while it takes NT=50 for the standard Euler. This is just a quick observation from the above table. I did not
do anything special and used matlab's own random number generator. I am sure that going to higher level will be far
better in accuracy but we have to take all the terms to higher level and selectively taking one term from the higher
level (like I earlier naiively did)  will introduce biases unless somebody has done special analysis for an SDE.

---

### #68 — savr
*May 11, 2016, 8:22 AM*

Could you please explain in words the difference between your new method and the "Strong Taylor Approximations" presented, for example, in slides 6-7 of [http://www.damtp.cam.ac.uk/user/na/FoCM ... loeden.pdf](http://www.damtp.cam.ac.uk/user/na/FoCM/FoCM08/Talks/Kloeden.pdf) ?

---

### #69 — Cuchulainn
*May 11, 2016, 9:20 AM*

QuoteOriginally posted by: savrCould you please explain in words the difference between your new method and the "Strong Taylor Approximations" presented, for example, in slides 6-7 of [http://www.damtp.cam.ac.uk/user/na/FoCM ... loeden.pdf](http://www.damtp.cam.ac.uk/user/na/FoCM/FoCM08/Talks/Kloeden.pdf) ?Looking at the two schemes produced by Ahsan the terms look like Hermite polynomial chaos expansion. So, it must be the relationship between Wienr integrals and Hermite polynomials(?)  (due to K. Ito?)  I am beginning to see the rationale behind his scheme, slowly.

---

### #70 — Cuchulainn
*May 11, 2016, 2:23 PM*

QuoteOriginally posted by: AminHere is my table of Results. I quickly did some quick simulations.NT             NSIM
Euler                       A.Amin1               10^6                 3.94247                   4.05782
10^6                 3.98663                   4.07155               10^6                 4.04323
4.078810             10^6                 4.05666                   4.0746320             10^6                 4.06806
4.0765950             10^6                 4.07302                   4.07637100           10^6                 4.0691
4.0707Exact answer suggested by Daniel is 4.07326. We can see that both methods have enough monte carlo variance. Only
NT=2 can get my method in the approximate right territory while it takes NT=50 for the standard Euler. This is just a
quick observation from the above table. I did not do anything special and used matlab's own random number generator. I
am sure that going to higher level will be far better in accuracy but we have to take all the terms to higher level and
selectively taking one term from the higher level (like I earlier naiively did)  will introduce biases unless somebody
has done special analysis for an SDE.I agree with these results in the main. Which RNG did you use for Euler? I used
C++11 Mersenne Twister which is probably the reason my Euler results are closer to yours.

---

### #71 — Amin (Topic Author)
*May 13, 2016, 3:37 PM*

Many people asked me the question what exactly is the breakthrough in the understanding and simulation of SDEs. Well,
the breakthrough is new understanding of how higher derivatives of drift and volatility term of an SDE and their
interaction affect the dynamics of evolution of the particular SDE probabilistically(or conditionally when the normal
draw or particular realization of the normal has been realized)  when driving uncertainty is a normal distribution .
When we solve an SDE, we need exact values of drift and volatility in continuous time along the path of the SDE variable
which is mostly not known analytically. Of course, we can never tell/predict the future realization of the SDE since
normal uncertainty cannot be predicted. but once we know the particular draw or realization of the normal uncertainty,
we can, at least theoretically, tell with great accuracy what would be the expansions of drift and volatility to any
increasing degree of precision by taking a higher order of expansion of drift and volatility functions and by using it
in conjunction with hermite polynomials functions of realized value of the normal draw which models the driving
uncertainty. The Ito change of variable formula tells us how 1st two derivatives affect the evolution of functions
dependent on a stochastic process described by an SDE. When we apply Ito formula, we need exact value of 1st two
derivatives dependent terms in continuous time along the path of the stochastic process conditional on the particular
realization of normal uncertainty something which is not known analytically for most SDEs. I was able to express the
forward values(in continuous time along the path conditional on normal driving uncertainty) of drift and variance into
first two derivatives dependent terms evaluated at  time zero plus higher order terms in forward time by using Ito
formula. The higher order forward time terms in turn can be expressed as sum of further time zero terms and further
higher order forward time terms by repeated use of Ito formula and this process continues depending upon the structure
of drift and volatility functions and their derivatives. Each time we repeatedly apply Ito formula in the above method
on time forward terms of drift and volatility expansion, the accuracy and precision of the forward value of drift and
volatility as a function of normal uncertainty draw increases.However sometimes there is a problem with use of higher
order terms in some non-linear SDEs since they are used in conjunction with higher order hermite polynomials. The
current normal random variable sampling/generation techniques many times do not sample variance with very high accuracy.
Normal is known by two moments only but when variance increases slightly, the higher moments of normal increase more
drastically. For methods with smaller order expansions that use hermite polynomials upto level two, we are almost always
fine with some very rare exceptions. However the variance of higher order hermite polynomials start to blow with a small
increase in the variance of normal draws since these hermite polynomials use third, fourth or higher powers of normal
random variable. This may not always be the case but sometimes for non-linear SDEs there is a loss of robustness due to
blowing of variance of higher order hermite polynomials. So we have the theoretical apparatus in place to do very high
precision monte carlo but we need better normal random variable sampling techniques in which variance of higher order
hermite polynomials along the monte carlo path does not blow. No research has been done on it since there was no
knowledge of higher order monte carlo and especially of use of hermite polynomials in the monte carlo was not known so
nobody probably ever cared about better and precise sampling techniques that would closely match the variance of higher
order hermite polynomials.I will just complete my paper with explanation of monte carlo with second order hermite
polynomial and also apply it to generation of transition probabilities with greater order hermite polynomials. Though I
would describe the theoretical procedure how to expand drift, volatility and other stochastic integrals of an SDE to any
level or any degree of precision something which is just a straightforward extension of what I have mentioned on this
thread.However totally robust and very high precision monte carlo methods could only be available after other people
have done research on precise methods of drawing normal random numbers in a way that variances of high order hermite
polynomials are retrieved.

---

### #72 — Cuchulainn
*May 15, 2016, 10:03 AM*

QuoteHowever totally robust and very high precision monte carlo methods could only be available after other people have
done research on precise methods of drawing normal random numbers in a way that variances of high order hermite
polynomials are retrieved. Any supporting literature?

---

### #73 — Amin (Topic Author)
*May 17, 2016, 9:00 AM*

Here is a small matlab program that makes a graph comparison of density of CEV noise from Euler Monte Carlo and
Stochastic Calculus of Standard Deviations. I hope many friends would really like this program.function [] =
SDEXticsInfinitiTechnologiesCEVNoise01_Public( )X0_max=800;%Total number of SD Fractions.X0_mid=400.5;%Mid of the SD
Grid. Lies at z0 by definition.X0_mid0=400;X0_start=1;
dX0=.0125;%Width of SD cells in terms of Standard Deviations.              T_index=200; dt=.005/1.0;
epsilon=0.750gamma=.750;z0=1.0;dz_integral1(1:X0_max)=z0;iivector(1:X0_max)=1:X0_max;paths=1000000; %No. of Paths for
creation of Monte Carlo density by simulating;zz4(1:paths)=z0; C1=1/sqrt(2*pi)/2;C2=1/(2*pi)/4;for nn=1:T_index
%Loop over time.    t=(nn)*dt;      t0=(nn-1)*dt;
prob=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)/(sqrt(t)*epsilon);
prob2=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)*dX0;     dt=t-t0;        dz_integral1=dz_integral1+...
epsilon.*dz_integral1.^gamma.*(iivector-X0_mid).*dX0*(sqrt(t)-sqrt(t0))...
+epsilon.*gamma.*dz_integral1.^(gamma-1).*(epsilon.*dz_integral1.^(gamma).*(t-t0)/2.0.*(((iivector-X0_mid).*dX0).^2.*C2-1))...
+.5*epsilon.*gamma.*(gamma-1).*dz_integral1.^(gamma-2).*epsilon.^2.*dz_integral1.^(2*gamma).*(t.^1.5-t0.^1.5)./sqrt(3).*(((iivector-X0_mid).*dX0)).*C1;
%Naive brute force Monte carlo part follows. Since the steps are extremely    %short the monte carlo is quite close to
the right density for most of the cases     %but may be off for a very small number of cases but it is a good initial
%check on our analytic density       Random1=randn(size(zz4));      RandTemp1=Random1.*sqrt(dt);    zz4
=zz4+zz4.^gamma.*RandTemp1*epsilon;endeffective_sigma=epsilon;Jacobian_dz1(1:X0_max)=0;for ii=4:X0_max-3
Jacobian_dz1(ii)=((dz_integral1(ii-2))-8*(dz_integral1(ii-1))+8*(dz_integral1(ii+1))-(dz_integral1(ii+2)))/(12*dX0*sqrt((T_index-1+1)*dt)*effective_sigma);
if(Jacobian_dz1(ii)~=0.0)      Jacobian_dz1(ii)=1/Jacobian_dz1(ii);  endendBinSize=.005;%Here you can change the
resolution of monte carlo density. You might have to look at the graph and if it is jagged and noisy, increase the bin
size%If it is made of straight line increments, decrease the bin size.MaxCutOff=20;[XDensity,IndexOutX,IndexMaxX] =
MakeDensityFromSimulation_Infiniti(zz4,paths,BinSize,MaxCutOff );   str=input('Press any key to see the graph, Please
make sure to rescale the graph from Edit menu on the matlab graph when diffusion reaches zero.')
plot(IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'g',(dz_integral1(X0_start+2:X0_max-2)),prob(X0_start+2:X0_max-2).*Jacobian_dz1(X0_start+2:X0_max-2),'k')
str=input('look at overlaid Graph comparison of Monte carlo density of SDE(green line) with density of SDE generated
from analytic method(black line)>');     end

---

### #74 — Amin (Topic Author)
*May 18, 2016, 8:41 AM*

Here is the helper function to graph from monte carlo and you will need this as a separate function in matlab to make a
graph from monte carlo paths. Some friends pointed out that this function is missing in the previous code. I had
distributed it earlier in the same thread but I am writing it here again.function [XDensity,IndexOut,IndexMax] =
MakeDensityFromSimulation_Infiniti(X,Paths,BinSize,MaxCutOff )%Processes monte carlo paths to return a series Xdensity
as a function of IndexOut. IndexMax is the maximum value of index.% Xmin=0;Xmax=0;for
p=1:Pathsif(X(p)>MaxCutOff)X(p)=MaxCutOff;endif(Xmin>real(X(p)))Xmin=real(X(p));endif(XmaxIndexMax)index=IndexMax;endXDensity(index)=XDensity(index)+1.0/Paths/BinSize;endIndexOut(1:IndexMax)=Xmin+(0:(IndexMax-1))*BinSize;end

---

### #75 — Amin (Topic Author)
*May 18, 2016, 11:32 AM*

In stochastic calculus of standard deviations, we divide the normal density of standard brownian motion into a large
number of subdivisions measured in terms of standard deviations (as difference of standard deviations which are units of
normal density). These subdivisions remain constant when measured in terms of standard deviations but expand in time in
absolute terms with increasing variance such that probability mass in each sub division remains exactly the same at any
point in the evolution of the density. Each subdivision can be considered as a branch of a non-recombining tree so that
number of branches(or subdivisions) remain exactly the same from the start from origin to expiry at any future time.
Each branch expands straight in the direction of the same realization of normal(measured again in standard deviations)
but expanding and moving out due to increase in variance with t. In stochastic calculus of standard deviations, these
branches do not interact, and stochastic calculus is applied on each branch independently. Here we use n as index for
number of branches of the tree with each subdivisions/branch of equal width${\Delta X0}$ so that$n{\Delta X0}$ ranges
typicaly between -5 to 5, the entire range of normal with constant increments of${\Delta X0}$ between successive
subdivisions. At any time in the evolution of the tree, we have that centre of nth branch or subdivision is given by
$X_n(t)=n \Delta\text{X0} \sqrt{t}$ The absolute width of each of these subdivisions is given as
$\Delta\text{X0} \sqrt{t}$ Since probability mass in each of these subdivisions remain constant as a function of time,
we can apply the formulas as
$\int _{X_n(t)-.5\Delta\text{X0} \sqrt{t}}^{X_n(t)+.5\Delta\text{X0} \sqrt{t}} f(X(t))dX(t)=\int _{X_n(s)-.5\Delta\text{X0} \sqrt{s}}^{X_n(s)+.5\Delta\text{X0} \sqrt{s}}f(X(s))dX(s)$
or any two times s or t.For the case of evaluation of powers of Normal in case of hermite polynomials, we have to
analytically evaluate the integrals of the kind for power p
$\int _{X_n(t)-.5\Delta\text{X0} \sqrt{t}}^{X_n(t)+.5\Delta\text{X0} \sqrt{t}}(X(t))^p f(X(t))dX(t)$ and we have to
calculate, for the evolution from density at time s to density at time t, the following integrals
$\int _{X_n(t)-.5\Delta\text{X0} \sqrt{t}}^{X_n(t)+.5\Delta\text{X0} \sqrt{t}}(X(t))^p f(X(t))dX(t)-\int _{X_n(s)-.5\Delta\text{X0} \sqrt{s}}^{X_n(s)+.5\Delta\text{X0} \sqrt{s}}(X(t))^p f(X(s))dX(s)$
where$f(X(t))=\frac{1}{\sqrt{2 \text{Pi} t}}\text{Exp}\left[-.5\frac{\left(X\right){}^2}{t}\right]$ The above formulas
help us find the constants that multiply with powers of Z in the analysis of stochastic calculus of standard
deviations.The above discussion was for stochastic calculus of standard deviations applied to evolution of normal
density. For a general SDE, we simply follow the previous discussion in the thread and subdivisions expand nonlinearly
but we make use of fact that evolution of standard normal density employed in the evolution of general nonlinear SDE is
independent of evolution of any nonlinear SDE.The code I gave above in a recent post was an initial demonstration and
the constants in that code will change now.

---

### #76 — Cuchulainn
*May 18, 2016, 12:55 PM*

QuoteNT             NSIM                  Euler                       A.Amin1               10^6                 3.94247
4.05782               10^6                 3.98663                   4.07155               10^6                 4.04323
4.078810             10^6                 4.05666                   4.0746320             10^6                 4.06806
4.0765950             10^6                 4.07302                   4.07637100           10^6                 4.0691
4.0707Looking at the exact put ~ 4.07326 we ask the question "how many dt (1/NT) and NSIM needed to get the same answer,
numerically?". In other words the computational effort needed to achieve a given accuracy?For your O(dt^3/2) model I
need NT = 1000, NSIM  = 100 million.I have converted the SDE into a Random ODE using Karhunen-Loeve (separated)
expansion to approximate the Wiener process. So, I have a RODE that I can approximate using Runge Kutta, Bulisch-Stoer
etc. I also take NT = 1000 for each draw.For RNG I take Mersenne Twister (some tuning maybe later).Result: I get exact
put price with NSIM = 5 million draws. That's  a twenty-fold difference.Big difference. Any idea why?// The RODE must be
written in Stratonovich form, not Ito form.

---

### #77 — Amin (Topic Author)
*May 18, 2016, 6:48 PM*

Daniel, I think I explained two or three times that O(dt^3/2) as I wrote was bad and did not have a proper order since
all terms required to achieve order were not added. When I wrote O(dt) scheme which is exact and right , I was tempted
to add a term of noise that was in powers of dt^3/2 but all terms from previous order or level had to be added to get a
consistent scheme. I am sure you can easily do simple math to find the correct O(dt^3/2) scheme by following the
discussion. The numbers I gave and you have quoted in your previous post are from O(dt) scheme as I had mentioned which
is good.

---

### #78 — Cuchulainn
*May 18, 2016, 7:14 PM*

**(broken latex: Unbalanced $$: 1)**

```latex
QuoteOriginally posted by: AminDaniel, I think I explained two or three times that O(dt^3/2) as I wrote was bad and did
not have a proper order since all terms required to achieve order were not added. When I wrote O(dt) scheme which is
exact and right , I was tempted to add a term of noise that was in powers of dt^3/2 but all terms from previous order or
level had to be added to get a consistent scheme. I am sure you can easily do simple math to find the correct O(dt^3/2)
scheme by following the discussion. The numbers I gave and you have quoted in your previous post are from O(dt) scheme
as I had mentioned which is good.Well, the O(dt^3/2) does seem to converge. So, I don't think is the issue is what it
seems to be.I also tested your O(dt) scheme and it also take 100 million draws to get near to the exact put. is this
scheme correct?Now we can get the monte carlo simulation scheme.
$x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)^2x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$
$+\text{sig}^2x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t}}{2}$ The above is order$\Delta\text{t}$ accurate
with some terms of higher order.
```

---

### #79 — Cuchulainn
*May 18, 2016, 7:16 PM*

**(broken latex: Unbalanced $$: 1)**

```latex
QuoteOriginally posted by: CuchulainnQuoteAdding one more term that comes from further expansion will take the order to
$\Delta\text{t}$ ^1.5. The new better scheme would be
$x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)(r-d)x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2*\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$
$+\text{sig}^2*x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t} }{2}+\text{sig}^3*x(t)\left(\text{nor}(0,1)^3-3\text{nor}(0,1)\right)\frac{\Delta\text{t}^{1.5}}{6}$
OK, I have put this this into MC code. Looking at it I see that it is Euler plus extra terms of order O(dt) and
O(dt^3/2). Intuitively, accuracy will be similar to Euler, which is borne out on the example (put). If anything, Euler
is very very slightly more accurate.K = 10, S=5, r = 0.12, sig = 0.5, T = 1.I can try other use cases but at this stage
I am curious on how to proceed. // One thing I do miss is that all of a sudden the schemes no longer explicitly use
Hermite polynomials.For the record, this scheme is incorrect?(?) Please verify and suggest a fix.
```

---

### #80 — Amin (Topic Author)
*May 19, 2016, 8:45 AM*

Sorry bad post.

---

### #81 — Amin (Topic Author)
*May 19, 2016, 2:01 PM*

Sorry, bad post.

---

### #82 — Amin (Topic Author)
*May 20, 2016, 10:15 AM*

QuoteOriginally posted by: AminIn stochastic calculus of standard deviations, we divide the normal density of standard
brownian motion into a large number of subdivisions measured in terms of standard deviations (as difference of standard
deviations which are units of normal density). These subdivisions remain constant when measured in terms of standard
deviations but expand in time in absolute terms with increasing variance such that probability mass in each sub division
remains exactly the same at any point in the evolution of the density. Each subdivision can be considered as a branch of
a non-recombining tree so that number of branches(or subdivisions) remain exactly the same from the start from origin to
expiry at any future time. Each branch expands straight in the direction of the same realization of normal(measured
again in standard deviations) but expanding and moving out due to increase in variance with t. In stochastic calculus of
standard deviations, these branches do not interact, and stochastic calculus is applied on each branch independently.
Here we use n as index for number of branches of the tree with each subdivisions/branch of equal width${\Delta X0}$ so
that$n{\Delta X0}$ ranges typicaly between -5 to 5, the entire range of normal with constant increments of${\Delta X0}$
between successive subdivisions. At any time in the evolution of the tree, we have that centre of nth branch or
subdivision is given by$X_n(t)=n \Delta\text{X0} \sqrt{t}$ The absolute width of each of these subdivisions is given as
$\Delta\text{X0} \sqrt{t}$ Since probability mass in each of these subdivisions remain constant as a function of time,
we can apply the formulas as
$\int _{X_n(t)-.5\Delta\text{X0} \sqrt{t}}^{X_n(t)+.5\Delta\text{X0} \sqrt{t}} f(X(t))dX(t)=\int _{X_n(s)-.5\Delta\text{X0} \sqrt{s}}^{X_n(s)+.5\Delta\text{X0} \sqrt{s}}f(X(s))dX(s)$
or any two times s or t.For the case of evaluation of powers of Normal in case of hermite polynomials, we have to
analytically evaluate the integrals of the kind for power p
$\int _{X_n(t)-.5\Delta\text{X0} \sqrt{t}}^{X_n(t)+.5\Delta\text{X0} \sqrt{t}}(X(t))^p f(X(t))dX(t)$ and we have to
calculate, for the evolution from density at time s to density at time t, the following integrals
$\int _{X_n(t)-.5\Delta\text{X0} \sqrt{t}}^{X_n(t)+.5\Delta\text{X0} \sqrt{t}}(X(t))^p f(X(t))dX(t)-\int _{X_n(s)-.5\Delta\text{X0} \sqrt{s}}^{X_n(s)+.5\Delta\text{X0} \sqrt{s}}(X(t))^p f(X(s))dX(s)$
where$f(X(t))=\frac{1}{\sqrt{2 \text{Pi} t}}\text{Exp}\left[-.5\frac{\left(X\right){}^2}{t}\right]$ The above formulas
help us find the constants that multiply with powers of Z in the analysis of stochastic calculus of standard
deviations.The above discussion was for stochastic calculus of standard deviations applied to evolution of normal
density. For a general SDE, we simply follow the previous discussion in the thread and subdivisions expand nonlinearly
but we make use of fact that evolution of standard normal density employed in the evolution of general nonlinear SDE is
independent of evolution of any nonlinear SDE.The code I gave above in a recent post was an initial demonstration and
the constants in that code will change now.Ok now we follow the above analysis to retrieve the first order term in Z. We
include volatility here for more clarity. Integrating the density over each small subdivision, we get the following.
$\int _{X_n(t)-\sigma \Delta\text{X0} \sqrt{t}}^{X_n(t)+\sigma \Delta\text{X0} \sqrt{t}} f(X(t))dX(t)$
$=-0.5 \text{Erf}[\text{dX0} (-0.353553+0.707107 n)]+0.5 \text{Erf}[\text{dX0} (0.353553 +0.707107 n)]$ Eq(1)Now, we
find the difference of integrals over first power of Z in each subdivision, as in the equation of below
$\int _{X_n(t)-\sigma \Delta\text{X0} \sqrt{t}}^{X_n(t)+\sigma \Delta\text{X0} \sqrt{t}}X(t) f(X(t))dX(t)-\int _{X_n(t)-\sigma \Delta\text{X0} \sqrt{s}}^{X_n(t)+\sigma \Delta\text{X0} \sqrt{s}}X(s) f(X(s))dX(s)$
$=0.398942 e^{-\text{dX0}^2 \left(0.25 + n^2\right)} \left(- e^{0.5 \text{dX0}^2 (-0.5+n)^2}+e^{0.5 \text{dX0}^2 (0.5 +n)^2}\right) \sigma \left( \sqrt{t}-\sqrt{\text{t0}}\right)$
Eq(2)Before we use the above equation, we have to divide by the probability mass in each subdivision. This is due to an
application of conditional Bayes Law.I would like to mention that above Z is totally different from the one I used in
the program I distributed earlier. Once you use the above Z, your mean would be within a few basis points of the true
mean if you just change the 1st order z term and keep the wrong higher order terms.I will like to tell friends that
X_n(t)must not be used as a mean of each subdivision as I had earlier indicated in a post that I have now corrected. A
corrected program will follow soon over the weekend.The values for other powers of Z in stochastic calculus of standard
deviations can be very similarly calculated.

---

### #83 — Amin (Topic Author)
*May 20, 2016, 11:40 AM*

Here is the new matlab program for Stochastic Calculus of Standard Deviations. The integration of density is a very
rough summation just to give an idea.function [] = SDEXticsInfinitiTechnologiesCEVNoise02_Public( )X0_max=800;%Total
number of SD Fractions.X0_mid=400.5;%Mid of the SD Grid. Lies at z0 by definition.X0_mid0=400;X0_start=1;
dX0=.0125;%Width of SD cells in terms of Standard Deviations.              T_index=200*1; dt=.005/1.0;
epsilon=0.750gamma=1.0;z0=1.0;dz_integral1(1:X0_max)=z0;dz_integral2(1:X0_max)=z0;iivector(1:X0_max)=1:X0_max;paths=1000000;
%No. of Paths for creation of Monte Carlo density by simulating z, F(z);zz4(1:paths)=z0;
const=.398942*exp(-dX0^2.*(.25+(iivector-X0_mid).^2)).*(-exp(.5*dX0^2.*(-.5+(iivector-X0_mid)).^2)+exp(.5*dX0^2.*(.5+(iivector-X0_mid)).^2));;
const2=.398942*(dX0.*exp(-.5*dX0^2.*(.5+(iivector-X0_mid)).^2).*(-.5-(iivector-X0_mid))+...
dX0.*exp(-.5*dX0^2.*(-.5+(iivector-X0_mid)).^2).*(-.5+(iivector-X0_mid))-...
1.25331*erf(dX0.*(-.353553+.707107*(iivector-X0_mid)))+...
1.25331*erf(dX0.*(.353553+.707107*(iivector-X0_mid)))); for nn=1:T_index
%Loop over time.    t=(nn)*dt;      t0=(nn-1)*dt;
prob=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)/(sqrt(t)*epsilon);        %Probability in each SD Grid cell.
prob2=exp(-.5*((iivector-X0_mid).*dX0).^2)./sqrt(22/7.0*2.0)*dX0;     dt=t-t0;        dz_integral2=dz_integral2+...
epsilon.*dz_integral2.^gamma.*(sqrt(t)-sqrt(t0)).*const./prob2...
+epsilon.*gamma.*dz_integral2.^(gamma-1).*(epsilon.*dz_integral2.^(gamma)).*(t-t0)/2.0.*((const2./prob2.*dX0.^1-1))...
+.5*epsilon.*gamma.*(gamma-1).*dz_integral2.^(gamma-2).*epsilon.^2.*dz_integral2.^(2*gamma).*(t.^1.5-t0.^1.5)./sqrt(3).*const./prob2.*dX0;
%Naive brute force Monte carlo part follows. Since the steps are extremely    %short the monte carlo is uite close to
the right density for most of the cases     %but may be off for a very small number of cases but it is a good initial
%check on our analytic density       Random1=randn(size(zz4));      RandTemp1=Random1.*sqrt(dt);    zz4
=zz4+zz4.^gamma.*RandTemp1*epsilon;        zz4(zz4');     end

---

### #84 — Amin (Topic Author)
*May 20, 2016, 7:08 PM*

The above program is still ad hoc for second order term. But I hope to finish everything regarding the stochastic
calculus of standard deviations over the weekend. For those friends who would like to do things on their own, we take a
jacobian(change of variable in the density) between mid points so values of Z, Z^2  or Z^n, must be computed at the mid
of each subdivision. I will also mention that integrals have to be calculated for finding conditional values of noise or
its powers since it could not be easily possible to calculate conditional values along a certain standard deviation line
without integration. Z^2 and higher powers need special treatment since average value of Z^2 over the integration
interval differs from the value of Z^2 at the mid-point. I hope to fix all these minor issues over the weekend.

---

### #85 — Amin (Topic Author)
*May 22, 2016, 9:18 AM*

I may not be able to get anything definitive done for a few more days since my computers are being hacked actively.
However I am very confident of the future roadmap for finessing the technique and would write it here for the friends
who want to do it on their own. Most of the work has been done but I do think there has to be an integration, at least
for higher order terms(where I naiively multiplied by dX0 in my program) on the sde variable itself(as opposed to
integrations of normal z and z^2 that we have been doing) and this integration will have to be done taking into account
limits of the non-linear subdivisions dubbed as dz_integral in the program i.e limits of this integration would be ends
of each subdivision of dz-integral. The reader should make the observation that subdivisions of SDE variable named as
dz_integral are non-linear as opposed to linear independent subdivisions of z. This integration probably has to be done
at the start of the time interval t0(in my program) only. Please try replacing the time zero value of SDE variable terms
at the start of the time interval(in terms of order t and t^1.5) by their integrated value at start of the interval.For
example try integrating second order quadratic variation
.5*epsilon*gamma*(gamma-1)*dz_integral.^(gamma-2).*epsilon.^2*dz_integral.^(2*gamma) at time t0 between ends of each
subdivision of dz_integral2.I wish I could have worked but all my computers are badly bugged and my programs are altered
at will. I will write more about it in my off-topic thread.

---

### #86 — Cuchulainn
*May 22, 2016, 9:30 AM*

Well, you are able to communicate freely on Wilmott. You seem to be using/learning well-known result in numerical
quadrature.

---

### #87 — Amin (Topic Author)
*May 29, 2016, 9:03 AM*

Since it may not be possible for me to complete a full worked out paper, in just a few days, whose scope was decided by
me to include applications of the new method of solution of stochastic differential equations to monte carlo simulation
of the stochastic differential equations, transition probability simulation of the density and calculation of density of
functionals of stochastic differential equation and finally to the evolution of density of SDEs with stochastic calculus
of standard deviations. I will make a bare bone initial online copy of the paper available on SSRN detailing the
foundation of the breakthrough applied to SDEs. I will then take a few more weeks to complete the work required to
achieve the scope of the paper.However since there are other applications of the new method to other branches of
mathematics like solution of ordinary differential equations and extensions to solution of partial differential
equations which are not of immediate concern to me to write a research paper, I will make a bare bone initial online
copy of the paper available on SSRN detailing the foundation of the breakthrough applied to SDEs(and that can be adapted
to ODEs just with parallel mathematics), so other people who want to publish their research, could give me credit for my
work to solution of stochastic differential equations in general when they publish more advanced research based on the
application of breakthrough to solution of stochastic differential equations, ordinary differential equations, or
partial differential equations. I hope to make the online copy of the initial draft available on Tuesday 31st May.

---

### #88 — Amin (Topic Author)
*May 30, 2016, 5:06 AM*

Sorry it may take a few more days before I could make a basic draft available. But for other genuine researchers who
want to write their own research papers and submit for publication etc, I would say that you could give me credit for my
work by making the following citation,"On the expansion of variable coefficients of an ordinary differential equation or
a stochastic differential equation in the form of a series of iterated integrals with constant integrands with
applications towards solution of Stochastic Differential Equations and their functionals." by Ahsan Amin.Thank you.

---

### #89 — Amin (Topic Author)
*June 2, 2016, 6:49 AM*

Though I think most intelligent friends would already have realized how my expansion of variable coefficients into
iterated integrals with constant integrands in the case of SDEs as I have shown in the previous discussion applies to
ODEs, I will still like to give a general example.we have an ODE of the form$\frac{dX}{dt}=a(X)+b(X)$ Eq(1)where a(X)
and b(X) are totally general variable coefficients.In order to make exposition more clear, we emphasize the implicit
dependence of X on t. X depends on t but not necessarily explicitly and a(X) and b(X) are coefficients that depend
explicitly on X but would usually have dependence on t only through implicit dependence of X on t.
$\frac{dX(t)}{dt}=a(X(t))+b(X(t))$ Eq(2)We start at time t=t0 and want to find the value of X at a t=t1.We have for
variable coefficient a(X)
$a(X(t))=a(X(\text{t0}))+\int _{\text{t0}}^{\text{t}}\frac{\partial (a(X(t))}{\partial X}\frac{dX(t)}{dt}\text{dt}$
Eq(3)Let us see how we can improve on this expansion
$\frac{\partial (a(X(t)))}{\partial X}\frac{dX(t)}{dt}=\frac{\partial (a(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}+\int _{\text{t0}}^{\text{t}}\frac{\partial }{\partial X}\left(\frac{\partial (a(X(t))}{\partial X}\frac{dX(t)}{dt}\right)\frac{dX(t)}{dt}dt$
Eq(4)substituting eq(4) in Eq(3), we get
$a(X(t))=a(X(\text{t0}))+\int _{\text{t0}}^{\text{t}}\frac{\partial (a(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\text{dt}+\int _{\text{t0}}^{\text{t}}\int _{\text{t0}}^{\text{t}}\frac{\partial }{\partial X}\left(\frac{\partial (a(X(t))}{\partial X}\frac{dX(t)}{dt}\right)\frac{dX(t)}{dt}\text{dt} \text{dt}$
Similarly, we can expand again to find.
$a(X(t))=a(X(\text{t0}))+\int _{\text{t0}}^{\text{t}}\frac{\partial (a(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\text{dt}+\int _{\text{t0}}^{\text{t}}\int _{\text{t0}}^{\text{t}}\frac{\partial }{\partial X}\left(\frac{\partial (a(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\right)\frac{dX(\text{t0})}{dt}\text{dt} \text{dt} + Third order Iterated Integral $
Since$\frac{\partial (a(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}$ and
$\frac{\partial }{\partial X}\left(\frac{\partial (a(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\right)\frac{dX(\text{t0})}{dt}$
are constants, we can write$X(\text{t1})=X(\text{t0})+$
$a(X(\text{t0}))\int _{\text{t0}}^{\text{t1}}\text{dt}+\left(\frac{\partial (a(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\right)\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\text{dt} \text{dt}+\left(\frac{\partial }{\partial X}\left(\frac{\partial (a(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\right)\frac{dX(\text{t0})}{dt}\right)\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\text{dt} \text{dt}$
$+b(X(\text{t0}))\int _{\text{t0}}^{\text{t1}}\text{dt}+\left(\frac{\partial (b(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\right)\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\text{dt} \text{dt}+\left(\frac{\partial }{\partial X}\left(\frac{\partial (b(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\right)\frac{dX(\text{t0})}{dt}\right)\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\text{dt} \text{dtdt}$
We have to realize that the higher order terms(>3 in the above equation) continue and their addition will continue to
add more accuracy. Many mathematicians would have realized that dt integral terms when considered alone without constant
coefficients converge to exponential of dt. But we have now constant weights on each term of the Taylor expansion of the
exponential and this expansion with constant weights gets equated with the solution of ODEs with variable coefficients.
Please note that this method can be used for other kind of ODES like 2nd order with variable coefficients and many other
ODEs and so on. You could probably use it for many PDEs as well. You have to be ingenious.Is it(for ODEs) not exactly
the same methodology and same series of steps what we have been doing for SDEs in this thread.

---

### #90 — Cuchulainn
*June 2, 2016, 7:34 AM*

Quotewhere a(X) and b(X) are totally general variable coefficients.In that case we do not know if ODE (1) has a (unique)
solution in some interval. (1) can be coalesced todX/dt = f(X).For ODE a more general, non-autonomous ODEdX/dt =
f(X,t)Caveat: there is a huge literature on ODE solvers so you run risk of 1) reinvent wheel 2) suboptimal divergent
schemes 3)  ~ reinvent random ODEs are well-known as in one of my post below. QuoteYou have to be ingenious.Oops. It
feels like juggling with symbols, which is not the same as mathematical analysis..

---

### #91 — Amin (Topic Author)
*June 2, 2016, 7:50 AM*

Cuch, you have to talk to a few good mathematicians and see what they have to say. If I were you, I would not start
giving negative opinions before doing a bit of solid research about it and asking a few mathematician friends. I would
encourage you to do that to find on your own.

---

### #92 — Cuchulainn
*June 2, 2016, 7:59 AM*

QuoteOriginally posted by: AminCuch, you have to talk to a few good mathematicians and see what they have to say. If I
were you, I would not start giving negative opinions before doing a bit of solid research about it and asking a few
mathematician friends. I would encourage you to do that to find on your own.Sure.  Can you recommend one?

---

### #93 — Amin (Topic Author)
*June 2, 2016, 9:33 AM*

QuoteOriginally posted by: CuchulainnFor ODE a more general, non-autonomous ODEdX/dt = f(X,t)It does not take a great
mathematical vision to see that the above ODE can very easily be solved by the above method. It just would not have
constant integrands as we see for the simplest type.Cuch, I leave it as an exercise for you to solve the problem in
light of simple ODE I solved.

---

### #94 — Cuchulainn
*June 2, 2016, 9:36 AM*

QuoteOriginally posted by: AminQuoteOriginally posted by: CuchulainnFor ODE a more general, non-autonomous ODEdX/dt =
f(X,t)It does not take a great mathematical vision to see that the above ODE can very easily be solved by the above
method. It just would not have constant integrands as we see for the simplest type.Cuch, I leave it as an exercise for
you to solve the problem in light of simple ODE I solved.When is the deadline? Looks like it's similar to a multistep
method

---

### #95 — Amin (Topic Author)
*June 2, 2016, 9:53 AM*

QuoteOriginally posted by: CuchulainnWhen is the deadline? It took me less than ten minutes to scribble a few equations
to see that the very general ODE you mentioned can be exactly solved to any order of accuracy by the method of iterated
integrals that I have proposed.

---

### #96 — Cuchulainn
*June 2, 2016, 10:07 AM*

Quoteexactly solved to any order of accuracy by the method of iterated integralsThat's the part my simple numerical
analysis brain does not understand. It seems too good to be true.

---

### #97 — Cuchulainn
*June 2, 2016, 11:14 AM*

Quotewe have an ODE of the form$\frac{dX}{dt}=a(X)+b(X)$ Eq(1)$X(\text{t1})=X(\text{t0})+$
$a(X(\text{t0}))\int _{\text{t0}}^{\text{t1}}\text{dt}+\left(\frac{\partial (a(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\right)\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\text{dt} \text{dt}+\left(\frac{\partial }{\partial X}\left(\frac{\partial (a(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\right)\frac{dX(\text{t0})}{dt}\right)\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\text{dt} \text{dt}$
$+b(X(\text{t0}))\int _{\text{t0}}^{\text{t1}}\text{dt}+\left(\frac{\partial (b(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\right)\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\text{dt} \text{dt}+\left(\frac{\partial }{\partial X}\left(\frac{\partial (b(X(\text{t0}))}{\partial X}\frac{dX(\text{t0})}{dt}\right)\frac{dX(\text{t0})}{dt}\right)\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\int _{\text{t0}}^{\text{t1}}\text{dt} \text{dtdt}$
Let's take the simplest scalar ODE a(X) = X, b(X) == 0, X(0) = 1. Then we get X(t) = exp(t). (3)AGREE?And using your
notationX(t_1) = d(t_1,t_0) * X(t_0) where d(t1, t_0) = exp(t_1 - t_0). Expand d(t_1, t_0) to give Pade(n,m)
approximant. Yours seems to be (1,0) which means conditionally stable. (dt = t_1 - t_0)I cannot see how your stuff and
my equation (3) are similar.

---

### #98 — Amin (Topic Author)
*June 2, 2016, 3:46 PM*

Let us give this new method a formal name. What about "Method of Iterated Integrals" to solve ODEs and SDEs and might
even have more limitless possiblities in Mathematics.

---

### #99 — Cuchulainn
*June 2, 2016, 6:29 PM*

QuoteOriginally posted by: AminLet us give this new method a formal name. What about "Method of Iterated Integrals" to
solve ODEs and SDEs and might even have more limitless possiblities in Mathematics.Don't forget PDEs. I can't see how,
but maybe we should ask someone.

---

### #100 — Amin (Topic Author)
*June 5, 2016, 8:04 AM*

You could easily apply the method of iterated integrals for the evaluation of integrals. I will give a general example
and later we will see in an application that many integrals like for example, fourier, laplace, mellin and other
transforms can be very easily calculated by the method sometimes even when the closed form formulas for those transforms
do not exist.Let us consider an integral of the form$g(k)=\int _a^bf(k,x)\text{dx}$ Eq(1)Just like we did in the
expansion of ODE coefficients, we can write the function f(k,x) as
$f(k,x)=f(k,x(a))+\int _a^b\frac{\partial f(k,x)}{\partial x}\text{dx}$ Eq(2)Expanding further two terms one by one, we
get the equation
$f(k,x)=f(k,x(a))+\int _a^b\frac{\partial f(k,x(a))}{\partial x}\text{dx}+\int _a^b\int _a^b\frac{\partial ^2f(k,x(a))}{\partial x^2}\text{dxdx}\text{++}\int _a^b\int _a^b\int _a^b\frac{\partial ^3f(k,x)}{\partial x^3}\text{dxdxdx}$
Eq(3)Now we put Eq(3) in the integral in Eq(1) to get
$g(k)=\int _a^bf(k,x(a))\text{dx}+\int _a^b\int _a^b\frac{\partial f(k,x(a))}{\partial x}\text{dxdx}+\int _a^b\int _a^b\int _a^b\frac{\partial ^2f(k,x(a))}{\partial x^2}\text{dxdxdx}+\text{higher order terms}$
$=f(k,x(a))\int _a^b\text{dx}+\frac{\partial f(k,x(a))}{\partial x}\int _a^b\int _a^b\text{dxdx}+\frac{\partial ^2f(k,x(a))}{\partial x^2}\int _a^b\int _a^b\int _a^b\text{dxdxdx}+\text{higher order terms}$
Eq(4)One could observe the similarity with expansion of ODE and SDE coefficients when one would look at similar iterated
integrals and constant coefficients.our function f(k,x) can have many many simpler forms. For example Eq(1) could be
$g(k)=\int _a^be^{i \text{kx}}h(x)\text{dx}$$g(k)=\int _a^bv(k,x)h(x)\text{dx}$ Just like exponential of very large
numbers, we might have to take very large number of terms in expansion to get complete convergence for difficult
transforms though the problem should not be severe for most of the transform integrals. But when the solution of a
difficult transform has to be found, one could easily divide the integration domain into 4, 8, or 16 subdivisions and
locally apply the method of iterated integrals. This could also work very well for numerical calculation of transforms
where one could find transform locally in each of the subdivisions by the formula by expanding upto 5-6 terms and then
patch the solutions together across different subdivisions.We can see that after calculation of fourier/laplace
transform, our transform could be in the form of sum of terms of the kind$a e^{b k}k^n$ Eq(5) where a and b are
arbitrary constants and n is arbitrary power. The way we generally find the solution of a PDE by transforms could now be
modified by taking a general solution of for the term given by equation (5) above (by for example substituting in the
PDE) and finding a complete solution by the principle of superposition of different terms. As complexity increases,
there could be many modifications on the theme I mentioned limited only by ingenuity of the mathematician.

---

[← Previous](page_001.md) | [Index](index.md) | [Next →](page_003.md)
