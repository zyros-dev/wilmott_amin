# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 11 of 59** — Posts #501–#550

[← Previous](page_010.md) | [Index](index.md) | [Next →](page_012.md)

---

### #501 — Amin (Topic Author)
*March 15, 2017, 5:06 PM*

Since the original purpose of this thread was to solve the SDEs with the method of iterated integrals, I want to write a
few comments on the work I posted on this thread earlier. I had proposed a numerical method as in post 105 (It has small
error in quadratic variation term if I correctly recall). The idea of the method was to solve the probability
distribution of SDEs by dividing the initial density along the standard deviations of the normal density into small
subdivisions. The value of normal standard deviation units at the center of corresponding subdivision on normal density
was used to evolve the center of the subdivision for the distribution of SDEs. Later, the density of the SDE was
constructed by doing an appropriate change of variable between the density of normal and the density of SDE since
probability mass in corresponding subdivisions of normal density and SDE density must be the same. Here are some
observations.

1. SDEs can be evolved like ODEs but for particular value of corresponding standard deviation units on the normal
density. We have to use the iterated dz and dz, dt integrals using formulas I gave earlier in this thread.

2. I believe that accuracy using the method suggested in post 105(after accounting for small error on dt term) and later
posts would  be because I was taking the value of corresponding normal standard deviation units at the center of the
subdivision but the probability mass is defined by an integral over the subdivision. It would be far more accurate to
see how the ends of the SDE subdivisions are expanding/contracting and then calculate the probability mass using change
of variable. An analogy would be how accuracy changes when we numerically integrate using the single value at the center
of the integration grid versus when we integrate using the values of function at both ends. I was using the mid-point
version but we could just as easily use the ends and have more accuracy.

---

### #502 — outrun
*March 15, 2017, 6:28 PM*

A very straightforward way is to use the binomial Gaussian filter [https://www.researchgate.net/publicatio ... ure_filter](https://www.researchgate.net/publication/274954009_Binomial_Gaussian_mixture_filter)

.., and apply the unscented Kalman filter or sigma points

---

### #503 — Cuchulainn
*March 15, 2017, 11:40 PM*

> A very straightforward way is to use the binomial Gaussian filter [https://www.researchgate.net/publicatio ... ure_filter](https://www.researchgate.net/publication/274954009_Binomial_Gaussian_mixture_filter)
>
>
>
> .., and apply the unscented Kalman filter or sigma points
If this is the answer, what is the problem that it solves? I don't see any connection with Amin's ODE???

IMO Amin is still coming to terms with other unanswered issue relating to ODEs. He has not answered @amike's fundamental
question.

---

### #504 — outrun
*March 16, 2017, 8:52 AM*

> I don't see any connection with Amin's ODE???
>
>
>
> IMO Amin is still coming to terms with other unanswered issue relating to ODEs. He has not answered @amike's
fundamental question.
Yes he hasn't but he also wants to discuss stochastic things now. Don't expect him to answer questions that conflict
with his view of having breakthrough, you won't be able to chaise him through the corridor of rationality to your
abattoir.

From what I read in his post he's using a mesh-free particle type Gaussian mixture model and there has of course already
been done a lot in that area, ..hence my pointers. It will of course inherit all the ODE issues as well.

Amin, have you looked at polynomial chaos expansion methods?

---

### #505 — amike
*March 16, 2017, 11:31 AM*

> When I wrote my post and made comparison with multistep numerical methods, I was trying to say that you can use the
method even if you do not take enough series terms for the solution to converge(totally analytic solution will take
enough terms and just one step). Sometimes, you might have just a few terms and then the solution may not converge for
the terminal value of independent variable but in that special case, you can take smaller steps like we do in numerical
methods and numerically solve the ODE by taking more than one step.
Please try solving the system I posted and tell me how many terms in the series you need to solve the problem in a
single step.  It is a very simple problem and I believe that you have mathematica code that will allow you to try this
very quickly.

In order for your method to be use-able in practice the user will have to somehow be able to decide how many terms will
be required, or if a single step is not going to work then how the multi-step algorithm will work.

---

### #506 — Cuchulainn
*March 16, 2017, 2:20 PM*

> From what I read in his post he's using a mesh-free particle type Gaussian mixture model and there has of course
already been done a lot in that area, ..hence my pointers. It will of course inherit all the ODE issues as well.
>
>
Not really...  Wrong solution for the wrong problem. ODEs have *nothing* to do with meshfree IMO.  Meshless is primarily
for PDEs in n space variables and 1 time variable. Of course Gaussian radial functions can be used but that's just
coincidence.

For an accurate assessment, see amike's more recent post.

---

### #507 — Cuchulainn
*March 16, 2017, 2:34 PM*

*Amin, have you looked at polynomial chaos expansion methods?*

A bit-off topic.

I tried doing this but was not successful because it is a bit turgid and I could not get a goo example.

Is this post just out of curiosity or has it been done, really?

Just a simple GBM SDE as example and I will believe it.

---

### #508 — outrun
*March 16, 2017, 3:17 PM*

if you google you'll find many papers and slides.

(random first hit) [https://papers.ssrn.com/sol3/papers.cfm ... id=2143783](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2143783)

There a various direction Amin could take with SDE's. The drawback with the mixture method he described is that
approximating a Gaussian with smaller Gaussian is not very accurate when I did that in some project.

---

### #509 — Amin (Topic Author)
*March 19, 2017, 4:56 PM*

Sorry. Bad post.

---

### #510 — Amin (Topic Author)
*March 19, 2017, 5:20 PM*

Sorry. Bad post.

---

### #511 — Cuchulainn
*March 19, 2017, 8:11 PM*

.

---

### #512 — Paul
*March 19, 2017, 8:41 PM*

Amin, you are doing a "list." Any reputation you had is rapidly disappearing. My advice is to stop now, and take some
appropriate math courses.

---

### #513 — Cuchulainn
*March 19, 2017, 9:33 PM*

This MIT offerring looks good

[https://ocw.mit.edu/courses/mathematics ... /calendar/](https://ocw.mit.edu/courses/mathematics/18-152-introduction-to-partial-differential-equations-fall-2011/calendar/)

But i would do this first

[https://ocw.mit.edu/courses/mathematics ... -lectures/](https://ocw.mit.edu/courses/mathematics/18-03-differential-equations-spring-2010/video-lectures/)

And do the exercises/exam. The only way to walk the talk!

---

### #514 — Amin (Topic Author)
*March 20, 2017, 5:10 PM*

very very sorry. I confused dp with dp/dt. dp=0 at any given time while obviously dp/dt is not. I would request people
to know that under brain control, the brain control agencies continue to take neurotransmitters out of the brain that
occasionally results in such lapses. These agencies then ask their favorite pawns to start making fun of the target.
From my experience any such lapses are not permanent and my neurotransmitters always continued to come back. Yes it was
a lapse as Cuch and Paul suggested. I thank you both for pointing out the error.

---

### #515 — Cuchulainn
*March 20, 2017, 8:15 PM*

I don't agree. As we both say, you need to learn some mathematics. And you can't blame the CIA in this case.

*I confused dp with dp/dt. dp=0 at any given time while obviously dp/dt is not.*

This is not maths. This is like what kids learn in junior cert school.

**Serious question: which PDE books have you studied in the past? **Can you tell us that? And for how many years? In
judo, you can see how advanced someone is by belt colour. Are you white, yellow, orange, green, blue, brown or black
belt in PDE?

---

### #516 — Paul
*March 20, 2017, 8:22 PM*

I agree with Cuch. You have a very uneven understanding of mathematics. You don't even know where your gaps are. Take
some courses.

---

### #517 — Amin (Topic Author)
*March 21, 2017, 10:18 PM*

I will try to present a completely worked out solution for simple diffusion equation in a few days. The idea is very
simple. Write the dependent function in terms of integrals that depend on its arguments and then solve the integrals by
method of iterated integrals after substituting the PDE for time derivatives. Following is a brief sketch that might
change a bit in the final version. I copied the equations from a previous post and some notation might be slightly off.

In p(x,t) when we start from p(x_0,t_0)

We can write

$\zeta (x,t)=\zeta \left(x_0,t_0\right)+\int_{t_0}^t \frac{\partial }{\partial s}\zeta (x(s),s) \, ds+\int _{t_0}^t\frac{\partial }{\partial x}\zeta (x(s),s)\frac{\partial x}{\partial s}ds$

From integration by parts

$\int _{t_0}^t\frac{\partial }{\partial x}\zeta (x(s),s)\frac{\partial x}{\partial s}ds=x(t)\frac{\partial }{\partial x}\zeta (x(t),t)-x\left(t_0\right)\frac{\partial }{\partial x}\zeta \left(x\left(t_0\right),t_0\right)$

$-\int _{t_0}^tx(s)\frac{\partial }{\partial x}\left[\frac{\partial }{\partial s}\zeta (x(s),s)\right]ds$

I really believe that all terms and relevant integrals can be solved by the method of iterated integrals to get the
final solution as a two dimensional series. In order to be able to convince Cuch and Paul, I will give a completely
worked out numerical example so they can verify analytics with real numbers.

---

### #518 — Amin (Topic Author)
*March 22, 2017, 10:54 AM*

> I will try to present a completely worked out solution for simple diffusion equation in a few days. The idea is very
simple. Write the dependent function in terms of integrals that depend on its arguments and then solve the integrals by
method of iterated integrals after substituting the PDE for time derivatives. Following is a brief sketch that might
change a bit in the final version. I copied the equations from a previous post and some notation might be slightly off.
>
>
>
> In p(x,t) when we start from p(x_0,t_0)
>
> We can write
>
>
$\zeta (x,t)=\zeta \left(x_0,t_0\right)+\int_{t_0}^t \frac{\partial }{\partial s}\zeta (x(s),s) \, ds+\int _{t_0}^t\frac{\partial }{\partial x}\zeta (x(s),s)\frac{\partial x}{\partial s}ds$
>
> From integration by parts
>
>
$\int _{t_0}^t\frac{\partial }{\partial x}\zeta (x(s),s)\frac{\partial x}{\partial s}ds=x(t)\frac{\partial }{\partial x}\zeta (x(t),t)-x\left(t_0\right)\frac{\partial }{\partial x}\zeta \left(x\left(t_0\right),t_0\right)$
>
> $-\int _{t_0}^tx(s)\frac{\partial }{\partial x}\left[\frac{\partial }{\partial s}\zeta (x(s),s)\right]ds$
>
>
>
> I really believe that all terms and relevant integrals can be solved by the method of iterated integrals to get the
final solution as a two dimensional series. In order to be able to convince Cuch and Paul, I will give a completely
worked out numerical example so they can verify analytics with real numbers.
When we find an integral of a function of two variables of the sort we usually find in PDEs, the right expansion for the
terms inside the integral should be

$\zeta (x(s),s)=\zeta \left(x(t_0),s\right)+\int _{t_0}^s\frac{\partial }{\partial x}\zeta (x(u),s)\frac{\partial x}{\partial u}du$
Equation(1)

which can be further expanded as

$\zeta (x(s),s)=\zeta \left(x(t_0),t_0\right)+\int_{t_0}^s \frac{\partial }{\partial u}\zeta (x(t_0),u) \, du+\int _{t_0}^s\frac{\partial }{\partial x}\zeta (x(u),s)\frac{\partial x}{\partial u}du$
Equation (2)

We could in fact use this last equation (2) for the solution of first order odes but we preferred to use equation (1)
since it was far more convenient there. Obviously equation (2) and equation (1) are equivalent. In case of PDEs, we
would have to prefer to use equation (2) in most general cases. We would have to continue to further expand each
integrand term in terms of higher derivatives by representing the integrand in terms of time zero value(initial time)
and its derivatives just like we did in equation (1) or equation (2). we would also have to substitute actual PDE
wherever we encounter time derivatives. Sorry for slightly bad notation but partial derivatives should be replaced by
dx/du in equation(2).

Trying to quickly write the right version of last equation in previous post that I have quoted. From integration by
parts

$\int _{t_0}^s\frac{\partial }{\partial x}\zeta (x(u),s)\frac{\partial x}{\partial u}du=x(s)\frac{\partial }{\partial x}\zeta (x(s),s)-x\left(t_0\right)\frac{\partial }{\partial x}\zeta \left(x\left(t_0\right),s\right)$

$-\int _{t_0}^s x(u)\frac{\partial }{\partial x}\left[\frac{\partial }{\partial u}\zeta (x(u),s)\right]du$

In the final expansion solution all terms will be expanded until the the terms inside the integrals are in the form of
$\zeta (x(t_0),t_0)$ or its x derivatives at time t0 if x has dependence on t. If x does not have a dependence on t, the
solution could be easier.

---

### #519 — Amin (Topic Author)
*March 22, 2017, 3:09 PM*

Though I will soon follow with application to PDEs, I would recall what many friends were saying that many times it is
very difficult to analytically integrate the iterated integrals that arise when solving ODEs using the method I
presented in my paper which is based on equation 1 in previous post. In all such cases, we could use equation (2) and
calculate initial derivatives with respect to time at starting time t0 and then use only Taylor coefficients that will
follow from iterated integrals over constants. But it will increase computational complexity of the problem. I hope this
does help many applied mathematicians who want to apply this method towards more difficult but interesting applications.

---

### #520 — outrun
*March 22, 2017, 4:23 PM*

Many friends here at the forum and applied mathematicians  have asked some very simple question, but you are probably
being manipulated by brain agents to ignore those questions so that it looks like you are not able to answer them.

---

### #521 — Amin (Topic Author)
*March 22, 2017, 7:46 PM*

*outrun:*

Amin, have you looked at polynomial chaos expansion methods?

I do not know very much in detail about those methods. I do recall reading some papers a few years ago. I do think this
method is more natural.

---

### #522 — Cuchulainn
*April 2, 2017, 10:59 AM*

[Embedded Video]

accessible and precise treatment of PDE

---

### #523 — Amin (Topic Author)
*April 5, 2017, 4:03 PM*

> I will try to present a completely worked out solution for simple diffusion equation in a few days. The idea is very
simple. Write the dependent function in terms of integrals that depend on its arguments and then solve the integrals by
method of iterated integrals after substituting the PDE for time derivatives. Following is a brief sketch that might
change a bit in the final version. I copied the equations from a previous post and some notation might be slightly off.
>
>
>
> In p(x,t) when we start from p(x_0,t_0)
>
> We can write
>
>
$\zeta (x,t)=\zeta \left(x_0,t_0\right)+\int_{t_0}^t \frac{\partial }{\partial s}\zeta (x(s),s) \, ds+\int _{t_0}^t\frac{\partial }{\partial x}\zeta (x(s),s)\frac{\partial x}{\partial s}ds$
>
> From integration by parts
>
>
$\int _{t_0}^t\frac{\partial }{\partial x}\zeta (x(s),s)\frac{\partial x}{\partial s}ds=x(t)\frac{\partial }{\partial x}\zeta (x(t),t)-x\left(t_0\right)\frac{\partial }{\partial x}\zeta \left(x\left(t_0\right),t_0\right)$
>
> $-\int _{t_0}^tx(s)\frac{\partial }{\partial x}\left[\frac{\partial }{\partial s}\zeta (x(s),s)\right]ds$
>
>
>
> I really believe that all terms and relevant integrals can be solved by the method of iterated integrals to get the
final solution as a two dimensional series. In order to be able to convince Cuch and Paul, I will give a completely
worked out numerical example so they can verify analytics with real numbers.
When we find an integral of a function of two variables of the sort we usually find in PDEs, the right expansion for the
terms inside the integral should be

$\zeta (x(s),s)=\zeta \left(x(t_0),s\right)+\int _{t_0}^s\frac{\partial }{\partial x}\zeta (x(u),s)\frac{\partial x}{\partial u}du$
Equation(1)

which can be further expanded as

$\zeta (x(s),s)=\zeta \left(x(t_0),t_0\right)+\int_{t_0}^s \frac{\partial }{\partial u}\zeta (x(t_0),u) \, du+\int _{t_0}^s\frac{\partial }{\partial x}\zeta (x(u),s)\frac{\partial x}{\partial u}du$
Equation (2)

We could in fact use this last equation (2) for the solution of first order odes but we preferred to use equation (1)
since it was far more convenient there. Obviously equation (2) and equation (1) are equivalent. In case of PDEs, we
would have to prefer to use equation (2) in most general cases. We would have to continue to further expand each
integrand term in terms of higher derivatives by representing the integrand in terms of time zero value(initial time)
and its derivatives just like we did in equation (1) or equation (2). we would also have to substitute actual PDE
wherever we encounter time derivatives. Sorry for slightly bad notation but partial derivatives should be replaced by
dx/du in equation(2).

Trying to quickly write the right version of last equation in previous post that I have quoted. From integration by
parts

$\int _{t_0}^s\frac{\partial }{\partial x}\zeta (x(u),s)\frac{\partial x}{\partial u}du=x(s)\frac{\partial }{\partial x}\zeta (x(s),s)-x\left(t_0\right)\frac{\partial }{\partial x}\zeta \left(x\left(t_0\right),s\right)$

$-\int _{t_0}^s x(u)\frac{\partial }{\partial x}\left[\frac{\partial }{\partial u}\zeta (x(u),s)\right]du$

In the final expansion solution all terms will be expanded until the the terms inside the integrals are in the form of
$\zeta (x(t_0),t_0)$ or its x derivatives at time t0 if x has dependence on t. If x does not have a dependence on t, the
solution could be easier.
Sorry friends, I got carried away by a lot of other important things. Probably tomorrow or Friday, I will present a
detailed derivation of series solution of PDEs given a certain initial data distribution. I will repeatedly use equation
(2) in the quoted post above or its simpler equivalents until all the integrands terms are based only on initial data at
time t0 to get a two-dimensional Taylor like expansion. I will give a very detailed derivation. We will use the PDE to
convert time derivatives into space derivatives of initial data calculated at t0. The whole derivation is very simple
and straightforward. I will put all notes on next post here tomorrow or by Friday.

---

### #524 — Amin (Topic Author)
*April 6, 2017, 2:10 PM*

Given$\zeta(x(t_0),t_0)$ with a certain initial distribution of$x(t_0)$ , we want to find out the final solution which
can be formally written using Green's function inside an integral over the initial data.

$\zeta(x(t),t)=\int_{-\infty}^{\infty} \Phi(x(t),t,x(t_0),t_0) \zeta(x(t_0),t_0) dx(t_0)$  Equation(1)

We would like to recall that when initial data is a Dirac delta distribution, the green's function inside the integral
in Equation(1)and the LHS of Equation(1) will coincide. We try to find out the LHS of Equation(1) with Dirac delta
initial arguments and try to use it as a solution to Green's function for the particular PDE.

We write Equation(2) from the previous post as

$\zeta(x(t),t)=\zeta(x(t_0),t_0)+\int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds + \int_{x(t_0)}^{x(t)} \frac{\partial \zeta(x(s),t)}{\partial x} dx(s)$

Equation(2)

First trying to work with the 2nd term(or first integral) in the RHS of Equation(2), we get

$ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\

=\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial \zeta(x(t_0),u)}
{\partial u} du \big] ds $

Equation(3)

We notice that the integral inside large brackets in RHS of Equation (3) can similarly be further expanded many times to
give other versions of Equation(3) as

$ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\

=\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial \zeta(x(t_0),u)}
{\partial u} du \big] ds \\

=\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial \zeta(x(t_0),v)} {\partial v} dv \big] du \big] ds \\

=\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\

+ \int_{t_0}^{v} \frac {\partial \zeta(x(t_0),w)} {\partial w} dw \big] dv \big] du \big] ds$

Equation(4)

We can continue the expansions till higher orders and any symbolic computing program might actually want to expand
several tens of terms but here we stop and substitute$\int_{t_0}^{v} \frac {\partial \zeta(x(t_0),t_0)} {\partial w} dw$
for$\int_{t_0}^{v} \frac {\partial \zeta(x(t_0),w)} {\partial w} dw$ which is obviously an approximation and we get the
resulting approximate equation (We have chosen very few terms only so that we can calculate the integrals very easily to
show the simple ideas). We copy the first and last equation parts in Equation(4) in Equation(5) and then try to solve
the integrals in RHS of resulting equation (5) later.

$ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\

=\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\

+ \int_{t_0}^{v} \frac {\partial \zeta(x(t_0),t_0)} {\partial w} dw \big] dv \big] du \big] ds$

Equation(5)

Solving the integrals in above Equation (5) iteratively one by one we get the equations as

$ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\

=\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\

+ \int_{t_0}^{v} \frac {\partial \zeta(x(t_0),t_0)} {\partial w} dw \big] dv \big] du \big] ds \\

=\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\

+ \frac {\partial \zeta(x(t_0),t_0)} {\partial v} |^{v=t_0} (v-t_0) \big]  dv \big] du \big] ds \\

=\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \frac {\partial \zeta(x(t_0),t_0)} {\partial u} |^{u=t_0} (u-t_0) \\

+ \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial u^2} |^{u=t_0} \frac{(u-t_0)^2}{2} \big] du \big] ds \\

=\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \frac {\partial \zeta(x(t_0),t_0)} {\partial
s} |^{s=t_0} (s-t_0) + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial s^2} |^{s=t_0} \frac{(s-t_0)^2}{2} \\

+\frac {\partial^3 \zeta(x(t_0),t_0)} {\partial s^3} |^{s=t_0} \frac{(s-t_0)^3}{6} \big]  ds \\

= \frac{\partial \zeta(x(t_0),t_0)}{\partial t} |^{t=t_0} (t-t_0) + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial
t^2} |^{t=t_0} \frac{(t-t_0)^2}{2} \\

+ \frac {\partial^3 \zeta(x(t_0),t_0)} {\partial t^3} |^{t=t_0} \frac{(t-t_0)^3}{6} + \frac {\partial^4
\zeta(x(t_0),t_0)} {\partial t^4} |^{t=t_0} \frac{(t-t_0)^4}{24}$

Equation(6)

In the above I used product rule for derivatives with the fact that $(s-t_0)=0$ when $s=t_0$

Suppose we are given a PDE as

$\frac {\partial \zeta} {\partial t} = a \frac{ \partial^2 \zeta}{\partial x^2} + b \frac{ \partial \zeta}{\partial x} + c \zeta$

We can use the following formulas in the expansion of Equation(6) and other expansions.

$\frac {\partial \zeta(x(t_0),t_0)} {\partial t} = a \frac{ \partial^2 \zeta(x(t_0),t_0)}{\partial x^2} + b \frac{ \partial \zeta(x(t_0),t_0)}{\partial x} + c \zeta(x(t_0),t_0)$

and

$\frac {\partial^2 \zeta(x(t_0),t_0)} {\partial t^2} = (a \frac{ \partial^2}{\partial x^2} + b \frac{ \partial}{\partial x} + c)^2 [\zeta(x(t_0),t_0)]$

and

$\frac {\partial^n \zeta(x(t_0),t_0)} {\partial t^n} = (a \frac{ \partial^2}{\partial x^2} + b \frac{ \partial}{\partial x} + c)^n [\zeta(x(t_0),t_0)]$

In the above attempt at explanation I have only expanded the first integral in Equation(2), the expansion for second
integral(or third term) in Equation(2) though very similar but a little bit more tedious. I will write that in detail
tomorrow and complete the solution expansion and then try to follow with numerical examples over the weekend.

---

### #525 — Amin (Topic Author)
*April 8, 2017, 2:45 PM*

> Given$\zeta(x(t_0),t_0)$ with a certain initial distribution of$x(t_0)$ , we want to find out the final solution which
can be formally written using Green's function inside an integral over the initial data.
>
>
>
> $\zeta(x(t),t)=\int_{-\infty}^{\infty} \Phi(x(t),t,x(t_0),t_0) \zeta(x(t_0),t_0) dx(t_0)$  Equation(1)
>
>
>
> We would like to recall that when initial data is a Dirac delta distribution, the green's function inside the integral
in Equation(1)and the LHS of Equation(1) will coincide. We try to find out the LHS of Equation(1) with Dirac delta
initial arguments and try to use it as a solution to Green's function for the particular PDE.
>
>
>
> We write Equation(2) from the previous post as
>
>
>
>
$\zeta(x(t),t)=\zeta(x(t_0),t_0)+\int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds + \int_{x(t_0)}^{x(t)} \frac{\partial \zeta(x(s),t)}{\partial x} dx(s)$
>
> Equation(2)
>
> First trying to work with the 2nd term(or first integral) in the RHS of Equation(2), we get
>
> $ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial \zeta(x(t_0),u)}
{\partial u} du \big] ds $
>
> Equation(3)
>
> We notice that the integral inside large brackets in RHS of Equation (3) can similarly be further expanded many times
to give other versions of Equation(3) as
>
> $ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial \zeta(x(t_0),u)}
{\partial u} du \big] ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial \zeta(x(t_0),v)} {\partial v} dv \big] du \big] ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\
>
> + \int_{t_0}^{v} \frac {\partial \zeta(x(t_0),w)} {\partial w} dw \big] dv \big] du \big] ds$
>
> Equation(4)
>
>
>
> We can continue the expansions till higher orders and any symbolic computing program might actually want to expand
several tens of terms but here we stop and substitute$\int_{t_0}^{v} \frac {\partial \zeta(x(t_0),t_0)} {\partial w} dw$
for$\int_{t_0}^{v} \frac {\partial \zeta(x(t_0),w)} {\partial w} dw$ which is obviously an approximation and we get the
resulting approximate equation (We have chosen very few terms only so that we can calculate the integrals very easily to
show the simple ideas). We copy the first and last equation parts in Equation(4) in Equation(5) and then try to solve
the integrals in RHS of resulting equation (5) later.
>
>
>
> $ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\
>
> + \int_{t_0}^{v} \frac {\partial \zeta(x(t_0),t_0)} {\partial w} dw \big] dv \big] du \big] ds$
>
> Equation(5)
>
>
>
> Solving the integrals in above Equation (5) iteratively one by one we get the equations as
>
> $ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\
>
> + \int_{t_0}^{v} \frac {\partial \zeta(x(t_0),t_0)} {\partial w} dw \big] dv \big] du \big] ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\
>
> + \frac {\partial \zeta(x(t_0),t_0)} {\partial v} |^{v=t_0} (v-t_0) \big]  dv \big] du \big] ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \frac {\partial \zeta(x(t_0),t_0)} {\partial u} |^{u=t_0} (u-t_0) \\
>
> + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial u^2} |^{u=t_0} \frac{(u-t_0)^2}{2} \big] du \big] ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \frac {\partial \zeta(x(t_0),t_0)} {\partial
s} |^{s=t_0} (s-t_0) + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial s^2} |^{s=t_0} \frac{(s-t_0)^2}{2} \\
>
> +\frac {\partial^3 \zeta(x(t_0),t_0)} {\partial s^3} |^{s=t_0} \frac{(s-t_0)^3}{6} \big]  ds \\
>
> = \frac{\partial \zeta(x(t_0),t_0)}{\partial t} |^{t=t_0} (t-t_0) + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial
t^2} |^{t=t_0} \frac{(t-t_0)^2}{2} \\
>
> + \frac {\partial^3 \zeta(x(t_0),t_0)} {\partial t^3} |^{t=t_0} \frac{(t-t_0)^3}{6} + \frac {\partial^4
\zeta(x(t_0),t_0)} {\partial t^4} |^{t=t_0} \frac{(t-t_0)^4}{24}$
>
> Equation(6)
>
> In the above I used product rule for derivatives with the fact that $(s-t_0)=0$ when $s=t_0$
>
> Suppose we are given a PDE as
>
>
$\frac {\partial \zeta} {\partial t} = a \frac{ \partial^2 \zeta}{\partial x^2} + b \frac{ \partial \zeta}{\partial x} + c \zeta$
>
> We can use the following formulas in the expansion of Equation(6) and other expansions.
>
>
$\frac {\partial \zeta(x(t_0),t_0)} {\partial t} = a \frac{ \partial^2 \zeta(x(t_0),t_0)}{\partial x^2} + b \frac{ \partial \zeta(x(t_0),t_0)}{\partial x} + c \zeta(x(t_0),t_0)$
>
> and
>
>
$\frac {\partial^2 \zeta(x(t_0),t_0)} {\partial t^2} = (a \frac{ \partial^2}{\partial x^2} + b \frac{ \partial}{\partial x} + c)^2 [\zeta(x(t_0),t_0)]$
>
> and
>
>
$\frac {\partial^n \zeta(x(t_0),t_0)} {\partial t^n} = (a \frac{ \partial^2}{\partial x^2} + b \frac{ \partial}{\partial x} + c)^n [\zeta(x(t_0),t_0)]$
>
>
>
> In the above attempt at explanation I have only expanded the first integral in Equation(2), the expansion for second
integral(or third term) in Equation(2) though very similar but a little bit more tedious. I will write that in detail
tomorrow and complete the solution expansion and then try to follow with numerical examples over the weekend.
We again write Equation(2) from the previous posts as

$\zeta(x(t),t)=\zeta(x(t_0),t_0)+\int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds + \int_{x(t_0)}^{x(t)} \frac{\partial \zeta(x(s),t)}{\partial x} dx(s)$

Equation(2)

and try to solve the second integral.

$\int_{x(t_0)}^{x(t)} \frac{\partial \zeta(x(s),t)}{\partial x} dx(s)$

$=\int_{x(t_0)}^{x(t)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),s)}{\partial s} ds \\

+ \int_{x(t_0)}^{x(s)} \frac {\partial \zeta(x(u),t)}{\partial x} dx(u) \big ] dx(s)$

$=\int_{x(t_0)}^{x(t)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),s)}{\partial s} ds \\

+ \int_{x(t_0)}^{x(s)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),u)}{\partial u} du \\

+ \int_{x(t_0)}^{x(u)} \frac {\partial \zeta(x(v),t)}{\partial x} dx(v) \big ] dx(u) \big ] dx(s)$

$=\int_{x(t_0)}^{x(t)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),s)}{\partial s} ds \\

+ \int_{x(t_0)}^{x(s)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),u)}{\partial u} du \\

+ \int_{x(t_0)}^{x(u)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),v)}{\partial v} dv \\

+ \int_{x(t_0)}^{x(v)} \frac {\partial \zeta(x(w),t)}{\partial x} dx(w) \big ] dx(v) \big ] dx(u) \big ] dx(s)$

Equation (8)

We can divide the above series into two series so that integrals in each series are similar as

Series (1) is given as

$=\int_{x(t_0)}^{x(t)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{x(t_0)}^{x(s)}
\frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) \\

+ \int_{x(t_0)}^{x(u)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{x(t_0)}^{x(v)}
\frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \dots \big ] dx(w) \big ] dx(v) \big ] dx(u) \big ] dx(s) $

Equation (9)

While series (2) is given as

$\int_{x(t_0)}^{x(t)} \frac{\partial}{\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds
+ \int_{x(t_0)}^{x(s)} \frac{\partial}{\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),u)}{\partial u} du
\\

+ \int_{x(t_0)}^{x(u)} \frac{\partial}{\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),v)}{\partial v} dv
+ \int_{x(t_0)}^{x(v)} \frac{\partial}{\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),w)}{\partial w} dw
+ \dots \big ] dx(w) \big ] dx(v) \big ] dx(u) \big ] dx(s) $

Equation(10)

Series (1) is solved and results in a simple Taylor series solution in one dimension as we found for time integrals in
the previous posts and the solution is given as

$= \frac {\partial \zeta(x(t_0),t_0)} {\partial x} (x(t)-x(t_0)) + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial x^2}
\frac {(x(t)-x(t_0))^2}{2} \\

+ \frac {\partial^3 \zeta(x(t_0),t_0)} {\partial x^3} \frac {(x(t)-x(t_0))^3}{6} + \frac {\partial^4 \zeta(x(t_0),t_0)}
{\partial x^4} \frac {(x(t)-x(t_0))^4}{24} + \dots $

Equation (11)

while the solution to series (2) is given as

$= \frac {\partial} {\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds \big ]
(x(t)-x(t_0)) + \frac {\partial^2} {\partial x^2} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds
\big ] \frac {(x(t)-x(t_0))^2}{2} \\

+ \frac {\partial^3 } {\partial x^3} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds \big ] \frac
{(x(t)-x(t_0))^3}{6} + \frac {\partial^4} {\partial x^4} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial
s} ds \big ] \frac {(x(t)-x(t_0))^4}{24} + \dots $

Equation (12)

where solution to each of the time integrals inside large brackets in the above equation is given by expansion in
Equation (6) of previous post and this series would correspond to cross derivatives in two dimensional Taylor series.

---

### #526 — Amin (Topic Author)
*May 2, 2017, 1:37 PM*

I made a related post on a different thread about how to represent Taylor series weights of a function into Legendre polynomial weights and then convert Legendre polynomial weights into some other orthogonal polynomial weights. Here is the new thread. [Taylor Series, Legendre Polynomials and Change of Orthogonal Polynomials/Basis](https://forum.wilmott.com/viewtopic.php?f=4&t=100713)

Please contribute to discussion on that new thread.

---

### #527 — Amin (Topic Author)
*May 2, 2017, 1:55 PM*

I will soon be following with Sage Math programs for analytical solution of PDEs. Hard drive of a computer failed and
some mathematical programs were deleted that is why I stayed away from posting earlier. Sometimes I had to do
calculations with calculator.

---

### #528 — Amin (Topic Author)
*May 5, 2017, 11:57 AM*

> Given$\zeta(x(t_0),t_0)$ with a certain initial distribution of$x(t_0)$ , we want to find out the final solution which
can be formally written using Green's function inside an integral over the initial data.
>
>
>
> $\zeta(x(t),t)=\int_{-\infty}^{\infty} \Phi(x(t),t,x(t_0),t_0) \zeta(x(t_0),t_0) dx(t_0)$  Equation(1)
>
>
>
> We would like to recall that when initial data is a Dirac delta distribution, the green's function inside the integral
in Equation(1)and the LHS of Equation(1) will coincide. We try to find out the LHS of Equation(1) with Dirac delta
initial arguments and try to use it as a solution to Green's function for the particular PDE.
>
>
>
> We write Equation(2) from the previous post as
>
>
>
>
$\zeta(x(t),t)=\zeta(x(t_0),t_0)+\int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds + \int_{x(t_0)}^{x(t)} \frac{\partial \zeta(x(s),t)}{\partial x} dx(s)$
>
> Equation(2)
>
> First trying to work with the 2nd term(or first integral) in the RHS of Equation(2), we get
>
> $ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial \zeta(x(t_0),u)}
{\partial u} du \big] ds $
>
> Equation(3)
>
> We notice that the integral inside large brackets in RHS of Equation (3) can similarly be further expanded many times
to give other versions of Equation(3) as
>
> $ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial \zeta(x(t_0),u)}
{\partial u} du \big] ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial \zeta(x(t_0),v)} {\partial v} dv \big] du \big] ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\
>
> + \int_{t_0}^{v} \frac {\partial \zeta(x(t_0),w)} {\partial w} dw \big] dv \big] du \big] ds$
>
> Equation(4)
>
>
>
> We can continue the expansions till higher orders and any symbolic computing program might actually want to expand
several tens of terms but here we stop and substitute$\int_{t_0}^{v} \frac {\partial \zeta(x(t_0),t_0)} {\partial w} dw$
for$\int_{t_0}^{v} \frac {\partial \zeta(x(t_0),w)} {\partial w} dw$ which is obviously an approximation and we get the
resulting approximate equation (We have chosen very few terms only so that we can calculate the integrals very easily to
show the simple ideas). We copy the first and last equation parts in Equation(4) in Equation(5) and then try to solve
the integrals in RHS of resulting equation (5) later.
>
>
>
> $ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\
>
> + \int_{t_0}^{v} \frac {\partial \zeta(x(t_0),t_0)} {\partial w} dw \big] dv \big] du \big] ds$
>
> Equation(5)
>
>
>
> Solving the integrals in above Equation (5) iteratively one by one we get the equations as
>
> $ \int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\
>
> + \int_{t_0}^{v} \frac {\partial \zeta(x(t_0),t_0)} {\partial w} dw \big] dv \big] du \big] ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \int_{t_0}^{u} \frac {\partial} {\partial v} \big[ \zeta(x(t_0),t_0) \\
>
> + \frac {\partial \zeta(x(t_0),t_0)} {\partial v} |^{v=t_0} (v-t_0) \big]  dv \big] du \big] ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \int_{t_0}^{s} \frac {\partial } {\partial u}
\big[ \zeta(x(t_0),t_0) + \frac {\partial \zeta(x(t_0),t_0)} {\partial u} |^{u=t_0} (u-t_0) \\
>
> + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial u^2} |^{u=t_0} \frac{(u-t_0)^2}{2} \big] du \big] ds \\
>
> =\int_{t_0}^{t} \frac{\partial}{\partial s} \big[ \zeta(x(t_0),t_0) + \frac {\partial \zeta(x(t_0),t_0)} {\partial
s} |^{s=t_0} (s-t_0) + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial s^2} |^{s=t_0} \frac{(s-t_0)^2}{2} \\
>
> +\frac {\partial^3 \zeta(x(t_0),t_0)} {\partial s^3} |^{s=t_0} \frac{(s-t_0)^3}{6} \big]  ds \\
>
> = \frac{\partial \zeta(x(t_0),t_0)}{\partial t} |^{t=t_0} (t-t_0) + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial
t^2} |^{t=t_0} \frac{(t-t_0)^2}{2} \\
>
> + \frac {\partial^3 \zeta(x(t_0),t_0)} {\partial t^3} |^{t=t_0} \frac{(t-t_0)^3}{6} + \frac {\partial^4
\zeta(x(t_0),t_0)} {\partial t^4} |^{t=t_0} \frac{(t-t_0)^4}{24}$
>
> Equation(6)
>
> In the above I used product rule for derivatives with the fact that $(s-t_0)=0$ when $s=t_0$
>
> Suppose we are given a PDE as
>
>
$\frac {\partial \zeta} {\partial t} = a \frac{ \partial^2 \zeta}{\partial x^2} + b \frac{ \partial \zeta}{\partial x} + c \zeta$
>
> We can use the following formulas in the expansion of Equation(6) and other expansions.
>
>
$\frac {\partial \zeta(x(t_0),t_0)} {\partial t} = a \frac{ \partial^2 \zeta(x(t_0),t_0)}{\partial x^2} + b \frac{ \partial \zeta(x(t_0),t_0)}{\partial x} + c \zeta(x(t_0),t_0)$
>
> and
>
>
$\frac {\partial^2 \zeta(x(t_0),t_0)} {\partial t^2} = (a \frac{ \partial^2}{\partial x^2} + b \frac{ \partial}{\partial x} + c)^2 [\zeta(x(t_0),t_0)]$
>
> and
>
>
$\frac {\partial^n \zeta(x(t_0),t_0)} {\partial t^n} = (a \frac{ \partial^2}{\partial x^2} + b \frac{ \partial}{\partial x} + c)^n [\zeta(x(t_0),t_0)]$
>
>
>
> In the above attempt at explanation I have only expanded the first integral in Equation(2), the expansion for second
integral(or third term) in Equation(2) though very similar but a little bit more tedious. I will write that in detail
tomorrow and complete the solution expansion and then try to follow with numerical examples over the weekend.
We again write Equation(2) from the previous posts as

$\zeta(x(t),t)=\zeta(x(t_0),t_0)+\int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds + \int_{x(t_0)}^{x(t)} \frac{\partial \zeta(x(s),t)}{\partial x} dx(s)$

Equation(2)

and try to solve the second integral.

$\int_{x(t_0)}^{x(t)} \frac{\partial \zeta(x(s),t)}{\partial x} dx(s)$

$=\int_{x(t_0)}^{x(t)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),s)}{\partial s} ds \\

+ \int_{x(t_0)}^{x(s)} \frac {\partial \zeta(x(u),t)}{\partial x} dx(u) \big ] dx(s)$

$=\int_{x(t_0)}^{x(t)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),s)}{\partial s} ds \\

+ \int_{x(t_0)}^{x(s)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),u)}{\partial u} du \\

+ \int_{x(t_0)}^{x(u)} \frac {\partial \zeta(x(v),t)}{\partial x} dx(v) \big ] dx(u) \big ] dx(s)$

$=\int_{x(t_0)}^{x(t)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),s)}{\partial s} ds \\

+ \int_{x(t_0)}^{x(s)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),u)}{\partial u} du \\

+ \int_{x(t_0)}^{x(u)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),v)}{\partial v} dv \\

+ \int_{x(t_0)}^{x(v)} \frac {\partial \zeta(x(w),t)}{\partial x} dx(w) \big ] dx(v) \big ] dx(u) \big ] dx(s)$

Equation (8)

We can divide the above series into two series so that integrals in each series are similar as

Series (1) is given as

$=\int_{x(t_0)}^{x(t)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{x(t_0)}^{x(s)}
\frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) \\

+ \int_{x(t_0)}^{x(u)} \frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \int_{x(t_0)}^{x(v)}
\frac{\partial}{\partial x} \big [ \zeta(x(t_0),t_0) + \dots \big ] dx(w) \big ] dx(v) \big ] dx(u) \big ] dx(s) $

Equation (9)

While series (2) is given as

$\int_{x(t_0)}^{x(t)} \frac{\partial}{\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds
+ \int_{x(t_0)}^{x(s)} \frac{\partial}{\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),u)}{\partial u} du
\\

+ \int_{x(t_0)}^{x(u)} \frac{\partial}{\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),v)}{\partial v} dv
+ \int_{x(t_0)}^{x(v)} \frac{\partial}{\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),w)}{\partial w} dw
+ \dots \big ] dx(w) \big ] dx(v) \big ] dx(u) \big ] dx(s) $

Equation(10)

Series (1) is solved and results in a simple Taylor series solution in one dimension as we found for time integrals in
the previous posts and the solution is given as

$= \frac {\partial \zeta(x(t_0),t_0)} {\partial x} (x(t)-x(t_0)) + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial x^2}
\frac {(x(t)-x(t_0))^2}{2} \\

+ \frac {\partial^3 \zeta(x(t_0),t_0)} {\partial x^3} \frac {(x(t)-x(t_0))^3}{6} + \frac {\partial^4 \zeta(x(t_0),t_0)}
{\partial x^4} \frac {(x(t)-x(t_0))^4}{24} + \dots $

Equation (11)

while the solution to series (2) is given as

$= \frac {\partial} {\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds \big ]
(x(t)-x(t_0)) + \frac {\partial^2} {\partial x^2} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds
\big ] \frac {(x(t)-x(t_0))^2}{2} \\

+ \frac {\partial^3 } {\partial x^3} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds \big ] \frac
{(x(t)-x(t_0))^3}{6} + \frac {\partial^4} {\partial x^4} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial
s} ds \big ] \frac {(x(t)-x(t_0))^4}{24} + \dots $

Equation (12)

where solution to each of the time integrals inside large brackets in the above equation is given by expansion in
Equation (6) of previous post and this series would correspond to cross derivatives in two dimensional Taylor series.

Sorry, though my previous two post had very valid derivations and my original suggestion, to use the actual PDE to
convert partial derivatives w.r.t time into partial derivatives w.r.t space as given in initial data, was crucial for
the analytic series solution of the PDE, I had made the following erroneous statement which I have edited and corrected
in the earlier post. The erroneous statement is given as

> Given$\zeta(x(t_0),t_0)$ with a certain initial distribution of$x(t_0)$ , we want to find out the final solution which
can be formally written using Green's function inside an integral over the initial data.
>
>
>
> $\zeta(x(t),t)=\int_{-\infty}^{\infty} \Phi(x(t),t,x(t_0),t_0) \zeta(x(t_0),t_0) dx(t_0)$  Equation(1)
>
>
>
> We would like to recall that when initial data is a Dirac delta distribution, the green's function inside the integral
in Equation(1)and the LHS of Equation(1) will coincide. We try to find out the LHS of Equation(1) with Dirac delta
initial arguments and try to use it as a solution to Green's function for the particular PDE.
>
instead the true statement should be written as

> Given the solution$\zeta(x(t_0),t_0)$ at initial point$(x(t_0),t_0)$ , we can find the solution$\zeta(x(t),t)$ at any
other neighboring point$(x(t),t)$ as a solution to the integral equation below
>
>
$\zeta(x(t),t)=\zeta(x(t_0),t_0)+\int_{t_0}^{t} \frac{\partial \zeta(x(t_0),s)}{\partial s} ds + \int_{x(t_0)}^{x(t)} \frac{\partial \zeta(x(s),t)}{\partial x} dx(s)$
>
> Equation(2)
>
> As we discussed in previous two posts, the solution is given in terms of two dimensional Taylor series around the
initial point where we have substituted the initial derivatives w.r.t time by initial space derivatives at initial point
$(x(t_0),t_0)$ using the PDE itself for this substitution. Thus, we only need information about the space derivatives.
>
>
>
> $\zeta(x(t),t)=\zeta(x(t_0),t_0)+ \frac{\partial \zeta(x(t_0),t_0)}{\partial t} (t-t_0) + \frac {\partial^2
\zeta(x(t_0),t_0)} {\partial t^2} \frac{(t-t_0)^2}{2} \\
>
> + \frac {\partial^3 \zeta(x(t_0),t_0)} {\partial t^3} \frac{(t-t_0)^3}{6} + \frac {\partial^4 \zeta(x(t_0),t_0)}
{\partial t^4} \frac{(t-t_0)^4}{24}+ \dots \\
>
> +\frac {\partial \zeta(x(t_0),t_0)} {\partial x} (x(t)-x(t_0)) + \frac {\partial^2 \zeta(x(t_0),t_0)} {\partial x^2}
\frac {(x(t)-x(t_0))^2}{2} \\
>
> + \frac {\partial^3 \zeta(x(t_0),t_0)} {\partial x^3} \frac {(x(t)-x(t_0))^3}{6} + \frac {\partial^4
\zeta(x(t_0),t_0)} {\partial x^4} \frac {(x(t)-x(t_0))^4}{24} + \dots \\
>
> + \frac {\partial} {\partial x} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds \big ]
(x(t)-x(t_0)) + \frac {\partial^2} {\partial x^2} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds
\big ] \frac {(x(t)-x(t_0))^2}{2} \\
>
> + \frac {\partial^3 } {\partial x^3} \big [ \int_{t_0}^{t} \frac {\partial \zeta(x(t_0),s)}{\partial s} ds \big ]
\frac {(x(t)-x(t_0))^3}{6} + \frac {\partial^4} {\partial x^4} \big [ \int_{t_0}^{t} \frac {\partial
\zeta(x(t_0),s)}{\partial s} ds \big ] \frac {(x(t)-x(t_0))^4}{24} + \dots$
>
>
>
> which can easily be seen to be equivalent (but more general since it is an equivalent in the form of integrals that
can be handy for so many applications)to two dimensional Taylor Series. We also use the following formula from the
previous posts.
>
>
$\frac {\partial^n \zeta(x(t_0),t_0)} {\partial t^n} = (a \frac{ \partial^2}{\partial x^2} + b \frac{ \partial}{\partial x} + c)^n [\zeta(x(t_0),t_0)]$
>
> which again makes use of the  following general time dependent PDE.
>
>
$\frac {\partial \zeta} {\partial t} = a \frac{ \partial^2 \zeta}{\partial x^2} + b \frac{ \partial \zeta}{\partial x} + c \zeta$
>
We try to present an initial easier example for calculation of solution of simple Brownian motion diffusion partial
differential equation (heat equation). For the sake of ease we take an "initial data" distribution of Brownian motion at
time$t=t_0$ and$x(t_0)=mu$ given as$\frac {1}{\sigma \sqrt{2 \pi t}} e^{-.5 (\frac {(x(t_0)-mu)}{\sigma \sqrt{t}})^2}$

In our first initial example, we try to calculate the solution at$t=t_1$ while keeping$x(t_1)$ constant at
$x(t_1)=x(t_0)=mu$ This helps since all the original space derivatives terms in the Taylor series go to zero (as
$(x(t)-\mu)^n=0$ and we are left with the opportunity to check how the expansion will behave when we substitute the
diffusion PDE for the derivatives w.r.t time in order to transform derivatives w.r.t time into derivatives w.r.t x(space
derivatives) which was the original premise that allowed us to use Taylor(or iterated integrals) expansion for
calculation of series solution. Once we have verified our method for this very basic toy example, we will solve the
diffusion PDE with completely general arguments and then move on to other more difficult PDEs.

We write the original PDE as

$\frac {\partial \zeta}{\partial t}=.5 \sigma^2 \frac {\partial^2 \zeta}{\partial x^2}$

The initial data distribution is assumed to be at time$t=t_0$ given as
$\frac {1}{\sigma \sqrt{2 \pi t}} e^{-.5 (\frac {(x(t_0)-mu)}{\sigma \sqrt{t}})^2}$

Since in our initial toy example, we have chosen$x(t_1)=x(t_0)=\mu$ , well known analytic solution to heat equation in
our case gives us

$\zeta(x(t_1),t_1)=\frac {1}{\sigma \sqrt{2 \pi t}} e^{-.5 (\frac {(x(t_0)-mu)}{\sigma \sqrt{t}})^2} \\

=\frac {1}{\sigma \sqrt{2 \pi t}}$

Since our solution method will give us a series expansion solution using equation (2) and equation (6) of post#  and
later using the last equations of the same post #  that help us substitute space derivatives for time derivatives. We
follow this as our method for calculation of the series solution. To check whether our method is right, we will find the
numerical solution from analytic solution of arithmetic Brownian motion and see whether both results match.

 Method 1:

We write the Taylor/iterated integrals expansion of the solution of heat equation at$(t_1,x(t_1))=(t_1),\mu)$ given the
solution of heat at PDE initial point$(t_0,x(t_0))=(t_0,\mu)$ as

$ \zeta(x(t_1),t_1)= \zeta(x(t_0),t_0)+ \frac{\partial \zeta(x(t_0),t_0)}{\partial t} (t-t_0) + \frac {\partial^2
\zeta(x(t_0),t_0)} {\partial t^2} \frac{(t-t_0)^2}{2} \\

+ \frac {\partial^3 \zeta(x(t_0),t_0)} {\partial t^3} \frac{(t-t_0)^3}{6} + \frac {\partial^4 \zeta(x(t_0),t_0)}
{\partial t^4} \frac{(t-t_0)^4}{24}+ \dots$

This follows because all$x(t_1)-x(t_0)$ terms vanish as$x(t_1)=x(t_0)= \mu$ and so all original x_derivatives and cross
derivatives terms vanish and we are left with time derivatives terms.

using the PDE () and specifying$x(t_0)=\mu$ and$x(t_1)=\mu$ we can write the above equation in terms of space
derivatives of initial data as

$\zeta(\mu,t_1)= \zeta(\mu,t_0)+ .5 \sigma^2 \frac{\partial^2 \zeta(\mu,t_0)}{\partial x^2} (t-t_0) + (.5 \sigma^2)^2
\frac{\partial^4 \zeta(\mu,t_0)}{\partial x^4} \frac{(t-t_0)^2}{2} \\

+ (.5 \sigma^2)^3 \frac{\partial^6 \zeta(\mu,t_0)}{\partial x^6} \frac{(t-t_0)^3}{6} + (.5 \sigma^2)^4 \frac{\partial^8
\zeta(\mu,t_0)}{\partial x^8} \frac{(t-t_0)^4}{24}+ \dots$

---

### #529 — Amin (Topic Author)
*May 5, 2017, 12:04 PM*

Sorry friends, the above post is the draft I saved on Wilmott for posting on this thread. It was last edited on April
20, 2017, 7:25 A.M according to Wilmott clock. I thought I had posted it and when I was looking at the thread today, I
realized, I had not done that. Basically the post is meant to clear the wrong statement that we would be finding out
Green's function. Instead, we just expand the PDE solution as Taylor/iterated integrals directly just like I had
mentioned but not for Green's function and expansion technique mentioned works directly for the PDE solution instead. It
does work and I would be posting a few programs for solution of several PDE classes using symbolic computing program
Sage Math.

---

### #530 — amike
*May 6, 2017, 2:23 PM*

> ...
>
> We give another general simulation expansion as
$\int _0^t z(s)\sigma\text{dz}(s)=\frac{2.5}{\sqrt{2\text{Pi}}}z(0)\sigma \sqrt{t}N(0,1) +.5\frac{2.5}{\sqrt{2\text{Pi}}}\sigma ^2t\text{  }N(0,1)^2-.5\sigma ^2t $
The above simulation for the stochastic integral is valid for any length of time...
This is a curious statement since the `exact' solution of this is quite well known (Kloeden+Platen, "numerical solutions
to stochastic differential equations", first edition, page 79, eqn (1.17)):

$\int _0^t z(s)\sigma dz(s)=\frac{\sigma}{2}(z(t)^2-t) $

(oops, small typo corrected...)

---

### #531 — Cuchulainn
*May 6, 2017, 7:59 PM*

.

---

### #532 — amike
*May 6, 2017, 8:14 PM*

... the fact that the left side is linear in sigma and the right has mysteriously picked up sigma^2 terms should be
enough to conclude something.   :)

---

### #533 — Amin (Topic Author)
*May 7, 2017, 12:39 PM*

> ...
>
> We give another general simulation expansion as
$\int _0^t z(s)\sigma\text{dz}(s)=\frac{2.5}{\sqrt{2\text{Pi}}}z(0)\sigma \sqrt{t}N(0,1) +.5\frac{2.5}{\sqrt{2\text{Pi}}}\sigma ^2t\text{  }N(0,1)^2-.5\sigma ^2t $
The above simulation for the stochastic integral is valid for any length of time...
This is a curious statement since the `exact' solution of this is quite well known (Kloeden+Platen, "numerical solutions
to stochastic differential equations", first edition, page 79, eqn (1.17)):

$\int _0^t z(s)\sigma dz(s)=\frac{\sigma}{2}(z(t)^2-t) $

(oops, small typo corrected...)

When I first presented the idea, I just knew that I would have to solve these iterated stochastic integrals in order to
present a complete numerical method. As a start, I went to matlab and ran a few simulations and some initial results
might have mistakes. But I presented definitive answers in this post 32 made a few days later.
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
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}=H_1(N)\frac{\sigma\text{t}^{1.5}}{\sqrt{1!}\sqrt{3}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)=H_2(N)\frac{\sigma ^2t}{\sqrt{2!}\sqrt{2}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\sigma\text{dz}(v)=\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\sigma\text{dz}(u)\int _0^u\sigma\text{dz}(v)=H_2(N)\frac{\sigma ^2t^2}{\sqrt{2!}\sqrt{12}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\text{du}\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\sigma\text{dz}(u)\int _0^u\text{dv}=\int _0^t \text{ds}\int _0^s\text{du}\int _0^u\sigma\text{dz}(v)=H_1(N)\frac{\sigma ^2t^{2.5}}{\sqrt{1!}\sqrt{20}}$
$\int _0^t \sigma\text{dz}(s)\int _0^s\sigma\text{dz}(u)\int _0^u\sigma\text{dz}(v)=H_3(N)\frac{\sigma ^3t^{1.5}}{\sqrt{3!}\sqrt{6}}$
Fourth order and higher integrals can be evaluated to perfect precision using this method so I am not giving examples
for that.

---

### #534 — amike
*May 7, 2017, 1:23 PM*

The validity of your proof I will leave you(/others?) to investigate, I merely point out that:

1. the left side is proportional to sigma, your right side is not.

2. There is a well-known result that your result does not agree with.

For me that is sufficient to conclude that your result is either incorrect or some sort of approximation.

I am willing to do a bit of work to demonstrate this, but only if you tell me what it would take to convince you -- I'm
not interested in doing the work if you are just going to ignore it.

---

### #535 — Cuchulainn
*May 7, 2017, 2:12 PM*

.

---

### #536 — Amin (Topic Author)
*May 7, 2017, 2:12 PM*

> The validity of your proof I will leave you(/others?) to investigate, I merely point out that:
>
> 1. the left side is proportional to sigma, your right side is not.
>
> 2. There is a well-known result that your result does not agree with.
>
> For me that is sufficient to conclude that your result is either incorrect or some sort of approximation.
>
>
>
> I am willing to do a bit of work to demonstrate this, but only if you tell me what it would take to convince you --
I'm not interested in doing the work if you are just going to ignore it.
You probably did not completely read my post 533 and the reference to an earlier post in post 533. You current post is
totally out of context after that.

---

### #537 — amike
*May 7, 2017, 2:44 PM*

I thought the logic was fairly clear: one of the results that you provided (that presumably resulted from the
development in your `definitive answers' post) appears to be in conflict with known results.  If I can convince you
(somehow) that this is the case, then you might have to go back and revisit or re-interpret your proof.

Willing to help, but it's up to you.

---

### #538 — amike
*May 7, 2017, 7:45 PM*

It might be quite simple: the constants 2.5/sqrt(2 Pi) is nearly equal to one, so perhaps you have rounded something
somewhere.  If you set this equal to one, get rid of the sigma on the left and assume that dz is a driftless Wiener
process with volatility sigma, then you're fine I think.

---

### #539 — Amin (Topic Author)
*May 10, 2017, 12:37 PM*

For those friends who would want to solve other partial differential equations like Navier  Stokes in 3d using this
method, they would have to use a Taylor series expansion in 4d (3d space + 1d time) where they would need derivatives of
initial data for each velocity component (in 3d)  with respect to space for all three dimensions and they could
substitute the  Navier Stokes PDE for time dependent partial derivatives in order to convert them into spatial
derivatives with respect to initial data. Boundary conditions would require some extra tact. Though writing this program
is on my list of things to do and I plan to post it here, if you would want some challenging application of Navier
Stokes PDE with special boundaries using this new method, I would love to try to be of help.

There would also be special cases when all spatial derivatives of velocity vector components would not be available and
we would need special methods to solve the PDE that could take advantage of the knowledge of the analytic structure of
the solution of Navier Stokes PDE.

---

### #540 — Amin (Topic Author)
*May 12, 2017, 2:08 PM*

Taylor series of $f(x_1)$ around $f(x_2)$ is calculated as

$f(x_1)=f(x_2)+ (x_1-x_2) \frac {d f(x_2)}{d x}+ \frac {(x_1-x_2)^2}{2} \frac {d^2 f(x_2)}{d x^2} + \\ \frac {(x_1-x_2)^3}{6} \frac {d^3 f(x_2)}{d x^3} + \frac {(x_1-x_2)^4}{24} \frac {d^4 f(x_2)}{d x^4}+ \dots$

Similarly Taylor series of $f(x_2)$ around $f(x_1)$ is calculated as

$f(x_2)=f(x_1)+ (x_2-x_1) \frac {d f(x_1)}{d x}+ \frac {(x_2-x_1)^2}{2} \frac {d^2 f(x_1)}{d x^2} + \\ \frac {(x_2-x_1)^3}{6} \frac {d^3 f(x_1)}{d x^3} + \frac {(x_2-x_1)^4}{24} \frac {d^4 f(x_1)}{d x^4}+ \dots $
\

differencing we get

$f(x_2)-f(x_1) \\

=(x_2-x_1) (\frac {df(x_1)}{d x}-\frac {df(x_2)}{dx}) \\

-\frac {(x_2-x_1)^2}{2} (\frac {d^2f(x_1)}{d x^2}+\frac {d^2f(x_2)}{dx^2}) \\

+\frac {(x_2-x_1)^3}{6} (\frac {d^3 f(x_1)}{d x^3}-\frac {d^3 f(x_2)}{d x^3}) \\

-\frac {(x_2-x_1)^4}{24} (\frac {d^4f(x_1)}{d x^4}+\frac {d^4f(x_2)}{dx^4}) + \dots$

We  could probably use the analogue of above formula for Taylor interpolation of a function. We will need un-normalized
interpolation weights such that

$a_1+a_2=(x_2-x_1)$  gives us $a_1=x-x_1$ and $a_2=x_2-x$

$b_1^2+b_2^2=(x_2-x_1)^2$  gives us $b_1=\sqrt{(x-x_1)}$ and $b_2=\sqrt{((x_2-x_1)^2-(x-x_1)^2)}$

$c_1^3+c_2^3=(x_2-x_1)^3$

$d_1^4+d_2^4=(x_2-x_1)^4$

Interpolation series tomorrow with possible application to Boundary value problems of ordinary differential equations.

---

### #541 — Cuchulainn
*May 13, 2017, 8:15 PM*

> For those friends who would want to solve other partial differential equations like Navier  Stokes in 3d using this
method, they would have to use a Taylor series expansion in 4d (3d space + 1d time) where they would need derivatives of
initial data for each velocity component (in 3d)  with respect to space for all three dimensions and they could
substitute the  Navier Stokes PDE for time dependent partial derivatives in order to convert them into spatial
derivatives with respect to initial data. Boundary conditions would require some extra tact. Though writing this program
is on my list of things to do and I plan to post it here, if you would want some challenging application of Navier
Stokes PDE with special boundaries using this new method, I would love to try to be of help.
>
> There would also be special cases when all spatial derivatives of velocity vector components would not be available
and we would need special methods to solve the PDE that could take advantage of the knowledge of the analytic structure
of the solution of Navier Stokes PDE.
*Prove or give a counter-example of the following statement:*

 In three space dimensions and time, given an initial velocity field, there exists a vector velocity and a scalar
pressure field, which are both smooth and globally defined, that solve the Navier–Stokes equations.

If you solve it I get 10% of the prize.

---

### #542 — Amin (Topic Author)
*May 24, 2017, 6:36 PM*

> For those friends who would want to solve other partial differential equations like Navier  Stokes in 3d using this
method, they would have to use a Taylor series expansion in 4d (3d space + 1d time) where they would need derivatives of
initial data for each velocity component (in 3d)  with respect to space for all three dimensions and they could
substitute the  Navier Stokes PDE for time dependent partial derivatives in order to convert them into spatial
derivatives with respect to initial data. Boundary conditions would require some extra tact. Though writing this program
is on my list of things to do and I plan to post it here, if you would want some challenging application of Navier
Stokes PDE with special boundaries using this new method, I would love to try to be of help.
>
> There would also be special cases when all spatial derivatives of velocity vector components would not be available
and we would need special methods to solve the PDE that could take advantage of the knowledge of the analytic structure
of the solution of Navier Stokes PDE.
*Prove or give a counter-example of the following statement:*

 In three space dimensions and time, given an initial velocity field, there exists a vector velocity and a scalar
pressure field, which are both smooth and globally defined, that solve the Navier–Stokes equations.

If you solve it I get 10% of the prize.
Of  course, we can use Taylor expansion of components of vector velocity as a function of its 3d position + time. All we
need are initial space derivatives of velocity vector components which are given by initial data and partial derivative
of each velocity component  with respect to initial time which are in turn converted to space derivatives of the initial
data using Navier Stokes equation. Space derivatives of pressure(used in calculation of time derivatives
after substitution of Navier Stokes equation where they occur) would be found by application of Bernoulli  principle  on
initial velocity data and time derivatives of pressure which would be non zero in case of unsteady flow would again be
found by appropriate application of Bernoulli's principle. If we  cannot find all derivatives of velocity and pressure
we can write a simple explicit numerical algorithm to advance the solution in time whose order would depend upon number
of derivatives of velocity and pressure that are available or the number of derivatives of velocity components  and
pressure that can easily be calculated. Once we have found velocity forward in time, we can easily apply Bernoulli
principle again to calculate pressure field forward in time.

Do friends agree?

---

### #543 — outrun
*May 24, 2017, 7:55 PM*

Congratulations to both of you, enjoy the money!

---

### #544 — Cuchulainn
*May 25, 2017, 3:28 PM*

[YouTube Video](https://www.youtube.com/embed/)Bernoullli explains. The PDE is here.

https://en.wikipedia.org/wiki/Water_hammer

While back I wrote the program for Stadtsverwarming for den Haag using this model. Method of Characteristics.

---

### #545 — outrun
*May 25, 2017, 4:40 PM*

Cool. I once worked on a water storage and transportation optimising model for the Rotterdam region, and that shockwave
at 1:15 was the thing to avoid. If that ever happened (due to the storage running empty and a sudden pressure drop) it
would cost billions!

---

### #546 — Cuchulainn
*May 25, 2017, 6:37 PM*

> Cool. I once worked on a water storage and transportation optimising model for the Rotterdam region, and that
shockwave at 1:15 was the thing to avoid. If that ever happened (due to the storage running empty and a sudden pressure
drop) it would cost billions!
Exactly! The program I worked on was first on a CCD 6600 supercomputer (took 3 hours to complete), then I ported it to a
Pr1me minicomputer and was faster. As time went on new snazzy valves, surge tanks and etc. had to be added to avoid such
potential calamities.

I suppose your model,was a yuge network of pipes and links. What were you optimising? Flow accesssibility?

// Method of Characteristics is cool because you can reduce a PDE to a ODE and then solve the ODE along characteriistic
curves. The 2X2 system is for speed and hydrostatic pressure.

---

### #547 — outrun
*May 25, 2017, 7:42 PM*

> Cool. I once worked on a water storage and transportation optimising model for the Rotterdam region, and that
shockwave at 1:15 was the thing to avoid. If that ever happened (due to the storage running empty and a sudden pressure
drop) it would cost billions!
Exactly! The program I worked on was first on a CCD 6600 supercomputer (took 3 hours to complete), then I ported it to a
Pr1me minicomputer and was faster. As time went on new snazzy valves, surge tanks and etc. had to be added to avoid such
potential calamities.

I suppose your model,was a yuge network of pipes and links. What were you optimising? Flow accesssibility?

// Method of Characteristics is cool because you can reduce a PDE to a ODE and then solve the ODE along characteriistic
curves. The 2X2 system is for speed and hydrostatic pressure.
Cool! So you helped them design the protections at the right places with the right dimensions based on simulations?

I had to look at the *profitability* of the company. Their operation was highly over-dimensioned because of people like
you , everything had triple backups, their target failure rate was once every 5000 years.

I had to figure out how they could make more money. That had to be found by minimising cost, and the main cost element
was energy consumption. They have big pump and pipes that transport huge amounts of water from lakes in the region, then
they have to clean that water which also consumes a lot of energy, then pump it in a buffer reservoir, and finally push
it into the regional nets.

To optimize the reservoir  I looked at water consumption patters (people  shower in the morning, they cook in the
evening, they hardly use any water at night etc). Based on that I made a real option model of the water reservoir and
how to operate it up in such a way that it alway had enough water to match demand while at the same time minimize their
energy cost. I use Bellman equations for this. At night electricity prices are half that of daytime prices so they ended
up cleaning more water at night, and less during the day-time, and and as consequence letting the volume in the
reservoir swing more during the day. That last bit was hard to sell to the ultra-conservative managers.

Changing the collection schedule of water from the lakes was also very interesting. I tried to move that to the night
time as well, but the resistance of the pipes grows with the flow speed. transporting a lot at night at higher flow
rates and less during the day increases the overall eletricity consumption, .. but not the costs of electricity.

It was a great fun project, mainly because of the peek in the kitchen, and because it was interesting to expose them to
QF methods and ideas.

---

### #548 — Cuchulainn
*May 25, 2017, 9:58 PM*

I suppose the output from your analysis is the input to the engineers who design a bigger pump and snazzy hysterisis
valves and plug them into the flow simulator?

Safety is probably also a major issue.

I (very) vaguely remember having to model valve characteristics in the model

![Image](http://processindustryforum.com/wp-content/uploads/2014/03/Hysteresis-Graph-1024x724.jpg)

---

### #549 — Cuchulainn
*May 26, 2017, 8:12 AM*

I reckon it's an optimal flow algorithm to determine the largest daily flow the system will meet. And the associated
cost in delivery of the water supply.It could be a linear programming model.

These kinds of models have greater applicability than just water slushing in pipes. Very useful stuff IMO.

---

### #550 — Cuchulainn
*May 26, 2017, 8:30 AM*

*Navier-Stokes*

I think this is not a feasible project for Amin in the short term. Formal mathematics and symbols won't help. You first
need to get insights into the issues (I am sure that Paul will testify to this) I would suggest to start with convection
diffusion/Burgers' equation to encounter essential modelling difficulties.

Here is a nice,well-written article (as with waterhammer they use Method of Characteristics) with Strang Splitting
(cool) to model the convection part.

Strange that this approach is not used so much in finance..

[http://www4.ncsu.edu/~acherto/papers/Ch ... rganov.pdf](http://www4.ncsu.edu/~acherto/papers/Chertock-Kurganov.pdf)

Program it up and examine the output.

---

[← Previous](page_010.md) | [Index](index.md) | [Next →](page_012.md)
