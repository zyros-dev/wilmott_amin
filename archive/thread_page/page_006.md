# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 6 of 59** — Posts #251–#300

[← Previous](page_005.md) | [Index](index.md) | [Next →](page_007.md)

---

### #251 — outrun
*January 4, 2017, 10:18 AM*

Fast multipole is used to simulate graviational (or other forces) of large number of bodies on supercomputers, like
galaxies with millions of bodies.

e.g. from this: [http://web.ipac.caltech.edu/staff/fmasc ... Us2011.pdf](http://web.ipac.caltech.edu/staff/fmasci/home/astro_refs/NbodySimsGPUs2011.pdf)
>
> *Gordon Bell prize record*
>
> N-body simulations have persistently been at
>
> the forefront of high-performance computing in
>
> terms of the flop/s that they deliver. Groundbreaking
>
> N-body simulations have won the coveted
>
> Gordon Bell prize of computing fourteen
>
> times from 1992 to 20106;8–20. Some may argue
>
> that it is not the achieved flop/s that counts,
>
> but the science that they deliver. This is a valid
>
> assertion, in the same sense that reaching exaflop/s
>
> in itself should not be the purpose of
>
> high-performance computing. The maximum
>
> flop/s for N-body simulations is obtained with
>
> the embarrassingly parallel O(N2
>
> ) all-pairs summation,
>
> whereas the maximum amount of science
>
> will often be delivered by a fast algorithm.
>
> Many of the award-winning N-body simulations
>
> mentioned above used hierarchical N-body algorithms,
>
> and not the all-pairs summation. We discuss
>
> these fast N-body algorithms in what follows.

---

### #252 — outrun
*January 4, 2017, 10:26 AM*

but don't get distracted, it has been asked many times: please try to come up with *something* that motivates your claim
of "breakthrough". I think you don't have a breakthrough at all, but please convince us!

---

### #253 — ppauper
*January 4, 2017, 10:36 AM*

> I am not an expert at n-body problem but I try to sometimes read and understand what is going on about interesting
applications of mathematics in other areas. I seriously regret having wasted half my life working with mathematical
finance. I think outrun is not a great expert either at n-body problem. As I read about fast multipole method, it is
used to lump together sources that are close together and treat them as a single entity. I would suppose you would still
have to solve a large number of differential equations after employing the fast multipole method.
indeed

I suspect one point here is that the maestro's method can be used for a broad range of problems, and that is one of its
strengths.

Inevitably, for some of those problems, a "specialist" method will be faster numerically for that specific problem, but
in a way, that's missing the point.

When you are faced with a new problem, rather than spending days or weeks figuring out which method to use and then
spending weeks learning that method, Amin's method can be used straight away

---

### #254 — outrun
*January 4, 2017, 11:48 AM*

Yes, don't get distracted by n-body. Get a Shaum's ODE textbook to get up to speed with the basics without wasting too
much time and then adjust your "sales" strategy using newly acquired reference knowledge.

---

### #255 — Amin (Topic Author)
*January 4, 2017, 12:02 PM*

> Yes, don't get distracted by n-body. Get a Shaum's ODE textbook to get up to speed with the basics without wasting too
much time and then adjust your "sales" strategy using newly acquired reference knowledge.
You deleted all your posts in my persecution thread in off topic. Cannot stand up to what you had written?

---

### #256 — ppauper
*January 4, 2017, 12:17 PM*

> Get a Shaum's ODE textbook
you got the name wrong

that would be "Schaum's"

you should read it yourself, although to be honest, the only thing that series has going for it is the price

---

### #257 — outrun
*January 4, 2017, 1:03 PM*

> Yes, don't get distracted by n-body. Get a Shaum's ODE textbook to get up to speed with the basics without wasting too
much time and then adjust your "sales" strategy using newly acquired reference knowledge.
You deleted all your posts in my persecution thread in off topic. Cannot stand up to what you had written?
No, I didn't delete it. My posts weren't transferred to the new forum. Do you want to discuss something? I'm always
happy to express my honest, stable in time, opinion.

---

### #258 — outrun
*January 4, 2017, 1:04 PM*

> Get a Shaum's ODE textbook
you got the name wrong

that would be "Schaum's"

you should read it yourself, although to be honest, the only thing that series has going for it is the price
Why should I read it myself? What made you say that, ..because of the typo?

---

### #259 — Amin (Topic Author)
*January 4, 2017, 1:50 PM*

> Yes, don't get distracted by n-body. Get a Shaum's ODE textbook to get up to speed with the basics without wasting too
much time and then adjust your "sales" strategy using newly acquired reference knowledge.
You deleted all your posts in my persecution thread in off topic. Cannot stand up to what you had written?
No, I didn't delete it. My posts weren't transferred to the new forum. Do you want to discuss something? I'm always
happy to express my honest, stable in time, opinion.
All our posts got transferred. Everybody else's posts got transferred. It was text. What is so special?

---

### #260 — outrun
*January 4, 2017, 2:09 PM*

>
> You deleted all your posts in my persecution thread in off topic. Cannot stand up to what you had written?
No, I didn't delete it. My posts weren't transferred to the new forum. Do you want to discuss something? I'm always
happy to express my honest, stable in time, opinion.
All our posts got transferred. Everybody else's posts got transferred. It was text. What is so special?
What was special was that I had an outrun account and test posts on the new forum during the time it was being
build/deployed/tested and prepared for launch. That account  caused a conflict and relational integrity issues during
the conversion of all the posts, the database can't handle two outruns.

---

### #261 — Cuchulainn
*January 4, 2017, 2:23 PM*

> Get a Shaum's ODE textbook
you got the name wrong

that would be "Schaum's"

you should read it yourself, although to be honest, the only thing that series has going for it is the price
The older 60s Cold War editions are very good (see e.g. Theoretical Mechanics, Numerical Analysis(!) and Real Variable).

Is Coddington ODE not a must?

---

### #262 — list1
*January 4, 2017, 2:50 PM*

Coddington is an advance ODE good written handbook not probably for 1st time reading.

As one who a long time worked in math area I should remark that Amin's work does not look mathematically professional.
!st you need formulate conditions and specify class equations you are going to work. Of course, you can use an equation
to illustrate idea in case when equation has a close form solution. But reduce the problem to such illustration does not
have a sense.

2. You need to prove that chosen class of equations given your conditions has a unique solution.

3. You present iterative process which one expects should converge to unique solution. You should  prove that and define
area where your iterative process converges .

---

### #263 — Cuchulainn
*January 4, 2017, 4:35 PM*

> Coddington is an advance ODE good written handbook not probably for 1st time reading.
>
> As one who a long time worked in math area I should remark that Amin's work does not look mathematically professional.
!st you need formulate conditions and specify class equations you are going to work. Of course, you can use an equation
to illustrate idea in case when equation has a close form solution. But reduce the problem to such illustration does not
have a sense.
>
> 2. You need to prove that chosen class of equations given your conditions has a unique solution.
>
> 3. You present iterative process which one expects should converge to unique solution. You should  prove that and
define area where your iterative process converges .
You are 100% correct; it has been stated a few times here already. But to get to that stage take years of
pencil-and-paper mathematical analysis. Not sure if OP wants to go down that road at this stage.

---

### #264 — Amin (Topic Author)
*January 4, 2017, 5:25 PM*

> Coddington is an advance ODE good written handbook not probably for 1st time reading.
>
> As one who a long time worked in math area I should remark that Amin's work does not look mathematically professional.
!st you need formulate conditions and specify class equations you are going to work. Of course, you can use an equation
to illustrate idea in case when equation has a close form solution. But reduce the problem to such illustration does not
have a sense.
>
> 2. You need to prove that chosen class of equations given your conditions has a unique solution.
>
> 3. You present iterative process which one expects should converge to unique solution. You should  prove that and
define area where your iterative process converges .
My method is based on mathematical common sense. When most of the work on finding solutions to ordinary differential
equations was done in past few centuries, many mathematicians were motivated by the desire to solve  a certain problem
and they were not obsessed so much with class equations and exact formal proofs. I am sure many of those things help but
formal proofs and regularity conditions can be given by any mathematician who has been trained for long years in that
approach and has understood the method which is again based totally on mathematical common sense. There is no deal to
the understanding of the basic idea. Many of these things are totally trivial to understand once they have been
presented and you have understood it but only difficult to do in advance when nobody has done it. All the mathematicians
and scientists added  a little bit to science and it all added up to something quite significant which is the body of
knowledge humanity uses for its benefit today. Many people will agree that if something has greatly transformed humanity
as we see it today, it is science and obviously most science is founded on mathematics.

---

### #265 — list1
*January 4, 2017, 6:30 PM*

O'k we can start from the very beginning. Let we have the ODE

$$ y^{'} = f ( t , y )$$

What is your formal statement ?

---

### #266 — Cuchulainn
*January 4, 2017, 6:47 PM*

> O'k we can start from the very beginning. Let we have the ODE
>
> $$ y^{'} = f ( t , y )$$
>
> What is your formal statement ?
Picard–Lindelöf

Peano

Carathéodory

Banach fixed point theorem

Gronwall's lemma

*My method is based on mathematical common sense.*

Mathematics is not based on common sense.

---

### #267 — Cuchulainn
*January 4, 2017, 6:54 PM*

$dy/dt = a y^{2/3},   y(0) = 0$

---

### #268 — ppauper
*January 4, 2017, 9:05 PM*

> O'k we can start from the very beginning. Let we have the ODE
>
> $$ y^{'} = f ( t , y )$$
>
> What is your formal statement ?

he covered that on Thu Nov 24, 2016 in

>> 2. Introduction to the Method of Iterated Integrals

>> To start the discussion, we try to find the solution to General initial value problem associated with

>> first order Ordinary Differential Equations given as

$\frac{dy}{dt}=f(t,y)$, $t\ge 0$, $y(t_0)=y_0$

---

### #269 — Amin (Topic Author)
*January 4, 2017, 9:16 PM*

> O'k we can start from the very beginning. Let we have the ODE
>
> $$ y^{'} = f ( t , y )$$
>
> What is your formal statement ?
Other than standard regularity conditions, I see two things. I differentiate the ODE with respect to y, which requires
the differentiability condition of f(y,t) w.r.t y(t). I then integrate with respect to t so all the conditions(and
various possibilities of retrieving primitives from derivatives that I might not have considered) required to retrieve a
primitive from its derivative will apply. The purpose of various terms in the series of iterated integrals is to
retrieve "evolution of various order dy/dt(t0)-derivatives"(which are the primitives) after repeated integrations with
respect to t.

Peter, may be you can help me arrange my thoughts better about the above ideas. I will be very thankful.

---

### #270 — Cuchulainn
*January 4, 2017, 9:34 PM*

> O'k we can start from the very beginning. Let we have the ODE
>
> $$ y^{'} = f ( t , y )$$
>
> What is your formal statement ?

he covered that on Thu Nov 24, 2016 in

>> 2. Introduction to the Method of Iterated Integrals

>> To start the discussion, we try to find the solution to General initial value problem associated with

>> first order Ordinary Differential Equations given as

$\frac{dy}{dt}=f(t,y)$, $t\ge 0$, $y(t_0)=y_0$
Anyone write that!  It's just formal symbols. It means nothing.

BTW typo fixed.

$\frac{dy}{dt}=f(t,y)$, $t\ge t_{0}$, $y(t_0)=y_0$

And why not go the whole hog $t\le t_{0}$

---

### #271 — list1
*January 5, 2017, 12:35 AM*

> O'k we can start from the very beginning. Let we have the ODE
>
> $$ y^{'} = f ( t , y )$$
>
> What is your formal statement ?
Other than standard regularity conditions, I see two things. I differentiate the ODE with respect to y, which requires
the differentiability condition of f(y,t) w.r.t y(t). I then integrate with respect to t so all the conditions(and
various possibilities of retrieving primitives from derivatives that I might not have considered) required to retrieve a
primitive from its derivative will apply. The purpose of various terms in the series of iterated integrals is to
retrieve "evolution of various order dy/dt(t0)-derivatives"(which are the primitives) after repeated integrations with
respect to t.

Peter, may be you can help me arrange my thoughts better about the above ideas. I will be very thankful.
Thus we assume that there exists unique solution and we are trying to present its consecutive approximation. You need to
present n-th term  and sow convergence n-th term to the solution. We do not discuss whether this methods better or worse
of well known constructions. We need to do this in order to present that it makes sense to do.

---

### #272 — ppauper
*January 5, 2017, 7:11 AM*

>
>
>
> And why not go the whole hog $t\le t_{0}$

I thought you wanted him to do initial value problems!

---

### #273 — Cuchulainn
*January 5, 2017, 11:38 AM*

>
>
>
> And why not go the whole hog $t\le t_{0}$

I thought you wanted him to do initial value problems!
Yes.

This is probably an example of an ill-posed/ backward time problem.  Most methods will give unbounded solutions, My
hunch is iterated integral gives a divergent series?(?)

It was to show that the problem is not properly scoped.

Here is IVP with TWO solutions

$y' = t \sqrt y,   y(0) = 0 $

i.e $ y = 0 , y = t^4/16$

---

### #274 — Cuchulainn
*January 5, 2017, 3:43 PM*

At the other extreme

$y' = y/x, y(0) = 1$ has NO solution

So, you also have to take into account the interval in which a solution is sought.

There you have it.

---

### #275 — list1
*January 5, 2017, 5:03 PM*

> At the other extreme
>
>
>
> $y' = y/x, y(0) = 1$ has NO solution
>
>
>
> So, you also have to take into account the interval in which a solution is sought.
>
>
>
> There you have it.
The initial step is we assume that there exists unique solution on [ 0 , T ] with a sufficient smoothness. Next we are
trying to present its approximation.

---

### #276 — Cuchulainn
*January 5, 2017, 8:05 PM*

> At the other extreme
>
>
>
> $y' = y/x, y(0) = 1$ has NO solution
>
>
>
> So, you also have to take into account the interval in which a solution is sought.
>
>
>
> There you have it.
The initial step is we assume that there exists unique solution on [ 0 , T ] with a sufficient smoothness. Next we are
trying to present its approximation.
LOL

So, let's pretend this IVP has a solution. How would you approximate it?

---

### #277 — Cuchulainn
*January 5, 2017, 8:10 PM*

> At the other extreme
>
>
>
> $y' = y/x, y(0) = 1$ has NO solution
>
>
>
> So, you also have to take into account the interval in which a solution is sought.
>
>
>
> There you have it.
The initial step is we assume that there exists unique solution on [ 0 , T ] with a sufficient smoothness. Next we are
trying to present its approximation.
LOL

So, let's pretend this IVP has a solution. How would you approximates it? Don't let non-existence get in the way, did I
understand you correctly?

---

### #278 — outrun
*January 5, 2017, 9:07 PM*

I think the most natural way forward would be to *compare* Amin's method against simple methods that give power series
approximations. Is there a difference? Are there positive differences?

Here is a example Airy's equation power series solution tutorial. This example gives a simple recurrent solution for all
the power series terms
[YouTube Video](https://www.youtube.com/embed/)

---

### #279 — Cuchulainn
*January 5, 2017, 9:18 PM*

Could do, but count me out  It's soo engineering methods style and old-fashioned. It's just about 1st year maths method
and offer little insights.

But it won't help as I already noted by both comrade list and myself.

For Airy, just use Boost.

[http://www.boost.org/doc/libs/1_52_0/li ... ry/ai.html](http://www.boost.org/doc/libs/1_52_0/libs/math/doc/sf_and_dist/html/math_toolkit/special/airy/ai.html)

And the method needs a supercomputer to produce numerical values!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Getting tired of this discussion.

---

### #280 — outrun
*January 5, 2017, 9:36 PM*

Yes very tired, that why I think it needs to move forward.

Amin's method gives a series expansion, so we need to compare apples with apples. You only need supercomputer if the
series don't converge quickly, but that would be the same for *any* other power series expansion method.

Yes it's 1st year math method which makes it a good benchmark to test Amin's method against. By plugging in power
series, differentiating and integrating of terms are as easy as it gets.

---

### #281 — amike
*January 5, 2017, 10:00 PM*

I could be wrong, but it seems to me that the onus is on the person claiming that they have made a `breakthrough' to
clearly explain what the breakthrough is, and how the breakthrough actually makes progress on several hundred years of
research in this field.  Not for readers of this particular twitter feed to try to guess.

I would vote for a post moratorium until a new, more complete version of the paper comes out that explains all this... 
it's possible that I am just overly grumpy today though.

---

### #282 — Amin (Topic Author)
*January 5, 2017, 10:10 PM*

> O'k we can start from the very beginning. Let we have the ODE
>
> $$ y^{'} = f ( t , y )$$
>
> What is your formal statement ?
Other than standard regularity conditions, I see two things. I differentiate the ODE with respect to y, which requires
the differentiability condition of f(y,t) w.r.t y(t). I then integrate with respect to t so all the conditions(and
various possibilities of retrieving primitives from derivatives that I might not have considered) required to retrieve a
primitive from its derivative will apply. The purpose of various terms in the series of iterated integrals is to
retrieve "evolution of various order dy/dt(t0)-derivatives"(which are the primitives) after repeated integrations with
respect to t.

Peter, may be you can help me arrange my thoughts better about the above ideas. I will be very thankful.
Thus we assume that there exists unique solution and we are trying to present its consecutive approximation. You need to
present n-th term  and sow convergence n-th term to the solution. We do not discuss whether this methods better or worse
of well known constructions. We need to do this in order to present that it makes sense to do.
I have re-written the introduction to method of iterated integrals and tried to make it more accessible. Earlier
exposition was not very good but in the revision, I am sure that people would easily understand most concepts. Here is
the new simpler version of the explanation of the basics of the method. It is probably not a formal proof but I am sure
a formal proof can easily be derived from these lines.

2. Introduction to the Method of Iterated Integrals

To start the discussion, we try to find the solution to General initial value problem associated with first order
Ordinary Differential Equations given as

$\frac{dy}{dt}=f(t,y)$,  $t\geq 0$, $y\left(t_0\right)=y_0$ Equation(1)

Integrating Equation (1), we get the formal solution to the initial value problem as

$y(t)=y\left(t_0\right)+\int_{t_0}^t f(\tau ,y(\tau )) \, d\tau$  Equation(2)

If only we could exactly solve the formal integral in equation (2), we would find our desired solution. Obviously
$f(\tau ,y(\tau ))$ cannot in general be directly and analytically integrated in the above integral.

However we can write differential function in the formal integral in equation (2) as a function of initial value of
$y\left(t_0\right)$ and a formal integral of appropriate derivative of the differential function with respect to y so
that sum of both terms is equated with differential function in formal integral in equation (2). We can for example
write as

$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]\frac{dy(s)}{ds}ds$
Equation(3)

$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))ds$
Equation(4)

Where we have used equation (1) with equation (3) to get equation (4).

Equation (2) can now be written after substituting Equation(4) in it as

$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))dsd\tau$
Equation(5)

In Equation(5), we notice that first order integral in second term could mostly be easily evaluated while the second
order integral in third term has to be taken in formal sense and this second order integral could not, in general, be
easily evaluated.

However the term inside the second order formal integral in equation (5) can again similarly be written in terms of
initial values$y\left(t_0\right)$ and an appropriate formal integral as

$\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))=\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)$

$+\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]\frac{dy(v)}{dv}dv$

$=\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)+\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]f(v,y(v))dv$
Equation(6)

Substituting Equation(6) in the second order formal integral in equation (5), we can write as

$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)dsd\tau$

$+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\left(\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]f(v,y(v))\right)dvdsd\tau$
Equation (7)

In the equation (7), the first order and second order integrals can easily be evaluated at initial values
$y\left(t_0\right)$ while the third integral has to be taken in the formal sense.

We can continue to expand the highest order formal integral in form of iterated integral terms evaluated at
$y\left(t_0\right)$ and one order higher formal integral and continue to add further terms in our series solution.

It is interesting to notice intuitively how the upper limits of the inside integrals go to time in each outer integral
so as the higher indirect derivative in inner integrals make a contribution to lower indirect derivatives only till
running time in successive outer integral.

---

### #283 — Paul
*January 5, 2017, 10:21 PM*

Give him a difficult example that doesn't have coefficients being powers of the independent variable and then he won't
get a power series!

---

### #284 — amike
*January 5, 2017, 11:35 PM*

Here is "my" approach to solving odes...

Write the system as:

$$ \frac{dy(t)}{dt}=\epsilon f(t,y(t)),\quad y(t_0)=y_0, $$

The parameter epsilon is in there as a formal expansion parameter, but this can easily be seen to be a small time
expansion by scaling the interval to [0,1].

Now, introduce the formal series solution:

$$ y(t)=y_0+\epsilon y_1(t)+\epsilon^2y_2(t)+\epsilon^3y_3(t)+\ldots, $$

Insert this into the left and right sides of the ode, and perform a Taylor expansion in epsilon and match
order-by-order.

The first non-trivial order gives:

$$ y_1(t)=\int_{t_0}^t ds f(s,y(t_0)), $$

the next:

$
$ y_2(t)=\int_{t_0}^t ds \frac{\partial f}{\partial y}(s,y(t_0)) y_1(s)=\int_{t_0}^t ds \int_{t_0}^s du  \frac{\partial f}{\partial y}(s,y(t_0)) f(u,y(t_0)) $
$

and so on.

Now:

1. This approach is definitely not new (wasn't Newton doing something like this when he `invented' calculus?).

2. This approach is seldom useful -- in fact, I see perturbation expansions like this more often in the introduction of
books dedicated to giving better approaches.

So definitely not a breakthrough.

But:

1. The first two orders in the expansion given above are the same as the `iterated integrals' approach.

2. I can reproduce all the expansions (to all orders given) of first order ode examples using this expansion (with a
straightforward extension to systems of equations) -- power series or not.

3. The results from the few higher-order examples I looked at were also replicated by naive conversion into a system of
first-order equations.

Obviously I can't claim that iterated integrals is just a simple perturbation expansion in disguise (because I still do
not understand the presentation of ii), but I am still left wondering how/where it is making significant progress...

---

### #285 — Paul
*January 5, 2017, 11:41 PM*

There is no progress. But the thread refuses to die! And Amin is so darn polite about any criticism!

---

### #286 — Amin (Topic Author)
*January 6, 2017, 3:13 AM*

> Give him a difficult example that doesn't have coefficients being powers of the independent variable and then he won't
get a power series!
I have solved this ODE(here in post 234,[viewtopic.php?f=4&t=99702&start=225](https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=225) ) that has an exponential in both t and y after transformation.  Paul always sets the bar higher so we have to work harder.

---

### #287 — Cuchulainn
*January 6, 2017, 8:04 AM*

> Yes very tired, that why I think it needs to move forward.
>
>
>
> Amin's method gives a series expansion, so we need to compare apples with apples. You only need supercomputer if the
series don't converge quickly, but that would be the same for *any* other power series expansion method.
>
>
>
> Yes it's 1st year math method which makes it a good benchmark to test Amin's method against. By plugging in power
series, differentiating and integrating of terms are as easy as it gets.
No, it is not a good benchmark. That's not the issue. Churning out buckets of examples proves nothing at this stage.

This is school maths which is usually wrong.

The fundamental assumption of needing double/iterated integral js overkill. EX is is possible to reduce a 2nd order ODE
to an integral equation with ONE integral.

---

### #288 — Cuchulainn
*January 6, 2017, 9:04 AM*

> Give him a difficult example that doesn't have coefficients being powers of the independent variable and then he won't
get a power series!
I have solved this ODE(here in post 234,[viewtopic.php?f=4&t=99702&start=225](https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=225) ) that has an exponential in both t and y after transformation.  Paul always sets the bar higher so we have to work harder.

This is a half-hearted answer. It does not get us anywhere.

---

### #289 — Amin (Topic Author)
*January 6, 2017, 9:30 AM*

> I have re-written the introduction to method of iterated integrals and tried to make it more accessible. Earlier
exposition was not very good but in the revision, I am sure that people would easily understand most concepts. Here is
the new simpler version of the explanation of the basics of the method. It is probably not a formal proof but I am sure
a formal proof can easily be derived from these lines.
>
>
>
> 2. Introduction to the Method of Iterated Integrals
>
>
>
> To start the discussion, we try to find the solution to General initial value problem associated with first order
Ordinary Differential Equations given as
>
> $\frac{dy}{dt}=f(t,y)$,  $t\geq 0$, $y\left(t_0\right)=y_0$ Equation(1)
>
>
>
> Integrating Equation (1), we get the formal solution to the initial value problem as
>
> $y(t)=y\left(t_0\right)+\int_{t_0}^t f(\tau ,y(\tau )) \, d\tau$  Equation(2)
>
>
>
> If only we could exactly solve the formal integral in equation (2), we would find our desired solution. Obviously
$f(\tau ,y(\tau ))$ cannot in general be directly and analytically integrated in the above integral.
>
> However we can write differential function in the formal integral in equation (2) as a function of initial value of
$y\left(t_0\right)$ and a formal integral of appropriate derivative of the differential function with respect to y so
that sum of both terms is equated with differential function in formal integral in equation (2). We can for example
write as
>
>
$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]\frac{dy(s)}{ds}ds$
Equation(3)
>
>
$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))ds$
Equation(4)
>
> Where we have used equation (1) with equation (3) to get equation (4).
>
>
>
> Equation (2) can now be written after substituting Equation(4) in it as
>
>
$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))dsd\tau$
Equation(5)
>
>
>
> In Equation(5), we notice that first order integral in second term could mostly be easily evaluated while the second
order integral in third term has to be taken in formal sense and this second order integral could not, in general, be
easily evaluated.
>
> However the term inside the second order formal integral in equation (5) can again similarly be written in terms of
initial values$y\left(t_0\right)$ and an appropriate formal integral as
>
>
$\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))=\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)$
>
>
$+\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]\frac{dy(v)}{dv}dv$
>
>
$=\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)+\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]f(v,y(v))dv$
Equation(6)
>
>
>
> Substituting Equation(6) in the second order formal integral in equation (5), we can write as
>
>
$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)dsd\tau$
>
>
$+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\left(\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]f(v,y(v))\right)dvdsd\tau$
Equation (7)
>
>
>
> In the equation (7), the first order and second order integrals can easily be evaluated at initial values
$y\left(t_0\right)$ while the third integral has to be taken in the formal sense.
>
> We can continue to expand the highest order formal integral in form of iterated integral terms evaluated at
$y\left(t_0\right)$ and one order higher formal integral and continue to add further terms in our series solution.
>
> It is interesting to notice intuitively how the upper limits of the inside integrals go to time in each outer integral
so as the higher indirect derivative in inner integrals make a contribution to lower indirect derivatives only till
running time in successive outer integral.
Cuch, do you understand this explanation? Did you get the logic of equations 3,4 and 5 ?

---

### #290 — outrun
*January 6, 2017, 9:56 AM*

> Here is "my" approach to solving odes...
>
>
>
> Write the system as:
>
> $$ \frac{dy(t)}{dt}=\epsilon f(t,y(t)),\quad y(t_0)=y_0, $$
>
> The parameter epsilon is in there as a formal expansion parameter, but this can easily be seen to be a small time
expansion by scaling the interval to [0,1].
>
>
>
> Now, introduce the formal series solution:
>
> $$ y(t)=y_0+\epsilon y_1(t)+\epsilon^2y_2(t)+\epsilon^3y_3(t)+\ldots, $$
>
> Insert this into the left and right sides of the ode, and perform a Taylor expansion in epsilon and match
order-by-order.
>
>
>
> The first non-trivial order gives:
>
> $$ y_1(t)=\int_{t_0}^t ds f(s,y(t_0)), $$
>
> the next:
>
> $
$ y_2(t)=\int_{t_0}^t ds \frac{\partial f}{\partial y}(s,y(t_0)) y_1(s)=\int_{t_0}^t ds \int_{t_0}^s du  \frac{\partial f}{\partial y}(s,y(t_0)) f(u,y(t_0)) $
$
>
> and so on.
>
>
>
> Now:
>
> 1. This approach is definitely not new (wasn't Newton doing something like this when he `invented' calculus?).
>
> 2. This approach is seldom useful -- in fact, I see perturbation expansions like this more often in the introduction
of books dedicated to giving better approaches.
>
> So definitely not a breakthrough.
>
>
>
> But:
>
> 1. The first two orders in the expansion given above are the same as the `iterated integrals' approach.
>
> 2. I can reproduce all the expansions (to all orders given) of first order ode examples using this expansion (with a
straightforward extension to systems of equations) -- power series or not.
>
> 3. The results from the few higher-order examples I looked at were also replicated by naive conversion into a system
of first-order equations.
>
>
>
> Obviously I can't claim that iterated integrals is just a simple perturbation expansion in disguise (because I still
do not understand the presentation of ii), but I am still left wondering how/where it is making significant progress...
So it looks like this is a "perturbation expansion"? Shouldn't you research this Amin? It would be a waste of time to
continue if it has all been done before.

---

### #291 — Cuchulainn
*January 6, 2017, 10:02 AM*

> I have re-written the introduction to method of iterated integrals and tried to make it more accessible. Earlier
exposition was not very good but in the revision, I am sure that people would easily understand most concepts. Here is
the new simpler version of the explanation of the basics of the method. It is probably not a formal proof but I am sure
a formal proof can easily be derived from these lines.
>
>
>
> 2. Introduction to the Method of Iterated Integrals
>
>
>
> To start the discussion, we try to find the solution to General initial value problem associated with first order
Ordinary Differential Equations given as
>
> $\frac{dy}{dt}=f(t,y)$,  $t\geq 0$, $y\left(t_0\right)=y_0$ Equation(1)
>
>
>
> Integrating Equation (1), we get the formal solution to the initial value problem as
>
> $y(t)=y\left(t_0\right)+\int_{t_0}^t f(\tau ,y(\tau )) \, d\tau$  Equation(2)
>
>
>
> If only we could exactly solve the formal integral in equation (2), we would find our desired solution. Obviously
$f(\tau ,y(\tau ))$ cannot in general be directly and analytically integrated in the above integral.
>
> However we can write differential function in the formal integral in equation (2) as a function of initial value of
$y\left(t_0\right)$ and a formal integral of appropriate derivative of the differential function with respect to y so
that sum of both terms is equated with differential function in formal integral in equation (2). We can for example
write as
>
>
$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]\frac{dy(s)}{ds}ds$
Equation(3)
>
>
$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))ds$
Equation(4)
>
> Where we have used equation (1) with equation (3) to get equation (4).
>
>
>
> Equation (2) can now be written after substituting Equation(4) in it as
>
>
$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))dsd\tau$
Equation(5)
>
>
>
> In Equation(5), we notice that first order integral in second term could mostly be easily evaluated while the second
order integral in third term has to be taken in formal sense and this second order integral could not, in general, be
easily evaluated.
>
> However the term inside the second order formal integral in equation (5) can again similarly be written in terms of
initial values$y\left(t_0\right)$ and an appropriate formal integral as
>
>
$\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))=\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)$
>
>
$+\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]\frac{dy(v)}{dv}dv$
>
>
$=\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)+\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]f(v,y(v))dv$
Equation(6)
>
>
>
> Substituting Equation(6) in the second order formal integral in equation (5), we can write as
>
>
$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)dsd\tau$
>
>
$+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\left(\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]f(v,y(v))\right)dvdsd\tau$
Equation (7)
>
>
>
> In the equation (7), the first order and second order integrals can easily be evaluated at initial values
$y\left(t_0\right)$ while the third integral has to be taken in the formal sense.
>
> We can continue to expand the highest order formal integral in form of iterated integral terms evaluated at
$y\left(t_0\right)$ and one order higher formal integral and continue to add further terms in our series solution.
>
> It is interesting to notice intuitively how the upper limits of the inside integrals go to time in each outer integral
so as the higher indirect derivative in inner integrals make a contribution to lower indirect derivatives only till
running time in successive outer integral.
Cuch, do you understand this explanation? Did you get the logic of equations 3,4 and 5 ?
No, I don't get it. And I don't know why you are dong it.

Equation (2) is fine and standard.

**The leap of faith (for me) is which result of calculus was used in deriving (3)?**

And show how its evolves for this problem

Here is IVP with TWO solutions

$y' = t \sqrt y,   y(0) = 0 $

i.e $ y = 0 , y = t^4/16$

---

### #292 — Cuchulainn
*January 6, 2017, 10:03 AM*

> Here is "my" approach to solving odes...
>
>
>
> Write the system as:
>
> $$ \frac{dy(t)}{dt}=\epsilon f(t,y(t)),\quad y(t_0)=y_0, $$
>
> The parameter epsilon is in there as a formal expansion parameter, but this can easily be seen to be a small time
expansion by scaling the interval to [0,1].
>
>
>
> Now, introduce the formal series solution:
>
> $$ y(t)=y_0+\epsilon y_1(t)+\epsilon^2y_2(t)+\epsilon^3y_3(t)+\ldots, $$
>
> Insert this into the left and right sides of the ode, and perform a Taylor expansion in epsilon and match
order-by-order.
>
>
>
> The first non-trivial order gives:
>
> $$ y_1(t)=\int_{t_0}^t ds f(s,y(t_0)), $$
>
> the next:
>
> $
$ y_2(t)=\int_{t_0}^t ds \frac{\partial f}{\partial y}(s,y(t_0)) y_1(s)=\int_{t_0}^t ds \int_{t_0}^s du  \frac{\partial f}{\partial y}(s,y(t_0)) f(u,y(t_0)) $
$
>
> and so on.
>
>
>
> Now:
>
> 1. This approach is definitely not new (wasn't Newton doing something like this when he `invented' calculus?).
>
> 2. This approach is seldom useful -- in fact, I see perturbation expansions like this more often in the introduction
of books dedicated to giving better approaches.
>
> So definitely not a breakthrough.
>
>
>
> But:
>
> 1. The first two orders in the expansion given above are the same as the `iterated integrals' approach.
>
> 2. I can reproduce all the expansions (to all orders given) of first order ode examples using this expansion (with a
straightforward extension to systems of equations) -- power series or not.
>
> 3. The results from the few higher-order examples I looked at were also replicated by naive conversion into a system
of first-order equations.
>
>
>
> Obviously I can't claim that iterated integrals is just a simple perturbation expansion in disguise (because I still
do not understand the presentation of ii), but I am still left wondering how/where it is making significant progress...
So it looks like this is a "perturbation expansion"? Shouldn't you research this Amin? It would be a waste of time to
continue if it has all been done before.
This is a special class of ODEs. And people spend their lives working on this.

---

### #293 — list1
*January 6, 2017, 10:25 AM*

> I have re-written the introduction to method of iterated integrals and tried to make it more accessible. Earlier
exposition was not very good but in the revision, I am sure that people would easily understand most concepts. Here is
the new simpler version of the explanation of the basics of the method. It is probably not a formal proof but I am sure
a formal proof can easily be derived from these lines.
>
>
>
> 2. Introduction to the Method of Iterated Integrals
>
>
>
> To start the discussion, we try to find the solution to General initial value problem associated with first order
Ordinary Differential Equations given as
>
> $\frac{dy}{dt}=f(t,y)$,  $t\geq 0$, $y\left(t_0\right)=y_0$ Equation(1)
>
>
>
> Integrating Equation (1), we get the formal solution to the initial value problem as
>
> $y(t)=y\left(t_0\right)+\int_{t_0}^t f(\tau ,y(\tau )) \, d\tau$  Equation(2)
>
>
>
> If only we could exactly solve the formal integral in equation (2), we would find our desired solution. Obviously
$f(\tau ,y(\tau ))$ cannot in general be directly and analytically integrated in the above integral.
>
> However we can write differential function in the formal integral in equation (2) as a function of initial value of
$y\left(t_0\right)$ and a formal integral of appropriate derivative of the differential function with respect to y so
that sum of both terms is equated with differential function in formal integral in equation (2). We can for example
write as
>
>
$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]\frac{dy(s)}{ds}ds$
Equation(3)
>
>
$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))ds$
Equation(4)
>
> Where we have used equation (1) with equation (3) to get equation (4).
>
>
>
> Equation (2) can now be written after substituting Equation(4) in it as
>
>
$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))dsd\tau$
Equation(5)
>
>
>
> In Equation(5), we notice that first order integral in second term could mostly be easily evaluated while the second
order integral in third term has to be taken in formal sense and this second order integral could not, in general, be
easily evaluated.
>
> However the term inside the second order formal integral in equation (5) can again similarly be written in terms of
initial values$y\left(t_0\right)$ and an appropriate formal integral as
>
>
$\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))=\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)$
>
>
$+\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]\frac{dy(v)}{dv}dv$
>
>
$=\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)+\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]f(v,y(v))dv$
Equation(6)
>
>
>
> Substituting Equation(6) in the second order formal integral in equation (5), we can write as
>
>
$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)dsd\tau$
>
>
$+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\left(\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]f(v,y(v))\right)dvdsd\tau$
Equation (7)
>
>
>
> In the equation (7), the first order and second order integrals can easily be evaluated at initial values
$y\left(t_0\right)$ while the third integral has to be taken in the formal sense.
>
> We can continue to expand the highest order formal integral in form of iterated integral terms evaluated at
$y\left(t_0\right)$ and one order higher formal integral and continue to add further terms in our series solution.
>
> It is interesting to notice intuitively how the upper limits of the inside integrals go to time in each outer integral
so as the higher indirect derivative in inner integrals make a contribution to lower indirect derivatives only till
running time in successive outer integral.
Cuch, do you understand this explanation? Did you get the logic of equations 3,4 and 5 ?
Thus you assumed that there exists a solution y ( t ) and arrived at formula (7) given that f ( t , y ) is 3-times
differentiable. Therefore you can state that if y is a solution then it satisfies (7). Is it the (7) is what you tried
to prove?

---

### #294 — outrun
*January 6, 2017, 10:29 AM*

> Here is "my" approach to solving odes...
>
>
>
> Write the system as:
>
> $$ \frac{dy(t)}{dt}=\epsilon f(t,y(t)),\quad y(t_0)=y_0, $$
>
> The parameter epsilon is in there as a formal expansion parameter, but this can easily be seen to be a small time
expansion by scaling the interval to [0,1].
>
>
>
> Now, introduce the formal series solution:
>
> $$ y(t)=y_0+\epsilon y_1(t)+\epsilon^2y_2(t)+\epsilon^3y_3(t)+\ldots, $$
>
> Insert this into the left and right sides of the ode, and perform a Taylor expansion in epsilon and match
order-by-order.
>
>
>
> The first non-trivial order gives:
>
> $$ y_1(t)=\int_{t_0}^t ds f(s,y(t_0)), $$
>
> the next:
>
> $
$ y_2(t)=\int_{t_0}^t ds \frac{\partial f}{\partial y}(s,y(t_0)) y_1(s)=\int_{t_0}^t ds \int_{t_0}^s du  \frac{\partial f}{\partial y}(s,y(t_0)) f(u,y(t_0)) $
$
>
> and so on.
>
>
>
> Now:
>
> 1. This approach is definitely not new (wasn't Newton doing something like this when he `invented' calculus?).
>
> 2. This approach is seldom useful -- in fact, I see perturbation expansions like this more often in the introduction
of books dedicated to giving better approaches.
>
> So definitely not a breakthrough.
>
>
>
> But:
>
> 1. The first two orders in the expansion given above are the same as the `iterated integrals' approach.
>
> 2. I can reproduce all the expansions (to all orders given) of first order ode examples using this expansion (with a
straightforward extension to systems of equations) -- power series or not.
>
> 3. The results from the few higher-order examples I looked at were also replicated by naive conversion into a system
of first-order equations.
>
>
>
> Obviously I can't claim that iterated integrals is just a simple perturbation expansion in disguise (because I still
do not understand the presentation of ii), but I am still left wondering how/where it is making significant progress...
So it looks like this is a "perturbation expansion"? Shouldn't you research this Amin? It would be a waste of time to
continue if it has all been done before.
This is a special class of ODEs. And people spend their lives working on this.
No, the post is about this next quote (and for strange reason both you and Amin miss this?):

"Obviously I can't claim that iterated integrals is just a simple perturbation expansion in disguise (because I still do
not understand the presentation of ii).."

---

### #295 — Amin (Topic Author)
*January 6, 2017, 11:01 AM*

> I have re-written the introduction to method of iterated integrals and tried to make it more accessible. Earlier
exposition was not very good but in the revision, I am sure that people would easily understand most concepts. Here is
the new simpler version of the explanation of the basics of the method. It is probably not a formal proof but I am sure
a formal proof can easily be derived from these lines.
>
>
>
> 2. Introduction to the Method of Iterated Integrals
>
>
>
> To start the discussion, we try to find the solution to General initial value problem associated with first order
Ordinary Differential Equations given as
>
> $\frac{dy}{dt}=f(t,y)$,  $t\geq 0$, $y\left(t_0\right)=y_0$ Equation(1)
>
>
>
> Integrating Equation (1), we get the formal solution to the initial value problem as
>
> $y(t)=y\left(t_0\right)+\int_{t_0}^t f(\tau ,y(\tau )) \, d\tau$  Equation(2)
>
>
>
> If only we could exactly solve the formal integral in equation (2), we would find our desired solution. Obviously
$f(\tau ,y(\tau ))$ cannot in general be directly and analytically integrated in the above integral.
>
> However we can write differential function in the formal integral in equation (2) as a function of initial value of
$y\left(t_0\right)$ and a formal integral of appropriate derivative of the differential function with respect to y so
that sum of both terms is equated with differential function in formal integral in equation (2). We can for example
write as
>
>
$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]\frac{dy(s)}{ds}ds$
Equation(3)
>
>
$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))ds$
Equation(4)
>
> Where we have used equation (1) with equation (3) to get equation (4).
>
>
>
> Equation (2) can now be written after substituting Equation(4) in it as
>
>
$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))dsd\tau$
Equation(5)
>
>
>
> In Equation(5), we notice that first order integral in second term could mostly be easily evaluated while the second
order integral in third term has to be taken in formal sense and this second order integral could not, in general, be
easily evaluated.
>
> However the term inside the second order formal integral in equation (5) can again similarly be written in terms of
initial values$y\left(t_0\right)$ and an appropriate formal integral as
>
>
$\frac{\partial }{\partial y}[f(\tau ,y(s))]f(s,y(s))=\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)$
>
>
$+\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]\frac{dy(v)}{dv}dv$
>
>
$=\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)+\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]f(v,y(v))dv$
Equation(6)
>
>
>
> Substituting Equation(6) in the second order formal integral in equation (5), we can write as
>
>
$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)dsd\tau$
>
>
$+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\left(\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(v))]f(s,y(v))\right]f(v,y(v))\right)dvdsd\tau$
Equation (7)
>
>
>
> In the equation (7), the first order and second order integrals can easily be evaluated at initial values
$y\left(t_0\right)$ while the third integral has to be taken in the formal sense.
>
> We can continue to expand the highest order formal integral in form of iterated integral terms evaluated at
$y\left(t_0\right)$ and one order higher formal integral and continue to add further terms in our series solution.
>
> It is interesting to notice intuitively how the upper limits of the inside integrals go to time in each outer integral
so as the higher indirect derivative in inner integrals make a contribution to lower indirect derivatives only till
running time in successive outer integral.
Cuch, do you understand this explanation? Did you get the logic of equations 3,4 and 5 ?
Thus you assumed that there exists a solution y ( t ) and arrived at formula (7) given that f ( t , y ) is 3-times
differentiable. Therefore you can state that if y is a solution then it satisfies (7). Is it the (7) is what you tried
to prove?
f(t,y) has to be just once differentiable. Try equation (7) and related exercise on dy/dt=y(t). here f(y,t)=y. I have
given this example in the preliminary version of the paper and you could look at that. I wanted people to know that even
once differentiable functions can have expansions with infinite terms. Let me know what you would like to comment after
you have worked out this simple case.

---

### #296 — list1
*January 6, 2017, 11:24 AM*

The primary question was what do you wish to state about (7).

Secondary question is differentiability. If you look at the right hand side (7) and apply differentiation with respect
to y then you will get 2nd derivative of f with respect y. Expending your approach by n times the derivative order looks
like should be increased.

---

### #297 — Cuchulainn
*January 6, 2017, 12:00 PM*

>
> So it looks like this is a "perturbation expansion"? Shouldn't you research this Amin? It would be a waste of time to
continue if it has all been done before.
This is a special class of ODEs. And people spend their lives working on this.
No, the post is about this next quote (and for strange reason both you and Amin miss this?):

"Obviously I can't claim that iterated integrals is just a simple perturbation expansion in disguise (because I still do
not understand the presentation of ii).."
Have you ever worked in this area? It is stiff ODE, singular/regular perturbations and are numerically very difficult.

---

### #298 — outrun
*January 6, 2017, 12:05 PM*

>
> This is a special class of ODEs. And people spend their lives working on this.
No, the post is about this next quote (and for strange reason both you and Amin miss this?):

"Obviously I can't claim that iterated integrals is just a simple perturbation expansion in disguise (because I still do
not understand the presentation of ii).."
Have you ever worked in this area? It is stiff ODE, singular/regular perturbations and are numerically very difficult.
Yes I have. But you keep bending the discussion to "you" and change the topic to "who is authority" or something..
that's not interesting.

Read that post I quoted, it's one of the few posts that actually adds something here. Everyone one else is running
around in circles with their fingers in their ears.

---

### #299 — outrun
*January 6, 2017, 12:09 PM*

>
> No, the post is about this next quote (and for strange reason both you and Amin miss this?):
>
>
>
>
>
> "Obviously I can't claim that iterated integrals is just a simple perturbation expansion in disguise (because I still
do not understand the presentation of ii).."
Have you ever worked in this area? It is stiff ODE, singular/regular perturbations and are numerically very difficult.
Yes I have. But you keep bending the discussion to "you" and change the topic to "who is authority" or something..
that's not interesting.

Read that post I quoted, it's one of the few posts that actually adds something here. Everyone one else is running
around in circles with their fingers in their ears.
It's not about solving an ODE and if "perturbations and are numerically very difficult", it's about showing that there
is nothing new here (addressing the "breakthrough" claim) and that it's not a good idea in general either. I'll quote it
again, snipping it even further (an removing too much context) to get you to focus on the essence:

"iterated integrals is just a simple perturbation expansion in disguise"

..so it's *not* saying "le'ts try to do perturbation expansion for this specific ODE because I think it' a good idea"

..no no no, instead it's saying

"iterated integrals is just a simple perturbation expansion in disguise"

---

### #300 — Amin (Topic Author)
*January 6, 2017, 12:18 PM*

> The primary question was what do you wish to state about (7).
>
> Secondary question is differentiability. If you look at the right hand side (7) and apply differentiation with respect
to y then you will get 2nd derivative of f with respect y. Expending your approach by n times the derivative order looks
like should be increased.
Equation(7) is another formal solution to Equation(1) which is equivalent to formal solution as stated in Equation(2).
However the first two terms in the formal solution in Equation (7) can be easily evaluated as they are evaluated at
y(t0) and the last third term has to be considered in the formal sense. We can find infinite number of formal solutions
equivalent to Equation(2) and equivalent to each other where n number of terms (n is an arbitrary integer) have been
evaluated at y(t0) and final n+1 th term has to be understood in formal sense and could not be evaluated in general. We
hope to choose a formal solution in which enough number of terms have been evaluated at y(t0) so that the last term
which is considered in formal sense and cannot be evaluated has negligible value. Of course, like many other series,
this may always not be the case. And of course, some mathematical conditions would need to apply for all solutions to be
equivalent but I am sure most mathematicians can easily work that out since most of the ideas are based on simple
calculus.

However, since the method finds out series solution in natural derivatives of function y(t), we can many time look at
the series and be able to find out what function it is representing and it could lead us to closed form solution of the
problem. This is a new method and I am sure there is a lot of work that needs to be done to work out everything in
complete detail. For example there could be some better ways of 'finding the primitive' in many specialized cases but
integration is a natural generic choice that would mostly work. I have tried to make enough effort by sharing
mathematica programs so other friends could easily try it on ODEs of their choice. It would have been almost impossible
to work out these iterated integrals by hand in most of the practical cases.

Regarding your secondary question. before I differentiate the function each time, I multiply the previous result first
with the dy/dt=f(y,t) and that is why the function has to be just once differentiable. I am sure if you do an example
 ODE dy/dt=y, you will very easily find out.

---

[← Previous](page_005.md) | [Index](index.md) | [Next →](page_007.md)
