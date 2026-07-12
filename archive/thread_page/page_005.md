# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 5 of 65** — Posts #201–#250

[← Previous](page_004.md) | [Index](index.md) | [Next →](page_006.md)

---

### #201 — Paul
*December 17, 2016, 1:59 PM*

I'm inclined to agree!

---

### #202 — Amin (Topic Author)
*December 17, 2016, 10:41 PM*

Hi Cuch, Yes I may be wrong but I am not thinking of MOL anymore. I will not make the definite claim unless I
numerically check things but I do think that PDEs like Fokker Planck can be expanded to a series solution using method
of iterated integrals. I was thinking of writing, numerically verifying and then posting a small program that would use
the series solution of a Fokker Planck to calculate the transition probabilities on a given grid.

@Cuch, did you find my mathematica program for solution of ODEs with the new method helpful. Any comments or suggestions
for improvement.

---

### #203 — amike
*December 18, 2016, 12:45 AM*

> ...
>
> As amike suggested, I am doing a revision of my paper adding many other problems that are not basic and hint at near
universal applicability of the method. I thank amike for his critical review.
Has there been a revision of the paper that gives a clear example where this method gives something
interesting/better/new?

I'm seeing posts where I'm told how great a great method it is, but not a lot of evidence IMHO...

---

### #204 — Amin (Topic Author)
*December 18, 2016, 4:07 AM*

Thank you for your opinion amike. I have still not completed the revision of the paper. But, in order to make my point
across that the method does work very well, I will post the solution from my mathematica code given earlier for riccati
and logistic ODEs that you had proposed earlier. Hope that would work to convince you that the method does work.

1. One problem is when there are complicated functions of t(independent variable) in ODE that you cannot symbolically
integrate but even then there could be some expert way around using analysis of integrals if the ODE must be solved for
a special purpose/project where solution of ODE is crucial for the project.

2. Mostly for singular initial value problems, the initial conditions are specified so that some initial conditions are
zero that take care of singular nature of the problem but, yes, some work might have to be done  to solve singular
initial value problems and related issues.

These are the only two problems I see with the method of iterated integrals.

In the small mathematica code I have given on Wilmott (post 196-198 above), I have substituted initial values for  y(0)
and dy/dt(0) before doing integrations so that if the appropriate initial values are zero and the ODE is otherwise
singular, there would be no need for integrations in terms multiplying with  y(0)=0, or dy/dt(0)=0; These terms would
just go to zero. However, sometimes, one would like a solution with general initial values and in that case, you could
do integrations first and only substitute particular initial values for each step when you actually solve the ODE. You
will just have to play with the code a little bit to do appropriate modifications.

---

### #205 — amike
*December 19, 2016, 4:00 PM*

> Thank you for your opinion amike. I have still not completed the revision of the paper. But, in order to make my point
across that the method does work very well, I will post the solution from my mathematica code given earlier for riccati
and logistic ODEs that you had proposed earlier. Hope that would work to convince you that the method does work.
>
> ...
Well, to be clear: it's not that I really doubt that the method `works', it's that I don't yet see where/how it works
better than other methods.  Can you maybe at least give one case/problem where this approach is demonstrably better than
another approach (and be somewhat clear what you mean by `better')?

(In fact, I suspect that it is really a fairly standard perturbation approach in disguise... but I can't really follow
the derivation in your paper, so this remains speculation.)

---

### #206 — Cuchulainn
*December 19, 2016, 4:11 PM*

*I can't really follow the derivation in your paper, *

Same here. I can't get a handle on the essential idea, the 'spark', whatever.

Another question: OP started with SDE, now it's a discussion on ODE.  What's the link?

---

### #207 — outrun
*December 19, 2016, 4:51 PM*

Maybe rename it "investigation in series expansions of ODE" instead of "breakthrough in SDE" ?

---

### #208 — Amin (Topic Author)
*December 20, 2016, 2:23 PM*

>
> Another question: OP started with SDE, now it's a discussion on ODE.  What's the link?
The method I have proposed is a general way to solve integrals that involve functions of dependent variables and
one(possibly more) independent variable where the dependence structure is given as dictated by the ODE or SDE itself.
Solution of ordinary differential equations can be written as a deterministic integral while the solution of stochastic
differential equations can be written as a stochastic integral. Both deterministic and stochastic integrals can be
solved by the method of iterated integrals. We also know that solution to drift of an SDE is given by an ODE which is
solved just like we solved the ODEs in my paper(Most are very simple). In the solution to stochastic integrals, we have
iterated integrals some/all of which can be stochastic or deterministic or a mix of both. The method originated while I
was working on SDEs hence I started out with the current name of the thread. Obviously solution to drift of an SDE is
given by solution to an ODE.

---

### #209 — Amin (Topic Author)
*December 24, 2016, 10:12 AM*

Here I want to post the mathematica program for solution of 2nd order ODEs and then describe how to extend it to nth
order by making very minor modifications. I will give some more examples but I have initially chosen the example from my
paper that I also discussed in post 150.

Consider the 2nd order initial value problem given as

$y''=f\left(\tau ,y(\tau ),y'(\tau )\right)=-2 y y'$       $y(0)=y_0=0$      $y'(0)=y'_0=1$

The mathematica routine goes as:

1.$\text{ClearAll}[Z,t,y,\text{Zi},\text{Wi},\text{Xi},X,\text{y0},\text{y10},i,\text{i1},n,\text{ZAns}]$

2.$Z\text{:=}-2y \text{y1};$

3.$\text{y0}=0$

4.$\text{y10}=1$

5.$n=15;$

6.$X\text{:=}\text{y0}+t \text{y10}$

7.$\text{Zi}[3]=(Z\text{/.}t\to \text{ti}[3])$

8.$\text{For}*=D[\text{Zi},y]*(\text{y1})+D[\text{Zi},\text{y1}]*(Z\text{/.}t\to \text{ti}[i+1]))]$

9.$\text{For}=(\text{Zi}\text{/.}\{y\to \text{y0},\text{y1}\to \text{y10}\}))]$

10.$\text{For}=\text{Wi};$

$\text{For}[\text{i1}=i,\text{i1}\geq 2,\text{i1}\text{--},(\text{Xi}[\text{i1}-1]=\text{Integrate}[\text{Xi}[\text{i1}],\{\text{ti}[\text{i1}],0,\text{ti}[\text{i1}-1]\}])];$

$X=X+(\text{Xi}[\text{i1}]\text{/.}\text{ti}[1]\to t);)]$

11.
$\text{ZAns}=\text{Collect}[X,t,\text{Simplify}]\text{//}\text{PolynomialForm}[\#,\text{TraditionalOrder}\to \text{False}]\&$

The output is:

$t-\frac{t^3}{3}+\frac{2 t^5}{15}-\frac{17 t^7}{315}+\frac{62 t^9}{2835}-\frac{1382 t^{11}}{155925}+\frac{21844 t^{13}}{6081075}-\frac{929569 t^{15}}{638512875}$

The ODE is specified in Command(2) where dy/dt is replaced by y1. In command(3) and (4), the initial values are
specified. These two lines can be omitted if you want to keep the values general in terms of y0 and y10. In command(5),
the number of terms in expansion are specified. It can sometimes take mathematica a long time for large number of terms
if recursions and algebra becomes too large. In any of the commands (8),(9), and 10, you can add a print command to see
the values of various terms if that is sometimes needed. The solution is given in command(11).

In case of third ordr ODE, you need to make some changes in command(8) and add a derivative operator with respect to y2
and you will have to replace initial index 3 in commnads (7),(8),(9),(10) with 4 as there will be three integrations in
the initial term as opposed to two integrations in the second order ODEs(one extra integration and hence the
corresponding change in initial index). The 2nd inner loop index in command 10 will remain 2 in all order ODEs.

You might want to add assumptions when integrating from a general t0 instead of t0=0, as I mentioned in post 198 and the
initial integration limits would also change.

Here are the commands in text format.

1. ClearAll[Z, t, y, Zi, Wi, Xi, X, y0, y10, i, i1, n, ZAns]

2. Z := -2 y y1;

3. y0 = 0

4. y10 = 1

5. n = 15;

6. X := y0 + t y10

7. Zi[3] = (Z /. t -> ti[3])

8. For[i = 3, i i++, (Zi[i + 1] = D[Zi, y]*(y1) + D[Zi, y1]*(Z /. t -> ti[i + 1]))]**

9. For[i = 3, i  = (Zi[i] /. {y -> y0, y1 -> y10}))]**

10. For[i = 3, i

  For[i1 = i, i1 >= 2, i1--, (Xi[i1 - 1] = Integrate[Xi[i1], {ti[i1], 0, ti[i1 - 1]}])];

  X = X + (Xi[i1] /. ti[1] -> t);)]

11. ZAns = Collect[X, t, Simplify] // PolynomialForm[#, TraditionalOrder -> False] &*

---

### #210 — Amin (Topic Author)
*December 24, 2016, 11:52 AM*

In cases of some ODEs that have complicated expressions in independent variable, many times addition of each next
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

On the related question of solution of PDEs, there are several analytic techniques like many versions of separation of variables that transform the PDEs into ODEs that can easily be solved by the method of iterated integrals. here is initial reference https://en.wikipedia.org/wiki/Separation_of_variables and many people have done very advanced research on solution of navier stokes, fokker plank, Laplace equation, wave equation and many other PDEs after converting them into ODEs. I hope many other smart friends would want to explore doing more research in this area.

---

### #211 — Cuchulainn
*December 24, 2016, 12:30 PM*

*On the related question of solution of PDEs, there are several analytic techniques like many versions of separation of
variables that transform the PDEs into ODEs that can easily be solved by the method of iterated integrals.*

Separation of variables (they don't work except in toy examples)  is quite a crude method. It avoids existence and
uniqueness theorems. Nit-picking, SoV leads to Boundary Value Problems while your ODE are Initial Value Problems, a
completely different kettle of fish!!!!!

Even when it does work, SOV needs hairy orthogonal polynomials on non-bounded domains.

I don't see a high ROI in this context.

It's much easier, more robust and mathematically justified  to solve PDEs by FDM and MOL and be done with it. SoV is
school maths, to be honest and not worthy of  your attention.

A good advice is to learn Mathematica. And C++

[https://www.quantnet.com/forum/c-progra ... eering.61/](https://www.quantnet.com/forum/c-programming-for-financial-engineering.61/)

---

### #212 — Cuchulainn
*December 24, 2016, 1:29 PM*

.Furthermore, on the subject of ODEs hardly anyone does it by hand these days. Computers do it MUCH better.

[viewtopic.php?f=34&t=94057&p=662845&hilit=boost#p662845](https://forum.wilmott.com/viewtopic.php?f=34&t=94057&p=662845&hilit=boost#p662845)

*Suggestion: the thread title can be seen as misleading. Maybe a title that is more in line with its contents would
help? just my 2 cents on this.*

---

### #213 — Amin (Topic Author)
*December 24, 2016, 4:29 PM*

>  SoV leads to Boundary Value Problems while your ODE are Initial Value Problems, a completely different kettle of
fish!!!!!
>
Thank you for indicating. I was not looking at boundary value problems initially so did not try to include them in my
paper. I had expanded my original integral equation around t0 for the initial integral and all of the derivatives in
higher iterated integrals. It could certainly be possible to expand the original terms and its higher derivatives
 around terminal time T, or any other intermediate time in a way that formal definition of the original integral is
satisfied by the expansion in terms of iterated integrals using appropriate integration limits. My initial derivation
was intuitive as a start but I believe there is no need to strictly expand around initial time. I am very sure that
boundary value problems can be solved by this method as well. Please give me a day or two and I will present some worked
out examples here.

---

### #214 — Paul
*December 24, 2016, 5:12 PM*

A really easy one should be valuing a call option in the BS framework.

(Cuch, no hints pls.)

---

### #215 — Amin (Topic Author)
*December 25, 2016, 2:31 AM*

> A really easy one should be valuing a call option in the BS framework.
Thank you for your suggestion Paul. It is a real goal to do what you proposed but it might be a week ahead given its
priority with respect to other things to be done. Thanks though for the great suggestion in applied finance setting.

---

### #216 — Amin (Topic Author)
*December 25, 2016, 3:32 AM*

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
If you would ever want to analyze the above series using the results of program given in post 209, you would want the
results for solution of each set of iterated integral terms and that can easily be done by modifying the command 10 in
program in post 209 so that it gives solution of each iterated integrals in addition to one simplified solution(using
next command (11)).  Thenew command (10) would be

$\text{For}*=\text{Wi};\text{Print}[i-1];$

$\text{For}[\text{i1}=i,\text{i1}\geq 2,\text{i1}\text{--},(\text{Xi}[\text{i1}-1]=\text{Integrate}[\text{Xi}[\text{i1}],\{\text{ti}[\text{i1}],0,\text{ti}[\text{i1}-1]\}])];$

$X=X+(\text{Xi}[\text{i1}]\text{/.}\text{ti}[1]\to t);\text{Print}[\text{Xi}[\text{i1}]\text{/.}\text{ti}[1]\to t]]$

For[i = 3, i  = Wi; Print[i-1];For[i1 = i, i1 >= 2, i1--, (Xi[i1 - 1] = Integrate[Xi[i1], {ti[i1], 0, ti[i1 - 1]}])];

  X = X + (Xi[i1] /. ti[1] -> t); Print[Xi[i1] /. ti[1] -> t]]*

---

### #217 — Amin (Topic Author)
*December 25, 2016, 11:37 AM*

For the boundary value problems, we are given the following problem to solve

$y''=f\left(\tau ,y(\tau ),y'(\tau )\right)$,    $y\left(t_0\right)=y_0$,   $y(T)=y_T$

The formal solution to $y(T)$ is given as

$y(T)=y\left(t_0\right)+y'\left(t_0\right)\int _{t_0}^Td\tau +\int _{t_0}^T\int _{t_0}^{\tau }f\left(s,y(s),y'(s)\right)dsd\tau$
Equation(A)

Mostly, we can solve the above integral with method of iterated integrals in terms of generic initial values and once
all the values and boundaries are substituted in solution of Equation(A), the only unknown in the equation after the
solution from the method of iterated integrals is$y'\left(t_0\right)$ which can readily be found to give us the solution
to the boundary value problem. This is the particular value of$y'\left(t_0\right)$ that makes sure that$y(T)=y_T$ is
satisfied. Once we have found this, we have a general solution given by initial value problem where$y'\left(t_0\right)$
has been appropriately chosen so that boundary is satisfied. the solution for$y(t)$ , tOne caveat is that we have to
find enough terms in the solution so that series solution of Equation (A) converges given the terminal time T. Many
times this will not be a problem. We have to consider that exponential and many other functions are internally
calculated by the computer as a series and similarly we could find enough terms in the series solution by the method of
iterated integrals for the answer to be exact. If it is not possible for the solution to be exact and the problem must
be solved, it could be possible to use numerical stepping with root finding of$y'\left(t_0\right)$ to get the answer to
boundary value problem.

Incidentally, we could similarly solve boundary+multiple intermediate value problems given higher order ODEs. For
example, in case of a third order ODE, the value of initial 1st order derivative could fix one intermediate point while
the value of initial second order derivative could fix the boundary. Though of course, totally arbitrary points could
not be interpolated and only the ones who lie in the set of possible solutions could be solved for.

---

### #218 — Cuchulainn
*December 25, 2016, 12:44 PM*

The above is  called a two-point boundary value problem. I think you have trivialised these problems  with 'formal
mathematics" without having researched this huge topic.

There might be hope by transforming BVP to IVP using

https://en.wikipedia.org/wiki/Shooting_method

You can make it credible by implementing Paul's suggestion and stick to one problem A-Z. The discussion is all over the
place.

I am not convinced. What will happen is that the method produces a series solution which may be DIVERGENT.

---

### #219 — Amin (Topic Author)
*December 25, 2016, 1:39 PM*

> The above is  called a two-point boundary value problem. I think you have trivialised these problems  with 'formal
mathematics" without having researched this huge topic.
>
> There might be hope by transforming BVP to IVP using
Thank you for your critical comments Cuch. I have edited post 217 and tried to explain better in the post 217. I hope
this is more accessible now. Yes this is like transforming from BVP to IVP as you have suggested.

---

### #220 — list1
*December 25, 2016, 3:01 PM*

> For the boundary value problems, we are given the following problem to solve
>
>
>
> $y''=f\left(\tau ,y(\tau ),y'(\tau )\right)$,    $y\left(t_0\right)=y_0$,   $y(T)=y_T$
>
>
>
> The formal solution to $y(T)$ is given as
>
>
$y(T)=y\left(t_0\right)+y'\left(t_0\right)\int _{t_0}^Td\tau +\int _{t_0}^T\int _{t_0}^{\tau }f\left(s,y(s),y'(s)\right)dsd\tau$
Equation(A)
>
>
>
> Mostly, we can solve the above integral with method of iterated integrals in terms of generic initial values and once
all the values and boundaries are substituted in solution of Equation(A), the only unknown in the equation after the
solution from the method of iterated integrals is$y'\left(t_0\right)$ which can readily be found to give us the solution
to the boundary value problem. This is the particular value of$y'\left(t_0\right)$ that makes sure that$y(T)=y_T$ is
satisfied. Once we have found this, we have a general solution given by initial value problem where$y'\left(t_0\right)$
has been appropriately chosen so that boundary is satisfied. the solution for$y(t)$ , t
>
>
>
$y(t)=y\left(t_0\right)+y'\left(t_0\right)\int _{t_0}^td\tau +\int _{t_0}^t\int _{t_0}^{\tau }f\left(s,y(s),y'(s)\right)dsd\tau$
>
> with the particular value of$y'\left(t_0\right)$ that makes sure that$y(T)=y_T$ and has been calculated from the
solution of Equation (A) above by method of iterated integrals as earlier described.
>
>
>
> One caveat is that we have to find enough terms in the solution so that series solution of Equation (A) converges
given the terminal time T. Many times this will not be a problem. We have to consider that exponential and many other
functions are internally calculated by the computer as a series and similarly we could find enough terms in the series
solution by the method of iterated integrals for the answer to be exact. If it is not possible for the solution to be
exact and the problem must be solved, it could be possible to use numerical stepping with root finding of
$y'\left(t_0\right)$ to get the answer to boundary value problem.
>
> Incidentally, we could similarly solve boundary+multiple intermediate value problems given higher order ODEs. For
example, in case of a third order ODE, the value of initial 1st order derivative could fix one intermediate point while
the value of initial second order derivative could fix the boundary. Though of course, totally arbitrary points could
not be interpolated and only the ones who lie in the set of possible solutions could be solved for.
I did not read all messages to this post and therefore can be wrong. Nevertheless a couple remarks.

I can assume that the iterated series converges on [ 0 , T ] but

1. it would be looks good to prove it.

 The problem and methods used are typical mathematics. Also it might make sense to illustrate the problem with examples
when the problem has analytical ( explicit ) solution and iterated series can be represented in closed form.

2. Show that the sum is a solution of the problem on ( 0 , T )continuous on [ 0 , T ] .

---

### #221 — Cuchulainn
*December 25, 2016, 4:36 PM*

> For the boundary value problems, we are given the following problem to solve
>
>
>
> $y''=f\left(\tau ,y(\tau ),y'(\tau )\right)$,    $y\left(t_0\right)=y_0$,   $y(T)=y_T$
>
>
>
> The formal solution to $y(T)$ is given as
>
>
$y(T)=y\left(t_0\right)+y'\left(t_0\right)\int _{t_0}^Td\tau +\int _{t_0}^T\int _{t_0}^{\tau }f\left(s,y(s),y'(s)\right)dsd\tau$
Equation(A)
>
>
>
> Mostly, we can solve the above integral with method of iterated integrals in terms of generic initial values and once
all the values and boundaries are substituted in solution of Equation(A), the only unknown in the equation after the
solution from the method of iterated integrals is$y'\left(t_0\right)$ which can readily be found to give us the solution
to the boundary value problem. This is the particular value of$y'\left(t_0\right)$ that makes sure that$y(T)=y_T$ is
satisfied. Once we have found this, we have a general solution given by initial value problem where$y'\left(t_0\right)$
has been appropriately chosen so that boundary is satisfied. the solution for$y(t)$ , t
>
>
>
$y(t)=y\left(t_0\right)+y'\left(t_0\right)\int _{t_0}^td\tau +\int _{t_0}^t\int _{t_0}^{\tau }f\left(s,y(s),y'(s)\right)dsd\tau$
>
> with the particular value of$y'\left(t_0\right)$ that makes sure that$y(T)=y_T$ and has been calculated from the
solution of Equation (A) above by method of iterated integrals as earlier described.
>
>
>
> One caveat is that we have to find enough terms in the solution so that series solution of Equation (A) converges
given the terminal time T. Many times this will not be a problem. We have to consider that exponential and many other
functions are internally calculated by the computer as a series and similarly we could find enough terms in the series
solution by the method of iterated integrals for the answer to be exact. If it is not possible for the solution to be
exact and the problem must be solved, it could be possible to use numerical stepping with root finding of
$y'\left(t_0\right)$ to get the answer to boundary value problem.
>
> Incidentally, we could similarly solve boundary+multiple intermediate value problems given higher order ODEs. For
example, in case of a third order ODE, the value of initial 1st order derivative could fix one intermediate point while
the value of initial second order derivative could fix the boundary. Though of course, totally arbitrary points could
not be interpolated and only the ones who lie in the set of possible solutions could be solved for.
I did not read all messages to this post and therefore can be wrong. Nevertheless a couple remarks.

I can assume that the iterated series converges on [ 0 , T ] but

1. it would be looks good to prove it.

 The problem and methods used are typical mathematics. Also it might make sense to illustrate the problem with examples
when the problem has analytical ( explicit ) solution and iterated series can be represented in closed form.

2. Show that the sum is a solution of the problem on ( 0 , T )continuous on [ 0 , T ] .
Actually (just came into my head, in bed with pneumonia) posed a 2d integral (what essentially Amin is doing) as a
Goursat PDE for the 2d bivariate cdf that i solve using FDM; ts is accurate, fast and list's conditions can be checked.

[http://epubs.siam.org/doi/abs/10.1137/0 ... e=smjmap.1](http://epubs.siam.org/doi/abs/10.1137/0108036?journalCode=smjmap.1)

Now, even the extension to 3d I have also done as $u_{xyz} = f(x,y,z)$

Here is FDM for Goursat

http://file.scirp.org/pdf/OALibJ_2016030814540238.pdf

It might be coincidence but there is  spark here?

---

### #222 — list1
*December 25, 2016, 4:59 PM*

Cuch, I wish you to get better and meet 2017 in a good healthy condition with good brandy or wine.

Nevertheless two point second order ODE which is written above my message does not remind me Goursat PDE. Though my
remark also make sense for Goursat problem too

---

### #223 — Amin (Topic Author)
*December 26, 2016, 4:33 PM*

Here is the way to solve a system of differential equations using the method of iterated integrals.

Let us write the problem of a system of two first order differential equations with initial conditions.

$y'=f(\tau ,y(\tau ),u(\tau ))$,     $y\left(t_0\right)=y_0$

$u'=g(\tau ,y(\tau ),u(\tau ))$,    $u\left(t_0\right)=u_0$

Just following the logic of the method as given for the first and second order ODEs, I will write the first few iterated
integrals terms of the solution to each dependent variable in the system of two first order differential equations.
Since in general each variable in the system of two first order equations depends upon both variables in the system, we
have to differentiate each of the differential equations with respect to both variables and then convert everything into
derivative with respect to independent variable using both differential equations posed in the problem while evaluating
each dependent variable in the solution of iterated integrals conveniently at its initial(or possibly some other) value.

$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right) \, d\tau$

$+\int _{t_0}^t\int _{t_0}^{\tau }\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right.$

$\left.+\frac{\partial }{\partial u}\left[f\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]g\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right]dsd\tau$

$+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right.\right.$

$\left.\left.+\frac{\partial }{\partial u}\left[f\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]g\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right]f\left(v,y\left(t_0\right),u\left(t_0\right)\right)\right]dvdsd\tau$

$+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\left[\frac{\partial }{\partial u}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right.\right.$

$\left.\left.+\frac{\partial }{\partial u}\left[f\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]g\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right]g\left(v,y\left(t_0\right),u\left(t_0\right)\right)\right]dvdsd\tau$

$+\text{higher} \text{Order} \text{Integral} \text{terms}$

$u(t)=u\left(t_0\right)+\int_{t_0}^t g\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right) \, d\tau$

$+\int _{t_0}^t\int _{t_0}^{\tau }\left[\frac{\partial }{\partial y}\left[g\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right.$

$\left.+\frac{\partial }{\partial u}\left[g\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]g\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right]dsd\tau$

$+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[g\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right.\right.$

$\left.\left.+\frac{\partial }{\partial u}\left[g\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]g\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right]f\left(v,y\left(t_0\right),u\left(t_0\right)\right)\right] dvdsd\tau$

$+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\left[\frac{\partial }{\partial u}\left[\frac{\partial }{\partial y}\left[g\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right.\right.$

$\left.\left.+\frac{\partial }{\partial u}\left[g\left(\tau ,y\left(t_0\right),u\left(t_0\right)\right)\right]g\left(s,y\left(t_0\right),u\left(t_0\right)\right)\right]g\left(v,y\left(t_0\right),u\left(t_0\right)\right)\right]dvdsd\tau$

$+\text{higher} \text{Order} \text{Integral} \text{terms}$

The way I have written equations there are two third order iterated integral terms in solution to each variable and both
terms could have been written together in one third order integral as one term. Systems of large number of equations and
systems of higher order differential equations can also be very easily solved.

I will soon be posting an automated mathematica code to deal with solution to systems of first order differential
equations with a few worked out examples.

---

### #224 — list1
*December 26, 2016, 5:10 PM*

Amin, in your reduction one condition should be at one end other condition should be on other end of the interval. Other
observation is that if you do not make some assumptions your transformed problem should be the same complexity as the
initial problem. The role of assumptions is to specify a particular case of the initial complex problem when you can get
a solution or approximation of the solution.

The straightforward substitution you use does not suggest that outcome is simpler than original problem.

---

### #225 — Amin (Topic Author)
*December 27, 2016, 2:42 PM*

Here is a small program to calculate the analytic series solution for a system of m first order equations. Here is the
very simple problem on which I used it

$x'=y$,  $x(0)=x_0=1$

$y'=6x-y$,   $y(0)=y_0=-2$

In the following mathematica code, I have replaced  x by y[1], and y by y[2] and so on till y[m] for a set of m first
order differential equations. Of course all the differential equations would have to be input by hand but I have tried
to automate it as much as possible.

Here is some explanation to use the problem. Command 2 defines the number of first order equations in the system. I have
explicitly defined arrays/list varaibles as compared to previous programs. In command (5) and (6) you have to specify
the ODEs. Command (7) defines an array of inital values that is populated in command (8) and (9) which can be omitted in
case of general initial values. Command (15) defines the number of iterated integral terms that will be included in the
expansion. The brain of the method is in command 17, 18, 19, 20 the last three of which have three loops each. command
21 gives the answer which I have calculated and compared with closed form solution. I have shown the series solution at
the end.

1.$\text{ClearAll}[Z,t,y,\text{Zi},\text{Wi},\text{Xi},X,\text{y0},i,\text{i1},m,n,\text{ZAns}]$

2.$m=2;$

3.$\text{Array}[Z,m]$

4.$\text{Array}[y,m]$

5.$Z[1]\text{:=}y[2]$

6.$Z[2]\text{:=}6 y[1]-y[2]$

7.$\text{Array}[\text{y0},m]$

8.$\text{y0}[1]=1$

9.$\text{y0}[2]=-2$

10.$n=15;$

11.$\text{Array}[X,m]$

12.$\text{For}[j=1,j\leq m,j\text{++},X[j]\text{:=}\text{y0}[j]]$

13.$\text{Array}[\text{Zi},m,n+1];$

14,$\text{Array}[\text{Wi},m,n+1];$

15,$\text{Array}[\text{Xi},m,n+1];$

16.$\text{Array}[\text{ti},n+1];$

17.$\text{For}[j=1,j\leq m,j\text{++},\text{Zi}[j][2]=(Z[j]\text{/.}t\to \text{ti}[2]);]$

18.$\text{For}[j=1,j \text{ti}[i + 1]));]);]);];$

19.$\text{For}[j=1,j\leq m,j\text{++},(\text{For}=\text{Zi}[j];$

$\text{For}[k=1,k\leq m,k\text{++},(\text{Wi}[j]=(\text{Wi}[j]\text{/.}y[k]\to \text{y0}[k]))]]);];$

20.$\text{For}[j=1,j\leq m,j\text{++},(\text{For}=\text{Wi}[j];$

$\text{For}[\text{i1}=i,\text{i1}\geq 2,\text{i1}\text{--},(\text{Xi}[j][\text{i1}-1]=\text{Integrate}[\text{Xi}[j][\text{i1}],\{\text{ti}[\text{i1}],0,\text{ti}[\text{i1}-1]\}])];$

$X[j]=X[j]+(\text{Xi}[j][1]\text{/.}\text{ti}[1]\to t);)]]$

21.$\text{For}[j=1,j\leq m,j\text{++},(\text{ZAns}[j]=\text{Collect}[X[j],t,\text{Simplify}]$

$\text{//}\text{PolynomialForm}[\#,\text{TraditionalOrder}\to \text{False}]\&)]$

Here is the output which exactly matches with the true answer for reasonable values of t.

$ZAns[1]$

$1-2 t+4 t^2-\frac{10 t^3}{3}+\frac{17 t^4}{6}-\frac{47 t^5}{30}+\frac{149 t^6}{180}-\frac{431 t^7}{1260}+\frac{265 t^8}{2016}$

$-\frac{3911 t^9}{90720}+\frac{11861 t^{10}}{907200}-\frac{35327 t^{11}}{9979200}+\frac{106493 t^{12}}{119750400}-\frac{63691 t^{13}}{311351040}+\frac{957413 t^{14}}{21794572800}$

$ZAns[2]$

$-2+8 t-10 t^2+\frac{34 t^3}{3}-\frac{47 t^4}{6}+\frac{149 t^5}{30}-\frac{431 t^6}{180}+\frac{265 t^7}{252}-\frac{3911 t^8}{10080}$

$+\frac{11861 t^9}{90720}-\frac{35327 t^{10}}{907200}+\frac{106493 t^{11}}{9979200}-\frac{63691 t^{12}}{23950080}+\frac{957413 t^{13}}{1556755200}-\frac{2868143 t^{14}}{21794572800}$

Here is the program in text format.

1.ClearAll[Z, t, y, Zi, Wi, Xi, X, y0, i, i1, m, n, ZAns]

2. m = 2;

3. Array[Z, m]

4. Array[y, m]

5. Z[1] := y[2]

6. Z[2] := 6 y[1] - y[2]

7. Array[y0, m]

8. y0[1] = 1

9. y0[2] = -2

10. n = 15;

11. Array[X, m]

12. For[j = 1, j  ti[2]);]

18. For[j = 1, j j++ , (For[i = 2, i i++, (Zi[j][i + 1] = 0;

       For[k = 1, k k++,

      (Zi[j][i + 1] =Zi[j][i + 1] +D[Zi[j], y[k]]*(Z[k] /. t -> ti[i + 1]));]);]);];**

19. For[j = 1, j j++, (For[i = 2, i i++, (Wi[j][i] = Zi[j][i];

      For[k = 1, k  y0[k]))]]);];

20. For[j = 1, j = 2, i1--, (Xi[j][i1 - 1] = Integrate[Xi[j][i1], {ti[i1], 0, ti[i1 - 1]}])];

     X[j] = X[j] + (Xi[j][1] /. ti[1] -> t);)]]

21. For[j = 1, j

 (ZAns[j] = Collect[X[j], t, Simplify] // PolynomialForm[#, TraditionalOrder -> False] &)]*

---

### #226 — Amin (Topic Author)
*December 30, 2016, 9:11 PM*

My revised paper would be ready in a few days. Meanwhile here is a general program for nth order ODE. I have tried it on
the following third order ODE.

$y'''=-\left(t^2-2t+5\right)y''-(t-8)y'+4y$,   $y(0)=y_0=1$,   $y'(0)=y'_0=0$,  $y''(0)=y''_0=0$

Here is the mathematica code for the nth order ODEs

1. $\text{Clear}[t,y,\text{Zi},\text{Wi},\text{Yi},Y,\text{y0},i,\text{i1},m,n,\text{ZAns}]$

2. $n=3;$

3. $\text{Array}[y,n+1,0];$

4. $y[3]\text{:=}-\left(t^2-2t+5\right)y[2]-(t-8)y[1]+4y[0];$

5. $\text{Array}[\text{y0},n,0];$

6. $\text{y0}[0]=1;$

7. $\text{y0}[1]=0;$

8. $\text{y0}[2]=0;$

9. $m=10;$

10. $Y\text{:=}\text{y0}[0];$

11. $\text{For}\left[k=1,k,y[k]]*(y[k+1]\text{/.}t\to \text{ti}[i+1]));]);];$

18. $\text{For}=\text{Zi};$

$\text{For}[k=0,k=(\text{Wi}\text{/.}y[k]\to \text{y0}[k]))]];$

19. $\text{For}=\text{Wi};$

$\text{For}[\text{i1}=i,\text{i1}\geq 1,\text{i1}\text{--},(\text{Yi}[\text{i1}-1]=\text{Integrate}[\text{Yi}[\text{i1}],\{\text{ti}[\text{i1}],0,\text{ti}[\text{i1}-1]\}])];$

$Y=Y+(\text{Yi}[0]\text{/.}\text{ti}[0]\to t);)];$

20.
$\text{ZAns}=\text{Collect}[Y,t,\text{Simplify}]\text{//}\text{PolynomialForm}[\#,\text{TraditionalOrder}\to \text{False}]\&$

Here is the output of the program:

$1+\frac{2 t^3}{3}-\frac{5 t^4}{6}+\frac{37 t^5}{30}-\frac{13 t^6}{9}+\frac{488 t^7}{315}-\frac{15217 t^8}{10080}+\frac{3527 t^9}{2592}-\frac{346613 t^{10}}{302400}$

$+\frac{604993 t^{11}}{665280}-\frac{5851111 t^{12}}{8553600}+\frac{99059131 t^{13}}{222393600}-\frac{5515344179 t^{14}}{21794572800}+\frac{282742837 t^{15}}{2286144000}-\frac{2129736739 t^{16}}{40236134400}+\frac{294469674259 t^{17}}{14820309504000}-\frac{41387702887 t^{18}}{6252318072000}$

$+\frac{3724417254023 t^{19}}{1900704693888000}-\frac{4927551036823 t^{20}}{9503523469440000}+\frac{8883103150331 t^{21}}{72572361039360000}-\frac{2024005375607 t^{22}}{78404068622880000}$

$+\frac{19521921165283 t^{23}}{4039377615450777600}-\frac{55406789656619 t^{24}}{69246473407727616000}+\frac{45276924013 t^{25}}{392020343114400000}-\frac{351185810849 t^{26}}{24462069410338560000}$

$+\frac{118838862811 t^{27}}{79952342651685504000}-\frac{9751 t^{28}}{78835165373952}+\frac{1458473 t^{29}}{196974499673952000}-\frac{t^{30}}{3706422720000}$

The nomenclature of the program has changed. The indexing now starts at zero and is better to understand and relate with
variables and their derivatives.  In the above program y[0] stands for y(t), y[1] stands for first derivative, y[2]
stands for second derivative and so on. n represents the order of the ODE. m stands for the number of iterated integral
terms involved in the series expansion. y0[0], y0[1], y0[2] stand for the initial values of y(t) and its derivatives.
The series solution result is output in Capital Y as opposed to (confusing) X in previous versions. The algorithm is the
same as for earlier versions but slightly better at places in indexing and names of variables.

Here is the mathematica code in text format.

1. Clear[t, y, Zi, Wi, Yi, Y, y0, i, i1, m, n, ZAns];

2. n = 3;

3. Array[y, n + 1, 0];

4. y[3] := -(t^2 - 2 t + 5) y[2] - (t - 8) y[1] + 4 y[0];

5. Array[y0, n, 0];

6. y0[0] = 1;

7. y0[1] = 0;

8. y0[2] = 0;

9. m = 10;

10. Y := y0[0];

11. For[k = 1, k  ti[n]);

17. For[i = n, i  k++, (Zi[i + 1] = Zi[i + 1] + D[Zi, y[k]]*(y[k + 1] /. t -> ti[i + 1]));]);];**

18. For[i = n, i  = Zi[i];**

For[k = 0, k  y0[k]))]];

19. For[i = n, i

   For[i1 = i, i1 >= 1,i1--, (Yi[i1 - 1] = Integrate[Yi[i1], {ti[i1], 0, ti[i1 - 1]}])];

   Y = Y + (Yi[0] /. ti[0] -> t);)];

20. ZAns = Collect[Y, t, Simplify] // PolynomialForm[#, TraditionalOrder -> False] &*

---

### #227 — Amin (Topic Author)
*December 31, 2016, 5:58 PM*

**(broken latex: Unbalanced $: 61)**

```latex
I had been working to include some material on solution of systems of possibly non-linear ordinary higher order
differential equations in my paper. I have written some mathematica code for the solution of system of m ordinary
differential equations each of which could have different order and the code would solve the system. I have tried it on
a system of three second order non-linear differential equations. Here are the system ODEs and the mathematica code.

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

### #228 — Cuchulainn
*January 2, 2017, 12:37 PM*

These formulae make me shudder.. What do you do with them after Mathematica churn out a solution?

Some issues still remain:

1. in which interval [0, T] does a solution exist?

2. How do I numerically compute a solution for a specific value of t?

3. What's the compelling reason for using this model? Why not just plug it into an ODE solver and be done with it?

Still, you might be on to something, I have a feeling one of those 19th century guys (Goursat, Darboux) must have done
something like this?

---

### #229 — Cuchulainn
*January 2, 2017, 1:36 PM*

> Here is a small program to calculate the analytic series solution for a system of m first order equations. Here is the
very simple problem on which I used it
>
>
>
> $x'=y$,  $x(0)=x_0=1$
>
> $y'=6x-y$,   $y(0)=y_0=-2$
>
>
>
> In the following mathematica code, I have replaced  x by y[1], and y by y[2] and so on till y[m] for a set of m first
order differential equations. Of course all the differential equations would have to be input by hand but I have tried
to automate it as much as possible.
>
> Here is some explanation to use the problem. Command 2 defines the number of first order equations in the system. I
have explicitly defined arrays/list varaibles as compared to previous programs. In command (5) and (6) you have to
specify the ODEs. Command (7) defines an array of inital values that is populated in command (8) and (9) which can be
omitted in case of general initial values. Command (15) defines the number of iterated integral terms that will be
included in the expansion. The brain of the method is in command 17, 18, 19, 20 the last three of which have three loops
each. command 21 gives the answer which I have calculated and compared with closed form solution. I have shown the
series solution at the end.
>
>
>
> 1.$\text{ClearAll}[Z,t,y,\text{Zi},\text{Wi},\text{Xi},X,\text{y0},i,\text{i1},m,n,\text{ZAns}]$
>
> 2.$m=2;$
>
> 3.$\text{Array}[Z,m]$
>
> 4.$\text{Array}[y,m]$
>
> 5.$Z[1]\text{:=}y[2]$
>
> 6.$Z[2]\text{:=}6 y[1]-y[2]$
>
> 7.$\text{Array}[\text{y0},m]$
>
> 8.$\text{y0}[1]=1$
>
> 9.$\text{y0}[2]=-2$
>
> 10.$n=15;$
>
> 11.$\text{Array}[X,m]$
>
> 12.$\text{For}[j=1,j\leq m,j\text{++},X[j]\text{:=}\text{y0}[j]]$
>
> 13.$\text{Array}[\text{Zi},m,n+1];$
>
> 14,$\text{Array}[\text{Wi},m,n+1];$
>
> 15,$\text{Array}[\text{Xi},m,n+1];$
>
> 16.$\text{Array}[\text{ti},n+1];$
>
> 17.$\text{For}[j=1,j\leq m,j\text{++},\text{Zi}[j][2]=(Z[j]\text{/.}t\to \text{ti}[2]);]$
>
>
>
> 18.
$\text{For}[j=1,j> [\text{](\text{For}[i = 2, i > [\text{](\text{Zi}[j][i + 1]=0;\text{For}[k=1,k> [\text{](\text{Zi}[j][i + 1]=\text{Zi}[j][i + 1] + D[\text{Zi}[j]*, y[k]]*(Z[k] \text{/.} t \text{-}> \text{ti}[i + 1]));]);]);];$
>
>
>
> 19.$\text{For}[j=1,j\leq m,j\text{++},(\text{For}=\text{Zi}[j];$
>
> $\text{For}[k=1,k\leq m,k\text{++},(\text{Wi}[j]=(\text{Wi}[j]\text{/.}y[k]\to \text{y0}[k]))]]);];$
>
>
>
> 20.$\text{For}[j=1,j\leq m,j\text{++},(\text{For}=\text{Wi}[j];$
>
>
$\text{For}[\text{i1}=i,\text{i1}\geq 2,\text{i1}\text{--},(\text{Xi}[j][\text{i1}-1]=\text{Integrate}[\text{Xi}[j][\text{i1}],\{\text{ti}[\text{i1}],0,\text{ti}[\text{i1}-1]\}])];$
>
> $X[j]=X[j]+(\text{Xi}[j][1]\text{/.}\text{ti}[1]\to t);)]]$
>
>
>
> 21.$\text{For}[j=1,j\leq m,j\text{++},(\text{ZAns}[j]=\text{Collect}[X[j],t,\text{Simplify}]$
>
> $\text{//}\text{PolynomialForm}[\#,\text{TraditionalOrder}\to \text{False}]\&)]$
>
>
>
> Here is the output which exactly matches with the true answer for reasonable values of t.
>
> $ZAns[1]$
>
>
$1-2 t+4 t^2-\frac{10 t^3}{3}+\frac{17 t^4}{6}-\frac{47 t^5}{30}+\frac{149 t^6}{180}-\frac{431 t^7}{1260}+\frac{265 t^8}{2016}$
>
>
$-\frac{3911 t^9}{90720}+\frac{11861 t^{10}}{907200}-\frac{35327 t^{11}}{9979200}+\frac{106493 t^{12}}{119750400}-\frac{63691 t^{13}}{311351040}+\frac{957413 t^{14}}{21794572800}$
>
>
>
> $ZAns[2]$
>
>
$-2+8 t-10 t^2+\frac{34 t^3}{3}-\frac{47 t^4}{6}+\frac{149 t^5}{30}-\frac{431 t^6}{180}+\frac{265 t^7}{252}-\frac{3911 t^8}{10080}$
>
>
$+\frac{11861 t^9}{90720}-\frac{35327 t^{10}}{907200}+\frac{106493 t^{11}}{9979200}-\frac{63691 t^{12}}{23950080}+\frac{957413 t^{13}}{1556755200}-\frac{2868143 t^{14}}{21794572800}$
>
>
>
>
>
> Here is the program in text format.
>
> 1.ClearAll[Z, t, y, Zi, Wi, Xi, X, y0, i, i1, m, n, ZAns]
>
> 2. m = 2;
>
> 3. Array[Z, m]
>
> 4. Array[y, m]
>
> 5. Z[1] := y[2]
>
> 6. Z[2] := 6 y[1] - y[2]
>
> 7. Array[y0, m]
>
> 8. y0[1] = 1
>
> 9. y0[2] = -2
>
> 10. n = 15;
>
> 11. Array[X, m]
>
> 12. For[j = 1, j
> 13. Array[Zi, m, n + 1];
>
> 14. Array[Wi, m, n + 1];
>
> 15. Array[Xi, m, n + 1];
>
> 16. Array[ti, n + 1];
>
> 17. For[j = 1, j  ti[2]);]
>
>
>
> 18. For[j = 1, j j++ , (For[i = 2, i i++, (Zi[j][i + 1] = 0;
>
>        For[k = 1, k k++,
>
>       (Zi[j][i + 1] =Zi[j][i + 1] +D[Zi[j], y[k]]*(Z[k] /. t -> ti[i + 1]));]);]);];**
>
>
>
> 19. For[j = 1, j j++, (For[i = 2, i i++, (Wi[j][i] = Zi[j][i];
>
>       For[k = 1, k  y0[k]))]]);];
>
>
>
> 20. For[j = 1, j
>      For[i1 = i, i1 >= 2, i1--, (Xi[j][i1 - 1] = Integrate[Xi[j][i1], {ti[i1], 0, ti[i1 - 1]}])];
>
>      X[j] = X[j] + (Xi[j][1] /. ti[1] -> t);)]]
>
>
>
> 21. For[j = 1, j
>
>  (ZAns[j] = Collect[X[j], t, Simplify] // PolynomialForm[#, TraditionalOrder -> False] &)]**

It is possible to double-check the solution of this linear ODE system using matrix exponentials + added benefit of a
solution involving exp:*
[YouTube Video](https://www.youtube.com/embed/)

---

### #230 — Amin (Topic Author)
*January 2, 2017, 2:38 PM*

> These formulae make me shudder.. What do you do with them after Mathematica churn out a solution?
>
>
>
> Some issues still remain:
>
>
>
> 1. in which interval [0, T] does a solution exist?
>
> 2. How do I numerically compute a solution for a specific value of t?
>
>
>
> 3. What's the compelling reason for using this model? Why not just plug it into an ODE solver and be done with it?
>
>
>
> Still, you might be on to something, I have a feeling one of those 19th century guys (Goursat, Darboux) must have done
something like this?
1. in which interval [0, T] does a solution exist?

It is a series solution and I am sure there are many other extensive mathematical methods that can help determine given
a series on which interval it converges and is valid. There is however a very simple mathematica check to determine the
validity of the solution. Let us say I am given an ODE problem and I have found a series solution using the method of
iterated integrals. If the series solution is in t, For any given t, I can plug the series solution in the ODE and see
how well the ODE is satisfied there. IF the error is extremely small, it means that approximation is very good. Let me
explain it with an extremely simple example.

Here is the ODE, I am trying to solve.

$y'=f(\tau ,y(\tau ))=\frac{y}{\sqrt{\tau }},\text{    }y(0)=.5$,   $t_0=0$

I have the series solution to say eight terms here.

$Y=0.5 +1. \sqrt{t}+1. t+0.666667 t^{3/2}+0.333333 t^2+0.133333 t^{5/2}$

$+0.0444444 t^3+0.0126984 t^{7/2}+0.0031746 t^4$

Obviously this solution should satisfy the original ODE. Let us see how well it satisfies the ODE at different values of
t.

I use the mathematica command to evaluate the goodness of solution at t=.05;

$D[Y,t]-\frac{Y}{\sqrt{t}}\text{/.}t\to .05 $ and get the answer -8.87329*10^-8 (This value would be zero if the ODE
would be perfectly satisfied at that value of t given the series solution)

Now I evaluate it at t=.5 using mathematica command

$D[Y,t]-\frac{Y}{\sqrt{t}}\text{/.}t\to .5 $ and get the answer  -0.000280598

let us see what we get at t=1

$D[Y,t]-\frac{Y}{\sqrt{t}}\text{/.}t\to 1 $and I got the answer -0.0031746

Now we try to find how good the solution is at t=5

$D[Y,t]-\frac{Y}{\sqrt{t}}\text{/.}t\to 5$ and I get the answer -0.887329

So you see how the solution deteriorates with increasing time. You could add more terms if you need more accuracy at
larger values of t and you could always plug the series solution in the ODE using mathematica, evaluate it for a certain
value of t and see how close the result is to zero and you could know how good the approximation is.

---

### #231 — ppauper
*January 2, 2017, 3:27 PM*

> Here is a small program to calculate the analytic series solution for a system of m first order equations. Here is the
very simple problem on which I used it
>
>
>
> $x'=y$,  $x(0)=x_0=1$
>
> $y'=6x-y$,   $y(0)=y_0=-2$
>
> (snip)
>
> Here is the output which exactly matches with the true answer for reasonable values of t.
>
> $ZAns[1]$
>
>
$1-2 t+4 t^2-\frac{10 t^3}{3}+\frac{17 t^4}{6}-\frac{47 t^5}{30}+\frac{149 t^6}{180}-\frac{431 t^7}{1260}+\frac{265 t^8}{2016}$
>
>
$-\frac{3911 t^9}{90720}+\frac{11861 t^{10}}{907200}-\frac{35327 t^{11}}{9979200}+\frac{106493 t^{12}}{119750400}-\frac{63691 t^{13}}{311351040}+\frac{957413 t^{14}}{21794572800}$
>
>
>
> $ZAns[2]$
>
>
$-2+8 t-10 t^2+\frac{34 t^3}{3}-\frac{47 t^4}{6}+\frac{149 t^5}{30}-\frac{431 t^6}{180}+\frac{265 t^7}{252}-\frac{3911 t^8}{10080}$
>
>
$+\frac{11861 t^9}{90720}-\frac{35327 t^{10}}{907200}+\frac{106493 t^{11}}{9979200}-\frac{63691 t^{12}}{23950080}+\frac{957413 t^{13}}{1556755200}-\frac{2868143 t^{14}}{21794572800}$
>
> (snip)
It is possible to double-check the solution of this linear ODE system using matrix exponentials + added benefit of a
solution involving exp:
[YouTube Video](https://www.youtube.com/embed/)

even easier, y=x' so you can check by writing it as a 2nd order ODE,

x′=y,

y′=6x−y,

so

x'′=y'=6x−y=6x-x'

yields

x''+x'-6x=0

solution x=C_1 exp(2t)+C_2 exp(-3t)

initial conditions give

x=1/5 exp(2t)+4/5 exp(-3t)

y=x'=2/5 exp(2t)-12/5 exp(-3t)

which agrees with what the maestro had

---

### #232 — Paul
*January 2, 2017, 5:25 PM*

What is the point of doing more and more trivial examples when you haven't addressed any of the real issues here?

Every time you do another example you add further weight to the hypothesis that you don't know the subject.

---

### #233 — Amin (Topic Author)
*January 2, 2017, 5:43 PM*

> What is the point of doing more and more trivial examples when you haven't addressed any of the real issues here?
>
>
>
> Every time you do another example you add further weight to the hypothesis that you don't know the subject.
>
Sorry. Yes the example was totally trivial and I fully agree with you on that. But the purpose was to share general code
to solve first order systems (and later I shared code for system of arbitrary order ODEs) and I am sure if you run the
code on far more complex problems, it would perfectly work. You could work with the code to solve for a system of
non-linear ODEs if you like.

Regarding some issues you mentioned, I would like to add that I am adding material to my paper regarding the solution to
singular initial value problems. As with many other methods of solution of the ODEs, you have to treat the singular
problems first to make it suitable for solution by the method of iterated integrals and the standard theory regarding
various transformations for that applies here as well.

---

### #234 — Amin (Topic Author)
*January 2, 2017, 6:23 PM*

For friends, here is the solution to Lane-Emden ODE which is a singular initial value problem that I thought I would be
adding to my paper. Here are some initial notes I made.

![Image](https://i.imgsafe.org/a987c2e504.jpg)![Image](https://i.imgsafe.org/a987fef880.jpg)

---

### #235 — Cuchulainn
*January 2, 2017, 7:45 PM*

Lane-Emden ODE has exact solution which look benign enough.

[https://en.wikipedia.org/wiki/Lane%E2%8 ... n_equation](https://en.wikipedia.org/wiki/Lane%E2%80%93Emden_equation)

BTW your definition of LE ODE differs from above.

---

### #236 — Amin (Topic Author)
*January 3, 2017, 12:34 AM*

Cuch, you are right. Thanks for pointing out. Yes, it is not Lane-Emden, the ODE I solved is poisson-Boltzmann differential equation. [http://mathworld.wolfram.com/Poisson-Bo ... ation.html](http://mathworld.wolfram.com/Poisson-BoltzmannDifferentialEquation.html)

There are many other singular ODEs that would take the same transformation in addition to Poisson-Boltzmann ODEs which I
tried to solve. For example Ivey's equation and Lane-Emden-Fowler class of differential  equations can be similarly
solved using the same transformation I used in the above post. Solution to many of these ODEs are known in case of
special values of parameters but using the method of iterated integrals, we can find a series solution to any arbitrary
parameters.

---

### #237 — Cuchulainn
*January 3, 2017, 9:22 AM*

> Here is a small program to calculate the analytic series solution for a system of m first order equations. Here is the
very simple problem on which I used it
>
>
>
> $x'=y$,  $x(0)=x_0=1$
>
> $y'=6x-y$,   $y(0)=y_0=-2$
>
> (snip)
>
> Here is the output which exactly matches with the true answer for reasonable values of t.
>
> $ZAns[1]$
>
>
$1-2 t+4 t^2-\frac{10 t^3}{3}+\frac{17 t^4}{6}-\frac{47 t^5}{30}+\frac{149 t^6}{180}-\frac{431 t^7}{1260}+\frac{265 t^8}{2016}$
>
>
$-\frac{3911 t^9}{90720}+\frac{11861 t^{10}}{907200}-\frac{35327 t^{11}}{9979200}+\frac{106493 t^{12}}{119750400}-\frac{63691 t^{13}}{311351040}+\frac{957413 t^{14}}{21794572800}$
>
>
>
> $ZAns[2]$
>
>
$-2+8 t-10 t^2+\frac{34 t^3}{3}-\frac{47 t^4}{6}+\frac{149 t^5}{30}-\frac{431 t^6}{180}+\frac{265 t^7}{252}-\frac{3911 t^8}{10080}$
>
>
$+\frac{11861 t^9}{90720}-\frac{35327 t^{10}}{907200}+\frac{106493 t^{11}}{9979200}-\frac{63691 t^{12}}{23950080}+\frac{957413 t^{13}}{1556755200}-\frac{2868143 t^{14}}{21794572800}$
>
> (snip)
It is possible to double-check the solution of this linear ODE system using matrix exponentials + added benefit of a
solution involving exp:
[YouTube Video](https://www.youtube.com/embed/)

even easier, y=x' so you can check by writing it as a 2nd order ODE,

x′=y,

y′=6x−y,

so

x'′=y'=6x−y=6x-x'

yields

x''+x'-6x=0

solution x=C_1 exp(2t)+C_2 exp(-3t)

initial conditions give

x=1/5 exp(2t)+4/5 exp(-3t)

y=x'=2/5 exp(2t)-12/5 exp(-3t)

which agrees with what the maestro had
Neat, avoids computing eigenvectors (and matrix inversion).

---

### #238 — Cuchulainn
*January 3, 2017, 9:25 AM*

> Cuch, you are right. Thanks for pointing out. Yes, it is not Lane-Emden, the ODE I solved is poisson-Boltzmann differential equation. [http://mathworld.wolfram.com/Poisson-Bo ... ation.html](http://mathworld.wolfram.com/Poisson-BoltzmannDifferentialEquation.html)
>
> There are many other singular ODEs that would take the same transformation in addition to Poisson-Boltzmann ODEs which
I tried to solve. For example Ivey's equation and Lane-Emden-Fowler class of differential  equations can be similarly
solved using the same transformation I used in the above post. Solution to many of these ODEs are known in case of
special values of parameters but using the method of iterated integrals, we can find a series solution to any arbitrary
parameters.
Is it possible to graph the solution on an interval by plugging in values of t using your symbolic series solution?

Most importantly, how can you determine how many terms to take in the series to achieve a desired accuracy?

A random search threw us a almost analytical solution to PB BVP

[http://ac.els-cdn.com/S089571770500169X ... 3f40e414f6](http://ac.els-cdn.com/S089571770500169X/1-s2.0-S089571770500169X-main.pdf?_tid=9535abb6-d19b-11e6-a959-00000aacb360&acdnat=1483437863_9b2cbbc00eda55b4123fa63f40e414f6)

---

### #239 — Amin (Topic Author)
*January 3, 2017, 9:46 AM*

> Cuch, you are right. Thanks for pointing out. Yes, it is not Lane-Emden, the ODE I solved is poisson-Boltzmann differential equation. [http://mathworld.wolfram.com/Poisson-Bo ... ation.html](http://mathworld.wolfram.com/Poisson-BoltzmannDifferentialEquation.html)
>
> There are many other singular ODEs that would take the same transformation in addition to Poisson-Boltzmann ODEs which
I tried to solve. For example Ivey's equation and Lane-Emden-Fowler class of differential  equations can be similarly
solved using the same transformation I used in the above post. Solution to many of these ODEs are known in case of
special values of parameters but using the method of iterated integrals, we can find a series solution to any arbitrary
parameters.
Is it possible to graph the solution on an interval by plugging in values of t using your symbolic series solution?

Most importantly, how can you determine how many terms to take in the series to achieve a desired accuracy?
Yes, it should be certainly possible and I will try to post a graph for the solution to the problem in the evening
today. It could be more interesting but my computer is relatively slow and it starts to take a very long time after more
than ten iterated integral terms for many problems. It would be interesting how to optimize computers for mathematica to
run faster.

---

### #240 — Cuchulainn
*January 3, 2017, 9:56 AM*

> Cuch, you are right. Thanks for pointing out. Yes, it is not Lane-Emden, the ODE I solved is poisson-Boltzmann differential equation. [http://mathworld.wolfram.com/Poisson-Bo ... ation.html](http://mathworld.wolfram.com/Poisson-BoltzmannDifferentialEquation.html)
>
> There are many other singular ODEs that would take the same transformation in addition to Poisson-Boltzmann ODEs which
I tried to solve. For example Ivey's equation and Lane-Emden-Fowler class of differential  equations can be similarly
solved using the same transformation I used in the above post. Solution to many of these ODEs are known in case of
special values of parameters but using the method of iterated integrals, we can find a series solution to any arbitrary
parameters.
Is it possible to graph the solution on an interval by plugging in values of t using your symbolic series solution?

Most importantly, how can you determine how many terms to take in the series to achieve a desired accuracy?
Yes, it should be certainly possible and I will try to post a graph for the solution to the problem in the evening
today. It could be more interesting but my computer is relatively slow and it starts to take a very long time after more
than ten iterated integral terms for many problems. It would be interesting how to optimize computers for mathematica to
run faster.
No excuses! It meas the method is not good, A ODE solver does it in no time, Sorry.

Speaking of Poisson B a long time ago I worked on numerical simulation of semiconductor devices, and PB boundary value
problem had to be solved numerically using Gummel (fitting). By no means trivial (boundary layers, large gradients etc.)

You have made an initial value problems from it??

---

### #241 — Amin (Topic Author)
*January 3, 2017, 10:06 AM*

>
> It is possible to double-check the solution of this linear ODE system using matrix exponentials + added benefit of a
solution involving exp:
> [YouTube Video](https://www.youtube.com/embed/)

even easier, y=x' so you can check by writing it as a 2nd order ODE,

x′=y,

y′=6x−y,

so

x'′=y'=6x−y=6x-x'

yields

x''+x'-6x=0

solution x=C_1 exp(2t)+C_2 exp(-3t)

initial conditions give

x=1/5 exp(2t)+4/5 exp(-3t)

y=x'=2/5 exp(2t)-12/5 exp(-3t)

which agrees with what the maestro had
Neat, avoids computing eigenvectors (and matrix inversion).
Cuch, my method is also totally explicit and avoids any matrix inversions or calculation of eigenvectors.

---

### #242 — Cuchulainn
*January 3, 2017, 10:16 AM*

>
>
>
> even easier, y=x' so you can check by writing it as a 2nd order ODE,
>
> x′=y,
>
> y′=6x−y,
>
> so
>
> x'′=y'=6x−y=6x-x'
>
> yields
>
> x''+x'-6x=0
>
> solution x=C_1 exp(2t)+C_2 exp(-3t)
>
> initial conditions give
>
> x=1/5 exp(2t)+4/5 exp(-3t)
>
> y=x'=2/5 exp(2t)-12/5 exp(-3t)
>
> which agrees with what the maestro had
Neat, avoids computing eigenvectors (and matrix inversion).
Cuch, my method is also totally explicit and avoids any matrix inversions or calculation of eigenvectors.
OK, but it is computationally infeasible as you state yourself.

I reckon it took ppauper 2 minutes to come up with his solution. It takes a similar amount of time to plug the 2X2
system into ODE solver.

..

---

### #243 — Amin (Topic Author)
*January 3, 2017, 11:15 AM*

>
> Neat, avoids computing eigenvectors (and matrix inversion).
Cuch, my method is also totally explicit and avoids any matrix inversions or calculation of eigenvectors.
OK, but it is computationally infeasible as you state yourself.

I reckon it took ppauper 2 minutes to come up with his solution. It takes a similar amount of time to plug the 2X2
system into ODE solver.

..
You could solve the ODE problem once with arbitrary initial values and continue to use it forever. For simple problems
it would probably not make sense since so many ways of exactly solving the ODEs are available but for complex problems
that have never been solved, the method should work very well. I was complaining about speed since the computer I am
using is several years old.

 Cuch: It takes a similar amount of time to plug the 2X2 system into ODE solver.

You can now solve systems with very large number of equations all of which could possibly be nonlinear. There are
extensively huge applications of large systems of differential equations. As one of those stimulating ideas, I was
thinking that large n-body problems modeled by large systems of differential equations can be solved by the method of
iterated integrals.

---

### #244 — Cuchulainn
*January 3, 2017, 11:46 AM*

For n-body problem you're gonna need a bigger boat.

---

### #245 — Amin (Topic Author)
*January 3, 2017, 11:52 AM*

> For n-body problem you're gonna need a bigger boat.
Yes, We can now put supercomputers to good work. Better solution of weather and related forecasting problems also come
to mind that can benefit all of us.

---

### #246 — ppauper
*January 3, 2017, 4:05 PM*

>
> Neat, avoids computing eigenvectors (and matrix inversion).
Cuch, my method is also totally explicit and avoids any matrix inversions or calculation of eigenvectors.
OK, but it is computationally infeasible as you state yourself.

I reckon it took ppauper 2 minutes to come up with his solution. It takes a similar amount of time to plug the 2X2
system into ODE solver.

..
the point would be that it can solve far more complicated problems but you test it on problems to which you know the
solutions in order to check that it works

---

### #247 — outrun
*January 3, 2017, 4:18 PM*

> For n-body problem you're gonna need a bigger boat.
In certain machine learning algorithm the core numerical aspect is similar to the gravitational n body problem. To speed
that up there is an awesome method called "the fast multipole method" considered one of the top algorithm developed in
the 20th century.

---

### #248 — Cuchulainn
*January 3, 2017, 5:04 PM*

> For n-body problem you're gonna need a bigger boat.
In certain machine learning algorithm the core numerical aspect is similar to the gravitational n body problem. To speed
that up there is an awesome method called "the fast multipole method" considered one of the top algorithm developed in
the 20th century.
Yes, I remember Javabean/Quantmeh mentioning this. But can it beat "iterated integrals"?

---

### #249 — outrun
*January 3, 2017, 5:31 PM*

> For n-body problem you're gonna need a bigger boat.
In certain machine learning algorithm the core numerical aspect is similar to the gravitational n body problem. To speed
that up there is an awesome method called "the fast multipole method" considered one of the top algorithm developed in
the 20th century.
Yes, I remember Javabean/Quantmeh mentioning this. But can it beat "iterated integrals"?
I think it even beats a  simple power series substitution y=sum c_i x^i !!

---

### #250 — Amin (Topic Author)
*January 4, 2017, 9:17 AM*

I am not an expert at n-body problem but I try to sometimes read and understand what is going on about interesting
applications of mathematics in other areas. I seriously regret having wasted half my life working with mathematical
finance. I think outrun is not a great expert either at n-body problem. As I read about fast multipole method, it is
used to lump together sources that are close together and treat them as a single entity. I would suppose you would still
have to solve a large number of differential equations after employing the fast multipole method.

---

[← Previous](page_004.md) | [Index](index.md) | [Next →](page_006.md)
