# Broken LaTeX Posts

Total: 46 posts with errors

---

## Error 1: Unbalanced $$: 1

**Snippet:** `I will try to give wilmott friends an idea about my new research on stochastic d`

**Full content:**

```
I will try to give wilmott friends an idea about my new research on stochastic differential equations and their simulation. My formal research paper will be ready in a week but I will present some preview details about the research for the friends for discussion.Let us write a simple stochastic differential equation in the general form with a finite step here as $x(t)=\int _0^t\mu (x(t)) \text{dt}+\int _0^t\sigma (x(t)) \text{dz}(t)\text{     }\text{Eq (1)}$When we simulate the above stochastic differential equation, the simplest method is to freeze the drift and volatility coefficients at their initial value, and multiply with dt and Normal(sqrt(t)) as $x(t)=\mu (x(0)) \text{dt}+\sigma (x(0)) \text{sqrt}(t)z.$Though many better techniques exist to simulate the stochastic differential equations for a finite step or to find their density, most of them lack generalization and have to be applied in special settings. We derive a generic new method that can simulate even non-linear stochastic differential equations to arbitrary accuracy. The method is extremely simple and is based on the simple understanding of how the non-linear coefficient functions are changing in time. I have tried to give some intuition about it in the exposition below.Before, we embark on a full-fledged scheme for the above general SDE, we would like to give the reader some crucial insights. To give the proper insights, we would like to start by taking a normal diffusion so that we could proceed in a step by step manner $\text{dx}(s)=\sigma  \text{dz}(s)$ Eq(2)or $x(t)=x(0)+\int _0^t\sigma  \text{dz}(s)$  Eq(3)We would like to start by learning how to calculate the following time integral with extreme precision and arbitrary accuracy $I(t)=\int _0^t\mu (x(s)) \text{ds}$  Eq(4)We would also like to explain how to calculate the following stochastic integral with extreme precision and arbitrary accuracy $S(t)=\int _0^t\sigma (x(s)) \text{dz}(s)$  Eq(5)Since we want to proceed step by step, we will first calculate these integrals for a normal brownian motion as given in  Eq (2)  and after gaining intuition , we later generalize the SDE from Eq(2) to Eq(1) and calculate I(t) and  S(t) with the most general dynamics as given by Eq(1).We start by calculating I(t) as given by Eq(4) and Eq(2).$\int _0^t\mu (x(s))\text{ds}=t \mu (x(t)) -\int _0^ts d[\mu (x(s))]$ Eq(6)Expanding the second term on RHS $\int _0^ts d[\mu (x(s))]=\int _0^t \frac{\partial \mu (x(s))}{\partial x}s\sigma\text{dz}(s)+.5\int _0^t \frac{\partial ^2\mu (x(s))}{\partial x^2}s\sigma ^2 \text{ds}$ Eq(7)We know that $\frac{\partial \mu (x(s))}{\partial x}$  in first term of Eq(7)  is a function of x(s) and we can apply Ito Change of variable formula on this as $\frac{\partial \mu (x(s))}{\partial x}=\frac{\partial \mu (x(0))}{\partial x}+\int _0^s \frac{\partial ^2\mu (x(u))}{\partial x^2}\sigma\text{dz}(u)+.5\int _0^s \frac{\partial ^3\mu (x(u))}{\partial x^3}\sigma ^2 \text{du}$   Eq(8)Now we come to the most important step towards understanding of this expansion. We expand the first noise term on RHS of Eq(7) by substituting Eq(8) in it. $\int _0^t \frac{\partial \mu (x(s))}{\partial x}s\sigma\text{dz}(s)=\int _0^t \frac{\partial \mu (x(0))}{\partial x}s\sigma\text{dz}(s)+\int _0^t s \sigma\text{dz}(s)\int _0^s \frac{\partial ^2\mu (x(u))}{\partial x^2}\sigma\text{dz}(u) +\int _0^t s\sigma\text{dz}(s)\int _0^s .5 \frac{\partial ^3\mu (x(u))}{\partial x^3}\sigma ^2 \text{du}\text{  }$ Eq(9)So we have a few nested integrals and we can easily deal with them. We could continue the expansions of  $\frac{\partial ^2\mu (x(u))}{\partial x^2}$ and $\frac{\partial ^3\mu (x(u))}{\partial x^3}$  to further order just by following Eq(8) but we stop the order here for initial simplicity and explanation of the basic example. We freeze $\frac{\partial ^2\mu (x(u))}{\partial x^2}$ and $\frac{\partial ^3\mu (x(u))}{\partial x^3}$   in the above equation to their initial time zero values (we could have continued to expand them to desired accuracy if we wished) and write  Eq(9) as $\int _0^t \frac{\partial \mu (x(s))}{\partial x}s\sigma\text{dz}(s)=\frac{\partial \mu (x(0))}{\partial x}\int _0^t s\sigma\text{dz}(s)+\frac{\partial ^2\mu (x(0))}{\partial x^2}\int _0^t s \sigma\text{dz}(s)\int _0^s \sigma\text{dz}(u) +.5 \frac{\partial ^3\mu (x(0))}{\partial x^3}\int _0^t s\sigma\text{dz}(s)\int _0^s \sigma ^2 \text{du}\text{  }$  Eq(10)Now we are left to evaluation of intgrals $\int _0^t \text{s}\sigma\text{dz}(s)$  Eq(11)and double nested integrals $\int _0^t s \sigma\text{dz}(s)\int _0^s \sigma\text{dz}(u)=\int _0^t s \sigma ^2\text{  }(z(s)-z(0))\text{dz}(s)$$\int _0^t s\sigma\text{dz}(s)\int _0^s \sigma ^2 \text{du}=\int _0^t s\sigma  \left(\left.\sigma ^2 s\right)\text{dz}(s)\right.$None of the above nested integrals vanishes and their continuations do not go to zero. I have devised schemes in my research that can calculate all different types of above integrals with arbitrary complexity of nesting to perfect precision using very simple integral calculus in a form that is a function of only time t, and a unit gaussian.We would similarly expand the second term of Eq(7) on RHS using Ito expansion of $\frac{\partial ^2\mu (x(s))}{\partial x^2}$ and substituting it in Eq(7) . We will freeze the coefficients of above expansion at time zero like we did to get Eq(10) and get different integrals like Eq(11-13). All these stochastic integrals can be trivially solved by scheme I have devised in my research.To be continued tomorrow. Sorry, tired of writing more at the moment.  
```

---

## Error 2: Unbalanced $$: 9

**Snippet:** `Daniel, I will do simple math behind the sde you are simulating. Here is the equ`

**Full content:**

```
Daniel, I will do simple math behind the sde you are simulating. Here is the equation that we expanded just one level more than traditional monte carlo. This is equation right after equation six in previous post. I will write it again.$x(t)=x(0)+\mu (x(0))\int _0^t\text{ds}+\frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\int _0^t\int _0^s \text{dvds}+\frac{\partial \mu (x(0))}{\partial x}\sigma (x(0))\int _0^t\int _0^s \text{dz}(v)\text{ds}+.5\frac{\partial ^2\mu (x(0))}{\partial x^2}\sigma ^2(x(0)) \int _0^t\int _0^s  \text{dv} \text{ds}$$+\sigma (x(0))\int _0^t\text{dz}(s)+\frac{\partial \sigma (x(0))}{\partial x}\mu (x(0))\int _0^t\int _0^s \text{dvdz}(s)+\frac{\partial \sigma (x(0))}{\partial x}\sigma (x(0))\int _0^t\int _0^s \text{dz}(v)\text{dz}(s)+.5\frac{\partial ^2\sigma (x(0))}{\partial x^2}\sigma ^2(x(0))\int _0^t\int _0^s\text{dv}\text{dz}(s)$  Eq(1)I have tried to use your notation.we use $\mu\text{(x(0))=(r-d)x(0)}$$\frac{\partial \mu (x(0))}{\partial x}\text{=(r-d)}$$\frac{\partial ^2\mu (x(0))}{\partial x^2}\text{=0}$$\sigma\text{(x(0))= sig x(0)}$$\frac{\partial \sigma (x(0))}{\partial x}\text{=sig}$$\frac{\partial ^2\sigma (x(0))}{\partial x^2}\text{=0}$substituting the above values in Eq(1), we get $x(t)=x(0)+(r-d)x(0) \Delta\text{t}+(r-d)^2x(0)\frac{\Delta\text{t}^2}{2}+(r-d)\text{sig} x(0)\int _0^t\int _0^s \text{dz}(v)\text{ds}$$+\text{sig} x(0)\text{nor}(0,1)\sqrt{\Delta\text{t}}+\text{sig} (r-d)x(0)\int _0^t\int _0^s \text{dvdz}(s)+\text{sig}^2 x(0)\int _0^t\int _0^s \text{dz}(v)\text{dz}(s)$We use the identities $\int _0^t\int _0^s \text{dz}(v)\text{ds}=\int _0^t\int _0^s \text{dvdz}(s)=\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$and $\int _0^t\int _0^s \text{dz}(v)\text{dz}(s)=\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t}}{2}$Now we can get the monte carlo simulation scheme.$x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)^2x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$$+\text{sig}^2x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t}}{2}$The above is order $\Delta\text{t}$ accurate with some terms of higher order. Adding one more term that comes from further expansion will take the order to  $\Delta\text{t}$^1.5.   The new better scheme would be $x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)(r-d)x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2*\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$$+\text{sig}^2*x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t} }{2}+\text{sig}^3*x(t)\left(\text{nor}(0,1)^3-3\text{nor}(0,1)\right)\frac{\Delta\text{t}^{1.5}}{6}$  
```

---

## Error 3: Unbalanced $$: 1

**Snippet:** `QuoteAdding one more term that comes from further expansion will take the order `

**Full content:**

```
QuoteAdding one more term that comes from further expansion will take the order to  $\Delta\text{t}$^1.5.   The new better scheme would be $x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)(r-d)x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2*\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$$+\text{sig}^2*x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t} }{2}+\text{sig}^3*x(t)\left(\text{nor}(0,1)^3-3\text{nor}(0,1)\right)\frac{\Delta\text{t}^{1.5}}{6}$OK, I have put this this into MC code. Looking at it I see that it is Euler plus extra terms of order O(dt) and O(dt^3/2). Intuitively, accuracy will be similar to Euler, which is borne out on the example (put). If anything, Euler is very very slightly more accurate.K = 10, S=5, r = 0.12, sig = 0.5, T = 1.I can try other use cases but at this stage I am curious on how to proceed. // One thing I do miss is that all of a sudden the schemes no longer explicitly use Hermite polynomials.   
```

---

## Error 4: Unbalanced $$: 9

**Snippet:** `QuoteOriginally posted by: AminDaniel, I will do simple math behind the sde you `

**Full content:**

```
QuoteOriginally posted by: AminDaniel, I will do simple math behind the sde you are simulating. Here is the equation that we expanded just one level more than traditional monte carlo. This is equation right after equation six in previous post. I will write it again.$x(t)=x(0)+\mu (x(0))\int _0^t\text{ds}+\frac{\partial \mu (x(0))}{\partial x}\mu (x(0))\int _0^t\int _0^s \text{dvds}+\frac{\partial \mu (x(0))}{\partial x}\sigma (x(0))\int _0^t\int _0^s \text{dz}(v)\text{ds}+.5\frac{\partial ^2\mu (x(0))}{\partial x^2}\sigma ^2(x(0)) \int _0^t\int _0^s  \text{dv} \text{ds}$$+\sigma (x(0))\int _0^t\text{dz}(s)+\frac{\partial \sigma (x(0))}{\partial x}\mu (x(0))\int _0^t\int _0^s \text{dvdz}(s)+\frac{\partial \sigma (x(0))}{\partial x}\sigma (x(0))\int _0^t\int _0^s \text{dz}(v)\text{dz}(s)+.5\frac{\partial ^2\sigma (x(0))}{\partial x^2}\sigma ^2(x(0))\int _0^t\int _0^s\text{dv}\text{dz}(s)$  Eq(1)I have tried to use your notation.we use $\mu\text{(x(0))=(r-d)x(0)}$$\frac{\partial \mu (x(0))}{\partial x}\text{=(r-d)}$$\frac{\partial ^2\mu (x(0))}{\partial x^2}\text{=0}$$\sigma\text{(x(0))= sig x(0)}$$\frac{\partial \sigma (x(0))}{\partial x}\text{=sig}$$\frac{\partial ^2\sigma (x(0))}{\partial x^2}\text{=0}$substituting the above values in Eq(1), we get $x(t)=x(0)+(r-d)x(0) \Delta\text{t}+(r-d)^2x(0)\frac{\Delta\text{t}^2}{2}+(r-d)\text{sig} x(0)\int _0^t\int _0^s \text{dz}(v)\text{ds}$$+\text{sig} x(0)\text{nor}(0,1)\sqrt{\Delta\text{t}}+\text{sig} (r-d)x(0)\int _0^t\int _0^s \text{dvdz}(s)+\text{sig}^2 x(0)\int _0^t\int _0^s \text{dz}(v)\text{dz}(s)$We use the identities $\int _0^t\int _0^s \text{dz}(v)\text{ds}=\int _0^t\int _0^s \text{dvdz}(s)=\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$and $\int _0^t\int _0^s \text{dz}(v)\text{dz}(s)=\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t}}{2}$Now we can get the monte carlo simulation scheme.$x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)^2x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$$+\text{sig}^2x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t}}{2}$The above is order $\Delta\text{t}$ accurate with some terms of higher order. Adding one more term that comes from further expansion will take the order to  $\Delta\text{t}$^1.5.   The new better scheme would be $x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)(r-d)x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2*\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$$+\text{sig}^2*x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t} }{2}+\text{sig}^3*x(t)\left(\text{nor}(0,1)^3-3\text{nor}(0,1)\right)\frac{\Delta\text{t}^{1.5}}{6}$Neither scheme is an improvement on Euler in any way.. Believe me. I won't be posting numbers because they all the same. The schemes fall short for MC simulation. Most disconcerting is that convergence is erratic and not monotone.QuoteI added a higher order term quickly thinking it might add to accuracyAnd it might not.       
```

---

## Error 5: Unbalanced $$: 1

**Snippet:** `QuoteOriginally posted by: AminDaniel, I think I explained two or three times th`

**Full content:**

```
QuoteOriginally posted by: AminDaniel, I think I explained two or three times that O(dt^3/2) as I wrote was bad and did not have a proper order since all terms required to achieve order were not added. When I wrote O(dt) scheme which is exact and right , I was tempted to add a term of noise that was in powers of dt^3/2 but all terms from previous order or level had to be added to get a consistent scheme. I am sure you can easily do simple math to find the correct O(dt^3/2) scheme by following the discussion. The numbers I gave and you have quoted in your previous post are from O(dt) scheme as I had mentioned which is good.Well, the O(dt^3/2) does seem to converge. So, I don't think is the issue is what it seems to be.I also tested your O(dt) scheme and it also take 100 million draws to get near to the exact put.  is this scheme correct?Now we can get the monte carlo simulation scheme.$x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)^2x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$$+\text{sig}^2x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t}}{2}$The above is order $\Delta\text{t}$ accurate with some terms of higher order.   
```

---

## Error 6: Unbalanced $$: 1

**Snippet:** `QuoteOriginally posted by: CuchulainnQuoteAdding one more term that comes from f`

**Full content:**

```
QuoteOriginally posted by: CuchulainnQuoteAdding one more term that comes from further expansion will take the order to  $\Delta\text{t}$^1.5.   The new better scheme would be $x(t+\Delta\text{t})=x(t)+(r-d)*x(t) \Delta\text{t}+(r-d)(r-d)x(t)\frac{\Delta\text{t}^2}{2}+\text{sig}* x(t)\text{nor}(0,1)\sqrt{\Delta\text{t}}+2*\text{sig}* (r-d)x(t)\text{nor}(0,1)\frac{\Delta\text{t}^{1.5}}{\sqrt{3}}$$+\text{sig}^2*x(t)\left(\text{nor}(0,1)^2-1\right)\frac{\Delta\text{t} }{2}+\text{sig}^3*x(t)\left(\text{nor}(0,1)^3-3\text{nor}(0,1)\right)\frac{\Delta\text{t}^{1.5}}{6}$OK, I have put this this into MC code. Looking at it I see that it is Euler plus extra terms of order O(dt) and O(dt^3/2). Intuitively, accuracy will be similar to Euler, which is borne out on the example (put). If anything, Euler is very very slightly more accurate.K = 10, S=5, r = 0.12, sig = 0.5, T = 1.I can try other use cases but at this stage I am curious on how to proceed. // One thing I do miss is that all of a sudden the schemes no longer explicitly use Hermite polynomials.For the record, this scheme is incorrect?(?) Please verify and suggest a fix. 
```

---

## Error 7: Unbalanced $: 61

**Snippet:** `I had been working to include some material on solution of systems of possibly n`

**Full content:**

```
I had been working to include some material on solution of systems of possibly non-linear ordinary higher order differential equations in my paper. I have written some mathematica code for the solution of system of m ordinary differential equations each of which could have different order and the code would solve the system. I have tried it on a system of three second order non-linear differential equations. Here are the system ODEs and the mathematica code.



The system of three 2nd order ODEs is given as 

1.   $y_1''=-.5y_1'{}^2-y_1'$,  $y_1(0)=0$,  $y_1'(0)=2$

2.   $y_2''=-.5y_2'{}^2-y_1'y_2'-y_2'$,  $y_2(0)=0$,  $y_2'(0)=-3$

3.   $y_3''=-y_3'{}^2-y_1'y_3'-y_2'y_3'-y_3'$,  $y_3(0)=0$,  $y_3'(0)=-2$



Here is the paper that has analytical solution of the above system: http://file.scirp.org/pdf/AM_2014021310154871.pdf I matched the constants in the analytical solution with the initial values of derivatives for each ODE in the system as used in my code and found exactly the same series expansion for the solution as given by analytical answer in the above paper.





Here is the mathematica code for general system of m equations with each equation having its own arbitrary order.

1.  $Clear[t, y, Zi, Wi, Yi, Y, y0, i, i1, l, m, n, p, j, k, p, ZAns]$

2.  $m=3;$

3.  $Array[n, m, 0]$

4.  $n[0] = 2;$

5.  $n[1] = 2;$

6.  $n[2] = 2;$

7.  $nmax = 2;$

8.  $Array[y, {m, nmax + 1}, {0, 0}]$

9.  $y[0,2]\text{:=}-.5y[0,1]^2-y[0,1];$

10.$y[1, 2] := -.5 y[1, 1]^2 - y[1, 1] y[0, 1] - y[1, 1];$

11.$y[2, 2] := -y[2, 1]^2 - y[1, 1] y[2, 1] - y[0, 1] y[2, 1] - y[2, 1];$  

12.$Array[y0, {m, nmax}, {0, 0}];$ 

13.$y0[0, 0] = 0;$

14.$y0[0, 1] = 2;$

15.$y0[1, 0] = 0;$

16.$y0[1, 1] = -3;$

17.$y0[2, 0] = 0;$

18.$y0[2, 1] = -2;$

19.$Array[Y, m, 0]$

20.$\text{For}[j=0,j ti[n[j]]);]$

27.$For[j = 0, j  t);)])]$

30.$\text{For}[j=0,j ti[n[j]]);]

27. For[j = 0, j j++, (For[i = n[j], i 

      For[k = 0, k k++, (For[l = 0, l l++,

     (Zi[j, i + 1] = Zi[j, i + 1] +  D[Zi[j, i],  y[k, l]]*(y[k, l + 1] /. t -> ti[i + 1]))])]])]

28. For[j = 0, j j++, (For[i = n[j], i 

    For[k = 0, k 

      (Wi[j, i] = (Wi[j, i] /. y[k, l] -> y0[k, l]))]]])]

29. For[j = 0, j j++, (For[i = n[j], i 

    For[i1 = i, i1 >= 1,  i1--, (Yi[j, i1 - 1] =  Integrate[Yi[j, i1], {ti[i1], 0, ti[i1 - 1]}])];

    Y[j] = Y[j] + (Yi[j, 0] /. ti[0] -> t);)])]

30.For[j = 0, j j++, 

(ZAns[j] = Collect[Y[j], t, Simplify] // PolynomialForm[#, TraditionalOrder -> False] &)]*
```

---

## Error 8: Unbalanced $: 1

**Snippet:** `> I've never actually done a Picard iteration, so this was good therapy -- and p`

**Full content:**

```
> I've never actually done a Picard iteration, so this was good therapy -- and probably belongs firmly in the student forum, but whatever.
> 
> 
> 
> It seems that the Picard iterates will agree with "my" perturbation expansion for linear problems, but all bets are off for nonlinear cases.  So if I can examine a nonlinear example where the two differ, then I should be able to rule out one of the two approaches.
> 
> 
> 
> So, let's have a look at Example 2 from Amin's paper, page 9, with y_0=0 to keep things simple:
> 
> $$ \frac{dy}{dt}=(1+y^2), \quad y(0)=0. $$
> 
> 
> 
> Amin's expansion to fifth order is:
> 
> $$ y\approx t+\tfrac{1}{3}t^3+\tfrac{2}{15}t^5+\ldots $$
> 
> "My" perturbation expansion also gives this at fifth order.
> 
> 
> 
> Now do a Picard iteration:
> 
> $$ y^{n+1}(t)=y_0+\int_0^t ds f(s,y^n(s)) $$
> 
> 
> 
> we get:
> 
> $$ y^{1}(t)=t $$
> 
> 
> 
> $$ y^{2}(t)=t+\tfrac{1}{3}t^3 $$
> 
> 
> 
> $$ y^{3}(t)=t +\tfrac{1}{3}t^3 +\tfrac{2}{15}t^5+\tfrac{1}{63}t^7 $$
> 
> and the differences get larger from there...
> 
> 
> 
> Am I doing this incorrectly?
I get the same for Picard.

Picard is used to prove existence and uniqueness in a certain time interval. In the current case the example does not satisfy the hypotheses. In this case we must have $abs(t) 
```

---

## Error 9: Unbalanced $: 5

**Snippet:** `> I've never actually done a Picard iteration, so this was good therapy -- and p`

**Full content:**

```
> I've never actually done a Picard iteration, so this was good therapy -- and probably belongs firmly in the student forum, but whatever.
> 
> ...
> 
> Am I doing this incorrectly?
I get the same for Picard.

Picard is used to prove existence and uniqueness in a certain time interval. In the current case the example does not satisfy the hypotheses. In this case we must have $abs(t) 

Well, I guess my point was that the third (or higher) Picard iterate did not seem to be *identical* to Amin's example expansion.  If you perturb to the next order you get (17/315) t^7, which will only agree with the t^7 term in the next order Picard iterate -- but then Picard has a large number of higher-order terms in t.

> 
> The solution is $tan(t)$, what happens to values of t when $cos(t) == 0$??
> 
> 
> 
> Here is the numerical solution of Amin's example 2. Does his series diverge when t ~ PI/2?
Since it ends up effectively being a power series in t it will never deal with the divergence of the solution very well...
```

---

## Error 10: Unbalanced $: 3

**Snippet:** `Here's a test case; maybe for amike and Amin? BTW i have an numeric answer ..   `

**Full content:**

```
Here's a test case; maybe for amike and Amin? BTW i have an numeric answer ..



$ y'(t) = f(t,y(t)),  y(0) = 0 $  on interval $ 0 
```

---

## Error 11: Unbalanced $: 1

**Snippet:** `> Yeah, that's a fun one -- although the solution is pretty simple in the end.  `

**Full content:**

```
> Yeah, that's a fun one -- although the solution is pretty simple in the end.  I am definitely of the opinion that one needs to do some analysis of the problem before using any method, and I would not blindly attempt a formal series solution to this.  
Yes, i solve it using ODE solver and it's too easy. However, the Peano/Picard iterates oscillate between t^2 and -t^2 for a slightly more complicated problem. 



Just looking at f



$df/dy = -4/t, 0 
```

---

## Error 12: Unbalanced $: 1

**Snippet:** `> Yeah, that's a fun one -- although the solution is pretty simple in the end.  `

**Full content:**

```
> Yeah, that's a fun one -- although the solution is pretty simple in the end.  I am definitely of the opinion that one needs to do some analysis of the problem before using any method, and I would not blindly attempt a formal series solution to this.  
Yes, i solve it using ODE solver and it's too easy. However, the Peano/Picard iterates oscillate between t^2 and -t^2 for a slightly more complicated problem. 



Just looking at f



$df/dy = -4/t, 0 
cuch, aming transformations make sense under a certain conditions. in particular when derivative of the right hand side is differentiable on the interval. your example consider the function which does not bounded in t = 0. thus his method might not work in the case. 
```

---

## Error 13: Unbalanced $: 5

**Snippet:** `>  > Here f ( t , y ) = $y^2 ( t ) $ then y ( t )  = y ( 0 ) + $\int_{0}^{t} y ^`

**Full content:**

```
> 
> Here f ( t , y ) = $y^2 ( t ) $ then y ( t )  = y ( 0 ) + $\int_{0}^{t} y ^2 ( s ) ds $
> 
> Hence at t depends on all values of f up to this moment.
немой как рыба



..



как два раза два четыре

смотреть



$ y(t) =  a/(1-at), -\infty 
```

---

## Error 14: Unbalanced $: 1

**Snippet:** `> amin did not present conditions for convergence of his iterative process but h`

**Full content:**

```
> amin did not present conditions for convergence of his iterative process but heuristically one can suppose that he consider the problem under regular, standard conditions on right hand side of the ODE. Cuch 's example(s) is a singular case that probably could not be considered as counterexample. Though say Picard iterations method can be work there. In this particular case we can state that Picard methods works better than Amin's one assuming that Amin approach is correct. Game analogy nevertheless often can be helpful too.
Whether the right-hand side is a nice function per se is irrelevant.
Here is an example to counteract llst's unfounded claim.

$ y' = 1, 0 And the standard numerical double check. You see more steps are needed at the bend. Why?
```

---

## Error 15: Unbalanced $$: 1

**Snippet:** `> Instead of Black Scholes, I was a little more bold and tried solution of CEV n`

**Full content:**

```
> Instead of Black Scholes, I was a little more bold and tried solution of CEV noise fokker planck pde. I have given initial steps and I will complete full numerical analysis tomorrow.
> 
> 
> 
> We try to find the solution of following fokker planck equation
> 
> $\frac{\partial p}{\partial t}=.5 \sigma ^2\frac{\partial ^2\left[x^{2\gamma }p\right]}{\partial x^2}=.5 \sigma ^2x^{2\gamma }\frac{\partial ^2p}{\partial x^2}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial p}{\partial x}+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}p$ Equation(1)
> 
> 
> 
> We change coordinates from p(x,t) to $\text{w(}\zeta\text{,t)}$ such that   $\text{p(x,t)=w(}\zeta\text{,t)}$  We have after the change of coordinates
> 
> $\frac{\partial p}{\partial x}=\frac{\partial w}{\partial \zeta }\frac{\partial \zeta }{\partial x}$
> 
> $\frac{\partial p}{\partial t}=\frac{\partial w}{\partial \zeta }\frac{\partial \zeta }{\partial t}+\frac{\partial w}{\partial t}$
> 
> $\frac{\partial ^2p}{\partial x^2}=\frac{\partial ^2w}{\partial \zeta ^2}\left(\frac{\partial \zeta }{\partial x}\right)^2+\frac{\partial w}{\partial \zeta }\frac{\partial ^2\zeta }{\partial x^2}$  Equations(2)
> 
> 
> 
> Substituting Equations(2) in Equation(1), we get
> 
> $\frac{\partial w}{\partial t}=.5 \sigma ^2x^{2\gamma }(\frac{\partial \zeta }{\partial x})^2\frac{\partial ^2w}{\partial \zeta ^2}+\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }$
> 
> $+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w$ Equation(3)
> 
> 
> 
> We want to convert the transformed equation(3) into standard heat equation in new coordinates. Assuming we can successfully do that we will get a standard brownian motion as the solution to heat equation in new coordinates.
> 
> For that to happen, we will have to impose the conditions
> 
> $.5 \sigma ^2x^{2\gamma }(\frac{\partial \zeta }{\partial x})^2=1$  Equation(4)
> 
> $\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w=0$ Equation(5)
> 
> 
> 
> But we also know once we have satisfied the above conditions, as we stated earlier we will get a standard brownian motion as the solution to heat equation in new coordinates.
> 
> $w=\frac{1}{\sqrt{4\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{4t}\right]$  Equation(6)
> 
> $\frac{\partial w}{\partial \zeta }=\frac{1}{\sqrt{4\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{4t}\right]\left(-\frac{\zeta }{2t}\right)$  Equation(7)
> 
> 
> 
> From Equation (4) , we get
> 
> $\frac{\partial \zeta }{\partial x}=\frac{1}{\sqrt{.5 }\sigma\text{x}^{\gamma }}$ Equation(8)
> 
> From above equation
> 
> $\zeta (x)=\frac{x^{1-\gamma }}{\sqrt{.5 }\sigma (1-\gamma )}-\frac{x_0{}^{1-\gamma }}{\sqrt{.5 }\sigma (1-\gamma )}$  Equation(9)
> 
> $\frac{\partial ^2\zeta }{\partial x^2}=\frac{(-\gamma )}{\sqrt{.5 }\sigma\text{x}^{\gamma +1}}$ Equation(10)
> 
> Putting Equations (6) and (7) in Equaiton(5) and simplifying to cancel the exponential, we get
> 
> $\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\left(-\frac{\zeta }{2t}\right)+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}=0$ Equation(11)
> 
> We try to solve the following ODE  which can be solved for both zeta or x.(I will attempt to give the complete solution tomorrow but we will have to convert the eqution into zeta or x because a map between both variables exists as given by equation(9) for example. 
> 
> $\frac{\partial \zeta }{\partial t}=\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)-\left(\frac{2t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$
> 
> 
> 
> I will try to give complete numerically worked out solution tomorrow. The PDE can then easily be solved in the light of example I cited in the previous post. Here is the reference again. Please look at equation 4.24 in example 4.7 on page 48 of the book, "Essential partial differential equations: Analytical and computational aspects" by David F. Griffiths, John W. Dold, and David J. Silvester. I followed the reference in the above derivation.
I have tried to solve the fokker-planck PDE related to driftless CEV diffusion. Here is the steps I have taken for the solution. Unlike the above analysis, I used the standard definition of normal with .5 in the exponential and .5 in the standard heat equation.

The equation (3) in the quoted post above becomes

$\frac{\partial w}{\partial t}=.5 \sigma ^2x^{2\gamma }(\frac{\partial \zeta }{\partial x})^2\frac{\partial ^2w}{\partial \zeta ^2}+\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }$

$+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w$   Equation(1)



We want to convert the transformed equation into standard heat equation in new coordinates. Assuming we can successfully do that we will get a standard brownian motion as the solution to heat equation in new coordinates. For that to happen, we will have to impose the conditions

$\sigma ^2x^{2\gamma }\left(\frac{\partial \zeta }{\partial x}\right)^2=1$   Equation(2)

$\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w=0$  Equation(3)



But we also know once we have satisfied the above conditions, 



$w=\frac{1}{\sqrt{2\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{2t}\right]$ Equation(4)

$\frac{\partial w}{\partial \zeta }=\frac{1}{\sqrt{2\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{2t}\right]\left(-\frac{\zeta }{t}\right)$   Equation(5)



From equation(2) above, we can find the following three equations

$\frac{\partial \zeta }{\partial x}=\frac{1}{\sigma\text{x}^{\gamma }}$  Equation(6)

$\zeta (x,0)=\frac{x^{1-\gamma }}{\sigma (1-\gamma )}-\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}$   Equation(7)

$\frac{\partial ^2\zeta }{\partial x^2}=\frac{(-\gamma )}{\sigma\text{x}^{\gamma +1}}$   Equation(8)



From equation(3), we derive the following equation

$$

\frac{\partial \zeta }{\partial t}=\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)$

$-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$   Equation(9)

which simplifies in the case of driftless diffusion where we have to account only for second order derivative as

$\frac{\partial \zeta }{\partial t}=.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$ Equation(10)

using equation(6), we get from equation(10)

$\frac{\partial \zeta }{\partial t}=-.5 \sigma \gamma x^{\gamma -1}-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$ Equation(11)

From equation(7), we get the inverse map from zeta to x which is valid at time zero

$x=\left[\sigma (1-\gamma )\left(\zeta (x,0)+\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}\right)\right]{}^{\frac{1}{(1-\gamma )}}$  Equation(12)

using the above inverse map, we get from equation (11), the following ode

$\frac{\partial \zeta }{\partial t}=-.5 \sigma  \gamma \left[\sigma (1-\gamma )\left(\zeta (x,0)+\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}\right)\right]{}^{-1}$

$-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)[\sigma (1-\gamma )\left(\zeta (x,0)+\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}\right)]{}^{-2}$

We can very easily solve the above ordinary differential equation with method of iterated integrals in terms of general initial value. I would like the friends to recall that in the method of iterated integrals the series solution only depends on initial values of the dependent variable which are handily available in almost all the cases. The right initial value would usually be $\zeta (x,0)=0$  which will make many terms in the series expansion solution singular but once we change coordinates back to x  from equation (12), after the solution of ODE in zeta without giving numerical value of zeta(0) in the solution from the method of iterated integrals, the right initial value in terms of x would be x(0) which will give us a very valid solution.
```

---

## Error 16: Unbalanced $$: 3

**Snippet:** `Sorry I failed to explain properly. Once you know how I solved these integrals, `

**Full content:**

```
Sorry I failed to explain properly. Once you know how I solved these integrals, you would know that this is in fact very easy to do that. I try to explain one third order integral again in better detail. These integrals start from $t_0$ and it is not straightforward how to solve them with $t_0$ limit. However if we can convert lower limits to zero, we can easily solve them with Ito isometry. Here is the integral under consideration. Please note that I have removed subscript n from $z_n(t)$ for the sake of simplicity here. 

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^vdz(u)dz(v)dz(s)$  equation 1.



We take the inner most integral.

$\int _{t_0}^vdz(u)$       integral 2

This integral has limits $t_0$ to v. We divide it into two integrals. The first is zero to v and we subtract the integral from zero to $t_0$ so that both new integrals have lower limit from zero and they sum up to integral 2.

$\int _{t_0}^vdz(u)=\int _0^vdz(u)-\int _0^{t_0}dz(u)$  equation(3)

We have divided the innermost integral in equation 1 into two integrals that both have lower limit at zero. Now we add the middle integral in equation 1 and we have that

$\int _{t_0}^s\int _{t_0}^vdz(u)dz(v)$  equation(4)

applying equation 3 to inner integral in above equation(4), we get

$\int _{t_0}^s\int _{t_0}^vdz(u)dz(v)=\int _{t_0}^s\int _0^vdz(u)dz(v)-\int _{t_0}^s\int _0^{t_0}dz(u)dz(v)$ Equation(5)

Now we apply the same change of lower limits to zero for 1st integral in RHS of equation (5) and divide outer integral from $t_0$ to s into two integrals with limits zero to s minus zero to $t_0$

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

$-\int _{t_0}^t\int _0^s\int _0^{t_0}dz(u)dz(v)dz(s)$$+\int _{t_0}^t\int _0^{t_0}\int _0^{t_0}dz(u)dz(v)dz(s)$  Equation(9)

All the inner integrals have lower limit at zero. We repeat the previous technique with outer integral and divide it into two integrals such that both have a zerl lower limit. Taking the first third order integral in RHS of equation(9), we get



$\int _{t_0}^t\int _{0}^s\int _0^vdz(u)dz(v)dz(s)=\int _0^t\int _{0}^s\int _0^vdz(u)dz(v)dz(s)-\int _0^{t_0}\int _{0}^s\int _0^vdz(u)dz(v)dz(s)$ Equation(10)

Similalry for other three integrals in the RHS of equation 9 to get the answer

$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^vdz(u)dz(v)dz(s)$ 

$=\int _0^t\int _0^s\int _0^vdz(u)dz(v)dz(s)-\int _0^{t_0}\int _0^s\int _0^vdz(u)dz(v)dz(s)$

$-\int _0^t\int _0^{t_0}\int _0^vdz(u)dz(v)dz(s)+\int _0^{t_0}\int _0^{t_0}\int _0^vdz(u)dz(v)dz(s)$

$-\int _0^t\int _0^s\int _0^{t_0}dz(u)dz(v)dz(s)+\int _0^{t_0}\int _0^s\int _0^{t_0}dz(u)dz(v)dz(s)$

$+\int _0^t\int _0^{t_0}\int _0^{t_0}dz(u)dz(v)dz(s)-\int _0^{t_0}\int _0^{t_0}\int _0^{t_0}dz(u)dz(v)dz(s)$  Equation(11)

Basically all of the above is extremely simple and only play with the limits of integrals.

Now using ito isometry with stochastic integrals, we get the answer as

$=\text{H3}(n)\frac{t^{1.5}}{6}-\text{H3}(n)\frac{t_0{}^{1.5}}{6}$

$-z(t)\text{H2}(n)\frac{t_0}{2}+z\left(t_0\right)\text{H2}(n)\frac{t_0}{2}$

$-\text{H2}(n)\frac{t}{2}z\left(t_0\right)+\text{H2}(n)\frac{t_0}{2}z\left(t_0\right)$

$+z(t)z\left(t_0\right)z\left(t_0\right)-z\left(t_0\right)z\left(t_0\right)z\left(t_0\right)$





 
```

---

## Error 17: Unbalanced $$: 1

**Snippet:** `> Instead of Black Scholes, I was a little more bold and tried solution of CEV n`

**Full content:**

```
> Instead of Black Scholes, I was a little more bold and tried solution of CEV noise fokker planck pde. I have given initial steps and I will complete full numerical analysis tomorrow.
> 
> 
> 
> We try to find the solution of following fokker planck equation
> 
> $\frac{\partial p}{\partial t}=.5 \sigma ^2\frac{\partial ^2\left[x^{2\gamma }p\right]}{\partial x^2}=.5 \sigma ^2x^{2\gamma }\frac{\partial ^2p}{\partial x^2}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial p}{\partial x}+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}p$ Equation(1)
> 
> 
> 
> We change coordinates from p(x,t) to $\text{w(}\zeta\text{,t)}$ such that   $\text{p(x,t)=w(}\zeta\text{,t)}$  We have after the change of coordinates
> 
> $\frac{\partial p}{\partial x}=\frac{\partial w}{\partial \zeta }\frac{\partial \zeta }{\partial x}$
> 
> $\frac{\partial p}{\partial t}=\frac{\partial w}{\partial \zeta }\frac{\partial \zeta }{\partial t}+\frac{\partial w}{\partial t}$
> 
> $\frac{\partial ^2p}{\partial x^2}=\frac{\partial ^2w}{\partial \zeta ^2}\left(\frac{\partial \zeta }{\partial x}\right)^2+\frac{\partial w}{\partial \zeta }\frac{\partial ^2\zeta }{\partial x^2}$  Equations(2)
> 
> 
> 
> Substituting Equations(2) in Equation(1), we get
> 
> $\frac{\partial w}{\partial t}=.5 \sigma ^2x^{2\gamma }(\frac{\partial \zeta }{\partial x})^2\frac{\partial ^2w}{\partial \zeta ^2}+\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }$
> 
> $+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w$ Equation(3)
> 
> 
> 
> We want to convert the transformed equation(3) into standard heat equation in new coordinates. Assuming we can successfully do that we will get a standard brownian motion as the solution to heat equation in new coordinates.
> 
> For that to happen, we will have to impose the conditions
> 
> $.5 \sigma ^2x^{2\gamma }(\frac{\partial \zeta }{\partial x})^2=1$  Equation(4)
> 
> $\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w=0$ Equation(5)
> 
> 
> 
> But we also know once we have satisfied the above conditions, as we stated earlier we will get a standard brownian motion as the solution to heat equation in new coordinates.
> 
> $w=\frac{1}{\sqrt{4\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{4t}\right]$  Equation(6)
> 
> $\frac{\partial w}{\partial \zeta }=\frac{1}{\sqrt{4\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{4t}\right]\left(-\frac{\zeta }{2t}\right)$  Equation(7)
> 
> 
> 
> From Equation (4) , we get
> 
> $\frac{\partial \zeta }{\partial x}=\frac{1}{\sqrt{.5 }\sigma\text{x}^{\gamma }}$ Equation(8)
> 
> From above equation
> 
> $\zeta (x)=\frac{x^{1-\gamma }}{\sqrt{.5 }\sigma (1-\gamma )}-\frac{x_0{}^{1-\gamma }}{\sqrt{.5 }\sigma (1-\gamma )}$  Equation(9)
> 
> $\frac{\partial ^2\zeta }{\partial x^2}=\frac{(-\gamma )}{\sqrt{.5 }\sigma\text{x}^{\gamma +1}}$ Equation(10)
> 
> Putting Equations (6) and (7) in Equaiton(5) and simplifying to cancel the exponential, we get
> 
> $\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\left(-\frac{\zeta }{2t}\right)+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}=0$ Equation(11)
> 
> We try to solve the following ODE  which can be solved for both zeta or x.(I will attempt to give the complete solution tomorrow but we will have to convert the eqution into zeta or x because a map between both variables exists as given by equation(9) for example. 
> 
> $\frac{\partial \zeta }{\partial t}=\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)-\left(\frac{2t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$
> 
> 
> 
> I will try to give complete numerically worked out solution tomorrow. The PDE can then easily be solved in the light of example I cited in the previous post. Here is the reference again. Please look at equation 4.24 in example 4.7 on page 48 of the book, "Essential partial differential equations: Analytical and computational aspects" by David F. Griffiths, John W. Dold, and David J. Silvester. I followed the reference in the above derivation.
I have tried to solve the fokker-planck PDE related to driftless CEV diffusion. Here is the steps I have taken for the solution. Unlike the above analysis, I used the standard definition of normal with .5 in the exponential and .5 in the standard heat equation.

The equation (3) in the quoted post above becomes

$\frac{\partial w}{\partial t}=.5 \sigma ^2x^{2\gamma }(\frac{\partial \zeta }{\partial x})^2\frac{\partial ^2w}{\partial \zeta ^2}+\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }$

$+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w$   Equation(1)



We want to convert the transformed equation into standard heat equation in new coordinates. Assuming we can successfully do that we will get a standard brownian motion as the solution to heat equation in new coordinates. For that to happen, we will have to impose the conditions

$\sigma ^2x^{2\gamma }\left(\frac{\partial \zeta }{\partial x}\right)^2=1$   Equation(2)

$\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w=0$  Equation(3)



But we also know once we have satisfied the above conditions, 



$w=\frac{1}{\sqrt{2\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{2t}\right]$ Equation(4)

$\frac{\partial w}{\partial \zeta }=\frac{1}{\sqrt{2\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{2t}\right]\left(-\frac{\zeta }{t}\right)$   Equation(5)



From equation(2) above, we can find the following three equations

$\frac{\partial \zeta }{\partial x}=\frac{1}{\sigma\text{x}^{\gamma }}$  Equation(6)

$\zeta (x,0)=\frac{x^{1-\gamma }}{\sigma (1-\gamma )}-\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}$   Equation(7)

$\frac{\partial ^2\zeta }{\partial x^2}=\frac{(-\gamma )}{\sigma\text{x}^{\gamma +1}}$   Equation(8)



From equation(3), we derive the following equation

$$

\frac{\partial \zeta }{\partial t}=\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)$

$-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$   Equation(9)

which simplifies in the case of driftless diffusion where we have to account only for second order derivative as

$\frac{\partial \zeta }{\partial t}=.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$ Equation(10)

using equation(6), we get from equation(10)

$\frac{\partial \zeta }{\partial t}=-.5 \sigma \gamma x^{\gamma -1}-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$ Equation(11)

From equation(7), we get the inverse map from zeta to x which is valid at time zero

$x=\left[\sigma (1-\gamma )\left(\zeta (x,0)+\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}\right)\right]{}^{\frac{1}{(1-\gamma )}}$  Equation(12)

using the above inverse map, we get from equation (11), the following ode

$\frac{\partial \zeta }{\partial t}=-.5 \sigma  \gamma \left[\sigma (1-\gamma )\left(\zeta (x,0)+\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}\right)\right]{}^{-1}$

$-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)[\sigma (1-\gamma )\left(\zeta (x,0)+\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}\right)]{}^{-2}$

We can very easily solve the above ordinary differential equation with method of iterated integrals in terms of general initial value. I would like the friends to recall that in the method of iterated integrals the series solution only depends on initial values of the dependent variable which are handily available in almost all the cases. The right initial value would usually be $\zeta (x,0)=0$  which will make many terms in the series expansion solution singular but once we change coordinates back to x  from equation (12), after the solution of ODE in zeta without giving numerical value of zeta(0) in the solution from the method of iterated integrals, the right initial value in terms of x would be x(0) which will give us a very valid solution.
I made this post about semi-analytic solution to Fokker-Planck PDEs. I hope to code it in matlab for a fairly general PDE and post it here on Wilmott. There will be very minor changes to the above derivation.
```

---

## Error 18: Unbalanced $$: 1

**Snippet:** `> Instead of Black Scholes, I was a little more bold and tried solution of CEV n`

**Full content:**

```
> Instead of Black Scholes, I was a little more bold and tried solution of CEV noise fokker planck pde. I have given initial steps and I will complete full numerical analysis tomorrow.
> 
> 
> 
> We try to find the solution of following fokker planck equation
> 
> $\frac{\partial p}{\partial t}=.5 \sigma ^2\frac{\partial ^2\left[x^{2\gamma }p\right]}{\partial x^2}=.5 \sigma ^2x^{2\gamma }\frac{\partial ^2p}{\partial x^2}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial p}{\partial x}+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}p$ Equation(1)
> 
> 
> 
> We change coordinates from p(x,t) to $\text{w(}\zeta\text{,t)}$ such that   $\text{p(x,t)=w(}\zeta\text{,t)}$  We have after the change of coordinates
> 
> $\frac{\partial p}{\partial x}=\frac{\partial w}{\partial \zeta }\frac{\partial \zeta }{\partial x}$
> 
> $\frac{\partial p}{\partial t}=\frac{\partial w}{\partial \zeta }\frac{\partial \zeta }{\partial t}+\frac{\partial w}{\partial t}$
> 
> $\frac{\partial ^2p}{\partial x^2}=\frac{\partial ^2w}{\partial \zeta ^2}\left(\frac{\partial \zeta }{\partial x}\right)^2+\frac{\partial w}{\partial \zeta }\frac{\partial ^2\zeta }{\partial x^2}$  Equations(2)
> 
> 
> 
> Substituting Equations(2) in Equation(1), we get
> 
> $\frac{\partial w}{\partial t}=.5 \sigma ^2x^{2\gamma }(\frac{\partial \zeta }{\partial x})^2\frac{\partial ^2w}{\partial \zeta ^2}+\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }$
> 
> $+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w$ Equation(3)
> 
> 
> 
> We want to convert the transformed equation(3) into standard heat equation in new coordinates. Assuming we can successfully do that we will get a standard brownian motion as the solution to heat equation in new coordinates.
> 
> For that to happen, we will have to impose the conditions
> 
> $.5 \sigma ^2x^{2\gamma }(\frac{\partial \zeta }{\partial x})^2=1$  Equation(4)
> 
> $\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w=0$ Equation(5)
> 
> 
> 
> But we also know once we have satisfied the above conditions, as we stated earlier we will get a standard brownian motion as the solution to heat equation in new coordinates.
> 
> $w=\frac{1}{\sqrt{4\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{4t}\right]$  Equation(6)
> 
> $\frac{\partial w}{\partial \zeta }=\frac{1}{\sqrt{4\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{4t}\right]\left(-\frac{\zeta }{2t}\right)$  Equation(7)
> 
> 
> 
> From Equation (4) , we get
> 
> $\frac{\partial \zeta }{\partial x}=\frac{1}{\sqrt{.5 }\sigma\text{x}^{\gamma }}$ Equation(8)
> 
> From above equation
> 
> $\zeta (x)=\frac{x^{1-\gamma }}{\sqrt{.5 }\sigma (1-\gamma )}-\frac{x_0{}^{1-\gamma }}{\sqrt{.5 }\sigma (1-\gamma )}$  Equation(9)
> 
> $\frac{\partial ^2\zeta }{\partial x^2}=\frac{(-\gamma )}{\sqrt{.5 }\sigma\text{x}^{\gamma +1}}$ Equation(10)
> 
> Putting Equations (6) and (7) in Equaiton(5) and simplifying to cancel the exponential, we get
> 
> $\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\left(-\frac{\zeta }{2t}\right)+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}=0$ Equation(11)
> 
> We try to solve the following ODE  which can be solved for both zeta or x.(I will attempt to give the complete solution tomorrow but we will have to convert the eqution into zeta or x because a map between both variables exists as given by equation(9) for example. 
> 
> $\frac{\partial \zeta }{\partial t}=\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)-\left(\frac{2t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$
> 
> 
> 
> I will try to give complete numerically worked out solution tomorrow. The PDE can then easily be solved in the light of example I cited in the previous post. Here is the reference again. Please look at equation 4.24 in example 4.7 on page 48 of the book, "Essential partial differential equations: Analytical and computational aspects" by David F. Griffiths, John W. Dold, and David J. Silvester. I followed the reference in the above derivation.
I have tried to solve the fokker-planck PDE related to driftless CEV diffusion. Here is the steps I have taken for the solution. Unlike the above analysis, I used the standard definition of normal with .5 in the exponential and .5 in the standard heat equation.

The equation (3) in the quoted post above becomes

$\frac{\partial w}{\partial t}=.5 \sigma ^2x^{2\gamma }(\frac{\partial \zeta }{\partial x})^2\frac{\partial ^2w}{\partial \zeta ^2}+\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }$

$+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w$   Equation(1)



We want to convert the transformed equation into standard heat equation in new coordinates. Assuming we can successfully do that we will get a standard brownian motion as the solution to heat equation in new coordinates. For that to happen, we will have to impose the conditions

$\sigma ^2x^{2\gamma }\left(\frac{\partial \zeta }{\partial x}\right)^2=1$   Equation(2)

$\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\frac{\partial \zeta }{\partial t}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)\frac{\partial w}{\partial \zeta }+\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}w=0$  Equation(3)



But we also know once we have satisfied the above conditions, 



$w=\frac{1}{\sqrt{2\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{2t}\right]$ Equation(4)

$\frac{\partial w}{\partial \zeta }=\frac{1}{\sqrt{2\text{pi} t}}\text{Exp}\left[-\frac{\zeta ^2}{2t}\right]\left(-\frac{\zeta }{t}\right)$   Equation(5)



From equation(2) above, we can find the following three equations

$\frac{\partial \zeta }{\partial x}=\frac{1}{\sigma\text{x}^{\gamma }}$  Equation(6)

$\zeta (x,0)=\frac{x^{1-\gamma }}{\sigma (1-\gamma )}-\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}$   Equation(7)

$\frac{\partial ^2\zeta }{\partial x^2}=\frac{(-\gamma )}{\sigma\text{x}^{\gamma +1}}$   Equation(8)



From equation(3), we derive the following equation

$$

\frac{\partial \zeta }{\partial t}=\left.(.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}+2\gamma \sigma ^2x^{2\gamma -1}\frac{\partial \zeta }{\partial x}\right)$

$-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$   Equation(9)

which simplifies in the case of driftless diffusion where we have to account only for second order derivative as

$\frac{\partial \zeta }{\partial t}=.5 \sigma ^2x^{2\gamma }\frac{\partial ^2\zeta }{\partial x^2}-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$ Equation(10)

using equation(6), we get from equation(10)

$\frac{\partial \zeta }{\partial t}=-.5 \sigma \gamma x^{\gamma -1}-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)x^{2\gamma -2}$ Equation(11)

From equation(7), we get the inverse map from zeta to x which is valid at time zero

$x=\left[\sigma (1-\gamma )\left(\zeta (x,0)+\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}\right)\right]{}^{\frac{1}{(1-\gamma )}}$  Equation(12)

using the above inverse map, we get from equation (11), the following ode

$\frac{\partial \zeta }{\partial t}=-.5 \sigma  \gamma \left[\sigma (1-\gamma )\left(\zeta (x,0)+\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}\right)\right]{}^{-1}$

$-\left(\frac{t}{\zeta }\right)\gamma \sigma ^2(2\gamma -1)[\sigma (1-\gamma )\left(\zeta (x,0)+\frac{x_0{}^{1-\gamma }}{\sigma (1-\gamma )}\right)]{}^{-2}$

We can very easily solve the above ordinary differential equation with method of iterated integrals in terms of general initial value. I would like the friends to recall that in the method of iterated integrals the series solution only depends on initial values of the dependent variable which are handily available in almost all the cases. The right initial value would usually be $\zeta (x,0)=0$  which will make many terms in the series expansion solution singular but once we change coordinates back to x  from equation (12), after the solution of ODE in zeta without giving numerical value of zeta(0) in the solution from the method of iterated integrals, the right initial value in terms of x would be x(0) which will give us a very valid solution.
I made this post about semi-analytic solution to Fokker-Planck PDEs. I hope to code it in matlab for a fairly general PDE and post it here on Wilmott. There will be very minor changes to the above derivation.
Sorry, this probably would not work. I tried but as the time increases their is more and more discrepancy with true solution. Probably some derivatives that are supposedly fixed cannot be constrained. If somebody still would be interested, I could send my matlab program but I am afraid the approach might not work. 
```

---

## Error 19: Unbalanced $: 143

**Snippet:** `Since my work is very close to completion, I would like to explain my method in `

**Full content:**

```
Since my work is very close to completion, I would like to explain my method in a more formal way.

Let us consider a non-linear SDE of the form 

$dX(t)=\mu_1 X^{\beta_1}(t) dt +\mu_2 X^{\beta_2}(t) dt + \sigma X^{\gamma} dz(t)$

In my work I took a Lamperti transform of the above SDE and defined the new transformed variable as $w(t)=\frac{X(t)^{(1-\gamma)}}{(1-\gamma)}$. I did not take $\sigma$ in the denominator of the transformed variable.

Applying Ito change of variable formula on the transformed variable, we get

$dw(t)=d[\frac{X(t)^{(1-\gamma)}}{1-\gamma}]=\mu_1 X(t)^{(\beta_1-\gamma)} dt+ \mu_2 X(t)^{(\beta_2-\gamma)} dt$

$ -.5 \gamma {\sigma}^2 X(t)^{(\gamma-1)} dt +\sigma dz(t)$ 

Integral form of the above SDE would be written as

$w(t)=\frac{X(t)^{(1-\gamma)}}{1-\gamma}=w(0)+\int_0^t \mu_1 X(s)^{(\beta_1-\gamma)} ds+\int_0^t \mu_2 X(s)^{(\beta_2-\gamma)} ds$

$ -\int_0^t .5 \gamma {\sigma}^2 X(s)^{(\gamma-1)} ds +\int_0^t \sigma dz(s)$ 



To get a second order Ito-Taylor expansion, we will do a repeated Ito on each of the variable drift term of the above transformed SDE of $w(t)$

Taking the repeated Ito of the first term in the SDE, we get

$\int_0^t \mu_1 X(s)^{(\beta_1-\gamma)} ds= \mu_1 X(0)^{(\beta_1-\gamma)} \int_0^t ds$

$ + \int_0^t \int_0^s \mu_1(\beta_1-\gamma) X(v)^{(\beta_1-\gamma-1)} (\mu_1 X(v)^{\beta_1} + \mu_2 X(v)^{\beta_2})dv ds$

$+\int_0^t \int_0^s \mu_1(\beta_1-\gamma) X(v)^{(\beta_1-\gamma-1)} \sigma X(v)^{\gamma} dz(v) ds$

$+\int_0^t \int_0^s .5 \mu_1  (\beta_1-\gamma)(\beta_1-\gamma-1) X(v)^{(\beta_1-\gamma-2)} {\sigma}^2 X(v)^{2 \gamma} dv ds$

notice that first term in the above expansion is calculated at initial time zero and rest of the terms are calculated along the evolution path of the stochastic integrals. We could continue higher order expansion inside the integrals but if the interval is small we can just stop the expansion and find a very good approximation by substituting the terms that have to be calculated along the evolution path by their values at time zero. Our above expansion would become

$\int_0^t \mu_1 X(s)^{(\beta_1-\gamma)} ds]= \mu_1 X(0)^{(\beta_1-\gamma)} \int_0^t ds$

$ + \mu_1(\beta_1-\gamma) X(0)^{(\beta_1-\gamma-1)} (\mu_1 X(0)^{\beta_1} + \mu_2 X(0)^{\beta_2}) \int_0^t \int_0^s dv ds$

$+ \mu_1(\beta_1-\gamma) X(0)^{(\beta_1-\gamma-1)} \sigma X(0)^{\gamma} \int_0^t \int_0^s  dz(v) ds$

$+ .5 \mu_1(\beta_1-\gamma)(\beta_1-\gamma-1) X(0)^{(\beta_1-\gamma-2)} {\sigma}^2 X(0)^{2 \gamma} \int_0^t \int_0^s  dv ds$

We know from basic calculus and stochastic calculus that 

$\int_0^t \int_0^s dv ds = \frac{t^2}{2} $ and

$\int_0^t \int_0^s dz(v) ds = (1-\frac{1}{\sqrt{3}}) t^{1.5} Z $ where $Z$ is a standard normal.



We have to find repeated Ito of all the three drift terms. There is no further expansion of the volatility terms as it has no variable coefficients. After the Ito Taylor expansion of the all three drift terms, the expansion of the transformed SDE becomes

$w(t)=\frac{X(t)^{(1-\gamma)}}{1-\gamma}=w(0)+ \mu_1 X(s)^{(\beta_1-\gamma)} {\Delta t}+ \mu_2 X(s)^{(\beta_2-\gamma)} {\Delta t}$

$ - .5 \gamma {\sigma}^2 X(s)^{(\gamma-1)} {\Delta t} $

$ + (\mu_1(\beta_1-\gamma) X(0)^{(\beta_1-\gamma-1)} +\mu_2(\beta_2-\gamma) X(0)^{(\beta_2-\gamma-1)} -.5\gamma (\gamma-1) X(0)^{(\gamma-2)})$

$* (\mu_1 X(0)^{\beta_1} + \mu_2 X(0)^{\beta_2})  \frac{{\Delta t}^2}{2}$

$+ .5 (\mu_1(\beta_1-\gamma)(\beta_1-\gamma-1) X(0)^{(\beta_1-\gamma-2)} +\mu_2(\beta_2-\gamma)(\beta_2-\gamma-1) X(0)^{(\beta_2-\gamma-2)} -.5\gamma (\gamma-1)(\gamma-2) X(0)^{(\gamma-3)} )$

$*{\sigma}^2 X(0)^{2 \gamma} \frac{{\Delta t}^2}{2}$

$+ \sigma \sqrt{\Delta t} Z$ 

$+ ( \mu_1(\beta_1-\gamma) X(0)^{(\beta_1-\gamma-1)} +  \mu_2(\beta_2-\gamma) X(0)^{(\beta_2-\gamma-1)}-.5\gamma (\gamma-1) X(0)^{(\gamma-2)}) (\sigma X(0)^{\gamma} ) (1-\frac{1}{\sqrt{3}}) {\Delta t}^{1.5} Z $



We can write the one step differential evolution equation as 

$w(t+\Delta t)= w(t)+ \mu_{\Delta t} + \alpha_{\Delta t} Z $

where particularly 

$\alpha_{\Delta t}= \sigma \sqrt{\Delta t}+ ( \mu_1(\beta_1-\gamma) X(0)^{(\beta_1-\gamma-1)} +  \mu_2(\beta_2-\gamma) X(0)^{(\beta_2-\gamma-1)}-.5\gamma (\gamma-1) X(0)^{(\gamma-2)}) (\sigma X(0)^{\gamma} ) (1-\frac{1}{\sqrt{3}}) {\Delta t}^{1.5})$

After looking at Ito-Taylor expansion, we proceed towards the main density evolution algorithm that advances the density over each small time interval in our setting that is different from monte carlo simulation.

I have divided the density into N subdivisions with a value of normal random variable linearly associated with each subdivision. In my program, these subdivisions are linearly associated with normal RV. Let $Z_n$ be value of normal RV associated with nth subdivision with roughly $Z_1=-4.0$ and $Z_N=4.0$ . In my current program I have taken $N=46$ covering the gaussian from -4.5 to +4.5.

I took Lamperti transform of the SDE in original coordinates X and the transformed SDE variable w became very linear with respect to normal RV which greatly helped in analytics. In fact, in most of the SDEs only first order variance was of relevance. 

I define existing density as starting transformed density at any point $t$ in evolution and it is written as $w(t)$ , and then a differential term is added for an evolution period $\Delta t$ and then we find density at next step $T=t+\Delta t$ denoted as $w(T)$

In order to calculate the one step evolution of first order variance, we have to calculate the first order Hermite representation of the existing SDE along nth subdivision or nth point in the grid and also calculate the one step first order hermite representation of the innovation/differential term. It is very easy to calculate the hermite represntation of the differential term due to Ito-Taylor expansion of the SDE and there is a huge literature on that. With help of Ito-Taylor expansion we can easily calculate the evolution in terms of hermite polynomials and thereby decompose the variance into first order and higher orders based on association with each hermite polynomial of different order. After taking Lamperti transform, it was usually the first order variance that was significant. But despite taking Lamperti transform, on each step SDE still evolves slightly non linearly due to non-linearity in drift terms and it was not straightforward how to represent the existing SDE variable $w(t)$ in terms of hermite polynomials. If we could represent the existing and differential parts of the SDE variable in terms of hermite polynomials, we could get a representation of the evolved variable $w_T(n)$ in terms of hermite polynomial.

Hermite representation of existing SDE variable on each point of the evolving grid could be represented as $w_t(n)=\mu_w+\alpha_t(n)Z(n)$ and hermite representation of the differential term could be written as $w_{\Delta t}(n)=\mu_{\Delta t}(n)+ \alpha_{\Delta t}(n) Z(n)$, then representation of evolved SDE at next step $T=t+\Delta t$  i.e $w_T$ could be written as $w_T(n)= \mu_{\Delta t}(n)+\mu_w+ \sqrt{{\alpha}^2_t(n)+{\alpha}^2_{\Delta t}(n)} Z(n)$

where $\mu_w$ associated with existing density w(t) is defined as $\mu_w = \int_{-inf}^{+inf} w p(w) dw$

Here $\mu_{\Delta t}(n)$ is the total deterministic contribution from all the drift terms in the SDE for the nth subdivision for time interval $\Delta t$.

Again it was very easy to find a Hermite representation of the differential part of SDE due to Ito-Taylor but it was not simple at all to find a hermite representation of the existing SDE on each step. My contribution came in here as I noticed that $w(t)$ was very close to scaled Z and it could be possible to omit the step of finding the hermite representation of the existing SDE and instead use the first order evolution equation for the SDE as

$w_T(n)=\mu_{\Delta t}(n)+\mu_{w} + \sqrt{(w_t(n)-\mu_{w})^2+(\alpha_{\Delta t}(n) Z(n))^2}$

This worked since $w_t$ is reasonably linear with respect to Z due to Lamperti transform and $w_t(n)-\mu_w$ was a valid proxy for $\alpha_t(n) Z(n)$.

When I made this first step approximation, things worked perfectly with linear SDEs where $w(t)$ remains linear with $Z$. But particularly for mean reverting type SDEs which have multiple terms in the drift and when volatility is high, due to non-linear dynamics in the drift, a huge quantity of second order derivative of $w(t)$ with respect to $Z$ is introduced and dealing with the first order is not enough to get good results for the density of mean reverting type SDEs.

Then a recent breakthrough came when I found from my experiments that second order hermite term in the expansion of the existing SDE $w(t)$ was making a contribution to the SDE evolution. If we denote the hermite representation of $w(t)$ up to second order as $w_t(n)=\alpha_t(n) Z(n) + \beta_t(n) (Z^2(n)-1)$.

This contribution from the coefficients of second hermite polynomial to one step evolution of the SDE was empirically found up to a positive scaling constant $c$  as equal to $ -.5 c \beta_t(n)(Z^2(n)-1) {\sigma}^2(t) \frac{\Delta t}{2}$

Here $\sigma(t)$ is volatility in the noise term of the SDE. 

But again all of this was approximate since it is not very simple to find a hermite representation of the existing SDE and it was particularly difficult to find coefficients of second hermite polynomial accurately. So analogously to my approximation for coefficients of coefficients of first order hermite polynomials for the existing density, I devised a similar approximation to coefficients of second order hermite polynomial and used the formula

$\beta_t(n) (Z^2(n)-1) = (w_t(n)-\mu_w)^2- \sigma^2_w$ which is very valid due to high relative linearity of the transformed variable.

So our contribution from the second order derivative from the surface of w(t) could now be written as

$-.5 c \beta_t(n)(Z^2(n)-1) {\sigma}^2(t) \frac{\Delta t}{2} = -.5 c ((w_t(n)-\mu_w)^2- \sigma^2_w)  {\sigma}^2(t) \frac{\Delta t}{2}$

Here $\sigma^2_w=\int_{-\inf}^{+\inf} (w-\mu_w)^2 p(w) dw$

if there is a contribution from the second order hermite polynomial of differential part of SDE evolution, it would be added to the above second order contribution from the existing surface w(t) in a squared fashion and resulting second order addition to one step evolution of the SDE would become as

$\sqrt{(.5 c ((w_t(n)-\mu_w)^2- \sigma^2_w)  {\sigma}^2(t) \frac{\Delta t}{2})^2 + (\beta_{\Delta t}(n) (Z(n)^2-1))^2}$

where $ \beta_{\Delta t} $ are the coefficients of second order hermite polynomial in the Ito-Taylor expansion of the differential term of the SDE. After the second order correction, the evolution equation for the SDE becomes

$w_T(n)=\mu_{\Delta t}(n)+\mu_{w} + \sqrt{(w_t(n)-\mu_{w})^2+(\alpha_{\Delta t}(n) Z(n))^2}$

$+ \sqrt{(.5 c ((w_t(n)-\mu_w)^2- \sigma^2_w)  {\sigma}^2(t) \frac{\Delta t}{2})^2 + (\beta_{\Delta t}(n) (Z(n)^2-1))^2}$



In our simulations we found that second order contribution from the differential term after taking Lamperti transform was completely miniscule as compared to the second order contribution from the existing density surface and this contribution from differential term to the density average never made a difference of more than one basis point (.0001) in our simulations with high volatility and mean reversion. We write this as

 $\beta_{\Delta t}(n) (Z(n)^2-1) 
```

---

## Error 20: Unbalanced $$: 47

**Snippet:** `Those friends who are unfamiliar with mathematica might be daunted by large numb`

**Full content:**

```
Those friends who are unfamiliar with mathematica might be daunted by large number of terms in expression for various derivatives. This is very easy in mathematica. For example, you can use the following command in mathematica to calculate various derivatives of Zt with respect to Bm as given in my program.(since Zt=(Bn-Bm-Muw)/Sigmaw) in our setup)



D[(-Bm+Bn-Muw[Bm])/Sigmaw[Bm],{Bm,5}]

(here 5 in parantheses brackets means that you want to calculate fifth derivative given as d5ZtdBm5 in the program.) and mathematica comes up with the expression

> -10 ((2 (Sigmaw^$$Prime])[Bm]^2)/Sigmaw[Bm]^3-(Sigmaw^$$Prime]$$Prime])[Bm]/Sigmaw[Bm]^2) (Muw^(3))[Bm]-10 (Muw^$$Prime]$$Prime])[Bm] (-((6 (Sigmaw^$$Prime])[Bm]^3)/Sigmaw[Bm]^4)+(6 (Sigmaw^$$Prime])[Bm] (Sigmaw^$$Prime]$$Prime])[Bm])/Sigmaw[Bm]^3-(Sigmaw^(3))[Bm]/Sigmaw[Bm]^2)+(5 (Sigmaw^$$Prime])[Bm] (Muw^(4))[Bm])/Sigmaw[Bm]^2+5 (-1-(Muw^$$Prime])[Bm]) ((24 (Sigmaw^$$Prime])[Bm]^4)/Sigmaw[Bm]^5-(36 (Sigmaw^$$Prime])[Bm]^2 (Sigmaw^$$Prime]$$Prime])[Bm])/Sigmaw[Bm]^4+(6 (Sigmaw^$$Prime]$$Prime])[Bm]^2)/Sigmaw[Bm]^3+(8 (Sigmaw^$$Prime])[Bm] (Sigmaw^(3))[Bm])/Sigmaw[Bm]^3-(Sigmaw^(4))[Bm]/Sigmaw[Bm]^2)-(Muw^(5))[Bm]/Sigmaw[Bm]+(-Bm+Bn-Muw[Bm]) (-((120 (Sigmaw^$$Prime])[Bm]^5)/Sigmaw[Bm]^6)+(240 (Sigmaw^$$Prime])[Bm]^3 (Sigmaw^$$Prime]$$Prime])[Bm])/Sigmaw[Bm]^5-(90 (Sigmaw^$$Prime])[Bm] (Sigmaw^$$Prime]$$Prime])[Bm]^2)/Sigmaw[Bm]^4-(60 (Sigmaw^$$Prime])[Bm]^2 (Sigmaw^(3))[Bm])/Sigmaw[Bm]^4+(20 (Sigmaw^$$Prime]$$Prime])[Bm] (Sigmaw^(3))[Bm])/Sigmaw[Bm]^3+(10 (Sigmaw^$$Prime])[Bm] (Sigmaw^(4))[Bm])/Sigmaw[Bm]^3-(Sigmaw^(5))[Bm]/Sigmaw[Bm]^2)
You can use "copy as plain text" from mathematica and paste the expression in matlab file. Then you can use "find/replace" command in matlab to convert mathematica symbolic names to variable names used in matlab. For example choose  "(Sigmaw^$$Prime]$$Prime])[Bm]" in find and select "d2SigmawdBm2" in replace and replace in all of the expression. Giving another example, you can replace "(Sigmaw^(3))[Bm]" in above expression to "d3SigmawdBm3" in matlab.

Similarly to find the partial derivatives of CDF of normal density with respect to Bm, you can use the following command in mathematica. For the expression of 4th derivative of CDF Pm0n with respect to Bm, you will use the following command

D[Pm0n[Zt[Bm]], {Bm, 4}]

and it will give the result
> 3 (Pm0n^$$Prime]$$Prime])[Zt[Bm]] (Zt^$$Prime]$$Prime])[Bm]^2+6 (Zt^$$Prime])[Bm]^2 (Zt^$$Prime]$$Prime])[Bm] (Pm0n^(3))[Zt[Bm]]+4 (Zt^$$Prime])[Bm] (Pm0n^$$Prime]$$Prime])[Zt[Bm]] (Zt^(3))[Bm]+(Zt^$$Prime])[Bm]^4 (Pm0n^(4))[Zt[Bm]]+(Pm0n^$$Prime])[Zt[Bm]] (Zt^(4))[Bm]
Now you choose "copy as plain text" from mathematica and paste it in matlab editor where you will use find/replace command to give your own matlab programming names to mathematica symbolic names. For example you could select "(Pm0n^(4))[Zt[Bm]]" in find and replace it with "d4Pm0ndZt4" throughout the expression. Similarly you could replace "(Zt^$$Prime]$$Prime])[Bm]" with "d2ZtdBm2" which is the programming name I used in matlab for second derivative of Zt with respect to Bm.

To make it intuitively easy to understand the first derivative of CDF with respect to Bm, you use the command

D[Pm0n[Zt[Bm]], {Bm, 1}]

which will give the result
> (Pm0n^$$Prime])[Zt[Bm]] (Zt^$$Prime])[Bm]
In matlab, I changed the above mathematica symbolic equation  to  dPm0ndBm= dPm0ndZt * dZtdBm



I am posting another working program that calculates the "unweighted" CDF of normal with variable drift and variable volatility. I wanted to check how the convergence of Taylor series increases as the order of expansion increases, so I calculated the CDF Taylor expansion to 10th order and then compared numbers of zero order, 2nd order, 4th order, 6th order, 8th order, and 10th order. It seems that for difficult integrals even with small cell size of .03125 (which means 32 cells as Bm changes by one) , every second order expansion increases the convergence to true result by one decimal point. You can throw numbers on this program and see how it goes.


```
function [] = CheckCDFfromSubdivDriftVol08(Bn,Bm0,dB)
%This function integrates gaussian transition CDF(to target point Bn) over 
%a subdivision with centre Bm0 and symmetric boundaries Bm1=Bm0-.5*dB; and 
%Bm2=Bm0+.5*dB;
%And compares it with integration by parts expression

delta_t=.1;
sigma0=.15*sqrt(delta_t);
mu1=.50*delta_t;
beta=.95;
gamma=0.650;%1.65;
%variable vol is defined as Sigmaw=Sigma0*Bm.^gamma;
%variable drift is defined as Muw=mu1*Bm.^beta;
%real drift and vol and their derivatives would be in terms of a sum of large number of terms
%that come out of Ito-hermite expansion.


Bm1=Bm0-.5*dB;
Bm2=Bm0+.5*dB;
dBm=(Bm2-Bm1)/100000;
Integral0=0;
Integral1=0;
Integral2=0;
IntegralVol0=0;
IntegralMu0=0;
for n=1:100001
    if(n==1)
        BmI=Bm1+(n-1)*dBm;
        Muw=mu1*BmI.^beta;
        Sigmaw=sigma0*BmI.^gamma;
        Zt=(Bn-BmI-Muw)/Sigmaw;
        dSigmawdBm=sigma0*gamma.*BmI.^(gamma-1);
        dMuwdBm=mu1*beta.*BmI.^(beta-1);
        %dZtdBm=(-1 - dMuwdBm )/ Sigmaw - ((-BmI + Bn - Muw)* dSigmawdBm)/Sigmaw^2;
        dZtdBm=(-1 - dMuwdBm )/ Sigmaw - ((Zt)* dSigmawdBm)/Sigmaw;
        Integral0=Integral0+.5*normcdf(Zt,0,1)*dBm;
    end
    if((n>1)&&(n<100001))
        BmI=Bm1+(n-1)*dBm;
        Muw=mu1*BmI.^beta;
        Sigmaw=sigma0*BmI.^gamma;
        Zt=(Bn-BmI-Muw)/Sigmaw;
        dSigmawdBm=sigma0*gamma.*BmI.^(gamma-1);
        dMuwdBm=mu1*beta.*BmI.^(beta-1);
        %dZtdBm=(-1 - dMuwdBm )/ Sigmaw - ((-BmI + Bn - Muw)* dSigmawdBm)/Sigmaw^2;
        dZtdBm=(-1 - dMuwdBm )/ Sigmaw - ((Zt)* dSigmawdBm)/Sigmaw;
        Integral0=Integral0+normcdf(Zt,0,1)*dBm;
    end
    if((n==100001))
        BmI=Bm1+(n-1)*dBm;
        Muw=mu1*BmI.^beta;
        Sigmaw=sigma0*BmI.^gamma;
        Zt=(Bn-BmI-Muw)/Sigmaw;
        dSigmawdBm=sigma0*gamma.*BmI.^(gamma-1);
        dMuwdBm=mu1*beta.*BmI.^(beta-1);
        %dZtdBm=(-1 - dMuwdBm )/ Sigmaw - ((-BmI + Bn - Muw)* dSigmawdBm)/Sigmaw^2;
        dZtdBm=(-1 - dMuwdBm )/ Sigmaw - ((Zt)* dSigmawdBm)/Sigmaw;
        Integral0=Integral0+.5*normcdf(Zt,0,1)*dBm;
    end
end



Muw=mu1*Bm0.^beta;
Sigmaw=sigma0*Bm0.^gamma;


Zt=(Bn-Bm0-Muw)/Sigmaw;

Zt2=Zt.*Zt;
Zt3=Zt2.*Zt;
Zt4=Zt3.*Zt;
Zt5=Zt4.*Zt;
Zt6=Zt5.*Zt;
Zt7=Zt6.*Zt;
Zt8=Zt7.*Zt;
Zt9=Zt8.*Zt;
Zt10=Zt9.*Zt;


Pm0n=normcdf(Zt,0,1);
dPm0ndZt=normpdf(Zt,0,1);
d2Pm0ndZt2=-dPm0ndZt*(Zt);
d3Pm0ndZt3=dPm0ndZt*(Zt2-1);
d4Pm0ndZt4=-dPm0ndZt.*(Zt3-3*Zt);
d5Pm0ndZt5=dPm0ndZt.*(Zt4-6*Zt2+3);
d6Pm0ndZt6=-dPm0ndZt.*(Zt5-10*Zt3+15*Zt);
d7Pm0ndZt7=dPm0ndZt.*(Zt6-15*Zt4+45*Zt2-15);
d8Pm0ndZt8=-dPm0ndZt.*(Zt7-21*Zt5+105*Zt3-105*Zt);
d9Pm0ndZt9=dPm0ndZt.*(Zt8-28*Zt6+210*Zt4-420*Zt2+105);
d10Pm0ndZt10=-dPm0ndZt.*(Zt9-36*Zt7+378*Zt5-1260*Zt3+945*Zt);

Sigmaw=sigma0.*Bm0.^(gamma);
dSigmawdBm=sigma0*gamma.*Bm0.^(gamma-1);
d2SigmawdBm2=sigma0*gamma.*(gamma-1).*Bm0.^(gamma-2);
d3SigmawdBm3=sigma0*gamma.*(gamma-1).*(gamma-2).*Bm0.^(gamma-3);
d4SigmawdBm4=sigma0*gamma.*(gamma-1).*(gamma-2).*(gamma-3).*Bm0.^(gamma-4);
d5SigmawdBm5=sigma0*gamma.*(gamma-1).*(gamma-2).*(gamma-3).*(gamma-4).*Bm0.^(gamma-5);
d6SigmawdBm6=sigma0*gamma.*(gamma-1).*(gamma-2).*(gamma-3).*(gamma-4).*(gamma-5).*Bm0.^(gamma-6);
d7SigmawdBm7=sigma0*gamma.*(gamma-1).*(gamma-2).*(gamma-3).*(gamma-4).*(gamma-5).*(gamma-6).*Bm0.^(gamma-7);
d8SigmawdBm8=sigma0*gamma.*(gamma-1).*(gamma-2).*(gamma-3).*(gamma-4).*(gamma-5).*(gamma-6).*(gamma-7).*Bm0.^(gamma-8);
d9SigmawdBm9=sigma0*gamma.*(gamma-1).*(gamma-2).*(gamma-3).*(gamma-4).*(gamma-5).*(gamma-6).*(gamma-7).*(gamma-8).*Bm0.^(gamma-9);
d10SigmawdBm10=sigma0*gamma.*(gamma-1).*(gamma-2).*(gamma-3).*(gamma-4).*(gamma-5).*(gamma-6).*(gamma-7).*(gamma-8).*(gamma-9).*Bm0.^(gamma-10);

Muw=mu1*Bm0.^(beta);
dMuwdBm=mu1*beta.*Bm0.^(beta-1);
d2MuwdBm2=mu1*beta.*(beta-1).*Bm0.^(beta-2);
d3MuwdBm3=mu1*beta.*(beta-1).*(beta-2).*Bm0.^(beta-3);
d4MuwdBm4=mu1*beta.*(beta-1).*(beta-2).*(beta-3).*Bm0.^(beta-4);
d5MuwdBm5=mu1*beta.*(beta-1).*(beta-2).*(beta-3).*(beta-4).*Bm0.^(beta-5);
d6MuwdBm6=mu1*beta.*(beta-1).*(beta-2).*(beta-3).*(beta-4).*(beta-5).*Bm0.^(beta-6);
d7MuwdBm7=mu1*beta.*(beta-1).*(beta-2).*(beta-3).*(beta-4).*(beta-5).*(beta-6).*Bm0.^(beta-7);
d8MuwdBm8=mu1*beta.*(beta-1).*(beta-2).*(beta-3).*(beta-4).*(beta-5).*(beta-6).*(beta-7).*Bm0.^(beta-8);
d9MuwdBm9=mu1*beta.*(beta-1).*(beta-2).*(beta-3).*(beta-4).*(beta-5).*(beta-6).*(beta-7).*(beta-8).*Bm0.^(beta-9);
d10MuwdBm10=mu1*beta.*(beta-1).*(beta-2).*(beta-3).*(beta-4).*(beta-5).*(beta-6).*(beta-7).*(beta-8).*(beta-9).*Bm0.^(beta-10);





Zt=(-Bm0 + Bn - Muw)/Sigmaw;


 dZtdBm=(-1 - dMuwdBm )/ Sigmaw - ((Zt)* dSigmawdBm)/Sigmaw;
 
 
 d2ZtdBm2=-(((-1-dMuwdBm).* dSigmawdBm)/Sigmaw^2)+(Zt.* dSigmawdBm^2)/Sigmaw^2-( dSigmawdBm.* dZtdBm)/Sigmaw- ...
     d2MuwdBm2/Sigmaw-(Zt .* d2SigmawdBm2)/Sigmaw;
 
  d3ZtdBm3=(2.* (-1-dMuwdBm).* dSigmawdBm.^2)/Sigmaw^3-(2.* Zt.* dSigmawdBm^3)/Sigmaw^3+(2 .*dSigmawdBm.^2 .* ...
      dZtdBm)/Sigmaw.^2+(2.* dSigmawdBm.* d2MuwdBm2)/Sigmaw.^2-((-1-dMuwdBm).* d2SigmawdBm2)/Sigmaw.^2+ ...
      (3.* Zt.* dSigmawdBm .*d2SigmawdBm2)/Sigmaw.^2-(2.* dZtdBm.* d2SigmawdBm2)/Sigmaw- ...
      (dSigmawdBm.* d2ZtdBm2)/Sigmaw-d3MuwdBm3/Sigmaw-(Zt.* d3SigmawdBm3)/Sigmaw;
 

  
 d4ZtdBm4=-6.* d2MuwdBm2.* ((2.* dSigmawdBm.^2)/Sigmaw^3-d2SigmawdBm2/Sigmaw^2)+(4.* dSigmawdBm .* d3MuwdBm3)/Sigmaw.^2+ ...
      4.* (-1-dMuwdBm) .*(-((6 .*dSigmawdBm.^3)/Sigmaw^4)+(6.* dSigmawdBm .* d2SigmawdBm2)/Sigmaw^3- d3SigmawdBm3/Sigmaw^2)- ...
      d4MuwdBm4/Sigmaw+(-Bm0+Bn-Muw).* ((24.* dSigmawdBm.^4)/Sigmaw^5-(36.* dSigmawdBm.^2 .*d2SigmawdBm2)/Sigmaw^4+ ...
      (6.* d2SigmawdBm2.^2)/Sigmaw^3+(8 .*dSigmawdBm .* d3SigmawdBm3)/Sigmaw.^3-d4SigmawdBm4/Sigmaw^2);
  
  
 
 d5ZtdBm5=-10.* ((2.* dSigmawdBm^2)/Sigmaw^3-d2SigmawdBm2/Sigmaw^2).* d3MuwdBm3-10.* d2MuwdBm2.* ...
     (-((6.* dSigmawdBm^3)/Sigmaw^4)+(6 .*dSigmawdBm.* d2SigmawdBm2)/Sigmaw^3-d3SigmawdBm3/Sigmaw^2)+ ...
     (5.* dSigmawdBm.* d4MuwdBm4)/Sigmaw^2+5.* (-1-dMuwdBm).* ((24.* dSigmawdBm^4)/Sigmaw^5- ...
     (36.* dSigmawdBm^2.* d2SigmawdBm2)/Sigmaw^4+(6.* d2SigmawdBm2^2)/Sigmaw^3+ ...
     (8.* dSigmawdBm.* d3SigmawdBm3)/Sigmaw^3-d4SigmawdBm4/Sigmaw^2)-d5MuwdBm5/Sigmaw+(-Bm0+Bn-Muw).* ...
     (-((120.* dSigmawdBm^5)/Sigmaw^6)+(240.* dSigmawdBm^3 .*d2SigmawdBm2)/Sigmaw^5- ...
     (90.* dSigmawdBm.* d2SigmawdBm2^2)/Sigmaw^4-(60.* dSigmawdBm^2.* d3SigmawdBm3)/Sigmaw^4+ ...
     (20 .*d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^3+(10.* dSigmawdBm.* d4SigmawdBm4)/Sigmaw^3-d5SigmawdBm5/Sigmaw^2); 
  
  
  
  
  d6ZtdBm6=-20.* d3MuwdBm3.* (-((6 .*dSigmawdBm.^3)/Sigmaw^4)+(6 .* dSigmawdBm.* d2SigmawdBm2)/Sigmaw^3- ...
      d3SigmawdBm3/Sigmaw.^2)-15.* ((2.* dSigmawdBm^2)/Sigmaw^3-d2SigmawdBm2/Sigmaw^2) .*d4MuwdBm4-15  .* ...
      d2MuwdBm2 .*((24.* dSigmawdBm.^4)/Sigmaw^5-(36.* dSigmawdBm^2 .* d2SigmawdBm2)/Sigmaw^4+ ...
      (6.* d2SigmawdBm2.^2)/Sigmaw^3+(8 .*dSigmawdBm .* d3SigmawdBm3)/Sigmaw^3-d4SigmawdBm4/Sigmaw^2)+ ...
      (6.* dSigmawdBm .* d5MuwdBm5)/Sigmaw^2+6 .*(-1-dMuwdBm) .* (-((120.* dSigmawdBm.^5)/Sigmaw^6)+ ...
      (240.* dSigmawdBm.^3.* d2SigmawdBm2)/Sigmaw^5-(90 .* dSigmawdBm .* d2SigmawdBm2.^2)/Sigmaw^4- ...
      (60 .*dSigmawdBm.^2.* d3SigmawdBm3)/Sigmaw^4+(20 .* d2SigmawdBm2 .* d3SigmawdBm3)/Sigmaw^3+ ...
      (10.* dSigmawdBm .* d4SigmawdBm4)/Sigmaw^3-d5SigmawdBm5/Sigmaw^2)-d6MuwdBm6/Sigmaw+(-Bm0+Bn-Muw).* ...
      ((720.* dSigmawdBm.^6)/Sigmaw^7-(1800.* dSigmawdBm.^4.* d2SigmawdBm2)/Sigmaw^6+(1080 .*dSigmawdBm.^2 .* d2SigmawdBm2.^2)/Sigmaw^5- ...
      (90.* d2SigmawdBm2^3)/Sigmaw^4+(480.* dSigmawdBm.^3.* d3SigmawdBm3)/Sigmaw^5- ...
      (360.* dSigmawdBm .*  d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^4+(20 .* d3SigmawdBm3.^2)/Sigmaw^3- ...
      (90.* dSigmawdBm.^2 .* d4SigmawdBm4)/Sigmaw^4+(30.* d2SigmawdBm2 .* d4SigmawdBm4)/Sigmaw^3+ ...
      (12 .* dSigmawdBm .* d5SigmawdBm5)/Sigmaw^3-d6SigmawdBm6/Sigmaw^2);
  
  d7ZtdBm7=-35.* (-((6.* dSigmawdBm^3)/Sigmaw^4)+(6.* dSigmawdBm.* d2SigmawdBm2)/Sigmaw^3-d3SigmawdBm3/Sigmaw^2).* d4MuwdBm4- ...
      35.* d3MuwdBm3.* ((24.* dSigmawdBm^4)/Sigmaw^5-(36.* dSigmawdBm^2.* d2SigmawdBm2)/Sigmaw^4+(6.* d2SigmawdBm2^2)/Sigmaw^3+ ...
      (8.* dSigmawdBm.* d3SigmawdBm3)/Sigmaw^3-d4SigmawdBm4/Sigmaw^2)-21.* ((2.* dSigmawdBm^2)/Sigmaw^3-d2SigmawdBm2/Sigmaw^2).* d5MuwdBm5- ...
      21.* d2MuwdBm2 .*(-((120.* dSigmawdBm^5)/Sigmaw^6)+(240.* dSigmawdBm^3 .*d2SigmawdBm2)/Sigmaw^5-(90.* dSigmawdBm.* d2SigmawdBm2^2)/Sigmaw^4- ...
      (60.* dSigmawdBm^2.* d3SigmawdBm3)/Sigmaw^4+(20.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^3+(10.* dSigmawdBm.* d4SigmawdBm4)/Sigmaw^3- ...
      d5SigmawdBm5/Sigmaw^2)+(7.* dSigmawdBm.* d6MuwdBm6)/Sigmaw^2+7 .*(-1-dMuwdBm).* ((720.* dSigmawdBm^6)/Sigmaw^7- ...
      (1800.* dSigmawdBm^4 .*d2SigmawdBm2)/Sigmaw^6+(1080.* dSigmawdBm^2.* d2SigmawdBm2^2)/Sigmaw^5-(90.* d2SigmawdBm2^3)/Sigmaw^4+ ...
      (480.* dSigmawdBm^3 .*d3SigmawdBm3)/Sigmaw^5-(360 .*dSigmawdBm.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^4+ ...
      (20.* d3SigmawdBm3^2)/Sigmaw^3-(90.* dSigmawdBm^2.* d4SigmawdBm4)/Sigmaw^4+(30.* d2SigmawdBm2.* d4SigmawdBm4)/Sigmaw^3+ ...
      (12.* dSigmawdBm.* d5SigmawdBm5)/Sigmaw^3-d6SigmawdBm6/Sigmaw^2)-d7MuwdBm7/Sigmaw+(-Bm0+Bn-Muw) .*(-((5040.* dSigmawdBm^7)/Sigmaw^8)+ ...
      (15120.* dSigmawdBm^5.* d2SigmawdBm2)/Sigmaw^7-(12600 .*dSigmawdBm^3.* d2SigmawdBm2^2)/Sigmaw^6+ ...
      (2520.* dSigmawdBm.* d2SigmawdBm2^3)/Sigmaw^5-(4200 .*dSigmawdBm^4.* d3SigmawdBm3)/Sigmaw^6+ ...
      (5040.* dSigmawdBm^2.* d2SigmawdBm2 .*d3SigmawdBm3)/Sigmaw^5-(630.* d2SigmawdBm2^2 .*d3SigmawdBm3)/Sigmaw^4- ...
      (420.* dSigmawdBm.* d3SigmawdBm3^2)/Sigmaw^4+(840.* dSigmawdBm^3 .*d4SigmawdBm4)/Sigmaw^5- ...
      (630.* dSigmawdBm.* d2SigmawdBm2.* d4SigmawdBm4)/Sigmaw^4+(70.* d3SigmawdBm3.* d4SigmawdBm4)/Sigmaw^3- ...
      (126.* dSigmawdBm^2.* d5SigmawdBm5)/Sigmaw^4+(42.* d2SigmawdBm2.* d5SigmawdBm5)/Sigmaw^3+ ...
      (14 .*dSigmawdBm .*d6SigmawdBm6)/Sigmaw^3-d7SigmawdBm7/Sigmaw^2);
  
  d8ZtdBm8=-70.* d4MuwdBm4.* ((24.* dSigmawdBm^4)./Sigmaw^5-(36.* dSigmawdBm^2.* d2SigmawdBm2)/Sigmaw^4+ ...
      (6.* d2SigmawdBm2^2)/Sigmaw^3+(8.* dSigmawdBm.* d3SigmawdBm3)/Sigmaw^3-d4SigmawdBm4/Sigmaw^2)-56.* (-((6.* dSigmawdBm^3)/Sigmaw^4)+ ...
      (6.* dSigmawdBm.* d2SigmawdBm2)/Sigmaw^3-d3SigmawdBm3/Sigmaw^2).* d5MuwdBm5-56.* d3MuwdBm3 .*(-((120.* dSigmawdBm^5)/Sigmaw^6)+ ...
      (240.* dSigmawdBm^3.* d2SigmawdBm2)/Sigmaw^5-(90.* dSigmawdBm.* d2SigmawdBm2^2)/Sigmaw^4-(60.* dSigmawdBm^2.* d3SigmawdBm3)/Sigmaw^4+ ...
      (20.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^3+(10.* dSigmawdBm.* d4SigmawdBm4)/Sigmaw^3-d5SigmawdBm5/Sigmaw^2)- ...
      28.* ((2 .*dSigmawdBm^2)/Sigmaw^3-d2SigmawdBm2/Sigmaw^2).* d6MuwdBm6-28.* d2MuwdBm2.* ((720 .*dSigmawdBm^6)/Sigmaw^7- ...
      (1800.* dSigmawdBm^4.* d2SigmawdBm2)/Sigmaw^6+(1080.* dSigmawdBm^2.* d2SigmawdBm2^2)/Sigmaw^5-(90.* d2SigmawdBm2^3)/Sigmaw^4+ ...
      (480.* dSigmawdBm^3.* d3SigmawdBm3)/Sigmaw^5-(360.* dSigmawdBm .*d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^4+ ...
      (20.* d3SigmawdBm3^2)/Sigmaw^3-(90.* dSigmawdBm^2 .*d4SigmawdBm4)/Sigmaw^4+(30 .*d2SigmawdBm2 .*d4SigmawdBm4)/Sigmaw^3+ ...
      (12.* dSigmawdBm.* d5SigmawdBm5)/Sigmaw^3-d6SigmawdBm6/Sigmaw^2)+(8.* dSigmawdBm .*d7MuwdBm7)/Sigmaw^2+8 .*(-1-dMuwdBm).*...
      (-((5040 .*dSigmawdBm^7)/Sigmaw^8)+(15120.* dSigmawdBm^5.* d2SigmawdBm2)/Sigmaw^7-(12600.* dSigmawdBm^3.* d2SigmawdBm2^2)/Sigmaw^6+ ...
      (2520.* dSigmawdBm.* d2SigmawdBm2^3)/Sigmaw^5-(4200.* dSigmawdBm^4.* d3SigmawdBm3)/Sigmaw^6+ ...
      (5040.* dSigmawdBm^2 .*d2SigmawdBm2 .*d3SigmawdBm3)/Sigmaw^5-(630.* d2SigmawdBm2^2.* d3SigmawdBm3)/Sigmaw^4- ...
      (420.* dSigmawdBm.* d3SigmawdBm3^2)/Sigmaw^4+(840.* dSigmawdBm^3.* d4SigmawdBm4)/Sigmaw^5- ...
      (630.* dSigmawdBm.* d2SigmawdBm2.* d4SigmawdBm4)/Sigmaw^4+(70.* d3SigmawdBm3 .*d4SigmawdBm4)/Sigmaw^3- ...
      (126 .*dSigmawdBm^2 .*d5SigmawdBm5)/Sigmaw^4+(42.* d2SigmawdBm2 .*d5SigmawdBm5)/Sigmaw^3+ ...
      (14 .*dSigmawdBm .*d6SigmawdBm6)/Sigmaw^3-d7SigmawdBm7/Sigmaw^2)-d8MuwdBm8/Sigmaw+ ...
      (-Bm0+Bn-Muw).* ((40320.* dSigmawdBm^8)/Sigmaw^9-(141120.* dSigmawdBm^6.* d2SigmawdBm2)/Sigmaw^8+ ...
      (151200.* dSigmawdBm^4.* d2SigmawdBm2^2)/Sigmaw^7-(50400.* dSigmawdBm^2 .*d2SigmawdBm2^3)/Sigmaw^6+ ...
      (2520.* d2SigmawdBm2^4)/Sigmaw^5+(40320.* dSigmawdBm^5.* d3SigmawdBm3)/Sigmaw^7-...
      (67200.* dSigmawdBm^3.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^6+(20160 .*dSigmawdBm.* d2SigmawdBm2^2 .*d3SigmawdBm3)/Sigmaw^5+ ...
      (6720.* dSigmawdBm^2.* d3SigmawdBm3^2)/Sigmaw^5-(1680.* d2SigmawdBm2.* d3SigmawdBm3^2)/Sigmaw^4- ...
      (8400.* dSigmawdBm^4.* d4SigmawdBm4)/Sigmaw^6+(10080.* dSigmawdBm^2.* d2SigmawdBm2 .*d4SigmawdBm4)/Sigmaw^5- ...
      (1260 .*d2SigmawdBm2^2.* d4SigmawdBm4)/Sigmaw^4-(1680.* dSigmawdBm .*d3SigmawdBm3 .*d4SigmawdBm4)/Sigmaw^4+ ...
      (70 .*d4SigmawdBm4^2)/Sigmaw^3+(1344 .*dSigmawdBm^3.* d5SigmawdBm5)/Sigmaw^5-(1008 .*dSigmawdBm.* d2SigmawdBm2.* d5SigmawdBm5)/Sigmaw^4+ ...
      (112.* d3SigmawdBm3.* d5SigmawdBm5)/Sigmaw^3-(168.* dSigmawdBm^2.* d6SigmawdBm6)/Sigmaw^4+(56 .*d2SigmawdBm2.* d6SigmawdBm6)/Sigmaw^3+ ...
      (16.* dSigmawdBm.* d7SigmawdBm7)/Sigmaw^3-d8SigmawdBm8/Sigmaw^2);
  
  
  
  
  
  
  d9ZtdBm9=-126.* ((24.* dSigmawdBm^4)/Sigmaw^5-(36 .*dSigmawdBm^2.* d2SigmawdBm2)/Sigmaw^4+(6.* d2SigmawdBm2^2)/Sigmaw^3+ ...
      (8.* dSigmawdBm.* d3SigmawdBm3)/Sigmaw^3-d4SigmawdBm4/Sigmaw^2).* d5MuwdBm5-126.* d4MuwdBm4.* (-((120 .*dSigmawdBm^5)/Sigmaw^6)+ ...
      (240.* dSigmawdBm^3.* d2SigmawdBm2)/Sigmaw^5-(90.* dSigmawdBm .*d2SigmawdBm2^2)/Sigmaw^4-(60.* dSigmawdBm^2 .*d3SigmawdBm3)/Sigmaw^4+ ...
      (20.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^3+(10.* dSigmawdBm.* d4SigmawdBm4)/Sigmaw^3-d5SigmawdBm5/Sigmaw^2)- ...
      84.* (-((6 .*dSigmawdBm^3)/Sigmaw^4)+(6.* dSigmawdBm .*d2SigmawdBm2)/Sigmaw^3-d3SigmawdBm3/Sigmaw^2).* d6MuwdBm6- ...
      84 .*d3MuwdBm3.* ((720.* dSigmawdBm^6)/Sigmaw^7-(1800.* dSigmawdBm^4 .*d2SigmawdBm2)/Sigmaw^6+ ...
      (1080.* dSigmawdBm^2.* d2SigmawdBm2^2)/Sigmaw^5-(90.* d2SigmawdBm2^3)/Sigmaw^4+(480.* dSigmawdBm^3.* d3SigmawdBm3)/Sigmaw^5- ...
      (360.* dSigmawdBm.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^4+(20.* d3SigmawdBm3^2)/Sigmaw^3-(90.* dSigmawdBm^2.* d4SigmawdBm4)/Sigmaw^4+ ...
      (30.* d2SigmawdBm2.* d4SigmawdBm4)/Sigmaw^3+(12.* dSigmawdBm .*d5SigmawdBm5)/Sigmaw^3-d6SigmawdBm6/Sigmaw^2)- ...
      36.* ((2 .*dSigmawdBm^2)/Sigmaw^3-d2SigmawdBm2/Sigmaw^2) .*d7MuwdBm7-36.* d2MuwdBm2 .*(-((5040.* dSigmawdBm^7)/Sigmaw^8)+ ...
      (15120 .*dSigmawdBm^5.* d2SigmawdBm2)/Sigmaw^7-(12600.* dSigmawdBm^3.* d2SigmawdBm2^2)/Sigmaw^6+ ...
      (2520.* dSigmawdBm.* d2SigmawdBm2^3)/Sigmaw^5-(4200.* dSigmawdBm^4 .*d3SigmawdBm3)/Sigmaw^6+ ...
      (5040.* dSigmawdBm^2.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^5-(630 .*d2SigmawdBm2^2.* d3SigmawdBm3)/Sigmaw^4- ...
      (420.* dSigmawdBm.* d3SigmawdBm3^2)/Sigmaw^4+(840.* dSigmawdBm^3.* d4SigmawdBm4)/Sigmaw^5- ...
      (630.* dSigmawdBm.* d2SigmawdBm2.* d4SigmawdBm4)/Sigmaw^4+(70 .*d3SigmawdBm3.* d4SigmawdBm4)/Sigmaw^3- ...
      (126.* dSigmawdBm^2.* d5SigmawdBm5)/Sigmaw^4+(42.* d2SigmawdBm2 .*d5SigmawdBm5)/Sigmaw^3+ ...
      (14.* dSigmawdBm.* d6SigmawdBm6)/Sigmaw^3-d7SigmawdBm7/Sigmaw^2)+(9.* dSigmawdBm .*d8MuwdBm8)/Sigmaw^2+ ...
      9 .*(-1-dMuwdBm).* ((40320.* dSigmawdBm^8)/Sigmaw^9-(141120.* dSigmawdBm^6.* d2SigmawdBm2)/Sigmaw^8+ ...
      (151200.* dSigmawdBm^4.* d2SigmawdBm2^2)/Sigmaw^7-(50400.* dSigmawdBm^2 .*d2SigmawdBm2^3)/Sigmaw^6+ ...
      (2520.* d2SigmawdBm2^4)/Sigmaw^5+(40320.* dSigmawdBm^5.* d3SigmawdBm3)/Sigmaw^7- ...
      (67200 .*dSigmawdBm^3.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^6+(20160.* dSigmawdBm .*d2SigmawdBm2^2.* d3SigmawdBm3)/Sigmaw^5+ ...
      (6720.* dSigmawdBm^2.* d3SigmawdBm3^2)/Sigmaw^5-(1680.* d2SigmawdBm2.* d3SigmawdBm3^2)/Sigmaw^4- ...
      (8400 .*dSigmawdBm^4.* d4SigmawdBm4)/Sigmaw^6+(10080.* dSigmawdBm^2.* d2SigmawdBm2.* d4SigmawdBm4)/Sigmaw^5- ...
      (1260.* d2SigmawdBm2^2.* d4SigmawdBm4)/Sigmaw^4-(1680 .*dSigmawdBm .*d3SigmawdBm3.* d4SigmawdBm4)/Sigmaw^4+ ...
      (70.* d4SigmawdBm4^2)/Sigmaw^3+(1344.* dSigmawdBm^3.* d5SigmawdBm5)/Sigmaw^5-(1008.* dSigmawdBm.* d2SigmawdBm2.* d5SigmawdBm5)/Sigmaw^4+ ...
      (112 .*d3SigmawdBm3.* d5SigmawdBm5)/Sigmaw^3-(168 .*dSigmawdBm^2.* d6SigmawdBm6)/Sigmaw^4+(56.* d2SigmawdBm2 .*d6SigmawdBm6)/Sigmaw^3+ ...
      (16.* dSigmawdBm .*d7SigmawdBm7)/Sigmaw^3-d8SigmawdBm8/Sigmaw^2)-d9MuwdBm9/Sigmaw+(-Bm0+Bn-Muw).* (-((362880.* dSigmawdBm^9)/Sigmaw^10)+ ...
      (1451520.* dSigmawdBm^7 .*d2SigmawdBm2)/Sigmaw^9-(1905120.* dSigmawdBm^5 .*d2SigmawdBm2^2)/Sigmaw^8+ ...
      (907200 .*dSigmawdBm^3.* d2SigmawdBm2^3)/Sigmaw^7-(113400.* dSigmawdBm.* d2SigmawdBm2^4)/Sigmaw^6- ...
      (423360.* dSigmawdBm^6.* d3SigmawdBm3)/Sigmaw^8+(907200.* dSigmawdBm^4.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^7- ...
      (453600.* dSigmawdBm^2 .*d2SigmawdBm2^2.* d3SigmawdBm3)/Sigmaw^6+(30240.* d2SigmawdBm2^3 .*d3SigmawdBm3)/Sigmaw^5- ...
      (100800.* dSigmawdBm^3.* d3SigmawdBm3^2)/Sigmaw^6+(60480.* dSigmawdBm .*d2SigmawdBm2 .*d3SigmawdBm3^2)/Sigmaw^5- ...
      (1680.* d3SigmawdBm3^3)/Sigmaw^4+(90720.* dSigmawdBm^5 .*d4SigmawdBm4)/Sigmaw^7- ...
      (151200.* dSigmawdBm^3 .*d2SigmawdBm2.* d4SigmawdBm4)/Sigmaw^6+(45360.* dSigmawdBm.* d2SigmawdBm2^2.* d4SigmawdBm4)/Sigmaw^5+ ...
      (30240.* dSigmawdBm^2.* d3SigmawdBm3.* d4SigmawdBm4)/Sigmaw^5-(7560.* d2SigmawdBm2.* d3SigmawdBm3.* d4SigmawdBm4)/Sigmaw^4- ...
      (1890 .*dSigmawdBm.* d4SigmawdBm4^2)/Sigmaw^4-(15120.* dSigmawdBm^4.* d5SigmawdBm5)/Sigmaw^6+ ...
      (18144.* dSigmawdBm^2.* d2SigmawdBm2.* d5SigmawdBm5)/Sigmaw^5-(2268.* d2SigmawdBm2^2.* d5SigmawdBm5)/Sigmaw^4- ...
      (3024.* dSigmawdBm .*d3SigmawdBm3.* d5SigmawdBm5)/Sigmaw^4+(252.* d4SigmawdBm4.* d5SigmawdBm5)/Sigmaw^3+ ...
      (2016 .*dSigmawdBm^3.* d6SigmawdBm6)/Sigmaw^5-(1512.* dSigmawdBm.* d2SigmawdBm2.* d6SigmawdBm6)/Sigmaw^4+ ...
      (168 .*d3SigmawdBm3.* d6SigmawdBm6)/Sigmaw^3-(216.* dSigmawdBm^2.* d7SigmawdBm7)/Sigmaw^4+ ...
      (72.* d2SigmawdBm2.* d7SigmawdBm7)/Sigmaw^3+(18.* dSigmawdBm.* d8SigmawdBm8)/Sigmaw^3-d9SigmawdBm9/Sigmaw^2);
  
  d10ZtdBm10=-252.* d5MuwdBm5 .*(-((120.* dSigmawdBm^5)/Sigmaw^6)+(240 .*dSigmawdBm^3.* d2SigmawdBm2)/Sigmaw^5- ...
      (90.* dSigmawdBm.* d2SigmawdBm2^2)/Sigmaw^4-(60.* dSigmawdBm^2.* d3SigmawdBm3)/Sigmaw^4+(20 .*d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^3+ ...
      (10.* dSigmawdBm.* d4SigmawdBm4)/Sigmaw^3-d5SigmawdBm5/Sigmaw^2)-210.* ((24.* dSigmawdBm^4)/Sigmaw^5- ...
      (36.* dSigmawdBm^2 .*d2SigmawdBm2)/Sigmaw^4+(6.* d2SigmawdBm2^2)/Sigmaw^3+(8 .*dSigmawdBm .*d3SigmawdBm3)/Sigmaw^3- ...
      d4SigmawdBm4/Sigmaw^2).* d6MuwdBm6-210.* d4MuwdBm4.* ((720 .*dSigmawdBm^6)/Sigmaw^7-(1800.* dSigmawdBm^4 .*d2SigmawdBm2)/Sigmaw^6+ ...
      (1080.* dSigmawdBm^2.* d2SigmawdBm2^2)/Sigmaw^5-(90.* d2SigmawdBm2^3)/Sigmaw^4+(480.* dSigmawdBm^3 .*d3SigmawdBm3)/Sigmaw^5- ...
      (360.* dSigmawdBm.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^4+(20.* d3SigmawdBm3^2)/Sigmaw^3-(90.* dSigmawdBm^2 .*d4SigmawdBm4)/Sigmaw^4+ ...
      (30.* d2SigmawdBm2.* d4SigmawdBm4)/Sigmaw^3+(12.* dSigmawdBm.* d5SigmawdBm5)/Sigmaw^3-d6SigmawdBm6/Sigmaw^2)- ...
      120.* (-((6.* dSigmawdBm^3)/Sigmaw^4)+(6.* dSigmawdBm.* d2SigmawdBm2)/Sigmaw^3-d3SigmawdBm3/Sigmaw^2) .*d7MuwdBm7- ...
      120.* d3MuwdBm3.* (-((5040 .*dSigmawdBm^7)/Sigmaw^8)+(15120.* dSigmawdBm^5.* d2SigmawdBm2)/Sigmaw^7- ...
      (12600.* dSigmawdBm^3.* d2SigmawdBm2^2)/Sigmaw^6+(2520.* dSigmawdBm.* d2SigmawdBm2^3)/Sigmaw^5- ...
      (4200.* dSigmawdBm^4.* d3SigmawdBm3)/Sigmaw^6+(5040 .*dSigmawdBm^2.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^5- ...
      (630.* d2SigmawdBm2^2.* d3SigmawdBm3)/Sigmaw^4-(420.* dSigmawdBm.* d3SigmawdBm3^2)/Sigmaw^4+ ...
      (840.* dSigmawdBm^3.* d4SigmawdBm4)/Sigmaw^5-(630.* dSigmawdBm.* d2SigmawdBm2 .*d4SigmawdBm4)/Sigmaw^4+ ...
      (70.* d3SigmawdBm3.* d4SigmawdBm4)/Sigmaw^3-(126 .*dSigmawdBm^2.* d5SigmawdBm5)/Sigmaw^4+(42.* d2SigmawdBm2.* d5SigmawdBm5)/Sigmaw^3+ ...
      (14.* dSigmawdBm.* d6SigmawdBm6)/Sigmaw^3-d7SigmawdBm7/Sigmaw^2)-45.* ((2 .*dSigmawdBm^2)/Sigmaw^3-d2SigmawdBm2/Sigmaw^2).* d8MuwdBm8- ...
      45.* d2MuwdBm2.* ((40320 .*dSigmawdBm^8)/Sigmaw^9-(141120.* dSigmawdBm^6 .*d2SigmawdBm2)/Sigmaw^8+ ...
      (151200.* dSigmawdBm^4.* d2SigmawdBm2^2)/Sigmaw^7-(50400 .*dSigmawdBm^2 .*d2SigmawdBm2^3)/Sigmaw^6+(2520.* d2SigmawdBm2^4)/Sigmaw^5+ ...
      (40320.* dSigmawdBm^5.* d3SigmawdBm3)/Sigmaw^7-(67200 .*dSigmawdBm^3.* d2SigmawdBm2.* d3SigmawdBm3)/Sigmaw^6+ ...
      (20160.* dSigmawdBm.* d2SigmawdBm2^2.* d3SigmawdBm3)/Sigmaw^5+(6720.* dSigmawdBm^2.* d3SigmawdBm3^2)/Sigmaw^5- ...
      (1680 .*d2SigmawdBm2.* d3SigmawdBm3^2)/Sigmaw^4-(8400.* dSigmawdBm^4 .*d4SigmawdBm4)/Sigmaw^6+ ...
      (10080 .*dSigmawdBm^2.* d2SigmawdBm2.* d4SigmawdBm4)/Sigmaw^5-(1260.* d2SigmawdBm2^2 .*d4SigmawdBm4)/Sigmaw^4- ...
      (1680 .*dSigmawdBm.* d3SigmawdBm3.* d4SigmawdBm4)/Sigmaw^4+(70 .*d4SigmawdBm4^2)/Sigmaw^3+(1344.* dSigmawdBm^3.* d5SigmawdBm5)/Sigmaw^5- ...
      (1008.* dSigmawdBm.* d2SigmawdBm2.* d5SigmawdBm5)/Sigmaw^4+(112.* d3SigmawdBm3 .*d5SigmawdBm5)/Sigmaw^3- ...
      (168.* dSigmawdBm^2.* d6SigmawdBm6)/Sigmaw^4+(56.* d2SigmawdBm2.* d6SigmawdBm6)/Sigmaw^3+(16.* dSigmawdBm .*d7SigmawdBm7)/Sigmaw^3-d8SigmawdBm8/Sigmaw^2)+ ...
      (10.* dSigmawdBm.* d9MuwdBm9)/Sigmaw^2+10 .*(-1-dMuwdBm).* (-((362880 .*dSigmawdBm^9)/Sigmaw^10)+(1451520.* dSigmawdBm^7 .*d2SigmawdBm2)/Sigmaw^9- ...
      (1905120.* dSigmawdBm^5.* d2SigmawdBm2^2)/Sigmaw^8+(907200.* dSigmawdBm^3.* d2SigmawdBm2^3)/Sigmaw^7- ...
      (113400.* dSigmawdBm.* d2SigmawdBm2^4)/Sigmaw^6-(423360.* dSigmawdBm^6 .*d3SigmawdBm3)/Sigmaw^8+ ...
      (907200.* dSigmawdBm^4.* d2SigmawdBm2 .*d3SigmawdBm3)/Sigmaw^7-(453600 .*dSigmawdBm^2.* d2SigmawdBm2^2.* d3SigmawdBm3)/Sigmaw^6+ ...
      (30240.* d2SigmawdBm2^3.* d3SigmawdBm3)/Sigmaw^5-(100800.* dSigmawdBm^3.* d3SigmawdBm3^2)/Sigmaw^6+ ...
      (60480.* dSigmawdBm.* d2SigmawdBm2.* d3SigmawdBm3^2)/Sigmaw^5-(1680.* d3SigmawdBm3^3)/Sigmaw^4+ ...
      (90720 .*dSigmawdBm^5 .*d4SigmawdBm4)/Sigmaw^7-(151200.* dSigmawdBm^3.* d2SigmawdBm2 .*d4SigmawdBm4)/Sigmaw^6+ ...
      (45360.* dSigmawdBm.* d2SigmawdBm2^2.* d4SigmawdBm4)/Sigmaw^5+(30240.* dSigmawdBm^2 .*d3SigmawdBm3.* d4SigmawdBm4)/Sigmaw^5- ...
      (7560.* d2SigmawdBm2.* d3SigmawdBm3.* d4SigmawdBm4)/Sigmaw^4-(1890.* dSigmawdBm.* d4SigmawdBm4^2)/Sigmaw^4- ...
      (15120 .*dSigmawdBm^4.* d5SigmawdBm5)/Sigmaw^6+(18144.* dSigmawdBm^2.* d2SigmawdBm2 .*d5SigmawdBm5)/Sigmaw^5- ...
      (2268 .*d2SigmawdBm2^2.* d5SigmawdBm5)/Sigmaw^4-(3024.* dSigmawdBm.* d3SigmawdBm3.* d5SigmawdBm5)/Sigmaw^4+ ...
      (252.* d4SigmawdBm4.* d5SigmawdBm5)/Sigmaw^3+(2016 .*dSigmawdBm^3.* d6SigmawdBm6)/Sigmaw^5- ...
      (1512.* dSigmawdBm.* d2SigmawdBm2.* d6SigmawdBm6)/Sigmaw^4+(168.* d3SigmawdBm3.* d6SigmawdBm6)/Sigmaw^3- ...
      (216 .*dSigmawdBm^2.* d7SigmawdBm7)/Sigmaw^4+(72.* d2SigmawdBm2.* d7SigmawdBm7)/Sigmaw^3+(18.* dSigmawdBm.* d8SigmawdBm8)/Sigmaw^3- ...
      d9SigmawdBm9/Sigmaw^2)-d10MuwdBm10/Sigmaw+(-Bm0+Bn-Muw) .*((3628800.* dSigmawdBm^10)/Sigmaw^11- ...
      (16329600.* dSigmawdBm^8.* d2SigmawdBm2)/Sigmaw^10+(25401600.* dSigmawdBm^6 .*d2SigmawdBm2^2)/Sigmaw^9- ...
      (15876000 .*dSigmawdBm^4.* d2SigmawdBm2^3)/Sigmaw^8+(3402000.* dSigmawdBm^2 .*d2SigmawdBm2^4)/Sigmaw^7- ...
      (113400.* d2SigmawdBm2^5)/Sigmaw^6+(4838400.* dSigmawdBm^7.* d3SigmawdBm3)/Sigmaw^9- ...
      (12700800.* dSigmawdBm^5.* d2SigmawdBm2 .*d3SigmawdBm3)/Sigmaw^8+(9072000.* dSigmawdBm^3 .*d2SigmawdBm2^2 .*d3SigmawdBm3)/Sigmaw^7- ...
      (1512000.* dSigmawdBm.* d2SigmawdBm2^3.* d3SigmawdBm3)/Sigmaw^6+(1512000 .*dSigmawdBm^4.* d3SigmawdBm3^2)/Sigmaw^7- ...
      (1512000 .*dSigmawdBm^2.* d2SigmawdBm2.* d3SigmawdBm3^2)/Sigmaw^6+(151200.* d2SigmawdBm2^2 .*d3SigmawdBm3^2)/Sigmaw^5+ ...
      (67200.* dSigmawdBm.* d3SigmawdBm3^3)/Sigmaw^5-(1058400 .*dSigmawdBm^6.* d4SigmawdBm4)/Sigmaw^8+ ...
      (2268000.* dSigmawdBm^4.* d2SigmawdBm2 .*d4SigmawdBm4)/Sigmaw^7-(1134000.* dSigmawdBm^2.* d2SigmawdBm2^2.* d4SigmawdBm4)/Sigmaw^6+ ...
      (75600 .*d2SigmawdBm2^3.* d4SigmawdBm4)/Sigmaw^5-(504000.* dSigmawdBm^3.* d3SigmawdBm3 .*d4SigmawdBm4)/Sigmaw^6+ ...
      (302400 .*dSigmawdBm.* d2SigmawdBm2.* d3SigmawdBm3.* d4SigmawdBm4)/Sigmaw^5- ...
      (12600.* d3SigmawdBm3^2.* d4SigmawdBm4)/Sigmaw^4+(37800.* dSigmawdBm^2.* d4SigmawdBm4^2)/Sigmaw^5- ...
      (9450.* d2SigmawdBm2.* d4SigmawdBm4^2)/Sigmaw^4+(181440.* dSigmawdBm^5 .*d5SigmawdBm5)/Sigmaw^7- ...
      (302400.* dSigmawdBm^3.* d2SigmawdBm2.* d5SigmawdBm5)/Sigmaw^6+(90720.* dSigmawdBm.* d2SigmawdBm2^2.* d5SigmawdBm5)/Sigmaw^5+ ...
      (60480.* dSigmawdBm^2.* d3SigmawdBm3.* d5SigmawdBm5)/Sigmaw^5-(15120 .*d2SigmawdBm2 .*d3SigmawdBm3 .*d5SigmawdBm5)/Sigmaw^4- ...
      (7560.* dSigmawdBm.* d4SigmawdBm4 .*d5SigmawdBm5)/Sigmaw^4+(252 .*d5SigmawdBm5^2)/Sigmaw^3- ...
      (25200.* dSigmawdBm^4.* d6SigmawdBm6)/Sigmaw^6+(30240.* dSigmawdBm^2 .*d2SigmawdBm2.* d6SigmawdBm6)/Sigmaw^5- ...
      (3780.* d2SigmawdBm2^2.* d6SigmawdBm6)/Sigmaw^4-(5040.* dSigmawdBm.* d3SigmawdBm3.* d6SigmawdBm6)/Sigmaw^4+ ...
      (420.* d4SigmawdBm4.* d6SigmawdBm6)/Sigmaw^3+(2880 .*dSigmawdBm^3.* d7SigmawdBm7)/Sigmaw^5- ...
      (2160 .*dSigmawdBm .*d2SigmawdBm2.* d7SigmawdBm7)/Sigmaw^4+(240.* d3SigmawdBm3.* d7SigmawdBm7)/Sigmaw^3- ...
      (270.* dSigmawdBm^2.* d8SigmawdBm8)/Sigmaw^4+(90.* d2SigmawdBm2.* d8SigmawdBm8)/Sigmaw^3+(20 .*dSigmawdBm.* d9SigmawdBm9)/Sigmaw^3- ...
      d10SigmawdBm10/Sigmaw^2);
  
dPm0ndBm=dPm0ndZt.*dZtdBm;
d2Pm0ndBm2=d2Pm0ndZt2.*dZtdBm.^2+dPm0ndZt.*d2ZtdBm2;
d3Pm0ndBm3=d3Pm0ndZt3.*dZtdBm.^3+3*d2Pm0ndZt2.*dZtdBm.*d2ZtdBm2+dPm0ndZt.*d3ZtdBm3;
d4Pm0ndBm4=d4Pm0ndZt4.*dZtdBm.^4+6*d3Pm0ndZt3.*dZtdBm.^2.*d2ZtdBm2+4*d2Pm0ndZt2.*dZtdBm.*d3ZtdBm3+ ...
    3*d2Pm0ndZt2.*d2ZtdBm2.^2+dPm0ndZt.*d4ZtdBm4;
d5Pm0ndBm5=d5Pm0ndZt5.*dZtdBm.^5+10*d4Pm0ndZt4.*dZtdBm.^3.*d2ZtdBm2+15*d3Pm0ndZt3.*dZtdBm.*d2ZtdBm2.^2+ ...
    10*d3Pm0ndZt3.*dZtdBm.^2.*d3ZtdBm3+10*d2Pm0ndZt2.*d2ZtdBm2.*d3ZtdBm3+ ...
    5*d2Pm0ndZt2.*dZtdBm.*d4ZtdBm4+dPm0ndZt.*d5ZtdBm5;
d6Pm0ndBm6=d6Pm0ndZt6.*dZtdBm.^6+15*d5Pm0ndZt5.*dZtdBm.^4.*d2ZtdBm2+45*d4Pm0ndZt4.*dZtdBm.^2.*d2ZtdBm2.^2+ ...
    20*d4Pm0ndZt4.*dZtdBm.^3.*d3ZtdBm3+15*d3Pm0ndZt3.*d2ZtdBm2.^3+ ...
    +60*d3Pm0ndZt3.*dZtdBm.*d2ZtdBm2.*d3ZtdBm3+15*d3Pm0ndZt3.*dZtdBm.^2.*d4ZtdBm4+ ...
    +10*d2Pm0ndZt2.*d3ZtdBm3.^2+15*d2Pm0ndZt2.*d2ZtdBm2.*d4ZtdBm4+ ...
    6*d2Pm0ndZt2.*dZtdBm.*d5ZtdBm5+dPm0ndZt.*d6ZtdBm6;

d7Pm0ndBm7=105.* d2ZtdBm2^2.* d3Pm0ndZt3.* d3ZtdBm3+70.* dZtdBm.* d3Pm0ndZt3.* d3ZtdBm3^2+ ...
    105.* dZtdBm.* d2ZtdBm2^3.* d4Pm0ndZt4+210.* dZtdBm^2.* d2ZtdBm2.* d3ZtdBm3.* d4Pm0ndZt4+ ...
    105.* dZtdBm.* d2ZtdBm2.* d3Pm0ndZt3.* d4ZtdBm4+35.* d2Pm0ndZt2.* d3ZtdBm3.* d4ZtdBm4+ ...
    35.* dZtdBm^3.* d4Pm0ndZt4.* d4ZtdBm4+105.* dZtdBm^3.* d2ZtdBm2^2.* d5Pm0ndZt5+ ...
    35 .*dZtdBm^4.* d3ZtdBm3.* d5Pm0ndZt5+21.* d2Pm0ndZt2.* d2ZtdBm2.* d5ZtdBm5+21.* dZtdBm^2.* d3Pm0ndZt3.* d5ZtdBm5+...
    21.* dZtdBm^5.* d2ZtdBm2.* d6Pm0ndZt6+7 .*dZtdBm.* d2Pm0ndZt2.* d6ZtdBm6+dZtdBm^7.* d7Pm0ndZt7+dPm0ndZt.* d7ZtdBm7;
d8Pm0ndBm8=280.* d2ZtdBm2.* d3Pm0ndZt3.* d3ZtdBm3^2+105.* d2ZtdBm2^4.* d4Pm0ndZt4+840.* dZtdBm.* d2ZtdBm2^2.* d3ZtdBm3.* d4Pm0ndZt4+ ...
    280.* dZtdBm^2.* d3ZtdBm3^2.* d4Pm0ndZt4+210.* d2ZtdBm2^2.* d3Pm0ndZt3.* d4ZtdBm4+280.* dZtdBm.* d3Pm0ndZt3.* d3ZtdBm3.* d4ZtdBm4+...
    420.* dZtdBm^2.* d2ZtdBm2.* d4Pm0ndZt4 .*d4ZtdBm4+35.* d2Pm0ndZt2.* d4ZtdBm4^2+420.* dZtdBm^2.* d2ZtdBm2^3.* d5Pm0ndZt5+ ...
    560.* dZtdBm^3.* d2ZtdBm2.* d3ZtdBm3.* d5Pm0ndZt5+70.* dZtdBm^4.* d4ZtdBm4.* d5Pm0ndZt5+168.* dZtdBm.* d2ZtdBm2.* d3Pm0ndZt3.* d5ZtdBm5+ ...
    56.* d2Pm0ndZt2.* d3ZtdBm3.* d5ZtdBm5+56.*dZtdBm^3.* d4Pm0ndZt4 .*d5ZtdBm5+210.* dZtdBm^4.* d2ZtdBm2^2.* d6Pm0ndZt6+ ...
    56.* dZtdBm^5.* d3ZtdBm3.* d6Pm0ndZt6+28.* d2Pm0ndZt2.* d2ZtdBm2 .*d6ZtdBm6+28.* dZtdBm^2.* d3Pm0ndZt3.* d6ZtdBm6+ ...
    28.* dZtdBm^6.* d2ZtdBm2.* d7Pm0ndZt7+8.* dZtdBm.* d2Pm0ndZt2.* d7ZtdBm7+dZtdBm^8.* d8Pm0ndZt8+dPm0ndZt.* d8ZtdBm8;


d9Pm0ndBm9=280.* d3Pm0ndZt3.* d3ZtdBm3^3+1260 .*d2ZtdBm2^3.* d3ZtdBm3.* d4Pm0ndZt4+2520.* dZtdBm.* d2ZtdBm2.* d3ZtdBm3^2.* d4Pm0ndZt4+ ...
    1260.* d2ZtdBm2.* d3Pm0ndZt3.* d3ZtdBm3 .*d4ZtdBm4+1890.* dZtdBm .*d2ZtdBm2^2.* d4Pm0ndZt4.* d4ZtdBm4+ ...
    1260.* dZtdBm^2.* d3ZtdBm3.* d4Pm0ndZt4.* d4ZtdBm4+315 .*dZtdBm.* d3Pm0ndZt3.* d4ZtdBm4^2+945.* dZtdBm .*d2ZtdBm2^4.* d5Pm0ndZt5+ ...
    3780.* dZtdBm^2.* d2ZtdBm2^2.* d3ZtdBm3.* d5Pm0ndZt5+840.* dZtdBm^3.* d3ZtdBm3^2.* d5Pm0ndZt5+ ...
    1260.* dZtdBm^3.* d2ZtdBm2.* d4ZtdBm4.* d5Pm0ndZt5+378.* d2ZtdBm2^2 .*d3Pm0ndZt3 .*d5ZtdBm5+504 .*dZtdBm .*d3Pm0ndZt3.* d3ZtdBm3.* d5ZtdBm5+...
    756.* dZtdBm^2.* d2ZtdBm2.* d4Pm0ndZt4.* d5ZtdBm5+126.* d2Pm0ndZt2.* d4ZtdBm4.* d5ZtdBm5+126.* dZtdBm^4.* d5Pm0ndZt5.* d5ZtdBm5+ ...
    1260.* dZtdBm^3.* d2ZtdBm2^3.* d6Pm0ndZt6+1260.* dZtdBm^4.* d2ZtdBm2 .*d3ZtdBm3 .*d6Pm0ndZt6+ ...
    126 .*dZtdBm^5.* d4ZtdBm4.* d6Pm0ndZt6+252.* dZtdBm.* d2ZtdBm2.* d3Pm0ndZt3.* d6ZtdBm6+84.* d2Pm0ndZt2.* d3ZtdBm3.* d6ZtdBm6+ ...
    84.* dZtdBm^3.* d4Pm0ndZt4.* d6ZtdBm6+378.* dZtdBm^5 .*d2ZtdBm2^2 .*d7Pm0ndZt7+84 .*dZtdBm^6.* d3ZtdBm3.* d7Pm0ndZt7+ ...
    36.* d2Pm0ndZt2.* d2ZtdBm2.* d7ZtdBm7+36.* dZtdBm^2 .*d3Pm0ndZt3.* d7ZtdBm7+36 .*dZtdBm^7.* d2ZtdBm2 .*d8Pm0ndZt8+ ...
    9 .*dZtdBm.* d2Pm0ndZt2.* d8ZtdBm8+dZtdBm^9.* d9Pm0ndZt9+dPm0ndZt.* d9ZtdBm9;
d10Pm0ndBm10=6300.* d2ZtdBm2^2.* d3ZtdBm3^2.* d4Pm0ndZt4+2800.* dZtdBm.* d3ZtdBm3^3.* d4Pm0ndZt4+2100 .*d3Pm0ndZt3.* d3ZtdBm3^2.* d4ZtdBm4+ ...
    3150.* d2ZtdBm2^3 .*d4Pm0ndZt4.* d4ZtdBm4+12600.* dZtdBm.* d2ZtdBm2.* d3ZtdBm3.* d4Pm0ndZt4.* d4ZtdBm4+ ...
    1575 .*d2ZtdBm2 .*d3Pm0ndZt3.* d4ZtdBm4^2+1575 .*dZtdBm^2.* d4Pm0ndZt4.* d4ZtdBm4^2+945.* d2ZtdBm2^5.* d5Pm0ndZt5+ ...
    12600.* dZtdBm.* d2ZtdBm2^3.* d3ZtdBm3.* d5Pm0ndZt5+12600.* dZtdBm^2.* d2ZtdBm2.* d3ZtdBm3^2 .*d5Pm0ndZt5+ ...
    9450.* dZtdBm^2.* d2ZtdBm2^2.* d4ZtdBm4.* d5Pm0ndZt5+4200 .*dZtdBm^3 .*d3ZtdBm3.* d4ZtdBm4.* d5Pm0ndZt5+ ...
    2520.* d2ZtdBm2.* d3Pm0ndZt3.* d3ZtdBm3.* d5ZtdBm5+3780.* dZtdBm.* d2ZtdBm2^2.* d4Pm0ndZt4 .*d5ZtdBm5+ ...
    2520.* dZtdBm^2.* d3ZtdBm3.* d4Pm0ndZt4.* d5ZtdBm5+1260.* dZtdBm.* d3Pm0ndZt3.* d4ZtdBm4.* d5ZtdBm5+ ...
    2520.* dZtdBm^3.* d2ZtdBm2.* d5Pm0ndZt5.* d5ZtdBm5+126.* d2Pm0ndZt2 .*d5ZtdBm5^2+4725.* dZtdBm^2.* d2ZtdBm2^4 .*d6Pm0ndZt6+ ...
    12600.* dZtdBm^3.* d2ZtdBm2^2.* d3ZtdBm3.* d6Pm0ndZt6+2100.* dZtdBm^4.* d3ZtdBm3^2.* d6Pm0ndZt6+ ...
    3150.* dZtdBm^4.* d2ZtdBm2 .*d4ZtdBm4.* d6Pm0ndZt6+252.* dZtdBm^5.* d5ZtdBm5.* d6Pm0ndZt6+630.* d2ZtdBm2^2 .*d3Pm0ndZt3.* d6ZtdBm6+ ...
    840.* dZtdBm.* d3Pm0ndZt3.* d3ZtdBm3.* d6ZtdBm6+1260.* dZtdBm^2 .*d2ZtdBm2 .*d4Pm0ndZt4.* d6ZtdBm6+ ...
    210.* d2Pm0ndZt2.* d4ZtdBm4.* d6ZtdBm6+210.* dZtdBm^4.* d5Pm0ndZt5.* d6ZtdBm6+ ...
    3150.* dZtdBm^4.* d2ZtdBm2^3.* d7Pm0ndZt7+2520.* dZtdBm^5.* d2ZtdBm2.* d3ZtdBm3.* d7Pm0ndZt7+210 .*dZtdBm^6.* d4ZtdBm4.* d7Pm0ndZt7+ ...
    360.* dZtdBm.* d2ZtdBm2.* d3Pm0ndZt3 .*d7ZtdBm7+120.* d2Pm0ndZt2 .*d3ZtdBm3 .*d7ZtdBm7+120.* dZtdBm^3.* d4Pm0ndZt4.* d7ZtdBm7+ ...
    630 .*dZtdBm^6.* d2ZtdBm2^2.* d8Pm0ndZt8+120 .*dZtdBm^7 .*d3ZtdBm3 .*d8Pm0ndZt8+45.* d2Pm0ndZt2.* d2ZtdBm2.* d8ZtdBm8+ ...
    45 .*dZtdBm^2.* d3Pm0ndZt3.* d8ZtdBm8+45 .*dZtdBm^8.* d2ZtdBm2.* d9Pm0ndZt9+10 .*dZtdBm.* d2Pm0ndZt2 .*d9ZtdBm9+ ...
    dZtdBm^10.* d10Pm0ndZt10+dPm0ndZt.* d10ZtdBm10;

dBm=Bm2-Bm1;
%dBm1 is not needed.
dBm1=1/2* ((Bm2 - Bm0)^2 - (Bm1 - Bm0)^2);
dBm2=1/3* ((Bm2 - Bm0)^3 - (Bm1 - Bm0)^3)/2;
dBm3=1/4* ((Bm2 - Bm0)^4 - (Bm1 - Bm0)^4)/6;
dBm4=1/5* ((Bm2 - Bm0)^5 - (Bm1 - Bm0)^5)/24;
dBm5=1/6* ((Bm2 - Bm0)^6 - (Bm1 - Bm0)^6)/120;
dBm6=1/7* ((Bm2 - Bm0)^7 - (Bm1 - Bm0)^7)/720;
dBm7=1/8* ((Bm2 - Bm0)^8 - (Bm1 - Bm0)^8)/(720*7);
dBm8=1/9* ((Bm2 - Bm0)^9 - (Bm1 - Bm0)^9)/(720*7*8);
dBm9=1/10* ((Bm2 - Bm0)^10 - (Bm1 - Bm0)^10)/(720*7*8*9);
dBm10=1/11* ((Bm2 - Bm0)^11 - (Bm1 - Bm0)^11)/(720*7*8*9*10);




% IntegralAnalytic=Pm0n.*dBm + ...
%     +(dPm0ndBm)*dBm1+ ...
%     +(d2Pm0ndBm2) *dBm2 + ...  
%     +(d3Pm0ndBm3) *dBm3 + ...
%     +(d4Pm0ndBm4)*dBm4+ ...
%     +(d5Pm0ndBm5)*dBm5+ ...
%     +(d6Pm0ndBm6)*dBm6 + ...
%     (d7Pm0ndBm7)*dBm7 + ...
%     (d8Pm0ndBm8)*dBm8 + ...
%     (d9Pm0ndBm9)*dBm9 + ...
%     (d10Pm0ndBm10)*dBm10;
IntegralAnalyticO0=Pm0n.*dBm;

IntegralAnalyticO2=Pm0n.*dBm + ...
    +(dPm0ndBm)*dBm1+ ...
    +(d2Pm0ndBm2) *dBm2;   

IntegralAnalyticO4=Pm0n.*dBm + ...
    +(dPm0ndBm)*dBm1+ ...
    +(d2Pm0ndBm2) *dBm2 + ...  
    +(d3Pm0ndBm3) *dBm3 + ...
    +(d4Pm0ndBm4)*dBm4;

IntegralAnalyticO6=Pm0n.*dBm + ...
    +(dPm0ndBm)*dBm1+ ...
    +(d2Pm0ndBm2) *dBm2 + ...  
    +(d3Pm0ndBm3) *dBm3 + ...
    +(d4Pm0ndBm4)*dBm4+ ...
    +(d5Pm0ndBm5)*dBm5+ ...
    +(d6Pm0ndBm6)*dBm6;

IntegralAnalyticO8=Pm0n.*dBm + ...
    +(dPm0ndBm)*dBm1+ ...
  +(d2Pm0ndBm2) *dBm2 + ...  
    +(d3Pm0ndBm3) *dBm3 + ...
    +(d4Pm0ndBm4)*dBm4+ ...
    +(d5Pm0ndBm5)*dBm5+ ...
    +(d6Pm0ndBm6)*dBm6 + ...
    (d7Pm0ndBm7)*dBm7 + ...
    (d8Pm0ndBm8)*dBm8;

IntegralAnalyticO10=Pm0n.*dBm + ...
    +(dPm0ndBm)*dBm1+ ...
    +(d2Pm0ndBm2) *dBm2 + ...  
    +(d3Pm0ndBm3) *dBm3 + ...
    +(d4Pm0ndBm4)*dBm4+ ...
    +(d5Pm0ndBm5)*dBm5+ ...
    +(d6Pm0ndBm6)*dBm6 + ...
    (d7Pm0ndBm7)*dBm7 + ...
    (d8Pm0ndBm8)*dBm8 + ...
    (d9Pm0ndBm9)*dBm9 + ...
    (d10Pm0ndBm10)*dBm10;


 

IntegralAnalyticO0
IntegralAnalyticO2
IntegralAnalyticO4
IntegralAnalyticO6
IntegralAnalyticO8
IntegralAnalyticO10
Integral0


end
```


Here is the result of this program when run by command>> CheckCDFfromSubdivDriftVol08(.8,.75,.03125)

IntegralAnalyticO0 =

   0.019356181958274

IntegralAnalyticO2 =

   0.019272312682345

IntegralAnalyticO4 =

   0.019273921209310

IntegralAnalyticO6 =

   0.019273899789850

IntegralAnalyticO8 =

   0.019273899942692

IntegralAnalyticO10 =

   0.019273899943666

Integral0 =

   0.019273899943599
```

---

## Error 21: Unbalanced $: 117

**Snippet:** `>  > Friends I had some ideas about series solution of fokker-planck equation an`

**Full content:**

```
> 
> Friends I had some ideas about series solution of fokker-planck equation and I decided to share my initial ideas with friends. I have not yet implemented anything but the ideas are interesting so I hope friends would like them. I intend to represent the solution of PDE as a series in Z and then find an algorithm how to advance the series coefficients in time. This is first part that I will discuss in this post. There is a second part in which I will represent the series coefficients in powers of t and then find an iterated integral type solution for longer stepping of solution in time. I will come to this second part in a later post in a few days.
> 
> 
> 
> First we suppose that we can express the solution of X(t) where X is the SDE/PDE variable as 
> 
> 
> 
> $X(t)=a_0  \,+ a_1 \, Z + a_2 \, Z^2 + a_3 \, Z^3 +  a_4 \, Z^4 +\, ... $ 
> 
> 
> 
> its derivatives can be calculated as
> 
> 
> 
> $\frac{\partial X(t)}{\partial Z}= a_1 \, + 2 \,a_2 \, Z +3 \, a_3 \, Z^2 +4 \,  a_4 \, Z^3 +\, ... $ 
> 
> $\frac{\partial^2 X(t)}{\partial Z^2}=  2 \,a_2 \, +6 \, a_3 \, Z +12 \,  a_4 \, Z^2 +\, ... $ 
> 
> 
> 
> Let us suppose that we can represent the solution $X(t+\Delta t)$ as 
> 
> 
> 
> $X(t+\Delta t)=c_0  \,+ c_1 \, Z + c_2 \, Z^2 + c_3 \, Z^3 +  c_4 \, Z^4 +\, ... $
> 
> 
> 
> All the coefficients c's at next time step variable $X(t+\Delta t)$ are supposedly unknown and these are the ones we want to find out in our recursions.
> 
> 
> 
> For our analytics, we would have to also represent the time dependent drift as a series in Z 
> 
> 
> 
> $\mu(X(t))=b_0  \,+ b_1 \, Z + b_2 \, Z^2 + b_3 \, Z^3 +  b_4 \, Z^4 +\, ... $
> 
> 
> 
> We do not want to use finite differences anywhere so in order to find the coefficients $b_0, \, b_1, \, b_2$ and so on we use 
> 
> 
> 
> $b_0 = \mu(X(Z_0))$  where $Z_0$ means calculating at  Z=0.
> 
> 
> 
> $b_1 = \frac{\partial \mu}{\partial X} \, \frac{\partial X}{\partial Z}=\frac{\partial \mu}{\partial X} \, [a_0  \,+ a_1 \, Z + a_2 \, Z^2 + a_3 \, Z^3 +  a_4 \, Z^4 ] |^{Z=0} $
> 
> $=a_1 \,\frac{\partial \mu}{\partial X}|^{Z=0}$
> 
> 
> 
> $b_2 = \frac{\partial^2 \mu}{\partial X^2} \, {(\frac{\partial X}{\partial Z})}^2 + \frac{\partial \mu}{\partial X} \, \frac{\partial^2 X}{\partial Z^2}=[\frac{\partial^2 \mu}{\partial X^2} \, {a_1}^2 + \frac{\partial \mu}{\partial X} 2 \, a_2 ] |^{Z=0} $
> 
> 
> 
> and so we can analytically find the derivatives of drift to any order analytically since derivatives with respect to X are found by analytic differentiation.
> 
> 
> 
> Now we have the evolution equation of the solution of Fokker-planck equation along CDF lines as
> 
> 
> 
> $X(t+\Delta t)=X(t) \, + \, \mu(X(t))\, + .5 \sigma^2 \Delta t \, Z \, \frac{\partial Z}{\partial X} +  .5 \sigma^2 \Delta t \, {(\frac{\partial Z}{\partial X})}^2 \frac{\partial^2 X}{\partial Z^2}$
> 
> 
> 
> Now we want to insert the series for $X(t), \, X(t+\Delta t) ,\, \mu(X(t))$ and try to solve for the coefficients but first We multiply both sides by ${(\frac{\partial X}{\partial Z})}^2$ so that series in denominator goes to numerator. This gives us
> 
> 
> 
> $X(t+\Delta t) \, {(\frac{\partial X}{\partial Z})}^2=X(t) \, {(\frac{\partial X}{\partial Z})}^2+ \, \mu(X(t))\, {(\frac{\partial X}{\partial Z})}^2+ .5 \sigma^2 \Delta t \, Z \, \frac{\partial X}{\partial Z} +  .5 \sigma^2 \Delta t \,  \frac{\partial^2 X}{\partial Z^2}$
> 
> 
> 
> Now we insert our series for each of the term in above expression as
> 
>  
> 
> $[c_0  \,+ c_1 \, Z + c_2 \, Z^2 + c_3 \, Z^3 + \, ...] \, {({a_1}^2+ 4 a_1 a_2 Z+ 4 {a_2}^2 Z^2+ 6 a_1 a_3 Z^2 + 12 a2 a_3 Z^3 + 8 a_1 a_4 Z^3 + 9 {a_3}^2 Z^4+ 16 a_2 a_4 Z^4 + \, ...)}$
> 
> $=[a_0  \,+ a_1 \, Z + a_2 \, Z^2 + a_3 \, Z^3 +  a_4 \, Z^4 +\, ...]  {({a_1}^2+ 4 a_1 a_2 Z+ 4 {a_2}^2 Z^2+ 6 a_1 a_3 Z^2 + 12 a2 a_3 Z^3 + 8 a_1 a_4 Z^3 + 9 {a_3}^2 Z^4+ 16 a_2 a_4 Z^4 + \, ...)}$
> 
> $+ \, [b_0  \,+ b_1 \, Z + b_2 \, Z^2 + b_3 \, Z^3 +  b_4 \, Z^4 +\, ...]  {({a_1}^2+ 4 a_1 a_2 Z+ 4 {a_2}^2 Z^2+ 6 a_1 a_3 Z^2 + 12 a2 a_3 Z^3 + 8 a_1 a_4 Z^3 + 9 {a_3}^2 Z^4+ 16 a_2 a_4 Z^4 + \, ...)}$
> 
> $+ .5 \sigma^2 \Delta t \, Z \, [a_1 \, + 2 \,a_2 \, Z +3 \, a_3 \, Z^2 +4 \,  a_4 \, Z^3 +\, ...] $
> 
> $+  .5 \sigma^2 \Delta t \,  [2 \,a_2 \, +6 \, a_3 \, Z +12 \,  a_4 \, Z^2 +\, ...]$
> 
> 
> 
> In the above ${(\frac{\partial X}{\partial Z})}^2={({a_1}^2+ 4 a_1 a_2 Z+ 4 {a_2}^2 Z^2+ 6 a_1 a_3 Z^2 + 12 a2 a_3 Z^3 + 8 a_1 a_4 Z^3 + 9 {a_3}^2 Z^4+ 16 a_2 a_4 Z^4 + \, ...)}$
> 
> This last few terms of the above series would depend on our order of expansion. Rest of the series substitutions are obvious and are just copied from their description at the start.
> 
> Now we know the coefficients a's in the expansion of X(t) and b's in the expansion of drift and we want to determine the coefficients of c's in the expansion of X(t+1). In order to that first we compare the constant terms(with zero power of Z) on both sides of the equation. Then we compare the first power of Z in both sides of the equation and then second power of Z and then so on towards comparing higher powers of Z.
> 
> Comparing the constant terms, we get
> 
> $c_0  \, {a_1}^2 =a_0  \, {a_1}^2 + b_0  \, {a_1}^2+  .5 \sigma^2 \Delta t \,  2 \,a_2$
> 
> from where we get the solution to constant in the series $c_0$ as
> 
> $c_0  =a_0  \, + b_0  \,+   \sigma^2 \Delta t  \, \frac{a_2}{{a_1}^2}$
> 
> 
> 
> In order to find $c_1$, we compare the coefficients of Z on both sides of the main series equation to find 
> 
> 
> 
> $[ \, 4 \, c_0 \, a_1 a_2 Z+ c_1 \,{a_1}^2 \, Z ] =[4 a_0  \, a_1 a_2 Z+ {a_1}^3\, Z ] + [\,4 b_0 \,a_1 a_2 Z+ b_1 \,{a_1}^2\, Z ]$
> 
> $+ .5 \sigma^2 \Delta t \, Z \, a_1 \, +  3 \sigma^2 \Delta t  \, a_3 \, Z $
> 
> 
> 
> Solving for $c_1$, we get
> 
> 
> 
> $ c_1=-[\, 4 \, c_0 \ a_2/a_1 ] + [4 a_0   a_2/a_1 + {a_1}\,] + [\,4 b_0  a_2/a_1 + b_1 ]$
> 
> $+ .5 \sigma^2 \Delta t \, /a_1 \, +  3 \sigma^2 \Delta t  \, a_3/{a_1}^2 \, $
> 
> or
> 
> $c_1=a_1+b_1- \, 4 \, c_0 \ a_2/a_1 + 4 a_0   a_2/a_1 + \,4 b_0  a_2/a_1  $
> 
> $+ .5 \sigma^2 \Delta t \, /a_1 \, +  3 \sigma^2 \Delta t  \, a_3/{a_1}^2 \, $
> 
> 
> 
> In order to find $c_2$, we have to compare the coefficients of $Z^2$
> 
> 
> 
> $[4 c_0  \, {a_2}^2 Z^2+4 c_1 \,  a_1 a_2 Z^2+{a_1}^2 c_2 \, Z^2 ] \,=[4 a_0  \, {a_2}^2 Z^2+4 {a_1}^2 a_2 Z^2+{a_1}^2 a_2 \, Z^2 ] \,$+[4 b_0  \, {a_2}^2 Z^2+4 b_1 \,  a_1 a_2 Z^2+{a_1}^2 b_2 \, Z^2 ] \,$
> 
> $+ .5 \sigma^2 \Delta t \, Z \, [2 \, a_2 \, Z^2 ] +  .5 \sigma^2 \Delta t \,  [12 \,  a_4 \, Z^2 ]$
> 
> solving for $c_2$, we get
> 
> $ c_2 \,=- [4 c_0  \, {a_2}^2/{a_1}^2 +4 c_1 \,  a_2/{a_1} ]+[4 a_0  \, {a_2}^2/{a_1}^2 +4  a_2 + a_2  ] \,+[4 b_0  \, {a_2}^2/{a_1}^2 +4 b_1 \,  a_2/{a_1} +b_2 ] \,$
> 
> $+ \sigma^2 \Delta t \, a_2 /{a_1}^2 +  6 \sigma^2 \Delta t \,  a_4 /{a_1}^2$
> 
> which gives us the solution for $c_2$ as
> 
> $ c_2 \,= a_2 +b_2- [4 c_0  \, {a_2}^2/{a_1}^2 +4 c_1 \,  a_2/{a_1} ]+[4 a_0  \, {a_2}^2/{a_1}^2 +4  a_2 ] \,+[4 b_0  \, {a_2}^2/{a_1}^2 +4 b_1 \,  a_2/{a_1} ] \,$
> 
> $+ \sigma^2 \Delta t  \,  a_2 /{a_1}^2 +  6 \sigma^2 \Delta t \,    a_4/{a_1}^2$
> 
> 
> 
> Please note in the recursions for c's we only need indices that have already been found. All a's and b's are supposed to be known from previous time step.
> 
> Though the series is interesting, I must warn the friends that in order to get accuracy out to several years, they might have to get 20 or 30 or even more terms in the expansion which can easily become very tedious.
> 
> My game plan is to increase order of the solution using "method of iterated integrals-like" solution and solve the equations that are at least second order accurate in time. 
> 
> Later we can see if we can get a reasonably fast algorithm in two dimensions.
> 

Sorry, I missed a term in the recursion of $c_2$. The correct solution for $c_2$ should be



In order to find $c_2$, we have to compare the coefficients of $Z^2$





$[4 c_0  \, {a_2}^2 Z^2+ 6 c_0 \,a_1 a_3 Z^2+4 c_1 \,  a_1 a_2 Z^2+{a_1}^2 c_2 \, Z^2 ] \,=[4 a_0  \, {a_2}^2 Z^2+ 6 a_0 \,a_1 a_3 Z^2+4 {a_1}^2 a_2 Z^2+{a_1}^2 a_2 \, Z^2 ] \,$

$+[4 b_0  \, {a_2}^2 Z^2+ 6 b_0 \,a_1 a_3 Z^2+4 b_1 \,  a_1 a_2 Z^2+{a_1}^2 b_2 \, Z^2 ] \,$

$+ .5 \sigma^2 \Delta t \, Z \, [2 \, a_2 \, Z^2 ] +  .5 \sigma^2 \Delta t \,  [12 \,  a_4 \, Z^2 ]$

solving for $c_2$, we get

$ c_2 \,=- [4 c_0  \, {a_2}^2/{a_1}^2 + 6 c_0  a_3/a_1+4 c_1 \,  a_2/{a_1} ]+[4 a_0  \, {a_2}^2/{a_1}^2 + 6 a_0  a_3/a_1+4  a_2 + a_2  ] \,$

$+[4 b_0  \, {a_2}^2/{a_1}^2 + 6 b_0  a_3/a_1+4 b_1 \,  a_2/{a_1} +b_2 ] \,$

$+ \sigma^2 \Delta t \, a_2 /{a_1}^2 +  6 \sigma^2 \Delta t \,  a_4 /{a_1}^2$

which gives us the solution for $c_2$ as

$ c_2 \,= a_2 +b_2- [4 c_0  \, {a_2}^2/{a_1}^2+ 6 c_0  a_3/a_1  +4 c_1 \,  a_2/{a_1} ]+[4 a_0  \, {a_2}^2/{a_1}^2 + 6 a_0  a_3/a_1 +4  a_2 ] \,+[4 b_0  \, {a_2}^2/{a_1}^2 + 6 b_0  a_3/a_1 +4 b_1 \,  a_2/{a_1} ] \,$

$+ \sigma^2 \Delta t  \,  a_2 /{a_1}^2 +  6 \sigma^2 \Delta t \,    a_4/{a_1}^2$
```

---

## Error 22: Unbalanced $: 7

**Snippet:** `Friends, while finding marginal densities for our hermite regression framework, `

**Full content:**

```
Friends, while finding marginal densities for our hermite regression framework, we have tried to fit four moments. That means that valid equation for Z-series random variable underlying density would be 



$X\, = \, a_0 \, + \, a_1 \, Z \, +\, a_2 \, Z^2 \, +\, a_3 \, Z^3 \,$ 



The first derivative of X with respect to Z is given as



$\frac{dX}{dZ}\, =  \, a_1  \, +\, 2\, a_2 \, Z \, +\, 3\, a_3 \, Z^2 \,$ 



In order to have a nicely behaved density, we need  $\frac{dX}{dZ}\,>0 \,$  everywhere. So as Z increases, X also increases. If somewhere   $\frac{dX}{dZ}\,
```

---

## Error 23: Unbalanced $: 1

**Snippet:** `Friends, I have been saying all along that black sheep in American army and Pent`

**Full content:**

```
Friends, I have been saying all along that black sheep in American army and Pentagon are absolutely determined to continue my persecution. I am very sure they had decided to detain me but changed their plans after I raised hue and cry on this forum and I am sure good people really made some effort to deter them from detaining me. 

I have been very quiet about it for past seven to ten days but lot of things have completely changed during this time. First of all, there is a renewed attempt to drug bottled water in the city. Till December last year, both nestle water, and dasani (coka-cola water) were very good and I used to think that times when water was completely drugged at manufacturing source were over. But both dasani and nestle water in Dec 2022 became very bad and they were drugged at manufacturing source by the respective companies. At that time, I lived by buying water from inner part of the cities with older manufacturing dates as I had previously told friends in a post. Dasani water turned good again in March 2023 and I started freely using it again. Nestle water remained drugged with mind control chemicals even after that but I did not care and simply used dasani water.

Here I will digress to tell friends that some distributors buy very large quantities of bottled water from coca-cola and Nestle at very deep discounts and later slowly offload the water to the retailers in the market. 

Since last ten days, I was very surprised to find dasani water(with manufacturing dates that were very good earlier) had turned bad even in remote parts of the city or small street markets where I would earlier go and get good water. I really believe "rishwat-khor" crooks in  Pakistan army tracked the distributors who would supply water to retailers in various areas and asked them to drug the water they had bought from coca-cola and then distribute it in the entire target areas. Though I have still been able to get good water during past few days, the level of difficulty required to get good water has exponentially increased. 

I am very sure that crooks of Pakistan army will follow by drugging underground water in  they city within a few days.

They have also been using mind control gases in my room recently despite that I mentioned it several times. My sleep is definitely better as compared to worst but I still mostly do not get a good quality sleep. And they continue to target lasers on several parts of my body including my head.

Another serious problem with is that all of the coffee and tea in the city is drugged with mind control chemicals. As friends know that I am on antipsychotics and it is very difficult for me to stimulate my mind to think deeper and creatively about my research. It had been impossible to get good coffee in most large cities of Pakistan where I have lived but I was still able to get good tea with increasing difficulty. About a year ago all large tea companies(there are four or five of them) were selling tea with mind control drugs. But there is still a reasonably large market of independent distributors who just pack the tea in paper and plastic and it can be found at some cheap retailers. Some retailers buy, for example, a large sack of tea from the distributor and continue to sell 500 grams or so to their customers. But recently all of such tea has been drugged by Pakistan army or they have approached distributors to drug their entire cache of tea. In past one month, I have tried tea to buy dozens of time but every time, it was drugged with mind control chemicals. Last time when I got tea by chance was when I was driving my motorcycle on the outskirts of the city in a poor neighborhood and there was "tea"  especially written on a small store. When I asked the shopkeeper in detail about the tea, I came to know that he had tea in a sack from last year and he had not been able to completely sell it. I told him that this is precisely the tea I wanted and bought tea from there. I have not been using the tea for past ten days now since I have only a few servings left from that tea and I might need to use it at some difficult time. I really believe that I remained relatively dull in past ten days despite that effect of antipsychotic injection had decreased since I could not have tea several times a days as I previously used to do.

I really miss good coffee like anything but I cannot even have good tea now.

There is another thing I would like to tell friends. In the autumn of last year I had told friends that I used to get very limited money regularly from my parents and it was not even enough for food after food prices increased. Please let me digress and tell friends that when I resigned in 2010 to go to UK, even though I was on very high antipsychotics, I was making a decent money and my yearly income in last year was more than $ 120,000. My father had borrowed Rs: 5,500,000 from me roughly equivalent of  \$50,000 at that time (and would be equivalent of Rs: 12,500,000 today) . I was told that he would return the money in a few years. Later he refused to give me any money. I was just given enough money barely sufficient for my expenses. I continued to ask my father for money and there were times he would say he would give me some money later while there were other times when he would totally refuse. Later my father would say that I was not earning any money and I would say that if he could return my money, I can start something for income. So my father gave me ten lac rupees  equivalent of \$4,000 in OCT/NOV last year and only then I was able to restart my research. It is only because of this money that I have been able to survive and as able to do relatively good research in past few months. I only spend money on food. I do not eat expensive food but still try to get some good food when I can. And yes, I spent quite some reasonable money \$700 on the last computer I bought that was damaged by mind control crooks in my absence when I was away from home.

I would still have to be able to make some money in a few months but my first priority was good research and I hope that other normal things would slowly follow.
```

---

## Error 24: Unbalanced $: 1

**Snippet:** `Friends, I am posting the matlab programs. These are still tentative and hopeful`

**Full content:**

```
Friends, I am posting the matlab programs. These are still tentative and hopefully I will come up with a final version of the programs in another 3-4 days and then we will move forward to calculations of asset density in future conditional on asset value and stochastic volatility value at some point in monte carlo all in a parametric form. 

Before I post the program, I want to remind the friends that wherever they see these variables in the program, please as you change parameters of the SDE, change these variables to conservative values. As in below, the maximum domain for asset is defined as seven and maximum domain for stocahstic volatility is defined as 1.1, these are conservative values and whenever you change SDE parameters, change these values appropriately. Failure to change these values may deteriorate the quality of solution. In the present program, these values are

MaxCutOffX=7;

MaxCutOffV=1.1; 

Unnecessarily large values of these cutoffs will deteriorate program solution quality.



Here are all the matlab functions.


```
function [] = SVMonteCarloAndAssetConditionalDensity()

X0=1.0;
alpha1=0;
alpha2=1;
kappaX=0;
thetaX=1;
a=kappaX*thetaX;
b=-kappaX;

rho=0;
sigma1=1;
gammaV=.5;
gammaX=.85;
%%%%%%%%`%%%%%
V0=.35;
thetaV=.05;
kappaV=1.50;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.65;
sigma0=.750;
%%%%%%%%%%%%

dt=.03125/2;
Tt=64*2;

T=Tt*dt;


%%%%%%%%%%%%%%%%%%%%%%%%5

%rng(29079137, 'twister')
rng(15898837, 'twister')
paths=100000;
V(1:paths)=V0;  %Original process monte carlo.
X(1:paths)=X0;
Random1(1:paths)=0;
Random2(1:paths)=0;

for tt=1:Tt
Random1=randn(size(Random1));
Random2=randn(size(Random2));


X(1:paths)=X(1:paths)+ ...
    (a* X(1:paths).^alpha1 + b* X(1:paths).^alpha2)* dt + ...
    sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.* X(1:paths).^gammaX .*Random1(1:paths) * sqrt(dt) + ...
    rho* sigma1* V(1:paths).^gammaV .*X(1:paths).^gammaX .*Random2(1:paths)*sqrt(dt) + ...
    (a*alpha1* X(1:paths).^(alpha1-1)+b*alpha2* X(1:paths).^(alpha2-1)).* ...
    (((a* X(1:paths).^alpha1 + b* X(1:paths).^alpha2)* dt^2/2)+ ...
    (sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.* X(1:paths).^gammaX .*Random1(1:paths) *(1-1/sqrt(3)).*dt^1.5+ ...
    rho* sigma1* V(1:paths).^gammaV .*X(1:paths).^gammaX .*Random2(1:paths)*(1-1/sqrt(3)).*dt^1.5))+ ...
    .5*(a*alpha1*(alpha1-1)* X(1:paths).^(alpha1-2)+b*alpha2*(alpha2-1).* X(1:paths).^(alpha2-2)).* ...
    ( sigma1^2* V(1:paths).^(2*gammaV).* X(1:paths).^(2*gammaX)) *dt^2/2 + ...
    sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.*gammaX.* X(1:paths).^(gammaX-1).* ...
    ((a* X(1:paths).^alpha1 + b* X(1:paths).^alpha2).*Random1(1:paths) * 1/sqrt(3).* dt^1.5 + ...
    sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.* X(1:paths).^gammaX .*(Random1(1:paths).^2-1) * dt/2 + ...
    rho* sigma1* V(1:paths).^gammaV .*X(1:paths).^gammaX .*Random1(1:paths).*Random2(1:paths)*dt/2)+ ...
    .5*sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.*gammaX.*(gammaX-1).* X(1:paths).^(gammaX-2).* ...
    (sigma1^2* V(1:paths).^(2*gammaV).* X(1:paths).^(2*gammaX) .*Random1(1:paths).*1/sqrt(3).*dt^1.5)+ ...
    sqrt(1-rho^2)* sigma1*gammaV.* V(1:paths).^(gammaV-1).* X(1:paths).^(gammaX).* ...
    ((mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2).*Random1(1:paths) * 1/sqrt(3).* dt^1.5 + ...
    sigma0*V(1:paths).^gamma.*Random1(1:paths).*Random2(1:paths)*dt/2)+ ...
    .5*sqrt(1-rho^2)* sigma1*gammaV.*(gammaV-1).* V(1:paths).^(gammaV-2).* X(1:paths).^(gammaX).* ...
    (sigma0^2*V(1:paths).^(2*gamma).*Random1(1:paths)*1/sqrt(3)*dt^1.5)+ ...
    sqrt(1-rho^2)* sigma1*gammaV.* V(1:paths).^(gammaV-1).*gammaX.* X(1:paths).^(gammaX-1).* ...
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX .*sigma0.*V(1:paths).^gamma.*Random1(1:paths)*1/sqrt(3)*dt^1.5+ ...
    rho* sigma1* V(1:paths).^gammaV.*gammaX.* X(1:paths).^(gammaX-1).* ...
    ((a* X(1:paths).^alpha1 + b* X(1:paths).^alpha2).*Random2(1:paths) * 1/sqrt(3).* dt^1.5 + ...
    sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.* X(1:paths).^gammaX .*Random1(1:paths).*Random2(1:paths) * dt/2 + ...
    rho* sigma1* V(1:paths).^gammaV .*X(1:paths).^gammaX .*(Random2(1:paths).^2-1)*dt/2)+ ...
    .5*rho* sigma1* V(1:paths).^gammaV.*gammaX.*(gammaX-1).* X(1:paths).^(gammaX-2).* ...
    (sigma1^2* V(1:paths).^(2*gammaV).* X(1:paths).^(2*gammaX) .*Random2(1:paths).*1/sqrt(3).*dt^1.5)+ ...
    rho* sigma1*gammaV.* V(1:paths).^(gammaV-1).* X(1:paths).^(gammaX).* ...
    ((mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2).*Random2(1:paths) * 1/sqrt(3).* dt^1.5 + ...
    sigma0*V(1:paths).^gamma.*(Random2(1:paths).^2-1)*dt/2)+ ...
    .5*rho* sigma1*gammaV.*(gammaV-1).* V(1:paths).^(gammaV-2).* X(1:paths).^(gammaX).* ...
    sigma0^2.*V(1:paths).^(2*gamma).*Random2(1:paths) * 1/sqrt(3).* dt^1.5+ ...
    rho* sigma1*gammaV.* V(1:paths).^(gammaV-1).*gammaX.* X(1:paths).^(gammaX-1).* ...
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX .*sigma0.*V(1:paths).^gamma.*Random2(1:paths)*1/sqrt(3)*dt^1.5;
    

    V(1:paths)=V(1:paths)+ ...
        (mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2)*dt + ...
        sigma0*V(1:paths).^gamma .*Random2(1:paths)*sqrt(dt) + ...
        (mu1.*beta1*V(1:paths).^(beta1-1) + mu2.*beta2.*V(1:paths).^(beta2-1)).* ...
        ((mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2)*dt^2/2 + ...
        sigma0*V(1:paths).^gamma .*Random2(1:paths)*(1-1/sqrt(3))*dt^1.5) + ...
        .5*(mu1.*beta1.*(beta1-1).*V(1:paths).^(beta1-2) + mu2.*beta2.*(beta2-1).*V(1:paths).^(beta2-2)).* ...    
        sigma0^2.*V(1:paths).^(2*gamma).*dt^2/2 + ...
        sigma0*gamma*V(1:paths).^(gamma-1) .* ...
        ((mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2).*Random2(1:paths).*1/sqrt(3)*dt^1.5 + ...
        sigma0.*V(1:paths).^gamma .*(Random2(1:paths).^2-1)*dt/2) + ...
        .5*sigma0*gamma*(gamma-1).*V(1:paths).^(gamma-2) .* ...
        sigma0^2.*V(1:paths).^(2*gamma) .*Random2(1:paths).*1/sqrt(3)*dt^1.5;


end


X(X<0)=0;
V(V<0)=0;
X=real(X);
V=real(V);

% tic
% X_s=sort(X);
% toc
% str=input("elapsed time is above");


SVolMeanAnalytic=thetaV+exp(-kappaV*T)*(V0-thetaV)
SVolMean=sum(V(1:paths))/paths
AssetMeanAnalytic=thetaX+exp(-kappaX*T)*(X0-thetaX)
AssetMean=sum(X(1:paths))/paths


NoOfBinsV=50;
MaxCutOffV=1.1;

[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] = FindConditionalZSeriesXAndZyFromSimulation_nonUGridLS(X,V,paths,NoOfBinsV,MaxCutOffV,gamma);
%The function above finds numerically calculated conditional Z-series coefficietns associated with each volatility grid cell.
%aa0 is zeroth coefficient/median array while aa is a matrix of (5 X NoOfBins+1) coeffs. 


%The series of functions below take each coefficient array and convert it
%to a Z_series of analytic coeffs dependent on Zv. I will explain this
%further in a separate post on wilmott.
[Coeff(1,1),Coeff(1,2:6)] = FindZSeriesCoeffsByInnerProduct(aa0,Zv,VProbMass,IndexMaxV);
[Coeff(2,1),Coeff(2,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(1,:),Zv,VProbMass,IndexMaxV);
[Coeff(3,1),Coeff(3,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(2,:),Zv,VProbMass,IndexMaxV);
[Coeff(4,1),Coeff(4,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(3,:),Zv,VProbMass,IndexMaxV);
[Coeff(5,1),Coeff(5,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(4,:),Zv,VProbMass,IndexMaxV);
[Coeff(6,1),Coeff(6,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(5,:),Zv,VProbMass,IndexMaxV);






for indexV=1:IndexMaxV

    clf;
    PlotZSeriesDensity(aa0(indexV),aa(:,indexV),'g');
    hold on
    %str=input("Look at X conditional density graph");
    %Below conditional coefficients are calculated from coefficients of
    %coefficients dependent on Zv. Then a graphical comparison is made
    %between conditional density of asset from analytic coefficients and 
    %conditional asset density from individually numerically  calculated
    %coefficients of Z-series
    
    
    b0=Coeff(1,1)+Coeff(1,2).*Zv(indexV)+Coeff(1,3).*Zv(indexV).^2+Coeff(1,4).*Zv(indexV).^3+Coeff(1,5).*Zv(indexV).^4+Coeff(1,6).*Zv(indexV).^5;
    
    for mm=2:6
        b(mm-1)=Coeff(mm,1)+Coeff(mm,2).*Zv(indexV)+Coeff(mm,3).*Zv(indexV).^2+Coeff(mm,4).*Zv(indexV).^3+Coeff(mm,5).*Zv(indexV).^4+Coeff(mm,6).*Zv(indexV).^5;
    end
    PlotZSeriesDensity(b0,b,'r');
    title(sprintf('Conditional V=%.3f,Zv=%.3f,x0 = %.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f', Vm(indexV),Zv(indexV), X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));
    legend({'Conditional Asset density From numerical Z-series','Conditional Asset density From new analytic Coeffs Z-series'},'Location','northeast')
    xlabel('Asset'), ylabel('Conditional Asset Density')
    display(fprintf('conditional value of stochastic volatility Grid cell for this graph: V=%.3f,Zv=%.3f,SV grid cell number = %.1f, Total SV Grid Cells=%.1f',Vm(indexV),Zv(indexV),indexV, IndexMaxV));
    str=input("Lok at comparison of numerically calculated conditional asset density and analytic coeffs conditional asset density plots")
    hold off
end


%Please note that for drawing bivariate density of asset and stochastic volatility, grid parameters have changed from brom before in below.


NoOfBinsV=150;
NoOfBinsX=150;
MaxCutOffX=7;
MaxCutOffV=1.1;

%[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv]= Find2DDensityAndCDFFromSimulation_Infiniti(X,V,paths,NoOfBinsX,NoOfBinsV);
[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv,BinSizeX,BinSizeV]= Find2DDensityAndCDFFromSimulation_Infiniti04(X,V,paths,NoOfBinsX,NoOfBinsV,MaxCutOffX,MaxCutOffV);
%[XYProbDensity2D,XYProbMass2D,XProbMass,YProbMass,IndexMaxX,IndexMaxY,Xn,Ym,Zx,Zy,BinSizeX,BinSizeY]
%Please look at matlab file of above function for etailed explanation of
%all its input and output parameters.



surf(Xn,Vm,transpose(XYProbDensity2D));

xlabel('Asset'), ylabel('Stochastic Volatility'), zlabel('Probability Density 2D')
title('Graph of 2D Density of Asset and SV from Parzen Density')









aH0=0;
aH(1:7)=0;
for nn=1:IndexMaxV
aH0  =  aH0+Vm(nn).*VProbMass(nn);    
aH(1)=aH(1)+Vm(nn).*Zv(nn).*VProbMass(nn);
aH(2)=aH(2)+.5*Vm(nn).*(Zv(nn).^2-1).*VProbMass(nn);
aH(3)=aH(3)+1/6*Vm(nn).*(Zv(nn).^3-3*Zv(nn)).*VProbMass(nn);
aH(4)=aH(4)+1/24*Vm(nn).*(Zv(nn).^4-6*Zv(nn).^2+3).*VProbMass(nn);
aH(5)=aH(5)+1/120*Vm(nn).*(Zv(nn).^5-10*Zv(nn).^3+15*Zv(nn)).*VProbMass(nn);
end

[a0,a] = ConvertHCoeffsToZCoeffs(aH0,aH,5);


[pXY2D] = Calculate2VariablesOn2DGridFromAnalyticZSeries(Xn,Vm,NoOfBinsX,NoOfBinsV,Coeff,a0,a);
%[pXY2D] = Calculate2VariablesOn2DGridFromAnalyticZSeries(XX,YY,NoOfBinsX,NoOfBinsY,Coeff,a0,a)


surf(Xn,Vm,transpose(XYProbDensity2D))
title(sprintf('Numerical Density : x0 = %.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f', X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f', kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and Volatility')

str=input("Look at numerical bivariate density of Asset and Stochastic Volatility")
surf(Xn,Vm,transpose(pXY2D))
title(sprintf('Analytic Density : x0 = %.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f', X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f', kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at Analytic density of Asset and Stochastic volatility")
surf(Xn,Vm,transpose(pXY2D-XYProbDensity2D))
title(sprintf('Difference of Analytic and Numerical Density  : x0 = %.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f', X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f', kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at difference of numerical and analytic densities of Asset and stochastic volatility")




end


```

.

.

.

.

```
function [a0,a,WProbMass,IndexMaxW,Ym,Zy] = FindConditionalZSeriesXAndZyFromSimulation_nonUGridLS(X,Y,Paths,NoOfBinsW,MaxCutOffY,gamma)
                                                                                                                                                            
Y(Y>MaxCutOffY)=MaxCutOffY;

W=Y.^(1-gamma);

hW=maxk(W,10);
Wmax2=min(hW);
lW=mink(W,10);
Wmin2=max(lW);

BinSizeW=(Wmax2-Wmin2)/NoOfBinsW;
IndexMaxW=floor((Wmax2-Wmin2)/BinSizeW+.5)+1;
Wm(1:IndexMaxW)=Wmin2+(0:(IndexMaxW-1))*BinSizeW;

Ym(1:IndexMaxW)=(Wm(1:IndexMaxW)).^(1/(1-gamma));


WProbMass(1:IndexMaxW)=0;
pv(1:IndexMaxW)=0;

for p=1:Paths

indexW=real(floor(real(W(p)-Wmin2)/BinSizeW+.5)+1);

if(real(indexW)IndexMaxW)
indexW=IndexMaxW;
end

WProbMass(indexW)=WProbMass(indexW)+1/Paths;

pv(indexW)=pv(indexW)+1;

Xv(pv(indexW),indexW)=X(p);

end
Mean(1:IndexMaxW)=0;
for indexW=1:IndexMaxW
   Mean(indexW)=sum(Xv(:,indexW))./pv(indexW);
   %Mean(indexW)
   Xv(:,indexW)=Xv(:,indexW)./Mean(indexW);

 
   Xv0=0;
   Xv0(1:pv(indexW))=Xv(1:pv(indexW),indexW);
    [a0(indexW),a(:,indexW)] = CalculateZSeriesDensityByIdealMeasureMean05(Xv0);
    
    %d0=a0(indexW)
    %d=a(:,indexW)
    
    
end
    
%a0
%a
%str=input("Look at coefficients matrix");


YCDF(1:IndexMaxW)=0;
Zy(1:IndexMaxW)=0;
YCDF(1)=WProbMass(1)*.5;
Zy(1)=norminv(YCDF(1));
for nn=2:IndexMaxW
    YCDF(nn)=YCDF(nn-1)+WProbMass(nn-1)*.5+WProbMass(nn)*.5;
    Zy(nn)=norminv(YCDF(nn));
    if (Zy(nn)5)
            Zy(nn)=5;
    end
end


end
```

.

.

.

.

```
function [a0,a] = CalculateZSeriesDensityByIdealMeasureMean05(data)


Ndata=length(data);
Sigma=1.0;
[ZI] = StandardNormalIdealDesity02(Ndata,Sigma);

%The function above produces standard normal density with Ndata grid cells
%and each of the cell having probability mass 1/Ndata and ZI(1:Ndata) are 
%centres of each of the Ndata grid cells.


p(1:Ndata)=1/Ndata;
[alpha, beta, gamma,eata,zeta] = TrProbsMatchMoments0O4A(Ndata,ZI,p);
%The above function fixes the probability density so that first four moments are
%matched


if((abs(beta)>1)||(abs(gamma)>1)||(abs(eata)>1)||(abs(zeta)>1)) 
pnew(1:Ndata)=p(1:Ndata);
%if multiplier parameters are too large do not change the density at all since parameters have probably become unstable. 
str=input("Parameters became unstable--I am not altering the density--press Enter to continue")
else
%if multiplier parameters are small, alter the probability density.
pnew(1:Ndata)=p(1:Ndata).*(alpha+beta*ZI(1:Ndata)+gamma*(ZI(1:Ndata).^2-1)+eata*(ZI(1:Ndata).^3-3.*ZI(1:Ndata))+ ...
    zeta*(ZI(1:Ndata).^4-6.*ZI(1:Ndata).^2+3));
end

%Transfer the change from probability density to ZI so that expectation of
%each grid cell stays the same. Higher moments still might not be matched
%but this is an improvement. I need to do further research to make sure
%that higher moments are properly matched.Expectation stays the same as ZI 
%is changed so that ZInew(1:Ndata)*pnew(I:Ndata)=ZI(I:Ndata).*p(1:NData). 
%Using equation below change in probability density is transferred to 
%change in Z.  
ZI(1:Ndata)=ZI(1:Ndata)./pnew(1:Ndata).*p(1:Ndata);

%ZI=(ZI*.75+ZI0*.25);

Sdata=sort(data);
Y(1:Ndata,1)=Sdata(1:Ndata);
Mean=sum(Y(1:Ndata,1))/Ndata;
Y(1:Ndata,1)=Y(1:Ndata,1)-Mean; %subtract the mean. Variance standardization might not have an effect.
if (rem(Ndata,2)==0)
Median=sum(Y(Ndata/2,1)+Y(Ndata/2+1,1))/2;
else
Median=Y(floor(Ndata/2+1),1);
end

Ymu(1:Ndata,1)=Y(1:Ndata,1)-Median;%subtract the median
Zu=0;   %Since median is subtracted from mean-standardized data, we have to 
%subtract the Z=0 from ZI i.e subtract nothing.
X(1:Ndata,1:6)=0;
%Below I am regressing powers of Z as in Z-series but hermites could
%equally be regressed and I expect that results would probably be extremely
%close.
for nn=1:Ndata
    X(nn,1)=1;
    X(nn,2)=(ZI(nn)-Zu);
    X(nn,3)=(ZI(nn)-Zu).^2;
    X(nn,4)=(ZI(nn)-Zu).^3;
    X(nn,5)=(ZI(nn)-Zu).^4;
    X(nn,6)=(ZI(nn)-Zu).^5;
    %X(nn,7)=(ZI(nn)-Zu).^6;
    %X(nn,8)=(ZI(nn)-Zu).^7;
end

%coeff=inv(X'*X)*(X'*Ymu);
coeff=(X'*X)$X'*Ymu);
c0=coeff(1,1);
c(1:5)=coeff(2:6,1);

a0=c0;
a=c;
a0=a0+Median+Mean;
end
```

.

.

.

.

```
function [ZZ] = StandardNormalIdealDesity02(Ndata,Sigma)
%Ndata is number of data points in sample, for which we want to find the
%coefficients of the Z-series.
%Sigma=1+.06;
%Sigma=1;
if (rem(Ndata,2)==0)
    NnMid=Ndata/2;
    ZZ(NnMid+1)=norminv(.5+1/Ndata*.5,0,Sigma);
    ZZ(NnMid)=norminv(.5-1/Ndata*.5,0,Sigma);
    for nn=2:NnMid-1
        ZZ(nn+NnMid)=norminv(.5+(nn-.5)*1/Ndata,0,Sigma);
        ZZ(-nn+1+NnMid)=norminv(.5-(nn-.5)*1/Ndata,0,Sigma);
    end
    %A=normcdf((Ndata-1)/Ndata);
    %ZZ(Ndata)=exp(-5*A^2)/(1/Ndata);
    A=norminv((Ndata-1)/Ndata);
    ZZ(Ndata)=A +0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
    ZZ(1)=-A-0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
end

if (rem(Ndata,2)==1)
    NnMid=(Ndata+1)/2;
    ZZ(NnMid)=0;
    for nn=1:NnMid-2
        ZZ(nn+NnMid)=norminv(.5+(nn)*1/Ndata,0,Sigma);
        ZZ(-nn+NnMid)=norminv(.5-(nn)*1/Ndata,0,Sigma);
    end
   A=norminv((Ndata-1)/Ndata);
    ZZ(Ndata)=A +0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
    ZZ(1)=-A-0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
end

%ZZ
%A
%plot(ZZ)
%str=input("Look at density plot standard")

end


```

.

.

.

.

```
function [alpha, beta, gamma,eata,zeta] = TrProbsMatchMoments0O4A(Nn2,Zt,pt)


    a1=sum(pt(1:Nn2));
    b1=sum(Zt(1:Nn2).*pt(1:Nn2));
    c1=sum((Zt(1:Nn2).^2-1).*pt(1:Nn2));
    d1=sum((Zt(1:Nn2).^3-3.*Zt(1:Nn2)).*pt(1:Nn2));
    g1=sum((Zt(1:Nn2).^4-6.*Zt(1:Nn2).^2+3).*pt(1:Nn2));
    a2=sum(Zt(1:Nn2).*pt(1:Nn2));
    b2=sum(Zt(1:Nn2).^2.*pt(1:Nn2));
    c2=sum(Zt(1:Nn2).*(Zt(1:Nn2).^2-1).*pt(1:Nn2));
    d2=sum(Zt(1:Nn2).*(Zt(1:Nn2).^3-3.*Zt(1:Nn2)).*pt(1:Nn2));
    g2=sum(Zt(1:Nn2).*(Zt(1:Nn2).^4-6.*Zt(1:Nn2).^2+3).*pt(1:Nn2));
    a3=sum(Zt(1:Nn2).^2.*pt(1:Nn2));
    b3=sum(Zt(1:Nn2).^3.*pt(1:Nn2));
    c3=sum(Zt(1:Nn2).^2.*(Zt(1:Nn2).^2-1).*pt(1:Nn2));
    d3=sum(Zt(1:Nn2).^2.*(Zt(1:Nn2).^3-3*Zt(1:Nn2)).*pt(1:Nn2));
    g3=sum(Zt(1:Nn2).^2.*(Zt(1:Nn2).^4-6.*Zt(1:Nn2).^2+3).*pt(1:Nn2));
    a4=sum(Zt(1:Nn2).^3.*pt(1:Nn2));
    b4=sum(Zt(1:Nn2).^3.*Zt(1:Nn2).*pt(1:Nn2));
    c4=sum(Zt(1:Nn2).^3.*(Zt(1:Nn2).^2-1).*pt(1:Nn2));
    d4=sum( Zt(1:Nn2).^3.*(Zt(1:Nn2).^3-3.*Zt(1:Nn2)).*pt(1:Nn2));
    g4=sum(Zt(1:Nn2).^3.*(Zt(1:Nn2).^4-6.*Zt(1:Nn2).^2+3).*pt(1:Nn2));
    
    a5=sum(Zt(1:Nn2).^4.*pt(1:Nn2));
    b5=sum(Zt(1:Nn2).^4.*Zt(1:Nn2).*pt(1:Nn2));
    c5=sum(Zt(1:Nn2).^4.*(Zt(1:Nn2).^2-1).*pt(1:Nn2));
    d5=sum( Zt(1:Nn2).^4.*(Zt(1:Nn2).^3-3.*Zt(1:Nn2)).*pt(1:Nn2));
    g5=sum(Zt(1:Nn2).^4.*(Zt(1:Nn2).^4-6.*Zt(1:Nn2).^2+3).*pt(1:Nn2));

    
    A(1,1)=a1;
    A(1,2)=b1;
    A(1,3)=c1;
    A(1,4)=d1;
    A(1,5)=g1;
    A(2,1)=a2;
    A(2,2)=b2;
    A(2,3)=c2;
    A(2,4)=d2;
    A(2,5)=g2;
    A(3,1)=a3;
    A(3,2)=b3;
    A(3,3)=c3;
    A(3,4)=d3;
    A(3,5)=g3;
    A(4,1)=a4;
    A(4,2)=b4;
    A(4,3)=c4;
    A(4,4)=d4;
    A(4,5)=g4;
    A(5,1)=a5;
    A(5,2)=b5;
    A(5,3)=c5;
    A(5,4)=d5;
    A(5,5)=g5;

    b(1,1)=1;
    b(2,1)=0;
    b(3,1)=1;
    b(4,1)=0;
    b(5,1)=3;
    
    params = linsolve(A,b);
    
    alpha=params(1,1);
    beta=params(2,1);
    gamma=params(3,1);
    eata=params(4,1);
    zeta=params(5,1);
    
%     
%     
%     Denominator0=   (-(((d2 *g1 - d1* g2)* (b3* g1 - b1* g3) - (b2* g1 -b1* g2)* ...
%               (d3 *g1 - d1* g3))* (c4 *d2 *g1^2 - c2 *d4* g1^2 - c4* d1* g1* g2 + c1* d4* g1* g2 + c2* d1* g1* g4 - ... 
%             c1* d2* g1* g4) - ((d2* g1 - d1* g2)* (c3* g1 - c1* g3) - (c2 *g1 -c1* g2)* (d3* g1 - d1* g3))* ...
%             ((d2* g1 - d1* g2)* (b4* g1 - b1* g4) - (b2* g1 - b1* g2)* (d4* g1 - d1* g4)))* ...
%             ((c4* d2* g1^2 - c2 *d4* g1^2 - c4* d1* g1* g2 + c1* d4* g1* g2 + c2* d1 *g1* g4 - c1* d2* g1 *g4)* ...
%             ((d2* g1 - d1* g2) *(a5* g1 - a1* g5) - (a2* g1 - a1* g2)* (d5* g1 - d1* g5)) - ((d2* g1 - d1* g2)* ...
%             (a4* g1 - a1* g4) - (a2* g1 - a1* g2)* (d4* g1 - d1* g4))* ((d2* g1 - d1* g2)* (c5* g1 - c1* g5) - ...
%             (c2* g1 - c1* g2)* (d5 *g1 - d1* g5))) + (((d2* g1 - d1* g2)* (a3* g1 - a1 *g3) - (a2* g1 - a1* g2)* ...
%             (d3 *g1 - d1* g3))* (c4* d2* g1^2 - c2* d4* g1^2 - c4 *d1* g1* g2 + c1* d4 *g1 *g2 + c2* d1* g1* g4 - ...
%            c1* d2* g1 *g4) - ((d2* g1 - d1* g2)* (c3* g1 - c1* g3) - (c2* g1 - c1 *g2)* (d3* g1 - d1* g3)) * ...
%            ((d2* g1 - d1* g2)* (a4 *g1 - a1* g4) - (a2* g1 - a1* g2)* (d4 *g1 - d1 *g4))) *((c4 *d2 *g1^2 - ...
%            c2 *d4 *g1^2 - c4* d1* g1* g2 + c1* d4* g1* g2 + c2* d1* g1* g4 - c1* d2* g1 *g4) * ...
%            ((d2* g1 - d1* g2) *(b5* g1 - b1* g5) - (b2* g1 - b1 *g2)* (d5* g1 - d1* g5)) - ((d2* g1 - d1* g2)* ...
%            (b4 *g1 - b1 *g4) - (b2* g1 - b1* g2)* (d4* g1 - d1* g4))* ((d2* g1 - d1* g2)* ...
%            (c5* g1 - c1* g5) - (c2* g1 - c1* g2)* (d5* g1 - d1* g5))));
%     
%  
%        Denominator1=(a5* b4* c3* d2 *g1 - a4* b5* c3 *d2* g1 - a5* b3* c4 *d2* g1 + ... 
%     a3* b5* c4* d2* g1 + a4* b3* c5* d2 *g1 - a3* b4* c5* d2* g1 - ... 
%     a5 *b4* c2* d3* g1 + a4* b5* c2* d3* g1 + a5* b2* c4* d3* g1 - ... 
%     a2* b5* c4* d3* g1 - a4* b2* c5* d3* g1 + a2* b4* c5* d3* g1 + ... 
%     a5* b3* c2* d4* g1 - a3* b5* c2* d4* g1 - a5* b2* c3* d4* g1 + ... 
%     a2* b5* c3* d4* g1 + a3* b2* c5* d4* g1 - a2* b3* c5* d4* g1 - ... 
%     a4* b3* c2* d5* g1 + a3* b4* c2* d5* g1 + a4* b2* c3* d5* g1 - ... 
%     a2* b4* c3* d5* g1 - a3* b2* c4* d5* g1 + a2* b3* c4* d5* g1 - ...
%     a5* b4* c3* d1* g2 + a4* b5* c3* d1* g2 + a5* b3* c4* d1* g2 - ... 
%     a3* b5* c4* d1* g2 - a4* b3* c5* d1* g2 + a3* b4* c5* d1* g2 + ... 
%     a5* b4* c1* d3* g2 - a4* b5* c1* d3 *g2 - a5* b1* c4* d3* g2 + ... 
%     a1* b5* c4* d3* g2 + a4* b1* c5* d3* g2 - a1* b4* c5* d3* g2 - ... 
%     a5* b3* c1* d4* g2 + a3* b5* c1* d4* g2 + a5* b1* c3* d4* g2 - ... 
%     a1* b5* c3* d4* g2 - a3* b1* c5* d4* g2 + a1* b3* c5* d4* g2 + ... 
%     a4* b3* c1* d5* g2 - a3* b4* c1* d5* g2 - a4 *b1* c3* d5* g2 + ... 
%     a1* b4* c3* d5* g2 + a3* b1* c4* d5* g2 - a1* b3* c4* d5* g2 + ... 
%     a5* b4* c2* d1* g3 - a4* b5* c2* d1* g3 - a5* b2 *c4 *d1* g3 + ... 
%     a2* b5* c4 *d1* g3 + a4* b2* c5 *d1 *g3 - a2* b4* c5* d1* g3 - ... 
%     a5 *b4* c1* d2* g3 + a4* b5* c1* d2* g3 + a5* b1* c4* d2 *g3 - ...
%     a1* b5* c4* d2* g3 - a4* b1* c5* d2* g3 + a1* b4* c5* d2 *g3 + ...
%     a5* b2* c1* d4* g3 - a2* b5* c1* d4* g3 - a5* b1* c2* d4* g3 + ...
%     a1* b5* c2* d4* g3 + a2* b1* c5* d4* g3 - a1 *b2* c5* d4* g3 - ...
%     a4* b2* c1* d5* g3 + a2* b4* c1* d5* g3 + a4* b1* c2* d5* g3 - ... 
%     a1* b4* c2* d5* g3 - a2* b1* c4* d5* g3 + a1* b2* c4* d5* g3 - ...
%     a5* b3* c2* d1* g4 + a3* b5* c2* d1* g4 + a5* b2* c3* d1* g4 - ... 
%     a2* b5* c3* d1* g4 - a3* b2* c5* d1* g4 + a2* b3* c5* d1* g4 + ...
%     a5* b3* c1* d2* g4 - a3* b5* c1* d2* g4 - a5* b1* c3* d2* g4 + ... 
%     a1* b5* c3* d2* g4 + a3* b1* c5* d2* g4 - a1* b3* c5* d2* g4 - ... 
%     a5* b2* c1* d3* g4 + a2* b5* c1* d3* g4 + a5* b1* c2* d3* g4 - ...
%     a1* b5* c2* d3* g4 - a2* b1* c5* d3* g4 + a1* b2* c5* d3* g4 + ...
%     a3* b2* c1* d5* g4 - a2* b3* c1* d5* g4 - a3* b1* c2* d5* g4 + ... 
%     a1* b3* c2* d5* g4 + a2* b1* c3* d5* g4 - a1* b2* c3* d5* g4 + ...
%     a4* b3* c2* d1* g5 - a3* b4* c2* d1* g5 - a4* b2* c3* d1* g5 + ... 
%     a2* b4* c3* d1* g5 + a3* b2* c4* d1* g5 - a2* b3* c4* d1* g5 - ... 
%     a4* b3* c1* d2* g5 + a3* b4* c1* d2* g5 + a4* b1* c3* d2* g5 - ... 
%     a1* b4* c3* d2* g5 - a3* b1* c4* d2* g5 + a1* b3* c4* d2* g5 + ...
%     a4* b2* c1* d3 *g5 - a2* b4* c1* d3* g5 - a4* b1* c2* d3* g5 + ... 
%     a1* b4* c2* d3* g5 + a2* b1* c4* d3* g5 - a1* b2* c4* d3* g5 - ...
%     a3* b2* c1* d4* g5 + a2* b3* c1* d4* g5 + a3* b1* c2* d4* g5 - ...
%     a1* b3* c2* d4* g5 - a2* b1* c3* d4* g5 + a1* b2* c3* d4* g5);
% 
%     alpha= -(-(((d2 *g1 - d1* g2)* (b3* g1 - b1* g3) - (b2* g1 - b1* g2).* ...
%         (d3* g1 - d1 *g3)) *(c4* d2* g1^2 - c2* d4* g1^2 - c4* d1* g1* g2 + ... 
%             c1* d4* g1* g2 + c2 *d1 *g1 *g4 - c1* d2* g1* g4) - ...
%             ((d2* g1 - d1* g2)* (c3* g1 - c1* g3) - (c2* g1 - c1* g2)* ...
%             (d3* g1 - d1* g3))* ((d2* g1 - d1* g2)* (b4 *g1 - b1* g4) -...
%             (b2* g1 - b1* g2)* (d4* g1 - d1* g4)))* ((c4* d2* g1^2 - c2* d4* g1^2 - ...
%             c4* d1* g1* g2 + c1* d4* g1* g2 + c2* d1* g1* g4 - c1* d2* g1* g4)* ...
%             ((d2* g1 - d1* g2)* (-3 *g1 + g5) - g2* (d5* g1 - d1* g5)) - ((d2* g1 - d1* g2)* g4 - ... 
%            g2 *(d4* g1 - d1* g4))* ((d2* g1 - d1* g2)* (c5* g1 - c1* g5) - (c2* g1 - c1* g2)* ...
%            (d5* g1 - d1* g5))) + (((d2* g1 - d1* g2)* (-g1 + g3) - g2* (d3* g1 - d1* g3))* ...
%            (c4* d2* g1^2 - c2* d4* g1^2 - c4* d1* g1* g2 + c1* d4* g1* g2 + c2* d1* g1* g4 - ... 
%            c1* d2* g1* g4) - ((d2* g1 - d1* g2) *(c3 *g1 - c1* g3) - (c2* g1 - c1* g2)* ...
%            (d3* g1 - d1* g3))* ((d2* g1 - d1* g2)* g4 - g2* (d4* g1 - d1* g4)))* ...
%            ((c4* d2* g1^2 - c2* d4* g1^2 - c4* d1* g1 *g2 + c1* d4* g1* g2 + c2 *d1* g1 *g4 - ... 
%            c1* d2* g1* g4)* ((d2* g1 - d1 *g2)* (b5* g1 - b1* g5) - (b2* g1 - b1* g2)* (d5 *g1 - d1* g5)) - ...
%            ((d2* g1 - d1* g2)* (b4* g1 -b1* g4) - (b2 *g1 - b1* g2)* (d4 *g1 - d1 *g4))* ((d2 *g1 - d1 *g2) * ...
%            (c5* g1 - c1* g5) - (c2* g1 - c1* g2)* (d5* g1 - d1* g5))))/ Denominator0;
%        
%        
%        
%     beta=   -(3 *a4* c3 *d2 *g1 - 3 *a3* c4* d2* g1 + a5* c4* d2* g1 - a4* c5* d2* g1 - ... 
%     3* a4* c2* d3* g1 + 3* a2* c4* d3* g1 + 3* a3* c2* d4* g1 - a5* c2* d4* g1 - ... 
%     3 *a2* c3* d4* g1 + a2* c5* d4* g1 + a4* c2* d5* g1 - a2* c4* d5* g1 - ... 
%     3 *a4* c3* d1* g2 + 3 *a3* c4* d1* g2 - a5* c4 *d1 *g2 + a4* c5* d1* g2 + ... 
%     3 *a4* c1* d3* g2 - 3* a1* c4* d3* g2 + a5* c4* d3* g2 - a4* c5* d3* g2 - ... 
%     3 *a3* c1* d4* g2 + a5* c1* d4* g2 + 3 *a1* c3* d4 *g2 - a5* c3 *d4* g2 - ... 
%     a1* c5* d4* g2 + a3* c5* d4* g2 - a4* c1* d5 *g2 + a4* c3* d5 *g2 +  ...
%     a1 *c4 *d5* g2 - a3* c4* d5* g2 + 3 *a4* c2* d1* g3 - 3* a2* c4* d1* g3 - ... 
%     3 *a4* c1* d2* g3 + 3 *a1* c4* d2* g3 - a5 *c4* d2* g3 + a4* c5* d2* g3 + ... 
%     3* a2* c1* d4* g3 - 3* a1* c2* d4 *g3 + a5* c2* d4* g3 - a2* c5* d4* g3 - ... 
%     a4* c2* d5* g3 + a2* c4* d5 *g3 - 3* a3* c2* d1* g4 + a5* c2* d1* g4 + ... 
%     3 *a2 *c3* d1* g4 - a2* c5 *d1* g4 + 3* a3* c1* d2* g4 - a5* c1* d2* g4 - ... 
%     3* a1* c3* d2* g4 + a5* c3* d2* g4 + a1* c5* d2* g4 - a3* c5* d2* g4 - ... 
%     3* a2* c1* d3* g4 + 3* a1* c2* d3* g4 - a5* c2* d3* g4 + a2* c5 *d3 *g4 +  ...
%     a2* c1* d5* g4 - a1* c2* d5* g4 + a3* c2* d5* g4 - a2* c3 *d5* g4 - ... 
%     a4* c2* d1* g5 + a2* c4* d1* g5 + a4* c1* d2* g5 - a4 *c3* d2* g5 - ... 
%     a1 *c4* d2* g5 + a3* c4* d2* g5 + a4* c2* d3* g5 - a2* c4 *d3 *g5 - ... 
%     a2 *c1* d4* g5 + a1* c2* d4* g5 - a3 *c2* d4* g5 + a2* c3* d4* g5)/ Denominator1;
%     
%        
%    gamma=-(3* a4* b3* d2 *g1 - 3 *a3 *b4 *d2 *g1 + a5* b4* d2* g1 - a4* b5* d2 *g1 - ...
%    3* a4* b2* d3* g1 + 3* a2* b4* d3* g1 + 3* a3* b2* d4* g1 - a5* b2* d4* g1 - ... 
%    3* a2* b3* d4* g1 + a2* b5* d4* g1 + a4* b2* d5* g1 - a2* b4* d5* g1 - ... 
%    3* a4* b3* d1* g2 + 3* a3* b4* d1* g2 - a5 *b4* d1* g2 + a4* b5* d1* g2 + ... 
%    3* a4* b1* d3* g2 - 3 *a1* b4* d3* g2 + a5* b4* d3* g2 - a4* b5* d3* g2 - ... 
%    3 *a3* b1* d4* g2 + a5* b1* d4* g2 + 3* a1* b3* d4* g2 - a5* b3* d4* g2 - ... 
%    a1* b5* d4* g2 + a3* b5* d4* g2 - a4* b1* d5* g2 + a4* b3* d5* g2 + ... 
%    a1* b4* d5* g2 - a3* b4* d5* g2 + 3 *a4* b2* d1* g3 - 3* a2* b4* d1* g3 - ... 
%    3* a4* b1* d2* g3 + 3* a1 *b4 *d2 *g3 - a5* b4* d2* g3 + a4* b5* d2* g3 + ... 
%    3* a2* b1* d4* g3 - 3* a1* b2* d4 *g3 + a5* b2* d4* g3 - a2* b5* d4* g3 - ... 
%    a4* b2* d5* g3 + a2* b4* d5* g3 - 3 *a3* b2* d1 *g4 + a5* b2* d1* g4 + ... 
%    3* a2* b3* d1* g4 - a2* b5* d1* g4 + 3 *a3* b1* d2* g4 - a5* b1* d2* g4 - ... 
%    3* a1* b3* d2* g4 + a5* b3* d2* g4 + a1* b5* d2* g4 - a3* b5* d2* g4 - ... 
%    3* a2* b1* d3* g4 + 3 *a1* b2* d3* g4 - a5 *b2* d3* g4 + a2 *b5* d3* g4 + ... 
%    a2* b1* d5* g4 - a1* b2* d5* g4 + a3* b2* d5* g4 - a2* b3* d5* g4 - ... 
%    a4* b2* d1* g5 + a2* b4* d1* g5 + a4* b1* d2 *g5 - a4* b3* d2* g5 - ... 
%    a1* b4* d2* g5 + a3* b4* d2* g5 + a4* b2* d3* g5 - a2* b4* d3* g5 -  ...
%    a2* b1* d4* g5 + a1* b2* d4* g5 - a3* b2* d4* g5 + a2* b3* d4* g5)/(-Denominator1);
%        
%        
%     
% eata=-(3 *a4* b3 *c2* g1 - 3* a3* b4* c2 *g1 + a5* b4 *c2* g1 - a4* b5* c2* g1 - ... 
%     3* a4* b2* c3* g1 + 3* a2* b4* c3* g1 + 3* a3* b2* c4* g1 - a5* b2* c4 *g1 - ...
%     3* a2* b3* c4* g1 + a2* b5* c4* g1 + a4* b2* c5* g1 - a2* b4* c5* g1 - ... 
%     3* a4* b3* c1* g2 + 3* a3* b4 *c1 *g2 - a5 *b4* c1* g2 + a4 *b5* c1* g2 + ... 
%     3* a4* b1* c3* g2 - 3* a1* b4* c3* g2 + a5* b4* c3* g2 - a4* b5* c3* g2 - ... 
%     3* a3* b1* c4* g2 + a5* b1* c4* g2 + 3 *a1 *b3* c4* g2 - a5* b3* c4* g2 - ... 
%     a1* b5* c4* g2 + a3* b5* c4* g2 - a4* b1* c5* g2 + a4* b3* c5* g2 + ...
%     a1* b4* c5* g2 - a3* b4* c5* g2 + 3 *a4 *b2* c1* g3 - 3 *a2* b4* c1* g3 - ... 
%     3* a4* b1* c2* g3 + 3* a1 *b4 *c2 *g3 - a5* b4 *c2 *g3 + a4* b5 *c2 *g3 + ...
%     3 *a2* b1* c4* g3 - 3* a1* b2* c4* g3 + a5* b2* c4* g3 - a2* b5* c4* g3 - ...
%     a4* b2* c5* g3 + a2* b4* c5* g3 - 3* a3* b2 *c1* g4 + a5* b2* c1* g4 + ... 
%     3* a2* b3* c1* g4 - a2* b5* c1* g4 + 3* a3* b1* c2* g4 - a5* b1* c2* g4 - ... 
%     3* a1* b3* c2* g4 + a5* b3* c2* g4 + a1* b5* c2* g4 - a3* b5* c2* g4 - ... 
%     3* a2 *b1* c3* g4 + 3 *a1* b2* c3* g4 - a5* b2* c3* g4 + a2* b5* c3* g4 + ... 
%     a2 *b1* c5* g4 - a1* b2* c5* g4 + a3* b2* c5* g4 - a2 *b3 *c5* g4 - ... 
%     a4* b2* c1* g5 + a2* b4* c1* g5 + a4* b1* c2* g5 - a4* b3* c2* g5 - ... 
%     a1* b4* c2* g5 + a3* b4* c2* g5 + a4* b2* c3* g5 - a2* b4* c3* g5 - ...
%     a2* b1* c4* g5 + a1* b2* c4* g5 - a3* b2* c4 *g5 + a2* b3* c4* g5)/(Denominator1);
%     
% 
% zeta=-(3* a4* b3* c2* d1 - 3* a3* b4* c2* d1 + a5* b4* c2* d1 - a4* b5* c2* d1 - ... 
%    3* a4* b2* c3* d1 + 3 *a2* b4* c3* d1 + 3 *a3* b2* c4* d1 - a5 *b2* c4* d1 -  ...
%    3* a2* b3* c4* d1 + a2* b5* c4* d1 + a4* b2* c5* d1 - a2* b4* c5* d1 - ... 
%    3* a4* b3* c1* d2 + 3* a3* b4* c1* d2 - a5* b4* c1* d2 + a4* b5* c1* d2 + ... 
%    3 *a4 *b1* c3* d2 - 3* a1* b4* c3* d2 + a5* b4* c3* d2 - a4* b5* c3 *d2 - ... 
%    3 *a3 *b1* c4* d2 + a5* b1* c4* d2 + 3* a1* b3* c4 *d2 - a5* b3* c4 *d2 - ...
%    a1* b5* c4* d2 + a3* b5* c4* d2 - a4* b1* c5* d2 + a4* b3* c5* d2 + ... 
%    a1* b4* c5* d2 - a3* b4* c5* d2 + 3 *a4* b2* c1* d3 - 3* a2* b4* c1* d3 - ... 
%    3* a4* b1* c2* d3 + 3 *a1* b4* c2* d3 - a5 *b4* c2* d3 + a4* b5* c2* d3 + ... 
%    3* a2* b1* c4* d3 - 3* a1* b2* c4* d3 + a5* b2* c4* d3 - a2* b5* c4* d3 - ... 
%    a4* b2* c5* d3 + a2* b4* c5* d3 - 3* a3* b2* c1* d4 + a5 *b2* c1* d4 + ...
%    3* a2* b3* c1* d4 - a2* b5* c1* d4 + 3* a3* b1* c2* d4 - a5* b1* c2* d4 - ... 
%    3 *a1* b3* c2* d4 + a5* b3* c2* d4 + a1 *b5* c2* d4 - a3* b5* c2* d4 - ... 
%    3 *a2* b1* c3* d4 + 3* a1* b2* c3* d4 - a5* b2* c3* d4 + a2* b5 *c3 *d4 + ...
%    a2* b1* c5* d4 - a1* b2* c5* d4 + a3* b2* c5* d4 - a2* b3* c5 *d4 - ... 
%    a4* b2* c1* d5 + a2* b4* c1* d5 + a4* b1* c2* d5 - a4* b3* c2* d5 - ... 
%    a1* b4* c2* d5 + a3 *b4 *c2* d5 + a4 *b2* c3* d5 - a2* b4* c3 *d5 - ... 
%    a2* b1* c4* d5 + a1* b2* c4* d5 - a3* b2* c4* d5 + a2* b3* c4* d5)/(-Denominator1);
%     

end



```

.

.

.

.

```
function [a0,a] = FindZSeriesCoeffsByInnerProduct(Vm,Zv,VProbMass,IndexMaxV)



aH0=0;
aH(1:5)=0;
for nn=1:IndexMaxV
aH0  =  aH0+Vm(nn).*VProbMass(nn);    
aH(1)=aH(1)+Vm(nn).*Zv(nn).*VProbMass(nn);
aH(2)=aH(2)+.5*Vm(nn).*(Zv(nn).^2-1).*VProbMass(nn);
aH(3)=aH(3)+1/6*Vm(nn).*(Zv(nn).^3-3*Zv(nn)).*VProbMass(nn);
aH(4)=aH(4)+1/24*Vm(nn).*(Zv(nn).^4-6*Zv(nn).^2+3).*VProbMass(nn);
aH(5)=aH(5)+1/120*Vm(nn).*(Zv(nn).^5-10*Zv(nn).^3+15*Zv(nn)).*VProbMass(nn);
%aH(6)=aH(6)+1/720*Vm(nn).*(Zv(nn).^6-15*Zv(nn).^4+45*Zv(nn).^2-15).*VProbMass(nn);
%aH(7)=aH(7)+1/720/7*Vm(nn).*(Zv(nn).^7-21*Zv(nn).^5+105*Zv(nn).^3-105*Zv(nn)).*VProbMass(nn);
end


[a0,a] = ConvertHCoeffsToZCoeffs(aH0,aH,5);

end


```

.

.

.

```
function [a0,a] = ConvertHCoeffsToZCoeffs(aH0,aH,SeriesOrder)


if(SeriesOrder==3)
a0=aH0-aH(2);
a(1)=aH(1)-3*aH(3);
a(2)=aH(2);
a(3)=aH(3);
end

if(SeriesOrder==4)
a0=aH0-aH(2)+3*aH(4);
a(1)=aH(1)-3*aH(3);
a(2)=aH(2)-6*aH(4);
a(3)=aH(3);
a(4)=aH(4);
end

if(SeriesOrder==5)
a0=aH0-aH(2)+3*aH(4);
a(1)=aH(1)-3*aH(3)+15*aH(5);
a(2)=aH(2)-6*aH(4);
a(3)=aH(3)-10*aH(5);
a(4)=aH(4);
a(5)=aH(5);
end

if(SeriesOrder==5)
a0=aH0-aH(2)+3*aH(4);
a(1)=aH(1)-3*aH(3)+15*aH(5);
a(2)=aH(2)-6*aH(4);
a(3)=aH(3)-10*aH(5);
a(4)=aH(4);
a(5)=aH(5);
end
% if(SeriesOrder==5)
% a0=aH0-aH(2)-3*aH(4);
% a(1)=aH(1)-3*aH(3)-15*aH(5);
% a(2)=aH(2)-6*aH(4);
% a(3)=aH(3)-10*aH(5);
% a(4)=aH(4);
% a(5)=aH(5);
% end
if(SeriesOrder==6)
a0=aH0-aH(2)+3*aH(4)-15*aH(6);
a(1)=aH(1)-3*aH(3)+15*aH(5);
a(2)=aH(2)-6*aH(4)+45*aH(6);
a(3)=aH(3)-10*aH(5);
a(4)=aH(4)-15*aH(6);
a(5)=aH(5);
a(6)=aH(6);
end

if(SeriesOrder==7)
a0=aH0-aH(2)+3*aH(4)-15*aH(6);
a(1)=aH(1)-3*aH(3)+15*aH(5)-105*aH(7);
a(2)=aH(2)-6*aH(4)+45*aH(6);
a(3)=aH(3)-10*aH(5)+105*aH(7);
a(4)=aH(4)-15*aH(6);
a(5)=aH(5)-21*aH(7);
a(6)=aH(6);
a(7)=aH(7);
end


end


```

.

.

.

.

```
function [] = PlotZSeriesDensity(c0,c,Color)

Index=length(c);

dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=45*4;  % No of normal density subdivisions
NnMid=((1+Nn)/2)*dNn;
Z(1:Nn)=(((1:Nn)*dNn)-NnMid);
%Z
%str=input('Look at Z');
%Now calculate Y as a function of normal random variable.
Y(1:Nn)=c0;
for nn=1:Index
    Y(1:Nn)=Y(1:Nn)+c(nn)*Z(1:Nn).^nn;
end

%Now take change of densities derivative of Y with respect to normal
DfY(1:Nn)=0;
for nn=2:Nn-1
    DfY(nn) = (Y(nn + 1) - Y(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    %Change of variable derivative for densities
end
DfY(Nn)=DfY(Nn-1);
DfY(1)=DfY(2);

%Now calculate the density of Y from density of normal random variable
%using change of probability derivative.
pY(1:Nn)=0;
for nn = 1:Nn    
    pY(nn) = (normpdf(Z(nn),0, 1))/abs(DfY(nn));
end

plot(Y(1:Nn),pY(1:Nn),Color);
title('Density of the Z-Series Variable with Fitted Moments');
%str=input('Look at density');

end


```

.

.

.

.

```
function [XYProbDensity2D,XYProbMass2D,XProbMass,YProbMass,IndexMaxX,IndexMaxY,Xn,Ym,Zx,Zy,BinSizeX,BinSizeY] = Find2DDensityAndCDFFromSimulation_Infiniti04(X,Y,Paths,NoOfBinsX,NoOfBinsY,MaxCutOffX,MaxCutOffY)
                                                                                                                                                            

%This function processes joint observations of two stochastic variables X and Y from 
%common monte carlo paths and makes a two dimensional density of X and Y.

%Explanation of Input Parameters
%X and Y are 1D arrays so that nth element of each makes a joint 
%observation of nth monte carlo path X(n) and Y(n) form joint nth observation of two stochastic variables.
%paths ---- total monte carlo paths.
%NoOfBinsX ---- Uniform Grid size in X for density construction. You can alter
%this. But you will have to make sure to alter grid sizes in main program after
%this function has returned results.
%NoOfBinsY ---- Uniform Grid size in Y for density construction. You can alter
%this.

%Explanation of output Parameters
%XYProbDensity2D --- is 2D numerically constructed Parzen density on input
%grid in X and Y.
%XYProbMass2D, ------ is integrated version of 2D parzen density that gives
%two D probability mass on input grid in X and Y.
%XProbMass  ---- is probability mass of 1D marginal density in X on NoOfBinsX Grid.
%YProbMass  ---- is probability mass of 1D marginal density in Y on NoOfBinsY Grid.
%IndexMaxX ----- This is size of grid in X and corresponds to NoOfBinsX and
%is NoOfBinsX+1. Naturally This is also size of array that returns
%X-values on the X-axis of 2D uniform grid.
%IndexMaxY ----- This is size of grid in X and corresponds to NoOfBinsY and
%is  NoOfBinsY+1. Naturally This is also size of array that returns
%Y-values on Y-axis of the 2D uniform grid.
%Xn--- is an array of size IndexMaxX that contains values of X at the
%center of each grid cell on X-axis on 2D uniform grid.
%Ym--- is an array of size IndexMaxY that contains values of Y at the
%center of each grid cell on Y-axis on 2D uniform grid.
%Zx----- this is a 2D array. This returns the value of standard normal associated with Xn for every
%Ym grid cell. Given a certain grid cell Ym, we calculate CDF along all X grid
%cells with the same Ym. This is derived from inversion of univariate CDF on X-grid
%or X-axis associated with each Y grid cell. Zx(n,m) is a 2D array.
%Zy----- this is the value of standard normal associated with Ym at center
%of each grid cell on Y-axis. This is derived from inversion of univariate CDF on Y-grid
%or Y-axis. This is 1D array. This is used for vol which is independent of
%X.


X(X>MaxCutOffX)=MaxCutOffX;
Y(Y>MaxCutOffY)=MaxCutOffY;



hX = maxk(X,5);
Xmax2=min(hX);
Xmin2=min(X);

hY=maxk(Y,5);
Ymax2=min(hY);
Ymin2=min(Y);


Xmax2
Ymax2

str=input("Look at max values");



BinSizeX=(Xmax2-Xmin2)/NoOfBinsX;
BinSizeY=(Ymax2-Ymin2)/NoOfBinsY;
IndexMaxX=floor((Xmax2-Xmin2)/BinSizeX+.5)+1;
IndexMaxY=floor((Ymax2-Ymin2)/BinSizeY+.5)+1;

Xn(1:IndexMaxX)=Xmin2+(0:(IndexMaxX-1))*BinSizeX;
Ym(1:IndexMaxY)=Ymin2+(0:(IndexMaxY-1))*BinSizeY;

XYProbMass2D(1:IndexMaxX,1:IndexMaxY)=0.0;
XYProbDensity2D(1:IndexMaxX,1:IndexMaxY)=0.0;
XProbMass(1:IndexMaxX)=0;
YProbMass(1:IndexMaxY)=0;

for p=1:Paths
indexX=real(floor(real(X(p)-Xmin2)/BinSizeX+.5)+1);
%indexXp=real(X(p)-Xmin2)/BinSizeX+1;


if(real(indexX)IndexMaxX)
indexX=IndexMaxX;
end


indexY=real(floor(real(Y(p)-Ymin2)/BinSizeY+.5)+1);
%indexYp=real(Y(p)-Ymin2)/BinSizeY;

if(real(indexY)IndexMaxY)
indexY=IndexMaxY;
end



%XDensity(index)=XDensity(index)+1.0/Paths/BinSize;
XProbMass(indexX)=XProbMass(indexX)+1.0/Paths;
YProbMass(indexY)=YProbMass(indexY)+1.0/Paths;
XYProbMass2D(indexX,indexY)=XYProbMass2D(indexX,indexY)+1.0/Paths;
XYProbDensity2D(indexX,indexY)=XYProbDensity2D(indexX,indexY)+1.0/Paths/BinSizeX/BinSizeY;


end


X_avg=sum(X(1:Paths))/Paths

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Below calculate Zx by inversion of 1D X-CDF associated with each volatility grid cell
%so that resulting array is 2D.
XProbSum(1:IndexMaxX,1:IndexMaxY)=0;
XCDF(1:IndexMaxX,1:IndexMaxY)=0;
Zx(1:IndexMaxX,1:IndexMaxY)=0;

for mm=1:IndexMaxY
    XProbSum(1,mm)=XYProbMass2D(1,mm)*.5;
    if(YProbMass(mm)>0)
        XCDF(1,mm)=XProbSum(1,mm)./YProbMass(mm);
        
    else
        XCDF(1,mm)=0;
    end
    if((XCDF(1,mm)>0) && (XCDF(1,mm).999999999)
        Zx(1,mm)=5;
    end
    for nn=2:IndexMaxX
        XProbSum(nn,mm)=XProbSum(nn-1,mm)+XYProbMass2D(nn-1,mm)*.5+XYProbMass2D(nn,mm)*.5;
        if(YProbMass(mm)>0)
            XCDF(nn,mm)=XProbSum(nn,mm)./YProbMass(mm);
        else
            XCDF(nn,mm)=0;
        end
        if((XCDF(nn,mm)>0) && (XCDF(nn,mm).999999999)
            Zx(nn,mm)=5;
        end
        if (Zx(nn,mm)5)
            Zx(nn,mm)=5;
        end
    end
end
    
    

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



YCDF(1:IndexMaxY)=0;
Zy(1:IndexMaxY)=0;
YCDF(1)=YProbMass(1)*.5;
Zy(1)=norminv(YCDF(1));
for nn=2:IndexMaxY
    YCDF(nn)=YCDF(nn-1)+YProbMass(nn-1)*.5+YProbMass(nn)*.5;
    Zy(nn)=norminv(YCDF(nn));
    if (Zy(nn)5)
            Zy(nn)=5;
    end
end

end
```

.

.

.

.

```
function [pXY2D] = Calculate2VariablesOn2DGridFromAnalyticZSeries(XX,YY,NoOfBinsX,NoOfBinsY,Coeff,a0,a)


%YY are Y-coordinates of 2D Grid. In our case this is stochastic
%volatility and is univariate and independent of asset so it can be
%inverted as a univariate Z-series. its Z-series is given by a0 and a.

[Zy] = CalculateZgivenXAndZSeriesC5(YY,a0,a);


for mm=1:NoOfBinsY+1
    if(Zy(mm)>5.0)
        Zy(mm)=5.0;
    end
    if(Zy(mm)5.0)
        Zx(nn,mm)=5.0;   %possible error block
    end
    if(Zx(nn,mm)<-5.0)
        Zx(nn,mm)=-5.0;   %possible error block
    end 
%    if(Zx(nn+1,mm)<Zx(nn,mm))
%        Zx(nn+1,mm)=Zx(nn,mm);   %possible error block
%    end
    end
end


 

%Below we make calculations of density in original coordinates by doing 
%change of probability derivative with respect to gaussian density.
DinvfXX(1:NoOfBinsX+1,1:NoOfBinsY+1)=0;
for mm=1:NoOfBinsY+1
    for nn=2:NoOfBinsX
    
        DinvfXX(nn,mm) = (Zx(nn + 1,mm) - Zx(nn - 1,mm))/(XX(nn + 1) - XX(nn - 1));
    
    end
    DinvfXX(NoOfBinsX+1,mm)=DinvfXX(NoOfBinsX,mm);
    DinvfXX(1,mm)=DinvfXX(2,mm);
end


DinvfYY(1:NoOfBinsY+1)=0;
for mm=2:NoOfBinsY
    
        DinvfYY(mm) = (Zy(mm+1) - Zy(mm-1))/(YY(mm + 1) - YY(mm - 1));
    
end
DinvfYY(NoOfBinsY+1)=DinvfYY(NoOfBinsY);
DinvfYY(1)=DinvfYY(2);


pXY2D(1:NoOfBinsX+1,1:NoOfBinsY+1)=0;
for mm=1:NoOfBinsY
    for nn=1:NoOfBinsX
    
    pXY2D(nn,mm) = (normpdf(Zx(nn,mm),0, 1))*abs(DinvfXX(nn,mm)).*(normpdf(Zy(mm),0, 1))*abs(DinvfYY(mm));
 
    end
end


end


```

.

.

.

.

```
function [Z] = CalculateZgivenXAndZSeriesC5(X,c0,c)

Z(1:length(X))=0;

for nn=1:length(X)
    %X(nn)
    %c0
        Z(nn)=CalculateZgivenXAndZSeriesBisection2C5(X(nn),c0,c);
    %Z(nn)    
end

end


```

.

.

.

.

```
function [Z]=CalculateZgivenXAndZSeriesBisection2C5(Y,c0,c)

%This program takes a value of Y as input and returns the corresponding 
%value of Z given the parameters of the Z-series.
%It first see if the value of Y is greater than median or smaller than
%median. If the value of Y is greater than median Z has to be greater than
%zero and if the value of Y is smaller than median Z has to be negative.
% Once we know whether Z is greater than Z or smaller than Zero, we divide
% the program into two repeated if loops, one for Z greater than zero and 
%one for Z smaller than zero. 
%If Z is positive, we have to assign it a valid band of upper and
%lower values between which it can be found. 
%This is done sequentially by calculating Y(.5) at Z=.5, if Y is smaller 
%than Y(.5), we know that true value of Y will lie between 0 and .5
%so we assign a lower band value Za=0 and upper band value Zb=.5
%If however Y is greater than Y(.5), we know that true Z should be larger 
%than .5 and we again evaluate Y(1) at Z=1, If Y is smaller than Y(1), 
%we know that true value of Z should be between .5 and 1, and we assign a 
%lower band value Za=.5 and upper band value of Zb=1. Through repeated 
%elseif we continue until we find an appropriate band value of Z.

%Once we have determined the upper band value of Zb and lower band value of
%Za, We find Zmid=(Za+Zb)/2. We then evaluate Y(Zmid) and if Y  Y(Zmid), we assign the lower band value equal to Zmid as Za=Zmid. In a
% few iterations, this bisection procedure gets extremely close to true
% value of Z for which Y(Z)=Y

if(Y>c0)
    %Z=.5;
    if(Y  EvaluateZSeriesC5(c0,c,Zmid))
            Za=Zmid;
        end
    Z=.5*Za+.5*Zb; %This can be taken out of the loop and does not 
    %necessarily have to be calculated again and again. Has to be
    %calculated at least once after the loop to determine the true value of
    %Z.
    
    end
    
end
        
if(Y  EvaluateZSeriesC5(c0,c,-.5))
        Za=-.5;
        Zb=0;
    elseif(Y>  EvaluateZSeriesC5(c0,c,-1))
        Za=-1;
        Zb=-.5;
    elseif(Y>  EvaluateZSeriesC5(c0,c,-1.5))
        Za=-1.5;
        Zb=-1;  
    elseif(Y>  EvaluateZSeriesC5(c0,c,-2))
        Za=-2;
        Zb=-1.5;
    elseif(Y>  EvaluateZSeriesC5(c0,c,-2.5))
        Za=-2.5;
        Zb=-2.0; 
    elseif(Y>  EvaluateZSeriesC5(c0,c,-3))
        Za=-3;
        Zb=-2.5;
    elseif(Y>  EvaluateZSeriesC5(c0,c,-3.5))
        Za=-3.5;
        Zb=-3.0;
    elseif(Y>  EvaluateZSeriesC5(c0,c,-4))
        Za=-4;
        Zb=-3.5;
    elseif(Y>  EvaluateZSeriesC5(c0,c,-4.5))
        Za=-4.5;
        Zb=-4.0;
    elseif(Y>  EvaluateZSeriesC5(c0,c,-5))
        Za=-4.5;
        Zb=-5.0;  
    elseif(Y>  EvaluateZSeriesC5(c0,c,-5.5))
        Za=-5.0;
        Zb=-5.5; 
    elseif(Y>  EvaluateZSeriesC5(c0,c,-6.0))
        Za=-5.5;
        Zb=-6.0;     
    else
        Za=-12.0;
        Zb=-6.0;
    end
    for mm=1:20
        Zmid=.5*Za+.5*Zb;
        if(Y EvaluateZSeriesC5(c0,c,Zmid))
            Za=Zmid;
        end
    Z=.5*Za+.5*Zb; %This can be taken out of the loop and does not 
    %necessarily have to be calculated again and again. Has to be
    %calculated at least once after the loop to determine the true value of
    %Z
    end
    
end        
        
end


```

.

.

.

.

```
function [X] = EvaluateZSeriesC5(c0,c,Z)

X=c0+c(1)*Z+c(2)*Z.^2+c(3)*Z.^3+c(4)*Z.^4+c(5)*Z.^5;

end


```

.

.

.

.

you will see the following last output of the program as you run it.



str =

     []

Xmax2 =

     7

Ymax2 =

   1.100000000000000

Look at max values

X_avg =

   0.999194242414060

Zy =

  Columns 1 through 3

  -1.784802675247192  -1.293603658676147  -0.652314424514771

  Columns 4 through 6

  -0.258935689926147  -0.026485204696655   0.140625715255737

  Columns 7 through 9

   0.273208379745483   0.384335756301880   0.480751276016235

  Columns 10 through 12

   0.566397428512573   0.643787622451782   0.714626550674438

  Columns 13 through 15

   0.780125856399536   0.841181516647339   0.898474454879761

  Columns 16 through 18

   0.952534437179565   1.003784894943237   1.052567243576050

  Columns 19 through 21

   1.099162817001343   1.143804788589478   1.186691522598267

  Columns 22 through 24

   1.227989912033081   1.267844438552856   1.306379079818726

  Columns 25 through 27

   1.343703031539917   1.379911184310913   1.415087938308716

  Columns 28 through 30

   1.449307680130005   1.482637166976929   1.515136003494263

  Columns 31 through 33

   1.546857595443726   1.577850580215454   1.608158826828003

  Columns 34 through 36

   1.637822389602661   1.666877985000610   1.695358991622925

  Columns 37 through 39

   1.723295927047729   1.750716447830200   1.777647733688354

  Columns 40 through 42

   1.804113149642944   1.830135107040405   1.855734586715698

  Columns 43 through 45

   1.880930662155151   1.905741453170776   1.930183649063110

  Columns 46 through 48

   1.954272985458374   1.978024244308472   2.001451253890991

  Columns 49 through 51

   2.024566888809204   2.047383546829224   2.069913148880005

  Columns 52 through 54

   2.092165708541870   2.114152193069458   2.135882139205933

  Columns 55 through 57

   2.157364606857300   2.178609132766724   2.199622869491577

  Columns 58 through 60

   2.220414876937866   2.240991353988647   2.261360883712769

  Columns 61 through 63

   2.281529188156128   2.301503419876099   2.321289777755737

  Columns 64 through 66

   2.340893507003784   2.360321283340454   2.379577875137329

  Columns 67 through 69

   2.398669004440308   2.417598962783813   2.436372995376587

  Columns 70 through 72

   2.454995870590210   2.473471879959106   2.491805315017700

  Columns 73 through 75

   2.509999990463257   2.528060197830200   2.545989751815796

  Columns 76 through 78

   2.563791990280151   2.581470727920532   2.599029779434204

  Columns 79 through 81

   2.616471529006958   2.633799791336060   2.651017427444458

  Columns 82 through 84

   2.668127775192261   2.685133218765259   2.702037096023560

  Columns 85 through 87

   2.718841791152954   2.735550165176392   2.752164602279663

  Columns 88 through 90

   2.768687486648560   2.785121202468872   2.801468610763550

  Columns 91 through 93

   2.817732095718384   2.833913087844849   2.850013971328735

  Columns 94 through 96

   2.866037130355835   2.881984949111938   2.897858858108521

  Columns 97 through 99

   2.913660764694214   2.929393053054810   2.945057630538940

  Columns 100 through 102

   2.960655927658081   2.976189851760864   2.991661310195923

  Columns 103 through 105

   3.007071733474731   3.022423028945923   3.037717103958130

  Columns 106 through 108

   3.052954912185669   3.068138837814331   3.083269834518433

  Columns 109 through 111

   3.098349809646606   3.113379716873169   3.128361940383911

  Columns 112 through 114

   3.143296957015991   3.158186674118042   3.173032999038696

  Columns 115 through 117

   3.187836408615112   3.202598810195923   3.217321634292603

  Columns 118 through 120

   3.232006311416626   3.246653318405151   3.261265039443970

  Columns 121 through 123

   3.275841951370239   3.290385961532593   3.304898023605347

  Columns 124 through 126

   3.319379568099976   3.333831548690796   3.348255872726440

  Columns 127 through 129

   3.362653017044067   3.377024412155151   3.391371488571167

  Columns 130 through 132

   3.405695676803589   3.419997453689575   3.434278726577759

  Columns 133 through 135

   3.448540449142456   3.462784051895142   3.477010488510132

  Columns 136 through 138

   3.491220712661743   3.505416154861450   3.519598722457886

  Columns 139 through 141

   3.533768415451050   3.547927141189575   3.562076330184937

  Columns 142 through 144

   3.576216936111450   3.590349912643433   3.604476690292358

  Columns 145 through 147

   3.618598699569702   3.632717370986938   3.646833181381226

  Columns 148 through 150

   3.660948514938354   3.675063848495483   3.689180612564087

  Column 151

   3.703300237655640

Look at Zy

Look at numerical bivariate density of Asset and Stochastic Volatility

str =

     []

Look at Analytic density of Asset and Stochastic volatility

str =

     []

Look at difference of numerical and analytic densities of Asset and stochastic volatility

str =

     []
```

---

## Error 25: Unbalanced $: 1

**Snippet:** `Sorry. I noticed that some functions are still missing. I am attaching them here`

**Full content:**

```
Sorry. I noticed that some functions are still missing. I am attaching them here.


```
function [ZnNew] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable)
[Zn] = StandardNormalIdealDesity02(Ndata,1);


[alpha0,beta0,gamma0] = ReadParamsFile(Ndata,Mtable)



ZnNew(1:Ndata)=Zn(1:Ndata).*(alpha0+beta0*(Zn(1:Ndata).^2-1)+gamma0*(Zn(1:Ndata).^4-6*Zn(1:Ndata).^2+3));
        
Moment2=sum(ZnNew(1:Ndata).^2)*1/Ndata;
Moment4=sum(ZnNew(1:Ndata).^4)*1/Ndata;
Moment6=sum(ZnNew(1:Ndata).^6)*1/Ndata;        


Moment2
Moment4
Moment6
display("fitted Moments");
%str=input("Look at moment values")

end


```

.

.

.

```
function [a0,a] = CalculateZSeriesDensityByIdealMeasureMean05WithZI(data,ZI,ZProb)


Ndata=length(data);



Sdata=sort(data);


Y(1:Ndata,1)=Sdata(1:Ndata);
Mean=sum(Y(1:Ndata,1))/Ndata;
Y(1:Ndata,1)=Y(1:Ndata,1)-Mean; %subtract the mean. Variance standardization might not have an effect.
if (rem(Ndata,2)==0)
%Median1=sum(Y(Ndata/2,1)+Y(Ndata/2+1,1))/2;

x0=0;
x1=ZI(Ndata/2-3);
x2=ZI(Ndata/2-2);
x3=ZI(Ndata/2-1);
x4=ZI(Ndata/2+1);
x5=ZI(Ndata/2+2);
x6=ZI(Ndata/2+3);

y1=Y(Ndata/2-3);
y2=Y(Ndata/2-2);
y3=Y(Ndata/2-1);
y4=Y(Ndata/2+1);
y5=Y(Ndata/2+2);
y6=Y(Ndata/2+3);
N=6;
[y0] = InterpolateOrderN6(N,x0,x1,x2,x3,x4,x5,x6,y1,y2,y3,y4,y5,y6);

Median=y0;

% Median1
% Median
% %str=input("Look at Medians");
else
Median=Y(floor(Ndata/2+1),1);
end

Ymu(1:Ndata,1)=Y(1:Ndata,1)-Median;%subtract the median
Zu=0;   %Since median is subtracted from mean-standardized data, we have to 
%subtract the Z=0 from ZI i.e subtract nothing.
X(1:Ndata,1:6)=0;
%Below I am regressing powers of Z as in Z-series but hermites could
%equally be regressed and I expect that results would probably be extremely
%close.
for nn=1:Ndata
    X(nn,1)=1;
    X(nn,2)=(ZI(nn)-Zu);
    X(nn,3)=(ZI(nn)-Zu).^2;
    X(nn,4)=(ZI(nn)-Zu).^3;
    X(nn,5)=(ZI(nn)-Zu).^4;
    X(nn,6)=(ZI(nn)-Zu).^5;
    %X(nn,7)=(ZI(nn)-Zu).^6;
    %X(nn,8)=(ZI(nn)-Zu).^7;
end

%coeff=inv(X'*X)*(X'*Ymu);
coeff=(X'*X)$X'*Ymu);
c0=coeff(1,1);
c(1:5)=coeff(2:6,1);

a0=c0;
a=c;
a0=a0+Median+Mean;
end
```


.

.

.

```
function [X] = EvaluateZSeriesC5(c0,c,Z)

X=c0+c(1)*Z+c(2)*Z.^2+c(3)*Z.^3+c(4)*Z.^4+c(5)*Z.^5;

end



```

.

.

.

```
function [dXdZ] = EvaluateZSeriesdXdZC5(c0,c,Z)

dXdZ=c(1)+2*c(2)*Z+3*c(3)*Z.^2+4*c(4)*Z.^3+5*c(5)*Z.^4;

end


```

.

.

.

```
function [aH0,aH] = ConvertZCoeffsToHCoeffs(a0,a,SeriesOrder)

if(SeriesOrder==3)
aH0=a0+a(2);
aH(1)=a(1)+3*a(3);
aH(2)=a(2);
aH(3)=a(3);
end


if(SeriesOrder==4)
aH0=a0+a(2)+3*a(4);
aH(1)=a(1)+3*a(3);
aH(2)=a(2)+6*a(4);
aH(3)=a(3);
aH(4)=a(4);
end


if(SeriesOrder==5)
aH0=a0+a(2)+3*a(4);
aH(1)=a(1)+3*a(3)+15*a(5);
aH(2)=a(2)+6*a(4);
aH(3)=a(3)+10*a(5);
aH(4)=a(4);
aH(5)=a(5);
end



if(SeriesOrder==6)
aH0=a0+a(2)+3*a(4)+15*a(6);
aH(1)=a(1)+3*a(3)+15*a(5);
aH(2)=a(2)+6*a(4)+45*a(6);
aH(3)=a(3)+10*a(5);
aH(4)=a(4)+15*a(6);
aH(5)=a(5);
aH(6)=a(6);
end


if(SeriesOrder==7)
aH0=a0+a(2)+3*a(4)+15*a(6);
aH(1)=a(1)+3*a(3)+15*a(5)+105*a(7);
aH(2)=a(2)+6*a(4)+45*a(6);
aH(3)=a(3)+10*a(5)+105*a(7);
aH(4)=a(4)+15*a(6);
aH(5)=a(5)+21*a(7);
aH(6)=a(6);
aH(7)=a(7);
end



end


```

.

.

.

```
function [alpha0,beta0,gamma0] = ReadParamsFile(Ndata,Mtable)

A=Mtable;
NSubDivs=A.(1);
alpha=A.(2);
beta=A.(3);
gamma=A.(4);
% NSubDivs
% alpha
% beta
% gamma
% 
% A.(1)(1)

%Ndata;

nn=1;
if(NdataNdata))
            alpha1=alpha(nn-1);
            alpha2=alpha(nn);
            alpha3=alpha(nn+1)
            alpha4=alpha(nn+2);
            
            beta1=beta(nn-1);
            beta2=beta(nn);
            beta3=beta(nn+1)
            beta4=beta(nn+2);
            
            gamma1=gamma(nn-1);
            gamma2=gamma(nn);
            gamma3=gamma(nn+1)
            gamma4=gamma(nn+2);
            
            x1=NSubDivs(nn-1);
            x2=NSubDivs(nn);
            x3=NSubDivs(nn+1);
            x4=NSubDivs(nn+2);
            
            x0=Ndata;
            N=4;
            
            [alpha0] = InterpolateOrderN6(N,x0,x1,x2,x3,x4,0,0,alpha1,alpha2,alpha3,alpha4,0,0);
            [beta0] = InterpolateOrderN6(N,x0,x1,x2,x3,x4,0,0,beta1,beta2,beta3,beta4,0,0);
            [gamma0] = InterpolateOrderN6(N,x0,x1,x2,x3,x4,0,0,gamma1,gamma2,gamma3,gamma4,0,0);
            %alpha0=alpha(nn)*(Ndata-NSubDivs(nn))/(NSubDivs(nn+1)-NSubDivs(nn))+alpha(nn+1)*(NSubDivs(nn+1)-Ndata)/(NSubDivs(nn+1)-NSubDivs(nn));
            %beta0=beta(nn)*(Ndata-NSubDivs(nn))/(NSubDivs(nn+1)-NSubDivs(nn))+beta(nn+1)*(NSubDivs(nn+1)-Ndata)/(NSubDivs(nn+1)-NSubDivs(nn));
            %gamma0=gamma(nn)*(Ndata-NSubDivs(nn))/(NSubDivs(nn+1)-NSubDivs(nn))+gamma(nn+1)*(NSubDivs(nn+1)-Ndata)/(NSubDivs(nn+1)-NSubDivs(nn));
            display("I am in part--2");
        end
        nn=nn+1;
    end
else
    display("data out of range")
end




end


```

.

.

.
```

---

## Error 26: Unbalanced $: 1

**Snippet:** `Friends, I am posting the program in the hope that it would be helpful for frien`

**Full content:**

```
Friends, I am posting the program in the hope that it would be helpful for friends and they could just try their version of equations for summation without having to go through writing all the basic program.

Sorry for breaking the excitement but it seems that more work needs to be done to settle the problem and I realized that a lot of scenarios are not working very well. I am trying to concentrate on this problem to solve the addition and products with correlations and will try to see if I can think of anything interesting.



Case for correlation between asset and SV needs to be more deeply considered. One reason for lack of good program might be that I am using almost lognormal asset and almost lognormal volatility and even fore moderate volatilities, they cannot be described by five hermite polynomials. Please try some smaller CEV indexes. Though I believe more serious work has to be done on the problem.



Here is the program. You might have to look for the thread for some basic functions that we have been using all the time.


```
function [] = AnalyticAddTwoSDEDensities()

X0=1.0;
alpha1=0;
alpha2=1;
kappaX=0;
thetaX=1;
a=kappaX*thetaX;
b=-kappaX;

rho=0;
sigma1=.65;
gammaV=.5;
gammaX=.95;
%%%%%%%%`%%%%%
V0=.950;
thetaV=.75;
kappaV=.650;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.95;
sigma0=.65;


dt=.03125/2;
Tt=64*1;

T=Tt*dt;




%%%%%%%%%%%%%%%%%%%%%%%%5
rng(82139475, 'twister')
paths=500000;
V(1:paths)=V0;  %Original process monte carlo.
X(1:paths)=X0;
% paths0=paths/2;
% paths00=paths/4;
% Random1(1:paths00)=0;
% Random2(1:paths0)=0;


paths0=paths;
paths00=paths;
Random1(1:paths00)=0;
Random2(1:paths0)=0;

for tt=1:Tt
    
Random2=randn(size(Random2)); 
Random1=randn(size(Random1)); 

% sum(Random1)/paths
% sum(Random1.^2)/paths
% sum(Random1.^3)/paths
% sum(Random1.^4)/paths
% sum(Random1.^5)/paths
% sum(Random1.^6)/paths
% 
% tt
% 
% str=input("Look at moments of MC Normals");

%Random1(paths00+1:2*paths00)=-1*Random1(1:paths00);
%Random2(paths0+1:2*paths0)=-1*Random2(1:paths0);    
%Random1(paths0+1:2*paths0)=Random1(1:paths0);    
%antithetic variates above


X(1:paths)=X(1:paths)+ ...
    (a* X(1:paths).^alpha1 + b* X(1:paths).^alpha2)* dt + ...
    sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.* X(1:paths).^gammaX .*Random1(1:paths) * sqrt(dt) + ...
    rho* sigma1* V(1:paths).^gammaV .*X(1:paths).^gammaX .*Random2(1:paths)*sqrt(dt) + ...
    (a*alpha1* X(1:paths).^(alpha1-1)+b*alpha2* X(1:paths).^(alpha2-1)).* ...
    (((a* X(1:paths).^alpha1 + b* X(1:paths).^alpha2)* dt^2/2)+ ...
    (sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.* X(1:paths).^gammaX .*Random1(1:paths) *(1-1/sqrt(3)).*dt^1.5+ ...
    rho* sigma1* V(1:paths).^gammaV .*X(1:paths).^gammaX .*Random2(1:paths)*(1-1/sqrt(3)).*dt^1.5))+ ...
    .5*(a*alpha1*(alpha1-1)* X(1:paths).^(alpha1-2)+b*alpha2*(alpha2-1).* X(1:paths).^(alpha2-2)).* ...
    ( sigma1^2* V(1:paths).^(2*gammaV).* X(1:paths).^(2*gammaX)) *dt^2/2 + ...
    sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.*gammaX.* X(1:paths).^(gammaX-1).* ...
    ((a* X(1:paths).^alpha1 + b* X(1:paths).^alpha2).*Random1(1:paths) * 1/sqrt(3).* dt^1.5 + ...
    sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.* X(1:paths).^gammaX .*(Random1(1:paths).^2-1) * dt/2 + ...
    rho* sigma1* V(1:paths).^gammaV .*X(1:paths).^gammaX .*Random1(1:paths).*Random2(1:paths)*dt/2)+ ...
    .5*sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.*gammaX.*(gammaX-1).* X(1:paths).^(gammaX-2).* ...
    (sigma1^2* V(1:paths).^(2*gammaV).* X(1:paths).^(2*gammaX) .*Random1(1:paths).*1/sqrt(3).*dt^1.5)+ ...
    sqrt(1-rho^2)* sigma1*gammaV.* V(1:paths).^(gammaV-1).* X(1:paths).^(gammaX).* ...
    ((mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2).*Random1(1:paths) * 1/sqrt(3).* dt^1.5 + ...
    sigma0*V(1:paths).^gamma.*Random1(1:paths).*Random2(1:paths)*dt/2)+ ...
    .5*sqrt(1-rho^2)* sigma1*gammaV.*(gammaV-1).* V(1:paths).^(gammaV-2).* X(1:paths).^(gammaX).* ...
    (sigma0^2*V(1:paths).^(2*gamma).*Random1(1:paths)*1/sqrt(3)*dt^1.5)+ ...
    sqrt(1-rho^2)* sigma1*gammaV.* V(1:paths).^(gammaV-1).*gammaX.* X(1:paths).^(gammaX-1).* ...
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX .*sigma0.*V(1:paths).^gamma.*Random1(1:paths)*1/sqrt(3)*dt^1.5+ ...
    rho* sigma1* V(1:paths).^gammaV.*gammaX.* X(1:paths).^(gammaX-1).* ...
    ((a* X(1:paths).^alpha1 + b* X(1:paths).^alpha2).*Random2(1:paths) * 1/sqrt(3).* dt^1.5 + ...
    sqrt(1-rho^2)* sigma1* V(1:paths).^gammaV.* X(1:paths).^gammaX .*Random1(1:paths).*Random2(1:paths) * dt/2 + ...
    rho* sigma1* V(1:paths).^gammaV .*X(1:paths).^gammaX .*(Random2(1:paths).^2-1)*dt/2)+ ...
    .5*rho* sigma1* V(1:paths).^gammaV.*gammaX.*(gammaX-1).* X(1:paths).^(gammaX-2).* ...
    (sigma1^2* V(1:paths).^(2*gammaV).* X(1:paths).^(2*gammaX) .*Random2(1:paths).*1/sqrt(3).*dt^1.5)+ ...
    rho* sigma1*gammaV.* V(1:paths).^(gammaV-1).* X(1:paths).^(gammaX).* ...
    ((mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2).*Random2(1:paths) * 1/sqrt(3).* dt^1.5 + ...
    sigma0*V(1:paths).^gamma.*(Random2(1:paths).^2-1)*dt/2)+ ...
    .5*rho* sigma1*gammaV.*(gammaV-1).* V(1:paths).^(gammaV-2).* X(1:paths).^(gammaX).* ...
    sigma0^2.*V(1:paths).^(2*gamma).*Random2(1:paths) * 1/sqrt(3).* dt^1.5+ ...
    rho* sigma1*gammaV.* V(1:paths).^(gammaV-1).*gammaX.* X(1:paths).^(gammaX-1).* ...
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX .*sigma0.*V(1:paths).^gamma.*Random2(1:paths)*1/sqrt(3)*dt^1.5;
    

    V(1:paths)=V(1:paths)+ ...
        (mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2)*dt + ...
        sigma0*V(1:paths).^gamma .*Random2(1:paths)*sqrt(dt) + ...
        (mu1.*beta1*V(1:paths).^(beta1-1) + mu2.*beta2.*V(1:paths).^(beta2-1)).* ...
        ((mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2)*dt^2/2 + ...
        sigma0*V(1:paths).^gamma .*Random2(1:paths)*(1-1/sqrt(3))*dt^1.5) + ...
        .5*(mu1.*beta1.*(beta1-1).*V(1:paths).^(beta1-2) + mu2.*beta2.*(beta2-1).*V(1:paths).^(beta2-2)).* ...    
        sigma0^2.*V(1:paths).^(2*gamma).*dt^2/2 + ...
        sigma0*gamma*V(1:paths).^(gamma-1) .* ...
        ((mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2).*Random2(1:paths).*1/sqrt(3)*dt^1.5 + ...
        sigma0.*V(1:paths).^gamma .*(Random2(1:paths).^2-1)*dt/2) + ...
        .5*sigma0*gamma*(gamma-1).*V(1:paths).^(gamma-2) .* ...
        sigma0^2.*V(1:paths).^(2*gamma) .*Random2(1:paths).*1/sqrt(3)*dt^1.5;


end
% X1=X;
% V1=V;
% 
% save('MonteCarloData1','X1','V1');


%str=input("Monte carlo data has been saved");
X(X<0)=0;
V(V<0)=0;
X=real(X);
V=real(V);

% SVolMeanAnalytic=thetaV+exp(-kappaV*T)*(V0-thetaV)
% SVolMean=sum(V(1:paths))/paths
% AssetMeanAnalytic=thetaX+exp(-kappaX*T)*(X0-thetaX)
% AssetMean=sum(X(1:paths))/paths

    W=X+V; %Add asset and volatility to find sum variable

    
    
    
    Ndata=paths;
    Mtable=readtable('C:\Users\Lenovo\Documents\MATLAB\MATLAB1\MomentMatchParams08.txt');
    [Xs,Ix]=sort(X);
    [ZI] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable);
    ZProb(1:Ndata)=1/Ndata;
    [a0,a] = CalculateZSeriesDensityByIdealMeasureMean05WithZI(Xs,ZI,ZProb);
    [ah0,ah] = ConvertZCoeffsToHCoeffs(a0,a,5);
    
    %Above ah0, ah are coefficients of hermite series of asset. a0,a are
    %coefficients of Z-series of assset.

    
    [Vs,Iv]=sort(V);
    %[ZI] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable);
    ZProb(1:Ndata)=1/Ndata;
    [b0,b] = CalculateZSeriesDensityByIdealMeasureMean05WithZI(Vs,ZI,ZProb);
    [bh0,bh] = ConvertZCoeffsToHCoeffs(b0,b,5);
    
     %Above bh0, bh are coefficients of hermite series of SV. b0,b are
    %coefficients of Z-series of SV.
    
    
    
    [Zx0] = CalculateZgivenXAndZSeriesC5Improved(X,a0,a);
    [Zv0] = CalculateZgivenXAndZSeriesC5Improved(V,b0,b);
    
    for pp=1:paths
       Zx1(Ix(pp))=norminv(pp/paths-.000001*pp/paths);
       Zv1(Iv(pp))=norminv(pp/paths-.000001*pp/paths);
    end
    
    Nhermites=5;
    [CorrH1] = CalculateCorrelationsBetweenTwoZSeriesRVs(Zx0,Zv0,paths,Nhermites);
    
    [CorrH] = CalculateCorrelationsBetweenTwoZSeriesRVs(Zx1,Zv1,paths,Nhermites);
    
    CorrH
    CorrH1
    str=input("Look at correlations");
    
    ch0=ah0+bh0;
    
    
%     chh(1)=sqrt((ah(1)+CorrH(1).*bh(1)).^2+(1-CorrH(1).^2).*bh(1).^2);
%     chh(2)=sqrt((ah(2)+CorrH(2).*bh(2)).^2+(1-CorrH(2).^2).*bh(2).^2);
%     chh(3)=sqrt((ah(3)+CorrH(3).*bh(3)).^2+(1-CorrH(3).^2).*bh(3).^2);
%     chh(4)=sqrt((ah(4)+CorrH(4).*bh(4)).^2+(1-CorrH(4).^2).*bh(4).^2);
%     chh(5)=sqrt((ah(5)+CorrH(5).*bh(5)).^2+(1-CorrH(5).^2).*bh(5).^2);
%     
%     

%Equations for Sum random variable as posted on wilmott.
     ch(1)=sqrt((bh(1)+CorrH(1).*ah(1)).^2+(1-CorrH(1).^2).*ah(1).^2);
     ch(2)=sqrt((bh(2)+CorrH(2).*ah(2)).^2+(1-CorrH(2).^2).*ah(2).^2);
     ch(3)=sqrt((bh(3)+CorrH(3).*ah(3)).^2+(1-CorrH(3).^2).*ah(3).^2);
     ch(4)=sqrt((bh(4)+CorrH(4).*ah(4)).^2+(1-CorrH(4).^2).*ah(4).^2);
     ch(5)=sqrt((bh(5)+CorrH(5).*ah(5)).^2+(1-CorrH(5).^2).*ah(5).^2);
     
     
     
%Works very well for uncorrelated(in traditional sense) but is seemingly wrong.     
%     ch(1)=sqrt((bh(1)+CorrH(1).*ah(1)).^2+(1-CorrH(1)).^2.*ah(1).^2);
%     ch(2)=sqrt((bh(2)+CorrH(2).*ah(2)).^2+(1-CorrH(2)).^2.*ah(2).^2);
%     ch(3)=sqrt((bh(3)+CorrH(3).*ah(3)).^2+(1-CorrH(3)).^2.*ah(3).^2);
%     ch(4)=sqrt((bh(4)+CorrH(4).*ah(4)).^2+(1-CorrH(4)).^2.*ah(4).^2);
%     ch(5)=sqrt((bh(5)+CorrH(5).*ah(5)).^2+(1-CorrH(5)).^2.*ah(5).^2);
%     
    
%     ch(1)=.5*ch(1)+.5*chh(1);
%     ch(2)=.5*ch(2)+.5*chh(2);
%     ch(3)=.5*ch(3)+.5*chh(3);
%     ch(4)=.5*ch(4)+.5*chh(4);
%     ch(5)=.5*ch(5)+.5*chh(5);
        
    
    [c0,c] = ConvertHCoeffsToZCoeffs(ch0,ch,5);
    
    [Ws,Iw]=sort(W);
    [d0,d] = CalculateZSeriesDensityByIdealMeasureMean05WithZI(Ws,ZI,ZProb);
    [dh0,dh] = ConvertHCoeffsToZCoeffs(d0,d,5);

    
    ah0
    ah
    bh0
    bh
    ch0
    ch
    dh0
    dh
    
    a0
    a
    b0
    b
    d0
    c0
    d
    c
    

    
    
    dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=45*4;  % No of normal density subdivisions
NnMid=((1+Nn)/2)*dNn;
Z(1:Nn)=(((1:Nn)*dNn)-NnMid);


XX(1:Nn)=c0;
for nn=1:5
    XX(1:Nn)=XX(1:Nn)+c(nn)*Z(1:Nn).^nn;
end

XX0(1:Nn)=d0;
for nn=1:5
    XX0(1:Nn)=XX0(1:Nn)+d(nn)*Z(1:Nn).^nn;
end

clf;

plot(Z(1:Nn),XX(1:Nn),'r',Z(1:Nn),XX0(1:Nn),'g')
    
    
    
    str=input("Look at coeffs of Added variable and Graph comparison")
    
    
    clf;
    PlotZSeriesDensity(d0,d,'g');
    hold on
    PlotZSeriesDensity(c0,c,'r');
    hold off
    str=input("Look at densities Graph comparison")
    
    
end


```


.

.

.


```
function [ZnNew] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable)
[Zn] = StandardNormalIdealDesity02(Ndata,1);


[alpha0,beta0,gamma0] = ReadParamsFile(Ndata,Mtable)



ZnNew(1:Ndata)=Zn(1:Ndata).*(alpha0+beta0*(Zn(1:Ndata).^2-1)+gamma0*(Zn(1:Ndata).^4-6*Zn(1:Ndata).^2+3));
        
Moment2=sum(ZnNew(1:Ndata).^2)*1/Ndata;
Moment4=sum(ZnNew(1:Ndata).^4)*1/Ndata;
Moment6=sum(ZnNew(1:Ndata).^6)*1/Ndata;        


Moment2
Moment4
Moment6
display("fitted Moments");
%str=input("Look at moment values")

end


```


.

.

.


```
function [a0,a] = CalculateZSeriesDensityByIdealMeasureMean05WithZI(data,ZI,ZProb)


Ndata=length(data);



Sdata=sort(data);


Y(1:Ndata,1)=Sdata(1:Ndata);
Mean=sum(Y(1:Ndata,1))/Ndata;
Y(1:Ndata,1)=Y(1:Ndata,1)-Mean; %subtract the mean. Variance standardization might not have an effect.
if (rem(Ndata,2)==0)
%Median1=sum(Y(Ndata/2,1)+Y(Ndata/2+1,1))/2;

x0=0;
x1=ZI(Ndata/2-3);
x2=ZI(Ndata/2-2);
x3=ZI(Ndata/2-1);
x4=ZI(Ndata/2+1);
x5=ZI(Ndata/2+2);
x6=ZI(Ndata/2+3);

y1=Y(Ndata/2-3);
y2=Y(Ndata/2-2);
y3=Y(Ndata/2-1);
y4=Y(Ndata/2+1);
y5=Y(Ndata/2+2);
y6=Y(Ndata/2+3);
N=6;
[y0] = InterpolateOrderN6(N,x0,x1,x2,x3,x4,x5,x6,y1,y2,y3,y4,y5,y6);

Median=y0;

% Median1
% Median
% %str=input("Look at Medians");
else
Median=Y(floor(Ndata/2+1),1);
end

Ymu(1:Ndata,1)=Y(1:Ndata,1)-Median;%subtract the median
Zu=0;   %Since median is subtracted from mean-standardized data, we have to 
%subtract the Z=0 from ZI i.e subtract nothing.
X(1:Ndata,1:6)=0;
%Below I am regressing powers of Z as in Z-series but hermites could
%equally be regressed and I expect that results would probably be extremely
%close.
for nn=1:Ndata
    X(nn,1)=1;
    X(nn,2)=(ZI(nn)-Zu);
    X(nn,3)=(ZI(nn)-Zu).^2;
    X(nn,4)=(ZI(nn)-Zu).^3;
    X(nn,5)=(ZI(nn)-Zu).^4;
    X(nn,6)=(ZI(nn)-Zu).^5;
    %X(nn,7)=(ZI(nn)-Zu).^6;
    %X(nn,8)=(ZI(nn)-Zu).^7;
end

%coeff=inv(X'*X)*(X'*Ymu);
coeff=(X'*X)$X'*Ymu);
c0=coeff(1,1);
c(1:5)=coeff(2:6,1);

a0=c0;
a=c;
a0=a0+Median+Mean;
end
```


.

.

.


```
function [CorrH] = CalculateCorrelationsBetweenTwoZSeriesRVs(Z1,Z2,paths,Nhermites)

CorrH(1:Nhermites)=0;
CovH(1:Nhermites)=0;
VarH1(1:Nhermites)=0;
VarH2(1:Nhermites)=0;
for pp=1:paths
    for hh=1:Nhermites
        if(hh==1)
            CovH(hh)=CovH(hh)+Z1(pp).*Z2(pp)/paths;
            VarH1(hh)=VarH1(hh)+Z1(pp).*Z1(pp)/paths;
            VarH2(hh)=VarH2(hh)+Z2(pp).*Z2(pp)/paths;
        end
        if(hh==2)
            CovH(hh)=CovH(hh)+(Z1(pp).^2-1).*(Z2(pp).^2-1)/paths;
            VarH1(hh)=VarH1(hh)+(Z1(pp).^2-1).*(Z1(pp).^2-1)/paths;
            VarH2(hh)=VarH2(hh)+(Z2(pp).^2-1).*(Z2(pp).^2-1)/paths;
        end
        if(hh==3)
            CovH(hh)=CovH(hh)+(Z1(pp).^3-3*Z1(pp)).*(Z2(pp).^3-3*Z2(pp))/paths;
            VarH1(hh)=VarH1(hh)+(Z1(pp).^3-3*Z1(pp)).*(Z1(pp).^3-3*Z1(pp))/paths;
            VarH2(hh)=VarH2(hh)+(Z2(pp).^3-3*Z2(pp)).*(Z2(pp).^3-3*Z2(pp))/paths;
        end
        if(hh==4)
            CovH(hh)=CovH(hh)+(Z1(pp).^4-6*Z1(pp).^2+3).*(Z2(pp).^4-6*Z2(pp).^2+3)/paths;
            VarH1(hh)=VarH1(hh)+(Z1(pp).^4-6*Z1(pp).^2+3).*(Z1(pp).^4-6*Z1(pp).^2+3)/paths;
            VarH2(hh)=VarH2(hh)+(Z2(pp).^4-6*Z2(pp).^2+3).*(Z2(pp).^4-6*Z2(pp).^2+3)/paths;
        end
        if(hh==5)
            CovH(hh)=CovH(hh)+(Z1(pp).^5-10*Z1(pp).^3+15*Z1(pp)).*(Z2(pp).^5-10*Z2(pp).^3+15*Z2(pp))/paths;
            VarH1(hh)=VarH1(hh)+(Z1(pp).^5-10*Z1(pp).^3+15*Z1(pp)).*(Z1(pp).^5-10*Z1(pp).^3+15*Z1(pp))/paths;
            VarH2(hh)=VarH2(hh)+(Z2(pp).^5-10*Z2(pp).^3+15*Z2(pp)).*(Z2(pp).^5-10*Z2(pp).^3+15*Z2(pp))/paths;
        end
    end
end


for hh=1:Nhermites
     CorrH(hh)=CovH(hh)./sqrt(VarH1(hh))./sqrt(VarH2(hh));
%      if(hh==1)
%          CorrH(hh)=CovH(hh);
%      end
%      if(hh==2)
%          CorrH(hh)=CovH(hh)/2;;
%      end
%     if(hh==3)
%          CorrH(hh)=CovH(hh)/6;
%     end
%     if(hh==4)
%          CorrH(hh)=CovH(hh)/24;
%     end
%     if(hh==5)
%          CorrH(hh)=CovH(hh)/120;
%      end 
     
end

VarH1
VarH2
CovH
CorrH

end


```


.

.

.


```
function [] = PlotZSeriesDensity(c0,c,Color)

Index=length(c);

dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=45*4;  % No of normal density subdivisions
NnMid=((1+Nn)/2)*dNn;
Z(1:Nn)=(((1:Nn)*dNn)-NnMid);
%Z
%str=input('Look at Z');
%Now calculate Y as a function of normal random variable.
Y(1:Nn)=c0;
for nn=1:Index
    Y(1:Nn)=Y(1:Nn)+c(nn)*Z(1:Nn).^nn;
end

%Now take change of densities derivative of Y with respect to normal
DfY(1:Nn)=0;
for nn=2:Nn-1
    DfY(nn) = (Y(nn + 1) - Y(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    %Change of variable derivative for densities
end
DfY(Nn)=DfY(Nn-1);
DfY(1)=DfY(2);

%Now calculate the density of Y from density of normal random variable
%using change of probability derivative.
pY(1:Nn)=0;
for nn = 1:Nn    
    pY(nn) = (normpdf(Z(nn),0, 1))/abs(DfY(nn));
end
Y;
%clf;
plot(Y(1:Nn),pY(1:Nn),Color);
title('Density of the Z-Series Variable with Fitted Moments');
str=input('Look at density');

% %clf;
% plot(Z(1:Nn),Y(1:Nn),Color);
% title('Graph of Z-Series Variable as a function of underlying standard normal');
% str=input('Look at Graph of Z-Series Variable as a function of underlying standard normal');
% 

end


```

.

.

.
```

---

## Error 27: Unbalanced $$: 3

**Snippet:** `Friends, this is a simple program that multiplies a bivariate 2D Density with an`

**Full content:**

```
Friends, this is a simple program that multiplies a bivariate 2D Density with another Bivariate 2D Density.

You can multiply a variable repeatedly with itself to get its powers and also find expectations of those powers.

There is no bound on size of the series and their results per se but of course extremely high values of expectations of large powers of normal density may create problems in calculation of their expectations.

I have given the variables below to represent as they appear in program. Variables(X1,X2,X3) do not appear in program input rather coefficients(aa,bb,cc) are input to program.

The program also calculates the expectation of the product X3(Zy,Zx)



$X1(Z_y,Z_x)\, = \, aa_{1,1} \, + \, aa_{2,1} \, Z_y \,+ \, aa_{3,1} \, {Z_y}^2 \,+ \, \ldots \,+ \, aa_{N1,1} \, {Z_y}^{(N1-1)} \, \\ 

\,+\, \Big[ \, aa_{1,2} \, + \, aa_{2,2} \, Z_y \,+ \, aa_{3,2} \, {Z_y}^2 \,+ \, \ldots \,+ \, aa_{N1,2} \, {Z_y}^{(N1-1)} \,\Big] \, Z_x \\ 

\,+\, \Big[ \, aa_{1,3} \, + \, aa_{2,3} \, Z_y \,+ \, aa_{3,3} \, {Z_y}^2 \,+ \, \ldots \,+ \, aa_{N1,3} \, {Z_y}^{(N1-1)} \,\Big] \, {Z_x}^2 \\ 

\,+\, \cdots \, \\

\,+\, \cdots \, \\

\,+\, \Big[ \, aa_{1,M1} \, + \, aa_{2,M1} \, Z_y \,+ \, aa_{3,M1} \, {Z_y}^2 \,+ \, \ldots \,+ \, aa_{N1,M1} \, {Z_y}^{(N1-1)} \,\Big] \, {Z_x}^{M1-1} \$$$] 



In the above

SeriesOrder10=N1;

SeriesOrder01=M1;



$X2(Z_y,Z_x)\, = \, bb_{1,1} \, + \, bb_{2,1} \, Z_y \,+ \, bb_{3,1} \, {Z_y}^2 \,+ \, \ldots \,+ \, bb_{N2,1} \, {Z_y}^{(N2-1)} \, \\ 

\,+\, \Big[ \, bb_{1,2} \, + \, bb_{2,2} \, Z_y \,+ \, bb_{3,2} \, {Z_y}^2 \,+ \, \ldots \,+ \, bb_{N2,2} \, {Z_y}^{(N2-1)} \,\Big] \, Z_x \\ 

\,+\, \Big[ \, bb_{1,3} \, + \, bb_{2,3} \, Z_y \,+ \, bb_{3,3} \, {Z_y}^2 \,+ \, \ldots \,+ \, bb_{N2,3} \, {Z_y}^{(N2-1)} \,\Big] \, {Z_x}^2 \\ 

\,+\, \cdots \, \\

\,+\, \cdots \, \\

\,+\, \Big[ \, bb_{1,M2} \, + \, bb_{2,M2} \, Z_y \,+ \, bb_{3,M2} \, {Z_y}^2 \,+ \, \ldots \,+ \, bb_{N2,M2} \, {Z_y}^{(N2-1)} \,\Big] \, {Z_x}^{M2-1} \$$$] 



In the above

SeriesOrder20=N2;

SeriesOrder02=M2;







Above is the form of 2D Density in the matlab program below.



Here is the header of the program



[cc,EX] =SeriesProduct2DAlgorithmicNew(aa,bb,SeriesOrder10,SeriesOrder01,SeriesOrder20,SeriesOrder02)

or

[cc,EX] =SeriesProduct2DAlgorithmicNew(aa,bb,N1,M1,N2,M2)

We are multiplying 

X1(Zy,Zx) with X2(Zy,Zx)

to get 

X3(Zy,Zx)

X3(Zy,Zx) has dimensions

SeriesOrder30=N1+N2-1;

SeriesOrder03=M1+M2-1;

and result is represented as a 2D Z-series as



$X3(Z_y,Z_x)\, = \, cc_{1,1} \, + \, cc_{2,1} \, Z_y \,+ \, cc_{3,1} \, {Z_y}^2 \,+ \, \ldots \,+ \, cc_{N1+N2-1,1} \, {Z_y}^{(N1+N2-2)} \, \\ 

\,+\, \Big[ \, cc_{1,2} \, + \, cc_{2,2} \, Z_y \,+ \, cc_{3,2} \, {Z_y}^2 \,+ \, \ldots \,+ \, cc_{N1+N2-1,2} \, {Z_y}^{(N1+N2-2)} \,\Big] \, Z_x \\ 

\,+\, \Big[ \, cc_{1,3} \, + \, cc_{2,3} \, Z_y \,+ \, cc_{3,3} \, {Z_y}^2 \,+ \, \ldots \,+ \, cc_{N1+N2-1,3} \, {Z_y}^{(N1+N2-2)} \,\Big] \, {Z_x}^2 \\ 

\,+\, \cdots \, \\

\,+\, \cdots \, \\

\,+\, \Big[ \, cc_{1,M1+M2-1} \, + \, cc_{2,M1+M2-1} \, Z_y \,+ \, cc_{3,M1+M2-1} \, {Z_y}^2 \,+ \, \ldots \,+ \, cc_{N1+N2-1,M1+M2-1} \, {Z_y}^{(N1+N2-2)} \,\Big] \, {Z_x}^{M1+M2-2} \$$$] 





.

.

.

```
function [cc,EX] =SeriesProduct2DAlgorithmicNew(aa,bb,SeriesOrder10,SeriesOrder01,SeriesOrder20,SeriesOrder02)



SeriesOrder30=SeriesOrder10+SeriesOrder20-1; %Size of the first index of the product. applies to Coeffs cc
SeriesOrder03=SeriesOrder01+SeriesOrder02-1; %Size of the second index of the product. applies to Coeffs cc

cc(1:SeriesOrder30,1:SeriesOrder03)=0;

for nn1=1:SeriesOrder30
    if(nn1<=SeriesOrder10) %%%Check to make sure that first index of X1, given by Coeffs aa does not exceed valid range.
        nn3=nn1;
    else
        nn3=SeriesOrder10;
    end
    for nn2=1:SeriesOrder03 [size=85][font=monospace]%%%Check to make sure that second index of X1, given by Coeffs aa does not exceed valid range.[/font][/size]
        if(nn2<=SeriesOrder01)
            nn4=nn2;
        else
            nn4=SeriesOrder01;
        end    
        for jj1=1:nn3
            if(nn1-jj1+1 <=SeriesOrder20)[size=85][font=monospace]%%%Check to make sure that first index of X2, given by Coeffs bb does not exceed valid range.[/font][/size] 
                for jj2=1:nn4
                    if(nn2-jj2+1 <=SeriesOrder02)[size=85][font=monospace]%%%Check to make sure that second index of X2, given by Coeffs bb does not exceed valid range.[/font][/size]
                        cc(nn1,nn2)=cc(nn1,nn2)+aa(jj1,jj2).*bb(nn1-jj1+1,nn2-jj2+1);
                    end
                end
            end
        end
    end
end


[EZ] = EZZ2();


EX=0;
for nn1=1:SeriesOrder30
    for nn2=1:SeriesOrder03
        EX=EX+cc(nn1,nn2).*EZ(nn1).*EZ(nn2);
    end
end


end
```

.

.

.

```
function [EZ] = EZZ2()

EZ(1)=1;
EZ(2)=0;
EZ(3)=1;
for nn=4:64 %Increase for larger products.
    if rem(nn,2)==0
        EZ(nn)=0;
    else
        EZ(nn)=EZ(nn-2)*(nn-2);
        EZ(nn);
    end
end
% EZ(64)
% EZ(64).*EZ(64)

end


```

```

---

## Error 28: Unbalanced $$: 1

**Snippet:** `Friends, what I tried to show in previous post in 2D conditional Hermite-series `

**Full content:**

```
Friends, what I tried to show in previous post in 2D conditional Hermite-series framework can also be calculated directly within 2D conditional Z-series framework. Here I describe how to do that.



First we want to take a look at cross moments with first order in X2(Z1,Z2) and order one to N in random variable  X1(Z1). We know that by construction in our framework $Z_1$ and $Z_2$ and all their hermites are uncorrelated. So we see that 



$ \, E \big[{X_1(Z_1)}^n \, X_2(Z_1,Z_2) \, \big]\,=\,E^{Z_1} \Big[{X_1(Z_1)}^n \, E^{Z_2}\big[X_2(Z_1,Z_2)\big] \, \Big]\,$  Eq(1) 



So in order to calculate above cross moments, we can first find expectation of $X2(Z_1,Z_2)$ with respect to $Z_2$, and then later multiply with powers of X1 and then find expectation with respect to $Z_1$. We will use this observation in what follows.



We can write 2D conditional Z-series in expanded form as



$X2(Z_1 \, , \, Z_2)\,=\, b_{0,0} \, + \, b_{1,0} \,Z_1 \,+\, b_{2,0} \, {Z_1}^2 \,+\, \ldots \, + \, b_{N,0} \,{Z_1}^N\, \\

+\, \Big[ \, b_{0,1} \, + \, b_{1,1} \, Z_1 \,+\, b_{2,1} \, {Z_1}^2 \,+\, \ldots \, + \, b_{N,1} \,{Z_1}^N\, \Big] \, Z_2 \, \\

+\, \Big[ \, b_{0,2} \, + \, b_{1,2} \,Z_1 \,+\, b_{2,2} \, {Z_1}^2 \,+\, \ldots \, + \, b_{N,2} \, {Z_1}^N\, \Big] \, {Z_2}^2 \, \\

+\, \ldots \, \\

+\, \ldots \, \\

+\, \Big[ \, b_{0,M} \, + \, b_{1,M} \, Z_1 \,+\, b_{2,M} \, {Z_1}^2 \,+\, \ldots \, + \, b_{N,M} \,{Z_1}^N\, \Big] \, {Z_2}^M \, $  Eq(2)



Taking expectation of above $X2(Z_1,Z_2)$ with respect to  $Z_2$  we get 1D  Z-series form, we have



$E^{Z_2}\big[X2(Z_1,Z_2)\, \big]=\, b_{0,0} \, + \, b_{1,0} \,Z_1 \,+\, b_{2,0} \, {Z_1}^2 \,+\, \ldots \, + \, b_{N,0} \,{Z_1}^N\, \\



+\, \Big[ \, b_{0,2} \, + \, b_{1,2} \,Z_1 \,+\, b_{2,2} \, {Z_1}^2 \,+\, \ldots \, + \, b_{N,2} \, {Z_1}^N\, \Big] \, \, \\



+\,3\, \Big[ \, b_{0,4} \, + \, b_{1,4} \,Z_1 \,+\, b_{2,4} \, {Z_1}^2 \,+\, \ldots \, + \, b_{N,4} \, {Z_1}^N\, \Big] \, \, \\

+\, \ldots \, \\

+\, \ldots \, \\

+\,E[{Z_2}^M] \, \Big[ \, b_{0,M} \,+\, b_{2,M} \, \,+ \,3\, b_{4,M} \,\,+\, \ldots \,  \Big] \,  $  Eq(3)



 To simplify we introduce  new coefficient variables each for different powers of $Z_1$ that sums along the coefficients of even powers of $X_2$ as



$\, c_0 \, = \,\, b_{0,0} \,+ \, b_{0,2} \,+ 3 \, b_{0,4} \, + 15 \, b_{0,6} + \ldots $  

$\, c_1 \, = \,\, b_{1,0} \,+ \, b_{1,2} \,+ 3 \, b_{1,4} \, + 15 \, b_{1,6} + \ldots $  

$\, c_2 \, = \,\, b_{2,0} \,+ \, b_{2,2} \,+ 3 \, b_{2,4} \, + 15 \, b_{2,6} + \ldots $  

and so on till

$\, c_N \, = \,\, b_{N,0} \,+ \, b_{N,2} \,+ 3 \, b_{N,4} \, + 15 \, b_{N,6} + \ldots $  Eqs(4)



and then we substitute these coefficients from Eqs(4) into Eq(3) to get a simpler equation as



$E^{Z_2}\big[X2(Z_1,Z_2)\, \big]=\, c_{0} \, + \, c_{1} \,Z_1 \,+\, c_{2} \, {Z_1}^2 \,+\, \ldots \, + \, c_{N} \,{Z_1}^N\, \$$$]  Eq(5)



We want to use the above equation(5) by substituting it in the Eq(1) to get cross moments. We will have to multiply the univariate Z-series in Eq(5) with univariate Z-series of moments of $X_1(Z_1)$. I write Eq(1) here again



$ \, E \big[{X_1(Z_1)}^n \, X_2(Z_1,Z_2) \, \big]\,=\,E^{Z_1} \Big[{X_1(Z_1)}^n \, E^{Z_2}\big[X_2(Z_1,Z_2)\big] \, \Big]\,$  Eq(1) 



After multiplication with univariate Z-series of powers of $X_1(Z_1)$ whose all coefficients are already numerically known, each of the equation of product of   $E^{Z_2}\big[X2(Z_1,Z_2)\, \big]$ with Z-series of powers of  $X_1(Z_1)$ will result, after taking expectations with respect to $Z_1$, in a linear equation whose unknowns are  $c_n$ that were result of a simplification as in Eq(4).

So with N cross moments of X1 with first moment of X2 would result in N linear equations that can be solved with gaussian elimination or any other method to give us numerical values of coefficients in Eq(4). 

After solving these equations, we can fix the coefficients in first row of Eq(2) as

$\, b_{0,0} \, = \,c_0\,  \,-\big[ \, b_{0,2} \,+ 3 \, b_{0,4} \, + 15 \, b_{0,6} + \ldots \big] $  



$\, b_{1,0} \, = \,\, c_{1} \,- \big[ \, b_{1,2} \,+ 3 \, b_{1,4} \, + 15 \, b_{1,6} + \ldots \big]$  

$\, b_{2,0} \, = \,\, c_{2} \,-\big[ \, b_{2,2} \,+ 3 \, b_{2,4} \, + 15 \, b_{2,6} + \ldots \big] $  

and so on till

$\, b_{N,0} \, = \,\, c_{N} \,-\big[ \, b_{N,2} \,+ 3 \, b_{N,4} \, + 15 \, b_{N,6} + \ldots \big] $  Eqs(6)



I think the technique could be applied to higher cross moments but that will take more effort.
```

---

## Error 29: Unbalanced $$: 1

**Snippet:** `Friends, I am tentatively giving the expression for fourth power of dependent va`

**Full content:**

```
Friends, I am tentatively giving the expression for fourth power of dependent variable X. Now I will carefully check all coefficients and give all equations on the same page. And then hopefully think of some way to solve these equations.





We want to calculate $X(Z_y,Z_x)^4$ and then multiply it with powers of $Y(Z_y)$ to calculate cross moments of second power of X with various powers of Y.



After a bit of algebra and re-arranging terms, we get





$X2(Z_y \, , \, Z_x)^4\,= \Big[ {Bh_0}(Z_x)^4 + 6 {Bh_0}(Z_x)^2 {Bh_1}(Z_x)^2 + 3 {Bh_1}(Z_x)^4 + 24 {Bh_0}(Z_x)\,{Bh_1}(Z_x)^2 {Bh_2}(Z_x)\,+ 12 {Bh_0}(Z_x)^2 {Bh_2}(Z_x)^2 +\, \\

 60 {Bh_1}(Z_x)^2 {Bh_2}(Z_x)^2 + 32 {Bh_0}(Z_x)\,{Bh_2}(Z_x)^3 + 60 {Bh_2}(Z_x)^4 +\,

 24 {Bh_1}(Z_x)\,\,\big[{Bh_1}(Z_x)^2 + 6 {Bh_2}(Z_x)\,\,\big[{Bh_0}(Z_x)\,+ 4 {Bh_2}(Z_x))\,\,\big]{Bh_3}(Z_x)\,+\, \\

 36 ({Bh_0}(Z_x)^2 + 7 {Bh_1}(Z_x)^2 + 12 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 62 {Bh_2}(Z_x)^2)\,{Bh_3}(Z_x)^2 +\, \\

 1296 {Bh_1}(Z_x)\,{Bh_3}(Z_x)^3 + 3348 {Bh_3}(Z_x)^4 \, \Big] \\

+\Big[ \, 4 {Bh_1}(Z_x)\,\,\big[{Bh_0}(Z_x)^3 + 6 {Bh_0}(Z_x)^2 {Bh_2}(Z_x)\,+ 12 {Bh_1}(Z_x)^2 {Bh_2}(Z_x)\,+ 68 {Bh_2}(Z_x)^3 +\, \\

\,\,\, 3 {Bh_0}(Z_x)\,\,\big[{Bh_1}(Z_x)^2 + 10 {Bh_2}(Z_x)^2)\,\,\big]+\, \\

 72 ({Bh_0}(Z_x)^2 {Bh_2}(Z_x)\,+ 9 {Bh_1}(Z_x)^2 {Bh_2}(Z_x)\,+ 26 {Bh_2}(Z_x)^3 +\, \\

\,\,\,\,{Bh_0}(Z_x)\,\,\big[{Bh_1}(Z_x)^2 + 8 {Bh_2}(Z_x)^2)\,\,\big]{Bh_3}(Z_x)\,+ 72 {Bh_1}(Z_x)\,(7 {Bh_0}(Z_x)\,+ 68 {Bh_2}(Z_x)\,\,\big]{Bh_3}(Z_x)^2 +\, \\

 432 (3 {Bh_0}(Z_x)\,+ 37 {Bh_2}(Z_x)\,\,\big]{Bh_3}(Z_x)^3 \, \Big] \, H_1(Z_y)  \\

+\Big[ \,2 (3 {Bh_1}(Z_x)^4 + 2 {Bh_0}(Z_x)^3 {Bh_2}(Z_x)\,+ 54 {Bh_1}(Z_x)^3 {Bh_3}(Z_x)\,+\, \\

\,\, 102 {Bh_1}(Z_x)^2 ({Bh_2}(Z_x)^2 + 6 {Bh_3}(Z_x)^2)\,+\, 3 {Bh_0}(Z_x)^2 ({Bh_1}(Z_x)^2 + 4 {Bh_2}(Z_x)^2 \, \\

\, + 6 {Bh_1}(Z_x)\,{Bh_3}(Z_x)\,+ 18 {Bh_3}(Z_x)^2)\,+\, 6 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,(5 {Bh_1}(Z_x)^2 + 10 {Bh_2}(Z_x)^2 \, \\

\, + 48 {Bh_1}(Z_x)\,{Bh_3}(Z_x)\,+ 186 {Bh_3}(Z_x)^2)\,+\, 108 {Bh_1}(Z_x)\,(13 {Bh_2}(Z_x)^2 {Bh_3}(Z_x)\, \\

+ 37 {Bh_3}(Z_x)^3)\,+\,\, 4 (34 {Bh_2}(Z_x)^4 + 1665 {Bh_2}(Z_x)^2 {Bh_3}(Z_x)^2 + 2997 {Bh_3}(Z_x)^4)) \, \Big] \, H_2(Z_y)  \\

+\Big[ \, \,\, 4 ({Bh_0}(Z_x)^3 {Bh_3}(Z_x)\,+ 3 {Bh_0}(Z_x)^2 {Bh_2}(Z_x)\,\,\big[{Bh_1}(Z_x)\,+ 6 {Bh_3}(Z_x)\,\,\big]+\,

\,\,\,{Bh_2}(Z_x)\,(9 {Bh_1}(Z_x)^3 + 78 {Bh_1}(Z_x)\,{Bh_2}(Z_x)^2 + 204 {Bh_1}(Z_x)^2 {Bh_3}(Z_x)\, \\

+ 740 {Bh_2}(Z_x)^2 {Bh_3}(Z_x)\,+\,\,\, 1998 {Bh_1}(Z_x)\,{Bh_3}(Z_x)^2 + 7992 {Bh_3}(Z_x)^3)\,+\, \\

\,\,\,{Bh_0}(Z_x)\,\,\big[{Bh_1}(Z_x)^3 + 21 {Bh_1}(Z_x)^2 {Bh_3}(Z_x)\,+ 186 {Bh_3}(Z_x)\,\,\big[{Bh_2}(Z_x)^2 + 3 {Bh_3}(Z_x)^2)\,+\, \\

\,\,\,\,\, 6 {Bh_1}(Z_x)\,(4 {Bh_2}(Z_x)^2 + 27 {Bh_3}(Z_x)^2)))\, \Big] \, H_3(Z_y)  \\

+\Big[ \,\,\,{Bh_1}(Z_x)^4 + 48 {Bh_1}(Z_x)^3 {Bh_3}(Z_x)\,+ 6 {Bh_1}(Z_x)^2 (2 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 13 {Bh_2}(Z_x)^2 + 129 {Bh_3}(Z_x)^2)\,+\, \\

 12 {Bh_1}(Z_x)\,{Bh_3}(Z_x)\,\,\big[{Bh_0}(Z_x)^2 + 22 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 142 {Bh_2}(Z_x)^2 + 546 {Bh_3}(Z_x)^2)\,+\, \\

 6 ({Bh_2}(Z_x)^2 ({Bh_0}(Z_x)^2 + 8 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 26 {Bh_2}(Z_x)^2)\,+\, \\

\,\,\, 3 (3 {Bh_0}(Z_x)^2 + 80 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 592 {Bh_2}(Z_x)^2)\,{Bh_3}(Z_x)^2 + 3996 {Bh_3}(Z_x)^4) \, \Big] \, H_4(Z_y)  \\

+\Big[ \,\,\,\, 4 ({Bh_1}(Z_x)^3 {Bh_2}(Z_x)\,+ 3 {Bh_1}(Z_x)\,{Bh_2}(Z_x)^2 ({Bh_0}(Z_x)\,+ 6 {Bh_2}(Z_x)\,\,\big]+\,

\,\, 3 {Bh_1}(Z_x)^2 ({Bh_0}(Z_x)\,+ 17 {Bh_2}(Z_x)\,\,\big]{Bh_3}(Z_x)\,+\, \\

\,\, 3 {Bh_2}(Z_x)\,\,\big[{Bh_0}(Z_x)^2 + 16 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 88 {Bh_2}(Z_x)^2)\,{Bh_3}(Z_x)\,+\, \\

\,\, 9 {Bh_1}(Z_x)\,(5 {Bh_0}(Z_x)\,+ 82 {Bh_2}(Z_x)\,\,\big]{Bh_3}(Z_x)^2 + 36 (6 {Bh_0}(Z_x)\,+ 107 {Bh_2}(Z_x)\,\,\big]{Bh_3}(Z_x)^3) \, \Big] \, H_5(Z_y)  \\

+\Big[ \, \,\, 6 {Bh_1}(Z_x)^2 {Bh_2}(Z_x)^2 + 4 {Bh_2}(Z_x)^3 ({Bh_0}(Z_x)\,+ 6 {Bh_2}(Z_x)\,\,\big]+\, \\

 4 {Bh_1}(Z_x)\,\,\big[{Bh_1}(Z_x)^2 + 6 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 69 {Bh_2}(Z_x)^2)\,{Bh_3}(Z_x)\,+\, \\

 6 ({Bh_0}(Z_x)^2 + 22 {Bh_1}(Z_x)^2 + 42 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 428 {Bh_2}(Z_x)^2)\,{Bh_3}(Z_x)^2 +\,

 1620 {Bh_1}(Z_x)\,{Bh_3}(Z_x)^3 + 7704 {Bh_3}(Z_x)^4\, \Big] \, H_6(Z_y)  \\

+\Big[ \,  4 ({Bh_1}(Z_x)\,{Bh_2}(Z_x)^3 + 3 {Bh_2}(Z_x)\,\,\big[{Bh_1}(Z_x)^2 +\,{Bh_2}(Z_x)\,\,\big[{Bh_0}(Z_x)\,+ 10 {Bh_2}(Z_x))\,\,\big]{Bh_3}(Z_x)\,+\, \\

\,\, 3 {Bh_1}(Z_x)\,\,\big[{Bh_0}(Z_x)\,+ 29 {Bh_2}(Z_x)\,\,\big]{Bh_3}(Z_x)^2 + 9 (3 {Bh_0}(Z_x)\,+ 74 {Bh_2}(Z_x)\,\,\big]{Bh_3}(Z_x)^3)

\, \Big] \, H_7(Z_y)  \\

+\Big[ \,\,{Bh_2}(Z_x)^4 + 12 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,{Bh_3}(Z_x)^2 + 6 {Bh_2}(Z_x)^2 {Bh_3}(Z_x)\,(2 {Bh_1}(Z_x)\,+ 37 {Bh_3}(Z_x)\,\,\big]+\, \\

 3 {Bh_3}(Z_x)^2 (2 {Bh_1}(Z_x)^2 + 48 {Bh_1}(Z_x)\,{Bh_3}(Z_x)\,+ 333 {Bh_3}(Z_x)^2)\, \Big] \, H_8(Z_y)  \\

+\Big[ \, 4 {Bh_3}(Z_x)\,\,\big[{Bh_2}(Z_x)^3 +\,{Bh_0}(Z_x)\,{Bh_3}(Z_x)^2 + 3 {Bh_2}(Z_x)\,{Bh_3}(Z_x)\,\,\big[{Bh_1}(Z_x)\,+ 15 {Bh_3}(Z_x)))

\, \Big] \, H_9(Z_y)  \\

+\Big[ \,2 {Bh_3}(Z_x)^2 \, \big[\,3\, {Bh_2}(Z_x)^2 \,+\, {Bh_3}(Z_x) \, \big[ \,2\, {Bh_1}(Z_x)\, + \, 27\, {Bh_3}(Z_x)\, \big] \, \big]

\, \Big] \, H_{10}(Z_y)  \\

+\Big[ \, 4 {Bh_2}(Z_x)\,{Bh_3}(Z_x)^3 \, \Big] \, H_{11}(Z_y)  \\

+\Big[ \, {Bh_3}(Z_x)^4\, \Big] \, H_{12}(Z_y)  \$$$]
```

---

## Error 30: Unbalanced $$: 1

**Snippet:** `Friends, I could not work properly yesterday and the day before yesterday. I had`

**Full content:**

```
Friends, I could not work properly yesterday and the day before yesterday. I had to spend a lot of time in the bank to activate my dormant foreign currency account where I had some money deposited that I now need. Bank systems were not working properly and I continued to wait the day before yesterday for the system to get online but it did not work. Only yesterday, I was able to withdraw the money. 



I hope I will be able to work on full speed now to end the research project. 

I have carefully checked the previous equations and checked each coefficient very carefully. Earlier there were minor errors in some coefficients and I have fixed that by redoing all the calculations carefully. Here are the four powers of dependent variable X described in terms of the hermites. 

Each hermite polynomial in Z_y (including zeroth hermite) would give one equation for all of the following powers of X after solution of linear equations. And then we will get a lot of non-linear equations to solve but it seems that all the equations can be solved systematically. Later today, I will try to outline strategy to solve for the equations.



$X2(Z_y \, , \, Z_x)\,=\, {Bh_0}(Z_x)\,+\,{Bh_1}(Z_x)\, H_1(Z_y) \,+\,{Bh_2}(Z_x)\, H_2(Z_y) \,+\,{Bh_3}(Z_x)\, H_3(Z_y) \,$







$X2(Z_y \, , \, Z_x)^2\,= \Big[{Bh_0}^2(Z_x) \, +\, {Bh_1}^2(Z_x) \,+ 2 \, {Bh_2}^2(Z_x) \,+\, 6 \, {Bh_3}^2(Z_x) \,\Big] \, \\

\,+\, \Big[2\, {Bh_0}(Z_x) \,\, {Bh_1}(Z_x) \, +\,4\, {Bh_1}(Z_x) \,\, {Bh_2}(Z_x) \,+ 12 \, {Bh_2}(Z_x) \,\, {Bh_3}(Z_x) \,\Big] \, \, H_1(Z_y) \, \\

\,+\, \Big[ {Bh_1}^2(Z_x) \, +\,2\, {Bh_0}(Z_x) \,\, {Bh_2}(Z_x) \,+\, 4 \,{Bh_2}^2(Z_x) \, +  6 \, {Bh_1}(Z_x) \,\, {Bh_3}(Z_x) \,\,+\, 18 \,{Bh_3}^2(Z_x) \,\Big] \, \, H_2(Z_y) \, \\

\,+\, \Big[ \,2\, {Bh_1}(Z_x) \,\, {Bh_2}(Z_x) \,+ \, 2\, {Bh_0}(Z_x) \,\, {Bh_3}(Z_x) \,\,+\, 12 \,{Bh_2}(Z_x) \,\,{Bh_3}(Z_x) \,\Big] \, \, H_3(Z_y) \, \\

\,+\, \Big[ \, {Bh_2}^2(Z_x)  \,+ \,2\, {Bh_1}(Z_x) \,\, {Bh_3}(Z_x) \,\,+\, 9 \,{Bh_3}^2(Z_x) \,\Big] \, \, H_4(Z_y) \, \\

\,+\, \Big[ \,2\, {Bh_2}(Z_x) \, {Bh_3}(Z_x) \,\Big] \, \, H_5(Z_y) \, \\

\,+\, \Big[  {Bh_3}^2(Z_x) \,\,\Big] \, \, H_6(Z_y) \,$





$X2(Z_y \, , \, Z_x)^3\,= \Big[{Bh_0}(Z_x)^3 + 3 \, {Bh_0}(Z_x) \, \big[{Bh_1}(Z_x)^2 + 2 \,{Bh_2}(Z_x)^2 + 6\, {Bh_3}(Z_x)^2 \big] + \, \\

 2 \,{Bh_2}(Z_x)  \big[3\, {Bh_1}(Z_x)^2 + 4\, {Bh_2}(Z_x)^2 + 18\, {Bh_1}(Z_x) {Bh_3}(Z_x) + 54\, {Bh_3}(Z_x)^2 \big]\,\Big] \, \\

\,+\, \Big[\, 3\, \big[\, {Bh_0}(Z_x)^2 \,{Bh_1}(Z_x) + {Bh_1}(Z_x)^3 + 10 \,{Bh_1}(Z_x) \,{Bh_2}(Z_x)^2 \,+\, 6\, {Bh_1}(Z_x)^2 \,{Bh_3}(Z_x) \,+ \,48\, {Bh_2}(Z_x)^2\, {Bh_3}(Z_x)\, +\, \\

  42 \,{Bh_1}(Z_x)\, {Bh_3}(Z_x)^2 \,+ \,108 \,{Bh_3}(Z_x)^3\, +\, 4\, {Bh_0}(Z_x) \,{Bh_2}(Z_x) \,\big[{Bh_1}(Z_x) \,+ 3\, {Bh_3}(Z_x)\big] \,\big]\,\Big] \, \, H_1(Z_y)\, \\

\,+\, \Big[\,3\,\big[\, {Bh_0}(Z_x)^2 \,{Bh_2}(Z_x) \,+\, {Bh_0}(Z_x)\, \big[\,{Bh_1}(Z_x)^2 +\, 4\, {Bh_2}(Z_x)^2 \,+ 6\, {Bh_1}(Z_x)\, {Bh_3}(Z_x)\, + \,18 \,{Bh_3}(Z_x)^2 \, \big]\, +\, \\

   {Bh_2}(Z_x)\, \big[\,5 \,{Bh_1}(Z_x)^2 \,+\, 10\, {Bh_2}(Z_x)^2 \,+ \,48 \,{Bh_1}(Z_x)\, {Bh_3}(Z_x) \,+ \,186\, {Bh_3}(Z_x)^2\,\big]\,\big] \,\Big] \, \, H_2(Z_y) \, \\ 

\,+\, \Big[ \,{Bh_1}(Z_x)^3 \,+\, 21 \,{Bh_1}(Z_x)^2\, {Bh_3}(Z_x)\, + \,6 \,{Bh_1}(Z_x) \, \big[\,{Bh_0}(Z_x)\, {Bh_2}(Z_x) \,+ \,4\, {Bh_2}(Z_x)^2 \,+\, 27\, {Bh_3}(Z_x)^2 \,\big] \\+\, 3\, {Bh_3}(Z_x) \big[{Bh_0}(Z_x)^2 \,+ 12 \,{Bh_0}(Z_x)\, {Bh_2}(Z_x) \,+\, 62 \,\big[{Bh_2}(Z_x)^2 \,+ \,3\, {Bh_3}(Z_x)^2\,\big]\,\big] \,\Big] \, \, H_3(Z_y) \,\\

\,+\, \Big[ \, 3 \,\big[ \,{Bh_1}(Z_x)^2 \,{Bh_2}(Z_x) \,+ \,2 \,{Bh_1}(Z_x)\, \, {Bh_3}(Z_x)\, \big[\,{Bh_0}(Z_x) + \,11\, {Bh_2}(Z_x)\,\big] \,+\, {Bh_0}(Z_x) \,\big[{Bh_2}(Z_x)^2 \,+\, 9\, {Bh_3}(Z_x)^2\, \big] +  \\

   4 \,\big[{Bh_2}(Z_x)^3 \,+ \,30\, {Bh_2}(Z_x)\, {Bh_3}(Z_x)^2\,\big]\,\big] \,\Big] \, \, H_4(Z_y) \, \\

\,+\, \Big[ \,3\, \big[\,{Bh_1}(Zx)^2 \,{Bh_3}(Zx) \,+\, {Bh_1}(Zx) \,\big[{Bh_2}(Zx)^2 \,+ \,15\, {Bh_3}(Zx)^2 \,\big]\, + \\

   2 \,{Bh_3}(Zx)\, \big[\,{Bh_0}(Zx) {Bh_2}(Zx)\, +\, 8\, {Bh_2}(Zx)^2 \,+\, 36 \,{Bh_3}(Zx)^2 \,\big]\,\big] \,\Big] \, \, H_5(Z_y) \, \\

\,+\, \Big[ \, {Bh_2}(Zx)^3 \,+\, 3\, {Bh_0}(Zx)\, {Bh_3}(Zx)^2 \,+\, 3\, {Bh_2}(Zx)\, {Bh_3}(Zx) \,\big[\, 2 \,{Bh_1}(Zx) \,+\, 21 \,{Bh_3}(Zx)\, \big]\,\,\Big] \, \, H_6(Z_y) \, \\

\,+\, \Big[ \,3 \,{Bh_3}(Zx) \,\big[\, {Bh_2}(Zx)^2 \,+\, {Bh_3}(Zx) \,\big[\,{Bh_1}(Zx) \,+\, 9\, {Bh_3}(Zx)\,\big]\,\big]\,\,\Big] \, \, H_7(Z_y) \,\\

\,+\, \Big[\, 3\, {Bh_2}(Zx)\, {Bh_3}(Zx)^2\,\,\Big] \, \, H_8(Z_y) \,\\

 \,+\, \Big[\, {Bh_3}(Zx)^3\,\,\Big] \, \, H_9(Z_y) \,$







$X2(Z_y \, , \, Z_x)^4\,= \Big[ {Bh_0}(Z_x)^4 + 6 {Bh_0}(Z_x)^2 {Bh_1}(Z_x)^2 + 3 {Bh_1}(Z_x)^4 + 24 {Bh_0}(Z_x)\,{Bh_1}(Z_x)^2 {Bh_2}(Z_x)\,+ 12 {Bh_0}(Z_x)^2 {Bh_2}(Z_x)^2 +\, \\

 60 {Bh_1}(Z_x)^2 {Bh_2}(Z_x)^2 + 32 {Bh_0}(Z_x)\,{Bh_2}(Z_x)^3 + 60 {Bh_2}(Z_x)^4 +\,

 24 {Bh_1}(Z_x)\,{Bh_3}(Z_x)\,\,\big[{Bh_1}(Z_x)^2 + 6 {Bh_2}(Z_x)\,\big[{Bh_0}(Z_x)\,+ 4 {Bh_2}(Z_x)\,\big]\,\big]\,+\, \\

 \, 36\,{Bh_3}(Z_x)^2\, \big[\,{Bh_0}(Z_x)^2 + 7 {Bh_1}(Z_x)^2 + 12 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 62 {Bh_2}(Z_x)^2 \, \big] +\,1296\,  {Bh_1}(Z_x)\,{Bh_3}(Z_x)^3 \, +\,  3348 \, {Bh_3}(Z_x)^4 \, \Big] \\

+\Big[ \, 4 {Bh_1}(Z_x)\,\,\big[{Bh_0}(Z_x)^3 + 6 {Bh_0}(Z_x)^2 {Bh_2}(Z_x)\,+ 12 {Bh_1}(Z_x)^2 {Bh_2}(Z_x)\,+ 68 {Bh_2}(Z_x)^3 +\,

\,\,\, 3 {Bh_0}(Z_x)\,\,\big[{Bh_1}(Z_x)^2 + 10 {Bh_2}(Z_x)^2)\,\big]\,\big]+\, \\

 72\,{Bh_3}(Z_x)\, \big[\,{Bh_0}(Z_x)^2 \,{Bh_2}(Z_x)\,+ 9 {Bh_1}(Z_x)^2 \,{Bh_2}(Z_x)\,+ 26 \,{Bh_2}(Z_x)^3 +\,

\,\,\,\,{Bh_0}(Z_x)\,\,\big[{Bh_1}(Z_x)^2 + 8 {Bh_2}(Z_x)^2\, \big]\,\big] \\

+ 72 {Bh_1}(Z_x)\,{Bh_3}(Z_x)^2 \,\big[ \,7 \,{Bh_0}(Z_x)\,+ 68 {Bh_2}(Z_x)\,\,\big]+\,

 432 {Bh_3}(Z_x)^3 \, \big[\,3 \,{Bh_0}(Z_x)\,+ 37 \, {Bh_2}(Z_x)\,\,\big] \Big] \, H_1(Z_y)  \\

+\Big[ \,2 \big[\,3 \,{Bh_1}(Z_x)^4 \, +\,  2 \, {Bh_0}(Z_x)^3 \,  {Bh_2}(Z_x)\,+\, 54 \,{Bh_1}(Z_x)^3 {Bh_3}(Z_x)\,+\, 

\,\, 102 \, {Bh_1}(Z_x)^2 \, \big[\, {Bh_2}(Z_x)^2 \, +\,  6 \,{Bh_3}(Z_x)^2\,\big]\,+\, \\

 3 {Bh_0}(Z_x)^2 \, \big[\,{Bh_1}(Z_x)^2 + 4 {Bh_2}(Z_x)^2 \,\, + 6\,  {Bh_1}(Z_x)\,{Bh_3}(Z_x)\,+ 18 {Bh_3}(Z_x)^2 \, \big]\,+\,\\

 6 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,\big[\,5\, {Bh_1}(Z_x)^2 + 10 {Bh_2}(Z_x)^2 \, +\, 48 \, {Bh_1}(Z_x)\,{Bh_3}(Z_x)\,+ \, 186\,  {Bh_3}(Z_x)^2\, \big]\, +\, \\

108 {Bh_1}(Z_x)\,\big[\,13 \,{Bh_2}(Z_x)^2 {Bh_3}(Z_x)\,+\, 37\,  {Bh_3}(Z_x)^3\,\big]\,+\,\, 4 \, \big[\,34\,  {Bh_2}(Z_x)^4 \,+ \,1665 \, {Bh_2}(Z_x)^2 \, {Bh_3}(Z_x)^2 + \,2997\, {Bh_3}(Z_x)^4\, \big]\, \big]\, \Big] \, H_2(Z_y)  \\

+\Big[ \, \,\, 4 \, \big[\,{Bh_0}(Z_x)^3 \, {Bh_3}(Z_x)\,+\, 3 \,{Bh_0}(Z_x)^2\, {Bh_2}(Z_x)\,\,\big[{Bh_1}(Z_x)\,+ 6 {Bh_3}(Z_x)\,\,\big]+\,

\,\,\,{Bh_2}(Z_x)\,\big[\,9\, {Bh_1}(Z_x)^3 +\, \\ 78\, {Bh_1}(Z_x)\,{Bh_2}(Z_x)^2 \,+\, 204\, {Bh_1}(Z_x)^2 \, {Bh_3}(Z_x)\,

+ \,740\, {Bh_2}(Z_x)^2 \,{Bh_3}(Z_x)\,+\, 1998 \,{Bh_1}(Z_x)\,{Bh_3}(Z_x)^2 \,+ \,7992 \,{Bh_3}(Z_x)^3\,\big]\,+\, \\

\,{Bh_0}(Z_x)\,\big[\,{Bh_1}(Z_x)^3 \,+ \, 21\,  {Bh_1}(Z_x)^2 \, {Bh_3}(Z_x)\,+ \, 186\, {Bh_3}(Z_x)\,\big[{Bh_2}(Z_x)^2 \,+\, 3\, {Bh_3}(Z_x)^2\,\big]\,+\,

\, 6 \,{Bh_1}(Z_x)\,\big[\,4\, {Bh_2}(Z_x)^2 \,+\, 27\, {Bh_3}(Z_x)^2\,\big]\,\big]\,\big]\, \Big] \, H_3(Z_y)  \\

+\Big[ \,{Bh_1}(Z_x)^4 \,+\, 48 \,{Bh_1}(Z_x)^3 \,{Bh_3}(Z_x)\,+\, 6\, {Bh_1}(Z_x)^2 \,\big[2 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+\, 13\, {Bh_2}(Z_x)^2 \,+\, 129\, {Bh_3}(Z_x)^2\,\big]\,+\, \\

 12 {Bh_1}(Z_x)\,{Bh_3}(Z_x)\,\,\big[{Bh_0}(Z_x)^2 + \,22\, {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+\, 142\, {Bh_2}(Z_x)^2 \, +\, 546\, {Bh_3}(Z_x)^2\,\big]\,+\, \\

 \,6\,\big[\, {Bh_2}(Z_x)^2 \,\big[\,{Bh_0}(Z_x)^2 \,+\, 8 \,{Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 26\, {Bh_2}(Z_x)^2)\,+\,

\, 3\, \big[\,3\,\,{Bh_3}(Z_x)^2 \, {Bh_0}(Z_x)^2 + \,80\, {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+\, \\

 \,592 \,{Bh_2}(Z_x)^2\,\big] \,+\, 3996\, {Bh_3}(Z_x)^4\,\big] \, \Big] \, H_4(Z_y)  \\

+\Big[ \, 4 \, \big[\,{Bh_1}(Z_x)^3 {Bh_2}(Z_x)\,+ 3 {Bh_1}(Z_x)\,{Bh_2}(Z_x)^2 \,\big[\,{Bh_0}(Z_x)\,+\, 6\, {Bh_2}(Z_x)\,\,\big]+\,

\,\, 3 {Bh_1}(Z_x)^2 \,{Bh_3}(Z_x)\, \big[{Bh_0}(Z_x)\,+ 17 {Bh_2}(Z_x)\,\,\big]\,+\, \\

\,\, 3 {Bh_2}(Z_x)\,{Bh_3}(Z_x)\,\big[{Bh_0}(Z_x)^2 + 16 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 88 {Bh_2}(Z_x)^2\,\big]\,+\, \\

\,\, 9 {Bh_1}(Z_x)\,{Bh_3}(Z_x)^2 \,\big[\,5\, {Bh_0}(Z_x)\,+ 82 {Bh_2}(Z_x)\,\big]+\, 36\,{Bh_3}(Z_x)^3 \,\big[\,6\, {Bh_0}(Z_x)\,+\, 107\, {Bh_2}(Z_x)\,\big] \,\big]\, \Big] \, H_5(Z_y)  \\

+\Big[ \, \,\, 6 {Bh_1}(Z_x)^2 {Bh_2}(Z_x)^2 + 4 {Bh_2}(Z_x)^3 \,\big[\,{Bh_0}(Z_x)\,+ 6 {Bh_2}(Z_x)\,\,\big]+\, 

 4 \,{Bh_1}(Z_x)\,{Bh_3}(Z_x)\,\big[{Bh_1}(Z_x)^2 + 6 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ 69 {Bh_2}(Z_x)^2\, \big]\,+\, \\

 6\,{Bh_3}(Z_x)^2 \, \big[\,{Bh_0}(Z_x)^2 + \,22\, {Bh_1}(Z_x)^2 +\, 42\, {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,+ \,428 \,{Bh_2}(Z_x)^2\,\big]\,+\,

 1620 {Bh_1}(Z_x)\,{Bh_3}(Z_x)^3 + 7704 {Bh_3}(Z_x)^4\, \Big] \, H_6(Z_y)  \\

+\Big[ \,  4 \big[\,{Bh_1}(Z_x)\,{Bh_2}(Z_x)^3 + 3 {Bh_2}(Z_x)\,{Bh_3}(Z_x)\,\big[{Bh_1}(Z_x)^2 +\,{Bh_2}(Z_x)\,\big[{Bh_0}(Z_x)\,+ 10 {Bh_2}(Z_x)\,\big]\,\big]\,+\, \\

\, 3\, {Bh_1}(Z_x)\,{Bh_3}(Z_x)^2\,\big[{Bh_0}(Z_x)\,+ 29 {Bh_2}(Z_x)\,\,\big] + 9 \,{Bh_3}(Z_x)^3\,\big[\,3\, {Bh_0}(Z_x)\,+ 74 {Bh_2}(Z_x)\,\,\big] \, \big]

\, \Big] \, H_7(Z_y)  \\

+\Big[ \,\,{Bh_2}(Z_x)^4 + 12 {Bh_0}(Z_x)\,{Bh_2}(Z_x)\,{Bh_3}(Z_x)^2 + 6 {Bh_2}(Z_x)^2 {Bh_3}(Z_x)\,\big[\,2\, {Bh_1}(Z_x)\,+ \,37\, {Bh_3}(Z_x)\,\big]+\, \\

 3 {Bh_3}(Z_x)^2\, \big[\,2\, {Bh_1}(Z_x)^2 \,+\, 48 {Bh_1}(Z_x)\,{Bh_3}(Z_x)\,+\, 333\, {Bh_3}(Z_x)^2\,\big]\, \Big] \, H_8(Z_y)  \\

+\Big[ \, 4 {Bh_3}(Z_x)\,\,\big[{Bh_2}(Z_x)^3 +\,{Bh_0}(Z_x)\,{Bh_3}(Z_x)^2 + 3 {Bh_2}(Z_x)\,{Bh_3}(Z_x)\,\,\big[{Bh_1}(Z_x)\,+ 15 {Bh_3}(Z_x)\,\big]\,\big]

\, \Big] \, H_9(Z_y)  \\

+\Big[ \,2 {Bh_3}(Z_x)^2 \, \big[\,3\, {Bh_2}(Z_x)^2 \,+\, {Bh_3}(Z_x) \, \big[ \,2\, {Bh_1}(Z_x)\, + \, 27\, {Bh_3}(Z_x)\, \big] \, \big]

\, \Big] \, H_{10}(Z_y)  \\

+\Big[ \, 4 {Bh_2}(Z_x)\,{Bh_3}(Z_x)^3 \, \Big] \, H_{11}(Z_y)  \\

+\Big[ \, {Bh_3}(Z_x)^4\, \Big] \, H_{12}(Z_y)  \$$$]
```

---

## Error 31: Unbalanced $: 1

**Snippet:** `Friends, I am posting a very preliminary version of the main function that optim`

**Full content:**

```
Friends, I am posting a very preliminary version of the main function that optimizes. It has several errors. For many idisosyncratic cases, parameters, loops count, loops order and many other things have to be tweaked. I still have not done the part that perfectly fixes the first column and first row and I am resorting to keeping that constant at ad-hoc calculated values and then running optimization there at the very end. This function will change in many ways but I am still posting it to keep friends in touch.

This is a different version of the function I used yesterday.

Summary of some major changes.



1. I keep objective function analytic.



Here is the objective function I used for graphs yesterday. w2D are weights for cross moments in squared difference of model and target cross moments.



w2D(1:NMomentsY,1:NMomentsX)=1;

for nn=NMomentsY-1 : -1 : 1

    for mm=NMomentsX-1 : -1 : 1

        w2D(nn,mm)=w2D(nn+1,mm+1)*(nn+1).^2*(mm+1).^2.0;

    end

end



Please feel free to use non-integer powers if you want to experiment but better to keep objective function in an analytic form.



2. I used a multiplicative iterative optimization in addition to additive iterative optimization that seems to work very well.



additive optimization is simply updated element-wise a single coefficient at a time as

bnmHCoeffNew(kk,jj)=bnmHCoeff(kk,jj)+delta_bnmHCoeff(kk,jj);



while  multiplicative optimization is multiplied to one entire column and one entire row at a time with weights proportional to their powers of standard deviations as

bnmHCoeffNew(kk,2:6)=bnmHCoeff(kk,2:6).*(1+delta_bnmHCoeff1(kk,2:6));



weights along rows are 

delta_bnmHCoeff1(1:SeriesOrderIter10,mm)=.005.*XmVar.^((mm)/2);

while weights along columns are

delta_bnmHCoeff2(nn,1:SeriesOrderIter01)=.005.*YmVar.^((nn)/2)



In yesterday's graphs, I did not use any multiplicative optimization. I simply used iterative optimization and in second last batch of 500 iterative optimizations, I allowed optimization of first column and in last batch of 500 iterated optimizations, I also allowed optimization of first column.



Mean during optimization cannot be changed from zero for since optimization is done on standardized data. This was not previously properly taken into account in optimization and was fixed at the end after optimization.



There are other small changes. One year and two year with the same parameters that I had in last matlab program can be priced well. I did not check three years and four years. Five years were not working and had problems but I am sure we will soon fix them.



Here is the latest program for reference and it will undergo many more changes in coming days. I am posting the appropriate function only that does optimization.



.

.


```
function [bnm,aa] = CalculateConditionalProbabilitiesYtoXLinearRegression04IterB(Yin,Xin)

%Yin argument translates to independent random variable Y
%Xin argument translates to dependent variable X.
%This function takes observations of an independent variable Y and
%dependent varaible X. These have to be joint observations in the sense
%that nth observation of Y, given by Y(n) is taken jointly with nth
%observation of X, given by X(n). Two arrays of observations are the same
%length and nth mmber of independent variable Y is jointly observed with nth
%member of depedent variable X.
%We want to find the detailed relationship between Y and X so we can get
%the conditional density of dependent variable X given a particular value
%of independent variable Y. This will be done by calibrating coefficients
%of our 2D hermite series to data so that a very good fit to cross moments
%between X and Y is retrieved.
%We will first find univariate Z-series/hermite series of both random
%variables independently. For joint dynamics of dependent variable given 
%te independnet variable, we will assume a 2D hermite series (This has to 
%be two dimensional to be able to capture the dynamics from independent variable Y
%and have its own dynamics) and form but we do not know the coefficients of 
%this 2D hermite series. In this program, we try to use iterative optimization 
%to find the unknown coefficients of 2D hermite series of dependent variable X 
%in a way that after taking products with independent varaible Y, expectation   
%of these products i.e cross moments are as exactly retrieved as possible.
%Our iterative optimization procedure perturbs each hermite coefficient in 
%2D hermite series  by a very slight amount and checks the objective function.
%If the objective function decreases, we eccept the perturbation otherwise
%reject it and then perturb by a small amount in other opposite direction
%and then again check the objective function. If perturbations in both sides 
%are rejected, we do not change the coefficients but slightly decrease the
%perturbation size. 
%We will first standardize the data of both random variables and then
%calculate univariate hermite series of both variables and also their 
%cross moments in standardized form. We do all the calculations of coefficients
%of independent variable Y and 2D dependent variable X
%in standardized version of variables and moments. After optimization of coefficents on 
%standardized data, at the end, we invert the standardization of both 
%dependent and independent variables appropriately to get the Z-series and
%hermite series of actual varaibles in theri original coordinates back from
%standardized coordinates.
%Before optimization, we place two conditions on 2D dependent variable X so that
%first row and first column of 2D hermite coefficents of X is already
%known before optimization stage and it is not changed in optimization. 
%We do not iteratively optimize over this first row and first colums
%which are analytically known from these two conditions.
%Our first condition is that after integration (of bivaraite density or
%alternatively bivaraite 2D Z-series/2D Hermite series) over independent
%variable, we should get the univaraite marginal density/Z-series/Hermite series of X
%which has already been calculated out of data. This fixes the zeroth
%hermite(of independent varaible Y) related terms in the Z-series/hermite series. 
%Please look at this forum post# 2121 for explanation of this first condition.
% https://forum.wilmott.com/viewtopic.php?t=99702&start=2115#p879042

%We can analytically solve for first order cross moments of X with higher
%order in Y. From the analytical solution of these moments, we find first
%row of coefficents in the hermite form.


% 2D Hermite Series Form used in this program is given as
% 
% X = bnmH(1,1) + bnmH(2,1) H_1(Z_y) + bnmH(3,1) H_2(Z_y) + bnmH(4,1) H_3(Z_y) + bnmH(5,1) H_4(Z_y) + bnmH(6,1) H_5(Z_y) 
% + [ bnmH(1,2) + bnmH(2,2) H_1(Z_y) + bnmH(3,2) H_2(Z_y) + bnmH(4,2) H_3(Z_y) + bnmH(5,2) H_4(Z_y) + bnmH(6,2) H_5(Z_y)] H_1(Zx) 
% + [ bnmH(1,3) + bnmH(2,3) H_1(Z_y) + bnmH(3,3) H_2(Z_y) + bnmH(4,3) H_3(Z_y) + bnmH(5,3) H_4(Z_y) + bnmH(6,3) H_5(Z_y)] H_2(Zx)
% + [ bnmH(1,4) + bnmH(2,4) H_1(Z_y) + bnmH(3,4) H_2(Z_y) + bnmH(4,4) H_3(Z_y) + bnmH(5,4) H_4(Z_y) + bnmH(6,4) H_5(Z_y)] H_3(Zx)
% + [ bnmH(1,5) + bnmH(2,5) H_1(Z_y) + bnmH(3,5) H_2(Z_y) + bnmH(4,5) H_3(Z_y) + bnmH(5,5) H_4(Z_y) + bnmH(6,5) H_5(Z_y)] H_4(Zx)
% + [ bnmH(1,6) + bnmH(2,6) H_1(Z_y) + bnmH(3,6) H_2(Z_y) + bnmH(4,6) H_3(Z_y) + bnmH(5,6) H_4(Z_y) + bnmH(6,6) H_5(Z_y)] H_5(Zx)
 
% 2D Z-Series Form used in this program is given as
% 
% X = bnm(1,1) + bnm(2,1) Z_y + bnm(3,1) (Z_y)^2 + bnm(4,1) (Z_y)^3 + bnm(5,1) (Z_y)^4 + bnm(6,1) (Z_y)^5 
% + [ bnm(1,2) + bnm(2,2) Z_y + bnm(3,2) (Z_y)^2 + bnm(4,2) (Z_y)^3 + bnm(5,2) (Z_y)^4 + bnm(6,2) (Z_y)^5 ] Zx 
% + [ bnm(1,3) + bnm(2,2) Z_y + bnm(3,3) (Z_y)^2 + bnm(4,3) (Z_y)^3 + bnm(5,3) (Z_y)^4 + bnm(6,3) (Z_y)^5 ] Zx^2 
% + [ bnm(1,4) + bnm(2,2) Z_y + bnm(3,4) (Z_y)^2 + bnm(4,4) (Z_y)^3 + bnm(5,4) (Z_y)^4 + bnm(6,4) (Z_y)^5 ] Zx^3 
% + [ bnm(1,5) + bnm(2,2) Z_y + bnm(3,5) (Z_y)^2 + bnm(4,5) (Z_y)^3 + bnm(5,5) (Z_y)^4 + bnm(6,5) (Z_y)^5 ] Zx^4 
% + [ bnm(1,6) + bnm(2,2) Z_y + bnm(3,6) (Z_y)^2 + bnm(4,6) (Z_y)^3 + bnm(5,6) (Z_y)^4 + bnm(6,6) (Z_y)^5 ] Zx^5




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%In the code block below, we standardize the independent variable Y and dependent variable X.
%We do all later calculations of various Z-series and cross moments in 
%standardized framework and then at the end of the program, we convert 
%the calculated coefficients of 2D hermite series/Z-series of dependent 
%variable X into original non-standardized framework.

 Ndata=length(Yin);
 
 MeanY=sum(Yin(1:Ndata))/Ndata;
 MeanX=sum(Xin(1:Ndata))/Ndata;
 
 Ym(1:Ndata)=Yin(1:Ndata)-MeanY;
 Xm(1:Ndata)=Xin(1:Ndata)-MeanX;
 
 YmVar=sum(Ym(1:Ndata).^2)/Ndata;
 XmVar=sum(Xm(1:Ndata).^2)/Ndata;
 
 Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);
 X(1:Ndata)=Xm(1:Ndata)/sqrt(XmVar);

 
 sqrt(YmVar)
 sqrt(XmVar)
 
 str=input("Look at standardization constants");
 

 NMomentsY=6;
 NMomentsX=6;
     for nn=1:NMomentsY
        for mm=1:NMomentsX
            CrossMoments11(nn,mm)=0;
            for pp=1:Ndata
               CrossMoments11(nn,mm)=CrossMoments11(nn,mm)+Yin(pp).^nn.*Xin(pp).^mm/Ndata;
               %CrossMoments11(nn,mm)=CrossMoments11(nn,mm)+Y(pp).^nn.*X(pp).^mm/Ndata;
               %CrossMoments11(nn,mm)=CrossMoments11(nn,mm)+Ym(pp).^nn.*Xm(pp).^mm/Ndata;
            end
        end
     end
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Code block below uses polynomial regression to find univariate Z-series 
%coefficients of independent variable Y.
%To know more about polynomial regression read the following and associated
%posts:  https://forum.wilmott.com/viewtopic.php?t=99702&start=2010#p877143
 
%You can get the text file MomentMatchParams08.txt from the forum post below
%https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=2040#p877863

Mtable=readtable('C:\Users\Lenovo\Documents\MATLAB\MATLAB1\MomentMatchParams08.txt');

%ZI is moment matched grid along the normal density with number of grid
%points equal to data elements in Y given by Ndata. The grid is constructed
%so that probability mass in each grid cell is 1/Ndata so this matches the
%observation probability of Ndata data elements. Due to equal probability
%mass in each grid cell, we call it equiprobable grid.

[ZI] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable);

Ys=sort(Y);
Ymu(1:Ndata,1)=Ys(1:Ndata);

W(1:Ndata,1)=1;
W(1:Ndata,2)=ZI(1:Ndata);
W(1:Ndata,3)=ZI(1:Ndata).^2;
W(1:Ndata,4)=ZI(1:Ndata).^3;
W(1:Ndata,5)=ZI(1:Ndata).^4;
W(1:Ndata,6)=ZI(1:Ndata).^5;
% W(1:Ndata,7)=ZI(1:Ndata).^6;
% W(1:Ndata,8)=ZI(1:Ndata).^7;


coeff=inv(W'*W)*(W'*Ymu);

%Above, we get coefficients of univariate Z-series of independent
%variable Y by least square regression.


a0=coeff(1,1);
a(1:5)=coeff(2:6,1);

%Above, we assign zeroth power Z-series coefficient to a0 and rest of
%the coefficients to array a.
%This was older format but we might need it since many old functions are written 
%in this format.

%Below, we assign same Z-series coefficients to a single array. This is
%newer format that we want to use mostly.
aa(1:6)=coeff(1:6);


%uncomment these lines if you want to see shape of Z-series constructed
%density of Y. We had calculated coefficients of this Z-series by
%least square polynomial regression.
%PlotZSeriesDensity(a0,a,'r')
%str=input("Look at the density of volatility");
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5    
%In this code block, we calcualate the coefficients of univariate marginal
%density of dependent variable X again by least square polynomial
%regression as we did in previous block for independent variable Y.
    
Xs=sort(X);
Xmu(1:Ndata,1)=Xs(1:Ndata);

W(1:Ndata,1)=1;
W(1:Ndata,2)=ZI(1:Ndata);
W(1:Ndata,3)=ZI(1:Ndata).^2;
W(1:Ndata,4)=ZI(1:Ndata).^3;
W(1:Ndata,5)=ZI(1:Ndata).^4;
W(1:Ndata,6)=ZI(1:Ndata).^5;

coeff=inv(W'*W)*(W'*Xmu);

c0=coeff(1,1);
c(1:5)=coeff(2:6,1);

cc(1:6)=coeff(1:6,1);

[ccH] = ConvertZSeriesToHermiteSeriesNew(cc,5);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Zy= CalculateZgivenXAndZSeriesC5Improved(Y,a0,a);

[Xs,I]=sort(X);

Zys=Zy(I);

Zx=ZI;

Xmu(1:Ndata,1)=Xs(1:Ndata);


W=0;

W(1:Ndata,1)=1.0;
W(1:Ndata,2)=Zx(1:Ndata);
W(1:Ndata,3)=(Zx(1:Ndata).^2-1);
W(1:Ndata,4)=(Zx(1:Ndata).^3-3*Zx(1:Ndata));
W(1:Ndata,5)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3);
W(1:Ndata,6)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata));

W(1:Ndata,7)=1.*Zys(1:Ndata);
W(1:Ndata,8)=Zx(1:Ndata).*Zys(1:Ndata);
W(1:Ndata,9)=(Zx(1:Ndata).^2-1).*Zys(1:Ndata);
W(1:Ndata,10)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*Zys(1:Ndata);
W(1:Ndata,11)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*Zys(1:Ndata);
W(1:Ndata,12)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata)).*Zys(1:Ndata);

W(1:Ndata,13)=(Zys(1:Ndata).^2-1);
W(1:Ndata,14)=Zx(1:Ndata).*(Zys(1:Ndata).^2-1);
W(1:Ndata,15)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^2-1);
W(1:Ndata,16)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^2-1);
W(1:Ndata,17)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^2-1);
W(1:Ndata,18)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata)).*(Zys(1:Ndata).^2-1);

W(1:Ndata,19)=(Zys(1:Ndata).^3-3*Zy(1:Ndata));
W(1:Ndata,20)=Zx(1:Ndata).*(Zys(1:Ndata).^3-3*Zy(1:Ndata));
W(1:Ndata,21)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^3-3*Zy(1:Ndata));
W(1:Ndata,22)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));
W(1:Ndata,23)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));
W(1:Ndata,24)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata)).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));

W(1:Ndata,25)=(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
W(1:Ndata,26)=Zx(1:Ndata).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
W(1:Ndata,27)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
W(1:Ndata,28)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
W(1:Ndata,29)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
W(1:Ndata,30)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata)).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);

W(1:Ndata,31)=(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
W(1:Ndata,32)=Zx(1:Ndata).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
W(1:Ndata,33)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
W(1:Ndata,34)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
W(1:Ndata,35)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
W(1:Ndata,36)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata)).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));

coeff=inv(W'*W)*(W'*Xmu);


bnmH0(1,1:6)=ccH(1:6);  %Replace first line of X-hermites with Marginal density retrieval condition
bnmH0(2,1:6)=coeff(7:12);
bnmH0(3,1:6)=coeff(13:18);
bnmH0(4,1:6)=coeff(19:24);
bnmH0(5,1:6)=coeff(25:30);
bnmH0(6,1:6)=coeff(31:36);

bnmH=bnmH0;





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


SeriesOrder1=6;
NMomentsY=6;


SeriesOrder10=6; %SeriesOrder10 = 1 + highest power of Zy in 2D Z-series%Here highest power of Zy is five 
SeriesOrder01=6; %SeriesOrder01 = 1 + highest power of Zx in 2D Z-series%Here highest power of Zx is also five
%notation is  bnm(1:SeriesOrder10,1:SeriesOrder01)
%Similalry    bnmH(1:SeriesOrder10,1:SeriesOrder01)
 
NMomentsX=6; %Highest moment of X in cross moments of X and Y
NMomentsY=6; %Highest moment of Y in cross moments of X and Y

%Below we calculate various cross moments between X and Y. These are
%calculated from standardized data.
for nn=1:NMomentsY
   for mm=1:NMomentsX
       CrossMoments(nn,mm)=0;
       for pp=1:Ndata
          CrossMoments(nn,mm)=CrossMoments(nn,mm)+Y(pp).^nn.*X(pp).^mm/Ndata;
       end
   end
end
    
    
%Below are the weights on calculation of objective function. More weight on
%a particular moment means that its better match with target moments gets more emphasized as
%compared to match of other moments.
%Choice of good weights is non-trivial.
%Current choice is only haphazard. Please try improvements/
    
    
 w2D(1:NMomentsY,1:NMomentsX)=1;
for nn=NMomentsY-1:-1:1
    for mm=NMomentsX-1:-1:1
        %w2D(nn,mm)=w2D(nn+1,mm+1)*(nn+1)*(mm+1);
        w2D(nn,mm)=w2D(nn+1,mm+1)*(nn+1).^2*(mm+1).^2.0;
    end
end

% w2D(:,1)=w2D(:,1)*100000000;
% w2D(1,:)=w2D(1,:)*100000000;
% w2D(:,2)=w2D(:,2)*500000;
% w2D(2,:)=w2D(2,:)*500000;
% w2D(1,2)=w2D(1,2)*100;
% w2D(2,2)=w2D(2,2)*10;
% w2D(3,2)=w2D(3,2)*5;
% w2D(:,3)=w2D(:,3)*100000;
% w2D(1,3)=w2D(1,3)*20;
% w2D(2,3)=w2D(2,3)*5;
% w2D(1,:)=w2D(1,:)*10000;
% w2D(2,:)=w2D(2,:)*100;
% w2D(3,:)=w2D(3,:)*10;
% w2D(:,4)=w2D(:,4)*10000;
% w2D(1,4)=w2D(1,4)*10;
% w2D(2,4)=w2D(2,4)*2;
% w2D(:,5)=w2D(:,5)*1000;  
% w2D(:,6)=w2D(:,6)*20;  

%Please look on detailed comments inside function below for more insight about it.
%The function below returns coefficients on first row of hermite series so that all
%cross moments of first order in dependent variable X and various orders in independent
%variable Y are matched.

[ddH] = ProduceFirstRowofConditioal2DZSeries02_6M_A(aa,SeriesOrder1,CrossMoments);

%Below we define a 2D array of hermite series coefficents and populate its
%first row with output from above function so that all cross moments of
%first order in X and different orders in Y are matched.
%We also populate first column with univariate hermite coefficients of 
%marginal density of X because of the condition that upon integration of
%the bivariate hermite form, we should get univariate marginal density as a
%result. %Please look at this forum post# 2121 for explanation of this first condition.
% https://forum.wilmott.com/viewtopic.php?t=99702&start=2115#p879042

% 
% %%%%%%%%%%%%%%%%%%%%%%%%%5
% 
ccH0=ccH;

for nn=2:6
    %ccH(nn)=sign(ccH(nn)-dd(nn)).*sqrt(abs(sign(ccH(nn)).*ccH(nn).^2-sign(dd(nn)).*dd(nn).^2));
    if(abs(ccH(nn))>abs(ddH(nn)))
        ccH(nn)=sign(ccH(nn)).*sqrt(ccH(nn).^2-ddH(nn).^2);
    else
    
        ccH(nn)=0;
    end 
end

% %[ccH1] = SubtractZSeriesRVsByMonteCarlo(ccH0,ddH);
% 
% %[ccH2] = SubtractDensity(ccH0,ddH)
% 
% 
% %ddH
% 
% %ccH0
% 
% ccH
% 
% %ccH1
% 
% %ccH2
% %str=input("Look at comparison of ccH");
% 
  bnmH(1,1:6)=ccH(1:6);     %populate first column with univariate margianl density hermite coefficients of X.
% % %bnmH(1,1)=MeanX;
  bnmH(1:6,1)=ddH(1:6);      %populate first row so that all cross moments of first order in X are matched.
  bnmH(1,1)=0;
% % % 
% %%%%%%%%%%%%%%%%%%%%%%%5

% [Zy] = CalculateZgivenXAndZSeriesC5Improved(Y,a0,a);
% [Zx] = CalculateZgivenXAndZSeriesC5Improved(X,c0,c);
% 
 paths=Ndata;
 [CorrH0] = CalculateCorrelationBivariateHermiteCH(Zx,Zy,paths,5);
% 
% bnmH(1,1)=ddH(1);
% bnmH(1,2)=sqrt(1-CorrH0(1).^2).*ccH(2);
% bnmH(1,3)=sqrt(1-CorrH0(2).^2).*ccH(3);
% bnmH(1,4)=sqrt(1-CorrH0(3).^2).*ccH(4);
% bnmH(1,5)=sqrt(1-CorrH0(4).^2).*ccH(5);
% bnmH(1,6)=sqrt(1-CorrH0(5).^2).*ccH(6);
% 
% bnmH(2,1)=CorrH0(1).*ccH(2);
% bnmH(3,1)=CorrH0(2).*ccH(3);
% bnmH(4,1)=CorrH0(3).*ccH(4);
% bnmH(5,1)=CorrH0(4).*ccH(5);
% bnmH(6,1)=CorrH0(5).*ccH(6);
% 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%In our iterative optimization, we will not alter the above first column and first row of 2D hermite coefficients array.


%In the block below, we convert 2D hermite coefficients array bnmH to 2D
%Z-series array bnm. We calculate the values of cross moments given the values of 
%coefficients in 2D Z-series bnm. We use these model cross moments and
%co1mpare them with target cross moments to evaluate the objective function.

%Convert from 2D Hermite Series Coefficients bnmH to 2D Z-series
%coefficients bnm
[bnm] = Convert2DHermitesInto2DSeries(bnmH);
%Evaluate the model cross moments in the function below.
[Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%Evaluate the objective function based on weighted squared difference
%between model cross moments and target cross momensts from data.
[ObjFuncBest] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
    %%%%%%%%%%%%%%%%

SeriesOrderIter10=6;
SeriesOrderIter01=6;
alphaSuccessCount(1:SeriesOrderIter10,1:SeriesOrderIter01)=0;
SuccessPrevalpha(1:SeriesOrderIter10,1:SeriesOrderIter01)=0;


%array of perturbation sizes of coefficients of the 2D Hermite form 
%of dependent variable X in iterative optimization.
for nn=1:SeriesOrderIter10
    for mm=1:SeriesOrderIter01
%         if(bnmH(nn,mm)~=0)
%             delta_bnmHCoeff(nn,mm)=bnmH(nn,mm)./50;
%             if((mm>1)&&(nn>1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*CorrH0(nn-1).*sqrt(1-CorrH0(mm-1).^2);
%             end
%             if((mm==1)&&(nn==1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2);
%             end
%             if((mm>1)&&(nn==1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*sqrt(1-CorrH0(mm-1).^2);
%             end
%             if((mm==1)&&(nn>1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*CorrH0(nn-1);
%             end
%         else
%             delta_bnmHCoeff(nn,mm)=.0000025;
%         end
        
        if(bnmH(nn,mm)~=0)
            delta_bnmHCoeff(nn,mm)=bnmH(nn,mm)./50;
            if((mm>1)&&(nn>1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*YmVar.^((nn)/2);%.*CorrH0(nn-1);
            end
            if((mm==1)&&(nn==1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*YmVar.^((nn)/2);
            end
            if((mm>1)&&(nn==1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*YmVar.^((nn)/2);
            end
            if((mm==1)&&(nn>1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*YmVar.^((nn)/2);%.*CorrH0(nn-1);
            end
        else
            delta_bnmHCoeff(nn,mm)=.0000025;
        end
    end    
end

%Assign initial value of bnmH to workhorse variable bnmHCoeff which will be
%used in iterative ioptimization

%load("bnmHFile02.mat","bnmH");

bnmHCoeff=bnmH;

mul1=.9; %decrease the perturbation step size by multiplying it with .9 when 
%objective function does not decrease upon perturbation on both sides.  
mul2=1.1; %Increase the perturbation step size after several successive 
%successes in decreasing the objective function
Iterations=000;
MM1=2;
NN1=2;
MM2=2
NN2=2;

KK1=2;
JJ1=2;
for iter=1:Iterations
iter
bnmHCoeff
ObjFuncBest

%Below we run a two dimensional loop that loops over all rows and columns
%of 2D array of hermite series coefficients. However, we exclude first row
%and first column from this optimization as values there were already fixed
%analytically.


%     for kk=NN1:MM1 %SeriesOrderIter10 %Optimize over Zy hermites.
%         for jj=NN2:MM2 %Optimize over Zx hermites
%             if(iter>500)
%                 NN1=2;
%                 MM1=3;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             if(iter>1000)
%                 NN1=2;
%                 MM2=SeriesOrderIter10;
%                 NN2=2;
%                 MM2=3;
%                 
%             end
%             if(iter>1500)
%                 NN1=2;
%                 MM1=4;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             if(iter>2000)
%                 NN1=2;
%                 MM1=SeriesOrderIter10;
%                 NN2=2;
%                 MM2=4;
%             end
%             if(iter>2500)
%                 NN1=2;
%                 MM1=5;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             
%             if(iter>3000)
%                 NN1=2;
%                 MM1=SeriesOrderIter01;
%                 NN2=2;
%                 MM2=6;
%             end
%         
%             if(iter>3500)
%                 NN1=2;
%                 MM1=SeriesOrderIter01;
%                 NN2=1;
%                 MM2=6;
%             end
%             if(iter>4000)
%                 NN1=1;
%                 MM1=SeriesOrderIter01;
%                 NN2=1;
%                 MM2=6;
%             end
            
%             if(rem(iter,1002)==0)
%                 for nn=2:6
%                     bnmHCoeff(nn,2)=bnmHCoeff(nn,2).*(.9995);%.^(nn-1);
%                     bnmHCoeff(nn,4)=bnmHCoeff(nn,4).*(.9995);%.^(nn-1);
%                     bnmHCoeff(nn,6)=bnmHCoeff(nn,6).*(.9995);%.^(nn-1);
%                 end
%                 [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeff);
%                 [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%                 %Calculate the objective function value.
%                 [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%                     
%                 ObjFuncBest=ObjFuncNew;                
%             end
            
            
%      for kk=2:SeriesOrderIter10 %Optimize over Zy hermites.
%          for jj=2:SeriesOrderIter01 %Optimize over Zx hermites
        
      for kk=KK1:SeriesOrderIter10 %Optimize over Zy hermites.
          for jj=JJ1:SeriesOrderIter01 %Optimize over Zx hermites
        
              if(iter>1500)
                  JJ1=1;

              end
              if(iter>1000)
                  KK1=1;

              end
            %Assign 2D hermite coefficients to workhorse variable
            bnmHCoeffNew(1:SeriesOrderIter10,1:SeriesOrderIter01)=bnmHCoeff(1:SeriesOrderIter10,1:SeriesOrderIter01);
            %perturb the (kk,jj) coefficient by magnitude given in its
            %delta array named delta_bnmHCoeff(kk,jj)
            bnmHCoeffNew(kk,jj)=bnmHCoeff(kk,jj)+delta_bnmHCoeff(kk,jj);
            %convert to Z-series to calculate the cross moments
            [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeffNew);
            [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
            %Calculate the objective function value.
            [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
        

            if(ObjFuncNew3) %After successive successes, increase the perturbation step size.
                delta_bnmHCoeff(kk,jj)=delta_bnmHCoeff(kk,jj).*mul2;
            end
        end
    end
   if(rem(iter,500)==0)
         bnm
         Moments2D
         CrossMoments
         Moments2D(:,1)
         CrossMoments(:,1)
         
         ObjFuncBest
         
         str=input("Look at fit of moments");
         
      end
   
end

bnmH=bnmHCoeff;



%save("bnmHFile03.mat","bnmH");
%load("bnmHFile.mat","bnmH");

%str=input("File has been loaded");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
alphaSuccessCount1(1:SeriesOrderIter10)=0;
alphaSuccessCount2(1:SeriesOrderIter01)=0;
SuccessPrevalpha1(1:SeriesOrderIter10)=0;
SuccessPrevalpha2(1:SeriesOrderIter01)=0;

mul1=.997; %decrease the perturbation step size by multiplying it with .9 when 
%objective function does not decrease upon perturbation on both sides.  
mul2=1.003; %Increase the perturbation step size after several successive 




for mm=1:SeriesOrderIter01
    if(mm>1)
delta_bnmHCoeff1(1:SeriesOrderIter10,mm)=.005.*XmVar.^((mm)/2);%.*sqrt(1-CorrH0(mm-1).^2);
    else
    delta_bnmHCoeff1(1:SeriesOrderIter10,mm)=.005.*XmVar.^((mm)/2);
    end
end
for nn=1:SeriesOrderIter10
    if(nn>1)
delta_bnmHCoeff2(nn,1:SeriesOrderIter01)=.005.*YmVar.^((nn)/2);%.*CorrH0(nn-1);
    else
        delta_bnmHCoeff2(nn,1:SeriesOrderIter01)=.005.*YmVar.^((nn)/2);
    end
end

%           delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*CorrH0(nn-1).*sqrt(1-CorrH0(mm-1).^2);
% 

bnmHCoeff=bnmH;

Iterations01=1000;
for iter=1:Iterations01
iter
bnmHCoeff
ObjFuncBest

%Below we run a two dimensional loop that loops over all rows and columns
%of 2D array of hermite series coefficients. However, we exclude first row
%and first column from this optimization as values there were already fixed
%analytically.


%     for kk=NN1:MM1 %SeriesOrderIter10 %Optimize over Zy hermites.
%         for jj=NN2:MM2 %Optimize over Zx hermites
%             if(iter>500)
%                 NN1=2;
%                 MM1=3;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             if(iter>1000)
%                 NN1=2;
%                 MM2=SeriesOrderIter10;
%                 NN2=2;
%                 MM2=3;
%                 
%             end
%             if(iter>1500)
%                 NN1=2;
%                 MM1=4;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             if(iter>2000)
%                 NN1=2;
%                 MM1=SeriesOrderIter10;
%                 NN2=2;
%                 MM2=4;
%             end
%             if(iter>2500)
%                 NN1=2;
%                 MM1=5;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             
%             if(iter>3000)
%                 NN1=2;
%                 MM1=SeriesOrderIter01;
%                 NN2=2;
%                 MM2=6;
%             end
%         
%             if(iter>3500)
%                 NN1=2;
%                 MM1=SeriesOrderIter01;
%                 NN2=1;
%                 MM2=6;
%             end
%             if(iter>4000)
%                 NN1=1;
%                 MM1=SeriesOrderIter01;
%                 NN2=1;
%                 MM2=6;
%             end
            
%             if(rem(iter,1002)==0)
%                 for nn=2:6
%                     bnmHCoeff(nn,2)=bnmHCoeff(nn,2).*(.9995);%.^(nn-1);
%                     bnmHCoeff(nn,4)=bnmHCoeff(nn,4).*(.9995);%.^(nn-1);
%                     bnmHCoeff(nn,6)=bnmHCoeff(nn,6).*(.9995);%.^(nn-1);
%                 end
%                 [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeff);
%                 [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%                 %Calculate the objective function value.
%                 [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%                     
%                 ObjFuncBest=ObjFuncNew;                
%             end
            
            
%      for kk=2:SeriesOrderIter10 %Optimize over Zy hermites.
%          for jj=2:SeriesOrderIter01 %Optimize over Zx hermites
        
      for kk=2:SeriesOrderIter10 %Optimize over Zy hermites.
          %for jj=JJ1:SeriesOrderIter01 %Optimize over Zx hermites
%         
%               if(iter>5000)
%                   JJ1=1;
% 
%               end
%               if(iter>5500)
%                   KK1=1;
% 
%               end
            %Assign 2D hermite coefficients to workhorse variable
            bnmHCoeffNew(1:SeriesOrderIter10,1:SeriesOrderIter01)=bnmHCoeff(1:SeriesOrderIter10,1:SeriesOrderIter01);
            %perturb the (kk,jj) coefficient by magnitude given in its
            %delta array named delta_bnmHCoeff(kk,jj)
            bnmHCoeffNew(kk,2:6)=bnmHCoeff(kk,2:6).*(1+delta_bnmHCoeff1(kk,2:6));
            bnmHCoeffNew(1,1)=0;
            
            %convert to Z-series to calculate the cross moments
            [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeffNew);
            [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
            %Calculate the objective function value.
            [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
        

            if(ObjFuncNew5000)
%                   JJ1=1;
% 
%               end
%               if(iter>5500)
%                   KK1=1;
% 
%               end
            %Assign 2D hermite coefficients to workhorse variable
            bnmHCoeffNew(1:SeriesOrderIter10,1:SeriesOrderIter01)=bnmHCoeff(1:SeriesOrderIter10,1:SeriesOrderIter01);
            %perturb the (kk,jj) coefficient by magnitude given in its
            %delta array named delta_bnmHCoeff(kk,jj)
            bnmHCoeffNew(2:6,jj)=bnmHCoeff(2:6,jj).*(1+delta_bnmHCoeff2(2:6,jj));
            bnmHCoeffNew(1,1)=0;
            %convert to Z-series to calculate the cross moments
            [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeffNew);
            [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
            %Calculate the objective function value.
            [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
        

            if(ObjFuncNew4) %After successive successes, increase the perturbation step size.
                delta_bnmHCoeff1(kk,:)=delta_bnmHCoeff1(kk,:).*mul2;
            end
       
    end
    
    for jj=2:SeriesOrderIter01
            if(alphaSuccessCount2(jj)>4) %After successive successes, increase the perturbation step size.
                delta_bnmHCoeff2(:,jj)=delta_bnmHCoeff2(:,jj).*mul2;
            end
        end
   if(rem(iter,500)==0)
         bnm
         Moments2D
         CrossMoments
         Moments2D(:,1)
         CrossMoments(:,1)
         
         ObjFuncBest
         
         str=input("Look at fit of moments");
         
      end
   
end

bnmH=bnmHCoeff;


%In the block below, we convert 2D hermite coefficients array bnmH to 2D
%Z-series array bnm. We calculate the values of cross moments given the values of 
%coefficients in 2D Z-series bnm. We use these model cross moments and
%co1mpare them with target cross moments to evaluate the objective function.

%Convert from 2D Hermite Series Coefficients bnmH to 2D Z-series
%coefficients bnm
[bnm] = Convert2DHermitesInto2DSeries(bnmH);
%Evaluate the model cross moments in the function below.
[Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%Evaluate the objective function based on weighted squared difference
%between model cross moments and target cross momensts from data.
[ObjFuncBest] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
    %%%%%%%%%%%%%%%%

SeriesOrderIter10=6;
SeriesOrderIter01=6;
alphaSuccessCount(1:SeriesOrderIter10,1:SeriesOrderIter01)=0;
SuccessPrevalpha(1:SeriesOrderIter10,1:SeriesOrderIter01)=0;


%array of perturbation sizes of coefficients of the 2D Hermite form 
%of dependent variable X in iterative optimization.
for nn=1:SeriesOrderIter10
    for mm=1:SeriesOrderIter01
%         if(bnmH(nn,mm)~=0)
%             delta_bnmHCoeff(nn,mm)=bnmH(nn,mm)./50;
%             if((mm>1)&&(nn>1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*CorrH0(nn-1).*sqrt(1-CorrH0(mm-1).^2);
%             end
%             if((mm==1)&&(nn==1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2);
%             end
%             if((mm>1)&&(nn==1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*sqrt(1-CorrH0(mm-1).^2);
%             end
%             if((mm==1)&&(nn>1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*CorrH0(nn-1);
%             end
%         else
%             delta_bnmHCoeff(nn,mm)=.0000025;
%         end
        
        if(bnmH(nn,mm)~=0)
            delta_bnmHCoeff(nn,mm)=bnmH(nn,mm)./200;
            if((mm>1)&&(nn>1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm);%.*YmVar.^((nn)/2);%.*CorrH0(nn-1);
            end
            if((mm==1)&&(nn==1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm);%.*YmVar.^((nn)/2);
            end
            if((mm>1)&&(nn==1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm);%.*YmVar.^((nn)/2);
            end
            if((mm==1)&&(nn>1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm);%.*YmVar.^((nn)/2);%.*CorrH0(nn-1);
            end
        else
            delta_bnmHCoeff(nn,mm)=.00000000000025;
        end
        if(delta_bnmHCoeff(nn,mm)500)
%                 NN1=2;
%                 MM1=3;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             if(iter>1000)
%                 NN1=2;
%                 MM2=SeriesOrderIter10;
%                 NN2=2;
%                 MM2=3;
%                 
%             end
%             if(iter>1500)
%                 NN1=2;
%                 MM1=4;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             if(iter>2000)
%                 NN1=2;
%                 MM1=SeriesOrderIter10;
%                 NN2=2;
%                 MM2=4;
%             end
%             if(iter>2500)
%                 NN1=2;
%                 MM1=5;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             
%             if(iter>3000)
%                 NN1=2;
%                 MM1=SeriesOrderIter01;
%                 NN2=2;
%                 MM2=6;
%             end
%         
%             if(iter>3500)
%                 NN1=2;
%                 MM1=SeriesOrderIter01;
%                 NN2=1;
%                 MM2=6;
%             end
%             if(iter>4000)
%                 NN1=1;
%                 MM1=SeriesOrderIter01;
%                 NN2=1;
%                 MM2=6;
%             end
            
%             if(rem(iter,1002)==0)
%                 for nn=2:6
%                     bnmHCoeff(nn,2)=bnmHCoeff(nn,2).*(.9995);%.^(nn-1);
%                     bnmHCoeff(nn,4)=bnmHCoeff(nn,4).*(.9995);%.^(nn-1);
%                     bnmHCoeff(nn,6)=bnmHCoeff(nn,6).*(.9995);%.^(nn-1);
%                 end
%                 [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeff);
%                 [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%                 %Calculate the objective function value.
%                 [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%                     
%                 ObjFuncBest=ObjFuncNew;                
%             end
            
            
%      for kk=2:SeriesOrderIter10 %Optimize over Zy hermites.
%          for jj=2:SeriesOrderIter01 %Optimize over Zx hermites
        
      for kk=KK1:SeriesOrderIter10 %Optimize over Zy hermites.
          for jj=JJ1:SeriesOrderIter01 %Optimize over Zx hermites
        
              if(iter>1500)
                  JJ1=1;

              end
              if(iter>1000)
                  KK1=1;

              end
            %Assign 2D hermite coefficients to workhorse variable
            bnmHCoeffNew(1:SeriesOrderIter10,1:SeriesOrderIter01)=bnmHCoeff(1:SeriesOrderIter10,1:SeriesOrderIter01);
            %perturb the (kk,jj) coefficient by magnitude given in its
            %delta array named delta_bnmHCoeff(kk,jj)
            bnmHCoeffNew(kk,jj)=bnmHCoeff(kk,jj)+delta_bnmHCoeff(kk,jj);
            bnmHCoeffNew(1,1)=0;
            %convert to Z-series to calculate the cross moments
            [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeffNew);
            [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
            %Calculate the objective function value.
            [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
        

            if(ObjFuncNew3) %After successive successes, increase the perturbation step size.
                delta_bnmHCoeff(kk,jj)=delta_bnmHCoeff(kk,jj).*mul2;
            end
        end
    end
   if(rem(iter,500)==0)
         bnm
         Moments2D
         CrossMoments
         Moments2D(:,1)
         CrossMoments(:,1)
         
         ObjFuncBest
         
         str=input("Look at fit of moments");
         
      end
   
end

bnmH=bnmHCoeff;



%save("bnmHFile03.mat","bnmH");
%load("bnmHFile.mat","bnmH");

%str=input("File has been loaded");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% 
% 
% str=input("Entering Newton Root Search");
% 
% SeriesOrder1=6;
% SeriesOrder10=6;
% SeriesOrder01=6;
% NMomentsY=6;
% NMomentsX=6;
% 
%     %[F,dF] = CalculateMomentsAndDerivativesConditional2DNew02(Ms,aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%     [F,dF] = CalculateMomentsAndDerivativesConditional2DForNewton02(CrossMoments,aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
% % 
% %         for mm1=2:SeriesOrder01
% %        for nn1=2:SeriesOrder10
% %           da((mm1-2)*(SeriesOrder10-1)+nn1-1,1)=bnmH(nn1,mm1);
% %        end
% %         end
%         
%         for mm1=1:SeriesOrder01
%        for nn1=1:SeriesOrder10
%           da((mm1-1)*(SeriesOrder10)+nn1,1)=bnmH(nn1,mm1);
%        end
%         end
% 
%     da
%     F
%     dF
%     size(F)
%     size(dF)
%     size(da)
%     str=input("Look at sizes of variables F and dF")'
%     
%     
%     
%     %w2D(1:NMomentsY,1:NMomentsX)=1;
%     %for nn=NMomentsY-1:-1:1
%     %    for mm=NMomentsX-1:-1:1
%     %        w2D(nn,mm)=w2D(nn+1,mm+1)*(nn+1)*(mm+1);
%     %    end
%     %end
%     [bnm] = Convert2DHermitesInto2DSeries(bnmH);
%     
%     [Moments2D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
% 
%     [ObjBest] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%     
%     Moments2D
%     CrossMoments
%     ObjBest
%     str=input("Look at data and model moments");
%     %[ObjMomentOut] = CalculateObjMoment2D(Moment2D0,Moment2D,w2D,MOrder1,MOrder2);
%     
%    bnmHBest=bnmH;
%  nn=0;
%  %while((nn.000000000001) || (abs(F(2,1))>.000000000001) || (abs(F(3,1))>.000000000001) || (abs(F(4,1))>.00000000001)|| (abs(F(5,1))>.00000000001)|| (abs(F(6,1))>.00000000001)|| (abs(F(7,1))>.00000000001)|| (abs(F(8,1))>.00000000001)  ))
%  for nn=1:500
%      %nn=nn+1;
% % %     %Below Newton matrix equation to improve the Z-series coefficients guess at previous step.
%     
% if(nn==1)
% %da=da-1000000*dF\F;
% %da=da-F/dF;
% 
% da=da-50000.*dF $F);
% else
% da=da-50000.*dF\F;    
% end
% % for mm1=2:SeriesOrder01
% %        for nn1=2:SeriesOrder10
% %           bnmH(nn1,mm1)=da((mm1-2)*(SeriesOrder10-1)+nn1-1,1);
% %        end
% % end  
%      
% for mm1=1:SeriesOrder01
%        for nn1=1:SeriesOrder10
%           bnmH(nn1,mm1)=da((mm1-1)*(SeriesOrder10)+nn1,1);
%        end
%      end  
%      
%      dF
%      F
%      da
%      bnmH
%      nn
%      
%      str=input("Look at numbers---nn loop");
%      
%      
%      
%      
%     
%      [bnm] = Convert2DHermitesInto2DSeries(bnmH);
%      [Moments2D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
% [ObjNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%      
%      
%      Moments2D
%      CrossMoments
%      ObjBest
%      ObjNew
%      nn
%      str=input("Look at new numbers in the loop after update")
%      
%      
%        
%     
% 
%      if(ObjBest>ObjNew) %%%%&&( IsValidFlag))
%        
%         ObjBest=ObjNew;
%         bnmHBest=bnmH;
%         
%      end
%      
% %    [F,dF] = CalculateMomentsAndDerivativesConditional2DNew02(CrossMoments,aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%     [F,dF] = CalculateMomentsAndDerivativesConditional2DForNewton02(CrossMoments,aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
% 
%  end
%  bnmH=bnmHBest;
%  
%  [bnm] = Convert2DHermitesInto2DSeries(bnmH);
%      [Moments2D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
% [ObjFinal] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%  
% ObjFinal
% 
% str=input("Look at ObjFinal");
% 
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% W=0;
% 
% % W(1:Ndata,1)=1.0;
% % W(1:Ndata,2)=Zx(1:Ndata);
% % W(1:Ndata,3)=(Zx(1:Ndata).^2-1);
% % W(1:Ndata,4)=(Zx(1:Ndata).^3-3*Zx(1:Ndata));
% % W(1:Ndata,5)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3);
% % W(1:Ndata,6)=(Zx(1:Ndata).^5-10*Zx(1:Ndata)+15*Zx(1:Ndata));
% 
% W(1:Ndata,1)=1.*Zys(1:Ndata);
% W(1:Ndata,2)=Zx(1:Ndata).*Zys(1:Ndata);
% W(1:Ndata,3)=(Zx(1:Ndata).^2-1).*Zys(1:Ndata);
% W(1:Ndata,4)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*Zys(1:Ndata);
% W(1:Ndata,5)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*Zys(1:Ndata);
% W(1:Ndata,6)=(Zx(1:Ndata).^5-10*Zx(1:Ndata)+15*Zx(1:Ndata)).*Zys(1:Ndata);
% 
% W(1:Ndata,7)=(Zys(1:Ndata).^2-1);
% W(1:Ndata,8)=Zx(1:Ndata).*(Zys(1:Ndata).^2-1);
% W(1:Ndata,9)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^2-1);
% W(1:Ndata,10)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^2-1);
% W(1:Ndata,11)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^2-1);
% W(1:Ndata,12)=(Zx(1:Ndata).^5-10*Zx(1:Ndata)+15*Zx(1:Ndata)).*(Zys(1:Ndata).^2-1);
% 
% W(1:Ndata,13)=(Zys(1:Ndata).^3-3*Zy(1:Ndata));
% W(1:Ndata,14)=Zx(1:Ndata).*(Zys(1:Ndata).^3-3*Zy(1:Ndata));
% W(1:Ndata,15)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^3-3*Zy(1:Ndata));
% W(1:Ndata,16)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));
% W(1:Ndata,17)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));
% W(1:Ndata,18)=(Zx(1:Ndata).^5-10*Zx(1:Ndata )+15*Zx(1:Ndata)).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));
% 
% W(1:Ndata,19)=(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% W(1:Ndata,20)=Zx(1:Ndata).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% W(1:Ndata,21)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% W(1:Ndata,22)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% W(1:Ndata,23)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% W(1:Ndata,24)=(Zx(1:Ndata).^5-10*Zx(1:Ndata)+15*Zx(1:Ndata)).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% 
% W(1:Ndata,25)=(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
% 
% W(1:Ndata,27)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
% W(1:Ndata,28)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
% W(1:Ndata,29)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
% W(1:Ndata,30)=(Zx(1:Ndata).^5-10
% 
% 
% bnmH=bnmH0;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
SeriesOrder1=6;
NMomentsY=6;
NMomentsX=6;
    for nn=1:NMomentsY
       for mm=1:NMomentsX
           CrossMoments(nn,mm)=0;
           for pp=1:Ndata
              CrossMoments(nn,mm)=CrossMoments(nn,mm)+Y(pp).^nn.*X(pp).^mm/Ndata;
           end
       end
    end



[chh] = ProduceFirstRowofConditioal2DZSeries02_6M_A(aa,SeriesOrder1,CrossMoments);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[bnm] = Convert2DHermitesInto2DSeries(bnmH);

SeriesOrder1=6;
SeriesOrder10=6;
SeriesOrder01=6;
NMomentsX=6;
NMomentsY=6;
[Moments2D0] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);

Moments2D0

CrossMoments

str=input("Look at comparison of moments--first-standardized");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%In the code block below, we convert 2D hermite series coefficients of 
%dependent variable X from standardized version to original version.
%For that we first multiply the entire 2D Hermite series by square root of
%variance.
%Later we multiply each column of hermite series of X with particular 
%order of Zy hermite polynomials by square root of volatility(independent variable)
%raised to that power of Zy polynomial order as below.
%bnmH=bnmH.*sqrt(XmVar);
%bnmH(:,1)=bnmH(:,1)*sqrt(XmVar);
%for nn=2:6
%    bnmH(nn,:)=bnmH(nn,:).*(sqrt(YmVar)).^(nn-1);
%end

 bnmH=bnmH*sqrt(XmVar);
% for nn=2:6
%     bnmH(nn,:)=bnmH(nn,:).*(sqrt(YmVar)).^(nn-1);
% end
% for nn=2:6
%     bnmH(:,nn)=bnmH(:,nn).*(sqrt(XmVar)).^(nn-1);
% end

%We convert X from hermite series form to Z-series form.
[bnm] = Convert2DHermitesInto2DSeries(bnmH);
bnm(1,1)=MeanX-bnm(3,1)-3*bnm(5,1)-1*bnm(1,3)-1*3*bnm(1,5)-3*bnm(5,3)-bnm(3,3)-3*bnm(3,5)-9*bnm(5,5);

%Finally in above line, we make sure that mean of the 2D Z-series is


%Below, we convert Z-series of independent variable Y from standard form to
%original variable form.

aa=aa*sqrt(YmVar);
aa(1)=MeanY-aa(3)-3*aa(5);


 SeriesOrder1=6;
 SeriesOrder10=6;
 SeriesOrder01=6;
 NMomentsX=6;
 NMomentsY=6;
 [Moments2D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
 
 Moments2D
 
 CrossMoments11
 
 str=input("Look at comparison of moments");
% 
% 
% for nn=1:NMomentsX
%     for mm=1:NMomentsY
%         
%         Moments2D(mm,nn)
%         Moments2D0(mm,nn).*(sqrt(YmVar)).^(mm).*(sqrt(XmVar)).^(nn)
%         Moments2D0(mm,nn)./(sqrt(YmVar)).^(mm)./(sqrt(XmVar)).^(nn)
%         Moments2D(mm,nn)./(sqrt(YmVar)).^(mm)./(sqrt(XmVar)).^(nn)
%         nn
%         mm
%         str=input("Look at moments again---22---22-222---")
%     end
% end
        




end
```

 
```

---

## Error 32: Unbalanced $: 1

**Snippet:** `I think it might be of some help so I just decided to post the working program a`

**Full content:**

```
I think it might be of some help so I just decided to post the working program as such.

.

.

```
function [bnm,aa] = CalculateConditionalProbabilitiesYtoXLinearRegression04IterB(Yin,Xin)

%Yin argument translates to independent random variable Y
%Xin argument translates to dependent variable X.
%This function takes observations of an independent variable Y and
%dependent varaible X. These have to be joint observations in the sense
%that nth observation of Y, given by Y(n) is taken jointly with nth
%observation of X, given by X(n). Two arrays of observations are the same
%length and nth mmber of independent variable Y is jointly observed with nth
%member of depedent variable X.
%We want to find the detailed relationship between Y and X so we can get
%the conditional density of dependent variable X given a particular value
%of independent variable Y. This will be done by calibrating coefficients
%of our 2D hermite series to data so that a very good fit to cross moments
%between X and Y is retrieved.
%We will first find univariate Z-series/hermite series of both random
%variables independently. For joint dynamics of dependent variable given 
%te independnet variable, we will assume a 2D hermite series (This has to 
%be two dimensional to be able to capture the dynamics from independent variable Y
%and have its own dynamics) and form but we do not know the coefficients of 
%this 2D hermite series. In this program, we try to use iterative optimization 
%to find the unknown coefficients of 2D hermite series of dependent variable X 
%in a way that after taking products with independent varaible Y, expectation   
%of these products i.e cross moments are as exactly retrieved as possible.
%Our iterative optimization procedure perturbs each hermite coefficient in 
%2D hermite series  by a very slight amount and checks the objective function.
%If the objective function decreases, we eccept the perturbation otherwise
%reject it and then perturb by a small amount in other opposite direction
%and then again check the objective function. If perturbations in both sides 
%are rejected, we do not change the coefficients but slightly decrease the
%perturbation size. 
%We will first standardize the data of both random variables and then
%calculate univariate hermite series of both variables and also their 
%cross moments in standardized form. We do all the calculations of coefficients
%of independent variable Y and 2D dependent variable X
%in standardized version of variables and moments. After optimization of coefficents on 
%standardized data, at the end, we invert the standardization of both 
%dependent and independent variables appropriately to get the Z-series and
%hermite series of actual varaibles in theri original coordinates back from
%standardized coordinates.
%Before optimization, we place two conditions on 2D dependent variable X so that
%first row and first column of 2D hermite coefficents of X is already
%known before optimization stage and it is not changed in optimization. 
%We do not iteratively optimize over this first row and first colums
%which are analytically known from these two conditions.
%Our first condition is that after integration (of bivaraite density or
%alternatively bivaraite 2D Z-series/2D Hermite series) over independent
%variable, we should get the univaraite marginal density/Z-series/Hermite series of X
%which has already been calculated out of data. This fixes the zeroth
%hermite(of independent varaible Y) related terms in the Z-series/hermite series. 
%Please look at this forum post# 2121 for explanation of this first condition.
% https://forum.wilmott.com/viewtopic.php?t=99702&start=2115#p879042

%We can analytically solve for first order cross moments of X with higher
%order in Y. From the analytical solution of these moments, we find first
%row of coefficents in the hermite form.


% 2D Hermite Series Form used in this program is given as
% 
% X = bnmH(1,1) + bnmH(2,1) H_1(Z_y) + bnmH(3,1) H_2(Z_y) + bnmH(4,1) H_3(Z_y) + bnmH(5,1) H_4(Z_y) + bnmH(6,1) H_5(Z_y) 
% + [ bnmH(1,2) + bnmH(2,2) H_1(Z_y) + bnmH(3,2) H_2(Z_y) + bnmH(4,2) H_3(Z_y) + bnmH(5,2) H_4(Z_y) + bnmH(6,2) H_5(Z_y)] H_1(Zx) 
% + [ bnmH(1,3) + bnmH(2,3) H_1(Z_y) + bnmH(3,3) H_2(Z_y) + bnmH(4,3) H_3(Z_y) + bnmH(5,3) H_4(Z_y) + bnmH(6,3) H_5(Z_y)] H_2(Zx)
% + [ bnmH(1,4) + bnmH(2,4) H_1(Z_y) + bnmH(3,4) H_2(Z_y) + bnmH(4,4) H_3(Z_y) + bnmH(5,4) H_4(Z_y) + bnmH(6,4) H_5(Z_y)] H_3(Zx)
% + [ bnmH(1,5) + bnmH(2,5) H_1(Z_y) + bnmH(3,5) H_2(Z_y) + bnmH(4,5) H_3(Z_y) + bnmH(5,5) H_4(Z_y) + bnmH(6,5) H_5(Z_y)] H_4(Zx)
% + [ bnmH(1,6) + bnmH(2,6) H_1(Z_y) + bnmH(3,6) H_2(Z_y) + bnmH(4,6) H_3(Z_y) + bnmH(5,6) H_4(Z_y) + bnmH(6,6) H_5(Z_y)] H_5(Zx)
 
% 2D Z-Series Form used in this program is given as
% 
% X = bnm(1,1) + bnm(2,1) Z_y + bnm(3,1) (Z_y)^2 + bnm(4,1) (Z_y)^3 + bnm(5,1) (Z_y)^4 + bnm(6,1) (Z_y)^5 
% + [ bnm(1,2) + bnm(2,2) Z_y + bnm(3,2) (Z_y)^2 + bnm(4,2) (Z_y)^3 + bnm(5,2) (Z_y)^4 + bnm(6,2) (Z_y)^5 ] Zx 
% + [ bnm(1,3) + bnm(2,2) Z_y + bnm(3,3) (Z_y)^2 + bnm(4,3) (Z_y)^3 + bnm(5,3) (Z_y)^4 + bnm(6,3) (Z_y)^5 ] Zx^2 
% + [ bnm(1,4) + bnm(2,2) Z_y + bnm(3,4) (Z_y)^2 + bnm(4,4) (Z_y)^3 + bnm(5,4) (Z_y)^4 + bnm(6,4) (Z_y)^5 ] Zx^3 
% + [ bnm(1,5) + bnm(2,2) Z_y + bnm(3,5) (Z_y)^2 + bnm(4,5) (Z_y)^3 + bnm(5,5) (Z_y)^4 + bnm(6,5) (Z_y)^5 ] Zx^4 
% + [ bnm(1,6) + bnm(2,2) Z_y + bnm(3,6) (Z_y)^2 + bnm(4,6) (Z_y)^3 + bnm(5,6) (Z_y)^4 + bnm(6,6) (Z_y)^5 ] Zx^5




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%In the code block below, we standardize the independent variable Y and dependent variable X.
%We do all later calculations of various Z-series and cross moments in 
%standardized framework and then at the end of the program, we convert 
%the calculated coefficients of 2D hermite series/Z-series of dependent 
%variable X into original non-standardized framework.

 Ndata=length(Yin);
 
 MeanY=sum(Yin(1:Ndata))/Ndata;
 MeanX=sum(Xin(1:Ndata))/Ndata;
 
 Ym(1:Ndata)=Yin(1:Ndata)-MeanY;
 Xm(1:Ndata)=Xin(1:Ndata)-MeanX;
 
 YmVar=sum(Ym(1:Ndata).^2)/Ndata;
 XmVar=sum(Xm(1:Ndata).^2)/Ndata;
 
 Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);
 X(1:Ndata)=Xm(1:Ndata)/sqrt(XmVar);

 
 sqrt(YmVar)
 sqrt(XmVar)
 
 str=input("Look at standardization constants");
 

 NMomentsY=6;
 NMomentsX=6;
     for nn=1:NMomentsY
        for mm=1:NMomentsX
            CrossMoments11(nn,mm)=0;
            for pp=1:Ndata
               CrossMoments11(nn,mm)=CrossMoments11(nn,mm)+Yin(pp).^nn.*Xin(pp).^mm/Ndata;
               %CrossMoments11(nn,mm)=CrossMoments11(nn,mm)+Y(pp).^nn.*X(pp).^mm/Ndata;
               %CrossMoments11(nn,mm)=CrossMoments11(nn,mm)+Ym(pp).^nn.*Xm(pp).^mm/Ndata;
            end
        end
     end
 
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Code block below uses polynomial regression to find univariate Z-series 
%coefficients of independent variable Y.
%To know more about polynomial regression read the following and associated
%posts:  https://forum.wilmott.com/viewtopic.php?t=99702&start=2010#p877143
 
%You can get the text file MomentMatchParams08.txt from the forum post below
%https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=2040#p877863

Mtable=readtable('C:\Users\Lenovo\Documents\MATLAB\MATLAB1\MomentMatchParams08.txt');

%ZI is moment matched grid along the normal density with number of grid
%points equal to data elements in Y given by Ndata. The grid is constructed
%so that probability mass in each grid cell is 1/Ndata so this matches the
%observation probability of Ndata data elements. Due to equal probability
%mass in each grid cell, we call it equiprobable grid.

[ZI] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable);

Ys=sort(Y);
Ymu(1:Ndata,1)=Ys(1:Ndata);

W(1:Ndata,1)=1;
W(1:Ndata,2)=ZI(1:Ndata);
W(1:Ndata,3)=ZI(1:Ndata).^2;
W(1:Ndata,4)=ZI(1:Ndata).^3;
W(1:Ndata,5)=ZI(1:Ndata).^4;
W(1:Ndata,6)=ZI(1:Ndata).^5;
% W(1:Ndata,7)=ZI(1:Ndata).^6;
% W(1:Ndata,8)=ZI(1:Ndata).^7;


coeff=inv(W'*W)*(W'*Ymu);

%Above, we get coefficients of univariate Z-series of independent
%variable Y by least square regression.


a0=coeff(1,1);
a(1:5)=coeff(2:6,1);

%Above, we assign zeroth power Z-series coefficient to a0 and rest of
%the coefficients to array a.
%This was older format but we might need it since many old functions are written 
%in this format.

%Below, we assign same Z-series coefficients to a single array. This is
%newer format that we want to use mostly.
aa(1:6)=coeff(1:6);


%uncomment these lines if you want to see shape of Z-series constructed
%density of Y. We had calculated coefficients of this Z-series by
%least square polynomial regression.
%PlotZSeriesDensity(a0,a,'r')
%str=input("Look at the density of volatility");
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5    
%In this code block, we calcualate the coefficients of univariate marginal
%density of dependent variable X again by least square polynomial
%regression as we did in previous block for independent variable Y.
    
Xs=sort(X);
Xmu(1:Ndata,1)=Xs(1:Ndata);

W(1:Ndata,1)=1;
W(1:Ndata,2)=ZI(1:Ndata);
W(1:Ndata,3)=ZI(1:Ndata).^2;
W(1:Ndata,4)=ZI(1:Ndata).^3;
W(1:Ndata,5)=ZI(1:Ndata).^4;
W(1:Ndata,6)=ZI(1:Ndata).^5;

coeff=inv(W'*W)*(W'*Xmu);

c0=coeff(1,1);
c(1:5)=coeff(2:6,1);

cc(1:6)=coeff(1:6,1);

[ccH] = ConvertZSeriesToHermiteSeriesNew(cc,5);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Zy= CalculateZgivenXAndZSeriesC5Improved(Y,a0,a);

[Xs,I]=sort(X);

Zys=Zy(I);

Zx=ZI;

Xmu(1:Ndata,1)=Xs(1:Ndata);


W=0;

W(1:Ndata,1)=1.0;
W(1:Ndata,2)=Zx(1:Ndata);
W(1:Ndata,3)=(Zx(1:Ndata).^2-1);
W(1:Ndata,4)=(Zx(1:Ndata).^3-3*Zx(1:Ndata));
W(1:Ndata,5)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3);
W(1:Ndata,6)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata));

W(1:Ndata,7)=1.*Zys(1:Ndata);
W(1:Ndata,8)=Zx(1:Ndata).*Zys(1:Ndata);
W(1:Ndata,9)=(Zx(1:Ndata).^2-1).*Zys(1:Ndata);
W(1:Ndata,10)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*Zys(1:Ndata);
W(1:Ndata,11)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*Zys(1:Ndata);
W(1:Ndata,12)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata)).*Zys(1:Ndata);

W(1:Ndata,13)=(Zys(1:Ndata).^2-1);
W(1:Ndata,14)=Zx(1:Ndata).*(Zys(1:Ndata).^2-1);
W(1:Ndata,15)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^2-1);
W(1:Ndata,16)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^2-1);
W(1:Ndata,17)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^2-1);
W(1:Ndata,18)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata)).*(Zys(1:Ndata).^2-1);

W(1:Ndata,19)=(Zys(1:Ndata).^3-3*Zy(1:Ndata));
W(1:Ndata,20)=Zx(1:Ndata).*(Zys(1:Ndata).^3-3*Zy(1:Ndata));
W(1:Ndata,21)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^3-3*Zy(1:Ndata));
W(1:Ndata,22)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));
W(1:Ndata,23)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));
W(1:Ndata,24)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata)).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));

W(1:Ndata,25)=(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
W(1:Ndata,26)=Zx(1:Ndata).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
W(1:Ndata,27)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
W(1:Ndata,28)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
W(1:Ndata,29)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
W(1:Ndata,30)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata)).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);

W(1:Ndata,31)=(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
W(1:Ndata,32)=Zx(1:Ndata).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
W(1:Ndata,33)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
W(1:Ndata,34)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
W(1:Ndata,35)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
W(1:Ndata,36)=(Zx(1:Ndata).^5-10*Zx(1:Ndata).^3+15*Zx(1:Ndata)).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));

coeff=inv(W'*W)*(W'*Xmu);


bnmH0(1,1:6)=ccH(1:6);  %Replace first line of X-hermites with Marginal density retrieval condition
bnmH0(2,1:6)=coeff(7:12);
bnmH0(3,1:6)=coeff(13:18);
bnmH0(4,1:6)=coeff(19:24);
bnmH0(5,1:6)=coeff(25:30);
bnmH0(6,1:6)=coeff(31:36);

bnmH=bnmH0;





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


SeriesOrder1=6;
NMomentsY=6;


SeriesOrder10=6; %SeriesOrder10 = 1 + highest power of Zy in 2D Z-series%Here highest power of Zy is five 
SeriesOrder01=6; %SeriesOrder01 = 1 + highest power of Zx in 2D Z-series%Here highest power of Zx is also five
%notation is  bnm(1:SeriesOrder10,1:SeriesOrder01)
%Similalry    bnmH(1:SeriesOrder10,1:SeriesOrder01)
 
NMomentsX=6; %Highest moment of X in cross moments of X and Y
NMomentsY=6; %Highest moment of Y in cross moments of X and Y

%Below we calculate various cross moments between X and Y. These are
%calculated from standardized data.
for nn=1:NMomentsY
   for mm=1:NMomentsX
       CrossMoments(nn,mm)=0;
       for pp=1:Ndata
          CrossMoments(nn,mm)=CrossMoments(nn,mm)+Y(pp).^nn.*X(pp).^mm/Ndata;
       end
   end
end
    
    
%Below are the weights on calculation of objective function. More weight on
%a particular moment means that its better match with target moments gets more emphasized as
%compared to match of other moments.
%Choice of good weights is non-trivial.
%Current choice is only haphazard. Please try improvements/
    
    
 w2D(1:NMomentsY,1:NMomentsX)=1;
for nn=NMomentsY-1:-1:1
    for mm=NMomentsX-1:-1:1
        %w2D(nn,mm)=w2D(nn+1,mm+1)*(nn+1)*(mm+1);
        w2D(nn,mm)=w2D(nn+1,mm+1)*(nn+1).^2*(mm+1).^2.0;
    end
end

% w2D(:,1)=w2D(:,1)*100000000;
% w2D(1,:)=w2D(1,:)*100000000;
% w2D(:,2)=w2D(:,2)*500000;
% w2D(2,:)=w2D(2,:)*500000;
% w2D(1,2)=w2D(1,2)*100;
% w2D(2,2)=w2D(2,2)*10;
% w2D(3,2)=w2D(3,2)*5;
% w2D(:,3)=w2D(:,3)*100000;
% w2D(1,3)=w2D(1,3)*20;
% w2D(2,3)=w2D(2,3)*5;
% w2D(1,:)=w2D(1,:)*10000;
% w2D(2,:)=w2D(2,:)*100;
% w2D(3,:)=w2D(3,:)*10;
% w2D(:,4)=w2D(:,4)*10000;
% w2D(1,4)=w2D(1,4)*10;
% w2D(2,4)=w2D(2,4)*2;
% w2D(:,5)=w2D(:,5)*1000;  
% w2D(:,6)=w2D(:,6)*20;  

%Please look on detailed comments inside function below for more insight about it.
%The function below returns coefficients on first row of hermite series so that all
%cross moments of first order in dependent variable X and various orders in independent
%variable Y are matched.

[ddH] = ProduceFirstRowofConditioal2DZSeries02_6M_A(aa,SeriesOrder1,CrossMoments);

%Below we define a 2D array of hermite series coefficents and populate its
%first row with output from above function so that all cross moments of
%first order in X and different orders in Y are matched.
%We also populate first column with univariate hermite coefficients of 
%marginal density of X because of the condition that upon integration of
%the bivariate hermite form, we should get univariate marginal density as a
%result. %Please look at this forum post# 2121 for explanation of this first condition.
% https://forum.wilmott.com/viewtopic.php?t=99702&start=2115#p879042

% 
% %%%%%%%%%%%%%%%%%%%%%%%%%5
% 
ccH0=ccH;

% for nn=2:6
%     %ccH(nn)=sign(ccH(nn)-dd(nn)).*sqrt(abs(sign(ccH(nn)).*ccH(nn).^2-sign(dd(nn)).*dd(nn).^2));
%     if(abs(ccH(nn))>abs(ddH(nn)))
%         ccH(nn)=sign(ccH(nn)).*sqrt(ccH(nn).^2-ddH(nn).^2);
%     else
%     
%         ccH(nn)=0;
%     end 
% end

% %[ccH1] = SubtractZSeriesRVsByMonteCarlo(ccH0,ddH);
% 
% 
% 
% %ddH
% 
% %ccH0
% 
% ccH
% 
% %ccH1
% 
% %ccH2
% %str=input("Look at comparison of ccH");
% 
%  bnmH(1,1:6)=ccH(1:6);     %populate first column with univariate margianl density hermite coefficients of X.
% % %bnmH(1,1)=MeanX;
%  bnmH(1:6,1)=ddH(1:6);      %populate first row so that all cross moments of first order in X are matched.
%  bnmH(1,1)=0;
% % % 
% %%%%%%%%%%%%%%%%%%%%%%%5

 [Zy] = CalculateZgivenXAndZSeriesC5Improved(Y,a0,a);
 [Zx] = CalculateZgivenXAndZSeriesC5Improved(X,c0,c);
% 
 paths=Ndata;
 [CorrH0] = CalculateCorrelationBivariateHermiteCH(Zx,Zy,paths,5);

 
 CorrH0
 ccH
 ddH
 
 str=input("Look at correlation related variables");
 ccH0=ccH;
% ccH0(1)=0;
%ddH(1)=0;
 %ddH_Corr(2:6)=ddH(2:6).*CorrH0(1:5);
 for nn=2:6
     ddH_Corr(nn)=ddH(nn).*CorrH0(nn-1);
 end
 ddH_Corr(1)=ddH(1);%.*CorrH0(nn-1);
 
 
 
[ccH2] = SubtractDensity(ccH0,ddH_Corr);
%[ccH2] = SubtractDensity(ccH0,ddH);


%bnmH(1,2:6)=ccH2(2:6);


CorrH0
 ccH
 ddH
 ccH2
 str=input("Look at correlation related variables----2");

 %[ba01,ba1]=ConvertHCoeffsToZCoeffs(bnmH(1,1),bnmH(1,2:6),5);
 %[ba02,ba2]=ConvertHCoeffsToZCoeffs(bnmH(1,1),bnmH(2:6,1),5);
 
 [ba01,ba1]=ConvertHCoeffsToZCoeffs(ccH2(1),ccH2(2:6),5);
 %[ba02,ba2]=ConvertHCoeffsToZCoeffs(ddH(1),ddH(2:6),5);
 
 [ba02,ba2]=ConvertHCoeffsToZCoeffs(ddH_Corr(1),ddH_Corr(2:6),5);
 %[ba02,ba2]=ConvertHCoeffsToZCoeffs(ddH(1),ddH(2:6),5);
 
 [IsValidFlag1] = CheckIsValidDensity(ba01,ba1);
 [IsValidFlag2] = CheckIsValidDensityPN(ba02,ba2);
 
 IsValidFlag1
 IsValidFlag2
 
 str=input("Look at correlation related variables----3");
%  loopCount=0;
%  if(IsValidFlag1==0)
%      while((IsValidFlag1==0) && (loopCountabs(ddH(2)))
%  bnmH(1,2)=sign(ccH(2)-CorrH0(1).*ddH(2)).*sqrt(ccH(2).^2-CorrH0(1).^2.*ddH(2).^2);
%  bnmH(2,1)=ddH(2);
% else
%  bnmH(1,2)=ccH(2);   
%  bnmH(2,1)=sign(ddH(2)-CorrH0(1).*ccH(2)).*sqrt(ddH(2).^2-CorrH0(1).^2.*ccH(2).^2);   
% end
% if(abs(ccH(3))>abs(ddH(3)))
%  bnmH(1,3)=sign(ccH(3)-CorrH0(2).*ddH(3)).*sqrt(ccH(3).^2-CorrH0(2).^2.*ddH(3).^2);
%  bnmH(3,1)=ddH(3);
% else
%  bnmH(1,3)=ccH(3);
%  bnmH(3,1)=sign(ddH(3)-CorrH0(2).*ccH(3)).*sqrt(ddH(3).^2-CorrH0(2).^2.*ccH(3).^2);
%     
% end
% if(abs(ccH(4))>abs(ddH(4)))
%  bnmH(1,4)=sign(ccH(4)-CorrH0(3).*ddH(4)).*sqrt(ccH(4).^2-CorrH0(3).^2.*ddH(4).^2);
%  bnmh(4,1)=ddH(4);
% else
% bnmH(4,1)=sign(ddH(4)-CorrH0(3).*ccH(4)).*sqrt(ddH(4).^2-CorrH0(3).^2.*ccH(4).^2);
%  bnmh(1,4)=ccH(4);    
% end
% if(abs(ccH(5))>abs(ddH(5)))
%  bnmH(1,5)=sign(ccH(5)-CorrH0(4).*ddH(5)).*sqrt(ccH(5).^2-CorrH0(4).^2.*ddH(5).^2);
%  bnmh(5,1)=ddH(5);
% else
% bnmH(5,1)=sign(ddH(5)-CorrH0(4).*ccH(5)).*sqrt(ddH(5).^2-CorrH0(4).^2.*ccH(5).^2);
%  bnmh(1,5)=ccH(5);    
% end
% if(abs(ccH(6))>abs(ddH(6)))
%  bnmH(1,6)=sign(ccH(6)-CorrH0(5).*ddH(6)).*sqrt(ccH(6).^2-CorrH0(5).^2.*ddH(6).^2);
%  bnmh(6,1)=ddH(6);
% else
% bnmH(6,1)=sign(ddH(6)-CorrH0(5).*ccH(6)).*sqrt(ddH(6).^2-CorrH0(5).^2.*ccH(6).^2);
%  bnmh(1,6)=ccH(6);    
% end% 
% % bnmH(2,1)=CorrH0(1).*ccH(2);
% % bnmH(3,1)=CorrH0(2).*ccH(3);
% % bnmH(4,1)=CorrH0(3).*ccH(4);
% % bnmH(5,1)=CorrH0(4).*ccH(5);
% % bnmH(6,1)=CorrH0(5).*ccH(6);
% % 






%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%In our iterative optimization, we will not alter the above first column and first row of 2D hermite coefficients array.


%In the block below, we convert 2D hermite coefficients array bnmH to 2D
%Z-series array bnm. We calculate the values of cross moments given the values of 
%coefficients in 2D Z-series bnm. We use these model cross moments and
%co1mpare them with target cross moments to evaluate the objective function.

%Convert from 2D Hermite Series Coefficients bnmH to 2D Z-series
%coefficients bnm
[bnm] = Convert2DHermitesInto2DSeries(bnmH);
%Evaluate the model cross moments in the function below.
[Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%Evaluate the objective function based on weighted squared difference
%between model cross moments and target cross momensts from data.
[ObjFuncBest] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
    %%%%%%%%%%%%%%%%

SeriesOrderIter10=6;
SeriesOrderIter01=6;
alphaSuccessCount(1:SeriesOrderIter10,1:SeriesOrderIter01)=0;
SuccessPrevalpha(1:SeriesOrderIter10,1:SeriesOrderIter01)=0;


%array of perturbation sizes of coefficients of the 2D Hermite form 
%of dependent variable X in iterative optimization.
for nn=1:SeriesOrderIter10
    for mm=1:SeriesOrderIter01
%         if(bnmH(nn,mm)~=0)
%             delta_bnmHCoeff(nn,mm)=bnmH(nn,mm)./50;
%             if((mm>1)&&(nn>1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*CorrH0(nn-1).*sqrt(1-CorrH0(mm-1).^2);
%             end
%             if((mm==1)&&(nn==1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2);
%             end
%             if((mm>1)&&(nn==1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*sqrt(1-CorrH0(mm-1).^2);
%             end
%             if((mm==1)&&(nn>1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*CorrH0(nn-1);
%             end
%         else
%             delta_bnmHCoeff(nn,mm)=.0000025;
%         end
        
        if(bnmH(nn,mm)~=0)
            delta_bnmHCoeff(nn,mm)=bnmH(nn,mm)./50;
            if((mm>1)&&(nn>1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*YmVar.^((nn)/2);%.*CorrH0(nn-1);
            end
            if((mm==1)&&(nn==1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*YmVar.^((nn)/2);
            end
            if((mm>1)&&(nn==1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*YmVar.^((nn)/2);
            end
            if((mm==1)&&(nn>1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*YmVar.^((nn)/2);%.*CorrH0(nn-1);
            end
        else
            delta_bnmHCoeff(nn,mm)=.0000025;
        end
    end    
end

%Assign initial value of bnmH to workhorse variable bnmHCoeff which will be
%used in iterative ioptimization

%load("bnmHFile02.mat","bnmH");

bnmHCoeff=bnmH;

mul1=.9; %decrease the perturbation step size by multiplying it with .9 when 
%objective function does not decrease upon perturbation on both sides.  
mul2=1.1; %Increase the perturbation step size after several successive 
%successes in decreasing the objective function
Iterations=00;
MM1=2;
NN1=2;
MM2=2
NN2=2;

KK1=2;
JJ1=2;
for iter=1:Iterations
iter
bnmHCoeff
ObjFuncBest

%Below we run a two dimensional loop that loops over all rows and columns
%of 2D array of hermite series coefficients. However, we exclude first row
%and first column from this optimization as values there were already fixed
%analytically.


    for kk=NN1:MM1 %SeriesOrderIter10 %Optimize over Zy hermites.
        for jj=NN2:MM2 %Optimize over Zx hermites
            if(iter=300))
                NN1=2;
                MM2=SeriesOrderIter10;
                NN2=SeriesOrderIter01-1;
                MM2=SeriesOrderIter01;
                
            end
            if((iter=600))
                NN1=2;
                MM2=SeriesOrderIter10;
                NN2=SeriesOrderIter01-2;
                MM2=SeriesOrderIter01;
            end
            if((iter=900))
                NN1=2;
                MM2=SeriesOrderIter10;
                NN2=SeriesOrderIter01-3;
                MM2=SeriesOrderIter01;
            end
            if((iter=1200))
                NN1=2;
                MM2=SeriesOrderIter10;
                NN2=SeriesOrderIter01-4;
                MM2=SeriesOrderIter01;
            end
            
            if(iter>3000)
                NN1=2;
                MM1=SeriesOrderIter01;
                NN2=2;
                MM2=6;
            end
        
            if(iter>3500)
                NN1=2;
                MM1=SeriesOrderIter01;
                NN2=1;
                MM2=6;
            end
            if(iter>4000)
                NN1=1;
                MM1=SeriesOrderIter01;
                NN2=1;
                MM2=6;
            end
            %Assign 2D hermite coefficients to workhorse variable
            bnmHCoeffNew(1:SeriesOrderIter10,1:SeriesOrderIter01)=bnmHCoeff(1:SeriesOrderIter10,1:SeriesOrderIter01);
            %perturb the (kk,jj) coefficient by magnitude given in its
            %delta array named delta_bnmHCoeff(kk,jj)
            bnmHCoeffNew(kk,jj)=bnmHCoeff(kk,jj)+delta_bnmHCoeff(kk,jj);
            %convert to Z-series to calculate the cross moments
            [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeffNew);
            [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
            %Calculate the objective function value.
            [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
        

            if(ObjFuncNew3) %After successive successes, increase the perturbation step size.
                delta_bnmHCoeff(kk,jj)=delta_bnmHCoeff(kk,jj).*mul2;
            end
        end
    end
   if(rem(iter,500)==0)
         bnm
         Moments2D
         CrossMoments
         Moments2D(:,1)
         CrossMoments(:,1)
         
         ObjFuncBest
         
         str=input("Look at fit of moments");
         
      end
   
end

bnmH=bnmHCoeff;



%save("bnmHFile03.mat","bnmH");
%load("bnmHFile.mat","bnmH");

%str=input("File has been loaded");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
alphaSuccessCount1(1:SeriesOrderIter10)=0;
alphaSuccessCount2(1:SeriesOrderIter01)=0;
SuccessPrevalpha1(1:SeriesOrderIter10)=0;
SuccessPrevalpha2(1:SeriesOrderIter01)=0;

mul1=.996; %decrease the perturbation step size by multiplying it with .9 when 
%objective function does not decrease upon perturbation on both sides.  
mul2=1.004; %Increase the perturbation step size after several successive 




for mm=1:SeriesOrderIter01
    if(mm>1)
delta_bnmHCoeff1(1:SeriesOrderIter10,mm)=.005.*XmVar.^((mm)/2);%.*sqrt(1-CorrH0(mm-1).^2);
    else
    delta_bnmHCoeff1(1:SeriesOrderIter10,mm)=.005.*XmVar.^((mm)/2);
    end
end
for nn=1:SeriesOrderIter10
    if(nn>1)
delta_bnmHCoeff2(nn,1:SeriesOrderIter01)=.005.*YmVar.^((nn)/2);%.*CorrH0(nn-1);
    else
        delta_bnmHCoeff2(nn,1:SeriesOrderIter01)=.005.*YmVar.^((nn)/2);
    end
end

%           delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*CorrH0(nn-1).*sqrt(1-CorrH0(mm-1).^2);
% 

bnmHCoeff=bnmH;

Iterations01=000;
for iter=1:Iterations01
iter
bnmHCoeff
ObjFuncBest

%Below we run a two dimensional loop that loops over all rows and columns
%of 2D array of hermite series coefficients. However, we exclude first row
%and first column from this optimization as values there were already fixed
%analytically.


%     for kk=NN1:MM1 %SeriesOrderIter10 %Optimize over Zy hermites.
%         for jj=NN2:MM2 %Optimize over Zx hermites
%             if(iter>500)
%                 NN1=2;
%                 MM1=3;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             if(iter>1000)
%                 NN1=2;
%                 MM2=SeriesOrderIter10;
%                 NN2=2;
%                 MM2=3;
%                 
%             end
%             if(iter>1500)
%                 NN1=2;
%                 MM1=4;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             if(iter>2000)
%                 NN1=2;
%                 MM1=SeriesOrderIter10;
%                 NN2=2;
%                 MM2=4;
%             end
%             if(iter>2500)
%                 NN1=2;
%                 MM1=5;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             
%             if(iter>3000)
%                 NN1=2;
%                 MM1=SeriesOrderIter01;
%                 NN2=2;
%                 MM2=6;
%             end
%         
%             if(iter>3500)
%                 NN1=2;
%                 MM1=SeriesOrderIter01;
%                 NN2=1;
%                 MM2=6;
%             end
%             if(iter>4000)
%                 NN1=1;
%                 MM1=SeriesOrderIter01;
%                 NN2=1;
%                 MM2=6;
%             end
            
%             if(rem(iter,1002)==0)
%                 for nn=2:6
%                     bnmHCoeff(nn,2)=bnmHCoeff(nn,2).*(.9995);%.^(nn-1);
%                     bnmHCoeff(nn,4)=bnmHCoeff(nn,4).*(.9995);%.^(nn-1);
%                     bnmHCoeff(nn,6)=bnmHCoeff(nn,6).*(.9995);%.^(nn-1);
%                 end
%                 [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeff);
%                 [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%                 %Calculate the objective function value.
%                 [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%                     
%                 ObjFuncBest=ObjFuncNew;                
%             end
            
            
%      for kk=2:SeriesOrderIter10 %Optimize over Zy hermites.
%          for jj=2:SeriesOrderIter01 %Optimize over Zx hermites
        
      for kk=2:SeriesOrderIter10 %Optimize over Zy hermites.
          %for jj=JJ1:SeriesOrderIter01 %Optimize over Zx hermites
%         
%               if(iter>5000)
%                   JJ1=1;
% 
%               end
%               if(iter>5500)
%                   KK1=1;
% 
%               end
            %Assign 2D hermite coefficients to workhorse variable
            bnmHCoeffNew(1:SeriesOrderIter10,1:SeriesOrderIter01)=bnmHCoeff(1:SeriesOrderIter10,1:SeriesOrderIter01);
            %perturb the (kk,jj) coefficient by magnitude given in its
            %delta array named delta_bnmHCoeff(kk,jj)
            bnmHCoeffNew(kk,2:6)=bnmHCoeff(kk,2:6).*(1+delta_bnmHCoeff1(kk,2:6));
            bnmHCoeffNew(1,1)=0;
            
            %convert to Z-series to calculate the cross moments
            [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeffNew);
            [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
            %Calculate the objective function value.
            [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
        

            if(ObjFuncNew5000)
%                   JJ1=1;
% 
%               end
%               if(iter>5500)
%                   KK1=1;
% 
%               end
            %Assign 2D hermite coefficients to workhorse variable
            bnmHCoeffNew(1:SeriesOrderIter10,1:SeriesOrderIter01)=bnmHCoeff(1:SeriesOrderIter10,1:SeriesOrderIter01);
            %perturb the (kk,jj) coefficient by magnitude given in its
            %delta array named delta_bnmHCoeff(kk,jj)
            bnmHCoeffNew(2:6,jj)=bnmHCoeff(2:6,jj).*(1+delta_bnmHCoeff2(2:6,jj));
            bnmHCoeffNew(1,1)=0;
            %convert to Z-series to calculate the cross moments
            [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeffNew);
            [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
            %Calculate the objective function value.
            [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
        

            if(ObjFuncNew4) %After successive successes, increase the perturbation step size.
                delta_bnmHCoeff1(kk,:)=delta_bnmHCoeff1(kk,:).*mul2;
            end
       
    end
    
    for jj=2:SeriesOrderIter01
            if(alphaSuccessCount2(jj)>4) %After successive successes, increase the perturbation step size.
                delta_bnmHCoeff2(:,jj)=delta_bnmHCoeff2(:,jj).*mul2;
            end
        end
   if(rem(iter,500)==0)
         bnm
         Moments2D
         CrossMoments
         Moments2D(:,1)
         CrossMoments(:,1)
         
         ObjFuncBest
         
         str=input("Look at fit of moments");
         
      end
   
end

bnmH=bnmHCoeff;


%In the block below, we convert 2D hermite coefficients array bnmH to 2D
%Z-series array bnm. We calculate the values of cross moments given the values of 
%coefficients in 2D Z-series bnm. We use these model cross moments and
%co1mpare them with target cross moments to evaluate the objective function.

%Convert from 2D Hermite Series Coefficients bnmH to 2D Z-series
%coefficients bnm
[bnm] = Convert2DHermitesInto2DSeries(bnmH);
%Evaluate the model cross moments in the function below.
[Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%Evaluate the objective function based on weighted squared difference
%between model cross moments and target cross momensts from data.
[ObjFuncBest] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
    %%%%%%%%%%%%%%%%

SeriesOrderIter10=6;
SeriesOrderIter01=6;
alphaSuccessCount(1:SeriesOrderIter10,1:SeriesOrderIter01)=0;
SuccessPrevalpha(1:SeriesOrderIter10,1:SeriesOrderIter01)=0;


%array of perturbation sizes of coefficients of the 2D Hermite form 
%of dependent variable X in iterative optimization.
for nn=1:SeriesOrderIter10
    for mm=1:SeriesOrderIter01
%         if(bnmH(nn,mm)~=0)
%             delta_bnmHCoeff(nn,mm)=bnmH(nn,mm)./50;
%             if((mm>1)&&(nn>1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*CorrH0(nn-1).*sqrt(1-CorrH0(mm-1).^2);
%             end
%             if((mm==1)&&(nn==1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2);
%             end
%             if((mm>1)&&(nn==1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*sqrt(1-CorrH0(mm-1).^2);
%             end
%             if((mm==1)&&(nn>1))
%             delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm).*XmVar.^((mm)/2).*YmVar.^((nn)/2).*CorrH0(nn-1);
%             end
%         else
%             delta_bnmHCoeff(nn,mm)=.0000025;
%         end
        
        if(bnmH(nn,mm)~=0)
            delta_bnmHCoeff(nn,mm)=bnmH(nn,mm)./200;
            if((mm>1)&&(nn>1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm);%.*YmVar.^((nn)/2);%.*CorrH0(nn-1);
            end
            if((mm==1)&&(nn==1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm);%.*YmVar.^((nn)/2);
            end
            if((mm>1)&&(nn==1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm);%.*YmVar.^((nn)/2);
            end
            if((mm==1)&&(nn>1))
            delta_bnmHCoeff(nn,mm)=delta_bnmHCoeff(nn,mm);%.*YmVar.^((nn)/2);%.*CorrH0(nn-1);
            end
        else
            delta_bnmHCoeff(nn,mm)=.00000000000025;
        end
        if(delta_bnmHCoeff(nn,mm)500)
%                 NN1=2;
%                 MM1=3;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             if(iter>1000)
%                 NN1=2;
%                 MM2=SeriesOrderIter10;
%                 NN2=2;
%                 MM2=3;
%                 
%             end
%             if(iter>1500)
%                 NN1=2;
%                 MM1=4;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             if(iter>2000)
%                 NN1=2;
%                 MM1=SeriesOrderIter10;
%                 NN2=2;
%                 MM2=4;
%             end
%             if(iter>2500)
%                 NN1=2;
%                 MM1=5;
%                 NN2=2;
%                 MM2=SeriesOrderIter01;
%             end
%             
%             if(iter>3000)
%                 NN1=2;
%                 MM1=SeriesOrderIter01;
%                 NN2=2;
%                 MM2=6;
%             end
%         
%             if(iter>3500)
%                 NN1=2;
%                 MM1=SeriesOrderIter01;
%                 NN2=1;
%                 MM2=6;
%             end
%             if(iter>4000)
%                 NN1=1;
%                 MM1=SeriesOrderIter01;
%                 NN2=1;
%                 MM2=6;
%             end
            
%             if(rem(iter,1002)==0)
%                 for nn=2:6
%                     bnmHCoeff(nn,2)=bnmHCoeff(nn,2).*(.9995);%.^(nn-1);
%                     bnmHCoeff(nn,4)=bnmHCoeff(nn,4).*(.9995);%.^(nn-1);
%                     bnmHCoeff(nn,6)=bnmHCoeff(nn,6).*(.9995);%.^(nn-1);
%                 end
%                 [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeff);
%                 [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%                 %Calculate the objective function value.
%                 [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%                     
%                 ObjFuncBest=ObjFuncNew;                
%             end
            
            
%      for kk=2:SeriesOrderIter10 %Optimize over Zy hermites.
%          for jj=2:SeriesOrderIter01 %Optimize over Zx hermites
        
      for kk=KK1:SeriesOrderIter10 %Optimize over Zy hermites.
          for jj=JJ1:SeriesOrderIter01 %Optimize over Zx hermites
        
              if(iter>1500)
                  JJ1=1;

              end
              if(iter>1000)
                  KK1=1;

              end
            %Assign 2D hermite coefficients to workhorse variable
            bnmHCoeffNew(1:SeriesOrderIter10,1:SeriesOrderIter01)=bnmHCoeff(1:SeriesOrderIter10,1:SeriesOrderIter01);
            %perturb the (kk,jj) coefficient by magnitude given in its
            %delta array named delta_bnmHCoeff(kk,jj)
            bnmHCoeffNew(kk,jj)=bnmHCoeff(kk,jj)+delta_bnmHCoeff(kk,jj);
            bnmHCoeffNew(1,1)=0;
            %convert to Z-series to calculate the cross moments
            [bnm] = Convert2DHermitesInto2DSeries(bnmHCoeffNew);
            [Moments2D,Moments1D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
            %Calculate the objective function value.
            [ObjFuncNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
        

            if(ObjFuncNew3) %After successive successes, increase the perturbation step size.
                delta_bnmHCoeff(kk,jj)=delta_bnmHCoeff(kk,jj).*mul2;
            end
        end
    end
   if(rem(iter,500)==0)
         bnm
         Moments2D
         CrossMoments
         Moments2D(:,1)
         CrossMoments(:,1)
         
         ObjFuncBest
         
         str=input("Look at fit of moments");
         
      end
   
end

bnmH=bnmHCoeff;



%save("bnmHFile03.mat","bnmH");
%load("bnmHFile.mat","bnmH");

%str=input("File has been loaded");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% 
% 
% str=input("Entering Newton Root Search");
% 
% SeriesOrder1=6;
% SeriesOrder10=6;
% SeriesOrder01=6;
% NMomentsY=6;
% NMomentsX=6;
% 
%     %[F,dF] = CalculateMomentsAndDerivativesConditional2DNew02(Ms,aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%     [F,dF] = CalculateMomentsAndDerivativesConditional2DForNewton02(CrossMoments,aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
% % 
% %         for mm1=2:SeriesOrder01
% %        for nn1=2:SeriesOrder10
% %           da((mm1-2)*(SeriesOrder10-1)+nn1-1,1)=bnmH(nn1,mm1);
% %        end
% %         end
%         
%         for mm1=1:SeriesOrder01
%        for nn1=1:SeriesOrder10
%           da((mm1-1)*(SeriesOrder10)+nn1,1)=bnmH(nn1,mm1);
%        end
%         end
% 
%     da
%     F
%     dF
%     size(F)
%     size(dF)
%     size(da)
%     str=input("Look at sizes of variables F and dF")'
%     
%     
%     
%     %w2D(1:NMomentsY,1:NMomentsX)=1;
%     %for nn=NMomentsY-1:-1:1
%     %    for mm=NMomentsX-1:-1:1
%     %        w2D(nn,mm)=w2D(nn+1,mm+1)*(nn+1)*(mm+1);
%     %    end
%     %end
%     [bnm] = Convert2DHermitesInto2DSeries(bnmH);
%     
%     [Moments2D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
% 
%     [ObjBest] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%     
%     Moments2D
%     CrossMoments
%     ObjBest
%     str=input("Look at data and model moments");
%     %[ObjMomentOut] = CalculateObjMoment2D(Moment2D0,Moment2D,w2D,MOrder1,MOrder2);
%     
%    bnmHBest=bnmH;
%  nn=0;
%  %while((nn.000000000001) || (abs(F(2,1))>.000000000001) || (abs(F(3,1))>.000000000001) || (abs(F(4,1))>.00000000001)|| (abs(F(5,1))>.00000000001)|| (abs(F(6,1))>.00000000001)|| (abs(F(7,1))>.00000000001)|| (abs(F(8,1))>.00000000001)  ))
%  for nn=1:500
%      %nn=nn+1;
% % %     %Below Newton matrix equation to improve the Z-series coefficients guess at previous step.
%     
% if(nn==1)
% %da=da-1000000*dF\F;
% %da=da-F/dF;
% 
% da=da-50000.*dF $F);
% else
% da=da-50000.*dF\F;    
% end
% % for mm1=2:SeriesOrder01
% %        for nn1=2:SeriesOrder10
% %           bnmH(nn1,mm1)=da((mm1-2)*(SeriesOrder10-1)+nn1-1,1);
% %        end
% % end  
%      
% for mm1=1:SeriesOrder01
%        for nn1=1:SeriesOrder10
%           bnmH(nn1,mm1)=da((mm1-1)*(SeriesOrder10)+nn1,1);
%        end
%      end  
%      
%      dF
%      F
%      da
%      bnmH
%      nn
%      
%      str=input("Look at numbers---nn loop");
%      
%      
%      
%      
%     
%      [bnm] = Convert2DHermitesInto2DSeries(bnmH);
%      [Moments2D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
% [ObjNew] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%      
%      
%      Moments2D
%      CrossMoments
%      ObjBest
%      ObjNew
%      nn
%      str=input("Look at new numbers in the loop after update")
%      
%      
%        
%     
% 
%      if(ObjBest>ObjNew) %%%%&&( IsValidFlag))
%        
%         ObjBest=ObjNew;
%         bnmHBest=bnmH;
%         
%      end
%      
% %    [F,dF] = CalculateMomentsAndDerivativesConditional2DNew02(CrossMoments,aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
%     [F,dF] = CalculateMomentsAndDerivativesConditional2DForNewton02(CrossMoments,aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
% 
%  end
%  bnmH=bnmHBest;
%  
%  [bnm] = Convert2DHermitesInto2DSeries(bnmH);
%      [Moments2D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
% [ObjFinal] = CalculateObjMoment2D1D(CrossMoments,Moments2D,w2D,NMomentsX,NMomentsY);
%  
% ObjFinal
% 
% str=input("Look at ObjFinal");
% 
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% W=0;
% 
% % W(1:Ndata,1)=1.0;
% % W(1:Ndata,2)=Zx(1:Ndata);
% % W(1:Ndata,3)=(Zx(1:Ndata).^2-1);
% % W(1:Ndata,4)=(Zx(1:Ndata).^3-3*Zx(1:Ndata));
% % W(1:Ndata,5)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3);
% % W(1:Ndata,6)=(Zx(1:Ndata).^5-10*Zx(1:Ndata)+15*Zx(1:Ndata));
% 
% W(1:Ndata,1)=1.*Zys(1:Ndata);
% W(1:Ndata,2)=Zx(1:Ndata).*Zys(1:Ndata);
% W(1:Ndata,3)=(Zx(1:Ndata).^2-1).*Zys(1:Ndata);
% W(1:Ndata,4)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*Zys(1:Ndata);
% W(1:Ndata,5)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*Zys(1:Ndata);
% W(1:Ndata,6)=(Zx(1:Ndata).^5-10*Zx(1:Ndata)+15*Zx(1:Ndata)).*Zys(1:Ndata);
% 
% W(1:Ndata,7)=(Zys(1:Ndata).^2-1);
% W(1:Ndata,8)=Zx(1:Ndata).*(Zys(1:Ndata).^2-1);
% W(1:Ndata,9)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^2-1);
% W(1:Ndata,10)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^2-1);
% W(1:Ndata,11)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^2-1);
% W(1:Ndata,12)=(Zx(1:Ndata).^5-10*Zx(1:Ndata)+15*Zx(1:Ndata)).*(Zys(1:Ndata).^2-1);
% 
% W(1:Ndata,13)=(Zys(1:Ndata).^3-3*Zy(1:Ndata));
% W(1:Ndata,14)=Zx(1:Ndata).*(Zys(1:Ndata).^3-3*Zy(1:Ndata));
% W(1:Ndata,15)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^3-3*Zy(1:Ndata));
% W(1:Ndata,16)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));
% W(1:Ndata,17)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));
% W(1:Ndata,18)=(Zx(1:Ndata).^5-10*Zx(1:Ndata )+15*Zx(1:Ndata)).*(Zys(1:Ndata).^3-3*Zys(1:Ndata));
% 
% W(1:Ndata,19)=(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% W(1:Ndata,20)=Zx(1:Ndata).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% W(1:Ndata,21)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% W(1:Ndata,22)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% W(1:Ndata,23)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% W(1:Ndata,24)=(Zx(1:Ndata).^5-10*Zx(1:Ndata)+15*Zx(1:Ndata)).*(Zys(1:Ndata).^4-6*Zys(1:Ndata).^2+3);
% 
% W(1:Ndata,25)=(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
% 
% W(1:Ndata,27)=(Zx(1:Ndata).^2-1).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
% W(1:Ndata,28)=(Zx(1:Ndata).^3-3*Zx(1:Ndata)).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
% W(1:Ndata,29)=(Zx(1:Ndata).^4-6*Zx(1:Ndata).^2+3).*(Zys(1:Ndata).^5-10*Zys(1:Ndata).^3+15*Zys(1:Ndata));
% W(1:Ndata,30)=(Zx(1:Ndata).^5-10
% 
% 
% bnmH=bnmH0;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
SeriesOrder1=6;
NMomentsY=6;
NMomentsX=6;
    for nn=1:NMomentsY
       for mm=1:NMomentsX
           CrossMoments(nn,mm)=0;
           for pp=1:Ndata
              CrossMoments(nn,mm)=CrossMoments(nn,mm)+Y(pp).^nn.*X(pp).^mm/Ndata;
           end
       end
    end



[chh] = ProduceFirstRowofConditioal2DZSeries02_6M_A(aa,SeriesOrder1,CrossMoments);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[bnm] = Convert2DHermitesInto2DSeries(bnmH);

SeriesOrder1=6;
SeriesOrder10=6;
SeriesOrder01=6;
NMomentsX=6;
NMomentsY=6;
[Moments2D0] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);

Moments2D0

CrossMoments

str=input("Look at comparison of moments--first-standardized");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%In the code block below, we convert 2D hermite series coefficients of 
%dependent variable X from standardized version to original version.
%For that we first multiply the entire 2D Hermite series by square root of
%variance.
%Later we multiply each column of hermite series of X with particular 
%order of Zy hermite polynomials by square root of volatility(independent variable)
%raised to that power of Zy polynomial order as below.
%bnmH=bnmH.*sqrt(XmVar);
%bnmH(:,1)=bnmH(:,1)*sqrt(XmVar);
%for nn=2:6
%    bnmH(nn,:)=bnmH(nn,:).*(sqrt(YmVar)).^(nn-1);
%end

 bnmH=bnmH*sqrt(XmVar);
% for nn=2:6
%     bnmH(nn,:)=bnmH(nn,:).*(sqrt(YmVar)).^(nn-1);
% end
% for nn=2:6
%     bnmH(:,nn)=bnmH(:,nn).*(sqrt(XmVar)).^(nn-1);
% end

%We convert X from hermite series form to Z-series form.
[bnm] = Convert2DHermitesInto2DSeries(bnmH);
bnm(1,1)=MeanX-bnm(3,1)-3*bnm(5,1)-1*bnm(1,3)-1*3*bnm(1,5)-3*bnm(5,3)-bnm(3,3)-3*bnm(3,5)-9*bnm(5,5);

%Finally in above line, we make sure that mean of the 2D Z-series is


%Below, we convert Z-series of independent variable Y from standard form to
%original variable form.

aa=aa*sqrt(YmVar);
aa(1)=MeanY-aa(3)-3*aa(5);


 SeriesOrder1=6;
 SeriesOrder10=6;
 SeriesOrder01=6;
 NMomentsX=6;
 NMomentsY=6;
 [Moments2D] = CalculateCrossMomentsConditional2DNew02(aa,bnm,SeriesOrder1,SeriesOrder10,SeriesOrder01,NMomentsX,NMomentsY);
 
 Moments2D
 
 CrossMoments11
 
 str=input("Look at comparison of moments");
% 
% 
% for nn=1:NMomentsX
%     for mm=1:NMomentsY
%         
%         Moments2D(mm,nn)
%         Moments2D0(mm,nn).*(sqrt(YmVar)).^(mm).*(sqrt(XmVar)).^(nn)
%         Moments2D0(mm,nn)./(sqrt(YmVar)).^(mm)./(sqrt(XmVar)).^(nn)
%         Moments2D(mm,nn)./(sqrt(YmVar)).^(mm)./(sqrt(XmVar)).^(nn)
%         nn
%         mm
%         str=input("Look at moments again---22---22-222---")
%     end
% end
        




end
```

```

---

## Error 33: Unbalanced $: 39

**Snippet:** `Friends, on a risk neutral measure, the hermite series of terminal distribution `

**Full content:**

```
Friends, on a risk neutral measure, the hermite series of terminal distribution of asset random variable at terminal time T is given as



$ X(t, T) \, = \,x_0 \, \exp(r\,(T-t)) + a_1 \, H_1(Z)\, +\,  a_2 \,H_2(Z) \, + \, a_3 \, H_3(Z)$



while terminal distribution of a call price is given as



$V_x(Z)\,=\, \begin{cases}

(\, \,x_0 \, \exp(r\,(T-t))\,- k\,) + \, a_1\, Z\,+ \, a_2\, (Z^2-1)\, + \, a_3 \, (Z^3\,-\,3\,Z)\, , & \text{ if } Z \geq Z_k \\

0,   & \text{ otherwise }

\end{cases}  $

In the above equation $Z_k$ represents the value of Z at which asset equals the value of strike X(Z)=k. or in other words $X(Z_k)=k$



I need to clarify this first since I had not been correct in some of the recent earlier posts. We can use risk neutral pricing argument only due to delta hedging which mitigates the option value risk due to movements of the spot asset. Our underlying asset can be assumed to grow at the riskless rate only due to delta hedging argument 

There are other different types of hedging. For example in spirit of vega hedging, we can hedge against the changes in hermite series coefficients, $a_1$, $a_2$ and a $a_3$ of the terminal distribution. 

We can also decrease the variance of any of(or some combination, or all of) the hermite polynomials thus altering the effective variance of the risk neutral portfolio of the derivative and its hedge instruments. 

So there is delta hedging that ensures that our portfolio is immune to small changes in spot. Then there is vega hedging that makes the portfolio immune to changes in the hermite series coefficients or alternatively immune to changes in different modes of cumulative variance till maturity. Then there could be other types of hedging that could altogether alter the variance of the portfolio. We could also mitigate a multi-option portfolio against changes in variance of some select stocks or we could go one step further and make our portfolio totally insensitive to variance of some stocks/components. 



We will continue to explore all of this along with correlations but first I want to discuss delta hedging in our framework. I had earlier given a wrong formula for delta hedging a few posts earlier in which I hedged for the first hermite polynomial and erroneously called it delta hedging.

Here is the right formula.

First expected value of call option is given without interest rates(we will cover all complete formulas very soon) as



$\,E[V_x\,]=\, \int\limits_{Z_k}^{\infty}\, \Big[ \,(\,x_0 \, \,- k\,) + \, a_1\, Z\,+ \, a_2\, (Z^2-1)\, + \, a_3 \, (Z^3\,-\,3\,Z) \Big] \, p(Z) \, dZ\,$ 

or simplifying

$\,E[V_x\,]=\, \int\limits_{Z_k}^{\infty}\, g(x_0,Z) \, p(Z) \, dZ\,$

 

By Liebniz Rule, we can right the derivative of above integral with respect to $x_0$ as



$\Large{\frac{d[E[V_x]]}{dx_0}\, = \, - g(x_0,Z_k)\, \frac{dZ_k}{dx_0} \, + \, \, \int\limits_{Z_k}^{\infty}\, \frac{dg(x_0,Z)}{dx_0} \, p(Z) \, dZ\,}$



To calculate  $\frac{dZ_k}{dx_0} \,$, we first write the hermite representation of the asset as



$ X(t, T) \, = \,x_0 \, + a_1 \, H_1(Z)\, +\,  a_2 \,H_2(Z) \, + \, a_3 \, H_3(Z)$



We know that $Z_k] is value of Z for which X(Z) is equal to strike, K. So



$ k \, = \,x_0 \, + a_1 \, H_1(Z_k)\, +\,  a_2 \,H_2(Z_k) \, + \, a_3 \, H_3(Z_k)$



Differentiating above equation with respect to $x_0$, we get



$\, 0\,=\, 1\,+ a_1\, \frac{dZ_k}{dx_0}\, + \,a_2\, 2\, Z_k\, \frac{dZ_k}{dx_0}\,+\, a_3\, (3\, {Z_k}^2\, -\, 3\,) \frac{dZ_k}{dx_0}\,$ 



or 



$\Large{\, \frac{dZ_k}{dx_0}\,=\, \frac{-1}{a_1\, +\,2\,  a_2\, Z_k \, + \,   a_3\, (3\, {Z_k}^2\, -\, 3\,)}}$



So formula for our delta becomes



$\Large{\frac{d[E[V_x]]}{dx_0}\, = \, - g(x_0,Z_k)\, \frac{dZ_k}{dx_0} \, + \, \, \int\limits_{Z_k}^{\infty}\, \frac{dg(x_0,Z)}{dx_0} \, p(Z) \, dZ\,}$





$= \large{\, -  \Big[ \, \big[(\,x_0 \, \,- k\,) + \, a_1\, {Z_k}\,+ \, a_2\, ({Z_k}^2-1)\, + \, a_3 \, ({Z_k}^3\,-\,3\,Z_k) \big] \, \phi(Z_k)\Big]\,} \Large{ \Big[\, \frac{-1}{a_1\, +\,2\,  a_2\, Z_k \, + \,   a_3\, (3\, {Z_k}^2\, -\, 3\,)}  \Big] \,} \\

+\large{\, \big[1\, -\, \Phi(Z_k) \big]\,}$
```

---

## Error 34: Unbalanced $: 1

**Snippet:** `Please read posts 1893, 1894, 1895 and 1896 together to see how a prestigious ba`

**Full content:**

```
Please read posts 1893, 1894, 1895 and 1896 together to see how a prestigious bank in Pakistan stole $ 2500 from my account on orders of CIA. When I was in London in 2010-11, Lloyds TSB also stole my thousand pounds. They go to the limits of using banks to strip innocent people of their money and most banks silently comply.

You can see the bank statements as proof of theft by the Pakistani bank. Following four posts and download the PDF bank statement.

https://forum.wilmott.com/viewtopic.php?t=99702&start=1890#p876174



Read here about theft by Lioyds TSB:



https://forum.wilmott.com/viewtopic.php?t=99702&start=1890#p876182



I am very sure that my speaking against corrupt banks will protect many innocent individuals in the society because in most of the places in the world banks continue to deceive innocent people when ordered by military agencies. 



We are all aware that I have made an allegation of theft on Lloyds TSB. I want Lloyds TSB to either accept responsibility for theft and deception or sue me for maligning them openly on internet.



I am sure my writing about corrupt practices of the banks will save many innocent individuals like me because even many prestigious banks all over the world are ready to cheat and deceive innocent citizens when asked to do so by military agencies.
```

---

## Error 35: Unbalanced $: 1

**Snippet:** `%Post Starts%  Please read posts 1893, 1894, 1895 and 1896 together to see how a`

**Full content:**

```
%Post Starts%

Please read posts 1893, 1894, 1895 and 1896 together to see how a prestigious bank in Pakistan stole $ 2500 from my account on orders of CIA. When I was in London in 2010-11, Lloyds TSB also stole my thousand pounds. They go to the limits of using banks to strip innocent people of their money and most banks silently comply.

You can see the bank statements as proof of theft by the Pakistani bank. Following four posts and download the PDF bank statement.

https://forum.wilmott.com/viewtopic.php?t=99702&start=1890#p876174



Read here about theft by Lioyds TSB:



https://forum.wilmott.com/viewtopic.php?t=99702&start=1890#p876182



I am very sure that my speaking against corrupt banks will protect many innocent individuals in the society because in most of the places in the world banks continue to deceive innocent people when ordered by military agencies. 



We are all aware that I have made an allegation of theft on Lloyds TSB. I want Lloyds TSB to either accept responsibility for theft and deception or sue me for maligning them openly on internet.



I am sure my writing about corrupt practices of the banks will save many innocent individuals like me because even many prestigious banks all over the world are ready to cheat and deceive innocent citizens when asked to do so by military agencies.

%Post Ends%





%Post Starts%

I want friends to please protest to American defense that has become a puppet in the hands of rich jews. Scumbags of American defense consider successful Muslims a stain on social fabric of United States. I am just a Muslim by birth and do not believe in any religion and there are thousands of Muslims like me that are kept on mind control by American defense to prevent them from being successful. And majority of such victims are  American born Muslims who are like other natives of US even though I was admittedly a foreigner. Black sheep in American defense behind mind control are given very prestigious jobs paying millions of dollars in Jewish companies after they retire and rich jews want to block talented muslims from being successful in United States with an iron fist since they are afraid that if some muslims become successful, they would start wielding some influence and start opposing American policies in Israel and they want to nip this supposed evil in the bud. And American defense has no dearth of wannabees who desperately want to join the ranks of so many others who have gotten extremely high paying jobs with great social status in jewish companies after retirement from American defense. Please do not blindly believe me and find out somebody in your social circle(or well known to somebody in your social circle) you know well and who is in mind control agency of US defense and ask them about my allegations and your eyes would open forever about role of rich jews in United States and how they openly use mind control on anyone they wish especially on a large number of even white Americans whose families have been living in US for hundreds of years. If your eyes do not open forever, I am ready to take any blame you wish. 



Especially very talented American people in science and technology are forced to work in Jewish owned companies due to fear of mind control. Many such people who want to leave are coldly told by administration to leave but their mind control is initiated by American defense on insistence of jews right after they leave the jewish company and once they know the reason behind mind control was that they tried to leave the jewish company against the will of the company owners. And due to large number of such precedents well known to many professionals in many jewish companies, most of the very talented people do not dare to leave the jewish companies against the will of administration since they know very well that they would be instantly put on mind control by American defense who dances on the tunes of rich jews since they want extremely high paying prestigious jobs with jewish companies having great social status. Please do not believe a single word I say blindly but try to find out the actual truth on your own from authentic sources you know well and you will find the truth that would open your eyes forever.



Not everybody is the same, there are at the same time a large number of jews who have nothing to do with any of this and many good jewish companies who do not follow any inhuman practice. But there is a close group of rich jews who are actually involved in large scale mind control with American defsnse working as their proxy. Please try to know the truth on your own.



I want to advise American defense to watch a lot of American movies and try to behave like heroes in those movies. Instead people in American defense are short-tempered scumbags who became belligerent when anybody criticizes them. Contrary to American and Western spirit of freedom of criticism and speech that we all cherish, these short-tempered scumbags are unwilling to tolerate anything other than eulogies based on complete lies. Just like Henry Ford used to say that you can buy any color of car as long as it is black, to these scumbags of American defense the freedom of speech means that you can say anything you like as long it is a eulogy otherwise they become belligerent and start moving thousands of people to silence someone who speaks the truth about them. Let us all of us start cursing Erdogan together now.

%Post Ends%







%Post Starts%

I want to request Pakistanis abroad and at home to please let some Pakistani investigative reporters and other journalists know about my thread on Wilmott. Please also inform dawn, Jang, business recorder, tribune, ARY news and all other Pakistani newspapers so that they could come to know how our army systematically fails Pakistani talent in return from bribes from CIA and American Army. This is how crooks in our army buy islands in New Zealand and properties in Belgium. There are more than 500 very talented Pakistanis who are kept constantly on mind control by our army. They have continued to do this over past twenty years since Pervaiz Musharraf came to power. If bastards in our army had not retarded intelligent Pakistanis, there would be many very successful international enterprises coming from our country and we would still be at Par with India and Bangladesh in per capita income who were much behind in per capita income 25 years ago and today are much ahead of us. This is since our army continues to darken the future of our nation in return for hundreds of billions of rupee generals are given by CIA. This is probably one of the most successful operations by CIA to silently fail an entire nation.



I want to request Pakistanis abroad and at home to please tell brave journalists and others like Hamid Mir, Aitezaz Ahsan, Latif Khosa, factfocus people, and other prominent people in political parties and government that readers of my blog can think about my thread. Every chief of our army lives abroad after retirement. But we want to live in our country forever and build our "dhirti Maan" as famously quoted by Latif Khosa.



I want to say again that if I have survived to say this today, it is only due to help and support from good American people.  Most of the good American people  have a lot of humanity for us and they always want our poor nations to progress. Good people in United States supported me when nobody in my own country was ready to support me. American people are not a bad people at all and they do not support any mind control in our nations or their own nation. 

However large armies in most countries are composed of corrupt crooks only. China, America, Pakistan, Russia. All these countries have large corrupt armies. American army for example plays in hands of rich Jews among other forms of rampant corruption. So please be careful to not generalize my posts about corrupt American army and defense to good American people.

%Post Ends%





%Post Starts%

This is also a relevant post I copied from past.  https://forum.wilmott.com/viewtopic.php?t=99702&start=1965#p876890



Many friends who are used to formal language all the time might be disturbed by my use of slang expletives for bad people but after reading Einstein's letter to Marie Curie, I consider myself perfectly validated to use the word of scum for American army and for bad jews who have no ethics and are ready to fall to every low level of humanity for some material gain or due to their hatred, venom, poison or malice as in case of bad jews. 



Even though American society keeps jews in very high regard, they are not gold-plated. Just like any other people or race, some of them are extremely good human beings, some of them are extremely evil and some of them simply do not care. They tend to be more intelligent and when this intelligence shows itself in the form of Einstein we see one of the greatest human beings ever born but when this intelligence turns evil and machinatory we have exactly opposite form of humanity like evil jewish billionaire godfather/goldfather and his rich jewish cohort who has taken complete control of American army to advance their nefarious designs and have retarded thousands of innocent and intelligent people they did not like. So respect has to be shown in abundance to good people but very carefully to evil people. When great respect is shown to evil people, they become even more emboldened to advance their agendas based on hatred, venom,  poison and malice.



When I was undergraduate I had transferred to US after two years and in my last year I lost all interest in engineering and my GPA composed of only two years was very bad so I had to go to a not so good school for masters in Economics. But I had decided to work very hard and I was confident that with my hard work I will succeed again. But some third class malicious jews at the university got slighted by my talent for mathematics. These evil jews were very aware of mind control even in 1997 and jewish billionaire had already great influence in US army at that time. I was just like a boy working hard to find my future that all of a sudden, from nowhere, the stone of mind control fell on my head. When mind control agencies told malicious jews that I had several special neurotransmitters, the malicious jews were completely resolved to force mind control on me at all cost. US Defence was already a puppet in hands of evil jewish billionaire and when mind control guys knew that billionaire was taking special interest in my mind control, they were extremely enthusiastic to please him and do all sort of efforts to retard me.



I want to tell friends that American army, due to pressure from evil jewish billionaire, had appointed one or two jews from academia from my graduate university who were enthusiastic about retarding me and they are the ones who take key decisions about what to do with me. They continue to think in my brain for several hours every day and completely remain in touch with all progress in mind control on a daily basis. All cruelties and torture that was unleashed on me was in their complete knowledge and was authorized by them on suggestions of mind control agents.

Over past thirty years, lot of bad jews have developed a network in academia(with absolute apology to all the great jewish people in academia) and when a victim has to be retarded most of the jews in the network start orchestrating totally complete lies about the victim so that good people think that retarding the victim is indeed is a very good thing. 



Several other smart people are paid by American army to keep thinking in my brain and they remain oriented with what I am doing. For example, if there is something silly in my work, these people who are keeping track of my programs already inform the jewish network and this jewish network starts spreading fun about my work several days in advance. As my research progresses and my programs are updated, several people have access to my programs and its logic several days in advance before I post them in public.



And I want to tell people that this network of evil jews has greatly perfected itself over past thirty years and not only muslims are retarded, everyone they do not like including europeans, blacks and a large number of white talented Americans are retarded at whim by this network of emboldened evil jews. 

I want to request all good people in American society and in european countries to end and thwart this gang of evil jews who are bent on retarding intelligent people of every nation and creed they do not like.



I am sure that intolerant and arrogant scum of American army will again resort to torture and violence and start focusing their lasers on my temple, eyes, teeth and ears.

%Post Ends%





%Post Starts%

Friends very sorry for so many off-topic posts. This is the last post on the persecution topic for now. I will be getting an antipsychotic injection in a few hours now. And I will try to avoid this topic unless there is some other development in my persecution or some threat by army etc. I will go back to technical work and try to post new things about my research but I may not be able to do good work for next 10-15 days due to effect of injection.

I am copying this last post (for now) from the past. I will try my best to revert to my research work now and post about it.



The following post is composed of my own genuine thoughts why Jews were wronged so many times throughout history.

https://forum.wilmott.com/viewtopic.php?t=99702&start=2145#p879442



Friends, I am very sorry to have come to this point to be forced to write this post. 

Please read what I have been trying to say since so many years. https://forum.wilmott.com/viewtopic.php?f=15&t=101453

People know that despite my brutal, cruel and sadistic persecution on hands of rich American jews that has now lasted for 25 years, I always tried to mention very carefully that all jews are not bad people and a large number of them are very good human beings. 



And in order to avoid offending the jews who are good human beings, many times in the past, I had been very careful to not say my mind about bad and evil jews in United States. Now there is this evil jewish billionaire who is Godfather/Goldfather of mind control, who is an exact example of what happens when scum makes big money by chance. Shit-piece thinks of himself as a God and decides the destiny of thousands of innocent but intelligent people by asking American defense to retard these innocent and intelligent people(on recommendation of many evil jews). And when people complain about crimes of these evil jews, a large cohort of jewish cronies responds by calling the victims of jewsih trickery and machinations as anti-semite.  These evil jewish scumbags are so offensive human creatures that they would happily, boldly and habitually tarnish the most sacred memory of innocent holocaust victims for their nefarious designs to retard and persecute intelligent people who are declared anti-semite only because they try to expose the truth about evil jewish cohort's attempts to retard them. Several times in the past when I tried to tell people that some evil jews were behind my persecution and told the torture stories, I was right away told that I was an anti-semite who was trying to tarnish the reputation of jews.



Again with a great due to apology to good jewish human beings, I want to tell people that due to my experiences of cruelty, torture and persecution on insinuation of evil jews, I have come to realize that throughout history there were always some jewish scumbags who had absolutely no humanity for non-jewish people and these evil jewish people always machinated to hurt other people and in the meantime brought bad name to even those jews who were good human beings. Forgive me but world follows laws of physics. I may be politically very incorrect but everything in this world follows a cause and effect. No good human being wants to wrong even a stray dog in their right mind then why were jews persecuted throughout history. I am of the opinion that there were always a group of evil jews who had no humanity for non-jews and they continued to cruelly machinate against non-jews and when their machinations became common knowledge in the respective societies, people hated even a large number of good jewish humans due to crimes of bad jews in the society and there was always a backlash that was against all the jews irrespective. 



99.9% of jews burnt in gas chambers were totally innocent and good haumn beings and were wondering rightfully why would they ever be wronged or killed by anyone in their right mind even right before their execution but the evil and machinatory ones had who brought this day on them had already left for other countries of Europe or America with all their wealth. 



I am no expert at history of jews but recently Ukraine's war brought its history to limelight and I was reading that there was a period in Ukrainian history when Polish entrusted jews to rule and collect revenue from Ukrainian public. Jews were extremely cruel in collecting the revenue and were very offensive to local population. This jewish control continued for forty or so years and polish were ousted by some other power and jewish control ended the same time. And then local population who had borne their cruelties and torture for so many decades, killed them en masse at many places in Ukraine since they had extreme anger against them. 



Again World follows laws of Physics. If Jews were so good to others, why everyone wanted to wrong them. Human beings everywhere have enough empathy to not wrong anyone if they do not have any grudges and grievances against them.



Again my thesis is that even though a large number of jews everywhere were good nice folks, there was always a group of cruel and inhuman jews who had no sympathies for non-jews and this evil group of jews always machinated to wrong other people and due to machinations of this evil group of jews, ordinary folks in the respective societies harbored grievances against jews in general (which was a very wrong thing) and persecuted them whenever they had a chance. Since world always follows cause and effect, I am not going to believe that ordinary folks in every society hated them for no reason and just persecuted them for the fun of it.



Please cherish the memory of sacred souls who were killed in holocuast but stop giving this anti-semite shit to people when you are the one who is showing cruelty to nice, good and intelligent human beings as is habitually done by a lot of evil jews these days.



I want to request all jews and non-jews that this group of evil jews again has started to machinate boldly in United States and it would be good for both Jews and non-jews to thwart this group of evil jews before this is too late.



I want to request(and suggest to good jews as a friend) to disavow any relationship with jewish scumbag billionaire and his rich jewish cohort who are involved with mind control of innocent and intelligent people of so many nations for their nefarious designs.



I also want to explain very clearly that I have been very severely criticizing bad jews and American defense but this is limited to criticism in writing only. I do not want anyone including myself to take the law in our own hands. We have to respect the human dignity of every jew and every human being including those involved in bad practices so even though I openly talk about bad people, it is not an invitation to anyone to take the law in their hands or hurt any any human being. I will continue to fight for my cause of ending mind control of innocent and intelligent people but I want people to completely respect all good jews and good people in American army and make a political struggle for the law or government actions to take their course against corrupt and evil people. I absolutely do not suggest any violence or anybody taking law in their hands.

%Post Ends%





MSNBC

NBC

CNN

Fox Business

Fox News

American Broadcasting Company

USA Network

CBS

CNBC

Fox

HLN

Blaze Media

Al Jazeera America

Discovery Channel

RT

HBO

NewsNation

MyNetworkTV

Free Speech TV

Newsmax TV

Scripps News

CNN en Español

PBS

ABC News Live

Link TV

Lifetime

VH1

France 24

Univision

ION Television

NBC News

Investigation Discovery

MeTV

DD India

ESPNews

BBC America

CNBC Europe

C-SPAN

A & E Network

Hallmark Channel

DoD News Channel

National Geographic

TNT

euronews

Sky News

Bloomberg Television



New York Times.

Washington  Post.

CNN.

Fox News.

USA Today.

Los Angeles Times.

Chicago Tribune.

Boston Globe.

Minnesota Star Tribune

New York Post

Newsday

San Fransisco Chronicle

The Dallas Morning News

Tampa Bay Times

Hartford Courant

Publick Occurrences Both Forreign and Domestick

The Michigan Daily

The Denver Post

Pittsburgh Post-Gazette

The Seattle Times

Las Vegas Sun

Bourbon County Citizen

The Register Star

NewYork Metro

The Queens Ledger

Philadelphia Tribune

Baltimore Afro-American

Portland Tribune

Indianapolis Recorder

The Patriot-News

El Diario NY

The Modesto Bee

Fairfax County Times

The Epoch Times

Barron's

Queens Chronicle

Phoenix New Times

El Informador

The Philadelphia Inquirer

New York Daily News

The Star-Ledger

St. Louis Post-Dispatch

The Mercury News

The Arizona Republic

The Plain Dealer

Detroit Free Press

The Press-Enterprise

The Tennessean

Sun Sentinel





The Copenhagen Post

The Slovak Spectator

The Budapest Times

Tirana Times

Menorca Sun

The Vienna Review

Le News

The Irish Times

Die Welt

Het Nieuwsblad

Le Soir

Albania Today

Algemeen Dagblad

De Telegraaf

de Volkskrant

The European

Het Laatste Nieuws

The Daily Telegraph

Daily Mirror

The Sun

Pravda

The Moscow Times

The Guardian

Le Figaro

Le Monde

ABC

la Repubblica

Il Messaggero

El Periódico de Catalunya

El Mundo

Libération

El País

Kronen Zeitung

La Stampa

Frankfurter Allgemeine Zeitung

Bild

20 minutes

Sport

Aftenposten

Marca

Gazeta Wyborcza

Izvestia

Die Presse

Süddeutsche Zeitung

La Tribune

Novaya Gazeta

Neue Zürcher Zeitung

Dagens Nyheter

Expressen

La Gazzetta dello Sport

Mladá fronta Dnes



Urdu News

Daily Pakistan

Dawn

Daily Express

Daily Jang

The Express Tribune

The News International

The Nation

Pakistan Today

Daily Dunya

Daily Ummat

Nawaiwaqt

The Regional Times of Sindh

Pakistan Observer

Khabrain

Daily Ausaf

Daily Jasarat

Daily Nai Baat

Daily Basharat

Daily Times

The Frontier Post

Daily Sarhad

Daily Imroze

The Pakistan Times

The Financial Daily

Daily Aaj

Daily Mashriq

Millat

Business Recorder

Daily Inqilab

Kawish

Daily Lokaai

Talár

Maidan Daily

Daily Asas

Christian Voice

The Friday Times

Awam

Daily Awami Awaz

The Star

Al Akhbar

Khyber Mail

Nawai Watan

Sajjan

Daily Hilal Pakistan

Daily Sindhu

Daily Koshish

Daily Mehran

Bhulekha

Civil and Military Gazette
```

---

## Error 36: Unbalanced $: 3

**Snippet:** `Friends, this is preliminary version of automated program that computes the Herm`

**Full content:**

```
Friends, this is preliminary version of automated program that computes the Hermite polynomial design matrix. I will change this program further and this is rather preliminary only for friends who have been following my blog for sometime now. I will come up with a final formal version soon.



I also believe that after converting the regression matrix from hermite polynomials to one with polynomials in original variables, we might need further optimization in original variables that tries to find an optimum relationship in the neighborhood of hermite implied relationship in original variables. We would want the optimization to increase R-squared without increasing degrees of freedom in the original variables polynomial. I am sure this can be done with a bit of effort. I mean neural networks are mostly all about optimization. We have a very good initial guess and many derivative based methods might work since there may not be many local minima as we are already in close neighborhood of true solution.



.

.

.

```
function [WH1] = CalculateHermiteDesignMatrixAutomated(Q,Yl,NN,OrderH)

%Q is a multidimensional array that is NN X 7 size. You can easily
%decrease or increase number of regressors from seven after understanding
%the code.
%Yl is NN sized array of regressand. One dimensional.
%OrderH is order of Hermite polynomials of every variable and is common.

%The first part of This function takes seven arrays/regressors input at joint data values in the same
%sequence. And returnd a Hermite polynomials design matrix with all Hermite polynomials
%evaluated at their data values and their possible product values. 
%You can use it anywhere in other problems if there are seven regressors.

%Second loop in this function calculates the loss of R-Squared when a
%specific variable is removed from the least squares design matrix.

%Third loop removes all those variables that are smaller than a threshold
%value and 

OrderH0=OrderH+1;

Ndata=NN;
Mtable=readtable('C:\Users\Lenovo\Documents\MATLAB\MATLAB1\MomentMatchParams08.txt');
[ZI] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable);
[W] = EvalHermiteArrayH0(ZI,OrderH);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%This part of program calculates Hermite design matrix 


for n1=0:1    
    for n2=0:1
        for n3=0:1
            for n4=0:1
                for n5=0:1
                    for n6=0:1
                        for n7=0:1
                            Bindex=[n1 n2 n3 n4 n5 n6 n7]
                            index = binaryVectorToDecimal(Bindex);
                            BBindex(index+1,:)=Bindex(:);
                            ParamsRegress(1:Ndata,index+1)=1;
                            for nn=1:7
                                if(Bindex(nn)==1)
                                    ParamsRegress(1:Ndata,index+1)=ParamsRegress(1:Ndata,index+1).*Q(1:Ndata,nn);
                                else
                                    ParamsRegress(1:Ndata,index+1)=ParamsRegress(1:Ndata,index+1).*1;
                                end
                            end                            
                                                        
                            [Paramss,Ix]=sort(ParamsRegress(1:Ndata,index+1));
                            %Wx(Ix(1:Ndata))=W(1:Ndata,1:OrderH);
                            Wx(Ix(1:Ndata),:)=W(1:Ndata,:);
                         
                            if(index==0)
                                WH(1:Ndata,1)=1;
                            elseif (index==1)
                                WH(1:Ndata,1+1:1+OrderH)=Wx(1:Ndata,2:OrderH0);
                            else
                                WH(1:Ndata,1+OrderH*(index-1)+1:1+OrderH*index)=Wx(1:Ndata,2:OrderH0);
                            end
                        end
                    end
                end
            end
        end
    end
end


Yl(1:Ndata,1)=Yl(1:Ndata);
CoeffH=(WH'*WH)$WH'*Yl);

bhs(1:NN,1)=0;
for rr=1:OrderH0+126*OrderH
    bhs(1:NN,1)=bhs(1:NN)+CoeffH(rr,1).*WH(1:NN,rr);
    %RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffL(rr,9).*WL(1:NN,rr);
end


RSquared0=1-sum((Yl(:,1)-bhs(:,1)).^2)/sum((Yl(:,1)-sum(Yl(:,1))/(NN)).^2);


str=input("Look at CoeffH");

%This part of program removes one variable at a time from Hermite design 
%matrix and calculates its effect on total R-squared.

for n1=0:1    
    for n2=0:1
        for n3=0:1
            for n4=0:1
                for n5=0:1
                    for n6=0:1
                        for n7=0:1
                            Bindex=[n1 n2 n3 n4 n5 n6 n7]
                            index = binaryVectorToDecimal(Bindex);
                            BBindex(index+1,:)=Bindex(:);
                            
                            WH0(1:Ndata,1:1+OrderH*(index))=WH(1:Ndata,1:1+OrderH*(index));
                            WH0(1:Ndata,1+OrderH*(index)+1:1+OrderH*126)=WH(1:Ndata,1+OrderH*(index+1)+1:1+OrderH*127);                            
                            
                            Yl(1:Ndata,1)=Yl(1:Ndata);
                            CoeffH0=(WH0'*WH0)$WH0'*Yl);

                            bhs(1:NN,1)=0;
                            for rr=1:OrderH0+125*OrderH
                                bhs(1:NN,1)=bhs(1:NN)+CoeffH0(rr,1).*WH0(1:NN,rr);
    
                            end


                            RSquared(index+1)=1-sum((Yl(:,1)-bhs(:,1)).^2)/sum((Yl(:,1)-sum(Yl(:,1))/(NN)).^2)

                            RSquared0
                            
                            DiffRSquared=RSquared0-RSquared(index+1)
                            
                       %     str=input("Look at change in R-squared")
                            
                            
                        end
                    end
                end
            end
        end
    end
end


%This part of the program removes those variables from hermite design matrix that
%make a smaller contribution to R-squared than a small threshold value.
%This threshold has to be different for every regressor.

RemoveCount=0;
ColCount=0;
WH1=0;
for n1=0:1    
    for n2=0:1
        for n3=0:1
            for n4=0:1
                for n5=0:1
                    for n6=0:1
                        for n7=0:1
                            Bindex=[n1 n2 n3 n4 n5 n6 n7]
                            index = binaryVectorToDecimal(Bindex);
                            BBindex(index+1,:)=Bindex(:);
                            
                            
                            DiffRSquared=RSquared0-RSquared(index+1)
                               
                            %if(DiffRSquared 0)
                                WH1(1:Ndata,ColCount+1:ColCount+OrderH)=WH(1:Ndata,ColCount+RemoveCount+1:ColCount+RemoveCount+OrderH);        
                             
                                    ColCount=ColCount+OrderH;
                                else
                                    WH1(1:Ndata,1)=1;
                                    ColCount=ColCount+1;
                                end
                            end
                            
                            
                        end
                    end
                end
            end
        end
    end
end


Yl(1:Ndata,1)=Yl(1:Ndata);
CoeffH=(WH1'*WH1)$WH1'*Yl);

size(WH1)
RemoveCount
ColCount

str=input("Look at CoeffH---00000------");




bhs(1:NN,1)=0;
for rr=1:OrderH0+(126-RemoveCount)*OrderH
    bhs(1:NN,1)=bhs(1:NN)+CoeffH(rr,1).*WH1(1:NN,rr);
    %RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffL(rr,9).*WL(1:NN,rr);
end


RSquaredNew=1-sum((Yl(:,1)-bhs(:,1)).^2)/sum((Yl(:,1)-sum(Yl(:,1))/(NN)).^2)

str=input("Look at R-Squared after removal of variables");



end


```

```

---

## Error 37: Unbalanced $: 1

**Snippet:** `Friends, here is the program used for making the graphs and other calculations g`

**Full content:**

```
Friends, here is the program used for making the graphs and other calculations given in previous post. For functions previously posted that I have not given here,  please check recent earlier posts in past few weeks.

.

.

.

```
function [] = SDEsWithMathAIMain08E8Standard()


%The mean reverting SDE is given as
%dY(t)= kappa (theta - Y(t)) dt + sigma Y(t)^gamma dZ(t)
%Y(0) = y0


%We specify Low and High SDE parameters range below.
kappaL=.25;%Lower range of kappa
kappaH=3;%Upper range of kappa
thetaL=.5;%Lower range of theta
thetaH=2;%Upper range of theta
y0L=.5;%Lower range of y0 
y0H=2;%Higher range of y0
gammaL=.5;%Lower range of gamma
gammaH=1;%Higher range of gamma
sigmaL=.1;
sigmaH=1.0;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Below five sets of uniform random numbers are sampled in batches of one
%thousand. These random numbers are later mapped on five input parameters
%over the their range previously defined. 
%Sampling is done in batches of thousands since I wanted to first simulate
%one thousand SDEs and later continue to add more batches of thousand SDEs 
%without spoiling the data of earlier batches from random number sequence.
%Since I was doing antithetic sampling, I did it at level of local batches
%of thousand.

seed=83098561;
rng(seed);
MM=5;    %No of Batches of simulation
NN0=1000;%Scenarios in each batch.
NN=MM*NN0;%Number of SDE runs in the training sample. Ideally would be much larger.

for mm=1:MM
    SampleRand(1:NN0/2,1)=rand(NN0/2,1);    
    Rand1((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand1((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.


    SampleRand(1:NN0/2,1)=rand(NN0/2,1);    
    Rand2((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand2((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);    
    Rand3((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand3((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.


    SampleRand(1:NN0/2,1)=rand(NN0/2,1);    
    Rand4((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand4((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.


    SampleRand(1:NN0/2,1)=rand(NN0/2,1);    
    Rand5((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand5((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

end


kappaU(1:NN)=kappaL+(kappaH-kappaL).*Rand1(1:NN,1);%Map unifrom random variates on kappa.

thetaU(1:NN)=thetaL+(thetaH-thetaL).*Rand2(1:NN,1);%Map unifrom random variates on theta.
  
y0U(1:NN)=y0L+(y0H-y0L).*Rand3(1:NN,1);%Map unifrom random variates on starting value of the SDE.

gammaU(1:NN)=gammaL+(gammaH-gammaL).*Rand4(1:NN,1);%Map unifrom random variates on gamma.

sigmaU(1:NN)=sigmaL+(sigmaH-sigmaL).*Rand5(1:NN,1);%Taking sigma at mid of upper and lower range.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5


SDEpaths=200000;
MOrder=16;     %Order of moment matching of standard normal random numbers for simulation in SDEs
Order=7;       %Order of hermite series that is used to represent SDE densities.

%alphas below are used for moment matching of normal random numbers.
alpha(1) =0.993024015547037;
alpha(3)= 0.008264111853961;
alpha(5)= 0.008237591744137;                   
alpha(7)= 0.006556372747340;
alpha(9)= 0.001939786779503;
alpha(11)=0.000289238364672;                   
alpha(13)=0.000019850983839;
alpha(15)=0.000000562412998;

[Zn] = StandardNormalIdealDesity02(SDEpaths,1);
[ZI] = CalculateZnAfterHermiteSeriesMultiplication(Zn,alpha,MOrder);

%ZI is a 16 moment matched version of discretized standard normal density 
%with 200000 elements. This would be used for both hermite regressions and
%monte carlo simulations.

[W] = EvalHermiteArrayH0(ZI,Order);
% W is a matrix that contains hermite polynomials evaluated at discretized
% version of standard normal density. This matrix is used for finding
% hermite series coefficients of densities of SDEs.
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Below, we define time parameters of monte carlo simulation of SDEs.

seed0=90728436;
rng(seed0, 'combRecursive')
TtM=256*2;  %Terminal time for SDE simulation, here four years.
dtM=1/64/2; %time step size for monte carlo simulations.
dt=dtM;
Sfrequency=16;%The density of every 16th time step is sampled and all 
%sampled densities till terminal time are returned in a matrix.
Random0(1:SDEpaths,1:TtM)=0;

for tt=1:TtM
%Since SDEs are simulated with different parameters in a loop. We calculate 
%moment matched normal random variates for all of the time steps just once
%and input them to SDE simulation program so we do not have to generate
%these random numbers again and again every time we simulate a different
%SDE inside the SDE simulation loop.
URandom=0;
URandom(1:SDEpaths/2)=0;
URandom=rand(size(URandom)); 
URandom(SDEpaths/2+1:SDEpaths)=1-URandom(1:SDEpaths/2);
[URandomS,I]=sort(URandom);

Random1=ZI(I);

Random0(1:SDEpaths,tt)=Random1(1:SDEpaths);
end
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Run this loop and above loop only once and save the data on disk as below.
%Then comment both these loops and keep reading the data from disk.



for nn=1:NN      
 nn
 NN
%if(nn>4*NN0) %This commented if would have to be used to specify that only
%parameters with index nn greater than 1000 would be simulated etc. 
 [coeff] = MeanRevertingMonteCarloDensity04New(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,Sfrequency);
 %[coeff,coeff2] = MeanRevertingMonteCarloDensity04(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,W2);
 Coeff(1:Order+1,1:TtM/Sfrequency,nn)=coeff(1:Order+1,1:TtM/Sfrequency);
%end

end

%save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC16.mat","Coeff")
%str=input("I have saved the densities coefficients variable--Stop");


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%You can comment the SDE simulations loop and continue to load the 
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.

%Below is my code since I was making monte carlo simulations in batches of 1000 and
%saved each batch in a different file on disk.
% % % 
% load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC.mat","Coeff")
%  str=input("I have loaded the densities coefficients variable");
%  
%  Coeff0=Coeff;
%  
%  load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC2.mat","Coeff")
%  str=input("I have loaded the densities coefficients variable");
%  
%  Coeff2=Coeff;
%  
%  load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC4.mat","Coeff")
%  str=input("I have loaded the densities coefficients variable");
%  
%  Coeff3=Coeff;
%  
%  load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC9.mat","Coeff")
%  str=input("I have loaded the densities coefficients variable");
%  
%  Coeff4=Coeff;
%  
%  
%  load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC16.mat","Coeff")
%  str=input("I have loaded the densities coefficients variable");
%  
%  Coeff5=Coeff;
%  
%  
%  Coeff(1:Order+1,1:TtM/Sfrequency,1:1000)=Coeff0(1:Order+1,1:TtM/Sfrequency,1:1000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,1001:2000)=Coeff2(1:Order+1,1:TtM/Sfrequency,1001:2000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,2001:3000)=Coeff3(1:Order+1,1:TtM/Sfrequency,2001:3000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,3001:4000)=Coeff4(1:Order+1,1:TtM/Sfrequency,3001:4000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,4001:5000)=Coeff5(1:Order+1,1:TtM/Sfrequency,4001:5000);
% 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%Dimensions of Coeff are Coeff(,1:Order+1,1:TtM/Sfrequency,1:NN).

%Below we choose one time slice between 1 and TtM for finding coefficients 
%of hermite series from Legendre regression. I have taken slice 18 that occurs at time
%18*Sfrequency*dtM. Please choose different time slices and see how the
%program works.

%
%TimeSlice variable below
Ts=13;
CoeffH0(1:Order+1,1:NN)=Coeff(1:Order+1,Ts,1:NN);%Hermite series coefficients at time slice chosen for analytics.
CoeffH=transpose(CoeffH0);

% clf;
% 
% plot((1:NN),CoeffH(1:NN,2),'g');
% 
% str=input("Look at coeffs plot --Z1 coeff");

TT=Ts*dtM*Sfrequency;%Time at end of chosen slice. This will be used in analytic calculation of SDE mean later.
%We will replace the first mean coefficient of zeroth hermite associated
%with the Hermite series of SDEs with the analytic value.

%Below we calculate square root of variance(sum of hermite coefficients squared formula) to standardize the coefficients
VarSqRt(1:NN,1)= sqrt(CoeffH(1:NN,2).^2+CoeffH(1:NN,3).^2*2+CoeffH(1:NN,4).^2*6+CoeffH(1:NN,5).^2*24+CoeffH(1:NN,6).^2*120+CoeffH(1:NN,7).^2*720+CoeffH(1:NN,8).^2*7*720);
%Below are six standardized coefficients


SHCoeff(1:NN,1:8)=CoeffH(1:NN,1:8)./VarSqRt(1:NN,1);
% SHCoeff stands for standardized hermite series coefficients.

str=input("Reached Level 1");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




for nn=1:NN

C(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
YT(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
Y0T(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
UU(nn)=C(nn).*Y0T(nn);
VV(nn)=C(nn).*YT(nn);
UV(nn)=UU(nn).*VV(nn);
qq(nn)=2*(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
BB(nn)=besseli(qq(nn),sqrt(UV(nn)));    



Q(nn,1)=C(nn).*YT(nn);
Q(nn,2)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
Q(nn,3)=C(nn).*Y0T(nn);
Q(nn,4)=gammaU(nn);
Q(nn,5)=sigmaU(nn).^2;
Q(nn,6)=thetaU(nn);

end
 
 

[Q(:,7)] = CalculateApproximateVarianceOfMRSDEs(kappaU,thetaU,y0U,gammaU,sigmaU,NN,Ts,Sfrequency,dt);


%The above is approximate variance of the SDE and its value for each of the
%NN parameters scenarios is used as seventh regressor in Legendre
%polynomial regression. This variable is time dependent and has to be
%recalculated for each time slice.



Q(:,1)=Q(:,1)./max(Q(:,1));
Q(:,2)=Q(:,2)./max(Q(:,2));
Q(:,3)=Q(:,3)./max(Q(:,3));
Q(:,4)=Q(:,4)./max(Q(:,4));
Q(:,5)=Q(:,5)./max(Q(:,5));
Q(:,6)=Q(:,6)./max(Q(:,6));
Q(:,7)=Q(:,7)./max(Q(:,7));


%Above the regression variables are ad-hoc normalized. It does not make any
%difference since regression would pick up any normalization scaling.


OrderOrig=6;
OrderOrig0=OrderOrig+1;
for qq=1:8
    Yl(1:NN,qq)=SHCoeff(1:NN,qq); %First eight standardized hermite coefficients to be predicted. 
end
Yl(1:NN,9)=VarSqRt(1:NN,1);%Square root of variance used to standardize has to be predicted as well.



%The function below returns the design matrix in original variable. This
%consists of powers of distance from the median of the variable.
[WOrig] = CalculateOrigVariableDesignMatrixAutomated(Q,NN,OrderOrig);


CoeffOrig=(WOrig'*WOrig)$WOrig'*Yl);%Original Variable polynomial coefficients 
%to predict seven variables. six standardized coefficients 
%and one square root of variance of each SDE.

str=input("Look if there is matlab warning about ill conditioned matrix inversion");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

SHCoeff(1:NN,1:8)=Yl(1:NN,1:8);

%bhs: Regressed value of standardized hermite coefficients produced from Legendre Regression %
bhs(1:NN,1:8)=0;   %
%RegressedVarSqRt: Regressed value of square root of volatility produced from Legendre Regression 
RegressedVarSqRt(1:NN,1)=0;

%Below calculate SDE hermite coefficients by regressing on original variable polynomials 
% with all calculated coefficients and polynomials evaluated at
% input data values used to find regression coefficients. This is in-sample
% testing only.
 
for rr=1:OrderOrig0+126*OrderOrig
    bhs(1:NN,1:8)=bhs(1:NN,1:8)+CoeffOrig(rr,1:8).*WOrig(1:NN,rr);
    RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffOrig(rr,9).*WOrig(1:NN,rr);
end


%Below are seven calculations of R-squared for each of 
%the standardized six coefficients and seventh value of square root of variance. 
1-sum((SHCoeff(:,1)-bhs(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)
1-sum((VarSqRt(:,1)-RegressedVarSqRt(:,1)).^2)/sum((VarSqRt(:,1)-sum(VarSqRt(:,1))/(NN)).^2)

str=input("Look at R^2s of eight standardized hermite series coefficients and ninth square root of variance");

%Since all coefficents were standardized before regression, Hermite series densities 
%calculated from them should have variance one. However, variance would be slightly 
%different from one after Legendre regression. So we calculate this
%variance of each hermite series density in regression.
VarSqRtbhs(1:NN,1)= sqrt(bhs(1:NN,2).^2+bhs(1:NN,3).^2*2+bhs(1:NN,4).^2*6+bhs(1:NN,5).^2*24+bhs(1:NN,6).^2*120+bhs(1:NN,7).^2*720+bhs(1:NN,8).^2*7*720);

%bhs0 is re-standardized estimates of predicted from regression values of hermite series coefficients
bhs0(1:NN,1)=bhs(1:NN,1);
%Restandardization below to make sure that we get unit variance of each of
%the hermite series density.
bhs0(1:NN,2:8)=bhs(1:NN,2:8)./VarSqRtbhs(1:NN,1);


1-sum((SHCoeff(:,1)-bhs0(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs0(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs0(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs0(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs0(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs0(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs0(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs0(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)
1-sum((VarSqRt(:,1)-RegressedVarSqRt(:,1)).^2)/sum((VarSqRt(:,1)-sum(VarSqRt(:,1))/(NN)).^2)


str=input("Look at R^2s of first eight standardized hermite series coefficients");

%Below plot each of the in-sample densities and re-calculate them from 
%Legendre regression and make an overlaid comparison. 
for nn=1:NN
    
    %de-standardize by multiplying with square root of variance of each
    %density and get actual predicted coefficients of hermite-series of SDE
    %densities
    ch(1:8)=bhs0(nn,1:8).*RegressedVarSqRt(nn,1);
    
    %Below we repeat the same step for original Hermite series data found
    %from simulation. These are true values of hermite series coefficients and not predicted values.
    HCoeff(1:8)=SHCoeff(nn,1:8).*VarSqRt(nn);
    
    ch(1)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));%Replacing predicted value of mean with analytic value.

    ch(1:8)
    HCoeff(1:8)
    
    nn
    str=input("Look at predicted coefficients above and true coefficietns below for nnth SDE in data: First coefficent(mean of SDE) in predicted values has been replaced by its analytic known value")
    
    
    clf;
    nn
    PlotHermiteSeriesDensityAndRvGraph(ch(1),ch(2:Order+1),'r');

    hold on

    PlotHermiteSeriesDensityAndRvGraph(HCoeff(1),HCoeff(2:Order+1),'g');
    nn

    str=input("Look at comparison of graphs of nnth density in sample--Green is data and red is our regression from Legendre Polynomial coefficients");
    clf;
end


end
```

.

.

.

```
function [WOriginal] = CalculateOrigVariableDesignMatrixAutomated(Q,NN,OrderOrig)

%Q is a multidimensional array that is NN X 7 size. You can easily
%decrease or increase number of regressors from seven after understanding
%the code.
%Yl is NN sized array of regressand. One dimensional.
%OrderH is order of Hermite polynomials of every variable and is common.

%The first part of This function takes seven arrays/regressors input at joint data values in the same
%sequence. And returnd a Hermite polynomials design matrix with all original variable polynomials
%evaluated at their data values and their possible product values. 
%You can use it anywhere in other problems if there are seven regressors.

OrderOrig0=OrderOrig+1;
Ndata=NN;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%This part of program calculates Hermite design matrix 


for n1=0:1    
    for n2=0:1
        for n3=0:1
            for n4=0:1
                for n5=0:1
                    for n6=0:1
                        for n7=0:1
                            Bindex=[n1 n2 n3 n4 n5 n6 n7]
                            index = binaryVectorToDecimal(Bindex);
                            BBindex(index+1,:)=Bindex(:);
                            ParamsRegress(1:Ndata,index+1)=1;
                            
                            %Calculate desired product
                            for nn=1:7
                                if(Bindex(nn)==1)
                                    ParamsRegress(1:Ndata,index+1)=ParamsRegress(1:Ndata,index+1).*Q(1:Ndata,nn);
                                else
                                    ParamsRegress(1:Ndata,index+1)=ParamsRegress(1:Ndata,index+1).*1;
                                end
                            end
                            
                            %Calculate MEdian
                            if(rem(Ndata,2)==0)
                                Y0=(ParamsRegress(Ndata/2,index+1)+ParamsRegress(Ndata/2+1,index+1))/2;
                            end
                            if(rem(Ndata,2)==1)
                                Y0=ParamsRegress(ceil(Ndata/2),index+1);%+Ys(Ndata/2+1))/2;
                            end

    
                            %Calculate expansion basis for each
                            %product variable
                            for mm=1:OrderOrig0
                                WOrig(1:Ndata,mm)=(ParamsRegress(1:Ndata,index+1)-Y0).^(mm-1);
                            end


                           %Arrange all above products in a single least squares design matrix 
                           if(index==0)
                               % WH(1:Ndata,1)=1;
                                WOriginal(1:Ndata,1)=1;
                            elseif (index==1)
                               % WH(1:Ndata,1+1:1+OrderH)=Wx(1:Ndata,2:OrderH0);
                                WOriginal(1:Ndata,1+1:1+OrderOrig)=WOrig(1:Ndata,2:OrderOrig0);
                            else
                               % WH(1:Ndata,1+OrderH*(index-1)+1:1+OrderH*index)=Wx(1:Ndata,2:OrderH0);
                                WOriginal(1:Ndata,1+OrderOrig*(index-1)+1:1+OrderOrig*index)=WOrig(1:Ndata,2:OrderOrig0);
                                
                            end
                            
                                                        
                        end
                    end
                end
            end
        end
    end
end


end


```

```

---

## Error 38: Unbalanced $: 1

**Snippet:** `Friends, I want to describe again what happens to victims of mind control on a r`

**Full content:**

```
Friends, I want to describe again what happens to victims of mind control on a regular basis.



First thing is that EM waves emitting devices and lasers are fitted all over my room and also in all other rooms of my family home. For example when I am having a good deep sleep which is rather unusual, they would target my head with lasers and high frequency waves and I will feel very tired when I would wake up as if I had not slept at all. Just like neurotransmitters, when molecular weights of enzymes and hormones is known , they can be targeted with resonance of appropriate frequency to not allow them in certain areas of the body or at least decrease their concentration in particular areas. For example when I had a foot fracture in 2014, they never allowed it to heal properly by targeting waves of appropriate frequencies on the fractured area. Many times when I am working in my good spirits in my room or in garage etc, the mind control agents would point high frequency lasers towards my forehead to cause pain so that I would not be able to concentrate on anything and get angry and start ranting and would not be able to work anymore. Sometimes, when they are more cautious, they would simply point EM waves with appropriate resonance to cause me to sleep or become drowsy. They change the position of a lot of devices everyday based on their anticipation of position and place where I would next work on my research and sleep.

In our house, every bed, sofa or chair that has foam on it, causes severe itch in my back when I sit on it. I think this is because they inject some chemical that settles in pores of the foam and then becomes volatile when EM waves of a particular frequency are focused on it. The volatile chemical enters the body of the mind control victim through the anus since it has "potential" to combine with some of the neurotransmitters in the body. It is extremely painful to sit on these beds, sofas or chairs. If I have to do that, I place two or three cotton pillows on top of the foam bed, sofa or chair and then sit on the pillows. I have a large double bed in my room but I never sleep on it and instead sleep on a small cot (with cotton filled quilts beneath me) in my room since it is impossible to sleep on the bed. Again sleeping on the bed causes unbearable and very large physical pain and huge itch in the anus. 

It is impossible for the victim to shower everyday since the water in the washroom is charged with mind control chemicals that make the victim feel half faint and totally energy-less. Several years ago, I discovered the water in our kitchen did not have mind control chemicals to charge the skin and I would simply take water from the kitchen to the wash room and take a rich sumptuous shower. Even though mind control was not very high at that time, they closed the loophole after a few weeks.

Soaps of all large Pakistani companies have mind control chemicals in them that charge the skin and when EM waves are focused on the face, forehead and the skin, the victims feels a completely altered consciousness and sometimes extreme anxiety and nervousness. I have been living on Indian soaps (Did we separate from India only to fill the pockets of corrupt scumbag generals of Pakistan army who take hundreds of millions in bribes from CIA and then heroically stab "dhirti mata"/motherland in its back?)

The antipsychotic drugs and injections are mixed at the manufacturing source on orders of scumbags of Pakistan army and  they have a huge deteriorating effect on the victim. They would take away all neurotransmitters from my body  they can using mind control injections and I would not be able to have a proper conversation with anyone or do any research work until 7-10 days after the injections. I would have muscular pains and other aches all over my body. Sometimes they take away some special neurotransmitters from the body and the victim would feel as if he is losing all energy in the body and the victim would have to eat something or take a drink to get better. This happens to me all the time despite my sugar tests both fasting and random and H1BAC are perfectly good. Since food is one of the only few things that can help you get better when the victim is under mind control drugs, my weight has increased beyond limits and I am 30 kg over weight now.  There were small periods when I did not take antipsychotics and my weight decreased quite fast in those periods so I expect if my antipsychotics filled with mind control drugs end, I will easily lose a lot of weight quickly.

I tried to re-start my morning walk several times last year but mind control agents tried everything in their power to deter me by taking out my neurotransmitters and even went to the limits of Police threatening me to walk not on sidewalk of  public service roads but in parks only (Police has no such authority but they can harass anyone). I have done a complete post on this harassment incident somewhere else.

They can even kill the vicitm remotely when the vicitim is under mind control drugs but the scumloads of American defense have still not done that to me.

Another very nasty thing these "proud" scumloads of American defense do is that when the vicitm goes into wash room where his penis is exposed, they use some device that throws small amount of some chemical that settles on the tip of the penis and then they target the victim with EM waves and it causes unbearable and excruciating pain. I am recalling a few older posts about this. They used to do this routinely but when my research got known well, they stopped doing it. This is from more than three or four years earlier.

This is an excerpt from post 971 written on June 01, 2019 here: [forum.wilmott.com/viewtopic.php?f=15&t=94796&start=960#p846210](https://forum.wilmott.com/forum.wilmott.com/viewtopic.php?f=15&t=94796&start=960#p846210)
> Ok, I am not complaining but I decided to write this post several days ago when I was forced on shameful and humiliating torture three days ago. They locked directed energy on the tip of my penis and it was very painful and unsettling for me. I urinated more than twenty times in two hours. I would feel better when I would be able to take a very small amount of urine out of my penis each time. They had done this two times previously for several hours but I did not write here since I thought that it was a self-humiliating exercise to tell people about my persecution like this but when they did it last time, I decided to write about it lest it becomes a common practice and starts to happen everyday. I would say again that many of these mind control people have absolutely no respect or regard for my or anybody's human dignity. I want people to recall how American army soldiers were openly urinating on prisoners in Abu-Gharib and most of the staff there knew about it but such humiliatory actions were considered perfectly normal by most of them. It was until the tapes were run on TV and news was on air everywhere that many of them started to think that we have made a mistake. Mind control agents are not very different and when they are angry about their failure in controlling me, they resort to punishing me using humiliating actions like targeting directed energy on the tip of my penis. I would like to ask Americans if such actions represent American ethics and mentality and if they do not represent American ethics I wonder why such things do not stop even after I write here openly about them. Please own your actions if you do not want to stop them.
> 
> 
> I want to ask friends that some of the mind control agents become extremely mean when they fail to control their target victim properly and they resort to such ugly tactics. For example one of the tactic mind control agents used to exercise was that they would make a very little injury/cut on my tongue with microwaves. It will not bleed but it would be constantly painful all the day since tongue is extremely sensitive. This used to happen almost every two weeks or ten days. They charged my penis this morning today, as I mentioned in post #1063 written this morning, again though it was far less severe than what I have described in the above post but such activities continue unabated and the experience this morning made me recall the horrible experience above. I want to request friends to force the mind control agencies to replace the guy who controls me as he has a very mean nature which is evident from the above post.
.

https://forum.wilmott.com/viewtopic.php?p=854970

.
> I have previously told friends that, during brain control, charged ions enter the body from every opening we have into the body. I am very sorry to write this here and want to make an apology to friends for the relatively gross nature of this post. But I would like to tell friends that  I firmly tape my penis with a paper tape to prevent charges going inside it. When I do not do this tape, my eyesight sharply deteriorates and I become extremely lethargic. There are such things I never mentioned on this forum because they are too disgusting to mention but once the torture continues, I finally decided to mention some of the things here. The way it works for the charges to go into the body, I believe, they release a small amount of very ionizable gas in the air and charge a pathway through gaseous air with laser beams towards the body, for example towards the mouth, nose or the anus and apply potential across it. At the same time, they create opposite potential by ionizing the chemicals that have gone into the body with food using microwave resonance caused by laser beams. And then chemicals mixed with ionized gas start to go inside the body from the anus etc and this becomes a self-sustaining process as long as the potential is maintained at both ends. I have seen a lot of such instances over past twenty years of persecution when chemicals will zap inside through the anus causing severe pain. I believe flow of charges is really directly proportional to applied potential and pathway conductivity caused by the ionized gas.  I keep some soft tissues in my anus as it helps. I have tried other things that could more firmly block the anus but then mind control agents greatly increase the potential and it causes extreme pain and minor seepage like bleeding(it might possibly be because of very high frequency microwaves). Mind control agents love such torture tricks that prevent people from doing anything that blocks their mind control. I also tried other tricks like lubricating the anus but they would simply and freely add mind control chemicals that would charge the body to the creams and lotions in the supermarkets just like they drug the food on the shelves. I am sure these practices are done all over the world since adding chemicals to creams and lotions was widely done when I was in UK for six months and even upscale chains like body shop and others had ionizing chemicals added to their creams and lotions once mind control agents would suspect that any such shop could fall on my way. 
> 
> Ok, mind control agents in Pakistan had been making anywhere between 10-40 million dollars per year depending upon how good the year had been for mind control operations. These agents want to continue mind control one way or other. These agents tell their like-minded hardliner right wing bosses that there are certain things I never mention in my writing of the journal (because they are probably too disgusting to write) and these are the things mind control agents need to apply for my mind control since people would not know about these practices when they would not be written in the journal. A few weeks ago I mentioned briefly that they cause severe itching in my back/anus but then I never wrote about it again even though it continued. They almost always have charges going into the body of the target from the back but sometimes it becomes very painful. And yesterday, it was again so painful that several times I would step up from the chair while working on my research, open my pants and rub and scratch my anus and replace the tissue that has already been charged but they would continue to increase potential again and again and I would be repeating the whole thing again. I also woke up several times at night due to sheer itching in my anus. 
> 
> I had talked about reprieve from gas in my room in the previous post but I fear that might have been because for past three to four days before writing of that post, I did not leave the home for long and mind control agents might not have enough opportunity to come to my home and recharge the ionizing and resonance laser beams and refill the gas because I remained in the neighborhood very close to home and returned quickly.
> 
> I want to request all good American people to force their government to stop such inhuman, cruel and  animal barbaric practices on other humans only because some powerful people in US do not like intelligent muslims/others to excel and use their influence to continue such animal practices that hurt the image of American people and such practices are becoming more and more of a norm with every passing year. Sorry to say but there are good and bad people everywhere in every country, culture and religion and US is no exception. In US where many bad people do not openly do bad things because being cruel to other humans is really not appreciated by the American society, but when evil and cruel people know that their cruelties would not be noticed by the general american people, they are very ready to expose their true nature and use the methods of cruelties and persecution when they are sure these things would not be noticed by the American people. These evil, bad and cruel but powerful people have no regard for the goodwill of American people but just want to use their influence in US right wing to extend their personal agendas. I am very sure if all of these things would be known to American people in their true entirety, none of these mind control persecutions would ever take place.
.

Post 1370 on this thread.

.
> Friends, I drove from Islamabad to Kot Addu today. It took me around eight hours to reach kot Addu. Long drives are very stimulating and I thought of several new ideas both about SDEs and stocks trading. But when I reached Kot Addu, I had extreme uneasiness in my penis since mind control agents continued to charge my penis on the way as I had to be in the same accurately predictable position for many hours sitting in the driving seat. After reaching home, I urinated again and again to feel better but it did not work. I also realized that my urine was reddish as there was blood mixed with urine as I urinated. 
> 
> When they force electromagnetic waves inside the penis, the body tissues inside the penis tube get damaged and blood starts to seep through the tissues and gets mixed with urine. Forcing waves into the penis is a very important part of mind control since it is impossible to control adrenaline and dopamine without controlling the sex organ. Adrenaline and dopamine give us drive to concentrate and force ourselves to work hard so mind control agents really have to control these and several other similar neurotransmitters and they have to force waves into our penis to be able to do that. 
> 
> I normally do not like to urinate in the wash room since when I urinate there, it is very easy for them to force high frequency waves inside the penis and it feels like a needle is going into the penis when urine is coming out and high frequency waves are going inside. I would rather take a mineral water bottle and urine into it in my room and drop the urine in the wash room and wash the bottle to use again. But if I would remain in a single place in my room to urinate, they install gadgets and urinating in my room is no different from urinating in the wash room as they can again force waves into the penis and the target victim would have needle like feeling going into the penis so I have to continue to change places randomly in my room to urinate. 
> 
> Anyway they were doing the same thing again and blood was coming out of my penis mixed with urine as I supposed the inside of tube that carries urine out of our body was damaged due to high frequency waves. This is very serious thing so I decided to write about it so as to deter the mind control crooks who are bringing a great name to American people by such feats. But these hardliner conservative crooks in army will continue their ugly antics since their desire to enter the paradise of Jewish billionaire godfather is stronger than regard for any country or any human ethics.
> 
> Previously I had told friends several times (may be eight or nine times in total) that they force chemicals into my mouth when I am sleeping. This is sheer science though I do not know underlying exact details but I know they can create potential at a precise place for special types of ions(neurotransmitters) emitted from elsewhere with lasers and EM waves. Well I continued to mention that they charge my mouth every night with special mind control chemicals that settle on my tongue and inside of upper jaw and my mouth is very bitter and I have to wash it or brush inside of my mouth to feel better. I continued to mention it again and again on this forum but they never stopped so I stopped writing about it.
> 
> I want to tell Americans that Americans are mostly not bad people at all but these hardliner conservative crooks in army and mind control who are dying to enter the paradise of the jewish billionaire godfather are not bringing any good name to Americans with their inhuman machinations.
> 
> Another thing I have mentioned several times before is that I find likes on several linkedin posts (in my activity) that I never liked. They know my passwords and have enough control over my computer and they repeatedly like something I never liked (I never like anything unless I strongly feel about it which is usually relatively rare). This is something that gets known to me since there is a log of every like in my Linkedin activity. Imagine what else they are doing from my internet traffic that I never came to know.
Another big problem is that when I approach people all over the world for consulting projects, the scumloads of American defense reach them as well with their infrastructure in that particular country and threaten people to not work with me or give me any project. Depending upon the nature of person, they would tell some particular lie so that they would not be willing to work with me at all. In past 14 years, I have only earned 3500 dollars.



I have tried to hold despite all odds and tried to do good research. If things were as good as with other people free from mind control, I would have been able to do far better research. From my side, I am not enemies with anyone and would like everyone to use my research and make money utilizing it.



Again the The rich anal jews including the jewish billionaire are extraordinarily pleased when they hear these torture stories and reward the scumloads of American defense (who are ready to do any nasty, disgusting or degrading thing to other humans to prove their allegiance to rich jews). These scumloads of American defense, whose arrogance pierces through the seventh sky, would do every anal and disgusting thing to innocent and intelligent victims in order to please the rich jewish cohort who would in turn reward them with great jobs and high social status in successful jewish companies and these scumloads of American defense have absolutely no regard for anybody's human diginity once rich jews have beaconed them to retard someone.



Friends, when I returned from United States, I was taken to a military psychiatrist in Rawalpindi who immediately diagnosed me of very acute schizophrenia and gave me an antipsychotic Larjectil along with other biweekly injections. This drug is known to cause drug induced jaundice in some of the patients. After seeing the doctor in Rawalpindi, I was brought home in Kot Addu where I lived for four or five months without seeing any doctor in the meantime while taking a steady dose of Larjectil. However after a few months my color and eyes became totally pale even though I was not feeling anything odd other than probably strange color of my stool. However one month further later my condition became very bad and I started to become very weak physically. When everybody became alarmed, I was taken again to the same psychiatrist in Rawalpindi who immediately knew that I had jaundice and immediately stopped my medication. I was still feeling reasonable but the nightmare was yet to follow. Within a few days of stopping the drugs, I had so severe itch in my body that it is totally hard to describe. I could not sleep for a whole month due to sheer itch. I simply could not resist it at all and there were blood marks all over my legs and arms due to itching. And I was given a glucose drip every day with medicine for more than a month but my biluribin continued to increase instead of decreasing. And then doctors decided to give me two glucose drips everyday and only then after two and half months months (a total of three and a half to four months) after starting two glucose drips that my biluribin came close to normal. This was one of the worst times of my life.

Later probably in 2017, I was taken to another psychiatrist the second time. This psychiatrist had earlier given me electric shocks without interviewing me in order to retard me in year 2001. When I was taken to this psychiatrist again in 2017, he knew from my history that most antipsychotics had failed in retarding me and he wanted to give me Larjectil again. He was told that Larjectil had previously backfired and I had extremely severe drug induced jaundice but the psychiatrist bitterly wanted to experiment and told everyone that it was not necessary that the drug would cause jaundice every time. And within a few weeks, I was extremely pale all over and my medication had to be stopped. However for several years, many of my major enzymes remained disturbed and elevated despite that bilurbin had become normal. I think that severely weakened my liver and now in the tests, friends can notice that several liver enzymes are highly elevated.

I used to try to eat healthy but everything I would eat consistently, the scumbags of Pakistan army would go after the company that manufactures that food and ask them to add mind control chemicals to it. I really like taking a glass or two of packaged Yogurt everyday. On insistence of CIA, Mir Jafirs and Mir Sadiqs (scumbag generals of Pakistan army) of our nation approached every yogurt manufacturing company and now it is totally impossible to find a brand of Yogurt that does not contain mind control chemical in it. I simply cannot take healthy yogurt anywhere anymore. Similarly for milk, I really liked to take some milk every day or two since it is healthy and I would also add it to tea, but now there is no single brand of packaged milk or tea whiteners that does not contain mind control drugs. And then I used to really drink a lot of freshly squeezed juices especially in winters since they are so wholesome and absolutely cheap when there is abundance of fruit. But then Mir Jafirs and Mir Sadiqs(scumbag generals of Pakistan army) of my country would send their thullahs (sepoys) to every food stall or juice shop in the city and give them mind control chemicals and ask them to add to some ingredient and continue to add to everybody's food freely. Similarly there is not a single large brand of water that is without mind control chemicals despite that temperature has regularly been going to a high of 115F to 125F. 

I usually take pepsi-cola or coca-cola in glass bottles that have to be returned to shop after drinking. There are probably eight major types of drinks in these bottles and earlier usually one or two types used to be good and one would have to really work to find which kind of bottle is good in this month. But when I started drinking these bottles, all manufacturers started supplying good Pepsi-cola and coca-cola drinks in the city because they realized that these drinks are extremely bad for my health. Many times when temperature is around 120F, I might have no option other than to drink a cola to get better. They never allowed water, milk or Yogurt to get better but all colas became good in past two months. Water bottled by Pepsi-cola and Coca-cola and Nestle is very thoroughly drugged and never became better after January this year.

I believe that mind control become difficult to work when people take enough calcium. This is why scumbags of American defense(under Jewish billionaire's command) have to make sure that all yogurt, milk and other sources of calcium are totally kept drugged with mind control chemicals. Almost all calcium supplements manufactured by different Pharma companies have mind control drugs in them. I still remember about a week ago I bought a Calcium supplement from Cell LAboratories and thought that I had never come across it before. I knew most supplements are not good but I thought I should try it and I took one tablet in the shop right after buying the supplement and in a few minutes I was ranting all over about evil of jews and biden's mockery of justice to please the jews and there was no end to my rants. When I was composed after twenty minutes, I took the remaining tablets to the shop and returned them telling that they had caused very severe headache. 

Similalry selenium is very important for proper working of Thyroid but I cannot take any multivitamins since all of them are drugged on orders of scumbag Mir Jaffars and Mir Sadiqs of my nation to please CIA. 

For many naiive people who still believe in goodness of scumbags of American defense, I will like to tell them that I there were several times in past few years when I became sick and had huge fever. I have had very severe dengue and also corona and many times just plain high fever. And whenever I would be extremely sick, mind control agents would increase mind control several fold. I think they would take it as a window of opportunity to possibly be able to permanently block my neurotransmitters when my mind is in a weakened state and my body is not working properly. I really think that the reason behind increasing mind control when I would be sick is definitely that they believe that it might become possible for them to accomplish in weakened state of my body and mind what they have otherwise failed to accomplish. So much so for the humanity of these scumbags.  



My country is firmly in grip of tentacles of Jewish Octopus(of billionaire jewish bastard and his rich cohort)  who are not ready to let anyone become successful here due to their venom. And there are many such other countries. These bad jews have restarted their machinations as they always did in their history and when their will be a backlash they will all start whining that everybody persecutes us for no reason despite that we are so good.



I believe that it is good for every society including US to stop these jewish machinations in their tracks and try to teach them to respect the dignity of other human beings who are not jewish. We do not want these scumbags to be treated in any inhuman way and we do not want any human being to be treated with the extraordinary cruelty of these scumbags. Even if they are incapable of respecting other human beings, I think it is important and good for all of us in the society to force them to give enough respect to to others and not allow a free hand to their machinations. As opposed to American defense that has already become a puppet in hands of this bad jewish cohort. We do not want anyone getting wronged and we do not want any backlash to anyone.



People do not believe in me. They want to find out the truth on their own. Do not believe in google or random articles on internet.



Ask the history experts in your university why jews were persecuted throughout history? Was there a persistent cause and effect behind there repeated persecutions. Or different people just took a liking to persecuting them and had fun.



I am not validating any persecution of jews and certainly not holocaust which was one of the darkest chapters of humanity. Everything has to be dealt with law and with enough human decency and respect for human dignity. 



But why was it so easy to turn Germans against jews? Just because they had become too rich? 



I do not believe in any political correctness and would like to know the actual true reasons behind it. Even before period preceding Second world war, Jews had seen many rises and falls in Europe. It would be good to know from true history experts what were the reasons behind their repeated persecutions.



A poet says that cup of life continues to get stronger as it passes from generation to generation. Because every generation learns from experience of all previous generations that had passed.



We want to know true history so that we can know true facts about what happened about so many different things and do not repeat mistakes of the past and be able to stop those things that would later become far worse in light of history. So if jews were always persecuted when they were innocent, we want to be very careful that it never happens. And if they were persecuted due to their machinations, we want to make sure we never allow them to express their machinatory side again. 



Tens of thousands of people majority of whom were actually American citizens have been retarded by American defense in past two decades on insinuation of a Jewish billionaire and his rich jewish cohort. American defense loves this because all the high ranking officials involved in this massacre are given extremely high paying jobs in Jewish companies after they retire and they enjoy extremely high social status and therefore they love to retard anyone who the billionaire and his jewish cohort points towards. Bad Jews have complete control of most vital Arm of American government -- American defense. Once somebody's (including Americans) neurotransmitters get known early in their student life before they have become successful, mostly the decision is up to jews to allow them to succeed or ask American defense to retard them by putting them on mind control for the rest of their life. It is easiest to retard intelligent people in their student life since most of them have absolutely no resources and most other people still do not know whether they could be extremely successful in their later life as clearly as mind control agency and associated Jews get to know and therefore a lot of lies could be fabricated by American defense and told as a reason for retarding the victim. And it is only people who are supposed to become quite successful that are retarded. For example many muslims who might have actual venom for jews would almost never be touched at all despite that many jews might know about them but muslims who are predicted to become very successful are always retarded with an iron fist. Again majority of people retarded are not Muslims and rather are typical American citizens who have special neurotransmitters.



Please ask for a free and fair Judicial commission to investigate retarding of innocent human beings and punish any culprits in American defense and Jewish actors behind them. Is justice only to punish menial criminals who have to be jailed because they snatch money after days of hunger to get some food? Or go after the real and true criminals who are reworking the fabric of American nation with their extreme meanness and exceptional cruelty. But even though everybody wants to go after the petty criminals very forcefully and with complete might of the law, not many people in any society however advanced have courage to ask about trial of big crocodiles who commit great crimes against humanity with complete impunity. Really interesting and rather ironic.



I know that some of American friends and other people may not like my expressing myself honestly without any political correctness. I want to tell Americans as I have said several times on this forum previously that I admire so many things about good American people. Americans are a good, nice and decent people who like to work hard and are some of the most enterprising people on earth. And I always think that American values coincide with all the good things and practices that intelligent humanity appreciates all over the world. 



And I am indebted to quite a few good Americans who tried to protect me from persecution when absolutely nobody in my own country was ready to help me. They appreciated my talent and gave me a new life by forcing American government to be better with me. This is a debt I can never repay all my life. 



The purpose of my honest criticism is never to malign Americans and on the contrary I would like to tell everyone that most American people are some of the best human beings on earth and they would abhor the idea of wronging anyone with great cruelty. But still there are good and some bad people in every country and in every part of the world.



I want to request good natured Americans to please let me write openly on this forum about mind control. I have been writing on this forum against mind control for many many years now. Many good American people tried to verify my claims about involvement of jews in mind control on their own and were rightly very alarmed when they got to know the complete truth. And bad jews (the subset of jews associated with mind control of innocent people under command of this jewish billionaire) know that there is enough awareness in American society about their crimes. And this deters them from openly starting mind control of many intelligent young people who were otherwise likely potential victims of their mind control activity. I really believe that possibly thousands of people have been spared from mind control in past few years because bad jews and American defense have become far more aware that some good people are really keeping an eye on their activity despite that it is difficult to do anything against jews (however bad)  when every other US politician is dying to meet Netanyahu. 



So please let me expose these scumbags (bad jews only) and as I expose their crimes and their exceptional cruelty, many of these bad actors actors have to pretend to be good and really have to decrease their mind control activity which spares the life of hundreds if not  thousands of innocent and intelligent people (majority of who are Americans) who would have been made target of mind control otherwise.



Mind control guy was telling me that American defense wanted to machinate to increase her reach in India by installing mind control infrastructure on major indian roads and cities. And Indian puppets were moved to convince the Indian authorities that only evil people would be controlled and relationship with America would dramatically improve after allowing mind control. However due to my writing on this forum, a lot of indians got to know the true nature of mind control and decided to not allow any large scale installation of mind control infrastructure in India. So I am extremely happy to know that a lot of good, innocent and intelligent Indians would be spared the fate I had to go through. Though I am a very proud Pakistani, I consider myself a second Indian since all of this part of the subcontinent used to be just one India.



Similarly a lot of intelligent Europeans who would have been retarded were spared since there was a greater awareness there about true nature of mind control and reasons behind it and at many places the governments stopped cooperating with American defense to retard their own people.



So please let me openly speak against the evil of mind control and about scumbags behind mind control. Because for most Americans saying anything against the cruel mind control of evil jewish cohort would instantly earn them the label of anti-semite and all the politicians lining up to meet Natanyahu would turn against them. 



I again assure people that I have absolutely nothing against Jews who are unassociated with mind control and I totally respect them and purpose of my writing is only to end cruel mind control of good, innocent and intelligent people on hands of mean and cruel people.





%Post Starts%



Please read posts 1893, 1894, 1895 and 1896 together to see how a prestigious bank in Pakistan stole $ 2500 from my account on orders of CIA. When I was in London in 2010-11, Lloyds TSB also stole my thousand pounds. They go to the limits of using banks to strip innocent people of their money and most banks silently comply.

You can see the bank statements as proof of theft by the Pakistani bank. Following four posts and download the PDF bank statement.

https://forum.wilmott.com/viewtopic.php?t=99702&start=1890#p876174



Read here about theft by Lioyds TSB:



https://forum.wilmott.com/viewtopic.php?t=99702&start=1890#p876182



I am very sure that my speaking against corrupt banks will protect many innocent individuals in the society because in most of the places in the world banks continue to deceive innocent people when ordered by military agencies. 



We are all aware that I have made an allegation of theft on Lloyds TSB. I want Lloyds TSB to either accept responsibility for theft and deception or sue me for maligning them openly on internet.



I am sure my writing about corrupt practices of the banks will save many innocent individuals like me because even many prestigious banks all over the world are ready to cheat and deceive innocent citizens when asked to do so by military agencies.

%Post Ends%





%Post Starts%

I want friends to please protest to American defense that has become a puppet in the hands of rich jews. Scumbags of American defense consider successful Muslims a stain on social fabric of United States. I am just a Muslim by birth and do not believe in any religion and there are thousands of Muslims like me that are kept on mind control by American defense to prevent them from being successful. And majority of such victims are  American born Muslims who are like other natives of US even though I was admittedly a foreigner. Black sheep in American defense behind mind control are given very prestigious jobs paying millions of dollars in Jewish companies after they retire and rich jews want to block talented muslims from being successful in United States with an iron fist since they are afraid that if some muslims become successful, they would start wielding some influence and start opposing American policies in Israel and they want to nip this supposed evil in the bud. And American defense has no dearth of wannabees who desperately want to join the ranks of so many others who have gotten extremely high paying jobs with great social status in jewish companies after retirement from American defense. Please do not blindly believe me and find out somebody in your social circle(or well known to somebody in your social circle) you know well and who is in mind control agency of US defense and ask them about my allegations and your eyes would open forever about role of rich jews in United States and how they openly use mind control on anyone they wish especially on a large number of even white Americans whose families have been living in US for hundreds of years. If your eyes do not open forever, I am ready to take any blame you wish. 



Especially very talented American people in science and technology are forced to work in Jewish owned companies due to fear of mind control. Many such people who want to leave are coldly told by administration to leave but their mind control is initiated by American defense on insistence of jews right after they leave the jewish company and once they know the reason behind mind control was that they tried to leave the jewish company against the will of the company owners. And due to large number of such precedents well known to many professionals in many jewish companies, most of the very talented people do not dare to leave the jewish companies against the will of administration since they know very well that they would be instantly put on mind control by American defense who dances on the tunes of rich jews since they want extremely high paying prestigious jobs with jewish companies having great social status. Please do not believe a single word I say blindly but try to find out the actual truth on your own from authentic sources you know well and you will find the truth that would open your eyes forever.



Not everybody is the same, there are at the same time a large number of jews who have nothing to do with any of this and many good jewish companies who do not follow any inhuman practice. But there is a close group of rich jews who are actually involved in large scale mind control with American defsnse working as their proxy. Please try to know the truth on your own.



I want to advise American defense to watch a lot of American movies and try to behave like heroes in those movies. Instead people in American defense are short-tempered scumbags who became belligerent when anybody criticizes them. Contrary to American and Western spirit of freedom of criticism and speech that we all cherish, these short-tempered scumbags are unwilling to tolerate anything other than eulogies based on complete lies. Just like Henry Ford used to say that you can buy any color of car as long as it is black, to these scumbags of American defense the freedom of speech means that you can say anything you like as long it is a eulogy otherwise they become belligerent and start moving thousands of people to silence someone who speaks the truth about them. Let us all of us start cursing Erdogan together now.

%Post Ends%







%Post Starts%

I want to request Pakistanis abroad and at home to please let some Pakistani investigative reporters and other journalists know about my thread on Wilmott. Please also inform dawn, Jang, business recorder, tribune, ARY news and all other Pakistani newspapers so that they could come to know how our army systematically fails Pakistani talent in return from bribes from CIA and American Army. This is how crooks in our army buy islands in New Zealand and properties in Belgium. There are more than 500 very talented Pakistanis who are kept constantly on mind control by our army. They have continued to do this over past twenty years since Pervaiz Musharraf came to power. If bastards in our army had not retarded intelligent Pakistanis, there would be many very successful international enterprises coming from our country and we would still be at Par with India and Bangladesh in per capita income who were much behind in per capita income 25 years ago and today are much ahead of us. This is since our army continues to darken the future of our nation in return for hundreds of billions of rupee generals are given by CIA. This is probably one of the most successful operations by CIA to silently fail an entire nation.



I want to request Pakistanis abroad and at home to please tell brave journalists and others like Hamid Mir, Aitezaz Ahsan, Latif Khosa, factfocus people, and other prominent people in political parties and government that readers of my blog can think about my thread. Every chief of our army lives abroad after retirement. But we want to live in our country forever and build our "dhirti Maan" as famously quoted by Latif Khosa.



I want to say again that if I have survived to say this today, it is only due to help and support from good American people.  Most of the good American people  have a lot of humanity for us and they always want our poor nations to progress. Good people in United States supported me when nobody in my own country was ready to support me. American people are not a bad people at all and they do not support any mind control in our nations or their own nation. 

However large armies in most countries are composed of corrupt crooks only. China, America, Pakistan, Russia. All these countries have large corrupt armies. American army for example plays in hands of rich Jews among other forms of rampant corruption. So please be careful to not generalize my posts about corrupt American army and defense to good American people.

%Post Ends%





%Post Starts%

This is also a relevant post I copied from past.  https://forum.wilmott.com/viewtopic.php?t=99702&start=1965#p876890



Many friends who are used to formal language all the time might be disturbed by my use of slang expletives for bad people but after reading Einstein's letter to Marie Curie, I consider myself perfectly validated to use the word of scum for American army and for bad jews who have no ethics and are ready to fall to every low level of humanity for some material gain or due to their hatred, venom, poison or malice as in case of bad jews. 



Even though American society keeps jews in very high regard, they are not gold-plated. Just like any other people or race, some of them are extremely good human beings, some of them are extremely evil and some of them simply do not care. They tend to be more intelligent and when this intelligence shows itself in the form of Einstein we see one of the greatest human beings ever born but when this intelligence turns evil and machinatory we have exactly opposite form of humanity like evil jewish billionaire godfather/goldfather and his rich jewish cohort who has taken complete control of American army to advance their nefarious designs and have retarded thousands of innocent and intelligent people they did not like. So respect has to be shown in abundance to good people but very carefully to evil people. When great respect is shown to evil people, they become even more emboldened to advance their agendas based on hatred, venom,  poison and malice.



When I was undergraduate I had transferred to US after two years and in my last year I lost all interest in engineering and my GPA composed of only two years was very bad so I had to go to a not so good school for masters in Economics. But I had decided to work very hard and I was confident that with my hard work I will succeed again. But some third class malicious jews at the university got slighted by my talent for mathematics. These evil jews were very aware of mind control even in 1997 and jewish billionaire had already great influence in US army at that time. I was just like a boy working hard to find my future that all of a sudden, from nowhere, the stone of mind control fell on my head. When mind control agencies told malicious jews that I had several special neurotransmitters, the malicious jews were completely resolved to force mind control on me at all cost. US Defence was already a puppet in hands of evil jewish billionaire and when mind control guys knew that billionaire was taking special interest in my mind control, they were extremely enthusiastic to please him and do all sort of efforts to retard me.



I want to tell friends that American army, due to pressure from evil jewish billionaire, had appointed one or two jews from academia from my graduate university who were enthusiastic about retarding me and they are the ones who take key decisions about what to do with me. They continue to think in my brain for several hours every day and completely remain in touch with all progress in mind control on a daily basis. All cruelties and torture that was unleashed on me was in their complete knowledge and was authorized by them on suggestions of mind control agents.

Over past thirty years, lot of bad jews have developed a network in academia(with absolute apology to all the great jewish people in academia) and when a victim has to be retarded most of the jews in the network start orchestrating totally complete lies about the victim so that good people think that retarding the victim is indeed is a very good thing. 



Several other smart people are paid by American army to keep thinking in my brain and they remain oriented with what I am doing. For example, if there is something silly in my work, these people who are keeping track of my programs already inform the jewish network and this jewish network starts spreading fun about my work several days in advance. As my research progresses and my programs are updated, several people have access to my programs and its logic several days in advance before I post them in public.



And I want to tell people that this network of evil jews has greatly perfected itself over past thirty years and not only muslims are retarded, everyone they do not like including europeans, blacks and a large number of white talented Americans are retarded at whim by this network of emboldened evil jews. 

I want to request all good people in American society and in european countries to end and thwart this gang of evil jews who are bent on retarding intelligent people of every nation and creed they do not like.



I am sure that intolerant and arrogant scum of American army will again resort to torture and violence and start focusing their lasers on my temple, eyes, teeth and ears.

%Post Ends%





%Post Starts%

Friends very sorry for so many off-topic posts. This is the last post on the persecution topic for now. I will be getting an antipsychotic injection in a few hours now. And I will try to avoid this topic unless there is some other development in my persecution or some threat by army etc. I will go back to technical work and try to post new things about my research but I may not be able to do good work for next 10-15 days due to effect of injection.

I am copying this last post (for now) from the past. I will try my best to revert to my research work now and post about it.



The following post is composed of my own genuine thoughts why Jews were wronged so many times throughout history.

https://forum.wilmott.com/viewtopic.php?t=99702&start=2145#p879442



Friends, I am very sorry to have come to this point to be forced to write this post. 

Please read what I have been trying to say since so many years. https://forum.wilmott.com/viewtopic.php?f=15&t=101453

People know that despite my brutal, cruel and sadistic persecution on hands of rich American jews that has now lasted for 25 years, I always tried to mention very carefully that all jews are not bad people and a large number of them are very good human beings. 



And in order to avoid offending the jews who are good human beings, many times in the past, I had been very careful to not say my mind about bad and evil jews in United States. Now there is this evil jewish billionaire who is Godfather/Goldfather of mind control, who is an exact example of what happens when scum makes big money by chance. Shit-piece thinks of himself as a God and decides the destiny of thousands of innocent but intelligent people by asking American defense to retard these innocent and intelligent people(on recommendation of many evil jews). And when people complain about crimes of these evil jews, a large cohort of jewish cronies responds by calling the victims of jewsih trickery and machinations as anti-semite.  These evil jewish scumbags are so offensive human creatures that they would happily, boldly and habitually tarnish the most sacred memory of innocent holocaust victims for their nefarious designs to retard and persecute intelligent people who are declared anti-semite only because they try to expose the truth about evil jewish cohort's attempts to retard them. Several times in the past when I tried to tell people that some evil jews were behind my persecution and told the torture stories, I was right away told that I was an anti-semite who was trying to tarnish the reputation of jews.



Again with a great due to apology to good jewish human beings, I want to tell people that due to my experiences of cruelty, torture and persecution on insinuation of evil jews, I have come to realize that throughout history there were always some jewish scumbags who had absolutely no humanity for non-jewish people and these evil jewish people always machinated to hurt other people and in the meantime brought bad name to even those jews who were good human beings. Forgive me but world follows laws of physics. I may be politically very incorrect but everything in this world follows a cause and effect. No good human being wants to wrong even a stray dog in their right mind then why were jews persecuted throughout history. I am of the opinion that there were always a group of evil jews who had no humanity for non-jews and they continued to cruelly machinate against non-jews and when their machinations became common knowledge in the respective societies, people hated even a large number of good jewish humans due to crimes of bad jews in the society and there was always a backlash that was against all the jews irrespective. 



99.9% of jews burnt in gas chambers were totally innocent and good haumn beings and were wondering rightfully why would they ever be wronged or killed by anyone in their right mind even right before their execution but the evil and machinatory ones had who brought this day on them had already left for other countries of Europe or America with all their wealth. 



I am no expert at history of jews but recently Ukraine's war brought its history to limelight and I was reading that there was a period in Ukrainian history when Polish entrusted jews to rule and collect revenue from Ukrainian public. Jews were extremely cruel in collecting the revenue and were very offensive to local population. This jewish control continued for forty or so years and polish were ousted by some other power and jewish control ended the same time. And then local population who had borne their cruelties and torture for so many decades, killed them en masse at many places in Ukraine since they had extreme anger against them. 



Again World follows laws of Physics. If Jews were so good to others, why everyone wanted to wrong them. Human beings everywhere have enough empathy to not wrong anyone if they do not have any grudges and grievances against them.



Again my thesis is that even though a large number of jews everywhere were good nice folks, there was always a group of cruel and inhuman jews who had no sympathies for non-jews and this evil group of jews always machinated to wrong other people and due to machinations of this evil group of jews, ordinary folks in the respective societies harbored grievances against jews in general (which was a very wrong thing) and persecuted them whenever they had a chance. Since world always follows cause and effect, I am not going to believe that ordinary folks in every society hated them for no reason and just persecuted them for the fun of it.



Please cherish the memory of sacred souls who were killed in holocuast but stop giving this anti-semite shit to people when you are the one who is showing cruelty to nice, good and intelligent human beings as is habitually done by a lot of evil jews these days.



I want to request all jews and non-jews that this group of evil jews again has started to machinate boldly in United States and it would be good for both Jews and non-jews to thwart this group of evil jews before this is too late.



I want to request(and suggest to good jews as a friend) to disavow any relationship with jewish scumbag billionaire and his rich jewish cohort who are involved with mind control of innocent and intelligent people of so many nations for their nefarious designs.



I also want to explain very clearly that I have been very severely criticizing bad jews and American defense but this is limited to criticism in writing only. I do not want anyone including myself to take the law in our own hands. We have to respect the human dignity of every jew and every human being including those involved in bad practices so even though I openly talk about bad people, it is not an invitation to anyone to take the law in their hands or hurt any any human being. I will continue to fight for my cause of ending mind control of innocent and intelligent people but I want people to completely respect all good jews and good people in American army and make a political struggle for the law or government actions to take their course against corrupt and evil people. I absolutely do not suggest any violence or anybody taking law in their hands.

%Post Ends%
```

---

## Error 39: Unbalanced $: 1

**Snippet:** `Above output in previous program uses the matlab code below  .  .  ``` function `

**Full content:**

```
Above output in previous program uses the matlab code below

.

.

```
function [] = SlidingWindowZSeriesEstimation()


TT=500;
seed=15898837;

seed=98831629;

[X1] = ProduceSDEDataTimeSeries(TT,seed);


NIntervals=15;  %Intervals used to estimate moments


plot((1:TT),X1(1:TT),'g');
str=input("Look at graph of Time Series variable X");


for tt=(1+NIntervals):TT
    muA(1:4)=0;
    for nn=1:NIntervals
        dXt=X1(tt-NIntervals+nn)-X1(tt-NIntervals+nn-1); %Moments are calculated for dX(t)
        muA(1:4)=muA(1:4)+(dXt.^(1:4))/NIntervals;
    end

    [c(1,tt),c(2:4,tt),FittedMoments] = CalculateZSeriesDensityFromRawMoments02M4(muA,0);
 
    c
    %str=input("Look at new Coeffs");

end

% save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\DynamicCoeffs01.mat","c");
% 
% str=input("I have saved dynamic coeffs");
% 
% 
% load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\DynamicCoeffs01.mat","c");




bnm1=EstimateDynamicCoeffParameters(c(1,:));
bnm2=EstimateDynamicCoeffParameters(c(2,:));
bnm3=EstimateDynamicCoeffParameters(c(3,:));
bnm4=EstimateDynamicCoeffParameters(c(4,:));


bnm1
bnm2
bnm3
bnm4

str=input("Please look at 2D Z-series of four dynamic coefficients above");


%c
clf;
yyaxis left
plot((1:TT),X1(1:TT),'g')
ylabel('Random Variable X')
xlabel('Time Intervals')
yyaxis right
plot((1+NIntervals:TT),c(1,1+NIntervals:TT),'b');

hold on
yyaxis right
plot((1+NIntervals:TT),c(2,1+NIntervals:TT),'r');
ylabel('Coefficients c0 and c1 of Z-series of X')

title("Graph of time series X and first two Coefficients of its Z-series, c0 and c1");
legend('X','c0','c1','Location','northeast');
%plot((1:TT),X1(1:TT),'g',(1+NIntervals:TT),c(1,1+NIntervals:TT),'b',(1+NIntervals:TT),c(2,1+NIntervals:TT),'r',(1+NIntervals:TT),c(3,1+NIntervals:TT),'k',(1+NIntervals:TT),c(4,1+NIntervals:TT),'m');
str=input("Look at graph--final");



clf;
yyaxis left
plot((1:TT),X1(1:TT),'g')
ylabel('Random Variable X')
xlabel('Time Intervals')
 hold on
yyaxis right
plot((1+NIntervals:TT),c(3,1+NIntervals:TT),'k');
ylabel('Coefficients c2 of Z-series of X')

title("Graph of time series X and third coefficients of its Z-series, c2");
legend('X','c2','Location','northeast');

str=input("Graph--Fianl--2")


clf;
yyaxis left
plot((1:TT),X1(1:TT),'g')
ylabel('Random Variable X')
xlabel('Time Intervals')
hold on
yyaxis right
plot((1+NIntervals:TT),c(4,1+NIntervals:TT),'m');
ylabel('Coefficients c3 of Z-series of X')

title("Graph of time series X and fourth coefficient of its Z-series, c3");
legend('X','c3','Location','northeast');

end


```

.

.

.

```
function [bnm] = EstimateDynamicCoeffParameters(X)

Ndata=length(X)-1;
Order=7;


%Calculate transition dX
for nn=1:Ndata
    dX(nn)=X(nn+1)-X(nn);
end

%Below Calculate Z-series of X and dX.

[CoeffX,ZX,RSquared1] = CalculateActualZSeriesFromData(X,Order);
[CoeffdX,ZdX,RSquared2] = CalculateActualZSeriesFromData(dX,Order);



Ymu1(1:Ndata,1)=dX(1:Ndata);
dXcorr(1:Ndata,1)=0;
[W1] = EvalHermiteArrayH0(ZX(1:Ndata),Order);
        %Below, do the regression to find the coefficients of part of dX
        %random variable that is correalted with X.
coeff1=inv(W1'*W1)*(W1'*Ymu1);
        %Below, we evaluate the correalted part of dX random variable
        %with X by summing over all the hermite polynomials out
        %to Order.
for hh=0:Order 
            %Below dXcorr continues to sum corelated part over all hermites of X
            
      dXcorr(1:Ndata,1)=dXcorr(1:Ndata,1)+coeff1(hh+1,1).*W1(1:Ndata,hh+1);
            
end

%Below, we calculate orthogonal part of DX that is uncorrelated with dX

dXdecorr(1:Ndata,1)=Ymu1(1:Ndata,1)-dXcorr(1:Ndata,1);


%Below calculat moments of correalted (with X)  part and orthogonal (with respect to X) part of dX 
for kk=1:8
    rMudecorr(kk)=sum(dXdecorr(1:Ndata,1).^kk)/Ndata;
    rMucorr(kk)=sum(dXcorr(1:Ndata,1).^kk)/Ndata; 
end


rMudecorr
rMucorr
%dXcorr
%dXdecorr

%str=input("Look at decorrelated part moments");


NMoments=6;
Iterations=20000;

%The function below finds the 2D Z-series of orthogonal part of dX.

[bnm,ObjFunc] = ZSeriesCoeffsFromMomentsIterativeNoiseTerm2D01A(rMudecorr,NMoments,Iterations);



end


```

.

.


```
function [bnm,ObjFunc] = ZSeriesCoeffsFromMomentsIterativeNoiseTerm2D01A(rMu,NMoments,Iterations)


%This program computes coeffs of Z-series when values of raw moments are
%given using Iterative method. 

%rMu are raw moments;

%Hermite Series Form is      

% 
% Y=  +(bnmh(1,2) + bnmh(2,2)* Z1 + bnmh(3,2)* (Z1^2-1) + bnmh(4,2)* (Z1^3-3*Z1))* Z2
%     +(bnmh(1,3) + bnmh(2,3)* Z1 + bnmh(3,3)* (Z1^2-1) + bnmh(4,3)* (Z1^3-3*Z1))* (Z2^2-1)
%
% Equivalent 2D Z-series form is 
% Y=   (bnm(1,1) + bnm(2,1) Z1 + bnm(3,1) Z1^2 + bnm(4,1) Z1^3)
%     +(bnm(1,2) + bnm(2,2) Z1 + bnm(3,2) Z1^2 + bnm(4,2) Z1^3) Z2
%     +(bnm(1,3) + bnm(2,3) Z1 + bnm(3,3) Z1^2 + bnm(4,3) Z1^3) Z2^2
% 
% 
% Var(Y)= bnmh(1,2).^2 + bnmh(2,2).^2 + 2* bnmh(3,2).^2 + 6* bnmh(4,2).^2
%        +2*(bnmh(1,3).^2 + bnmh(2,3).^2 + 2* bnmh(3,3).^2 + 6* bnmh(4,3).^2)
% 
%     
%     
% bnm(1,1)= -bnmh(1,3) + bnmh(3,3)  
% bnm(2,1)= -bnmh(2,3) + 3* bnmh(4,3)  
% bnm(3,1)= -bnmh(3,3)
% bnm(4,1)= -bnmh(4,3)    
%     
% bnm(1,2)= bnmh(1,2) - bnmh(3,2)  
% bnm(2,2)= bnmh(2,2) - 3* bnmh(4,2)  
% bnm(3,2)= bnmh(3,2)
% bnm(4,2)= bnmh(4,2)
% 
% bnm(1,3)= bnmh(1,3) - bnmh(3,3)  
% bnm(2,3)= bnmh(2,3) - 3* bnmh(4,3)  
% bnm(3,3)= bnmh(3,3)
% bnm(4,3)= bnmh(4,3)


%We have used the notation
%cH0=bnmh(1,2);
%cH(1)=bnmh(2,2);
%CH(2)=bnmh(3,2);
%CH(3)=bnmh(4,2);
%cH(4)=bnmh(1,3);
%cH(5)=bnmh(2,3);
%CH(6)=bnmh(3,3);
%CH(7)=bnmh(4,3);

% SO We will use the equations


% cH0=1-sqrt(cH(1).^2 + 2*cH(2).^2 + 6*cH(3).^2+2*(cH(4).^2 + cH(5).^2 + 2*cH(6).^2 + 6*cH(7).^2));
% 
% 
% bnm(1,1)= -cH(4) + cH(6);  
% bnm(2,1)= -cH(5) + 3*cH(7);  
% bnm(3,1)= -cH(6);
% bnm(4,1)= -cH(7);    
%     
% bnm(1,2)= cH0 - cH(2);  
% bnm(2,2)= cH(1) - 3*cH(3);  
% bnm(3,2)= cH(2);
% bnm(4,2)= cH(3);
% 
% bnm(1,3)= cH(4) - cH(6);  
% bnm(2,3)= cH(5) - 3*cH(7);  
% bnm(3,3)= cH(6);
% bnm(4,3)= cH(7);    
    
    
   


    
mOrder=NMoments;         %Number of raw moments in calibration.      

%%%%Standardize the Raw Moments

                  %Find central Moments from raw moments  
[Mu1,cMu] = ConvertRawMomentsToCentralMoments(rMu,mOrder);
                  %Find standardized Moments from central moments  
sMu(1)=0;
sMu(2)=1;
sMu(3)=cMu(3)/cMu(2).^1.5;
sMu(4)=cMu(4)/cMu(2).^2.0;
sMu(5)=cMu(5)/cMu(2).^2.5;
sMu(6)=cMu(6)/cMu(2).^3.0;
%sMu(7)=cMu(7)/cMu(2).^3.5;
%sMu(8)=cMu(8)/cMu(2).^4.0;

%cH(1)=1;

SeriesOrder=7;
cH(1:SeriesOrder)=0;
cH(1)=.001;%.05
%%%%%%Choose the iteration step size.

for nn=1:3
    DeltaX(nn)=.00125/sqrt(factorial(nn+1));
end
for nn=4:7
    DeltaX(nn)=.00125/sqrt(factorial(nn+1-3))*2;
end



%%%Weights on objective function that shows fit to moments
w(NMoments)=1;
for nn=NMoments-1:-1:1
    w(nn)=w(nn+1)*(nn+1)*(nn+2);
end

w(3)=w(3)*2;
w(5)=w(5)*2;
w(4)=w(4)*1;

    


cH0=sqrt(1-(cH(1).^2 + 2*cH(2).^2 + 6*cH(3).^2+2*(cH(4).^2 + cH(5).^2 + 2*cH(6).^2 + 6*cH(7).^2)));



bnm(1,1)= -cH(4) + cH(6);  
bnm(2,1)= -cH(5) + 3*cH(7);  
bnm(3,1)= -cH(6);
bnm(4,1)= -cH(7);    
    
bnm(1,2)= cH0 - cH(2);  
bnm(2,2)= cH(1) - 3*cH(3);  
bnm(3,2)= cH(2);
bnm(4,2)= cH(3);

bnm(1,3)= cH(4) - cH(6);  
bnm(2,3)= cH(5) - 3*cH(7);  
bnm(3,3)= cH(6);
bnm(4,3)= cH(7);    


SeriesOrder10=4;
SeriesOrder01=3;

[Moments] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMoments);

Moments
%str=input("Look at Moments");


[ObjFuncBest] = CalculateObjMoment(sMu,Moments,w,mOrder);

cHBest=cH;

ImproveFlag(1:SeriesOrder)=1;
ImproveFlagPrev(1:SeriesOrder)=0;
ImproveCount=0;


for mm=1:Iterations
AdjustFlag=0;
    %mm
    %First 500 iterations try to fit three moments only
    if(mm=500)&&(mm=4000)&&(mm=10000))
        SeriesOrder1=1;
        SeriesOrder2=7;
        NMoments=6;
        mOrder=NMoments;
        
        
        %Block Below: Once we move from fitting five moments to six moments
        %Best Objective Function changes and becomes larger. This
        %has to be reset at the start of six moments optimization.
        %We also increase the weight associated with already
        %calibrated third, fourth and fifth moment is increased so 
        %that stays in calibration
        if(mm==10000)
        SeriesOrder10=4;
        SeriesOrder01=3;
        
        [Moments] = Calculate2DSeriesMoments(bnmBest,SeriesOrder10,SeriesOrder01,NMoments);
        cH=cHBest;
        w(3:5)=4*w(3:5);
        [ObjFuncBest] = CalculateObjMoment(sMu,Moments,w,mOrder);
        ObjFuncBest
        %str=input("I am in here NMoments =6 ");
        AdjustFlag=1;
        end
    end 
    
    for nn=SeriesOrder1:SeriesOrder2  
        
        ImproveFlagPrev(nn)=ImproveFlag(nn);    
        
        cinH=cH;
        cinH(nn)=cinH(nn)+DeltaX(nn);
        
        
        %Below lines keep the total variance equal to one.
        CondFlag=1;
        VarYP=cinH(1).^2 + 2*cinH(2).^2 + 6*cinH(3).^2+2*(cinH(4).^2 + cinH(5).^2 + 2*cinH(6).^2 + 6*cinH(7).^2);
        if(VarYP>1)
            cinH=cinH/sqrt(VarYP)*.98;
            %CondFlag=0;
        end
        
        cinH0=abs(sqrt(1-(VarYP)));
        
        %Convert to 2D Z-series Coeffs from Hermite Coeffs
        
        bnm(1,1)= -cinH(4) + cinH(6);  
        bnm(2,1)= -cinH(5) + 3*cinH(7);  
        bnm(3,1)= -cinH(6);
        bnm(4,1)= -cinH(7);    

        bnm(1,2)= cinH0 - cinH(2);  
        bnm(2,2)= cinH(1) - 3*cinH(3);  
        bnm(3,2)= cinH(2);
        bnm(4,2)= cinH(3);

        bnm(1,3)= cinH(4) - cinH(6);  
        bnm(2,3)= cinH(5) - 3*cinH(7);  
        bnm(3,3)= cinH(6);
        bnm(4,3)= cinH(7);    
 
        
        SeriesOrder10=4;
        SeriesOrder01=3;
        
        [Moments] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMoments);
                
        [ObjFunc] = CalculateObjMoment(sMu,Moments,w,mOrder);
        
        if((ObjFunc1)
                cinH=cinH/sqrt(VarYP)*.98;
                %CondFlag=0;
            end

            cinH0=abs(sqrt(1-(VarYP)));

            %Convert to 2D Z-series Coeffs from Hermite Coeffs
            bnm(1,1)= -cinH(4) + cinH(6);  
            bnm(2,1)= -cinH(5) + 3*cinH(7);  
            bnm(3,1)= -cinH(6);
            bnm(4,1)= -cinH(7);    

            bnm(1,2)= cinH0 - cinH(2);  
            bnm(2,2)= cinH(1) - 3*cinH(3);  
            bnm(3,2)= cinH(2);
            bnm(4,2)= cinH(3);

            bnm(1,3)= cinH(4) - cinH(6);  
            bnm(2,3)= cinH(5) - 3*cinH(7);  
            bnm(3,3)= cinH(6);
            bnm(4,3)= cinH(7);    


            SeriesOrder10=4;
            SeriesOrder01=3;

            [Moments] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMoments);
            
            [ObjFunc] = CalculateObjMoment(sMu,Moments,w,mOrder);
            if((ObjFunc10)&&(ObjFuncBest==ObjFuncBestBefore))
        ResetFlag=1;
    end
    ObjFuncBestBefore=ObjFuncBest;
    %DeltaX
    %ImproveCount
    
    end
    if(ResetFlag==1)
     %  DeltaX=DeltaX*5; 
        
    end
    
    ImproveFlag0=0;
    for nn=1:SeriesOrder
       if(ImproveFlag(nn)==1)
           ImproveFlag0=1;
           ImproveCount=ImproveCount+1;
       end
    end
    for nn=2:SeriesOrder
        if(ImproveFlag0==0)
            DeltaX(nn)=DeltaX(nn)*.95;
            ImproveCount=0;
        end
    end
    if(ImproveCount>4)
       for nn=2:SeriesOrder
            DeltaX(nn)=DeltaX(nn)*1.05;
       end
    end 
    
    end
    
end

bnm=bnmBest;
[Moments] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMoments);

Moments
sMu

str=input("Look at comparison of Standardised model moments and Standardized target moments")

bnm=bnm*sqrt(cMu(2));

[Moments] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMoments)
rMu

str=input("Look at comparison of model raw moments and target raw moments")


end
```


.

.

.

```
function [mu1,cMu] = ConvertRawMomentsToCentralMoments(Mu,mOrder)

%cu
%mu
% %mOrder
%str=input('Look at numbers');
mu1=Mu(1);
for mm=2:mOrder
    cMu(mm)=0;
    for jj=0:mm
        if(jj==0)
            cMu(mm)=cMu(mm)+ (-1)^(mm-jj).*factorial(mm)/factorial(jj)/factorial(mm-jj)*1*mu1.^(mm-jj);
            
        else
            cMu(mm)=cMu(mm)+ (-1)^(mm-jj).*factorial(mm)/factorial(jj)/factorial(mm-jj)*Mu(jj)*mu1.^(mm-jj);
            
        end
    end
end


```

.

.

.

```
function [Moments1D] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMomentsX)






X(1:SeriesOrder10*NMomentsX-NMomentsX+1,1:SeriesOrder01*NMomentsX-NMomentsX+1,NMomentsX)=0;
X(1:SeriesOrder10,1:SeriesOrder01,1)=bnm(1:SeriesOrder10,1:SeriesOrder01);
anm=bnm;
SeriesOrder20=SeriesOrder10;
SeriesOrder02=SeriesOrder01;


EZ=EZZ2();
Moments1D(1)=0;
for nn=1:SeriesOrder10
    for mm=1:SeriesOrder01
        Moments1D(1)=Moments1D(1)+bnm(nn,mm).*EZ(nn).*EZ(mm);
    end
end

for nn=1:NMomentsX-1

[cnm,EX0] =SeriesProduct2DAlgorithmicNew(bnm,anm,SeriesOrder10,SeriesOrder01,SeriesOrder20,SeriesOrder02);
    
SeriesOrder20=SeriesOrder20+SeriesOrder10-1;
SeriesOrder02=SeriesOrder02+SeriesOrder01-1;

%size(cnm)
%SeriesOrder20
%SeriesOrder02
%nn+1
%str=input("Look at sizes of result of moments");



X(1:SeriesOrder20,1:SeriesOrder02,nn+1)=cnm(1:SeriesOrder20,1:SeriesOrder02);
anm=cnm;    
Moments1D(nn+1)=EX0;
end



end          


```

.

.

.

```
function [cc,EX] =SeriesProduct2DAlgorithmicNew(aa,bb,SeriesOrder10,SeriesOrder01,SeriesOrder20,SeriesOrder02)



SeriesOrder30=SeriesOrder10+SeriesOrder20-1;
SeriesOrder03=SeriesOrder01+SeriesOrder02-1;

cc(1:SeriesOrder30,1:SeriesOrder03)=0;

for nn1=1:SeriesOrder30
    if(nn1<=SeriesOrder10)
        nn3=nn1;
    else
        nn3=SeriesOrder10;
    end
    for nn2=1:SeriesOrder03
        if(nn2<=SeriesOrder01)
            nn4=nn2;
        else
            nn4=SeriesOrder01;
        end    
        for jj1=1:nn3
            if(nn1-jj1+1 <=SeriesOrder20) 
                for jj2=1:nn4
                    if(nn2-jj2+1 <=SeriesOrder02)
                        cc(nn1,nn2)=cc(nn1,nn2)+aa(jj1,jj2).*bb(nn1-jj1+1,nn2-jj2+1);
                    end
                end
            end
        end
    end
end


[EZ] = EZZ2();


EX=0;
for nn1=1:SeriesOrder30
    for nn2=1:SeriesOrder03
        EX=EX+cc(nn1,nn2).*EZ(nn1).*EZ(nn2);
    end
end




end
```

.

.

.

```
function [ObjMomentOut] = CalculateObjMoment(Moment0,Moment,w,MOrder)

ObjMomentOut=0;
for nn=1:MOrder
    ObjMomentOut=ObjMomentOut+(Moment(nn)-Moment0(nn)).^2.*w(nn);
end


end


```

.

.

.




```
function [Wh] = EvalHermiteArrayH0(Z,Order)

%Evaluates first Order-th hermites at the array of Z's. If input array of Z
%has a size of 100 and Order is 4, it will return a 100 X 5 array.

Hz=HermitePoly(Order);

Wh(1:length(Z),1:Order+1)=0;
for nn=1:Order+1
    Wh(:,nn)=0;
    for mm=1:nn
        Wh(:,nn)=Wh(:,nn)+Hz(nn,mm).*Z(:).^(mm-1);
    end
end

end


```

.

.

.


```
function [EZ] = EZZ2()

EZ(1)=1;
EZ(2)=0;
EZ(3)=1;
for nn=4:96 %Increase for larger products.
    if rem(nn,2)==0
        EZ(nn)=0;
    else
        EZ(nn)=EZ(nn-2)*(nn-2);
        EZ(nn);
    end
end
% EZ(64)
% EZ(64).*EZ(64)

end


```

.

.

.


```
function [Hz] = HermitePoly(Order)
Hz(1:Order+1,1:Order+1)=0.0;
Hz(1,1)=1.0;
for k=1:Order
    for m=1:k
       Hz(k+1,m+1)=Hz(k,m);
       if (m>1)
            Hz(k+1,m-1)=Hz(k+1,m-1)-(m-1)*Hz(k,m);
       end
    end
end

end


```


.

.

.


```
function [Coeff,Zy,RSquared] = CalculateActualZSeriesFromData(Yin,Order)

Ndata=length(Yin);

Hz=HermitePoly(Order);  
MeanYin=sum(Yin(1:Ndata))/Ndata;
%Ys=sort(Yin);
%MedianYin=(Ys(Ndata/2)+Ys(Ndata/2+1))/2;

Ym(1:Ndata)=Yin(1:Ndata)-MeanYin;
%Y(1:Ndata)=Yin(1:Ndata)-MedianYin;
YmVar=sum(Ym(1:Ndata).^2)/Ndata;
Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);


%Mtable=readtable('C:\Users\Lenovo\Documents\MATLAB\MATLAB1\MomentMatchParams08.txt');
%[ZI] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable);


[Zn] = StandardNormalIdealDesity02(Ndata,1);
%[ZI] = CalculateZI(Zn);


ZI=Zn;
%Below W is the design matrix for least squares regression i.e the matrix
%that contains all the hermite polynomials calculated at ideal normal
%density grid of size Ndata. 
[W] = EvalZArrayZ0(ZI,Order);

%W
%W0=W;
%W(:,1:Order)=W0(:,2:Order+1);
%We first sort the data so that we can assign one appropriate Z-grid
%point(and associated hermite polynomials calculated at that grid point)
%to each data element. This ideal normal density Z-grid is
%constructed so that its size is equal to data observations count. We
%suppose that first derivative of random variables with repsect to Z
%does not switch sign meaning that increasing values of data
%observations have to aligned with increasing values of ideal normal
%density grid.
[Ys,I]=sort(Y(1:Ndata));
%In the line below, the data sort is reversed so that now the ideal 
%normal density grid elements assigned to various observations of random 
%variable face it on data observations index. For details, Please look 
%on interent the definition of matlab sort command with role of "I" 
%in output and how it alters the index.   
Zs1(I(1:Ndata))=ZI(1:Ndata);
%Below the values to be regressed facing the design matrix are assigned
Ymu(1:Ndata,1)=Ys(1:Ndata);
%Below, implement least squares regression.
coeff=(W'*W)$W'*Ymu);

size(coeff)
coeff
str=input("Look at coeff size");

%Store in coefficietns array of all random varaibles
Coeff(1:Order+1)= coeff(1:Order+1,1);
%Store the associated Z in Z-array of all coefficients.   
Zy(1:Ndata)=Zs1(1:Ndata);


[W2] = EvalZArrayZ0(Zy,Order);

Coeff(1:Order+1)=Coeff(1:Order+1).*sqrt(YmVar);
Coeff(1)=Coeff(1)+MeanYin;

Coeff
%Coeff(1)=Coeff(1)+MedianYin;

Coeff2(:,1)=Coeff(:);
X=W2*Coeff2;
size(W2)
size(Coeff2)
size(X)
 RSquared=1-sum(((Yin(:)-X(:,1)).^2))./(YmVar*Ndata)
 %1-sum((aa(:,1)-b0(:,1)).^2)/sum((aa(:,1)-sum(aa(:,1))/(NN)).^2)

end
```





.

.
```

---

## Error 40: Unbalanced $: 19

**Snippet:** `Friends, this post is to explain 2D Z-series and 2D Hermite series in more detai`

**Full content:**

```
Friends, this post is to explain 2D Z-series and 2D Hermite series in more detail. This is preliminary to understand yesterday's matlab program.  I will make another post explaining details of yesterday's matlab program.



Friends, I have given a good introduction to 1D Z-series and Hermite Series in my paper here: [https://papers.ssrn.com/sol3/papers.cfm ... id=4933283](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4933283)

You have to read that if you are not familiar with Z-series and Hermite-series at all. (SSRN froze the counter of my paper on instructions from CIA so when you download it, please see if download counter moves.)



Here I give a primer on 2D Z-series and Hermite series.





A Primer on 2D Z-series and 2D Hermite Series 





Why Both Hermite Series and Z-series



The Hermite series representation of a particular order is algebraically equivalent to Z-series representation of the same order. There are many analytics on non-Gaussian random variables like transformation of random variables using Taylor series, multiplication of random variables, calculation of moments and cross-moments where a Z-series representation is more useful. While there are some other analytics associated with correlations, variances and conditional expectation of non-Gaussian random variables where Hermite-Series representation would be more useful. In most of our numerical algorithms, we will have to continue to switch between Z-Series of a random variable and its equivalent Hermite series.



Two Dimensional Z-series



A Two dimensional Z-series expansion can be made for a non-gaussian random variable that depends upon more than one sources of uncertainty. Both $Z_x$ and $Z_y$ are two uncorrelated and independent standard Gaussians. 

A Two dimensional Z-series can be written as

\begin{equation}

X(Z_y\,,\,Z_x)\,=\, \sum\limits_{n=0}^{N}\,\, \sum\limits_{m=0}^{M}\, b_{n,m}\,{Z_y}^n\,{Z_x}^m 

\end{equation}



An explicit example of a 3 X 3 2D Z-series is given below. 



\begin{align}

X(Z_y \, , \, Z_x)\, &=\,\Big[ b_{0,0} \, + \, b_{0,1} \, Z_x \,+\, b_{0,2} \, {Z_x}^2 \,\, + \, b_{0,3} \,{Z_x}^3\,\, \Big] \\

&+\, \Big[ \, b_{1,0} \, + \, b_{1,1} \,Z_x \,+\, b_{1,2} \, {Z_x}^2\, \, + \, b_{1,3} \,{Z_x}^3\,\, \Big] \, Z_y \, \\

&+\, \Big[ \, b_{2,0} \, + \, b_{2,1} \,Z_x \,+\, b_{2,2} \, {Z_x}^2\, \,  + \, b_{2,3} \,{Z_x}^3\,\, \Big] \, {Z_y}^2 \, \\

&+\, \Big[ \, b_{3,0} \, + \, b_{3,1} \,Z_x \,+\, b_{3,2} \, {Z_x}^2\,  \, + \, b_{3,3} \,{Z_x}^3\, \Big] \,  {Z_y}^3\, 

\end{align}



Two Dimensional Hermite Series



A two dimensional Hermite Series can be written as

\begin{equation}

X(Z_y\,,\,Z_x)\,=\, \sum\limits_{n=0}^{N}\,\, \sum\limits_{m=0}^{M}\, bh_{n,m}\,H_n(Z_y)\,H_m(Z_x) 

\end{equation}



An explicit example of a 3 X 3 2D Hermite series is given below.



\begin{align}

X(Z_y \, , \, Z_x)\, &=\, \Big[\, bh_{0,0} \, + \, bh_{0,1} \,H_1(Z_x) \,+\, bh_{0,2} \, H_2(Z_x) \,\, + \, bh_{0,3} \,H_3(Z_x)\,\Big] \\

&+\, \Big[ \, bh_{1,0} \, + \, bh_{1,1} \,H_1(Z_x) \,+\, bh_{1,2} \, H_2(Z_x) \, + \, bh_{1,3} \,H_3(Z_x)\, \Big] \, H_1(Z_y) \, \\

&+\, \Big[ \, bh_{2,0} \, + \, bh_{2,1} \,H_1(Z_x) \,+\, bh_{2,2} \, H_2(Z_x) \, \, + \, bh_{2,3} \,H_3(Z_x)\, \Big] \, H_2(Z_y) \, \\

&+\, \Big[ \, bh_{3,0} \, + \, bh_{3,1} \,H_1(Z_x) \,+\, bh_{3,2} \, H_2(Z_x) \, + \, bh_{3,3} \,H_3(Z_x)\, \Big] \, H_3(Z_y) \, 

\end{align}



Hermite Series are very convenient for analytics associated with correlations, variances and conditional expectation of non-Gaussian random variables. Since variance of nth order hermite polynomial is given as $n!$, using the orthogonality property of hermite polynomials, we can easily calculate the variance of above 3 X 3 hermite series as



\begin{align}

Var(X)\, &=\, {bh_{0,1}}^2 \,+\, 2\,{bh_{0,2}}^2 \,+\,6\, {bh_{0,3}}^2 \,\\

&+\, {bh_{1,0}}^2 \,+\, {bh_{1,1}}^2 \,+\, 4\,{bh_{1,2}}^2 \,+\,6\, {bh_{1,3}}^2 \,\\

&+\, 2\,{bh_{2,0}}^2 \,+\,2\, {bh_{2,1}}^2 \,+\, 4\,{bh_{2,2}}^2 \,+\,12\, {bh_{2,3}}^2 \,\\

&+\, 6\,{bh_{3,0}}^2 \,+\,6\, {bh_{3,1}}^2 \,+\, 12\,{bh_{3,2}}^2 \,+\,36\, {bh_{3,3}}^2 \,\\ 

\end{align}







Product and Moments of Z-series Random variables



Product of 2D Z-series follow exactly the algebra behind the product of Two dimensional power series where we multiply the two series and algebraically collect the coefficients with same powers of $Z_x$, and $Z_y$ and the cross products of $Z_x$, and $Z_y$. 



In order to take moments, we take the appropriate product of two dimensional Z-series and then apply expectation on powers of standard normals. 

For calculation of products and moments of random variables, we have to use their Z-series and when we have their hermite series given, we would have to convert them to two dimensional Z-series and then find the desired products and moments . We cannot easily do the calculations of products and moments directly in 2D Hermite series representations.  



Taylor Series of 2D Z-series Random variables.



We can find functions of two dimensional Z-series random variables by applying multidimensional Taylor series to them. We have to apply Taylor series of random variables on their Z-series representation. We use a very small toy expansion only to second order since multidimensional Taylor series quickly become very cumbersome. We have to find automated algorithms for multidimensional Taylor series calculation of functions of multi-dimensional Z-series. Let us write a Toy 2D Taylor expansion of a random variable below as



\begin{align}

& f(X(Z_y,Z_x)\,=\, \Biggr[ f(X(0,0)) +f'(X) \frac{\partial X}{\partial Z_x} Z_x+1/2 \Big(f''(X) \frac{\partial X}{\partial Z_x}^2+f'(X) \frac{\partial^2 X}{\partial {Z_x}^2} \Big) Z_x^2+O[Z_x]^3 \Biggr]\\

&+\Biggr[\,f'(X) \frac{\partial X}{\partial {Z_y}  }+\left(f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial X}{\partial {Z_y}  }+f'(X) \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}\right) Z_x \\

&+\left(\left(1/2 f^{3}(X) \frac{\partial X}{\partial Z_x}^2+f''(X) \frac{\partial^2 X}{\partial {Z_x}^2} \right) \frac{\partial X}{\partial {Z_y}  }+f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}+1/2 f'(X) \frac{\partial^2 X}{\partial {Z_y} \partial{Z_x}^2 } \right) Z_x^2+O[Z_x]^3  \Biggr]Z_y \\

&+\Biggr[\,1/2 \left(f''(X) \frac{\partial X}{\partial {Z_y}  }^2+f'(X) \frac{\partial^2 X}{\partial {Z_y}^2  } \right) \\

&+1/2 \left( f^{3}(X) \frac{\partial X}{\partial Z_x} \frac{\partial X}{\partial {Z_y}  }^2+2 f''(X) \frac{\partial X}{\partial {Z_y}  } \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}+f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial^2 X}{\partial {Z_y}^2  }+f'(X) \frac{\partial^3 X}{\partial {Z_y}^2 \partial {Z_x}}\right) Z_x \\

&+1/2 \Biggr(1/2  \Big( f^{4}(X) \Big[{\frac{\partial X}{\partial Z_x}}\Big]^2+f^3(X) \frac{\partial^2 X}{\partial {Z_x}^2} \Big) \Big[{\frac{\partial X}{\partial {Z_y}  }}\Big]^2+2 f^3(X) \frac{\partial X}{\partial Z_x} \frac{\partial X}{\partial {Z_y}  } \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}} \\

&+f''(X) \Big( \Big[\frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}\Big]^2+\frac{\partial X}{\partial {Z_y}  } \frac{\partial^2 X}{\partial {Z_y} \partial{Z_x}^2 } \Big) \\

&+1/2 \Big(f^{3}(X) \Big[\frac{\partial X}{\partial Z_x}\Big]^2+f''(X) \frac{\partial^2 X}{\partial {Z_x}^2} \Big) \frac{\partial^2 X}{\partial {Z_y}^2  }+f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial^3 X}{\partial {Z_y}^2 \partial {Z_x}}+1/2 f'(X) \frac{\partial^4 X}{\partial {Z_y}^2 \partial{Z_x}^2 } \Biggr) Z_x^2+O[Z_x]^3 ) \Biggr]Z_y^2+O[Z_y]^3

\end{align}



From this Taylor expansion, just like we did for one dimensional  composition of functions, we can find a function that is applied to a two dimensional Z-series and matches it to another different two dimensional Z-series. Suppose two dimensional Z-series of a target random variable is given with known coefficients as as



\begin{align}

Y(Z_y \, , \, Z_x)\, &=\,\Big[ b_{0,0} \, + \, b_{0,1} \, Z_x \,+\, b_{0,2} \, {Z_x}^2 \,\,\,\, \Big] \\

&+\, \Big[ \, b_{1,0} \, + \, b_{1,1} \,Z_x \,+\, b_{1,2} \, {Z_x}^2\, \,\, \Big] \, Z_y \, \\

&+\, \Big[ \, b_{2,0} \, + \, b_{2,1} \,Z_x \,+\, b_{2,2} \, {Z_x}^2\, \,\, \Big] \, {Z_y}^2 \, \\

\end{align}



Then We can match the powers of two dimensional composition of Z-series and the target Z-series to find



\begin{align}

b_{0,1}\,&=\,f'(X) \frac{\partial X}{\partial Z_x}\\

b_{0,2}\,&=\,1/2 \Big(f''(X) \frac{\partial X}{\partial Z_x}^2+f'(X) \frac{\partial^2 X}{\partial {Z_x}^2} \Big) \\

b_{1,0}\,&=\,f'(X) \frac{\partial X}{\partial {Z_y}  } \\

b_{1,1}\,&=\,\left(\,(f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial X}{\partial {Z_y}  }+f'(X) \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}\right) \\

b_{1,2}\,&=\,\left(\left(1/2 f^{3}(X) \frac{\partial X}{\partial Z_x}^2+f''(X) \frac{\partial^2 X}{\partial {Z_x}^2}\right) \frac{\partial X}{\partial {Z_y}  }+f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}+1/2 f'(X) \frac{\partial^2 X}{\partial {Z_y} \partial{Z_x}^2 } \right) \\

b_{2,0}\,&=\, 1/2\, \left(\, f''(X) \frac{\partial X}{\partial {Z_y}  }^2+f'(X) \frac{\partial^2 X}{\partial {Z_y}^2  } \right) \\

b_{2,1}\,&=\,+1/2 \,\left(f^{3}(X) \frac{\partial X}{\partial Z_x} \frac{\partial X}{\partial {Z_y}  }^2+2 f''(X) \frac{\partial X}{\partial {Z_y}  } \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}+f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial^2 X}{\partial {Z_y}^2  }+f'(X) \frac{\partial^3 X}{\partial {Z_y}^2 \partial {Z_x}}\right) \\

b_{2,2}\,&=\,1/2 \Biggr(1/2  \Big( f^{4}(X) \Big[{\frac{\partial X}{\partial Z_x}}\Big]^2+f^3(X) \frac{\partial^2 X}{\partial {Z_x}^2} \Big) \Big[{\frac{\partial X}{\partial {Z_y}  }}\Big]^2+2 f^3(X) \frac{\partial X}{\partial Z_x} \frac{\partial X}{\partial {Z_y}  } \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}} \\

&+f''(X) \Big( \Big[\frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}\Big]^2+\frac{\partial X}{\partial {Z_y}  } \frac{\partial^2 X}{\partial {Z_y} \partial{Z_x}^2 } \Big) \\

&+1/2 \Big(f^{3}(X) \Big[\frac{\partial X}{\partial Z_x}\Big]^2+f''(X) \frac{\partial^2 X}{\partial {Z_x}^2} \Big) \frac{\partial^2 X}{\partial {Z_y}^2  }+f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial^3 X}{\partial {Z_y}^2 \partial {Z_x}}+1/2 f'(X) \frac{\partial^4 X}{\partial {Z_y}^2 \partial{Z_x}^2 } \Biggr)

\end{align}



using above equations, we can solve for the values of derivatives ( $f'(X),\,f"(X),\,\ldots, \, f^n(X) \,$) of the required applied function so that its composition with given Z-series function matches the given Z-series function with a target Z-series function. 







Equivalence of Hermite-Series and Z-Series Random Variables in Two Dimensions And Conversion of Coefficients across the Two Types of Series.



The equivalence and conversion of Z-series and Hermite Series in multidimensions works just analogously to the way it works in a single dimension. We first apply single dimensional conversion from Z-series to Hermite-series across one index and then across the second index and similarly for conversion from Hermite-series to Z-series.



Here I am first explaining one dimensional equivalence of both types of series and their conversion across each other.

Nth order Z-series and Nth order Hermite-Series share a common span of Nth order polynomials so any random variable that can be represented with Nth order Z-series, can also be represented by a Hermite-Series up to Nth order Hermite Polynomial. In fact, once coefficients of Z-series are known, it is easily possible to find coefficients of equivalent Hermite-Series and Vice versa and this is just consequence of simple algebra.



If we have Z-series representation of a non-Gaussian random variable is given, we can easily find coefficients of its Hermite-Series and vice versa.



If we represent a Z-series as 

\begin{equation}

X(Z)\,=\, \sum\limits_{n=0}^{N}\, a_n\, {Z}^n 

\end{equation}

and a hermite series as

\begin{equation}

X(Z)\,=\, \sum\limits_{n=0}^{N}\, ah_n\, H_n(Z) 

\end{equation}



then for $N=7$ (for $N\, 
```

---

## Error 41: Unbalanced $$: 19

**Snippet:** `Friends, this is description of iterative optimization matlab program named as  `

**Full content:**

```
Friends, this is description of iterative optimization matlab program named as



function [bnm,ObjFunc] = ZSeriesCoeffsFromMomentsIterativeNoiseTerm2D01A(rMu,NMoments,Iterations)



This program was only an initial version and in a few days I want to come up with a better program that uses Newton method in calculation of the coefficients of orthogonal part of transition increments. I will also do work to convert 2D hermite-series or 2D Z-series into functions of X and $Z_y$.



Here are the details of the above program



Objective:



Objective of the program is to find stochastic dynamics of a random variable $\bar{Y}$ that is dependent on X but is uncorrelated with X. Meaning variance of random variable $\bar{Y}$ systematically depends on X but in a way that $\bar{Y}$ is uncorrelated with X. We suppose that univariate stochastic dynamics of both X and $\bar{Y}$ are already known to us in the form of moments but we want to find two dimensional stochastic dynamics of $bar{Y}$ that capture the dependency of its variance on X.



Context of the Program and Preparing data of $\bar{Y}$:



Context of the program is that we have the joint observation data of two correlated random variables X and Y. We can find univariate Z-series of both X and Y from this data. We can also calculate the correlation between hermite polynomials of hermite-series of both X and Y. Hermite-series of X and Y are given respectively as



$$\,X(Z_x)\,=\, ah_0 \, +\, ah_1 \,H_1(Z_x) \,+\, ah_2 \,H_2(Z_x) \,+\, ah_3 \,H_3(Z_x) \, \\

\,Y(Z_y)\,=\, bh_0 \, +\, bh_1 \,H_1(Z_y) \,+\, bh_2 \,H_2(Z_y) \,+\, bh_3 \,H_3(Z_y) \, $$



We want to divide the random variable Y into two parts, one is conditional expectation part of  Y (E(Y|X)) that is perfectly correlated with X and second is part of Y ($\bar{Y}$) that is orthogonal to X. We can do this by calculating hermite correlations and then using the correlations to find conditional expectation part. But another simple way is do a regression of Y on hermite polynomials of X.



Suppose we have P joint observations of random variables $X_p$ $\,(p\,=\,1\, \ldots P)$ and $Y_p$ $\,(p\,=\,1\, \ldots P)$. From $X_p$ and  $Y_p$, We would have to invert equations below to find $Z_{X,p}$ $\,(p\,=\,1\, \ldots P)$ and then use the regression equation



$$\,Y_p\,=\,c_0\,+\,c_1\,H_1(Z_{X,p})\,+\,c_2\,H_2(Z_{X,p})\,+\,c_3\,H_3(Z_{X,p})\,+\,c_4\,H_4(Z_{X,p})\,+\,c_5\,H_5(Z_{X,p})\,$$



This way we find the regression coefficients which are given by ($c_0,\,c_1,\,\dots,\,c_M$)



Now we use the regression equation with each of the pth observations of X to find the conditional value of pth observation of Y. This is simply explainable part of regression 



 $$\,E\left[Y_p\,|\,X_p\right]\,=\,c_0\,+\,c_1\,H_1(Z_{X,p})\,+\,c_2\,H_2(Z_{X,p})\,+\,c_3\,H_3(Z_{X,p})\,+\,c_4\,H_4(Z_{X,p})\,+\,c_5\,H_5(Z_{X,p})\,$$



The above equation is repeated for all P observations of X.



From above calculated conditional expected values of each of the pth observation of $Y_p$ given $X_p$, we are able to calculate the orthogonal and uncorrelated part of the pth observation of $Y_p$ denoted as $\bar{Y}_p$  as



$$\,\bar{Y}_{p}\, =\, Y_p\,-\, \,E\left[Y_p\,|\,X_p\right]\,$$



In many cases where Y is a dependent variable as in the case of transition increment, this orthogonal random variable part given as $\bar{Y}$ would also be dependent on X even though it would be orthogonal to X and would not have any first order correlation with X.



Using above procedure, we can get data of P observation of $\bar{Y}$ that we can use to calculate its various moments. The above calculations to prepare data of $\bar{Y}$ are done in the case of transition increments of X in the matlab function given as EstimateDynamicCoeffParameters(X).



After choosing an appropriate two dimensional Z-series/ Hermite-series form of $\bar{Y}$ in next section, We will use optimization on above calculated moments of $\bar{Y}$ to find coefficients of the 2D Hermite- series form we would have selected as best possible.



Candidate Form of 2D Hermite-series of $\bar{Y}$



A simple form of stochastic dynamics of $\bar{Y}$ that is dependent on X could be selected as



$$\bar{Y}\,=\,g_0(X)\,+\,g_1(X) \,Z_y\,+\,g_2(X)\,\left({Z_y}^2\,-\,1\right) $$



since all of functions involved in above stochastic form given by $g_0(X)$, $g_1(X)$, and $g_2(X)$ can be represented in Z-series of X with $Z_x$ as its argument, the above stochastic form could be equivalent (give or take some change in order of 2D hermite series) to 2D hermite series form below.



\begin{align}



X(Z_y \, , \, Z_x)\, &=\, \Big[\, bh_{0,0} \, + \, bh_{0,1} \,H_1(Z_x) \,+\, bh_{0,2} \, H_2(Z_x) \,\, + \, bh_{0,3} \,H_3(Z_x)\,\Big] \\

&+\, \Big[ \, bh_{1,0} \, + \, bh_{1,1} \,H_1(Z_x) \,+\, bh_{1,2} \, H_2(Z_x) \, + \, bh_{1,3} \,H_3(Z_x)\, \Big] \, H_1(Z_y) \, \\

&+\, \Big[ \, bh_{2,0} \, + \, bh_{2,1} \,H_1(Z_x) \,+\, bh_{2,2} \, H_2(Z_x) \, \, + \, bh_{2,3} \,H_3(Z_x)\, \Big] \, H_2(Z_y) \, \\

\end{align}



 However, we notice that $g_0(X)$ in the above candidate stochastic form would be directly correlated with random variable X which is not what we want. Therefor I want friends to notice that in equivalent  2D hermite form, the zeroth hermite term with respect to $Z_y$ is given as



$$\Big[\, bh_{0,0} \, + \, bh_{0,1} \,H_1(Z_x) \,+\, bh_{0,2} \, H_2(Z_x) \,\, + \, bh_{0,3} \,H_3(Z_x)\,\Big] $$



In a 2D hermite form, first order correlation can appear only with respect to terms in zeroth hermite (with respect to appropriate Z, $Z_x,\, or\, Z_y$. Since zeroth hermite (with respect to Z_y) cannot be a function of $Z_x$, we choose the right form for 2D stochastic of $\bar{Y}$ in next section.



True Possible Form of 2D Hermite-series of $\bar{Y}$



In light of discussion in previous paragraph, we know that there can be no $Z_x$ dependent dynamics in zeroth hermite with respect to $Z_y$. Therefore a simple form of stochastic dynamics of $\bar{Y}$ that is dependent on X could be selected as



$$\bar{Y}\,=\,g_1(X) \,Z_y\,+\,g_2(X)\,\left({Z_y}^2\,-\,1\right) $$



since all of functions involved in above stochastic form given by $$g_1(X)$, and $g_2(X)$ can be represented in Z-series of X with $Z_x$ as its argument, the above true stochastic form could be equivalent to 2D hermite series form below.





\begin{align}

\bar{Y}(Z_y \, , \, Z_x)\, &=\,\, \Big[ \, bh_{1,0} \, + \, bh_{1,1} \,H_1(Z_x) \,+\, bh_{1,2} \, H_2(Z_x) \, + \, bh_{1,3} \,H_3(Z_x)\, \Big] \, H_1(Z_y) \, \\

&+\, \Big[ \, bh_{2,0} \, + \, bh_{2,1} \,H_1(Z_x) \,+\, bh_{2,2} \, H_2(Z_x) \, \, + \, bh_{2,3} \,H_3(Z_x)\, \Big] \, H_2(Z_y) \, \\

\end{align}



In the above 2D Hermite-series there are dynamics of variance that depend on $Z_x$ but zeroth hermite with respect to $Z_y$ has no dependence on $Z_x$. I want to emphasize that this is only one of the possible forms since for some random variables we might have to increase order of 2D Hermite-series in one or both directions. But if $\bar{Y}$ has to maintain orthogonality with X, there can be no polynomials terms in Z_x associated with zeroth hermite of $Z_y$.



Description of Numerical Problem:



We want to find the coefficients of above two dimensional hermite series so that numerically calculated moments from data of orthogonal part given by $\bar{Y}$ are perfectly retrieved from the  optimized coefficients of the above selected 2D hermite series form.



Preliminaries Before optimization:



Calculation of 2D Hermite-Series Variance



Before starting the optimization, we standardize the moments of $Y$ which means that variance of the 2D hermite-series should always be one. We also use unity variance property to fix one of the coefficients of hermite series. In above selected hermite series form the variance would be calculated as



\begin{align}

Var[\bar{Y}]\,&=\, {bh_{1,0}}^2\,+\,{bh_{1,1}}^2\,+\,2\,{bh_{1,2}}^2\,+\,6\,{bh_{1,3}}^2\, \\

&\,2\, {bh_{2,0}}^2\,+\,2\,{bh_{2,1}}^2\,+\,4\,{bh_{2,2}}^2\,+\,12\,{bh_{2,3}}^2\,

\end{align}



In the iterative perturbations numerical procedure, the variance is maintained at unity. When we perturb any coefficient in the iterative perturbation procedure, we readjust the value of $ {bh_{1,0}}$ so that unit variance is retrieved. This is done by calculating the value of   $Var[\bar{Y}]\,$ from equation below after the perturbation but without including ${bh_{1,0}}$



\begin{align}

Var[\bar{Y_0}]\,&=\, \,{bh_{1,1}}^2\,+\,2\,{bh_{1,2}}^2\,+\,6\,{bh_{1,3}}^2\, \\

&\,2\, {bh_{2,0}}^2\,+\,2\,{bh_{2,1}}^2\,+\,4\,{bh_{2,2}}^2\,+\,12\,{bh_{2,3}}^2\,

\end{align}



and then fixing the value of coefficient  $ {bh_{1,0}}$  by the following equation as



$$bh_{1,0}\,=\,\sqrt{1-Var[\bar{Y_0}]}$$



Conversion of 2D Hermite-Series Coefficients to 2D Z-series Coefficients



Even though modelling the required stochastic form was convenient in Hermite series since we could maintain orthogonality and zero correlations very easily but for calculation of moments, we have to convert 2D hermite-series to 2D Z-series. 

Using the calculations from yesterday's program, we can convert 2D Hermite Series coefficients to 2D Z-series Coefficients, and we get





\begin{align}

b_{0,0}&=-\left( bh_{2,0} \,-\,bh_{2,2} \right)\,\\

b_{0,1}&=\, - \left( bh_{2,1} \,-\,3\,bh_{2,3} \right)\\

b_{0,2}&= \,-bh_{2,2} \,\\

b_{0,3}&=\,-bh_{2,3} \\

b_{1,0}&=\,\left( bh_{1,0} \,-\,bh_{1,2} \right)\,\,\\

b_{1,1}&= \,\left( bh_{1,1} \, - 3\, bh_{1,3}\right)\, \,\\

b_{1,2}&=\, bh_{1,2} \,\\

b_{1,3}&=\, bh_{1,3}  \\

b_{2,0}&=\,\left( bh_{2,0} \,-\,bh_{2,2} \right)\, \\

b_{2,1}&=\,\left( bh_{2,1} \, -\,bh_{2,3} \right)\, \\

b_{2,2}&= \,bh_{2,2} \\

b_{2,3} &= \, bh_{2,3} \\

\end{align}



I think in the given program, my coefficients are in reverse which does not make a difference in calculations but I will fix them in new version to maintain convention.



Objective Function For optimization:



For optimization of coefficients to moments, we calculate moments from our trial coefficients with kth moment generated from trial coefficients denoted as $\mu(k)$ and target kth moment is denoted as $mu_0(k)$. We use different weights in the optimization for different moments. Since we are using standardized moments, typically smaller moments have a lot higher weight and larger moments have a lot smaller weight. We can also strategically alter the weights during optimization especially when one of the moments has already been well optimized, we increase its weight in the objective function so deviations from its optimized values are highly penalized while the iterative algorithm continues to fit other moments that have already not been fitted. 



This objective function is calculated as



$$\,Obj_N\,=\, \sum\limits_{k=1}^N\, w_k\,{\left(\mu(k)\,-\,\mu_0(k)\right)}^2$$





Details of Iterative Perturbation Optimization Procedure:



We have to iterate over eight coefficients of the following 2D hermite-series



\begin{align}

Var[\bar{Y}]\,&=\, {bh_{1,0}}^2\,+\,{bh_{1,1}}^2\,+\,2\,{bh_{1,2}}^2\,+\,6\,{bh_{1,3}}^2\, \\

&\,2\, {bh_{2,0}}^2\,+\,2\,{bh_{2,1}}^2\,+\,4\,{bh_{2,2}}^2\,+\,12\,{bh_{2,3}}^2\,

\end{align}



In actual procedure, we serially perturb over seven coefficients of above hermite series with a small perturbative step roughly inversely proportional to variance of the hermite polynomial associated with the coefficient and after perturbation in each coefficient we fix the first coefficient $bh_{1,0}$ so that standardized variance remains unity and accept the perturbation change if the objective function improves. Our perturbation strategy is to add the perturbation step size in one of the coefficients, then adjust bh_{1,0} from variance and then accept the perturbative change  if the objective function decreases below the best objective function and update the parameter in that dimension. If the objective function does not decrease by addition of perturbation step in that dimension, you subtract the perturbation step in the same coefficient dimension, and alter bh_{1,0} to keep unity variance and then see if the objective function decreases. Again decrease in parameter is accepted if the objective function decreases with perturbation in that direction. If the objective function does not decrease in both directions by adding or subtracting the perturbative step, we do not change the coefficient and keep it at its old value from previous iteration. So we serially iterate over all coefficients one by one. And when there is no decrease in objective function after adding and subtracting the perturbative steps sizes in all coefficient dimensions, we cut the step size along all dimensions to .95 or .9 of the previous step size and optimization starts working again.



Initial perturbation step size is very small and is kept proportional to inverse of variance of hermite polynomial associated with the particular coefficient.



After every few hundred iterations, we reset the perturbation step and make it equal to a fraction (like possibly 1/50) of the already found best fir values of the coefficients. 



In our case first moment was zero and second moment is kept fixed all along iterative optimization procedure. We have adopted this strategy to alter the coefficients so that only three moments are first calibrated with a three moment objective function. This is particularly easy and we use about 500 iterations for this purpose in first stage. After 500 perturbations, we switch to four dimension optimization. But in order to do that we need a four coefficient best objective function for decision making. At 500th iteration, when switching from three moments optimization to four moments optimization, we use the calibrated coefficients from three moments optimization and use them to calculate four moments and these four moments from best fit values are then used to find best initial objective function that has to be improved in four moments calibration. At the same time, after switching to four moments optimization, we also increase the weight of the third moment that has already been fixed several times so that deviations from already fixed third moment are highly penalized while perturbing the coefficients to find the best fit to fourth moments. We use 500th to 4000th iterations to find the best fit to fourth moment. At 4000th iteration, we move from four moment optimization to five moments optimization. Like before, we project best fit coefficients from four moments optimization to five moments and then calculate the initial five moments best fit objective function. We also increase the weight on already calibrated third and four moments further so they are kept in close calibration while  iterative perturbation procedure optimizes for fifth moment. We repeat the same process when we switch from five moments optimization to six moments optimization on 10000th iteration.



In the program all seven hermite coefficients that we iteratively perturb to find best values are kept in a singly array called cH.
```

---

## Error 42: Unbalanced $: 7

**Snippet:** `.  .  .  .  ``` function []= ConditionalDensityHermitesBivariate()  %SV SDE is  `

**Full content:**

```
.

.

.

.

```
function []= ConditionalDensityHermitesBivariate()

%SV SDE is 
%dV(t)=mu1 V(t)^beta1 dt+ mu2 V(t)^beta2 dt + sigma0 V(t)^gamma dZ(t)
%In mean reverting SDEs we ususally have
%mu1= kappaV * thetaV
%beta1=0
%mu2=-kappa
%beta2=0


%NDim=4;%Three assets and one SV.

%%%%%%%%%%%%%%%%%%%5

V0=1.0;%.32;
thetaV=1.0;%.045;%1;%.04;
kappaV=1.0;%1.5;%1.5;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;

beta2=1;
gamma=.95;
sigma0=.65;%.45;

dt=.03125/2;
Tt=64*1;


T=Tt*dt;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%In this code block, we do monte carlo simulation of stochastic volatility SDEs
%And also calculate monte carlo call prices.

seed0=82150987;
%seed0=52130649;
rng(seed0, 'twister')
paths=100000;
V(1:paths,1)=V0;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5


Random2(1:paths,1)=0;

for tt=1:Tt
    
Random2=randn(size(Random2)); 



    V(1:paths,1)=V(1:paths,1)+ ...
        (mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*sqrt(dt) + ...
        (mu1.*beta1*V(1:paths,1).^(beta1-1) + mu2.*beta2.*V(1:paths,1).^(beta2-1)).* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt^2/2 + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*(1-1/sqrt(3))*dt^1.5) + ...
        .5*(mu1.*beta1.*(beta1-1).*V(1:paths,1).^(beta1-2) + mu2.*beta2.*(beta2-1).*V(1:paths,1).^(beta2-2)).* ...    
        sigma0^2.*V(1:paths,1).^(2*gamma).*dt^2/2 + ...
        sigma0*gamma*V(1:paths,1).^(gamma-1) .* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2).*Random2(1:paths,1).*1/sqrt(3)*dt^1.5 + ...
        sigma0.*V(1:paths,1).^gamma .*(Random2(1:paths,1).^2-1)*dt/2) + ...
        .5*sigma0*gamma*(gamma-1).*V(1:paths,1).^(gamma-2) .* ...
        sigma0^2.*V(1:paths,1).^(2*gamma) .*Random2(1:paths,1).*1/sqrt(3)*dt^1.5;

    V(V<0)=.00001;

    
    if(tt==32)
        Xin(1:paths,1)=V(1:paths,1);
    end
        
    if(tt==34)
        Yin(1:paths,1)=V(1:paths,1);
    end
end

Order=5;

%The function belwo does all the analytics of caclulation of 2D conditional
%and joint densities
 CalculateBivariateHermiteSeries0(Yin,Xin,Order)

str=input("Ihave reached after the function");


end
```

.

.

.

```
function [] = CalculateBivariateHermiteSeries0(Yin,Xin,Order)

Ndata=length(Yin);


%Below find one dimensional Hermite-Series of variable that is taken as
%independent in the analytics.
[CoeffX,Zx] = CalculateHermiteSeriesFromData(Xin,Order);

%With respect to HErmite-series of X, find correlated and orthogonal parts of 
%observations of dependent variable Y.
[Ycorr0,Ydecorr,Coeffyx] = FindDecorrelatedYwrtX(Yin,Zx,Order);

%I was trying to work with regression on variance but dropped this idea.
%%Below, on orhtogonal part of  
[YExplainedVar,RSquared,YdecorrAdj] = FindConditionalVarianceAdjustedOrthogonalRV(Ydecorr,Zx,Order);

%The functions below need YdecorrAdj as input but do not use it in the latest version.
%This is basically redundant. The above function and resulting value of
%YdecorrAdj is redundant in the latest versions of the program.

% 
% 
%str=input("We have reached close to end");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%The function below finds 2D conditional hermite series of uncorrelated
%orthogonal part of Y from regression
[aCoeffHH] = Calculate2DHermiteSeriesConditionalOrthogonal(Ydecorr,YdecorrAdj,Zx,Order);

%Below we add 1D correlated part Hermite Series coefficients to
%uncorrelated 2D Hermite series to get one single 2D hermite series of all
%of Y
aaCoeffHH=aCoeffHH;
aaCoeffHH(1,1:Order+1)=aaCoeffHH(1,1:Order+1)+Coeffyx(1:Order+1,1).';


%The function below finds 2D conditional hermite series of all of Y directly from regression.
[bCoeffHH] = Calculate2DHermiteSeriesConditional(Ydecorr,YdecorrAdj,Yin,Zx,Order);


aaCoeffHH
bCoeffHH

str=input("Look at comparison of both 2D Series (orthogonal regressed+correlated) and singly regressed");

[cCoeffHH] = Calculate2DHermiteSeriesJoint(Ydecorr,YdecorrAdj,Yin,Xin,Zx,Order);

%The function above calculates 2D joint Hermite-series of W=XY from regression 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Below calculate six moments of W=XY from data of X and Y
for mm=1:6
    MomentsData(mm)=sum(Xin(1:Ndata).^mm.*Yin(1:Ndata).^mm)./Ndata;
end
SeriesOrder10=Order+1;
SeriesOrder01=Order+1;
NMomentsXY=6;
[Moments1D1] = Calculate1DMomentsOf2DHermiteSeries(cCoeffHH,SeriesOrder10,SeriesOrder01,NMomentsXY);

Moments1D1
MomentsData


str=input("Look at comparison of moments of 2D product W=XY from the data and from 2D Hermite-Series");


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
%Convert 2D conditional HErmite-Series of Y into 2D Z-series. This is
%required for finding its product with univariate Z-series of X.
[bCoeff] = Convert2DHermitesInto2DSeries(bCoeffHH);
%Below, convert univariate hermite-series of X into univariate Z-series
[cCoeffX(1),cCoeffX(2:6)] = ConvertHermiteSeriesToZSeries(CoeffX(1),CoeffX(2:6),Order);


%Below do calculations to find product of 2D conditional Z-series of Y and
%univariate Z-series of X with the aim to find 2D joint Z-series of W=XY 
SeriesOrder10=Order+1;
SeriesOrder01=Order+1;
SeriesOrder20=1;
SeriesOrder02=Order+1;

%Below calculate the product: 2D product of Z-series [Y|X](Zx,Zy)*X(Zx)
[ccCoeff,EXY] =SeriesProduct2DAlgorithmicNew(bCoeff,cCoeffX,SeriesOrder10,SeriesOrder01,SeriesOrder20,SeriesOrder02);


[ccCoeffHH] = Convert2dSeriesInto2DHermites(ccCoeff);


SeriesOrder10=6;
SeriesOrder01=6;
NMomentsXY=6;

[Moments1D2] = Calculate1DMomentsOf2DHermiteSeries(ccCoeffHH,SeriesOrder10,SeriesOrder01,NMomentsXY);


Moments1D2
MomentsData


str=input("Look at comparison of moments of 2D product densities. Moments Found from data itself and moments found from 2D product [Y|X](Zx,Zy)*X(Zx) ");




end
```

.

.

.

.

```
function [Coeff,Zy] = CalculateHermiteSeriesFromData(Yin,Order)

Ndata=length(Yin);

%Hz=HermitePoly(Order);  
MeanYin=sum(Yin(1:Ndata))/Ndata;
Ym(1:Ndata)=Yin(1:Ndata)-MeanYin;
YmVar=sum(Ym(1:Ndata).^2)/Ndata;
Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);



[Zn] = StandardNormalIdealDesity02(Ndata,1);
%[ZI] = CalculateZI(Zn);


ZI=Zn;
%Below W is the design matrix for least squares regression i.e the matrix
%that contains all the hermite polynomials calculated at ideal normal
%density grid of size Ndata. 
[W] = EvalHermiteArrayH0(ZI,Order);

%We first sort the data so that we can assign one appropriate Z-grid
%point(and associated hermite polynomials calculated at that grid point)
%to each data element. This ideal normal density Z-grid is
%constructed so that its size is equal to data observations count. We
%suppose that first derivative of random variables with repsect to Z
%does not switch sign meaning that increasing values of data
%observations have to aligned with increasing values of ideal normal
%density grid.
[Ys,I]=sort(Y(1:Ndata));
%In the line below, the data sort is reversed so that now the ideal 
%normal density grid elements assigned to various observations of random 
%variable face it on data observations index. For details, Please look 
%on interent the definition of matlab sort command with role of "I" 
%in output and how it alters the index.   

%%Zs1(I(1:Ndata))=ZI(1:Ndata);

%Below the values to be regressed facing the design matrix are assigned
Ymu(1:Ndata,1)=Ys(1:Ndata);
%Below, implement least squares regression.
coeff=(W'*W)$W'*Ymu);
%Store in coefficietns array of all random varaibles
Coeff(1:Order+1)= coeff(1:Order+1,1);
%Store the associated Z in Z-array of all coefficients.   
Zy(I(1:Ndata))=W(1:Ndata,2);



Coeff(1:Order+1)=Coeff(1:Order+1).*sqrt(YmVar);
Coeff(1)=Coeff(1)+MeanYin;

end




```

.

.

.

```
function [Ycorr,Ydecorr,coeffcorr] = FindDecorrelatedYwrtX(Y,Zx,Order)

%1. This function takes in observations of a random variable Y.
%2. This function takes in Zx underlying Hermite-series of another correlated variable X
%which is in the order of observations of X and Y. 
%3. This function takes in Order upto which to perform the decorrelation analytics.

%This function takes observations of Y, and finds out a part of
%each of the observations that is correlated with X and another par that is
%orthogonal to X.

%Correlated part is returned as Ycorr.
%Orthogonal part is returned as Ydecorr
%Coefficients of correlated part as a function of Hermite polynomials
%series of Zx are returned in coeffcorr/

    Ndata=length(Y);
   
    Ycorr(1:Ndata,1)=0;
    Ymu1(1:Ndata,1)=Y(1:Ndata);
        %Z1(:)=Zx(:,1);
        %Below find the least squares regression design matrix including
        %hermites of mmth ZOrtho.
        [W1] = EvalHermiteArrayH0(Zx,Order);
        %Below, do the regression to find the hermite series coefficients of part of
        %random variable Y that is correalted with Zx.

        coeffcorr=(W1'*W1)$W1'*Ymu1);
 
        for hh=1:Order+1
            %Below Y corr continues to sum over all hermites of Zx
            Ycorr(1:Ndata,1)=Ycorr(1:Ndata,1)+coeffcorr(hh,1).*W1(1:Ndata,hh);
            
        end

    Ydecorr(1:Ndata,1)=Y(1:Ndata,1)-Ycorr(1:Ndata,1);




end


```

.

.

.

```
function [YExplainedVar,RSquared,YdecorrAdj] = FindConditionalVarianceAdjustedOrthogonalRV(Ydecorr,Zx,Order)

%This function regresses variance of orthogonal part of Y on hermite
%polynomials of Zx and finds




    Ndata=length(Ydecorr);
    EYdecorr=sum(Ydecorr(1:Ndata))/Ndata;
    YVar(1:Ndata,1)=Ydecorr(1:Ndata,1).^2-(EYdecorr).^2;
    Ymu(1:Ndata,1)=YVar(1:Ndata,1);
    [W1] = EvalHermiteArrayH0(Zx,2*Order);
    %Below, do the least squares regression
    coeff=(W1'*W1)$W1'*Ymu);
    YExplainedVar(1:Ndata,1)=0;
    %YExplainedVar0(1:Ndata,1)=0;
    for hh=1:2*Order+1
            %Below Y corr continues to sum over all hermites of all mm
            %Zorthos that are less than nnth random variable.
            YExplainedVar(1:Ndata,1)=YExplainedVar(1:Ndata,1)+coeff(hh,1).*W1(1:Ndata,hh);
            
    end

    SStot=sum((YVar(1:Ndata,1)-(sum(YVar(1:Ndata,1))/Ndata)).^2);    
    SSfit=sum((YVar(1:Ndata,1)-YExplainedVar(1:Ndata,1)).^2);
    
    RSquared=1-SSfit/SStot
    
    str=input("Look at R-Squared");
    
    
    YExplainedVarP=YExplainedVar(YExplainedVar>0);
    YExplainedVarPMin=min(YExplainedVarP);
    YExplainedVar(YExplainedVar<0)=YExplainedVarPMin;
    
    YVarOut(1:Ndata,1)=(1-RSquared)*YVar(1:Ndata,1)+((RSquared)*YVar(1:Ndata,1))./YExplainedVar(1:Ndata,1);
    
   %  YdecorrAdj(1:Ndata,1)=EYdecorr+sqrt((1-RSquared)*YVar(1:Ndata,1))+sqrt(((RSquared)*YVar(1:Ndata,1))./YExplainedVar(1:Ndata,1));
    
    %YdecorrAdj(1:Ndata,1)=Ydecorr(1:Ndata,1).*sqrt(YVarOut(1:Ndata,1)./YVar(1:Ndata,1));
    
    %YdecorrAdj(1:Ndata,1)=EYdecorr+Ydecorr(1:Ndata,1).*sqrt((1-RSquared))+Ydecorr(1:Ndata,1).*sqrt(1./YVar(1:Ndata,1).*YExplainedVar(1:Ndata,1)./(RSquared));
  %  YdecorrAdj(1:Ndata,1)=EYdecorr+Ydecorr(1:Ndata,1).*sqrt((1-RSquared))+Ydecorr(1:Ndata,1).*(-sqrt(RSquared.*YVar(1:Ndata,1))+sqrt(YExplainedVar(1:Ndata,1)))./sqrt(YVar(1:Ndata,1));
    YdecorrAdj(1:Ndata,1)=EYdecorr+(Ydecorr(1:Ndata,1)-EYdecorr).*sqrt((1-RSquared))+(Ydecorr(1:Ndata,1)-EYdecorr).*(RSquared).*sqrt(YVar(1:Ndata,1)./YExplainedVar(1:Ndata,1));
  
    
end


```

.

.

.

```
function [bCoeffHH] = Calculate2DHermiteSeriesConditionalOrthogonal(Ydecorr,YdecorrAdj,Zx,Order)

%As the function name states Orthogonal decorrelated part of Y called Ydecorr is regressed in this function.

Ndata=length(Ydecorr);

%Ydecorr0(1:Ndata,1)=Ydecorr(1:Ndata,1)./sqrt(abs(YVar(1:Ndata,1)));

%YVarP=YVar(YVar>0);
%YVarPMin=min(YVarP);
%YVar(YVar<0)=YVarPMin;

%Ydecorr0(1:Ndata,1)=Ydecorr(1:Ndata,1)./sqrt((YVar(1:Ndata,1)));


[Ydecorr0s,I]=sort(Ydecorr(1:Ndata,1));
%[Ydecorr0s,I]=sort(YdecorrAdj(1:Ndata,1));

[Zn] = StandardNormalIdealDesity02(Ndata,1);
%[ZI] = CalculateZI(Zn);

ZI=Zn;

Zy(I(1:Ndata))=ZI(1:Ndata);
[Wx] = EvalHermiteArrayH0(Zx,Order);
[Wy] = EvalHermiteArrayH0(Zy,Order);

Ymu(1:Ndata,1)=Ydecorr(1:Ndata,1); %As the function name states Orthogonal decorrelated part of Y is regressed.
    
for nn=1:Order+1
    Wxy(1:Ndata,nn+(nn-1)*Order:nn+nn*Order)=Wx(1:Ndata,1:Order+1).*Wy(1:Ndata,nn);
end

    coeff=(Wxy'*Wxy)$Wxy'*Ymu);

for nn=1:Order+1    
    bCoeffHH(nn,1:Order+1)=coeff(nn+(nn-1)*Order:nn+nn*Order);
end


end
```

.

.

.

```
function [bCoeffHH] = Calculate2DHermiteSeriesConditional(Ydecorr,YdecorrAdj,Y,Zx,Order)
 %As the function name states All of Y is regressed and conditional value found.

Ndata=length(Ydecorr);

% Ydecorr0(1:Ndata,1)=Ydecorr(1:Ndata,1)./sqrt(abs(YVar(1:Ndata,1)));
% [Ydecorr0s,I]=sort(Ydecorr0(1:Ndata,1));

%[Ydecorr0s,I]=sort(YdecorrAdj(1:Ndata,1));

[Ydecorr0s,I]=sort(Ydecorr(1:Ndata,1));


[Zn] = StandardNormalIdealDesity02(Ndata,1);
%[ZI] = CalculateZI(Zn);

ZI=Zn;

Zy(I(1:Ndata))=ZI(1:Ndata);
[Wx] = EvalHermiteArrayH0(Zx,Order);
[Wy] = EvalHermiteArrayH0(Zy,Order);

Ymu(1:Ndata,1)=Y(1:Ndata);%As the function name states All of Y is regressed and conditional value found.
    
for nn=1:Order+1
    Wxy(1:Ndata,nn+(nn-1)*Order:nn+nn*Order)=Wx(1:Ndata,1:Order+1).*Wy(1:Ndata,nn);
end

    coeff=(Wxy'*Wxy)$Wxy'*Ymu);

for nn=1:Order+1    
    bCoeffHH(nn,1:Order+1)=coeff(nn+(nn-1)*Order:nn+nn*Order);
end


end


```

.

.

.

```
function [bCoeffHH] = Calculate2DHermiteSeriesJoint(Ydecorr,YdecorrAdj,Y,X,Zx,Order)


%As the function name states All of joint value W=Y*X is regressed in this function.



Ndata=length(Ydecorr);

%[Ydecorr0s,I]=sort(YdecorrAdj(1:Ndata,1));
[Ydecorr0s,I]=sort(Ydecorr(1:Ndata,1));


[Zn] = StandardNormalIdealDesity02(Ndata,1);
%[ZI] = CalculateZI(Zn);

ZI=Zn;

Zy(I(1:Ndata))=ZI(1:Ndata);
[Wx] = EvalHermiteArrayH0(Zx,Order);
[Wy] = EvalHermiteArrayH0(Zy,Order);

Ymu(1:Ndata,1)=Y(1:Ndata).*X(1:Ndata);%As the function name states All of joint value W=Y*X is regressed in this function.

    
for nn=1:Order+1
    Wxy(1:Ndata,nn+(nn-1)*Order:nn+nn*Order)=Wx(1:Ndata,1:Order+1).*Wy(1:Ndata,nn);
end

    coeff=(Wxy'*Wxy)$Wxy'*Ymu);

for nn=1:Order+1    
    bCoeffHH(nn,1:Order+1)=coeff(nn+(nn-1)*Order:nn+nn*Order);
end


end


```

.

.

.

```
function [bCoeffHH] = Calculate2DHermiteSeriesJoint(Ydecorr,YdecorrAdj,Y,X,Zx,Order)


%As the function name states All of joint value W=Y*X is regressed in this function.



Ndata=length(Ydecorr);

%[Ydecorr0s,I]=sort(YdecorrAdj(1:Ndata,1));
[Ydecorr0s,I]=sort(Ydecorr(1:Ndata,1));


[Zn] = StandardNormalIdealDesity02(Ndata,1);
%[ZI] = CalculateZI(Zn);

ZI=Zn;

Zy(I(1:Ndata))=ZI(1:Ndata);
[Wx] = EvalHermiteArrayH0(Zx,Order);
[Wy] = EvalHermiteArrayH0(Zy,Order);

Ymu(1:Ndata,1)=Y(1:Ndata).*X(1:Ndata);%As the function name states All of joint value W=Y*X is regressed in this function.

    
for nn=1:Order+1
    Wxy(1:Ndata,nn+(nn-1)*Order:nn+nn*Order)=Wx(1:Ndata,1:Order+1).*Wy(1:Ndata,nn);
end

    coeff=(Wxy'*Wxy)$Wxy'*Ymu);

for nn=1:Order+1    
    bCoeffHH(nn,1:Order+1)=coeff(nn+(nn-1)*Order:nn+nn*Order);
end


end


```

.

.

.

```
function [cc,EX] =SeriesProduct2DAlgorithmicNew(aa,bb,SeriesOrder10,SeriesOrder01,SeriesOrder20,SeriesOrder02)



SeriesOrder30=SeriesOrder10+SeriesOrder20-1;
SeriesOrder03=SeriesOrder01+SeriesOrder02-1;

cc(1:SeriesOrder30,1:SeriesOrder03)=0;

for nn1=1:SeriesOrder30
    if(nn1<=SeriesOrder10)
        nn3=nn1;
    else
        nn3=SeriesOrder10;
    end
    for nn2=1:SeriesOrder03
        if(nn2<=SeriesOrder01)
            nn4=nn2;
        else
            nn4=SeriesOrder01;
        end    
        for jj1=1:nn3
            if(nn1-jj1+1 <=SeriesOrder20) 
                for jj2=1:nn4
                    if(nn2-jj2+1 <=SeriesOrder02)
                        cc(nn1,nn2)=cc(nn1,nn2)+aa(jj1,jj2).*bb(nn1-jj1+1,nn2-jj2+1);
                    end
                end
            end
        end
    end
end


[EZ] = EZZ2();


EX=0;
for nn1=1:SeriesOrder30
    for nn2=1:SeriesOrder03
        EX=EX+cc(nn1,nn2).*EZ(nn1).*EZ(nn2);
    end
end




end
```

.

.

.

```
function [gHH] = Convert2DSeriesInto2DHermites(g)

gH(1,:)=g(1,:)+g(3,:)+3*g(5,:);
gH(2,:)=g(2,:)+3*g(4,:)+15*g(6,:);
gH(3,:)=g(3,:)+6*g(5,:);
gH(4,:)=g(4,:)+10*g(6,:);
gH(5,:)=g(5,:);
gH(6,:)=g(6,:);


gHH(:,1)=gH(:,1)+gH(:,3)+3*gH(:,5);
gHH(:,2)=gH(:,2)+3*gH(:,4)+15*gH(:,6);
gHH(:,3)=gH(:,3)+6*gH(:,5);
gHH(:,4)=gH(:,4)+10*gH(:,6);
gHH(:,5)=gH(:,5);
gHH(:,6)=gH(:,6);


end


```

.

.

.

```
function [g] = Convert2DHermitesInto2DSeries(gHH)


gH(:,1)=gHH(:,1)-gHH(:,3)+3*gHH(:,5);
gH(:,2)=gHH(:,2)-3*gHH(:,4)+15*gHH(:,6);
gH(:,3)=gHH(:,3)-6*gHH(:,5);
gH(:,4)=gHH(:,4)-10*gHH(:,6);
gH(:,5)=gHH(:,5);
gH(:,6)=gHH(:,6);





g(1,:)=gH(1,:)-gH(3,:)+3*gH(5,:);
g(2,:)=gH(2,:)-3*gH(4,:)+15*gH(6,:);
g(3,:)=gH(3,:)-6*gH(5,:);
g(4,:)=gH(4,:)-10*gH(6,:);
g(5,:)=gH(5,:);
g(6,:)=gH(6,:);


end


```

.

.

.

```
function [b0,b] = ConvertHermiteSeriesToZSeries(ch0,ch,Order)

dh(1)=ch0;
dh(2:Order+1)=ch(1:Order);

c(1:Order+1)=0;
[Hz] = HermitePoly(Order);
for nn=1:Order+1
    for mm=1:Order+1
        c(mm)=c(mm)+dh(nn).*Hz(nn,mm);
    end
end

b0=c(1);
b(1:Order)=c(2:Order+1);

end


```

.

.

.

```
function [Wh] = EvalHermiteArrayH0(Z,Order)

%Evaluates first Order-th hermites at the array of Z's. If input array of Z
%has a size of 100 and Order is 4, it will return a 100 X 5 array.

Hz=HermitePoly(Order);

Wh(1:length(Z),1:Order+1)=0;
for nn=1:Order+1
    Wh(:,nn)=0;
    for mm=1:nn
        Wh(:,nn)=Wh(:,nn)+Hz(nn,mm).*Z(:).^(mm-1);
    end
end

end
```

.

.

.

```
function [ZZ] = StandardNormalIdealDesity02(Ndata,Sigma)
%Ndata is number of data points in sample, for which we want to find the
%coefficients of the Z-series.
%Sigma=1+.06;
%Sigma=1;
if (rem(Ndata,2)==0)
    NnMid=Ndata/2;
    NnMid
    ZZ(NnMid+1)=norminv(.5+1/Ndata*.5,0,Sigma);
    ZZ(NnMid)=norminv(.5-1/Ndata*.5,0,Sigma);
    for nn=2:NnMid-1
        ZZ(nn+NnMid)=norminv(.5+(nn-.5)*1/Ndata,0,Sigma);
        ZZ(-nn+1+NnMid)=norminv(.5-(nn-.5)*1/Ndata,0,Sigma);
    end
    %A=normcdf((Ndata-1)/Ndata);
    %ZZ(Ndata)=exp(-5*A^2)/(1/Ndata);
    A=norminv((Ndata-1)/Ndata);
    ZZ(Ndata)=A +0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
    ZZ(1)=-A-0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
end

if (rem(Ndata,2)==1)
    NnMid=(Ndata+1)/2;
    ZZ(NnMid)=0;
    for nn=1:NnMid-2
        ZZ(nn+NnMid)=norminv(.5+(nn)*1/Ndata,0,Sigma);
        ZZ(-nn+NnMid)=norminv(.5-(nn)*1/Ndata,0,Sigma);
    end
   A=norminv((Ndata-1)/Ndata);
    ZZ(Ndata)=A +0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
    ZZ(1)=-A-0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
end

%ZZ
%A
%plot(ZZ)
%str=input("Look at density plot standard")

end


```

.

.

.

Here is the last output you will see when you will run this program.



Moments1D1 =

   1.0e+04 *

  Columns 1 through 3

   0.000114060460541   0.000228695824181   0.000828666794056

  Columns 4 through 6

   0.005717055625406   0.058480038566825   2.892109408517658

MomentsData =

   1.0e+03 *

  Columns 1 through 3

   0.001141788451688   0.002295214895405   0.008514052298269

  Columns 4 through 6

   0.057361881005992   0.606090575346114   8.344067932971779

Look at comparison of moments of 2D product W=XY from the data and from 2D Hermite-Series

Moments1D2 =

   1.0e+03 *

  Columns 1 through 3

   0.001135234336760   0.002222469499063   0.007496676913725

  Columns 4 through 6

   0.042956603322803   0.401536302194722   5.799563781458257

MomentsData =

   1.0e+03 *

  Columns 1 through 3

   0.001141788451688   0.002295214895405   0.008514052298269

  Columns 4 through 6

   0.057361881005992   0.606090575346114   8.344067932971779

Look at comparison of moments of 2D product densities. Moments Found from data itself and moments found from 2D product [Y|X](Zx,Zy)*X(Zx) 
```

---

## Error 43: Unbalanced $: 3

**Snippet:** `Here are the matlab programs.    .  .  .  ``` function []= ConditionalDensityHer`

**Full content:**

```
Here are the matlab programs.



.

.

.

```
function []= ConditionalDensityHermitesBivariate()

%SV SDE is 
%dV(t)=mu1 V(t)^beta1 dt+ mu2 V(t)^beta2 dt + sigma0 V(t)^gamma dZ(t)
%In mean reverting SDEs we ususally have
%mu1= kappaV * thetaV
%beta1=0
%mu2=-kappa
%beta2=0


%NDim=4;%Three assets and one SV.

%%%%%%%%%%%%%%%%%%%5

V0=1.0;%.32;
thetaV=.80;%.045;%1;%.04;
kappaV=1.0;%1.5;%1.5;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;

beta2=1;
gamma=.95;
sigma0=.55;%.45;

dt=.03125/2;
Tt=64*1;


T=Tt*dt;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%In this code block, we do monte carlo simulation of stochastic volatility SDEs
%And also calculate monte carlo call prices.

seed0=82150987;
%seed0=52130649;
rng(seed0, 'twister')
paths=50000
V(1:paths,1)=V0;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5


Random2(1:paths,1)=0;

for tt=1:Tt
    
Random2=randn(size(Random2)); 



    V(1:paths,1)=V(1:paths,1)+ ...
        (mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*sqrt(dt) + ...
        (mu1.*beta1*V(1:paths,1).^(beta1-1) + mu2.*beta2.*V(1:paths,1).^(beta2-1)).* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt^2/2 + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*(1-1/sqrt(3))*dt^1.5) + ...
        .5*(mu1.*beta1.*(beta1-1).*V(1:paths,1).^(beta1-2) + mu2.*beta2.*(beta2-1).*V(1:paths,1).^(beta2-2)).* ...    
        sigma0^2.*V(1:paths,1).^(2*gamma).*dt^2/2 + ...
        sigma0*gamma*V(1:paths,1).^(gamma-1) .* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2).*Random2(1:paths,1).*1/sqrt(3)*dt^1.5 + ...
        sigma0.*V(1:paths,1).^gamma .*(Random2(1:paths,1).^2-1)*dt/2) + ...
        .5*sigma0*gamma*(gamma-1).*V(1:paths,1).^(gamma-2) .* ...
        sigma0^2.*V(1:paths,1).^(2*gamma) .*Random2(1:paths,1).*1/sqrt(3)*dt^1.5;

    V(V<0)=.00001;

    
    if(tt==32)
        Xin(1:paths,1)=V(1:paths,1);
    end
        
    if(tt==34)
        Yin(1:paths,1)=V(1:paths,1);
    end
end

Order=5;

%The function belwo does all the analytics of caclulation of 2D conditional
%and joint densities
 CalculateBivariateHermiteSeries01(Yin,Xin,Order)

str=input("Ihave reached after the function");


end
```

.

.

.

```
function [] = CalculateBivariateHermiteSeries01(Yin,Xin,Order)

Ndata=length(Yin);


[ZnNew] = StandardNormalIdealDesity02(Ndata,1);

ZI=ZnNew;
%Below find one dimensional Hermite-Series of variable that is taken as
%independent in the analytics.
[XCoeffH,Zx] = CalculateHermiteSeriesFromData01(Xin,Order,ZI);

%With respect to HErmite-series of X, find correlated and orthogonal parts of 
%observations of dependent variable Y.
[Ycorr0,Ydecorr,Coeffyx] = FindDecorrelatedYwrtX(Yin,Zx,Order);

%I was trying to work with regression on variance but dropped this idea.
%%Below, on orhtogonal part of  
%[YExplainedVar,RSquared,YdecorrAdj] = FindConditionalVarianceAdjustedOrthogonalRV(Ydecorr,Zx,Order);

%The functions below need YdecorrAdj as input but do not use it in the latest version.
%This is basically redundant. The above function and resulting value of
%YdecorrAdj is redundant in the latest versions of the program.

YdecorrAdj=0;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%The function below calculates the 2D joint hermite-series of W=XY
%XYCoeffHH is the 2D joint hermite Series of W=XY
%YCoeffHH is 2D conditional hermite-series of Y|X

[XYCoeffHH,YCoeffHH] = Calculate2DHermiteSeriesConditionalAndJoint(Ydecorr,YdecorrAdj,Yin,Xin,Zx,Order,ZI);

%XYCoeffHH are coefficients of 2D joint Hermite-Series of X and Y. 
%YCoeffHH are coefficients of 2D conditional Hermite-Series of Y given X.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Below calculate six moments of W=XY from data of X and Y
for mm=1:6
    MomentsData(mm)=sum(Xin(1:Ndata).^mm.*Yin(1:Ndata).^mm)./Ndata;
end
SeriesOrder10=Order+1;
SeriesOrder01=Order+1;
NMomentsXY=6;
[Moments1D1] = Calculate1DMomentsOf2DHermiteSeries(XYCoeffHH,SeriesOrder10,SeriesOrder01,NMomentsXY);

Moments1D1
MomentsData


str=input("Look at comparison of moments of 2D product W=XY from the data and from 2D Hermite-Series");


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55



 [YCoeff2D] = Convert2DHermitesInto2DSeries(YCoeffHH);
 %Below, convert univariate hermite-series of X into univariate Z-series
 
 [XCoeff(1),XCoeff(2:6)] = ConvertHermiteSeriesToZSeries(XCoeffH(1),XCoeffH(2:6),Order);
 
 
 %Below do calculations to find product of 2D conditional Z-series of Y and
 %univariate Z-series of X with the aim to find 2D joint Z-series of W=XY 
 SeriesOrder10=Order+1;
 SeriesOrder01=Order+1;
 SeriesOrder20=1;
 SeriesOrder02=Order+1;
 
 %Below calculate the product: 2D product of Z-series [Y|X](Zx,Zy)*X(Zx)
 [XYCoeff2,EXY] =SeriesProduct2DAlgorithmicNew(YCoeff2D,XCoeff,SeriesOrder10,SeriesOrder01,SeriesOrder20,SeriesOrder02);
 
 
 [XYCoeffHH2] = Convert2dSeriesInto2DHermites(XYCoeff2);
 
 %Below 2D Hermite series coefficients matrix XYCoeffHH2 is derived from multiplying 
 %2D conditional Hermite-Series of Y|X with univariate HErmite-Series of X
 %The above multiplication is carried out in the form of repsective Z-series.
 %It is compared with 2D Hermite-series Coefficients matrix XYCoeffHH found
 %directly from data.
 %The both 2D hermite-series could precisely be the same but for that we would 
 %have to increase order in X-direction
 XYCoeffHH2
 XYCoeffHH
 
 
 str=input("Look at comparison of Hermite-series of W directly from data and after multiplying 2D conditional Hermite series of Y|X with hermite-series of X ");



end
```

.

.

.

```
function [aCoeffHH,cCoeffHH] = Calculate2DHermiteSeriesConditionalAndJoint(Ydecorr,YdecorrAdj,Yin,Xin,Zx,Order,ZI)

%This function returns two bivariate hermite-Series.
%bCoeffHH(1:Order+1,1:Order+1) is a matrix containing coefficients of 2D
%Hermite-Series of Joint distribution of X and Y.
%The way to construct Hermite-series from bCoeffHH is sum of terms bCoeffHH(n,m)H_{n-1)(Z_y)H_{m-1}(Z_x) 
%cCoeffHH(1:Order+1,1:Order+1) is a matrix containing coefficients of 2D
%Hermite-Series of Conditional distribution of Y given X (or Z_x).

%Inputs are
%1. Ydecorr is decorrelated part of observations of Y:decorrelated with
%respect to X
%2. YdecorrAdj is currently redundant.
%3. Yin are observations of Y
%4. Xin are observations of X.
%5. Zx are standard normal values underlying observations of X. Z_{x,p} --> X_p
%6. Order is Order of expansion in both sides of Hermite-series. Univariate
%Hermite-Series had the same order.
%7. ZI is discretized normal density array and appears as input so its moment
%matched version is passed to all functions in the program.




Ndata=length(Ydecorr);


[Ydecorr0s,I]=sort(Ydecorr(1:Ndata,1));
%[Ydecorr0s,I]=sort(YdecorrAdj(1:Ndata,1));

Zy(I(1:Ndata))=ZI(1:Ndata);
[Wx] = EvalHermiteArrayH0(Zx,Order);
[Wy] = EvalHermiteArrayH0(Zy,Order);

Ymu(1:Ndata,1)=Yin(1:Ndata,1);


for nn=1:Order+1
    Wxy(1:Ndata,nn+(nn-1)*Order:nn+nn*Order)=Wx(1:Ndata,1:Order+1).*Wy(1:Ndata,nn)./Xin(1:Ndata,1);
end

    coeff=(Wxy'*Wxy)$Wxy'*Ymu);

    
%Below aCoeffHH are coefficients of 2D Hermite-Series of W=XY.    
for nn=1:Order+1    
    aCoeffHH(nn,1:Order+1)=coeff(nn+(nn-1)*Order:nn+nn*Order);
end


%Below, we construct the coefficients of H_{n-1}(Z_x) that are realized for
%pth observations of data.
%These are values for nth row and pth observation set
% XrowCoeff(n,p)=\sum_{m=0}^{Order+1}  aCoeffHH(n,m} H_{m-1}(Z_{x,p})./X_p

for nn=1:Order+1  %Repeat over all rows multiplying (n-1)th Hermite of Z_y  
    XrowCoeff(1:Ndata,1)=0;
    for hh=1:Order+1
        XrowCoeff(1:Ndata,1)=XrowCoeff(1:Ndata,1)+aCoeffHH(nn,hh).*Wx(1:Ndata,hh)./Xin(1:Ndata,1);
    end
    
    % XrowCoeff(n,p)values are regressed on hermites of Z_{x,p} to find
    % coefficients of conditional 2D Hermite-Series of Y
    
    Ccoeff=(Wx'*Wx)$Wx'*XrowCoeff);
    
    %cCoeffHH are Coefficients of 2D conditional Hermite-Series of Y given X. 
    cCoeffHH(nn,1:Order+1)=Ccoeff(1:Order+1);
    
end

end
```

.

.

.

```
function [Coeff,Zy] = CalculateHermiteSeriesFromData01(Yin,Order,ZI)

Ndata=length(Yin);

%Hz=HermitePoly(Order);  
MeanYin=sum(Yin(1:Ndata))/Ndata;
Ym(1:Ndata)=Yin(1:Ndata)-MeanYin;
YmVar=sum(Ym(1:Ndata).^2)/Ndata;
Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);



% [Zn] = StandardNormalIdealDesity02(Ndata,1);
% %[ZI] = CalculateZI(Zn);
% 
% 
% ZI=Zn;
%Below W is the design matrix for least squares regression i.e the matrix
%that contains all the hermite polynomials calculated at ideal normal
%density grid of size Ndata. 
[W] = EvalHermiteArrayH0(ZI,Order);

%We first sort the data so that we can assign one appropriate Z-grid
%point(and associated hermite polynomials calculated at that grid point)
%to each data element. This ideal normal density Z-grid is
%constructed so that its size is equal to data observations count. We
%suppose that first derivative of random variables with repsect to Z
%does not switch sign meaning that increasing values of data
%observations have to aligned with increasing values of ideal normal
%density grid.
[Ys,I]=sort(Y(1:Ndata));
%In the line below, the data sort is reversed so that now the ideal 
%normal density grid elements assigned to various observations of random 
%variable face it on data observations index. For details, Please look 
%on interent the definition of matlab sort command with role of "I" 
%in output and how it alters the index.   

%%Zs1(I(1:Ndata))=ZI(1:Ndata);

%Below the values to be regressed facing the design matrix are assigned
Ymu(1:Ndata,1)=Ys(1:Ndata);
%Below, implement least squares regression.
coeff=(W'*W)$W'*Ymu);
%Store in coefficietns array of all random varaibles
Coeff(1:Order+1)= coeff(1:Order+1,1);
%Store the associated Z in Z-array of all coefficients.   
Zy(I(1:Ndata))=W(1:Ndata,2);



Coeff(1:Order+1)=Coeff(1:Order+1).*sqrt(YmVar);
Coeff(1)=Coeff(1)+MeanYin;

end




```

.

.

.

Here is the output when you run the program.



>> ConditionalDensityHermitesBivariate

paths =

       50000

NnMid =

       25000

Moments1D1 =

   1.0e+02 *

  Columns 1 through 3

   0.009339351085975   0.013200875000722   0.028453859426203

  Columns 4 through 6

   0.093886217211554   0.470396115324018   4.342938543379914

MomentsData =

   1.0e+02 *

  Columns 1 through 3

   0.009338782489851   0.013260671466972   0.029144878365143

  Columns 4 through 6

   0.098749147821191   0.482519142215311   3.036909143098590

Look at comparison of moments of 2D product W=XY from the data and from 2D Hermite-Series

XYCoeffHH2 =

  Columns 1 through 3

   0.932221321011216   0.591445809432458   0.189701382591621

   0.082982186373105   0.027421287964677   0.000067742925991

   0.003364974582490  -0.000238472470643  -0.000774375241723

   0.002102646723133   0.001182213260259  -0.003128196897984

   0.000144803030191  -0.000065088854855   0.000354581888335

  -0.000099379412715   0.000058854088147  -0.000327172574743

  Columns 4 through 6

   0.042133626500634   0.005786325190427   0.000871571667574

   0.000657075757547  -0.001161399499040   0.000019185933235

  -0.000682596039671  -0.000304275511237   0.000096124900127

  -0.000064513661092  -0.000919391286407  -0.000051727012841

   0.000017168323118   0.000044684389062  -0.000006685298461

   0.000030734746599  -0.000093027084532  -0.000006626450210

XYCoeffHH =

  Columns 1 through 3

   0.933935108597543   0.592593274637135   0.194841408666432

   0.084096953744043   0.029030164570997   0.003551514056271

   0.004001523746690   0.000429099976038   0.001181745064122

   0.002670815351835   0.002118011545015  -0.001340236395074

   0.000077513888080  -0.000147464339133   0.000145142945969

  -0.000044354075573   0.000155126728597  -0.000153196177191

  Columns 4 through 6

   0.043173506428318   0.007344588694457   0.000903896700903

   0.002208944671472  -0.000036438613800   0.000181420704333

  -0.000028344740759   0.000313177032308   0.000157844900384

   0.000836552771282  -0.000334819306111   0.000048160612949

  -0.000062621183501  -0.000022475515157  -0.000014434972600

   0.000123179776919  -0.000035796617422   0.000003726752674

Look at comparison of Hermite-series of W directly from data and after multiplying 2D conditional Hermite series of Y|X with hermite-series of X
```

---

## Error 44: Unbalanced $: 5

**Snippet:** `I have attached all necessary matlab files but if there is anything left not att`

**Full content:**

```
I have attached all necessary matlab files but if there is anything left not attached, please let me know. You can also search for relevant files that have been attached in the past. 

.

.

.

```
function []= ConditionalDensityHermitesBivariateNew()

%SV SDE is 
%dV(t)=mu1 V(t)^beta1 dt+ mu2 V(t)^beta2 dt + sigma0 V(t)^gamma dZ(t)
%In mean reverting SDEs we ususally have
%mu1= kappaV * thetaV
%beta1=0
%mu2=-kappa
%beta2=0


%NDim=4;%Three assets and one SV.

%%%%%%%%%%%%%%%%%%%5

V0=.850;%.32;
V00=V0;

thetaV=1.20;%.045;%1;%.04;
kappaV=1.150;%1.5;%1.5;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;

beta2=1;
gamma=.50;
sigma0=.4;%.45;

dt=.03125/2;
Tt=64*1;

V00f=thetaV+(V0-thetaV)*exp(-kappaV*dt*36);
T=Tt*dt;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%In this code block, we do monte carlo simulation of stochastic volatility SDEs
%And also calculate monte carlo call prices.

seed0=82150987;
%seed0=52130649;
rng(seed0, 'twister')
paths=100000;
V(1:paths,1)=V0;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
TT1=18; %Transition distribution start
TT2=36; %Transition distribution end

Random2(1:paths,1)=0;

for tt=1:Tt
    
Random2=randn(size(Random2)); 



    V(1:paths,1)=V(1:paths,1)+ ...
        (mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*sqrt(dt) + ...
        (mu1.*beta1*V(1:paths,1).^(beta1-1) + mu2.*beta2.*V(1:paths,1).^(beta2-1)).* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt^2/2 + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*(1-1/sqrt(3))*dt^1.5) + ...
        .5*(mu1.*beta1.*(beta1-1).*V(1:paths,1).^(beta1-2) + mu2.*beta2.*(beta2-1).*V(1:paths,1).^(beta2-2)).* ...    
        sigma0^2.*V(1:paths,1).^(2*gamma).*dt^2/2 + ...
        sigma0*gamma*V(1:paths,1).^(gamma-1) .* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2).*Random2(1:paths,1).*1/sqrt(3)*dt^1.5 + ...
        sigma0.*V(1:paths,1).^gamma .*(Random2(1:paths,1).^2-1)*dt/2) + ...
        .5*sigma0*gamma*(gamma-1).*V(1:paths,1).^(gamma-2) .* ...
        sigma0^2.*V(1:paths,1).^(2*gamma) .*Random2(1:paths,1).*1/sqrt(3)*dt^1.5;

    V(V<0)=.00001;

    
    if(tt==TT1)
        Xin(1:paths,1)=V(1:paths,1);
    end
        
    if(tt==TT2)
        Yin(1:paths,1)=V(1:paths,1);
    end
end


str=input("I have reached stone 1");


Order=5;

%Ndata=paths;
%[ZI] = StandardNormalIdealDesity02(Ndata,1);
%[YCoeffH,Zy] = CalculateHermiteSeriesFromData01(Yin,Order,ZI)


%The function belwo does all the analytics of caclulation of 2D conditional
%and joint densities
 [XYCoeffHH,YCoeffHH,XCoeffH] =CalculateBivariateHermiteSeries01(Yin,Xin,Order);
 
 size(XYCoeffHH)
 size(YCoeffHH)
 str=input("I have reached stone 2");
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
% % %This block is 2D graphs and can be skipped. I am commenint it. 
% % 
% % 
% %  NoOfBinsX=200;
% %  NoOfBinsY=100;
% %  
% %  
% %  XX(1)=min(Xin);
% %  XX(NoOfBinsX)=max(Xin);
% %  XX(2:NoOfBinsX-1)=XX(1)+(1:NoOfBinsX-2)*(XX(NoOfBinsX)-XX(1))/(NoOfBinsX-1);
% %  
% %  
% %  
% %  YY(1)=min(Yin);
% %  YY(NoOfBinsY)=max(Yin);
% %  YY(2:NoOfBinsY-1)=YY(1)+(1:NoOfBinsY-2)*(YY(NoOfBinsY)-YY(1))/(NoOfBinsY-1);
% %  
% %  
% %  
% %  [pXY2D] = Calculate2VariablesOn2DGridFromAnalyticZSeriesNew(XX,YY,XYCoeffHH,XCoeffH);
% % 
% % clf; 
% % surf(XX(3:NoOfBinsX),YY(3:NoOfBinsY),pXY2D(3:NoOfBinsY,3:NoOfBinsX));
% % 
% % xlabel('Random Variable X'), ylabel('Random Variable Y'),zlabel('Bivariate Density of XY')
% % 
% % title('Graph of Bivariate joint Density of XY');
% % str=input("Look at graph of joint density of XY ----1");
% % 
% % 
% % 
% % [pY2D] = Calculate2VariablesOn2DGridFromAnalyticZSeriesNew(XX,YY,YCoeffHH,XCoeffH);
% % 
% % clf;
% % 
% % surf(XX(3:NoOfBinsX),YY(3:NoOfBinsY),pY2D(3:NoOfBinsY,3:NoOfBinsX));
% % 
% % xlabel('Random Variable X'), ylabel('Random Variable Y'),zlabel('Bivariate Density of Y conditional on X')
% % title('Graph of Bivariate conditional Density of Y|X');
% % 
% % str=input("Look at graph of conditional density Y|X ----2");
% % 
% % 
% % 
% % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Below we numerically and analytically find
%transition probabilities from point v10 and make a comparison of both
%numerically constructed density and analytically constructed density so
%that both of them are originating from arbitrary point V10.

%V10 below is the delta origin at time TT1 from where the transition
%probabilities will originate. Feel free to move it around in the
%distribution of X.
V10=.75;
%V10=1.10;

V(1:paths)=V10;

Random2(1:paths,1)=0;


for tt=TT1+1:TT2
    
Random2=randn(size(Random2)); 



    V(1:paths,1)=V(1:paths,1)+ ...
        (mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*sqrt(dt) + ...
        (mu1.*beta1*V(1:paths,1).^(beta1-1) + mu2.*beta2.*V(1:paths,1).^(beta2-1)).* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt^2/2 + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*(1-1/sqrt(3))*dt^1.5) + ...
        .5*(mu1.*beta1.*(beta1-1).*V(1:paths,1).^(beta1-2) + mu2.*beta2.*(beta2-1).*V(1:paths,1).^(beta2-2)).* ...    
        sigma0^2.*V(1:paths,1).^(2*gamma).*dt^2/2 + ...
        sigma0*gamma*V(1:paths,1).^(gamma-1) .* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2).*Random2(1:paths,1).*1/sqrt(3)*dt^1.5 + ...
        sigma0.*V(1:paths,1).^gamma .*(Random2(1:paths,1).^2-1)*dt/2) + ...
        .5*sigma0*gamma*(gamma-1).*V(1:paths,1).^(gamma-2) .* ...
        sigma0^2.*V(1:paths,1).^(2*gamma) .*Random2(1:paths,1).*1/sqrt(3)*dt^1.5;

    V(V<0)=.00001;

end


NoOfBins=200;
MaxCutOff=10;

[XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(V,paths,NoOfBins,MaxCutOff )


clf;

plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'r');

hold on

xOrder=Order;
yOrder=Order;
[Zx] = CalculateZgivenXAndHSeriesCoeffs(V10,XCoeffH,xOrder);
%The above is calculation for Zx corresponding to delta origin of
%transition probabilities at mid-starting time TT1;

%The regression below is for conditional mean of Y|X.
Dim=1;
NN=paths;
[CoeffR,CoeffX] = RegressYOnX(Yin,Xin,NN,Dim,Order)
[Wh] = EvalHermiteArrayH0(Zx,Order);
Ymu=CoeffR(1,1);
for hh=2:Order+1
    Ymu=Ymu+Wh(1,hh).*CoeffR(hh,1);
end
Ymu
%Ymu is conditional mean of Y given a delta origin at density X. It is the
%conditional mean of Y given X.

%Below, we collapse two dimensional pdf of Y|X to one dimensional pdf given
%Zx i.e. this Y|X=X(Zx)
He(1)=1;
He(2)=Zx
He(3)=Zx^2-1;
He(4)=Zx^3-3*Zx;
He(5)=Zx^4-6*Zx.^2+3;
He(6)=Zx^5-10*Zx.^3+15*Zx;
for hh=1:yOrder+1
    YCoeffh(hh)=0.0;
    for hh2=1:xOrder+1
        YCoeffh(hh)=YCoeffh(hh)+YCoeffHH(hh,hh2).*He(hh2);
    end
end

YCoeffh=YCoeffh/V10.^(1-gamma)/XCoeffH(1).^gamma;
%YCoeffh=YCoeffh/V10.^(1-gamma/2)/XCoeffH(1).^(gamma);


%We have to divide by a function of mean XCoeffH(1).^gamma of the starting distribution X
%and a function of transition delta origin V10.^(1-gamma)

YCoeffh(1)=Ymu

PlotHermiteSeriesDensityAndRvGraph(YCoeffh(1),YCoeffh(2:yOrder+1),'g')
title(sprintf('V00 = %.3f; kappa=%.3f, theta=%.3f,gamma=%.3f,sigma=%.3f;transition probs delta origin at V10=%.3f at TT1=%.3f;transition probs end TT2=%.3f ',V00, kappaV, thetaV,gamma,sigma0, V10,(TT1*dt),(TT2*dt)));%,sprintf('theta= %f', theta), sprintf('kappa = %f', kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
legend({'Numerical Density','Analytic Density'}, ...
    'Location','northeast')



YCoeffh



end
```

.

.

.

.

```
function [YCoeffHH,XYCoeffHH,XCoeffH] = CalculateBivariateHermiteSeries01(Yin,Xin,Order)

Ndata=length(Yin);


%[ZnNew] = StandardNormalIdealDesity02(Ndata,1);
[ZI] = MomentMatchedStandardNormalDiscretizedDensity(Ndata);

%ZI=ZnNew;
%Below find one dimensional Hermite-Series of variable that is taken as
%independent in the analytics.
[XCoeffH,Zx] = CalculateHermiteSeriesFromData01(Xin,Order,ZI);

%With respect to HErmite-series of X, find correlated and orthogonal parts of 
%observations of dependent variable Y.
[Ycorr0,Ydecorr,Coeffyx] = FindDecorrelatedYwrtX(Yin,Zx,Order);



YdecorrAdj=0;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%The function below calculates the 2D joint hermite-series of W=XY
%XYCoeffHH is the 2D joint hermite Series of W=XY
%YCoeffHH is 2D conditional hermite-series of Y|X

[XYCoeffHH,YCoeffHH] = Calculate2DHermiteSeriesConditionalAndJoint(Ydecorr,YdecorrAdj,Yin,Xin,Zx,Order,ZI);

%XYCoeffHH are coefficients of 2D joint Hermite-Series of X and Y. This
%value XYCoeffHH is bad and it has to be treated for common covariance before further
%use. I am not doing that since I will not need it in conditional
%probabilities calculations. This will be fixed in a future version.

%YCoeffHH are coefficients of 2D conditional Hermite-Series of Y given X.

%size(YCoeffHH)
%size(YCoeffHH(1,1:Order+1))
%size(Coeffyx(1:Order+1))
YCoeffHH(1,1:Order+1)=YCoeffHH(1,1:Order+1)+Coeffyx(1:Order+1)';

%Above I add common covariance in the orthogonal part

% % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % %Below calculate six moments of W=XY from data of X and Y
% % for mm=1:Order+1
% %     MomentsData(mm)=sum(Xin(1:Ndata).^mm.*Yin(1:Ndata).^mm)./Ndata;
% % end
% % SeriesOrder10=Order+1;
% % SeriesOrder01=Order+1;
% % NMomentsXY=Order+1;
% % 
% % Order
% % [Moments1D1] = Calculate1DMomentsOf2DHermiteSeries(XYCoeffHH,SeriesOrder10,SeriesOrder01,NMomentsXY);
% % 
% % Moments1D1
% % MomentsData
% % 
% % 
% % str=input("Look at comparison of moments of 2D product W=XY from the data and from 2D Hermite-Series");
% % 
% % 
% % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
% % 
% % 
% % 
% %  [YCoeff2D] = Convert2DHermitesInto2DSeries(YCoeffHH);
% %  %Below, convert univariate hermite-series of X into univariate Z-series
% %  
% %  [XCoeff(1),XCoeff(2:Order+1)] = ConvertHermiteSeriesToZSeries(XCoeffH(1),XCoeffH(2:Order+1),Order);
% %  
% %  
% %  %Below do calculations to find product of 2D conditional Z-series of Y and
% %  %univariate Z-series of X with the aim to find 2D joint Z-series of W=XY 
% %  SeriesOrder10=Order+1;
% %  SeriesOrder01=Order+1;
% %  SeriesOrder20=1;
% %  SeriesOrder02=Order+1;
% %  
% %  %Below calculate the product: 2D product of Z-series [Y|X](Zx,Zy)*X(Zx)
% %  [XYCoeff2,EXY] =SeriesProduct2DAlgorithmicNew(YCoeff2D,XCoeff,SeriesOrder10,SeriesOrder01,SeriesOrder20,SeriesOrder02);
% %  
% %  
% %  [XYCoeffHH2] = Convert2dSeriesInto2DHermites(XYCoeff2);
% %  
% %  %Below 2D Hermite series coefficients matrix XYCoeffHH2 is derived from multiplying 
% %  %2D conditional Hermite-Series of Y|X with univariate HErmite-Series of X
% %  %The above multiplication is carried out in the form of repsective Z-series.
% %  %It is compared with 2D Hermite-series Coefficients matrix XYCoeffHH found
% %  %directly from data.
% %  %The both 2D hermite-series could precisely be the same but for that we would 
% %  %have to increase order in X-direction
% %  XYCoeffHH2
% %  XYCoeffHH
% %  
% %  
% %  str=input("Look at comparison of Hermite-series of W directly from data and after multiplying 2D conditional Hermite series of Y|X with hermite-series of X ");
% % 
% % SeriesOrder10=Order+1;
% % SeriesOrder01=Order+1;
% % NMomentsXY=Order+1;
% % [Moments1D2] = Calculate1DMomentsOf2DHermiteSeries(XYCoeffHH2,SeriesOrder10,SeriesOrder01,NMomentsXY);
% % 
% % Moments1D1
% % Moments1D2
% % MomentsData
% % 
% % 
% % str=input("Look at comparison of moments of 2D product W=XY from the data and from 2D Hermite-Series");


end
```

.

.

.

.

.

```
function [aCoeffHH,cCoeffHH] = Calculate2DHermiteSeriesConditionalAndJoint(Ydecorr,YdecorrAdj,Yin,Xin,Zx,Order,ZI)

%This function returns two bivariate hermite-Series.
%bCoeffHH(1:Order+1,1:Order+1) is a matrix containing coefficients of 2D
%Hermite-Series of Joint distribution of X and Y.
%The way to construct Hermite-series from bCoeffHH is sum of terms bCoeffHH(n,m)H_{n-1)(Z_y)H_{m-1}(Z_x) 
%cCoeffHH(1:Order+1,1:Order+1) is a matrix containing coefficients of 2D
%Hermite-Series of Conditional distribution of Y given X (or Z_x).

%Inputs are
%1. Ydecorr is decorrelated part of observations of Y:decorrelated with
%respect to X
%2. YdecorrAdj is currently redundant.
%3. Yin are observations of Y
%4. Xin are observations of X.
%5. Zx are standard normal values underlying observations of X. Z_{x,p} --> X_p
%6. Order is Order of expansion in both sides of Hermite-series. Univariate
%Hermite-Series had the same order.
%7. ZI is discretized normal density array and appears as input so its moment
%matched version is passed to all functions in the program.




Ndata=length(Ydecorr);


[Ydecorr0s,I]=sort(Ydecorr(1:Ndata,1));
%[Ydecorr0s,I]=sort(YdecorrAdj(1:Ndata,1));

Zy(I(1:Ndata))=ZI(1:Ndata);
[Wx] = EvalHermiteArrayH0(Zx,Order);
[Wy] = EvalHermiteArrayH0(Zy,Order);

%Ymu(1:Ndata,1)=Yin(1:Ndata,1);
Ymu(1:Ndata,1)=Ydecorr(1:Ndata,1);


for nn=1:Order+1
    Wxy(1:Ndata,nn+(nn-1)*Order:nn+nn*Order)=Wx(1:Ndata,1:Order+1).*Wy(1:Ndata,nn)./Xin(1:Ndata,1);
end

    coeff=(Wxy'*Wxy)$Wxy'*Ymu);

    
%Below aCoeffHH are coefficients of 2D Hermite-Series of W=XY.    
for nn=1:Order+1    
    aCoeffHH(nn,1:Order+1)=coeff(nn+(nn-1)*Order:nn+nn*Order);
end


%Below, we construct the coefficients of H_{n-1}(Z_x) that are realized for
%pth observations of data.
%These are values for nth row and pth observation set
% XrowCoeff(n,p)=\sum_{m=0}^{Order+1}  aCoeffHH(n,m} H_{m-1}(Z_{x,p})./X_p

for nn=1:Order+1  %Repeat over all rows multiplying (n-1)th Hermite of Z_y  
    XrowCoeff(1:Ndata,1)=0;
    for hh=1:Order+1
        XrowCoeff(1:Ndata,1)=XrowCoeff(1:Ndata,1)+aCoeffHH(nn,hh).*Wx(1:Ndata,hh)./Xin(1:Ndata,1);
    end
    
    % XrowCoeff(n,p)values are regressed on hermites of Z_{x,p} to find
    % coefficients of conditional 2D Hermite-Series of Y
    
    Ccoeff=(Wx'*Wx)$Wx'*XrowCoeff);
    
    %cCoeffHH are Coefficients of 2D conditional Hermite-Series of Y given X. 
    cCoeffHH(nn,1:Order+1)=Ccoeff(1:Order+1);
    
end

% % % YProjected(1:Ndata,1)=0;
% % % for nn=1:Order+1  %Repeat over all rows multiplying (n-1)th Hermite of Z_y  
% % %     
% % %     for hh=1:Order+1
% % %         YProjected(1:Ndata,1)=YProjected(1:Ndata,1)+aCoeffHH(nn,hh).*Wx(1:Ndata,hh).*Wy(1:Ndata,nn)./Xin(1:Ndata,1);
% % %     end
% % %     
% % % end
% % % 
% % % STot=sum((Yin(1:Ndata,1)-sum(Yin(1:Ndata,1))/Ndata).^2);
% % % SRes=sum((Yin(1:Ndata,1)-YProjected(1:Ndata,1)).^2);
% % % 
% % % RSquared=1-SRes/STot;
% % % 
% % % RSquared
% % % 
% % % str=input("Look at RSquared--0002")
% % % 



end
```

.

.

.

.

```
function [ZnNew] = MomentMatchedStandardNormalDiscretizedDensity(Ndata)

[ZnNew] = StandardNormalIdealDesity02(Ndata,1);

if((Ndata=30))
    MOrder=6;


alpha(1) =1.002706567896411;
alpha(3)=-0.001341612601616;
alpha(5)=0.000431803496557;


elseif((Ndata>=250)&&(Ndata=2000)&&(Ndata=50000)&&(Ndata=100000)&&(Ndata=350000))
    MOrder=14;  
    
    
    alpha(1) =1.000899195470733;
    alpha(3)=-0.000414380757501;
  alpha(5)=0.000161271457889;
  alpha(7)=0.000037987998807;
  alpha(9)=0;%.000016308099635;
  alpha(11)=0.;%000002045556572;                   0
  alpha(13)=0;%.000000157715037;
end


%[ZnNew,alpha,Moment] = MatchMomentParametersOfIdealZhalfNew01(ZnNew,MOrder);

% alpha(1)=0.998665620502348;
% alpha(3)=0.000729818387735;
% alpha(5)=0.000026530286747;
% alpha(7)=0.000021718051556;
% alpha(9)=0.000008734265559;
% alpha(11)=-0.000000362716896;                  0
% alpha(13)=-0.000000010818264;




[ZnNew,alpha] = NewtonRootSearchForMatchingMomentsOfGaussianVariates01(ZnNew,alpha,MOrder);


% alpha
% 
% str=input("Look at alpha");

end


```

.

.

.

```
function [ZnNew,alpha] = NewtonRootSearchForMatchingMomentsOfGaussianVariates01(Zn,alpha,MOrder)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               


Ndata=length(Zn);
 
 %MOrder=12;
 HOrder=MOrder-2;
 
 EZ(1)=0;
EZ(2)=1;
for nn=3:MOrder
    if rem(nn,2)==1
        EZ(nn)=0;
    else
        EZ(nn)=EZ(nn-2)*(nn-1);
        %EZ(nn)
    end
end

TMoment(1:MOrder)=EZ(1:MOrder);
 %CalculateMomentsAndDerivativesOfIdealNormalGrid(Zn,alpha,MOrder,HOrder);
 [F,dF] = CalculateMomentsAndDerivativesOfIdealNormalGrid(Zn,alpha,MOrder,HOrder,TMoment);
 
% F
% dF
% str=input("Look at results");
 
 

w(MOrder)=1;
for nn=MOrder-2:-2:2
w(nn)=w(nn+2).*(nn+2)*(nn+1);%*.5;    
end
%w(2)=w(2)*1024;
%w(8)=w(8)*2;
%w(10)=w(10)*sqrt(2);
%w
%str=input("Look at weights--12")


[ZnNew] = CalculateZnAfterHermiteSeriesMultiplication(Zn,alpha,MOrder);

for mm=1:MOrder
    Moment(mm)=sum(ZnNew(1:Ndata).^mm)/Ndata;
end


ObjFuncBest=CalculateObjMoment(EZ,Moment,w,MOrder);

ObjFuncBest
%str=input("Look at ObjFuncBest");
%b0Best=c0;
alphaBest(1:HOrder+1)=alpha(1:HOrder+1);


    
    qq=0;
    for mm=2:2:MOrder
        qq=qq+1;
        da(qq,1)=alpha(mm-1);
    end

    

nn=0;
while((nn.000000000001) || (abs(F(2,1))>.000000000001) || (abs(F(3,1))>.000000000001)))% || (abs(F(4,1))>.00000000001)))%|| (abs(F(5,1))>.00000000001)))%|| (abs(F(6,1))>.00000000001)))%|| (abs(F(7,1))>.00000000001)|| (abs(F(8,1))>.00000000001)  ))

    nn=nn+1;
    %Below Newton matrix equation to improve the Z-series coefficients guess at previous step.
    da=da-dF\F;

    qq=0;
    for mm=2:2:MOrder
        qq=qq+1;
        alpha(mm-1)=da(qq,1);
    end
    %b(1:SeriesOrder)=da(2:SeriesOrder+1,1);
    
 
    
    [ZnNew] = CalculateZnAfterHermiteSeriesMultiplication(Zn,alpha,MOrder);
    
    for mm=1:MOrder
        Moment(mm)=sum(ZnNew(1:Ndata).^mm)/Ndata;
    end

  
 
    ObjFuncNew=CalculateObjMoment(EZ,Moment,w,MOrder);

ObjFuncBest
ObjFuncNew
%str=input("Look at objfunction--11--");

%alpha

%str=input("Look at alpha");

    if(ObjFuncBest>ObjFuncNew)
      
       ObjFuncBest=ObjFuncNew;
       alphaBest=alpha;
       %bBest(1:SeriesOrder)=b(1:SeriesOrder);
    end
    
    [F,dF] = CalculateMomentsAndDerivativesOfIdealNormalGrid(Zn,alpha,MOrder,HOrder,TMoment);


    qq=0;
    for mm=2:2:MOrder
        qq=qq+1;
        da(qq,1)=alpha(mm-1);
    end

end
alpha=alphaBest;%Best;


   [ZnNew] = CalculateZnAfterHermiteSeriesMultiplication(Zn,alpha,MOrder);
 
 
end
```

.

.

.

```
function [F,dF] = CalculateMomentsAndDerivativesOfIdealNormalGrid(Zn,alpha,MOrder,HOrder,TMoment)



Ndata=length(Zn);



[Hz] = HermitePoly(HOrder);


for nn=1:2:HOrder+1
    ZZ(nn,1:Ndata)=Zn(1:Ndata).^(nn-1);
end

HermiteSeries(1:Ndata)=alpha(1);
HermiteZ(1:Ndata,1:HOrder)=0;
for nn=2:2:HOrder
    %Ndata
    %nn
    HermiteZ(1:Ndata)=0;
    for mm=1:2:(nn+1)
        %HermiteZ(nn,:)=HermiteZ(nn,:)+Hz(nn+1,mm).*ZZ(mm,:);
        HermiteZ(1:Ndata)=HermiteZ(1:Ndata)+Hz(nn+1,mm).*ZZ(mm,1:Ndata);
    end
    HermiteSeries(1:Ndata)=HermiteSeries(1:Ndata)+ alpha(nn+1).*HermiteZ(1:Ndata);
end
    
ZnNew(1:Ndata)=Zn(1:Ndata).*HermiteSeries(1:Ndata);


for mm=1:MOrder
    Moment(mm)=sum(ZnNew(1:Ndata).^mm)/Ndata;
    for nn=2:2:HOrder
        HermiteZ(1:Ndata)=0;
        for kk=1:2:(nn+1)
            HermiteZ(1:Ndata)=HermiteZ(1:Ndata)+Hz(nn+1,kk).*ZZ(kk,1:Ndata);
        end
        dG(mm,nn)=sum(Zn(1:Ndata).^(mm).*mm.*HermiteSeries(1:Ndata).^(mm-1).*HermiteZ(1:Ndata))/Ndata;
        
    end
    
    dG0(mm)=sum(Zn(1:Ndata).^(mm).*mm.*HermiteSeries(1:Ndata).^(mm-1))/Ndata;
    
    G(mm,1)=Moment(mm)-TMoment(mm);
end

%dG0

%str=input("Look at dG0");
QQ=round(MOrder/2);
qq=0;
for nn=2:2:MOrder
qq=qq+1;
F(qq,1)=G(nn,1);
dF(qq,1)=dG0(nn);
dF(qq,2:QQ)=dG(nn,2:2:(2+(QQ-2)*2));
end

% F(1,1)=G(2,1);
% F(2,1)=G(4,1);
% F(3,1)=G(6,1);
% F(4,1)=G(8,1);
% F(5,1)=G(10,1);
% F(6,1)=G(12,1);
% 
% dF(1,1)=dG0(2);
% dF(2,1)=dG0(4);
% dF(3,1)=dG0(6);
% dF(4,1)=dG0(8);
% dF(5,1)=dG0(10);
% dF(6,1)=dG0(12);
% 
% dF(1,2)=dG(2,2);
% dF(2,2)=dG(4,2);
% dF(3,2)=dG(6,2);
% dF(4,2)=dG(8,2);
% dF(5,2)=dG(10,2);
% dF(6,2)=dG(12,2);
% 
% dF(1,3)=dG(2,4);
% dF(2,3)=dG(4,4);
% dF(3,3)=dG(6,4);
% dF(4,3)=dG(8,4);
% dF(5,3)=dG(10,4);
% dF(6,3)=dG(12,4);
% 
% dF(1,4)=dG(2,6);
% dF(2,4)=dG(4,6);
% dF(3,4)=dG(6,6);
% dF(4,4)=dG(8,6);
% dF(5,4)=dG(10,6);
% dF(6,4)=dG(12,6);
% 
% dF(1,5)=dG(2,8);
% dF(2,5)=dG(4,8);
% dF(3,5)=dG(6,8);
% dF(4,5)=dG(8,8);
% dF(5,5)=dG(10,8);
% dF(6,5)=dG(12,8);
% 
% dF(1,6)=dG(2,10);
% dF(2,6)=dG(4,10);
% dF(3,6)=dG(6,10);
% dF(4,6)=dG(8,10);
% dF(5,6)=dG(10,10);
% dF(6,6)=dG(12,10);
%Moment

%dMoment

% F
% dF
% dG
% Moment
% 
% str=input("Look at moments and F");

end


```

.

.

.

```
function [ZnNew] = CalculateZnAfterHermiteSeriesMultiplication(Zn,alpha,MOrder)

HOrder=MOrder-2;

Ndata=length(Zn);

[Hz] = HermitePoly(HOrder);

for nn=1:2:HOrder+1
    ZZ(nn,1:Ndata)=Zn(1:Ndata).^(nn-1);
end

HermiteSeries(1:Ndata)=alpha(1);
HermiteZ(1:Ndata,1:HOrder)=0;
for nn=2:2:HOrder
    Ndata;
    nn;
    HermiteZ(1:Ndata)=0;
    for mm=1:2:(nn+1)
        %HermiteZ(nn,:)=HermiteZ(nn,:)+Hz(nn+1,mm).*ZZ(mm,:);
        HermiteZ(1:Ndata)=HermiteZ(1:Ndata)+Hz(nn+1,mm).*ZZ(mm,1:Ndata);
    end
    HermiteSeries(1:Ndata)=HermiteSeries(1:Ndata)+ alpha(nn+1).*HermiteZ(1:Ndata);
end
    
ZnNew(1:Ndata)=Zn(1:Ndata).*HermiteSeries(1:Ndata);

% Moment2=sum(ZnNew(1:Ndata).^2)*1/Ndata
% Moment4=sum(ZnNew(1:Ndata).^4)*1/Ndata
% Moment6=sum(ZnNew(1:Ndata).^6)*1/Ndata        
% Moment8=sum(ZnNew(1:Ndata).^8)*1/Ndata
% Moment10=sum(ZnNew(1:Ndata).^10)*1/Ndata
% Moment12=sum(ZnNew(1:Ndata).^12)*1/Ndata 
% Moment14=sum(ZnNew(1:Ndata).^14)*1/Ndata 



plot((1:Ndata),Zn(1:Ndata),'g',(1:Ndata),ZnNew(1:Ndata),'r')

end


```

.

.

.

```
function [ObjMomentOut] = CalculateObjMoment(Moment0,Moment,w,MOrder)

ObjMomentOut=0;
for nn=1:MOrder
    ObjMomentOut=ObjMomentOut+(Moment(nn)-Moment0(nn)).^2.*w(nn);
end


end


```

.

.

.

```
function [ZZ] = StandardNormalIdealDesity02(Ndata,Sigma)
%Ndata is number of data points in sample, for which we want to find the
%coefficients of the Z-series.
%Sigma=1+.06;
%Sigma=1;
if (rem(Ndata,2)==0)
    NnMid=Ndata/2;
    NnMid
    ZZ(NnMid+1)=norminv(.5+1/Ndata*.5,0,Sigma);
    ZZ(NnMid)=norminv(.5-1/Ndata*.5,0,Sigma);
    for nn=2:NnMid-1
        ZZ(nn+NnMid)=norminv(.5+(nn-.5)*1/Ndata,0,Sigma);
        ZZ(-nn+1+NnMid)=norminv(.5-(nn-.5)*1/Ndata,0,Sigma);
    end
    %A=normcdf((Ndata-1)/Ndata);
    %ZZ(Ndata)=exp(-5*A^2)/(1/Ndata);
    A=norminv((Ndata-1)/Ndata);
    ZZ(Ndata)=A +0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
    ZZ(1)=-A-0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
end

if (rem(Ndata,2)==1)
    NnMid=(Ndata+1)/2;
    ZZ(NnMid)=0;
    for nn=1:NnMid-2
        ZZ(nn+NnMid)=norminv(.5+(nn)*1/Ndata,0,Sigma);
        ZZ(-nn+NnMid)=norminv(.5-(nn)*1/Ndata,0,Sigma);
    end
   A=norminv((Ndata-1)/Ndata);
    ZZ(Ndata)=A +0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
    ZZ(1)=-A-0.398942 *exp(-.5*A^2)/sqrt(1/Ndata)/sqrt(.5);
end

%ZZ
%A
%plot(ZZ)
%str=input("Look at density plot standard")

end


```

.

.

.

```
function [Coeff,Zy] = CalculateHermiteSeriesFromData01(Yin,Order,ZI)

Ndata=length(Yin);

%Hz=HermitePoly(Order);  
MeanYin=sum(Yin(1:Ndata))/Ndata;
Ym(1:Ndata)=Yin(1:Ndata)-MeanYin;
YmVar=sum(Ym(1:Ndata).^2)/Ndata;
Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);



% [Zn] = StandardNormalIdealDesity02(Ndata,1);
% %[ZI] = CalculateZI(Zn);
% 
% 
% ZI=Zn;
%Below W is the design matrix for least squares regression i.e the matrix
%that contains all the hermite polynomials calculated at ideal normal
%density grid of size Ndata. 
[W] = EvalHermiteArrayH0(ZI,Order);

%We first sort the data so that we can assign one appropriate Z-grid
%point(and associated hermite polynomials calculated at that grid point)
%to each data element. This ideal normal density Z-grid is
%constructed so that its size is equal to data observations count. We
%suppose that first derivative of random variables with repsect to Z
%does not switch sign meaning that increasing values of data
%observations have to aligned with increasing values of ideal normal
%density grid.
[Ys,I]=sort(Y(1:Ndata));
%In the line below, the data sort is reversed so that now the ideal 
%normal density grid elements assigned to various observations of random 
%variable face it on data observations index. For details, Please look 
%on interent the definition of matlab sort command with role of "I" 
%in output and how it alters the index.   

%%Zs1(I(1:Ndata))=ZI(1:Ndata);

%Below the values to be regressed facing the design matrix are assigned
Ymu(1:Ndata,1)=Ys(1:Ndata);
%Below, implement least squares regression.
coeff=(W'*W)$W'*Ymu);
%Store in coefficietns array of all random varaibles
Coeff(1:Order+1)= coeff(1:Order+1,1);
%Store the associated Z in Z-array of all coefficients.   
Zy(I(1:Ndata))=W(1:Ndata,2);



Coeff(1:Order+1)=Coeff(1:Order+1).*sqrt(YmVar);
Coeff(1)=Coeff(1)+MeanYin;

end




```

.

.

.

```
function [Wh] = EvalHermiteArrayH0(Z,Order)

%Evaluates first Order-th hermites at the array of Z's. If input array of Z
%has a size of 100 and Order is 4, it will return a 100 X 5 array.

Hz=HermitePoly(Order);

Wh(1:length(Z),1:Order+1)=0;
for nn=1:Order+1
    Wh(:,nn)=0;
    for mm=1:nn
        Wh(:,nn)=Wh(:,nn)+Hz(nn,mm).*Z(:).^(mm-1);
    end
end

end


```

.

.

.

```
function [Ycorr,Ydecorr,coeffcorr] = FindDecorrelatedYwrtX(Y,Zx,Order)

%1. This function takes in observations of a random variable Y.
%2. This function takes in Zx underlying Hermite-series of another correlated variable X
%which is in the order of observations of X and Y. 
%3. This function takes in Order upto which to perform the decorrelation analytics.

%This function takes observations of Y, and finds out a part of
%each of the observations that is correlated with X and another par that is
%orthogonal to X.

%Correlated part is returned as Ycorr.
%Orthogonal part is returned as Ydecorr
%Coefficients of correlated part as a function of Hermite polynomials
%series of Zx are returned in coeffcorr/

    Ndata=length(Y);
   
    Ycorr(1:Ndata,1)=0;
    Ymu1(1:Ndata,1)=Y(1:Ndata);
        %Z1(:)=Zx(:,1);
        %Below find the least squares regression design matrix including
        %hermites of mmth ZOrtho.
        [W1] = EvalHermiteArrayH0(Zx,Order);
        %Below, do the regression to find the hermite series coefficients of part of
        %random variable Y that is correalted with Zx.

        coeffcorr=(W1'*W1)$W1'*Ymu1);
 
        for hh=1:Order+1
            %Below Y corr continues to sum over all hermites of Zx
            Ycorr(1:Ndata,1)=Ycorr(1:Ndata,1)+coeffcorr(hh,1).*W1(1:Ndata,hh);
            
        end

    Ydecorr(1:Ndata,1)=Y(1:Ndata,1)-Ycorr(1:Ndata,1);




end


```

.

.

.

.

```
function [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(X,Paths,NoOfBins,MaxCutOff )
%Processes monte carlo paths to return a series Xdensity as a function of IndexOut. IndexMax is the maximum value of index.
% 


Xmin=10000;
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

.

.

.

```
function [Z] = CalculateZgivenXAndHSeriesCoeffs(X,Coeff,Order)

%Finds Z given an array of X-values and Coeffs of hermite series.

Z(1:length(X))=0;
Hz=HermitePoly(Order);
median=0;
for nn=1:Order+1
    median=median+Coeff(nn).*Hz(nn,1);
end

for nn=1:length(X)
    Z(nn)=CalculateZgivenXAndHermiteSeriesBisection(X(nn),Coeff,median,Hz,Order);
end

end


```

.

.

.

```
function [Z]=CalculateZgivenXAndHermiteSeriesBisection(Y,coeff,median,Hz,Order)
%[Z]=CalculateZgivenXAndZSeriesBisection2C5(Y,c0,c);

%This program takes a value of Y as input and returns the corresponding 
%value of Z given the parameters of the Z-series.
%It first see if the value of Y is greater than median or smaller than
%median. If the value of Y is greater than median Z has to be greater than
%zero and if the value of Y is smaller than median Z has to be negative.
% Once we know whether Z is greater than Z or smaller than Zero, we divide
% the program into two repeated if loops, one for Z greater than zero and 
%one for Z smaller than zero. 
%If Z is positive, we have to assign it a valid band of upper and
%lower values between which it can be found. 
%This is done sequentially by calculating Y(.5) at Z=.5, if Y is smaller 
%than Y(.5), we know that true value of Y will lie between 0 and .5
%so we assign a lower band value Za=0 and upper band value Zb=.5
%If however Y is greater than Y(.5), we know that true Z should be larger 
%than .5 and we again evaluate Y(1) at Z=1, If Y is smaller than Y(1), 
%we know that true value of Z should be between .5 and 1, and we assign a 
%lower band value Za=.5 and upper band value of Zb=1. Through repeated 
%elseif we continue until we find an appropriate band value of Z.

%Once we have determined the upper band value of Zb and lower band value of
%Za, We find Zmid=(Za+Zb)/2. We then evaluate Y(Zmid) and if Y  Y(Zmid), we assign the lower band value equal to Zmid as Za=Zmid. In a
% few iterations, this bisection procedure gets extremely close to true
% value of Z for which Y(Z)=Y
%EvalHermiteSeriesH0(Coeff,Z,Order,Hz)

Z=(Y-coeff(1))/coeff(2);
BracketSize=.5;
if(Y>=median)
    Ztry=.5;
    ZtryBefore=0;
    NotBracketed=1;
    while((NotBracketed)&&(Ztry Ymid)
            Za=Zmid;
        end
    Z=.5*Za+.5*Zb; %This can be taken out of the loop and does not 
    %necessarily have to be calculated again and again. Has to be
    %calculated at least once after the loop to determine the true value of
    %Z.
    
    end
    
end


if(Y=-8))
        [Ytry,dYtrydZ]= EvalHermiteSeriesH0(coeff,Ztry,Order,Hz); 
        if((Y>= Ytry) || (dYtrydZ  Ymid)|| (dYmiddZ<0))
            Za=Zmid;
        elseif(Y<  Ymid)
            Zb=Zmid;
        end
    Z=.5*Za+.5*Zb; %This can be taken out of the loop and does not 
    %necessarily have to be calculated again and again. Has to be
    %calculated at least once after the loop to determine the true value of
    %Z.
    
    end
    
end

       
end


```

.

.

.

```
function [Xh,dXh] = EvalHermiteSeriesH0(Coeff,Z,Order,Hz)

%Hz=HermitePoly(Order);

%Xh=Coeff(1);
Xh(1:length(Z))=0;
dXh(1:length(Z))=0;
for nn=1:Order+1
    for mm=1:nn
        Xh(:)=Xh(:)+Coeff(nn).*Hz(nn,mm).*Z(:).^(mm-1);
    end
    for mm=1:nn-1
        dXh(:)=dXh(:)+Coeff(nn).*(nn-1)*Hz(nn-1,mm).*Z(:).^(mm-1);
    end
end

end


```

.

.

.

```
function [Hz] = HermitePoly(Order)
Hz(1:Order+1,1:Order+1)=0.0;
Hz(1,1)=1.0;
for k=1:Order
    for m=1:k
       Hz(k+1,m+1)=Hz(k,m);
       if (m>1)
            Hz(k+1,m-1)=Hz(k+1,m-1)-(m-1)*Hz(k,m);
       end
    end
end

end


```

.

.

.

```
function [CoeffR,CoeffX] = RegressYOnX(Y,Xin,NN,Dim,Order)


[ZI] = StandardNormalIdealDesity02(NN,1);
for mm=1:Dim
    [CoeffX(mm,1:Order+1),Zx(1:NN,mm)] = CalculateHermiteSeriesFromData(Xin(1:NN,mm),Order,ZI);
end

WW(1:NN,1:Order+1)=EvalHermiteArrayH0(Zx(1:NN,1),Order);


for mm=2:Dim
    WW(1:NN,(mm-1)*Order+2:mm*Order+1)=EvalHermiteArrayH1(Zx(1:NN,mm),Order);
end

Ymu(1:NN,1)=Y(1:NN);

CoeffR=(WW'*WW)$WW'*Ymu);


end


```

.

.

.

```
function [] = PlotHermiteSeriesDensityAndRvGraph(c0,c,Color)

Index=length(c);

dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=45*4;  % No of normal density subdivisions
NnMid=((1+Nn)/2)*dNn;
Z(1:Nn)=(((1:Nn)*dNn)-NnMid);
%Z
%str=input('Look at Z');
%Now calculate Y as a function of normal random variable.
[W] = EvalHermiteArrayH0(Z,Index);  

Y(1:Nn,1)=c0;
for nn=1:Index
    Y(1:Nn,1)=Y(1:Nn,1)+W(1:Nn,nn+1).*c(nn);
end

%Now take change of densities derivative of Y with respect to normal
DfY(1:Nn)=0;
for nn=2:Nn-1
    DfY(nn) = (Y(nn + 1) - Y(nn - 1))/(Z(nn + 1) - Z(nn - 1));
    %Change of variable derivative for densities
end
DfY(Nn)=DfY(Nn-1);
DfY(1)=DfY(2);

%Now calculate the density of Y from density of normal random variable
%using change of probability derivative.
pY(1:Nn)=0;
for nn = 1:Nn    
    pY(nn) = (normpdf(Z(nn),0, 1))/abs(DfY(nn));
end
Y;
%clf;
plot(Y(1:Nn),pY(1:Nn),Color);
%title('Density of the Z-Series Variable with Fitted Moments');
title('Density of the Uniform Variable in terms of Hermite Series');
str=input('Look at density');

%clf;
%plot(Z(1:Nn),Y(1:Nn),Color);
%title('Graph of Z-Series Variable as a function of underlying standard normal');
%str=input('Look at Graph of Z-Series Variable as a function of underlying standard normal');


end


```

.

.

.

```
function [Hz] = HermitePoly(Order)
Hz(1:Order+1,1:Order+1)=0.0;
Hz(1,1)=1.0;
for k=1:Order
    for m=1:k
       Hz(k+1,m+1)=Hz(k,m);
       if (m>1)
            Hz(k+1,m-1)=Hz(k+1,m-1)-(m-1)*Hz(k,m);
       end
    end
end

end


```

```

---

## Error 45: Unbalanced $: 83

**Snippet:** `In order to calibrate the coefficients of three dimensional conditional Hermite-`

**Full content:**

```
In order to calibrate the coefficients of three dimensional conditional Hermite-Series of W, we first describe what form this three dimensional Hermite-Series has. It has the following form





\begin{align}



\left[  W\,  \,|X,Y \right]&(Z_w \, , \, Z_y,\,Z_x\,)\, \,\\

&=\, \Big[\, cH_0 \, + \, cH_{1,0,0} \,H_1(Z_w) \,+\, cH_{2,0,0} \, H_2(Z_w) \,\, + \, cH_{3,0,0} \,H_3(Z_w)\,\,+\, cH_{4,0,0} \, H_4(Z_w) \,\, + \, cH_{5} \,H_5(Z_w)\,\,\Big] \\

&+\, \Big[\, 0.0 \, + \, cH_{0,1,0} \,H_1(Z_x) \,+\, cH_{0,2,0} \, H_2(Z_x) \,\, + \, cH_{0,3,0} \,H_3(Z_x)\,\,+\,\ldots\,\Big] \\

&+\, \Big[ \, 0.0 \, + \, cH_{1,1,0} \,H_1(Z_x) \,+\, cH_{1,2,0} \, H_2(Z_x) \,\, + \, cH_{1,3,0} \,H_3(Z_x)\,\,+\,\ldots\, \Big] \, H_1(Z_w) \, \\

&+\, \Big[ \, 0.0 \, + \, cH_{2,1,0} \,H_1(Z_x) \,+\, cH_{2,2,0} \, H_2(Z_x) \,\, + \, cH_{2,3,0} \,H_3(Z_x)\,\,+\,\ldots\, \Big] \, H_2(Z_w) \, \\

&+\, \Big[ \, 0.0 \, + \, cH_{3,1,0} \,H_1(Z_x) \,+\, cH_{3,2,0} \, H_2(Z_x) \, \,+ \, cH_{3,3,0} \,H_3(Z_x)\,\,+\,\ldots\, \Big] \, H_3(Z_w) \, \\

&+\, \Big[ \, 0.0 \, + \, cH_{4,1,0} \,H_1(Z_x) \,+\, cH_{4,2,0} \, H_2(Z_x) \,\, + \, cH_{4,3,0} \,H_3(Z_x)\,\,+\,\ldots\, \Big] \, H_4(Z_w) \, \\

&+\, \Big[ \, 0.0 \, + \, cH_{5,1,0} \,H_1(Z_x) \,+\, cH_{5,2,0} \, H_2(Z_x) \, \,+ \, cH_{5,3,0} \,H_3(Z_x)\,\,+\,\ldots\, \Big] \, H_5(Z_w) \, \\

&+\, \Big[\, 0.0 \, + \, cH_{0,0,1} \,H_1(Z_y) \,+\, cH_{0,0,2} \, H_2(Z_y) \,\, + \, cH_{0,0,3} \,H_3(Z_y)\,\,+\,\ldots\,\Big] \\

&+\, \Big[ \, 0.0 \, + \, cH_{1,0,1} \,H_1(Z_y) \,+\, cH_{1,0,2} \, H_2(Z_y) \,\, + \, cH_{1,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_1(Z_w) \, \\

&+\, \Big[ \, 0.0 \, + \, cH_{2,0,1} \,H_1(Z_y) \,+\, cH_{2,0,2} \, H_2(Z_y) \,\, + \, cH_{2,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_2(Z_w) \, \\

&+\, \Big[ \, 0.0 \, + \, cH_{3,0,1} \,H_1(Z_y) \,+\, cH_{3,0,2} \, H_2(Z_y) \, \,+ \, cH_{3,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_3(Z_w) \, \\

&+\, \Big[ \, 0.0 \, + \, cH_{4,0,1} \,H_1(Z_y) \,+\, cH_{4,0,2} \, H_2(Z_y) \,\, + \, cH_{4,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_4(Z_w) \, \\

&+\, \Big[ \, 0.0 \, + \, cH_{5,0,1} \,H_1(Z_y) \,+\, cH_{5,0,2} \, H_2(Z_y) \, \,+ \, cH_{5,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_5(Z_w) \, \\

\end{align} 



Following our two dimensional hermite-series coefficient calibration procedure, we remove any correlation effect of $Z_x$ and $Z_y$ from W and make sure that any remaining part of W with this effect removed is orthogonal to both $Z_x$ and $Z_y$ and this would ensure that its underlying Z_w is orthogonal to both $Z_x$ and $Z_y$.



We calibrate the following two rows from the above three dimensional Hermite-Series of W from correlations with X and Y.



\begin{align}

&+\, \Big[\, cH_{0,0,0} \, + \, cH_{0,1,0} \,H_1(Z_x) \,+\, cH_{0,2,0} \, H_2(Z_x) \,\, + \, cH_{0,3,0} \,H_3(Z_x)\,\,+\,\ldots\,\Big] \\

&+\, \Big[\, 0.0 \, + \, cH_{0,0,1} \,H_1(Z_y) \,+\, cH_{0,0,2} \, H_2(Z_y) \,\, + \, cH_{0,0,3} \,H_3(Z_y)\,\,+\,\ldots\,\Big] \\

\end{align}



We find an orthogonal form of W represented by $\tilde{W}$ which is orthogonal of both X and Y and is found as



\begin{align}

& \tilde{W}_p\,=\,W_p\,-\, \\ 

&+\, \Big[\, cH_{0,0,0} \, + \, cH_{0,1,0} \,H_1(Z_{x_p}) \,+\, cH_{0,2,0} \, H_2(Z_{x_p}) \,\, + \, cH_{0,3,0} \,H_3(Z_{x_p})\,\,+\,\ldots\,\Big] \\

&+\, \Big[\, 0.0 \, + \, cH_{0,0,1} \,H_1(Z_{y_p}) \,+\, cH_{0,0,2} \, H_2(Z_{y_p}) \,\, + \, cH_{0,0,3} \,H_3(Z_{y_p})\,\,+\,\ldots\,\Big] \\

\end{align}

Please note that p above indicates pth data element in a sample of total P data and the above equation is applied on each pth data element pair (of X, Y and W) in joint sense.



Now we take cross moments of $Z_X$ and this orthogonal $\tilde{W}$ and fit a two dimensional Hermite-series of the form below to it. Please note that we now do not fit other lines to this data. We only fit the following portion omitting the other lines and this is fitted to cross moments of  $Z_X$ and $\tilde{W}$ given below as



\begin{align}

& \,\left[\tilde{W}|\,X\right](Z_w,Z_x)\,=\, \\



&+\, \Big[ \, cH_{1,0,0} \, + \, cH_{1,1,0} \,H_1(Z_x) \,+\, cH_{1,2,0} \, H_2(Z_x) \,\, + \, cH_{1,3,0} \,H_3(Z_x)\,\,+\,\ldots\, \Big] \, H_1(Z_w) \, \\

&+\, \Big[ \,  cH_{2,0,0} \, + \, cH_{2,1,0} \,H_1(Z_x) \,+\, cH_{2,2,0} \, H_2(Z_x) \,\, + \, cH_{2,3,0} \,H_3(Z_x)\,\,+\,\ldots\, \Big] \, H_2(Z_w) \, \\

&+\, \Big[ \,  cH_{3,0,0} \, + \, cH_{3,1,0} \,H_1(Z_x) \,+\, cH_{3,2,0} \, H_2(Z_x) \, \,+ \, cH_{3,3,0} \,H_3(Z_x)\,\,+\,\ldots\, \Big] \, H_3(Z_w) \, \\

&+\, \Big[ \,  cH_{4,0,0} \, + \, cH_{4,1,0} \,H_1(Z_x) \,+\, cH_{4,2,0} \, H_2(Z_x) \,\, + \, cH_{4,3,0} \,H_3(Z_x)\,\,+\,\ldots\, \Big] \, H_4(Z_w) \, \\

&+\, \Big[ \,  cH_{5,0,0} \, + \, cH_{5,1,0} \,H_1(Z_x) \,+\, cH_{5,2,0} \, H_2(Z_x) \, \,+ \, cH_{5,3,0} \,H_3(Z_x)\,\,+\,\ldots\, \Big] \, H_5(Z_w) \, \\

\end{align}



Please note that we have not done any fitting of coefficients multiplied with hermite polynomials of $Z_y$ on this step.



After fitting above form, we can remove the effect of coefficients that depend on $Z_x$ simply by subtracting the above form $\tilde{W}$ as





\begin{align}

& \,\tilde{\tilde{W}}_p=\,\tilde{W}_p\,-\, \\

&\, \Big[ \, cH_{1,1,0} \,H_1(Z_{x_p}) \,+\, cH_{1,2,0} \, H_2(Z_{x_p}) \,\, + \, cH_{1,3,0} \,H_3(Z_{x_p})\,\,+\,\ldots\, \Big] \, H_1(Z_{w_p}) \, \\

&-\, \Big[ \, \, cH_{2,1,0} \,H_1(Z_{x_p}) \,+\, cH_{2,2,0} \, H_2(Z_{x_p}) \,\, + \, cH_{2,3,0} \,H_3(Z_{x_p})\,\,+\,\ldots\, \Big] \, H_2(Z_{w_p}) \, \\

&-\, \Big[ \, \, cH_{3,1,0} \,H_1(Z_{x_p}) \,+\, cH_{3,2,0} \, H_2(Z_{x_p}) \, \,+ \, cH_{3,3,0} \,H_3(Z_{x_p})\,\,+\,\ldots\, \Big] \, H_3(Z_{w_p}) \, \\

&-\, \Big[ \,  \, cH_{4,1,0} \,H_1(Z_{x_p}) \,+\, cH_{4,2,0} \, H_2(Z_{x_p}) \,\, + \, cH_{4,3,0} \,H_3(Z_{x_p})\,\,+\,\ldots\, \Big] \, H_4(Z_{w_p}) \, \\

&-\, \Big[ \,  \, cH_{5,1,0} \,H_1(Z_{x_p}) \,+\, cH_{5,2,0} \, H_2(Z_{x_p}) \, \,+ \, cH_{5,3,0} \,H_3(Z_{x_p})\,\,+\,\ldots\, \Big] \, H_5(Z_{w_p}) \, \\

\end{align}



Please note that p above indicates pth data element in a sample of total P data and the above equation is applied on each pth data element pair (of X, Y and W) in joint sense.



Please also note that going from  $\tilde{W}$  to  $\tilde{\tilde{W}}$ does not alter correlations of $Z_w$ with $Z_x$ and $Z_y$ and both  $\tilde{W}$  and  $\tilde{\tilde{W}}$ remain orthogonal to $Z_x$ and $Z_y$.



Now we take cross moments of $Z_y$ and this double tilde  $\tilde{\tilde{W}}$ and fit a two dimensional Hermite-series of the form below to it. Please note that we now do not fit other lines to this data. We only fit the following portion omitting the other lines and this is fitted to cross moments of  $Z_y$ and $\tilde{\tilde{W}}$ given below as



\begin{align}



& \,\left[\tilde{\tilde{W}}|\,Y\right](Z_w,Z_y)\,=\, \\

&+\, \Big[ \, cH_{1,0,0} \, + \, cH_{1,0,1} \,H_1(Z_y) \,+\, cH_{1,0,2} \, H_2(Z_y) \,\, + \, cH_{1,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_1(Z_w) \, \\

&+\, \Big[ \, cH_{2,0,0} \, + \, cH_{2,0,1} \,H_1(Z_y) \,+\, cH_{2,0,2} \, H_2(Z_y) \,\, + \, cH_{2,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_2(Z_w) \, \\

&+\, \Big[ \, cH_{3,0,0} \, + \, cH_{3,0,1} \,H_1(Z_y) \,+\, cH_{3,0,2} \, H_2(Z_y) \, \,+ \, cH_{3,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_3(Z_w) \, \\

&+\, \Big[ \, cH_{4,0,0} \, + \, cH_{4,0,1} \,H_1(Z_y) \,+\, cH_{4,0,2} \, H_2(Z_y) \,\, + \, cH_{4,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_4(Z_w) \, \\

&+\, \Big[ \, cH_{5,0,0} \, + \, cH_{5,0,1} \,H_1(Z_y) \,+\, cH_{5,0,2} \, H_2(Z_y) \, \,+ \, cH_{5,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_5(Z_w) \, \\



\end{align}



 From the above calibration all $cH_{n,0,0}$ will become the final values of these coefficients in the first equation and rest of it shown as will be dependent on $Z_y$ and $Z_w$ as shown below.



\begin{align}



&+\, \Big[\, cH_{1,0,1} \,H_1(Z_y) \,+\, cH_{1,0,2} \, H_2(Z_y) \,\, + \, cH_{1,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_1(Z_w) \, \\

&+\, \Big[  \, cH_{2,0,1} \,H_1(Z_y) \,+\, cH_{2,0,2} \, H_2(Z_y) \,\, + \, cH_{2,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_2(Z_w) \, \\

&+\, \Big[  \, cH_{3,0,1} \,H_1(Z_y) \,+\, cH_{3,0,2} \, H_2(Z_y) \, \,+ \, cH_{3,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_3(Z_w) \, \\

&+\, \Big[  \, cH_{4,0,1} \,H_1(Z_y) \,+\, cH_{4,0,2} \, H_2(Z_y) \,\, + \, cH_{4,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_4(Z_w) \, \\

&+\, \Big[  \, cH_{5,0,1} \,H_1(Z_y) \,+\, cH_{5,0,2} \, H_2(Z_y) \, \,+ \, cH_{5,0,3} \,H_3(Z_y)\,\,+\,\ldots\, \Big] \, H_5(Z_w) \, \\



\end{align}



This will complete the third variable coefficients calibration procedure.



This way when calibrating coefficients of higher order hermite-series, first we have to remove the correlation effect of all previously calibrated variables and then find the remaining orthogonal part of the variable. This orthogonal part of the variable will be used to construct the orthogonal gaussian underlying this variable and then (in order to fit cross hermite terms with earlier variables) we will fit the cross-moments of each previously calibrated variables one by one and each time we fit a cross-term, we remove its effect by subtracting these fitted cross-terms from its value from previous orthogonal variable. We found cross-hermites of $Z_x$ and $Z_w$ by calibrating to cross moments of $\tilde{W}$ and $Z_X$. Then we subtracted these terms from \{\tilde{W}$ to find double tilde  W $\tilde{\tilde{W}}$ and then used its cross moments with $Z_y$ to calibrate the coefficients of cross-hermites of $Z_y$ and $Z_w$. For fourth order coefficients fitting, we would have to find a triple tilde by removing the effect of recently calibrated $Z_y$ and $Z_w$ from double tilde and then find its cross-moments with $Z_w$ (or whatever the third variable).



I realize that fourth variable calibration is directly simple extension of this three variable coefficients calibration so I am not writing that.
```

---

## Error 46: Unbalanced $: 1

**Snippet:** `Friends, here is the new very preliminary program for calculation of 2D Coeffici`

**Full content:**

```
Friends, here is the new very preliminary program for calculation of 2D Coefficients.

.

.

```
function []= ConditionalDensityHermitesBivariateNewtonItersRegSqr()

%SV SDE is 
%dV(t)=mu1 V(t)^beta1 dt+ mu2 V(t)^beta2 dt + sigma0 V(t)^gamma dZ(t)
%In mean reverting SDEs we ususally have
%mu1= kappaV * thetaV
%beta1=0
%mu2=-kappa
%beta2=0

Order=5;
%NDim=4;%Three assets and one SV.
NMomentsY=Order+1;
NMomentsX=Order+1;


w2D5(1:NMomentsY,1:NMomentsX)=1;
 w2D6(1:NMomentsY,1:NMomentsX)=1;
for nn=NMomentsY-1:-1:1
    for mm=NMomentsX-1:-1:1
        
        w2D5(nn,mm)=w2D5(nn+1,mm+1)*(nn+1).^5*(mm+1).^5.0;
        w2D6(nn,mm)=w2D6(nn+1,mm+1)*(nn+1).^6*(mm+1).^6.0;
    end
end
 
 
 w2D0(1:NMomentsY,1:NMomentsX)=1;
 w2Dh(1:NMomentsY,1:NMomentsX)=1;
 w2D1(1:NMomentsY,1:NMomentsX)=1;
 w2D2(1:NMomentsY,1:NMomentsX)=1;
 w2D3(1:NMomentsY,1:NMomentsX)=1;
 w2D4(1:NMomentsY,1:NMomentsX)=1;
 
for nn=NMomentsY-1:-1:1
    for mm=NMomentsX-1:-1:1
        w2Dh(nn,mm)=w2Dh(nn+1,mm+1)*(nn+1).^.5*(mm+1).^.5;
        w2D1(nn,mm)=w2D1(nn+1,mm+1)*(nn+1)*(mm+1);
        w2D2(nn,mm)=w2D2(nn+1,mm+1)*(nn+1).^2*(mm+1).^2.0;
        w2D3(nn,mm)=w2D3(nn+1,mm+1)*(nn+1).^3*(mm+1).^3.0;
        w2D4(nn,mm)=w2D4(nn+1,mm+1)*(nn+1).^4*(mm+1).^4.0;
    end
end

%%%%%%%%%%%%%%%%%%%5

V0=1.00;%.32;
V00=V0;
thetaV=1.250;%.045;%1;%.04;
kappaV=.20;%1.5;%1.5;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.5;%.950;
sigma0=.55;%.45;%
dt=.03125/2;
Tt=64*2;
T=Tt*dt;

seed0=52130649;
seed0=94210876;
rng(seed0, 'twister')
paths=10000;
V(1:paths,1)=V0;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
TT1=30; %Transition distribution start
TT2=124; %Transition distribution end

Random2(1:paths/2,1)=0;

for tt=1:Tt
    
    Random2(1:paths/2)=randn(paths/2,1);
    Random2(paths/2+1:paths)=-Random2(1:paths/2);

    V(1:paths,1)=V(1:paths,1)+ ...
        (mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*sqrt(dt) + ...
        (mu1.*beta1*V(1:paths,1).^(beta1-1) + mu2.*beta2.*V(1:paths,1).^(beta2-1)).* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt^2/2 + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*(1-1/sqrt(3))*dt^1.5) + ...
        .5*(mu1.*beta1.*(beta1-1).*V(1:paths,1).^(beta1-2) + mu2.*beta2.*(beta2-1).*V(1:paths,1).^(beta2-2)).* ...    
        sigma0^2.*V(1:paths,1).^(2*gamma).*dt^2/2 + ...
        sigma0*gamma*V(1:paths,1).^(gamma-1) .* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2).*Random2(1:paths,1).*1/sqrt(3)*dt^1.5 + ...
        sigma0.*V(1:paths,1).^gamma .*(Random2(1:paths,1).^2-1)*dt/2) + ...
        .5*sigma0*gamma*(gamma-1).*V(1:paths,1).^(gamma-2) .* ...
        sigma0^2.*V(1:paths,1).^(2*gamma) .*Random2(1:paths,1).*1/sqrt(3)*dt^1.5;

    V(V<0)=.00001;

    
    if(tt==TT1)
        Xin(1:paths,1)=V(1:paths,1);
    end
        
    if(tt==TT2)
        Yin(1:paths,1)=V(1:paths,1);
    end
end

str=input("I have reached stone 1");

Order=5;
% 
Ndata=paths;
% 
[ZI] = MomentMatchedStandardNormalDiscretizedDensity(Ndata);

[XCoeffH,Zx] = CalculateHermiteSeriesFromData01(Xin,Order,ZI); 
[XCoeffZ(1:Order+1)] = ConvertHermiteSeriesToZSeries01(XCoeffH(1:Order+1),Order);
for qq1=1:Order+1
    XMoments(qq1)=sum(Xin(1:paths).^qq1)/paths;
end
[XCoeffZ(1),XCoeffZ(2:6)] = CalculateZSeriesDensityFromRawMomentsM6(XMoments,XCoeffZ(2:6));

for nn=1:paths
  
  [Zx(nn)]=CalculateZgivenXAndZSeriesBisection2C5Improved(Xin(nn),XCoeffZ(1),XCoeffZ(2:6));
end

Zx0(1:Ndata,1)=Zx(1:Ndata);

[YCoeffH,Zy] = CalculateHermiteSeriesFromData01(Yin,Order,ZI); 
[YCoeffZ(1:Order+1)] = ConvertHermiteSeriesToZSeries01(YCoeffH(1:Order+1),Order);

for pp1=1:Order+1
    YMoments(pp1)=sum(Yin(1:paths).^pp1)/paths;
end
[YCoeffZ(1),YCoeffZ(2:6)] = CalculateZSeriesDensityFromRawMomentsM6(YMoments,YCoeffZ(2:6));

[YCoeffH0] = ConvertZSeriesToHermiteSeriesNew(YCoeffZ,Order);  

for nn=1:paths
  [Zy(nn)]=CalculateZgivenXAndZSeriesBisection2C5Improved(Yin(nn),YCoeffZ(1),YCoeffZ(2:6));
end

HH=5;
[CorrH] = CalculateCorrelationBivariateHermiteCH0(Zx,Zy,paths,HH)
   
CorrH
 
str=input("Look at hermites correlation");
   


Coeffyx2(1)=YCoeffH0(1);
Coeffyx2(2:6)=CorrH(1:5).*YCoeffH0(2:6);

Ydecorr(1:Ndata,1)=Yin(1:Ndata,1)-Coeffyx2(1) ...
    -Coeffyx2(2).*Zx0(1:Ndata,1) ...
    -Coeffyx2(3).*(Zx0(1:Ndata,1).^2-1) ...
    -Coeffyx2(4).*(Zx0(1:Ndata,1).^3-3*Zx0(1:Ndata,1)) ...
    -Coeffyx2(5).*(Zx0(1:Ndata,1).^4-6*Zx0(1:Ndata,1).^2+3) ...
    -Coeffyx2(6).*(Zx0(1:Ndata,1).^5-10*Zx0(1:Ndata,1).^3+15*Zx0(1:Ndata,1));% ...

Coeffyx2
PlotHermiteSeriesDensityAndRvGraph(Coeffyx2(1),Coeffyx2(2:Order+1),'b')

str=input("Look at initial correlated hermite series plot---2");


[YdCoeffH,Zyd] = CalculateHermiteSeriesFromData01(Ydecorr,Order,ZI); 
[YdCoeffZ(1:Order+1)] = ConvertHermiteSeriesToZSeries01(YdCoeffH(1:Order+1),Order);

for pp1=1:Order+1
    YdecorrMoments(pp1)=sum(Ydecorr(1:paths).^pp1)/paths;
end
[YdCoeffZ(1),YdCoeffZ(2:6)] = CalculateZSeriesDensityFromRawMomentsM6(YdecorrMoments,YdCoeffZ(2:6));

[YdCoeffH] = ConvertZSeriesToHermiteSeriesNew(YdCoeffZ,Order);  

for nn=1:paths
  [Zyd(nn)]=CalculateZgivenXAndZSeriesBisection2C5Improved(Ydecorr(nn),YdCoeffZ(1),YdCoeffZ(2:6));
end

MaxIter=15000;
%[YCoeffHHOut,ObjFunc] = HSeriesCoeffsFromDataIterative2D1st(YObs,Zx,Zy,MaxIter,Order)
[YCoeffHH,ObjFunc] = HSeriesCoeffsFromDataIterative2D1st(Yin,Zx,Zyd,MaxIter,Order,paths)



YCoeffHH


%YCoeffHH(1,1:Order+1)=YCoeffHH(1,1:Order+1)+Coeffyx2(1,1:Order+1);


str=input("Look at the new form of 2D Hermite-series YCoeffHH");
MaxIter=500;
%%%%%%%%%%%%%%%%%%%%%%%%%%[YCoeffHH,ObjFunc] = HSeriesCoeffsFromCrossMomentsIterative2D2nd(YCoeffHH,XCoeffZ,MomentsYX0,YCoeffZ,MaxIter,w2D)
for pp1=1:Order+1
      for qq1=1:Order+1
          %MomentsYX0((pp1-1)*(Order+1)+qq1,1)=sum(Yin(1:paths).^pp1.*Xin(1:paths).^qq1)/paths;
          %MomentsYX(pp1,qq1)=sum(Yin(1:paths).^pp1.*Xin(1:paths).^qq1)/paths;
          %if(pp1~=5)
          MomentsYX0((pp1-1)*(Order+1)+qq1,1)=sum(Yin(1:paths).^pp1.*Zx0(1:paths,1).^qq1)/paths;
          MomentsYX(pp1,qq1)=sum(Ydecorr(1:paths).^pp1.*Zx0(1:paths,1).^qq1)/paths;
          %end
          %if(pp1==5)
          %MomentsYX0((pp1-1)*(Order+1)+qq1,1)=sum(Ydecorr(1:paths).^pp1.*Zx1(1:paths,1).^qq1)/paths/1.1;
          %MomentsYX(pp1,qq1)=sum(Ydecorr(1:paths).^pp1.*Zx1(1:paths,1).^qq1)/paths/1.1;
          %end
          if(pp1==1)
              %MomentsYXN1(1,qq1)=sum(Yin(1:paths).^pp1.*Xin(1:paths).^qq1)/paths;%/(sum(Xin(1:paths).^(qq1)));
              
              %MomentsYXN1(1,qq1)=sum(Yin(1:paths).^pp1.*Zx1(1:paths,1).^qq1)/paths;
          end
      end
  end
  
  MomentsYX
  
 ZCoeff(1)=0.0;
  ZCoeff(2)=1;
  ZCoeff(3:6)=0.0; 

MaxIter=500; 
%In the function below, we do iterative optimization on all 2D Hermite
%coefficients including the first row. This function is applied when we
%have become too close to the true values by optimization through previous
%function.
[YCoeffHH,ObjFunc] = HSeriesCoeffsFromCrossMomentsIterative2D2nd(YCoeffHH,ZCoeff,MomentsYX0,YCoeffZ,MaxIter,w2D0);
%[YCoeffHH,ObjFunc] = HSeriesCoeffsFromCrossMomentsIterative2D2nd(YCoeffHH,ZCoeff,MomentsYX0,YCoeffZ,MaxIter,w2D0);




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5


%MaxIter=500; 
%In the function below, we do iterative optimization on all 2D Hermite
%coefficients including the first row. This function is applied when we
%have become too close to the true values by optimization through previous
%function.
%[YCoeffHH,ObjFunc] = HSeriesCoeffsFromCrossMomentsIterative2D2nd(YCoeffHH,XCoeffZ,MomentsYX0,YCoeffZ,MaxIter,w2D0);
%[YCoeffHH,ObjFunc] = HSeriesCoeffsFromCrossMomentsIterative2D2nd(YCoeffHH,ZCoeff,MomentsYX0,YCoeffZ,MaxIter,w2D0);


[YCoeffZZ] = Convert2DHermitesInto2DSeriesNew(YCoeffHH,Order,Order);
  
 [Y1DMoments]=CalculateMomentsOfZSeries(YCoeffZ(1),YCoeffZ(2:6),5,6)

 OrderY=Order;
 OrderX=Order;
 NMoments=6;
 [YMoments] = CalculateMomentsOf2DZSeriesY(YCoeffZZ,OrderY,OrderX,NMoments);
% 
% 
 Y1DMoments
 YMoments
 str=input("Look at comparison of second moments/moments");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%In this block, we do conditional Monte Carlo of SDE which is the true
%numerical 1D conditional density of Y conditional on X having a given
%value. This value of X on which we are conditionin is defined by V10 below.
%We can alter V10 below and it will take out a 1D slice from the 2D density
%of Y conditional on X  taking a specific value (here V10).
%Zx=2.0;
%V10=XCoeffZ(1)+XCoeffZ(2).*Zx+XCoeffZ(3).*Zx^2+XCoeffZ(4).*Zx^3+XCoeffZ(5).*Zx^4+XCoeffZ(6).*Zx^5;
%V10
%str=input("Look at V10");
V10=1.50;
V(1:paths)=V10;
Random2(1:paths,1)=0;

for tt=TT1+1:TT2
    
    Random2(1:paths/2)=randn(paths/2,1);
    Random2(paths/2+1:paths)=-Random2(1:paths/2);


    V(1:paths,1)=V(1:paths,1)+ ...
        (mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*sqrt(dt) + ...
        (mu1.*beta1*V(1:paths,1).^(beta1-1) + mu2.*beta2.*V(1:paths,1).^(beta2-1)).* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2)*dt^2/2 + ...
        sigma0*V(1:paths,1).^gamma .*Random2(1:paths,1)*(1-1/sqrt(3))*dt^1.5) + ...
        .5*(mu1.*beta1.*(beta1-1).*V(1:paths,1).^(beta1-2) + mu2.*beta2.*(beta2-1).*V(1:paths,1).^(beta2-2)).* ...    
        sigma0^2.*V(1:paths,1).^(2*gamma).*dt^2/2 + ...
        sigma0*gamma*V(1:paths,1).^(gamma-1) .* ...
        ((mu1.*V(1:paths,1).^beta1 + mu2.*V(1:paths,1).^beta2).*Random2(1:paths,1).*1/sqrt(3)*dt^1.5 + ...
        sigma0.*V(1:paths,1).^gamma .*(Random2(1:paths,1).^2-1)*dt/2) + ...
        .5*sigma0*gamma*(gamma-1).*V(1:paths,1).^(gamma-2) .* ...
        sigma0^2.*V(1:paths,1).^(2*gamma) .*Random2(1:paths,1).*1/sqrt(3)*dt^1.5;

    V(V<0)=.00001;

end

%Below

NoOfBins=200;
MaxCutOff=10;

[XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(V,paths,NoOfBins,MaxCutOff );


clf;

plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'r');

hold on

for qq=1:6
    
    DataMoments(qq)=sum(V(:).^qq)/paths;
    
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Below, we calculate the value of Zx0 corresponding to X0 (here V10). This
%comes from inverting the Z-series of X so that X=V10;

xOrder=Order;
yOrder=Order;
[Zx0] = CalculateZgivenXAndHSeriesCoeffs(V10,XCoeffH,xOrder);


%Below, we collapse two dimensional pdf of Y|X to one dimensional pdf given
%Zx i.e. this Y|X=X(Zx)
%Here we take out a 1D slice from the 2D density
%of Y conditional on X  taking a specific value (here V10).
He(1)=1;
He(2)=Zx0;
He(3)=Zx0^2-1;
He(4)=Zx0^3-3*Zx0;
He(5)=Zx0^4-6*Zx0.^2+3;
He(6)=Zx0^5-10*Zx0.^3+15*Zx0;
He(7)=Zx0^6-15*Zx0.^4+45*Zx0.^2-15;
He(8)=Zx0^7-21*Zx0.^5+105*Zx0.^3-105*Zx0;

YCoeffh(1:Order+1)=0;
for hh=1:yOrder+1
    for hh2=1:xOrder+1
        YCoeffh(hh)=YCoeffh(hh)+YCoeffHH(hh,hh2).*He(hh2);
    end
end

 [YCoeffz(1:Order+1)] = ConvertHermiteSeriesToZSeries01(YCoeffh(1:Order+1),Order);

 
 [YMomentsModel]=CalculateMomentsOfZSeries(YCoeffz(1),YCoeffz(2:6),5,6);
 
 YMomentsModel
 
 DataMoments
 
 str=input("Look at comparison of moments");
 


PlotHermiteSeriesDensityAndRvGraph(YCoeffh(1),YCoeffh(2:yOrder+1),'b')

%hold on
%PlotHermiteSeriesDensityAndRvGraph(YCoeffh(1),YCoeffh1(2:yOrder+1),'g')
title(sprintf('V00 = %.3f; kappa=%.3f, theta=%.3f,gamma=%.3f,sigma=%.3f;V10=%.3f at TT1=%.3f;TT2=%.3f;Paths=%d ',V00, kappaV, thetaV,gamma,sigma0, V10,(TT1*dt),(TT2*dt),paths));%,sprintf('theta= %f', theta), sprintf('kappa = %f', kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
legend({'Numerical Density','Analytic Density1'}, ...
    'Location','northeast')

str=input("This is the first version without altering the moments of conditional density")


[YMoments0]=CalculateMomentsOfZSeries(YCoeffz(1),YCoeffz(2:6),5,6)



end
```

.

.

.

```
function [YCoeffHHOut,ObjFunc] = HSeriesCoeffsFromDataIterative2D1st(YObs,Zx,Zy,MaxIter,Order,Ndata)


str=input("Hi--I am here again--02");


%This program computes coeffs of 2D Hermite-series when values of raw cross-moments are
%given using Iterative method. 

%MomentsYX0 are raw cross-moments stacked in a single array;
%YCoeffHH are coeffs of 2D Hermite-series to be found and when passed as parameters
%contain starting guess for 2D Hermite-series coeffs.

%Total number of Iterations of the iterative method are given by input 
%parameter MaxIter.
%The present program is written for SeriesOrder=6*6.
%  SeriesOrder=6;  %Z-series till 7th power.
%  
%  NMoments=6;
%  Order=5;
 
 SeriesOrder=Order+1;  %Z-series till 7th power.
 
 NMoments=Order+1;
 
 YMean=sum(YObs)/Ndata;

[Hx] = EvalHermiteArrayH0(Zx,Order);
[Hy] = EvalHermiteArrayH0(Zy,Order);

 for nn=1:Order+1
    for mm=1:Order+1
        Hxy(1:Ndata,(nn-1)*(Order+1)+mm)=Hx(1:Ndata,mm).*Hy(1:Ndata,nn);
        YCoeffHH((nn-1)*(Order+1)+mm,1)=0.000;
    end
end
YCoeffHH(1,1)=YMean;
YModel=Hxy*YCoeffHH;

ObjFuncBest=sum((YObs-YModel).^2+(YObs.^2-YModel.^2).^2) 

str=input("Look at ObjBest");
ObjFuncBestBefore=ObjFuncBest; 
 
%%%%%%Choose the iteration step size.
for nn=1:SeriesOrder
    for mm=1:SeriesOrder
        DeltaX(nn,mm)=.00125/16/(factorial(nn)).^2/factorial(mm).^2;%/2^((nn-1)/2)/2^((mm-1)/2);
        DeltaXMax(nn,mm)=DeltaX(nn,mm)*5;
        
        %DeltaX(nn,mm)=.00125/2/(factorial(nn)).^1.0/factorial(mm).^2.0;
        %DeltaXMax(nn,mm)=DeltaX(nn,mm)*5;
    end
end




% [ObjFuncBest] = CalculateObjMoment2D1D(Moments2D0,Moments2D,w2D,Order+1,Order+1);
% 
% ObjFuncBestBefore
% ObjFuncBest
% ObjFuncBestBefore-ObjFuncBest
% str=input("Look at difference of indicators");

ImproveFlag(1:SeriesOrder,1:SeriesOrder)=1;
ImproveFlagPrev(1:SeriesOrder,1:SeriesOrder)=0;
%ImproveCount(1:SeriesOrder,1:SeriesOrder)=0;
kk=0;
StopCount=0;
while ((kk1)&&(StopCount0)&&(DValue2>0)&&(DValue3>0)&&(DValue4>0)&&(DValue5>0)&&(DValue6>0);
%                 [DValue1] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-3.0,Order);
%                 [DValue2] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,3.0,Order);
%                 [DValue3] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-2.5,Order);
%                 [DValue4] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,2.5,Order);
%                 [DValue5] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-2.0,Order);
%                 [DValue6] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,2.0,Order);
%                 
%                 DFlag2=(DValue1>0)&&(DValue2>0)&&(DValue3>0)&&(DValue4>0)&&(DValue5>0)&&(DValue6>0);
 DFlag1=1;
 DFlag2=1;
            if(rem(kk,1000)==0)
     for nn=1:SeriesOrder
    for mm=1:SeriesOrder
        DeltaX(nn,mm)=.00125/16/(factorial(nn)).^2/factorial(mm).^2;%/2^((nn-1)/2)/2^((mm-1)/2);
        DeltaXMax(nn,mm)=DeltaX(nn,mm)*5;
        
        %DeltaX(nn,mm)=.00125/2/(factorial(nn)).^1.0/factorial(mm).^2.0;
        %DeltaXMax(nn,mm)=DeltaX(nn,mm)*5;
    end
end

            end
       %     str=input("Look at DValues");
            if((ObjFunc10)&&(DValue2>0)&&(DValue3>0)&&(DValue4>0)&&(DValue5>0)&&(DValue6>0);
%                 [DValue1] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-3.0,Order);
%                 [DValue2] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,3.0,Order);
%                 [DValue3] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-2.5,Order);
%                 [DValue4] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,2.5,Order);
%                 [DValue5] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-2.0,Order);
%                 [DValue6] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,2.0,Order);
%                 
%                 DFlag2=(DValue1>0)&&(DValue2>0)&&(DValue3>0)&&(DValue4>0)&&(DValue5>0)&&(DValue6>0);
 %DValue1=1;
 %DValue2=1;
 
 DFlag1=1;
 DFlag2=1;
                if((ObjFunc2DeltaXMax(nn,mm))
           DeltaX(nn,mm)=DeltaXMax(nn,mm);
       end
        end
    end

   
end

ObjFunc=ObjFuncBest;

for nn=1:Order+1
    for mm=1:Order+1
        YCoeffHHOut(nn,mm)=YCoeffHH((nn-1)*(Order+1)+mm,1);
        %bnmHH((nn-1)*(Order+1)+mm,1)=0.0;
    end
end

end
```

.

.

.

```
function [YCoeffHH,ObjFunc] = HSeriesCoeffsFromCrossMomentsIterative2D2nd(YCoeffHH,XCoeffZ,MomentsYX0,YCoeffZ,MaxIter,w2D)



SeriesOrder=6; 
NMoments=6;
Order=5;
 
[YMoments]=CalculateMomentsOfZSeries(YCoeffZ(1),YCoeffZ(2:6),5,6);
        
%Below, we calculate first and 2nd moment of 2D Hermite series       
[MeanHH,M2HH] = CalculateMeanAndVarOf2DHSeriesY(YCoeffHH,Order,Order);
%VarHH is model variance .      
VarHH=M2HH-MeanHH.^2;
%VarIn is input variance 
VarIn=YMoments(2)-YMoments(1).^2;
%Variance correction is applied below to all rows but not to first row of hermite series.       
YCoeffHH(1:6,1:6)=YCoeffHH(1:6,1:6).*sqrt(VarIn/VarHH);
%We convert final 2D Hermite series to 2D Z-series        

[YCoeffZZ] = Convert2DHermitesInto2DSeriesNew(YCoeffHH,Order,Order);

for nn=1:SeriesOrder
    for mm=1:SeriesOrder
        DeltaX(nn,mm)=.00125/(factorial(nn+1))/factorial(mm+1);%/2^((nn-1)/2)/2^((mm-1)/2);
        DeltaXMax(nn,mm)=DeltaX(nn,mm)*10;
    end
end

ObjFunc1=0;
ObjFunc2=0;

%%%Weights on objective function that shows fit to moments
w2D(NMoments,NMoments)=1;
for nn=NMoments-1:-1:1
    for mm=NMoments-1:-1:1
        w2D(nn,mm)=w2D(nn+1,mm+1)*(nn+1).^0*(mm+1).^0;
    end
end

[AMat] = CalculateCrossMomentsofTwo2Dand1DZSeries(YCoeffZZ,XCoeffZ,Order,Order);

for pp1=1:Order+1
     for qq1=1:Order+1
         Moments2D(pp1,qq1)=AMat((pp1-1)*(Order+1)+qq1,1);
         Moments2D0(pp1,qq1)=MomentsYX0((pp1-1)*(Order+1)+qq1,1);
     end
    % Moments1D(pp1)=AMat((Order+1)*(Order+1)+pp1,1);
 end
[ObjFuncBest] = CalculateObjMoment2D1D(Moments2D0,Moments2D,w2D,Order+1,Order+1);
%[ObjFuncBest] = CalculateObjMoment(sMu,Moments,w,mOrder);

%cBest=c;

ImproveFlag(1:SeriesOrder,1:SeriesOrder)=1;
ImproveFlagPrev(1:SeriesOrder,1:SeriesOrder)=0;
ImproveCount(1:SeriesOrder,1:SeriesOrder)=0;
kk=0;
while ((kk.001))
kk=kk+1;    
    %We only iteratively alter c(2:7), first and second moments are
    %retrieved automatically in our set up
    for nn=1:SeriesOrder
        for mm=1:SeriesOrder
            
            ImproveFlagPrev(nn,mm)=ImproveFlag(nn,mm);


            YCoeffHHnew=YCoeffHH;
            YCoeffHHnew(nn,mm)=YCoeffHHnew(nn,mm)+DeltaX(nn,mm);

            %Below, we calculate first and 2nd moment of 2D Hermite series       
            [MeanHH,M2HH] = CalculateMeanAndVarOf2DHSeriesY(YCoeffHHnew,Order,Order);
            %VarHH is model variance .      
            VarHH=M2HH-MeanHH.^2;
            %VarIn is input variance 
            VarIn=YMoments(2)-YMoments(1).^2;
            %Variance correction is applied below to all rows but not to first row of hermite series.       
            YCoeffHHnew(1:6,1:6)=YCoeffHHnew(1:6,1:6).*sqrt(VarIn/VarHH);
            %We convert final 2D Hermite series to 2D Z-series        
        
            [YCoeffZZnew] = Convert2DHermitesInto2DSeriesNew(YCoeffHHnew,Order,Order);
        
        
            [AMat] = CalculateCrossMomentsofTwo2Dand1DZSeries(YCoeffZZnew,XCoeffZ,Order,Order);
            for pp1=1:Order+1
                for qq1=1:Order+1
                    Moments2D(pp1,qq1)=AMat((pp1-1)*(Order+1)+qq1,1);
                    Moments2D0(pp1,qq1)=MomentsYX0((pp1-1)*(Order+1)+qq1,1);
                end
            end
            [ObjFunc1] = CalculateObjMoment2D1D(Moments2D0,Moments2D,w2D,Order+1,Order+1);
        
            if(ObjFunc1DeltaXMax(nn,mm))
           DeltaX(nn,mm)=DeltaXMax(nn,mm);
       end
        end
    end
   
end

ObjFunc=ObjFuncBest;



end
```

.

.

.

```
function [Coeff,Zy] = CalculateHermiteSeriesFromData01(Yin,Order,ZI)

Ndata=length(Yin);

%Hz=HermitePoly(Order);  
MeanYin=sum(Yin(1:Ndata))/Ndata;
Ym(1:Ndata)=Yin(1:Ndata)-MeanYin;
YmVar=sum(Ym(1:Ndata).^2)/Ndata;
Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);



 %[Zn] = StandardNormalIdealDesity02(Ndata,1);
% %[ZI] = CalculateZI(Zn);
% 
% 
% ZI1=Zn;
%Below W is the design matrix for least squares regression i.e the matrix
%that contains all the hermite polynomials calculated at ideal normal
%density grid of size Ndata. 
[W] = EvalHermiteArrayH0(ZI,Order);
%[W1] = EvalHermiteArrayH0(ZI1,Order);

for nn=1:Ndata
    p(nn)=1;%sqrt(normpdf(ZI(nn)));
end


for nn=1:Ndata
    for hh=1:Order+1
W(nn,hh)=W(nn,hh).*p(nn);%sqrt(normpdf(ZI(1,1:Ndata)));
    end
end

%We first sort the data so that we can assign one appropriate Z-grid
%point(and associated hermite polynomials calculated at that grid point)
%to each data element. This ideal normal density Z-grid is
%constructed so that its size is equal to data observations count. We
%suppose that first derivative of random variables with repsect to Z
%does not switch sign meaning that increasing values of data
%observations have to aligned with increasing values of ideal normal
%density grid.
[Ys,I]=sort(Y(1:Ndata));
%In the line below, the data sort is reversed so that now the ideal 
%normal density grid elements assigned to various observations of random 
%variable face it on data observations index. For details, Please look 
%on interent the definition of matlab sort command with role of "I" 
%in output and how it alters the index.   

%%Zs1(I(1:Ndata))=ZI(1:Ndata);

%Below the values to be regressed facing the design matrix are assigned
Ymu(1:Ndata,1)=Ys(1:Ndata).*p(1:Ndata);

%Below, implement least squares regression.
WW=(W'*W);
%WW1=W1'*W1;
%WW(6,6)=120*Ndata;

% for nn=1:6
%     mul(nn+1)=sum(ZI(1:Ndata).^(2*nn))/sum(ZI1(1:Ndata).^(2*nn));
% end
% 
% mul=sqrt(mul)
% 
% mul(3)=1;
% mul(5)=1;

 %W(1:Ndata,2)=mul(2)*ZI(1:Ndata);
 %W(1:Ndata,3)=mul(3).*ZI(1:Ndata).^2-1;
% W(1:Ndata,4)=mul(4).*(ZI(1:Ndata).^3 - 3.*ZI(1:Ndata));
 %W(1:Ndata,5)=mul(5).*ZI(1:Ndata).^4-6.*mul(3).*ZI(1:Ndata).^2+3;
% W(1:Ndata,6)=mul(6).*(ZI(1:Ndata).^5-10.*ZI(1:Ndata).^3+15*ZI(1:Ndata));

% mul
% 
% str=input("Look at

%W(1:Ndata,2)=W(1:Ndata,2)./sqrt(mul(2));
%W(1:Ndata,4)=W(1:Ndata,4)./sqrt(mul(4));
%W(1:Ndata,6)=W(1:Ndata,6)./sqrt(mul(6));


coeff=(WW)$W'*Ymu);

%WW1
WW
%inv(WW1)
%inv(WW)

str=input("Look at variances of hermite polynomials inside function")



%Store in coefficietns array of all random varaibles
Coeff(1:Order+1)= coeff(1:Order+1,1);
%Store the associated Z in Z-array of all coefficients.   
Zy(I(1:Ndata))=W(1:Ndata,2);



Coeff(1:Order+1)=Coeff(1:Order+1).*sqrt(YmVar);
Coeff(1)=Coeff(1)+MeanYin;

end




```

.

.

.

```
function [c0,c] = CalculateZSeriesDensityFromRawMomentsM6(rMu,bGuess)

    mOrder=6;
    [Mu1,cMu] = ConvertRawMomentsToCentralMoments(rMu,mOrder);

    sMu(1)=0;
    sMu(2)=1;
    sMu(3)=cMu(3)/cMu(2).^1.5;
    sMu(4)=cMu(4)/cMu(2).^2.0;
    sMu(5)=cMu(5)/cMu(2).^2.5;
    sMu(6)=cMu(6)/cMu(2).^3.0;
    %sMu(7)=cMu(7)/cMu(2).^3.5;
    %sMu(8)=cMu(8)/cMu(2).^4.0;
    

    w(mOrder)=1;
for nn=mOrder-1:-1:1
w(nn)=w(nn+1).*(nn+1)*(nn);    
end
%w(2)=w(2)*1024;
%w(8)=w(8)*2;
%w(10)=w(10)*sqrt(2);

    
    iter=2000;
    %bGuess(1:5)=0;
    %bGuess(1)=1;
    [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNewC5(sMu,bGuess,iter);
    

    
    SeriesOrder=5;
    NMoments=6;    
    
    [F,dF] = CalculateMomentsAndDerivatives_0(sMu,c0,c,SeriesOrder,SeriesOrder,NMoments);

da(1,1)=c0;
da(2:SeriesOrder+1,1)=c(1:SeriesOrder);

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);
Moments
sMu
%str=input('Look at comparison of moments');
%Replace with your own more intelligent objective function if you like.
%ObjBest=100000*(abs(sMu(1)-Moments(1)))+abs(sMu(2)-Moments(2))+abs((sMu(3)-Moments(3))^(1/1.5))+abs((sMu(4)-Moments(4))^(1/2.0)) + ...
%    abs((sMu(5)-Moments(5))^(1/2.0))+abs((sMu(6)-Moments(6))^(1/2.0));
[ObjBest] = CalculateObjMoment(sMu,Moments,w,mOrder)


b0Best=c0;
bBest(1:SeriesOrder)=c(1:SeriesOrder);

nn=0;
while((nn.000000000001) || (abs(F(2,1))>.000000000001) || (abs(F(3,1))>.000000000001) || (abs(F(4,1))>.00000000001)|| (abs(F(5,1))>.00000000001)|| (abs(F(6,1))>.00000000001)  ))

    nn=nn+1;
    %Below Newton matrix equation to improve the Z-series coefficients guess at previous step.
    if(nnObjNew) &&( IsValidFlag))
      
       ObjBest=ObjNew;
       b0Best=b0;
       bBest(1:SeriesOrder)=b(1:SeriesOrder);
    end

    da(1,1)=b0;
    da(2:SeriesOrder+1,1)=b(1:SeriesOrder);

end
c0=b0Best;%Best;
c(1:SeriesOrder)=bBest;%Best(1:SeriesOrder);
[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);
    
b0Best
bBest
Moments
sMu
cMu(2)
%str=input('Look at fit of density----0000 ')
    c0=c0*sqrt(cMu(2));
    c=c*sqrt(cMu(2));
    
    c0=c0+Mu1;


end


```

.

.

.

```
function [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNewC5(cmu,cin,iter)


%Mul=1.0;
SeriesOrder=5;
NMoments=6;

 EZ(1)=0;
 EZ(2)=1;
 for nn=3:NMoments*SeriesOrder+SeriesOrder+2
     if rem(nn,2)==1
         EZ(nn)=0;
     else
         EZ(nn)=EZ(nn-2)*(nn-1);
         EZ(nn);
     end
 end


c0=-(cin(2)+3*cin(4));  %This is for zero mean condition.
c=cin;
MaxIter=100;

for nn=1:iter     %increase the iterations over coefficients if neeeded


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[M3,dc2] = CalculateParticularMomentAndDerivativeOfItsCoeff(c0,c,SeriesOrder,3,EZ);

tolerance=.0000001*cmu(3);
mm=0;
while ((abs(M3-cmu(3)) >tolerance ) && (mmtolerance ) && (mmtolerance ) && (mmtolerance ) && (mm<MaxIter))
mm=mm+1;

c(5)=c(5)-(M6-cmu(6))/dc5;
[M6,dc5] = CalculateParticularMomentAndDerivativeOfItsCoeff(c0,c,SeriesOrder,6,EZ);

end

[SecondMoment] = CalculateSecondMomentC5(c0,c);

c=c/sqrt(SecondMoment);
c0=c0/sqrt(SecondMoment);


[c0,c] = IterateSmoothingGuessOverPreviousMomentsC5(cmu,c,6,2,EZ);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end


end


```

.

.

.

```
function [EnMoment,dEnMomentdCoeff] = CalculateParticularMomentAndDerivativeOfItsCoeff(a0,a,SeriesOrder,nMoment,EZ)


% if(SeriesOrder>=8)
% a0=-(a(2)+3*a(4)+15*a(6)+105*a(8));% ---1
% end
% if(SeriesOrder<8)
% a0=-(a(2)+3*a(4)+15*a(6));% ---1
% end
% 
% EZ(1)=0;
% EZ(2)=1;
% for nn=3:NMoments*SeriesOrder+NZterms+2
%     if rem(nn,2)==1
%         EZ(nn)=0;
%     else
%         EZ(nn)=EZ(nn-2)*(nn-1);
%         EZ(nn);
%     end
% end
% EZ;

%EXZ(1,1)=1;
%for pp1=1:NZterms
%        EXZ(1,pp1+1)=EZ(pp1);
%end


a(SeriesOrder+1:nMoment*SeriesOrder+1+SeriesOrder)=0;
b0=a0;
b=a;

for mm=2:nMoment
    
    [b0,b] =SeriesProduct(a0,a,b0,b,SeriesOrder*mm+SeriesOrder+1);
     b(SeriesOrder*mm+1:nMoment*SeriesOrder+SeriesOrder+1)=0;
     if(mm==nMoment-1)
         dEnMomentdCoeff=b0.*EZ(nMoment-1);
         for pp2=1:SeriesOrder*nMoment-1
            
            dEnMomentdCoeff=dEnMomentdCoeff+b(pp2).*EZ(pp2+nMoment-1);
        end
        dEnMomentdCoeff=dEnMomentdCoeff*nMoment; 
     end
     if(mm==nMoment)
        EnMoment=b0;
        for pp2=1:SeriesOrder*nMoment
            EnMoment=EnMoment+b(pp2).*EZ(pp2);
    
        end
     end
end   

    

end


```

.

.

.

```
function [mu1,cMu] = ConvertRawMomentsToCentralMoments(Mu,mOrder)

%cu
%mu
% %mOrder
%str=input('Look at numbers');
mu1=Mu(1);
for mm=2:mOrder
    cMu(mm)=0;
    for jj=0:mm
        if(jj==0)
            cMu(mm)=cMu(mm)+ (-1)^(mm-jj).*factorial(mm)/factorial(jj)/factorial(mm-jj)*1*mu1.^(mm-jj);
            
        else
            cMu(mm)=cMu(mm)+ (-1)^(mm-jj).*factorial(mm)/factorial(jj)/factorial(mm-jj)*Mu(jj)*mu1.^(mm-jj);
            
        end
    end
end


```

.

.

.

```
function [F,dF] = CalculateMomentsAndDerivatives_0(Ms,a0,a,SeriesOrder,NZterms,NMoments)
%[F,dF] = CalculateCumulantsAndDerivativesFromMoments(C,a0,a,SeriesOrder,SeriesOrder,NoOfCumulants);

%a(1)=a1;
%a(2)=a2;
%a(3)=a3;
%a(4)=a4;
%a(5)=a5;
%a(6)=a6;
%a(7)=a7;



%aa0=a0;
if(NMoments>8)
a0=-(a(2)+3*a(4)+15*a(6)+105*a(8));% ---1
end
if((NMoments==7)||(NMoments==8))
a0=-(a(2)+3*a(4)+15*a(6));% ---1
end
% if(NMoments==6)
% a0=-(a(2)+3*a(4));% ---1
% end



if((NMoments==6)||(NMoments==7))
a0=-(a(2)+3*a(4));% ---1
end

if((NMoments==3)||(NMoments==4))
a0=-(a(2));% ---1
end

EZ(1)=0;
EZ(2)=1;
for nn=3:NMoments*SeriesOrder+NZterms+2
    if rem(nn,2)==1
        EZ(nn)=0;
    else
        EZ(nn)=EZ(nn-2)*(nn-1);
        EZ(nn);
    end
end
EZ;

EXZ(1,1)=1;
for pp1=1:NZterms
        EXZ(1,pp1+1)=EZ(pp1);
end


a(SeriesOrder+1:NMoments*SeriesOrder+1)=0;
b0=a0;
b=a;

for mm=1:NMoments
    if(mm>1)
        [b0,b] =SeriesProduct(a0,a,b0,b,SeriesOrder*mm);
        b(SeriesOrder*mm+1:NMoments*SeriesOrder+1)=0;
    end
   % b0
   % b
%str=input('Look at numbers')    
    EXZ(mm+1,1)=b0;
    for pp2=1:SeriesOrder*mm
        
            EXZ(mm+1,1)=EXZ(mm+1,1)+b(pp2).*EZ(pp2);
    end
    for pp1=1:NZterms
        EXZ(mm+1,pp1+1)=b0.*EZ(pp1);
        for pp2=1:SeriesOrder*mm
        
            EXZ(mm+1,pp1+1)=EXZ(mm+1,pp1+1)+b(pp2).*EZ(pp2+pp1);
        end
    end
end

%u1=EXZ(2,1);
u2=EXZ(3,1);

if(NMoments>=3)
u3=EXZ(4,1);
end

%NMoments
if(NMoments>=4)
u4=EXZ(5,1);
end


u1=a0+a(2);
if(SeriesOrder>=4)
u1=a0+a(2)+3*a(4);
end
if(SeriesOrder>=6)
u1=u1+15*a(6);
end
if(SeriesOrder>=8)
u1=u1+105*a(8);
end


%k2=u2-u1^2;
%k3=u3-3*u2*u1+2*u1^3;
%k4=u4-4*u3*u1-3*u2^2+12*u2*u1^2-6*u1^4;


du1(1)=1;%----2
% du1(2)=0;%----2
% du1(3)=1;%----2
% du1(4)=0;%----2
% du1(5)=1;%----2
% du1(6)=0;%----2
% du1(7)=15;%----2
% du1(8)=0;%----2
% du1(9)=105;%----2
% du1(10)=0;%----2
 du2(1)=2*EXZ(2,1);
 
 
 
 
 if(NMoments>=3)
 
 du3(1)=3*EXZ(3,1);
 
 end
 
 if(NMoments>=4)
 du4(1)=4*EXZ(4,1);
 end

%du1(1)=1;%----2
%du2(1)=0;
%du3(1)=0;
%du4(1)=0;

for mm=2:SeriesOrder+1
du1(mm)=EXZ(1,mm);
du2(mm)=2*EXZ(2,mm);
if(NMoments>=3)

du3(mm)=3*EXZ(3,mm);
end
if(NMoments>=4)

du4(mm)=4*EXZ(4,mm);
end
end


if(NMoments>=5)
u5=EXZ(6,1);


%du5(1)=5*EXZ(5,1);

for mm=1:SeriesOrder+1
du5(mm)=5*EXZ(5,mm);
end

end

if(NMoments>=6)
u6=EXZ(7,1);
%du6(1)=0;

for mm=1:SeriesOrder+1
du6(mm)=6*EXZ(6,mm);
end

end


if(NMoments>=7)
u7=EXZ(8,1);
%str=input('Look at k7 and k71')

%du7(1)=0;

for mm=1:SeriesOrder+1
du7(mm)=7*EXZ(7,mm);
end

end
if(NMoments>=8)

u8=EXZ(9,1);
for mm=1:SeriesOrder+1
du8(mm)=8*EXZ(8,mm);
end

end

if(NMoments>=9)

u9=EXZ(10,1);
for mm=1:SeriesOrder+1
du9(mm)=9*EXZ(9,mm);
end

end
if(NMoments>=10)

u10=EXZ(11,1);
for mm=1:SeriesOrder+1
du10(mm)=10*EXZ(10,mm);
end

end




 F(1,1)=u1-Ms(1);
 F(2,1)=u2-Ms(2);
 F(3,1)=u3-Ms(3);
 if(NMoments>=4)
 F(4,1)=u4-Ms(4);
 end
 if(NMoments>=5)
 F(5,1)=u5-Ms(5);
 end
 if(NMoments>=6)
 F(6,1)=u6-Ms(6);
 end
 if(NMoments>=7)
 F(7,1)=u7-Ms(7);
 end
 if(NMoments>=8)
 F(8,1)=u8-Ms(8);
 end
 if(NMoments>=9)
 F(9,1)=u9-Ms(9);
 end
 if(NMoments>=10)
 F(10,1)=u10-Ms(10);
 end
 
 
      for mm=1:SeriesOrder+1
        dF(1,mm)=du1(mm);
        dF(2,mm)=du2(mm);
        dF(3,mm)=du3(mm);
        
        if(NMoments>=4)
        dF(4,mm)=du4(mm);
        end
        
        if(NMoments>=5)
            dF(5,mm)=du5(mm);
        end
        
        if(NMoments>=6)
        dF(6,mm)=du6(mm);
        end
        if(NMoments>=7)
        dF(7,mm)=du7(mm);
        end
        if(NMoments>=8)
        dF(8,mm)=du8(mm);
        end
        if(NMoments>=9)
        dF(9,mm)=du9(mm);
        end
        if(NMoments>=10)
        dF(10,mm)=du10(mm);
        end
        
      end
 


end


```

.

.

.

```
function [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNewC5(cmu,cin,iter)


%Mul=1.0;
SeriesOrder=5;
NMoments=6;

 EZ(1)=0;
 EZ(2)=1;
 for nn=3:NMoments*SeriesOrder+SeriesOrder+2
     if rem(nn,2)==1
         EZ(nn)=0;
     else
         EZ(nn)=EZ(nn-2)*(nn-1);
         EZ(nn);
     end
 end


c0=-(cin(2)+3*cin(4));  %This is for zero mean condition.
c=cin;
MaxIter=100;

for nn=1:iter     %increase the iterations over coefficients if neeeded


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[M3,dc2] = CalculateParticularMomentAndDerivativeOfItsCoeff(c0,c,SeriesOrder,3,EZ);

tolerance=.0000001*cmu(3);
mm=0;
while ((abs(M3-cmu(3)) >tolerance ) && (mmtolerance ) && (mmtolerance ) && (mmtolerance ) && (mm<MaxIter))
mm=mm+1;

c(5)=c(5)-(M6-cmu(6))/dc5;
[M6,dc5] = CalculateParticularMomentAndDerivativeOfItsCoeff(c0,c,SeriesOrder,6,EZ);

end

[SecondMoment] = CalculateSecondMomentC5(c0,c);

c=c/sqrt(SecondMoment);
c0=c0/sqrt(SecondMoment);


[c0,c] = IterateSmoothingGuessOverPreviousMomentsC5(cmu,c,6,2,EZ);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end


end


```

.

.

.

```
function [Moments] = CalculateMomentsOfZSeries(a0,a,SeriesOrder,NMoments)


%aa0=a0;
%a0=0;% ---1

EZ(1)=0;
EZ(2)=1;
%LogEZ(2)=0;
for nn=3:NMoments*SeriesOrder
    if rem(nn,2)==1
        EZ(nn)=0;
    else
        EZ(nn)=EZ(nn-2)*(nn-1);
        %LogEZ(nn)=log(EZ(nn-2))+log(nn-1);
        %EZ(nn);
    end
end
%EZ
%EZ(1:30)
%str=input('Look at numbers')
a(SeriesOrder+1:SeriesOrder*NMoments+1)=0;
b0=a0;
b=a;


for mm=1:NMoments
    if(mm>1)
        %[b0,b] =SeriesProductLogarithmic(a0,a,b0,b,SeriesOrder*mm);
        
        [b0,b] =SeriesProduct(a0,a,b0,b,SeriesOrder*mm);
        
        %b0-bb0
        
        %b-bb
        
        %str=input('Look at two products')
        
        
        b(SeriesOrder*mm+1:SeriesOrder*NMoments+1)=0;
    end
   % Logb=log(abs(b));
   % Signb=sign(b);
    EXZ(mm,1)=b0;
    for pp2=1:SeriesOrder*mm
        if rem(pp2,2)==0
            %EXZ(mm,1)=EXZ(mm,1)+exp(Logb(pp2)+LogEZ(pp2)).*Signb(pp2);
            EXZ(mm,1)=EXZ(mm,1)+b(pp2).*EZ(pp2);
 %           b(pp2).*EZ(pp2)
 %           exp(Logb(pp2)+LogEZ(pp2)).*Signb(pp2)
 %           mm
 %           pp2
            %str=input('Look at moment values')
        end
    end
end

    
for nn=1:NMoments
    Moments(nn)=EXZ(nn,1);
end



end


```

.

.

.

```
function [SecondMoment] = CalculateSecondMomentC5(a0,a)


SecondMoment=a0^2+a(1)^2 +2* a0* a(2) +3*(a(2).^2+2* a(1).* a(3) +2* a0* a(4))+ ...
    15*(a(3).^2 +2 *a(2).* a(4) +2 *a(1).* a(5))+105*(a(4).^2 +2* a(3).* a(5) )+ ...
    945*(a(5).^2 );
%a0^2+a1^2+2 a0 a2+3 (a2^2+2 a1 a3+2 a0 a4)+945 a5^2+15 (a3^2+2 a2 a4+2 a1 a5)+105 (a4^2+2 a3 a5)
end


```

.

.

.

```
function [Z]=CalculateZgivenXAndZSeriesBisection2C5Improved(Y,c0,c)

%[Z]=CalculateZgivenXAndZSeriesBisection2C5(Y,c0,c);

%This program takes a value of Y as input and returns the corresponding 
%value of Z given the parameters of the Z-series.
%It first see if the value of Y is greater than median or smaller than
%median. If the value of Y is greater than median Z has to be greater than
%zero and if the value of Y is smaller than median Z has to be negative.
% Once we know whether Z is greater than Z or smaller than Zero, we divide
% the program into two repeated if loops, one for Z greater than zero and 
%one for Z smaller than zero. 
%If Z is positive, we have to assign it a valid band of upper and
%lower values between which it can be found. 
%This is done sequentially by calculating Y(.5) at Z=.5, if Y is smaller 
%than Y(.5), we know that true value of Y will lie between 0 and .5
%so we assign a lower band value Za=0 and upper band value Zb=.5
%If however Y is greater than Y(.5), we know that true Z should be larger 
%than .5 and we again evaluate Y(1) at Z=1, If Y is smaller than Y(1), 
%we know that true value of Z should be between .5 and 1, and we assign a 
%lower band value Za=.5 and upper band value of Zb=1. Through repeated 
%elseif we continue until we find an appropriate band value of Z.

%Once we have determined the upper band value of Zb and lower band value of
%Za, We find Zmid=(Za+Zb)/2. We then evaluate Y(Zmid) and if Y  Y(Zmid), we assign the lower band value equal to Zmid as Za=Zmid. In a
% few iterations, this bisection procedure gets extremely close to true
% value of Z for which Y(Z)=Y


Z=0;



% [coeff0,coeff]=ConvertZCoeffsToHCoeffs(c0,c,5);
% Coeff(1)=coeff0;
% Coeff(2:6)=coeff(1:5);
% Order=5;
% Hz=HermitePoly(5);
% 
% for Z0=-5:.5:5
% 
% [Xh,dXh] = EvalHermiteSeriesH0(Coeff,Z0,Order,Hz);
% 
% 
% EvaluateZSeriesC5(c0,c,Z0)
% Xh
% EvaluateZSeriesdXdZC5(c0,c,Z0)
% c(1)+2*c(2)*Z0+3*c(3)*Z0.^2+4*c(4)*Z0.^3+5*c(5)*Z0.^4
% dXh
% 
% str=input("look at coeffs---bisection inside")
% 
% end
% 

if(Y>c0)
    %Z=.5;
    if((Y  EvaluateZSeriesC5(c0,c,Zmid))
            Za=Zmid;
        end
    Z=.5*Za+.5*Zb; %This can be taken out of the loop and does not 
    %necessarily have to be calculated again and again. Has to be
    %calculated at least once after the loop to determine the true value of
    %Z.
    
    end
    
end
        
if(Y  EvaluateZSeriesC5(c0,c,-.5))|| (EvaluateZSeriesdXdZC5(c0,c,-.5)  EvaluateZSeriesC5(c0,c,-1))|| (EvaluateZSeriesdXdZC5(c0,c,-1)  EvaluateZSeriesC5(c0,c,-1.5))|| (EvaluateZSeriesdXdZC5(c0,c,-1.5)  EvaluateZSeriesC5(c0,c,-2))|| (EvaluateZSeriesdXdZC5(c0,c,-2)  EvaluateZSeriesC5(c0,c,-2.5))|| (EvaluateZSeriesdXdZC5(c0,c,-2.5)  EvaluateZSeriesC5(c0,c,-3))|| (EvaluateZSeriesdXdZC5(c0,c,-3.0)  EvaluateZSeriesC5(c0,c,-3.5))|| (EvaluateZSeriesdXdZC5(c0,c,-3.5)  EvaluateZSeriesC5(c0,c,-4))|| (EvaluateZSeriesdXdZC5(c0,c,-4)  EvaluateZSeriesC5(c0,c,-4.5))|| (EvaluateZSeriesdXdZC5(c0,c,-4.5)  EvaluateZSeriesC5(c0,c,-5))|| (EvaluateZSeriesdXdZC5(c0,c,-5)  EvaluateZSeriesC5(c0,c,-5.5))|| (EvaluateZSeriesdXdZC5(c0,c,-5.5)  EvaluateZSeriesC5(c0,c,-6.0))|| (EvaluateZSeriesdXdZC5(c0,c,-6) EvaluateZSeriesC5(c0,c,Zmid))
%             Za=Zmid;
%         end
        if((Y> EvaluateZSeriesC5(c0,c,Zmid))|| (EvaluateZSeriesdXdZC5(c0,c,Zmid)<0))
            Za=Zmid;
        elseif(Y< EvaluateZSeriesC5(c0,c,Zmid))
            Zb=Zmid;
        end
    Z=.5*Za+.5*Zb; %This can be taken out of the loop and does not 
    %necessarily have to be calculated again and again. Has to be
    %calculated at least once after the loop to determine the true value of
    %Z
    end
    
end        
        
end


```

.

.

.

```
function [c] = ConvertHermiteSeriesToZSeries01(ch,Order)

c(1:Order+1)=0;
[Hz] = HermitePoly(Order);
for nn=1:Order+1
    for mm=1:Order+1
        c(mm)=c(mm)+ch(nn).*Hz(nn,mm);
    end
end

end


```

.

.

.

```
function [cH] = ConvertZSeriesToHermiteSeriesNew(c,Order)
%Order is order of highest hermite.
b(1:Order+1)=c(1:Order+1);
[Hz] = HermitePoly(Order);
if(b(Order+1)~= 0)
    for nn=Order+1:-1:1
        cH(nn)=b(nn);
        if((nn-1)>0)
            b(1:nn-1)=b(1:nn-1)-cH(nn).*Hz(nn,1:nn-1);
        end
    end
    bH0=cH(1);
    bH(1:Order)=cH(2:Order+1);
end



end


```

.

.

.

```
function [CorrH] = CalculateCorrelationBivariateHermiteCH0(Z1,Z2,paths,HH)

CorrH(1:HH)=0;
CovH(1:HH)=0;
Var1H(1:HH)=0;
Var2H(1:HH)=0;

[X1h] = EvalHermiteArrayH0(Z1,HH);
[X2h] = EvalHermiteArrayH0(Z2,HH);

for hh=1:HH
    CovH(hh)=CovH(hh)+sum(X1h(:,hh+1).*X2h(:,hh+1))/paths;
    Var1H(hh)=Var1H(hh)+sum(X1h(:,hh+1).*X1h(:,hh+1))/paths;
    Var2H(hh)=Var2H(hh)+sum(X2h(:,hh+1).*X2h(:,hh+1))/paths;
    CorrH(hh)=CovH(hh)./sqrt(Var1H(hh))./sqrt(Var2H(hh));
end

% Var1H
% Var2H
% 
% str=input("Look at variances of data hermites");

end


```

.

.

.

```
function [YCoeffHHOut,ObjFunc] = HSeriesCoeffsFromDataIterative2D1st(YObs,Zx,Zy,MaxIter,Order,Ndata)


str=input("Hi--I am here again--02");


%This program computes coeffs of 2D Hermite-series when values of raw cross-moments are
%given using Iterative method. 

%MomentsYX0 are raw cross-moments stacked in a single array;
%YCoeffHH are coeffs of 2D Hermite-series to be found and when passed as parameters
%contain starting guess for 2D Hermite-series coeffs.

%Total number of Iterations of the iterative method are given by input 
%parameter MaxIter.
%The present program is written for SeriesOrder=6*6.
%  SeriesOrder=6;  %Z-series till 7th power.
%  
%  NMoments=6;
%  Order=5;
 
 SeriesOrder=Order+1;  %Z-series till 7th power.
 
 NMoments=Order+1;
 
 YMean=sum(YObs)/Ndata;

[Hx] = EvalHermiteArrayH0(Zx,Order);
[Hy] = EvalHermiteArrayH0(Zy,Order);

 for nn=1:Order+1
    for mm=1:Order+1
        Hxy(1:Ndata,(nn-1)*(Order+1)+mm)=Hx(1:Ndata,mm).*Hy(1:Ndata,nn);
        YCoeffHH((nn-1)*(Order+1)+mm,1)=0.000;
    end
end
YCoeffHH(1,1)=YMean;
YModel=Hxy*YCoeffHH;

ObjFuncBest=sum((YObs-YModel).^2+(YObs.^2-YModel.^2).^2) 

str=input("Look at ObjBest");
ObjFuncBestBefore=ObjFuncBest; 
 
%%%%%%Choose the iteration step size.
for nn=1:SeriesOrder
    for mm=1:SeriesOrder
        DeltaX(nn,mm)=.00125/16/(factorial(nn)).^2/factorial(mm).^2;%/2^((nn-1)/2)/2^((mm-1)/2);
        DeltaXMax(nn,mm)=DeltaX(nn,mm)*5;
        
        %DeltaX(nn,mm)=.00125/2/(factorial(nn)).^1.0/factorial(mm).^2.0;
        %DeltaXMax(nn,mm)=DeltaX(nn,mm)*5;
    end
end




% [ObjFuncBest] = CalculateObjMoment2D1D(Moments2D0,Moments2D,w2D,Order+1,Order+1);
% 
% ObjFuncBestBefore
% ObjFuncBest
% ObjFuncBestBefore-ObjFuncBest
% str=input("Look at difference of indicators");

ImproveFlag(1:SeriesOrder,1:SeriesOrder)=1;
ImproveFlagPrev(1:SeriesOrder,1:SeriesOrder)=0;
%ImproveCount(1:SeriesOrder,1:SeriesOrder)=0;
kk=0;
StopCount=0;
while ((kk1)&&(StopCount0)&&(DValue2>0)&&(DValue3>0)&&(DValue4>0)&&(DValue5>0)&&(DValue6>0);
%                 [DValue1] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-3.0,Order);
%                 [DValue2] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,3.0,Order);
%                 [DValue3] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-2.5,Order);
%                 [DValue4] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,2.5,Order);
%                 [DValue5] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-2.0,Order);
%                 [DValue6] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,2.0,Order);
%                 
%                 DFlag2=(DValue1>0)&&(DValue2>0)&&(DValue3>0)&&(DValue4>0)&&(DValue5>0)&&(DValue6>0);
 DFlag1=1;
 DFlag2=1;
            if(rem(kk,1000)==0)
     for nn=1:SeriesOrder
    for mm=1:SeriesOrder
        DeltaX(nn,mm)=.00125/16/(factorial(nn)).^2/factorial(mm).^2;%/2^((nn-1)/2)/2^((mm-1)/2);
        DeltaXMax(nn,mm)=DeltaX(nn,mm)*5;
        
        %DeltaX(nn,mm)=.00125/2/(factorial(nn)).^1.0/factorial(mm).^2.0;
        %DeltaXMax(nn,mm)=DeltaX(nn,mm)*5;
    end
end

            end
       %     str=input("Look at DValues");
            if((ObjFunc10)&&(DValue2>0)&&(DValue3>0)&&(DValue4>0)&&(DValue5>0)&&(DValue6>0);
%                 [DValue1] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-3.0,Order);
%                 [DValue2] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,3.0,Order);
%                 [DValue3] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-2.5,Order);
%                 [DValue4] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,2.5,Order);
%                 [DValue5] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,-2.0,Order);
%                 [DValue6] = EvaluateDerivativeOf2DZSeries(YCoeffZZnew,3.0,2.0,Order);
%                 
%                 DFlag2=(DValue1>0)&&(DValue2>0)&&(DValue3>0)&&(DValue4>0)&&(DValue5>0)&&(DValue6>0);
 %DValue1=1;
 %DValue2=1;
 
 DFlag1=1;
 DFlag2=1;
                if((ObjFunc2DeltaXMax(nn,mm))
           DeltaX(nn,mm)=DeltaXMax(nn,mm);
       end
        end
    end

   
end

ObjFunc=ObjFuncBest;

for nn=1:Order+1
    for mm=1:Order+1
        YCoeffHHOut(nn,mm)=YCoeffHH((nn-1)*(Order+1)+mm,1);
        %bnmHH((nn-1)*(Order+1)+mm,1)=0.0;
    end
end

end
```

.

.

.
```

---

