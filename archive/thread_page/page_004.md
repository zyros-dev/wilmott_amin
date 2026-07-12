# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 4 of 65** — Posts #151–#200

[← Previous](page_003.md) | [Index](index.md) | [Next →](page_005.md)

---

### #151 — Amin (Topic Author)
*November 22, 2016, 11:14 AM*

Cuchulainn, what do you think about the above example. Seems alright? I hope you can put your hands on the book I
mentioned.

---

### #152 — list1
*November 22, 2016, 11:44 AM*

> This is example from my paper page 16-17. The example below is borrowed from the book Non Linear Ordinary Differential
Equations by Martin Hermann and Masoud Saravi. Example 2.7, page 50.
>
> Page 16 starts.
>
> Example 5
>
> Consider the 2nd order initial value problem given as
>
> $y''=f\left(\tau ,y(\tau ),y'(\tau )\right)=-2 y y'$       $y(0)=y_0=0$      $y'(0)=y'_0=1$
>
>
>
> From the general solution expansion given in Equation (22), we calculate the coefficients of the first few terms as
>
>
>
>
$\int _{t_0}^t\int _{t_0}^sf\left(\tau ,y\left(t_0\right),y'\left(t_0\right)\right)d\tau ds=\left(-2y'_0y_0\right)\frac{t^2}{2}=0$
>
>
>
>
$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0 +\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right) \right]dud\tau ds$
>
> $=\left(-2y'_0{}^2\right)\frac{t^3}{6}+\left(-2y_0\left(-2y'_0y_0\right)\frac{t^3}{6}=-\frac{t^3}{3}\right.$
>
>
>
>
$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]y'_0\right.$
>
>
$\left.+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]dv dud\tau ds$
>
>
>
>
$=0+\left(8y_0 y'_0{}^2\right)\frac{t^4}{24}+\left(8y_0 y'_0{}^2\right)\frac{t^4}{24}+\left(-8y_0{}^3y'_0\right)\frac{t^4}{24}=0$
>
>
>
>
$\int _{t_0}^t\int _{t_0}^s\int _{t_0}^{\tau }\int _{t_0}^u\int _{t_0}^v\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0\right.\right.\right.$
>
> $\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]y'_0$
>
> $+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0\right.$
>
>
$\left.\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]y'_0$
>
>
$+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]y'_0\right.$
>
> $+\frac{\partial }{\partial y'}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y_0,y'_0\right)\right]y'_0\right.$
>
>
$\left.\left.\left.+\frac{\partial }{\partial y'}\left[f\left(\tau ,y_0,y'_0\right)\right]f\left(u,y_0,y'_0\right)\right]f\left(v,y_0,y'_0\right)\right]f\left(w,y_0,y'_0\right)\right]dwdv dud\tau ds$
>
>
$\left.=0+\left(8y'_0{}^3\right)\frac{t^5}{120}+\left(8y'_0{}^3\right)\frac{t^5}{120}+\left(-24y_0{}^2y'_0{}^2\right)\right)\frac{t^5}{120}+0+$
>
>
$\left(16 y_0y'_0\left(-2y_0y'_0\right)\right)\frac{t^5}{120}+\left(16 y_0y'_0\left(-2y_0y'_0\right)\right)\frac{t^5}{120}-\left(8y_0{}^3\left(-2y_0y'_0\right)\right)\frac{t^5}{120}=\frac{2t^5}{15}$
>
>
>
> By continuing the expansion for another two terms, we can verify the next term in expansion as $\frac{-17t^7}{315}$
>
> And we get the first significant terms of the solution as
>
> $y(t)=t-\frac{t^3}{3}+\frac{2t^5}{15}-\frac{17t^7}{315}+\text{...}.$
>
>
>
> I never gave the last term of expansion but I did verify it. You can compare the solution with the one given in the
book page 50.
Explicit solution can be found very easy by making change u = $y^{/}$

---

### #153 — Amin (Topic Author)
*November 22, 2016, 12:04 PM*

@list, good. In that case you can probably verify. Now try this method somewhere else where you cannot easily make a
simple change of variables. It is a general method and I am glad now you could verify some example.

As I said, for every given ODE, you will get an explicit series solution in terms of arbitrary initial values and
independent variable once for all that would usually be lightning fast. You could once solve for the series solution for
any ODE in terms of arbitrary initial values and continue to use it forever. Sounds too good to be true?

---

### #154 — outrun
*November 22, 2016, 12:28 PM*

Hold your horses, first continue and try the two cases Cuch provided!

---

### #155 — Cuchulainn
*November 22, 2016, 12:49 PM*

> Yes, I do see a possible algebra error in the shown example. You know when I was writing the last day, I would correct
the errors and they would make them wrong again at places since they have controls on my computer. For most people it
would be impossible to do any work in such a case.
>
>
>
> Just solve the examples on your own and expand the actual solution in series and it would be the same.
>
> @cuch.
>
> Yes, I will like to solve your proposed examples. They are a very simple case. But give me a few hours since at the
moment I have some other things to do.
I already did post the correct answer! I use e.g. standard techniques, Again.,$y(t) = (1-t)e^{-t}$ . Your series is
incorrect.

@list1, have you tried you own proposal, answer?

---

### #156 — Cuchulainn
*November 22, 2016, 1:17 PM*

> Cuchulainn, what do you think about the above example. Seems alright? I hope you can put your hands on the book I
mentioned.
I don't have that book.  Another way:

Note

$ y'' = - (y^2)'$

Integrate once to get a 1st order Riccati ODE, which is well known. Actually, define$v = y^{-1}$ to get a nice linear
ODE in$v$ .

---

### #157 — Amin (Topic Author)
*November 22, 2016, 1:58 PM*

Please Cuch, your answer is wrong. The series I have given is perfectly right. However there is a typo in my answer. the
fourth term is 5t^3/6 (instead of 4t^3/3)but if you do algebra in initial values given there in my answer, this is what
you get. The right answer with initial values is y(t)=exp(-t)+2 t exp(-t). Which has the right series expansion in my
paper.

Brother cuch do not insist on wrong answer.

Edit:corrected the sign on exponential.

---

### #158 — amike
*November 22, 2016, 2:32 PM*

From what I can see, the examples always end up giving results in the form of power series in t, and I just checked that
you can get the same expansions (in a much simpler way IMHO) by simply assuming a series solution of the form: y(t)=y0 +
y1 * t + y2 * t^2 ..., inserting into the ode and solving order by order.

Since series solutions are nothing new, is there maybe a `more interesting' example showing where this method does
better?  (and no, I'm not really sure what 'better' means yet...)

---

### #159 — Cuchulainn
*November 22, 2016, 2:59 PM*

> Please Cuch, your answer is wrong. The series I have given is perfectly right. However there is a typo in my answer.
the fourth term is 5t^3/6 (instead of 4t^3/3)but if you do algebra in initial values given there in my answer, this is
what you get. The right answer with initial values is y(t)=exp(-t)+2 t exp(-t). Which has the right series expansion in
my paper.
>
> Brother cuch do not insist on wrong answer.
>
>
>
> Edit:corrected the sign on exponential.
I made a typo indeed. Could happen a bishop. Don't shoot me, I am trying to help this thread.

I got

$ y(t) = (a + bt) e^{-t}$

now initial conditions ==> $a = 1, b = 2$

QED

Anyways, you are now using exp which is better than those series.

*The series I have given is perfectly right. However there is a typo in my answer.*

A typo in a formula makes it wrong. This is what I found when I checked, was it a typo or is method wrong?

---

### #160 — Cuchulainn
*November 22, 2016, 3:08 PM*

> From what I can see, the examples always end up giving results in the form of power series in t, and I just checked
that you can get the same expansions (in a much simpler way IMHO) by simply assuming a series solution of the form:
y(t)=y0 + y1 * t + y2 * t^2 ..., inserting into the ode and solving order by order.
>
>
>
> Since series solutions are nothing new, is there maybe a `more interesting' example showing where this method does
better?  (and no, I'm not really sure what 'better' means yet...)
I posted Riccati and logistic ODE for Amin to try. A good example is Affine models (e.g. ODE for CIR). But I'm skeptical
it will work.

[https://en.wikipedia.org/wiki/Affine_te ... ture_model](https://en.wikipedia.org/wiki/Affine_term_structure_model)

Examples to date are more like undergrad methods examples.

---

### #161 — Paul
*November 22, 2016, 3:09 PM*

This thread is embarrassing.

P

---

### #162 — amike
*November 22, 2016, 4:19 PM*

possibly...   But given that it has very little to do with quantitative finance, perhaps the forum could do with a
little bit of moderation?

---

### #163 — Amin (Topic Author)
*November 22, 2016, 5:24 PM*

amike, my answer to your earlier post. There could be so many series solutions but I have proposed a general way to
series solutions. Let us see in next few days as people understand what I am trying to say. Besides, I think ODEs and
SDEs are used everywhere in finance.

I always proudly write in wilmott and I am sure a lot of friends would appreciate that. It is a good universal forum.

---

### #164 — Amin (Topic Author)
*November 22, 2016, 6:01 PM*

> Please Cuch, your answer is wrong. The series I have given is perfectly right. However there is a typo in my answer.
the fourth term is 5t^3/6 (instead of 4t^3/3)but if you do algebra in initial values given there in my answer, this is
what you get. The right answer with initial values is y(t)=exp(-t)+2 t exp(-t). Which has the right series expansion in
my paper.
>
> Brother cuch do not insist on wrong answer.
>
>
>
> Edit:corrected the sign on exponential.
I made a typo indeed. Could happen a bishop. Don't shoot me, I am trying to help this thread.

I got

$ y(t) = (a + bt) e^{-t}$

now initial conditions ==> $a = 1, b = 2$

QED

Anyways, you are now using exp which is better than those series.

*The series I have given is perfectly right. However there is a typo in my answer.*

A typo in a formula makes it wrong. This is what I found when I checked, was it a typo or is method wrong?
Sorry cuch, I was joking. My bad. No it is a typo since I have given the term in initial values of derivatives and that
is right. Only wrong part was that My arithmetic went off when I substituted numbers for initial values. Very minor typo
and you can indeed verify what I am saying.

But your answer is till bad since initial values are the same as in the paper y(0)=1 and y'(0)=1. the solution is
y(t)=C1 exp(-t) + C2 t exp(-t). Now you solve for the constants using y(0)=1 and y'(0)=1.  using y(t)=C1 exp(-t) + C2 t
exp(-t), you get 1=C1, and using y'(t)=-C1exp(-t)+C2 exp(-t)- C2 t exp(-t), you get

1=(-C1)+C2, gives you C2=2.

Or may be I did not understand and by initial conditions, you mean initial constants? In that case you are right.

The above answer I found using exponential is not from my method but from the usual technique for 2nd order ODEs with
constant coefficients and my method agrees with the series solution of this answer. My method would always give you a
series but remember even exponential is evaluated by computer software in terms of series so there is no difference at
the end of the day. You could get the series to any order required using the method of iterated integrals and it will
finally match the analytic answer.

---

### #165 — amike
*November 22, 2016, 7:20 PM*

> amike, my answer to your earlier post. There could be so many series solutions but I have proposed a general way to
series solutions. Let us see in next few days as people understand what I am trying to say. Besides, I think ODEs and
SDEs are used everywhere in finance.
>
> I always proudly write in wilmott and I am sure a lot of friends would appreciate that. It is a good universal forum.
But to be clear what I meant: your series solutions appear to be identical to standard power series solutions.  I have
attached screenshots from a standard algebraic manipulator for your examples 1, 3, 4 (I can do others if you like),
showing that the series solutions are the same as yours:
EX1.png
EX3.png
EX4.png
Since these series solutions are standard, I really want to see an example where your algorithm does something
new/different before I get too interested in investigating the algorithm in more detail.

---

### #166 — Paul
*November 22, 2016, 7:38 PM*

$t^2y'=y$

with $y(0)=0$.

P

Cuch, don't give any hints, pls!

---

### #167 — Cuchulainn
*November 22, 2016, 7:41 PM*

Ok, we have a series  for linear, homogeneous initial value problem with constant coefficients . Probably the quickest
way is an abacus to solve them.

 What's the next step?

---

### #168 — Paul
*November 22, 2016, 7:48 PM*

Don't distract him from my example!

P

---

### #169 — amike
*November 22, 2016, 8:07 PM*

Yeah, something sensible on that example would be interesting.

---

### #170 — Cuchulainn
*November 22, 2016, 8:29 PM*

>
> P
>
>
>
> Cuch, don't give any hints, pls!
https://www.youtube.com/watch?v=nX7CeTXoxyU

---

### #171 — Cuchulainn
*November 22, 2016, 11:50 PM*

*Or may be I did not understand and by initial conditions, you mean initial constants? In that case you are right.*

Thank you.

The former, which is the  standard jargon in maths. No other term is correct afaik.

https://en.wikipedia.org/wiki/Initial_value_problem

---

### #172 — Amin (Topic Author)
*November 23, 2016, 9:09 AM*

@Paul, as a start, I was trying to avoid singular initial value problems. But I will definitely come to this in a few
days.

@amike, You are very right that most of the solutions are identical to power series solutions or many times to taylor
series solutions. In fact I believe that there is a Taylor series analogue of every solution I find out  using my
method. If you look at the ODE books, the problems that are solved usually by Taylor series and power series are very
limited to a very small subset of ODEs. As I said there is a Taylor series analogue of every solution I find using my
method which hints towards universal applicability of taylor series like methods. Most examples I gave in paper were
very basic and the solution was mostly known so that reader could become familiar with the method using very familiar
examples. However you could see how easily my method solved the example for second order nonlinear ODE given in post
150. Example 5 on page 16 of my paper. People never traditionally used taylor series or power series methods on these
odes. However if you do a Taylor series expansion on that ODE, you will find the same solution as I gave. The crux of
the method is given in page 1-5 of the paper. It helps us determine how to take the nested derivatives and partials in a
simple sequential way. Again there is a taylor series analogue of every expansion I have given in my paper and that
hints at the universal applicability of the Taylor series and related methods. My method has the advantage that I have
done the same things in the form of integrals and when time/independent variable is present in the differential equation
,we get a better approximation since we have integrated the dependence of independent variable present in the
differential equation like a one dimensional integration.

Again answering amike's observation that each expansion using my methods is going to power series, or taylor series
solution of the problem, I would say the solution using my method goes to analytic solution as we increase the terms and
therefore it has to agree with the formal power series solutions wherever they can be found since they are expansion of
the same analytic solution. For the same analytic solution, if we have expanded it purely in powers x^n, it would
definitely make sense to all of us that  each power x^n should have the same coefficients whatever method we use for
evaluation of that function unless there are some complex(in sense of complexity and not complex varaibles) functions in
coefficients that have their own expansions.

As amike suggested, I am doing a revision of my paper adding many other problems that are not basic and hint at near
universal applicability of the method. I thank amike for his critical review.

---

### #173 — Cuchulainn
*November 23, 2016, 9:33 AM*

* I was trying to avoid singular initial value problems. But I will definitely come to this in a few days.*

We'll be waiting.

My hunch is the power series approach will break down, as will nonlinear IVP will be almost impossible.

I wonder if amike's s/w can solve Riccati and logistic ODE.

Here is a juicy one

$t^{1/2}y' = y$

$y'^2 = 4y$

 *near universal applicability of the method.*

*??*

Personally, I would consult this to see if my ODE was in there

**"Handbook of Exact Solutions for Ordinary Differential Equations"**

---

### #174 — Amin (Topic Author)
*November 23, 2016, 9:56 AM*

Cuch, thanks for adding to discussion. My approach is different from power series approach but agrees with power series
approach whenever power series approach is valid.

@Cuch, my approach is more close to taylor series approach as opposed to power series. If we consider a first order ODE,
in taylor series approach we take  higher partials w.r.t independent variable and higher partials w.r.t dependent
variable and connect them to independent variable through chain rule. But once we have analytically integrated the
differential equation w.r.t independent variable on the first level, we do not need further partial derivatives w.r.t
independent variable and we only need to take higher partials w.r.t dependent variables and use chain rule and integrate
each term with respect to dependent variable and this is where we diverge from classical taylor series method.

In our solution to  y'=f(t,y), we do not need higher partials with respect to t which would be needed in taylor series
method. Again since we analytically integrated t in method of iterated integrals, we do not need these higher partials
with respect to independent variable. Of course, this is assuming that we can analytically integrate t in y'=f(t,y).

@Cuch, yes, I would be solving both nonlinear problems you earlier suggested but please give me a bit of time(1-2 days).

---

### #175 — Cuchulainn
*November 23, 2016, 10:08 AM*

No problem. Take your time.

I am not sure how your formalism handles ODEs like

1. Have a solution only up to time T1, after that not.

2. Have no solution

3. Have multiple solutions

4. ODEs with complex coefficients

5. Systems of ODEs.

Just brainstorming. Maybe these are non-goals.

---

### #176 — Paul
*November 23, 2016, 10:23 AM*

There is a yawning chasm in your knowledge of undergrad maths, Amin, that means we have to doubt the originality of
pretty much everything here.

P

---

### #177 — Amin (Topic Author)
*November 23, 2016, 10:29 AM*

>  No problem. Take your time.
>
>
>
> I am not sure how your formalism handles ODEs like
>
>
>
> 1. Have a solution only up to time T1, after that not.
>
> 2. Have no solution
>
> 3. Have multiple solutions
>
> 4. ODEs with complex coefficients
>
> 5. Systems of ODEs.
>
>
>
> Just brainstorming. Maybe these are non-goals.
Yes Cuch, I will certainly try to tackle some of these things. My first priority right now is paper revision but your
opinion will surely help in better putting things together after your critical review.

---

### #178 — Amin (Topic Author)
*November 23, 2016, 10:34 AM*

> There is a yawning chasm in your knowledge of undergrad maths, Amin, that means we have to doubt the originality of
pretty much everything here.
>
>
>
> P
I am aware of what you are saying. I hope you will be finally convinced. If you doubt, it is good and I am sure it will
help me explain things better in the future. Of course, I have to put more effort in explaining my ideas. Will certainly
try to make the paper revision a better read. I hope you will finally like my work. I am very optimistic about it.

---

### #179 — Cuchulainn
*November 23, 2016, 11:22 AM*

> Here you can download my paper. [https://papers.ssrn.com/sol3/papers.cfm ... id=2872598](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598) I will improve it over next few days but interesting how so many second order ODEs can be so easily solved.
Looking at eq. 19, section 5.1 We see where things start to get out of hand (double integral equation + y' term on right
side).. go no further.

See Henrici (incidentally mon academic greatgrandpa) "Discrete Variable Methods in ODEs" wiley 1962 section  6.1 page
290 where from your (19) produces a single integral equation and no y' term.  After that, plain sailing. Or reduce 2nd
order to 1st order, also QED.

I agree that you have some/lot ODE reading to do, It has all been done before.

IMO your equation (3), (6) is wrong, at least I don't understand it.. Can you explain how you got it? You seem to be
assuming that everything is nice and differentiable everywhere (y) and always (t). Just take$y' = 1/(1-y)$

---

### #180 — amike
*November 23, 2016, 12:48 PM*

> * I was trying to avoid singular initial value problems. But I will definitely come to this in a few days.*
>
>
>
> We'll be waiting.
>
>
>
> My hunch is the power series approach will break down, as will nonlinear IVP will be almost impossible.
>
>
>
> I wonder if amike's s/w can solve Riccati and logistic ODE.
>
> Here is a juicy one
>
>
>
> $t^{1/2}y' = y$
>
> $y'^2 = 4y$
>
>
>
>  *near universal applicability of the method.*
>
> *??*
>
>
>
> Personally, I would consult this to see if my ODE was in there
>
>
>
> **"Handbook of Exact Solutions for Ordinary Differential Equations"**
Trying a power series with sqrt(t) fails as expected, but a simple transform to x=sqrt(t) and then back gives the
expected expansion in sqrt(t) -- which is probably cheating:
EXC1rev.png
This one gives both solutions as expected, and terminates after two terms:
EXC2.png
logistic, riccati in a sec.

---

### #181 — amike
*November 23, 2016, 1:05 PM*

> * I was trying to avoid singular initial value problems. But I will definitely come to this in a few days.*
>
>
>
> We'll be waiting.
>
>
>
> My hunch is the power series approach will break down, as will nonlinear IVP will be almost impossible.
>
>
>
> I wonder if amike's s/w can solve Riccati and logistic ODE.
>
> Here is a juicy one
>
>
>
> $t^{1/2}y' = y$
>
> $y'^2 = 4y$
>
>
>
>  *near universal applicability of the method.*
>
> *??*
>
>
>
> Personally, I would consult this to see if my ODE was in there
>
>
>
> **"Handbook of Exact Solutions for Ordinary Differential Equations"**
Logistic+Riccati, I think in the forms you mentioned earlier...
EXLogistic.png
EXRiccati.png

---

### #182 — amike
*November 23, 2016, 1:12 PM*

> @amike, You are very right that most of the solutions are identical to power series solutions or many times to taylor
series solutions. In fact I believe
>
> ...
>
> evaluation of that function unless there are some complex(in sense of complexity and not complex varaibles) functions
in coefficients that have their own expansions.
>
> As amike suggested, I am doing a revision of my paper adding many other problems that are not basic and hint at near
universal applicability of the method. I thank amike for his critical review.
ok, great, I will have a look again at the revised version.

---

### #183 — Amin (Topic Author)
*November 23, 2016, 4:03 PM*

> Here you can download my paper. [https://papers.ssrn.com/sol3/papers.cfm ... id=2872598](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598) I will improve it over next few days but interesting how so many second order ODEs can be so easily solved.
Looking at eq. 19, section 5.1 We see where things start to get out of hand (double integral equation + y' term on right
side).. go no further.

See Henrici (incidentally mon academic greatgrandpa) "Discrete Variable Methods in ODEs" wiley 1962 section  6.1 page
290 where from your (19) produces a single integral equation and no y' term.  After that, plain sailing. Or reduce 2nd
order to 1st order, also QED.

I agree that you have some/lot ODE reading to do, It has all been done before.

IMO your equation (3), (6) is wrong, at least I don't understand it.. Can you explain how you got it? You seem to be
assuming that everything is nice and differentiable everywhere (y) and always (t). Just take$y' = 1/(1-y)$
Very sorry. Regarding equation 19. sec 5.1, you have to replace "Integrating Equation (18), we get the solution" has to
be replaced by "Integrating Equation (18), we get the formal solution."  This is just formal solution and cannot usually
be evaluated. Sorry for this error. There are other such errors in the paper but will remove them in revision.

Yes, I will further explain equation(3) and equation(6) but tired now and will do it tomorrow.

---

### #184 — Cuchulainn
*November 23, 2016, 4:53 PM*

> * I was trying to avoid singular initial value problems. But I will definitely come to this in a few days.*
>
>
>
> We'll be waiting.
>
>
>
> My hunch is the power series approach will break down, as will nonlinear IVP will be almost impossible.
>
>
>
> I wonder if amike's s/w can solve Riccati and logistic ODE.
>
> Here is a juicy one
>
>
>
> $t^{1/2}y' = y$
>
> $y'^2 = 4y$
>
>
>
>  *near universal applicability of the method.*
>
> *??*
>
>
>
> Personally, I would consult this to see if my ODE was in there
>
>
>
> **"Handbook of Exact Solutions for Ordinary Differential Equations"**
Logistic+Riccati, I think in the forms you mentioned earlier...

EXLogistic.png

EXRiccati.png
I have checked standard logistic on paper and I get the same as yourself:

$f(t) = 1/(1+e^{-t}) == (1 + tanh(t/2))/2$

The even terms in your series and mine for $tanh(t/2)$ disappear so I reckon your s/w should be able to get $O(t^7)$.

On Riccati, I took a sanity check  (p = 1, q = r = 0) and defined $v = y^ {-1}$ to get $v = -t + 1/y_0$ Thus

$ y = y_0/(1- y_0t)$ which diverges if$abs(y_0t) >= 1$ . So a bounded solution exists it seems in a finite interval and
solution blow up at$t =1/y_0$ .

It is easy to check that $y' = y^2$

BTW your s/w writes $ y = y_0/(1- y_0t)$ in series form.

---

### #185 — amike
*November 23, 2016, 5:21 PM*

Yeah, this is pretty much what Maple is good for: checking series expansions that aren't necessarily difficult, but that
aren't interesting enough to engage enough neurons to avoid mistakes if done by hand.  :)  I'd be pretty surprised if it
got any of these wrong, but it can have difficulties finding solutions in some cases and may need a bit of help...

The reported O(t^6) is just the default order of these expansions.  It does not report the next non-zero order, it just
tells you where it stopped looking.

---

### #186 — ppauper
*November 23, 2016, 10:16 PM*

> $t^{1/2}y' = y$
easy, separable

$t^{1/2}dy/dt=y$

$dy/y=t^{-1/2}dt$

$\ln y =2t^{1/2}+c$

$y=C\exp(2t^{1/2})\sim C(1+2t^{1/2}+2t+4/3 t^{3/2}+2/3 t^2+4/15 t^{5/2}+4/45 t^3+\cdots)$

so not taylor-expandable about t=0

---

### #187 — Amin (Topic Author)
*November 24, 2016, 12:34 PM*

@Cuch, I will try to explain Eq(3) and (6) and put them in context. I am writing the section 2 of the paper and then I
will explain everything one equation evolves from the previous equation. If you have any further questions, I will love
to explain.

2. Introduction to the Method of Iterated Integrals

To start the discussion, we try to find the solution to General initial value problem associated with first order
Ordinary Differential Equations given as

$\frac{dy}{dt}=f(t,y),\text{   }t\geq 0,\text{    }y\left(t_0\right)=y_0$    Equation(1)

Integrating Equation (1), we get the solution to the initial value problem as

$y(t)=y\left(t_0\right)+\int_{t_0}^t f(\tau ,y(\tau )) \, d\tau$

Equation (2)

If only we could exactly solve the integral as a function of t, we would find our desired solution. Obviously
$f(\tau ,y(\tau ))$

cannot in general be directly and analytically integrated in the above integral. However, the simplest approximation to
initial value problem with Equation(2) could be found after substituting the initial values of y in the integral of
differential function. This simple solution which is a crude approximation could be given as

$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau$

Equation(3)

But the differential function has dependence on$y(\tau )$ which in turn depends on tau through the differential function
itself. We could write the first indirect derivative of differential function with respect to independent variable as

$\frac{\partial }{\partial y}[f(\tau ,y(\tau ))]\frac{dy(\tau )}{dt}=\frac{\partial }{\partial y}[f(\tau ,y(\tau ))]f(\tau ,y(\tau ))$

Equation (4)

In fact, once we evaluate the Equation (3) at initial value, we could still find the precise value of the integral
everywhere if we could exactly solve for the effect of first indirect derivative of t on the differential function. We
could easily write the Equation (5) as

$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(\tau ))]\frac{dy(s)}{dt}dsd\tau$

$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau +\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}[f(\tau ,y(\tau ))]f(s,y(s))dsd\tau$

Equation(5)

In general, just like the original problem we cannot solve for the integrals in second term of Equation(5) exactly.
However if we substitute initial values of variables in Equation(5), we have an approximation that is better than
approximation in Equation(3) since we have added the effect of one indirect derivative evaluated at initial values to
earlier approximation in Equation(3). Continuing to expand further on Equation(5), we get the new exact expansion in
terms of higher indirect derivatives as

$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau$

$+\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)dsd\tau$

$+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}[f(\tau ,y(\tau ))]f(s,y(s))\right]f(v,y(v))dvdsd\tau$

Equation(6)

Again substituting initial values in Equation(6), we get a better approximation that we got in Equation(5).This
expansion includes the effect of two indirect derivatives evaluated at initial values.

$y(t)=y\left(t_0\right)+\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau$

$+\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)dsd\tau$

$\left.\left.+\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(y\left(t_0\right)\right)\right)\right]f\left(s,y\left(t_0\right)\right)\right)\right]f\left(v,y\left(t_0\right)\right)\right)dvdsd\tau$

Equation (6a)

We can continue to add further terms in our solution and evaluate those terms at the initial value and order of the
method would continue to add precision.

if the independent variable is time, it is interesting to notice intuitively how the upper limits of the inside
integrals go to time in each outer integral so as the higher indirect derivative in inner integrals make a contribution
to lower indirect derivatives only till running time in successive outer integral.

The above is excerpt from the paper page(3-5).

Intuitive Explanation:

We all know that Equation(2) is a formal solution. As Cuch pointed out Eq(3) is not right at all. It is a very crude
approximation. In this equation, we have analytically integrated all the dependence on independent variable t and
substituted initial values for the dependent variable. We have to realize since we analytically integrated with respect
to independent variable t, the explicit dependence of differential equation/function w.r.t independent variable t has
been totally taken care of. We do not need to take further partial derivatives w.r.t independent variable t. Now further
dependence of differential equation/function on t is only through indirect derivative of t that is found after
calculating the partial derivative with respect to y and converting into derivative with respect to t through chain
rule. As in equation (5) we have calculated the first integral as in Equation (3) at the initial value and put all
dependence of true solution on the only first indirect derivative that we have to consider(This derivative is again
considered in the formal sense.)  So double integral in Equation (5) has to be considered in the formal sense.

In equation 6, we have calculated the formal double integral in Equation(5) by substituting initial values there and
again putting all the dependence of true solution on one order higher indirect derivative(derivative of the previous
indirect derivative of the differential equation/function converted into derivative with respect to independent variable
through chain rule) which again has to be considered in the formal sense for the solution to be truly valid. So last
triple integral in the equation (6) has to be considered in the formal sense.

Equation(6a) is a truncation of formal solution in Equation (6) to first three terms.

---

### #188 — Amin (Topic Author)
*November 24, 2016, 1:14 PM*

In the revision, I will be adding many interesting examples especially with significant explicit dependence  of
differential equation w.r.t independent variable that we analytically integrate in each successive iterated integral.

---

### #189 — Amin (Topic Author)
*November 25, 2016, 9:39 AM*

> Though I think most intelligent friends would already have realized how my expansion of variable coefficients into
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
Above is the post 89 on this thread in which I had already mentioned how method of iterated integrals can solve ODEs.
Friends can verify that my recent paper is entirely based on the same idea. The cited post was written on Thu Jun 02,
2016 6:49 am according to wilmott clock.

---

### #190 — Cuchulainn
*November 29, 2016, 10:26 AM*

> $t^{1/2}y' = y$
easy, separable

$t^{1/2}dy/dt=y$

$dy/y=t^{-1/2}dt$

$\ln y =2t^{1/2}+c$

$y=C\exp(2t^{1/2})\sim C(1+2t^{1/2}+2t+4/3 t^{3/2}+2/3 t^2+4/15 t^{5/2}+4/45 t^3+\cdots)$

so not taylor-expandable about t=0
Amin's article is silent on the continuity/Lipschitz conditions of his ODE. Formally plugging the above into article's
equation (6a) suggest the integral blows up. Paul's counterexample diverges even more quickly.

BTW The mathematical  notation in the article needs to be spruced up as it is confusing.

---

### #191 — Amin (Topic Author)
*November 29, 2016, 12:30 PM*

@Cuch, thank you for your helpful review. You will have to combine usual methods for singular initial value problems
with method of iterated integrals. And it is well known that most methods for solution of ODEs have to adapted and
enhanced when they have to tackle singular IVPs. There is a large literature on singular initial value problems so I
would not discus them but I will try to solve at least one example of singular initial value problems in my revision.

I will try to better explain the notation and hopefully my intuitive explanation in earlier post was helpful.

---

### #192 — Cuchulainn
*November 29, 2016, 12:47 PM*

> @Cuch, thank you for your helpful review. You will have to combine usual methods for singular initial value problems
with method of iterated integrals. And it is well known that most methods for solution of ODEs have to adapted and
enhanced when they have to tackle singular IVPs. There is a large literature on singular initial value problems so I
would not discus them but I will try to solve at least one example of singular initial value problems in my revision.
>
> I will try to better explain the notation and hopefully my intuitive explanation in earlier post was helpful.
Fair enough.

Amin, the article does need to define the scope upfront of which ODEs _are_ supported (singular IVPs are not)., It is
not all things to all men and this will save people guessing..

Here's a singularly-perturbed IVP

$\epsilon y' = f(t,y)$ where $\epsilon$ can be very small.

What does your model give?

---

### #193 — Amin (Topic Author)
*December 1, 2016, 7:00 AM*

> $t^{1/2}y' = y$
easy, separable

$t^{1/2}dy/dt=y$

$dy/y=t^{-1/2}dt$

$\ln y =2t^{1/2}+c$

$y=C\exp(2t^{1/2})\sim C(1+2t^{1/2}+2t+4/3 t^{3/2}+2/3 t^2+4/15 t^{5/2}+4/45 t^3+\cdots)$

so not taylor-expandable about t=0
Amin's article is silent on the continuity/Lipschitz conditions of his ODE. Formally plugging the above into article's
equation (6a) suggest the integral blows up. Paul's counterexample diverges even more quickly.

BTW The mathematical  notation in the article needs to be spruced up as it is confusing.
@Cuch, my method gives a perfect solution to the above example. You might have made some careless mistake but the method
works very well on the example. Here is my solution.

Consider the 1st order initial value problem given as

$y'=f(\tau ,y(\tau ))=\frac{y}{\sqrt{\tau }},\text{    }y(0)=y_0$,   $t_0=0$

From the general solution expansion given in Equation (6a), we calculate the coefficients of the first few terms as

$\int_{t_0}^t f\left(\tau ,y\left(t_0\right)\right) \, d\tau =\int_{t_0}^t \frac{y_0}{\sqrt{\tau }} \, d\tau =2\sqrt{t}y_0$

$\int _{t_0}^t\int _{t_0}^{\tau }\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(t_0\right)\right)\right]f\left(s,y\left(t_0\right)\right)dsd\tau$

$=\int _{t_0}^t\int _{t_0}^{\tau }\frac{1}{\sqrt{\tau }}\frac{y_0}{\sqrt{s}}dsd\tau$$=2t y_0$

$\left.\left.\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\frac{\partial }{\partial y}\left[\frac{\partial }{\partial y}\left[f\left(\tau ,y\left(y\left(t_0\right)\right)\right)\right]f\left(s,y\left(t_0\right)\right)\right)\right]f\left(v,y\left(t_0\right)\right)\right)dvdsd\tau$

$=\int _{t_0}^t\int _{t_0}^{\tau }\int _{t_0}^s\frac{1}{\sqrt{\tau }}\frac{1}{\sqrt{s}}\frac{y_0}{\sqrt{v}}dvdsd\tau =\frac{4}{3}t^{1.5} y_0$

And we get the first significant terms of the solution as

$y(t)$$=y_0+2\sqrt{t}y_0+2t y_0+\frac{4}{3}t^{1.5}y_0+\text{...}$

You can verify that higher order terms obtained by continuing are indeed perfectly the same as in true solution. BTW
this is a better example to show how time is integrated in various iterated integrals according to respective
integration variables.

---

### #194 — Cuchulainn
*December 1, 2016, 11:17 AM*

Good.

The correct conclusion that you get the same result as ppauper, although his exponential solution is elegant. Looking at
the series solution can I see it is an exponential?

---

### #195 — Amin (Topic Author)
*December 8, 2016, 12:21 PM*

Yes, of course, we can easily match the series with the exponential definition like

y(t)=y0(1+2 t^.5 + (2 t^.5)^2/2! + (2 t^.5)^3/3! +...)

I have written a small mathematica routine that automatically calculates the coefficients for the solution of first
order ODEs to arbitrary order in the series. It is a small routine but I am sure it will be extremely helpful for people
who have to deal with numerical solution of ODEs. I will take another day or two to extend this routine to 2nd order
ODEs and then distribute the program here for friends. You will be able to solve different 1st and 2nd order ODEs to
desired accuracy up to nth term specified by the user in series form using this small but very helpful mathematica code.

---

### #196 — Amin (Topic Author)
*December 9, 2016, 2:42 PM*

Here is the small program to find different terms in the series solution of first Order ODEs.

In the command 1, the ODE is specified. We have a bernoulli ODE in our case. dy/dt=ty^2-ty. y(0)=.5; You have to input
the appropriate ODE expression here in the form dy/dt=(ODE Expression);

Command 2 would appear as such.

In command 3,4 and 5,  10 is the number of terms in the series expansion. You can set it to any suitable integer.

In command 4, .5 is the initial value y(0) and this has to be appropriately adjusted when it changes.

In command 5, integration is done in the double loop. You have to adjust the starting limits appropriately, I have set
them at zero in the sense that independent variable starts at zero. I will make them totally general in the next version
. Different terms in the series solution are printed in a column at the end. In the next version, I will try to write a
function with all the required inputs. Please disregard any mistakes, I am just a beginner in mathematica programming
and normally use it only for simple symbolic computing.

1. $Z\text{:=}t y^2-t y;$

2. $\text{Zi}[2]=(Z\text{/.}t\to \text{ti}[2])$

3. $\text{For}*=D[\text{Zi},y]*(Z\text{/.}t\to \text{ti}[i+1]))]$

4. $\text{For}=(\text{Zi}\text{/.}y\to .5))]$

5. $\text{For}=\text{Wi};\text{Print};$

$\text{For}[\text{i1}=i,\text{i1}\geq 2,\text{i1}\text{--},(\text{Xi}[\text{i1}-1]=\text{Integrate}[\text{Xi}[\text{i1}],\{\text{ti}[\text{i1}],0,\text{ti}[\text{i1}-1]\}])];\text{Print}[\text{Xi}[\text{i1}]\text{/.}\text{ti}[1]\to t]]$

The true solution to above ODE is 1/(1+exp(x^2/2)) which has the same series solution that we get from our program. This
is a very initial version and I would request friends to report any possible errors, problems and suggestions.

I have given the commands below in text format so you can directly past them from here if you like.

Z := t y^2 - t y;

Zi[2] = (Z /. t -> ti[2])

For[i = 2, i , y]*(Z /. t -> ti[i + 1]))]

For[i = 2, i  = (Zi /. y -> .5))]

For[i = 2, i = 2, i1--, (Xi[i1 - 1] = Integrate[Xi[i1], {ti[i1], 0, ti[i1 - 1]}])];

 Print[Xi[i1] /. ti[1] -> t]]*

---

### #197 — Amin (Topic Author)
*December 10, 2016, 8:23 AM*

Very sorry friends for this typo but the line 2/Command 2 is

$\text{Zi}[2]=(Z\text{/.}t\to \text{ti}[2])$

I had previously wrongly written  $\text{Z}[2]=(Z\text{/.}t\to \text{t}[2])$

and in text format written as

Zi[2] = (Z /. t -> ti[2])

Rest is exactly the same. Again sorry for this typo, I will edit it in the above post as well. It was working well on my
computer but when I copied here on wilmott, I probably copied wrong code from some other line.

---

### #198 — Amin (Topic Author)
*December 12, 2016, 12:35 PM*

When evaluating command 5 that contains the double loop, if you change starting integration limit to general t0, it will
be conveneient to modify the command 5 to include general assumptions that would help mathematica evaluate the integrals
without worrying about complex numbers or other possible issues. Of course, friends would like to modify assumptions
when needed. (Another change is that I have used n instead of 10. for number of terms in the expansion in the previous
code).You could for example modify it as:

$\text{For}*=\text{Wi};\text{Print};$

$\text{For}[\text{i1}=i,\text{i1}\geq 2,\text{i1}\text{--},(\text{Xi}[\text{i1}-1]=\text{Integrate}[\text{Xi}[\text{i1}],\{\text{ti}[\text{i1}],\text{t0},\text{ti}[\text{i1}-1]\}$

$,\text{Assumptions} \to \{\text{ti}[\text{i1}-1]\in  \text{Reals},\text{t0} \in  \text{Reals}, \text{t0} 0\}])];$

$\text{Print}[\text{Xi}[\text{i1}]\text{/.}\text{ti}[1]\to t]]$

And in text as:

For[i = 2, i  = Wi; Print;

For[i1 = i, i1 >= 2, i1--, (Xi[i1 - 1] = Integrate[Xi[i1], {ti[i1], t0, ti[i1 - 1]}, Assumptions -> {ti[i1 - 1] $
$Element] Reals, t0 $ $Element] Reals, t0 0}])];

  Print[Xi[i1] /. ti[1] -> t]]

 It would also be straightforward to modify the expression to add the series in one variable and later use Simplify
command to get one series answer instead of the answer term by term  for each term in the series as I have given.*

---

### #199 — Amin (Topic Author)
*December 16, 2016, 2:44 PM*

Many PDEs of the kind that usually arise in mathematical finance and computational fluid dynamics can be solved with
method of lines with the new modification that the resulting ODEs can easily be solved explicitly with the method of
iterated integrals with large stepping in time. Since the solution is totally explicit, the new method could help much
faster numerical solution of the PDEs that took a very long time to solve. I will post my notes on Wilmott regarding
this application of the method of iterated integrals in the coming week.

---

### #200 — Cuchulainn
*December 17, 2016, 1:54 PM*

> Many PDEs of the kind that usually arise in mathematical finance and computational fluid dynamics can be solved with
method of lines with the new modification that the resulting ODEs can easily be solved explicitly with the method of
iterated integrals with large stepping in time. Since the solution is totally explicit, the new method could help much
faster numerical solution of the PDEs that took a very long time to solve. I will post my notes on Wilmott regarding
this application of the method of iterated integrals in the coming week.
I think you are getting ahead of yourself on this one.

MOL reduces to a study of $exp(At)$ where $A$ is a matrix. (but only for linear PDE)

[viewtopic.php?f=26&t=79451&start=420](https://forum.wilmott.com/viewtopic.php?f=26&t=79451&start=420)

---

[← Previous](page_003.md) | [Index](index.md) | [Next →](page_005.md)
