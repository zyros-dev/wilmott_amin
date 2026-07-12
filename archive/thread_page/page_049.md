# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 49 of 59** — Posts #2401–#2450

[← Previous](page_048.md) | [Index](index.md) | [Next →](page_050.md)

---

### #2401 — Amin (Topic Author)
*July 23, 2024, 6:59 PM*

Friends, I am writing this post to explain how easy Hermite polynomial regression is and how to use it in various
diverse settings. Please recall that we have worked with hermite regression and also with joint distribution of random
variables with hermite polynomials (which we did the last winters).

I will try to give two different examples. In first example, we suppose that all explanatory regressor variables can be
represented as a hermite series. In the second example, we will suppose that we have a few explanatory variables that
can be represented by hermite polynomials and one (or more) explanatory variables that are represented by Legendre
variables and we also have one dummy variable in regression.

The only important point is that hermite or in general orthogonal polynomial regression requires just one thing that all
explanatory regressor random variables are converted into their respectively appropriate orthogonal polynomial form. It
is not necessary to convert the  dependent regressand variable into any orthogonal polynomial. And rest of the
regression just goes as a least squares regression.

So taking up the first example, let us suppose we have three explanatory variables$X_1$ ,$X_2$ and$X_3$ and we have a
dependent variable whose value we want to find and is given as Y. And we are using first three hermite variables in the
orthogonal polynomial regression

Suppose we have hermite expansions of $X_1$,  $X_2$ and $X_3$ are given as

$X_1\, =\, a_0\, + \, a_1 \, H_1(Z_1) \,+ \, a_2 \, H_2(Z_1) \, + \, a_3 \, H_3(Z_1)$   Eq(1)

$X_2\, =\, b_0\, + \, b_1 \, H_1(Z_2) \,+ \, b_2 \, H_2(Z_2) \, + \, b_3 \, H_3(Z_2)$   Eq(2)

$X_3\, =\, c_0\, + \, c_1 \, H_1(Z_3) \,+ \, c_2 \, H_2(Z_3) \, + \, c_3 \, H_3(Z_3)$    Eq(3)

These hermite expansions would be found from the individual data points of (sample distribution of ) each explanatory
variable  as we have repeatedly done in the past.

Suppose we have N data points of four dimensional joint data (3 regressors + 1 dependent variable) denoted by index n.

First we would have to invert the sample data of each explanatory variable$X_1$ ,$X_2$ and$X_3$ into respective values
of$Z_1$ ,$Z_2$ and$Z_3$

So if$X_1$ data is given as$X_1(1),\, X_1(2),\, X_1(3),\, \ldots\, X_1(n), \, \ldots \, , \, X_1(N)$ , its inverse in
terms of$Z_1$ would be given as

$Z_1(1),\, Z_1(2),\, Z_1(3),\, \ldots\, Z_1(n), \, \ldots \, , \, Z_1(N)$, and this inverse would be found from Eq(1).

Similalry from Eq(2) , we would be able to find

$X_2(1),\, X_2(2),\, X_2(3),\, \ldots\, X_2(n), \, \ldots \, , \, X_2(N)$ , its inverse in terms of$Z_2$ would be given
as

$Z_2(1),\, Z_2(2),\, Z_2(3),\, \ldots\, Z_2(n), \, \ldots \, , \, Z_2(N)$,

and similarly

from Eq(3), we would be able to find

$X_3(1),\, X_3(2),\, X_3(3),\, \ldots\, X_3(n), \, \ldots \, , \, X_3(N)$ , its inverse in terms of$Z_3$ would be given
as

$Z_3(1),\, Z_3(2),\, Z_3(3),\, \ldots\, Z_3(n), \, \ldots \, , \, Z_3(N)$,

Now we would have to set up the regression matrix as

$\scriptsize{\begin{bmatrix} 1 & H_1(Z_1(1)) & H_2(Z_1(1)) & H_3(Z_1(1)) & H_1(Z_2(1)) & H_2(Z_2(1)) & H_3(Z_2(1)) &
H_1(Z_3(1)) & H_2(Z_3(1)) & H_3(Z_3(1)) \\

1 & H_1(Z_1(2)) & H_2(Z_1(2)) & H_3(Z_1(2)) & H_1(Z_2(2)) & H_2(Z_2(2)) & H_3(Z_2(2)) & H_1(Z_3(2)) & H_2(Z_3(2)) &
H_3(Z_3(2))\\ ... & ... & ... & ... & ... & ... & ... & ... & ... & ... \\ ... & ... & ... & ... & ... & ... & ... & ...
& ... & ... \\1 & H_1(Z_1(n)) & H_2(Z_1(n)) & H_3(Z_1(n)) & H_1(Z_2(n)) & H_2(Z_2(n)) & H_3(Z_2(n)) & H_1(Z_3(n)) &
H_2(Z_3(n)) & H_3(Z_3(n))\\  ... & ... & ... & ... & ... & ... & ... & ... & ... & ...  \\ ... & ... & ... & ... & ... &
... & ... & ... & ... & ... \\

1 & H_1(Z_1(N)) & H_2(Z_1(N)) & H_3(Z_1(N)) & H_1(Z_2(N)) & H_2(Z_2(N)) & H_3(Z_2(N)) & H_1(Z_3(N)) & H_2(Z_3(N)) &
H_3(Z_3(N))

\end{bmatrix} \begin{bmatrix}c_0 \\ c_{11} \\ c_{12} \\ c_{13} \\ c_{21} \\ c_{22} \\ c_{23}\\ c_{31} \\ c_{32} \\
c_{33}\end{bmatrix} \\ \,=\, \begin{bmatrix} Y(1) \\ Y(2) \\ ... \\ ... \\ Y(n) \\ ... \\ ... \\ Y(N) \end{bmatrix}}$

We have to find all the coefficients in above equation by least squares. Once these coefficients are known, for
prediction, first invert any explanatory variable to

associated Z and then use relevant hermite polynomials found from this Z to make a prediction of dependent variable.

Now suppose we have a case 2 where we have one explanatory variable that has hermite form and one variable that has a
Legendre form and one dummy variable.

$X_1\, =\, a_0\, + \, a_1 \, H_1(Z_1) \,+ \, a_2 \, H_2(Z_1) \, + \, a_3 \, H_3(Z_1)$   Eq(1)

$X_2\, =\, b_0\, + \, b_1 \, L_1(U_1) \,+ \, b_2 \, L_2(U_2) \, + \, b_3 \, L_3(U_2)$   Eq(2)

So if$X_1$ data is given as$X_1(1),\, X_1(2),\, X_1(3),\, \ldots\, X_1(n), \, \ldots \, , \, X_1(N)$ , its inverse in
terms of$Z_1$ would be given as

$Z_1(1),\, Z_1(2),\, Z_1(3),\, \ldots\, Z_1(n), \, \ldots \, , \, Z_1(N)$, and this inverse would be found from Eq(1).

and if

So if$X_2$ data is given as$X_2(1),\, X_2(2),\, X_2(3),\, \ldots\, X_2(n), \, \ldots \, , \, X_2(N)$ , its inverse in
terms of$U_1$ would be given as

$U_1(1),\, U_1(2),\, U_1(3),\, \ldots\, U_1(n), \, \ldots \, , \, U_1(N)$, and this inverse would be found from Eq(2).

while $I(1), \, I(2), \,, \ldots, I(n)\, \ldots\,, \, I(N)$ are the instances of dummy variable.

Now we would have to set up the regression matrix as

$\begin{bmatrix} 1 & H_1(Z_1(1)) & H_2(Z_1(1)) & H_3(Z_1(1)) & L_1(U_1(1)) & L_2(U_1(1)) & L_3(U_1(1)) & I(1) \\

1 & H_1(Z_1(2)) & H_2(Z_1(2)) & H_3(Z_1(2)) & L_1(U_1(2)) & L_2(U_1(2)) & L_3(U_1(2)) & I(2)\\ ... & ... & ... & ... &
... & ... & ... & ...  \\  ... & ... & ... & ... & ... & ... & ... & ... \\1 & H_1(Z_1(n)) & H_2(Z_1(n)) & H_3(Z_1(n)) 
& L_1(U_1(n)) & L_2(U_1(n)) & L_3(U_1(n)) & I(n)\\  ... & ... & ... & ... & ... & ... & ... & ...  \\ ... & ... & ... &
... & ... & ... & ... & ... \\

1 & H_1(Z_1(N)) & H_2(Z_1(N)) & H_3(Z_1(N))  & L_1(U_1(N)) & L_2(U_1(N)) & L_3(U_1(N)) & I(N)

\end{bmatrix} \begin{bmatrix}c_0 \\ c_{11} \\ c_{12} \\ c_{13} \\ c_{21} \\ c_{22} \\ c_{3}\end{bmatrix} \\ \,=\,
\begin{bmatrix} Y(1) \\ Y(2) \\ ... \\ ... \\ Y(n) \\ ... \\ ... \\ Y(N) \end{bmatrix}$

Again orthogonal polynomial regression goes just like a simple least square regression but all the explanatory variables
have to be pre-processed and represented in form of the appropriate respective orthogonal polynomials and the rest just
goes like a simple least squares regression.

---

### #2402 — Amin (Topic Author)
*July 24, 2024, 12:27 PM*

>
> In the graphs of last post, I took a time grid with ten seconds resolution. Crypto trades for 24 hours on binance so
there are 8640 points on time grid. I recalculated hermite-series of the log-returns of each of the ten largest
crypto-currencies with four coefficients (one zeroth hermite and three higher hermite polynomials) by ideal normal
measure method (first sorting the data and then regressing on associated values of hermite polynomials) after every
hundred points on our ten seconds grid. So calculation of hermite series was redone again and again after every 16.66
minutes. In each of the successive recalculations, all the data from start of the day was used so first regression had
hundred data count while second regression had 200 data count and so on.  After re-calculation of hermite series of each
crypto-currency, a regression was used to find the regression coefficients of bitcoin log returns on hermite polynomial
representation of one period past log-returns of all the ten currencies including past returns of bitcoin itself. This
regression was also repeated with the calculation of hermite series every 16.66 minutes or 100 time grid units of 10
seconds each. The latest regression coefficients available were used to predict the value of bitcoin log-returns as seen
in graphs on previous post.
>
>
>
> The choice of ten seconds grid, and choice of 100 intervals to redo all the hermite series and regression calculations
was a bit arbitrary and friends might like to use their own judgement about increasing and decreasing these intervals.
Since I had daily data in separate files and first regression was done after hundred time grid points, friends can see
that in all the graphs red line for predicted returns starts after 100 time intervals since this was the time when first
regression results became available in my set up.
>
>
>
> The complete Crypto data was for 42 days and despite that I was recalculating regression after 16.66 minutes of data,
it still took somewhere between 15 to 25 minutes to do all the calculation of 42 days of data on my simple laptop.
>
>
>
> My program made a hypothetical profit of 296,034 dollars for trading one bitcoin (which was roughly around 65,000
dollars) for 42 days(with 24 hours continuous trading) and made 127,969 trades making 2.31 dollars per trade. However
unfortunately due to high commissions proportional to currency being traded on crypto currencies, this was not able to
pay even the two side commissions on the Bitcoin trades for an ordinary user though it could have been hugely profitable
for a lot of stock trading in most stock markets due to a different fixed (as opposed to proportional) commission
structure in many stock markets.
>
>
>
> The seemingly high profits without commissions were possible since our hermite regression was able to capture quite a
large share of total variance/variation in bitcoin price on ten seconds scale as could be seen through graphs in
previous post. But in reality quite a few caveats would exist and making such profits would be impossible. But still I
believe there is very good opportunity for people who could have very high trading volumes and they can make very
handsome profits though actual profits would be substantially (possibly an order of magnitude smaller) smaller than in
the simulation.
>
>
>
> Average lifetime of a trade lasts for roughly 25 seconds for our 41 days of data (first day was missed since the
program was borrowed from an earlier program for stocks and I was missing first day there and I did not properly change
that) or roughly about two and a half ten seconds time intervals on our time grid.
>
>
>
> Profit00 =
>
>      2.960340000000077e+05
>
> NoOfTrades00 =
>
>       127969
>
> ans =
>
>    2.313325883612497
>
>
>
> I did not use precise values of predicted returns and just used a threshold for opening and closing the trades as I
had used before. However, in advanced trading precise values would naturally be very useful in proper and timely
execution of trades.
>
>
>
> Here is the graph of backtest profits without commissions. Unless special incentives are aviable in crypto trading,
the actual profits would be negative after commissions since two-side commissions on more than hundred thousand trades
would be quite larger than the profits shown in the graph.
>
> .
>
> .
>
> Please neglect the tiltle of the graph which is borrowed from stock trading data and is not relevant to crypto data.
This crypto data is for 42 days from June 01, 2024 to July 12, 2024.
>
> .
>
> [![Image](../images/i.postimg.cc/DZhc6XWp/Bit-Coin-Profits01.png)](https://postimg.cc/QB65xVJc)
>
.

.

Friends, who want to make similar numerical experiments and analytics on their own.

The regression for estimation of coefficients is done in cross-correlation sense. I am not using hermite polynomials
because purpose is to emphasize the time index only.

$\, Y(t) \, = \,c_0\, + \, c_1 \, X_1(t) \, + \, c_2 \, X_2(t) \, + \, c_3 \, X_3(t) \, + \, \ldots \, + \, c_N \, X_N(t) \,$

and prediction is done by using the equation ---- emphasizing time index only (In reality we would use hermite
polynomials)

$\, Y(t+1) \, = \,c_0\, + \, c_1 \, X_1(t) \, + \, c_2 \, X_2(t) \, + \, c_3 \, X_3(t) \, + \, \ldots \, + \, c_N \, X_N(t) \,$

The regression is done in cross-correlation sense on the dependent assets at the same  time level as dependent asset on
10 seconds grid. Here in regression index of regressand and regressors both is t.

The Prediction is done in auto-correlation sense. The dependent variable at t+1 is being described by explanatory
variables at time t. Regression coefficients are from previous step where regression was done in cross-correlation
sense.

This works best on ten seconds grid.

---

### #2403 — Amin (Topic Author)
*July 25, 2024, 11:57 AM*

Friends, I had been thinking about some interesting ideas regarding how to simultaneously predict a multi-dimensional
variable from a set of explanatory variables. Least square regression and its variants tell us how to do something like
this for a univariate dependent variable in regression. But what to do when there are more difficult joint
multidimensional distribution based random variables that we want to predict.

And when I thought for sometime about it, I realized that we can actually do it with the infrastructure we have. We can
see first scenario if different dimensions in multidimensional variable to be predicted are independent of each other,
we can simply predict each dimension independently and combine the results.

But that is mostly not the case in real life. Let us suppose we want to predict a three dimensional variable and we have
joint data of multidimensional variable to be predicted and also the joint data of explanatory variables. One thing we
can do is to remove the effect of first dimension variable from second and third dimension variables by running a
hermite regression or in some other intelligent way. And remove the effect of second variable from third variable again
by running a regression or some other statistical method. And then run regressions on combined effect of first variable
and combined effect of second variable and the remaining effect of third variable.

And then I recalled when we worked with solution of joint distribution of multivariate data with hermite polynomials of
different factors (what we did this last winters), we described the joint multidimensional distribution of random
variables in terms of orthogonal factors. We first calculated univariate hermite representation of first dimension in
terms of hermite polynomials of$Z_1$ . And then we removed the effect of$Z_1$ from all other dimensions and described
all this effect again in terms of hermite polynomials of$Z_1$ and this was calculated separately for each variable from
2nd dimension to Nth dimension. So we can call$Z_1$ an orthogonal factor (whose effect on various dimesnions is
described by its own orthogonal hermite polynomials of various degree). We repeated this and described second dimension
from which effect of$Z_1$ had been removed by calculating a second factor$Z_2$ whose hermite polynomials were able to
explain all the remining effect of second dimension. And again removed the effect of$Z_2$ from all other dimensions and
described all this joint effect in terms of hermite polynomials of second factor$Z_2$ . And similarly we divided the
data into N different orthogonal factor Z's ranging from$Z_1$ to$Z_N$ . The first dimension of variable to be explained
was described by factor$Z_1$ and second dimension was described by$Z_1$ and$Z_2$ and last dimension among N dimensions
of dependent variable was described by N Z's. So we basically converted data into N orthogonal factors(in a different
sense than orthogonal polynomials) And when we want to find the effect of explanatory variables on multidimensional
variables, we need to regress each of the orthogonal factor (of multidimensional dependent variable to be explained)
represented by$Z_n$ 's on the explanatory variables and then make a prediction of the multidimensional dependent
variable by inverting back the regression result from factor coordinates to the original random variable coordinates.

I think this way we can use mathematical analytics to solve for quite a few difficult problems where we use AI or ML to
get half baked solutions with limited success.

---

### #2404 — Amin (Topic Author)
*July 25, 2024, 1:18 PM*

Friends, just to explain the orthogonality of various factors as I described in last post a bit more. When we decomposed
the multidimensional random variables into various orthogonal factors$Z_n$ as I described in previous post, there was no
correlation across hermite polynomials of various factors across the polynomials of same order or different order.
However, since this construction was numerical, sometimes a few polynomials of same order picked 0-5% or similar very
low levels of spurious correlations which was actually quite insignificant and small from a practical perspective. This
spurious correlation generally decreased as the sample size increased.

Though there can be some very interesting applications of ideas in above post, I was particularly thinking about some
applications in Bayesian analysis. But please let me compose my thoughts first and I will try to write a detailed post
on that tomorrow.

---

### #2405 — Amin (Topic Author)
*July 25, 2024, 9:39 PM*

Friends, I really think that I should put together all the material on Z-series/Hermite Series research that I have
posted on the forum over past few years in the form of a formal paper. I have also posted a large number of programs on
calculation of Z-series, their transformations, and various applications and I will put the links to the matlab programs
posted on the forum in the footnote to appropriate sections of the paper and if some programs have any errors, I will
post an improved and updated version again on the forum.

I hope Paul would be kind to let me publish my paper in his journal after any advised changes/improvements.

I will start working on it on a full time basis tomorrow and hope that it would be complete in about three weeks. I will
try to make it a good paper and hope to explain everything very well. I have been working with different ideas for
several years now and writing a paper after all this time would be interesting since I have a better understanding of a
lot of work which would usually not be possible right after discovering many of these things. At the moment I just wish
that it goes very well. I hope that I will continue my research at a slower pace and keep posting some new things in the
meantime.

---

### #2406 — Amin (Topic Author)
*July 27, 2024, 10:02 AM*

Friends, I deleted yesterday's post and have an updated version of topics discussed in the paper since I went through
the thread today and found a few things I had missed earlier. I am attaching new outline of my paper here. Of course,
this is very basic and just starting and a large number of things will change but here it is for initial review of
friends. I hope I will prepare a basic paper in next 4-5 days but would have to slowly finesse it later for a few weeks.

.

.

[![Image](../images/i.postimg.cc/v8zSqwXb/PaperA1.png)](https://postimg.cc/231wyJPK)

[![Image](../images/i.postimg.cc/QtpcM701/PageA20.png)](https://postimg.cc/sQgM6MFg)

[![Image](../images/i.postimg.cc/KY3zGyJM/PageA30.png)](https://postimg.cc/qt00wWfJ)

[![Image](../images/i.postimg.cc/1t0Y1kQ0/PaperA4.png)](https://postimg.cc/623hd1TT)

---

### #2407 — Amin (Topic Author)
*July 27, 2024, 12:50 PM*

Friends, I continue to complain about gas in my AC. I am working on my research paper and they released some gas in the
AC. I could literally feel the gas and know that I am having a light headache but more importantly I could not do any
work after that. And then I decided to go out and turned off the AC. And I had some new ideas and I sat again on my
table and re-started my work. The weather was better and the room was not warm so I did not turn on the AC and I could
really work very well. So I continued to work very well for two hours without any AC.

Friends, please protest to American defense to be better and finally end their antics against me.

---

### #2408 — Amin (Topic Author)
*July 27, 2024, 9:34 PM*

Friends, I am working on my paper and reviewing my old work. And I noticed that we used data observations as the only
way to calculate correlations between Hermite polynomials of two hermite-series random variables. But as I was thinking
about it, we can also use values of moments and cross moments of two Hermite-series random variables in order to
calculate correlations between their Hermite polynomials even if we do not have detailed data observations between them.
I will try to explain tomorrow with equations. I want to add this to my paper as well.

The work on the paper is going well but rather a bit slowly. I have made further changes to structure of the paper and
also changed its title to highlight only standard gaussian random variable and Hermite polynomials. The new title is
"Representation of Distribution of Broad Classes of Continuous Random Variables by Power Series in Standard Gaussian
Random Variable And An Equivalent Series in Hermite Orthogonal Polynomials: Estimation, Analytics and Applications". But
I just do not want to keep on posting new versions and I am sure friends would have gotten basic  idea about my work
from previous paper structure.

---

### #2409 — Amin (Topic Author)
*July 28, 2024, 9:01 AM*

>
> Friends, I deleted yesterday's post and have an updated version of topics discussed in the paper since I went through
the thread today and found a few things I had missed earlier. I am attaching new outline of my paper here. Of course,
this is very basic and just starting and a large number of things will change but here it is for initial review of
friends. I hope I will prepare a basic paper in next 4-5 days but would have to slowly finesse it later for a few weeks.
>
> .
>
> .
>
> [![Image](../images/i.postimg.cc/v8zSqwXb/PaperA1.png)](https://postimg.cc/231wyJPK)
>
>
>
> [![Image](../images/i.postimg.cc/QtpcM701/PageA20.png)](https://postimg.cc/sQgM6MFg)
>
> [![Image](../images/i.postimg.cc/KY3zGyJM/PageA30.png)](https://postimg.cc/qt00wWfJ)
>
>
>
> [![Image](../images/i.postimg.cc/1t0Y1kQ0/PaperA4.png)](https://postimg.cc/623hd1TT)
>
.

.

Friends, I had absolutely no concern and I was not thinking about it but mind control guy told me that some persons are
(falsely) complaining that they did many of these things I have included in the paper structure on their own before me. 
I want to tell friends that anybody saying such stuff is absolutely lying. Most of the topics included in paper were
covered more than a year ago on this forum by me and I can cite posts and matlab programs for everything included in the
paper.

All of these things were my genuine ideas.

This basic research was done solely by me but I am sure many good friends might have done a lot of more interesting
things related to this work and for me that is a very welcome thing and that is not what I am talking about.

If some body claims they did some of this before me, please ask them to confront me on this forum so that any issue
could be resolved in front of everyone instead of making private claims behind anybody's back.

However, there is just one thing that I see that I did not do. I proposed conditional expectation in hermite framework
with both correlations and covariances. And that later led to hermite regression. However, I never wrote formulas for
variance of conditional expectations and I am sure quite a few smart people would have found  those formulas on their
own. However, to make my work comprehensive, I will be adding formulas for variance in conditional expectation
framework. This is the only thing I see in my paper that cannot be found on posts made more than a year ago and that
cannot be cited from posts on the forum.

---

### #2410 — Amin (Topic Author)
*July 29, 2024, 11:49 AM*

Friends, I am working on my paper and revisiting all the formulas. I noticed that in multidimensional Newton root search
method for fitting the moments, entries in Jacobian matrix of multidimensional Newton are calculated as.

$\frac{dE \left[{X(Z)}^m \right]}{dc_k}\,\approx E \left[\frac{d \left[{X(Z)}^m \right]}{dc_k}  \right]\, =\,E \left[\, m \,\left(\sum\limits_{n=0}^{N}\, a_n\, {Z}^n \right)^{(m-1)}\,Z^k \right] $

Which is wrong even though works very well on a large number of problems. I will be replacing with exact formula for
jacobain entries and relaese a new version of the program later tonight. I am working to fix this error.

---

### #2411 — Amin (Topic Author)
*July 29, 2024, 2:52 PM*

Friends, sorry the algorithm was already right. I re-did the calculations for the jacobian values with respect to
coefficients with a totally different method and was surprised to see that values of Jacobian derivatives from both
methods matched to last precision digit in matlab. This was probably not a problem.

---

### #2412 — Amin (Topic Author)
*July 30, 2024, 4:57 PM*

Friends, mind control agents have been frantically trying to drug my food and water everyday but I have been able to
survive and have been getting good water even though I was hit by bad food several times. I have continued to work but
at a decreased pace. Every day they try their best to waste my time in the hope that next day they would hit me with bad
food and water in a very significant way and I would not be able to work on my paper for next few days after that but I
have survived.

They have complete control over my computer and I am working with overleaf online latex editor but when I write some
equation, I get very obviously wrong display which is not possible and I have to waste a long time trying to correct the
equations somehow. They are trying to not let me work in the hope that they would be able to hit me with bad food and
water and then I would no longer be able to work on my paper for a longer time.

I want to beg people to please try to stop scum-retards of American defense who have their own racist agenda that they
pursue with great meanness and this in no way reflects the aspirations of good American people who never want to be mean
to people of any nation or religion.

---

### #2413 — Amin (Topic Author)
*July 30, 2024, 10:06 PM*

Friends, I am sort of filling in appropriate material in the paper with the intention to make it perfect with many many
revisions later. Here is a very early, very incomplete and very basic version of the paper I am working for review of
friends.

.

 [HermitePaper01.pdf](./download/file.php?id=10411&sid=dd9fc7ddf10aee49c12ef971984e1d31)
(208.49 KiB) Downloaded 15 times

I am specially writing this post out of the paper on correlations and conditional expectations. This is still very
incomplete and basic and will go through many revisions but still writing the incomplete and informal version as a post.
Again, I still have to explain quite a few more things on this topic and this section finally will be much larger and
will see many revisions. I just filled in basic information.

.

.

.

\section{Correlations Between Different Hermite-Series Random Variables}

\label{sec4}

Since when we find a hermite series representation of a random variable, we decompose it in terms of orthogonal hermite
polynomials. And variance of hermite series polynomial is given separately in terms of variances of hermite polynomials
of different order.  Due to orthogonality property, correlations and covariances between two random variables only exist
between hermite polynomials of both random variables having the same order. Due to this orthogonality property, When
calculating conditional expectation of a random variable with respect to other random variables, we can separately
calculate the conditional expectation of each orthogonal hermite polynomial of target random variable with respect to
hermite polynomials of the explanatory random variables of the same order.

Write calculation of covariance between two Hermite Series random variables.

\subsection{Estimation of Correlations Between two Hermite-Series Random variables }

\label{sec4.1}

 we write the equation for the correlation between first Hermite polynomial of Hermite-Series random variables X and Y
as

$
$\rho_{XY,1} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} \, Z_{X,p} \, \, Z_{Y,p} \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {Z_{X,p}}^2 \,\displaystyle\sum_{p=1}^{P} \, \, {Z_{Y,p}}^2 \,}}$
$

Again, Please notice that for calculation of above equation, we first have to find the specific values of$Z_{X,p}$ and
$Z_{Y,p}$ that are associated with particular pth observation of$X_{p}$ and$Y_{p}$ . This has to be done by numerical
inversion method we described in section ().

For Finding Correlation between second hermite polynomials, we write the equation for the correlation between second
hermite polynomial of X and Y as

$
$\rho_{XY,2} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} \, ({Z_{X,p}}^2-1) \, \, ({Z_{Y,p}}^2-1) \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {(Z_{X,p}^2-1)}^2 \,\displaystyle\sum_{p=1}^{P} \, \, {({Z_{Y,p}}^2-1})^2 \,}}$
$

similarly for nth hermite polynaomial correlations, we would write as

$
$\rho_{XY,n} \, = \,  \frac{\displaystyle\sum_{p=1}^{P}\, H_n(Z_{X,p}) \, \, H_n(Z_{Y,p}) \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {H_n(Z_{X,p})}^2 \,\displaystyle\sum_{p=1}^{P} \, \, {H_n(Z_{Y,p})}^2 \,}}$
$

Please note that correlations are in joint products of values of hermite polynomials. The coefficients of Hermite
Polynomials in respective Hermite-Series are only required for covariances between hermite polynomials.

\subsection{Conditional Expectation of a Hermite-series Random variable given the Value of Another Correlated Hermite
Series Random variable }

\label{sec4.2}

Conditional expectation was earlier known mostly for normal random variable with just a few exceptions. Normal random
variable is just one and most basic hermite polynomial but covariances/correlations and conditional expectations between
higher hermite polynomials go just like between instances of first hermite polynomial which is the normal random
variable itself. By converting a non-random variables into hermite-series, we can easily find conditional expectations
between non-normal random variables which was earlier not possible.

As we said at the start of the section that orthogonality property of hermite polynomials and decomposition of variance
into orthogonal parts means that variances and correlations between random variables exist between hermite polynomials
of the same order. And this implies that conditional expectation of a random variable with respect to other random
variables can be divided into separate covariance/correlation based relationships between hermite polynomials of
different random variables of the same order. Further implying that the conditional expectation of a target random
variable based on other explanatory random variables can be described by sum of separate conditional expectations of
each hermite polynomial of target random variable with respect to hermite polynomials of the explanatory random
variables of the same order.

First we describe univariate conditional expectation of one Hermite-Series random variable on another Hermite-Series
random variable and also calculate variance of this conditional expectation.

Suppose we know univariate hermite series of target variable X and explanatory variable Y. We define some basic
relationships again for clarity

$$X(Z_X)\,=\, \sum\limits_{n=0}^{N}\, b_n\, H_n(Z_X) \,=\, \sum\limits_{n=0}^{N}\, X_n $$

$$Y(Z_Y)\,=\, \sum\limits_{n=0}^{N}\, c_n\, H_n(Z_Y) \,=\, \sum\limits_{n=0}^{N}\, Y_n $$

Normal random variable is just first hermite polynomial and covariances/correlations and conditional expectations of
higher hermite polynomials go just analogously to those of first hermite polynomial.

The conditional expectation of nth hermite polynomial based term (with coefficient$c_n$ ) of the target variable Y is
given in terms of covariance$Cov_{XY,n}$ between nth polynomials of both random variables X and Y and variance
$Var_{X,n}$ of the nth hermite polynomial of explanatory variable X as

$$E[Y_n\,|\, X_n]\,= \, E[c_n \, H_n(Z_Y)\,|\,H_n(Z_X)]\,=\,\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X) $$

$
$Var[Y_n\,|\, X_n]\,= Var[c_n \, H_n(Z_Y)\,|\,H_n(Z_X)]\,=\,Var_{Y,n}\,-\frac{{Cov_{XY,n}}^2}{Var_{X,n}}\,=(1\,-\, {\rho_{XY,n}}^2) \, Var_{Y,n}\, $
$

We can write sum of conditional expectations of all hermite polynomials of target variable Y with respect to explanatory
variable as

$
$ \sum\limits_{n=1}^{N} E[c_n \, H_n(Z_Y),|\,H_n(Z_X)]\,=\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X) $
$

But we know that conditional expectation of Y is equal to sum of conditional expectations of each orthogonal polynomial
of Y including the zeroth hermite polynomial which is the unconditional mean of Y itself, so we can write

$$E[Y \, | \, X]=\mu_Y+ \sum\limits_{n=1}^{N} E[c_n \, H_n(Z_Y)\, | \,H_n(Z_X) ]$$

which means that

$$E[Y\, | \, X]=\mu_Y+\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X) $$

and

$$Var[Y\, | \, X]=\,\sum\limits_{n=1}^{N}\,Var_{Y,n}\,-\frac{{Cov_{XY,n}}^2}{Var_{X,n}}\, $$

$$=\,\sum\limits_{n=1}^{N}\,(1\,-\, {\rho_{XY,n}}^2) \, Var_{Y,n}\,\, $$

We have given the formulas for conditional expected value and the variance of a non-Gaussian random variable Y given
another non-Gausain random variable X, And now non-Gaussian Hermite-series of Y conditional on X could be given as

$
$ Y\, | \, X=\mu_Y+\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X)+\,\sum\limits_{n=1}^{N} \sqrt{(1\,-\, {\rho_{XY,n}}^2)} \, c_n \, H_n(Z_Y)$
$

In the above equation, the first summation term in the RHS sums to a point value which is conditional expected mean and
second summation in the RHS is the unexplained non-gaussian variance structure of the distribution in terms of hermite
polynomials which it inherits from the original distribution.

Multivariate version.....

---

### #2414 — Amin (Topic Author)
*July 31, 2024, 6:54 AM*

Friends, tonight I will present a different conditional expectation formula in which calculation of expectation of
conditional variance would be the same but algorithm for calculation of variance of expected value and resulting
conditional distribution of random variable would be more precise as compared to what I have written in previous post.

The difference would be that we would use all relevant moments of hermite series to get the variance structure of the
conditionally distributed random variable as opposed to only knowledge of variance that we used in our formulas in
previous post written last night. This is one dimensional version of work I did last winters.

I will make a detailed post tonight about it.

---

### #2415 — Amin (Topic Author)
*July 31, 2024, 4:35 PM*

Friends, I have sort of filled in information for the correlations and univariate conditional expectations part of the
paper. I am posting it for interest of friends.

.

.

\section{Correlations Between Different Hermite-Series Random Variables}

\label{sec4}

Since when we find a hermite series representation of a random variable, we decompose it in terms of orthogonal hermite
polynomials. And variance of hermite series polynomial is given separately in terms of variances of hermite polynomials
of different order.  Due to orthogonality property, correlations and covariances between two random variables only exist
between hermite polynomials of both random variables having the same order. Due to this orthogonality property, When
calculating conditional expectation of a random variable with respect to other random variables, we can separately
calculate the conditional expectation of each orthogonal hermite polynomial of target random variable with respect to
hermite polynomials of the explanatory random variables of the same order.

Write calculation of covariance between two Hermite Series random variables.

\subsection{Estimation of Correlations Between two Hermite-Series Random variables }

\label{sec4.1}

 we write the equation for the correlation between first Hermite polynomial of Hermite-Series random variables X and Y
as

$
$\rho_{XY,1} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} \, Z_{1,p} \, \, Z_{2,p} \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {Z_{1,p}}^2 \,\displaystyle\sum_{p=1}^{P} \, \, {Z_{2,p}}^2 \,}}$
$

Again, Please notice that for calculation of above equation, we first have to find the specific values of$Z_{1,p}$ and
$Z_{2,p}$ that are associated with particular pth observation of$X_{p}$ and$ZY_{p}$ . This has to be done by numerical
inversion method we described in section ().

For Finding Correlation between second hermite polynomials, we write the equation for the correlation between second
hermite polynomial of X and Y as

$
$\rho_{XY,2} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} \, ({Z_{1,p}}^2-1) \, \, ({Z_{2,p}}^2-1) \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {(Z_{1,p}^2-1)}^2 \,\displaystyle\sum_{p=1}^{P} \, \, {({Z_{2,p}}^2-1})^2 \,}}$
$

similarly for nth hermite polynaomial correlations, we would write as

$
$\rho_{XY,n} \, = \,  \frac{\displaystyle\sum_{p=1}^{P}\, H_n(Z_{1,p}) \, \, H_n(Z_{2,p}) \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {H_n(Z_{1,p})}^2 \,\displaystyle\sum_{p=1}^{P} \, \, {H_n(Z_{2,p})}^2 \,}}$
$

Please note that correlations are in joint products of values of hermite polynomials. The coefficients of Hermite
Polynomials in respective Hermite-Series are only required for covariances between hermite polynomials.

\subsection{Conditional Expectation of a Hermite-series Random variable given the Value of Another Correlated Hermite
Series Random variable }

\label{sec4.2}

Conditional expectation was earlier known mostly for normal random variable with just a few exceptions. Normal random
variable is just one and most basic hermite polynomial but covariances/correlations and conditional expectations between
higher hermite polynomials go just like between instances of first hermite polynomial which is the normal random
variable itself. By converting a non-random variables into hermite-series, we can easily find conditional expectations
between non-normal random variables which was earlier not possible.

As we said at the start of the section that orthogonality property of hermite polynomials and decomposition of variance
into orthogonal parts means that variances and correlations between random variables exist between hermite polynomials
of the same order. And this implies that conditional expectation of a random variable with respect to other random
variables can be divided into separate covariance/correlation based relationships between hermite polynomials of
different random variables of the same order. Further implying that the conditional expectation of a target random
variable based on other explanatory random variables can be described by sum of separate conditional expectations of
each hermite polynomial of target random variable with respect to hermite polynomials of the explanatory random
variables of the same order.

First we describe univariate conditional expectation of one Hermite-Series random variable on another Hermite-Series
random variable and also calculate variance of this conditional expectation.

Suppose we know univariate hermite series of target variable X and explanatory variable Y. We define some basic
relationships again for clarity

$$X(Z_X)\,=\, \sum\limits_{n=0}^{N}\, b_n\, H_n(Z_X) $$

$$ =\, \sum\limits_{n=0}^{N}\, X_n $$

$$Y(Z_Y)\,=\, \sum\limits_{n=0}^{N}\, c_n\, H_n(Z_Y) $$

$$ =\, \sum\limits_{n=0}^{N}\, Y_n $$

$$Var_{X,n}\,=\, E \left[ {X_n}^2\right]\,=\, {b_n}^2 E \left[ {H_n(Z_X)}^2\right]\,=\, {b_n}^2 n! $$

$$Var_{Y,n}\,=\, E \left[ {Y_n}^2\right]\,=\, {c_n}^2 E \left[ {H_n(Z_Y)}^2\right]\,=\, {c_n}^2 n! $$

$
$Cov_{XY,n}\,=\, E \left[ X_n \, Y_n\right]\,=\, b_n\, c_n\, E \left[ H_n(Z_X) \, H_n(Z_Y) \right]\,=\, b_n \, c_n \, \rho_{XY,n} n! $
$

$$Var[Y\,]=\,\sum\limits_{n=1}^{N}\,Var_{Y,n}\, $$

$$Var[X\,]=\,\sum\limits_{n=1}^{N}\,Var_{X,n}\, $$

$$Cov_{XY}\,=\,\sum\limits_{n=1}^{N}\,Cov_{XY,n}\, $$

Normal random variable is just first hermite polynomial and covariances/correlations and conditional expectations of
higher hermite polynomials go just analogously to those of first hermite polynomial.

The conditional expectation of nth hermite polynomial based term (with coefficient$c_n$ ) of the target variable Y is
given in terms of covariance$Cov_{XY,n}$ between nth polynomials of both random variables X and Y and variance
$Var_{X,n}$ of the nth hermite polynomial of explanatory variable X as

$$E[Y_n\,|\, X_n]\,= \, E[c_n \, H_n(Z_Y)\,|\,H_n(Z_X)]\,=\,\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X) $$

$
$Var[Y_n\,|\, X_n]\,= Var[c_n \, H_n(Z_Y)\,|\,H_n(Z_X)]\,=\,Var_{Y,n}\,-\frac{{Cov_{XY,n}}^2}{Var_{X,n}}\,=(1\,-\, {\rho_{XY,n}}^2) \, Var_{Y,n}\, $
$

We can write sum of conditional expectations of all hermite polynomials of target variable Y with respect to explanatory
variable as

$
$ \sum\limits_{n=1}^{N} E[c_n \, H_n(Z_Y),|\,H_n(Z_X)]\,=\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X) $
$

But we know that conditional expectation of Y is equal to sum of conditional expectations of each orthogonal polynomial
of Y including the zeroth hermite polynomial which is the unconditional mean of Y itself, so we can write

$$E[Y \, | \, X]=\mu_Y+ \sum\limits_{n=1}^{N} E[c_n \, H_n(Z_Y)\, | \,H_n(Z_X) ]$$

which means that

$$E[Y\, | \, X]=\mu_Y+\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X) $$

and

$$Var[Y\, | \, X]=\,\sum\limits_{n=1}^{N}\,Var_{Y,n}\,-\frac{{Cov_{XY,n}}^2}{Var_{X,n}}\, $$

$$=\,\sum\limits_{n=1}^{N}\,(1\,-\, {\rho_{XY,n}}^2) \, Var_{Y,n}\,\, $$

We have given the formulas for conditional expected value and the variance of the random variable, Hermite-series of Y
conditional on X could be given as

$
$ Y\, | \, X=\mu_Y+\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X)+\,\sum\limits_{n=1}^{N} \sqrt{(1\,-\, {\rho_{XY,n}}^2)} \, c_n \, H_n(Z_Y)$
$

$
$ =\mu_Y+\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \, c_n \, H_n(Z_X)+\,\sum\limits_{n=1}^{N} \sqrt{(1\,-\, {\rho_{XY,n}}^2)} \, c_n \, H_n(Z_Y)$
$

In the above equation, the first summation term in the RHS sums to a point value which is conditional expected mean and
second summation in the RHS is the unexplained non-gaussian variance structure of the distribution in terms of hermite
polynomials which it inherits from the original distribution.

Multivariate version.....

\subsection{De-correlating the effect of a Hermite-series Random variable from Another Correlated Hermite Series Random
variable }

\label{sec4.3}

In order to remove the effect of a random variable X from another correlated random variable Y, we remove the
conditional expected value of$E\left[Y|X\right]$ from the observed value of Y. This decorrelated value can be written as
an equation as

$$ \tilde{\tilde{X}} \,=\, X\, -\, E\left[Y|X \right] \, $$

This removal of effect of some correlated random variable could have some very interesting applications in finance where
we want to find the effect of a particular variable after removing effects of other variables.

\subsection{Calculating the true distribution structure in Uni-variate Conditional Expectation of a Correlated Random
variable }

\label{sec4.4}

In order to find the true distribution associated with univariate conditional expectation of a random variable, we
perform the de-correlation operation discussed in previous subsection on jointly observed values of data sample of X and
Y, we can find that$\tilde{\tilde{Y}}$ represents the true residual part of Y that has not been explained by the
variable X. Suppose we have a sample of P values represented by$\tilde{\tilde{Y}}_p\, , p\,=\,1,...,P$ , we use this
sample of values of$\tilde{\tilde{Y}}_p\, $ to construct an associated Hermite Series from one of the methods discussed
in section 3.00000.

Suppose this Hermite Series to be found from data of $\tilde{\tilde{Y}}_p\, $ is given as

$$\tilde{\tilde{Y}}(Z_Y)\,=\, \sum\limits_{n=0}^{N}\, \tilde{\tilde{c}}_n\, H_n(Z_Y) $$   Eq(A0)

We can write the variance of conditional expectation of X as

$
$Var \left[ Y|X \right] \,=\,Var \left[ \tilde{\tilde{Y}}_n \right] \,\,=\, \,\sum\limits_{n=1}^{N}\,{\tilde{\tilde{c_n}}}^2 n! $
$

The above point variance should perfectly match the conditional point variance we found in section 4.2 also given here
as

$
$Var[Y\, | \, X]=\,\sum\limits_{n=1}^{N}\,(1\,-\, {\rho_{XY,n}}^2) \, Var_{Y,n}\,\,=\, \,\sum\limits_{n=1}^{N}\,(1\,-\, {\rho_{XY,n}}^2) \,{c_n}^2 n! $
$

However we stress again that even though point variance is perfectly matched, the true structure of variance in
distribution sense is not given by  Eq(A) ( though usually close enough but not always)

$$ \,\sum\limits_{n=1}^{N} \sqrt{(1\,-\, {\rho_{XY,n}}^2)} \, c_n \, H_n(Z_Y)$$

and is rather given by Eq(B)

$$\tilde{\tilde{Y}}(Z_Y)\,=\, \sum\limits_{n=0}^{N}\, \tilde{\tilde{c}}_n\, H_n(Z_Y) $$

We want to mention again that point value of second central moment, variance, would be the same true value in both Eq(A)
and Eq(B) but Eq(B) gives the true distribution of unexplained part of random variable Y. The reason is that once effect
of conditional expected value is removed, even though total residual variance can be precisely calculated but there is
re-arrangement or re-distribution of variance among hermite polynomials and their coefficients cannot be analytically
calculated through correlations (which is reasonably close but not true) and have to be found from the data as we have
done in Eq(A0).

So now the conditional distribution of Y|X would be written as

$$ Y\, | \, X=\, E \left[ Y|X \right] + \, \tilde{\tilde{Y}}(Z_Y)\,$$

$
$ Y\, | \, X=\mu_Y+\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X)+\, \sum\limits_{n=0}^{N}\, \tilde{\tilde{c}}_n\, H_n(Z_Y)$
$

$
$ =\mu_Y+\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \, c_n \, H_n(Z_X)+\, \sum\limits_{n=0}^{N}\, \tilde{\tilde{c}}_n\, H_n(Z_Y)$
$

We want to emphasize that same data that is used to estimate correlation based variance and distribution in
subsection(4.2) can be used for calculation of true conditional distribution as described in this section (4.4) and once
above equation has been calculated from data, we can use it for conditional distribution of random variable Y as single
(or more) values of X become available just as easily as we did for correlation based conditional distribution.

---

### #2416 — Amin (Topic Author)
*August 1, 2024, 5:41 AM*

Friends, there is need for more work with conditional expectation especially when variance of a random variable is
dependent on another correlated explanatory variable.

While calculating conditional expectation in previous post, we have assumed that variance of Y is independent of X which
is most likely not the case. For example consider an SDE-like dependence equation of a random variable

$$ \,Y \,= \, \mu(X) \, + \, \sigma(X) \, Z $$

where$ \mu(X) $ and$ \sigma(X) $ are some functions of a random variable X. The first term$\, \mu(X) \,$ should be
perfectly captured by correlations in our conditional expectation equation but we see that variance term
$\,\,\sigma(X) \, Z\,\, $ , in equation that describes Y, even though orthogonal to X is not independent of X. So
different realizations of X over its density should also affect and alter the distribution of variance of Y and we would
have to do more analytics to calculate the effect of X on variance of Y for a right and proper calculation of
conditional distribution of Y.

I thought about this problem and this is very do-able when dependency structure of X on variance of Y i.e$ \sigma(X) $
is explicitly known and I will present a solution to it in a new post later tonight

---

### #2417 — Amin (Topic Author)
*August 1, 2024, 8:22 AM*

\subsection{Calculating the true distribution structure in Uni-variate Conditional Expectation of a Correlated Random
variable when its variance is dependent on Explanatory Variable }

\label{sec4.4}

While calculating conditional expectation in previous post, we have assumed that variance of Y is independent of X which
is most likely not the case. For example consider an SDE-like dependence equation of a random variable

$$ \,Y \,= \, \mu(X) \, + \, \sigma(X) \, W $$

where W would usually be a non-Gaussian random variable which is assumed to be independent of$\sigma(X) \,$ and
$ \mu(X) $ and$ \sigma(X) $ are some functions of a random variable X. The first term$\, \mu(X) \,$ should be perfectly
captured by correlations in our conditional expectation equation but we see that variance term$\,\,\sigma(X) \, Z\,\, $
, in equation that describes Y, even though orthogonal to X is not independent of X. So different realizations of X over
its density should also affect and alter the distribution of variance of Y and we would have to do more analytics to
calculate the effect of X on variance of Y for a right and proper calculation of conditional distribution of Y.

In order to find the true distribution associated with univariate conditional expectation of a random variable, we again
perform the de-correlation operation discussed in previous subsection on jointly observed values of data sample of X and
Y, we can find that$\tilde{\tilde{Y}}$ represents the true residual part of Y that has not been explained by the
variable X.

This decorrelated value can be written as an equation as

$$ \tilde{\tilde{Y}} \,=\, Y\, -\, E\left[Y|X \right] \, $$

From section (), we already know that we can find a Z-series of$\sigma(X(Z))$ through Taylor Series on Z-series of X as
given in subsection()

$$\sigma(X(Z_X))=\sum\limits_{n=0}^{N}\, d_n\, H_n(Z_X)$$

if $\mu_{\sigma(X),n}\,$ represents nth moment of $\sigma(X)$, We can find moments of $ \sigma(X)$ as

$$\mu_{\sigma(X),n}\, =\, E\left[\sum\limits_{n=0}^{N}\, d_n\, H_n(Z_X) \right]^n $$

Now we see that Z-series structure of $ \tilde{\tilde{Y}} $ with dependency structure included in equation is given as

$
$ \tilde{\tilde{Y}} \,=\, \, \sigma(X) \,\,W\,=\, \, \sigma(X) \,\, \sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y) \ \, $
$

The random variable$\,W\,$ with Hermite Series representation given as
$\, \sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y) \ \,$ with as yet undetermined coefficients is supposed to
capture the distribution structure of non-Gaussian noise in the variance equation. And if$\mu_{\tilde{\tilde{Y}},n}\,$
represents nth moment of$\tilde{\tilde{Y}}\,$ , this nth moment can be written because of independence between
$\,\mu_{\sigma(X),n}\,$ and$\, W \,$ as

$$\mu_{\tilde{\tilde{Y}},n}\, =\,\mu_{\sigma(X),n}\, \,\mu_{W,n}\, \, $$

Since$\mu_{\tilde{\tilde{Y}},n}\,$ can be easily calculated from data of decorrelated values$\tilde{\tilde{Y}} $ , and
we can also easily calculate the moments$\mu_{\sigma(X),n}\,$ as earlier describe, we get the equation for moments of
non-Gaussian noise W as

$$ \, \mu_{W,n} \, \,= \, \frac{\mu_{\tilde{\tilde{Y}},n}\,}{\,\mu_{\sigma(X),n}}\,$$

Once we have found the moments of non-Gaussian noise given as$\, \mu_{W,n} \, $ , we can use these moments with
multidimensional Newton root search method to estimate coefficients$\tilde{\tilde{c}}_m\,$ as described earlier in
section (3.) using the equations

$$ E \, \left[\sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y)\right]^n \,=\,\, \mu_{W,n} $$

Then conditional distribution of Y would be given as

$$ Y\, | \, X=\, E \left[ Y|X \right] + \, \tilde{\tilde{Y}}(Z_Y)\,$$

$
$ Y\, | \, X=\mu_Y+\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X)+\,\, \left[ \sum\limits_{n=0}^{N}\, d_n \, H_n(Z_X) \right] \, \left[\sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y)\right] $
$

$
$ Y\, | \, X=\mu_Y+\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \, c_n \, H_n(Z_X)+\,\, \left[ \sum\limits_{n=0}^{N}\, d_n \, H_n(Z_X) \right] \, \left[\sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y)\right] $
$

Again  once coefficients in above equation have been calculated from data, we can use it for conditional distribution of
random variable Y as single (or more) values of X become available just as easily as we did for correlation based
conditional distribution.

---

### #2418 — Amin (Topic Author)
*August 2, 2024, 12:54 PM*

Friends, I want to emphasize that once we have been given two two distributions, and we are asked to find
conditional/transition distribution between them. Important thing is to know that choice of conditional/transition
distribution between two fixed distributions is not unique at all and there are so many ways we can find
conditional/transition distributions between two densities to achieve perfectly the same structure of both given fixed
distributions.

So if probability density of first random variable X is given as$P_X(X)$ and probability density of another dependent
correlated variable Y is given as$P_Y(Y)$ then P(Y|X) is given as so that

$$P_Y(Y)\,=\, \int \, P(Y|X) \, P_X(X) \, dX$$   Eq(1)

Now this choice of$P(Y|X) $ is not unique at all and there are so many possible forms of$ P(Y|X)$ so that above
relationship between$P_Y(Y)$ and$P_X(X)$ is perfectly satisfied.

So we can have an independent variance in our conditional probability distribution of  P_1(Y|X) and we could also have
another conditional probability distribution P_2(Y|X)  where we have specified a functional dependence of conditional
variance of Y on X and both conditional distributions P_1(Y|X) and P_2(Y|X) would perfectly satisfy the relationship in
Eq(1) because of non-uniqueness of conditional probability density of Y given X once both distributions of Y and X have
been specified.

So important thing to know is that information relevant to problem at hand has to be embedded while calculating
transition distributions/conditional distributions since it is equally possible to construct condtional distributions
that are very ill suited for the problem at hand but they perfectly satisfy the conditional/transition distribution
relationship given in Equation(1) between both the specified distributions.

---

### #2419 — Amin (Topic Author)
*August 2, 2024, 9:41 PM*

\subsection{Calculating Parameters of an SDE that Define the true transition Probability distribution When starting
distribution and end distribution of the SDE across a time interval are exogenously specified }

\label{sec4.4}

Since an SDE is driven by a Gaussian noise in volatility term and distribution of this Gaussian noise is already fixed,
so all the burden of calibration to both starting and ending distribution across an interval falls on parameters of the
SDE. In this subsection, we discuss numerical algorithm that has to be followed to calibrate parameters of an SDE so
that its transition probability when applied to starting distribution, the distribution at the end of the interval is
perfectly retrieved.

In order to make the exposition more clear, we first define the equation for an SDE whose parameters have to be
determined from start and end distributions across an interval. We define the SDE as

$
$dX(t)\,=\,\left( \, \mu_1\, {X(t)}^{\beta_1} \,+\, \mu_2\, {X(t)}^{\beta_2} \, \right) \,dt\,+\, \sigma_0 \, {X(t)}^{\gamma} \, dZ(t) \, $
$

We define

$$\mu(X(t))\,=\,\, \mu_1\, {X(t)}^{\beta_1} \,+\, \mu_2\, {X(t)}^{\beta_2} $$

and

$$\sigma(X(t))\,=\, \sigma_0 \,{X(t)}^{\gamma} $$

so

$$X(t_2)\,=\,X(t_1)\,+  \mu(X_t)\,dt \,+\, \sigma(X(t)) \, dZ(t) \, $$

When distribution of$X(t_2)$ and$X(t_1)$ have been exogeneously specified, only free parameters that can calibrate the
transition disribution$P(X(t_2)|X(t_1))$ are parameters of the SDE given by
$\mu_1, \, \mu_2, \, \beta_1, \, \beta_2, \sigma_0, \,$ and$\gamma $

We also want to emphasize since distribution of $X(t_1)$ is known, we can easily find its Z-series representation.

$$X(t_1)\,=\,  \sum\limits_{n=0}^{N} c_n \, {Z_1}^n$$

We can also calculate Z-series of$\mu(X(t))\,$ and$\sigma(X(t))\,$ through Taylor series since their functional form is
already known. We represent these Z-series as

$$\mu(X(t))\,=\,\,\mu(Z_1,\Theta) $$

and

$$\sigma(X(t))\,=\,\,\sigma(Z_1,\Theta) $$

where$\Theta$ signifies the dependence of drift and volatility functions on parameters of the SDE given as
$\mu_1, \, \mu_2, \, \beta_1, \, \beta_2, \sigma_0, \,$ and$\gamma $

Now we discretize the SDE () to second order as

\begin{multline*}

 \, X(t_2) \, - \, X(t_1) \, = \, \mu(X(t_1) \Delta t \, + \, \sigma(X(t_1)) Z \sqrt{\Delta t} \\ + \, \frac{\partial
\mu(X(t_1))}{\partial X} \, \mu(X(t_1)) \, \frac{{\Delta t}^2}{2} \, + \, \frac{\partial \mu(X(t_1))}{\partial X} \,
\sigma(X(t_1)) \, \left(1 \, - \, \frac{1}{\sqrt{3}} \right) \, Z \, {\Delta t}^{1.5} \\ +\, .5  \, \frac{\partial^2
\mu(X(t_1))}{\partial X^2} \, {\sigma(X(t_1))}^2 \, \frac{{\Delta t}^2}{2} \,  + \, \frac{\partial
\sigma(X(t_1))}{\partial X} \, \mu(X(t_1)) \,  \left(\frac{1}{\sqrt{3}} \right) \, Z \, {\Delta t}^{1.5} \, \\+ \,
\frac{\partial \mu(X(t_1))}{\partial X} \, \sigma(X(t_1)) \, (Z^2\, - \, 1) \, \frac{\Delta t}{2}  +\, .5  \,
\frac{\partial^2 \sigma(X(t_1))}{\partial X^2} \, {\sigma(X(t_1))}^2 \, \,  \left(\frac{1}{\sqrt{3}} \right) \, Z \,
{\Delta t}^{1.5} \,

 \end{multline*}

We rearrange the above equation as

$$\, X(t_2) \, - X_(t_1) \, = h_0(Z_1,\Theta) \, + \,h_1(Z_1,\Theta) \,Z \,+ \,h_2(Z_1,\Theta) \,(\,Z^2\,-\,1\,) \, $$

Please note that $Z_1$ and $Z$ in above equation are both independent of each other.

where$ h_0(Z_1,\Theta) $ is Z-series representation of terms without any Z or$(\,Z^2\,-\,1\, )$ in them and is found
from application of Taylor series on Z-series of X(t)

\begin{multline*}

 \, h_0(Z_1,\Theta) \, = \, \, \mu(X(t_1) \Delta t \,+ \, \frac{\partial \mu(X(t_1))}{\partial X} \, \mu(X(t_1)) \,
\frac{{\Delta t}^2}{2} \,+\, .5  \, \frac{\partial^2 \mu(X(t_1))}{\partial X^2} \, {\sigma(X(t_1))}^2 \, \frac{{\Delta
t}^2}{2} \,

 \end{multline*}

 and   $h_1(Z_1,\Theta)$ is Z-series representation of terms multiplying Z.

 \begin{multline*}

 h_1(Z_1,\Theta) \,=\, \sigma(X(t_1)) \sqrt{\Delta t} + \, \frac{\partial \mu(X(t_1))}{\partial X} \, \sigma(X(t_1)) \,
\left( 1 \, - \, \frac{1}{\sqrt{3}} \right) \, {\Delta t}^{1.5}+ \, \frac{\partial \sigma(X(t_1))}{\partial X} \,
\mu(X(t_1)) \,  \left(\frac{1}{\sqrt{3}} \right) \, {\Delta t}^{1.5} \, \\+\, .5  \, \frac{\partial^2
\sigma(X(t_1))}{\partial X^2} \, {\sigma(X(t_1))}^2 \, \,  \left(\frac{1}{\sqrt{3}} \right) \, {\Delta t}^{1.5} \,

 \end{multline*}

$$h_2(Z_1,\Theta) \,=\, \, \frac{\partial \mu(X(t_1))}{\partial X} \, \sigma(X(t_1)) \, \frac{\Delta t}{2} $$

For joint calibration of SDE transition probabilities to distribution of$X(t_1)$ and$X(t_2)$ , we could alter the
parameters of the SDE given as$\mu_1, \, \mu_2, \, \beta_1, \, \beta_2, \sigma_0, \,$ and$\gamma $

so that in equation

$$\, X(t_2) \,- \, X(t_1)\, = h_0(Z_1,\Theta) \, + \,h_1(Z_1,\Theta) \,Z \,+ \,h_2(Z_1,\Theta) \,(\,Z^2\,-\,1\,) \, $$

moments of LHS$E \left[ { \left( \, X(t_2) \,-\, X(t_1) \right)}^n \right] $ in above equation perfectly match the
moments of RHS calculated as

$
$ \, E \left[ \left( \, h_0(Z_1,\Theta) \, + \,h_1(Z_1,\Theta) \,Z \,+ \,h_2(Z_1,\Theta) \,(\,Z^2\,-\,1\,) \, \right)^n \right]$
$

This can either be done by iterative optimization over parameters of$\Theta$ for each iteration which we slowly alter
the coefficients$\mu_1, \, \mu_2, \, \beta_1, \, \beta_2, \sigma_0, \,$ and$\gamma $ and recalculate
$ h_0(Z_1,\Theta) \,, \,h_1(Z_1,\Theta) \,Z \, $ and$ \,h_2(Z_1,\Theta) \,(\,Z^2\,-\,1\,) $ and then find moments
associated with RHS of Eq() and then check how well moments of RHS match with moments of terminal distribution of$X_2$
while perturbing the SDE parametrs slowly in the direction of better fit and improving objective function.

 When close enough, we can also use multi-dimensional Newton method to find the parameters of the SDE.

---

### #2420 — Amin (Topic Author)
*August 3, 2024, 3:16 PM*

Friends, I re-wrote one of the sections on conditional expectation. Once we have found conditional
expectation/transition density of$Y|X$ , we can use to to find the conditional density$X|Y_0$ when a value of$Y_0$
becomes available as observation. We can do very similar analytics it for SDEs and other sections as well. Here is the
new version of the section.

\subsection{Calculating the true distribution structure in Uni-variate Conditional Expectation of a Correlated Random
variable when its variance is dependent on Explanatory Variable }

\label{sec4.4}

While calculating conditional expectation in previous post, we have assumed that variance of Y is independent of X which
is most likely not the case. For example consider an SDE-like dependence equation of a random variable

$$ \,Y \,= \, \mu(X) \, + \, \sigma(X) \, W $$

where W would usually be a non-Gaussian random variable which is assumed to be independent of$\sigma(X) \,$ and
$ \mu(X) $ and$ \sigma(X) $ are some functions of a random variable X. The first term$\, \mu(X) \,$ should be perfectly
captured by correlations in our conditional expectation equation but we see that variance term$\,\,\sigma(X) \, W\,\, $
, in equation that describes Y, even though orthogonal to X is not independent of X. So different realizations of X over
its density should also affect and alter the distribution of variance of Y and we would have to do more analytics to
calculate the effect of X on variance of Y for a right and proper calculation of conditional distribution of Y.

In order to find the true distribution associated with univariate conditional expectation of a random variable, we again
perform the de-correlation operation discussed in previous subsection on jointly observed values of data sample of X and
Y, we can find that$\tilde{\tilde{Y}}$ represents the true residual part of Y that has not been explained by the
variable X.

This de-correlated value can be written as an equation as

$$ \tilde{\tilde{Y}} \,=\, Y\, -\, E\left[Y|X \right] \, $$

From section (), we already know that we can find a Z-series of$\sigma(X(Z))$ through Taylor Series on Z-series of X as
given in subsection()

$$\sigma(X(Z_X))=\sum\limits_{n=0}^{N}\, d_n\, H_n(Z_X)$$

if $\mu_{\sigma(X),n}\,$ represents nth moment of $\sigma(X)$, We can find moments of $ \sigma(X)$ as

$$\mu_{\sigma(X),n}\, =\, E\left[\sum\limits_{n=0}^{N}\, d_n\, H_n(Z_X) \right]^n $$

Now we see that Z-series structure of $ \tilde{\tilde{Y}} $ with dependency structure included in equation is given as

$
$ \tilde{\tilde{Y}} \,=\, \, \sigma(X) \,\,W\,=\, \, \sigma(X) \,\, \sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y) \ \, $
$

The random variable$\,W\,$ with Hermite Series representation given as
$\, \sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y) \ \,$ with as yet undetermined coefficients is supposed to
capture the distribution structure of non-Gaussian noise in the variance equation. And if$\mu_{\tilde{\tilde{Y}},n}\,$
represents nth moment of$\tilde{\tilde{Y}}\,$ , this nth moment can be written because of independence between
$\,\mu_{\sigma(X),n}\,$ and$\, W \,$ as

$$\mu_{\tilde{\tilde{Y}},n}\, =\,\mu_{\sigma(X),n}\, \,\mu_{W,n}\, \, $$

Since$\mu_{\tilde{\tilde{Y}},n}\,$ can be easily calculated from data of de-correlated values$\tilde{\tilde{Y}} $ , and
we can also easily calculate the moments$\mu_{\sigma(X),n}\,$ as earlier describe, we get the equation for moments of
non-Gaussian noise W as

$$ \, \mu_{W,n} \, \,= \, \frac{\mu_{\tilde{\tilde{Y}},n}\,}{\,\mu_{\sigma(X),n}}\,$$

Once we have found the moments of non-Gaussian noise given as$\, \mu_{W,n} \, $ , we can use these moments with
multidimensional Newton root search method to estimate coefficients$\tilde{\tilde{c}}_m\,$ as described earlier in
section (3.) using the equations

$$ E \, \left[\sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y)\right]^n \,=\,\, \mu_{W,n} $$

Then conditional distribution of Y would be given as

$$ Y\, | \, X=\, E \left[ Y|X \right] + \, \tilde{\tilde{Y}}(Z_Y)\,$$

$
$ Y\, | \, X=\mu_Y+\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,b_n \, H_n(Z_X)+\,\, \left[ \sum\limits_{n=0}^{N}\, d_n \, H_n(Z_X) \right] \, \left[\sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y)\right] $
$

$
$ Y\, | \, X=\mu_Y+\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \, c_n \, H_n(Z_X)+\,\, \left[ \sum\limits_{n=0}^{N}\, d_n \, H_n(Z_X) \right] \, \left[\sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y)\right] $
$

Again  once coefficients in above equation have been calculated from data, we can use it for conditional distribution of
random variable Y as single (or more) values of X become available just as easily as we did for correlation based
conditional distribution.

After calculation of$Y\, | \, X$ , we describe how to find the probability distribution
$p \left(X\, | \, Y\,=\,Y_0 \right) $ of X given an observation of$Y=Y_0$ . For calculation of
$p \left( X\, | \, Y\,=\,Y_0 \right) $ , we will use Bayes formula but First we define$Z_{Y_0}\,|\, Z_{X_0} $ as the
particular value of$Z_Y$ that solves for$Y=Y_0$ given$X=X_0$ in Eq () above.$Z_{Y_0}\,|\, Z_{X_0} $ is the particular
value of$Z_Y$ that equates the LHS of Eq() to$Y_0$ given$X=X_0$ and has to be backed out from the equation below as

$
$ Y_0\, | \, X_0 =\mu_Y+\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \, c_n \, H_n(Z_{X_0})+\,\, \left[ \sum\limits_{n=0}^{N}\, d_n \, H_n(Z_{X_0}) \right] \, \left[\sum\limits_{m=1}^{M}\, \tilde{\tilde{c}}_m\, H_m(Z_Y)\right] $
$

We invert above equation for$Z_{Y}$ to find the value of$Z_{Y_0}\,|\, Z_{X_0} $ since this is the particular value of
$Z_{Y}$ that relates the observation of$X=X_0$ with observation of$Y=Y_0$ through conditional expectation formula.

Below we calculate the probability of starting from a point$Z_{X_0}$ associated with an arbitrary point$X_0$ on density
of X and going to point$Y=Y_0$ on the density of second random variable.

$$p( \left(Y=Y_0 \right)\, \cap \, Z_{X_0} ) \, =\, p(Z_{Y_0}|Z_{X_0}) \, p(Z_{X_0}) $$

$$=\, \phi(Z_{Y_0}|Z_X) \, \phi(Z_{X_0}) $$

where $\phi(X)\,=\, \frac{\exp \left(-.5\, X^2 \right)}{\sqrt{2\, \pi}} $ is symbol for normal density value at X.

 We drop the subscript zero on $Z_{X_0}$ and simply write it as $Z_{X}$ for the sake of integration

$$p(Y=Y_0)\,\, \, =\,\int\limits_{Z_X=-\infty}^{\infty} \phi(Z_{Y_0}|Z_{X}) \, \phi(Z_X) dZ_X \, $$

We know from Bayes formula

$$p(Z_X\,|\, Y=Y_0)\,=\,\frac{p(\left(Y=Y_0 \right)\, \cap \, Z_{X} )}{p(Y=Y_0)}$$

so

$
$p(Z_X\,|\, Y=Y_0)\,=\,\frac{\, \phi(Z_{Y_0}|Z_X) \, \phi(Z_{X}) }{\,\int\limits_{Z_X=-\infty}^{\infty} \phi(Z_{Y_0}|Z_{X}) \, \phi(Z_X) dZ_X }$
$

further  since the probability densities of $Z_x$ and $X$ are related as

$$p_X(X) \,=\, p_Z(Z_X) \, \frac{d Z_X}{dX} $$ we can find the desired conditional probability density of X as

$
$p(X\,|\, Y=Y_0)\,=\,\frac{\, \phi(Z_{Y_0}|Z_X) \, \phi(Z_{X}) \, \frac{d Z_X}{dX}}{\,\int\limits_{Z_X=-\infty}^{\infty} \phi(Z_{Y_0}|Z_{X}) \, \phi(Z_X) dZ_X }$
$

Equation(AA)

where

$$ \frac{d X}{dZ_X}\,=\, \sum\limits_{n=0}^{N-1}\,(n+1)\, b_{n+1}\, {Z_X}^n $$

The above equation (AA) gives probability density of$X|\, Y=Y_0 $ on an arbitrary value of random variable X (arbitrary
point on density of X). In order to numerically construct a complete density, we would have to make a grid of points
$X_m$ on density of X and find the probability density on all grid points through the Equation(AA) above. Integration in
denominator of Eq(AA) would have to be done on the grid of points$Z_{X_m}$ associated with grid of$X_m$ on density of X.
Also not including$ \frac{d Z_X}{dX}$ in the denominator is not an error since integration in variable X or variable Z_x
would give the same result since$\int \, p(Z_X) \, dZ_X\,=\,\int \, p(X) \, dX\, $

If needed, we can represent the above equation of conditional probability$p(X\,|\, Y=Y_0)\, $ as a Z-series by one of
the methods discussed in section 3.

---

### #2421 — Amin (Topic Author)
*August 4, 2024, 7:51 PM*

Friends, I am writing this post to describe the new persecution that has dramatically increased in past two or three
days. First of all mind control agents and pak army have completely gone nuts and have become completely rabid and are
drugging the targeted food very thoroughly in the areas that lie on my path. I try to eat healthy food and avoid a large
number of things I used to eat earlier but that gives them even more clarity what to drug comprehensively. Especially
when I went out to get food on my motorcycle during this morning and later on my car in the afternoon, I noticed that
they had drugged the targeted food in all the close neighborhoods. I, for example, survived by eating quite a bit of ice
cream but such tricks would not work for long. There has been huge drugging activity of targeted food today and
yesterday.

Another problem is that bread manufactured by most of the bread making companies and most of the bakeries in the city
has again turned bad and mind control chemicals are being added at the manufacturing source to most of the bread sold in
the city. Bran bread and multi-grain bread is especially targeted but plain wheat bread is also comprehensively drugged.

Another thing that I also mentioned previously that I had been working in Air-conditioned room till a few days ago.
Earlier there used to be small amount of gas that would sometimes put me to sleep but that was mostly tolerable but the
gas increased dramatically about four days ago and it is virtually impossible to work in that room with AC on.

But when I went out to get food and water this morning, they fitted gas devices in ceiling fans of all rooms where I
work and also in a pedestal fan (that stands on the floor) and it became very difficult to sit in the air of these fans
but I have no choice but to use one of these fans.

It had been raining for past few days so temperature has decreased even though there is very high humidity and therefore
I was able to survive today but it would become very difficult when temperature rises a little bit again.

Even though aggressive drugging of food in special areas of the city is a very big problem for me, I am extremely
concerned about use of gases in AC and in the fans in my house and it has made it difficult for me to survive.  I was
able to work somewhat at night since I worked in the open garage and there was quite some fresh air there but it is not
possible to work there during the day when it is hot and later when temperatures rise a little again after a few day.

---

### #2422 — Amin (Topic Author)
*August 5, 2024, 4:47 PM*

Friends, I have sort of filled in the material for first few important sections and prepared a basic understandable
manuscript. It is still very rough, basic and totally preliminary. I hope that I would be able to prepare a similar very
preliminary version for all of the paper by end of this week. I have also given links to some matlab programs in
appropriate sections. There are some sections where I wanted to give links but I noticed that some nomenclature of the
programs was too confusing and derived from SDEs and difficult to understand for people not oriented with the background
so I decided to improve the names of a few variables and re-post the programs on Wilmott forum. Those changes will
appear in next version.

Here are first few  sections of the very preliminary paper..

.

.

[![Image](../images/i.postimg.cc/mgK8ZGtn/PaperI01.png)](https://postimg.cc/75MgXd11)

[![Image](../images/i.postimg.cc/26tprtN8/PaperI02.png)](https://postimg.cc/1nD7KJzL)

[![Image](../images/i.postimg.cc/qRqVfTY5/PaperI03.png)](https://postimg.cc/f3GgX6Mc)

[![Image](../images/i.postimg.cc/Hn8qxtT0/PaperI04.png)](https://postimg.cc/ctZ9kwg6)

[![Image](../images/i.postimg.cc/1RgXwhtB/PaperI05.png)](https://postimg.cc/XXbn6P9B)

[![Image](../images/i.postimg.cc/nV6z1R9J/PaperI06.png)](https://postimg.cc/4nQsf11L)

[![Image](../images/i.postimg.cc/c4wJkRf8/PaperI07.png)](https://postimg.cc/N5GY5rJg)

[![Image](../images/i.postimg.cc/QdDd2FqY/PaperI08.png)](https://postimg.cc/tYrbPCwF)

[![Image](../images/i.postimg.cc/g2K2mGSz/PaperI09.png)](https://postimg.cc/dhLY9ccp)

[![Image](../images/i.postimg.cc/zfXXf46n/PaperI10.png)](https://postimg.cc/hX6qyZSj)

[![Image](../images/i.postimg.cc/261kQhzy/PaperI11.png)](https://postimg.cc/S2pbqXYb)

[![Image](../images/i.postimg.cc/jjgqnZYB/PaperI12.png)](https://postimg.cc/CZ8pWC14)

[![Image](../images/i.postimg.cc/W3x2Xz3n/PaperI13.png)](https://postimg.cc/KkrSYZtk)

[![Image](../images/i.postimg.cc/BbDJy3PG/PaperI14.png)](https://postimg.cc/QK8L9Rq6)

[![Image](../images/i.postimg.cc/QNWNVQ4n/PaperI15.png)](https://postimg.cc/3WYQcvHg)

[![Image](../images/i.postimg.cc/bNcynZ4Y/PaperI16.png)](https://postimg.cc/9zbH5QWs)

[![Image](../images/i.postimg.cc/bNxz9zjx/PaperI17.png)](https://postimg.cc/LnsKHF55)

[![Image](../images/i.postimg.cc/K8mm9dZd/PaperI18.png)](https://postimg.cc/hf3FvZQr)

---

### #2423 — Amin (Topic Author)
*August 6, 2024, 7:47 AM*

Friends, I tried to explain the section on addition of correlated random variables. Question is if zero correlation
between$Z_X$ and$\tilde{Z}_Y$ in eq(30) and eq(31) imply independence. We have removed any correlations between (let us
say) first seven hermite polynomials through our conditional expectation solution algorithm so I suppose first eight
moments of$Z_X$ and$\tilde{Z}_Y$ would have no correlations but some correlations might possibly exist between higher
moments of$Z_X$ and$\tilde{Z}_Y$ . If all moments of$Z_X$ and$\tilde{Z}_Y$ would be perfectly retrieved without
correlation, I would certainly want to say that they are independent, So the method might be slightly approximate due to
possibility of some correlations between higher moments of$Z_X$ and$\tilde{Z}_Y$ . I am sure the algorithm can possibly
be improved but I would try to come back to it after completing the paper.

.

.

.

[![Image](../images/i.postimg.cc/Px1B7jdY/PaperI07.png)](https://postimg.cc/8JPKFxJz)

[![Image](../images/i.postimg.cc/SKBBVsbm/PaperI08.png)](https://postimg.cc/KK5p8mYW)

---

### #2424 — Amin (Topic Author)
*August 7, 2024, 2:31 PM*

Friends, I am re-doing many parts of the paper and trying to explain things better. Especially the section about using
discrete normal density to find hermite polynomial representation of data was very poorly explained and I have worked on
it again and tried to explain everything well. Also, I am making further changes to addition of correlated non-Gaussian
random variables (two pages posted in previous post have gone many through more changes) and requiring that additional
information has to be provided about dependence structure of variance.  After converting one variable into a correlated
part and orthogonal part, we have to further know if orthogonal variance part is independent  or has a dependency
structure and we would be able to add both types of correlated random variables (independent variance type and dependent
variance type with dependency structure given) with different formulas for adding them. I have also tried to define in
the very start (in the definition of Z-series) that mapping of non-Gaussian random variable on standard Gaussian to
calculate the Taylor series derivatives is through common CDF points of both random variables. I am also making a lot of
other changes and hope that first preliminary version of the paper would be ready by the end of weekend. And I really
hope that I would be able to mail it to Paul for sort of initial assessment on Monday.

---

### #2425 — Amin (Topic Author)
*August 8, 2024, 7:39 PM*

Friends, mind control agents are desperately trying their best to thwart my work. I had complained about gas in the AC
of room where I used to work for past few weeks and the gas in that room never decreased. I could work for another day
using the AC in the lounge which was not turned on by anybody in the house for weeks. However, very next day they filled
the AC in the lounge with gas as well and I could not use it any more. Temperature had been better yesterday so I could
work without any AC and could make progress but the temperature is increasing again.

They also have gas in the rooms and fans that they liberally release something they had pretty much stopped doing
earlier. Especially they release some heavy gas that highly charges the cotton trousers. Even though clothes would be
fully dry, it would seem like they are slightly moist and they seem to stick to the body and it is a very difficult
feeling and the whole of the lower body feels extremely uncomfortable. They release this gas from time to time usually
after an hour or two and sometimes more frequently while the fans would work fine during the period in between episodes
of heavy gas.

They used to release this heavy gas in special areas of the house earlier but had not ben using it for past few months.
However in past 4-5 days they have used it extremely frequently and they had never used it so frequently ever before in
past few years as I could recall.

---

### #2426 — Amin (Topic Author)
*August 11, 2024, 10:32 PM*

Friends, I continued to work at refining the paper and I cannot believe every time I revise it, I find some new errors.
And I still have to work on final two sections, add references and abstract and also give links to old and some newly
altered matlab programs. So I still suspect that it can take at least one more week to work on it and make it better.
But some sections are about final and may undergo only minor changes and I am posting them here for review of friends.
Posting a complete paper can still take one more week.

.

.

.

[![Image](../images/i.postimg.cc/V6cff3wF/Paper001.png)](https://postimg.cc/06cRZXb6)

[![Image](../images/i.postimg.cc/1Xmy6wfn/Paper002.png)](https://postimg.cc/DJNV3WQn)

[![Image](../images/i.postimg.cc/76MxfmYr/Paper003.png)](https://postimg.cc/Q9CLzgTf)

[![Image](../images/i.postimg.cc/d0CQKJb1/Paper004.png)](https://postimg.cc/Z9Tz8zKt)

[![Image](../images/i.postimg.cc/d35w93yW/Paper005.png)](https://postimg.cc/q66PJkQn)

[![Image](../images/i.postimg.cc/xj5fQx4K/Paper006.png)](https://postimg.cc/PNLsz4hx)

[![Image](../images/i.postimg.cc/02N8yYTh/Paper007.png)](https://postimg.cc/14LxWq5K)

[![Image](../images/i.postimg.cc/MKrzMcxH/Paper008.png)](https://postimg.cc/tYPK84sG)

[![Image](../images/i.postimg.cc/dVkw8qtB/Paper009.png)](https://postimg.cc/rDkBT240)

[![Image](../images/i.postimg.cc/13kPBL8Z/Paper010.png)](https://postimg.cc/qNx9MDcm)

[![Image](../images/i.postimg.cc/zfTNc0hH/Paper011.png)](https://postimg.cc/d7Qg7R4J)

[![Image](../images/i.postimg.cc/1tPShw0C/Paper012.png)](https://postimg.cc/SXZ3cXvC)

[![Image](../images/i.postimg.cc/SsrhyRDy/Paper013.png)](https://postimg.cc/YGhVRp5V)

[![Image](../images/i.postimg.cc/cCLN6Wbf/Paper014.png)](https://postimg.cc/7GdRQFDL)

[![Image](../images/i.postimg.cc/90gH7k6K/Paper015.png)](https://postimg.cc/N2Xnhdfk)

[![Image](../images/i.postimg.cc/fW8Np3VC/Paper016.png)](https://postimg.cc/SjY3zx7Y)

[![Image](../images/i.postimg.cc/CLdggFDg/Paper017.png)](https://postimg.cc/vcRj7w3q)

[![Image](../images/i.postimg.cc/SN5pQw7z/Paper018.png)](https://postimg.cc/7fgRmtRx)

[![Image](../images/i.postimg.cc/7Z2r5mmt/Paper019.png)](https://postimg.cc/QFhyPkLc)

[![Image](../images/i.postimg.cc/yNC4ccG1/Paper020.png)](https://postimg.cc/PCyRkph9)

[![Image](../images/i.postimg.cc/0NGgfrgp/Paper021.png)](https://postimg.cc/Ny0PGsjM)

[![Image](../images/i.postimg.cc/4dXDFZZj/Paper022.png)](https://postimg.cc/QBnYH2Fq)

[![Image](../images/i.postimg.cc/cHTVpjLC/Paper023.png)](https://postimg.cc/xJJxH6HV)

[![Image](../images/i.postimg.cc/gjJfmDxD/Paper024.png)](https://postimg.cc/Vrx7FXBr)

[![Image](../images/i.postimg.cc/MHFgTQR8/Paper025.png)](https://postimg.cc/QKcfYV06)

[![Image](../images/i.postimg.cc/7PsFXpRQ/Paper026.png)](https://postimg.cc/MXB3prqy)

[![Image](../images/i.postimg.cc/J4s9FpV7/Paper027.png)](https://postimg.cc/D8KjJdwR)

[![Image](../images/i.postimg.cc/RV2jxw47/Paper028.png)](https://postimg.cc/KRr9nkKj)

[![Image](../images/i.postimg.cc/GmY6L9mZ/Paper029.png)](https://postimg.cc/68WMzWR0)

[![Image](../images/i.postimg.cc/R0ByN93q/Paper030.png)](https://postimg.cc/JspP2f5W)

[![Image](../images/i.postimg.cc/0N03S3mn/Paper031.png)](https://postimg.cc/67TYJMM4)

[![Image](../images/i.postimg.cc/fLWPfKfN/Paper032.png)](https://postimg.cc/HJK3pbNZ)

[![Image](../images/i.postimg.cc/mrxxGCNx/Paper033.png)](https://postimg.cc/DScprWM5)

[![Image](../images/i.postimg.cc/MHvrhpL3/Paper034.png)](https://postimg.cc/CnpN8SSb)

[![Image](../images/i.postimg.cc/ydfbQZLS/Paper035.png)](https://postimg.cc/HcyzjVDp)

[![Image](../images/i.postimg.cc/kMpHWWV0/Paper036.png)](https://postimg.cc/MX1tSMm5)

[![Image](../images/i.postimg.cc/mkJ6RGfL/Paper037.png)](https://postimg.cc/30jZCVxV)

[![Image](../images/i.postimg.cc/wTRG23L7/Paper038.png)](https://postimg.cc/rKcjFVhk)

---

### #2427 — Amin (Topic Author)
*August 12, 2024, 6:06 AM*

Friends, I looked at the paper again this morning and I realize that section 4 has to be really re-worked. I am further
going to change its structure and alter the description and wording of various things at many places though I think most
equations might still be fine. I was going to delete the paper image attached in last post thinking I will upload it
again after a day or tow but I decided to not worry too much about uploaded paper. But this is still a very preliminary
version and a final version could be ready only at the end of this week or at the weekend.

---

### #2428 — Amin (Topic Author)
*August 13, 2024, 7:06 PM*

Friends, I have re-worked the section on conditional expectations. I added a small section about how to estimate
coefficients of conditional distribution Y|X when part of Y orthogonal to X is dependent on X by regressing our data on
hermite polynomials of our discrete normal density grid. I thought this method description would be very helpful. I made
several other smaller changes.

I have removed the last part about calculations of parameters of SDE and have transferred that to applications of
Z-series/Hermite Series.

Here are the new reworked sections

.

.

...

[![Image](../images/i.postimg.cc/5tMWwRrs/PaperB01.png)](https://postimg.cc/SnVP4Dk9)

[![Image](../images/i.postimg.cc/Qd7rK3fB/PaperB02.png)](https://postimg.cc/QFjzvRGs)

[![Image](../images/i.postimg.cc/m2JsrDyf/PaperB03.png)](https://postimg.cc/9rdS8ckJ)

[![Image](../images/i.postimg.cc/SNJ4q88f/PaperB04.png)](https://postimg.cc/JGVv5sps)

[![Image](../images/i.postimg.cc/vBYRK6b9/PaperB05.png)](https://postimg.cc/QByn9CBx)

[![Image](../images/i.postimg.cc/cJMyTcy0/PaperB06.png)](https://postimg.cc/4KdSxVxS)

[![Image](../images/i.postimg.cc/gJg9bk27/PaperB07.png)](https://postimg.cc/DJ4pqhsQ)

[![Image](../images/i.postimg.cc/8cc2pQFz/PaperB08.png)](https://postimg.cc/CnyP72H3)

[![Image](../images/i.postimg.cc/kGHkD18F/PaperB09.png)](https://postimg.cc/xNKs4P6c)

[![Image](../images/i.postimg.cc/G3S0M2N8/PaperB10.png)](https://postimg.cc/Yjgy0ptM)

[![Image](../images/i.postimg.cc/8PF2xGQy/PaperB11.png)](https://postimg.cc/qzTDC97n)

[![Image](../images/i.postimg.cc/pLzgXBdz/PaperB12.png)](https://postimg.cc/NKGNdmmj)

[![Image](../images/i.postimg.cc/GhZWCfbb/PaperB13.png)](https://postimg.cc/YhznNb4P)

---

### #2429 — Amin (Topic Author)
*August 17, 2024, 4:55 PM*

Friends, I have completed work on the main sections of my paper. I have decided to not include the section on
multidimensional conditional distributions related to the work we did last winters. I realized that it needed more work
and anything I would add would be only incomplete. Right after completing work on my paper and submitting it, I want to
do work with multidimensional conditional distributions on the lines of univariate conditional distributions where
orthogonal part to other variables is independent or dependent on them. I have more clarity and better ideas so I hope
that we would be easily able to complete this work soon as I intend to start working on it after completing my paper.

I still have to work with abstract, introduction, conclusion and references. I have given references to other equations
and sections all over the paper and I need to double check them again. And as I had said earlier that I want to give
links to Wilmott forum posts where programs related to various sections are posted and also modify some of the matlab
programs and repost them on forum and give links to them. So all of this still needs at least three days to complete. So
it would be Tuesday or Wednesday when first official version of the paper would be ready.

Meanwhile I really want to complain about ever increasing persecution  at hands of mind control agents. My father is
visiting us at our home in Lahore and I took his car to a closeby neighborhood and bought a red bull to drink as I was
feeling very down. Even though the shop had glass walls and I could see outside, it started raining and mind control
agents who were behind me took advantage of some small window of opportunity when I was paying bill at the counter to
quickly opened the trunk and added mind control drugs to water I had placed in the trunk of my car.

Later when I reached home and sat on the plastic chair to work, they had put some invisible "clothes charging chemical"
on the plastic chair and I could feel huge charges going into my cotton pants from behind (where I was sitting on the
chair) and also feeling extreme uneasiness as charges continued to get into cotton vest beneath my shirt. I had changed
my clothes and had worn new washed clothes just this morning today.

I really have not been able to work very well for past few days since I was given an antipsychotic injection this
Saturday that passed a week ago.

When the injection is given, I have to take one of the medicines (same salt)  Kemadrin, kempro or procye to avoid
negative effect of injections on other parts of the body. Doctors prescribe one of these medicine when they prescribe
Fluanxol injections. Now shit-pieces of Pak army have completely drugged all of these drugs by approaching their
manufacturers. I took kempro day before yesterday and after taking the drug, I could not work properly for next two days
since mind control agents continued to remove all good neurotransmitters from my brain after I took kempro tablets.

Getting good water is becoming very difficult since they continue to drug underground water at places around the city
that have possibly good water.

---

### #2430 — Amin (Topic Author)
*August 19, 2024, 4:27 PM*

I am giving references to matlab programs on this thread that I have posted over the years. I am changing two functions
since they are crucial and their nomenclature was poor.

This function is named:

function [b0,b] = CalculateTaylorCoeffsOfFunctionZSeries(fX,dnfXdXn,a,SeriesOrder)

It was earlier named

function [b0,b] = CalculateDriftbCoeffs08(wMu0dt,dwMu0dtdw,a,SeriesOrder)

.

.

.

```
function [b0,b] = CalculateTaylorCoeffsOfFunctionZSeries(fX,dnfXdXn,a,SeriesOrder)

%The following function expands the Taylor Series of f(X(Z)) around Z=Z_0=0
%and finds coeffs of Z-series of f(X(Z)). Where
% X(Z)=a0 + a(1) Z + a(2) Z^2 + ....+ a(SeriesOrder) Z^(SeriesOrder)
%while
%f(X(Z))= b0 + b(1) Z + b(2) Z^2 + ....+ b(SeriesOrder) Z^(SeriesOrder)

%dnfXdXn(m) means the mth derivative d^m(f(X(Z_0))_dX^m of f(X(Z)) with
%respect to X(Z) calculated at median Z=Z_0=0;
%fX represents the value f(X(Z_0)) calculated at median.
%a(1:SeriesOrder) are coefficients of Z^(1:SeriesOrder) as given in
%Z-series
%a0 is not needed in this calculation.
%SeriesOrder is the number of terms in Z-series not including a0
%This expansion is upto tenth order only.

b0=fX;

b(1)=a(1) *dnfXdXn(1);

b(2)=1/2*(2* a(2) *dnfXdXn(1)+a(1)^2 *dnfXdXn(2));

b(3)=1/6*(6 *a(3) *dnfXdXn(1)+6 *a(1)* a(2) *dnfXdXn(2)+a(1)^3 *dnfXdXn(3));

b(4)=1/24*(24* a(4) *dnfXdXn(1)+12* a(2)^2 *dnfXdXn(2)+24 *a(1)* a(3) *dnfXdXn(2)+ ...
    12* a(1)^2* a(2) *dnfXdXn(3)+a(1)^4 *dnfXdXn(4));

if(SeriesOrder>=5)
b(5)=1/120*(120* a(5) *dnfXdXn(1)+120* a(2) *a(3) *dnfXdXn(2)+120* a(1)* a(4) *dnfXdXn(2)+ ...
    60 *a(1)* a(2)^2 *dnfXdXn(3)+60* a(1)^2* a(3) *dnfXdXn(3)+ ...
    20 *a(1)^3* a(2) *dnfXdXn(4)+a(1)^5 *dnfXdXn(5));
end
if(SeriesOrder>=6)
b(6)=1/720*(720* a(6) *dnfXdXn(1)+360* a(3)^2 *dnfXdXn(2)+720* a(2)* a(4) *dnfXdXn(2)+720* a(1)* a(5) *dnfXdXn(2)+ ...
    120* a(2)^3 *dnfXdXn(3)+720* a(1)* a(2)* a(3) *dnfXdXn(3)+360* a(1)^2* a(4) *dnfXdXn(3)+ ...
    180* a(1)^2* a(2)^2 *dnfXdXn(4)+120* a(1)^3* a(3) *dnfXdXn(4)+ ...
    30* a(1)^4 *a(2) *dnfXdXn(5)+a(1)^6 *dnfXdXn(6));
end

if(SeriesOrder>=7)
  b(7)=1/(720*7)*(5040* a(7)*dnfXdXn(1)+5040* a(3)* a(4)*dnfXdXn(2)+5040* a(2)* a(5) *dnfXdXn(2)+5040 *a(1)* a(6)
*dnfXdXn(2)+ ...
      2520* a(2)^2* a(3) *dnfXdXn(3)+2520* a(1)* a(3)^2 *dnfXdXn(3)+5040 *a(1)* a(2)* a(4) *dnfXdXn(3)+2520* a(1)^2
*a(5) *dnfXdXn(3)+ ...
      840* a(1)* a(2)^3 *dnfXdXn(4)+2520* a(1)^2* a(2)* a(3) *dnfXdXn(4)+840* a(1)^3* a(4) *dnfXdXn(4)+ ...
      420* a(1)^3* a(2)^2 *dnfXdXn(5)+210* a(1)^4* a(3) *dnfXdXn(5)+ ...
      42* a(1)^5* a(2) *dnfXdXn(6)+a(1)^7 *dnfXdXn(7));

end

if(SeriesOrder>=8)
  b(8)=1/(720*7*8)*(40320* a(8) *dnfXdXn(1)+20160* a(4)^2 *dnfXdXn(2)+40320* a(3)* a(5) *dnfXdXn(2)+40320* a(2) *a(6)
*dnfXdXn(2)+ ...
      40320* a(1) *a(7) *dnfXdXn(2)+ ...
      20160* a(2)* a(3)^2 *dnfXdXn(3)+20160* a(2)^2* a(4) *dnfXdXn(3)+40320* a(1)* a(3)* a(4) *dnfXdXn(3)+40320* a(1)*
a(2)* a(5) *dnfXdXn(3)+ ...
      20160* a(1)^2* a(6) *dnfXdXn(3)+ ...
      1680* a(2)^4 *dnfXdXn(4)+20160* a(1)* a(2)^2* a(3) *dnfXdXn(4)+10080* a(1)^2* a(3)^2 *dnfXdXn(4)+20160* a(1)^2*
a(2) *a(4) *dnfXdXn(4)+ ...
      6720* a(1)^3* a(5) *dnfXdXn(4)+ ...
      3360* a(1)^2* a(2)^3 *dnfXdXn(5)+6720* a(1)^3 *a(2)* a(3) *dnfXdXn(5)+1680* a(1)^4* a(4) *dnfXdXn(5)+ ...
      840* a(1)^4* a(2)^2 *dnfXdXn(6)+336* a(1)^5* a(3) *dnfXdXn(6)+ ...
      56* a(1)^6* a(2) *dnfXdXn(7)+a(1)^8 *dnfXdXn(8));
end

if(SeriesOrder>=9)
b(9)=1/(720*7*8*9)*(362880* a(9) *dnfXdXn(1)+ ...
    362880* a(4)* a(5) *dnfXdXn(2)+ 362880* a(3)* a(6) *dnfXdXn(2) +362880* a(2)* a(7) *dnfXdXn(2) +362880* a(1) *a(8)
*dnfXdXn(2) + ...
    60480* a(3)^3 *dnfXdXn(3)+362880* a(2)* a(3)* a(4) *dnfXdXn(3)+181440* a(1)* a(4)^2 *dnfXdXn(3)+181440* a(2)^2* a(5)
*dnfXdXn(3) + ...
    362880* a(1)* a(3)* a(5) *dnfXdXn(3)+362880 *a(1)* a(2)* a(6) *dnfXdXn(3) +181440 *a(1)^2* a(7) *dnfXdXn(3)+ ...
    60480* a(2)^3* a(3) *dnfXdXn(4)+181440* a(1)* a(2)* a(3)^2 *dnfXdXn(4)+181440* a(1)* a(2)^2 *a(4) *dnfXdXn(4)+ ...
    181440* a(1)^2* a(3)* a(4) *dnfXdXn(4)+181440* a(1)^2* a(2)* a(5) *dnfXdXn(4)+60480* a(1)^3* a(6) *dnfXdXn(4)+ ...
    15120* a(1)* a(2)^4 *dnfXdXn(5)+90720* a(1)^2* a(2)^2* a(3) *dnfXdXn(5)+30240* a(1)^3* a(3)^2 *dnfXdXn(5)+ ...
    60480 *a(1)^3* a(2)* a(4) *dnfXdXn(5)+15120* a(1)^4* a(5) *dnfXdXn(5)+ ...
    10080* a(1)^3* a(2)^3 *dnfXdXn(6)+15120* a(1)^4 *a(2)* a(3) *dnfXdXn(6)+3024* a(1)^5* a(4) *dnfXdXn(6)+ ...
    1512* a(1)^5* a(2)^2 *dnfXdXn(7)+504* a(1)^6* a(3) *dnfXdXn(7)+ ...
    72* a(1)^7 *a(2) *dnfXdXn(8)+a(1)^9 *dnfXdXn(9));
end

if(SeriesOrder>=10)
b(10)=1/(720*7*8*9*10)*(3628800* a(10)* dnfXdXn(1)+ ...
    1814400 * a(5)^2 *dnfXdXn(2)+3628800 *a(4)* a(6)* dnfXdXn(2)+3628800* a(3)* a(7)* dnfXdXn(2)+3628800 *a(2)* a(8)*
dnfXdXn(2)+ ...
    3628800* a(1)* a(9)* dnfXdXn(2)+ ...
    1814400* a(3)^2* a(4)* dnfXdXn(3)+1814400* a(2)* a(4)^2* dnfXdXn(3)+3628800* a(2)* a(3)* a(5)* dnfXdXn(3)+3628800*
a(1)* a(4)* a(5) *dnfXdXn(3)+ ...
    1814400* a(2)^2* a(6)* dnfXdXn(3)+3628800* a(1)* a(3)* a(6)* dnfXdXn(3)+3628800 *a(1)* a(2)* a(7)*
dnfXdXn(3)+1814400* a(1)^2* a(8)* dnfXdXn(3)+ ...
    907200* a(2)^2 *a(3)^2* dnfXdXn(4)+604800* a(1)* a(3)^3* dnfXdXn(4)+604800* a(2)^3* a(4)* dnfXdXn(4)+3628800* a(1)*
a(2)* a(3)* a(4)* dnfXdXn(4)+ ...
    907200* a(1)^2* a(4)^2* dnfXdXn(4)+1814400* a(1)* a(2)^2* a(5)* dnfXdXn(4)+1814400* a(1)^2* a(3)* a(5)* dnfXdXn(4)+
...
    1814400* a(1)^2* a(2)* a(6)* dnfXdXn(4)+ 604800* a(1)^3* a(7) *dnfXdXn(4)+ ...
    30240 *a(2)^5* dnfXdXn(5)+604800* a(1)* a(2)^3* a(3)* dnfXdXn(5)+907200 *a(1)^2* a(2)* a(3)^2* dnfXdXn(5)+907200*
a(1)^2* a(2)^2* a(4) *dnfXdXn(5)+ ...
    604800* a(1)^3* a(3)* a(4)* dnfXdXn(5)+604800* a(1)^3* a(2)* a(5)* dnfXdXn(5)+151200* a(1)^4* a(6)* dnfXdXn(5)+ ...
    75600* a(1)^2* a(2)^4* dnfXdXn(6)+302400 *a(1)^3* a(2)^2* a(3)* dnfXdXn(6)+75600* a(1)^4 *a(3)^2* dnfXdXn(6)+151200*
a(1)^4* a(2)* a(4) *dnfXdXn(6)+ ...
    30240* a(1)^5* a(5)* dnfXdXn(6)+ ...
    25200* a(1)^4* a(2)^3* dnfXdXn(7)+30240* a(1)^5* a(2)* a(3)* dnfXdXn(7)+5040* a(1)^6* a(4)* dnfXdXn(7)+ ...
    2520* a(1)^6* a(2)^2* dnfXdXn(8)+720* a(1)^7* a(3)* dnfXdXn(8)+ ...
    90 *a(1)^8* a(2)* dnfXdXn(9)+ ...
    a(1)^10* dnfXdXn(10));

end

end
```

---

### #2431 — Amin (Topic Author)
*August 19, 2024, 4:30 PM*

This program computes coeffs of Z-series when values of raw moments of the random variable are given using Iterative
method.

.

.

.

.

```
function [c,ObjFunc] = ZSeriesCoeffsFromMomentsIterative(rMu,c0,c,SeriesOrder,NMoments,Iterations)

%This program computes coeffs of Z-series when values of raw moments are
%given using Iterative method.

%rMu are raw moments;
%c0,c are coeffs of Z-series to be found and when passed as parameters
%contain starting guess for Z-series coeffs.
%Series order is max coefficient of c. Here it is 7;
%Nmoments are maximum number of moments to use in calibration. Here this
%number is eight.
%The following relationship holds
%SeriesOrder=NMoments-1
%Total number of Iterations of the iterative method are given by input
%parameter iterations.
%The present program is written for SeriesOrder=7.
%To later it, you need to change the following line everywhere in program accordingly
%c0in=-(cin(2)+3*cin(4)+15*cin(6));
%If you change to SeriesOrder=10, the above line would change to
%c0in=-(cin(2)+3*cin(4)+15*cin(6)+105*c(8));
%If you change to SeriesOrder=6, the above line would change to
%c0in=-(cin(2)+3*cin(4));

% You can run the program by decommenting the following block if you are
% not using Input parameters of yours.
%
% rMu(1)=0.000012499863483*10^5;
% rMu(2)=0.000021197093700*10^5;
% rMu(3)=0.000050274347857*10^5;
% rMu(4)=0.000171368317209*10^5;
% rMu(5)=0.000856094970826*10^5;
% rMu(6)=0.006320436615909*10^5;
% rMu(7)=0.068698344472325*10^5;
% rMu(8)=1.084082326087001*10^5;
%
% c0=0;
% c(1)=1;
% c(2:7)=0;
%
% SeriesOrder=7;  %Z-series till 7th power.
%
% NMoments=8;
%
% Iterations=500000;

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
sMu(7)=cMu(7)/cMu(2).^3.5;
sMu(8)=cMu(8)/cMu(2).^4.0;

c(1)=1;
c(2:SeriesOrder)=0;

%%%%%%Choose the iteration step size.
for nn=2:SeriesOrder
    DeltaX(nn)=.00125/(factorial(nn));
end

%%%Weights on objective function that shows fit to moments
w(NMoments)=1;
for nn=NMoments-1:-1:1
    w(nn)=w(nn+1)*(nn+1).^2;
end

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

[ObjFuncBest] = CalculateObjMoment(sMu,Moments,w,mOrder);

cBest=c;

ImproveFlag(1:SeriesOrder)=1;
ImproveFlagPrev(1:SeriesOrder)=0;
ImproveCount(1:SeriesOrder)=0;
for mm=1:Iterations

    %We only iteratively alter c(2:7), first and second moments are
    %retrieved automatically in our set up
    for nn=2:SeriesOrder

        ImproveFlagPrev(nn)=ImproveFlag(nn);

        cin=c;
        cin(nn)=cin(nn)+DeltaX(nn);
        c0in=-(cin(2)+3*cin(4)+15*cin(6));

        [Moments] = CalculateMomentsOfZSeries(c0in,cin,SeriesOrder,2);
        SecondMoment=Moments(2);

        cin=cin/sqrt(SecondMoment);
        c0in=c0in/sqrt(SecondMoment);
        [Moments] = CalculateMomentsOfZSeries(c0in,cin,SeriesOrder,NMoments);

        [ObjFunc] = CalculateObjMoment(sMu,Moments,w,mOrder);

        if(ObjFunc<ObjFuncBest)

            ObjFuncBest=ObjFunc;

            cBest=cin;
            c=cin;
            ImproveFlag(nn)=1;

        else

            cin=c;
            cin(nn)=cin(nn)-DeltaX(nn);
            c0in=-(cin(2)+3*cin(4)+15*cin(6));
            [Moments] = CalculateMomentsOfZSeries(c0in,cin,SeriesOrder,2);
            SecondMoment=Moments(2);
            cin=cin/sqrt(SecondMoment);
            c0in=c0in/sqrt(SecondMoment);
            [Moments] = CalculateMomentsOfZSeries(c0in,cin,SeriesOrder,NMoments);

            [ObjFunc] = CalculateObjMoment(sMu,Moments,w,mOrder);
            if(ObjFunc<ObjFuncBest)

                ObjFuncBest=ObjFunc;
                cBest=cin;
                c=cin;
                ImproveFlag(nn)=-1;
            else
                 ImproveFlag(nn)=0;
            end
        end

    %Index(nn)
    end

    if(rem(mm,1000)==0)
    mm
    ObjFuncBest
    DeltaX
    ImproveCount
    end

    ImproveFlag0=0;
    for nn=2:SeriesOrder
       if(ImproveFlag(nn)==1)
           ImproveFlag0=1;
       end
    end
    for nn=2:SeriesOrder
        if(ImproveFlag0==0)
            DeltaX(nn)=DeltaX(nn)*.88;
        end
    end

end
c=cBest;
c0=-(c(2)+3*c(4)+15*c(6));
[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

Moments
sMu

str=input("Look at comparison of Standardised model moments and Standardized target moments")

c0=c0*sqrt(cMu(2)); %convert from standardized to central moments
c=c*sqrt(cMu(2));   %convert from standardized to central moments

c0=c0+Mu1;          %convert from central to raw moments by adding mean.

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments)
rMu

str=input("Look at comparison of model raw moments and target raw moments")

end
```

---

### #2432 — Amin (Topic Author)
*August 22, 2024, 7:49 AM*

Friends, I have posted a new version of the paper at SSRN. Here you can review it

https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4933283

Here is the abstract:

Abstract

We give a series representation of non-Gaussian continuous random variables in terms of a Taylor Series (Z-Series) in
Standard Gaussian random variable or alternatively a series in Hermite polynomials (Hermite-Series) of Standard Gaussian
random variable. We present simple numerical methods to find coefficients of these series given the density, data or
moments of the non-Gaussian random variable. We also show how to do basic operations like addition, subtraction, and
taking functions of non-Gaussian random variables using their Z-series. We present the concept of correlations between
Hermite polynomials of Hermite-Series of two non-Gaussian random variables. These Hermite polynomial correlations are
far more robust than the correlations between non-Gaussian random variables we presently see in literature. Then we
present methods to calculate conditional expected values and distributions of a non-Gaussian random variable given the
value or distribution of another correlated non-Gaussian random variable. We apply the conditional distribution
knowledge to calculation of regression coefficients in a Hermite-Series regression. At the end, We apply the methods
learnt to various applications in simulation of Stochastic differential equations, financial trading and hedging of
securities.

**Keywords:** Non-Gaussian Continuous Random variables, Non-Gaussian Conditional Expectation, Correlations, and
Hermite-Series Regression

---

### #2433 — Amin (Topic Author)
*August 27, 2024, 3:38 PM*

Why do people not invest hugely in Samsung Electronics.

NVIDIA  Revenue  For 12 months Ending in April 2024:  Roughly  85 Billion dollars

NVIDIA Market Cap: Roughly 3000 Billion dollars.

Samsung Electronics Revenue 2023: 200 Billion dollars

Samsung Electronics Market Cap: 380 Billion dollars

Samsung profit has been erratic in last few years ranging from eight billion dollars per year to 50 billion dollars per
year.

American companies should leverage their stock valuations to buy large stake in Samsung. Too cheap. It's a leader in
many key technology segments.

---

### #2434 — Amin (Topic Author)
*September 2, 2024, 4:15 PM*

I have corrected the post below. I have written dominance of Jews in US instead of US dominance for clarity. By UsS
dominance, I meant dominance of jews in US. Thousands of US born Americans are retarded by US Defense on behest of evil
jews, now that is not helping US dominance in any way at all. Here is the post.

Friends, mind control is raging at full swing in Lahore city. They are trying their best with hundreds of people all the
time to drug food and water when I go out to get good food. Still I was able to get good water from a remote area and
brought it home. But today I had to go to Daewoo transport office. My sister had gone to UK and had brought good Joggers
for me from there and had sent then to me through Daewoo transport. When I went in the building, I carried my food and
water with me but they asked me to go to another building. When I went to the different building, I parked my car
outside and did not take water and food with me but I continued to take a peek on my car from time to time like every
minute from the large open door. But I still had to talk to the staff and ask for the shoes. I did not make a  big deal
but when I came home, I realized that my water had been drugged. It was both charging my body and also making me say bad
things about shit-pieces of American defense.

I want to tell people that decades ago, I Watched a movie in which the world is destroyed after a nuke war and there are
a very few people left alive here and there among ruins. They showed a large group of hideous people who thoroughly
hated beauty and got together and would kill any beautiful human being they would come across.

I think this is a great analogy for scumloads of American defence and bad jews whose cruelty knows no bounds. All over
the world, wherever they see talent, intelligence, or brilliance, these loser jews ask the horses of defense (on which
these bad jews ride) to retard the intelligent or talented people with an iron fist. And these loser and cruel jews have
absolutely no humanity and empathy and are proud of their cruelty.

As I see this that most of the jews that came to United states were from very poor background and were also reasonably
intelligent and they knew they had to move their ass to get ahead in this world so they worked very hard and as a result
made quite a lot of contributions to science and technology and so many other fields. Now the new generations of jews
have nothing to do with poverty and are quite rich so they do not have the same strong urge to work their ass off to get
ahead in this world as they are already born with a silver spoon. When older generation of jews see that their
offsprings are not the same material, they resort to machinations and trickery to remain richest and most powerful group
in United States. Instead of making their children work harder, they ask US defense (who is their total crony) to retard
any other intelligent people who are trying to get ahead so that dominance of Jews in US that was once build on hard
work can be maintained by trickery and machinations. There was a time universities had to cut down on jewish students
entering their ranks but now percentage of jewish students is falling in all good universities despite they are
preferred by universities for admission in recent times.

Tens of thousands or possibly more than a hundred thousand intelligent people most of whom were US born Americans have
been retarded by US defense on behest of rich and corrupt jews so that they can maintain their dominant richest status
in US. But I am aghast at the extreme cruelty of these jews that they have absolutely no remorse about their evil deeds.
Even now when a lot of truth about them is getting exposed, they are more concerned with somehow continuing mind control
and have absolutely no remorse about their extreme cruelty.

It seems to me that many of these bad jews want society to behave very nicely towards them while they do not want to
fulfill any responsibility towards society. They want to keep retarding thousands of innocent souls every year while
systematically calling people anti-semite who object to their extreme cruelty. They simply just cannot get enough of the
best of all worlds.

Last of all, I was very determined to remain shut up and not say anything against these scumbag jews despite their
hideous evil but I was forced to say it because they mixed their bad neurotransmitters in my water when I went to Daewo
office to get my shoes one and a half hour earlier.

---

### #2435 — Amin (Topic Author)
*September 3, 2024, 7:37 AM*

About a week or two ago, I approached a bunch of people in risk management and trading regarding consulting work but I
know that scumbags of American defense approach all the concerned people and ask them to not cooperate at all. So I had
no luck. Here I want to tell friends that I have not earned any money other than 3500 USD after August 2010 when I went
to UK. Crooks of American defense approach everyone in Europe, Japan, Korea, Singapore, Australia and even India with
thorough consistency and force people through their respective governments/armies to not give me any sort of work at
all. But I remained unfazed and despite being forced on extremely high antipsychotics in the past, I continued to do my
research and post it on Wilmott.

I greatly try to avoid sending mails to people for any sort of consulting work since I already know the outcome, but
since I have done some reasonably decent research work in past few years, I was hopeful that somebody might be willing
to give me some consulting work but of course to no avail. After a week of thought I have come to this realization that
I will have to do something on a solo basis like algorithmic stocks trading or something like that. I have previously
done very good work on algorithmic trading and thought that I would use fast algorithmic trading to make some money but
the problem is that kind of fast trading that requires possible trade after ten every or a few tens of seconds requires
perfect infrastructure and very good programming. Army introduced government fire wall in pakistan  and that has greatly
decreased the data transfer rate and in slow times (that can be very frequent) a ping can take many seconds.

So I decided to work with trading on a larger time scale where I would have to trade every few hours or on a daily basis
or something like that. But as the time between trades increases, it continues to become harder to make significant
profits out of long term trades. But I am determined to follow this route and try to do some research to make some
profitable trading strategies. Even though it might be tough, I am willing to spend several months now to make something
possible. I have made up my mind and I do not want to go back on this idea so if anybody even asks me for consulting
work, I will like to politely refuse.

So for next few months, I would not be posting very frequently on Wilmott. However I have some ideas about use of
conditional distributions (orthogonal + dependent case) in stocks trading and I would possibly be posting some programs
about them and some other basic infrastructure related to Z-series. But I doubt that I would be posting very regularly.

However, I certainly want to say that I am very thankful that I had the opportunity of doing some decently good
research. And I am very grateful to be of help to some friends who might have used this research in their applications.
And I want to continue to do this for the rest of my life regardless of what people do or say or what they do not do or
do not say.

But until I have found some decent algorithms for trading on a medium term scale, I would not be present on Wilmott all
the time. However, as soon as my research is complete and I have some source of income, I would come back to Wilmott and
start doing and sharing my research as I used to do. I have a lot of ideas about further continuing the research work I
have presented in my recent paper and would want to take that towards successful completion and beyond. I would
certainly be posting from time to time like one or two posts a week and keep friends in touch with my progress and other
things. And resume again in about two months with new research work on Wilmott.

---

### #2436 — Amin (Topic Author)
*September 3, 2024, 8:59 PM*

Friends, I usually go to buy food and water every second day and today it was not my day to go out. But yesterday, I had
bought tea from four different small local brands. Many small shops usually allow the tea of these local brands to be
returned if the customer does not like the tea after taking a tea spoon or two out of the packing. I had talked to each
shop owner that I would return the tea  if I did not like it. And I had to return tea of all four brands since they were
all drugged with mind control. The weather in the evening was pleasant and I decided to return the tea and take my money
back. It was very sudden and I was not thinking of going out today. But I was surprised when I realized that even on a
very brief notice, army had started to revive their old practice of drugging the entire markets on my way something they
had not done since last December. They had realized that I was not suspecting anything of the sort that they would be
drugging the entire markets  and they could easily be able to drug my food somewhere. Many American friends can inquire
their Pakistani contacts to ask if army was drugging samanabad and several other adjacent areas and narrow streets today
evening.

When I returned home, I was also greeted by huge gas coming out of fans in almost every room of the house and especially
there was some different gas in my room. I am going to sleep no but frankly I am worried how they would use the gas on
me all the rest of tonight.

They have continued to increase the number devices and gadgets on my motorcycle. When I am driving along they keep
ejecting EM waves out of the motorcycle seat to target the anus and sometimes it is so extremely uncomfortable that I
have sit on the motorcycle with very odd positions. And recently they have made some precise calculations of throwing
gas that comes out of the front of the motorcycle possibly close to its front light and goes directly in the breath
despite sweeping air on all sides of the open motorcycle.

I want to advise American defense to watch a lot of American movies and try to behave like heroes in those movies.
Instead people in American defense are short-tempered scumbags who became belligerent when anybody criticizes them.
Contrary to American and Western spirit of freedom of criticism and speech that we all cherish, these short-tempered
scumbags are unwilling to tolerate anything other than eulogies based on complete lies. Just like Henry Ford used to say
that you can buy any color of car as long as it is black, to these scumbags of American defense the freedom of speech
means that you can say anything you like as long it is a eulogy otherwise they become belligerent and start moving
thousands of people to silence someone who speaks the truth about them. Let us all of us start cursing Erdogan together
now.

---

### #2437 — Amin (Topic Author)
*September 5, 2024, 10:44 AM*

Friends, I was a bit excited today since I wanted to write two special posts about continuation of my previous research.
Just an hour and a half ago, I decided to go out and buy something to eat and thought that I will write the posts after
taking food when I would be totally relaxed.

Here I want to tell friends that Fluanxol injection is manufactured by scumbags of lundbeck. This injection was used to
be so completely drugged with mind control chemicals about a year ago that I would not be able to have a proper
conversation with anyone for two weeks after I would be given half injection manufactured by scumbags of lundbeck. I
would have extreme pain all over my body for two to three weeks after the half injection. When I would have to make an
appointment with anyone or even talk on phone, I would make sure that this would not lie in fifteen days after the
injection by lundbeck since I would not be able to speak properly at all. All these scumbags of lundbeck want is money
and these shitpieces would even gladly kill people to make money.

I continued to write about bad injections for years and I am sure a lot of other victims complained about it and the
injections improved all of a sudden. Injections manufactured in 2022 till August 2022 were almost good with very little
amount of mind control chemicals. But nature of scumbags who start making big money out of bad things hardly ever
changes, so scumbags of lundbeck introduced bad injections again in 2023. Injections manufactured in 2023 are very bad
again. I have been complaining about it lightly for two to three months now but to no avail. So I have to be very
careful about fluanxol injections. Another big problem is that injections manufactured in 2022 are relatively rare in
market and I strongly believe that were bought off the market by bad people however there are still a few shops that
still carry injections manufactured in 2022. I was luckily able to buy a Fluanxol injection manufactured in 5/22 (when
scumbags of Lundbeck had temporarily turned better) from a remote place and I always kept it on myself. I used to keep
the injection in my cotton trouser's side pocket but once I had an odd angle and its ampule was broken. So this time I
kept the injection in front pocket of my shirt. Its storing temperature is 30 Centigrade so it is fine in shade these
days. New injection is due in less than a week.

Now when I went out to buy food, in some shop there was a lot of rush and some of the scumbag of Pakistan army very
quietly plucked the injection out of my pocket since they want to force an injection that is manufactured in 2023 by
scumbags of Lundbeck and contains mind control drugs in it.

I will have to buy a new injection in next few days and obviously I would try to buy a good injection if I can. Now
either shit-pieces of Pak army or lundbeck will go to various shops and supply new injections or ask them to not sell
old injections.

I have noticed previously that many times mind control agents try to be discreet when sending voice to skull messages
and conversation to many shop-keepers or pharmacy staff and I suspect that sometimes good people listen to what they say
to pharmacy staff/shopkeeprs using voice to skull and their such conversation are recorded. So if somebody good listens
to their voice to skull conversations, I want to request them to please keep a vigil and make sure they do not force
pharmacy owners in next few days to not give me injections (as they are asked to do when they find out that injection is
good) and force me to buy injections from some special shops.

I have previously noticed in past one week that mind control agents want to give me some special drug so I would not be
able to do any intellectual activity at least for a few months and they are becoming very bitter about doing this. And
therefore I became a bit extra cautious about my food recently. And stealing the injection out of my pocket is part of
the same activity as mind control agents are under extreme pressure to do something that I cannot continue my research
and also cannot write any post about evil activities of bad people in US defense.

Sorry but I will make my posts about Mathematics research in another two hours and hope even if I lose intellectual
activity, something positive will always be known to people.

---

### #2438 — Amin (Topic Author)
*September 5, 2024, 6:42 PM*

Friends, I have been trying to improve my iterative optimization algorithm that has worked reasonably well for finding
coefficients of the Z-series that match the moments. I was thinking that it would be nice if the program could be
generalized and used for more difficult multidimensional optimization problems. And I made some interesting
observations.

In general optimization theory states that step size in multiple dimensions for optimization purposes have to be chosen
proportional to derivative of the objective function being minimized/maximized. And I was surprised to know that this
works quite poorly when I tried it find coefficients of Z-series that minimize the objective function. I cannot say what
the reason but I speculate that this choice of step size in proportion to derivatives of objective function continues to
seek local minima and gets trapped there.

I think it is very important to stay away from local minima and still keep improving the objective function. While
working with optimization of coefficients of Z-series, I noticed that it is more important to keep the step size in most
important dimension changing independently with small increments while making sure that step size in other directions
changes inversely proportionally to derivatives of objective function with respect to those dimensions. This makes sure
that optimization does not go into local minima and it also makes sure that changes in objective function with respect
to coefficients of other dimensions are smaller or roughly close to changes in objective function with respect to the
most important dimension.

I really think that a large number of high dimensional optimization problems can be solved by iterative optimization
like we have used for fitting Z-series to moments but one has to find the optimal ratio of step sizes and algorithm to
optimally change this ratio along the optimization routine. If optimal ratio of step size could be known, iterative
optimization can be quite successful for many such difficult high dimensional optimization problems. It requires some
exploratory analysis of the problem and some experimentation with the problem to find optimal step size and how to alter
this step size along the progress of optimization algorithm.

I have tried this on our Z-series coefficients fitting program and the results seem to be quite good. I will do some
more experimentation with the program and post it for friends in a few days.

---

### #2439 — Amin (Topic Author)
*September 6, 2024, 7:09 PM*

Friends, I was thinking of PDEs and I just realized that a lot of PDEs with continuous derivatives on a finite domain
can be solved by expressing the underlying functions as Taylor series. With a finite domain, the Taylor series expansion
would not blow at the boundaries. Of course, all functions with continuous derivatives cannot be easily captured by
polynomials and normal density function is an obvious example. But most such functions can be captured by for example
product of an intelligently chosen analytic function and a polynomial like we can multiply a Gaussian exponential
function with  a polynomial with finite number of terms and then Taylor expand all of it and also take its derivatives
and substitute them in a PDE.

We worked quite a bit in the past with Z-series and an analogue of Z-series could be a U-series in which Taylor expanded
polynomial's integral over finite domain would be normalized to one and we could then solve many PDEs with such U-Series
polynomials or related Legendre polynomials. It would be many times convenient to normalize the integral but if we do
not want to do that, we could just use a Taylor series or other suitable analytic functions multiplied by polynomials
and apply it to the PDE to find the solution.

I worked for a few weeks with Schordinger equation to find orbitals of elements with multi-electrons. And I speculate
that hydrogen orbitals as basis functions for determining the electron structure of higher elements do not span the full
space required for a proper solution of the multi-electron problem since if they did somebody would have found the true
optimization of the unique problems associated with a handful of elements. I mean if hydrogen orbitals (or other trial
basis functions) spanned the full space, it would simply be an optimization problem. I believe that for a true solution
of schordinger equation, we might have to use some sort of Taylor expansion of the hydrogen orbitals or possibly
multiplication of another polynomial term with hydrogen orbitals or other trial basis functions. Even though, I learnt
that Euclidean coordinates are lesser used for multi-electron solutions, I would speculate that some intelligent
functions multiplied with appropriate polynomials in three dimensions might be somehow able to solve for the
multi-electron schordinger equation.

These are just some random thoughts and I thought I would share them with friends.

---

### #2440 — Amin (Topic Author)
*September 7, 2024, 3:49 AM*

I have copied this from previous post and expanding on it further

Friends, I was thinking of PDEs and I just realized that a lot of PDEs with continuous derivatives on a finite domain
can be solved by expressing the underlying functions as Taylor series. With a finite domain, the Taylor series expansion
would not blow at the boundaries. Of course, all functions with continuous derivatives cannot be easily captured by
polynomials and normal density function is an obvious example. But most such functions can be captured by for example
product of an intelligently chosen analytic function and a polynomial like we can multiply a Gaussian exponential
function with  a polynomial with finite number of terms and then Taylor expand all of it and also take its derivatives
and substitute them in a PDE.

For example, if you take a Gaussian exponential and multiply it with a polynomial to find a trial solution of a PDE, you
might possibly have some problems with integrations and differentiations but you could replace the polynomial part with
an equivalent hermite polynomial series and integrations and differentiations would go seamlessly. Similarly if for the
solution of your PDE, you have to deal with sinusoids and you want a guess solution in the form of some analytic
function sinusoids multiplied by a polynomial, you could replace the polynomial with a chebyshev series and integrations
and differentiations would go seamlessly.

Again whenever there is an analytic function as trial solution and we need to multiply it with a plain polynomial, many
times we can replace the polynomial with an equivalent series in some special polynomials so that integrations and
differentiations after multiplication with the analytic function (that can be a gaussian exponential of some sinusoidal
function) would go seamlessly.

---

### #2441 — Amin (Topic Author)
*September 8, 2024, 6:26 AM*

Friends, I would love to work with Schordinger equation again sometimes later after completing the current work at hand.
But my technique to solve it would be to guess basis functions that fully span the space of multielectron solution of
Schordinger equation. I have been away from Schordinger equation details for a bit but guessing: Every orbital in
multielectron case is affected by many other remaining orbitals, so to find orbitals of any electron, we at least need
an N dimensional representation (possibly N dimensional for each of more than one quantum numbers). Suppose we have
carefully found an appropriate set of basis that fully spans the space of N multielectron solution of the problem, we
can use Hartree-Fock method to find an initial solution of the problem in a usual way. We know that Hartree-Fock method
gives a close but not perfect result. So we can project the solution after performing optimizations on Hartree-Fock
equations and then project this solution from basis functions used for Hartree-Fock method to our newly designed basis
functions (that might possibly have higher dimensionality) that are supposed to fully span the solution of N-electron
problem. And then re-do the optimizations on full-span basis functions. Since our initial guess from Hartree-Fock is 
already very close to true solution, this optimization should not be extremely difficult.

This seems interesting to find the solution of a high dimensional problem in a low dimensional basis (if some low
dimensional basis is known that is good enough) and do the optimizations to get a good initial guess from low
dimensional basis and then project this approximate but good guess on full dimensional basis and then rather easily
solve the high dimensional optimization problem.

---

### #2442 — Amin (Topic Author)
*September 8, 2024, 4:39 PM*

>
> Friends, I have been trying to improve my iterative optimization algorithm that has worked reasonably well for finding
coefficients of the Z-series that match the moments. I was thinking that it would be nice if the program could be
generalized and used for more difficult multidimensional optimization problems. And I made some interesting
observations.
>
> In general optimization theory states that step size in multiple dimensions for optimization purposes have to be
chosen proportional to derivative of the objective function being minimized/maximized. And I was surprised to know that
this works quite poorly when I tried it find coefficients of Z-series that minimize the objective function. I cannot say
what the reason but I speculate that this choice of step size in proportion to derivatives of objective function
continues to seek local minima and gets trapped there.
>
> I think it is very important to stay away from local minima and still keep improving the objective function. While
working with optimization of coefficients of Z-series, I noticed that it is more important to keep the step size in most
important dimension changing independently with small increments while making sure that step size in other directions
changes inversely proportionally to derivatives of objective function with respect to those dimensions. This makes sure
that optimization does not go into local minima and it also makes sure that changes in objective function with respect
to coefficients of other dimensions are smaller or roughly close to changes in objective function with respect to the
most important dimension.
>
> I really think that a large number of high dimensional optimization problems can be solved by iterative optimization
like we have used for fitting Z-series to moments but one has to find the optimal ratio of step sizes and algorithm to
optimally change this ratio along the optimization routine. If optimal ratio of step size could be known, iterative
optimization can be quite successful for many such difficult high dimensional optimization problems. It requires some
exploratory analysis of the problem and some experimentation with the problem to find optimal step size and how to alter
this step size along the progress of optimization algorithm.
>
> I have tried this on our Z-series coefficients fitting program and the results seem to be quite good. I will do some
more experimentation with the program and post it for friends in a few days.
>
.

.

Friends, I believe that iterative optimization can be generalized to quite high dimensional optimization problems. All
you need to so is to follow the following points.

1. Keep initial step size quite small.

2. Make the step size in each dimension inversely proportional to gradient of objective function with respect to that
dimension meaning that change in objective function to perturbation in any dimension would be roughly of the same order
not considering the sign of change in objective function. You do not have to impose this condition on every step. Since
total optimization can take tens of thousands or hundreds of thousands iterations over all dimensions, you can apply the
condition of step size being roughly inverse of the gradient of objective function after every hundred iteration steps
(over all dimensions) or so.

3. Again when the step size has been fixed according to consideration in previous two points, all you have to do is to
add the step size in one direction and accept the iteration  if the objective function decreases and update the
parameter in that dimension. If the objective function does not decrease by addition of step size in that dimension, you
subtract the step size in that dimension and see if the objective function decreases. Again decrease in parameter is
accepted if the objective function decreases with decrease in parameter in that particular dimension. If the objective
function does not decrease in both directions by adding or subtracting the step size, we do not change the parameter of
that direction and keep it at its old value from previous iteration. We repeat this process over all dimensions. And
when there is no decrease in objective function after adding and subtracting the step sizes (that are roughly inversely
proportional to gradient of objective function with respect to that dimension) in all dimensions, we cut the step size
along all dimensions to .95 or .9 of the previous step size and optimization starts working again.

4. After repeated decrease of step size(as we cut step size when optimization in all dimensions fails with going step
sizes at that time) a few multiple times, we try to see if the variables are almost in the same neighborhood as they
were in previous decreases of step size, we can ascertain that we have reached close to global minimum and parameters
are changing in the same neighborhood and we can switch to some gradient based strategy or possibly some Newton type
strategy that can quickly take us to closest minimum since we expect that local minimum and global minimum there are the
same.

I think it would be certainly possible to make an iterative optimization strategy for multilayer neural networks but I
will need to first play with that before I can make any possible observations.

---

### #2443 — Amin (Topic Author)
*September 8, 2024, 10:09 PM*

Friends, I did some analytics about the optimization problem for fitting Coefficients of Z-series to moments. While
perturbing parameters for fitting to standardized moments, I am analytically trying to stay on the same plane where the
unity constraint for standardized variance is satisfied on coefficients. In a way I am already doing that numerically by
dividing the perturbations with square root of second moment but I want to try to do it more analytically. I believe
that any extra information like constraints on optimization should be very helpful as they add more information to the
problem and if tackled properly they should not be a hassle at all. I had earlier tried this but my analytics were very
poor and it took a very long time to make calculations to stay on the unity variance hyperplane.

I have done some analytics tonight and I want to try programming them tomorrow. Even though there is some chance that
things might not go perfectly well, but I am very hopeful that I would get a new program to work on the problem. And if
I could do that I would post it tomorrow.

---

### #2444 — Amin (Topic Author)
*September 10, 2024, 7:16 PM*

Friends, I was unable to get good water yesterday and remained unable to do any good work. Only today afternoon, I
managed to get plenty of good water for next two days. For past two three days I have been thinking about optimization
problems with constraints but really not have been able to do any work about related programming in matlab so basically
unable to post any program.

On Thursday, I have another fluanxol injection due and within days of that I might lose a lot of intellectual thought
for a week to ten days. How it goes with Fluanxol injection this time, I cannot say.

I will mostly be busy with programming for medium frequency trading for next few weeks as I had mentioned. I dropped the
programming for trading during past few days since this was last week before injection and I had some more better
facility of thought and I decided to spend this time thinking about other problems of interest.

I assure friends that in a few weeks, I would be back to programming and there are many interesting things to do. We
have to work with multidimensional conditional distributions, and I had ideas about inferring correlations between
various hermite polynomials from moments and cross moments data. There is also some more work about the case when
orthogonal part of variable in conditional expected distribution depends upon other variables. And I wanted to write an
optimization program that optimizes for the coefficients of a Z-series so that optimization remains on a hyperplane
where variance, skew and kurtosis remain simultaneously matched and hence first three coefficients are found from
constraint of remaining on this hyperplane while rest of the coefficients are perturbed in the direction of increasing
objective function. There are a lot of other interesting things to do. And the best thing is that in a few weeks warm
weather would be gone and I would love to work late at night in pleasant temperatures.

---

### #2445 — Amin (Topic Author)
*September 13, 2024, 11:45 AM*

Friends, I want to describe the method to find the conditional distribution of Y p(Y|X) when its orthogonal part is
dependent on X. I am copying the section of my paper for the friends to get oriented and will explain the detailed
method in next post.

**Calculating Conditional Distribution of Random Variable Y When its Part Orthogonal to X is Dependent on Correlated
Random Variable X**

While calculating conditional expectation in previous section (\ref{sec4.5}), we have assumed that part of Y orthogonal
to X is independent of X which is most likely not the case. For example consider an SDE-like dependence equation of a
random variable

\begin{equation}\label{4.6.1}

 \,Y \,= \, \mu(X) \, + \, \sigma(X) \, W

\end{equation}

where W would usually be a zero mean non-Gaussian random variable which is assumed to be independent of$\sigma(X) \,$ .
And$ \mu(X) $ and$ \sigma(X) $ are some functions of non-Gaussian random variable X. The first term$\, \mu(X) \,$ should
be perfectly captured by Hermite polynomial correlations in our conditional expectation equation but we see that
orthogonal term$\,\,\sigma(X) \, W\,\, $ , in equation that describes Y, even though orthogonal to X is not independent
of X. So different realizations of X over its density should also affect and alter the conditional distribution of part
of Y orthogonal to X and we would have to do more analytics to calculate the effect of X on orthogonal part of Y for a
proper calculation of conditional distribution of Y.

In order to find the true distribution associated with univariate conditional expectation of a random variable Y given
X, we again perform the de-correlation operation discussed in previous subsection (\ref{sec4.3}) on jointly observed
values of data sample of X and Y, and then we can find that$\tilde{Y}$ represents the Orthogonal part of Y that is not
correlated to the variable X.

This part of Y orthogonal to X can be written as an equation as

\begin{align}\label{4.6.2}

 & \tilde{Y} \,=\, Y\, -\, E\left[Y|X \right] \, \\ &=  \,
Y\,-\,\,\sum\limits_{n=1}^{N}\,\frac{Cov_{XY,n}}{Var_{X,n}}\,bh_n \, H_n(Z_X) \\ \, &=  \,
Y\,-\,\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \,ch_n \, H_n(Z_X)

\end{align}

We suppose that the knowledge of dependence structure of orthogonal term of Y on X is exogenously known and is given as
$\sigma(X)$ . From section (\ref{sec2.5}), we already know that we can find a Z-series of$\sigma(X(Z))$ through Taylor
Series on Z-series of X.

\begin{equation}\label{4.6.3}

\sigma(X(Z_X))=\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_X)

\end{equation}

Now we see that Z-series structure of $ \tilde{Y} $ with dependency structure included in equation is given as

\begin{equation}\label{4.6.6}

 \tilde{Y} \,=\, \, \sigma(X) \,\,W\,=\, \, \sigma(X) \,\, \sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \ \,

 \end{equation}

The random variable$\sum\limits_{m=1}^M \tilde{ch}_m  H_m(Z_W) $ with as yet undetermined coefficients
$\tilde{ch}_m, (m=1,\ldots,M) $ is supposed to capture the distribution structure of non-Gaussian noise in the equation
of part of Y that is orthogonal to X.

We use two different methods to estimate these coefficients depending upon if we are given data of joint observations of
random variable X and Y or if we have knowledge of moments of$\tilde{Y}$ that is part of Y orthogonal to X.

**Calculating Conditional Distribution of Part of Random Variable Y that is Orthogonal to but Dependent on Random
Variable X When Numerical Data of X and Y is Available**

Suppose. we have a total of P joint data observations of Y and X, with pth observation pair of both random variables is
given as$Y_p$ and$X_p$ . We first invert Hermite-Series equation of$X_p$ to find$Z_{X_p}$ and then use the following
equation for each pth observation

\begin{equation}\label{4.6.7}

 \tilde{Y_p} \,=  \, Y_p\,-\,\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \,ch_n \, H_n(Z_{X_p})

\end{equation}

As we described in previous section that we know the functional form of$\sigma(X)$ and we can easily Taylor expand it to
find a Hermite-series given by equation (\ref{4.6.3}). For pth observation, this value of$\sigma(X)$ can be represented
as

\begin{equation}\label{4.6.8}

\sigma(X(Z_{X_p}))=\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p})

\end{equation}

since $\tilde{Y_p} \,$ is given by equation(\ref{4.6.6}), for pth joint

observation of data, we would have

\begin{align}\label{4.6.9}

 &\tilde{Y_p} \,=\, \, \sigma(X_p) \,\,W_p\,\\

 & \,=\, \, \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\,W_p\,

 \end{align}

Since we have calculated$\tilde{Y}_p$ for each of the pth joint observation$(p\,=\,1,\,\ldots,P)$ of Y and X in
equation(\ref{4.6.7}) and we have also calculated Hermite Series of$\sigma(X_p)$ in equation(\ref{4.6.8}), we could
calculate the value of$W_p$ associated with pth observation of as

 \begin{align}\label{4.6.10}

 &\, \,W_p\, \,=\, \, \frac{\tilde{Y_p}}{\sigma(X_p)} \,\\

 & \,=\, \,\, \, \frac{\tilde{Y_p}}{\left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right)} \,\\

 \end{align}

Depending upon the problem and application, it would be advisable to consider removing those values of data for which
$\left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right)$ is very small and where above equation nearly beomes
singular.

After finding$W_p$ , we could use the method discussed in section(\ref{sec3.2}) by sorting data for
$W_p\,,(p\,=\,1,2,\ldots,P)$ and then regressing on Hermite polynomials calculated at discrete normal density grid
associated with data size P and thus finding the coefficients of uni-variate Hermite series of W. Once, we have this
series, represented as$\, W\,=\,\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \ \,$ , we could represent conditional
distribution of Y as

\begin{align}\label{4.6.11}

 & Y\, | \, X=\, E\left[Y|X \right]+\,\, \sigma(X(Z_{X_p})) \, W  \\

 &=\mu_Y+\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \, ch_n \, H_n(Z_X)+\,\, \left[ \sum\limits_{n=0}^{N}\, dh_n \, H_n(Z_X)
\right] \, \left[\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W)\right]

 \end{align}

---

### #2446 — Amin (Topic Author)
*September 13, 2024, 1:05 PM*

Once we have found the decorrelated $ \tilde{Y}$ as in previous post, we have the equation

\begin{align}\label{4.6.9}

 &\tilde{Y_p} \,=\, \, \sigma(X_p) \,\,W_p\,\\

 & \,=\, \, \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\,W_p\, \\

& \,=\, \, \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\, \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\,
H_m(Z_W) \right) \, \, \\

& \,=\, \, dh_0\, \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right) \, +\,  \left(\sum\limits_{n=1}^{N}\,
dh_n\, H_n(Z_{X_p}) \right) \,\, \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right) \, \,

 \end{align}

Explaining above equation, part of Y that is orthogonal to X, is described as a product of non-Gaussian zero mean noise
and a function of X denoted as$\sigma(X_p) $ . It is supposed that we do not know the precise Z-series coefficients of
$\sigma(X_p) $ that are given in$ \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right)$ even though we have
complete knowledge of$Z_{X_p}$ for every observation P since we are conditioning on X.

In the previous post, copied from the paper, we have assumed that we know these coefficients and we have given a
regression based method that calculates the coeffiicients of Hermite series of W when coefficients$dh_n$ of the hermite
series of$\sigma(X_p) $ are known.

However in this new post today, we assume that we do not know$dh_n$ with certainty and we also want to find$dh_n$ from
data.

In order to do that we take a reasonable intelligent starting guess of$dh_n$ that are hermit series coefficients of
$\sigma(X_p) $ and we do the regression to find the coefficients of Z-series of W. Now we calculate the R-squared$R^2$
explained by the terms below in the least squares regression to calculate the coefficients of W.

\begin{equation}

 \,  \left(\sum\limits_{n=1}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\, \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\,
H_m(Z_W) \right) \, \,

 \end{equation}

In the above calculation, we have excluded the R-squared $R^2$ explained by zeroth order term below

\begin{equation}

\, dh_0\, \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right) \,

 \end{equation}

We continue to iterate over the coefficients$dh_n$ that are hermit series coefficients of$\sigma(X_p) $ and continue to
re-do the regression and recalculate the coefficients of W and recalculate the R-squared associated with higher order
hermite polynomials terms of$\sigma(X_p) $ . Our true value of$dh_n$ would be the set of coefficients$dh_n$ found from
this iterative optimization that maximizes the R-squared associated with the terms

\begin{equation}

 \,  \left(\sum\limits_{n=1}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\, \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\,
H_m(Z_W) \right) \, \,

 \end{equation}

In practice, we might be fine with calculation of just three values (or third order expansion of$\sigma(X_p) $ ) given
by$dh_1$ ,$dh_2$ and$dh_3$ or at most till fifth order of Hermite-series so this iterative optimization should not be
very difficult. Taking a very high order expansion of$\sigma(X_p) $ would usually be unnecessary.

---

### #2447 — Amin (Topic Author)
*September 15, 2024, 12:58 PM*

Friends, I have been thinking of writing a matlab program with the optimization as mentioned in the previous post.
Because it will nicely conclude one dimensional version of my work. And when we re-start in this winters, we would be
able to start working with multidimensional conditional expected distributions.  So I am thinking of spending 2-3 days
to write an optimization program on above lines and post it on Wilmott during this coming week. really I hope that this
goes well.

As far as data is concerned, I will simulate an SDE till one year, denoted as X  and two years denoted as Y and then
estimate Y|X from the SDE data on the lines as explained in previous post.

---

### #2448 — Amin (Topic Author)
*September 19, 2024, 8:58 AM*

Friends, I have been working quite slowly due to effect of injection since the injection was very bad with huge mind
control chemicals in it. My program for optimization of R^2 is still not complete but I have been thinking of other
ideas to somehow analytically solve for the coefficients of Z-series that are dependent on X in the orthogonal but
dependent part of decorrelated Y.

Once we have found the decorrelated $ \tilde{Y}$ as in previous post, we have the equation

\begin{align}

 &\tilde{Y_p} \,=\, \, \sigma(X_p) \,\,W_p\,\\

 & \,=\, \, \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\,W_p\, \\

& \,=\, \, \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\, \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\,
H_m(Z_W) \right) \, \, \\

 \end{align}

Explaining above equation, part of Y that is orthogonal to X, is described as a product of non-Gaussian zero mean noise
and a function of X denoted as$\sigma(X_p) $ . It is supposed that we do not know the precise Z-series coefficients of
$\sigma(X_p) $ that are given in$ \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right)$ even though we have
complete knowledge of$Z_{X_p}$ for every observation P since we are conditioning on X.

We take square of both sides of the above equation as

\begin{align}

&{\tilde{Y_p}}^2 \,=\, \, \left[ \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\,
\left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right) \, \, \right]^2  \, \\

& \,=\, \, \left[ \sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right]^2 \,\, \left[\sum\limits_{m=1}^{M}\,
\tilde{ch}_m\, H_m(Z_W) \right]^2

\end{align}

We re-write both the summations in RHS of above equation that are being squared and notice after expanding them, the new
coefficients would range from zero to 2N instead of 0 to N and from zero to 2M in other expression in the summations
inside squares. We write second of these expansions as

\begin{equation}

\left[  \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right)  \right]^2 \,=\, \sum\limits_{m=0}^{2M}\,
\bar{ch}_m\, H_m(Z_{W})   \,

\end{equation}

Particularly, we want friends to notice that first coefficient associated with zeroth hermite in above equation would be
equal to expectation of the squared expression or second moment of the respective equation on LHS of above equation
which means that

\begin{equation}

\bar{ch}_0\, = E \left[ \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m \, H_m(Z_{W}) \right)^2  \,\right] \,

\end{equation}

So we can re-write one of the previous equations as

\begin{align}

&{\tilde{Y_p}}^2 \,=\, \, \left[ \sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right]^2 \,\,
\left[\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right]^2 \\

&\,=\, \left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \, \left[\, \sum\limits_{m=0}^{2M}\,
\bar{ch}_m\, H_m(Z_{W})   \,\right]\\

&\,=\, \left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \, \left[\, \bar{ch}_0\, +
\, \sum\limits_{m=1}^{2M}\, \bar{ch}_m\, H_m(Z_{W})   \,\right]\\

&\,=\, \bar{ch}_0\,\left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \,+\, \,\left[ \,
\sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right] \, \,\left[ \, \sum\limits_{m=1}^{2M}\, \bar{ch}_m\,
H_m(Z_{W})   \,\right]

\end{align}

We make the observation that$ \bar{ch}_0\, $ which is equal to expectation of square of W (second moment of W) cannot be
zero. We also notice that since$Z_W$ and$Z_{X_p}$ are both independent, the second term has a zero expectation because
$\left[ \, \sum\limits_{m=1}^{2M}\, \bar{ch}_m\, H_m(Z_{W})   \,\right]$ is all composed of higher hermites each of
which has a zero expectation.

We also notice that there are non-Zero correlations between first 2N Hermite polynomials,$H_n(Z_{X_p})$ and the first
part of above equation given as
$\, \bar{ch}_0\,\left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \, $ and we can find this
correlated part by regressing${\tilde{Y_p}}^2 \,$ which are squares of data values of orthogonal part (orthogonal to
Y|X). If we regress the${\tilde{Y_p}}^2 \,$ data values on first 2N Hermite polynomials of$Z_{X_p}$ we will be able to
find the coefficients$\bar{dh}_n\,$ in Hermite series expression of (these coefficients would be a constant multiple of
true values of coefficients since there is a multiplication by$\bar{ch}_0\, $ )

\begin{equation}

 \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,

\end{equation}

 and that can lead to coefficients of $\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) $ that we wanted to find since

\begin{equation}

 \, \sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p})   \,   \,=\, \sqrt{\left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\,
H_n(Z_{X_p})   \,  \right]}  \

\end{equation}

and we can find this square root on right hand side of above equation using our Taylor series expansion formula.
However, higher coefficients after 3rd or 4th coefficients would be rather approximate due to noise in regressions but I
am sure they would be very informative.

It seems interesting and we realize that a lot of analytics can be done by regressing the square, cube and fourth power
of data values on 2N, 3N and 4N hermites.

---

### #2449 — Amin (Topic Author)
*September 19, 2024, 9:36 AM*

Just to explain one of the ideas in previous post more clearly, Suppose we have a Z-series

\begin{equation}

Y\,=\, \sum\limits_{n=0}^{N} \, ah_n \, H_n(Z)

\end{equation}

if we take its square and want to find

\begin{equation}

Y^2\,=\, \left( \, \sum\limits_{n=0}^{N} \, ah_n \, H_n(Z) \, \right)^2 \, =\, \, \sum\limits_{n=0}^{2N} \, bh_n \,
H_n(Z) \,

\end{equation}

then

\begin{equation}

bh_0\,=\, E \left[ Y^2 \right]\,= \sum\limits_{n=0}^{N} \, {ah_n }^2\, n! \

\end{equation}

which cannot be zero until expectation of second moment is zero as I stated in previous post.

---

### #2450 — Amin (Topic Author)
*September 19, 2024, 7:13 PM*

Friends, I tried to program the above equations but they do not seem to work well apparently. I have been working on
iterative optimization program to  maximize the R-squared. I have coded optimization but a generic technique does not
seem to work well. I will try to improve iterative optimization in next few days and hope to come back with a matlab
working program by Sunday.

---

[← Previous](page_048.md) | [Index](index.md) | [Next →](page_050.md)
