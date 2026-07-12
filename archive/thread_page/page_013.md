# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 13 of 65** — Posts #601–#650

[← Previous](page_012.md) | [Index](index.md) | [Next →](page_014.md)

---

### #601 — Amin (Topic Author)
*January 22, 2018, 8:15 PM*

We give the Option payoff at the terminal time T on the asset grid. And we can later calculate the payoff at time T-1
using the transition probabilities since they are exactly known between any two points at grid at time T and at time
T-1.

1.To calculate American option, we need to know expected pay off at time T-1 given payoff at time T which is calculated
from transition probabilities.

2. The grid at T-1 also specifies the asset value that is needed for the American option pricing algorithm.

From 1 and 2, we can calculate the exercise boundary at time T-1 beyond which exercise is optimal. And the expected
payoff is again calculated at time T-2 by using the transition probabilities between time T-1 and T-2 and given the
expectation values of payoff at time T-1. Like for every step, exercise boundary is determined at time T-2 from the
knowledge of expected payoff and the asset value at the Grid at time T-2.

Should be very straightforward,

---

### #602 — Billy7
*January 22, 2018, 11:48 PM*

Sounds like a simple extension, don't you want to try it and see how it works? If I had spent so much time researching a
method, I'd be looking forward to show people what it can do.

---

### #603 — Amin (Topic Author)
*January 23, 2018, 3:25 PM*

Ok, will try to do it over this weekend if I can complete it. Though I would have liked a consulting project but I will
do it anyway.

---

### #604 — Cuchulainn
*January 23, 2018, 4:50 PM*

Life does not work that way.

---

### #605 — Amin (Topic Author)
*January 23, 2018, 5:29 PM*

> Life does not work that way.
What do you mean. Can you explain?

---

### #606 — outrun
*January 23, 2018, 5:35 PM*

Below is a link to people looking for help and who want to pay for it. Don't mention any personal problems because
people then will pick someone else without personal problems. They are selfish, want *their* problems solved, as simple
as possible.

Sell your skill realistically, measurable, don't call things breakthrough because that's very subjective and needs
thorough proof and aclaim by peers.

Here:

https://m.freelancer.com/jobs/mathematics

---

### #607 — Amin (Topic Author)
*January 23, 2018, 6:08 PM*

> Below is a link to people looking for help and who want to pay for it. Don't mention any personal problems because
people then will pick someone else without personal problems. They are selfish, want *their* problems solved, as simple
as possible.
>
>
>
> Sell your skill realistically, measurable, don't call things breakthrough because that's very subjective and needs
thorough proof and aclaim by peers.
>
>
>
> Here:
>
>
>
> https://m.freelancer.com/jobs/mathematics
I realized that I do not fit with any of the offered projects. I have always loved working with mathematical finance.
But people are asked to not hire me for any possible projects. I have recently been working with algorithmic trading and
have been able to find several very exploitable patterns in the markets and opportunities to make profit. I would rather
work on improving my algorithmic trading models and perfect them. My dilemma is to keep on doing some work in
mathematical finance even when it is a thankless job just because I love it. I hope after a few months of research and
perfecting my algorithms, I would be doing trading in the financial markets.

BTW the greatest lie that is grounded in the mathematical finance students is that markets are efficient and hence you
cannot make any money trading in the financial markets.

I would still post my programs for American options using the Stochastic calculus of standard deviations if I could
complete them in the time allocated in the coming weekend.

---

### #608 — outrun
*January 23, 2018, 6:31 PM*

So you don't want to do any consulting project that generates money for you. Instead you want to work unpaid on
perfecting your algo model that might generate some revenues.

I say "might" because  backtesting performed in a way that give confidence of future performance is a lot harder than
simulating sde's or proving that a method is superior compared to others. In the last 2 years I haven't seen any such
superior performance proof, so you need to realize your bias.

I hope you spend your time wisely. I understand you have your problems but trying to do a little paid project help you
see the reality of things. What do people want? How much are they willing to pay? How do I rank compared to others?

 Interacting with the outside world and learning to manouvre there might be an enriching experience that leads you in
new positive directions.

---

### #609 — Amin (Topic Author)
*January 23, 2018, 6:43 PM*

Thanks. I do not agree with you all. If you want to argue, make a thread in trading of off-topic. Please do not spoil my
research thread with things that do not belong here.

---

### #610 — outrun
*January 23, 2018, 6:46 PM*

I've seen profitable algorithms, I don't believe in the arbitrage free efficient market blablabla. We agree on that.

But I've also seen people do very naive backtesting on small dataset of daily close prices with overfitted models that
turned out to be very unrealistic. That's all.

---

### #611 — Amin (Topic Author)
*January 23, 2018, 6:52 PM*

My trade time-frame varies from a few seconds to a few minutes at max. Nothing to do with daily close.

---

### #612 — outrun
*January 23, 2018, 6:59 PM*

We can start a new thread of realistic backtesting of algos? No need to talk about the algo itself, only about
assumptions, optimization, and biased. I'll leave the thread creation up to you.

---

### #613 — Cuchulainn
*January 23, 2018, 7:19 PM*

> Life does not work that way.
What do you mean. Can you explain?
I still have difficulty with the mathematics. I can't relate it to anything I know.

[http://www2.math.uu.se/~takis/ETC/Halmo ... teMath.pdf](http://www2.math.uu.se/~takis/ETC/Halmos_howToWriteMath.pdf)

---

### #614 — Amin (Topic Author)
*January 24, 2018, 8:21 AM*

*Sorry bad post.*

---

### #615 — Amin (Topic Author)
*January 30, 2018, 2:02 PM*

I will soon be posting some very interesting, and far-reaching results in stochastics related to densities of SDEs. I
hope to make a post about the new results here tomorrow or day after tomorrow.

---

### #616 — Amin (Topic Author)
*January 30, 2018, 2:17 PM*

Ok, giving a little bit more details. I have been mentioning that transition density is known exactly  between any two
points in the SCSD grid at two different times. This is basically equivalent to knowing green's function related to the
SDE. Now I have found new results that give transition probability or green's function of an arbitrary SDE driven by 
Gaussian noise on two different arbitrary time grids only from the knowledge of the CDF at two different time Grids.
This is like saying that we have solution of density/CDF of an SDE on two different time grids and we can easily
calculate Green's function between all different points on two grids. These density solutions at two different time
grids can be found from a traditional PDE, transform method or something else. There are many methods in stochastics
that calculate marginal probability/density/CDF at a certain time and are used for calibration etc. and these solution
methods do not give knowledge of green's function between two points in time but now we can now easily know the green's
function and transition probabilities across two such arbitrary grids. It is a very powerful and extremely interesting
result and I am sure most stochastic experts would love it. I will post the details tomorrow or day after tomorrow. I
hope it will have far reaching consequences for many numerical methods.

---

### #617 — Amin (Topic Author)
*January 30, 2018, 3:59 PM*

There is a word of caution about programs I uploaded recently for calculation of density of diffusions by SCSD. When
there is absorbtion at zero, the CEV density becomes defective and absorbed particles do not go back into the positive
domain. In my programs, I have calculated such densities with a comparison with normal density and such comparison is no
longer valid for diffusion with absorbtion at zero. People would have noticed that all these densities of CEV diffusions
remain accurate when they do not get to zero but after reaching zero serious differences arise between the SCSD density
and the true density. Again to get good results, we would have to calculate defective normal density comparable to CEV
density with defect somehow and  make a comparison with that to get the true density. Again the reason is that we use
normal density without defect to make a comparison with another defective density and such a comparison is no longer
valid and this problem has to be dealt more carefully by comparing with appropriate defective normal density.

---

### #618 — Amin (Topic Author)
*February 1, 2018, 8:51 PM*

We have marginal densities of an SDE given at two differnt points$t_1$ and$t_2$ in time. I want to show how we can
easily find the conditional and joint density between the points$t_1$ and$t_2$ given only the knowledge of the marginal
densities at$t_1$ and$t_2$ .

Suppose we have solution of SDE density/marginal distribution given on a grid$X_n$ conisting of N subdivisions at time
$t_1$ . Suppose$X_n$ is the center of nth subdivision and$Q_n$ is the CDF associated with the end of nth subdivision on
this grid. Then we have that (integrated)probability mass in nth subdivision calculated from the difference of CDF over
the subdivision is given as

$P_n(t_1)=Q_n(t_1)-Q_{n-1}(t_1)$.

We further suppose we have solution of SDE density/marginal distribution given at a different larger time$t_2$ on a
different grid$X_m$ conisting of M subdivisions. Suppose$X_m$ is the centre of mth subdivision and$Q_m$ is the CDF
associated with the end of mth subdivision at time$t_2$ . Then we have that probability mass in mth subdivision is given
as

$P_m(t_2)=Q_m(t_2)-Q_{m-1}(t_2)$

We want to find out the transition probability/conditional distribution and Green's function between any arbitrary
points$X_n(t_1)$ , and$X_m(t_2)$ on two different time grids.

In order to find the conditional probability between$X_n(t_1)$ and$X_m(t_2)$ , Using the knowledge of$Q_n(t_1)$ , the
CDF associated with$X_n(t_1)$ grid, we first construct a corresponding standard brownian motion grid consisting of N
points denoted as$B_n(t_1)$ such that$Q_n(t_1)$ is the CDF at the end of the nth subdivision$B_n(t_1)$ . We have
constructed this brownian motion grid from knowlwdge of$Q_n(t_1)$ associted with$X_n(t_1)$ using inverse CDF for normal
brownian motion. We emphasize that this is the same CDF associated with$X_n(t_1)$ grid. We call$\tilde{P}_n(t_1)$ the
probability mass in nth subdivision. We emphasize that probabilty mass$\tilde{P}_n(t_1)$ in each of N subdivisions
$B_n(t_1)$ in this standard brownian motion grid is the same as$P_n(t_1)$ in the nth subdivision of$X_n(t_1)$ . This can
easily be done for example using norminv function in matlab or using Quantile function in boost in C++. I would like to
mention that this standard brownian motion$B_n(t_1)$ shares the CDF with$X_n(t_1)$ grid but this standard brownian
motion has its own grid and both$B_n(t_1)$ and$X_n(t_1)$ do not share the grid itself and these grids are constructed to
share the same CDF only. We call this CDF-Equivalent Brownian motion grid. The following holds for these grids

$P \left( X_n(t_1)=x_n\right)=\tilde{P} (B_n(t_1)=b_n)$

Similalry using the knowledge of$Q_m(t_2)$ , the CDF associated with$X_m(t_2)$ grid, we first construct a corresponding
standard brownian motion grid consisting of M points denoted as$B_m(t_2)$ such that$Q_m(t_2)$ is the CDF at the end of
the mth subdivision. The probabilty mass$\tilde{P}_m(t_2)$ in each of M subdivisions in this standard brownian motion
grid is the same as$P_m(t_2)$ in the mth subdivision of$X_m(t_2)$ . I would like to mention that this standard brownian
motion grid$B_m(t_2)$ shares the CDF with$X_m(t_2)$ grid but this standard brownian motion has its own grid and they do
not share the grid itself and this BM grid is constructed to share the CDF only with$X_m(t_2)$ grid. Since this is
CDF_Equivalent Brownian motion grid, the following holds for these grids

$P \left( X_m(t_2)=x_m\right)=\tilde{P} (B_n(t_2)=b_m)$

Now we have two standard brownian motion grids, one$\tilde{B}_n(t_1)$ grid that shares the same CDF associated with time
$t_1$ grid$X_n(t_1)$ with the same number of points. Second standard brownian motion grid$B_m(t_2)$ that shares the same
CDF associated with time$t_2$ grid$X_m(t_2)$ with the same number of points. I would like to mention that these standard
brownian motion grids that share CDF with corresponding X grids, do not share the grid itself and these grids are
constructed to share the CDF only.

The following holds obviously from Bayes's law.

$P\left(X_m\left(t_2\right)=x_m\right)$$=\sum _{n=1}^N P\left( X_m\left(t_2\right)=x_m,X_n\left(t_1\right)=x_n\right)$

$=\sum_{n=1}^N P( X_m(t_2)=x_m |  X_n(t_1)=x_n) P\left( X_n\left(t_1\right)=x_n\right)$

Similarly for Brownian motion grids, it holds that

$\tilde{P}\left(B_m\left(t_2\right)=b_m\right)$
$=\sum _{n=1}^N \tilde{P}\left( B_m\left(t_2\right)=b_m,B_n\left(t_1\right)=b_n\right)$

$=\sum_{n=1}^N \tilde{P}( B_m(t_2)=b_m |  B_n(t_1)=b_n) \tilde{P}\left( B_n\left(t_1\right)=b_n\right)$

if it holds that

$P \left( X_n(t_1)=x_n\right)=\tilde{P} (B_n(t_1)=b_n)$

and

$P \left( X_m(t_2)=x_m\right)=\tilde{P} (B_n(t_2)=b_m)$

Then it also holds that

$P( X_m(t_2)=x_m | X_n(t_1)=x_n)=\tilde{P}( B_m(t_2)=b_m| B_n(t_1)=b_n)$

it means that we can find the transition probabilities or equivalently Green's function between any two$x_n(t_1)$ grid
and$x_m(t_2)$ grid only from the knowledge of their marginal probabilities by equating their transition probabilities to
the ones found from CDF-Equivalent Brownian motion grids.

We Suppose that the process X is lognormal with drift with its transition probabilities are  given as

$P( X_m(t_2)=x_m| X_n(t_1)=x_n)=\int _{x_m-.5 \Delta x_m}^{x_m+.5 \Delta x_m}\frac{1}{X_m\text{sigma}\sqrt{2 \text{Pi}(t_2-t_1)}}\exp (-.5\frac{(\log(X_m)-\log(x_n)-(\text{mu}-.5\text{sigma}^2)(t_2-t_1)){}^2}{\text{sigma}^2(t_2-t_1)}) d X_m$

1st order approximation of this integral holds if subdivisions are small

$P( X_m(t_2)=x_m| X_n(t_1)=x_n)=\frac{1}{x_m\text{sigma}\sqrt{2 \text{Pi}(t_2-t_1)}}\exp(-.5\frac{(\log(x_m)-\log(x_n)-(\text{mu}-.5\text{sigma}^2)(t_2-t_1)){}^2}{\text{sigma}^2(t_2-t_1)})\Delta x_m$

Transition probabilities of the corresponding Brownian motion are given as

$\tilde{P}( B_m(t_2)=B_m| B_n(t_1)=b_n)=\int _{b_m-.5 \Delta b_m}^{b_m+.5 \Delta b_m}\frac{1}{\sqrt{2 \text{Pi}(t_2-t_1)}}\exp (-.5\frac{(B_m-b_n){}^2}{(t_2-t_1)}) d B_m$

1st order approximation of this integral holds that if subdivisions are small

$\tilde{P}( B_m(t_2)=b_m| B_n(t_1)=b_n)=\frac{1}{\sqrt{2 \text{Pi}(t_2-t_1)}}\exp(-.5\frac{(b_m-b_n){}^2}{(t_2-t_1)})\Delta b_m$

Now since $P( X_m(t_2)=x_m | X_n(t_1)=x_n)=\tilde{P}( B_m(t_2)=b_m| B_n(t_1)=b_n)$

Transition probabilities of lognormal diffusion in terms of Brownian motion probabilities will be given as

$P( X_m(t_2)=x_m | X_n(t_1)=x_n)=\frac{1}{\sqrt{2 \text{Pi}(t_2-t_1)}}\exp(-.5\frac{(b_m-b_n){}^2}{(t_2-t_1)})\Delta b_m$

and Green's function of the lognormal diffusion in terms of Brownian motion transition probabilities will be given as

$G( X_m(t_2)=x_m | X_n(t_1)=x_n)=\frac{1}{\sqrt{2 \text{Pi}(t_2-t_1)}}\exp(-.5\frac{(b_m-b_n){}^2}{(t_2-t_1)})\Delta b_m/\Delta x_m$

This result will hold for SDEs but will cease to hold in case of any anomaly like absorbtion of diffusions, barriers, or
killing etc. I think it should hold for SDEs with multiplicative diffusions like Stochastic volatility models but I have
not checked that so I cannot be sure.

There are so many problems in mathematical finance and derivatives pricing when we know the marginal probability but we
still have to use other methods  that require the knowledge of dynamics across different time horizons. I am sure this
research will also be used in filtering theory and stochastic control problems etc.

I will post a program tomorrow that constructs two grids equivalent to what I have posted above and we calculate the
transition probabilities and Green's function of a lognormal diffusion using CDF-Equivalent Brownian motions.

---

### #619 — outrun
*February 2, 2018, 10:03 AM*

> We have marginal densities of an SDE given at two differnt points$t_1$ and$t_2$ in time. I want to show how we can
easily find the conditional and joint density between the points$t_1$ and$t_2$ given only the knowledge of the marginal
densities at$t_1$ and$t_2$ .
Suppose the distribution of X(t1) is symmetrical, e.g. a Gaussian. Now look at two cases:

1) X(t2)=X(t1)

2) X(t2)= - X(t1)

Both version of X(t2) have the exact same marginal distribution, but the joint distributions P(X(t1),X(t2)) (and hence
the conditional distributions) are very different. You can't infer the joint distribution from marginals.

---

### #620 — Amin (Topic Author)
*February 2, 2018, 11:03 AM*

> Amin:We have marginal densities of an SDE given at two differnt points$t_1$ and$t_2$ in time. I want to show how we
can easily find the conditional and joint density between the points$t_1$ and$t_2$ given only the knowledge of the
marginal densities at$t_1$ and$t_2$ .
>
> Suppose the distribution of X(t1) is symmetrical, e.g. a Gaussian. Now look at two cases:
>
> 1) X(t2)=X(t1)
>
> 2) X(t2)= - X(t1)
>
> Both version of X(t2) have the exact same marginal distribution, but the joint distributions P(X(t1),X(t2)) (and hence
the conditional distributions) are very different. You can't infer the joint distribution from marginals.
I have already said that the result only holds for normal noise driven SDEs. Otherwise there could be thousands of
pathological cases. It does hold for lognormal SDEs and CEV SDEs when there is no absorbtion at zero. I am quite
confident it would also hold for most realistic SV models like heston and others but this has to be properly checked.

I will like to emphasize that in case of a negative product of normal driven SDEs, you might have to enhance the method
by intelligently multiplying the proposed method with a negative sign.

I am sure analogous method could work for different(other than normal) noise driven SDEs but that would have to be
worked out according to dynamics of the particular noise.

---

### #621 — outrun
*February 2, 2018, 12:21 PM*

> Amin:We have marginal densities of an SDE given at two differnt points$t_1$ and$t_2$ in time. I want to show how we
can easily find the conditional and joint density between the points$t_1$ and$t_2$ given only the knowledge of the
marginal densities at$t_1$ and$t_2$ .
>
> Suppose the distribution of X(t1) is symmetrical, e.g. a Gaussian. Now look at two cases:
>
> 1) X(t2)=X(t1)
>
> 2) X(t2)= - X(t1)
>
> Both version of X(t2) have the exact same marginal distribution, but the joint distributions P(X(t1),X(t2)) (and hence
the conditional distributions) are very different. You can't infer the joint distribution from marginals.
I have already said that the result only holds for normal noise driven SDEs. Otherwise there could be thousands of
pathological cases. It does hold for lognormal SDEs and CEV SDEs when there is no absorbtion at zero. I am quite
confident it would also hold for most realistic SV models like heston and others but this has to be properly checked.

I will like to emphasize that in case of a negative product of normal driven SDEs, you might have to enhance the method
by intelligently multiplying the proposed method with a negative sign.

I am sure analogous method could work for different(other than normal) noise driven SDEs but that would have to be
worked out according to dynamics of the particular noise.
Suppose simple Brownian motion  where the drift mu(t)  is either 1 in the first half of the interval  t1,t2 and 0 in the
second half,.. or the other way around. These two processes only differ by their deterministic drift function, they have
identical marginal distribution at t1 and t2, yet have very different join and conditional distributions for points in
time inside the interval, the mean on the distribution at points in time inside the interval will be different for the
two cases.

Is a BM with constant diffusion and a deterministic time varying drift something you call  "Normal noise driven SDE"?

dX_t = mu(t)dt + sigma dW

---

### #622 — Amin (Topic Author)
*February 2, 2018, 2:13 PM*

You are confused about something that I tried to explain. Conditional probability between two diffusions has
CDF-Equivalence and they are equated in terms of CDF-Equivalence. Two conditional probabilities are not supposed to be
the same but are equal only in terms of CDF.

I will post a program probably today or tomorrow. Just play with that and try to construct counter-examples and then I
could explain better.

.

---

### #623 — Cuchulainn
*February 2, 2018, 3:56 PM*

You like potato and I like potahto

You like tomato and I like tomahto

---

### #624 — Amin (Topic Author)
*February 2, 2018, 6:32 PM*

Here is a code in which I have compared transition probabilities of the lognormal density using analytic transition
probabilities and the method of CDF-Equivalent Brownian motion. I quickly wrote it and will post another more detailed
code later.

```
function [] = TRProbsFromCDF02()
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
%lognormal SDE is  dlog(X)=mu0 dt -.5*sigma0^2*dt+sigma0*dZ(t)
% with X0 as the starting point.
%We find the transition probability between X(T1) grid and X(T1) Grid from
%CDF-Equivalent Brownian motion method.
X0=1.0;%Start of lognormal desnity. If you change this a lot you might have to tweak with the X1 and X2 grids.
mu0=.2;%mean associated with
sigma0=.75;
T1=.5;%Time horizon for the first Grid.
N=200;%Grid points for the first X1 grid at time t1 or T1
dX1=.06*sigma0*sqrt(T1);
X1(1:N)=exp((1:N)*dX1-N/2*dX1)
%Above is the time 1 or T1 grid for the lognormal distribution
X1_Starts(1)=0;
X1_Starts(2:N-1)=.5*X1(1:N-2)+.5*X1(2:N-1);%Start of the nth subdivision for grid at time T1.
X1_Ends(1:N-1)=.5*X1(1:N-1)+.5*X1(2:N);%End of the nth subdivision for grid at time T1.
logX1CDF(1:N-1)=logncdf(X1_Ends(1:N-1),log(X0)+(mu0-.5*sigma0.^2)*T1,sigma0*sqrt(T1));
%Above, Calculate the CDF associated with each subdivision on T1 Grid.
for nn=1:N-1;
    BR1Ends(nn)=norminv(logX1CDF(nn),0,sqrt(T1));
    %Above Calculate CDF-Equivalent standard Brownian motion GridEnds at time 1,T1
end
BR1(2:N-1)=.5*BR1Ends(1:N-2)+.5*BR1Ends(2:N-1);
%Calculate standard Brownian motion Grid mid points from the Grid Ends
T2=1.0;%Time for the second lognormal grid at time T2.
M=200;%No of subdivisions for the second grid
dX2=.06*sigma0*sqrt(T2);
X2(1:M)=exp((1:M)*dX2-M/2*dX2)%Second non-liear(exponential) Grid mid-points%You can also use a
                              %grid with equal spacing.
X2_Starts(1)=0;
X2_Starts(2:M-1)=.5*X2(1:M-2)+.5*X2(2:M-1);%start of the mth subdivision for grid at time T2.
X2_Ends(1:M-1)=.5*X2(1:M-1)+.5*X2(2:M);%End of the mth subdivision for grid at time T2.
logX2CDF(1:M-1)=logncdf(X2_Ends(1:M-1),log(X0)+(mu0-.5*sigma0.^2)*T2,sigma0*sqrt(T2));
%Above, Calculate the CDF associated with each subdivision on T2 Grid.
for mm=1:M-1;
    BR2Ends(mm)=norminv(logX2CDF(mm),0,sqrt(T2));
    %Above Calculate CDF-Equivalent standard Brownian motion GridEnds at
    %time 2,T2
end
BR2Starts(2:M-1)=BR2Ends(1:M-2);%start of the mth subdivision for standard brownian motion grid at time T2.
BR2(2:M-1)=.5*BR2Ends(1:M-2)+.5*BR2Ends(2:M-1);
%Calculate second time 2, TT2 standard Brownian motion Grid mid points from the Grid Ends
str0='y';
while str0=='y'
    %below you can choose to see the match between the conditional probability
    %between point n at t1 Grid and point m at t2 Grid of the lognormal density.
    %You will input m and n that correspond to
    %nodes on first and second grid. You can continue to do this until the
    %above while loop does not end"
    n=input('Enter the first T1 grid subdivision index, lesser than N-1, greater than 1')
    m=input('Enter the second T2 grid subdivision index, lesser than M-1 greater than 1')

    normpdf(BR2(m)-BR1(n),0,sqrt(T2-T1))*(BR2Ends(m)-BR2Starts(m))
    str=input('Above is the transition probability between chosen points n and m on two lognormal grids calculated
solely from the Brownian motions.Enter to continue.')
    lognpdf(X2(m),log(X1(n))+(mu0-.5*sigma0.^2)*(T2-T1),sigma0*sqrt(T2-T1))*(X2_Ends(m)-X2_Starts(m))
    str=input('Above is the transition probability between chosen points n and m on two lognormal grids calculated
solely from the lognormaldensity.Enter to continue')

    normpdf(BR2(m)-BR1(n),0,sqrt(T2-T1))*(BR2Ends(m)-BR2Ends(m-1))./(X2_Ends(m)-X2_Starts(m))
    str=input('Above is the Greens function between chosen points n and m on two lognormal grids calculated solely from
the Brownian motions.Enter to continue.')
    lognpdf(X2(m),log(X1(n))+(mu0-.5*sigma0.^2)*(T2-T1),sigma0*sqrt(T2-T1))
    str=input('Above is the Greens function between chosen points n and m on two lognormal grids calculated solely from
the lognormaldensity.Enter to continue')

    str0=input('please enter  "y" with single commas to continue or any other input to end the loop')
end
end

```

When you first input 25 and second input 25, you get the following output 0.006855711782086;

Edit: Made a small change in code. Again the following holds as a check: When you first input 25 and second input 25,
you get the following output 0.006855711782086;

---

### #625 — Amin (Topic Author)
*February 7, 2018, 8:33 PM*

I have posted the research paper on SSRN here: [https://papers.ssrn.com/sol3/papers.cfm ... id=3119980](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3119980)

The title of the paper is: Calculation of Transition Probabilities of SDEs only From the Knowledge of Marginal
Probabilities using the CDF-Equivalent Brownian Motion Method.

The abstract is given as: In this article, we show how to calculate the conditional and transition probabilities of any
SDE between two different points across time only from the knowledge of their marginal probabilities on these two time
grids. Briefly, we construct CDF-Equivalent standard Brownian motion grids from the knowledge of marginal probabilities
of the SDE. The solution of conditional and transition probability of the SDE is the found from the solution of
transition probabilities between the corresponding nodes of the CDF-Equivalent standard Brownian motion grids which can
be easily calculated. What is the most interesting is that we do not need to know the SDE dynamics for calculation of
conditional probabilities and the method requires only the knowledge of marginal probabilities. We can, in fact, use
this method to determine the SDE that is best suited as a data generating process.

---

### #626 — ppauper
*February 8, 2018, 2:55 PM*

It looks very good.

I've never seen a forum post cited in a paper  before

---

### #627 — Cuchulainn
*February 8, 2018, 5:15 PM*

There is a precedent; WLD2014 acknowledges a peleton of comrades

[http://onlinelibrary.wiley.com/doi/10.1 ... 10366/epdf](http://onlinelibrary.wiley.com/doi/10.1002/wilm.10366/epdf)

---

### #628 — FaridMoussaoui
*February 8, 2018, 8:34 PM*

so in a paper, Paul wrote that he is the first man in the UK to get an online divorce.

It is less sexy than Nobel prize Jacques Dubochet CV which said:

"1955: First official dyslexic in the canton of Vaud - this permitted being bad at everything ... and to understand
those with difficulties"

[resume of Jacques Dubochet](https://www.unil.ch/dee/en/home/menuinst/people/emeritus-professors/prof-jacques-dubochet.html)

---

### #629 — Paul
*February 8, 2018, 8:46 PM*

> so in a paper, Paul wrote that he is the first man in the UK to get an online divorce.
>
> It is less sexy than...You want my sexy stuff? You couldn’t handle my sexy stuff!

---

### #630 — FaridMoussaoui
*February 8, 2018, 8:50 PM*

> so in a paper, Paul wrote that he is the first man in the UK to get an online divorce.
>
> It is less sexy than...
You want my sexy stuff? You couldn’t handle my sexy stuff!
As Stormy Daniels said, I can handle it

---

### #631 — tags
*February 11, 2018, 7:41 PM*

> It looks very good.
>
> I've never seen a forum post cited in a paper  before
>
> There is a precedent; WLD2014 acknowledges a peleton of comrades
![Image](../images/i.imgur.com/XK2jpwF.png)

---

### #632 — Cuchulainn
*February 12, 2018, 1:58 PM*

> It looks very good.
>
> I've never seen a forum post cited in a paper  before
>
> There is a precedent; WLD2014 acknowledges a peleton of comrades
![Image](../images/i.imgur.com/XK2jpwF.png)
Oh yeah, croot  I'm having flashbacks!

Tunito??

---

### #633 — Cuchulainn
*February 12, 2018, 2:20 PM*

**Seriously though, is anyone going to read Amin's SSRN article and provide feedback?**

After all, he has it all in one place now.

---

### #634 — Amin (Topic Author)
*February 12, 2018, 4:01 PM*

> **Seriously though, is anyone going to read Amin's SSRN article and provide feedback?**
>
>
>
> After all, he has it all in one place now.
No, I wrote the article only on the very latest work.

1. I have not included higher order Monte Carlo of SDEs using method of iterated integrals.

2. I have also not included simulation with stochastic calculus of standard deviations.

These two topics will be covered in two more research papers that I am working on.

---

### #635 — Amin (Topic Author)
*February 12, 2018, 4:06 PM*

I would welcome questions on the article already published on SSRN. If somebody wants to do further work or apply it to
derivatives, I would love to be helpful. I believe it would have a lot of far-reaching and interesting applications.
Please ask the questions or anything that you would like to know better than already explained in the article.

---

### #636 — ppauper
*February 12, 2018, 9:15 PM*

> **Seriously though, is anyone going to read Amin's SSRN article and provide feedback?**
>
I did both already. I said "It looks very good"

---

### #637 — Amin (Topic Author)
*February 15, 2018, 7:55 PM*

In a few days, I would formally present higher order Ito Change of variable formula that takes into account higher
derivatives than the second derivative. I am sure many stochastics experts would already have found it using the logic
of iterated integrals method. I am far slower than many smart people.

I also want to present a higher order PDE method that uses analytics based on higher derivatives to find out the
solution of the PDE. I hope I would be able to present both things sometime in the coming week. It would take sometime
since I want to explain these things via matlab programs.

---

### #638 — MaxwellSheffield
*February 16, 2018, 2:45 PM*

I do not know if these posts are serious, or the sarcasm behind them is too deep.

---

### #639 — Cuchulainn
*February 19, 2018, 8:32 AM*

> I do not know if these posts are serious, or the sarcasm behind them is too deep.
I am pretty sure these posts are serious.

---

### #640 — Amin (Topic Author)
*February 20, 2018, 10:28 PM*

I am very excited about the new results. I will present them with several SDEs with interesting drift and volatility
functions. It would still be two days because I want to confirm everything twice. Very very interesting new things.

---

### #641 — Amin (Topic Author)
*February 23, 2018, 1:46 PM*

If the SDE governing the evolution of stochastic process is given as

$\text{dX}(s)=\mu (X(s))\text{ds} + \sigma (X(s))\text{dz}(s)$

In that case a first order integral comprising only one term has iterated integral extension using Ito, is given as

$\int _0^tX(s)^{\gamma }dz(s)=\int _0^tX(0)^{\gamma }dz(s)$

$+\int _{\text{}^0}^t\int _0^s\gamma  X(v)^{\gamma -1} \mu (X(v))dvdz(s)$

$+\int _{\text{}^0}^t\int _0^s\gamma  X(v)^{\gamma -1} \sigma (X(v))dz(v)dz(s)$

$+.5\int _{\text{}^0}^t\int _0^s\gamma  (\gamma -1)X(v)^{\gamma -2} (\sigma (X(v)))^2dvdz(s)$

Also the first order integral comprising a product of two functions has its iterated integral expansion given as

$\int _0^tX(s)^{\gamma }X(s)^{\beta }dz(s)=\int _0^tX(0)^{\gamma }X(0)^{\beta }dz(s)$       Term (1)

$+\int _{\text{}^0}^t\int _0^sX(v)^{\beta } \gamma  X(v)^{\gamma -1} \mu (X(v))dvdz(s)$        Term(2)

$+\int _{\text{}^0}^t\int _0^sX(v)^{\beta }\gamma  X(v)^{\gamma -1} \sigma (X(v))dz(v)dz(s)$    Term(3)

$+.5\int _{\text{}^0}^t\int _0^sX(v)^{\beta }\gamma  (\gamma -1)X(v)^{\gamma -2} (\sigma (X(v)))^2dvdz(s)$     Term(4)

$+\int _{\text{}^0}^t\int _0^sX(v)^{\gamma } \beta  X(v)^{\beta -1} \mu (X(v))dvdz(s)$          Term(5)

$+\int _{\text{}^0}^t\int _0^sX(v)^{\gamma } \beta  X(v)^{\beta -1} \sigma (X(v))dz(v)dz(s)$            Term(6)

$+.5\int _{\text{}^0}^t\int _0^sX(v)^{\gamma }\beta  (\beta -1)X(v)^{\beta -2} (\sigma (X(v)))^2dvdz(s)$ Term(7)

$+\int _{\text{}^0}^t\int _0^s\gamma  X(v)^{\gamma -1} \beta  X(v)^{\beta -1}(\sigma (X(v)))^2dvdz(s)$           Term(8)

let me present the material that I want to post in next few hours.

---

### #642 — Amin (Topic Author)
*February 25, 2018, 7:57 PM*

> I have posted the research paper on SSRN here: [https://papers.ssrn.com/sol3/papers.cfm ... id=3119980](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3119980)
>
> The title of the paper is: Calculation of Transition Probabilities of SDEs only From the Knowledge of Marginal
Probabilities using the CDF-Equivalent Brownian Motion Method.
>
> The abstract is given as: In this article, we show how to calculate the conditional and transition probabilities of
any SDE between two different points across time only from the knowledge of their marginal probabilities on these two
time grids. Briefly, we construct CDF-Equivalent standard Brownian motion grids from the knowledge of marginal
probabilities of the SDE. The solution of conditional and transition probability of the SDE is the found from the
solution of transition probabilities between the corresponding nodes of the CDF-Equivalent standard Brownian motion
grids which can be easily calculated. What is the most interesting is that we do not need to know the SDE dynamics for
calculation of conditional probabilities and the method requires only the knowledge of marginal probabilities. We can,
in fact, use this method to determine the SDE that is best suited as a data generating process.
I believe that the method given in the paper can be used for very fast simulation of SV and SVJD models where marginal
probabilities are given by transform formulas. If somebody wants me to do this work for them, please email me at
anan2999(at)yahoo(dot)com

---

### #643 — Amin (Topic Author)
*March 1, 2018, 3:17 PM*

> I have posted the research paper on SSRN here: [https://papers.ssrn.com/sol3/papers.cfm ... id=3119980](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3119980)
>
> The title of the paper is: Calculation of Transition Probabilities of SDEs only From the Knowledge of Marginal
Probabilities using the CDF-Equivalent Brownian Motion Method.
>
> The abstract is given as: In this article, we show how to calculate the conditional and transition probabilities of
any SDE between two different points across time only from the knowledge of their marginal probabilities on these two
time grids. Briefly, we construct CDF-Equivalent standard Brownian motion grids from the knowledge of marginal
probabilities of the SDE. The solution of conditional and transition probability of the SDE is the found from the
solution of transition probabilities between the corresponding nodes of the CDF-Equivalent standard Brownian motion
grids which can be easily calculated. What is the most interesting is that we do not need to know the SDE dynamics for
calculation of conditional probabilities and the method requires only the knowledge of marginal probabilities. We can,
in fact, use this method to determine the SDE that is best suited as a data generating process.
I believe that the method given in the paper can be used for very fast simulation of SV and SVJD models where marginal
probabilities are given by transform formulas. If somebody wants me to do this work for them, please email me at
anan2999(at)yahoo(dot)com
In my paper, I have stated that this method could be used for stochastic differential equations driven by normal
uncertainty, however I believe that the method could be used for a much larger class of processes but I did not want to
broaden it since then there could also be many pathological cases and I would have to be very careful. However, I
believe that for most of the nice SV and SVJD, we could simulate using this method.

---

### #644 — Amin (Topic Author)
*March 1, 2018, 3:23 PM*

I would be posting my research paper on simulation of SDEs and related stochastic processes with method of iterated
integrals on coming Monday on SSRN. Though the gist of the method and a lot of simple examples have been on this thread
and on internet for more than a year now, I was not able to write a formal paper. I know there are far more intelligent
and learned people who would want to make very significant contributions  to stochastics than I ever could using this
method, however I would make this request to please give me credit for my original initial research. I hope to be
posting the paper on SSRN on this Monday.

---

### #645 — Amin (Topic Author)
*March 4, 2018, 11:43 AM*

Here I uploaded my paper [https://papers.ssrn.com/sol3/papers.cfm ... id=3133959](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3133959)

The title is: Method of Iterated Integrals for Solution of Stochastic Integrals with Applications to Monte Carlo
Simulation of Stochastic Differential Equations.

Abstract:

In this article we suggest a new method for solutions of stochastic integrals where the dynamics of the variables in
integrand are given by some stochastic differential equation.  We also propose numerical simulation of stochastic
differential equations which is based on iterated integrals method employing Ito change of variable expansion of the
drift and volatility function of the SDE. We repeatedly apply the Ito change of variable formula or Ito product rule to
integrand and find its higher order derivatives and later we find the contribution from these higher order derivatives
to the integrand using higher order iterated integrals. First order derivatives of the integrand, for example, would
employ second order iterated integrals to find their contribution to the solution. We evaluate these iterated integrals
terms at the initial time of the simulation along with the solution of the stochastic integrals which is found in terms
of Hermite polynomials and variance of the integrals. We apply the method of iterated integrals to simulation of various
stochastic differential equations. We find that the accuracy of simulation sharply increases using the method of
iterated integral as compared to naïve and simple monte carlo simulation methods.

---

### #646 — ppauper
*March 4, 2018, 2:42 PM*

as always, it looks very good and thanks once again for including this forum in the references

---

### #647 — Amin (Topic Author)
*March 4, 2018, 5:09 PM*

> Here I uploaded my paper [https://papers.ssrn.com/sol3/papers.cfm ... id=3133959](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3133959)
>
> The title is: Method of Iterated Integrals for Solution of Stochastic Integrals with Applications to Monte Carlo
Simulation of Stochastic Differential Equations.
>
> Abstract:
>
> In this article we suggest a new method for solutions of stochastic integrals where the dynamics of the variables in
integrand are given by some stochastic differential equation.  We also propose numerical simulation of stochastic
differential equations which is based on iterated integrals method employing Ito change of variable expansion of the
drift and volatility function of the SDE. We repeatedly apply the Ito change of variable formula or Ito product rule to
integrand and find its higher order derivatives and later we find the contribution from these higher order derivatives
to the integrand using higher order iterated integrals. First order derivatives of the integrand, for example, would
employ second order iterated integrals to find their contribution to the solution. We evaluate these iterated integrals
terms at the initial time of the simulation along with the solution of the stochastic integrals which is found in terms
of Hermite polynomials and variance of the integrals. We apply the method of iterated integrals to simulation of various
stochastic differential equations. We find that the accuracy of simulation sharply increases using the method of
iterated integral as compared to naïve and simple monte carlo simulation methods.
Sorry, I made minor changes to paper. The legends for some graphs were bad and one graph was misplaced and I had to
change that.

---

### #648 — Amin (Topic Author)
*March 4, 2018, 5:11 PM*

> as always, it looks very good and thanks once again for including this forum in the references
Thank you Peter for your kind words.

---

### #649 — Amin (Topic Author)
*March 4, 2018, 5:53 PM*

I want to ask friends what is the right reference for section 3 of my paper. When I did it, I followed a problem in
"Brownian motion and stochastic calculus" in exercises where the solution was given. I took cue from it, played slightly
around and came up with the formula in section 3. But I am sure the precise problem must have been solved decades ago.
Can somebody point me to appropriate reference and I will add it to my paper.

---

### #650 — Amin (Topic Author)
*March 6, 2018, 7:34 AM*

Ok, this is an older post for a related reference.

For a reference to above formulas with nested dz-integrals when you have calculated the appropriate variance, you can
calculate them by a slight modification after following the reference below.

"Brownian Motion and Stochastic Calculus" by Karatzas and Shreve. You have to follow the Exercise 3.31 on page 167.

Can somebody point to appropriate reference.

---

[← Previous](page_012.md) | [Index](index.md) | [Next →](page_014.md)
