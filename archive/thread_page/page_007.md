# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 7 of 59** — Posts #301–#350

[← Previous](page_006.md) | [Index](index.md) | [Next →](page_008.md)

---

### #301 — Paul
*January 6, 2017, 12:23 PM*

A. He hasn't addressed any of the examples with no solutions or multiple solutions. He has sidestepped these.

B. Find an example for which his first integral doesn't exist yet the ode has a solution. Easy.

---

### #302 — outrun
*January 6, 2017, 12:29 PM*

> A. He hasn't addressed any of the examples with no solutions or multiple solutions. He has sidestepped these.
>
>
>
> B. Find an example for which his first integral doesn't exist yet the ode has a solution. Easy.
That's pointless IMO, any method can be made to rank better/worse than other methods by constructing specific examples.
It'll be far more valuable to show that this method is "200 year old method X" and then you can refer to the body of
work written about that method and stop all this and move on.

---

### #303 — Cuchulainn
*January 6, 2017, 12:40 PM*

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
Because I know the answer. Well, I do have BA (Mod), MSc and PhD in this very area and applied in industry down many
years. So, yes, I do feel as I can say a little.

You miss the point here; The point is what **list **is saying. P,lease read it carefully. It;s all about **existence**
and **uniqueness** of the solution of the ODE. That's exactly what Paul and list (and myself) are saying!!

---

### #304 — Cuchulainn
*January 6, 2017, 12:42 PM*

> A. He hasn't addressed any of the examples with no solutions or multiple solutions. He has sidestepped these.
>
>
>
> B. Find an example for which his first integral doesn't exist yet the ode has a solution. Easy.
B. And vice versa?

---

### #305 — Amin (Topic Author)
*January 6, 2017, 12:48 PM*

> A. He hasn't addressed any of the examples with no solutions or multiple solutions. He has sidestepped these.
>
>
>
> B. Find an example for which his first integral doesn't exist yet the ode has a solution. Easy.
Yes, you have valid points. More work has to be done. Let us leave some of these questions for future work.

I hope to complete the next version of the paper over the weekend.

---

### #306 — outrun
*January 6, 2017, 1:03 PM*

>
> Have you ever worked in this area? It is stiff ODE, singular/regular perturbations and are numerically very difficult.
Yes I have. But you keep bending the discussion to "you" and change the topic to "who is authority" or something..
that's not interesting.

Read that post I quoted, it's one of the few posts that actually adds something here. Everyone one else is running
around in circles with their fingers in their ears.
Because I know the answer. Well, I do have BA (Mod), MSc and PhD in this very area and applied in industry down many
years. So, yes, I do feel as I can say a little.

You miss the point here; The point is what **list **is saying. P,lease read it carefully. It;s all about **existence**
and **uniqueness** of the solution of the ODE. That's exactly what Paul and list (and myself) are saying!!
It's completely useless (IMO) to try and find cases where it will fail because it would not prove a thing. I can make
Euler fail, Runge Kutta fail, I can make anything fail and it will hence not prove a thing, all these methods can also
be shown to be superior for other specific cased. So examining cases and examples is not getting us anywhere.

A far better approach is to ask: is this done before? If so then you can stop right there. If you're still interested
then you can go ahead and read all the things people have written about it in the past. I think it's very unlikely that
this is something new. It's probably something old and discarded at the time because better method evolved. That
expectation is based on the huge volume of work that has been done in this field by *tremendous* smart people (way more
than any of us) and the fact that Amin is very new to this and has a tendency to overestimate his importance. I know
very little people who would claim a breakthrough.

---

### #307 — Cuchulainn
*January 6, 2017, 1:13 PM*

> A. He hasn't addressed any of the examples with no solutions or multiple solutions. He has sidestepped these.
>
>
>
> B. Find an example for which his first integral doesn't exist yet the ode has a solution. Easy.
Yes, you have valid points. More work has to be done. Let us leave some of these questions for future work.

I hope to complete the next version of the paper over the weekend.
**I have an example, Amin. What I need is a last version of your article "on the general ..." Nov 16. In particular, are
equations (5) and (6) accurate?**

Ex. there are many use cases.

1. Equation (5) compared with ODE with 2 solutions

2. Equation (5) compared with ODE with no solution

Investigate 'discrepancy'.

---

### #308 — Paul
*January 6, 2017, 1:14 PM*

It was presented as a general method. We have found examples where it doesn't work (without other manipulation first).
That was useful.

In the examples we've seen where it works it appears to be no different from other methods. That was useful.

In other cases we've seen that it is slower than other methods. That was useful.

Everything has been useful except the method!

It is an elementary manipulation. No one else is going to call it a breakthrough. Perhaps no one would ever publish it.

"57+73-1234x9876-0.56473=..."? Is this original? Can I find it in the literature?

What we have here is an exam question. (And no one is going to look through 200 years of exams to confirm this!):

"Given ... show that ... provided ... . Use this result to show ..."

Amin: "Murder your darlings," as they say.

---

### #309 — outrun
*January 6, 2017, 1:16 PM*

> Amin: "Murder your darlings," as they say.
figuratively of course

---

### #310 — Paul
*January 6, 2017, 1:23 PM*

> Amin: "Murder your darlings," as they say.
figuratively of course
I did worry about using that quote here.

---

### #311 — Cuchulainn
*January 6, 2017, 3:10 PM*

I sat down the last two hours (and had planned to buy firelighters and the newspaper..) and have done the following:

1. Worked out the  examples and formula by hand. The method is not a) a series b) not really asymptotics but a c)
(convoluted) successive aproximation method. Multiple integrals are not needed.

2. Knowing the solution is c) I worked BY HAND the Picard's process of successive approximations because the ODE ==
Volterra Integral equation of 2nd kind (see Tricomi's book on integrals equations). I get the same terms as Amin's !!

3. Why the multiple integrals, Well, Picard has them as well (they call them *iterated kernels* ).. So it;'s just a
sequence of double integrals.

4. Think of each integral as a layer of an onion (or Russian doll) that you peel off at each iteration. This avoids the
horrendous list of integrals.

Conclusion

A. Seems Amin has rediscovered a powerful result from 19th century. I am 99% sure it's the same method.

B. Awkward notation (See how Tricomi does it).

C. No one uses this  method for numerics (wannie built for that).

D. Existence and uniqueness still an issue .. use Banach contraction mapping as I mentioned. Author does not seem to
care about these issues, or is oblivious to them.

E. Numerical solution of integral equation? See Numerical Recipes chapter 18.2

The big deflection  was not telling us his approach is **successive approximations**. This is real no-no in mathematics
and in scientific articles

QED? (?)

No more questions, mi Lords.

---

### #312 — amike
*January 6, 2017, 3:23 PM*

> A. He hasn't addressed any of the examples with no solutions or multiple solutions. He has sidestepped these.
>
>
>
> B. Find an example for which his first integral doesn't exist yet the ode has a solution. Easy.
Yes, you have valid points. More work has to be done. Let us leave some of these questions for future work.

I hope to complete the next version of the paper over the weekend.
ok, great.  I personally am hoping to see:

1. A clearer, more complete explanation of the derivation of the expansion/method -- I think it's fair to say that
nobody here really understands it.

2. A single example (at least) demonstrating how the method outperforms existing methods/approaches, including what you
mean by `outperform'.

I personally am ok with some vagueness about existence/uniqueness issues for now, since I think that dealing with the
above two issues would make the situation clear enough that they could start to be addressed.  But that's me (and
probably reveals my academic background...).

---

### #313 — Cuchulainn
*January 6, 2017, 3:33 PM*

*1. A clearer, more complete explanation of the derivation of the expansion/method -- I think it's fair to say that
nobody here really understands it.*

As in my previous post, it is Picard in disguise. The two methods are the same.

---

### #314 — amike
*January 6, 2017, 3:53 PM*

> *1. A clearer, more complete explanation of the derivation of the expansion/method -- I think it's fair to say that
nobody here really understands it.*
>
>
>
> As in my previous post, it is Picard in disguise. The two methods are the same.
Interesting.  I'll have a bit of a look at that when I have a chance...

(we crossed there.)

---

### #315 — Paul
*January 6, 2017, 4:08 PM*

> *1. A clearer, more complete explanation of the derivation of the expansion/method -- I think it's fair to say that
nobody here really understands it.*
>
>
>
> As in my previous post, it is Picard in disguise. The two methods are the same.
Interesting.  I'll have a bit of a look at that when I have a chance...

(we crossed there.)
Don't do it! Once you start knowing the history of maths you cease to be a mathematician!

---

### #316 — Cuchulainn
*January 6, 2017, 4:41 PM*

> *1. A clearer, more complete explanation of the derivation of the expansion/method -- I think it's fair to say that
nobody here really understands it.*
>
>
>
> As in my previous post, it is Picard in disguise. The two methods are the same.
Interesting.  I'll have a bit of a look at that when I have a chance...

(we crossed there.)
Don't do it! Once you start knowing the history of maths you cease to be a mathematician!
Not history, the technique.

Seems that the method also works for nth-order ODE but I forget who the inventor is.

---

### #317 — amike
*January 6, 2017, 5:28 PM*

I've never actually done a Picard iteration, so this was good therapy -- and probably belongs firmly in the student
forum, but whatever.

It seems that the Picard iterates will agree with "my" perturbation expansion for linear problems, but all bets are off
for nonlinear cases.  So if I can examine a nonlinear example where the two differ, then I should be able to rule out
one of the two approaches.

So, let's have a look at Example 2 from Amin's paper, page 9, with y_0=0 to keep things simple:

$$ \frac{dy}{dt}=(1+y^2), \quad y(0)=0. $$

Amin's expansion to fifth order is:

$$ y\approx t+\tfrac{1}{3}t^3+\tfrac{2}{15}t^5+\ldots $$

"My" perturbation expansion also gives this at fifth order.

Now do a Picard iteration:

$$ y^{n+1}(t)=y_0+\int_0^t ds f(s,y^n(s)) $$

we get:

$$ y^{1}(t)=t $$

$$ y^{2}(t)=t+\tfrac{1}{3}t^3 $$

$$ y^{3}(t)=t +\tfrac{1}{3}t^3 +\tfrac{2}{15}t^5+\tfrac{1}{63}t^7 $$

and the differences get larger from there...

Am I doing this incorrectly?

---

### #318 — Amin (Topic Author)
*January 6, 2017, 5:30 PM*

> A. He hasn't addressed any of the examples with no solutions or multiple solutions. He has sidestepped these.
>
>
>
> B. Find an example for which his first integral doesn't exist yet the ode has a solution. Easy.
Yes, you have valid points. More work has to be done. Let us leave some of these questions for future work.

I hope to complete the next version of the paper over the weekend.
ok, great.  I personally am hoping to see:

1. A clearer, more complete explanation of the derivation of the expansion/method -- I think it's fair to say that
nobody here really understands it.

2. A single example (at least) demonstrating how the method outperforms existing methods/approaches, including what you
mean by `outperform'.

I personally am ok with some vagueness about existence/uniqueness issues for now, since I think that dealing with the
above two issues would make the situation clear enough that they could start to be addressed.  But that's me (and
probably reveals my academic background...).
Thank you amike for your serious suggestion. OK, I chose ODEs where I could compare the solution with existing methods
that essentially meant that some method already existed to solve them. But I would ask you to suggest a good ODE where
solution is not known possibly nonlinear but not singular(since that would require special treatment) that could be
written in the form of Equation(2) and I will solve it. I am sure there are many many ODEs that cannot be solved by
existing methods but can be solved by the method of iterated integrals. Again, I do appreciate your honest suggestion.

---

### #319 — Amin (Topic Author)
*January 6, 2017, 5:37 PM*

When Picard's method and my method gives the same result to an ODE, it is because that specific ODE can have just one
solution and every method that works would eventually give the same solution. It would be wrong logic to suppose that my
method is the same as Picard's method or power series method because both methods gave the same answer. There was just
one right answer.

---

### #320 — amike
*January 6, 2017, 5:54 PM*

Err...  so you are claiming to have made a `breakthrough' but currently have no examples where your method does anything
new/better?   Even if I generated some examples for you, I could also solve them with the perturbative approach, so what
does the ability to calculate terms in an expansion actually show?

It seems to me that it is up to you to give us motivation to want to use your method, like: "here's the type of problem
where this method is superior, and here's an example of it in action", not for us to have to try to guess where your
method might be useful.

It's like you are trying to sell some gadget to people, and when they ask what it does, you just turn around and ask
them to tell you.  (Wait, that's how many consulting firms and software vendors operate...)

---

### #321 — Amin (Topic Author)
*January 6, 2017, 6:08 PM*

> Err...  so you are claiming to have made a `breakthrough' but currently have no examples where your method does
anything new/better?   Even if I generated some examples for you, I could also solve them with the perturbative
approach, so what does the ability to calculate terms in an expansion actually show?
>
>
>
> It seems to me that it is up to you to give us motivation to want to use your method, like: "here's the type of
problem where this method is superior, and here's an example of it in action", not for us to have to try to guess where
your method might be useful.
>
> It's like you are trying to sell some gadget to people, and when they ask what it does, you just turn around and ask
them to tell you.  (Wait, that's how many consulting firms and software vendors operate...)
Sorry, I was not trying to be so elaborately philosophical. I just was wondering if you would like to give me a
suggestion. It's totally alright otherwise.

---

### #322 — list1
*January 6, 2017, 8:16 PM*

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
"Equation(7) is another formal solution to Equation(1) which is equivalent to formal solution as stated in Equation(2)"
///

It is not right. Formally it should be sounded as Eq (1) and Eq(2) are equivalent. That means that each solution (1) is
a solution (2) and inverse. When you start with(1) it means that you assume that (1) has a solution otherwise it does
not make sense. Then starting from (2) assuming that there exists a solution of (2) you can arrive at (1), ie the eq (1)
and (2) are equivalent given your assumptions. You should also make an assumption on growth of the f in y. Otherwise
solution can reach infinity during a finite time interval. Actually you can do this for arbitrary finite iteration n > 1
too. If you think that having n-th iterative expression you can drop the last term that might be also true you need to
prove that given your assumption on f ( t , y ) the last term will tends to zero.

---

### #323 — Cuchulainn
*January 7, 2017, 10:52 AM*

**(broken latex: Unbalanced $: 1)**

```latex
> I've never actually done a Picard iteration, so this was good therapy -- and probably belongs firmly in the student
forum, but whatever.
>
>
>
> It seems that the Picard iterates will agree with "my" perturbation expansion for linear problems, but all bets are
off for nonlinear cases.  So if I can examine a nonlinear example where the two differ, then I should be able to rule
out one of the two approaches.
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

Picard is used to prove existence and uniqueness in a certain time interval. In the current case the example does not
satisfy the hypotheses. In this case we must have $abs(t)
```

---

### #324 — outrun
*January 7, 2017, 11:50 AM*

So there are cases where (any) power serie expansion blows up. This is a well known fact. What does this add?

I think Amins solution gives the same result as Picard, but it gets the result differently.

Picard does indeed have a uniqueness proof, so maybe it's more interesting to examine if there are cases where Amin's
methods gives different results from Picards? But I doubt that, it's an incremental algoritm where new higher order
terms don't change lower order terms?

---

### #325 — Cuchulainn
*January 7, 2017, 11:55 AM*

> It was presented as a general method. We have found examples where it doesn't work (without other manipulation first).
That was useful.
>
>
>
> In the examples we've seen where it works it appears to be no different from other methods. That was useful.
>
>
>
> In other cases we've seen that it is slower than other methods. That was useful.
>
>
The formal approach taken results in a series which gives little insight into the qualitative properties of the
solution, e.g. attractors, orbits.

I don't see it being used for Method Of Lines (MOL), either.

To be honest, I cannot see how to proceed.

---

### #326 — outrun
*January 7, 2017, 12:00 PM*

We've been discussing 3 power series expansion mehods here: Amin's, Picard's and the perpuative approach. These are
black and white TVs made by different brands. These cases are like "let's try a video of a red rose,.. Oops it fails, no
color. Now let's try a yellow bath duck, ...*again* no color" etc etc etc.

---

### #327 — Cuchulainn
*January 7, 2017, 12:09 PM*

> We've been discussing 3 power series expansion mehods here: Amin's, Picard's and the perpuative approach. These are
black and white TVs made by different brands. These cases are like "let's try a video of a red rose,.. Oops it fails, no
color. Now let's try a yellow bath duck, ...*again* no color" etc etc etc.
Don't know what you are trying to say. Could you explain? I feel that you are more of a spectator than a real
contributor in this thread..

Tell us what your insights on $y' = 1 + y^2, y(0) = 0$.are.

We are basically trying to reverse engineer Amin's method. He is unable to explain. Maybe you tell us?

First, read this

[https://en.wikipedia.org/wiki/Picard%E2 ... 6f_theorem](https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem)

---

### #328 — Cuchulainn
*January 7, 2017, 12:14 PM*

> So there are cases where (any) power serie expansion blows up. This is a well known fact. What does this add?
>
Mathematicians know: The answer is: for which values of t does the series converge?

Read Amin's example 2 and the assumptions behind Picard therorem.

BTW your remark about power series is only half-true.

---

### #329 — outrun
*January 7, 2017, 12:23 PM*

> So there are cases where (any) power serie expansion blows up. This is a well known fact. What does this add?
>
Mathematicians know: The answer is: for which values of t does the series converge?

Read Amin's example 2 and the assumptions behind Picard therorem.

BTW your remark about power series is only half-true.
Yes we all know, there is no need to try an divide the world in people who share the same knowledge as you, and those
who you feel you need to spoonfeed. We are all grown-ups here, no?

I'm talking about your deductive reasoning strategy. 1) you claim Amin's method is the same as Picards. 2) It is well
know that Picards has cases where is won't converge. 3) You pick one of those cases and say that Amin's method blows up
for that one and ask him to respond. This last step is a waste of time and childish IMO because it is already known and
directly follows if your claim 1). I think you should focus on proving 1) instead of using 1) to find cases that blow up
for both Picard and Amin and then tie it to Amins method.If 1) is true than you can stop digging up corner cases using
that right?

---

### #330 — Cuchulainn
*January 7, 2017, 12:31 PM*

> So there are cases where (any) power serie expansion blows up. This is a well known fact. What does this add?
>
Mathematicians know: The answer is: for which values of t does the series converge?

Read Amin's example 2 and the assumptions behind Picard therorem.

BTW your remark about power series is only half-true.
Yes we all know, there is no need to try an divide the world in people who share the same knowledge as you, and those
who you feel you need to spoonfeed. We are all grown-ups here, no?

I'm talking about your deductive reasoning strategy. 1) you claim Amin's method is the same as Picards. 2) It is well
know that Picards has cases where is won't converge. 3) You pick one of those cases and say that Amin's method blows up
for that one and ask him to respond. This last step is a waste of time because it is already known and directly follows
if your claim 1). I think you should focus on proving 1) instead of using 1) to find cases that blow up for both Picard
and Amin and then tie it to Amins method.If 1) is true than you can stop digging up corner cases using that right?
If you had been paying attention you would written the above differently. That corner case is from Amin himself and
taken up by amike. Capische?

And a good idea to read Amin's paper. I hope so. Especially EXAMPLE 2.

---

### #331 — outrun
*January 7, 2017, 12:41 PM*

>
> Mathematicians know: The answer is: for which values of t does the series converge?
>
> Read Amin's example 2 and the assumptions behind Picard therorem.
>
> BTW your remark about power series is only half-true.
Yes we all know, there is no need to try an divide the world in people who share the same knowledge as you, and those
who you feel you need to spoonfeed. We are all grown-ups here, no?

I'm talking about your deductive reasoning strategy. 1) you claim Amin's method is the same as Picards. 2) It is well
know that Picards has cases where is won't converge. 3) You pick one of those cases and say that Amin's method blows up
for that one and ask him to respond. This last step is a waste of time because it is already known and directly follows
if your claim 1). I think you should focus on proving 1) instead of using 1) to find cases that blow up for both Picard
and Amin and then tie it to Amins method.If 1) is true than you can stop digging up corner cases using that right?
If you had been paying attention you would written the above differently. That corner case is from Amin himself and
taken up by amike. Capische?

And a good idea to read Amin's paper. I hope so. Especially EXAMPLE 2.
Fair enough. I didn't realize the example came from Amin himself.

My apologies.

---

### #332 — amike
*January 7, 2017, 1:37 PM*

**(broken latex: Unbalanced $: 5)**

```latex
> I've never actually done a Picard iteration, so this was good therapy -- and probably belongs firmly in the student
forum, but whatever.
>
> ...
>
> Am I doing this incorrectly?
I get the same for Picard.

Picard is used to prove existence and uniqueness in a certain time interval. In the current case the example does not
satisfy the hypotheses. In this case we must have $abs(t)

Well, I guess my point was that the third (or higher) Picard iterate did not seem to be *identical* to Amin's example
expansion.  If you perturb to the next order you get (17/315) t^7, which will only agree with the t^7 term in the next
order Picard iterate -- but then Picard has a large number of higher-order terms in t.

>
> The solution is $tan(t)$, what happens to values of t when $cos(t) == 0$??
>
>
>
> Here is the numerical solution of Amin's example 2. Does his series diverge when t ~ PI/2?
Since it ends up effectively being a power series in t it will never deal with the divergence of the solution very
well...
```

---

### #333 — list1
*January 7, 2017, 4:10 PM*

Actually it looks somewhat strange that say the values$ f^{( n )} ( t_0 , y ( t_0 ))$ , n = 0 , 1, ... at the initial
moment are sufficient to represent a solution of the equation$ y' ( t ) = f ( t , y ( t ) )$ for a smooth function f ( t
, y ) on arbitrary finite interval$[ t_0 , T ] $ . Such statement looks incorrect and i think it is possible to present
an example.

---

### #334 — outrun
*January 7, 2017, 4:22 PM*

> Actually it looks somewhat strange that say the values$ f^{( n )} ( t_0 , y ( t_0 ))$ , n = 0 , 1, ... at the initial
moment are sufficient to represent a solution of the equation$ y' ( t ) = f ( t , y ( t ) )$ for a smooth function f ( t
, y ) on arbitrary finite interval$[ t_0 , T ] $ . Such statement looks incorrect and i think it is possible to present
an example.
Indeed. It's covered the smoothness constraint. The heavyside step function would be a good example of your point, but
that's not smooth..

---

### #335 — Cuchulainn
*January 7, 2017, 4:33 PM*

It looks as if we are all doing Amin's homework/legwork for him!

BTW it's called Heaviside, not  heavyside.

---

### #336 — list1
*January 7, 2017, 4:50 PM*

> It looks as if we are all doing Amin's homework/legwork for him!
>
>
>
> BTW it's called Heaviside, not  heavyside.
Cuch, Amin is a member of the W's community. He has spent a lot of time doing this work and it looks quite a good way to
express our subjective points. It is a situation that he probably does not clear understand the difference between what
does he think he wishes to do and what does he actually have got

---

### #337 — outrun
*January 7, 2017, 5:02 PM*

> It looks as if we are all doing Amin's homework/legwork for him!
>
>
>
> BTW it's called Heaviside, not  heavyside.
I think he plays us by using wordings like "breakthrough". A friend of mine loves arguing so much, he could do it 24/7.
He too makes bold claims all the time -to trigger getting attention-, except he doesn't believe why he says, he just
likes to argue and needs participants. the easiest way to get people's attention is to say stupid bold things.

---

### #338 — list1
*January 7, 2017, 6:15 PM*

> It looks as if we are all doing Amin's homework/legwork for him!
>
>
>
> BTW it's called Heaviside, not  heavyside.
I think he plays us by using wordings like "breakthrough". A friend of mine loves arguing so much, he could do it 24/7.
He too makes bold claims all the time -to trigger getting attention-, except he doesn't believe why he says, he just
likes to argue and needs participants. the easiest way to get people's attention is to say stupid bold things.
I think he does not have enough mathematical skills to go through the problem he started to work. Nevertheless, to make
diagnoses do not what we are calling for.

---

### #339 — outrun
*January 7, 2017, 6:41 PM*

I think he has skills, and knowledge gaps, but he deliberately evades evidence that contradicts his belief that he has a
breakthrough. It's a mega ego thing. You can read it between every single line he writes and the question and posts he
ignores.

If I was in his boots I would:

1) never start out calling something a breakthrough

2) would also worry a lot about prior work and try to establish is that exists or not, follow every lead, actively
search myself

3) don't even expect to have a breakthrough, people like Gauss, Netwon, Euler, Leibniz have examined the field and are
much smarter and more dedicated.

---

### #340 — list1
*January 7, 2017, 8:12 PM*

> I think he has skills, and knowledge gaps, but he deliberately evades evidence that contradicts his belief that he has
a breakthrough. It's a mega ego thing. You can read it between every single line he writes and the question and posts he
ignores.
>
>
>
> If I was in his boots I would:
>
> 1) never start out calling something a breakthrough
>
> 2) would also worry a lot about prior work and try to establish is that exists or not, follow every lead, actively
search myself
>
> 3) don't even expect to have a breakthrough, people like Gauss, Netwon, Euler, Leibniz have examined the field and are
much smarter and more dedicated.
'breakthrough' idea is quite popular in financial marketing when a company is going to sell their programs. In math I
never head about breakthrough results. In a such case they say a good result. Amin began with financial innovation and
then reduce it to pure math. As far as he started with finance applications he used business marketing probably a little
bit earlier than it should be. Though everyone might be wrong.

---

### #341 — ppauper
*January 7, 2017, 10:12 PM*

> BTW it's called Heaviside, not  heavyside.
indeed, what's that, first year undergrad?

---

### #342 — outrun
*January 7, 2017, 10:35 PM*

> BTW it's called Heaviside, not  heavyside.
indeed, what's that, first year undergrad?
Yes, high school. It's the simplest functions that has all derivatives zero, zero power series expansions, yet the
future value can't be approximated by series a passion. It's the primitive of the Dirac delta function.

---

### #343 — Amin (Topic Author)
*January 8, 2017, 6:51 AM*

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

---

### #344 — Cuchulainn
*January 8, 2017, 8:35 AM*

> BTW it's called Heaviside, not  heavyside.
indeed, what's that, first year undergrad?
Absolutely. Mispelling is a signal it kind of says "I've seen it once or twice".

It's also very sloppy.Like writing "Crank Nicholson" which is all over.

---

### #345 — Cuchulainn
*January 8, 2017, 8:37 AM*

> BTW it's called Heaviside, not  heavyside.
indeed, what's that, first year undergrad?
Yes, high school. It's the simplest functions that has all derivatives zero, zero power series expansions, yet the
future value can't be approximated by series a passion. It's the primitive of the Dirac delta function.
The issue was the typo; we all know what it is.

---

### #346 — outrun
*January 8, 2017, 10:51 AM*

>
> indeed, what's that, first year undergrad?
Yes, high school. It's the simplest functions that has all derivatives zero, zero power series expansions, yet the
future value can't be approximated by series a passion. It's the primitive of the Dirac delta function.
The issue was the typo; we all know what it is.
why would "first year undergrad" refer to a typo? What if it was high school like here, or 3rd year? Would any of that
matter?

---

### #347 — Cuchulainn
*January 8, 2017, 12:30 PM*

> It looks as if we are all doing Amin's homework/legwork for him!
>
>
>
> BTW it's called Heaviside, not  heavyside.
Cuch, Amin is a member of the W's community. He has spent a lot of time doing this work and it looks quite a good way to
express our subjective points. It is a situation that he probably does not clear understand the difference between what
does he think he wishes to do and what does he actually have got
Nothing wrong with asking questions. It;s just that it belongs to STUDENT forum. In fact, quite a few of your posts
belong there where.

---

### #348 — Cuchulainn
*January 8, 2017, 12:36 PM*

>
> Yes, high school. It's the simplest functions that has all derivatives zero, zero power series expansions, yet the
future value can't be approximated by series a passion. It's the primitive of the Dirac delta function.
The issue was the typo; we all know what it is.
why would "first year undergrad" refer to a typo? What if it was high school like here, or 3rd year? Would any of that
matter?
Give an example of an ODE with delta coefficient + solution. If you mention something, give a concrete example, like
ppauper and amike have done. We don't need an online descripition of delta. Numbers and insights better. HTH

*It's the primitive of the Dirac delta function.*

??

---

### #349 — Cuchulainn
*January 8, 2017, 12:59 PM*

>
> Cuch, do you understand this explanation? Did you get the logic of equations 3,4 and 5 ?
No, I don't get it. And I don't know why you are dong it.

Equation (2) is fine and standard.

**The leap of faith (for me) is which result of calculus was used in deriving (3)?**

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

---

### #350 — Amin (Topic Author)
*January 8, 2017, 1:00 PM*

>
> Cuch, do you understand this explanation? Did you get the logic of equations 3,4 and 5 ?
No, I don't get it. And I don't know why you are dong it.

Equation (2) is fine and standard.

**The leap of faith (for me) is which result of calculus was used in deriving (3)?**

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
Cuch, you did not answer my post 343 that I have quoted above.

---

[← Previous](page_006.md) | [Index](index.md) | [Next →](page_008.md)
