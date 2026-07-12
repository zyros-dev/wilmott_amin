# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 8 of 65** — Posts #351–#400

[← Previous](page_007.md) | [Index](index.md) | [Next →](page_009.md)

---

### #351 — outrun
*January 8, 2017, 1:06 PM*

>
> The issue was the typo; we all know what it is.
why would "first year undergrad" refer to a typo? What if it was high school like here, or 3rd year? Would any of that
matter?
Give an example of an ODE with delta coefficient + solution. If you mention something, give a concrete example, like
ppauper and amike have done. We don't need an online descripition of delta. Numbers and insights better. HTH

*It's the primitive of the Dirac delta function.*

??
Please focus on your task to substantiate your claim that Amins method is the same as Picard as you claimed because that
would advance thing. I will handle the dialogs I have with list1 and ppauper myself.

Who is the "we" you talks about all the time. Is that yourself? Do you think you are a selfassigned spokesman of some
group? It looks like it: you have the urge to reply on behave of list1 and ppauper but these is no need for that, it
only demonstrated that you have an ego control problem. Same goes with all the capitals, exclamation, are you having
problems controlling negative feelings?

---

### #352 — Amin (Topic Author)
*January 8, 2017, 1:20 PM*

>
> No, I don't get it. And I don't know why you are dong it.
>
> Equation (2) is fine and standard.
>
>
>
> **The leap of faith (for me) is which result of calculus was used in deriving (3)?**
>
Let me try to answer this question from cuch that I have quoted for understanding the concepts behind the new method..

Equation (3) and the idea behind it is very useful to understand and I am sure people will like to make applications of
such expressions everywhere in mathematics while dealing with functions of several variables. I am sure there could be
some exceptions where the result in equation(3) or its simpler version equation (3A) given below may not apply and would
break down and some things might have to be dealt more carefully. In general these two relationships do work very well.
Let us choose a function with decent complexity as a start and apply simpler equation(3A) given below on it.

Before I try to prove

$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]\frac{dy(s)}{ds}ds$
Equation(3)

Let us look at the simpler version of equation(3) and take a function of two variables where y does not necessarily have
dependence on tau

$f(\tau ,y_1)=f\left(\tau ,y_0\right)+\int _{y_0}^{y_1 }\frac{\partial }{\partial y}[f(\tau ,y)]dy$ Equation (3A)

Let us take a concrete function f(y,t) that has enough complexity.

I take: f(y,t)=Exp[ a t + b y + c t y]. We want to evaluate it y=10 while taking initial value of y=0. also keeping the
general value of t in the expression.

$\text{Exp}[a t+b\text{  }y +c t y]\text{/.}y \to  10$=$ E^(10 b + a t + 10 c t)$    Answer(a)

We take the above to be lhs of Equation (3A)

Below I evaluate the rhs of equation (3A) as

 $(Exp[a t + b  y + c t y] /. y -> 0 ) + Integrate[D[Exp[a t + b y + c t y], y], {y, 0, 10}]$

=$E^(10 b + (a + 10 c) t)$  Answer (b)

and I get the same answer (b) as answer (a) above

Equation (3) is a slightly more complex form of Equation (3A) when there is dependence between two variables.

Cuch, you agree?
Amin,

Let;s look at (3) and (3A), it's a trick like a magician pulling a rabbit out of a hat. But they are the equation upon
which your work is based.

Q

1. How to prove them (give a reference or you prove it). **Wait: NOW I KNOW; You are taking the TOTAL DERIVATIVE ==>
assuming f is infiinitely differentiable!!! Got it. You are applying Taylor's theorem ,yes?**

2. df/dy is too restrictive .. it's easy to give an example to break it.

3. For which values of t does your series converge?

4. Under which circumstances does your problem have a solution.

etc.

I think you do not understand my questions. This thread IMO belongs to STUDENT!!
Did you work through the exponential example I gave here in post 343.

Let us take a concrete function f(y,t) that has enough complexity.

I take: f(y,t)=Exp[ a t + b y + c t y]. We want to evaluate it y=10 while taking initial value of y=0. also keeping the
general value of t in the expression.

$\text{Exp}[a t+b\text{  }y +c t y]\text{/.}y \to  10$=$ E^(10 b + a t + 10 c t)$    Answer(a)

We take the above to be lhs of Equation (3A)

Below I evaluate the rhs of equation (3A) as

 $(Exp[a t + b  y + c t y] /. y -> 0 ) + Integrate[D[Exp[a t + b y + c t y], y], {y, 0, 10}]$

=$E^(10 b + (a + 10 c) t)$  Answer (b)

and I get the same answer (b) as answer (a) above

Equation (3) is a slightly more complex form of Equation (3A) when there is dependence between two variables.

I have not talked about any total derivative that you are claiming in bold. I have not mentioned any total derivative in
the equations 3 and 3A. The function needs to be once differentiable and not infinitely differentiable.

---

### #353 — Cuchulainn
*January 8, 2017, 2:47 PM*

>
> why would "first year undergrad" refer to a typo? What if it was high school like here, or 3rd year? Would any of that
matter?
Give an example of an ODE with delta coefficient + solution. If you mention something, give a concrete example, like
ppauper and amike have done. We don't need an online descripition of delta. Numbers and insights better. HTH

*It's the primitive of the Dirac delta function.

*

??
Please focus on your task to substantiate your claim that Amins method is the same as Picard as you claimed because that
would advance thing. I will handle the dialogs I have with list1 and ppauper myself.

Who is the "we" you talks about all the time. Is that yourself? Do you think you are a selfassigned spokesman of some
group? It looks like it: you have the urge to reply on behave of list1 and ppauper but these is no need for that, it
only demonstrated that you have an ego control problem. Same goes with all the capitals, exclamation, are you having
problems controlling negative feelings?
Booh. You're the one whining about Dirac.

Schaum has a book on Signals and Systems with examples on Dirac.

---

### #354 — Cuchulainn
*January 8, 2017, 3:00 PM*

Amin,

I now understand how you got your equations.It is not new (my great grandfather P..Henrici 'Dicrete Variable Methods in
ODE" page 118

(1) y'(t) = f(y(t))

Differentiate (1) (total derivative) to get

(2) y''(t) = df(y(t)/dy X f

Now integrate (2) twice which gives Amin's formula.

But the implicit assumptions are:

A. df/dy is nice function.

B. y'(t) is continuous at = 0.

There is not ;point looking at your exp(..) example because it was chosen not to violate assumptions A and B. All the
examples to date are trivial wit the exception of outrun's Dirac ODE (TBD ))

Is my analysis correct, Amin?

//

On a side remark; Henrici states this methods has no practical merit (especially for ODE systems)  as evaluating
derivatives is too involved. And Runge Kutta methods don't have these issues ... all they need is function values.

---

### #355 — Cuchulainn
*January 8, 2017, 3:06 PM*

* I have not talked about any total derivative that you are claiming in bold. I have not mentioned any total derivative
in the equations 3 and 3A. *

Yes you do on page 4 of your November 2016 article., OMG

Exhibit

[https://papers.ssrn.com/sol3/papers.cfm ... wnload=yes](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598&download=yes)

---

### #356 — Cuchulainn
*January 8, 2017, 3:31 PM*

*"Please focus on your task to substantiate your claim that Amin'smethod is the same as Picard as you claimed because
that would advance thing."*

Sorry gov, I got distracted by the real issue by the above side show.

I am gonna give an answer to show the equivalence but you will need to study some maths (see **Tricomi's book **on
integral equations page 18). Let's take 2nd order ODE as I just described, it is equivalent to Amin's iterated integral
 Again it's a Volterra integral equation.

Or **Handbook of Integral Equations** page 876 as well.\

However, however,  what Amin is doing is upgrading a 1st order ODE to 2nd order ODE and making a Vollerra integral
equation which is **mathematically incorrect**. What seems to be going on is indirectly morphing a 1st order ODE to a
2nd order ODE,. Bottleneck is the initial conditions.

*"I will handle the dialogs I have with list1 and ppauper myself"*

What will you say? They had good remarks IMO.

---

### #357 — amike
*January 8, 2017, 4:04 PM*

>
> Before I try to prove
>
>
$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]\frac{dy(s)}{ds}ds$
Equation(3)
>
> Let us look at the simpler version of equation(3) and take a function of two variables where y does not necessarily
have dependence on tau
>
> $f(\tau ,y_1)=f\left(\tau ,y_0\right)+\int _{y_0}^{y_1 }\frac{\partial }{\partial y}[f(\tau ,y)]dy$ Equation (3A)
Perhaps I am missing something here...  isn't this pretty basic?

Closing my eyes to the ode context, this is just the fundamental theorem of (integral) calculus, no?

$$ f(\tau ,y_1)=f\left(\tau ,y_0\right)+\int _{y_0}^{y_1 }\frac{\partial }{\partial y}[f(\tau ,y)]dy $$

The variable$\tau$ is fixed, so if you like define$g(y)=f(\tau,y)$ . So you need some continuity on the derivative of
the function.

Then this:

$
$ f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]\frac{dy(s)}{ds}ds $
$

is just a change of variables in the integral, which I think requires continuity on$y(t)$ and$y^\prime(t)$ . (explicitly
shown in Shaum's "Advanced Calculus", to make connection with earlier comments on this thread... ).

 I suspect that the interesting bit is the next step(s)...

---

### #358 — Cuchulainn
*January 8, 2017, 4:15 PM*

>
> Before I try to prove
>
>
$f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]\frac{dy(s)}{ds}ds$
Equation(3)
>
> Let us look at the simpler version of equation(3) and take a function of two variables where y does not necessarily
have dependence on tau
>
> $f(\tau ,y_1)=f\left(\tau ,y_0\right)+\int _{y_0}^{y_1 }\frac{\partial }{\partial y}[f(\tau ,y)]dy$ Equation (3A)
Perhaps I am missing something here...  isn't this pretty basic?

Closing my eyes to the ode context, this is just the fundamental theorem of (integral) calculus, no?

$$ f(\tau ,y_1)=f\left(\tau ,y_0\right)+\int _{y_0}^{y_1 }\frac{\partial }{\partial y}[f(\tau ,y)]dy $$

The variable$\tau$ is fixed, so if you like define$g(y)=f(\tau,y)$ . So you need some continuity on the derivative of
the function.

Then this:

$
$ f(\tau ,y(\tau ))=f\left(\tau ,y\left(t_0\right)\right)+\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(s))]\frac{dy(s)}{ds}ds $
$

is just a change of variables in the integral, which I think requires continuity on$y(t)$ and$y^\prime(t)$ . (explicitly
shown in Shaum's "Advanced Calculus", to make connection with earlier comments on this thread... ).

 I suspect that the interesting bit is the next step(s)...
Exactly,

I came to a similar conclusion in my post of Sun Jan 08, 2017 3:00 pm

---

### #359 — amike
*January 8, 2017, 4:19 PM*

Ah, right, sorry.  I'm finding the plot here a bit hard to follow at times...

---

### #360 — Cuchulainn
*January 8, 2017, 4:29 PM*

> Ah, right, sorry.  I'm finding the plot here a bit hard to follow at times...
Sorry. But I am 99% sure* now* how Amin got this stuff and I confirm your concerns about continuity.

For me, I will keep quiet now as i have worked it out with pencil and paper and the background. This technique has been
known for many years.

---

### #361 — Cuchulainn
*January 8, 2017, 6:03 PM*

**(broken latex: Unbalanced $: 3)**

```latex
Here's a test case; maybe for amike and Amin? BTW i have an numeric answer ..

$ y'(t) = f(t,y(t)),  y(0) = 0 $  on interval $ 0
```

---

### #362 — amike
*January 8, 2017, 8:52 PM*

Yeah, that's a fun one -- although the solution is pretty simple in the end.  I am definitely of the opinion that one
needs to do some analysis of the problem before using any method, and I would not blindly attempt a formal series
solution to this.  :)

---

### #363 — Cuchulainn
*January 8, 2017, 10:01 PM*

**(broken latex: Unbalanced $: 1)**

```latex
> Yeah, that's a fun one -- although the solution is pretty simple in the end.  I am definitely of the opinion that one
needs to do some analysis of the problem before using any method, and I would not blindly attempt a formal series
solution to this.
Yes, i solve it using ODE solver and it's too easy. However, the Peano/Picard iterates oscillate between t^2 and -t^2
for a slightly more complicated problem.

Just looking at f

$df/dy = -4/t, 0
```

---

### #364 — Amin (Topic Author)
*January 8, 2017, 11:40 PM*

Now you can download the new better written version of my paper here at SSRN: [https://papers.ssrn.com/sol3/papers.cfm ... id=2872598](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598)

Abstract: Our goal is to give a very simple, effective and intuitive algorithm for the solution of initial value problem
of ODEs of 1st and arbitrary higher order with general i.e. constant, variable or nonlinear coefficients and the systems
of these ordinary differential equations. We find an expansion of the differential equation/function to get an infinite
series containing iterated integrals evaluated solely at initial values of the dependent variables in the ordinary
differential equation. Our series represents the true series expansion of the closed form solution of the ordinary
differential equation. The method can also be used easily for general 2nd and higher order ordinary differential
equations. We explain with examples the steps to solution of initial value problems of 1st order ordinary differential
equations and later follow with more examples for linear and non-linear 2nd order and third order ODEs. We have given
mathematica code for the solution of nth order ordinary differential equations and show with examples how to use the
general code on 1st, 2nd and third order ordinary differential equations. We also give mathematica code for the solution
of systems of a large number of general ordinary differential equations each of arbitrary order. We give an example
showing the ease with which our method calculates the solution of system of three non-linear second order ordinary
differential equations.

---

### #365 — list1
*January 9, 2017, 2:50 AM*

**(broken latex: Unbalanced $: 1)**

```latex
> Yeah, that's a fun one -- although the solution is pretty simple in the end.  I am definitely of the opinion that one
needs to do some analysis of the problem before using any method, and I would not blindly attempt a formal series
solution to this.
Yes, i solve it using ODE solver and it's too easy. However, the Peano/Picard iterates oscillate between t^2 and -t^2
for a slightly more complicated problem.

Just looking at f

$df/dy = -4/t, 0
cuch, aming transformations make sense under a certain conditions. in particular when derivative of the right hand side
is differentiable on the interval. your example consider the function which does not bounded in t = 0. thus his method
might not work in the case.
```

---

### #366 — outrun
*January 9, 2017, 7:37 AM*

Is that condition already specified in Amin's paper?

---

### #367 — list1
*January 9, 2017, 8:02 AM*

> Is that condition already specified in Amin's paper?
No, the manner of his messages looks like a draft but his derivations uses integrals of the right hand side which
obviously should be integrable. Otherwise his transformations does not present equivalence initial eq to the eq which
represented after his transformations

---

### #368 — Cuchulainn
*January 9, 2017, 11:00 AM*

*Otherwise his transformations does not present equivalence initial eq to the eq which represented after his
transformations*

As I wrote what Amin does is upgrade 1st order ODE to 2nd order ODE, and then integrate the latter twice. He is then
working on a model that will break down.

I actually worked out the steps. If you do the same you will see exactly what is going on. All it involves is
integration.

Amin has not confirmed not denied my claims to date.

---

### #369 — Cuchulainn
*January 9, 2017, 11:03 AM*

> Is that condition already specified in Amin's paper?
If you read the paper you will see that it is not and this fact has already been noted.

---

### #370 — Cuchulainn
*January 9, 2017, 11:15 AM*

> Now you can download the new better written version of my paper here at SSRN: [https://papers.ssrn.com/sol3/papers.cfm ... id=2872598](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598)
>
> Abstract: Our goal is to give a very simple, effective and intuitive algorithm for the solution of initial value
problem of ODEs of 1st and arbitrary higher order with general i.e. constant, variable or nonlinear coefficients and the
systems of these ordinary differential equations. We find an expansion of the differential equation/function to get an
infinite series containing iterated integrals evaluated solely at initial values of the dependent variables in the
ordinary differential equation. Our series represents the true series expansion of the closed form solution of the
ordinary differential equation. The method can also be used easily for general 2nd and higher order ordinary
differential equations. We explain with examples the steps to solution of initial value problems of 1st order ordinary
differential equations and later follow with more examples for linear and non-linear 2nd order and third order ODEs. We
have given mathematica code for the solution of nth order ordinary differential equations and show with examples how to
use the general code on 1st, 2nd and third order ordinary differential equations. We also give mathematica code for the
solution of systems of a large number of general ordinary differential equations each of arbitrary order. We give an
example showing the ease with which our method calculates the solution of system of three non-linear second order
ordinary differential equations.
The paper tries to convince us that the method works taking (more) benign examples. Nothing has changed.

---

### #371 — outrun
*January 9, 2017, 11:22 AM*

> Is that condition already specified in Amin's paper?
If you read the paper you will see that it is not and this fact has already been noted.
So the example was meant to be an additional (after it being noted before) implicit hint (let's see if he can spot it??)
for Amin that he didn't explicitly say that integrals in his equations need to be computable? I think list1 has a fair
point in that respect? Maybe it's because of Amin not responding to everything (like just now, just announcing new
versions, ignoring discussion), but I personally think that this spoon feeding is not a pleasant sight.

---

### #372 — Cuchulainn
*January 9, 2017, 11:41 AM*

> Is that condition already specified in Amin's paper?
If you read the paper you will see that it is not and this fact has already been noted.
So the example was meant to be an additional (after it being noted before) implicit hint (let's see if he can spot it??)
for Amin that he didn't explicitly say that integrals in his equations need to be computable? I think list1 has a fair
point in that respect? Maybe it's because of Amin not responding to everything (like just now, just announcing new
versions, ignoring discussion), but I personally think that this spoon feeding is not a pleasant sight.
Indeed. He is just being coy.

If he responded like this at a seminar to a group of mathematicians there would leave the room.

---

### #373 — outrun
*January 9, 2017, 12:45 PM*

>
> If you read the paper you will see that it is not and this fact has already been noted.
So the example was meant to be an additional (after it being noted before) implicit hint (let's see if he can spot it??)
for Amin that he didn't explicitly say that integrals in his equations need to be computable? I think list1 has a fair
point in that respect? Maybe it's because of Amin not responding to everything (like just now, just announcing new
versions, ignoring discussion), but I personally think that this spoon feeding is not a pleasant sight.
Indeed. He is just being coy.

If he responded like this at a seminar to a group of mathematicians there would leave the room.
I think that's the reason why things get so emotional here. A bold claim and he's not responding rationally but simple
ignores discussion that don't fit in his dramatic view of being someone who publishes very important breakthroughs even
though people constantly try to stop him.

If we stopped the discussion he would continue nonetheless -he keeps on posting and posting how awesome things are- and
so we think we can't stop and let that happen. My hope was to have a rational discussion with join honest search for the
truth, I was hoping to get it over quickly that way. Sometimes you have to stop biting?

---

### #374 — Cuchulainn
*January 9, 2017, 1:44 PM*

In fairness, OP did not claim that the method was **fast**, which is what a lotta quants claim.

---

### #375 — list1
*January 9, 2017, 2:04 PM*

> *Otherwise his transformations does not present equivalence initial eq to the eq which represented after his
transformations*
>
>
>
> As I wrote what Amin does is upgrade 1st order ODE to 2nd order ODE, and then integrate the latter twice. He is then
working on a model that will break down.
>
>
>
> I actually worked out the steps. If you do the same you will see exactly what is going on. All it involves is
integration.
>
>
>
> Amin has not confirmed not denied my claims to date.
ODEs of the higher orders can be rewritten in vector form as the vector ODEs of the 1st order. On the other hand he
needs

1 to write the last term after n- times iterations $R_n$ in explicit form

2. to prove that it converges to zero. It might be other very strong conditions should be exposed.

Because he expects that values of the derivatives at the initial point are sufficient for construction of the solution
it somewhat remind analytical real valued functions. Without such work everything what were done look a work on idea's
level

---

### #376 — ppauper
*January 9, 2017, 2:50 PM*

> Is that condition already specified in Amin's paper?
If you read the paper you will see that it is not and this fact has already been noted.
cuch makes an excellent point: some of the people attacking amin's paper have not actually read it and don't actually
know what it contains, and that is evident in their attacks

credit where credit is due: unlike some, cuch has actually read the paper in some detail and is able to offer
constructive criticism.

---

### #377 — outrun
*January 9, 2017, 5:23 PM*

Yes he did read it and ended up saying that he figured out what was going on. For me the outline of methods was too
noisy to follow. I'll try again later, maybe there will be some consensus soon which is easier to follow?

---

### #378 — Cuchulainn
*January 9, 2017, 5:28 PM*

> Yes he did read it and ended up saying that he figured out what was going on. For me the outline of methods was too
noisy to follow. I'll try again later, maybe there will be some consensus soon which is easier to follow?
You need to study ODEs and the references I gave you. You should sit down and train yourself to solve maths problems.
It's not something you learn on a rainy Sunday afternoon.

Anyway, the method is flawed, speaking as a mathematician.

---

### #379 — outrun
*January 9, 2017, 5:30 PM*

> Yes he did read it and ended up saying that he figured out what was going on. For me the outline of methods was too
noisy to follow. I'll try again later, maybe there will be some consensus soon which is easier to follow?
You need to study ODEs and the references I gave you. It's not something you learn on a rainy Sunday afternoon.

Anyway, the method is flawed.
Yes, well I know ODEs of course..

---

### #380 — Cuchulainn
*January 9, 2017, 5:32 PM*

> Yes he did read it and ended up saying that he figured out what was going on. For me the outline of methods was too
noisy to follow. I'll try again later, maybe there will be some consensus soon which is easier to follow?
You need to study ODEs and the references I gave you. It's not something you learn on a rainy Sunday afternoon.

Anyway, the method is flawed.
Yes, well I know ODEs of course..

Sure.
So, tell us, what's the issue with Amin's approach?

 I fear the response will not be forthcoming.

---

### #381 — outrun
*January 9, 2017, 6:03 PM*

>
> You need to study ODEs and the references I gave you. It's not something you learn on a rainy Sunday afternoon.
>
> Anyway, the method is flawed.
Yes, well I know ODEs of course..

Sure.
So, tell us, what's the issue with Amin's approach?

 I fear the response will not be forthcoming.
Why so hostile?

For that I need to better understand what he's doing. The level op math isn't the issue IMO, it's just not very clear.
You also needed quite a bit of time to figure out what he was doing, no? Was that because you needed to get up to speed
with ODEs, or was it because it was unclear why he was/is doing?

---

### #382 — ppauper
*January 9, 2017, 6:11 PM*

it's a lengthy paper (32 pages)  so it took me a while to read

---

### #383 — Paul
*January 9, 2017, 6:20 PM*

May I ask which people here have done an undergraduate mathematics degree? (And where? As supplementary question!)

---

### #384 — Cuchulainn
*January 9, 2017, 6:59 PM*

> May I ask which people here have done an undergraduate mathematics degree? (And where? As supplementary question!)
That's what I wanted to ask, but was afraid. I guess most posters are not mathematics (ppauper is a maths guy i believe.

You can learn ODE at CS/EE level (just methods) but what is  needed is  anatysis ODE.

// I have 4-year BA (Mod) from Dublin University (Trinity College) in both pure and applied.

---

### #385 — Cuchulainn
*January 9, 2017, 7:05 PM*

>
> Yes, well I know ODEs of course..
>
> Sure.
So, tell us, what's the issue with Amin's approach?

 I fear the response will not be forthcoming.
Why so hostile?

For that I need to better understand what he's doing. The level op math isn't the issue IMO, it's just not very clear.
You also needed quite a bit of time to figure out what he was doing, no? Was that because you needed to get up to speed
with ODEs, or was it because it was unclear why he was/is doing?
I'm pretty annoyed with the level of maturity and quality of the discussion in general.

Extremely low-level and disappointing. Have you noticed that you respond to a question with another question? Nice
trick, like a Hague politician.

No, you need to see where the logic breaks down. I have explained how he gets his equation already.

**You only need to understand page 4.** A good maths 2nd year undergraduate can understand it in 5 minutes.

**The other pages is just a set of examples. **

---

### #386 — Cuchulainn
*January 9, 2017, 7:10 PM*

OK, here's a great high-school example, to see if you know ODE

$y' = 2y /t$

$y(t_0) = y_0$.

Consider the cases:

1. $t_0 \ne 0$

2.  $t_0 = 0, y_0 \ne 0$

3. $ y_0 = 0$

4.$ y_0 = 0, t_0 = 0$

Hint; 3 choices

a. unique solution

b no solution

c. infinite number of solutions.

Which is which?

Good luck. It's a make or break case.

---

### #387 — Paul
*January 9, 2017, 7:39 PM*

BA Maths, Oxford

No need to be afraid to ask!

Most people in finance don't have undergrad maths. And

A. whatever maths they have is usually v restricted, and very gappy

And

B. they overestimate the importance and relevance of the maths they do know.

This is a Social-Justice-Warrior-free website and therefore this profiling is permitted, even encouraged!

---

### #388 — Cuchulainn
*January 9, 2017, 7:52 PM*

B. they overestimate the importance and relevance of the maths they do know.

*A little learning is a dangerous thing; *

*drink deep, or taste not the Pierian spring: *

*there shallow draughts intoxicate the brain, *

*and drinking largely sobers us again.*

---

### #389 — outrun
*January 9, 2017, 8:20 PM*

LOL

You changes the answers set, right?

Initially you didn't have "none" and had "two" instead

1. t0 != 0, a unique solution

2. t0 = 0, y0 != 0, none

3. y0=0, infinite

---

### #390 — Cuchulainn
*January 9, 2017, 8:33 PM*

> LOL
>
> You changes the answers set, right?
>
> Initially you didn't have "none" and had "two" instead
>
>
>
> 1. t0 != 0, a unique solution
>
> 2. t0 = 0, y0 != 0, none
>
> 3. y0=0, infinite
No googling!

OK,, now apply Amin's methiod and Picard.iterations Off you go,

---

### #391 — Cuchulainn
*January 9, 2017, 8:34 PM*

> LOL
>
> You changes the answers set, right?
>
> Initially you didn't have "none" and had "two" instead
>
>
>
> 1. t0 != 0, a unique solution
>
> 2. t0 = 0, y0 != 0, none
>
> 3. y0=0, infinite
No googling!

**OK,, now apply Amin's method and Picard.iterations Off you go,**

---

### #392 — outrun
*January 9, 2017, 8:43 PM*

I'll do that tomorrow, sounds like a good plan

(binge watching a series right now, and I had lunch at Aegon again, so I'm in a fetal position on the floor because of
the food poisoning you always get there)

---

### #393 — amike
*January 9, 2017, 8:56 PM*

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

P.S. I will leave the ``my degree is bigger than yours'' discussion to the rest of you.  :)

---

### #394 — Paul
*January 9, 2017, 10:19 PM*

Is it a maths degree though, amike? Cuch was afraid to ask people, he's not as rude as I am! Yes, I know it's the
internet and therefore everyone's opinion is equally important, blah, blah, and we ought to vote on the validity of
maths,...But Cuch and I have seen this sort of discussion for years now and it's getting rather tedious. We both do
quite a bit of educating people and we see how standards are falling as rapidly as people's self belief skyrockets! (In
the past I've blamed lefties, google, and specifically Shirley Williams and Tony Blair!)

I don't see how any of this is helping Amin. It's just prolonging the agony.

I haven't read his paper because I don't believe that in the 21st century a simple application of the chain rule and the
definition of integration can possibly be original. And I've also read plenty of papers by finance people with dozens of
pages that a half decent mathematician could do in one page. That's tedious too!

Jeez, someone kill this thread! But I guess that should be me!

---

### #395 — amike
*January 9, 2017, 10:24 PM*

That's right!  This is all your fault -- the guy with the maths degree!

---

### #396 — Paul
*January 9, 2017, 10:26 PM*

I've been fighting losing battles now for nearly three decades! Dupire et al's local vol model is my nemesis!

---

### #397 — amike
*January 9, 2017, 10:38 PM*

I find this sort of discussion somewhat interesting because it highlights the fact that to actually understand a subject
well takes a good deal of time and effort -- which people firmly in the centre of the population distribution seem to
completely fail to appreciate.  So we have people who don't know what the greenhouse effect is having a strong opinion
about global warming, and... Donald Trump.  Aghk!

Anyway, the challenge seems to be to try to nudge well meaning people in the right direction so that they discover for
themselves how much they don't know -- without getting irritated and losing patience.  And as you say, such attempts
usually fail spectacularly.

But I also got to do a Picard iteration, which I have never done before and was somewhat amusing...

---

### #398 — Paul
*January 9, 2017, 10:52 PM*

10,000 hours, right? I've put in the 10k in each of maths, finance, running businesses and marriages. I'm still only in
the low hundreds with ukulele though.

---

### #399 — list1
*January 9, 2017, 11:36 PM*

> I find this sort of discussion somewhat interesting because it highlights the fact that to actually understand a
subject well takes a good deal of time and effort -- which people firmly in the centre of the population distribution
seem to completely fail to appreciate.  So we have people who don't know what the greenhouse effect is having a strong
opinion about global warming, and... Donald Trump.  Aghk!
>
>
>
> Anyway, the challenge seems to be to try to nudge well meaning people in the right direction so that they discover for
themselves how much they don't know -- without getting irritated and losing patience.  And as you say, such attempts
usually fail spectacularly.
>
>
>
> But I also got to do a Picard iteration, which I have never done before and was somewhat amusing...
What does Amin writing here does not related to Picard iterations. In classical approach known as Picard iteration we
define iterations consequently beginning with arbitrary function$y_0 ( t )$ . We can prove that under some broad
standard conditions iterations converge to a solution of the ODE.

Amin's starting point is eq itself which make sense only when we supposed that solution exists. His iterations make
sense under the assumptions that solution exists and for this function his integration by parts makes sense. Assume that
it is possible to omit the last term. This illustrates his idea. Now if we do not know that solution of the ODE exists.
He could write his approximations but he need to prove that they converge to a solution of the ODE. Otherwise it looks
like unwritten drama.

---

### #400 — amike
*January 9, 2017, 11:52 PM*

I wasn't saying that Amin's approach had anything to do with Picard.  I was just saying that somewhere during this
written drama I performed one, which was sort-of fun.

---

[← Previous](page_007.md) | [Index](index.md) | [Next →](page_009.md)
