# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 9 of 59** — Posts #401–#450

[← Previous](page_008.md) | [Index](index.md) | [Next →](page_010.md)

---

### #401 — outrun
*January 10, 2017, 7:34 AM*

Cuch said that it was Picard, and  also said that it was flawed.

---

### #402 — Cuchulainn
*January 10, 2017, 9:24 AM*

The modified Picard method can be used to generate the Taylor series solution. amike might like it

http://it-educ.jmu.edu/~sochacjs/full.pdf

The methods here are in a time wrap. Mathematicians such as Adams and Runge gave them up in 1878 and moved to numerical
methods. No one uses Taylor for ODEs, at least they should not.

It's like being in HG Wells' Time Machine. The dial has been switched to 1840 (Moigno), it needs to be fast forwadrt to
at least 1950.  I would at least move it to Student or even to the blender.

---

### #403 — Cuchulainn
*January 10, 2017, 10:10 AM*

Maybe I missed something; where are the applications of this approach to finance?

---

### #404 — outrun
*January 10, 2017, 10:16 AM*

> Maybe I missed something; where are the applications of this approach to finance?
It started out for SDEs, but then it drifted a bit to the left. I expect that the stochastic part will be added back
later on. First things first.

---

### #405 — Cuchulainn
*January 10, 2017, 10:34 AM*

> Maybe I missed something; where are the applications of this approach to finance?
It started out for SDEs, but then it drifted a bit to the left. I expect that the stochastic part will be added back
later on. First things first.
I know that, but my question is still applications of this approach to finance.

How can you put all this stuff into a computer? Remember, no numerical values have been given, so I remain a doubting
Thomas.

---

### #406 — outrun
*January 10, 2017, 10:47 AM*

> Maybe I missed something; where are the applications of this approach to finance?
It started out for SDEs, but then it drifted a bit to the left. I expect that the stochastic part will be added back
later on. First things first.
I know that, but my question is still applications of this approach to finance.

How can you put all this stuff into a computer? Remember, no numerical values have been given, so I remain a doubting
Thomas.
I think the idea was to use it to generate numerical schemes for various specific types of SDEs (initial branch of this
thread), e.g. a 7rd order simulation equation for Heston. Once the expansion is computer you can code it and run it with
various Heston parameters.

---

### #407 — ppauper
*January 10, 2017, 12:10 PM*

> binge watching a series right now,
what kind of series?

Taylor? Fourier?

---

### #408 — ppauper
*January 10, 2017, 12:12 PM*

> ppauper is a maths guy i believe.
indeed, my undergrad was in math (both pure and applied)

---

### #409 — Cuchulainn
*January 10, 2017, 12:17 PM*

> binge watching a series right now,
what kind of series?

Taylor? Fourier?
And it be a MacLauriin series when the expansion is around t_0 = 0 in the bespoke article.Or it could be the  Peyton
Place series?

.BTW here's an awfully interesting article on modified Picard for PDE and ODE and nonlinear solvers. I had never seen
that before yesterday.

[http://www.jmu.edu/hyper/visualization/ ... sitory.pdf](http://www.jmu.edu/hyper/visualization/nbody/expository.pdf)

---

### #410 — Billy7
*January 10, 2017, 12:52 PM*

> We both do quite a bit of educating people and we see how standards are falling as rapidly as people's self belief
skyrockets! (In the past I've blamed lefties, google, and specifically Shirley Williams and Tony Blair!)
That's exactly what I see as well and I'm not in the educating business, I just read the internet! It's full of people
with no built-in resistance regulating just how smart they can feel. People doubt anything, and genuinely believe they
have (or can have if they google for a day or two) an equally deep understanding of the universe as Einstein. I'm
blaming google whenever I raise this in conversations, but nobody had ever agreed with me, so I'm glad Paul agrees lol.

I admit to have been following this thread from time to time, but mostly for the banter between you guys:)

---

### #411 — Cuchulainn
*January 10, 2017, 1:02 PM*

> We both do quite a bit of educating people and we see how standards are falling as rapidly as people's self belief
skyrockets! (In the past I've blamed lefties, google, and specifically Shirley Williams and Tony Blair!)
That's exactly what I see as well and I'm not in the educating business, I just read the internet! It's full of people
with no built-in resistance regulating just how smart they can feel. People doubt anything, and genuinely believe they
have (or can have if they google for a day or two) an equally deep understanding of the universe as Einstein. I'm
blaming google whenever I raise this in conversations, but nobody had ever agreed with me, so I'm glad Paul agrees lol.

I admit to have been following this thread from time to time, but mostly for the banter between you guys:)
How do you solve ODEs?

---

### #412 — Paul
*January 10, 2017, 1:13 PM*

> ppauper is a maths guy i believe.
indeed, my undergrad was in math (both pure and applied)
I assumed so. It's all about wearing your learning lightly.

---

### #413 — Billy7
*January 10, 2017, 1:18 PM*

> We both do quite a bit of educating people and we see how standards are falling as rapidly as people's self belief
skyrockets! (In the past I've blamed lefties, google, and specifically Shirley Williams and Tony Blair!)
That's exactly what I see as well and I'm not in the educating business, I just read the internet! It's full of people
with no built-in resistance regulating just how smart they can feel. People doubt anything, and genuinely believe they
have (or can have if they google for a day or two) an equally deep understanding of the universe as Einstein. I'm
blaming google whenever I raise this in conversations, but nobody had ever agreed with me, so I'm glad Paul agrees lol.

I admit to have been following this thread from time to time, but mostly for the banter between you guys:)
How do you solve ODEs?
Numerically?

---

### #414 — Cuchulainn
*January 10, 2017, 3:22 PM*

> May I ask which people here have done an undergraduate mathematics degree? (And where? As supplementary question!)
and also maybe what the *weltanschauung* is!

[play ](https://www.merriam-webster.com/dictionary/weltanschauung?pronunciation&lang=en_us&dir=w&file=weltan01)

Mine is: no point looking for (quasi)analytic computable solutions (they don't exist).

---

### #415 — Paul
*January 10, 2017, 4:32 PM*

> May I ask which people here have done an undergraduate mathematics degree? (And where? As supplementary question!)
and also maybe what the *weltanschauung* is!

[play ](https://www.merriam-webster.com/dictionary/weltanschauung?pronunciation&lang=en_us&dir=w&file=weltan01)

Mine is: no point looking for (quasi)analytic computable solutions (they don't exist).
Most maths is easy. Applying maths to new problems is the most fun, and few people are any good at it. Never sit next to
a pure mathematician at a dinner party.

---

### #416 — Traden4Alpha
*January 10, 2017, 4:34 PM*

> May I ask which people here have done an undergraduate mathematics degree? (And where? As supplementary question!)
and also maybe what the *weltanschauung* is!

[play ](https://www.merriam-webster.com/dictionary/weltanschauung?pronunciation&lang=en_us&dir=w&file=weltan01)

Mine is: no point looking for (quasi)analytic computable solutions (they don't exist).
Most maths is easy. Applying maths to new problems is the most fun, and few people are any good at it. Never sit next to
a pure mathematician at a dinner party.Yes, the impure mathematicians are more fun!

---

### #417 — Cuchulainn
*January 10, 2017, 5:08 PM*

>
> and also maybe what the *weltanschauung* is!
>
>
>
> [play ](https://www.merriam-webster.com/dictionary/weltanschauung?pronunciation&lang=en_us&dir=w&file=weltan01)
>
>
>
> Mine is: no point looking for (quasi)analytic computable solutions (they don't exist).
Most maths is easy. Applying maths to new problems is the most fun, and few people are any good at it. Never sit next to
a pure mathematician at a dinner party.
Yes, the impure mathematicians are more fun!
Even worse, they think they know maths.

---

### #418 — Cuchulainn
*January 10, 2017, 5:11 PM*

> Now you can download the new better written version of my paper here at SSRN: [https://papers.ssrn.com/sol3/papers.cfm ... id=2872598](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598)
>
> ...
>
> system of three non-linear second order ordinary differential equations.
Ok, we still have no clear statement (that I could find) that indicated when one might want to use this method over any
of the many others out there, but I think I understand what is going on now--at least to the point where the equivalence
with the perturbative approach is easy to show.

It wasn't clear to me in the last version of the paper whether there was some approximation going on to obtain the
series expansion, but it is clear to me now that there isn't.  Equation (5) will (formally) solve the ode -- just by the
fundamental theorem of (integral) calculus.

Where I was starting was an iteration of the solution into itself, like:

$$ y(t)=y(t_0)+\epsilon \int_{t_0}^tdsf\left(s,y(t_0)+\epsilon \int_{t_0}^sduf(u,y(u))\right). $$

Then you keep iterating forever... and you get the perturbative solution by performing a Taylor series in$\epsilon$ .
However, this is actually equal to Equation (5) from the paper (putting the$\epsilon$ 's in):

$$ y(t)

=y(t_0)

+\epsilon\int_{t_0}^tdsf\left(s,y(t_0)\right)

+\epsilon^2\int_{t_0}^tds

\int_{t_0}^s du

\frac{\partial f}{\partial y}(s,y(u))

f\left(u,y(u))\right) $$

Now you play the same game with the integrand in the last term on the right (like Equation (6) from the paper), which
leaves this term but with$y(t_0)$ , and brings the next order term multiplied by$\epsilon^3$ , and so on. Series
expansion in$\epsilon$ .

So my conclusion at this point is: For ode's the method is equivalent to a very well known series solution, and
therefore adds nothing new.

(Of course all of the above assumes really `nice' functions, but that's ok with me as a start -- if it doesn't work
there it isn't likely to work anywhere.)

P.S. I will leave the ``my degree is bigger than yours'' discussion to the rest of you.
How does the above (regular, not singular) perturbation expansion tackle my counterexample?

---

### #419 — Paul
*January 10, 2017, 5:20 PM*

>
> and also maybe what the *weltanschauung* is!
>
>
>
> [play ](https://www.merriam-webster.com/dictionary/weltanschauung?pronunciation&lang=en_us&dir=w&file=weltan01)
>
>
>
> Mine is: no point looking for (quasi)analytic computable solutions (they don't exist).
Most maths is easy. Applying maths to new problems is the most fun, and few people are any good at it. Never sit next to
a pure mathematician at a dinner party.Yes, the impure mathematicians are more fun!
Unfortunately pure mathematicians exist and are not unique.

---

### #420 — outrun
*January 10, 2017, 5:39 PM*

About the wording/claim

"A counterexample is a special kind of example that disproves a statement or proposition"

Now Amin says little about for what type of functions his method works, but he does say:

"Thus we are saved

from having to determine the future evolution of the dependent variables while evaluating the integrals of **complicated
functions**"

Now I don't think Cuch's example is a "complicated function" at all, and so this is a counter example indeed, until Amin
add something along the lines of Amike "limited for real 'nice" functions".

Ps: Why do I see a screen grab, of a desktop, of an open pdf,  of a picture, of a notebook? That's 4 levels deep!

---

### #421 — list1
*January 10, 2017, 5:40 PM*

>
> Most maths is easy. Applying maths to new problems is the most fun, and few people are any good at it. Never sit next
to a pure mathematician at a dinner party.
Yes, the impure mathematicians are more fun!
Unfortunately pure mathematicians exist and are not unique.
Pure math is a specific style of thinking and speaking. The style of speaking is a formal proof of a theorem which
represents a statement which is right by definition. Applied mathematician does not care about broad conditions when the
statements are formally correct. They deal primarily with particular equations or problems.

I remember a company in a math conference where people who knows each other from differents cities and who worked in
probability area drank and talk together. One not from conference man jointed to the company drank with other then
probably want to be closer to other said I worked in math area too. One smart mathematician said o'k and asked formulate
at least one theorem he proved. The man looked as a student who failed on exam.

---

### #422 — amike
*January 10, 2017, 5:41 PM*

> Now you can download the new better written version of my paper here at SSRN: [https://papers.ssrn.com/sol3/papers.cfm ... id=2872598](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598)
>
> ...
>
> system of three non-linear second order ordinary differential equations.
Ok, we still have no clear statement (that I could find) that indicated when one might want to use this method over any
of the many others out there, but I think I understand what is going on now--at least to the point where the equivalence
with the perturbative approach is easy to show.

...

(Of course all of the above assumes really `nice' functions, but that's ok with me as a start -- if it doesn't work
there it isn't likely to work anywhere.)

P.S. I will leave the ``my degree is bigger than yours'' discussion to the rest of you.  :)
How does the above (regular, not singular) perturbation expansion tackle my counterexample?
Presumably one would have to more carefully determine the conditions required on f (and derivatives/products...) so that
this all works, and then your counterexample would be excluded.  :)  But since I am not the advocate for this series
solution I will leave that analysis to Amin.

---

### #423 — Cuchulainn
*January 10, 2017, 6:40 PM*

>
> Yes, the impure mathematicians are more fun!
Unfortunately pure mathematicians exist and are not unique.
Pure math is a specific style of thinking and speaking. The style of speaking is a formal proof of a theorem which
represents a statement which is right by definition. Applied mathematician does not care about broad conditions when the
statements are formally correct. They deal primarily with particular equations or problems.

I remember a company in a math conference where people who knows each other from differents cities and who worked in
probability area drank and talk together. One not from conference man jointed to the company drank with other then
probably want to be closer to other said I worked in math area too. One smart mathematician said o'k and asked formulate
at least one theorem he proved. The man looked as a student who failed on exam.
You're so binary. Ever heard of *Constructive Mathematics*?

Corollary: This thread is in freefall.

---

### #424 — Cuchulainn
*January 10, 2017, 6:43 PM*

*Never sit next to a pure mathematician at a dinner party.*

Could be worse, a midWest freshly minted liberal arts PhD going on about Finnegans Wake the whole evening.

---

### #425 — Cuchulainn
*January 10, 2017, 7:23 PM*

>
> Ok, we still have no clear statement (that I could find) that indicated when one might want to use this method over
any of the many others out there, but I think I understand what is going on now--at least to the point where the
equivalence with the perturbative approach is easy to show.
>
> ...
>
> (Of course all of the above assumes really `nice' functions, but that's ok with me as a start -- if it doesn't work
there it isn't likely to work anywhere.)
>
>
>
> P.S. I will leave the ``my degree is bigger than yours'' discussion to the rest of you.
How does the above (regular, not singular) perturbation expansion tackle my counterexample?
Presumably one would have to more carefully determine the conditions required on f (and derivatives/products...) so that
this all works, and then your counterexample would be excluded.    But since I am not the advocate for this series
solution I will leave that analysis to Amin.
Does the perturbation  method also flunk out for this case?

---

### #426 — amike
*January 10, 2017, 9:11 PM*

yeah, it doesn't like that.  Of course, it's quite possible that it could fail in a different way than iterated
integrals...

---

### #427 — ppauper
*January 11, 2017, 6:54 AM*

cuch, what method do you suggest for your problem $y'=\frac{2y}{t}$ with $y(0)=y_0\ne 0$ ?

(edit: cuch's initial condition added)

write as  $t'=\frac{t}{2y}$ with $t(y_0)=0$  where $y_0\ne 0$

---

### #428 — Amin (Topic Author)
*January 11, 2017, 10:01 AM*

> In cases of some ODEs that have complicated expressions in independent variable, many times addition of each next
iterated integrals solution has increasing number of terms. For example, for a 2nd order ODE, in some cases solution of
first double integral may have two terms, the solution to second third order integral would have three terms after
integration and next fourth order integral may have four terms and so on. While each set of terms is well behaved and
bounded collectively but when we collect lower powers across all integrals they seem to diverge in that specific power
but the whole solution would still converge because higher powers cancel the diverging effect of lower powers but I am
sure more intelligent mathematicians would want to work on how to analyze these expanding series(as solution of each
higher integral has more terms that solution of previous lower integral. May be there could be an analogy with two
dimensional series that each term in solution is itself a collection of many terms in a way that each increasing term
has more terms in it than the previous term.) I hope that programs I posted would be helpful for intelligent
mathematicians to analyze how to systematically simplify the growing term by term solution in a very simple form. If you
do intelligent research, Please do quote my paper and reference to my programs and this Wilmott thread(Our own forum.)
>
>
>
> On the related question of solution of PDEs, there are several analytic techniques like many versions of separation of variables that transform the PDEs into ODEs that can easily be solved by the method of iterated integrals. here is initial reference https://en.wikipedia.org/wiki/Separation_of_variables and many people have done very advanced research on solution of navier stokes, fokker plank, Laplace equation, wave equation and many other PDEs after converting them into ODEs. I hope many other smart friends would want to explore doing more research in this area.
When trying to solve partial differential equations, if we can convert them into a set of ODEs, we can again solve the
ODEs with method of iterated integrals to get a series solution in terms of arbitrary initial values. Many smart
mathematicians would like to identify the closed from solution from the series solution. If that could be possible, it
could result in a closed form solution to set of ODEs underlying the complete solution of the partial differential
equation after choosing appropriate constants that would satisfy the boundary conditions in the closed form solution of
the ODEs. This may always not be possible but I am sure it would be good to take advantage of this possibility whenever
we can.

---

### #429 — Cuchulainn
*January 11, 2017, 10:44 AM*

> In cases of some ODEs that have complicated expressions in independent variable, many times addition of each next
iterated integrals solution has increasing number of terms. For example, for a 2nd order ODE, in some cases solution of
first double integral may have two terms, the solution to second third order integral would have three terms after
integration and next fourth order integral may have four terms and so on. While each set of terms is well behaved and
bounded collectively but when we collect lower powers across all integrals they seem to diverge in that specific power
but the whole solution would still converge because higher powers cancel the diverging effect of lower powers but I am
sure more intelligent mathematicians would want to work on how to analyze these expanding series(as solution of each
higher integral has more terms that solution of previous lower integral. May be there could be an analogy with two
dimensional series that each term in solution is itself a collection of many terms in a way that each increasing term
has more terms in it than the previous term.) I hope that programs I posted would be helpful for intelligent
mathematicians to analyze how to systematically simplify the growing term by term solution in a very simple form. If you
do intelligent research, Please do quote my paper and reference to my programs and this Wilmott thread(Our own forum.)
>
>
>
> On the related question of solution of PDEs, there are several analytic techniques like many versions of separation of variables that transform the PDEs into ODEs that can easily be solved by the method of iterated integrals. here is initial reference https://en.wikipedia.org/wiki/Separation_of_variables and many people have done very advanced research on solution of navier stokes, fokker plank, Laplace equation, wave equation and many other PDEs after converting them into ODEs. I hope many other smart friends would want to explore doing more research in this area.
When trying to solve partial differential equations, if we can convert them into a set of ODEs, we can again solve the
ODEs with method of iterated integrals to get a series solution in terms of arbitrary initial values. Many smart
mathematicians would like to identify the closed from solution from the series solution. If that could be possible, it
could result in a closed form solution to set of ODEs underlying the complete solution of the partial differential
equation after choosing appropriate constants that would satisfy the boundary conditions in the closed form solution of
the ODEs. This may always not be possible but I am sure it would be good to take advantage of this possibility whenever
we can.
This is waffle. I am going to respond to this.

AFAIR your undergrad degree is EE so there are huge chunks of mathematics that you know nothing about, so telling is
about PDEs or even ODEs I take with a spoon of salt. Same with CS degree.UNLESS you studied in great detail afterwards.

Just be humble.

---

### #430 — Paul
*January 11, 2017, 10:50 AM*

It's another "signal."

---

### #431 — ppauper
*January 11, 2017, 11:13 AM*

>
> Just be humble.
[YouTube Video](https://www.youtube.com/embed/)

---

### #432 — Cuchulainn
*January 11, 2017, 1:10 PM*

>
> Just be humble.
[YouTube Video](https://www.youtube.com/embed/)
[YouTube Video](https://www.youtube.com/embed/)

---

### #433 — Cuchulainn
*January 11, 2017, 2:42 PM*

> cuch, what method do you suggest for your problem $y'=\frac{2y}{t}$ with $y(0)=y_0\ne 0$ ?
>
>
>
> (edit: cuch's initial condition added)
>
>
>
>
>
> write as  $t'=\frac{t}{2y}$ with $t(y_0)=0$  where $y_0\ne 0$
Personally, I tend to look at the problem:

A. Qualitative (analyse the ODE, determiinistic it has a solution (or not) and where).

B. Quantitative (get the solution: exact, numerical whatever).

In the above case (there are 3 other scenarios depending on t_0 and y_0) we can almost see it has no solution just be
letting t ->0. (the left and right sides give different answers. In fact, writing$ ty' = 2y, y(0) = y_0 ( y_0 \ne 0)$ it
look more like a classical singular perturbation problem.

So, to answer the question, I used Picard and it diverges after one iteration (it is clear why because it uses integrals
and series). We can pinpoint the reason that it is not converging and that gives insights. NB the iterates do not
involve y.

I have applied iterated integral as well and it too explodes. However, It involves y itself which is begging the
question and leads to circular reasoning.. Likewise, perturbation is based on Taylor expansions which are always scary.
Numerically, they are unstable (that's why RK methods were born). I challenge the feasability of asymptotic expansions
(the are popular in physics).

So, it seems proofs and counter-proofs are possible with Picard.

What's the idea behind $t' = t/2y$?

---

### #434 — list1
*January 11, 2017, 3:11 PM*

Two primary problems in the amin's problem

Whether he proved that last term converges to zero. As he has discussed it looks like he wishes to present approximation
of the solution of the ode y ' = f ( t , y ) on [ 0 , T ] as a power series with coefficients depending on values y ,
and f  and might be its derivatives at zero. It is well known that solution of the ODEs in general depends on values of
f on whole [ 0 , T ]. Thus any example in which solution depends on all values of f on [ 0 , T ] is a counterexample to
amin's idea.

---

### #435 — ppauper
*January 11, 2017, 3:27 PM*

> cuch, what method do you suggest for your problem $y'=\frac{2y}{t}$ with $y(0)=y_0\ne 0$ ?
>
>
>
> (edit: cuch's initial condition added)
>
>
>
>
>
> write as  $t'=\frac{t}{2y}$ with $t(y_0)=0$  where $y_0\ne 0$
Personally, I tend to look at the problem:

A. Qualitative (analyse the ODE, determiinistic it has a solution (or not) and where).

B. Quantitative (get the solution: exact, numerical whatever).

In the above case (there are 3 other scenarios depending on t_0 and y_0) we can almost see it has no solution just be
letting t ->0. (the left and right sides give different answers. In fact, writing$ ty' = 2y, y(0) = y_0 ( y_0 \ne 0)$ it
look more like a classical singular perturbation problem.

So, to answer the question, I used Picard and it diverges after one iteration (it is clear why because it uses integrals
and series). We can pinpoint the reason that it is not converging and that gives insights. NB the iterates do not
involve y.

I have applied iterated integral as well and it too explodes. However, It involves y itself which is begging the
question and leads to circular reasoning.. Likewise, perturbation is based on Taylor expansions which are always scary.
Numerically, they are unstable (that's why RK methods were born). I challenge the feasability of asymptotic expansions
(the are popular in physics).

So, it seems proofs and counter-proofs are possible with Picard.

What's the idea behind $t' = t/2y$?
$t'=\frac{t}{2y}$  with $t(y_0)=0$  where $y_0\ne 0$ you can solve,

$t(y)=c y^{1/2}$

and then initial condition gives$t(y)=0$ for all$y$ which you can't invert to find$y(t)$ , and sort of shows you what is
happening

that used to be a standard trick question in exams, set a question$\frac{dy}{dt}=f(y,t)$ that doesn't seem to fit into
any of the categories but when you flip it over and write$\frac{dt}{dy}$ it's easy

---

### #436 — amike
*January 11, 2017, 3:55 PM*

> ...
>
> Likewise, perturbation is based on Taylor expansions which are always scary. Numerically, they are unstable (that's
why RK methods were born).
>
> ...
Well I for one have never been frightened when doing a perturbation analysis...  :)

This does highlight what the real issue is here (IMHO).  Looking at cases where the ivp breaks down (or the structure of
the problem makes the method inapplicable...) is quite interesting, but all Amin needs to do is hire someone to write
down for him some conditions under which his method avoids these cases, and he is once again off to the races.

But it should be clear that given the ii method is equivalent to a small time expansion, there are a multitude of
(perfectly regular) examples where the method is completely ineffective.  Here is a classic example:

$$ \frac{dy(t)}{dt}=x(t),\quad

\frac{dx(t)}{dt}=-y(t)-\frac{1}{20}x(t),\quad

y(0)=0,\quad x(0)=1,\quad t\in[0,100].  $$

It is of course a damped SHO, probably the most common system in the universe...  (the damping isn't really necessary
here).

Runge-Kutta (4/5) happily integrates this without blinking, and gives a solution that agrees very well with the exact
solution on the interval.

Amin: How many terms of your expansion are required to give a reasonable approximation to the solution over the whole
interval?  Please, please, please  try this.

Here is 20 terms in your expansion (in red) plotted out to t=20, the blue line is the exact solution and rk45 (they
overlap):

---

### #437 — Cuchulainn
*January 11, 2017, 4:00 PM*

Nice post, amike.

---

### #438 — outrun
*January 11, 2017, 4:25 PM*

> Two primary problems in the amin's problem
>
> Whether he proved that last term converges to zero. As he has discussed it looks like he wishes to present
approximation of the solution of the ode y ' = f ( t , y ) on [ 0 , T ] as a power series with coefficients depending on
values y , and f  and might be its derivatives at zero. It is well known that solution of the ODEs in general depends on
values of f on whole [ 0 , T ]. Thus any example in which solution depends on all values of f on [ 0 , T ] is a
counterexample to amin's idea.
What do you mean by "depends" on the values in the interval?

I would say that the function needs to nice (the integrals need to be computable etc) on the interval for all initial
conditions.

---

### #439 — amike
*January 11, 2017, 5:48 PM*

> Nice post, amike.
time will tell...

---

### #440 — list1
*January 11, 2017, 6:33 PM*

> Two primary problems in the amin's problem
>
> Whether he proved that last term converges to zero. As he has discussed it looks like he wishes to present
approximation of the solution of the ode y ' = f ( t , y ) on [ 0 , T ] as a power series with coefficients depending on
values y , and f  and might be its derivatives at zero. It is well known that solution of the ODEs in general depends on
values of f on whole [ 0 , T ]. Thus any example in which solution depends on all values of f on [ 0 , T ] is a
counterexample to amin's idea.
What do you mean by "depends" on the values in the interval?

I would say that the function needs to nice (the integrals need to be computable etc) on the interval for all initial
conditions.

outrun, it was f that was missed.

It was written "It is well known that solution of the ODEs in general depends on values of $f $ on whole [ 0 , T ]."

Though, now I think if f can be expended in power series which converges in any finite sphere then solution can be
expended as $$ f ( t , y ) = \sum_{k = 0}^{\infty} f_{k} ( t ) y^k$
$ then one can try to resolve the problem can be resolve the problem iteratively. For k = 0 solve the problem and find $
f_0$ . Then using this  $ f_0$ to consider the case k = 1 find $ f_1$ and etc. Though it should be additional problem
with initial data.

What amin is trying to do is to present unknown solution in the form $$ y ( t ) = \sum_{k = 0}^{\infty} a_k \,t ^ k $
$ and find $ a_k$. It also might be possible but to get a full math result he need explicit condition on f when the
result takes place. His idea comes a little bit far from the actual problem. I am almost sure that it is possible than
it was already done.

---

### #441 — Cuchulainn
*January 11, 2017, 6:49 PM*

*"It is well known that solution of the ODEs in general depends on values off **on whole [ 0 , T ]."*

Says who? BTW What is T?

Try this

$y'= y^2, y(0) = a$

Beyond a certain T there is no solution. What is that T?

That's one of the issues as well.

---

### #442 — list1
*January 11, 2017, 7:27 PM*

>  *"It is well known that solution of the ODEs in general depends on values off **on whole [ 0 , T ]."*
>
>
>
> Says who? BTW What is T?
>
>
>
> Try this
>
>
>
> $y'= y^2, y(0) = a$
>
>
>
> Beyond a certain T there is no solution. What is that T?
>
>
>
> That's one of the issues as well.
Here f ( t , y ) = $y^2 ( t ) $ then y ( t )  = y ( 0 ) + $\int_{0}^{t} y ^2 ( s ) ds $

Hence at t depends on all values of f up to this moment.

---

### #443 — Paul
*January 11, 2017, 8:13 PM*

Wake me up. Somebody pinch me. Will it ever end?

---

### #444 — Traden4Alpha
*January 11, 2017, 11:15 PM*

> Wake me up. Somebody pinch me. Will it ever end?What should one expect from an ODEous topic?

---

### #445 — Cuchulainn
*January 11, 2017, 11:17 PM*

>  *"It is well known that solution of the ODEs in general depends on values off **on whole [ 0 , T ]."*
>
>
>
> Says who? BTW What is T?
>
>
>
> Try this
>
>
>
> $y'= y^2, y(0) = a$
>
>
>
> Beyond a certain T there is no solution. What is that T?
>
>
>
> That's one of the issues as well.
Here f ( t , y ) = $y^2 ( t ) $ then y ( t )  = y ( 0 ) + $\int_{0}^{t} y ^2 ( s ) ds $

Hence at t depends on all values of f up to this moment.

---

### #446 — Cuchulainn
*January 11, 2017, 11:19 PM*

**(broken latex: Unbalanced $: 5)**

```latex
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

### #447 — Cuchulainn
*January 11, 2017, 11:23 PM*

> Wake me up. Somebody pinch me. Will it ever end?
I'm thinking of joining the priesthood
[YouTube Video](https://www.youtube.com/embed/)
That post by list really is the pinnacle!

---

### #448 — Cuchulainn
*January 12, 2017, 11:31 AM*

>  *"It is well known that solution of the ODEs in general depends on values off **on whole [ 0 , T ]."*
>
>
>
> Says who? BTW What is T?
>
>
>
> Try this
>
>
>
> $y'= y^2, y(0) = a$
>
>
>
> Beyond a certain T there is no solution. What is that T?
>
>
>
> That's one of the issues as well.
Here's the answer.

1. If you do a Picard iteration you see exactly for which values of t the solution ($y(t) = 1/(1-t) $ converges. Some
real analysis (basic book by Apostol is useful here..) and you see immediately that t must be less than one.

2. Runge Kutta also.

[table][tr][td][/td]

[td][/td]

[td][/td]

[/tr]

[/table]

---

### #449 — Cuchulainn
*January 12, 2017, 11:54 AM*

> ppauper is a maths guy i believe.
indeed, my undergrad was in math (both pure and applied)
The major bottleneck IMO in this thread is that quite a few posters have seemingly no background in real analysis. and
the only place is in a maths degree. Other disciplines emulate by* calculus.*

This leads to communication problems.

---

### #450 — list1
*January 12, 2017, 1:57 PM*

when we consider ode we always should state the area where solutions should be defined. The standard sufficient
conditions for existence of the solution are continuous in t on [ 0 , T ] and boundness of the continuous first order
derivative in y on$ [ \,0 \,, T\,] \times ( - \infty , + \infty ) $ . These conditions are classical and they are
sufficient for the convergence of the Picard iterations too. Of course iterations and solution of the odes can be
constructed under more general conditions too.

---

[← Previous](page_008.md) | [Index](index.md) | [Next →](page_010.md)
