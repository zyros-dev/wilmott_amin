# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 41 of 65** — Posts #2001–#2050

[← Previous](page_040.md) | [Index](index.md) | [Next →](page_042.md)

---

### #2001 — Amin (Topic Author)
*October 8, 2023, 5:29 PM*

Friends, there can still be many other ways to find a two dimensional Z-series/Hermite Series of a bivariate random
variable.

For example if we want a bivariate Z-series/Hermite series of stochastic volatility and asset, in a monte carlo setting,
we can calculate all moments and cross moments up to a certain order(for example till eight order of moments) and then
use a procedure similar to what we devised for calculation of a single dimensional hermite series from its moments. (We
can always calculate 2D density of single asset from the bivariate density of stochastic volatility and asset.)

We can have an initial iterative procedure that would approximately calibrate(just like we did in one dimensional
Z-series) cross moments on appropriate products of hermites and 1D moments on univariate hermites of same order. I am
sure it is very do-able.

However we had a large number of calculations even while calculating moments of single dimensional Z-series and
calculations of 2D hermite series would approximately be roughly a square of the order of effort required for a single
dimensional Z-series. It would be interesting to find a most efficient algorithm that actually calculates all 2D moments
and cross moments for a 2D Z-series and matches it input values of cross moments. If we can do it, I believe this can be
most stable way to deal with the problem that could also tackle dependent and correlated bivariate variables.

Why do we have fast computers of today if we cannot solve these 2D or 3D random variable Z-series calculation problems
on them?

Though we have started work on 2D random variable models, I believe that it will take many more months (possibly up to
six months) for things to become perfectly clear about what is the best approach to tackle 2D random variable models and
find their Z-series and do appropriate analytics like hermite regressions on them.

I am really under pressure these days because my persecution and attempts at drugging my food in the city have sharply
increased in past one week. But I really hope that this problem would settle somewhat in next few weeks. I really want
to be in peace and try to focus on doing good research about the problem of calculation of 2D Z-series in the best and
most reliable way and also be able to do other analytics with the method like hermite regressions and other related
things.

---

### #2002 — Amin (Topic Author)
*October 9, 2023, 5:45 AM*

Friends, even though I do not believe in religion, I am probably still classified by many others as a non-practicing
muslim. I want to tell friends that like most other muslims, I totally condemn violence started by Hamas. In twenty
first century human civilization, there is no place for violence and brutality like this and this should end forever.

But, instead of increasing vicious circle of violence, there have to be serious attempts at bringing both parties in the
middle east conflict on the table. America, Britain and Europeans should force Israel to join the talks as Saudi Arabia
and Qatar should force Hamas and other Palestinians to start talks with Israelis (or end funding of Hamas and Al-Fatah
if they do not join the talks. They should also make sure and audit that their funding is only spent on humanitarian and
civilian needs and not on missile programs and also tell Palestinians that all funding will stop in case of any future
violence.)

Present vicious round of violence should make it clear to all the responsible regional and world powers that in order to
end violence forever, there should be a lasting solution to middle east conflict. A solution that is just, fair and
amicable to both parties. If the world powers and regional powers do not play their role and ignore the matter again,
the circle of violence will become even more vicious after it. America and Europeans should force Israel for a
reasonable settlement as Saudi Arabia and Qatar should force Palestinians to accept a reasonable solution to the
problem.

About two decades ago, there was huge activity by world powers to find a settlement of the conflict but later every
major country accepted the status quo and there were just only lukewarm efforts to bring Israelis and Palestinians
together for talks. If the momentum of talks, that was there some two decades ago, had continued, I am sure there would
have been a settlement of the matter and present violence could have been avoided and both Palestinians and Israelis
would have been living with their human dignity intact. Violence and wars have no respect for human dignity.

I would also ask people to not let the middle east violence overshadow our efforts to end cruel mind control in America
and all other countries. As I have explained several times earlier on this forum, my struggle was never against jews at
all. It was only against those people who connive together to bribe American defense in order to retard intelligent
people they do not like and many of those people happen to be jews so I had to mention this.

I totally respect good jews who abhor cruel mind control by the billionaire Godfather of mind control and his rich
cohort and have nothing to do with the activity of the billionaire Godfather and his cohort.

---

### #2003 — Amin (Topic Author)
*October 9, 2023, 1:02 PM*

Friends, weather here in Lahore is better but still warm. However it is not that hot now that it was a month or two ago.
I also have some good coffee so I want to make the most out of my time in terms of trying to do better research.

I noticed whenever data is very noisy, our original method to calculate Z-series from moments becomes non-robust. For
example, I tried it on asset distribution associated with each volatility grid cell but with very poor and non-robust
results. Method works well when we have very well defined precise moments as we find out of analytic solution of SDEs
but when data and resulting moments are very noisy, the method sometimes becomes very poor.

I am trying two other explicit methods to fit the data directly to find its Z-series and I hope these new methods will
be far more robust. I will give details in a few days but I am not working with inner product method for these two new
approaches.

I am a bit excited about the new possibilities and I really hope that my work goes well. As soon as I have more results
and I could verify that the new methods work, I will post the details here on the forum. This is a small diversion from
the earlier research project but it is required to make the project code work smoothly and in a few days, we will
restart the work towards the main research topic but work in this diversion will be very helpful towards that.

Only if I did not have to waste a few hours everyday trying to get good food and water, I would have totally enjoyed
this time to try doing good research.

I will post the details of new methods hopefully in another two days.

---

### #2004 — Amin (Topic Author)
*October 11, 2023, 8:09 AM*

Friends, There is a very huge increase in my persecution and attempts to drug my food in the city over past two weeks.
Both evil jews and corrupt American defense consider me responsible for the awareness in a lot of good people about
their nexus. And both evil jews and corrupt American defense bitterly want to continue their symbiotic relationship and
really want mind control of talented people to continue at all cost. Both are convinced that  they can dupe good
American people to say that they want mind control to end but only want to keep retarding intelligent and talented
people in the future. They consider me an obstacle in their future plans and know that the truth about mind control will
remain in limelight as long as I continue my research and keep posting it on internet.

They either want me to end my research forever or want to somehow keep it away from public. I think they plan to
accomplish this by drugging my food so I lose perfect balance of my brain and then everybody would suggest that I am
having mental problems and I had schizophrenic history so I will be detained again. And the new psychiatric doctor would
suggest that reason for my mental disease is that I am too attached to me research and in order to become mentally
healthy, I must end my research in mathematics.

So this way they would be able to stop my research and the whole thing will go out of limelight and then evil jews and
corrupt American defense would increase mind control slowly again.

Another possibility they have is to let me work full time somewhere so my research would be my employer's property and I
would never post anything after that on wilmott or elsewhere on internet.

I have plans to work in a few months (since I will have to earn money) but I just want to take some consulting work
related to my research in a way that it does not hinder my public research at all.

Bad People who have benefitted from mind control truly want it to continue one way or other and they really think that
it would be difficult as long as I keep posting my research on internet and the whole thing will remain in limelight.
Therefore American defense has hugely increased attempts to drug my food in the city on an unprecedented scale I have
rarely seen before. They are drugging all of food, beverages and water in the city. There is no large brand of water
that is manufacturing good water now. All the big brands are manufacturing drugged bottled water in the city. So I have
to be extremely careful in getting good food and water. There were some beverages and juices that were good but most of
them are turning into drugged juices and beverages now since recently manufactured supply that enters the market is
drugged at manufacturing source.

---

### #2005 — Amin (Topic Author)
*October 11, 2023, 9:51 PM*

Friends, I have been able to get very reasonable estimates of conditional Z-series of asset for every Stochastic
volatility subdivision. The densities found from Z-series coefficients are quite robust, stable and reasonable and seem
good when graphed.

I will give details of the method later but I used a variant of a method that I had earlier posted on this thread
before. I will give details later but briefly the data is first sorted. And then normal density is divided into equal
probability subdivisions equal to number of data members(in our case number of asset paths that fall in a particular
volatility grid.) We call this ideal normal density. From this density, we find the value of Z associated with each
sorted data member. And then the data members  are regressed on values of hermite polynomials found from Z associated
with each data member. I tried to match first four moments of the subdivisions so that moments of our ideal density
match with true normal density. This gives very robust results for noisy data where our original method of finding
Z-series from values of moments fails.

Now I will start working on finding Z-series of each of the eight coefficients of asset across different grid cells of 
of stochastic volatility. And then hermite regress it on stochastic volatility to find a single 2D Z-series from which
we can get a good estimate of conditional value of asset after substituting the value of V in the 2D Z-series. I hope
that the whole work goes well and we would be able to finish it in a few days or possibly in 2-3 weeks.

---

### #2006 — Amin (Topic Author)
*October 13, 2023, 8:02 AM*

Friends, I have been able to write a first prototype program about the conditional density research that works well. In
the new program, I used monte carlo to create generate joint paths of stochastic volatility and asset. Then I divided
the volatility density into forty subdivisions and found conditional density for asset associated with each subdivision.
I, then, found the univariate Z-series of each of these asset densities associated with different volatility grid
points/subdivisions. The coefficients of all of these subdivisions are different and slightly noisy.  These coefficients
can be represented as c0(1:N), c1(1:N), c2(1:N) and so on when there are total N grid points for volatility Then I took
each coefficient across all asset Z-series , for example c0(1:N) and then c1(1:N) and continued to c5(1:N), ( I took
only six coefficients since terminal time was only two years and I thought that 5th order Z-series will suffice for
short maturity.)

Please note that these coefficients of asset Z-series are conditional on stochastic volatility grid. Finally I
constructed a Z-series of each of these six coefficients of asset Z-series as a function of stochastic volatility as

$c_0(Z_v) \, = \, c_{00} \, + \, c_{01} \, Z_v \,+ \, c_{02} \, {Z_v}^2 \, + \, c_{03} \, {Z_v}^3 \, + \, c_{04} \, {Z_v}^4 \, + \, c_{05} \, {Z_v}^5 \,$

$c_1(Z_v) \, = \, c_{10} \, + \, c_{11} \, Z_v \,+ \, c_{12} \, {Z_v}^2 \, + \, c_{13} \, {Z_v}^3 \, + \, c_{14} \, {Z_v}^4 \, + \, c_{15} \, {Z_v}^5 \,$

$c_2(Z_v) \, = \, c_{20} \, + \, c_{21} \, Z_v \,+ \, c_{22} \, {Z_v}^2 \, + \, c_{23} \, {Z_v}^3 \, + \, c_{24} \, {Z_v}^4 \, + \, c_{25} \, {Z_v}^5 \,$

$c_3(Z_v) \, = \, c_{30} \, + \, c_{31} \, Z_v \,+ \, c_{32} \, {Z_v}^2 \, + \, c_{33} \, {Z_v}^3 \, + \, c_{34} \, {Z_v}^4 \, + \, c_{35} \, {Z_v}^5 \,$

$c_4(Z_v) \, = \, c_{40} \, + \, c_{41} \, Z_v \,+ \, c_{42} \, {Z_v}^2 \, + \, c_{43} \, {Z_v}^3 \, + \, c_{44} \, {Z_v}^4 \, + \, c_{45} \, {Z_v}^5 \,$

$c_5(Z_v) \, = \, c_{50} \, + \, c_{51} \, Z_v \,+ \, c_{52} \, {Z_v}^2 \, + \, c_{53} \, {Z_v}^3 \, + \, c_{54} \, {Z_v}^4 \, + \, c_{55} \, {Z_v}^5 \,$

Equations (A) -- parametric form of Z-series coefficients conditional on volatility

Z-series of asset, in stochastic volatility model, conditional on stochastic volatility will then be given as

$X(Z_x,Z_v) \, = \, c_{0}(Z_v) \, + \, c_{1}(Z_v) \, Z_x \,+ \, c_{2}(Z_v) \, {Z_x}^2 \, + \, c_{3}(Z_v) \, {Z_x}^3 \, + \, c_{4}(Z_v) \, {Z_x}^4 \, + \, c_{5}(Z_v) \, {Z_x}^5 \,$

In order to find Z-series of asset conditional on a particular stochastic volatility from Equations (A), we only need to
substitute the value of$Z_v$ associated with that stochastic volatility subdivision on the stochastic volatility grid. I
still have to see if the same algorithm would work for correlated SV models.

Finally, I compared the conditional asset density constructed from original noisy conditional Z-series that was
calculated separately for each of the stochastic volatility grid points with the conditional asset density constructed
from the above smooth universal expansion(after substituting the conditional value of Z_v associated with particular
volatility subdivision in Equations(A)) of each coefficient as given by Equations(A) and found that match between
conditional densities from both Z-series, numerically calculated and parametrically calculated, across all of the
volatility grid points was very good.

I will be posting some graphs showing this comparison later today.

I want to continue making more changes and will post the program at the end of weekend or possibly on Monday.

---

### #2007 — Amin (Topic Author)
*October 13, 2023, 10:56 AM*

Friends, here are some graphs that compare the conditional density of asset generated from individually calculated
Z-series VS a universal analytic Z-series with parameterized coefficients as described in previous post.

The SDE parameters are on the title. In the title, I have also given conditional value of stochastic volatility V and
associated Zv. From this Zv, you can easily tell the value of CDF of SV where the conditional density of asset is
calculated.

You can see that match between both types of graphs is perfect between Zv=-2 to Zv=+2. In the tails, I think analytical
universal Z-series with parameterized coefficients is better. In the next version, I will also add a totally numerically
calculated density for reference as well for comparison.

Here are the graphs.

.

.

.

[![Image](../images/i.postimg.cc/F1tT5Cg6/XConditional-Density01.png)](https://postimg.cc/xNRvLRZG)

[![Image](../images/i.postimg.cc/90wLkHTT/XConditional-Density02.png)](https://postimg.cc/K3F7KV0v)

[![Image](../images/i.postimg.cc/V6V74kSm/XConditional-Density03.png)](https://postimg.cc/phKYLxY6)

[![Image](../images/i.postimg.cc/zBBtngGx/XConditional-Density04.png)](https://postimg.cc/sBk4z1SW)

[![Image](../images/i.postimg.cc/N0QPjVqq/XConditional-Density05.png)](https://postimg.cc/yDrTfL8v)

[![Image](../images/i.postimg.cc/52BR1JrS/XConditional-Density06.png)](https://postimg.cc/yDNPXMsD)

[![Image](../images/i.postimg.cc/RZ5Djhg0/XConditional-Density07.png)](https://postimg.cc/GHKKDLw0)

[![Image](../images/i.postimg.cc/7LXtGVwC/XConditional-Density08.png)](https://postimg.cc/cKgBPfKZ)

[![Image](../images/i.postimg.cc/RVnYsKQ8/XConditional-Density09.png)](https://postimg.cc/yksnWJGX)

[![Image](../images/i.postimg.cc/1RdTrJ6w/XConditional-Density10.png)](https://postimg.cc/pyDq2QsL)

[![Image](../images/i.postimg.cc/mkK5ZgR8/XConditional-Density11.png)](https://postimg.cc/5Qq3n1XC)

[![Image](../images/i.postimg.cc/SRnPpM0n/XConditional-Density12.png)](https://postimg.cc/64NcrTpK)

[![Image](../images/i.postimg.cc/rmnHb9H6/XConditional-Density13.png)](https://postimg.cc/TLbQ5nGQ)

[![Image](../images/i.postimg.cc/1t5TJdJc/XConditional-Density14.png)](https://postimg.cc/qtSj71fz)

[![Image](../images/i.postimg.cc/MGYN0wbp/XConditional-Density15.png)](https://postimg.cc/bGsm8KB7)

[![Image](../images/i.postimg.cc/bvP42rn5/XConditional-Density16.png)](https://postimg.cc/k2jT0nfN)

[![Image](../images/i.postimg.cc/2ShP6h1v/XConditional-Density17.png)](https://postimg.cc/K1c9pKrv)

[![Image](../images/i.postimg.cc/4NrDsBxs/XConditional-Density18.png)](https://postimg.cc/YhznxNFs)

[![Image](../images/i.postimg.cc/Yq455Jkd/XConditional-Density19.png)](https://postimg.cc/JGLYJYsX)

[![Image](../images/i.postimg.cc/NGPhPghy/XConditional-Density20.png)](https://postimg.cc/3WpbkQx7)

[![Image](../images/i.postimg.cc/D0NtWcQQ/XConditional-Density21.png)](https://postimg.cc/64dHgnmT)

[![Image](../images/i.postimg.cc/8cc2PYvP/XConditional-Density22.png)](https://postimg.cc/9w38LJ1v)

[![Image](../images/i.postimg.cc/DZxVhh8M/XConditional-Density23.png)](https://postimg.cc/340fjPjX)

[![Image](../images/i.postimg.cc/3R8MzNJG/XConditional-Density24.png)](https://postimg.cc/f3rg9wdW)

[![Image](../images/i.postimg.cc/3wC5Lm77/XConditional-Density25.png)](https://postimg.cc/SXsvRXJt)

[![Image](../images/i.postimg.cc/g0Pbq4CN/XConditional-Density26.png)](https://postimg.cc/75XRq1Y2)

[![Image](../images/i.postimg.cc/MpB8QgFn/XConditional-Density27.png)](https://postimg.cc/gxG59tdp)

[![Image](../images/i.postimg.cc/7Ydkbqmv/XConditional-Density28.png)](https://postimg.cc/3dX6c5s9)

[![Image](../images/i.postimg.cc/rFKT8DGC/XConditional-Density29.png)](https://postimg.cc/JGVvx42G)

[![Image](../images/i.postimg.cc/SQZqF69x/XConditional-Density30.png)](https://postimg.cc/fk01Y05G)

[![Image](../images/i.postimg.cc/1XYZGSSq/XConditional-Density31.png)](https://postimg.cc/2LvJYPVk)

[![Image](../images/i.postimg.cc/L5spgXcS/XConditional-Density32.png)](https://postimg.cc/BLRydqZ7)

[![Image](../images/i.postimg.cc/P5vdMCPr/XConditional-Density33.png)](https://postimg.cc/mPRxL2Y0)

[![Image](../images/i.postimg.cc/9FMmr829/XConditional-Density34.png)](https://postimg.cc/JtfVFQG7)

[![Image](../images/i.postimg.cc/4NSJt64S/XConditional-Density35.png)](https://postimg.cc/qz2VHC3s)

[![Image](../images/i.postimg.cc/QthssSSH/XConditional-Density36.png)](https://postimg.cc/f321fcGN)

[![Image](../images/i.postimg.cc/FKjm2wyM/XConditional-Density37.png)](https://postimg.cc/NyfWXJPD)

[![Image](../images/i.postimg.cc/gJsp0RB4/XConditional-Density38.png)](https://postimg.cc/wy1Zftzs)

[![Image](../images/i.postimg.cc/7Lvwtq21/XConditional-Density39.png)](https://postimg.cc/XrgRpSxX)

[![Image](../images/i.postimg.cc/KcQccX6F/XConditional-Density40.png)](https://postimg.cc/JtDCKF7d)

---

### #2008 — Amin (Topic Author)
*October 13, 2023, 12:05 PM*

Just to make it easier for friends to find context of SDE parameters in the title of graphs in previous post. The
relevant SDEs are

Volatility and asset SDE equations are

Vt(0)=V0;

dVt=kappaV *(thetaV - Vt )*dt+sigma0 * Vt^gamma * dz1(t)

Xt(0)=X0

dXt=sigma1* Vt^gammaV * Xt^gammaX *dz2(t);

---

### #2009 — Amin (Topic Author)
*October 14, 2023, 8:10 AM*

Friends, I went ahead and tried the graph of bivariate density of Asset and Stochastic volatility(even though it might
not be needed and only density of X might be required)  that we were trying earlier with these new analytic universal
coefficients that are dependent on volatility. And the results are far better. Earlier we were not being able to capture
the shape of graph close to zero but now the shape is properly captured. I have shown the difference of numerical and
analytic densities(which are slightly different very close to zero).

After every 2D graph from numerical density follows a graph with analytic density from similar angle so that viewers can
compare both of them.

.....

.

.

.

.

[![Image](../images/i.postimg.cc/nLZqmj1N/SV2-DDensity04-A.png)](https://postimg.cc/PC3Lsq9M)

[![Image](../images/i.postimg.cc/YqGNBw9D/SV2-DDensity05-A.png)](https://postimg.cc/1fSVD2DD)

.

.

.

[![Image](../images/i.postimg.cc/QdcpVkcp/SV2-DDensity04-B.png)](https://postimg.cc/5XNHRz70)

[![Image](../images/i.postimg.cc/hjD8kzzV/SV2-DDensity05-B.png)](https://postimg.cc/f3P0Xbvb)

[![Image](../images/i.postimg.cc/sDkYV0Gj/SV2-DDensity04-C.png)](https://postimg.cc/jLhwcchm)

[![Image](../images/i.postimg.cc/Zn08qGLR/SV2-DDensity05-C.png)](https://postimg.cc/64J2j1gJ)

[![Image](../images/i.postimg.cc/Y0V1LdXx/SV2-DDensity04-D.png)](https://postimg.cc/tn31LNG1)

[![Image](../images/i.postimg.cc/NMd8BsmS/SV2-DDensity05-D.png)](https://postimg.cc/FdJkxQPV)

[![Image](../images/i.postimg.cc/yNzyTr7Q/SV2-DDensity04-E.png)](https://postimg.cc/68YZWc2n)

[![Image](../images/i.postimg.cc/mrNNpNDb/SV2-DDensity05-E.png)](https://postimg.cc/wtMm7NLP)

[![Image](../images/i.postimg.cc/05HG4N8J/SV2-DDensity06-A.png)](https://postimg.cc/4nVh7sHJ)

.....

.

.

.

[![Image](../images/i.postimg.cc/BvWMVnBC/SV2-DDensity01-B.png)](https://postimg.cc/sMcYBy8B)

[![Image](../images/i.postimg.cc/Z5vwHdpR/SV2-DDensity02-A.png)](https://postimg.cc/9DVPFzx5)

[![Image](../images/i.postimg.cc/XJ4xn1hG/SV2-DDensity01-C.png)](https://postimg.cc/06X7fn9P)

[![Image](../images/i.postimg.cc/7YWBSVCd/SV2-DDensity02-B.png)](https://postimg.cc/VdXB8XWW)

.

.

.

[![Image](../images/i.postimg.cc/SKWDFbZb/SV2-DDensity01-D.png)](https://postimg.cc/Y4C1YZKd)

[![Image](../images/i.postimg.cc/wTvftPBD/SV2-DDensity02-C.png)](https://postimg.cc/xqwyh6Md)

[![Image](../images/i.postimg.cc/2jT9SmCz/SV2-DDensity03.png)](https://postimg.cc/t7ZNBK1f)

---

### #2010 — Amin (Topic Author)
*October 14, 2023, 9:03 PM*

Friends, I might have to be busy tomorrow with family errands so I will post my matlab programs on Monday.

There is a lot of interesting things we can do with the basic work I have done. For example, I just calculated present
distribution of X given the value of volatility. But we could have just equally found the future one or two or three
years ahead distribution of asset given present volatility with exactly the same algorithm.

Next step would be to find the conditional density of asset some years/time ahead given both volatility and asset value
at current/future time.

Just like we found coefficients of Z-series that are dependent on just one variable that is stochastic volatility,
interesting thing would be to parametrize coefficients of a Z-series when the coefficients themselves depend on more
than one variable for example two, three or four possibly correlated variables analogous to coefficients depending upon
several features as we have in machine learning.

But we will have to do a lot of steady work to be able to do that.

---

### #2011 — Amin (Topic Author)
*October 16, 2023, 12:11 PM*

Friends, I will post my matlab files sometime tonight. I am sure friends are already familiar with most of the ideas I
used since I have described them in the thread earlier. However there are some things that I want to describe again even
though I have previously mentioned them.

In the program, I first calculated coefficients of conditional asset Z-series associated with each volatility grid
subdivision separately. And I want to describe its details and other related ideas.

First I transformed the stochastic volatility variable to bessel-like coordinates by using the formula
$W\, = \, V^{(1-\gamma)}$ . I would like to mention that this transformation preserves the probability mass within each
grid cell and also CDF along the grid cells when compared with stochastic volatility variable in original coordinates.
This was done to find a more normal-like grid for our analytics of Z-series calculations. There was no issue since
underlying Z, ($Z_w(n)\, = \, Z_v(n)$ ) would be the same for all of the arbitrary nth grid cells as CDF remains the
same across respective grid cells even after transformation.

First I put together all of the asset paths from monte carlo that lied in a particular stochastic volatility grid
cell/subdivision.

My first approach was to find the moments of asset paths lying in a particular SV grid cell and convert them into
Z-series associated with our original algorithm of calculating Z-series from first seven moments. But it was working
very poorly due to large noise in moments.

I then tried polynomial regression on the values of asset paths lying in a particular grid subdivision. Here I will take
a minute to give friends idea about polynomial regression as I did it.

We know that in a particular monte carlo run, the probability weight associated with each monte carlo path is reciprocal
of total number of monte carlo paths. We could do a polynomial regression (of monte carlo data on first few hermite
polynomials) on a collection of monte carlo paths, if we could associate corresponding values of hermite polynomials to
each of the monte carlo paths. Then we would pair each monte carlo path with set of associated hermite polynomials and
run the regression to find common coefficients of hermite polynomials.

Problem is that hermite polynomials are derived from normal distribution and there is no obvious way to associate
hermite polynomials values with data values of monte carlo paths.

But we can relate them with each other through probability values. As I earlier mentioned that in a particular monte
carlo run, the probability weight associated with each monte carlo path is reciprocal of total number of monte carlo
paths$\frac{1}{N_p}$ . We can divide the normal density into equal probability weight subdivisions with total number of
subdivisions equal to monte carlo paths$ N_p $ and probability of each subdivision equal to probability of each monte
carlo path$\frac{1}{N_p}$ . Suppose the center of each equal probability normal density subdivision is$Z_n$ . Then we
sort all the monte carlo paths and assign each of the data values$X_n$ to hermite polynomials based on$Z_n$ as given by
$H_m(Z_n)$ . So now we are able to pair, for linear regression, the set of polynomial values$H_m(Z_n)$ with each of the
associated data value$X_n$ and run the regression.

Again probability subdivisions in normal density equal in number to monte carlo paths and the probability associated
with each normal density subdivision is equal to probability associated with each monte carlo path. We then relate the
Z_n associated with center of each normal density subdivision with sorted value X_n of the monte carlo data.

I have previously briefly described this procedure earlier in posts 1817, 1818, 1819, 1820 and 1822.

The polynomial regression method was very robust as compared to matching moments method for noisy data. Earlier I was
trying all of this with 7th order Z-series but for the kind of problems I was playing, I noticed that 7th order Z-series
was an overkill and I worked later with 5th order Z-series and robustness further increased with polynomial regression
method. However I never tried moment matching method with 5th order Z-series. And for friends who would want to try very
high volatility for longer periods of time, you may have to actually use a 7th order Z-series for accuracy. But using
7th order Z-series for problems that only require 5th order Z-series causes decrease in robustness of the method.

For polynomial regression, our matrix formulation is

$ X\,=\, H \, \beta \ + \epsilon$

Where X is a N X 1 vector of asset values associated with sorted monte carlo paths in increasing order. Here N is total
number of monte carlo paths that lie in a particular stochastic volatility grid subdivision.

H is a N X (M+1) matrix of hermite polynomials calculated from Z_n associated with nth equal probability subdivision of
normal density in increasing order. M is the order of highest hermite polynomial and 1 is added for a constant
associated with zeroth order hermite polynomial.

$\beta$ is a M+1 X 1  vector of ceoefficient of hermite polynomials in Z-series to be found from regression.

Our hermite Series for the data random variable X, now would be

$ \, X \, = \, \beta_0 \, + \beta_1 \, Z \, + \beta_2 \, H_2(Z)+ \beta_3 \, H_3(Z)+ \beta_4 \, H_4(Z)+ \beta_5 \, H_5(Z)$

Also for reference of friends, I tried to improve the value of Z_n so that moments of the equal probability subdivisions
density match with normal moments since I am trying to use discrete values of Z_n. For paths greater than 100, this is
not a problem at all but for very small number of paths i.e close to twenty paths, this might be a minor issue. Mostly
this is a very slight correction to Z_n values and this correction decreases fast as number of paths increase.

So this is how I was able to generate relatively robust values of numerically calculated Z-series coefficients
associated with each stochastic volatility grid.

I still want to play around with matching moments method since I want to see if in a decreased order Z-series (as I
decreased the Z-series order from seven to five), moment matching method might be competitive with above regression
method but I have to play  with program further to see this.

Again regression method works very well especially as number of monte carlo paths (or data values in a data set)
increase.

In the next post, I will describe how I converted the separate coefficients of above numerically calculated Z-series
into one single analytic universal Z-series for each of the coefficients. However, a robust calculation of individual
numerically calculated Z-series was a pre-requisite for the later method to work well and that is what I have described
in this post.

---

### #2012 — Amin (Topic Author)
*October 16, 2023, 6:50 PM*

**(broken latex: Unbalanced $: 1)**

```latex
Friends, I am posting the matlab programs. These are still tentative and hopefully I will come up with a final version
of the programs in another 3-4 days and then we will move forward to calculations of asset density in future conditional
on asset value and stochastic volatility value at some point in monte carlo all in a parametric form.

Before I post the program, I want to remind the friends that wherever they see these variables in the program, please as
you change parameters of the SDE, change these variables to conservative values. As in below, the maximum domain for
asset is defined as seven and maximum domain for stocahstic volatility is defined as 1.1, these are conservative values
and whenever you change SDE parameters, change these values appropriately. Failure to change these values may
deteriorate the quality of solution. In the present program, these values are

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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random1(1:paths)*1/sqrt(3)*dt^1.5+ ...
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random2(1:paths)*1/sqrt(3)*dt^1.5;

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

[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_nonUGridLS(X,V,paths,NoOfBinsV,MaxCutOffV,gamma);
%The function above finds numerically calculated conditional Z-series coefficietns associated with each volatility grid
cell.
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
    title(sprintf('Conditional V=%.3f,Zv=%.3f,x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
Vm(indexV),Zv(indexV), X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));
    legend({'Conditional Asset density From numerical Z-series','Conditional Asset density From new analytic Coeffs
Z-series'},'Location','northeast')
    xlabel('Asset'), ylabel('Conditional Asset Density')
    display(fprintf('conditional value of stochastic volatility Grid cell for this graph: V=%.3f,Zv=%.3f,SV grid cell
number = %.1f, Total SV Grid Cells=%.1f',Vm(indexV),Zv(indexV),indexV, IndexMaxV));
    str=input("Lok at comparison of numerically calculated conditional asset density and analytic coeffs conditional
asset density plots")
    hold off
end

%Please note that for drawing bivariate density of asset and stochastic volatility, grid parameters have changed from
brom before in below.

NoOfBinsV=150;
NoOfBinsX=150;
MaxCutOffX=7;
MaxCutOffV=1.1;

%[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv]=
Find2DDensityAndCDFFromSimulation_Infiniti(X,V,paths,NoOfBinsX,NoOfBinsV);
[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv,BinSizeX,BinSizeV]=
Find2DDensityAndCDFFromSimulation_Infiniti04(X,V,paths,NoOfBinsX,NoOfBinsV,MaxCutOffX,MaxCutOffV);
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
title(sprintf('Numerical Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and Volatility')

str=input("Look at numerical bivariate density of Asset and Stochastic Volatility")
surf(Xn,Vm,transpose(pXY2D))
title(sprintf('Analytic Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at Analytic density of Asset and Stochastic volatility")
surf(Xn,Vm,transpose(pXY2D-XYProbDensity2D))
title(sprintf('Difference of Analytic and Numerical Density  : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at difference of numerical and analytic densities of Asset and stochastic volatility")

end

```

.

.

.

.

```
function [a0,a,WProbMass,IndexMaxW,Ym,Zy] =
FindConditionalZSeriesXAndZyFromSimulation_nonUGridLS(X,Y,Paths,NoOfBinsW,MaxCutOffY,gamma)

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
%               (d3 *g1 - d1* g3))* (c4 *d2 *g1^2 - c2 *d4* g1^2 - c4* d1* g1* g2 + c1* d4* g1* g2 + c2* d1* g1* g4 -
...
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
function [XYProbDensity2D,XYProbMass2D,XProbMass,YProbMass,IndexMaxX,IndexMaxY,Xn,Ym,Zx,Zy,BinSizeX,BinSizeY] =
Find2DDensityAndCDFFromSimulation_Infiniti04(X,Y,Paths,NoOfBinsX,NoOfBinsY,MaxCutOffX,MaxCutOffY)

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
%Za, We find Zmid=(Za+Zb)/2. We then evaluate Y(Zmid) and if Y  Y(Zmid), we assign the lower band value equal to Zmid as
Za=Zmid. In a
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

### #2013 — Amin (Topic Author)
*October 16, 2023, 7:18 PM*

Friends, I have taken various view comparisons of the 2D analytic and numerical density that you will find when you run
the previous program.

I have used the maximum cutoff values as given in previous post but I think that program solution quality might have
been even better if I chose the cutoff values slightly more conservatively.

And yes, I will follow tomorrow with more posts to explain the rest of the program. This is a tentative version and a
final version of the program will follow in 3-4 days.

.

.

.

[](https://postimg.cc/dD02FS9j)[![Image](../images/i.postimg.cc/dQ248bkp/SV2-DDensity07-A.png)](https://postimg.cc/dD02FS9j)

[![Image](../images/i.postimg.cc/hGX2ThT1/SV2-DDensity08-A.png)](https://postimg.cc/SXpLpSZn)

[![Image](../images/i.postimg.cc/vTshJzj0/SV2-DDensity07-B.png)](https://postimg.cc/phsK8DPj)

[![Image](../images/i.postimg.cc/RZVsCg08/SV2-DDensity08-B.png)](https://postimg.cc/MvNbdbVb)

[![Image](../images/i.postimg.cc/BbBp4Ff4/SV2-DDensity07-C.png)](https://postimg.cc/YLjYxhSs)

[![Image](../images/i.postimg.cc/hPnZ6DRK/SV2-DDensity08-C.png)](https://postimg.cc/14WKNZzd)

[![Image](../images/i.postimg.cc/XJFx1h2Z/SV2-DDensity07-D.png)](https://postimg.cc/7GHgfBrD)

[![Image](../images/i.postimg.cc/pXBctwPz/SV2-DDensity08-D.png)](https://postimg.cc/3ddFXb4x)

[![Image](../images/i.postimg.cc/0NhcfxCR/SV2-DDensity07-E.png)](https://postimg.cc/f3jczGFB)

[![Image](../images/i.postimg.cc/mkfpbRcN/SV2-DDensity08-E.png)](https://postimg.cc/phCJZwJp)

[![Image](../images/i.postimg.cc/Qd46Fc9M/SV2-DDensity09-A.png)](https://postimg.cc/yDRh5gTq)

[![Image](../images/i.postimg.cc/yxmQx5cq/SV2-DDensity09-B.png)](https://postimg.cc/zHfSPxxp)

[![Image](../images/i.postimg.cc/XNdDsZh2/SV2-DDensity09-C.png)](https://postimg.cc/XXN8JvnF)

---

### #2014 — Amin (Topic Author)
*October 17, 2023, 11:58 AM*

In next 3-4 days, I want to try making several significant changes to the present framework that I posted yesterday.

First, I want to try a volatility grid(on which to make conditional asset calculations) that is equiprobable as opposed
to equidistant and see how it goes.

Second, I want to try one dimensional hermite regression in place of the module where I found universal parameters with
inner product. It is likely that nothing will change in one dimension but I want to see how it goes.

I will also play around further and see if I can make any more changes to improve the previous program.

---

### #2015 — Amin (Topic Author)
*October 17, 2023, 8:10 PM*

Friends, I quickly wrote the program that calculates the conditional asset coefficients on an equi-probable volatility
grid. I am posting the program. I also noticed that increasing the resolution of graphs to 500 X 500 helps bring both
numerical and analytical 2D asset-volatility bivariate graphs closer to each other.

I will post final version in 3-4 days and then also add comments to programs and explain things again.

I am posting the new functions.

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
gammaX=.65;
%%%%%%%%`%%%%%
V0=.350;
thetaV=.05;
kappaV=1.250;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.65;
sigma0=.750;

dt=.03125/2;
Tt=64*2;

T=Tt*dt;

%%%%%%%%%%%%%%%%%%%%%%%%5

%rng(29079137, 'twister')
rng(15898837, 'twister')
paths=500000;
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random1(1:paths)*1/sqrt(3)*dt^1.5+ ...
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random2(1:paths)*1/sqrt(3)*dt^1.5;

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

NoOfBinsV=100;
MaxCutOffV=1.750;

[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_EquiProbGridLS(X,V,paths,NoOfBinsV,MaxCutOffV);
%[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_nonUGridLS(X,V,paths,NoOfBinsV,MaxCutOffV,gamma);
%The function above finds numerically calculated conditional Z-series coefficietns associated with each volatility grid
cell.
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
    title(sprintf('Conditional V=%.3f,Zv=%.3f,x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
Vm(indexV),Zv(indexV), X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));
    legend({'Conditional Asset density From numerical Z-series','Conditional Asset density From new analytic Coeffs
Z-series'},'Location','northeast')
    xlabel('Asset'), ylabel('Conditional Asset Density')
    display(fprintf('conditional value of stochastic volatility Grid cell for this graph: V=%.3f,Zv=%.3f,SV grid cell
number = %.1f, Total SV Grid Cells=%.1f',Vm(indexV),Zv(indexV),indexV, IndexMaxV));
    str=input("Lok at comparison of numerically calculated conditional asset density and analytic coeffs conditional
asset density plots")
    hold off
end

%Please note that for drawing bivariate density of asset and stochastic volatility, grid parameters have changed from
brom before in below.

NoOfBinsV=500;
NoOfBinsX=500;
MaxCutOffX=7;
MaxCutOffV=1.75;

%[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv]=
Find2DDensityAndCDFFromSimulation_Infiniti(X,V,paths,NoOfBinsX,NoOfBinsV);
[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv,BinSizeX,BinSizeV]=
Find2DDensityAndCDFFromSimulation_Infiniti04(X,V,paths,NoOfBinsX,NoOfBinsV,MaxCutOffX,MaxCutOffV);
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
title(sprintf('Numerical Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and Volatility')

str=input("Look at numerical bivariate density of Asset and Stochastic Volatility")
surf(Xn,Vm,transpose(pXY2D))
title(sprintf('Analytic Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at Analytic density of Asset and Stochastic volatility")
surf(Xn,Vm,transpose(pXY2D-XYProbDensity2D))
title(sprintf('Difference of Analytic and Numerical Density  : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at difference of numerical and analytic densities of Asset and stochastic volatility")

end

```

.

.

.

.

```
function [a0,a,YProbMass,NoOfBinsW,Ym,Zy] =
FindConditionalZSeriesXAndZyFromSimulation_EquiProbGridLS(X,Y,Paths,NoOfBinsW,MaxCutOffY)

Y(Y>MaxCutOffY)=MaxCutOffY;

[Ys,I]=sort(Y);

A(1)=1;
for nn=2:NoOfBinsW
A(nn)=A(nn-1)+floor(Paths/NoOfBinsW+.5);
B(nn-1)=A(nn)-1;
end
B(NoOfBinsW)=Paths;

A
B
pv(1)=B(1)-A(1)+1;

if(rem(pv(1),2)==0)
    YCDF(1)=((B(1)-A(1))/2+.5)/Paths;
else
    YCDF(1)=((B(1)-A(1))/2+.5)/Paths;
end

for indexW=1:NoOfBinsW

pv(indexW)=B(indexW)-A(indexW)+1;

%pv(indexW)
%size(X(I(A(indexW):B(indexW))))

%str=input("Look at variable sizes");
 %Xv0(1:pv(indexW))=X(I(A(indexW):B(indexW)));
 Xv(1:pv(indexW),indexW)=X(I(A(indexW):B(indexW)));
 Mean(indexW)=sum(Xv(:,indexW))./pv(indexW);
 Xv(:,indexW)=Xv(:,indexW)./Mean(indexW);
 Xv0(1:pv(indexW))=Xv(1:pv(indexW),indexW);

    [a0(indexW),a(:,indexW)] = CalculateZSeriesDensityByIdealMeasureMean05(Xv0);

if(rem(pv(indexW),2)==0)
    Ym(indexW)=Ys(floor((B(indexW)+A(indexW))/2));
    if(indexW>1)
    YCDF(indexW)=YCDF(indexW-1)+((B(indexW)-A(indexW))+1)/Paths;
    end
else

    Ym(indexW)=Ys(B(indexW)+A(indexW))/2+Ys(B(indexW)+A(indexW)+1)/2;
    if(indexW>1)
    YCDF(indexW)=YCDF(indexW-1)+((B(indexW)-A(indexW))+1)/Paths;
    end
end
YProbMass(indexW)=pv(indexW)/Paths;
Zy(indexW)=norminv(YCDF(indexW));

end

YProbMass
Ym
YCDF
Zy

str=input("Look at variables")
% YCDF(1:IndexMaxW)=0;
% Zy(1:IndexMaxW)=0;
% YCDF(1)=WProbMass(1)*.5;
% Zy(1)=norminv(YCDF(1));
% for nn=2:IndexMaxW
%     YCDF(nn)=YCDF(nn-1)+WProbMass(nn-1)*.5+WProbMass(nn)*.5;
%     Zy(nn)=norminv(YCDF(nn));
%     if (Zy(nn)5)
%             Zy(nn)=5;
%     end
% end

% W=Y.^(1-gamma);
%
% hW=maxk(W,3);
% Wmax2=min(hW);
% lW=mink(W,3);
% Wmin2=max(lW);
%
% BinSizeW=(Wmax2-Wmin2)/NoOfBinsW;
% IndexMaxW=floor((Wmax2-Wmin2)/BinSizeW+.5)+1;
% Wm(1:IndexMaxW)=Wmin2+(0:(IndexMaxW-1))*BinSizeW;
%
% Ym(1:IndexMaxW)=(Wm(1:IndexMaxW)).^(1/(1-gamma));
%
%
% WProbMass(1:IndexMaxW)=0;
% pv(1:IndexMaxW)=0;
%
% for p=1:Paths
%
% indexW=real(floor(real(W(p)-Wmin2)/BinSizeW+.5)+1);
%
% if(real(indexW)IndexMaxW)
% indexW=IndexMaxW;
% end
%
% WProbMass(indexW)=WProbMass(indexW)+1/Paths;
%
% pv(indexW)=pv(indexW)+1;
%
% Xv(pv(indexW),indexW)=X(p);
%
% end
% Mean(1:IndexMaxW)=0;
% for indexW=1:IndexMaxW
%    Mean(indexW)=sum(Xv(:,indexW))./pv(indexW);
%    %Mean(indexW)
%    Xv(:,indexW)=Xv(:,indexW)./Mean(indexW);
%
%
%    Xv0=0;
%    Xv0(1:pv(indexW))=Xv(1:pv(indexW),indexW);
%     [a0(indexW),a(:,indexW)] = CalculateZSeriesDensityByIdealMeasureMean05(Xv0);
%
%     %d0=a0(indexW)
%     %d=a(:,indexW)
%
%
% end
%
% %a0
% %a
% % %str=input("Look at coefficients matrix");
%
%
% YCDF(1:IndexMaxW)=0;
% Zy(1:IndexMaxW)=0;
% YCDF(1)=WProbMass(1)*.5;
% Zy(1)=norminv(YCDF(1));
% for nn=2:IndexMaxW
%     YCDF(nn)=YCDF(nn-1)+WProbMass(nn-1)*.5+WProbMass(nn)*.5;
%     Zy(nn)=norminv(YCDF(nn));
%     if (Zy(nn)5)
%             Zy(nn)=5;
%     end
% end

end
```

.

.

.

---

### #2016 — Amin (Topic Author)
*October 18, 2023, 10:08 AM*

Friends, even though 2D analytic bivariate density of asset and volatility might be very different from numerical
density extremely close to zero, I noticed that call prices calculated from the analytic density match well with call
prices calculated directly from monte carlo simulation. I made an array of call strikes from .5 to 2 with a spacing of
.05 and priced all of these calls from 2D analytic density and also directly from monte carlo simulation and compared
all these call prices with both methods. In most of the scenarios, almost all of the call prices from both methods were
within 10 basis points of each other and in many scenarios, all of the analytically calculated call prices were within
5-6 basis points of monte carlo calculated call values.

I will post this updated program with calculation of call prices in a few hours.

---

### #2017 — Amin (Topic Author)
*October 18, 2023, 12:19 PM*

Friends, I am posting the matlab program in which you can specify array of call prices that will be priced by the matlab
program.

I noticed that when volatility increases for gammaX=.95 i.e. lognormal asset, the accuracy deteriorates and I think that
for lognormal asset with very long tails we might need order of hermite polynomials equal to seven instead of five we
currently have. For gammaX smaller than .8, the program seems to work very well.

Here are the altered files.

Even though I have not added comments to files, in the final version, I will add comments to matlab files and explain
most of the ideas in detail.

.

.

.

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
gammaX=.8;
%%%%%%%%`%%%%%
V0=.35;
thetaV=.05;
kappaV=1.250;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.65;
sigma0=.80;

dt=.03125/2;
Tt=64*2;

T=Tt*dt;

%%%%%%%%%%%%%%%%%%%%%%%%5
rng(82139475, 'twister')
%rng(29079137, 'twister')
%rng(15898837, 'twister')
paths=1000000;
V(1:paths)=V0;  %Original process monte carlo.
X(1:paths)=X0;
paths0=paths/2;
paths00=paths/4;
Random1(1:paths00)=0;
Random2(1:paths0)=0;

for tt=1:Tt

Random2=randn(size(Random2));
Random1=randn(size(Random1));
Random1(paths00+1:2*paths00)=-1*Random1(1:paths00);
Random2(paths0+1:2*paths0)=-1*Random2(1:paths0);
Random1(paths0+1:2*paths0)=Random1(1:paths0);
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random1(1:paths)*1/sqrt(3)*dt^1.5+ ...
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random2(1:paths)*1/sqrt(3)*dt^1.5;

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

X(XCallStrikes(nn))
            CallPricesMC(nn)=CallPricesMC(nn)+(X(pp)-CallStrikes(nn))/paths;
        end
    end
end

% tic
% X_s=sort(X);
% toc
% str=input("elapsed time is above");

SVolMeanAnalytic=thetaV+exp(-kappaV*T)*(V0-thetaV)
SVolMean=sum(V(1:paths))/paths
AssetMeanAnalytic=thetaX+exp(-kappaX*T)*(X0-thetaX)
AssetMean=sum(X(1:paths))/paths

NoOfBinsV=100;
MaxCutOffV=12.750;

[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_EquiProbGridLS(X,V,paths,NoOfBinsV,MaxCutOffV);
%[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_nonUGridLS(X,V,paths,NoOfBinsV,MaxCutOffV,gamma);
%The function above finds numerically calculated conditional Z-series coefficietns associated with each volatility grid
cell.
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
    title(sprintf('Conditional V=%.3f,Zv=%.3f,x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
Vm(indexV),Zv(indexV), X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));
    legend({'Conditional Asset density From numerical Z-series','Conditional Asset density From new analytic Coeffs
Z-series'},'Location','northeast')
    xlabel('Asset'), ylabel('Conditional Asset Density')
    display(fprintf('conditional value of stochastic volatility Grid cell for this graph: V=%.3f,Zv=%.3f,SV grid cell
number = %.1f, Total SV Grid Cells=%.1f',Vm(indexV),Zv(indexV),indexV, IndexMaxV));
%    str=input("Lok at comparison of numerically calculated conditional asset density and analytic coeffs conditional
asset density plots")
    hold off
end

%Please note that for drawing bivariate density of asset and stochastic volatility, grid parameters have changed from
brom before in below.

NoOfBinsV=100;
NoOfBinsX=150;
MaxCutOffX=7;
MaxCutOffV=7.75;

%[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv]=
Find2DDensityAndCDFFromSimulation_Infiniti(X,V,paths,NoOfBinsX,NoOfBinsV);
[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv,BinSizeX,BinSizeV]=
Find2DDensityAndCDFFromSimulation_Infiniti04(X,V,paths,NoOfBinsX,NoOfBinsV,MaxCutOffX,MaxCutOffV);
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

surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(XYProbDensity2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Numerical Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and Volatility')

str=input("Look at numerical bivariate density of Asset and Stochastic Volatility")
surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(pXY2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Analytic Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at Analytic density of Asset and Stochastic volatility")
surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(pXY2D(2:NoOfBinsX+1,3:NoOfBinsV+1)-XYProbDensity2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Difference of Analytic and Numerical Density  : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at difference of numerical and analytic densities of Asset and stochastic volatility")

CallStrikes=[.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75]

VolZEquiDistGridSize=1000;
[CallPricesAnalytic]=PriceCallArrayOver2DDensity(Coeff,CallStrikes,VolZEquiDistGridSize);
CallPricesAnalytic
CallPricesMC

str=input("Look at call strikes");

end

```

.

.

.

```
function [CallPrice] = ZSeriesCallIntegrate(Xc,a0,a)

[Zc]=CalculateZgivenXAndZSeriesBisection2C5(Xc,a0,a);

[aH0,aH] = ConvertZCoeffsToHCoeffs(a0,a,5);

CallPrice= (aH0-Xc)*(1-normcdf(Zc))+exp(-.5*Zc^2)/sqrt(2*pi)*(aH(1) + aH(2) *Zc + aH(3)* (Zc^2-1) + aH(4) *(Zc^3 - 3
*Zc) + aH(5) *(Zc^4 -6 * Zc^2 +3));

end

```

.

.

.

```
function [CallPrices]=PriceCallArrayOver2DDensity(Coeff,CallStrikes,VolZEquiDistGridSize)

NoOfCallStrikes=length(CallStrikes);

%dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=VolZEquiDistGridSize;  % No of normal density subdivisions
dNn=(8)/Nn;
NnMid=((1+Nn)/2)*dNn;
Zv(1:Nn)=(((1:Nn)*dNn)-NnMid);
ZProb(1)=normcdf(.5*Zv(1)+.5*Zv(2),0,1)-normcdf(.5*Zv(1)+.5*Zv(2)-dNn,0,1);
ZProb(Nn)=normcdf(.5*Zv(Nn)+.5*Zv(Nn-1)+dNn,0,1)-normcdf(.5*Zv(Nn)+.5*Zv(Nn-1),0,1);
ZProb(2:Nn-1)=normcdf(.5*Zv(2:Nn-1)+.5*Zv(3:Nn),0,1)-normcdf(.5*Zv(2:Nn-1)+.5*Zv(1:Nn-2),0,1);

CallPriceV(1:Nn,1:NoOfCallStrikes)=0;

CallPrices(1:NoOfCallStrikes)=0;

for indexV=1:Nn
       
b0=Coeff(1,1)+Coeff(1,2).*Zv(indexV)+Coeff(1,3).*Zv(indexV).^2+Coeff(1,4).*Zv(indexV).^3+Coeff(1,5).*Zv(indexV).^4+Coeff(1,6).*Zv(indexV).^5;

    for mm=2:6
       
b(mm-1)=Coeff(mm,1)+Coeff(mm,2).*Zv(indexV)+Coeff(mm,3).*Zv(indexV).^2+Coeff(mm,4).*Zv(indexV).^3+Coeff(mm,5).*Zv(indexV).^4+Coeff(mm,6).*Zv(indexV).^5;
    end

    for ll=1:NoOfCallStrikes
        [CallPriceV(indexV,ll)] = ZSeriesCallIntegrate(CallStrikes(ll),b0,b);

        CallPrices(ll)=CallPrices(ll)+CallPriceV(indexV,ll).*ZProb(indexV);
    end
end

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
function [a0,a,YProbMass,NoOfBinsW,Ym,Zy] =
FindConditionalZSeriesXAndZyFromSimulation_EquiProbGridLS(X,Y,Paths,NoOfBinsW,MaxCutOffY)

Y(Y>MaxCutOffY)=MaxCutOffY;

[Ys,I]=sort(Y);

A(1)=1;
for nn=2:NoOfBinsW
A(nn)=A(nn-1)+floor(Paths/NoOfBinsW+.5);
B(nn-1)=A(nn)-1;
end
B(NoOfBinsW)=Paths;

A
B
pv(1)=B(1)-A(1)+1;

if(rem(pv(1),2)==0)
    YCDF(1)=((B(1)-A(1))/2+.5)/Paths;
else
    YCDF(1)=((B(1)-A(1))/2+.5)/Paths;
end

for indexW=1:NoOfBinsW

pv(indexW)=B(indexW)-A(indexW)+1;

%pv(indexW)
%size(X(I(A(indexW):B(indexW))))

%str=input("Look at variable sizes");
 %Xv0(1:pv(indexW))=X(I(A(indexW):B(indexW)));
 Xv(1:pv(indexW),indexW)=X(I(A(indexW):B(indexW)));
 Mean(indexW)=sum(Xv(:,indexW))./pv(indexW);
 Xv(:,indexW)=Xv(:,indexW)./Mean(indexW);
 Xv0(1:pv(indexW))=Xv(1:pv(indexW),indexW);

    [a0(indexW),a(:,indexW)] = CalculateZSeriesDensityByIdealMeasureMean05(Xv0);

if(rem(pv(indexW),2)==0)
    Ym(indexW)=Ys(floor((B(indexW)+A(indexW))/2));
    if(indexW>1)
    YCDF(indexW)=YCDF(indexW-1)+((B(indexW)-A(indexW))+1)/Paths;
    end
else

    Ym(indexW)=Ys(B(indexW)+A(indexW))/2+Ys(B(indexW)+A(indexW)+1)/2;
    if(indexW>1)
    YCDF(indexW)=YCDF(indexW-1)+((B(indexW)-A(indexW))+1)/Paths;
    end
end
YProbMass(indexW)=pv(indexW)/Paths;
Zy(indexW)=norminv(YCDF(indexW));

end

YProbMass
Ym
YCDF
Zy

str=input("Look at variables")
% YCDF(1:IndexMaxW)=0;
% Zy(1:IndexMaxW)=0;
% YCDF(1)=WProbMass(1)*.5;
% Zy(1)=norminv(YCDF(1));
% for nn=2:IndexMaxW
%     YCDF(nn)=YCDF(nn-1)+WProbMass(nn-1)*.5+WProbMass(nn)*.5;
%     Zy(nn)=norminv(YCDF(nn));
%     if (Zy(nn)5)
%             Zy(nn)=5;
%     end
% end

% W=Y.^(1-gamma);
%
% hW=maxk(W,3);
% Wmax2=min(hW);
% lW=mink(W,3);
% Wmin2=max(lW);
%
% BinSizeW=(Wmax2-Wmin2)/NoOfBinsW;
% IndexMaxW=floor((Wmax2-Wmin2)/BinSizeW+.5)+1;
% Wm(1:IndexMaxW)=Wmin2+(0:(IndexMaxW-1))*BinSizeW;
%
% Ym(1:IndexMaxW)=(Wm(1:IndexMaxW)).^(1/(1-gamma));
%
%
% WProbMass(1:IndexMaxW)=0;
% pv(1:IndexMaxW)=0;
%
% for p=1:Paths
%
% indexW=real(floor(real(W(p)-Wmin2)/BinSizeW+.5)+1);
%
% if(real(indexW)IndexMaxW)
% indexW=IndexMaxW;
% end
%
% WProbMass(indexW)=WProbMass(indexW)+1/Paths;
%
% pv(indexW)=pv(indexW)+1;
%
% Xv(pv(indexW),indexW)=X(p);
%
% end
% Mean(1:IndexMaxW)=0;
% for indexW=1:IndexMaxW
%    Mean(indexW)=sum(Xv(:,indexW))./pv(indexW);
%    %Mean(indexW)
%    Xv(:,indexW)=Xv(:,indexW)./Mean(indexW);
%
%
%    Xv0=0;
%    Xv0(1:pv(indexW))=Xv(1:pv(indexW),indexW);
%     [a0(indexW),a(:,indexW)] = CalculateZSeriesDensityByIdealMeasureMean05(Xv0);
%
%     %d0=a0(indexW)
%     %d=a(:,indexW)
%
%
% end
%
% %a0
% %a
% % %str=input("Look at coefficients matrix");
%
%
% YCDF(1:IndexMaxW)=0;
% Zy(1:IndexMaxW)=0;
% YCDF(1)=WProbMass(1)*.5;
% Zy(1)=norminv(YCDF(1));
% for nn=2:IndexMaxW
%     YCDF(nn)=YCDF(nn-1)+WProbMass(nn-1)*.5+WProbMass(nn)*.5;
%     Zy(nn)=norminv(YCDF(nn));
%     if (Zy(nn)5)
%             Zy(nn)=5;
%     end
% end

end
```

.

.

.

Here is the comparison of analytic call prices and Monte carlo simulation call prices that you will see when you run the
above program. SDE parameters are on the title of the 2D graph at end.

CallStrikes =

  Columns 1 through 3

   0.500000000000000   0.550000000000000   0.600000000000000

  Columns 4 through 6

   0.650000000000000   0.700000000000000   0.750000000000000

  Columns 7 through 9

   0.800000000000000   0.850000000000000   0.900000000000000

  Columns 10 through 12

   0.950000000000000   1.000000000000000   1.050000000000000

  Columns 13 through 15

   1.100000000000000   1.150000000000000   1.200000000000000

  Columns 16 through 18

   1.250000000000000   1.300000000000000   1.350000000000000

  Columns 19 through 21

   1.400000000000000   1.450000000000000   1.500000000000000

  Columns 22 through 24

   1.550000000000000   1.600000000000000   1.650000000000000

  Columns 25 through 26

   1.700000000000000   1.750000000000000

CallPricesAnalytic =

  Columns 1 through 3

   0.527883365794628   0.487002461218819   0.447969541414900

  Columns 4 through 6

   0.410911743545700   0.375931287050620   0.343102775586519

  Columns 7 through 9

   0.312471374140007   0.284052013860412   0.257829732813468

  Columns 10 through 12

   0.233761191015051   0.211777307544795   0.191786867175371

  Columns 13 through 15

   0.173680850162253   0.157337170096963   0.142625476247140

  Columns 16 through 18

   0.129411695229882   0.117562047552884   0.106946363025822

  Columns 19 through 21

   0.097440615951800   0.088928688322802   0.081303434879621

  Columns 22 through 24

   0.074467163354371   0.068331658429161   0.062817874675705

  Columns 25 through 26

   0.057855408887038   0.053381841930145

CallPricesMC =

  Columns 1 through 3

   0.527285528775324   0.486207754942085   0.446982550396558

  Columns 4 through 6

   0.409761856984464   0.374664895711768   0.341783698041079

  Columns 7 through 9

   0.311172785386904   0.282839639406455   0.256754343334394

  Columns 10 through 12

   0.232866870771368   0.211075557568832   0.191281961431987

  Columns 13 through 15

   0.173364492396926   0.157187090549631   0.142614641400151

  Columns 16 through 18

   0.129495915068427   0.117693902594023   0.107088452648265

  Columns 19 through 21

   0.097559995377762   0.088999247384665   0.081306449216455

  Columns 22 through 24

   0.074381527240031   0.068144989262120   0.062529756856655

  Columns 25 through 26

   0.057464515761093   0.052891676314255

Here is a view of 2D graph of the analytic density from above program.

[![Image](../images/i.postimg.cc/nzPdPdwy/SV2-DDensity10-A.png)](https://postimg.cc/2bnFqxYG)

---

### #2018 — Amin (Topic Author)
*October 18, 2023, 7:14 PM*

Friends, sorry for quickly posting corrections. I improved the function that calculates call prices and made minor
changes to main function. Here is the new matlab program. It will also work quite better for lognormal-like asset at
gammaX=.95

.

.

.

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
gammaX=.75;
%%%%%%%%`%%%%%
V0=.45;
thetaV=.05;
kappaV=1.30;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.65;
sigma0=.90;

dt=.03125/2;
Tt=64*2;

T=Tt*dt;

%%%%%%%%%%%%%%%%%%%%%%%%5
rng(82139475, 'twister')
%rng(29079137, 'twister')
%rng(15898837, 'twister')
paths=500000;
V(1:paths)=V0;  %Original process monte carlo.
X(1:paths)=X0;
paths0=paths/2;
paths00=paths/4;
Random1(1:paths00)=0;
Random2(1:paths0)=0;

for tt=1:Tt

Random2=randn(size(Random2));
Random1=randn(size(Random1));
Random1(paths00+1:2*paths00)=-1*Random1(1:paths00);
Random2(paths0+1:2*paths0)=-1*Random2(1:paths0);
Random1(paths0+1:2*paths0)=Random1(1:paths0);
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random1(1:paths)*1/sqrt(3)*dt^1.5+ ...
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random2(1:paths)*1/sqrt(3)*dt^1.5;

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

X(XCallStrikes(nn))
            CallPricesMC(nn)=CallPricesMC(nn)+(X(pp)-CallStrikes(nn))/paths;
        end
    end
end

% tic
% X_s=sort(X);
% toc
% str=input("elapsed time is above");

SVolMeanAnalytic=thetaV+exp(-kappaV*T)*(V0-thetaV)
SVolMean=sum(V(1:paths))/paths
AssetMeanAnalytic=thetaX+exp(-kappaX*T)*(X0-thetaX)
AssetMean=sum(X(1:paths))/paths

NoOfBinsV=100;
MaxCutOffV=12.750;

[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_EquiProbGridLS(X,V,paths,NoOfBinsV,MaxCutOffV);
%[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_nonUGridLS(X,V,paths,NoOfBinsV,MaxCutOffV,gamma);
%The function above finds numerically calculated conditional Z-series coefficietns associated with each volatility grid
cell.
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

    [Zc]=CalculateZgivenXAndZSeriesBisection2C5(0,b0,b);

    [aH0,aH] = ConvertZCoeffsToHCoeffs(b0,b,5);

    MeanXv(indexV)= (aH0)*(1-normcdf(Zc))+exp(-.5*Zc^2)/sqrt(2*pi)*(aH(1) + aH(2) *Zc + aH(3)* (Zc^2-1) + aH(4) *(Zc^3 -
3 *Zc) + aH(5) *(Zc^4 -6 * Zc^2 +3));

    b0=b0/MeanXv(indexV);
    b=b/MeanXv(indexV);

    [Zc]=CalculateZgivenXAndZSeriesBisection2C5(0,b0,b);

    [aH0,aH] = ConvertZCoeffsToHCoeffs(b0,b,5);

    MeanXvCorrected(indexV)= (aH0)*(1-normcdf(Zc))+exp(-.5*Zc^2)/sqrt(2*pi)*(aH(1) + aH(2) *Zc + aH(3)* (Zc^2-1) + aH(4)
*(Zc^3 - 3 *Zc) + aH(5) *(Zc^4 -6 * Zc^2 +3));

    PlotZSeriesDensity(b0,b,'r');
    title(sprintf('Conditional V=%.3f,Zv=%.3f,x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
Vm(indexV),Zv(indexV), X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));
    legend({'Conditional Asset density From numerical Z-series','Conditional Asset density From new analytic Coeffs
Z-series'},'Location','northeast')
    xlabel('Asset'), ylabel('Conditional Asset Density')
    display(fprintf('conditional value of stochastic volatility Grid cell for this graph: V=%.3f,Zv=%.3f,SV grid cell
number = %.1f, Total SV Grid Cells=%.1f',Vm(indexV),Zv(indexV),indexV, IndexMaxV));
    %str=input("Lok at comparison of numerically calculated conditional asset density and analytic coeffs conditional
asset density plots")
    hold off
end

MeanXv

MeanXvCorrected
str=input("Look at meanA");

%Please note that for drawing bivariate density of asset and stochastic volatility, grid parameters have changed from
brom before in below.

NoOfBinsV=100;
NoOfBinsX=150;
MaxCutOffX=7;
MaxCutOffV=7.75;

%[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv]=
Find2DDensityAndCDFFromSimulation_Infiniti(X,V,paths,NoOfBinsX,NoOfBinsV);
[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv,BinSizeX,BinSizeV]=
Find2DDensityAndCDFFromSimulation_Infiniti04(X,V,paths,NoOfBinsX,NoOfBinsV,MaxCutOffX,MaxCutOffV);
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

surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(XYProbDensity2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Numerical Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and Volatility')

str=input("Look at numerical bivariate density of Asset and Stochastic Volatility")
surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(pXY2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Analytic Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at Analytic density of Asset and Stochastic volatility")
surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(pXY2D(2:NoOfBinsX+1,3:NoOfBinsV+1)-XYProbDensity2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Difference of Analytic and Numerical Density  : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at difference of numerical and analytic densities of Asset and stochastic volatility")

CallStrikes=[.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75]

VolZEquiDistGridSize=200;
[CallPricesAnalytic]=PriceCallArrayOver2DDensity(a0,a,Coeff,CallStrikes,VolZEquiDistGridSize);
CallPricesAnalytic
CallPricesMC

str=input("Look at comparison of analytic and monte carlo call prices");

end

```

.

.

.

```
function [CallPrices]=PriceCallArrayOver2DDensity(a0,a,Coeff,CallStrikes,VolZEquiDistGridSize)

NoOfCallStrikes=length(CallStrikes);

%dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=VolZEquiDistGridSize;  % No of normal density subdivisions
dNn=(8)/Nn;
NnMid=((1+Nn)/2)*dNn;
Zv(1:Nn)=(((1:Nn)*dNn)-NnMid);
ZProb(1)=normcdf(.5*Zv(1)+.5*Zv(2),0,1)-normcdf(.5*Zv(1)+.5*Zv(2)-dNn,0,1);
ZProb(Nn)=normcdf(.5*Zv(Nn)+.5*Zv(Nn-1)+dNn,0,1)-normcdf(.5*Zv(Nn)+.5*Zv(Nn-1),0,1);
ZProb(2:Nn-1)=normcdf(.5*Zv(2:Nn-1)+.5*Zv(3:Nn),0,1)-normcdf(.5*Zv(2:Nn-1)+.5*Zv(1:Nn-2),0,1);

%ZProb(3:Nn)=ZProb(3:Nn).*1./sum(ZProb(3:Nn));

CallPriceV(1:Nn,1:NoOfCallStrikes)=0;

CallPrices(1:NoOfCallStrikes)=0;

for indexV=13:Nn-12

    V(indexV)=a0 + a(1)*Zv(indexV)+a(2)*Zv(indexV).^2+a(3).*Zv(indexV).^3+a(4).*Zv(indexV).^4+a(5).*Zv(indexV).^5;

       
b0=Coeff(1,1)+Coeff(1,2).*Zv(indexV)+Coeff(1,3).*Zv(indexV).^2+Coeff(1,4).*Zv(indexV).^3+Coeff(1,5).*Zv(indexV).^4+Coeff(1,6).*Zv(indexV).^5;

    for mm=2:6
       
b(mm-1)=Coeff(mm,1)+Coeff(mm,2).*Zv(indexV)+Coeff(mm,3).*Zv(indexV).^2+Coeff(mm,4).*Zv(indexV).^3+Coeff(mm,5).*Zv(indexV).^4+Coeff(mm,6).*Zv(indexV).^5;
    end
    %if(V(indexV)>0)
    [Zc]=CalculateZgivenXAndZSeriesBisection2C5(0,b0,b);

    [aH0,aH] = ConvertZCoeffsToHCoeffs(b0,b,5);

    MeanXv(indexV)= (aH0)*(1-normcdf(Zc))+exp(-.5*Zc^2)/sqrt(2*pi)*(aH(1) + aH(2) *Zc + aH(3)* (Zc^2-1) + aH(4) *(Zc^3 -
3 *Zc) + aH(5) *(Zc^4 -6 * Zc^2 +3));

    b0=b0/MeanXv(indexV);
    b=b/MeanXv(indexV);
    %end
    for ll=1:NoOfCallStrikes
        [CallPriceV(indexV,ll)] = ZSeriesCallIntegrate(CallStrikes(ll),b0,b);

    end

end
for ss=1:12
CallPriceV(ss,:)=CallPriceV(13,:);
CallPriceV(Nn-ss+1,:)=CallPriceV(Nn-12,:);
end
for indexV=1:Nn
    for ll=1:NoOfCallStrikes
        CallPrices(ll)=CallPrices(ll)+CallPriceV(indexV,ll).*ZProb(indexV);
    end
end

%CallPriceV
%str=input("Look at conditional call prices");

end

```

.

.

.

Here is the comparison of analytic and monte carlo call prices. SDE parameters are on the title of analytic calculated
2D density graph at the end.

CallStrikes =

  Columns 1 through 3

   0.500000000000000   0.550000000000000   0.600000000000000

  Columns 4 through 6

   0.650000000000000   0.700000000000000   0.750000000000000

  Columns 7 through 9

   0.800000000000000   0.850000000000000   0.900000000000000

  Columns 10 through 12

   0.950000000000000   1.000000000000000   1.050000000000000

  Columns 13 through 15

   1.100000000000000   1.150000000000000   1.200000000000000

  Columns 16 through 18

   1.250000000000000   1.300000000000000   1.350000000000000

  Columns 19 through 21

   1.400000000000000   1.450000000000000   1.500000000000000

  Columns 22 through 24

   1.550000000000000   1.600000000000000   1.650000000000000

  Columns 25 through 26

   1.700000000000000   1.750000000000000

CallPricesAnalytic =

  Columns 1 through 3

   0.536013731329159   0.496587187995463   0.458960654896129

  Columns 4 through 6

   0.423221905535930   0.389439229724963   0.357660101227713

  Columns 7 through 9

   0.327910283413016   0.300193464578145   0.274491499825151

  Columns 10 through 12

   0.250765309495295   0.228956445012633   0.208989283780107

  Columns 13 through 15

   0.190773760619019   0.174208491907820   0.159184109199259

  Columns 16 through 18

   0.145586599948308   0.133300458895875   0.122211484138150

  Columns 19 through 21

   0.112209100942308   0.103188154087098   0.095050165203508

  Columns 22 through 24

   0.087704096699275   0.081066693764112   0.075062490209328

  Columns 25 through 26

   0.069623565087539   0.064689129214114

CallPricesMC =

  Columns 1 through 3

   0.535631211240854   0.495935459274159   0.458086378266836

  Columns 4 through 6

   0.422178008589087   0.388295315479440   0.356494427154874

  Columns 7 through 9

   0.326790720534522   0.299192115769936   0.273660602687130

  Columns 10 through 12

   0.250149246300219   0.228554109786635   0.208786699057258

  Columns 13 through 15

   0.190763676264744   0.174359545099666   0.159452984159071

  Columns 16 through 18

   0.145923174698511   0.133651544064735   0.122524284216094

  Columns 19 through 21

   0.112451928646934   0.103316147845992   0.095046765154701

  Columns 22 through 24

   0.087555625800229   0.080763278930076   0.074602752992153

  Columns 25 through 26

   0.069007126364816   0.063910664809116

Look at comparison of analytic and monte carlo call prices

.

.

.

[![Image](../images/i.postimg.cc/R0hRkkJg/SV2-DDensity11-A.png)](https://postimg.cc/06gDmHfS)

---

### #2019 — Amin (Topic Author)
*October 20, 2023, 6:59 AM*

Friends, the actual purpose of our research exercise was to find conditional values of asset based on volatility with
one set of Coefficients(or  Coeffs derived from their own Z-series Coeffs). I noticed that without mean correction, my
algorithm for finding conditional values of asset is not very good especially for applications like mathematical finance
that require a good deal of precision.

I tried to re-do the old algorithm (finding coefficients by inner product) with a different regression-based method and
was amazed to find that without mean correction, the mean is only off between 0-25 bps off the true value of one as
opposed to 0-250 bps for previous inner product coefficients calculation algorithm that I have earlier distributed in my
programs. And even this small bias is totally systematic and due to density going into negative territory. Once the
density in positive territory is normalized to keep the mean in positive territory equal to one, the algorithm works
extremely well.

I will post the new program in a few hours. I am sure that friends who might have been slightly disappointed by
inaccuracies in the previous program to find conditional values of asset dependent on volatility would really like this
new version and it can easily be used in math finance applications.

This is important to keep our basics right since we want to extend the present rudimentary work to more sophisticated
applications as the research progresses.

I am also working on a density correction algorithm that would take a density that goes into negative territory and fix
it so that both the density mass in positive territory is unity and the mean of the corrected density also matches the
known analytic mean. This approach locally corrects the mean and density in area close to zero since this is where the
density is most distorted (when probability mass goes to zero) without unduly affecting right tail of density which
might be already good. I have written the equations for this density correction but it may be several days before I
could write a perfectly working algorithm for this. I really wanted to write such a small program especially when I was
working on analytic simulation of density of SDEs since many times when the density goes into negative territory the
whole simulation becomes more and more off so this new routine would be useful there as well.

I will be posting the new matlab program with improved version of the conditional asset density calculation program in a
few hours.

---

### #2020 — Amin (Topic Author)
*October 20, 2023, 12:36 PM*

Friends, here are the new version of matlab program files.

.

.

.

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
gammaX=.65;
%%%%%%%%`%%%%%
V0=.45;
thetaV=.05;
kappaV=1.50;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.5;
sigma0=.95;

dt=.03125/2;
Tt=64*2;

T=Tt*dt;

%%%%%%%%%%%%%%%%%%%%%%%%5
rng(82139475, 'twister')
%rng(29079137, 'twister')
%rng(15898837, 'twister')
paths=500000;
V(1:paths)=V0;  %Original process monte carlo.
X(1:paths)=X0;
paths0=paths/2;
paths00=paths/4;
Random1(1:paths00)=0;
Random2(1:paths0)=0;

for tt=1:Tt

Random2=randn(size(Random2));
Random1=randn(size(Random1));
Random1(paths00+1:2*paths00)=-1*Random1(1:paths00);
Random2(paths0+1:2*paths0)=-1*Random2(1:paths0);
Random1(paths0+1:2*paths0)=Random1(1:paths0);
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random1(1:paths)*1/sqrt(3)*dt^1.5+ ...
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random2(1:paths)*1/sqrt(3)*dt^1.5;

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

X(XCallStrikes(nn))
            CallPricesMC(nn)=CallPricesMC(nn)+(X(pp)-CallStrikes(nn))/paths;
        end
    end
end

% tic
% X_s=sort(X);
% toc
% str=input("elapsed time is above");

SVolMeanAnalytic=thetaV+exp(-kappaV*T)*(V0-thetaV)
SVolMean=sum(V(1:paths))/paths
AssetMeanAnalytic=thetaX+exp(-kappaX*T)*(X0-thetaX)
AssetMean=sum(X(1:paths))/paths

NoOfBinsV=100;
MaxCutOffV=12.750;

[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_EquiProbGridLS(X,V,paths,NoOfBinsV,MaxCutOffV);
%[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_nonUGridLS(X,V,paths,NoOfBinsV,MaxCutOffV,gamma);
%The function above finds numerically calculated conditional Z-series coefficietns associated with each volatility grid
cell.
%aa0 is zeroth coefficient/median array while aa is a matrix of (5 X NoOfBins+1) coeffs.

%The series of functions below take each coefficient array and convert it
%to a Z_series of analytic coeffs dependent on Zv. I will explain this
%further in a separate post on wilmott.
 [Coeff(1,1),Coeff(1,2:6)] = FindZSeriesCoeffsByInnerProduct(aa0,Zv,VProbMass,IndexMaxV)
%
 [CoeffA(1,1),CoeffA(1,2:6)]= FindZSeriesCoeffsOfCoeffs(aa0,Zv,VProbMass,IndexMaxV)
%
% Coeff(1,1)
% c0
% Coeff(1,2:6)
% c
% str=input("Look at comparison of Coeffs");
 [Coeff(2,1),Coeff(2,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(1,:),Zv,VProbMass,IndexMaxV);

[CoeffA(2,1),CoeffA(2,2:6)] = FindZSeriesCoeffsOfCoeffs(aa(1,:),Zv,VProbMass,IndexMaxV)

 [Coeff(3,1),Coeff(3,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(2,:),Zv,VProbMass,IndexMaxV);
[CoeffA(3,1),CoeffA(3,2:6)] = FindZSeriesCoeffsOfCoeffs(aa(2,:),Zv,VProbMass,IndexMaxV)

[Coeff(4,1),Coeff(4,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(3,:),Zv,VProbMass,IndexMaxV);
[CoeffA(4,1),CoeffA(4,2:6)] = FindZSeriesCoeffsOfCoeffs(aa(3,:),Zv,VProbMass,IndexMaxV)

[Coeff(5,1),Coeff(5,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(4,:),Zv,VProbMass,IndexMaxV);
[CoeffA(5,1),CoeffA(5,2:6)] = FindZSeriesCoeffsOfCoeffs(aa(4,:),Zv,VProbMass,IndexMaxV)

[Coeff(6,1),Coeff(6,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(5,:),Zv,VProbMass,IndexMaxV);
[CoeffA(6,1),CoeffA(6,2:6)] = FindZSeriesCoeffsOfCoeffs(aa(5,:),Zv,VProbMass,IndexMaxV)

% [Coeff(1,1),Coeff(1,2:6)]= FindZSeriesCoeffsOfCoeffs(aa0,Zv,VProbMass,IndexMaxV)
% [Coeff(2,1),Coeff(2,2:6)] = FindZSeriesCoeffsOfCoeffs(aa(1,:),Zv,VProbMass,IndexMaxV)
% [Coeff(3,1),Coeff(3,2:6)] = FindZSeriesCoeffsOfCoeffs(aa(2,:),Zv,VProbMass,IndexMaxV)
% [Coeff(4,1),Coeff(4,2:6)] = FindZSeriesCoeffsOfCoeffs(aa(3,:),Zv,VProbMass,IndexMaxV)
% [Coeff(5,1),Coeff(5,2:6)] = FindZSeriesCoeffsOfCoeffs(aa(4,:),Zv,VProbMass,IndexMaxV)
% [Coeff(6,1),Coeff(6,2:6)] = FindZSeriesCoeffsOfCoeffs(aa(5,:),Zv,VProbMass,IndexMaxV)
% %[Coeff(6,1),Coeff(6,2:6)] = FindZSeriesCoeffsByInnerProduct(aa(5,:),Zv,VProbMass,IndexMaxV);

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
   
d0=CoeffA(1,1)+CoeffA(1,2).*Zv(indexV)+CoeffA(1,3).*Zv(indexV).^2+CoeffA(1,4).*Zv(indexV).^3+CoeffA(1,5).*Zv(indexV).^4+CoeffA(1,6).*Zv(indexV).^5;

    for mm=2:6
       
b(mm-1)=Coeff(mm,1)+Coeff(mm,2).*Zv(indexV)+Coeff(mm,3).*Zv(indexV).^2+Coeff(mm,4).*Zv(indexV).^3+Coeff(mm,5).*Zv(indexV).^4+Coeff(mm,6).*Zv(indexV).^5;
       
d(mm-1)=CoeffA(mm,1)+CoeffA(mm,2).*Zv(indexV)+CoeffA(mm,3).*Zv(indexV).^2+CoeffA(mm,4).*Zv(indexV).^3+CoeffA(mm,5).*Zv(indexV).^4+CoeffA(mm,6).*Zv(indexV).^5;
    end

    [Zc]=CalculateZgivenXAndZSeriesBisection2C5(0,b0,b);
    [Zd]=CalculateZgivenXAndZSeriesBisection2C5(0,d0,d);

    [aH0,aH] = ConvertZCoeffsToHCoeffs(b0,b,5);
    [dH0,dH] = ConvertZCoeffsToHCoeffs(d0,d,5);

    MeanXv(indexV)= (aH0)*(1-normcdf(Zc))+exp(-.5*Zc^2)/sqrt(2*pi)*(aH(1) + aH(2) *Zc + aH(3)* (Zc^2-1) + aH(4) *(Zc^3 -
3 *Zc) + aH(5) *(Zc^4 -6 * Zc^2 +3))
    MeanXvd(indexV)= (dH0)*(1-normcdf(Zd))+exp(-.5*Zd^2)/sqrt(2*pi)*(dH(1) + dH(2) *Zd + dH(3)* (Zd^2-1) + dH(4) *(Zd^3
- 3 *Zd) + dH(5) *(Zd^4 -6 * Zd^2 +3))

    aH0
    dH0

    b0=b0/MeanXv(indexV);
    b=b/MeanXv(indexV);

    d0=d0/MeanXvd(indexV);
    d=d/MeanXvd(indexV);

%     [Zc]=CalculateZgivenXAndZSeriesBisection2C5(0,b0,b);
%
%     [aH0,aH] = ConvertZCoeffsToHCoeffs(b0,b,5);
%
%     MeanXvCorrected(indexV)= (aH0)*(1-normcdf(Zc))+exp(-.5*Zc^2)/sqrt(2*pi)*(aH(1) + aH(2) *Zc + aH(3)* (Zc^2-1) +
aH(4) *(Zc^3 - 3 *Zc) + aH(5) *(Zc^4 -6 * Zc^2 +3));

    PlotZSeriesDensity(b0,b,'r');
    hold on
    PlotZSeriesDensity(d0,d,'b');
    title(sprintf('Conditional V=%.3f,Zv=%.3f,x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
Vm(indexV),Zv(indexV), X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));
    legend({'Conditional Asset density From numerical Z-series','Conditional Asset density From new analytic Coeffs
Z-series'},'Location','northeast')
    xlabel('Asset'), ylabel('Conditional Asset Density')
    display(fprintf('conditional value of stochastic volatility Grid cell for this graph: V=%.3f,Zv=%.3f,SV grid cell
number = %.1f, Total SV Grid Cells=%.1f',Vm(indexV),Zv(indexV),indexV, IndexMaxV));
    str=input("Lok at comparison of numerically calculated conditional asset density and analytic coeffs conditional
asset density plots")
    hold off
end

MeanXv

%MeanXvCorrected
str=input("Look at meanA");

%Please note that for drawing bivariate density of asset and stochastic volatility, grid parameters have changed from
brom before in below.

NoOfBinsV=100;
NoOfBinsX=150;
MaxCutOffX=7;
MaxCutOffV=7.75;

%[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv]=
Find2DDensityAndCDFFromSimulation_Infiniti(X,V,paths,NoOfBinsX,NoOfBinsV);
[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv,BinSizeX,BinSizeV]=
Find2DDensityAndCDFFromSimulation_Infiniti04(X,V,paths,NoOfBinsX,NoOfBinsV,MaxCutOffX,MaxCutOffV);
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

[pXY2D] = Calculate2VariablesOn2DGridFromAnalyticZSeries(Xn,Vm,NoOfBinsX,NoOfBinsV,CoeffA,a0,a);
%[pXY2D] = Calculate2VariablesOn2DGridFromAnalyticZSeries(XX,YY,NoOfBinsX,NoOfBinsY,Coeff,a0,a)

surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(XYProbDensity2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Numerical Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and Volatility')

str=input("Look at numerical bivariate density of Asset and Stochastic Volatility")
surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(pXY2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Analytic Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at Analytic density of Asset and Stochastic volatility")
surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(pXY2D(2:NoOfBinsX+1,3:NoOfBinsV+1)-XYProbDensity2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Difference of Analytic and Numerical Density  : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at difference of numerical and analytic densities of Asset and stochastic volatility")

CallStrikes=[.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75]

VolZEquiDistGridSize=200;
[CallPricesAnalytic]=PriceCallArrayOver2DDensity(a0,a,Coeff,CallStrikes,VolZEquiDistGridSize);
CallPricesAnalytic
CallPricesMC

str=input("Look at comparison of analytic and monte carlo call prices");

end

```

.

.

.

```
function [a0,a] = FindZSeriesCoeffsOfCoeffs(aa0,Zy,VProbMass,IndexMaxV)

% rMu(1:6)=0;
% for nn=1:IndexMaxV
%     for mOrder=1:6
%         rMu(mOrder)=rMu(mOrder)+aa0(nn).^(mOrder).*VProbMass(nn);
%     end
% end

x0=0;
x1=Zy(IndexMaxV/2-3);
x2=Zy(IndexMaxV/2-2);
x3=Zy(IndexMaxV/2-1);
x4=Zy(IndexMaxV/2+1);
x5=Zy(IndexMaxV/2+2);
x6=Zy(IndexMaxV/2+3);

y1=aa0(IndexMaxV/2-3);
y2=aa0(IndexMaxV/2-2);
y3=aa0(IndexMaxV/2-1);
y4=aa0(IndexMaxV/2+1);
y5=aa0(IndexMaxV/2+2);
y6=aa0(IndexMaxV/2+3);
N=6;
[y0] = InterpolateOrderN6(N,x0,x1,x2,x3,x4,x5,x6,y1,y2,y3,y4,y5,y6)
%Median0=(aa0(IndexMaxV/2)+aa0(IndexMaxV/2+1))/2
Median=y0;
ZyMedian=(Zy(IndexMaxV/2)+Zy(IndexMaxV/2+1))/2

%aa0
%Median0
Median
ZyMedian
str=input("Look at median");
Zu=0;
Ymu(1:IndexMaxV,1)=aa0(1:IndexMaxV)-Median;
for nn=1:IndexMaxV
    X(nn,1)=1;
    X(nn,2)=(Zy(nn)-Zu);
    X(nn,3)=(Zy(nn)-Zu).^2;
    X(nn,4)=(Zy(nn)-Zu).^3;
    X(nn,5)=(Zy(nn)-Zu).^4;
    X(nn,6)=(Zy(nn)-Zu).^5;

%     %X(nn,1)=1;
%     X(nn,1)=(Zy(nn)-Zu);
%     X(nn,2)=(Zy(nn)-Zu).^2;
%     X(nn,3)=(Zy(nn)-Zu).^3;
%     X(nn,4)=(Zy(nn)-Zu).^4;
%     X(nn,5)=(Zy(nn)-Zu).^5;

    %X(nn,7)=(ZI(nn)-Zu).^6;
    %X(nn,8)=(ZI(nn)-Zu).^7;
end

coeff=(X'*X)$X'*Ymu);
c0=coeff(1,1);
c(1:5)=coeff(2:6,1);

a0=c0;
a=c;
a0=a0+Median;

% coeff=(X'*X)$X'*Ymu);
% c(1:5)=coeff(1:5,1);
% a=c;
% a0=Median;

%[c0,c,FittedMoments] = CalculateZSeriesDensityFromRawMoments02(rMu)
%[c0,c] = CalculateZSeriesDensityFromRawMomentsM6(rMu)

end

```

.

.

.

```
function [y0] = InterpolateOrderN6(N,x0,x1,x2,x3,x4,x5,x6,y1,y2,y3,y4,y5,y6)

if(N==6)
y0=(x0-x2).*(x0-x3).*(x0-x4).*(x0-x5).*(x0-x6)./((x1-x2).*(x1-x3).*(x1-x4).*(x1-x5).*(x1-x6)).*y1+ ...
   (x0-x1).*(x0-x3).*(x0-x4).*(x0-x5).*(x0-x6)./((x2-x1).*(x2-x3).*(x2-x4).*(x2-x5).*(x2-x6)).*y2+ ...
   (x0-x1).*(x0-x2).*(x0-x4).*(x0-x5).*(x0-x6)./((x3-x1).*(x3-x2).*(x3-x4).*(x3-x5).*(x3-x6)).*y3+ ...
   (x0-x1).*(x0-x2).*(x0-x3).*(x0-x5).*(x0-x6)./((x4-x1).*(x4-x2).*(x4-x3).*(x4-x5).*(x4-x6)).*y4+ ...
   (x0-x1).*(x0-x2).*(x0-x3).*(x0-x4).*(x0-x6)./((x5-x1).*(x5-x2).*(x5-x3).*(x5-x4).*(x5-x6)).*y5+ ...
   (x0-x1).*(x0-x2).*(x0-x3).*(x0-x4).*(x0-x5)./((x6-x1).*(x6-x2).*(x6-x3).*(x6-x4).*(x6-x5)).*y6;
end

if(N==5)
y0=(x0-x2).*(x0-x3).*(x0-x4).*(x0-x5)./((x1-x2).*(x1-x3).*(x1-x4).*(x1-x5)).*y1+ ...
   (x0-x1).*(x0-x3).*(x0-x4).*(x0-x5)./((x2-x1).*(x2-x3).*(x2-x4).*(x2-x5)).*y2+ ...
   (x0-x1).*(x0-x2).*(x0-x4).*(x0-x5)./((x3-x1).*(x3-x2).*(x3-x4).*(x3-x5)).*y3+ ...
   (x0-x1).*(x0-x2).*(x0-x3).*(x0-x5)./((x4-x1).*(x4-x2).*(x4-x3).*(x4-x5)).*y4+ ...
   (x0-x1).*(x0-x2).*(x0-x3).*(x0-x4)./((x5-x1).*(x5-x2).*(x5-x3).*(x5-x4)).*y5;
end
if(N==4)
y0=(x0-x2).*(x0-x3).*(x0-x4)./((x1-x2).*(x1-x3).*(x1-x4)).*y1+ ...
   (x0-x1).*(x0-x3).*(x0-x4)./((x2-x1).*(x2-x3).*(x2-x4)).*y2+ ...
   (x0-x1).*(x0-x2).*(x0-x4)./((x3-x1).*(x3-x2).*(x3-x4)).*y3+ ...
   (x0-x1).*(x0-x2).*(x0-x3)./((x4-x1).*(x4-x2).*(x4-x3)).*y4;
end
if(N==3)
y0=(x0-x2).*(x0-x3)./((x1-x2).*(x1-x3)).*y1+ ...
   (x0-x1).*(x0-x3)./((x2-x1).*(x2-x3)).*y2+ ...
   (x0-x1).*(x0-x2)./((x3-x1).*(x3-x2)).*y3;
end
if(N==2)
y0=(x0-x2)./((x1-x2)).*y1+ ...
   (x0-x1)./((x2-x1)).*y2;
end

%y0=(x0-x3)/(x2-x3)*y2+(x0-x2)/(x3-x2)*y3;

end
```

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

% %Below we make calculations of density in original coordinates by doing
% %change of probability derivative with respect to gaussian density.
% DinvfXX(1:NoOfBinsX+1,1:NoOfBinsY+1)=0;
% for mm=2:NoOfBinsY
%     for nn=2:NoOfBinsX
%
%         DinvfXX(nn,mm) = (Zx(nn + 1,mm) - Zx(nn - 1,mm))/(XX(nn + 1) - XX(nn - 1));
%
%     end
%     DinvfXX(NoOfBinsX+1,mm)=DinvfXX(NoOfBinsX,mm);
%     DinvfXX(1,mm)=DinvfXX(2,mm);
% end
% DinvfXX(:,1)=DinvfXX(:,2);
% DinvfXX(:,NoOfBinsY+1)=DinvfXX(:,NoOfBinsY);

%Below we make calculations of density in original coordinates by doing
%change of probability derivative with respect to gaussian density.
DinvfXX(1:NoOfBinsX+1,1:NoOfBinsY+1)=0;
for mm=1:NoOfBinsY
    DinvfXX(1,mm)= (Zx(1 + 1,mm) - Zx(1,mm))/(XX(1 + 1) - XX(1));
    for nn=2:NoOfBinsX

        DinvfXX(nn,mm) = (Zx(nn + 1,mm) - Zx(nn - 1,mm))/(XX(nn + 1) - XX(nn - 1));

    end
    %DinvfXX(nn,mm) = (Zx(nn + 1,mm) - Zx(nn - 1,mm))/(XX(nn + 1) - XX(nn - 1));
    DinvfXX(NoOfBinsX+1,mm)=DinvfXX(NoOfBinsX,mm);
    %DinvfXX(1,mm)=DinvfXX(2,mm);
end

DinvfYY(1:NoOfBinsY+1)=0;
DinvfYY(1) = (Zy(1+1) - Zy(1))/(YY(1 + 1) - YY(1));
for mm=2:NoOfBinsY

        DinvfYY(mm) = (Zy(mm+1) - Zy(mm-1))/(YY(mm + 1) - YY(mm - 1));

end
DinvfYY(NoOfBinsY+1)=DinvfYY(NoOfBinsY);
%DinvfYY(1)=DinvfYY(2);

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

here are the call prices you get at end.

CallStrikes =

  Columns 1 through 3

   0.500000000000000   0.550000000000000   0.600000000000000

  Columns 4 through 6

   0.650000000000000   0.700000000000000   0.750000000000000

  Columns 7 through 9

   0.800000000000000   0.850000000000000   0.900000000000000

  Columns 10 through 12

   0.950000000000000   1.000000000000000   1.050000000000000

  Columns 13 through 15

   1.100000000000000   1.150000000000000   1.200000000000000

  Columns 16 through 18

   1.250000000000000   1.300000000000000   1.350000000000000

  Columns 19 through 21

   1.400000000000000   1.450000000000000   1.500000000000000

  Columns 22 through 24

   1.550000000000000   1.600000000000000   1.650000000000000

  Columns 25 through 26

   1.700000000000000   1.750000000000000

CallPricesAnalytic =

  Columns 1 through 3

   0.539290243689707   0.499842263837271   0.462084631065679

  Columns 4 through 6

   0.426110588978143   0.391997871812819   0.359806609766627

  Columns 7 through 9

   0.329577590834143   0.301331003556603   0.275065779027724

  Columns 10 through 12

   0.250759629840779   0.228369846325036   0.207834857165970

  Columns 13 through 15

   0.189076496958798   0.172002856060418   0.156511529711101

  Columns 16 through 18

   0.142493045335374   0.129834237461553   0.118421360968469

  Columns 19 through 21

   0.108142780436897   0.098891135704802   0.090564948520072

  Columns 22 through 24

   0.083069691245701   0.076318378937973   0.070231768793159

  Columns 25 through 26

   0.064738257930599   0.059773565916314

CallPricesMC =

  Columns 1 through 3

   0.538992955696227   0.499293133221035   0.461321275922108

  Columns 4 through 6

   0.425172743633672   0.390941179947047   0.358684904911886

  Columns 7 through 9

   0.328465201396068   0.300287051098513   0.274127910700729

  Columns 10 through 12

   0.249968676414874   0.227741408421916   0.207375767884388

  Columns 13 through 15

   0.188787016585533   0.171854737331058   0.156446630183023

  Columns 16 through 18

   0.142479895137964   0.129833092092457   0.118388043139913

  Columns 19 through 21

   0.108041874210775   0.098707968343340   0.090287004756542

  Columns 22 through 24

   0.082685068916804   0.075814458224064   0.069601168352276

  Columns 25 through 26

   0.063983852584495   0.058898456155222

Look at comparison of analytic and monte carlo call prices

Here are the analytic graphs.

[![Image](../images/i.postimg.cc/BZkZbBXh/SV2-DDensity12-A.png)](https://postimg.cc/hh8R3x8x)

[![Image](../images/i.postimg.cc/L6P91gPm/SV2-DDensity12-B.png)](https://postimg.cc/F79XtRG6)

---

### #2021 — Amin (Topic Author)
*October 20, 2023, 9:16 PM*

Friends, I was thinking of possibilities of hermite regression for calculation of density of asset conditional on
volatility.

In our analytics, we found coefficients of conditional Z-series of asset for every volatility grid subdivision and then
later regressed these volatility dependent asset coefficients on volatility. We could not do a hermite regression of
these volatility dependent asset coefficients on volatility because underlying Zv is the same for volatility and these
coefficients in a particular subdivision and it will give us identical values of hermite polynomials for regressor and
regressand.

However, I believe there are other ways we can use hermite regression in our context.

First of all a plain unconditional univariate hermite regression of asset and volatility for all paths will not give us
the density of asset and it will only give us the average value of asset for each value of volatility.

I think one possibility to get the density of asset conditional on volatility would be to hermite-regress unconditional
value of asset X(by representing the unconditional value of X in data by its hermite polynomials derived from single
unconditional density of asset) on products of conditional value of asset in a particular volatility grid subdivision
and conditional value of volatility in that volatility grid subdivision(which will be represented by a product of
conditional value of hermite polynomials(derived for that particular volatility subdivision) of asset and the value of
hermite polynomials of volatility in that subdivision.) So we will decompose every monte carlo path into unconditional
hermite polynomials of asset and also into conditional value of hermite polynomials of asset for particular volatility
grid subdivision and also into hermite polynomials of volatility. This seems sense from what we have been doing in a
different framework. I will try to do this regression in a day or two and see how it goes and share it with friends.

I think that above method could also possibly take care of correlations between regressors and regressand as in a
correlated stochastic volatility model.

I am sure that a large number of possibilities will open up to tackle every problem as we get more understanding of the
related issues and our research effort grows.

---

### #2022 — Amin (Topic Author)
*October 21, 2023, 10:20 AM*

Friends, I was further able to improve the matlab program by increasing the accuracy of moments of normal density in
coefficients estimation by least squares. It has improved the accuracy further everywhere. The graphs of SDE density
with both extreme and benign SDE parameters including those of lognormal asset are a better match to numerical graphs
now. And accuracy of analytic call prices VS monte carlo call prices has remarkably improved. I am further trying to
improve the moments fit for today to make sure that this thing is settled and we could freely use Z-series coefficients
estimation by LS regression of data in the future.

We will now take a break from further research for two or three days and in about one or two days, I will post a final
commented version of the work we have done up till today and also explain all math ideas behind the programs in complete
detail in next few days.

We will move on only after we have a final working program for the work we have done till now and we will also
understand the logic of the basic ideas behind the program in next few days.

---

### #2023 — Amin (Topic Author)
*October 21, 2023, 8:32 PM*

Friends, I worked today at matching moments of normal density. This is regarding equi-probable normal density grid that
I use for least square hermite polynomial regression on data to find the coefficients of Z-series. The normal density
grid is constructed so that each point on normal density grid is at the centre of equi-probable grid subdivisions.
Again, this grid is constructed so that probability mass in each subdivision is exactly the same.

Even though the equi-probable grid is constructed from normal density, the moments of discrete grid with equal
probability of each grid point do not perfectly match the moments of standard normal density and there are slight
mismatches between the calculated moments of equiprobable grid and the moments standard normal density. This slight
mismatch can throw the regressions off and seriously deteriorate the accuracy of coefficients of Z-series. I was able to
get an improved program yesterday only when I tried to make a better match of the equiprobable density with standard
normal moments. But it was still ad-hoc.

Today I wrote a program that matches the above mentioned moments with standard normal density moments with an iterative
procedure and results in a match to moments that is upto six or seven digits  accurate. This improvement also results in
much better match between analytic call prices and monte carlo call prices. This iterative procedure takes 20-30 seconds
but it has to be run only once based on total number of paths in each equal probability subdivision. We can just save
the parameters values for all the possible number of popular path values and then we do not have to run the iterative
procedure again and again every time we run the program. I am sure this will be very helpful for friends who would want
to use the polynomial regression method to find the coefficients of Z-series from data.

The equations for matching moments are based on multiplication of data by even order hermite polynomials and are
difficult to solve analytically so I used a numerical iterative procedure that is reasonably fast and takes 20-30
seconds to find the matching parameters of hermite polynomials.

This new improvement has also remarkably improved fit to lognormal type asset SDE densities and mostly lognormal asset
SDE 2D density falls off smoothly close to  zero instead of starting to rise dramtically close to zero as was the
problem earlier.

---

### #2024 — Amin (Topic Author)
*October 22, 2023, 5:22 PM*

Friends, I want to share the details of my small algorithm to correct the moments of arrays of standard normals
associated with equiprobable normal grid subdivisions. These arrays of standard normals would later be used for
polynomial regression on the data to find parameters of Z-series from the data.

Suppose there are N data members and we want to do a hermite polynomial regression on this data to find Z-series
parameters of data random variable. We will divide the standard normal density into N subdivisions with each subdivision
sharing an equal probability mass of 1/N.

However discrete values of Zn when integrated on probability mass 1/N, can have moments different from moments of
standard normal density which will create inaccuracies in our polynomial regression to find Z-series parameters of the
data random variable.

I thought of multiplying the data array with an expression comprising sum of hermite polynomials with unspecified
coefficients. We would write equations of moments and then find coefficients of hermite polynomials that pin down the 
moments of new data precisely equal to target moments.

One consideration is that our Zn array is perfectly symmetric around zero so all odd moments are zero. We want to add
only even hermite polynomials in the expression of hermite polynomials with unspecified coefficients(that is multiplied
to original Zn array to make its moments equal to target moments). We do not want odd hermite polynomials in this
expression with unspecified coefficients as they would introduce skew in our array of equi-probable standard normal
values(and then we would have to do unnecessary work to cancel the skew). In order to have zero odd moments(as in case
of standard normals), we only multiply with a series in even hermite polynomials with unspecified coefficients that
preserves perfect symmetry around zero so we would not have to bother with any odd moments and all odd moments will be
zero by construction due to symmetry of our Zn array around zero.

Our original standard normal Zn array associated with equiprobable grid is multiplied with a series in hermite
polynomials as

$Z_{n,Corrected} \, = \, Z_n \, (\alpha \, +  \beta \, (Z_n^2-1) \, + \, \gamma \, ({Z_n}^4 \, + \, 6 \, {Z_n}^2 \, + \, 3 \,))\,$

We find coefficients$\alpha$ ,$\beta$ , and$\gamma$ so that our objective function matching moments of
$Z_{n,Corrected} \, $ with target moments is maximized.

$Moment2\, = \sum\limits_{n=1}^{n=N} \, {Z_{n,Corrected}}^2 \, \frac{1}{N} $

$= \, \sum\limits_{n=1}^{n=N} \,  {Z_n}^2 \, {(\alpha \, +  \beta \, (Z_n^2-1) \, + \, \gamma \, ({Z_n}^4 \, + \, 6 \, {Z_n}^2 \, + \, 3 \,))}^2\, \frac{1}{N} $

$Moment4\, = \sum\limits_{n=1}^{n=N} \, {Z_{n,Corrected}}^4 \, \frac{1}{N} $

$= \,  \sum\limits_{n=1}^{n=N} \, {Z_n}^4 \, {(\alpha \, +  \beta \, (Z_n^2-1) \, + \, \gamma \, ({Z_n}^4 \, + \, 6 \, {Z_n}^2 \, + \, 3 \,))}^4\, \frac{1}{N} $

$Moment6\, = \sum\limits_{n=1}^{n=N} \, {Z_{n,Corrected}}^6 \, \frac{1}{N} $

$= \, \sum\limits_{n=1}^{n=N} \,  {Z_n}^6 \, {(\alpha \, +  \beta \, (Z_n^2-1) \, + \, \gamma \, ({Z_n}^4 \, + \, 6 \, {Z_n}^2 \, + \, 3 \,))}^6\, \frac{1}{N} $

Here is an iterative optimization matlab program that finds$Z_{n,Corrected}$ whose moments match the standard normal
moments with great precision. I improved this program and now it takes only 3-7 seconds as opposed to 30-40 secs it was
taking yesterday. So if great speed is not the concern, you can easily embed it in your programs.

.

.

.

```
function [ZnNew] = MatchMomentsOfIdealZ(Zn)

Ndata=length(Zn);
if(Ndata100)&&(Ndata500)&&(Ndata1000)&&(Ndata3000)&&(Ndata6000)&&(Ndata10000)
    Iterations=50;
end
alpha=1;
beta=0;
gamma=0;

ZnNew(1:Ndata)=Zn(1:Ndata).*(alpha+beta*(Zn(1:Ndata).^2-1)+gamma*(Zn(1:Ndata).^4-6*Zn(1:Ndata).^2+3));

Moment2=sum(ZnNew(1:Ndata).^2)*1/Ndata
Moment4=sum(ZnNew(1:Ndata).^4)*1/Ndata
Moment6=sum(ZnNew(1:Ndata).^6)*1/Ndata

w1=5000;
w2=200;

ObjFuncBest=(Moment2-1).^2*w1+(Moment4-3).^2*w2+(Moment6-15).^2;

delta_alpha=.00025;
delta_beta=.0002;
delta_gamma=.0002;
alphaSuccessCount=0;
betaSuccessCount=0;
gammaSuccessCount=0;
SuccessPrevalpha=0;
SuccessPrevbeta=0;
SuccessPrevgamma=0;

mul1=.9;
mul2=1.1;

for iter=1:Iterations
    alphaNew=alpha+delta_alpha;
    betaNew=beta;
    gammaNew=gamma;
    ZnNew(1:Ndata)=Zn(1:Ndata).*(alphaNew+betaNew*(Zn(1:Ndata).^2-1)+gammaNew*(Zn(1:Ndata).^4-6*Zn(1:Ndata).^2+3));
    Moment2=sum(ZnNew(1:Ndata).^2)*1/Ndata;
    Moment4=sum(ZnNew(1:Ndata).^4)*1/Ndata;
    Moment6=sum(ZnNew(1:Ndata).^6)*1/Ndata;

    ObjFuncNew=(Moment2-1).^2*w1+(Moment4-3).^2*w2+(Moment6-15).^2;

    if(ObjFuncNew4)
        delta_alpha=delta_alpha*mul2;
    end
    if(betaSuccessCount>4)
        delta_beta=delta_beta*mul2;
    end
    if(gammaSuccessCount>4)
        delta_gamma=delta_gamma*mul2;
    end
end
ZnNew(1:Ndata)=Zn(1:Ndata).*(alpha+beta*(Zn(1:Ndata).^2-1)+gamma*(Zn(1:Ndata).^4-6*Zn(1:Ndata).^2+3));

Moment2=sum(ZnNew(1:Ndata).^2)*1/Ndata;
Moment4=sum(ZnNew(1:Ndata).^4)*1/Ndata;
Moment6=sum(ZnNew(1:Ndata).^6)*1/Ndata;

Moment2
Moment4
Moment6

%str=input("Look at moment values")

end

```

---

### #2025 — Amin (Topic Author)
*October 22, 2023, 6:41 PM*

I am writing this post to thank all those good Americans who tried to protect me again and again especially when times
were very tough for me. I was detained every year by different psychiatrists on totally flimsy issues before there was
strong opposition from good American friends and only then I was able to do better research.

I maintained an office for four years from 2013-2016 where I would try to do my research work. And many times, when I
would come back from office and park my car in the house, five or six people would appear from a corner of the house and
tell me that they had come from some mental facility to detain me. Instead of discussing any logical reasons for my
detention, doctors would have totally flimsy excuses and say things like that your mother knows your schizophrenia and
has told us that your schizophrenia has started to increase again and you need to be detained and treated for your
safety. Psychiatrists would start using typical talk and tell me that I totally lacked insight about my strong
schizophrenia and therefore they would have to force treatment and drugs on me to improve my health.

I would be detained again and again totally out of the blue and without any special event preceding it or without any
prior warning by my family.

Even now when I come to house, many times I would be seriously afraid that staff from some mental health facility might
already be in home to detain me. I would try to look for a suspicious car parked outside of my house and when I enter my
house when I return at night, I would look in dark corners to see if somebody might be hidden there and would emerge all
of a sudden to tell me that I needed to be hospitalized. Today when I tried to enter the inside of my house into the
lounge from the porch, it seemed to me that door was not opening as if somebody was behind the door and I was quite
certain that somebody might be hiding behind the door and I walked back from the door into the car garage. My mother
came out in a few minutes and I asked her if she had called hospital staff to detain me again.

I am also very alarmed these days since mind control agents are trying to do whatever it takes to drug my food and
disrupt my research. Every day they try to do something so that I would not be able to concentrate on my research for
several days. The desperate resolve with which they are trying to drug my food around the city makes me afraid that they
might finally  decide to detain me.

The only reason that I have not been detained recently and also for past three years is that a lot of good Americans
protested very strongly to their government and tried to protect me and that is the most major reason that I have been
able to do some reasonable research.

I am extremely thankful to and deeply indebted to good American people who tried to protect me against abuse and made
sure that I would not be detained at totally flimsy excuses. Without the support from good Americans, I would still be
regularly forced to stay in the mental hospitals.

Due to all the kindness and support from good American people, I have been able to do better research and I am truly
thankful to good American people who went out of the way to make attempts to protect me and end my mind control and
helped me especially when I was starting to lose faith in goodness of humanity.

---

### #2026 — Amin (Topic Author)
*October 23, 2023, 8:56 AM*

Since the Israeli-Palestinians conflict is raging and most people have a strong opinion about the issue. I thought I
will share my opinion as well.

I wrote the post(this is a slightly edited version) below as a Linkedin comment on a post by a very respectable, nice,
and a very good human who is from Israel in my connections.

I am totally with you in condemning terrorism by Hamas and feel the same as you when I see families, living happily,
shot dead all of a sudden by Hamas terrorists. Such a massacre cannot be allowed in twenty first century human
civilization. All these terrorists should be brought to trial and very appropriately punished or eliminated if trial is
not possible.

But at the same time when I think logically why so many Hamas people have become terrorists.

We all love life more than anything else and really want to live. For many human beings the mere act of living is a joy
in itself.

Hamas knew there would be large scale deaths of Palestinians after their terrorist acts but they still acted in the same
way and had no qualms about it.

Why have they lost all love for their life and lives of their fellow people? Why is it that life and death have become
meaningless for them? When people are treated without any dignity, they never learn to show any dignity. Israeli forces
normally treat Palestinians without much regard and there are regular news of shooting of Palestinian youth by IDF on
very minor issues.

Tit for tat is mostly not a solution to any problem. Israelis and Palestinians have to immediately do something to
decrease hatred and start to show some basic respect to each other. But their leaders are exploitative and want to
exploit widespread hatred. Masses in any nation are not super-intelligent and usually follow their gut reactions or tit
for tat reactions. A true leader is the one who does not exploit emotions of masses but makes the masses follow his true
wisdom for a better future of the people and nation.

I think both Israeli and Palestinians need good leaders who are ready to lead their people towards reconciliation and
decreasing polarization. After all, we are all human beings just irrationally torn into religions which have no
scientific basis.

Even if some good leaders in both nations follow the right path of reconciliation, they will have to be very persistent
and will have to follow long term objectives since fanatics and hardliners in both nations will try to sabotage rational
and logical policies of reconciliation by random acts of violence and terrorism. Good leaders would need to show a
strong resolve towards their longer term objectives. In our world, it can just take seconds to destroy something that is
meaningful but it can take decades for us humans to build something that is meaningful. It will take minutes or hours to
destroy peace or any attempts at peace but it can take decades of perseverance to bring a lasting peace.

Whatever has passed, we have to try to look towards a better future for everyone otherwise current hatred will ensue
more hatred and their will be more violence, aggression and terrorism.

Jews and Muslim Palestinians have to be able to think beyond their own religion, their own benefit and both need to
compromise for a better future and a lasting peace.

---

### #2027 — Amin (Topic Author)
*October 24, 2023, 5:02 PM*

Friends, one of my uncles passed away yesterday and a lot of our family from my mother's side were together. I also
attended my uncle's funeral and burial.

All of my uncles are getting old and I felt very sad when I saw that another of my uncles, who also arrived at the
funeral, was barely walking with great difficulty. He was so lively and joking until just a few years ago. My mother was
the eldest in her family but I am very happy that my father is still very healthy and going strong without any health
complication.

So could not do much work for past two days. I will be posting final version of the program tonight since it is already
getting too late. This is pretty much the final version but I will release a well commented version and explanation of
the program in another day or two.

In this post, I would like to explain another thing about polynomial regression. There are two types of data for
polynomial regression. One type of data is totally random and we do not know what is the associated value of CDF (in
continuous terms) with precision since data is not equi-spaced with respect to any metric. For this type of data, we
sorted it and associated an equi-probable normal array (equal to data length) and we also matched the moments of this
equi-probable normal array.  And then we followed with regression to find coefficients of Z-series. This is the case in
our program when we try to find individual Z-series coefficients of asset data paths (all of the asset paths that lie in
the particular volatility grid subdivision) associated with each of the volatility grid subdivisions.

Second type of data where we can also use LS regression is where we already know the underlying normal array associated
with each data element with perfect accuracy(for many reasons since data might have been created from a known array of
underlying normal density or so on), I call this case as non-randomly distributed data since as opposed to randomly
distributed data discussed in previous paragraph, we know the value of underlying normal array associated with each data
member with precision.  I am of the opinion that in such a case, we might not need to match moments of underlying normal
density array since we already know the true values of underlying array from normal density associated with data
elements. This is the case in our program when we are trying to find universal coefficients of each of the Z-series
coefficients and we know the value of particular Z-series coefficient associated with individual volatility grid points
where we know CDF associated with each volatility grid.

This is how I am treating different types of data in my program but urge friends to think on their own what would be the
right way to tackle both kinds of data and when would we need to match moments of associated normal array with true
moments and when we would not need to match moments of underlying normal array associated with the data.

---

### #2028 — Amin (Topic Author)
*October 24, 2023, 11:14 PM*

Friends, I will only be able to post the new program tomorrow (Tuesday) night. Sorry for this delay.

---

### #2029 — Amin (Topic Author)
*October 25, 2023, 7:17 PM*

Friends, when I started working on this research problem, the first few attempts were very poor at best but we fixed a
lot of problems one by one and now our program is in a relatively far better shape.

In the same spirit, I noticed that there is another problem with Z-series that sometimes the first derivative of
Z-series becomes negative and the density rolls back onto itself. We have seen this problem in the past as well. When I
wrote first versions of hermite regression programs at the start of this year, they were totally off and the whole thing
worked only when we fixed similar problem with three parameter Z-series we were working with.

This issue can cause serious problems with some SDE parameters. So I have decided to take my time to fix this issue in a
good way for the five coefficients Z-series. And this can take anywhere between 2-4 days. I want to settle this problem
in a good way so we will not have to bother about it in the future. Therefore it can take a few days before I release
the next version of the program. But I assure friends that final version will be a very good one and I hope that that
most friends would really like it.

---

### #2030 — Amin (Topic Author)
*October 27, 2023, 9:55 AM*

Friends, I want to make several major changes to the program.

I noticed that Z-series coefficients constructed from coeffs of coeffs behave well in the range that was used to
construct them. i.e. between Zv=-2.5 to Zv=+2.5 but outside of that range they can be quite off. We get reasonable
graphs and call prices since probability out side of this range is very small. But I want to improve this.

I used equi-probable underlying Z-grid for calculation of coeffs of coeffs and I want to see how to improve it or change
it to equi-distant grid or some other method in between.

I am also thinking of standardizing every asset density conditional on each volatility grid cell and then model
volatility(that appears in standardization of every conditional asset density) as a separate Z-series and finds coeffs
of coeffs for standardized densities. Final Z-series of conditional asset densities could be constructed as a product of
volatility Z-series and coefficients constructed from coeffs of coeffs (found from standardized conditional densities).

Another thing I was thinking about polynomial regression. When we know both Z and probability associated with an
observation as in case of an underlying grid, we could also use a weighted LS regression(weighted by probability
associated with each observation or grid cell etc.) instead of a plain LS regression. Even if we do not use
probabilities as weights, it would still be useful to find some other way of giving large weights, in polynomial
regression, to mid-density and small weights to far-tails.

I also start to believe that many times when Z-series density folds back onto itself, it can still be meaningful and
might have some non-linear dynamics for Z-series variables. In such cases, our simple method to construct the density is
not good at all but it will be far more meaningful in such cases to draw a graph of random variable X(constructed by
Z-series) as a function of Z in the Z-series. I noticed that graphs of densities of coeffs found from Z-series of coeffs
of coeffs were quite absurd but when I plotted coeffs as a function of underlying Z, I still found those graphs quite
meaningful and informative. I think it very informative whenever we graph a density from Z-series that we also graph X
as a function of Z.

Basically when density folds onto itself, it means that X is not monotonically increasing as a function of Z which is a
perfectly valid possibility and such dynamics might exist many times in reality. Moments of density folding onto itself
might still be matching perfectly with input moments. In such cases our method of density construction is not good and
it has to be re-written with a better mathematical logic. However if we do want X as a monotonically increasing function
of Z explicitly, these densities might not be of our use.

I am trying to make it a good program and it can still take sometime. Sorry to make friends wait for the final program.

---

### #2031 — Amin (Topic Author)
*October 28, 2023, 10:22 PM*

Friends, I have posted some graphs of bivariate densities each followed by the respective values of analytic call prices
and monte carlo call prices.

For first three graphs  gammaX=.95,.75,.55 while gamma=.5 (heston), vol of vol=sigma0=.75

For last three graphs  gammaX=.95,.75,.55 while gamma=.95 (approximately lognormal), vol of vol=sigma0=1.05

for all graphs v0=.35, thetaV=.06,kappaV=1.25, T=2

SDE parameters are also on the title of each graph.

dX(t)=V(t)^.5*X(t)^gammaX*dZ1(t)

dV(t)=kappaV* (thetaV - V(t) )*dt  + sigma0 *V(t)^gamma*dZ2(t)

T=2

correlation=0

Difference between analytic and MC call prices is between 0-5 bp for 90% of the times.

I will post the exact program that produced these results in the following post.

.

.

[![Image](../images/i.postimg.cc/Ss5fgW0K/SV2-DDensity13-A.png)](https://postimg.cc/9Rd9MwQ3)

[![Image](../images/i.postimg.cc/NG945PT2/SV2-DDensity13-B.png)](https://postimg.cc/dDFdf65J)

[![Image](../images/i.postimg.cc/Y0WfZhkz/SV2-DDensity13-C.png)](https://postimg.cc/YLtWm2vv)

.

.

.

CallStrikes =

  Columns 1 through 3

   0.500000000000000   0.550000000000000   0.600000000000000

  Columns 4 through 6

   0.650000000000000   0.700000000000000   0.750000000000000

  Columns 7 through 9

   0.800000000000000   0.850000000000000   0.900000000000000

  Columns 10 through 12

   0.950000000000000   1.000000000000000   1.050000000000000

  Columns 13 through 15

   1.100000000000000   1.150000000000000   1.200000000000000

  Columns 16 through 18

   1.250000000000000   1.300000000000000   1.350000000000000

  Columns 19 through 21

   1.400000000000000   1.450000000000000   1.500000000000000

  Columns 22 through 24

   1.550000000000000   1.600000000000000   1.650000000000000

  Columns 25 through 26

   1.700000000000000   1.750000000000000

CallPricesAnalytic =

  Columns 1 through 3

   0.525253867736018   0.484298258752238   0.445302773488913

  Columns 4 through 6

   0.408424110303058   0.373786612144249   0.341475487534358

  Columns 7 through 9

   0.311532638405545   0.283955566797947   0.258699512025336

  Columns 10 through 12

   0.235682496563740   0.214792462597328   0.195895452111138

  Columns 13 through 15

   0.178843815906312   0.163483658816911   0.149661031986292

  Columns 16 through 18

   0.137226674675436   0.126039333174289   0.115967826637012

  Columns 19 through 21

   0.106892097547315   0.098703497344218   0.091304536191633

  Columns 22 through 24

   0.084608287296751   0.078537592948872   0.073024179095091

  Columns 25 through 26

   0.068007751445149   0.063435119811372

CallPricesMC =

  Columns 1 through 3

   0.525126596429244   0.484175328731669   0.445189993826965

  Columns 4 through 6

   0.408348521341393   0.373770792273723   0.341531961013078

  Columns 7 through 9

   0.311649301778466   0.284122261230758   0.258891409701495

  Columns 10 through 12

   0.235897797191076   0.215016828140034   0.196089506726843

  Columns 13 through 15

   0.179010750189295   0.163611491888953   0.149747682307928

  Columns 16 through 18

   0.137260066346158   0.126002855651538   0.115865967665332

  Columns 19 through 21

   0.106737990575296   0.098520952672872   0.091108424181922

  Columns 22 through 24

   0.084412658170174   0.078361652215275   0.072873034627857

  Columns 25 through 26

   0.067882232625040   0.063333281977474

Look at comparison of analytic and monte carlo call prices

2.

[![Image](../images/i.postimg.cc/NFCqJCsH/SV2-DDensity14-A.png)](https://postimg.cc/n9mPMkQF)

[![Image](../images/i.postimg.cc/76Vy7YjX/SV2-DDensity14-B.png)](https://postimg.cc/k6BZP9Jt)

[![Image](../images/i.postimg.cc/BbnfCf03/SV2-DDensity14-C.png)](https://postimg.cc/zb6QJMv2)

.

.

CallPricesAnalytic =

  Columns 1 through 3

   0.530304072202647   0.489513740312223   0.450524351266409

  Columns 4 through 6

   0.413488393992952   0.378533186154997   0.345753945094770

  Columns 7 through 9

   0.315208755133874   0.286916164344508   0.260855733255845

  Columns 10 through 12

   0.236971356635172   0.215176740931439   0.195362165314762

  Columns 13 through 15

   0.177401622538941   0.161159584437791   0.146496880060780

  Columns 16 through 18

   0.133275428260425   0.121361775424509   0.110629530660119

  Columns 19 through 21

   0.100960867243964   0.092247285178882   0.084389822856395

  Columns 22 through 24

   0.077298881392155   0.070893794159935   0.065102243169492

  Columns 25 through 26

   0.059859596705886   0.055108220380379

CallPricesMC =

  Columns 1 through 3

   0.530522515672348   0.489820425753355   0.450899934593976

  Columns 4 through 6

   0.413919805326850   0.378996491461526   0.346226977356876

  Columns 7 through 9

   0.315646155087576   0.287287338983909   0.261114358197161

  Columns 10 through 12

   0.237110586875241   0.215196294786874   0.195250776475369

  Columns 13 through 15

   0.177160889744650   0.160810642413885   0.146062558282653

  Columns 16 through 18

   0.132777765570815   0.120810906082559   0.110044187546845

  Columns 19 through 21

   0.100361104811765   0.091659605934397   0.083834711662820

  Columns 22 through 24

   0.076799240214805   0.070464320581852   0.064758818469425

  Columns 25 through 26

   0.059602879300519   0.054926440862531

Look at comparison of analytic and monte carlo call prices

3.

[![Image](../images/i.postimg.cc/KzQdjpgH/SV2-DDensity15-A.png)](https://postimg.cc/xJJsFR5v)

[![Image](../images/i.postimg.cc/C5QXHZ7C/SV2-DDensity15-B.png)](https://postimg.cc/m17mTg0h)

[![Image](../images/i.postimg.cc/j25B76Hd/SV2-DDensity15-C.png)](https://postimg.cc/Vrx7yCZ3)

CallPricesAnalytic =

  Columns 1 through 3

   0.536000951909470   0.495405410306874   0.456432079404371

  Columns 4 through 6

   0.419221245903480   0.383898544242418   0.350568694636248

  Columns 7 through 9

   0.319309873342072   0.290169437866181   0.263161612285882

  Columns 10 through 12

   0.238267464969875   0.215437146800720   0.194594005533737

  Columns 13 through 15

   0.175639948448617   0.158461341693196   0.142934801500900

  Columns 16 through 18

   0.128932397428008   0.116325986052897   0.104990573363520

  Columns 19 through 21

   0.094806737428982   0.085662223940280   0.077452863594881

  Columns 22 through 24

   0.070082965240556   0.063465325058705   0.057520969828902

  Columns 25 through 26

   0.052178728037990   0.047374699975537

CallPricesMC =

  Columns 1 through 3

   0.536724676059649   0.496157314824361   0.457195701330113

  Columns 4 through 6

   0.419982652944329   0.384642676759648   0.351274660822558

  Columns 7 through 9

   0.319955351498254   0.290736242780666   0.263613776970552

  Columns 10 through 12

   0.238585666023161   0.215629028037995   0.194659005967058

  Columns 13 through 15

   0.175576208259224   0.158285549062930   0.142658372690963

  Columns 16 through 18

   0.128582906752158   0.115925249423483   0.104557870069883

  Columns 19 through 21

   0.094362631467552   0.085237439480430   0.077068684550064

  Columns 22 through 24

   0.069753564753062   0.063206636978306   0.057345371711900

  Columns 25 through 26

   0.052090746315515   0.047361162653977

Look at comparison of analytic and monte carlo call prices

4.

[![Image](../images/i.postimg.cc/hvkMtVMY/SV2-DDensity16-A.png)](https://postimg.cc/q6G2mhPc)

[![Image](../images/i.postimg.cc/zBP04sh8/SV2-DDensity16-B.png)](https://postimg.cc/WFgGkfSH)

[![Image](../images/i.postimg.cc/HncBm605/SV2-DDensity16-C.png)](https://postimg.cc/K3bnrrHv)

CallPricesAnalytic =

  Columns 1 through 3

   0.523726997769925   0.482985356056345   0.444337207676675

  Columns 4 through 6

   0.407908032116061   0.373779587822135   0.341989486670828

  Columns 7 through 9

   0.312533232913967   0.285368927497565   0.260423314584489

  Columns 10 through 12

   0.237598392968559   0.216778061542806   0.197834337315540

  Columns 13 through 15

   0.180632837265739   0.165037360973029   0.150913529497205

  Columns 16 through 18

   0.138131521515605   0.126568001648918   0.116107363426261

  Columns 19 through 21

   0.106642417061695   0.098074646598510   0.090314147515607

  Columns 22 through 24

   0.083279338783210   0.076896525519187   0.071099371648009

  Columns 25 through 26

   0.065828327269469   0.061030043176544

CallPricesMC =

  Columns 1 through 3

   0.523363523909651   0.482589459879851   0.443950193435061

  Columns 4 through 6

   0.407573940706207   0.373522550407220   0.341839829665716

  Columns 7 through 9

   0.312496384394458   0.285430779419062   0.260573880370127

  Columns 10 through 12

   0.237815311998995   0.217040055620438   0.198117528402273

  Columns 13 through 15

   0.180916837449105   0.165310431378750   0.151158829266362

  Columns 16 through 18

   0.138335529015453   0.126734053736175   0.116228021431724

  Columns 19 through 21

   0.106713826576129   0.098099034799170   0.090301361300098

  Columns 22 through 24

   0.083234738156757   0.076836552908685   0.071027535777598

  Columns 25 through 26

   0.065750919485909   0.060964646604885

Look at comparison of analytic and monte carlo call prices

5.

[![Image](../images/i.postimg.cc/DzfVhKSX/SV2-DDensity17-A.png)](https://postimg.cc/SnP1L37S)

[![Image](../images/i.postimg.cc/pdswX1j1/SV2-DDensity17-B.png)](https://postimg.cc/67GjMcYd)

[![Image](../images/i.postimg.cc/C1dWZHHM/SV2-DDensity17-C.png)](https://postimg.cc/TLMkFb4B)

CallPricesAnalytic =

  Columns 1 through 3

   0.528906847551764   0.488408688286294   0.449815183769210

  Columns 4 through 6

   0.413247024693038   0.378791699985848   0.346501749888178

  Columns 7 through 9

   0.316395117209368   0.288457328898019   0.262645078122135

  Columns 10 through 12

   0.238890711969435   0.217107146898517   0.197192804241212

  Columns 13 through 15

   0.179036255119262   0.162520366910106   0.147525836950468

  Columns 16 through 18

   0.133934075182811   0.121629453148613   0.110500973128881

  Columns 19 through 21

   0.100443431424970   0.091358157618217   0.083153410903036

  Columns 22 through 24

   0.075744508459921   0.069053751809805   0.063010206950693

  Columns 25 through 26

   0.057549383997860   0.052612852733435

CallPricesMC =

  Columns 1 through 3

   0.528805168134496   0.488348523322668   0.449813542816567

  Columns 4 through 6

   0.413316141670085   0.378920363574439   0.346679126047752

  Columns 7 through 9

   0.316619445961258   0.288698514350748   0.262879455555842

  Columns 10 through 12

   0.239103807155489   0.217279326275662   0.197309548233842

  Columns 13 through 15

   0.179088171315580   0.162510761286726   0.147456558290214

  Columns 16 through 18

   0.133802873723054   0.121447721092848   0.110285761561852

  Columns 19 through 21

   0.100197175852386   0.091087597178179   0.082874161056841

  Columns 22 through 24

   0.075469599935292   0.068791308753644   0.062771100627259

  Columns 25 through 26

   0.057342359695915   0.052450714659461

Look at comparison of analytic and monte carlo call prices

6.

[![Image](../images/i.postimg.cc/VvWBm2rJ/SV2-DDensity18-A.png)](https://postimg.cc/tn7VzSzb)

[![Image](../images/i.postimg.cc/GtCx0b20/SV2-DDensity18-B.png)](https://postimg.cc/R6gHK5KG)

[![Image](../images/i.postimg.cc/fLXfgVMj/SV2-DDensity18-C.png)](https://postimg.cc/S2S9nN2J)

CallPricesAnalytic =

  Columns 1 through 3

   0.534844283800728   0.494554046646359   0.455966894536881

  Columns 4 through 6

   0.419197476813717   0.384339274337369   0.351461643438059

  Columns 7 through 9

   0.320608064029987   0.291795670386162   0.265016016511277

  Columns 10 through 12

   0.240236918713314   0.217405140483678   0.196449645643871

  Columns 13 through 15

   0.177285143415309   0.159815676235268   0.143938047442844

  Columns 16 through 18

   0.129544940874191   0.116527639170862   0.104778296140000

  Columns 19 through 21

   0.094191757497170   0.084666952761058   0.076107899556351

  Columns 22 through 24

   0.068424371644624   0.061532285540836   0.055353859470052

  Columns 25 through 26

   0.049817594326836   0.044858120540568

CallPricesMC =

  Columns 1 through 3

   0.535079517868532   0.494810146703504   0.456255694906167

  Columns 4 through 6

   0.419533719891856   0.384718295898882   0.351864106150636

  Columns 7 through 9

   0.321032685243787   0.292228056257835   0.265430566708540

  Columns 10 through 12

   0.240623216862372   0.217746686978236   0.196731891863288

  Columns 13 through 15

   0.177491292631488   0.159951634301360   0.144002082599299

  Columns 16 through 18

   0.129535294334686   0.116454232218809   0.104660694057106

  Columns 19 through 21

   0.094042443071981   0.084492804429072   0.075925025204816

  Columns 22 through 24

   0.068247677286548   0.061371481198637   0.055213059256316

  Columns 25 through 26

   0.049713465537585   0.044797542080101

Look at comparison of analytic and monte carlo call prices

---

### #2032 — Amin (Topic Author)
*October 28, 2023, 11:27 PM*

Here is the matlab program used to create above graphs and call prices. This is still an intermediate program and will
go through several major changes.

.

.

.

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
gammaX=.55;
%%%%%%%%`%%%%%
V0=.35;
thetaV=.06;
kappaV=1.250;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.95;
sigma0=1.05;

dt=.03125/2;
Tt=64*2;

T=Tt*dt;

%%%%%%%%%%%%%%%%%%%%%%%%5
rng(82139475, 'twister')
paths=500000;
V(1:paths)=V0;  %Original process monte carlo.
X(1:paths)=X0;
paths0=paths/2;
paths00=paths/4;
Random1(1:paths00)=0;
Random2(1:paths0)=0;

for tt=1:Tt

Random2=randn(size(Random2));
Random1=randn(size(Random1));
Random1(paths00+1:2*paths00)=-1*Random1(1:paths00);
Random2(paths0+1:2*paths0)=-1*Random2(1:paths0);
Random1(paths0+1:2*paths0)=Random1(1:paths0);
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random1(1:paths)*1/sqrt(3)*dt^1.5+ ...
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
    rho.* sigma1.* V(1:paths).^gammaV .*X(1:paths).^gammaX
.*sigma0.*V(1:paths).^gamma.*Random2(1:paths)*1/sqrt(3)*dt^1.5;

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

X(XCallStrikes(nn))
            CallPricesMC(nn)=CallPricesMC(nn)+(X(pp)-CallStrikes(nn))/paths;
        end
    end
end

SVolMeanAnalytic=thetaV+exp(-kappaV*T)*(V0-thetaV)
SVolMean=sum(V(1:paths))/paths
AssetMeanAnalytic=thetaX+exp(-kappaX*T)*(X0-thetaX)
AssetMean=sum(X(1:paths))/paths

NoOfBinsV=500;
MaxCutOffV=12.750;

[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_EquiProbGridLS(X,V,paths,NoOfBinsV,MaxCutOffV);
%[aa0,aa,VProbMass,IndexMaxV,Vm,Zv] =
FindConditionalZSeriesXAndZyFromSimulation_nonUGridLS(X,V,paths,NoOfBinsV,MaxCutOffV,gamma);
%The function above finds numerically calculated conditional Z-series coefficietns associated with each volatility grid
cell.
%aa0 is zeroth coefficient/median array while aa is a matrix of (5 X NoOfBins+1) coeffs.
%Zv

%str=input("Look at Zv");

%The series of functions below take each coefficient array and convert it
%to a Z_series of analytic coeffs dependent on Zv. I will explain this
%further in a separate post on wilmott.

[coeff0,coeff]= FindZSeriesByPolynomialRegressionOnUnderlyingZ(aa0,Zv,VProbMass,IndexMaxV)
display("Look at coeffs of conditional median");
PlotZSeriesDensity(coeff0,coeff,'r');
 %str=input("Look at coeff density--0")

Coeff(1,1)=coeff0;
Coeff(1,2:6)=coeff(1:5);

[coeff0,coeff] = FindZSeriesByPolynomialRegressionOnUnderlyingZ(aa(1,:),Zv,VProbMass,IndexMaxV)
 PlotZSeriesDensity(coeff0,coeff,'r');
 str=input("Look at coeff density--1")
Coeff(2,1)=coeff0;
Coeff(2,2:6)=coeff(1:5);

[coeff0,coeff] = FindZSeriesByPolynomialRegressionOnUnderlyingZ(aa(2,:),Zv,VProbMass,IndexMaxV)
 PlotZSeriesDensity(coeff0,coeff,'r');
 str=input("Look at coeff density--2")
Coeff(3,1)=coeff0;
Coeff(3,2:6)=coeff(1:5);

%[Coeff(3,1),Coeff(3,2:6)] = CheckAndFixTheZSeriesDensityC5(coeff0,coeff)

[coeff0,coeff] = FindZSeriesByPolynomialRegressionOnUnderlyingZ(aa(3,:),Zv,VProbMass,IndexMaxV)
 PlotZSeriesDensity(coeff0,coeff,'r');
 str=input("Look at coeff density--3")
Coeff(4,1)=coeff0;
Coeff(4,2:6)=coeff(1:5);

[coeff0,coeff] = FindZSeriesByPolynomialRegressionOnUnderlyingZ(aa(4,:),Zv,VProbMass,IndexMaxV)
 PlotZSeriesDensity(coeff0,coeff,'r');
Coeff(5,1)=coeff0;
Coeff(5,2:6)=coeff(1:5);

[coeff0,coeff] = FindZSeriesByPolynomialRegressionOnUnderlyingZ(aa(5,:),Zv,VProbMass,IndexMaxV)
 PlotZSeriesDensity(coeff0,coeff,'r');
 str=input("Look at coeff density--5")
Coeff(6,1)=coeff0;
Coeff(6,2:6)=coeff(1:5);

for indexV=1:-1
%for indexV=1:IndexMaxV

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

    [Zc]=CalculateZgivenXAndZSeriesBisection2C5Improved(0,b0,b);

    [aH0,aH] = ConvertZCoeffsToHCoeffs(b0,b,5);

    MeanXv(indexV)= (aH0)*(1-normcdf(Zc))+exp(-.5*Zc^2)/sqrt(2*pi)*(aH(1) + aH(2) *Zc + aH(3)* (Zc^2-1) + aH(4) *(Zc^3 -
3 *Zc) + aH(5) *(Zc^4 -6 * Zc^2 +3));
    MeanXv(indexV);
    aH0;

    b0=b0/MeanXv(indexV);
    b=b/MeanXv(indexV);

    PlotZSeriesDensity(b0,b,'r');
    title(sprintf('Conditional V=%.3f,Zv=%.3f,x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
Vm(indexV),Zv(indexV), X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));
    legend({'Conditional Asset density From numerical Z-series','Conditional Asset density From new analytic Coeffs
Z-series'},'Location','northeast')
    xlabel('Asset'), ylabel('Conditional Asset Density')
    display(fprintf('conditional value of stochastic volatility Grid cell for this graph: V=%.3f,Zv=%.3f,SV grid cell
number = %.1f, Total SV Grid Cells=%.1f',Vm(indexV),Zv(indexV),indexV, IndexMaxV));
%    str=input("Lok at comparison of numerically calculated conditional asset density and analytic coeffs conditional
asset density plots")
    hold off
end

%MeanXv

%MeanXvCorrected
%str=input("Look at mean Asset");

[a0,a] = FindZSeriesByPolynomialRegressionOnUnderlyingZ(Vm,Zv,VProbMass,IndexMaxV);
% Zv
% VProbMass
% Vm
% IndexMaxV
% str=input("Look at variables--0101010");
% %[a0,a] = CheckAndFixTheZSeriesDensityC5(a0,a);
% %[a0,a] = FindZSeriesCoeffsByInnerProduct(Vm,Zv,VProbMass,IndexMaxV);
% clf;
% PlotZSeriesDensity(a0,a,'r');
% hold on
% MaxCutOff=5;
% NoOfBins=1200;%round(1*500*gamma^2*4*sigma0/sqrt(MCMean)/(1+kappa))*1;%Decrease the number of bins if the graph is too
% [YDensity,IndexOutY,IndexMaxY] = MakeDensityFromSimulation_Infiniti_NEW(V,paths,NoOfBins,MaxCutOff );
% plot(IndexOutY(1:IndexMaxY),YDensity(1:IndexMaxY),'g');
%
% str=input("Look at comparison of density graphs");
% hold off

%Please note that for drawing bivariate density of asset and stochastic volatility, grid parameters have changed from
brom before in below.

NoOfBinsV=200;
NoOfBinsX=200;
MaxCutOffX=7;
MaxCutOffV=1.75;

%[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv]=
Find2DDensityAndCDFFromSimulation_Infiniti(X,V,paths,NoOfBinsX,NoOfBinsV);
[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv,BinSizeX,BinSizeV]=
Find2DDensityAndCDFFromSimulation_Infiniti04(X,V,paths,NoOfBinsX,NoOfBinsV,MaxCutOffX,MaxCutOffV);
%[XYProbDensity2D,XYProbMass2D,XProbMass,YProbMass,IndexMaxX,IndexMaxY,Xn,Ym,Zx,Zy,BinSizeX,BinSizeY]
%Please look at matlab file of above function for etailed explanation of
%all its input and output parameters.

surf(Xn,Vm,transpose(XYProbDensity2D));

xlabel('Asset'), ylabel('Stochastic Volatility'), zlabel('Probability Density 2D')
title('Graph of 2D Density of Asset and SV from Parzen Density')

[pXY2D] = Calculate2VariablesOn2DGridFromAnalyticZSeries(Xn,Vm,NoOfBinsX,NoOfBinsV,Coeff,a0,a);
%[pXY2D] = Calculate2VariablesOn2DGridFromAnalyticZSeries(XX,YY,NoOfBinsX,NoOfBinsY,Coeff,a0,a)

surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(XYProbDensity2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Numerical Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and Volatility')

str=input("Look at numerical bivariate density of Asset and Stochastic Volatility")
surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(pXY2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Analytic Density : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at Analytic density of Asset and Stochastic volatility")
surf(Xn(2:NoOfBinsX+1),Vm(3:NoOfBinsV+1),transpose(pXY2D(2:NoOfBinsX+1,3:NoOfBinsV+1)-XYProbDensity2D(2:NoOfBinsX+1,3:NoOfBinsV+1)))
title(sprintf('Difference of Analytic and Numerical Density  : x0 =
%.4f,gammaX=%.3f,sigmaX=%.2f,gammaV=%.3f,v0=%.3f,kappaV=%.3f,thetaV=%.3f,gamma=%.3f,sigma0=%.3f,T=%.2f',
X0,gammaX,sigma1,gammaV,V0,kappaV,thetaV,gamma,sigma0,T));%,sprintf('theta= %f', theta), sprintf('kappa = %f',
kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));
xlabel('Asset'), ylabel('Stochastic Volatility'),zlabel('Bivariate Density of Asset and stochastic Volatility')

str=input("Look at difference of numerical and analytic densities of Asset and stochastic volatility")

CallStrikes=[.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75]

VolZEquiDistGridSize=200;
[CallPricesAnalytic]=PriceCallArrayOver2DDensity(a0,a,Coeff,CallStrikes,VolZEquiDistGridSize);
CallPricesAnalytic
CallPricesMC

str=input("Look at comparison of analytic and monte carlo call prices");

end

```

.

.

.

```
function [a0,a,YProbMass,NoOfBinsW,Ym,Zy] =
FindConditionalZSeriesXAndZyFromSimulation_EquiProbGridLS(X,Y,Paths,NoOfBinsW,MaxCutOffY)

Y(Y>MaxCutOffY)=MaxCutOffY;

[Ys,I]=sort(Y);

%Below A(nn) is first element of nnth subdivision and
%B(nn) is last element of nnth subdivision.

A(1)=1;
for nn=2:NoOfBinsW
A(nn)=A(nn-1)+floor(Paths/NoOfBinsW+.5);
B(nn-1)=A(nn)-1;
end
B(NoOfBinsW)=Paths;

%A
%B
Pv(1)=B(1)-A(1)+1;

%pv(nn) is number of volatility paths in nnth subdivision.

if(rem(Pv(1),2)==0)
    YCDF(1)=((B(1)-A(1))/2+.5)/Paths;
    YCDF0(1)=((B(1)-A(1))+1)/Paths;
else
    YCDF(1)=((B(1)-A(1))/2+.5)/Paths;
    YCDF0(1)=((B(1)-A(1))+1)/Paths;
end

%Below we find equi-probable normal density array once instead of
%calculating it again and again in every loop. This can be calculated once
%since the number of asset paths are the same in each of the volatility
%grid subdivisons.

%Below we find the number of asset paths from first subdivision and later
%continue to use this number for later subdivions since number of asset
%paths are the same in all of the volatility grid subdivisions
    Ndata=Pv(1);
    Sigma=1;
    [ZI] = StandardNormalIdealDesity02(Ndata,Sigma);
%Below we match the even moments of the equi-probable normal array with
%true moments
    [ZI] = MatchMomentsOfIdealZhalf(ZI);

for indexW=1:NoOfBinsW

pv(indexW)=B(indexW)-A(indexW)+1;

%Below Xv are asset paths array that lie in indexW-th subdivision.
 Xv(1:pv(indexW),indexW)=X(I(A(indexW):B(indexW)));
 Mean(indexW)=sum(Xv(:,indexW))./pv(indexW);
 Var(indexW)=sum((Xv(:,indexW)-Mean(indexW)).^2)/pv(indexW);

 Xv(:,indexW)=Xv(:,indexW)./Mean(indexW);
 %Xv(:,indexW)=(Xv(:,indexW)-Mean(indexW))./sqrt(Var(indexW));
 Xv0(1:pv(indexW))=Xv(1:pv(indexW),indexW);
 ZProb(1:pv(indexW))=1/pv(indexW);
 [a0(indexW),a(:,indexW)] = CalculateZSeriesDensityByIdealMeasureMean05WithZI(Xv0,ZI,ZProb);

  %  MeanMu=a0(indexW)+a(2,indexW)+3*a(4,indexW);
  %  MCorrection=1-MeanMu %In our new latest version, this MCorrection is virtually zero.
  %  a0(indexW)=a0(indexW)+MCorrection;

if(rem(pv(indexW),2)==0)
    Ym(indexW)=Ys(floor((B(indexW)+A(indexW))/2));
    if(indexW>1)
    YCDF(indexW)=YCDF0(indexW-1)+((B(indexW)-A(indexW))+1)/Paths/2;
    YCDF0(indexW)=YCDF0(indexW-1)+((B(indexW)-A(indexW))+1)/Paths;
    end
else

    Ym(indexW)=Ys(B(indexW)+A(indexW))/2+Ys(B(indexW)+A(indexW)+1)/2;
    if(indexW>1)
    YCDF(indexW)=YCDF0(indexW-1)+((B(indexW)-A(indexW))+1)/Paths/2;
    YCDF0(indexW)=YCDF0(indexW-1)+((B(indexW)-A(indexW))+1)/Paths;
    end
end
YProbMass(indexW)=pv(indexW)/Paths;
Zy(indexW)=norminv(YCDF(indexW));

end

%Zy
%YCDF
%YCDF0
%str=input("Look at CDF values and Zv");

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
function [ZnNew] = MatchMomentsOfIdealZhalf(Zn)

Ndata=length(Zn);
if(rem(Ndata,2)==0)
    Nh=Ndata/2;
else
    Nh=(Ndata+1)/2;
end

% Ndata
% Nh
% str=input("Look at number of data points");

if(Ndata100)&&(Ndata500)&&(Ndata1000)&&(Ndata3000)&&(Ndata6000)&&(Ndata10000)
    Iterations=500;
end
alpha=1;
beta=0;
gamma=0;

Moment2=sum(Zn(1:Ndata).^2)*1/Ndata
Moment4=sum(Zn(1:Ndata).^4)*1/Ndata
Moment6=sum(Zn(1:Ndata).^6)*1/Ndata
display("Initial Moments");

ZnNew(1:Nh)=Zn(1:Nh).*(alpha+beta*(Zn(1:Nh).^2-1)+gamma*(Zn(1:Nh).^4-6*Zn(1:Nh).^2+3));

w1=5000;
w2=200;

ObjFuncBest=(Moment2-1).^2*w1+(Moment4-3).^2*w2+(Moment6-15).^2;

delta_alpha=.00025;
delta_beta=.0002;
delta_gamma=.0002;
alphaSuccessCount=0;
betaSuccessCount=0;
gammaSuccessCount=0;
SuccessPrevalpha=0;
SuccessPrevbeta=0;
SuccessPrevgamma=0;

mul1=.9;
mul2=1.1;

for iter=1:Iterations
    alphaNew=alpha+delta_alpha;
    betaNew=beta;
    gammaNew=gamma;
    ZnNew(1:Nh)=Zn(1:Nh).*(alphaNew+betaNew*(Zn(1:Nh).^2-1)+gammaNew*(Zn(1:Nh).^4-6*Zn(1:Nh).^2+3));
    Moment2=sum(ZnNew(1:Nh).^2)*1/Ndata*2;
    Moment4=sum(ZnNew(1:Nh).^4)*1/Ndata*2;
    Moment6=sum(ZnNew(1:Nh).^6)*1/Ndata*2;

    ObjFuncNew=(Moment2-1).^2*w1+(Moment4-3).^2*w2+(Moment6-15).^2;

    if(ObjFuncNew4)
        delta_alpha=delta_alpha*mul2;
    end
    if(betaSuccessCount>4)
        delta_beta=delta_beta*mul2;
    end
    if(gammaSuccessCount>4)
        delta_gamma=delta_gamma*mul2;
    end
end

ZnNew(1:Ndata)=Zn(1:Ndata).*(alpha+beta*(Zn(1:Ndata).^2-1)+gamma*(Zn(1:Ndata).^4-6*Zn(1:Ndata).^2+3));

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
function [y0] = InterpolateOrderN6(N,x0,x1,x2,x3,x4,x5,x6,y1,y2,y3,y4,y5,y6)

if(N==6)
y0=(x0-x2).*(x0-x3).*(x0-x4).*(x0-x5).*(x0-x6)./((x1-x2).*(x1-x3).*(x1-x4).*(x1-x5).*(x1-x6)).*y1+ ...
   (x0-x1).*(x0-x3).*(x0-x4).*(x0-x5).*(x0-x6)./((x2-x1).*(x2-x3).*(x2-x4).*(x2-x5).*(x2-x6)).*y2+ ...
   (x0-x1).*(x0-x2).*(x0-x4).*(x0-x5).*(x0-x6)./((x3-x1).*(x3-x2).*(x3-x4).*(x3-x5).*(x3-x6)).*y3+ ...
   (x0-x1).*(x0-x2).*(x0-x3).*(x0-x5).*(x0-x6)./((x4-x1).*(x4-x2).*(x4-x3).*(x4-x5).*(x4-x6)).*y4+ ...
   (x0-x1).*(x0-x2).*(x0-x3).*(x0-x4).*(x0-x6)./((x5-x1).*(x5-x2).*(x5-x3).*(x5-x4).*(x5-x6)).*y5+ ...
   (x0-x1).*(x0-x2).*(x0-x3).*(x0-x4).*(x0-x5)./((x6-x1).*(x6-x2).*(x6-x3).*(x6-x4).*(x6-x5)).*y6;
end

if(N==5)
y0=(x0-x2).*(x0-x3).*(x0-x4).*(x0-x5)./((x1-x2).*(x1-x3).*(x1-x4).*(x1-x5)).*y1+ ...
   (x0-x1).*(x0-x3).*(x0-x4).*(x0-x5)./((x2-x1).*(x2-x3).*(x2-x4).*(x2-x5)).*y2+ ...
   (x0-x1).*(x0-x2).*(x0-x4).*(x0-x5)./((x3-x1).*(x3-x2).*(x3-x4).*(x3-x5)).*y3+ ...
   (x0-x1).*(x0-x2).*(x0-x3).*(x0-x5)./((x4-x1).*(x4-x2).*(x4-x3).*(x4-x5)).*y4+ ...
   (x0-x1).*(x0-x2).*(x0-x3).*(x0-x4)./((x5-x1).*(x5-x2).*(x5-x3).*(x5-x4)).*y5;
end
if(N==4)
y0=(x0-x2).*(x0-x3).*(x0-x4)./((x1-x2).*(x1-x3).*(x1-x4)).*y1+ ...
   (x0-x1).*(x0-x3).*(x0-x4)./((x2-x1).*(x2-x3).*(x2-x4)).*y2+ ...
   (x0-x1).*(x0-x2).*(x0-x4)./((x3-x1).*(x3-x2).*(x3-x4)).*y3+ ...
   (x0-x1).*(x0-x2).*(x0-x3)./((x4-x1).*(x4-x2).*(x4-x3)).*y4;
end
if(N==3)
y0=(x0-x2).*(x0-x3)./((x1-x2).*(x1-x3)).*y1+ ...
   (x0-x1).*(x0-x3)./((x2-x1).*(x2-x3)).*y2+ ...
   (x0-x1).*(x0-x2)./((x3-x1).*(x3-x2)).*y3;
end
if(N==2)
y0=(x0-x2)./((x1-x2)).*y1+ ...
   (x0-x1)./((x2-x1)).*y2;
end

%y0=(x0-x3)/(x2-x3)*y2+(x0-x2)/(x3-x2)*y3;

end
```

.

.

.

```
function [a0,a] = FindZSeriesByPolynomialRegressionOnUnderlyingZ(aa0,Zy,VProbMass,IndexMaxV)

[Zy] = MatchMomentsOfIdealZhalf(Zy);

x0=0;
x1=Zy(IndexMaxV/2-3);
x2=Zy(IndexMaxV/2-2);
x3=Zy(IndexMaxV/2-1);
x4=Zy(IndexMaxV/2+1);
x5=Zy(IndexMaxV/2+2);
x6=Zy(IndexMaxV/2+3);

y1=aa0(IndexMaxV/2-3);
y2=aa0(IndexMaxV/2-2);
y3=aa0(IndexMaxV/2-1);
y4=aa0(IndexMaxV/2+1);
y5=aa0(IndexMaxV/2+2);
y6=aa0(IndexMaxV/2+3);
N=6;
[y0] = InterpolateOrderN6(N,x0,x1,x2,x3,x4,x5,x6,y1,y2,y3,y4,y5,y6);
%Median0=(aa0(IndexMaxV/2)+aa0(IndexMaxV/2+1))/2
Median=y0;
%ZyMedian=(Zy(IndexMaxV/2)+Zy(IndexMaxV/2+1))/2

%aa0
%Median0
Median
%ZyMedian
%str=input("Look at median");
Zu=0;
Ymu(1:IndexMaxV,1)=aa0(1:IndexMaxV)-Median;
for nn=1:IndexMaxV
    X(nn,1)=1;
    X(nn,2)=(Zy(nn)-Zu);
    X(nn,3)=(Zy(nn)-Zu).^2;
    X(nn,4)=(Zy(nn)-Zu).^3;
    X(nn,5)=(Zy(nn)-Zu).^4;
    X(nn,6)=(Zy(nn)-Zu).^5;

end

coeff=(X'*X)$X'*Ymu);
c0=coeff(1,1);
c(1:5)=coeff(2:6,1);

a0=c0;
a=c;
a0=a0+Median;

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

%clf;
plot(Z(1:Nn),Y(1:Nn),Color);
title('Graph of Z-Series Variable as a function of underlying standard normal');
str=input('Look at Graph of Z-Series Variable as a function of underlying standard normal');

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
%Za, We find Zmid=(Za+Zb)/2. We then evaluate Y(Zmid) and if Y  Y(Zmid), we assign the lower band value equal to Zmid as
Za=Zmid. In a
% few iterations, this bisection procedure gets extremely close to true
% value of Z for which Y(Z)=Y

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

if(Y  EvaluateZSeriesC5(c0,c,-.5))|| (EvaluateZSeriesdXdZC5(c0,c,-.5)  EvaluateZSeriesC5(c0,c,-1))||
(EvaluateZSeriesdXdZC5(c0,c,-1)  EvaluateZSeriesC5(c0,c,-1.5))|| (EvaluateZSeriesdXdZC5(c0,c,-1.5) 
EvaluateZSeriesC5(c0,c,-2))|| (EvaluateZSeriesdXdZC5(c0,c,-2)  EvaluateZSeriesC5(c0,c,-2.5))||
(EvaluateZSeriesdXdZC5(c0,c,-2.5)  EvaluateZSeriesC5(c0,c,-3))|| (EvaluateZSeriesdXdZC5(c0,c,-3.0) 
EvaluateZSeriesC5(c0,c,-3.5))|| (EvaluateZSeriesdXdZC5(c0,c,-3.5)  EvaluateZSeriesC5(c0,c,-4))||
(EvaluateZSeriesdXdZC5(c0,c,-4)  EvaluateZSeriesC5(c0,c,-4.5))|| (EvaluateZSeriesdXdZC5(c0,c,-4.5) 
EvaluateZSeriesC5(c0,c,-5))|| (EvaluateZSeriesdXdZC5(c0,c,-5)  EvaluateZSeriesC5(c0,c,-5.5))||
(EvaluateZSeriesdXdZC5(c0,c,-5.5)  EvaluateZSeriesC5(c0,c,-6.0))|| (EvaluateZSeriesdXdZC5(c0,c,-6)
EvaluateZSeriesC5(c0,c,Zmid))
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
function [Z] = CalculateZgivenXAndZSeriesC5Improved(X,c0,c)

Z(1:length(X))=0;

for nn=1:length(X)
    %X(nn)
    %c0
        Z(nn)=CalculateZgivenXAndZSeriesBisection2C5Improved(X(nn),c0,c);
    %Z(nn)
end

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
function [XYProbDensity2D,XYProbMass2D,XProbMass,YProbMass,IndexMaxX,IndexMaxY,Xn,Ym,Zx,Zy,BinSizeX,BinSizeY] =
Find2DDensityAndCDFFromSimulation_Infiniti04(X,Y,Paths,NoOfBinsX,NoOfBinsY,MaxCutOffX,MaxCutOffY)

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

```
function [pXY2D] = Calculate2VariablesOn2DGridFromAnalyticZSeries(XX,YY,NoOfBinsX,NoOfBinsY,Coeff,a0,a)

%YY are Y-coordinates of 2D Grid. In our case this is stochastic
%volatility and is univariate and independent of asset so it can be
%inverted as a univariate Z-series. its Z-series is given by a0 and a.

[Zy] = CalculateZgivenXAndZSeriesC5Improved(YY,a0,a);

% for mm=1:NoOfBinsY+1
%     if(Zy(mm)>2.5)
%         if(Zy(mm+1)>.5+Zy(mm))
%             Zy(mm+1:NoOfBinsY+1)=Zy(mm);
%         end
%     end
% end

% for mm=1:NoOfBinsY+1
%     if(Zy(mm)>7)
%         Zy(mm)=7;
%     end
%     if(Zy(mm)7)
%         Zx(nn,mm)=7;   %possible error block
%     end
%     if(Zx(nn,mm)<-7)
%         Zx(nn,mm)=-7;   %possible error block
%     end
% %    if(Zx(nn+1,mm)<Zx(nn,mm))
% %        Zx(nn+1,mm)=Zx(nn,mm);   %possible error block
% %    end
%     end
% end

% %Below we make calculations of density in original coordinates by doing
% %change of probability derivative with respect to gaussian density.
% DinvfXX(1:NoOfBinsX+1,1:NoOfBinsY+1)=0;
% for mm=2:NoOfBinsY
%     for nn=2:NoOfBinsX
%
%         DinvfXX(nn,mm) = (Zx(nn + 1,mm) - Zx(nn - 1,mm))/(XX(nn + 1) - XX(nn - 1));
%
%     end
%     DinvfXX(NoOfBinsX+1,mm)=DinvfXX(NoOfBinsX,mm);
%     DinvfXX(1,mm)=DinvfXX(2,mm);
% end
% DinvfXX(:,1)=DinvfXX(:,2);
% DinvfXX(:,NoOfBinsY+1)=DinvfXX(:,NoOfBinsY);

%Below we make calculations of density in original coordinates by doing
%change of probability derivative with respect to gaussian density.
DinvfXX(1:NoOfBinsX+1,1:NoOfBinsY+1)=0;
for mm=1:NoOfBinsY
    %DinvfXX(1,mm)= (Zx(1 + 1,mm) - Zx(1,mm))/(XX(1 + 1) - XX(1));
    for nn=2:NoOfBinsX

        DinvfXX(nn,mm) = (Zx(nn + 1,mm) - Zx(nn - 1,mm))/(XX(nn + 1) - XX(nn - 1));

    end
    %DinvfXX(nn,mm) = (Zx(nn + 1,mm) - Zx(nn - 1,mm))/(XX(nn + 1) - XX(nn - 1));
    DinvfXX(NoOfBinsX+1,mm)=DinvfXX(NoOfBinsX,mm);
    DinvfXX(1,mm)=DinvfXX(2,mm);
end

DinvfYY(1:NoOfBinsY+1)=0;
%DinvfYY(1) = (Zy(1+1) - Zy(1))/(YY(1 + 1) - YY(1));
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

```
function [CallPrices]=PriceCallArrayOver2DDensity(a0,a,Coeff,CallStrikes,VolZEquiDistGridSize)

NoOfCallStrikes=length(CallStrikes);

%dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=VolZEquiDistGridSize;  % No of normal density subdivisions
dNn=(8)/Nn;
NnMid=((1+Nn)/2)*dNn;
Zv(1:Nn)=(((1:Nn)*dNn)-NnMid);
ZProb(1)=normcdf(.5*Zv(1)+.5*Zv(2),0,1)-normcdf(.5*Zv(1)+.5*Zv(2)-dNn,0,1);
ZProb(Nn)=normcdf(.5*Zv(Nn)+.5*Zv(Nn-1)+dNn,0,1)-normcdf(.5*Zv(Nn)+.5*Zv(Nn-1),0,1);
ZProb(2:Nn-1)=normcdf(.5*Zv(2:Nn-1)+.5*Zv(3:Nn),0,1)-normcdf(.5*Zv(2:Nn-1)+.5*Zv(1:Nn-2),0,1);

%ZProb(3:Nn)=ZProb(3:Nn).*1./sum(ZProb(3:Nn));

CallPriceV(1:Nn,1:NoOfCallStrikes)=0;

CallPrices(1:NoOfCallStrikes)=0;

for indexV=1:Nn

    V(indexV)=a0 + a(1)*Zv(indexV)+a(2)*Zv(indexV).^2+a(3).*Zv(indexV).^3+a(4).*Zv(indexV).^4+a(5).*Zv(indexV).^5;

       
b0=Coeff(1,1)+Coeff(1,2).*Zv(indexV)+Coeff(1,3).*Zv(indexV).^2+Coeff(1,4).*Zv(indexV).^3+Coeff(1,5).*Zv(indexV).^4+Coeff(1,6).*Zv(indexV).^5;

    for mm=2:6
       
b(mm-1)=Coeff(mm,1)+Coeff(mm,2).*Zv(indexV)+Coeff(mm,3).*Zv(indexV).^2+Coeff(mm,4).*Zv(indexV).^3+Coeff(mm,5).*Zv(indexV).^4+Coeff(mm,6).*Zv(indexV).^5;
    end
    %if(V(indexV)>0)
    [Zc]=CalculateZgivenXAndZSeriesBisection2C5(0,b0,b);

    [aH0,aH] = ConvertZCoeffsToHCoeffs(b0,b,5);

    MeanXv(indexV)= (aH0)*(1-normcdf(Zc))+exp(-.5*Zc^2)/sqrt(2*pi)*(aH(1) + aH(2) *Zc + aH(3)* (Zc^2-1) + aH(4) *(Zc^3 -
3 *Zc) + aH(5) *(Zc^4 -6 * Zc^2 +3));

    b0=b0/MeanXv(indexV);
    b=b/MeanXv(indexV);
    %end
    for ll=1:NoOfCallStrikes
        [CallPriceV(indexV,ll)] = ZSeriesCallIntegrate(CallStrikes(ll),b0,b);

        if(CallPriceV(indexV,ll) <0 )
            CallPriceV(indexV,ll)=0;
        end

    end

end
% for ss=1:12
% CallPriceV(ss,:)=CallPriceV(13,:);
% CallPriceV(Nn-ss+1,:)=CallPriceV(Nn-12,:);
% end
for indexV=1:Nn
    for ll=1:NoOfCallStrikes
        CallPrices(ll)=CallPrices(ll)+CallPriceV(indexV,ll).*ZProb(indexV);
    end
end

%CallPriceV
%str=input("Look at conditional call prices");

end

```

.

.

.

```
function [CallPrice] = ZSeriesCallIntegrate(Xc,a0,a)

[Zc]=CalculateZgivenXAndZSeriesBisection2C5(Xc,a0,a);

[aH0,aH] = ConvertZCoeffsToHCoeffs(a0,a,5);

CallPrice= (aH0-Xc)*(1-normcdf(Zc))+exp(-.5*Zc^2)/sqrt(2*pi)*(aH(1) + aH(2) *Zc + aH(3)* (Zc^2-1) + aH(4) *(Zc^3 - 3
*Zc) + aH(5) *(Zc^4 -6 * Zc^2 +3));

end

```

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
%Za, We find Zmid=(Za+Zb)/2. We then evaluate Y(Zmid) and if Y  Y(Zmid), we assign the lower band value equal to Zmid as
Za=Zmid. In a
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

---

### #2033 — Amin (Topic Author)
*October 30, 2023, 7:51 AM*

Friends, I am writing this post to inform friends about my increasing persecution everyday.

Corrupt American defense is extremely upset that I have exposed them all over the world and self stylized masters of the
universe (read scumloads of the universe ) are trying everything to finally succeed in retarding me what they have
always failed to do. The whole Lahore city is being drugged by puppet Pakistani army. This time it is unprecedented.
Mind control drugs have been given to food shops and street restaurants in most parts of the city and they keep adding
these drugs to their food when they prepare the food. Bakeries had been drugging their entire food for several weeks and
I have been totally avoiding them as a rule. Water manufactured by Nestle, Coca-cola and pepsi, which are three largest
bottled water distributors who capture 90% of the bottled water market, is thoroughly drugged with mind control drugs.
Underground water is also drugged in most parts of the city. Water by other large bottled water companies is also
drugged but I have survived by buying bottled water from some very small manufacturers but such water is only found in a
some isolated shops in lower middle class areas where it has been leftover in stock from scorching summers. Pakistan
army is trying to plug this gap by approaching very small water manufacturers across the city and giving them mind
control drugs to add to their water so I cannot continue to bank on such good bottled from very small manufacturers for
a very long time.

Even fruit like bananas and many other types of fruit are also being drugged with mind control chemicals on orders of
corrupt Pakistan army. Today I bought bananas from a random fruit stall and I picked the bananas myself but I was losing
my nerves after eating just one of the bananas. I am sure they are also drugging the fruit in several neighborhoods
where I frequently go to take food.

Most of the fresh juice shops and stalls in large parts of the city where I frequently go are adding drugs to their
fruit juices. I used to drink a lot of freshly squeezed grapefruit juice(which can cost as low as 30 cents for a 450 ml
glass) but they approached most of the fruit juice shops and small trolleys and I have been hit many times even though I
ask the small vendor to wash the juice container and squeeze the juice from machine in front of me and I do not allow
any them to add any salt or anything but still they sometimes show dexterity of their hand. One fruit juice owner, after
giving me the glass of juice, when I had drunk half the glass, asked me that very little juice was leftover in the juice
container and he wanted to add it to my glass as well for free. I was deceived by his nice offer. He had mixed some
drugs in the juice in the container while I was carelessly drinking the good juice glass that was made before my eyes. I
just took only one sip of the juice after he added more juice to my glass and I realized that it was drugged. I did not
drink any more juice but I remained under a hangover for more than eight hours even though I took a lot of good food
that I had on myself.

They had not been using strong gases in my room for past few weeks but today when I returned after bringing my mother
from her class, I noticed that there was some new gas in my room and it was strongly affecting my brain. It was due to
this gas that I decided to write this post.

And a lot of Pakistan army secret services people follow me when I try to go out to buy good food. It is a large city
and I have been trying a lot of new areas of the city where I did not use to go before. The way they have drugged
several neighborhoods, it would have been impossible for me to survive with my sanity. If I did not keep trying new
areas, I would have lost most of my good neurotransmitters by now. When I take good food from street restaurant in some
different remote area, the shop owner is asked (from voice to skull) to use all sort of delaying tactics to keep me in
wait until somebody from outside would approach with mind control drugs that have to be added to my food. This happens
everyday and many times I have to be almost rude to insist the shop owners to finally give me cooked food that is
already lying in the tray from before and there is no other customer.

I also believe they have plans to give me very strong mind control drugs somewhere and then make me agitated after
provocation from someone possibly in my family and then declare me mentally unstable again and then the new psychiatrist
would tell me that psychiatric treatment never worked for me since I did heavy mental work in form of mathematics
research and I most stop all mathematics research in order to finally get well and become mentally healthy.

I did not write about this increasing drugging of food earlier since I thought many good friends might already be aware
about it from their sources and I did not want to appear that I keep whining regularly. And I really never thought they
would go to this extent and they are not backing off. They are only increasing the drugging of the city. I was really
sure they would stop once I continue to evade them for a long time but they continue to up the ante everyday and
increasingly try to drug the city more thoroughly on a continuing basis.

---

### #2034 — Amin (Topic Author)
*October 30, 2023, 1:37 PM*

Friends, even though a large number of good Americans now know the complete truth about connivance between American
defense and jewish billionaire goldfather of mind control(and his rich jewish cohort), it is surprising that American
defense has greatly increased the cruel mind control of innocent victims instead of decreasing their mind control as
anybody would otherwise expect. I really think that scum-load crooks of defense have absolutely no intention of
decreasing mind control of innocent people anywhere much less end the mind control altogether. I had already told good
American people that most of these scum-loads in defense are dying and very bitterly waiting for the tens of millions of
dollars of jobs that they are offered by machinatory jewish cohort after their retirement. These scum-load crooks have
absolutely no intention of giving up the great life they would have to forego when they would end the mind control of
innocent people that they have continued for so long on behalf of machinatory jews.

I really think that the only way to end mind control once and forever is to make some investigative journalist of some
prestigious newspaper do a comprehensive story on decades of mind control of totally innocent but intelligent people by
American defense on behest of machinatory jewish cohort. I want to assure people that there is probably no other way to
end cruel and inhuman mind control and even if good American friends make American defense decrease mind control
somewhat, these crooks will come back and increase mind control again only making sure this time that there would be no
resistance to cruel mind control anymore. Only way to make the cruel mind control end forever is to make it a social
taboo by exposing all actors behind it completely in public.

Today this is only mind control but as science advances many more ills in the society(like mind control) would be born
and then it would be impossible to end the jungle law in any society. I know many good American people are totally
shocked when they come to know the complete truth about mind control and degree of organized connivance behind it and it
is hard for them to believe that anything like that could ever exist in their civilized and otherwise humane society.

I recall when mind control started army in Pakistan was not  very bold to drug entire markets but CIA told them dirty
tricks and trained them how to approach people with concocted ethics and lies and now army soldiers in Pakistan have
become experts at all tricks that have to be used to convince food places to drug their entire food and tell all sort of
lies about the mind control victims and now the whole society works together to strangulate the mind control victims and
it is a common everyday practice in the society. Similarly scum-loads of CIA and American defense literally used science
to teach people how to successfully employ trickery and deception to advance mind control. Now many armies in our poor
country and elsewhere have become very skilled at this art of lying(with ethics), trickery and deception that they were
taught by CIA  and use this training to deceive people of our entire nation in every field and in every area of life.

---

### #2035 — Amin (Topic Author)
*October 30, 2023, 5:00 PM*

Friends, my yesterday's program has many limitations. for example it does not work well for options and density out to
four years and some other issues like that.

I was actually not very excited about the program and wanted to change many things but when I increased the equiprobable
grid size to 500 grid cells and made changes to Z-series inversion program, it unexpectedly worked very well for two
years and therefore I posted the program.

I want to make several large changes to the program and am currently planning and working on all the changes I want to
make. I really hope that nothing unforeseen happens and I hope to continue with the next research project to calculate
the conditional density of asset at the terminal time given(conditional on) both the value of asset and volatility at
some specified time in between start and terminal maturity of the option.

But first I want to make the current program more robust especially across larger time frames and also want to try
different algorithms to achieve this. We also have to tackle correlations. So this is a lot of interesting stuff that
will keep us busy for next few weeks or a month or so. And then we will move on to more interesting things after getting
our basics right.

---

### #2036 — Amin (Topic Author)
*October 30, 2023, 6:46 PM*

>
> Friends, I am writing this post to inform friends about my increasing persecution everyday.
>
> Corrupt American defense is extremely upset that I have exposed them all over the world and self stylized masters of
the universe (read scumloads of the universe ) are trying everything to finally succeed in retarding me what they have
always failed to do. The whole Lahore city is being drugged by puppet Pakistani army. This time it is unprecedented.
Mind control drugs have been given to food shops and street restaurants in most parts of the city and they keep adding
these drugs to their food when they prepare the food. Bakeries had been drugging their entire food for several weeks and
I have been totally avoiding them as a rule. Water manufactured by Nestle, Coca-cola and pepsi, which are three largest
bottled water distributors who capture 90% of the bottled water market, is thoroughly drugged with mind control drugs.
Underground water is also drugged in most parts of the city. Water by other large bottled water companies is also
drugged but I have survived by buying bottled water from some very small manufacturers but such water is only found in a
some isolated shops in lower middle class areas where it has been leftover in stock from scorching summers. Pakistan
army is trying to plug this gap by approaching very small water manufacturers across the city and giving them mind
control drugs to add to their water so I cannot continue to bank on such good bottled from very small manufacturers for
a very long time.
>
> Even fruit like bananas and many other types of fruit are also being drugged with mind control chemicals on orders of
corrupt Pakistan army. Today I bought bananas from a random fruit stall and I picked the bananas myself but I was losing
my nerves after eating just one of the bananas. I am sure they are also drugging the fruit in several neighborhoods
where I frequently go to take food.
>
> Most of the fresh juice shops and stalls in large parts of the city where I frequently go are adding drugs to their
fruit juices. I used to drink a lot of freshly squeezed grapefruit juice(which can cost as low as 30 cents for a 450 ml
glass) but they approached most of the fruit juice shops and small trolleys and I have been hit many times even though I
ask the small vendor to wash the juice container and squeeze the juice from machine in front of me and I do not allow
any them to add any salt or anything but still they sometimes show dexterity of their hand. One fruit juice owner, after
giving me the glass of juice, when I had drunk half the glass, asked me that very little juice was leftover in the juice
container and he wanted to add it to my glass as well for free. I was deceived by his nice offer. He had mixed some
drugs in the juice in the container while I was carelessly drinking the good juice glass that was made before my eyes. I
just took only one sip of the juice after he added more juice to my glass and I realized that it was drugged. I did not
drink any more juice but I remained under a hangover for more than eight hours even though I took a lot of good food
that I had on myself.
>
> They had not been using strong gases in my room for past few weeks but today when I returned after bringing my mother
from her class, I noticed that there was some new gas in my room and it was strongly affecting my brain. It was due to
this gas that I decided to write this post.
>
> And a lot of Pakistan army secret services people follow me when I try to go out to buy good food. It is a large city
and I have been trying a lot of new areas of the city where I did not use to go before. The way they have drugged
several neighborhoods, it would have been impossible for me to survive with my sanity. If I did not keep trying new
areas, I would have lost most of my good neurotransmitters by now. When I take good food from street restaurant in some
different remote area, the shop owner is asked (from voice to skull) to use all sort of delaying tactics to keep me in
wait until somebody from outside would approach with mind control drugs that have to be added to my food. This happens
everyday and many times I have to be almost rude to insist the shop owners to finally give me cooked food that is
already lying in the tray from before and there is no other customer.
>
> I also believe they have plans to give me very strong mind control drugs somewhere and then make me agitated after
provocation from someone possibly in my family and then declare me mentally unstable again and then the new psychiatrist
would tell me that psychiatric treatment never worked for me since I did heavy mental work in form of mathematics
research and I most stop all mathematics research in order to finally get well and become mentally healthy.
>
> I did not write about this increasing drugging of food earlier since I thought many good friends might already be
aware about it from their sources and I did not want to appear that I keep whining regularly. And I really never thought
they would go to this extent and they are not backing off. They are only increasing the drugging of the city. I was
really sure they would stop once I continue to evade them for a long time but they continue to up the ante everyday and
increasingly try to drug the city more thoroughly on a continuing basis.
>
.

.

After writing this post, I went out on motorbike and bought some sweets from a place more than 15 kilometers from my
house almost at the other end of the city and the sweets were drugged. I was not expecting them to be drugged at all
otherwise I would have asked the shop owner to let me taste the sweets first. Then I had a biryani rice from another
different place and it was also drugged. I only realized after I had eaten half of the biryani rice that they were
drugged. I bought some water and it was very lightly drugged and I bought it and I only realized that it was lightly
drugged after I had a lot of it at home. I was able to buy good cooked chickpeas(maize) from a place that was again on
another corner of the city close to Ravi river. After buying drugged sweets and bad biryani rice, I only realized that I
needed to be far more careful in the future since I was really not expecting that food in those so remote neighborhoods
would have been drugged.

I wrote previous two posts after coming back home.

---

### #2037 — Amin (Topic Author)
*October 31, 2023, 11:21 PM*

Friends, I analyzed some graphs of coefficients of coefficients Z-series from standardized densities in similar SV
context that we had been working. In my limited SDE parameter scenario I noticed that for underlying standardized
densities, graph of median coefficient c_0 as a function of volatility grid was unique but graphs of c_1 to c_5 seemed
to have exactly the same shape and form but only were different in scale of the graph. It was very interesting
observation so decided to share it with friends. I will look further into it tomorrow to try to find out more details
and see if this systematic similarity could lead to something more interesting. And share with friends tomorrow if there
are some patterns or something more meaningful.

---

### #2038 — Amin (Topic Author)
*November 1, 2023, 7:10 AM*

>
> Since the Israeli-Palestinians conflict is raging and most people have a strong opinion about the issue. I thought I
will share my opinion as well.
>
> I wrote the post(this is a slightly edited version) below as a Linkedin comment on a post by a very respectable, nice,
and a very good human who is from Israel in my connections.
>
>
>
> I am totally with you in condemning terrorism by Hamas and feel the same as you when I see families, living happily,
shot dead all of a sudden by Hamas terrorists. Such a massacre cannot be allowed in twenty first century human
civilization. All these terrorists should be brought to trial and very appropriately punished or eliminated if trial is
not possible.
>
> But at the same time when I think logically why so many Hamas people have become terrorists.
>
> We all love life more than anything else and really want to live. For many human beings the mere act of living is a
joy in itself.
>
> Hamas knew there would be large scale deaths of Palestinians after their terrorist acts but they still acted in the
same way and had no qualms about it.
>
> Why have they lost all love for their life and lives of their fellow people? Why is it that life and death have become
meaningless for them? When people are treated without any dignity, they never learn to show any dignity. Israeli forces
normally treat Palestinians without much regard and there are regular news of shooting of Palestinian youth by IDF on
very minor issues.
>
> Tit for tat is mostly not a solution to any problem. Israelis and Palestinians have to immediately do something to
decrease hatred and start to show some basic respect to each other. But their leaders are exploitative and want to
exploit widespread hatred. Masses in any nation are not super-intelligent and usually follow their gut reactions or tit
for tat reactions. A true leader is the one who does not exploit emotions of masses but makes the masses follow his true
wisdom for a better future of the people and nation.
>
> I think both Israeli and Palestinians need good leaders who are ready to lead their people towards reconciliation and
decreasing polarization. After all, we are all human beings just irrationally torn into religions which have no
scientific basis.
>
> Even if some good leaders in both nations follow the right path of reconciliation, they will have to be very
persistent and will have to follow long term objectives since fanatics and hardliners in both nations will try to
sabotage rational and logical policies of reconciliation by random acts of violence and terrorism. Good leaders would
need to show a strong resolve towards their longer term objectives. In our world, it can just take seconds to destroy
something that is meaningful but it can take decades for us humans to build something that is meaningful. It will take
minutes or hours to destroy peace or any attempts at peace but it can take decades of perseverance to bring a lasting
peace.
>
> Whatever has passed, we have to try to look towards a better future for everyone otherwise current hatred will ensue
more hatred and their will be more violence, aggression and terrorism.
>
> Jews and Muslim Palestinians have to be able to think beyond their own religion, their own benefit and both need to
compromise for a better future and a lasting peace.
>
.

.

.

I totally agree with Israelis about eliminating Hamas. But would Israelis be willing to find a peaceful solution to
Israeli-Palestinian conflict after Hamas has been eradicated. If Israelis continued to treat the Palestinians with
disgrace after Hamas has been eradicated, there will be another Hamas after 5-7 years and you will keep repeating the
process. If you are ready to treat people with dignity, they will treat you with dignity but if you treat them like
animals they will behave like animals.

Again if finding a peaceful solution to Israeli-Palestinian conflict is a part of comprehensive Israeli strategy, I am
all for eradicating Hamas but if Israelis want to maintain status quo after eliminating Hamas, I want to warn that all
of this is an exercise in futility because you will sow seeds for a bigger Hamas in next few years and I am afraid that
a lot more blood of innocent humans on both sides will continue to flow. The whole conflict has to be tackled with human
wisdom and not with Muslim wisdom or Jewish wisdom.

---

### #2039 — Amin (Topic Author)
*November 1, 2023, 8:31 AM*

>
> Friends, I analyzed some graphs of coefficients of coefficients Z-series from standardized densities in similar SV
context that we had been working. In my limited SDE parameter scenario I noticed that for underlying standardized
densities, graph of median coefficient c_0 as a function of volatility grid was unique but graphs of c_1 to c_5 seemed
to have exactly the same shape and form but only were different in scale of the graph. It was very interesting
observation so decided to share it with friends. I will look further into it tomorrow to try to find out more details
and see if this systematic similarity could lead to something more interesting. And share with friends tomorrow if there
are some patterns or something more meaningful.
>
.

.

Friends, sorry for this but this is not generally true as I have realized after analyzing more carefully.

---

### #2040 — Amin (Topic Author)
*November 1, 2023, 5:58 PM*

I went to an ATM machine of my bank, MCB Bank this evening to withdraw cash. I am perfectly sure my password was right
but ATM machine captured my card and I was given a receipt by ATM machine that my card was retained. Later tonight when
I called their call center, the staff advised me that I should block my card and I was very upset that my card was in an
ATM machine of bank's own branch and why should I block the card while it was in bank's own custody. Staff did not give
me any appropriate reason why my card was captured.

About two months ago, I had problems with my card and it was blocked by the bank. MCB Bank previously stole my money and
I have given a detailed account of their theft with proof by attaching bank statement. Please look at the links below
where I have discussed the details and given proof of bank's theft of my money.

Post # 1893.  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&p=876174#p876174

Post # 1894  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&p=876174#p876175

Post # 1895   https://forum.wilmott.com/viewtopic.php?f=4&t=99702&p=876174#p876176

Post # 1896  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&p=876174#p876177

I have an antipsychotic injection due tomorrow and I also have to visit my aunt's house with my mother and I program to
resume my research work tomorrow night.

Edit: After I wrote the above post and locked my room to start preparing for sleep, they have started releasing some
mind control gas in my room.

---

### #2041 — Amin (Topic Author)
*November 1, 2023, 6:28 PM*

I went to an ATM machine of my bank, MCB Bank this evening to withdraw cash. I am perfectly sure my password was right
but ATM machine captured my card and I was given a receipt by ATM machine that my card was retained. Later tonight when
I called their call center, the staff advised me that I should block my card and I was very upset that my card was in an
ATM machine of bank's own branch and why should I block the card while it was in bank's own custody. Staff did not give
me any appropriate reason why my card was captured.

About two months ago, I had problems with my card and it was blocked by the bank. MCB Bank previously stole my money and
I have given a detailed account of their theft with proof by attaching bank statement. Please look at the links below
where I have discussed the details and given proof of bank's theft of my money.

MCB Bank is one of the largest banks in Pakistan but it is a bank of crooks. They have a complete software to change
their complete accounting and transaction records in back dates which they must have been using to deceive their
customers and alter their books to deceive the investors and stock exchange. The posts below are testimony that bank
alters their records and accounting in back dates. I am sure they never made these provisions in their system to alter
the records in back dates specifically to deceive me. Obviously the system existed for non scrupulous activities of the
bank to deceive customers and investors by altering the books of the banks.

I wanted to change my bank for the fear that a bank that alters its book might sink any time but I had very little money
in the bank(just a few thousand dollars that have greatly dwindled by now) so I thought it was not worth the hassle to
change the bank.

Look at the post below for complete description of the fraud by the MCB bank.

Post # 1893.  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&p=876174#p876174

Post # 1894  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&p=876174#p876175

Post # 1895   https://forum.wilmott.com/viewtopic.php?f=4&t=99702&p=876174#p876176

Post # 1896  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&p=876174#p876177

I have an antipsychotic injection due tomorrow and I also have to visit my aunt's house with my mother and I program to
resume my research work tomorrow night.

Edit: After I wrote the above post and locked my room to start preparing for sleep, they have started releasing some
mind control gas in my room.

---

### #2042 — Amin (Topic Author)
*November 2, 2023, 3:03 AM*

I am writing this post for Pakistani friends who know about my persecution in Lahore city. I want to tell Pakistanis
that scumbags of American defense are not our friends at all and they are controlled by rich and malicious jews in
United States who order these scumbags to retard muslims(and others including europeans, Americans but that is not the
issue of this post) very systematically all over the world(Malaysia was also roaring twenty years ago, American defense
totally grounded Malaysia with mind control by retarding brilliant people). Over past twenty years, these scumbags of
American defense have retarded several hundred very brilliant Pakistani minds causing a systematic cumulative damage of
several hundred billion dollars to our economy. No wonder that all south asian nations who were much behind us in per
capita income twenty five years ago are roaring economically today while we are begging for money from nations all over
the world to stabilize our finances.

I want to request all Pakistani friends who are in a position to help them to extort as much money from scumbags of
American defense as you can. If you were asking for one million dollars for cooperation with these scumbags in retarding
the city, please ask for 50 million dollars. And also spread the news about the actions and motives of these scumbags
all over the city and all over the country. I will also ask my Pakistani friends to not go beyond limits in cooperation
with these scumbags while taking as much money out of them as you can. Please do not get sold out cheap.

I also want to tell Pakistani friends that there are good and bad people in every nation. Americans are not a bad people
at all but their defense department is filled with filth and scum because scum in American defense inducts like-minded
people every year. On the other hand, many good human beings all over the world mostly from United States tried to
protect me several times while nobody in my own country was ready to help me and in my right mind I can never say that
Americans are a bad people. Americans, in general, are a great people but good and bad people are everywhere and there
defense department is full of scum.

Please do not cooperate with these racist pigs of American defense who are bent on destroying our nations on behest of
machinatory jews in united states. If you have to cooperate, please do not go beyond limits and extort as much money out
of these scumbags as you can. Pakistanis usually get sold out very cheap, so please do not make yourself a commodity and
ask for huge sums of money in return for cooperation.

---

### #2043 — Amin (Topic Author)
*November 2, 2023, 10:30 AM*

I want to ask friends in European universities to ask their embassies in Pakistan to prepare comprehensive reports about
how food is drugged with mind control chemicals on a huge scale and all other elevant aspects of mind control. Currently
there is a very large scale activity in Lahore city by crooks of American defense and it is a very good time to get to
know about all their tactics. It is also a very appropriate time for investigative journalists from all over the world
to try to get to know how food is drugged on a huge scale in entire markets to target innocent but intelligent people
pointed out to American defense by Jewish billionaire Goldfather and his machinatory rich Jewish cohort.

Also please ask the embassies of your country to try to protect innocent human beings who are targeted by mind control
in our poor country by telling their influential Pakistani contacts all the truth about mind control. And please
distribute these reports prepared by your embassies about mind control in Pakistan/Lahore among all your friends so that
everyone can know the tactics of racist pigs of American defense who want to corner innocent individuals by drugging the
food on a large scale in entire cities. These racist pigs are raging in Lahore city so it is a good time to know all
their hideous tactics.

Please ask the embassies to collect all the details from their sources how food in Lahore city was drugged with mind
control chemicals in past few days. I cannot say anything at all but they might possibly have to abort in a few days
under pressure from good people but what they have done in past few days would be enough to open the eyes of good people
about their tactics. Please check out before it is too late.

---

### #2044 — Amin (Topic Author)
*November 3, 2023, 4:40 PM*

Friends, I hope that good people in Europe and America would have asked European embassies to collect (using their
Pakistani sources) complete information about how food and beverages were drugged in Lahore city during past two weeks.
I am sure all such information will help intelligent and smart people in universities help understand the nature of mind
control. And in most free countries and democracies, it is the universities that are at the vanguard of ideas, thoughts
and suggestions for better governance of any country. So it would be helpful for individuals in universities to know how
CIA and thoroughly corrupt American defense drug the cooked foods in entire markets of some city to illegally corner an
individual especially in our poor countries. I am sure any such report prepared by embassies will be very informative.

Israeli-Palestinian conflict has come to limelight in just past few weeks while I have been speaking about connivance
between Jewish billionaire Goldfather of mind control and his rich jewish cohort for several large many years.
Connivance and nexus I have been speaking about is in reference to cruel and illegal mind control. Any Jewish support of
American Jews and lobbying for protecting Israel and attempts to influence American defense in that regard are naturally
understandable and probably a good right of any American jews and can never be called connivance or nexus. Even if I
keep trumpeting against Jewish support for Israel (which I do not at all), almost all Americans will never take offence
at any such Jewish support to protect Israel since they know that it is very understandable and natural.

The nexus I have been talking about is related to mind control of innocent and intelligent Americans, Europeans, and
Muslims who are pointed out to American defense by Jewish Goldfather and his rich jewish cohort. People are retarded for
economic gains by rich jewish cohort, to kill competition of jewish cohort, to steal ideas of other brilliant people
while retarding them, to force intelligent people to work with jewish cohort's companies due to fear of mind control,
and a large number of Americans and many Europeans are a victim of this nexus. People are also retarded due to hatred as
in case of retarding intelligent muslims and attempts to retard hundreds of intelligent people in Muslim countries to
solidly damage the entire economies of these Muslim countries on behest of rich jewish cohort . At this time, American
defense is totally a puppet in hands of jewish goldfather billionaire and his rich jewish cohort.

It may not sound nice but somebody has to do the dirty business of speaking against the rich and evil jewish cohort
before it is too late.

---

### #2045 — Amin (Topic Author)
*November 4, 2023, 9:37 AM*

Friends, I had decided to shift emphasis from speaking against mind control towards my mathematical finance research
since I had realized that many good Americans had gotten known the details and degree of connivance between rich jewish
cohort and American defense. I really thought that I had served my purpose and now good patriotic Americans will do what
is best for their country and rest of the world by making their government take right decisions about mind control.

Friends would have noticed that I was trying to pursue my research with enthusiasm and not writing about other things.

But American defense again started to drug the entire Lahore city to retard me. I still remained silent for a long time
thinking they will back down on their own but they continued to drug the city to unprecedented limits and I was forced
to speak about the old issues to protect myself.

I have stepped on the tails of many corrupt bigwigs of American defense and they totally want to eliminate me. Since
drugging the entire city has not worked for them, I am very sure their next step would be to ask my family to declare me
mentally ill and detain me with a psychiatrist so that during detention I could easily be given all mind control
chemicals that are needed to take good neurotransmitters out of my brain and my other neurotransmitters could easily be
blocked in captivity where I would have a very limited leeway to do anything unusual.

I really want to request all good Americans who protected me so many times before to force the American defense to end
my persecution because they are bent on detaining me with a psychiatrist again. If good people did not help me now, I
might be doomed for several years again and my cause of mind control will also be lost forever.

I am going to copy some previous posts that highlighted how psychiatry has become a joke in hands of American defense
and almost every psychiatrist resorts to unprofessional tactics to retard victims of mind control. Please read my
following posts carefully.

---

### #2046 — Amin (Topic Author)
*November 4, 2023, 9:46 AM*

Friends, in a previous post I told friends how staff at a lady psychiatrist's hospital started beating me and abused me.
During past twenty three years, there have been many many instances of my obvious abuse by different psychiatrists. I
will describe some of those instances in this post.

When I came from United States and till fifteen years after that, my father would proudly ask me that I could see any
psychiatrist I wish. This was because Pakistan army was managing my persecution and they would force psychiatrists to
declare me schizophrenic and my father was told that every psychiatrist would be forced to cooperate. However, by chance
in 2016, I came  across a psychiatrist who was far better. I never told him that I was under mind control but whenever
he interviewed me, he always said after the interview that I was perfectly sane and mentally healthy. When my family
would force him to increase the dosage of antipsychotics, the doctor first told me that I should not live with my family
and make a comprehensive plan to support myself and become independent (such a plan could never work since Pakistan army
was threatening people in Pakistan to not give me any business and CIA was making sure that every contact I would reach
for work in Europe (and Singapore/ Japan /Australia) would be approached by CIA telling them that I was a very bad guy
and they must not do business with me. I had not told the doctor any such thing that intelligence agencies were after
me.)  When I told the good doctor how previous psychiatrists had abused me, he would tell me that this used to be a very
widespread practice in America hundred years ago to wrong mentally healthy humans by using corrupt psychiatrists as
instruments to detain them and strip them of their sanity. The good doctor I am talking about was American national with
Pakistan background who had practiced psychiatry in America for over twenty years and had returned to Pakistan. That
good doctor kept me on very low antipsychotics (1 mg resperidone per day) and that too on extreme insistence of my
family. It was only during that time of treatment by that doctor that I got my first break in research and I solved the
problem of high order monte carlo simulations (and analytic series solution of ODEs)  and posted that solution on this
thread. Ok, when my family was fed with the doctor, they detained me with another doctor. They detained me again two
years ago when I requested my family that I wanted to see the same doctor of my choice again( I have been detained every
year for past six or seven years by different doctors), they detained me through a different doctor. So my family now
stubbornly refuses to allow me to see a professional qualified American psychiatrist of my own choice and detains me
every time I try to approach him.

Now back to my obvious abuse by two other psychiatrists. I was detained by this doctor who was running a mental health
facility and was not a psychiatrist himself. At that time I did not use to walk very much and my blood pressure used to
be somewhat high. Since other antipsychotics had failed to retard me, doctor suggested I take aripperizole injections.
These injections affect the heart and also elevate blood pressure but doctor who wanted to retard me had no regard for
my health while pretending to cure me. In initial days of my detention, staff at the hospital when checked my blood
pressure told me high enough blood pressure in line with what I used to have but after I complained about aripperizole
and its effect on blood pressure the staff started doctoring blood pressure and started telling me that my blood
pressure was very good or even low. This is a post I wrote on another thread in this forum about it. How to safeguard my
research - Page 32 - wilmott.com

.

> Amin:
>
>
>
> Since I wrote about high blood pressure and mentioned high blood pressure before the hospital staff, they have started
to doctor blood pressure. Now, everyday they tell me that my blood pressure is 120/80 or 110/70. While they always told
me that my blood pressure was 130/90 or 140/100 prior to injections. I have never had so good blood pressure for years
that they have started to tell me now. Friends would recall a previous post when I could not sleep at night and had to
take a sleeping pill. When the dispenser came to me at night(The hospital has no MBBS who stays here at night in
Ramadan. Dr. AS used to stay here on some nights earlier but has been totally absent in Ramadan). When the dispenser
checked my blood pressure, he told me that it upper blood pressure is 110. I did not believe him at all. He asked me to
check on my own and put the stethoscope head assembly in my ears. I could easily tell that upper blood pressure was more
than 140 and lower was more than 100. The staff has already started to doctor blood pressure. My parents are going to
Saudi Arabia for two weeks in a few days. Now Dr. AS has the plan to hold me in detention while my parents are abroad. I
had a complete settlement with Dr. N and we(I and the doctor N) both agreed that I would be visiting him every fifteen
days and all modalities were agreed. I do think as a patient it is my right to choose the psychiatrist and Dr. AS( who
is incharge of facility Pav.) has no right to change the doctor after I have selected a psychiatrist and we both agree
on terms of any treatment. Dr. AS has imposed another psychiatrist Dr. M who has not even seen me and has already
started giving me injections and increased medicine without looking at my present condition. Dr. N had explicitly stated
that I would be free to leave if it were his facility. Most major reason for detaining me now is that Dr.AS wants to
continue to detain me while my parents are leaving for abroad for more than two weeks
>
.

Later after a few days, I was given a second aripperizole injection and released from detention. An injection was due
every fifteen days. My parents were in Saudi Arabia and I was living with my sister. She insisted after fifteen days
that I get a new aripperizole injection. I complained about too much side effects and other serious problems but my
sister insisted that I must get the injection. She talked to another doctor and the doctor told her that if his blood
pressure and pulse are fine, just give him the injection. I asked my sister that my blood pressure must be checked
before I get the new injection. We went to a small hospital close to her house and when my blood pressure was checked my
lower blood pressure was 110. The hospital staff recommended that I stay at the hospital in their care until my blood
pressure decreases. It was a totally random blood perssure check. When hospital staff came to know that I had been given
aripperizole injections, they told my sister to not give me those injections any more. My sister asked the staff to
relieve me and we came home but I was not given aripperizole injections after that.

But this is interesting that the psychiatrist was initially desperate to prescribe aripperizole despite that I had told
him about my heart and blood pressure problems and his staff was asked to doctor blood pressure so that I would accept
the injections.

Good thing is that only after stopping aripperizole, I started my treatment with good psychiatrist  doctor Naeem Aftab
(who is an American national) and he gave me enough relief that I was able to get a break in my research and solve the
problem of high order monte carlo simulations. I would always be thankful to Dr. Naeem Aftab for giving me relief at
such a crucial point in my life.

Yet another experience for abuse was with a seasoned psychiatrist who is known for his connections with Pakistan army.
When army dictator Pervaiz Musharraf ruled the country, he made this doctor the dean(president) of the university of
health sciences which regulates most medical universities in Pakistan. He had treated me for three years in year 2001.
He started my treatment without interviewing me and gave me electric shocks at the start to jumpstart the therapy. I was
given electric shocks for fifteen days in early 2001. I still recall that doctor would place a wooden wedge between my
teeth and then give me an injection and I still recall how numbness would move in my body from feet to the upper body
after the injection.

When going to that doctor's psychiatrist facility in 2001 I had to travel from Kot Addu to Rawalpindi. My family had
given me some drug in my food and I became unconscious after an hour or so. I still recall how I was begging my younger
brother to help me that I do not want to go anywhere and if he could help me but he like everybody else in the family
refused. Slowly drug in food showed its effect and I have absolutely no memory of being taken in my father's car despite
that it would have taken him at least eight hours to take me to Rawalpindi. Psychiatrist did not interview me and
detained me and started giving me electric shocks. I still recall how I defecated in my bed there and they had to wash
it.

Anyway, I was taken to this psychiatrist in 2017 again. He was very clearly told that I had been given antipsychotic
drug larjactil by another doctor and it backfired and I had extremely severe drug-induced jaundice. But the doctor was
so haughty and cavalier and so desperate to retard me that he still insisted that I must get the same drug larjactil and
said that it was not necessary that it would cause jaundice every time. Problem for the doctor was that most
antipsychotics had failed to retard me and he wanted to give me some potent antipsychotic that had not been well-tried
on me. Though the drug was given to me earlier and later discontinued, the doctor wanted to take his chances to retard
me and he had no regard for my health. This doctor is a big crony of Pakistan army and really wanted to please the
generals and therefore he decided to give me larjactil again. And as would already be obvious to most friends, after two
weeks, I started to show all signs of drug-induced jaundice again and my body and eyes were all yellow. My Biluribin
shot like anything. And it took more than two months to control jaundice after that. Though my biluribin came back to
normal after two months, several less known enzymes in my liver remained disturbed for several years after that and
continued to show as abnormal in my liver function test reports.

I have been detained more than 30 times by various psychiatrists during past twenty-five years on orders of Pakistan
Army. This is despite that I have never been violent all my life. I have never hit anyone in my adult life and I rarely
speak with anyone in a loud voice. I have never done anything like breaking a glass or any utensils that is associated
with sick people.

Here, I will recall an incident eight years ago when I myself approached a lady psychiatrist for help and how she abused
me, and her staff beat me for twenty minutes and then tied me and started my treatment with antipsychotics again.

I am recalling this from early 2015. They had previously put me on extremely high antipsychotics and my creativity was
all gone. I could barely do any intellectual work. At that time, I was able to convince my family to decrease the
injections and they had agreed since I had already lost most of my creativity and intellectual capability. I think mind
control agencies were also thinking that I had lost my creativity forever and they wanted to see if it was right time to
decrease my drugs and still make sure that I would remain intellectually dull after injections had ended.

But I slowly started to work on my research and started to regain my brain. When mind control agencies realized that I
had started to do better research, they asked my family to do something again to retard me. My father asked a
self-stylized religious saint to come to our house and take care of me. He came to our house with one of his followers
and told me that he wanted to give me injections and I would go to sleep for 24 hours, and they would take scans of my
brain to treat me, but I continued to beg and plead him, and I was able to convince him to allow me to leave the home in
my car. The supposed saint allowed me to leave since he was probably sure that he would get me later as I had no other
place to go other than my home and, therefore, I was able to convince him to let me go outside. When I left the house, I
made posts about the saint on at least two different forums from outside my house and pleaded for help. Enough people
were following my story even at that time and the saint had to leave. I also called my father when I was outside and
protested against this.

My family still remained very tense with me, and I was very afraid that they would force antipsychotics injections and
mind control drugs on me therefore I stayed one night out of the home. Here is the post I made when I was away on April
14th, 2015, 2:09 pm

[viewtopic.php?f=15&t=94796&start=315#p748191](https://forum.wilmott.com/viewtopic.php?f=15&t=94796&start=315#p748191)

"I am staying out of my home for the night since I had realized that my father will try to force me into detention again
and I would request a court tomorrow for stay order to stop my father from hospitalizing me forcefully again and I would
request the court that if there has to be a check on my mental health, it has to be done and investigated properly by a
psychiatrist of my choice and I should remain free at the same time. I do not want to be at the mercy of my father's
chosen psychiatrist as we saw in the past year that they continued to quote mental health laws and forcefully manipulate
me into taking injections. If my father forcefully hospitalized me, I would be cutoff from the outer world and they
would do whatever they like. My father's self-stylized saint(peer) had already hinted that he wanted to give me
injections that would put me to sleep for 24 hours and he had no argument for my mental sickness at all.”

Next day, on April 15, 2015, I went to Lahore High Court to find some help but I was told that I had to submit an
application that would be considered several weeks later when its turn would arrive. When I realized that there was no
possibility of help from the court, I decided to see a psychiatrist on my own. I was driving in Garden town Lahore where
I came across B**** psychiatric clinic and decided to see the psychiatrist Dr. N*** there. It was evening but the
psychiatrist still not had arrived there. I waited for an hour in the reception and then had a consultation with her. I
asked her to listen to my case carefully and then decide if I was sane enough and tell my parents about it. She said
that I seemed perfectly fine and asked me that she wanted to hear what my family had to say. I agreed and took an
appointment to visit her again at April 20, 2015. I took my mother on the planned day and my mother did not have
anything decisive to say about any disease other than that I did not eat at home. The psychiatrist asked me to visit her
after one week on 27 April 2015. The next week when I went again to visit the psychiatrist, on April 27, and was sitting
in the waiting room so that I could visit the psychiatrist on my turn. Another lady who was a psychologist came to me
and asked me to go with her in a different room to have a session with psychologist but I declined and said that I was
only interested in seeing the psychiatrist who had promised to see me again the earlier week. After five minutes, at
least four men came to the room and started besting me. They gave me slaps on my face with full force and gave me blows
and they continued to do it for more than fifteen minutes. I had never been beaten like that ever before in my life. All
this time, I was simply trying to raise my hand to somehow protect me. Since I was sitting on the sofa, only my face and
head were the target of slaps and blows. They were very violent with all sort of slaps and blows on my face as I earlier
mentioned that I was sitting and they were standing. . They literally continued to beat me and I continued to beg them
to stop. After fifteen minutes of beating me, they tied my legs and lifted me and put me on a bed in a room in the
psychiatrist facility and told me that doctor had gone to America and she could not see me. It was a complete lie and
the psychiatrist was in her office and was interviewing other patients when I arrived. I continued to ask them to loosen
the knots but they continued to make fun of me. I was totally surprised since Dr. N had behaved very nicely in the
previous meeting held at 20th with my mother and myself and I was sure she would declare me mentally sane on this
meeting. After I was kept tied for about half an hour, a new guard came and opened my hands and legs and said that they
would keep me at the facility for three days. The next day my medication in the form of pills started and I was also
given two more injections. I was given about nine pills at night and about eight pills in the morning. I was still not
given the opportunity to meet the psychiatrist N, and I was told several different things by different people including
that psychiatrist N had gone to America, and she had gone to Islamabad. About three days into my treatment, I saw
through the glass walls that psychiatrist N was interviewing her clients in her office. After seven days, I was asked to
meet psychiatrist N, and she said that she was unaware of the beating as she was in a meeting. Psychiatrist N also
assured me that I had no schizophrenia and previous doctors had very wrongly diagnosed me but it was a case of some
mania that she would properly treat this time.  Her staff continued to say that they were giving me drugs so that the
effect of other drugs given to me by previous psychiatrists would decrease.

Before my computer was taken away from me, I was able to take notes for two days in the hospital on my computer that I
write here. After first two days of medication, I was so extremely weak that I could barely walk and I had extreme
difficulty speaking.

“My Diary for past two days.

4/27/2015

I had two sessions with the doctor N previously on the 20th of April and once before at 13 or 14th of April. I remained
away from home during this time and second meeting on 20th of April, evening after the night when I remained away from
home. I had told the doctor about my circumstances in the first meeting with her. She had said that I looked perfectly
fine mentally but she needed to talk to my family. On 20th of April, I took my mother for a second joint session of
myself and my and the psychiatrist said, after the meeting, that said she really could not call me schizophrenic but she
needed one more sessions and asked me to come to her facility on 27th of April.

When I arrived at the psychiatric facility, a psychologist had asked me to accompany her which I did and on the way to
the her room, I asked for the reason, after which she replied that she wanted to take a session of mine. I told her that
I already had a session with another psyc hologist and also with a psychiatrist so I would prefer to have a new session
with the psychiatrist now. She agreed and I returned to the waiting room. I was sitting on a sofa in the waiting room on
27th at 8:00 PM (PST) in the line to see the psychiatrist when about five guards took control of me, while I was sitting
on a sofa in the waiting room to see the doctor, and gave me an injection. I was beaten and my legs and hands were very
strictly tied for more than hour. Though the doctor was in her consultation room and a lot of people were waiting to see
her, I was told again and again that doctor was not present at the facility.

In the previous two sessions, she had given the impression I was healthy mentally but she used force without
interviewing for the third time or seeing me and without requests to comply. If she was given any special information,
she should have talked to me about it and she should have verified with me any change in circumstances.

One injection was given around 8 PM when I arrived for third session with the doctor N. I really think that the doctor
was there since there was a large rush of visitors and her SUV was parked in the hospital but everybody among the staff
continued to say that doctor did not come to the facility this evening.

I was kept tied for more than one hour. I was taken tied from the waiting room to my room. All these rooms have video
cameras so you can ask Dr. N for a video of the events though she might make the excuse that cameras were not working.
One of the staff had mentioned when they brought me into a patient room in the facility, that everything was watched by
cameras.I would request people familiar with the matter to request her to show them footage of the cameras. Of course,
there could be many excuses that cameras were not working but I insist that cameras were working.

Good Mental health facilities try to avoid treating humans like this.

Another injection was given at night before I slept.

and my internet USB device was also taken. They simply took possession of everything out of my pockets and also took my
laptop.

When I asked why they gave me injections, one of the staff told me you were ?hyper? and I was totally surprised since I
was quietly sitting on the sofa in the waiting lounge for the doctor. I was told that I would stay in the hospital for
three days. I am sure this matter can be resolved who is lying and who is truthful once you look apt video footage of
cameras in most rooms.

4/28/2015

One injection was given in the morning. One injection was given around noon. All injections were IM (given in the
muscle.)

Unknown pills(some pills in the morning +5 pills around noon + 3 pills at night) were given and I was told,? We will
tell you know the names of these pills only when you leave.?

Computer was returned today but I was told that we did not take your mobile and they continued to say we never took my
mobile. My mobile was never returned( despite I always keep my mobile on me.)

I was also not given my EVO USB device and I was told you cannot write anything on internet. However the USB device was
returned to my mother at night.

I was told today by the psychologist that doctor N had gone to America and will come back after seven days and only then
she would be able to see you. I was told we are adjusting your medicine and see what was a good medicine. I was told
they were discussing the drugs with her on phone and skype There were several conflicting statements about where Dr. N
was. Somebody said she was just out of city and had gone to Islamabad.

When I asked my mother who is living with me at the hospital, I wanted a second opinion, because of beating and other
irresponsible behavior of the psychiatrist, my mother would make all sort of excuses while the staff would say that you
cannot leave the hospital until Dr. N arrives who is currently out of country.

Earlier today, I was told that I would live at the hospital for fifteen days and later I was told that I would live at
the facility for seven days. When I was tied, somebody had told me that I would live in the hospital for three days
only.

My mother told me please do not write anything wrong on internet otherwise, they would take your USB forcefully like Dr.
A had done more than one year ago. The purpose was to threaten me to not write about any maltreatment so that the doctor
would continue to freely manipulate me.

7-8 pills were given in the afternoon and similar number of pills were given at night. At many times during the day, I
could barely walk and had extreme difficulty speaking.”

Friends, I have previously described several horror experiences with psychiatrists but there are many more such
experiences that I have not posted on this thread. Today I am going to describe a continuing experience in which the
psychiatrist did everything in his power to retard me.

This is from year 2004/2005. I had a sound logic at that time and I was working from Lahore at a job with a foreign
Japanese company that was paying me \$4000 per month. I was still on high antipsychotics and when high dosage of normal
antipsychotics did not work, in order to retard me, the psychiatrist employed a procedure that is not known in
psychiatric practice in any country. The psychiatrist would give me some drugs in a glucose drip every two/three days in
the operation theater. When I would be given the glucose drip, I would gradually start to lose consciousness and when
half of the drip bottle would have gone into my blood, I would literally be unconscious, and I would later be taken
unconscious to my hospital bed by the hospital staff and I would wake up several hours later on the bed in my hospital
room and I would be extremely weak.

It was such a frightening experience that I would shudder from horror as the day of this treatment would come closer and
continued to beg the psychiatrist to stop this treatment. The psychiatrist would say that he was giving me vitamins and
vitamins were always harmless. He insisted that vitamins had to be given to me. He never told me what drugs he gave me
that made me unconscious and never discussed it with me other than mentioning vitamins. The psychiatrist continued to
perform this procedure for several weeks after sometimes second or usually third day. Most people cannot imagine how it
would feel when the drug in glucose drip would go into my body and I would lose my senses. To this day I shudder from
complete horror and recall the extremely sick feeling when I would slowly lose consciousness.

Now when I look back, I realize that they were giving me mind control drugs in the drip to take the intelligent
neurotransmitters out of my body. They continued to try to take intelligent neurotransmitters out of my body again and
again through this procedure for several weeks. I was completely helpless before my family and the psychiatrist and had
to go through such unlawful medical procedures.

As friends would have realized that purpose of mind control agencies was always to retard me since neocon scumbags of
pentagon and their backers were not capable of appreciating my humanity and did everything in their power to retard me
with an iron fist.

I have seen continuing pain, trauma and torture in my life only because I had some special neurotransmitters that people
with hatred and venom were not ready to let me have since they considered it a threat to let a Muslim have those
neurotransmitters.

After starting mind control in Lahore in early 2000's, bad jews (again apologies to good jews) were very emboldened how
easy it was to manipulate army and government in Pakistan to start mind control of intelligent people in Pakistan. It
was a time when Pervaiz Musharraf who was an army dictator ruled the country. He was very ready to please the CIA in
order to get help from American army to prolong his illegal dictatorship in Pakistan. He fixed in place all the required
mind control infrastructure in all large cities of Pakistan to please American army who was playing in hand of bad jews
to damage the Muslim majority country.

When Americans rightly blame our country for terrorism, they must not forget that many neocon generals in American army
have played in the hand of bad jews and have made every effort to systematically destroy talent in Pakistan on a very
large scale using mind control technologies to keep it backward forever.

Mind control in Pakistan is ensured by top Pakistani army generals since they are given several hundred million dollars
by US army every year and the top brass of Pakistan army divides this money among themselves with bigger fish getting
larger share and smaller fish getting a smaller share. Therefore, mind control infrastructure in Pakistan is very
detailed and thorough.

From my own experience, there is very large mind control activity in Lahore and Islamabad, the two cities where I have
lived during the past twenty years. There are at least more than 500 mind control targets in Pakistan most of whom are
computer science majors.

Mind control in Pakistan and many other places increased dramatically like never before. We have in Lahore a huge
building called Arfa Towers where all the facilities for technology and IT companies were provided to attract new firms
and entrepreneurs and later Arfa Towers became a scene of mind control carnage since tens of aspiring computer
scientists and entrepreneurs were retarded and it became very easy for mind control agencies to find the talent since
the facility attracted talent and retard it. Time between 2008 and 2016 was like black death for talent in technology in
our country (I am not talking about pseudo-talent that American embassy continued to support and showcase heroically in
the meantime.)  I still recoil with horror when I look back and recall how difficult it was to get good drinking water
in Lahore during that time for more than six months in 2013-2014. I would have to go to remote parts of the city, go to
villages around the city and sometimes even go to other cities and only then I would be able to get some good water
after repeated attempts and my only worry during the day would be to somehow get good food and water.

At this point I like to tell friends that a lot of food and beverages that are drugged with mind control chemicals would
be eaten or taken by most of the population that is not on mind control and they would never notice any anomaly in taste
or any other effect since these mind control chemicals are inactive and inert and become chemically active only when
targeted remotely with precise electromagnetic wave frequencies so only target victims are affected and this is a very
cruel method to target intelligent people by drugging the entire supply of food and beverages and then focusing waves on
the targeted individuals to activate the mind control chemicals. Pakistan army and mind control agencies would drug the
entire public water supply and beverages knowing that the victim would have to drink something somewhere. Ground water
is also so thoroughly drugged with mind control chemicals that entire public water supply of the city and several
kilometers out of the city would be completely drugged with mind control chemicals. Pakistan army routinely does this in
Lahore city on behest of American mind control agencies.

Ten years ago, army soldiers and agents would go to markets to drug the targeted food and beverages with mind control
chemicals which they still. Large scale movements of soldiers and agents raise suspicions in general public and
therefore mind control chemicals are supplied to beverage and food manufacturing companies in Pakistan, and they simply
add the chemicals in food and beverages during the manufacturing process.

In Lahore city, there are more drugged beverages at any time than good beverages in small stores or large supermarkets
alike since most of the beverages are drugged at manufacturing source by coca-cola, pepsi-cola and Nestle.

Coffee stimulates the brain and the brain connects in new ways after taking coffee and good coffee creates problems with
keeping victims on mind control since their brain starts connecting in many new ways after taking good coffee. All
coffee and I repeat that entire coffee in the country present in the stores is drugged with mind control chemicals. Most
of the coffee on good stores is imported from foreign countries. I do not know how it works but importer is probably
told by army to drug the imported coffee before distributing it in the market. It is even very difficult or rather
impossible to get good coffee beans. Two or three years ago it was possible to find some brand of coffee that was good
by trying all new brands but it has not worked for past two years now for me despite that I keep trying. I even know of
instances that when I was able to buy good coffee of a certain brand from very large and posh stores, they took entire
coffee brand off the shelf from all their branches within two to three days. People know that Corrupt Army in Pakistan
that ensures mind control is more powerful than any political government here.

Tea used to be good but for past one year most mainstream Pakistani brands of black tea are drugged with mind control
drugs. This has still not caught up thoroughly like coffee is thoroughly drugged and it is still possible to find some
good foreign brands tea that is good.

All stimulant/energy drinks including red bull are well drugged at manufacturing source. Red bull was better till last
year but then it became drugged everywhere. I even tried it at remote places in several cities other than Lahore and it
has always been drugged lately.

Most of the soaps, shampoos, creams, toothpastes are drugged with mind control chemicals. I do not use shampoos or
creams but whatever rare I tried them once in a while they were drugged and they charged my skin. All of these have mind
control chemicals that charge the skin and make mind control extremely effective. Many people would be amazed when I
tell them that even though I would be in my full senses before washing my head and face with a soap but after washing my
head and face with a drugged soap, my eyesight would deteriorate and my conception of reality would completely change
and sometimes I would face extreme anxiety. It is hard to emphasize that even a small thing like this can completely
change the victim's state of mind and consciousness. Getting a good soap was very difficult for me till last year and I
would drive for several hours in different parts of the city especially looking at all the pharmacies on the way to find
some unknown brand or some soap that would have been manufactured several years ago when soaps were not getting
completely drugged. I tried all the soaps including beauty soaps that are specially made for women, even many unknown
brands, and specially imported soaps(which were all universally drugged thoroughly) and it was very very difficult to
find a good soap. After finding a good soap, I would keep it in my pocket all the time. This is a small thing but you
cannot live without it. Since our mouth is kept charged and some charges continue to go into victim's body from one's
mouth. Therefore toothpastes are also added with mind control chemicals to charge inside of our mouth. You can imagine
that after buying five or six tooth pastes of different remote brands, I would get a good tooth paste. I have recently
been using toothpaste that is imported from abroad and is good. Toothpastes manufactured in Pakistan are all drugged
with mind control chemicals.

Another big problem is that pharmaceutical companies add mind control chemicals to their drugs(pills etc). Most of the
mind control victims are targeted due to their talent and intelligence in mind many times might require special minerals
that are rare in our food.  Most of the mineral and vitamin formulas are also drugged with mind control chemicals. Most
mainstream mineral and vitamin pills in the market are thoroughly drugged with mind control chemicals. I never like to
take names but I would like to tell friends that greatest crook of all times is Glaxosmithkline( I would invite them to
sue me for writing this on Wilmott). GSK's mineral and vitamin formulas, effervescent calcium tablets, and toothpastes
are all drugged with mind control chemicals. There is a tablet by the name Kemadrin that has to be taken with
antipsychotics and GSK manufactures it and it is also drugged with mind control chemicals. My experience with GSK is so
bad that If I have to buy any medicine and if it is made by GSK, I would try my utmost to avoid taking it for the fear
of its being drugged with mind control chemicals and look for alternatives.

Injection fluanxol and clopixol are also drugged with mind control chemicals.

Again all this thorough infrastructure took more than fifteen years to develop in Pakistan and Pakistan army continued
to work hard to develop it over the years. There are at least five hundred brilliant Pakistanis most of whom are
computer scientists who are on active mind control to thwart them to contribute to society in any good way.

All this infrastructure exists in Pakistan and was developed because neocon generals wanted to please bad but rich jews
and American mind control agencies continue to perfect it over last twenty years. Again, mind control in Pakistan is
ensured by top Pakistani army generals since they are given several hundred million dollars by US army

I have not talked about special infrastructure that is used to project EM waves on the target and this infrastructure is
present on all major roads and public places in big cities and major highways and motorways in the country.

[My Letter To HRW About My Human Rights Abuse](https://forum.wilmott.com/viewtopic.php?f=15&t=102298)

Above is a very incomplete account of how various psychiatrists continued to play in hands of Pakistan army to retard
me. It also does not cover all the time till year 2022 and the account stops several years earlier.

---

### #2047 — Amin (Topic Author)
*November 4, 2023, 9:54 AM*

Before writing this post, I want to apologize to good jews but want to tell them there are enough evil jews who are
doing everything to tarnish the great goodwill jews have so rightly earned through generations of hard work and being
nice and kind to other people in the society. I want to request good jews to Please force these evil(jewish) people to
end the bad practices that are starting to take root in American and other societies on their behest and before it is
too late. I also really hope that my mind control would finally end(as I have been begging for past twenty years) and I
would never have to write a post like this again.

In the past, I continued to mention about my mind control persecution from time to time but only started writing regularly about it when I arrived in UK on a Highly Skilled Migrant work visa. Mind control agencies did everything in their power to fail me in UK. People were asked to not give me a job. People I contacted were routinely told brazen lies about me totally shamelessly. When I realized that I had no future in UK, I returned to Pakistan after a six month stint in UK. Since my hard earned money had thoroughly insulted mind control infrastructure in UK as they had to drug entire cities with mind control chemicals in UK (read briefly about it in my application to HRW in a previous thread) for a nobody like me and American government had to move all their grand and influential puppets in UK (again for a nobody like me) to force people to drug the manufactured food. British Banks went to the extent to steal my money to bleed me. Read here: https://forum.wilmott.com/viewtopic.php?f=15&t=102298#p857494. British police forcefully stopped me from seeing law firms(Brief details are given in my application to HRW attached as a link below).  Since my money had given mind control agencies a very tough time, mind control agencies decided to never let me make significant money after that. My old Japanese employer was told to not hire me after I returned to Pakistan. Whoever I would contact someone in Europe for job or consulting, mind control agencies would move American embassy infrastructure in that country and somebody highly influential (or army or secret services of that particular country)  in that particular country would approach my target employer and again brazen lies and fabricated stories would be told about me shamelessly. I am a fighter in life and I continued my research despite all economic, coercive and other hardships. All odds were against me but I tried my best to continue.  I have been presenting my research to friends on this forum for past five or six years. At this point, I want to request good American and friends from other countries who have come to know me through my research to please use their influence to end my mind control forever.

Since things might heat up after my writing this and my persecution might increase, I want to ask European embassies in
Pakistan to keep a vigil. I want to tell Europeans that my writing about mind control is in their great interest since
the very same people who instigate retarding of intelligent muslims are behind retarding of dozens of intelligent
europeans and once these people are exposed I am sure they will be far more careful in openly retarding European
talent(that they do not like).

I had told friends earlier that a jewish billionaire is Godfather of mind control. When my persecution started (in late
1997) at the university in New York which is a big time player in mind control of Muslims, blacks and foreigners, many
university officials were very pleased that they were getting written in good books of the billionaire jewish Godfather.
Though there are far richer billionaires in US who are staunchly opposed to mind control, they are not ready to shell
out hundreds of millions of dollars to bribe anyone to end mind control while mind control Godfather continues to give
large bribes to people to continue mind control. Many of the people related to defense in mind control are given
extremely high paying jobs in Godfather and his other jewish friends' companies after they retire from mind control and
Godfather is extremely generous towards them and it is well established and well known to scum in mind control that
after retarding muslims, blacks and others in their career, they will move to paradise(tens of people from army/Pentagon
who follow whims of Billionaire Godfather are given jobs paying milllons of dollars by Godfather and his jewish cohort
in several companies) after they retire. No wonder there is no let up in mind control whatever good people try.

We know in almost all classic folk lore stories evil is too strong and too sure of itself while good is mostly weak and
just trying to protect itself from evil who is bent on damaging and eradicating the weak and the poor good but it is the
weak and poor good that finally prevails. I want to tell good American friends that evil at this stage has become too
bold and thousands of talented people are retarded every year. And it is just not muslims and blacks that are on the
line, several hundreds of brilliant whites are retarded across United States by mind control agency every year that has
become too emboldened due to lack of any accountability. Thousands of foreigners are also kept retarded in dozens of
countries including many European countries.

My only intention behind this post is that I want mind control to end from our societies. I do not have any joy in
mentioning that there are some bad jewish actors behind it. In American society there are a large number of jews who
have excelled in the professions of science, education, medicine and have made great contributions to our societies.
There are a very large number of jewish professors each of whom would have taught tens of thousands of students on top
of making extraordinary contributions to body of human knowledge through their great research. Then there are
accomplished jewish scientists whose work, research and inventions make our everyday life better. There are great jewish
doctors and surgeons who would treat countless sick people and make them recover from disease. The list of contributions
of jewish people to humanity is very long and it continues. Then there are a large number of ordinary jewish folks who
are known for their goodness and civility to other people in the society. When we know all of this, we do not want to
say anything anti-jewish to hurt the feelings of so many good jewish people. But I still have to say there are really
some bad people who are unconnected with most of the nice and accomplished jews and they instigate and continue cruel
mind control torture on talented people of other ethnicities, religions and countries based on their personal dislike
and hatred. My purpose is only to end the mind control victimization and torture on otherwise nice and talented people
and I do not have any hidden intentions beyond that. And I am sure American society knows very well about the
contributions of good Jews to both their country and broader humanity and my exposing some bad actors would never have
any bad effect of any kind on these good and nice jews who we all respect and who are our role models.I want to tell
friends something I have said before here that I am sure American society would eventually end the menace of mind
control from their and other countries. I want to request all good Americans and Europeans to come forward and invite
any investigative journalist you know to read my threads and ask them to help end the menace of mind control in our
societies through their investigative journalism. Without any accountability evil will continue to grow stronger and
then mind control would start to threaten even those people who consider themselves safe due to affiliations, status or
wealth.

I want to request CNN, New York Times, Washington Post, Al-Jazeera and large reputed European media outlets to run a
comprehensive story on mind control torture, retarding and victimization of intelligent people of US and other nations
by scum in US army on behest of some powerful people in United States and due to rightwing extremist biases of these
scumloads. If you would like to do investigative research about animal practices of US army, one great resource would be
mainland European embassies in Muslim countries who keep a detailed account of mind control persecution of intelligent
muslims in these countries by scum in US army. Many of the staff in mainland European embassies are very good human
beings who abhor such practices and would love to cooperate with good journalists in exposing the evil animal practices
of US army scum. Only the accounts of people at mainland European embassies in muslim countries thorough animal
practices of American army's mind control wing would be enough to drop a great bombshell in the media and general public
all across the world. I want to warn all the good people who try to have a civilized dialogue with scum in American army
to end their evil practices that their being nice with US army scumloads is a very misguided approach. Since good people
do not have the power to forcefully end the evil practices of US army scum, only way to end the evil practices of US
army crooks is by exposing them openly in US public and all across the world.

It seems that scum in American army and mind control are unable to pay a heed to civilized calls by good American people
and others to end their animal cruel practices and remain bent on mischief. If crooks in American army and mind
control remain adamant on continuing evil practices, the only solution seems that some brave investigative journalists
expose them by running a comprehensive story on mind control practices by American army. It seems that doing a civilized
dialogue with hardened crooks in mind control gives them a strong sense of weakness of good people and makes the crooks
even more adamant to continue their evil practices.  Reminds me of Abu-Gharib. Very similarly, scum in defense had no
conception that they were doing any wrong thing when there was a culture of openly urinating on human captives. It was
an open thing in army and most scumloads thought it was indeed a very right thing to do( and I am sure some of those
crooks still believe that it was a right thing they did even after being reprimanded by the broader American society).
It was not until brave people at CNN did a daring story against animal practices by crooks that evil practices stopped.
Though American army scumloads retard intelligent people of all color and creed, these ultra right wing army scumloads
love to retard blacks and muslims with great relish. Blacks are only 8-10% of US population but make a very large
proportion of victims in united states since many ultra right wing scum in US army would rather die than let those
intelligent blacks succeed in American society in a big way.

---

### #2048 — Amin (Topic Author)
*November 5, 2023, 7:31 PM*

Friends, I have been trying to concentrate on my research work again. I have written an algorithm that can make all sort
of interesting SV grids in context of stochastic volatility monte carlo.

With new grid, most of the grid cells have different probability mass, and we want to use regression on standard normal
array(with probability of each normal subdivision equal to one monte carlo path) to calculate the coeffs of Z-series. We
would need a different sized array of normal random variable for regression and moment matching and it would take quite
some time when we do it over all SV subdivisions. I have tried an alternative and I ran optimizations on 1250 different
underlying grid sizes and results of 1250 X 4 array are stored in a  file.  Later, moment matching parameters are read
from the file once and these parameters are interpolated to find the appropriate parameters for the moment matching of
underlying standard normal. This is instantaneous and saves a lot of time in computation.

I am focusing on my work and will continue to do my research and post the research and programs on wilmott in coming
days.

---

### #2049 — Amin (Topic Author)
*November 7, 2023, 3:13 PM*

Friends, I have made the following changes to my previous program.

1. I have created a new probability grid for the random variable data(monte carlo paths in our case). In this grid, you
specify the maximum probability mass in a grid cell and a minimum probability mass in a grid cell and then probability
mass in any grid cell is proportional to standard normal probability density. So if I specify max grid probability to 1%
and min grid probability to .02% and total number of monte carlo paths are 500000 (half a million), then in the
constructed grid a few grid cells next to median would have 5000 paths and a few grid cells in the tails would have only
100 paths while in between there will be a variable number(proportional to standard normal density there and rounded to
min probability granularity) of paths with a granularity(multiple of) of 100 paths. You can specify any number for max
paths/max probability and min paths/min probability to make all sort of interesting grids. Such a grid can easily get
last cells in the tail get close to Z=3.75 in the tail.

2. Since our new grid has cells that have different probability mass probability, I had to change a few things related
to polynomial regression.

When we know underlying Z along the variable grid cells, as is the case when we have calculated Z-series coefficients
independently for each grid cell but we want to calculate coefficients of coefficients(Z-series for each coefficient). I
have added a numerical moment matching that slightly alters the underlying Z's related to each volatility subdivision
but this moment matching is done with respect to variable probability mass along the grid cells. Earlier we did this
moment matching for monte carlo paths that had an equal probability associated with them. But in this new program, I
have done moment matching of array of underlying Z whose elements are associated with all of the grid cells and this
moment matching is done with respect to underlying probability mass associated with each value of Z associated with that
grid cell.

I have used the old moment matching program but altered the underlying probabilities from equiprobable case( that was
for monte carlo paths carrying equal probability of realization) to  variable probability mass associated with each
underlying volatility grid cell.

3. I have used weighted least squares regression in the estimation of parameters in the case of volatility grid scenario
that is discussed in previous paragraph. I assigned a regression weight proportional to probability mass in that
subdivision along the volatility grid to calculate the coefficients of Z-series.

Again in my matlab program, I divided the monte carlo paths from stochastic volatility set of SDEs into volatility grid
cells along the increasing probability density of stochastic volatility. For each of these volatility grid cells, I
calculated Z-series representation of conditional asset random values associated with that particular volatility grid
cell. So there are as many conditional asset Z-series as there are volatility grid cells. These Z-series are numerically
calculated individually for asset conditional on each different cell along the volatility grid.

Each conditional Z-series can be represented as

$X(Z_v) \, = \, c_0(Z_v) \, +\, c_1(Z_v) \, Z_x \,+\, c_2(Z_v) \, {Z_x}^2 \,+\, c_3(Z_v) \, {Z_x}^3 \,+\, c_4(Z_v) \, {Z_x}^4 \,+\, c_5(Z_v) \, {Z_x}^5 \,$

Then I take each coefficient of the conditional asset Z-series along the entire volatility grid and represent it as a
further Z-series along the volatility grid as following ( I have previously called it calculation of coefficients of
coefficients)

$c_0(Z_v) \,=\, a_{00} \, + \, a_{01} \, Z_v\,+ \, a_{02} \, { Z_v}^2\,+ \, a_{03} \, {Z_v}^3\,+ \, a_{04} \, {Z_v}^4\,+ \, a_{05} \, {Z_v}^5\,$

$c_1(Z_v) \,=\, a_{10} \, + \, a_{11} \, Z_v\,+ \, a_{12} \, { Z_v}^2\,+ \, a_{13} \, {Z_v}^3\,+ \, a_{14} \, {Z_v}^4\,+ \, a_{15} \, {Z_v}^5\,$

$c_2(Z_v) \,=\, a_{20} \, + \, a_{21} \, Z_v\,+ \, a_{22} \, { Z_v}^2\,+ \, a_{23} \, {Z_v}^3\,+ \, a_{24} \, {Z_v}^4\,+ \, a_{25} \, {Z_v}^5\,$

$c_3(Z_v) \,=\, a_{30} \, + \, a_{31} \, Z_v\,+ \, a_{32} \, { Z_v}^2\,+ \, a_{33} \, {Z_v}^3\,+ \, a_{34} \, {Z_v}^4\,+ \, a_{35} \, {Z_v}^5\,$

$c_4(Z_v) \,=\, a_{40} \, + \, a_{41} \, Z_v\,+ \, a_{42} \, { Z_v}^2\,+ \, a_{43} \, {Z_v}^3\,+ \, a_{44} \, {Z_v}^4\,+ \, a_{45} \, {Z_v}^5\,$

$c_5(Z_v) \,=\, a_{50} \, + \, a_{51} \, Z_v\,+ \, a_{52} \, { Z_v}^2\,+ \, a_{53} \, {Z_v}^3\,+ \, a_{54} \, {Z_v}^4\,+ \, a_{55} \, {Z_v}^5\,$

Here are some graphs that show a comparison of above six conditional asset Z-series coefficients along the volatility
grid as numerically and individually calculated along each volatility grid VS analytically calculated after calculation
of the above further Z-series (Z-series of Z-series coefficients as given in equations above) along the volatility grid.
The graphs came after I made the improvements in the program I have mentioned at the start. I will be posting a new
matlab program for this in a day or two.

[![Image](../images/i.postimg.cc/B6JXpJfm/CCoeffs01-A.png)](https://postimg.cc/DWYvykZG)

[![Image](../images/i.postimg.cc/0NR66pWR/CCoeffs01-B.png)](https://postimg.cc/Jsx7vBCP)

[![Image](../images/i.postimg.cc/Gms8hMjx/CCoeffs01-C.png)](https://postimg.cc/cv04FB2v)

[![Image](../images/i.postimg.cc/cJRvfr2K/CCoeffs01-D.png)](https://postimg.cc/Y4S2Hqpk)

[![Image](../images/i.postimg.cc/xTZNQrLd/CCoeffs01-E.png)](https://postimg.cc/crQL7b9q)

[![Image](../images/i.postimg.cc/gkjL1cX5/CCoeffs01-F.png)](https://postimg.cc/8j8C6SbB)

---

### #2050 — Amin (Topic Author)
*November 7, 2023, 3:33 PM*

Below are the SV + Asset SDEs parameters associated with monte carlo simulation that was used to create above graphs.
With the latest improvements in the program, the results are even better than we had in the last matlab program I
posted.

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

gammaX=.95;

%%%%%%%%`%%%%%

V0=.35;

thetaV=.06;

kappaV=1.250;

mu1=kappaV*thetaV;

mu2=-kappaV;

beta1=0;

beta2=1;

gamma=.6;

sigma0=1.0;

dt=.03125/2;

Tt=64*2;

T=Tt*dt;

---

[← Previous](page_040.md) | [Index](index.md) | [Next →](page_042.md)
