# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 35 of 59** — Posts #1701–#1750

[← Previous](page_034.md) | [Index](index.md) | [Next →](page_036.md)

---

### #1701 — Amin (Topic Author)
*February 5, 2023, 4:14 PM*

In this second post today, I really want to ask friends for help. My persecution by mind control agencies continues with
full resolve. Underground water in the city already has mind control drugs in it and I am surviving by carefully buying
earlier manufactured water from remote places in the city. Nestle and Dasani water were both good until Dec 2022. Both
nestle and coca-cola drugged their water in Dec 2022. And water by both companies  manufactured in Jan 2023 is also
drugged with mind control chemicals. But dasani (coca-cola water) manufactured in Dec 2022 although drugged is drinkable
since it is very lightly drugged however dasani water manufactured in Jan 2023 is worse. Also Nestle water manufactured
in Jan 2023 is also worse and I try to avoid nestle water altogether since it is worse than dasani water.

I have been able to survive by buying older manufactured water in remote parts of the city where pak army has not gone
to drug water in the entire markets. Water of even earlier manufacturing dates is highly drugged in areas adjacent to
Johar town (where I live) since it was manually drugged by army.

Another positive thing happened that I Was able to buy a relatively good injection last time. I had noticed that
antipsychotic injections with some manufacturing dates were highly drugged with mind control drugs and it was extremely
difficult to even pass time after getting those injections and I would become extremely miserable after getting those
drugged injections. These injections(with particular expiry dates that are bad) are flooded in the market. However there
are injections with few other dates that are better and only have mild amount of mind control drugs in them. And this
time last Thursday, I Was able to quickly buy, from a remote place in the city, an injection with the right expiry date.
Getting a better injection that did not have mind control drugs is one reason that I have not become completely
miserable and have been able to pass time in a better way. That is one reason that I have continued to concentrate on my
research.

But mind control agents continue to try very hard to decrease my consciousness and take neurotransmitters out of my
brain. Despite getting a good injection and reasonable food and water, I still become very exhausted and have phases of
remarked decreased consciousness since mind control agents have increased their efforts to take neurotransmitters out of
my brain.

Another thing I noticed that my eye-sight remarkably deteriorated in past one week that coincides with the time when
they have been desperately trying to take neurotransmitters out of my brain. I still recall that I was trying to put
thread in a needle a few days ago and could not do that despite trying for 7-10 minutes.

I want to request friends to please protest to US government to end my mind control . Please also ask Coca-cola, nestle,
and pepsi-cola to not drug water in Lahore city. And also ask Lundbeck which is manufacturer of Fluanxol injections to
not add mind control drugs to anti-psychotic injections.

I have been able to get good water from a few remote places randomly but it will continue to become very difficult if
Nestle and coca-cola continued to add mind control chemicals in their water. Winter is already gone and temperatures are
fast increasing here in Lahore.

---

### #1702 — Amin (Topic Author)
*February 10, 2023, 9:09 AM*

Friends, I will be posting my  new programs in a few days. In the meantime, I wanted to write a small post about
importance of using new hermite correlations, that I discussed in some of the past posts, in asset management.

As we know that a large part of asset management is concerned with appropriate diversification of the financial
portfolio. And typically pearson correlation is used for the purpose of measuring co-movement of returns of the
components of the portfolio. But as we learnt after comparison with hermite correlations, that pearson correlation is
good only in the mid of the density of portfolio returns (between underlying -1.5 Z to +1.5 Z) i.e where first hermite
polynomial is usually dominant and higher hermite polynomials are typically smaller. But for portfolio returns in the
tails (beyond +- 2 Z) , the contribution to portfolio return correlation from higher hermite kicks in and this
contribution can be extremely large when portfolio returns go deep into the tails. This also explains the stylized fact
that pearson correlation works reasonably well in normal market conditions but when portfolio components returns go deep
into the tails, pearson correlation breaks down and many people complain about totally correlated market. This is
precisely because correlations from higher hermites cause large increase in the correlation when the portfolio returns
are deep in the tail.

Ans this can help us revisit portfolio optimization from a new perspective. While increasing diversification of the
portfolio, it will be understandable to  add stocks or financial assets in portfolio whose higher hermites have little
correlation or negative correlation with respect to hermites of other assets in the portfolio. Since portfolio
diversification has to work its best when the portfolio is under stress, we have to make sure that higher hermites in
the portfolio are as little (or possibly negatively correlated when required) correlated as possible since these hermite
correlations kick in a big way when portfolio returns are deep in the tail due huge market stress. Using simple pearson
correlation is not a good way to increase diversification when portfolio is under stress and portfolio returns are in
the tails.

Similarly it would be interesting to do research on the effectiveness of the portfolio management due to correlations
from skew-hermites(even ones) and variance and kurtosis hermites (the odd ones) and risk-manage using skew-hermites so
that downward risk is minimized while upward risk is unaffected as much as it can be possible while maximizing the total
returns of the portfolio.

I have some stocks data from S&P components and I will try to put together some correlation analysis on chosen stocks
but it will be at least a  weeks or more before I could do that.

---

### #1703 — Amin (Topic Author)
*February 11, 2023, 4:58 AM*

I will be posting, in a few days, a full-fledged matlab program using real stocks data (that I will share) with
calculations of hermite-correlations, covariances and distributions of returns of several stocks which I will later try
to extend towards optimization of the risk/reward frontier in choice of a portfolio.

---

### #1704 — Amin (Topic Author)
*February 12, 2023, 9:43 PM*

Friends, today I wrote a small program based on daily stock data and was able to calculate hermite correlations between
daily returns and also do one variable regressions based on calculated correlations. I will be posting the program later
tomorrow.

It seemed that for the small duration of one day, hermite correlations between daily returns were quite close to pearson
correlations.

---

### #1705 — Amin (Topic Author)
*February 13, 2023, 10:57 AM*

Friends, I am sharing graphs of hermite-correlations based regressions of daily log-returns of six tech stocks on Nasdaq
100 daily log returns. X-axis is Nasdaq 100 daily log-return and Y-axis is tech stock daily log-return.

These are pretty bland graphs and have very little non-linearity since the data has been thoroughly averaged over more
than a year of observations. In some other experiments I was able to get very interesting nonlinear shapes of the simple
one variable regressions.

However you can still see some slight non-linearities in meta regression and Nvidia regression to a smaller extent.

Here are the graphs. I will follow by posting the program that did all the calculations to make these graphs.

[![Image](../images/i.postimg.cc/g2SbGWdb/Regression01.jpg)](https://postimg.cc/BjKVCRXm)

[![Image](../images/i.postimg.cc/nhct8Ly1/Regression02.jpg)](https://postimg.cc/tYfcW9C1)

[![Image](../images/i.postimg.cc/sDJR0WNX/Regression03.jpg)](https://postimg.cc/JGtgssmV)

[![Image](../images/i.postimg.cc/ncxJk2Tg/Regression04.jpg)](https://postimg.cc/QVfwNp2J)

[![Image](../images/i.postimg.cc/SR6p4YQg/Regression05.jpg)](https://postimg.cc/BPnzc6KF)

[![Image](../images/i.postimg.cc/kMKCKzNW/Regression06.jpg)](https://postimg.cc/8spxVy0C)

---

### #1706 — Amin (Topic Author)
*February 13, 2023, 11:18 AM*

I used this program and attached functions to do all the correlation and regression calculations and then draw the
graphs that I showed in previous post.

If some function is missing, please check if I have posted it before and otherwise mention and I will post. I think I
have posted here every function required to run the program.

.

.

```
function [] = CalculateDensitiesAndCorrsTechStocks02()

%Below, read AAPL, AMZN, GOOGL,META,MSFT,NVDA, NASDAQ100 daily open and
%close data files and extract daily open from the files. All files are
%exactly the same length and therefore corresponding array entries are
%from the same dates.
T = readtable('C:\Users\Hp\Documents\HistoricalPricesAAPL2022.csv');
[NDays,NVar]=size(T);
ApplPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesAMZN2022.csv');
AmznPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesGOOGL2022.csv');
GooglPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesMETA2022.csv');
MetaPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesMSFT2022.csv');
MsftPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesNVDA2022.csv');
NvdaPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesNASDAQ1002022.csv');
NasdaqPrices(1:NDays)=table2array(T(1:NDays,2));

%Below calculate daily log-returns of each stock and nasdaq 100.
DApplPrices(1:NDays-1)=log(ApplPrices(2:NDays))-log(ApplPrices(1:NDays-1));
DAmznPrices(1:NDays-1)=log(AmznPrices(2:NDays))-log(AmznPrices(1:NDays-1));
DGooglPrices(1:NDays-1)=log(GooglPrices(2:NDays))-log(GooglPrices(1:NDays-1));
DMetaPrices(1:NDays-1)=log(MetaPrices(2:NDays))-log(MetaPrices(1:NDays-1));
DMsftPrices(1:NDays-1)=log(MsftPrices(2:NDays))-log(MsftPrices(1:NDays-1));
DNvdaPrices(1:NDays-1)=log(NvdaPrices(2:NDays))-log(NvdaPrices(1:NDays-1));
DNasdaqPrices(1:NDays-1)=log(NasdaqPrices(2:NDays))-log(NasdaqPrices(1:NDays-1));

%Below calculate first four raw moments of daily log returns. Since I was
%dealing with daily log-returns, I thought first four moments should be
%enough and calculating higher moments for density and correlation
%calculations for this data would be an over-kill.
NDays0=NDays-1;
rMuAppl=CalculateFourRawMomentsFromData(DApplPrices,NDays0);
rMuAmzn=CalculateFourRawMomentsFromData(DAmznPrices,NDays0);
rMuGoogl=CalculateFourRawMomentsFromData(DGooglPrices,NDays0);
rMuMeta=CalculateFourRawMomentsFromData(DMetaPrices,NDays0);
rMuMsft=CalculateFourRawMomentsFromData(DMsftPrices,NDays0);
rMuNvda=CalculateFourRawMomentsFromData(DNvdaPrices,NDays0);
rMuNasdaq=CalculateFourRawMomentsFromData(DNasdaqPrices,NDays0);

clf;
%Below construct log-return densities from first four moments
[c10,c1] = CalculateZSeriesDensityFromRawMomentsM4(rMuAppl)
str=input('Look at density of Apple daily log returns')

[c20,c2] = CalculateZSeriesDensityFromRawMomentsM4(rMuAmzn)
str=input('Look at density of Amazon daily log returns')

[c30,c3] = CalculateZSeriesDensityFromRawMomentsM4(rMuGoogl)
str=input('Look at density of Google daily log returns')

[c40,c4] = CalculateZSeriesDensityFromRawMomentsM4(rMuMeta)
str=input('Look at density of Meta daily log returns')

[c50,c5] = CalculateZSeriesDensityFromRawMomentsM4(rMuMsft)
str=input('Look at density of Microsoft daily log returns')
[c60,c6] = CalculateZSeriesDensityFromRawMomentsM4(rMuNvda)
str=input('Look at density of Nvidia daily log returns')

[c70,c7] = CalculateZSeriesDensityFromRawMomentsM4(rMuNasdaq)
str=input('Look at density of Nasdaq100 daily log returns')

%Below calculate Z value for each realization of log-returns. This function
%takes an array of log-returns and returns an array of corresponding Z
%vlues in output array.

[ZAppl] = CalculateZgivenXAndZSeriesC3(DApplPrices,c10,c1);

DApplPrices-(c10+c1(1).*ZAppl+c1(2).*ZAppl.^2+c1(3).*ZAppl.^3)
%If the difference above does not go to zero, their will be inaccuracies in
%correlation calculations and following regressions.
str=input('Look at APPL difference between log-returns and their values constructed from Z-series');

[ZAmzn] = CalculateZgivenXAndZSeriesC3(DAmznPrices,c20,c2);

DAmznPrices-(c20+c2(1).*ZAmzn+c2(2).*ZAmzn.^2+c2(3).*ZAmzn.^3)
%If the difference above does not go to zero, their will be inaccuracies in
%correlation calculations and following regressions.
str=input('Look at AMZN difference between log-returns and their values constructed from Z-series');

[ZGoogl] = CalculateZgivenXAndZSeriesC3(DGooglPrices,c30,c3);

DGooglPrices-(c30+c3(1).*ZGoogl+c3(2).*ZGoogl.^2+c3(3).*ZGoogl.^3)
%If the difference above does not go to zero, their will be inaccuracies in
%correlation calculations and following regressions.
str=input('Look at Googl difference between log-returns and their values constructed from Z-series');

[ZMeta] = CalculateZgivenXAndZSeriesC3(DMetaPrices,c40,c4);
DMetaPrices-(c40+c4(1).*ZMeta+c4(2).*ZMeta.^2+c4(3).*ZMeta.^3)
%If the difference above does not go to zero, their will be inaccuracies in
%correlation calculations and following regressions.
str=input('Look at META difference between log-returns and their values constructed from Z-series');

[ZMsft] = CalculateZgivenXAndZSeriesC3(DMsftPrices,c50,c5);
DMsftPrices-(c50+c5(1).*ZMsft+c5(2).*ZMsft.^2+c5(3).*ZMsft.^3)
%If the difference above does not go to zero, their will be inaccuracies in
%correlation calculations and following regressions.
str=input('Look at MSFT difference between log-returns and their values constructed from Z-series');

[ZNvda] = CalculateZgivenXAndZSeriesC3(DNvdaPrices,c60,c6);
DNvdaPrices-(c60+c6(1).*ZNvda+c6(2).*ZNvda.^2+c6(3).*ZNvda.^3)
%If the difference above does not go to zero, their will be inaccuracies in
%correlation calculations and following regressions.
str=input('Look at NVDA difference between log-returns and their values constructed from Z-series');

[ZNasdaq] = CalculateZgivenXAndZSeriesC3(DNasdaqPrices,c70,c7);
DNasdaqPrices-(c70+c7(1).*ZNasdaq+c7(2).*ZNasdaq.^2+c7(3).*ZNasdaq.^3)
%If the difference above does not go to zero, their will be inaccuracies in
%correlation calculations and following regressions.
str=input('Look at NASDAQ100 difference between log-returns and their values constructed from Z-series');

%Below calculate hermite coefficients from Z-series coefficients
[ch10,ch1]=ConvertZCoeffsToHCoeffs(c10,c1,3);
[ch20,ch2]=ConvertZCoeffsToHCoeffs(c20,c2,3);
[ch30,ch3]=ConvertZCoeffsToHCoeffs(c30,c3,3);
[ch40,ch4]=ConvertZCoeffsToHCoeffs(c40,c4,3);
[ch50,ch5]=ConvertZCoeffsToHCoeffs(c50,c5,3);
[ch60,ch6]=ConvertZCoeffsToHCoeffs(c60,c6,3);
[ch70,ch7]=ConvertZCoeffsToHCoeffs(c70,c7,3);

%In what follows, I will calculate correlations of first three hermites
%between each of the six tech stocks and Nasdaq100 index. And finally I
%will draw scatter-plots of joint observations of daily log-returns of each of the
%tech stocks against Nasdaq100 index returns. And then construct the
%conditional regression based graph of each of the tech stock returns VS
%Nasdaq100 returns.

%Below calculate correlations of first three hermites between APPL
%log-returns and Nasdaq100 log rturns.
rho17_1=sum(ZAppl.*ZNasdaq)/sqrt(sum(ZAppl.^2).*sum(ZNasdaq.^2))
rho17_2=sum((ZAppl.^2-1).*(ZNasdaq.^2-1))/sqrt(sum((ZAppl.^2-1).^2).*sum(((ZNasdaq.^2)-1).^2))
rho17_3=sum((ZAppl.^3-3*ZAppl).*(ZNasdaq.^3-3*ZNasdaq))/sqrt(sum((ZAppl.^3-3.*ZAppl).^2).*sum((ZNasdaq.^3-3*ZNasdaq).^2))

%Below calculate correlations of first three hermites between AMZN
%log-returns and Nasdaq100 log rturns.
rho27_1=sum(ZAmzn.*ZNasdaq)/sqrt(sum(ZAmzn.^2).*sum(ZNasdaq.^2))
rho27_2=sum((ZAmzn.^2-1).*(ZNasdaq.^2-1))/sqrt(sum((ZAmzn.^2-1).^2).*sum(((ZNasdaq.^2)-1).^2))
rho27_3=sum((ZAmzn.^3-3*ZAmzn).*(ZNasdaq.^3-3*ZNasdaq))/sqrt(sum((ZAmzn.^3-3.*ZAmzn).^2).*sum((ZNasdaq.^3-3*ZNasdaq).^2))

%Below calculate correlations of first three hermites between Googl
%log-returns and Nasdaq100 log rturns.
rho37_1=sum(ZGoogl.*ZNasdaq)/sqrt(sum(ZGoogl.^2).*sum(ZNasdaq.^2))
rho37_2=sum((ZGoogl.^2-1).*(ZNasdaq.^2-1))/sqrt(sum((ZGoogl.^2-1).^2).*sum(((ZNasdaq.^2)-1).^2))
rho37_3=sum((ZGoogl.^3-3*ZGoogl).*(ZNasdaq.^3-3*ZNasdaq))/sqrt(sum((ZGoogl.^3-3.*ZGoogl).^2).*sum((ZNasdaq.^3-3*ZNasdaq).^2))

%Below calculate correlations of first three hermites between META
%log-returns and Nasdaq100 log rturns.

rho47_1=sum(ZMeta.*ZNasdaq)/sqrt(sum(ZMeta.^2).*sum(ZNasdaq.^2))
rho47_2=sum((ZMeta.^2-1).*(ZNasdaq.^2-1))/sqrt(sum((ZMeta.^2-1).^2).*sum(((ZNasdaq.^2)-1).^2))
rho47_3=sum((ZMeta.^3-3*ZMeta).*(ZNasdaq.^3-3*ZNasdaq))/sqrt(sum((ZMeta.^3-3.*ZMeta).^2).*sum((ZNasdaq.^3-3*ZNasdaq).^2))

%Below calculate correlations of first three hermites between MSFT
%log-returns and Nasdaq100 log rturns.

rho57_1=sum(ZMsft.*ZNasdaq)/sqrt(sum(ZMsft.^2).*sum(ZNasdaq.^2))
rho57_2=sum((ZMsft.^2-1).*(ZNasdaq.^2-1))/sqrt(sum((ZMsft.^2-1).^2).*sum(((ZNasdaq.^2)-1).^2))
rho57_3=sum((ZMsft.^3-3*ZMsft).*(ZNasdaq.^3-3*ZNasdaq))/sqrt(sum((ZMsft.^3-3.*ZMsft).^2).*sum((ZNasdaq.^3-3*ZNasdaq).^2))

%Below calculate correlations of first three hermites between NVDA
%log-returns and Nasdaq100 log
rturns.ays0-1).^3-3*ZNasdaq(1:NDays0-1)))/sqrt(sum((ZMsft(2:NDays0).^3-3.*ZMsft(2:NDays0)).^2).*sum((ZNasdaq(1:NDays0-1).^3-3*ZNasdaq(1:NDays0-1)).^2))

rho67_1=sum(ZNvda.*ZNasdaq)/sqrt(sum(ZNvda.^2).*sum(ZNasdaq.^2))
rho67_2=sum((ZNvda.^2-1).*(ZNasdaq.^2-1))/sqrt(sum((ZNvda.^2-1).^2).*sum(((ZNasdaq.^2)-1).^2))
rho67_3=sum((ZNvda.^3-3*ZNvda).*(ZNasdaq.^3-3*ZNasdaq))/sqrt(sum((ZNvda.^3-3.*ZNvda).^2).*sum((ZNasdaq.^3-3*ZNasdaq).^2))

%Below do calculations to do regressions with daily log-returns of each
%tech stock as dependent variables and Nasdaq100 as independent variable.

dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=45*4;  % No of normal density subdivisions
NnMid=((1+Nn)/2)*dNn;
ZNasdaq0(1:Nn)=(((1:Nn)*dNn)-NnMid);

%Below reconstruct the Z-series representation of returns of each of the
%tech stock as a function of ZNasdaq, i.e the Z that underlies Nasdaq log
%returns. This is regression of each tech stock log-returns on log-returns of Nasdaq 100.
XAppl(1:Nn)=(ch10)+rho17_1.*(ch1(1))*ZNasdaq0(1:Nn)+rho17_2.*ch1(2).*(ZNasdaq0(1:Nn).^2-1)+rho17_3.*ch1(3).*(ZNasdaq0(1:Nn).^3-3*ZNasdaq0(1:Nn));
XAmzn(1:Nn)=(ch20)+rho27_1.*(ch2(1))*ZNasdaq0(1:Nn)+rho27_2.*ch2(2).*(ZNasdaq0(1:Nn).^2-1)+rho27_3.*ch2(3).*(ZNasdaq0(1:Nn).^3-3*ZNasdaq0(1:Nn));
XGoogl(1:Nn)=(ch30)+rho37_1.*(ch3(1))*ZNasdaq0(1:Nn)+rho37_2.*ch3(2).*(ZNasdaq0(1:Nn).^2-1)+rho37_3.*ch3(3).*(ZNasdaq0(1:Nn).^3-3*ZNasdaq0(1:Nn));
XMeta(1:Nn)=(ch40)+rho47_1.*(ch4(1))*ZNasdaq0(1:Nn)+rho47_2.*ch4(2).*(ZNasdaq0(1:Nn).^2-1)+rho47_3.*ch4(3).*(ZNasdaq0(1:Nn).^3-3*ZNasdaq0(1:Nn));
XMsft(1:Nn)=(ch50)+rho57_1.*(ch5(1))*ZNasdaq0(1:Nn)+rho57_2.*ch5(2).*(ZNasdaq0(1:Nn).^2-1)+rho57_3.*ch5(3).*(ZNasdaq0(1:Nn).^3-3*ZNasdaq0(1:Nn));
XNvda(1:Nn)=(ch60)+rho67_1.*(ch6(1))*ZNasdaq0(1:Nn)+rho67_2.*ch6(2).*(ZNasdaq0(1:Nn).^2-1)+rho67_3.*ch6(3).*(ZNasdaq0(1:Nn).^3-3*ZNasdaq0(1:Nn));
XNasdaq(1:Nn)=ch70+ch7(1)*ZNasdaq0(1:Nn)+ch7(2).*(ZNasdaq0(1:Nn).^2-1)+ch7(3).*(ZNasdaq0(1:Nn).^3-3*ZNasdaq0(1:Nn))

clf
hold on

scatter(DNasdaqPrices(1:NDays0),DApplPrices(1:NDays0))
plot(XNasdaq(1:Nn),XAppl(1:Nn),'g')
title('Regression of daily log returns of Apple on Daily log-returns of NASDAQ 100');
str=input('Look at scatterplot and regression between Apple daily log returns and Nasdaq100 daily log-returns');

clf
hold on

scatter(DNasdaqPrices(1:NDays0),DAmznPrices(1:NDays0))
plot(XNasdaq(1:Nn),XAmzn(1:Nn),'g')
title('Regression of daily log returns of Amazon on Daily log-returns of NASDAQ 100');
str=input('Look at scatterplot and regression between Amazon daily log returns and Nasdaq100 daily log-returns');

clf
hold on

scatter(DNasdaqPrices(1:NDays0),DGooglPrices(1:NDays0))
plot(XNasdaq(1:Nn),XGoogl(1:Nn),'g')
title('Regression of daily log returns of Google on Daily log-returns of NASDAQ 100');
str=input('Look at scatterplot and regression between Google daily log returns and Nasdaq100 daily log-returns');

clf
hold on

scatter(DNasdaqPrices(1:NDays0),DMetaPrices(1:NDays0))
plot(XNasdaq(1:Nn),XMeta(1:Nn),'g')
title('Regression of daily log returns of Meta on Daily log-returns of NASDAQ 100');

str=input('Look at scatterplot and regression between Meta daily log returns and Nasdaq100 daily log-returns');

clf
hold on

scatter(DNasdaqPrices(1:NDays0),DMsftPrices(1:NDays0))
plot(XNasdaq(1:Nn),XMsft(1:Nn),'g')
title('Regression of daily log returns of Microsoft on Daily log-returns of NASDAQ 100');
str=input('Look at scatterplot and regression between Microsoft daily log returns and Nasdaq100 daily log-returns');

clf
hold on

scatter(DNasdaqPrices(1:NDays0),DNvdaPrices(1:NDays0))
plot(XNasdaq(1:Nn),XNvda(1:Nn),'g')
title('Regression of daily log returns of Nvidia on Daily log-returns of NASDAQ 100');
str=input('Look at scatterplot and regression between Nvidia daily log returns and Nasdaq100 daily log-returns');

clf
end

```

.

.

.

```
function [rMu] = CalculateFourRawMomentsFromData(DPrices,NDays0)

rMu(1)=sum(DPrices)/NDays0;
rMu(2)=sum(DPrices.^2)/NDays0;
rMu(3)=sum(DPrices.^3)/NDays0;
rMu(4)=sum(DPrices.^4)/NDays0;

end

```

.

.

.

```
function [c0,c] = CalculateZSeriesDensityFromRawMomentsM4(rMu)

    mOrder=4;
    [Mu1,cMu] = ConvertRawMomentsToCentralMoments(rMu,mOrder);

    sMu(1)=0;
    sMu(2)=1;
    sMu(3)=cMu(3)/cMu(2).^1.5;
    sMu(4)=cMu(4)/cMu(2).^2.0;
    %sMu(5)=cMu(5)/cMu(2).^2.5;
    %sMu(6)=cMu(6)/cMu(2).^3.0;
    %sMu(7)=cMu(7)/cMu(2).^3.5;
    %sMu(8)=cMu(8)/cMu(2).^4.0;

    iter=20;
    bGuess(1:3)=0;
    bGuess(1)=1;
    [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNewC3(sMu,bGuess,iter);

    SeriesOrder=3;
    NMoments=4;

    [F,dF] = CalculateMomentsAndDerivatives_0(sMu,c0,c,SeriesOrder,SeriesOrder,NMoments);

da(1,1)=c0;
da(2:SeriesOrder+1,1)=c(1:SeriesOrder);

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

%Replace with your own more intelligent objective function if you like.
ObjBest=100000*(abs(sMu(1)-Moments(1)))+abs(sMu(2)-Moments(2))+abs((sMu(3)-Moments(3))^(1/1.5))+abs((sMu(4)-Moments(4))^(1/2.0));

b0Best=c0;
bBest(1:SeriesOrder)=c(1:SeriesOrder);

nn=0;
while((nn.000000000001) || (abs(F(2,1))>.000000000001) || (abs(F(3,1))>.000000000001) || (abs(F(4,1))>.00000000001)  ))

    nn=nn+1;
    %Below Newton matrix equation to improve the Z-series coefficients guess at previous step.
    da=da-dF\F;

    %b0=median
    b0=da(1,1);
    b(1:SeriesOrder)=da(2:SeriesOrder+1,1);

    %[F,dF] = CalculateCumulantsAndDerivativesFromMoments_0(C,b0,b,SeriesOrder,SeriesOrder,NoOfCumulants);
    [F,dF] = CalculateMomentsAndDerivatives_0(sMu,b0,b,SeriesOrder,SeriesOrder,NMoments);
    [IsValidFlag] =1;% CheckIsValidDensity(b0,b);
    [Moments] = CalculateMomentsOfZSeries(b0,b,SeriesOrder,NMoments);

   
ObjNew=100000*(abs(sMu(1)-Moments(1)))+abs(sMu(2)-Moments(2))+abs((sMu(3)-Moments(3))^(1/1.5))+abs((sMu(4)-Moments(4))^(1/2.0));

    if((ObjBest>ObjNew) &&( IsValidFlag))

       ObjBest=ObjNew;
       b0Best=b0;
       bBest(1:SeriesOrder)=b(1:SeriesOrder);
    end

    da(1,1)=b0;
    da(2:SeriesOrder+1,1)=b(1:SeriesOrder);

end
c0=b0Best;%Best;
c(1:SeriesOrder)=bBest;%Best(1:SeriesOrder);

    c0=c0*sqrt(cMu(2));
    c=c*sqrt(cMu(2));

    c0=c0+Mu1;

[FittedMoments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Please Uncomment this if you want to see a comparison of input moments and
%fitted moments
rMu
FittedMoments
str=input('Look at comparison of fitted moments with input moments');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%COMMENT lines below if you do not want to see the density of new Z-series random variable with
%fitted moments.
%First calculate normal random variable on a grid below
dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=45*4;  % No of normal density subdivisions
NnMid=((1+Nn)/2)*dNn;
Z(1:Nn)=(((1:Nn)*dNn)-NnMid);
%Z
%str=input('Look at Z');
%Now calculate Y as a function of normal random variable.
Y(1:Nn)=c0;
for nn=1:3
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

plot(Y(1:Nn),pY(1:Nn),'b');
title('Density of the Z-Series Variable with Fitted Moments');

%str=input('Look at the density of Z-series random variable')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end

```

.

.

.

```
function [mu1,cMu] = ConvertRawMomentsToCentralMoments(Mu,mOrder)

%cu
%mu
% %mOrder
%str=input('Look at numbers');
mu1=Mu(1);
for mm=2:mOrder
    cMu(mm)=0;
    for jj=0:mm
        if(jj==0)
            cMu(mm)=cMu(mm)+ (-1)^(mm-jj).*factorial(mm)/factorial(jj)/factorial(mm-jj)*1*mu1.^(mm-jj);
        else
            cMu(mm)=cMu(mm)+ (-1)^(mm-jj).*factorial(mm)/factorial(jj)/factorial(mm-jj)*Mu(jj)*mu1.^(mm-jj);
        end
    end
end

```

.

.

.

```
function [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNewC3(cmu,cin,iter)

%Mul=1.0;
SeriesOrder=3;
NMoments=4;

 EZ(1)=0;
 EZ(2)=1;
 for nn=3:NMoments*SeriesOrder+SeriesOrder+2
     if rem(nn,2)==1
         EZ(nn)=0;
     else
         EZ(nn)=EZ(nn-2)*(nn-1);
         EZ(nn);
     end
 end

c0=-(cin(2));  %This is for zero mean condition.
c=cin;
MaxIter=10;

for nn=1:iter     %increase the iterations over coefficients if neeeded

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[M3,dc2] = CalculateParticularMomentAndDerivativeOfItsCoeff(c0,c,SeriesOrder,3,EZ);

tolerance=.0000001*cmu(3);
mm=0;
while ((abs(M3-cmu(3)) >tolerance ) && (mmtolerance ) && (mm<MaxIter))
mm=mm+1;
c(3)=c(3)-(M4-cmu(4))/dc3;

[M4,dc3] = CalculateParticularMomentAndDerivativeOfItsCoeff(c0,c,SeriesOrder,4,EZ);

end

[SecondMoment] = CalculateSecondMomentC3(c0,c);

c=c/sqrt(SecondMoment);
c0=c0/sqrt(SecondMoment);

%[c0,c] = IterateSmoothingGuessOverPreviousMoments(cmu,c,4,2,EZ);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end

end

```

.

.

.

```
function [EnMoment,dEnMomentdCoeff] = CalculateParticularMomentAndDerivativeOfItsCoeff(a0,a,SeriesOrder,nMoment,EZ)

% if(SeriesOrder>=8)
% a0=-(a(2)+3*a(4)+15*a(6)+105*a(8));% ---1
% end
% if(SeriesOrder<8)
% a0=-(a(2)+3*a(4)+15*a(6));% ---1
% end
%
% EZ(1)=0;
% EZ(2)=1;
% for nn=3:NMoments*SeriesOrder+NZterms+2
%     if rem(nn,2)==1
%         EZ(nn)=0;
%     else
%         EZ(nn)=EZ(nn-2)*(nn-1);
%         EZ(nn);
%     end
% end
% EZ;

%EXZ(1,1)=1;
%for pp1=1:NZterms
%        EXZ(1,pp1+1)=EZ(pp1);
%end

a(SeriesOrder+1:nMoment*SeriesOrder+1+SeriesOrder)=0;
b0=a0;
b=a;

for mm=2:nMoment

    [b0,b] =SeriesProduct(a0,a,b0,b,SeriesOrder*mm+SeriesOrder+1);
     b(SeriesOrder*mm+1:nMoment*SeriesOrder+SeriesOrder+1)=0;
     if(mm==nMoment-1)
         dEnMomentdCoeff=b0.*EZ(nMoment-1);
         for pp2=1:SeriesOrder*nMoment-1

            dEnMomentdCoeff=dEnMomentdCoeff+b(pp2).*EZ(pp2+nMoment-1);
        end
        dEnMomentdCoeff=dEnMomentdCoeff*nMoment;
     end
     if(mm==nMoment)
        EnMoment=b0;
        for pp2=1:SeriesOrder*nMoment
            EnMoment=EnMoment+b(pp2).*EZ(pp2);

        end
     end
end

end

```

.

.

.

```
function [c0,c] =SeriesProduct(a0,a,b0,b,SeriesOrder)

c0=a0*b0;
c(1:SeriesOrder)=0.0;
for nn=1:SeriesOrder
    c(nn)=c(nn)+a0*b(nn);
    c(nn)=c(nn)+b0*a(nn);
    for kk=1:nn-1
        c(nn)=c(nn)+a(kk)*b(nn-kk);
    end
end

end

```

.

.

.

```
function [SecondMoment] = CalculateSecondMomentC3(a0,a)

SecondMoment=a0^2+a(1)^2 +2* a0* a(2) +3*(a(2).^2+2* a(1).* a(3))+ ...
    15*(a(3).^2) ;

end

```

.

.

.

```
function [F,dF] = CalculateMomentsAndDerivatives_0(Ms,a0,a,SeriesOrder,NZterms,NMoments)
%[F,dF] = CalculateCumulantsAndDerivativesFromMoments(C,a0,a,SeriesOrder,SeriesOrder,NoOfCumulants);

%a(1)=a1;
%a(2)=a2;
%a(3)=a3;
%a(4)=a4;
%a(5)=a5;
%a(6)=a6;
%a(7)=a7;

%aa0=a0;
if(NMoments>8)
a0=-(a(2)+3*a(4)+15*a(6)+105*a(8));% ---1
end
if(NMoments==8)
a0=-(a(2)+3*a(4)+15*a(6));% ---1
end
if(NMoments==6)
a0=-(a(2)+3*a(4));% ---1
end

EZ(1)=0;
EZ(2)=1;
for nn=3:NMoments*SeriesOrder+NZterms+2
    if rem(nn,2)==1
        EZ(nn)=0;
    else
        EZ(nn)=EZ(nn-2)*(nn-1);
        EZ(nn);
    end
end
EZ;

EXZ(1,1)=1;
for pp1=1:NZterms
        EXZ(1,pp1+1)=EZ(pp1);
end

a(SeriesOrder+1:NMoments*SeriesOrder+1)=0;
b0=a0;
b=a;

for mm=1:NMoments
    if(mm>1)
        [b0,b] =SeriesProduct(a0,a,b0,b,SeriesOrder*mm);
        b(SeriesOrder*mm+1:NMoments*SeriesOrder+1)=0;
    end
   % b0
   % b
%str=input('Look at numbers')
    EXZ(mm+1,1)=b0;
    for pp2=1:SeriesOrder*mm

            EXZ(mm+1,1)=EXZ(mm+1,1)+b(pp2).*EZ(pp2);
    end
    for pp1=1:NZterms
        EXZ(mm+1,pp1+1)=b0.*EZ(pp1);
        for pp2=1:SeriesOrder*mm

            EXZ(mm+1,pp1+1)=EXZ(mm+1,pp1+1)+b(pp2).*EZ(pp2+pp1);
        end
    end
end

%u1=EXZ(2,1);
u2=EXZ(3,1);
u3=EXZ(4,1);
u4=EXZ(5,1);

u1=a0+a(2);
if(SeriesOrder>=4)
u1=a0+a(2)+3*a(4);
end
if(SeriesOrder>=6)
u1=u1+15*a(6);
end
if(SeriesOrder>=8)
u1=u1+105*a(8);
end

%k2=u2-u1^2;
%k3=u3-3*u2*u1+2*u1^3;
%k4=u4-4*u3*u1-3*u2^2+12*u2*u1^2-6*u1^4;

du1(1)=1;%----2
% du1(2)=0;%----2
% du1(3)=1;%----2
% du1(4)=0;%----2
% du1(5)=1;%----2
% du1(6)=0;%----2
% du1(7)=15;%----2
% du1(8)=0;%----2
% du1(9)=105;%----2
% du1(10)=0;%----2
 du2(1)=2*EXZ(2,1);
 du3(1)=3*EXZ(3,1);
 du4(1)=4*EXZ(4,1);

%du1(1)=1;%----2
%du2(1)=0;
%du3(1)=0;
%du4(1)=0;

for mm=2:SeriesOrder+1
du1(mm)=EXZ(1,mm);
du2(mm)=2*EXZ(2,mm);
du3(mm)=3*EXZ(3,mm);
du4(mm)=4*EXZ(4,mm);

end

if(NMoments>=5)
u5=EXZ(6,1);

%du5(1)=5*EXZ(5,1);

for mm=1:SeriesOrder+1
du5(mm)=5*EXZ(5,mm);
end

end

if(NMoments>=6)
u6=EXZ(7,1);
%du6(1)=0;

for mm=1:SeriesOrder+1
du6(mm)=6*EXZ(6,mm);
end

end

if(NMoments>=7)
u7=EXZ(8,1);
%str=input('Look at k7 and k71')

%du7(1)=0;

for mm=1:SeriesOrder+1
du7(mm)=7*EXZ(7,mm);
end

end
if(NMoments>=8)

u8=EXZ(9,1);
for mm=1:SeriesOrder+1
du8(mm)=8*EXZ(8,mm);
end

end

if(NMoments>=9)

u9=EXZ(10,1);
for mm=1:SeriesOrder+1
du9(mm)=9*EXZ(9,mm);
end

end
if(NMoments>=10)

u10=EXZ(11,1);
for mm=1:SeriesOrder+1
du10(mm)=10*EXZ(10,mm);
end

end

 F(1,1)=u1-Ms(1);
 F(2,1)=u2-Ms(2);
 F(3,1)=u3-Ms(3);
 F(4,1)=u4-Ms(4);
 if(NMoments>=5)
 F(5,1)=u5-Ms(5);
 end
 if(NMoments>=6)
 F(6,1)=u6-Ms(6);
 end
 if(NMoments>=7)
 F(7,1)=u7-Ms(7);
 end
 if(NMoments>=8)
 F(8,1)=u8-Ms(8);
 end
 if(NMoments>=9)
 F(9,1)=u9-Ms(9);
 end
 if(NMoments>=10)
 F(10,1)=u10-Ms(10);
 end

     for mm=1:SeriesOrder+1
        dF(1,mm)=du1(mm);
        dF(2,mm)=du2(mm);
        dF(3,mm)=du3(mm);
        dF(4,mm)=du4(mm);
        if(NMoments>=5)
        dF(5,mm)=du5(mm);
        end
        if(NMoments>=6)
        dF(6,mm)=du6(mm);
        end
        if(NMoments>=7)
        dF(7,mm)=du7(mm);
        end
        if(NMoments>=8)
        dF(8,mm)=du8(mm);
        end
        if(NMoments>=9)
        dF(9,mm)=du9(mm);
        end
        if(NMoments>=10)
        dF(10,mm)=du10(mm);
        end
     end

end

```

.

.

.

```
function [Moments] = CalculateMomentsOfZSeries(a0,a,SeriesOrder,NMoments)

%aa0=a0;
%a0=0;% ---1

EZ(1)=0;
EZ(2)=1;
%LogEZ(2)=0;
for nn=3:NMoments*SeriesOrder
    if rem(nn,2)==1
        EZ(nn)=0;
    else
        EZ(nn)=EZ(nn-2)*(nn-1);
        %LogEZ(nn)=log(EZ(nn-2))+log(nn-1);
        %EZ(nn);
    end
end
%EZ
%EZ(1:30)
%str=input('Look at numbers')
a(SeriesOrder+1:SeriesOrder*NMoments+1)=0;
b0=a0;
b=a;

for mm=1:NMoments
    if(mm>1)
        %[b0,b] =SeriesProductLogarithmic(a0,a,b0,b,SeriesOrder*mm);

        [b0,b] =SeriesProduct(a0,a,b0,b,SeriesOrder*mm);

        %b0-bb0

        %b-bb

        %str=input('Look at two products')

        b(SeriesOrder*mm+1:SeriesOrder*NMoments+1)=0;
    end
   % Logb=log(abs(b));
   % Signb=sign(b);
    EXZ(mm,1)=b0;
    for pp2=1:SeriesOrder*mm
        if rem(pp2,2)==0
            %EXZ(mm,1)=EXZ(mm,1)+exp(Logb(pp2)+LogEZ(pp2)).*Signb(pp2);
            EXZ(mm,1)=EXZ(mm,1)+b(pp2).*EZ(pp2);
 %           b(pp2).*EZ(pp2)
 %           exp(Logb(pp2)+LogEZ(pp2)).*Signb(pp2)
 %           mm
 %           pp2
            %str=input('Look at moment values')
        end
    end
end

for nn=1:NMoments
    Moments(nn)=EXZ(nn,1);
end

end

```

.

.

.

```
function [Z] = CalculateZgivenXAndZSeriesC3(X,c0,c)

Z=(X-c0)/c(1)-(c(2) * (X-c0).^2)/c(1).^3+(((2* c(2).^2)./c(1).^2-c(3)./c(1)).* (X-c0).^3)./c(1).^3;

for nn=1:30

    X0=c0+c(1)*Z+c(2)*Z.^2+c(3).*Z.^3;
    dX0dZ=c(1)+2.*c(2)*Z+3.*c(3).*Z.^2;
    Z=Z-(X0-X)./(dX0dZ);
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

---

### #1707 — Amin (Topic Author)
*February 13, 2023, 1:14 PM*

Sorry friends, I forgot to attach the tech stocks data and nasdaq 100 data. Here they are in this small zip file. These
are csv files. I downloaded this data yesterday from WSJ web site.

![](./images/upload_icons/zip.gif) [CSVDataFiles.zip](./download/file.php?id=10172&sid=dbc2d4837bddbe9d5f2fcde92f8934c4)
(43.32 KiB) Downloaded 80 times

I have some other very interesting ideas about calculation of dynamic correlations that prevail for reasonably small
periods of time. I will come back with a detailed post in a day.

For example, there is huge correlation between Nasdaq 100 and all stocks when calculated over a period of more than one
year. However one period ahead serial correlations when calculated over the period of more than a year was practically
zero. However there were smaller stretches of data when one period ahead serial correlations were highly significant and
that led me to ask myself how to be able to infer dynamic serial correlations from smaller stretches of data in a
reasonable way. I will do my experiments and come back with a more detailed post soon and a program in a few days.

---

### #1708 — Amin (Topic Author)
*February 14, 2023, 10:59 AM*

Friends, I continued to think about calculation of dynamic correlations and want to share my ideas with friends.

First please let me explain my framework. I will explain calculation of correlation between two stocks but it can easily
be generalized to calculation of dynamic correlations between a portfolio of stocks based on their joint time series. I
suppose that we are given diagonal variances of both stocks independently. For example we may independently calculate
the diagonal variances from several months of data but we want to calculate correlations only from data of past one week
or ten or fifteen days. In other words, we suppose that correlations are more local and changing more quickly. If there
is some structure in diagonal variances as we have in stochastic volatility, we suppose that this effect has been
independently calculated for both diagonal variances before we want to calculate the dynamic correlations over shorter
stretches. So first observation is that we have decoupled calculations of  diagonal variances and calculation of dynamic
correlations and diagonal variances that enter the calculation of dynamic correlations have already been calculated.

First some background on two variable regressions. Suppose, I am regressing Amazon stock on Nasdaq 100 index.

Variance of Nasdaq 100 = ${\sigma_{N}}^2$

Variance of Amazon = ${\sigma_{A}}^2$

Correlation between Amazon and Nasdaq = $\rho_{N,A}$

Covariance between Amazon and Nasdaq= $\rho_{N,A} \, \sigma_{N} \,\sigma_{A}$

We know from regression lemma that (please note that variables with a bar are estimated values and variables without bar
are observed values)

$\bar{X_A} \, = \frac{Cov_{N,A}}{Var_N} \, (X_N \, - \mu_{N})$

$ \, = \frac{\rho_{N,A} \, \sigma_{N} \,\sigma_{A}}{{\sigma_{N}}^2} \, (X_N \, - \mu_{N})$

$ \, = \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N})$

Incidentally we can further simplify above in context of our Z-series framework, this time with only one polynomial by
noting that

$ X_N \, - \mu_{N} \, = \,  \sigma_{N} \, Z_N$ and replacing it in last line of above equation block as

$  \bar{X_A} \, \, = \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, ( \sigma_{N} \, Z_N)$

$ \, = \rho_{N,A} \, \,\sigma_{A} \,  \, Z_N$

I added last few lines because this was basis for my hermite polynomial based regression program that I uploaded
yesterday (here with just one polynomial).

Coming back to classic form, we have

$ \bar{X_A} \,\, = \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N})$

We notice that observed value of$X_A$ is equal to predicted from regression value of$\bar{X_A}$ and a residual${R_A}$
given as

$X_A \, = \, \bar{X_A} \, + \, {R_A}$

We want to calculate a dynamic correlation so that over the small stretch of data (in which we are calculating dynamic
correlation), our predicted values are maximized and residual values are minimized. This is done by minimizing the sum
of squared residuals. This minimization from regressions is made possible since we had made calculations of diagonal
variances exogenously from a possibly larger set of data.

Doing analytics, we get sum of squared residuals (over the time interval that is relevant to us for calculation of
dynamic correlations) as

$ \sum \, {R_A}^2 \, = \sum {(\, X_A \, - \, \bar{X_A})}^2 \,$

$ \sum \, {R_A}^2 \, = \sum {(\, X_A \, - \, \big[ \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N}) \big])}^2 \,$

All the values on rhs have either been observed or calculated earlier from data independently. So we minimize the sum of
residuals with respect to correlation parameter and apply the first order condition as

$ \frac{\partial [\sum \, {R_A}^2]}{\partial \rho_{N,A}} \, =\frac{\partial \big[ \sum {(\, X_A \, - \, \big[ \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N}) \big])}^2 \,\big]}{\partial \rho_{N,A}}=0$

Solution of the above FOC would give the dynamic correlation that maximizes the predicted value of Amazon stock over the
short stretch of data and minimizes the sum of squared residuals.

You can also apply above analytics to all mutual dynamic correlations in a basket of stocks by changing as in modelling
a multivariable regression(with vectors and matrices) as opposed to single variable regression.

I believe that minimization of squared residuals is underemphasized and can also be used intelligently in changepoint
detection and regime change detection. If you can cast your model in a two regime framework or changepoint framework and
apply minimization of sum of squared residuals, the hypothesis of regime change can easily be accepted if there is a
substantial decrease in sum of squared residuals due to regime change applied to the model.

---

### #1709 — Amin (Topic Author)
*February 14, 2023, 5:18 PM*

>
> Friends, I continued to think about calculation of dynamic correlations and want to share my ideas with friends.
>
> First please let me explain my framework. I will explain calculation of correlation between two stocks but it can
easily be generalized to calculation of dynamic correlations between a portfolio of stocks based on their joint time
series. I suppose that we are given diagonal variances of both stocks independently. For example we may independently
calculate the diagonal variances from several months of data but we want to calculate correlations only from data of
past one week or ten or fifteen days. In other words, we suppose that correlations are more local and changing more
quickly. If there is some structure in diagonal variances as we have in stochastic volatility, we suppose that this
effect has been independently calculated for both diagonal variances before we want to calculate the dynamic
correlations over shorter stretches. So first observation is that we have decoupled calculations of  diagonal variances
and calculation of dynamic correlations and diagonal variances that enter the calculation of dynamic correlations have
already been calculated.
>
>
>
> First some background on two variable regressions. Suppose, I am regressing Amazon stock on Nasdaq 100 index.
>
> Variance of Nasdaq 100 = ${\sigma_{N}}^2$
>
> Variance of Amazon = ${\sigma_{A}}^2$
>
> Correlation between Amazon and Nasdaq = $\rho_{N,A}$
>
> Covariance between Amazon and Nasdaq= $\rho_{N,A} \, \sigma_{N} \,\sigma_{A}$
>
>
>
> We know from regression lemma that (please note that variables with a bar are estimated values and variables without
bar are observed values)
>
>
>
> $\bar{X_A} \, = \frac{Cov_{N,A}}{Var_N} \, (X_N \, - \mu_{N})$
>
> $ \, = \frac{\rho_{N,A} \, \sigma_{N} \,\sigma_{A}}{{\sigma_{N}}^2} \, (X_N \, - \mu_{N})$
>
> $ \, = \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N})$
>
>
>
> Incidentally we can further simplify above in context of our Z-series framework, this time with only one polynomial by
noting that
>
> $ X_N \, - \mu_{N} \, = \,  \sigma_{N} \, Z_N$ and replacing it in last line of above equation block as
>
>
>
> $  \bar{X_A} \, \, = \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, ( \sigma_{N} \, Z_N)$
>
> $ \, = \rho_{N,A} \, \,\sigma_{A} \,  \, Z_N$
>
>
>
> I added last few lines because this was basis for my hermite polynomial based regression program that I uploaded
yesterday (here with just one polynomial).
>
> Coming back to classic form, we have
>
> $ \bar{X_A} \,\, = \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N})$
>
>
>
> We notice that observed value of$X_A$ is equal to predicted from regression value of$\bar{X_A}$ and a residual${R_A}$
given as
>
> $X_A \, = \, \bar{X_A} \, + \, {R_A}$
>
>
>
> We want to calculate a dynamic correlation so that over the small stretch of data (in which we are calculating dynamic
correlation), our predicted values are maximized and residual values are minimized. This is done by minimizing the sum
of squared residuals. This minimization from regressions is made possible since we had made calculations of diagonal
variances exogenously from a possibly larger set of data.
>
>
>
> Doing analytics, we get sum of squared residuals (over the time interval that is relevant to us for calculation of
dynamic correlations) as
>
> $ \sum \, {R_A}^2 \, = \sum {(\, X_A \, - \, \bar{X_A})}^2 \,$
>
>
$ \sum \, {R_A}^2 \, = \sum {(\, X_A \, - \, \big[ \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N}) \big])}^2 \,$
>
>
>
> All the values on rhs have either been observed or calculated earlier from data independently. So we minimize the sum
of residuals with respect to correlation parameter and apply the first order condition as
>
>
>
>
$ \frac{\partial [\sum \, {R_A}^2]}{\partial \rho_{N,A}} \, =\frac{\partial \big[ \sum {(\, X_A \, - \, \big[ \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N}) \big])}^2 \,\big]}{\partial \rho_{N,A}}=0$
>
>
>
> Solution of the above FOC would give the dynamic correlation that maximizes the predicted value of Amazon stock over
the short stretch of data and minimizes the sum of squared residuals.
>
> You can also apply above analytics to all mutual dynamic correlations in a basket of stocks by changing as in
modelling a multivariable regression(with vectors and matrices) as opposed to single variable regression.
>
>
>
> I believe that minimization of squared residuals is underemphasized and can also be used intelligently in changepoint
detection and regime change detection. If you can cast your model in a two regime framework or changepoint framework and
apply minimization of sum of squared residuals, the hypothesis of regime change can easily be accepted if there is a
substantial decrease in sum of squared residuals due to regime change applied to the model.
>
.

Friends, there was a minor error in some equations above and I am copying corrected version of the above post below. I
missed the mean of dependent variable that is Amazon stock everywhere in the equations. Below is the corrected post.

.

Friends, I continued to think about calculation of dynamic correlations and want to share my ideas with friends.

First please let me explain my framework. I will explain calculation of correlation between two stocks but it can easily
be generalized to calculation of dynamic correlations between a portfolio of stocks based on their joint time series. I
suppose that we are given diagonal variances of both stocks independently. For example we may independently calculate
the diagonal variances from several months of data but we want to calculate correlations only from data of past one week
or ten or fifteen days. In other words, we suppose that correlations are more local and changing more quickly. If there
is some structure in diagonal variances as we have in stochastic volatility, we suppose that this effect has been
independently calculated for both diagonal variances before we want to calculate the dynamic correlations over shorter
stretches. So first observation is that we have decoupled calculations of  diagonal variances and calculation of dynamic
correlations and diagonal variances that enter the calculation of dynamic correlations have already been calculated.

First some background on two variable regressions. Suppose, I am regressing Amazon stock on Nasdaq 100 index.

Variance of Nasdaq 100 = ${\sigma_{N}}^2$

Variance of Amazon = ${\sigma_{A}}^2$

Correlation between Amazon and Nasdaq = $\rho_{N,A}$

Covariance between Amazon and Nasdaq= $\rho_{N,A} \, \sigma_{N} \,\sigma_{A}$

We know from regression lemma that (please note that variables with a bar are estimated values and variables without bar
are observed values)

$\bar{X_A} \, = \mu_{A} \, + \, \frac{Cov_{N,A}}{Var_N} \, (X_N \, - \mu_{N})$

$ \, = \mu_{A} \, + \,\frac{\rho_{N,A} \, \sigma_{N} \,\sigma_{A}}{{\sigma_{N}}^2} \, (X_N \, - \mu_{N})$

$ \, = \mu_{A} \, + \,\frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N})$

Incidentally we can further simplify above in context of our Z-series framework, this time with only one polynomial by
noting that

$ X_N \, - \mu_{N} \, = \,  \sigma_{N} \, Z_N$ and replacing it in last line of above equation block as

$  \bar{X_A} \, \, = \mu_{A} \, + \,\frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, ( \sigma_{N} \, Z_N)$

$ \, = \mu_{A} \, + \,\rho_{N,A} \, \,\sigma_{A} \,  \, Z_N$

I added last few lines because this was basis for my hermite polynomial based regression program that I uploaded
yesterday (here with just one polynomial).

Coming back to classic form, we have

$ \bar{X_A} \,\, =\mu_{A} \, + \, \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N})$

We notice that observed value of$X_A$ is equal to predicted from regression value of$\bar{X_A}$ and a residual${R_A}$
given as

$X_A \, = \, \bar{X_A} \, + \, {R_A}$

We want to calculate a dynamic correlation so that over the small stretch of data (in which we are calculating dynamic
correlation), our predicted values are maximized and residual values are minimized. This is done by minimizing the sum
of squared residuals. This minimization from regressions is made possible since we had made calculations of diagonal
variances exogenously from a possibly larger set of data.

Doing analytics, we get sum of squared residuals (over the time interval that is relevant to us for calculation of
dynamic correlations) as

$ \sum \, {R_A}^2 \, = \sum {(\, X_A \, - \, \bar{X_A})}^2 \,$

$ \sum \, {R_A}^2 \, = \sum {(\, X_A \, - \, \big[ \mu_{A} \, + \,\frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N}) \big])}^2 \,$

All the values on rhs have either been observed or calculated earlier from data independently. So we minimize the sum of
residuals with respect to correlation parameter and apply the first order condition as

$ \frac{\partial [\sum \, {R_A}^2]}{\partial \rho_{N,A}} \, =\frac{\partial \big[ \sum {(\, X_A \, - \, \big[ \mu_{A} \, + \, \frac{\rho_{N,A} \, \,\sigma_{A}}{\sigma_{N}} \, (X_N \, - \mu_{N}) \big])}^2 \,\big]}{\partial \rho_{N,A}}=0$

Solution of the above FOC would give the dynamic correlation that maximizes the predicted value of Amazon stock over the
short stretch of data and minimizes the sum of squared residuals.

You can also apply above analytics to all mutual dynamic correlations in a basket of stocks by changing as in modelling
a multivariable regression(with vectors and matrices) as opposed to single variable regression.

I believe that minimization of squared residuals is underemphasized and can also be used intelligently in changepoint
detection and regime change detection. If you can cast your model in a two regime framework or changepoint framework and
apply minimization of sum of squared residuals, the hypothesis of regime change can easily be accepted if there is a
substantial decrease in sum of squared residuals due to regime change applied to the data.

---

### #1710 — Amin (Topic Author)
*February 18, 2023, 6:24 PM*

Friends, I did not have a very good day today. Mind control agents have sharply increased mind control activity very
recently. I had great difficulty thinking and concentrating and I lost threads of my thoughts again and again since mind
control agents kicked important neurotransmitters out of their pathways using EM resonance. It seemed that mind control
agents have a great urgency to somehow not let me continue my research. However I was still able to gain clarity about
my many things after repeated efforts. But mind control agents have increased their attempts to make it difficult for me
to do good research.

Here are my near future plans for research. I want to complete my programs for multivariable regressions in multiple
hermite polynomial setting. And I want to do it both by using average correlations (of different hermite polynomials)
and optimized correlations (of different hermite polynomials) by minimizing least squres in multivariable regression
setting.

I also want to share other interesting observations with friends. I ran a simulation over the attached data(in a recent
previous post) of Nasdaq tech stocks. The data stretches for little over a year and a month. I calculated skew and made
a strategy to shift money in stock with the max raw third moment (of daily log returns) among six stocks and Nasdaq
index. I made local calculations of third moment and you will have to play with number of days required for calculation
of local values of third raw moment of log returns that optimizes the strategy (though this sensitivity is not huge
which means that strategy is reasonably robust). I also took Nasdaq 100 as an asset in which you can shift money by
buying the index when Nasdaq 100 log returns would have more skew than any of the other six stocks in the sample. One
dollar of notional grew into  2.69 dollars of notional after 13.5 months of time with above strategy. Though all
calculations were in an idealized setting, I am sharing it for friends who find it interesting and want to explore it
further. The strategy probably worked well since I was picking the (locally) best stock among six very strong tech
stocks and Nasdaq 100 (considered as an asset in which you can park your money)

Another interesting thing for algorithmic trading would be to look at local autocorrelation (and local serial cross
correlations) of skew hermite polynomials and include that in the analysis.

---

### #1711 — Amin (Topic Author)
*February 20, 2023, 11:19 AM*

Friends, mind control agents are getting very impatient to retard me and stop me from my research. I went to a
restaurant around noon to eat food. I was not taking it extremely seriously and went to a random restaurant in Wapda
town which is a neighborhood close to where I live. As it turned out, army was tracking my movements and they had
already reached the restaurant. When I took first bite of food, I realized that it was drugged. I did not have anything
other than just one bite and I left the restaurant. Several hours later, I am still under hangover from that bite
despite that I had good food somewhere else and also drank a good red bull. I really remained unable to think properly
for several long hours despite that I had taken only one bite of bad drugged food.

I also noticed today that they had planted some device in my motorbike seat to charge my back. They had not done this
for several months and it was only today that I noticed it again. One reason might be that I went for a walk early in
the morning and was determined to continue my morning walk everyday and reduce my weight. Morning walk not only helps
keep me physically fit, it also helps to connect the brain in new ways and keeps it thinking intelligently reducing the
effect of mind control. It is my guess that mind control agents realized that I might get out of their whatever control
they have due to my walk and they needed to add other things to mind control and decided to plant devices in motorbike
seat so that they could continue to charge my back and make their mind control very effective.

I want to request friends to please protest to American government to ask pentagon generals to end my mind control and
let me live with my human dignity intact. Somebody has to teach humanity to crooks of pentagon that they first need to
respect human beings before getting promoted. These anal crooks of pentagon have no regard for any human ethics or good
reputation associated with American people and they are simply dying to enter the paradise of billionaire Goldfather and
have become instruments of Goldfather to retard anyone Goldfather wishes and these lowly crooks of pentagon are very
willing to destroy the great reputation associated with American nation so that they could enter the paradise of
billionaire goldfather.

---

### #1712 — Amin (Topic Author)
*February 21, 2023, 11:43 PM*

Friends, I have been able to greatly improve my previous regression program. I have mostly been able to get good shapes
for densities that have as few as only ten data observations and do all sorts of hermite regressions on these local
densities capturing non-linear effects. I have especially improved the program that converted the data to its standard
Z-values based on the parameters of the Z-series and now it is very rare to get a Z-value that has a residual with data
given the parameters of the Z-series. I have also written a program for multivariable, and multi-hermite regressions in
which you have to only input a matrix of explanatory variables and the vector of regressand and it will return the
coefficients of regressions for hermites associated with various variables right away. I hope to post the program later
today but it can still possibly be another day since I still have to check a few things. It is very interesting how
hermite polynomials capture the non-linear effects in the data. I look forward to posting the new improved programs in a
day.

---

### #1713 — Amin (Topic Author)
*February 22, 2023, 1:43 PM*

Friends, I am working on multivariate regression program. I regresses Apple stock returns for twenty days on Microsoft
stock returns and Nvidia stock returns. No financial significance but interesting to be able to do a good regression in
multiple hermite polynomial framework. R-Squared for this regression is 0.77 . Here is a quick 2D graph rotated to show
how the regression surface is passing through the scatterplot. There were only twenty data days in regression.

.

.[![Image](../images/i.postimg.cc/gJhfLdNX/Regress2-D01.jpg)](https://postimg.cc/njHd688p)

This is another view of the same graph.

.

.

[![Image](../images/i.postimg.cc/HWQqpYrF/Regress2-D01-A.jpg)](https://postimg.cc/Lh8CDMBV)

---

### #1714 — Amin (Topic Author)
*February 22, 2023, 6:20 PM*

Friends, though my program is complete, I still have to add comments and write equation numbers on code that could be
related to latex equations later explained on the forum. I also want to review the code if it can be revised to become
easier and more understandable. Therefore I will be posting my code later tomorrow and then also explain the logic with
latex equations. Sorry for this delay but we are already there and I hope friends would like my multivariate regressions
with multiple hermite polynomials code tomorrow.

---

### #1715 — Amin (Topic Author)
*February 23, 2023, 11:18 AM*

Friends, I have flu today and very difficult to work. My nose is running like anything so I am posting the program and
will give explanation later.

here are the matlab files for multivariate multiple hermite polynomial regression.

I have shown the user density of each variable involved in regression. Many times for smaller samples, these densities
are not stable and the first derivative of Z-series variable changes sign and density folds backwards on itself at the
ends instead of having deep tails. Usually this problem occurs when fourth moment calculated from small samples is
smaller than actual raw fourth moment (even though raw sample moments are unbiased predictors of true raw moments). In
my density calculation, I have increased fourth raw moment by a small value while keeping first three moments at their
sample values. This very heuristic correction in fourth raw moment is larger for very small samples and negligible for
larger samples. I will continue to work more systematically on proper density construction from small sample data after
posting this program. But this heuristic correction really helps to construct more stable densities with better
regression results. But this has to be more systematically studies.

Here is how I made change to fourth raw moments that is larger for small samples and negligible for larger samples.

```
rMu(4)=sum(DPrices(1:NDays0).^4)/NDays0*(NDays0)*(NDays0)/(NDays0-1)/(NDays0-1.5);
```

So the fourth raw moment is increased by   (NDays0)*(NDays0)/(NDays0-1)/(NDays0-1.5)

This is totally heuristic. I wanted to complete a working version of the program first and then later come back to
details that need to be fixed properly and rigorously.

All you have to do is to visualize the marginal density of each variable and if it is fine in the tails, your regression
would be good. Also because in new program, when densities are good enough in tail, you will not encounter any problems
finding standardized Z-values of each random variable.

There is a density visualization program but that will work only for two regressors. For more regressors, you will have
to alter the program for visualization purposes.

Here are the program files.

.

.

```
function [] = MultivariableMultiHermiteRegressionExample()

%Below, read AAPL, AMZN, GOOGL,MSFT,NVDA, NASDAQ100 daily open and
%close data files and extract daily open from the files. All files are
%exactly the same length and therefore corresponding array entries are
%from the same dates.
T = readtable('C:\Users\Hp\Documents\HistoricalPricesAAPL2022.csv');
[NDays,NVar]=size(T);
ApplPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesAMZN2022.csv');
AmznPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesGOOGL2022.csv');
GooglPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesMSFT2022.csv');
MsftPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesNVDA2022.csv');
NvdaPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesNASDAQ1002022.csv');
NasdaqPrices(1:NDays)=table2array(T(1:NDays,2));

StartI=01;%choose the start of the regression
EndI=46;%choose the last entry of the regression
NDays=EndI-StartI;

%Below calculate daily log-returns for regression.
DApplPrices(1:NDays)=log(ApplPrices(StartI+1:EndI))-log(ApplPrices(StartI:EndI-1));
DMsftPrices(1:NDays)=log(MsftPrices(StartI+1:EndI))-log(MsftPrices(StartI:EndI-1));
DNvdaPrices(1:NDays)=log(NvdaPrices(StartI+1:EndI))-log(NvdaPrices(StartI:EndI-1));
clf;
Y=DApplPrices(1:NDays); %Y is regressand
X(1,1:NDays)=DMsftPrices(1:NDays); %First row containing first explnatory variable
X(2,1:NDays)=DNvdaPrices(1:NDays); %Second row containing first explnatory variable
MM=2;   %Number of explanatory variables
TT=NDays;%Number of Data Entries in regression
HH=3; %Number of hermite polynomils used in regression
DoMultivariableMultiHermiteRegression(Y,X,MM,TT,HH) %Call the function that does regression.

end
```

.

.

.

```
function []= DoMultivariableMultiHermiteRegression(Y1,X1,MM,TT,HH)

W(1:MM,1:TT)=X1(1:MM,1:TT); %We add regressors to W
W(MM+1,1:TT)=Y1(1,1:TT);% We add regressand to W
%Above we added all explanatory and explained variables in a single matrix
%so that we could calculate correlations between respective Z-values of the
%W matrix.

for mm=1:MM+1  %total number of variables is number of regressors + 1(which is regressand)
    X(1:TT)=W(mm,1:TT); %Extract the time series of each variable in W
    rMu(mm,:) = CalculateFourRawMomentsFromDataA(X,TT);%Calculate four raw moments of each time series.
    [c0(mm),c(mm,:)] = CalculateZSeriesDensityFromRawMomentsM4(rMu(mm,:));%Calculate Z-series from each moment
    PlotZSeriesDensity(c0(mm),c(mm,:),'g');%Look at the density to make sure it is valid. If the tails fall
    %backwards in either direction, regression result can be flawed.
    Z(mm,1:TT)=CalculateZgivenXAndZSeriesC3(X,c0(mm),c(mm,:));%Calculate Z for each data entry in time series of every
variable(one by one through loop)
    [ch0(mm),ch(mm,:)]=ConvertZCoeffsToHCoeffs(c0(mm),c(mm,:),3);%Convert the Z-coeffs to H-coeffs

end

%below we calculate regression coefficients between standardized Z-values
%of regressors and regressand. We only use correlations and covariances do
%not enter this calculation.

NN=MM+1; %This is regressors + 1 which is explained variable.
%Z
%str=input('Look at Z');
%Z is a matrix containing standardized Z's of both regressors and
%regressand and we calculate all cross correlations in it.Three different
%correlation matrices are calculated each for 1st, second and third hermite
%as we are using three hermites in our analysis.
CorrH = CalculateCorrelationMatricesHermiteCH(Z,NN,TT,HH)
str=input('Look at CorrH');
for hh=1:HH %Loop over all hermite polynomials and calculate regression coefficients between
    %standardized Z-values of observation.
CorrHR(1:MM,1:MM)=CorrH(1:MM,1:MM,hh);%Correlation matrix containing regressors
CorrHr(1:MM)=CorrH(NN,1:MM,hh);%Correlation vector containing correlations between regressors and regressand
BetaHr(1:MM,hh)=CorrHr/CorrHR;%Do a inv(correlation matrix) right multiply to calculate regression coefficients between
standardized data
%This is repeated for each hermiote.
%BetaHr(mm,hh) is regression coefficient from mmth standardized explanatory
%variable in case of hhth hermite regression.
end

%If there are two explanatory variables they can also be visualized as
%below. The visualization function below will work only in case of two explanatory
%variables.
if(MM==2)
CalculateAndPlotRegressandVsTwoRegressors(MM,ch0,ch,BetaHr,X1,Y1,TT);
end

%Below we calculate predicted value of each data point and then calculate
%R-squared and TSS,ESS and RSS.
%The code block below assumes we are using three hermites in calculations
%and you will have to slightly alter it for different number of hermits.

TSS=0;
RSS=0;
ESS=0;
for tt=1:TT
    Yreg(tt)=ch0(NN);
    for mm=1:MM
        Yreg(tt)=Yreg(tt)+ch(NN,1).*BetaHr(mm,1)*Z(mm,tt)+ch(NN,2).*BetaHr(mm,2)*(Z(mm,tt).^2-1)+ ...
        ch(NN,3).*BetaHr(mm,3)*(Z(mm,tt).^3-3*Z(mm,tt));
    %Add a fourth hermite term if there are four hermites in regression.
    end
    TSS=TSS+(Y1(tt)-ch0(NN)).^2;  %Observed difference from mean.Squared.
    RSS=RSS+(Y1(tt)-Yreg(tt)).^2; %
    ESS=ESS+(Yreg(tt)-ch0(NN)).^2;
end

Rsquared=1-RSS/TSS;

TSS
RSS
ESS
Rsquared
str=input('Look at Regression numbers');

end

```

.

.

.

```
function [rMu] = CalculateFourRawMomentsFromDataA(DPrices,NDays0)

rMu(1)=sum(DPrices(1:NDays0))/NDays0;
rMu(2)=sum(DPrices(1:NDays0).^2)/(NDays0);
rMu(3)=sum(DPrices(1:NDays0).^3)/NDays0;%*(NDays0)/(NDays0-1);
rMu(4)=sum(DPrices(1:NDays0).^4)/NDays0*(NDays0)*(NDays0)/(NDays0-1)/(NDays0-1.5);
%rMu(4)=sum(DPrices(1:NDays0).^4)/NDays0*(NDays0)/(NDays0-1);

end

```

.

.

.

```
function [c0,c] = CalculateZSeriesDensityFromRawMomentsM4(rMu)

    mOrder=4;
    [Mu1,cMu] = ConvertRawMomentsToCentralMoments(rMu,mOrder);

    sMu(1)=0;
    sMu(2)=1;
    sMu(3)=cMu(3)/cMu(2).^1.5;
    sMu(4)=cMu(4)/cMu(2).^2.0;
    %sMu(5)=cMu(5)/cMu(2).^2.5;
    %sMu(6)=cMu(6)/cMu(2).^3.0;
    %sMu(7)=cMu(7)/cMu(2).^3.5;
    %sMu(8)=cMu(8)/cMu(2).^4.0;

    iter=20;
    bGuess(1:3)=0;
    bGuess(1)=1;
    [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNewC3(sMu,bGuess,iter);

    SeriesOrder=3;
    NMoments=4;

    [F,dF] = CalculateMomentsAndDerivatives_0(sMu,c0,c,SeriesOrder,SeriesOrder,NMoments);

da(1,1)=c0;
da(2:SeriesOrder+1,1)=c(1:SeriesOrder);

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

%Replace with your own more intelligent objective function if you like.
ObjBest=100000*(abs(sMu(1)-Moments(1)))+abs(sMu(2)-Moments(2))+abs((sMu(3)-Moments(3))^(1/1.5))+abs((sMu(4)-Moments(4))^(1/2.0));

b0Best=c0;
bBest(1:SeriesOrder)=c(1:SeriesOrder);

nn=0;
while((nn.000000000001) || (abs(F(2,1))>.000000000001) || (abs(F(3,1))>.000000000001) || (abs(F(4,1))>.00000000001)  ))

    nn=nn+1;
    %Below Newton matrix equation to improve the Z-series coefficients guess at previous step.
    da=da-dF\F;

    %b0=median
    b0=da(1,1);
    b(1:SeriesOrder)=da(2:SeriesOrder+1,1);

    %[F,dF] = CalculateCumulantsAndDerivativesFromMoments_0(C,b0,b,SeriesOrder,SeriesOrder,NoOfCumulants);
    [F,dF] = CalculateMomentsAndDerivatives_0(sMu,b0,b,SeriesOrder,SeriesOrder,NMoments);
    [IsValidFlag] =1;% CheckIsValidDensity(b0,b);
    [Moments] = CalculateMomentsOfZSeries(b0,b,SeriesOrder,NMoments);

   
ObjNew=100000*(abs(sMu(1)-Moments(1)))+abs(sMu(2)-Moments(2))+abs((sMu(3)-Moments(3))^(1/1.5))+abs((sMu(4)-Moments(4))^(1/2.0));

    if((ObjBest>ObjNew) &&( IsValidFlag))

       ObjBest=ObjNew;
       b0Best=b0;
       bBest(1:SeriesOrder)=b(1:SeriesOrder);
    end

    da(1,1)=b0;
    da(2:SeriesOrder+1,1)=b(1:SeriesOrder);

end
c0=b0Best;%Best;
c(1:SeriesOrder)=bBest;%Best(1:SeriesOrder);

    c0=c0*sqrt(cMu(2));
    c=c*sqrt(cMu(2));

    c0=c0+Mu1;

[FittedMoments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Please Uncomment this if you want to see a comparison of input moments and
%fitted moments
rMu
FittedMoments
str=input('Look at comparison of fitted moments with input moments');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%COMMENT lines below if you do not want to see the density of new Z-series random variable with
%fitted moments.
%First calculate normal random variable on a grid below
dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=45*4;  % No of normal density subdivisions
NnMid=((1+Nn)/2)*dNn;
Z(1:Nn)=(((1:Nn)*dNn)-NnMid);
%Z
%str=input('Look at Z');
%Now calculate Y as a function of normal random variable.
Y(1:Nn)=c0;
for nn=1:3
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

plot(Y(1:Nn),pY(1:Nn),'b');
title('Density of the Z-Series Variable with Fitted Moments');

%str=input('Look at the density of Z-series random variable')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end

```

.

.

.

```
function [mu1,cMu] = ConvertRawMomentsToCentralMoments(Mu,mOrder)

%cu
%mu
% %mOrder
%str=input('Look at numbers');
mu1=Mu(1);
for mm=2:mOrder
    cMu(mm)=0;
    for jj=0:mm
        if(jj==0)
            cMu(mm)=cMu(mm)+ (-1)^(mm-jj).*factorial(mm)/factorial(jj)/factorial(mm-jj)*1*mu1.^(mm-jj);
        else
            cMu(mm)=cMu(mm)+ (-1)^(mm-jj).*factorial(mm)/factorial(jj)/factorial(mm-jj)*Mu(jj)*mu1.^(mm-jj);
        end
    end
end

```

.

.

.

```
function [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNewC3(cmu,cin,iter)

%Mul=1.0;
SeriesOrder=3;
NMoments=4;

 EZ(1)=0;
 EZ(2)=1;
 for nn=3:NMoments*SeriesOrder+SeriesOrder+2
     if rem(nn,2)==1
         EZ(nn)=0;
     else
         EZ(nn)=EZ(nn-2)*(nn-1);
         EZ(nn);
     end
 end

c0=-(cin(2));  %This is for zero mean condition.
c=cin;
MaxIter=10;

for nn=1:iter     %increase the iterations over coefficients if neeeded

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[M3,dc2] = CalculateParticularMomentAndDerivativeOfItsCoeff(c0,c,SeriesOrder,3,EZ);

tolerance=.0000001*cmu(3);
mm=0;
while ((abs(M3-cmu(3)) >tolerance ) && (mmtolerance ) && (mm<MaxIter))
mm=mm+1;
c(3)=c(3)-(M4-cmu(4))/dc3;

[M4,dc3] = CalculateParticularMomentAndDerivativeOfItsCoeff(c0,c,SeriesOrder,4,EZ);

end

[SecondMoment] = CalculateSecondMomentC3(c0,c);

c=c/sqrt(SecondMoment);
c0=c0/sqrt(SecondMoment);

%[c0,c] = IterateSmoothingGuessOverPreviousMoments(cmu,c,4,2,EZ);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end

end

```

.

.

.

```
function [F,dF] = CalculateMomentsAndDerivatives_0(Ms,a0,a,SeriesOrder,NZterms,NMoments)
%[F,dF] = CalculateCumulantsAndDerivativesFromMoments(C,a0,a,SeriesOrder,SeriesOrder,NoOfCumulants);

%a(1)=a1;
%a(2)=a2;
%a(3)=a3;
%a(4)=a4;
%a(5)=a5;
%a(6)=a6;
%a(7)=a7;

%aa0=a0;
if(NMoments>8)
a0=-(a(2)+3*a(4)+15*a(6)+105*a(8));% ---1
end
if(NMoments==8)
a0=-(a(2)+3*a(4)+15*a(6));% ---1
end
if(NMoments==6)
a0=-(a(2)+3*a(4));% ---1
end

EZ(1)=0;
EZ(2)=1;
for nn=3:NMoments*SeriesOrder+NZterms+2
    if rem(nn,2)==1
        EZ(nn)=0;
    else
        EZ(nn)=EZ(nn-2)*(nn-1);
        EZ(nn);
    end
end
EZ;

EXZ(1,1)=1;
for pp1=1:NZterms
        EXZ(1,pp1+1)=EZ(pp1);
end

a(SeriesOrder+1:NMoments*SeriesOrder+1)=0;
b0=a0;
b=a;

for mm=1:NMoments
    if(mm>1)
        [b0,b] =SeriesProduct(a0,a,b0,b,SeriesOrder*mm);
        b(SeriesOrder*mm+1:NMoments*SeriesOrder+1)=0;
    end
   % b0
   % b
%str=input('Look at numbers')
    EXZ(mm+1,1)=b0;
    for pp2=1:SeriesOrder*mm

            EXZ(mm+1,1)=EXZ(mm+1,1)+b(pp2).*EZ(pp2);
    end
    for pp1=1:NZterms
        EXZ(mm+1,pp1+1)=b0.*EZ(pp1);
        for pp2=1:SeriesOrder*mm

            EXZ(mm+1,pp1+1)=EXZ(mm+1,pp1+1)+b(pp2).*EZ(pp2+pp1);
        end
    end
end

%u1=EXZ(2,1);
u2=EXZ(3,1);
u3=EXZ(4,1);
u4=EXZ(5,1);

u1=a0+a(2);
if(SeriesOrder>=4)
u1=a0+a(2)+3*a(4);
end
if(SeriesOrder>=6)
u1=u1+15*a(6);
end
if(SeriesOrder>=8)
u1=u1+105*a(8);
end

%k2=u2-u1^2;
%k3=u3-3*u2*u1+2*u1^3;
%k4=u4-4*u3*u1-3*u2^2+12*u2*u1^2-6*u1^4;

du1(1)=1;%----2
% du1(2)=0;%----2
% du1(3)=1;%----2
% du1(4)=0;%----2
% du1(5)=1;%----2
% du1(6)=0;%----2
% du1(7)=15;%----2
% du1(8)=0;%----2
% du1(9)=105;%----2
% du1(10)=0;%----2
 du2(1)=2*EXZ(2,1);
 du3(1)=3*EXZ(3,1);
 du4(1)=4*EXZ(4,1);

%du1(1)=1;%----2
%du2(1)=0;
%du3(1)=0;
%du4(1)=0;

for mm=2:SeriesOrder+1
du1(mm)=EXZ(1,mm);
du2(mm)=2*EXZ(2,mm);
du3(mm)=3*EXZ(3,mm);
du4(mm)=4*EXZ(4,mm);

end

if(NMoments>=5)
u5=EXZ(6,1);

%du5(1)=5*EXZ(5,1);

for mm=1:SeriesOrder+1
du5(mm)=5*EXZ(5,mm);
end

end

if(NMoments>=6)
u6=EXZ(7,1);
%du6(1)=0;

for mm=1:SeriesOrder+1
du6(mm)=6*EXZ(6,mm);
end

end

if(NMoments>=7)
u7=EXZ(8,1);
%str=input('Look at k7 and k71')

%du7(1)=0;

for mm=1:SeriesOrder+1
du7(mm)=7*EXZ(7,mm);
end

end
if(NMoments>=8)

u8=EXZ(9,1);
for mm=1:SeriesOrder+1
du8(mm)=8*EXZ(8,mm);
end

end

if(NMoments>=9)

u9=EXZ(10,1);
for mm=1:SeriesOrder+1
du9(mm)=9*EXZ(9,mm);
end

end
if(NMoments>=10)

u10=EXZ(11,1);
for mm=1:SeriesOrder+1
du10(mm)=10*EXZ(10,mm);
end

end

 F(1,1)=u1-Ms(1);
 F(2,1)=u2-Ms(2);
 F(3,1)=u3-Ms(3);
 F(4,1)=u4-Ms(4);
 if(NMoments>=5)
 F(5,1)=u5-Ms(5);
 end
 if(NMoments>=6)
 F(6,1)=u6-Ms(6);
 end
 if(NMoments>=7)
 F(7,1)=u7-Ms(7);
 end
 if(NMoments>=8)
 F(8,1)=u8-Ms(8);
 end
 if(NMoments>=9)
 F(9,1)=u9-Ms(9);
 end
 if(NMoments>=10)
 F(10,1)=u10-Ms(10);
 end

     for mm=1:SeriesOrder+1
        dF(1,mm)=du1(mm);
        dF(2,mm)=du2(mm);
        dF(3,mm)=du3(mm);
        dF(4,mm)=du4(mm);
        if(NMoments>=5)
        dF(5,mm)=du5(mm);
        end
        if(NMoments>=6)
        dF(6,mm)=du6(mm);
        end
        if(NMoments>=7)
        dF(7,mm)=du7(mm);
        end
        if(NMoments>=8)
        dF(8,mm)=du8(mm);
        end
        if(NMoments>=9)
        dF(9,mm)=du9(mm);
        end
        if(NMoments>=10)
        dF(10,mm)=du10(mm);
        end
     end

end

```

.

.

.

```
function [Moments] = CalculateMomentsOfZSeries(a0,a,SeriesOrder,NMoments)

%aa0=a0;
%a0=0;% ---1

EZ(1)=0;
EZ(2)=1;
%LogEZ(2)=0;
for nn=3:NMoments*SeriesOrder
    if rem(nn,2)==1
        EZ(nn)=0;
    else
        EZ(nn)=EZ(nn-2)*(nn-1);
        %LogEZ(nn)=log(EZ(nn-2))+log(nn-1);
        %EZ(nn);
    end
end
%EZ
%EZ(1:30)
%str=input('Look at numbers')
a(SeriesOrder+1:SeriesOrder*NMoments+1)=0;
b0=a0;
b=a;

for mm=1:NMoments
    if(mm>1)
        %[b0,b] =SeriesProductLogarithmic(a0,a,b0,b,SeriesOrder*mm);

        [b0,b] =SeriesProduct(a0,a,b0,b,SeriesOrder*mm);

        %b0-bb0

        %b-bb

        %str=input('Look at two products')

        b(SeriesOrder*mm+1:SeriesOrder*NMoments+1)=0;
    end
   % Logb=log(abs(b));
   % Signb=sign(b);
    EXZ(mm,1)=b0;
    for pp2=1:SeriesOrder*mm
        if rem(pp2,2)==0
            %EXZ(mm,1)=EXZ(mm,1)+exp(Logb(pp2)+LogEZ(pp2)).*Signb(pp2);
            EXZ(mm,1)=EXZ(mm,1)+b(pp2).*EZ(pp2);
 %           b(pp2).*EZ(pp2)
 %           exp(Logb(pp2)+LogEZ(pp2)).*Signb(pp2)
 %           mm
 %           pp2
            %str=input('Look at moment values')
        end
    end
end

for nn=1:NMoments
    Moments(nn)=EXZ(nn,1);
end

end

```

.

.

.

```
function [EnMoment,dEnMomentdCoeff] = CalculateParticularMomentAndDerivativeOfItsCoeff(a0,a,SeriesOrder,nMoment,EZ)

% if(SeriesOrder>=8)
% a0=-(a(2)+3*a(4)+15*a(6)+105*a(8));% ---1
% end
% if(SeriesOrder<8)
% a0=-(a(2)+3*a(4)+15*a(6));% ---1
% end
%
% EZ(1)=0;
% EZ(2)=1;
% for nn=3:NMoments*SeriesOrder+NZterms+2
%     if rem(nn,2)==1
%         EZ(nn)=0;
%     else
%         EZ(nn)=EZ(nn-2)*(nn-1);
%         EZ(nn);
%     end
% end
% EZ;

%EXZ(1,1)=1;
%for pp1=1:NZterms
%        EXZ(1,pp1+1)=EZ(pp1);
%end

a(SeriesOrder+1:nMoment*SeriesOrder+1+SeriesOrder)=0;
b0=a0;
b=a;

for mm=2:nMoment

    [b0,b] =SeriesProduct(a0,a,b0,b,SeriesOrder*mm+SeriesOrder+1);
     b(SeriesOrder*mm+1:nMoment*SeriesOrder+SeriesOrder+1)=0;
     if(mm==nMoment-1)
         dEnMomentdCoeff=b0.*EZ(nMoment-1);
         for pp2=1:SeriesOrder*nMoment-1

            dEnMomentdCoeff=dEnMomentdCoeff+b(pp2).*EZ(pp2+nMoment-1);
        end
        dEnMomentdCoeff=dEnMomentdCoeff*nMoment;
     end
     if(mm==nMoment)
        EnMoment=b0;
        for pp2=1:SeriesOrder*nMoment
            EnMoment=EnMoment+b(pp2).*EZ(pp2);

        end
     end
end

end

```

.

.

.

```
function [SecondMoment] = CalculateSecondMomentC3(a0,a)

SecondMoment=a0^2+a(1)^2 +2* a0* a(2) +3*(a(2).^2+2* a(1).* a(3))+ ...
    15*(a(3).^2) ;

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

plot(Y(1:Nn),pY(1:Nn),Color);
title('Density of the Z-Series Variable with Fitted Moments');
str=input('Look at density');

end

```

.

.

.

```
function [Z] = CalculateZgivenXAndZSeriesC3(X,c0,c)

Z=(X-c0)/c(1)-(c(2) * (X-c0).^2)/c(1).^3+(((2* c(2).^2)./c(1).^2-c(3)./c(1)).* (X-c0).^3)./c(1).^3;
mm=0;
while((max(abs(X-(c0+c(1)*Z+c(2)*Z.^2+c(3)*Z.^3)))>.00000001) && (mm=100)
    pp=0;
    for nn=1:length(X)
        if( abs(X(nn)-(c0+c(1)*Z+c(2)*Z.^2+c(3)*Z.^3))>.00000001 )
            pp=pp+1;
            Y(pp)=X(nn);
            Index(pp)=nn;
        end
    end
    for ppp=1:pp
        ZZ(ppp)=CalculateZgivenXAndZSeriesBisectionC3(Y(ppp),c0,c);
        Z(Index(ppp))=ZZ(ppp);
    end
end

end

```

.

.

.

```
function [Z]=CalculateZgivenXAndZSeriesBisectionC3(Y,c0,c)

if(Y>c0)
    if(Y c0+c(1)*Zmid+c(2)*Zmid^2 +c(3) * Zmid^3)
            Za=Zmid;
        end
    Z=.5*Za+.5*Zb;
    Za
    Zb
    Z
    end

end

if(Y c0+c(1)*-.5+c(2)*(-.5)^2 +c(3) * (-.5)^3)
        Za=-.5;
        Zb=0;
    elseif(Y> c0+c(1)*(-1)+c(2)*(-1)^2 +c(3) * (-1)^3)
        Za=-1;
        Zb=-.5;
    elseif(Y> c0+c(1)*(-1.5)+c(2)*(-1.5)^2 +c(3) * (-1.5)^3)
        Za=-1.5;
        Zb=-1;
    elseif(Y> c0+c(1)*(-2)+c(2)*(-2)^2 +c(3) * (-2)^3)
        Za=-2;
        Zb=-1.5;
    elseif(Y> c0+c(1)*(-2.5)+c(2)*(-2.5)^2 +c(3) * (-2.5)^3)
        Za=-2.5;
        Zb=-2.0;
    elseif(Y> c0+c(1)*(-3)+c(2)*(-3)^2 +c(3) * (-3)^3)
        Za=-3;
        Zb=-2.5;
    elseif(Y> c0+c(1)*(-3.5)+c(2)*(-3.5)^2 +c(3) * (-3.5)^3)
        Za=-3.5;
        Zb=-3.0;
    elseif(Y> c0+c(1)*(-4)+c(2)*(-4)^2 +c(3) * (-4)^3)
        Za=-4;
        Zb=-3.5;
    elseif(Y> c0+c(1)*(-4.5)+c(2)*(-4.5)^2 +c(3) * (-4.5)^3)
        Za=-4.5;
        Zb=-4.0;
    else
        Za=-5.5;
        Zb=-4.5;
    end
    for mm=1:100
        Zmid=.5*Za+.5*Zb;
        if(Y c0+c(1)*Zmid+c(2)*Zmid^2 +c(3) * Zmid^3)
            Za=Zmid;
        end
    Z=.5*Za+.5*Zb;
    Za
    Zb
    Z
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
function [CorrH] = CalculateCorrelationMatricesHermiteCH(Z,NN,TT,HH)

CorrH(1:NN,1:NN,1:HH)=0;
for mm=1:NN
    for nn=1:NN
        for tt=1:TT
            for hh=1:HH
                if(hh==1)
                    CorrH(mm,nn,hh)=CorrH(mm,nn,hh)+Z(mm,tt).*Z(nn,tt);
                end
                if(hh==2)
                    CorrH(mm,nn,hh)=CorrH(mm,nn,hh)+(Z(mm,tt).^2-1).*(Z(nn,tt).^2-1);
                end
                if(hh==3)
                    CorrH(mm,nn,hh)=CorrH(mm,nn,hh)+(Z(mm,tt).^3-3*Z(mm,tt)).*(Z(nn,tt).^3-3*Z(nn,tt));
                end
            end
        end

    end
end

for mm=1:NN
    for nn=1:NN
        if(mm~=nn)
        CorrH(mm,nn,1:3)=CorrH(mm,nn,1:3)./sqrt(CorrH(mm,mm,1:3))./sqrt(CorrH(nn,nn,1:3));
        end
    end
end
for mm=1:NN
    CorrH(mm,mm,1:3)=1;
end

end

```

.

.

.

```
function [] = CalculateAndPlotRegressandVsTwoRegressors(MM,ch0,ch,BetaHr,X1,Y1,TT)
%MM is number of independent Regressors. Here they are two.
%NN=MM+1; NNth variable is regressand.
%ch0(1:NN).  ch0(1:MM) are for each explanatory variable and ch0(NN) is for
%regressand.
%ch(1:NN,1:HH). index 1:NN is for different variables, index 1:HH is for
%different hermite polynomials. here they are three.

NN=MM+1;
 dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
 Nn=45*4;  % No of normal density subdivisions
 NnMid=((1+Nn)/2)*dNn;
 for mm=1:MM
    ZZ(mm,1:Nn)=(((1:Nn)*dNn)-NnMid); %The first index of ZZ is for every explanatory variable with which ZZ is
associated.
 end

%Below we take a square grid for two explanatory variables. Both grids are built on underlying
%independent Z's. Xs1(1:Nn,1:Nn) is value of first explanatory variable on
%square Z-grid. Xs2(1:Nn,1:Nn) is value of second explanatory variable on
%square grid. Ys2(1:Nn,1:Nn) is value of regressand variable on
%square grid (it has asset index equal to NN)
%Below explanatory variables are constructed as one-dimesional variables on
%their respective but different Z.
%Regressand is constructed as s function of both Z's of regressors on
%squared grid. Here BetaHr is used for effective correlation calculated after controlling for each of other
correlations.
Xs1(1:Nn,1:Nn)=ch0(1);
Xs2(1:Nn,1:Nn)=ch0(2);
Ys(1:Nn,1:Nn)=ch0(NN);
for nn=1:Nn
    for mm=1:Nn
        Xs1(mm,nn)=Xs1(mm,nn)+ch(1,1).*ZZ(1,nn)+ch(1,2).*(ZZ(1,nn).^2-1)+ch(1,3).*(ZZ(1,nn).^3-3*ZZ(1,nn));
        Xs2(mm,nn)=Xs2(mm,nn)+ch(2,1).*ZZ(2,mm)+ch(2,2).*(ZZ(2,mm).^2-1)+ch(2,3).*(ZZ(2,mm).^3-3*ZZ(2,mm));
        Ys(mm,nn)=Ys(mm,nn)+ch(NN,1).*BetaHr(1,1)*ZZ(1,nn)+ch(NN,2).*BetaHr(1,2)*(ZZ(1,nn).^2-1)+ ...
         ch(NN,3).*BetaHr(1,3)*(ZZ(1,nn).^3-3*ZZ(1,nn))+ ...
         ch(NN,1).*BetaHr(2,1)*ZZ(2,mm)+ch(NN,2).*BetaHr(2,2)*(ZZ(2,mm).^2-1)+ ...
         ch(NN,3).*BetaHr(2,3)*(ZZ(2,mm).^3-3*ZZ(2,mm));
    end
end

clf;
hold on
plot3(X1(1,1:TT),X1(2,1:TT),Y1(1:TT),'bo','linewidth',4);
surf(Xs1,Xs2,Ys)
str=input('Look at 2-D Graph');
clf;

end

```

.

.

.

Here is the regression plot you will see. 1st unrotated and second rotated. This is graph of first 45 daily returns of
APPL VS daily returns of MSFT and NVDA

[![Image](../images/i.postimg.cc/mk16hFGW/Regress2-D02-A.jpg)](https://postimg.cc/H8Hthnx6)

[![Image](../images/i.postimg.cc/63mm9fgh/Regress2-D02-B.jpg)](https://postimg.cc/njqk2BHs)

Here are the regression analytics you will see.

First hermite correlations

CorrH(:,:,1) =

   1.000000000000000   0.706373941869382   0.742423519593246

   0.706373941869382   1.000000000000000   0.781142661662286

   0.742423519593246   0.781142661662286   1.000000000000000

Second hermite correlations

CorrH(:,:,2) =

   1.000000000000000   0.399838064591523   0.572052566256445

   0.399838064591523   1.000000000000000   0.622166373120039

   0.572052566256445   0.622166373120039   1.000000000000000

Third hermite correlations.

CorrH(:,:,3) =

   1.000000000000000   0.338623911017974   0.481219060244469

   0.338623911017974   1.000000000000000   0.542437187825566

   0.481219060244469   0.542437187825566   1.000000000000000

Look at CorrH

Look at 2-D Graph

TSS =

   0.017116089682868

RSS =

   0.005497822501914

ESS =

   0.011777652804542

Rsquared =

   0.678792142143499

Look at Regression numbers

---

### #1716 — Amin (Topic Author)
*February 24, 2023, 3:20 AM*

Friends, I still have flu and light fever and hope to restart the work as soon as I get better.

I wanted to make more changes to the program but I knew that I would not be able to work further due to flu and decided
to post the program.

For example densities constructed probably have to be based on sample variance, sample skew and sample kurtosis. I had
been working with raw moments directly earlier. And I thought it was like an anomaly that sample central moments are
biased and have to be adjusted while sample raw moments are unbiased. In next version of my program, I will make
densities based on sample central moments after making required adjustments. There are further changes to graphing and
some other parts of the program that I want to make. It is not a lot of work so new program should be ready one or two
days after I get better.

I will try to find interesting applications of the hermite regressions. And then get back to resume the work on option
pricing where I left to start working on regression models. I hope I will continue interesting work that would be
helpful in research of many friends.

---

### #1717 — Amin (Topic Author)
*February 24, 2023, 7:33 PM*

Friends, I was playing around with the new regression program and I noticed that using sample central moments without
regard to raw moments deteriorates the fit while only increasing the fourth raw moment has a much better fit to data and
much larger R^2. I might be doing something wrong and will double check everything again but it seems that using only
central sample moments does not seem to work as well.

If all the densities involved are nice with good tails, the results are excellent but if some density had bad tails, it
can deteriorate the results. Here is a very beautiful graph that I found when I was playing around.

StartI=01+5*46;%choose the start of the regression

EndI=46+5*46;%choose the last entry of the regression

The R^2 was .82, but I had slightly increased fourth raw moment further.

Here is the same graph with different angles.

.

.

[![Image](../images/i.postimg.cc/DzPHSy2p/Regress2-D03-A.jpg)](https://postimg.cc/hJhpwnQV)

[![Image](../images/i.postimg.cc/cHDzc9tQ/Regress2-D03-B.jpg)](https://postimg.cc/vgVXYvzB)

[![Image](../images/i.postimg.cc/gJc58Fjz/Regress2-D03-C.jpg)](https://postimg.cc/DWDB3N1H)

---

### #1718 — Amin (Topic Author)
*February 25, 2023, 3:18 AM*

It seems that problem is not whether we have sample moments and not population moments. The problem is that in many
samples kutosis is too small for the density to have a positive first derivative (of X wrt Z as in Z-series) everywhere
and it folds onto itself and larger Z's after a certain value of Z start to map on smaller values of the variable. This
destroys the regression. It only requires that kurtosis is increased while keeping other moments constant. I will play
and try to come with a new version of the program that increases kurtosis of the density until first derivative of the
Z-series random variable with respect to Z is positive everywhere. In 90% of the densities, it will be a very small
increase in value of kurtosis. I am sure it will fix all the problems.

In the meanwhile, please enjoy these two different graphs.

The first graph has R^2 .717 and second graph has R^2 .96

.

.

[![Image](../images/i.postimg.cc/qqCngq89/Regress2-D04-A.jpg)](https://postimg.cc/T5fh4RN9)

[![Image](../images/i.postimg.cc/xCZM0Mbv/Regress2-D05-A.jpg)](https://postimg.cc/dk8L6763)

---

### #1719 — Amin (Topic Author)
*February 25, 2023, 9:25 AM*

**(broken latex: Unbalanced $: 7)**

```latex
Friends, while finding marginal densities for our hermite regression framework, we have tried to fit four moments. That
means that valid equation for Z-series random variable underlying density would be

$X\, = \, a_0 \, + \, a_1 \, Z \, +\, a_2 \, Z^2 \, +\, a_3 \, Z^3 \,$

The first derivative of X with respect to Z is given as

$\frac{dX}{dZ}\, =  \, a_1  \, +\, 2\, a_2 \, Z \, +\, 3\, a_3 \, Z^2 \,$

In order to have a nicely behaved density, we need$\frac{dX}{dZ}\,>0 \,$ everywhere. So as Z increases, X also
increases. If somewhere $\frac{dX}{dZ}\,
```

---

### #1720 — Amin (Topic Author)
*February 25, 2023, 9:38 PM*

Friends, I want to mention that an antipsychotic injection is due on coming Monday so I may not be able to work very
well after a few days. I have requested psychiatrist's office to arrange a phone meeting which should possibly follow in
next few days. I really want to ask the doctor to end my injections and antipsychotic medication as I am perfectly
mentally healthy. Many psychiatrists in Pakistan force antipsychotics on healthy people and also detain them for long
periods of time under pressure and coercion from Pakistan army (whose generals receive tens of millions of dollars in
bribes from US army to facilitate mind control of intelligent people in Pakistan).

I also want to request European embassies in Pakistan to keep a vigil and record my phone call with the psychiatrist so
they would know the tactics of CIA, Pakistan army and psychiatrists to gain an understanding of mind control abuse since
a lot of very talented Europeans suffer from a very similar abuse on hands of corrupt generals in American army(whose
many generals are desperate to do anything to please their billionaire Goldfather and would gladly and obediently retard
muslims, blacks, Europeans or even Americans who are talented  when Goldfather wishes them to do so).

I also want to request American and Pakistani friends if they can possibly approach my psychiatrist  (Far*** A. Minhas
of treehouse, Peshawar road, Rawalpindi) to tell him about horrors of mind control abuse and stop following the orders
of Pakistan military. Many times these psychiatrists are not bad people but they are told concocted lies and false
ethical justification about mind control by generals who would have already taken large sums of bribes. I am sure many
of these psychiatrists would be very careful about mistreating  their patients once they know the truth. But I cannot
take this risk on my own since there is a huge possibility that doctor might even increase my medication several fold if
I say this is all a conspiracy. It is unbelievably moronic but I have read it myself in psychiatry books that whoever
claims that secret services are after me is schizophrenic.

---

### #1721 — Amin (Topic Author)
*February 26, 2023, 1:57 PM*

Friends, I wrote a small function that increases fourth moment in calibration until our positivity of first derivative
dX/dZ condition is satisfied. Now regression seems to give very good results. I quickly went ahead and divided the data
I had into 27 blocks of ten days each. As daily returns were calculated, there were only nine entries in each regression
for each block of ten days. I plotted the 2-D graphs and tried to get the best view after rotating each graph. Here are
27 graphs which have APPL returns VS MSFT and NVDA returns for ten days each(nine returns each).

I will post this new program in a few hours that I used to generate these graphs.

b11 and b21 are standardized regression coefficients for MSFT and NVDA for explaining first hermite deviations in APPL

b12 and b22 are standardized regression coefficients for MSFT and NVDA for explaining second hermite deviations in APPL

b13 and b23 are standardized regression coefficients for MSFT and NVDA for explaining third hermite deviations in APPL

vh1, vh2, and vh3 are volatility coefficients of APPL for first, second and third hermite respectively.

These coefficients are given on title of the graphs.

Here are the graphs.

.

.

[![Image](../images/i.postimg.cc/SsSjtVRD/APPL2D01.jpg)](https://postimg.cc/8FY17Rh6)

[![Image](../images/i.postimg.cc/8CV7LTS8/APPL2D02.jpg)](https://postimg.cc/68Y6XJqz)

[![Image](../images/i.postimg.cc/BvcXgRSj/APPL2D03.jpg)](https://postimg.cc/kVGJM1tC)

[![Image](../images/i.postimg.cc/VLprLjZk/APPL2D04.jpg)](https://postimg.cc/0bG2VJqT)

[![Image](../images/i.postimg.cc/m2t1sdwn/APPL2D05.jpg)](https://postimg.cc/ykC8hy2h)

[![Image](../images/i.postimg.cc/fRd33J1j/APPL2D06.jpg)](https://postimg.cc/PCtf9rXP)

[![Image](../images/i.postimg.cc/nrLjMTtC/APPL2D07.jpg)](https://postimg.cc/62D5mrqX)

[![Image](../images/i.postimg.cc/Vs702yjM/APPL2D08.jpg)](https://postimg.cc/fk9b0rqT)

[![Image](../images/i.postimg.cc/hjsQS66k/APPL2D09.jpg)](https://postimg.cc/jwWScgsc)

[![Image](../images/i.postimg.cc/gJm6bmSy/APPL2D10.jpg)](https://postimg.cc/sBH2pdR1)

[![Image](../images/i.postimg.cc/MHrcBRWt/APPL2D11.jpg)](https://postimg.cc/rRxFXDRt)

[![Image](../images/i.postimg.cc/FKtLGj0B/APPL2D12.jpg)](https://postimg.cc/5X3y2Q7B)

[![Image](../images/i.postimg.cc/MKFRfkHx/APPL2D13.jpg)](https://postimg.cc/JGjtS2jd)

[![Image](../images/i.postimg.cc/SKWzPJrN/APPL2D14.jpg)](https://postimg.cc/67p326gD)

[![Image](../images/i.postimg.cc/6p4ZdH4Z/APPL2D15.jpg)](https://postimg.cc/w1H3zQVx)

[![Image](../images/i.postimg.cc/NGbRY2wK/APPL2D16.jpg)](https://postimg.cc/JtDs5n08)

[![Image](../images/i.postimg.cc/zXBKfDJ0/APPL2D17.jpg)](https://postimg.cc/5jh67VQC)

[![Image](../images/i.postimg.cc/3NLGZVZX/APPL2D18.jpg)](https://postimg.cc/dZyDsWp3)

[![Image](../images/i.postimg.cc/yx69cs06/APPL2D19.jpg)](https://postimg.cc/ZBgChkfX)

[![Image](../images/i.postimg.cc/j54PDLwk/APPL2D20.jpg)](https://postimg.cc/Q9VHPNqp)

[![Image](../images/i.postimg.cc/cHSf1QHn/APPL2D21.jpg)](https://postimg.cc/67M8Y4CW)

[![Image](../images/i.postimg.cc/bvbQj6zP/APPL2D22.jpg)](https://postimg.cc/PLXLWQpV)

[![Image](../images/i.postimg.cc/y82FtqCn/APPL2D23.jpg)](https://postimg.cc/xXyJN4Cb)

[![Image](../images/i.postimg.cc/htXL2D6f/APPL2D24.jpg)](https://postimg.cc/HrC8xgpg)

[![Image](../images/i.postimg.cc/v8vtBS5H/APPL2D25.jpg)](https://postimg.cc/s1vhHmnt)

[![Image](../images/i.postimg.cc/288FBFxd/APPL2D26.jpg)](https://postimg.cc/Rqynktyq)

[![Image](../images/i.postimg.cc/YqnNNGX5/APPL2D27.jpg)](https://postimg.cc/w7NsgvY2)

---

### #1722 — Amin (Topic Author)
*February 26, 2023, 4:17 PM*

Here are the updated files that are needed to make new changes to the program. Rest of the files are the same. I will
post a new updated version in a few days but quickly posting the new program so that fourth raw moment is fixed at first
derivative dX/dZ positivity condition as described in a previous post.

.

.

```
function []= DoMultivariableMultiHermiteRegression(Y1,X1,MM,TT,HH)

W(1:MM,1:TT)=X1(1:MM,1:TT); %We add regressors to W
W(MM+1,1:TT)=Y1(1,1:TT);% We add regressand to W
%Above we added all explanatory and explained variables in a single matrix
%so that we could calculate correlations between respective Z-values of the
%W matrix.

for mm=1:MM+1  %total number of variables is number of regressors + 1(which is regressand)
    X(1:TT)=W(mm,1:TT); %Extract the time series of each variable in W
    rMu(mm,:) = CalculateFourRawMomentsFromData(X,TT);%Calculate four raw moments of each time series.
    %[c0(mm),c(mm,:)] = CalculateZSeriesDensityFromRawMomentsM4(rMu(mm,:));%Calculate Z-series from each moment

    [c0(mm),c(mm,:)] = CalculateZSeriesDensityFromRawMomentsFix4thMoment(rMu(mm,:));
    %[cMu(mm,:),Mu1(mm)] = CalculateFourCentralMomentsFromDataA(X,TT);%Calculate four raw moments of each time series.
    %[c0(mm),c(mm,:)] = CalculateZSeriesDensityFromCentralMomentsM4(cMu(mm,:),Mu1(mm));%Calculate Z-series from each
moment

    PlotZSeriesDensity(c0(mm),c(mm,:),'g');%Look at the density to make sure it is valid. If the tails fall
    %backwards in either direction, regression result can be flawed.
    Z(mm,1:TT)=CalculateZgivenXAndZSeriesC3(X,c0(mm),c(mm,:));%Calculate Z for each data entry in time series of every
variable(one by one through loop)
    [ch0(mm),ch(mm,:)]=ConvertZCoeffsToHCoeffs(c0(mm),c(mm,:),3);%Convert the Z-coeffs to H-coeffs

end

%below we calculate regression coefficients between standardized Z-values
%of regressors and regressand. We only use correlations and covariances do
%not enter this calculation.

NN=MM+1; %This is regressors + 1 which is explained variable.
%Z
%str=input('Look at Z');
%Z is a matrix containing standardized Z's of both regressors and
%regressand and we calculate all cross correlations in it.Three different
%correlation matrices are calculated each for 1st, second and third hermite
%as we are using three hermites in our analysis.
CorrH = CalculateCorrelationMatricesHermiteCH(Z,NN,TT,HH)
str=input('Look at CorrH');
for hh=1:HH %Loop over all hermite polynomials and calculate regression coefficients between
    %standardized Z-values of observation.
CorrHR(1:MM,1:MM)=CorrH(1:MM,1:MM,hh);%Correlation matrix containing regressors
CorrHr(1:MM)=CorrH(NN,1:MM,hh);%Correlation vector containing correlations between regressors and regressand
BetaHr(1:MM,hh)=CorrHr/CorrHR;%Do a inv(correlation matrix) right multiply to calculate regression coefficients between
standardized data
%This is repeated for each hermiote.
%BetaHr(mm,hh) is regression coefficient from mmth standardized explanatory
%variable in case of hhth hermite regression.
end

%If there are two explanatory variables they can also be visualized as
%below. The visualization function below will work only in case of two explanatory
%variables.
if(MM==2)
CalculateAndPlotRegressandVsTwoRegressors(MM,ch0,ch,BetaHr,X1,Y1,TT);
end

%Below we calculate predicted value of each data point and then calculate
%R-squared and TSS,ESS and RSS.
%The code block below assumes we are using three hermites in calculations
%and you will have to slightly alter it for different number of hermits.

TSS=0;
RSS=0;
ESS=0;
for tt=1:TT
    Yreg(tt)=ch0(NN);
    for mm=1:MM
        Yreg(tt)=Yreg(tt)+ch(NN,1).*BetaHr(mm,1)*Z(mm,tt)+ch(NN,2).*BetaHr(mm,2)*(Z(mm,tt).^2-1)+ ...
        ch(NN,3).*BetaHr(mm,3)*(Z(mm,tt).^3-3*Z(mm,tt));
    %Add a fourth hermite term if there are four hermites in regression.
    end
    TSS=TSS+(Y1(tt)-ch0(NN)).^2;  %Observed difference from mean.Squared.
    RSS=RSS+(Y1(tt)-Yreg(tt)).^2; %
    ESS=ESS+(Yreg(tt)-ch0(NN)).^2;
end

Rsquared=1-RSS/TSS;

TSS
RSS
ESS
Rsquared
str=input('Look at Regression numbers');

end

```

.

.

.

```
function [c0,c] = CalculateZSeriesDensityFromRawMomentsFix4thMoment(rMu)

pMu=rMu;

[c0,c] = CalculateZSeriesDensityFromRawMomentsM4(rMu);

while((c(2)^2-3*c(1)*c(3))>=0)
    rMu(4)=rMu(4)*1.01;%increase the 4th raw moment by one percent everytime
    [c0,c] = CalculateZSeriesDensityFromRawMomentsM4(rMu);
end

pMu
rMu
str=input('Look at pMu--input moments and rMu-calibrated moments')

end

```

.

.

.

```
function [rMu] = CalculateFourRawMomentsFromData(DPrices,NDays0)

rMu(1)=sum(DPrices(1:NDays0))/NDays0;
rMu(2)=sum(DPrices(1:NDays0).^2)/(NDays0);%-1);
rMu(3)=sum(DPrices(1:NDays0).^3)/NDays0%/(NDays0-1)/(NDays0-2);
rMu(4)=sum(DPrices(1:NDays0).^4)/NDays0%*(NDays0-1)/(NDays0-1)/(NDays0-2)/(NDays0-3);
%rMu(5)=sum(DPrices(1:NDays0).^5)/NDays0;

end

```

.

Here almost nothing has changed but reposting.

.

.

```
function [] = MultivariableMultiHermiteRegressionExample()

%Below, read AAPL, AMZN, GOOGL,MSFT,NVDA, NASDAQ100 daily open and
%close data files and extract daily open from the files. All files are
%exactly the same length and therefore corresponding array entries are
%from the same dates.
T = readtable('C:\Users\Hp\Documents\HistoricalPricesAAPL2022.csv');
[NDays,NVar]=size(T);
ApplPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesAMZN2022.csv');
AmznPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesGOOGL2022.csv');
GooglPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesMSFT2022.csv');
MsftPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesNVDA2022.csv');
NvdaPrices(1:NDays)=table2array(T(1:NDays,2));
T = readtable('C:\Users\Hp\Documents\HistoricalPricesNASDAQ1002022.csv');
NasdaqPrices(1:NDays)=table2array(T(1:NDays,2));

%choose the last entry of the regression
StartI=01+0*10;%choose the start of the regression
EndI=10+0*10;%choose the last entry of the regression
NDays=EndI-StartI;

%Below calculate daily log-returns for regression.
DApplPrices(1:NDays)=log(ApplPrices(StartI+1:EndI))-log(ApplPrices(StartI:EndI-1));
DMsftPrices(1:NDays)=log(MsftPrices(StartI+1:EndI))-log(MsftPrices(StartI:EndI-1));
DNvdaPrices(1:NDays)=log(NvdaPrices(StartI+1:EndI))-log(NvdaPrices(StartI:EndI-1));
clf;
Y=DApplPrices(1:NDays); %Y is regressand
X(1,1:NDays)=DMsftPrices(1:NDays); %First row containing first explnatory variable
X(2,1:NDays)=DNvdaPrices(1:NDays); %Second row containing first explnatory variable
MM=2;   %Number of explanatory variables
TT=NDays;%Number of Data Entries in regression
HH=3; %Number of hermite polynomils used in regression
DoMultivariableMultiHermiteRegression(Y,X,MM,TT,HH) %Call the function that does regression.

end
```

.

.

Only title is added on graph in this function

.

```
function [] = CalculateAndPlotRegressandVsTwoRegressors(MM,ch0,ch,BetaHr,X1,Y1,TT)
%MM is number of independent Regressors. Here they are two.
%NN=MM+1; NNth variable is regressand.
%ch0(1:NN).  ch0(1:MM) are for each explanatory variable and ch0(NN) is for
%regressand.
%ch(1:NN,1:HH). index 1:NN is for different variables, index 1:HH is for
%different hermite polynomials. here they are three.

NN=MM+1;
 dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
 Nn=45*4;  % No of normal density subdivisions
 NnMid=((1+Nn)/2)*dNn;
 for mm=1:MM
    ZZ(mm,1:Nn)=(((1:Nn)*dNn)-NnMid); %The first index of ZZ is for every explanatory variable with which ZZ is
associated.
 end

%Below we take a square grid for two explanatory variables. Both grids are built on underlying
%independent Z's. Xs1(1:Nn,1:Nn) is value of first explanatory variable on
%square Z-grid. Xs2(1:Nn,1:Nn) is value of second explanatory variable on
%square grid. Ys2(1:Nn,1:Nn) is value of regressand variable on
%square grid (it has asset index equal to NN)
%Below explanatory variables are constructed as one-dimesional variables on
%their respective but different Z.
%Regressand is constructed as s function of both Z's of regressors on
%squared grid. Here BetaHr is used for effective correlation calculated after controlling for each of other
correlations.
Xs1(1:Nn,1:Nn)=ch0(1);
Xs2(1:Nn,1:Nn)=ch0(2);
Ys(1:Nn,1:Nn)=ch0(NN);
for nn=1:Nn
    for mm=1:Nn
        Xs1(mm,nn)=Xs1(mm,nn)+ch(1,1).*ZZ(1,nn)+ch(1,2).*(ZZ(1,nn).^2-1)+ch(1,3).*(ZZ(1,nn).^3-3*ZZ(1,nn));
        Xs2(mm,nn)=Xs2(mm,nn)+ch(2,1).*ZZ(2,mm)+ch(2,2).*(ZZ(2,mm).^2-1)+ch(2,3).*(ZZ(2,mm).^3-3*ZZ(2,mm));
        Ys(mm,nn)=Ys(mm,nn)+ch(NN,1).*BetaHr(1,1)*ZZ(1,nn)+ch(NN,2).*BetaHr(1,2)*(ZZ(1,nn).^2-1)+ ...
         ch(NN,3).*BetaHr(1,3)*(ZZ(1,nn).^3-3*ZZ(1,nn))+ ...
         ch(NN,1).*BetaHr(2,1)*ZZ(2,mm)+ch(NN,2).*BetaHr(2,2)*(ZZ(2,mm).^2-1)+ ...
         ch(NN,3).*BetaHr(2,3)*(ZZ(2,mm).^3-3*ZZ(2,mm));
    end
end

clf;
hold on
plot3(X1(1,1:TT),X1(2,1:TT),Y1(1:TT),'bo','linewidth',4);
surf(Xs1,Xs2,Ys)
title(sprintf('APPL Daily Returns VS MSFT AND NVDA Daily Returns: b11 =
%.3f,b21=%.3f,vh1=%.3f,b12=%.3f,b22=%.3f,vh2=%.5f,b13=%.3f,b23=%.3f,vh3=%.5f',
BetaHr(1,1),BetaHr(2,1),ch(NN,1),BetaHr(1,2),BetaHr(2,2),ch(NN,2),BetaHr(1,3),BetaHr(2,3),ch(NN,3)));%,sprintf('theta=
%f', theta), sprintf('kappa = %f', kappa),sprintf('sigma = %f', sigma0),sprintf('T = %f', T));

str=input('Look at 2-D Graph');
clf;

end

```

---

### #1723 — Amin (Topic Author)
*February 27, 2023, 8:46 PM*

Friends, I got an antipsychotic injection today and would be talking to my psychiatrist in a few days(I have not yet
heard back from his staff about the date).

Mind control agencies still continue to try to drug my food. Today, I bought food from a small street stall in a far off
area of Lahore.  The food had to be prepared but I knew that no mind control agent had reached there before I did so I
decided to wait and asked the guy to prepare food. Then a guy (mind control agent) from nowhere approached and started
talking to shop owner and then stood by him as if he were his partner while I was with the guy preparing food. Though
mind control guy was standing with the owner of the shop, I could see from their body movements that they were both very
reserved and not going well together. Then the mind control guy took a cloth from the owner and came towards the street
chef who was preparing the food and he was going to remove the cloth placed on food ingredients (to save them from dust
on the street) and replace it with the cloth he was carrying. I stopped him and told the street chef that if this new
guy replaces or touches anything among food ingredients, I would leave without buying any food from him so street chef
asked the mind control agent to stay behind. Mind control services project thought on food place workers and tell them
they are army intelligence and ask the workers to cooperate with the agents who would approach the shop so the workers
at the food shop become benign. Since I carefully noticed the guy preparing food, I could tell that everything he used
to prepare food was the same he had there from before and therefore I brought food home and it was good. So mind control
agents are still trying to somewhere give me drugged food and increase mind control.

After coming back home in the afternoon, I had a deep sleep since was tired and suffering from lesser sleep for past few
days trying to complete my work before the injection.

Now, I was thinking of new research directions that could follow the work on hermite regressions, and I thought that
there is a possibility of new research on Bayesian analysis, statistics and inference that would orthogonalize
non-linearity over hermite polynomials and then find solution to each hermite polynomial in a simple linear way. As an
obvious example, we could possibly have a kalman filter like algorithm for non-linear processes and divide non-linearity
in the evolution process into orthogonal hermite polynomial then update each orthogonal portion linearly.

There could also be many interesting applications in stochastic control.

I plan to do brainstorming for a day or two now and then re-start my work and try to present more interesting examples
of hermite regressions. I will also update my hermite regression program in a few days.

I really want to thank those friends who tried to help me by protesting to American government and defense since it
would never have been possible for me to properly concentrate on my research if things had not improved dramatically in
past few weeks. About three weeks earlier, mind control agencies were extremely aggressive  and they were drugging food
and water all over the city. Though they continued to try to drug my food, they were later trying to not make it very
obvious and they were far less aggressive and that made it easier for me to get good food and water and then concentrate
on my research. I do not believe I could do any substantial if things had continued like they were several weeks ago. I
am very thankful to good American friends for this favor that made it possible for me to do good work.

---

### #1724 — Amin (Topic Author)
*February 27, 2023, 10:06 PM*

I think the algorithm for hermite polynomial regressions would be easily understandable for most people but I will make
a detailed post tomorrow or day after that explaining everything in detail with latex equations.

---

### #1725 — Amin (Topic Author)
*February 27, 2023, 11:41 PM*

Friends, this is interesting but I am not sure whether it would be directly possible or not. Some thoughts that I am
sharing with friends. For example when I was working with solution of Z-series coefficients that match a particular set
of standardized central moments, I would think that I should possibly try to train some AI model and then retrieve
coefficients of Z-series out of it. Analytically, this required solution of highly non-linear equations with number of
equations equal to number of moments being matched. We could possibly solve for coefficients in sets of non-linear
equations by hermite regression.

For example if we want to find coefficients of Z-series that match a given set of moments and we can roughly know the
domain of solution, it could be possible with some effort to generate data of moments by picking approximately random
coefficients in the domain of solution and then find an approximate non-linear relationship (through non-linear hermite
regression) valid in that domain that gives us coefficients of Z-series given any set of moments. Though it might be
directly possible, even if it is not possible right away,  we would surely be solving for coefficients of sets of
non-linear equations with constraints (by generating random data and doing hermite non-linear regression on it) using
hermite polynomials with some further research in a few months or years.

I am sure there are many more interesting possibilities that  would open up with this research.

Though I will continue to post interesting examples of hermite regression and also a new program very soon, I would also
go back to completing my Z-series research paper with special emphasis on hermite non-linear regressions in it.

---

### #1726 — Amin (Topic Author)
*February 28, 2023, 10:01 AM*

I want to tell friends that mind control agencies have absolutely no intention of ending my mind control and mind
control of thousands of other innocent and talented people of different colors and creeds. They only want to buy time
and restart again with new even more aggressive tactics to somehow permanently retard me and thousands of other mind
control targets. If any people in defense say that they would end our mind control, they are completely lying and only
buying time. Corrupt generals in Pentagon have absolutely no intention of ending anybody's mind control at all. Due to
its relevance, I am copying another post here that I wrote earlier.

It seems that crooks in American army and mind control are unable to pay a heed to civilized calls by good American
people and others to end their animal cruel practices and remain bent on mischief. If crooks in American army and mind
control remain adamant on continuing evil practices, the only solution seems that some brave investigative journalists
expose them by running a comprehensive story on mind control practices by American army. It seems that doing a civilized
dialogue with hardened crooks in mind control gives them a strong sense of weakness of good people and makes the crooks
even more adamant to continue their evil practices.  Reminds me of Abu-Gharib. Very similarly, Crooks in defense had no
conception that they were doing any wrong thing when there was a culture of openly urinating on human captives. It was
an open thing in army and most crooks thought it was indeed a very right thing to do( and I am sure some of those crooks
still believe that it was a right thing they did even after being reprimanded by the broader American society). It was
not until brave people at CNN did a daring story against animal practices by crooks that evil practices stopped. Though
American army crooks retard intelligent people of all color and creed, these ultra right wing army crooks love to retard
blacks and muslims with great relish. Blacks are only 8-10% of US population but make a very large proportion of victims
in united states since many ultra right wing crooks in US army would rather die than let those intelligent blacks
succeed in American society in a big way.

I want to request CNN, New York Times, Washington Post, Al-Jazeera and large reputed European media outlets to run a
comprehensive story on mind control torture, retarding and victimization of intelligent people of US and other nations
by crooks in US army on behest of some powerful people in United States and due to rightwing extremist biases of these
crooks. If you would like to do investigative research about animal practices of US army, one great resource would be
mainland European embassies in Muslim countries who keep a detailed account of mind control persecution of intelligent
muslims in these countries by crooks in US army. Many of the staff in mainland European embassies are very good human
beings who abhor such practices and would love to cooperate with good journalists in exposing the evil animal practices
of US army crooks. Only the accounts of people at mainland European embassies in muslim countries thorough animal
practices of American army's mind control wing would be enough to drop a great bombshell in the media and general public
all across the world. I want to warn all the good people who try to have a civilized dialogue with crooks in American
army to end their evil practices that their being nice with crooks is a very misguided approach. Since good people do
not have the power to forcefully end the evil practices of US army crooks, only way to end the evil practices of US army
crooks is by exposing them openly in US public and all across the world.

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1680#p874052

---

### #1727 — Amin (Topic Author)
*February 28, 2023, 10:13 AM*

I have been detained more than 30 times by various psychiatrists during past twenty-five years on orders of Pakistan
Army.

Here, I will recall an incident eight years ago when I myself approached a lady psychiatrist for help and how she abused
me, and her staff beat me for twenty minutes and then tied me and started my treatment with antipsychotics again.

I am recalling this from early 2015. They had previously put me on extremely high antipsychotics and my creativity was
all gone. I could barely do any intellectual work. At that time, I was able to convince my family to decrease the
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

https://forum.wilmott.com/viewtopic.php?f=15&t=94796&start=315#p748191

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
that I seemed perfectly fine and asked me that she wanted to hear what my family had to say. I agreed and took an
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
mentioned that I was sitting and they were standing. . They literally continued to beat me and I continued to beg them
to stop. After fifteen minutes of beating me, they tied my legs and lifted me and put me on a bed in a room in the
psychiatrist facility and told me that doctor had gone to America and she could not see me. It was a complete lie and
the psychiatrist was in her office and was interviewing other patients when I arrived. I continued to ask them to loosen
the knots but they continued to make fun of me. I was totally surprised since Dr. N had behaved very nicely in the
previous meeting held at 20th with my mother and myself and I was sure she would declare me mentally sane on this
meeting. After I was kept tied for about half an hour, a new guard came and opened my hands and legs and said that they
would keep me at the facility for three days. The next day my medication in the form of pills started and I was also
given two more injections. I was given about nine pills at night and about eight pills in the morning. I was still not
given the opportunity to meet the psychiatrist N, and I was told several different things by different people including
that psychiatrist N had gone to America, and she had gone to Islamabad. About three days into my treatment, I saw
through the glass walls that psychiatrist N was interviewing her clients in her office. After seven days, I was asked to
meet psychiatrist N, and she said that she was unaware of the beating as she was in a meeting. Psychiatrist N also
assured me that I had no schizophrenia and previous doctors had very wrongly diagnosed me but it was a case of some
mania that she would properly treat this time.  Her staff continued to say that they were giving me drugs so that the
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

When I asked my mother who is living with me at the hospital, I wanted a second opinion, because of beating and other
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

---

### #1728 — Amin (Topic Author)
*February 28, 2023, 10:15 AM*

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

Now back to my obvious abuse by two other psychiatrists. I was detained by this doctor who was running a mental health facility and was not a psychiatrist himself. At that time I did not use to walk very much and my blood pressure used to be somewhat high. Since other antipsychotics had failed to retard me, doctor suggested I take aripperizole injections. These injections affect the heart and also elevate blood pressure but doctor who wanted to retard me had no regard for my health while pretending to cure me. In initial days of my detention, staff at the hospital when checked my blood pressure told me high enough blood pressure in line with what I used to have but after I complained about aripperizole and its effect on blood pressure the staff started doctoring blood pressure and started telling me that my blood pressure was very good or even low. This is a post I wrote on another thread in this forum about it. [How to safeguard my research - Page 32 - wilmott.com](https://forum.wilmott.com/viewtopic.php?f=15&t=94796&start=465#p785440)

.
>
>
> **Amin:**
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
He started my treatment without interviewing me and gave me electric shocks at the start to jumpstart the therapy. I was
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

---

### #1729 — Amin (Topic Author)
*February 28, 2023, 10:20 AM*

[My Letter To HRW About My Human Rights Abuse](https://forum.wilmott.com/viewtopic.php?f=15&t=102298)

Above is a very incomplete account of how various psychiatrists continued to play in hands of Pakistan army to retard
me. It also does not cover all the time till year 2022 and the account stops several years earlier.

Pakistan Army has no personal animosity with me. Chief of Pakistan Army staff is given more than 50 billion rupees every
year come rain or shine so that army continues American Mind control of intelligent people in Pakistan. Even when the
relations between both countries are extremely bad, this bribe is always given to Pakistan army generals in time.

Before writing this post, I want to apologize to good jews but want to tell them there are enough evil jews who are
doing everything to tarnish the great goodwill jews have so rightly earned through generations of hard work and being
nice and kind to other people in the society. I want to request good jews to Please force these evil(jewish) people to
end the bad practices that are starting to take root in American and other societies on their behest and before it is
too late. I also really hope that my mind control would finally end(as I have been begging for past twenty years) and I
would never have to write a post like this again.

In the past, I continued to mention about my mind control persecution from time to time but only started writing regularly about it when I arrived in UK on a Highly Skilled Migrant work visa. Mind control agencies did everything in their power to fail me in UK. People were asked to not give me a job. People I contacted were routinely told brazen lies about me totally shamelessly. When I realized that I had no future in UK, I returned to Pakistan after a six month stint in UK. Since my hard earned money had thoroughly insulted mind control infrastructure in UK as they had to drug entire cities with mind control chemicals in UK (read briefly about it in my application to HRW in a previous thread) for a nobody like me and American government had to move all their grand and influential puppets in UK (again for a nobody like me) to force people to drug the manufactured food. British Banks went to the extent to steal my money to bleed me. Read here: https://forum.wilmott.com/viewtopic.php?f=15&t=102298#p857494. British police forcefully stopped me from seeing law firms(Brief details are given in my application to HRW attached as a link below).  Since my money had given mind control agencies a very tough time, mind control agencies decided to never let me make significant money after that. My old Japanese employer was told to not hire me after I returned to Pakistan. Whoever I would contact someone in Europe for job or consulting, mind control agencies would move American embassy infrastructure in that country and somebody highly influential (or army or secret services of that particular country)  in that particular country would approach my target employer and again brazen lies and fabricated stories would be told about me shamelessly. I am a fighter in life and I continued my research despite all economic, coercive and other hardships. All odds were against me but I tried my best to continue.  I have been presenting my research to friends on this forum for past five or six years. At this point, I want to request good American and friends from other countries who have come to know me through my research to please use their influence to end my mind control forever.

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
Godfather is extremely generous towards them and it is well established and well known to people in mind control that
after retarding muslims, blacks and others in their career, they will move to paradise after they retire. No wonder
there is no let up in mind control whatever good people try.

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
by crooks in US army on behest of some powerful people in United States and due to rightwing extremist biases of these
crooks. If you would like to do investigative research about animal practices of US army, one great resource would be
mainland European embassies in Muslim countries who keep a detailed account of mind control persecution of intelligent
muslims in these countries by crooks in US army. Many of the staff in mainland European embassies are very good human
beings who abhor such practices and would love to cooperate with good journalists in exposing the evil animal practices
of US army crooks. Only the accounts of people at mainland European embassies in muslim countries thorough animal
practices of American army's mind control wing would be enough to drop a great bombshell in the media and general public
all across the world. I want to warn all the good people who try to have a civilized dialogue with crooks in American
army to end their evil practices that their being nice with crooks is a very misguided approach. Since good people do
not have the power to forcefully end the evil practices of US army crooks, only way to end the evil practices of US army
crooks is by exposing them openly in US public and all across the world.

It seems that crooks in American army and mind control are unable to pay a heed to civilized calls by good American
people and others to end their animal cruel practices and remain bent on mischief. If crooks in American army and mind
control remain adamant on continuing evil practices, the only solution seems that some brave investigative journalists
expose them by running a comprehensive story on mind control practices by American army. It seems that doing a civilized
dialogue with hardened crooks in mind control gives them a strong sense of weakness of good people and makes the crooks
even more adamant to continue their evil practices.  Reminds me of Abu-Gharib. Very similarly, Crooks in defense had no
conception that they were doing any wrong thing when there was a culture of openly urinating on human captives. It was
an open thing in army and most crooks thought it was indeed a very right thing to do( and I am sure some of those crooks
still believe that it was a right thing they did even after being reprimanded by the broader American society). It was
not until brave people at CNN did a daring story against animal practices by crooks that evil practices stopped. Though
American army crooks retard intelligent people of all color and creed, these ultra right wing army crooks love to retard
blacks and muslims with great relish. Blacks are only 8-10% of US population but make a very large proportion of victims
in united states since many ultra right wing crooks in US army would rather die than let those intelligent blacks
succeed in American society in a big way.

---

### #1730 — Amin (Topic Author)
*February 28, 2023, 8:37 PM*

Friends, in this post I want to explain the ideas behind hermite Z-series regressions. Even though though these ideas
are not difficult at all, I will keep things simple and first explain one variable hermite Z-series regression, and then
generalize it to multivariate hermite Z-series regressions.

In the first step of the regression, we have to find a Z-series representation of the marginal density of explained
variable and explanatory variable. This would usually be done by calculating moments of the explained and explanatory
random variable and then converting them into Z-series using method (and posted matlab program) I have previously
suggested on this forum. When we know that analytics between explained variable and explanatory variable are more
involved, we can easily fit up to eight moments to find Z-series if data set is large enough (and then run a hermite
regression to 7th order polynomial). In my initial experiments with hermite regressions, I just used first four moments.
First three moments were fixed at their observed values and fourth moment was fixed at positivity condition (Read here

about first derivative positivity condition: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1710#p874464) of first derivative dXdZ so that we could get a valid density.

Once we find a Z-series representation by fitting first four moment, it would be a third order polynomial. First the
Z-Series of regressand

$Y=a_0 + a_1 \, Z_1 + a_2 \, Z_1^2 + a_3 \, Z_1^3 $  Eq(A)

Then we find Z-series of regressor

$X=b_0 + b_1 \, Z_2 + b_2 \, Z_2^2 + b_3 \, Z_2^3 $  Eq(B)

We want to remind the friends that for every Z-series in powers of Z, there is an equivalent Z-series in hermite
polynomials given as

$Y=ah_0 + ah_1 \, Z_1 + ah_2 \, (Z_1^2-1) + ah_{3} \, (Z_1^3-3 \, Z_1) $

Then we find Z-series of regressor

$X=bh_0 + bh_1 \, Z_2 + bh_2 \, (Z_2^2 \, -\, 1) + bh_3 \, (Z_2^3 \, - \, 3 \, Z_2)$

Once we have found the Z-series, the first step is to find Z-values of regressors and regressand data with respect to
their marginal density. For each data point for every variable, we find out corresponding value of Z by inverting the
Z-series relationship given in equations A and B. This is non-linear standardization of data as opposed to linear
standardization used as ($Z=\frac{(X \, - \, \mu)}{\sigma}$ ). Again we are standardizing the data by finding inverse of
higher degree polynomial as opposed to linear standardization resulting from inverse of first degree polynomial. In what
follows, I will call this non-linear standardized values of observed data points as Z-values of data. These standardized
Z-values are found from observed data points by Newton root-finding algorithm after giving an intelligent starting
point.(This is included in my matlab program earlier posted)

Suppose we have a total of P (as in total paths of joint evolution of both stochastic processes) joint observations of
stochastic processes$X$ and Y. Here

$ Z_{1,p} $ denotes our standardized Z-value corresponding to pth observation of data of Y and$ Z_{2,p} $ denotes our
standardized Z-value corresponding to pth observation of data of explanatory variable$X$

For Finding Correlation between first hermite polynomial components, we write the equation for the correlation between
first hermites of one regressor and regressand as

$\rho_{XY,1} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} ah_1 \, Z_{1,p} \, bh_1 \, Z_{2,p} \,}{\sqrt{\displaystyle\sum_{p=1}^{P} ah_1^2 \, {Z_{1,p}}^2 \,\displaystyle\sum_{p=1}^{P} \, bh_1^2 \, {Z_{2,p}}^2 \,}}$

Again, Please notice that for calculation of above equation, we first have to find the specific values of$ Z_{1,p}$ and
$Z_{2,p}$ that are associated with particular pth observation of$X_p$ and$Y_p$ by some inversion method.

For Finding Correlation between second hermite polynomial components, we write the equation for the correlation between
second hermite polynomial of observation Z-values of one regressor and regressand as

$\rho_{XY,2} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} ah_2 \, ({Z_{1,p}}^2-1) \, bh_2 \, ({Z_{2,p}}^2-1) \,}{\sqrt{\displaystyle\sum_{p=1}^{P} ah_2^2 \, {(Z_{1,p}^2-1)}^2 \,\displaystyle\sum_{p=1}^{P} \, bh_2^2 \, {({Z_{2,p}}^2-1})^2 \,}}$

similarly for nth hermite polynaomial correlations, we would write as

$\rho_{XY,n} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} ah_n \, H_n(Z_1) \, bh_n \, H_n(Z_2) \,}{\sqrt{\displaystyle\sum_{p=1}^{P} ah_n^2 \, {H_n(Z_1)}^2 \,\displaystyle\sum_{p=1}^{P} \, bh_n^2 \, {H_n(Z_2)}^2 \,}}$

Please note that correlations are in joint products of hermite polynomials associated with observation Z-values. Their
coefficients are only required for covariances between hermite polynomials.

We know from simple regression theory that once we know correlation between two variables, we can write the regression
equation between them as

$Y \, = \, \mu_Y \, + \, \rho_{XY} \frac{s_Y}{s_X} \, (X\, - \, \mu_X) $

So we could write a variant of the above traditional formula in our new case (please notice that correlated contribution
from Z-values of regressors is being scaled by SD/volatility of marginal density of regressand) with hermite
correlations as

$Y \, = \, ah_0 \, + \, \rho_{XY,1} \, ah_1 \, Z_1 \, + \, \rho_{XY,2} \, ah_2 \, ({Z_1}^2 -1) \, + \, \rho_{XY,3} \, ah_3 \, ({Z_1}^3 -3 Z_1) + ...+\, \rho_{XY,n} \, ah_n \, H_n(Z_1)$

I will follow with generalization to multivariate hermite regression in next post.

---

### #1731 — Amin (Topic Author)
*March 1, 2023, 12:30 PM*

Friends, first of all my apology for not writing the second post yesterday. I was not feeling well and was making all
sort of mistakes and then I realized that I was not thinking properly and decided to not write the second post. Later I
noticed some errors in the first post as well. I am re-writing the corrected first post for univariate hermite
regression here and then I will start writing the second post for multivariate hermite regressions.

Here is the Yesterday's corrected post.

In the first step of the regression, we have to find a Z-series representation of the marginal density of explained
variable and explanatory variable. This would usually be done by calculating moments of the explained and explanatory
random variable and then converting them into Z-series using method (and posted matlab program) I have previously
suggested on this forum. When we know that analytics between explained variable and explanatory variable are more
involved, we can easily fit up to eight moments to find Z-series if data set is large enough (and then run a hermite
regression to 7th order polynomial). In my initial experiments with hermite regressions, I just used first four moments.
First three moments were fixed at their observed values and fourth moment was fixed at positivity condition (Read here

about first derivative positivity condition: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1710#p874464) of first derivative dXdZ so that we could get a valid density.

Once we find a Z-series representation by fitting first four moment, it would be a third order polynomial. First the
Z-Series of regressand

$Y=a_0 + a_1 \, Z_1 + a_2 \, Z_1^2 + a_3 \, Z_1^3 $  Eq(A)

Then we find Z-series of regressor

$X=b_0 + b_1 \, Z_2 + b_2 \, Z_2^2 + b_3 \, Z_2^3 $  Eq(B)

We want to remind the friends that for every Z-series in powers of Z, there is an equivalent Z-series in hermite
polynomials given as

$Y=ah_0 + ah_1 \, Z_1 + ah_2 \, (Z_1^2-1) + ah_{3} \, (Z_1^3-3 \, Z_1) $

Then we find Z-series of regressor

$X=bh_0 + bh_1 \, Z_2 + bh_2 \, (Z_2^2 \, -\, 1) + bh_3 \, (Z_2^3 \, - \, 3 \, Z_2)$

Once we have found the Z-series, the first step is to find Z-values of regressors and regressand data with respect to
their marginal density. For each data point for every variable, we find out corresponding value of Z by inverting the
Z-series relationship given in equations A and B. This is non-linear standardization of data as opposed to linear
standardization used as ($Z=\frac{(X \, - \, \mu)}{\sigma}$ ). Again we are standardizing the data by finding inverse of
higher degree polynomial as opposed to linear standardization resulting from inverse of first degree polynomial. In what
follows, I will call this non-linear standardized values of observed data points as Z-values of data. These standardized
Z-values are found from observed data points by Newton root-finding algorithm after giving an intelligent starting
point.(This is included in my matlab program earlier posted)

Suppose we have a total of P (as in total paths of joint evolution of both stochastic processes) joint observations of
stochastic processes$X$ and Y. Here

$ Z_{1,p} $ denotes our standardized Z-value corresponding to pth observation of data of Y and$ Z_{2,p} $ denotes our
standardized Z-value corresponding to pth observation of data of explanatory variable$X$

For Finding Correlation between first hermite polynomial components, we write the equation for the correlation between
first hermites of one regressor and regressand as follows in next equation. Here we are finding correlation between 1st
hermites of Z-values of observed data of both random variables.

[Disclaimer: We do not use hermite coefficients in calculations of hermite correlations as I wrote yesterday because
they can possibly lead to bad signs.]

$\rho_{XY,1} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} \, Z_{1,p} \, \, Z_{2,p} \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {Z_{1,p}}^2 \,\displaystyle\sum_{p=1}^{P} \, \, {Z_{2,p}}^2 \,}}$

Again, Please notice that for calculation of above equation, we first have to find the specific values of$ Z_{1,p}$ and
$Z_{2,p}$ that are associated with particular pth observation of$X_p$ and$Y_p$ by some inversion method.

For Finding Correlation between second hermite polynomial components, we write the equation for the correlation between
second hermite polynomial of observation Z-values of one regressor and regressand as follows in next equation.  Here we
are finding correlation between 2nd  hermites of Z-values of observed data of both random variables.

$\rho_{XY,2} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} \, ({Z_{1,p}}^2-1) \, \, ({Z_{2,p}}^2-1) \,}{\sqrt{\displaystyle\sum_{p=1}^{P}  \, {(Z_{1,p}^2-1)}^2 \,\displaystyle\sum_{p=1}^{P} \,  \, {({Z_{2,p}}^2-1})^2 \,}}$

similarly for nth hermite polynaomial correlations, we would write as

$\rho_{XY,n} \, = \,  \frac{\displaystyle\sum_{p=1}^{P}  \, H_n(Z_1)  \, H_n(Z_2) \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {H_n(Z_1)}^2 \,\displaystyle\sum_{p=1}^{P} \,  \, {H_n(Z_2)}^2 \,}}$

Please note that correlations are in joint products of hermite polynomials associated with observation Z-values. Their
coefficients are only required for covariances between hermite polynomials.

We know from simple regression theory that once we know correlation between two variables, we can write the regression
equation between them as

$Y \, = \, \mu_Y \, + \, \rho_{XY} \frac{s_Y}{s_X} \, (X\, - \, \mu_X) $

So we could write a variant of the above traditional formula in our new case (please notice that correlated contribution
from Z-values of regressors is being scaled by SD/volatility of marginal density of regressand) with hermite
correlations as

$Y \, = \, mu_Y \, + \, \rho_{XY,1} \, ah_1 \, Z_2 \, + \, \rho_{XY,2} \, ah_2 \, ({Z_2}^2 -1) \, + \, \rho_{XY,3} \, ah_3 \, ({Z_2}^3 -3 Z_2) + ...+\, \rho_{XY,n} \, ah_n \, H_n(Z_2)$

while explanatory variable X is given as before

$X=\mu_X \, + bh_1 \, Z_2 + bh_2 \, (Z_2^2 \, -\, 1) + bh_3 \, (Z_2^3 \, - \, 3 \, Z_2)$

I will follow with generalization to multivariate hermite regression in next post. I am writing it now.

---

### #1732 — Amin (Topic Author)
*March 1, 2023, 2:05 PM*

Here I explain  multivariate hermite polynomial regression with a simple multivariate regression example with three
hermite polynomials which can easily be generalized to any suitable order of hermite polynomials.

Just like in univariate regressions, we have to first find Z-series representations of marginal density of explained and
explanatory variables possibly by calculating moments and then converting them into appropriate Z-series.

Suppose we have found the Z-series of explained variable Y and M explanatory variables$X_1$ ,$ X_2$ up to$ X_M$ and they
are given as

$Y=a_0 + a_1 \, Z_y + a_2 \, {Z_y}^2 + a_3 \, {Z_y}^3 $  Eq(A)

Then we find Z-series of regressors

$X_1=b_0 + b_1 \, Z_{x1} + b_2 \, {Z_{x1}}^2 + b_3 \, {Z_{x1}}^3 $  Eq(B)

$X_2=c_0 + c_1 \, Z_{x2} + c_2 \, {Z_{x2}}^2 + c_3 \, {Z_{x2}}^3 $  Eq(B)

...

$X_M=d_0 + d_1 \, Z_{xM} + d_2 \, {Z_{xM}}^2 + d_3 \, {Z_{xM}}^3 $  Eq(B)

We find equivalent series in hermite polynomials  as

$Y=ah_0 + ah_1 \, Z_y + ah_2 \, ({Z_y}^2-1) + ah_{3} \, ({Z_y}^3-3 \, Z_y) $

Then we find  hermite series of regressors as

$X_1=bh_0 + bh_1 \, Z_{x1} + bh_2 \, ({Z_{x1}}^2 \, -\, 1) + bh_3 \, ({Z_{x1}}^3 \, - \, 3 \, {Z_{x1}})$

and

$X_2=ch_0 + ch_1 \, Z_{x2} + ch_2 \, ({Z_{x2}}^2 \, -\, 1) + ch_3 \, ({Z_{x2}}^3 \, - \, 3 \, {Z_{x2}})$

and

$X_M=dh_0 + dh_1 \, Z_{xM} + dh_2 \, ({Z_{xM}}^2 \, -\, 1) + dh_3 \, ({Z_{xM}}^3 \, - \, 3 \, {Z_{xM}})$

Once we have found the Z-series, the first step is to find Z-values of regressors and regressand data with respect to
their marginal density. For each data point observation for every variable, we find out corresponding value of Z by
inverting the Z-series relationship given in equations A and B. This is non-linear standardization of data to find the
Z-values of data.

Suppose we have a total of P (as in total paths of joint evolution of both stochastic processes) joint observations of
stochastic processes$X$ and Y. Here

$ Z_{x,p} $ denotes our standardized Z-value corresponding to pth observation of data of X and$ Z_{y,p} $ denotes our
standardized Z-value corresponding to pth observation of data of variable$Y$

We define

$\rho_{XY,1} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} \, Z_{x,p} \, \, Z_{y,p} \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {Z_{x,p}}^2 \,\displaystyle\sum_{p=1}^{P} \, \, {Z_{y,p}}^2 \,}}$

$\rho_{XY,2} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} \, ({Z_{x,p}}^2-1) \, \, ({Z_{y,p}}^2-1) \,}{\sqrt{\displaystyle\sum_{p=1}^{P}  \, {(Z_{x,p}^2-1)}^2 \,\displaystyle\sum_{p=1}^{P} \,  \, {({Z_{y,p}}^2-1})^2 \,}}$

similarly for nth hermite polynaomial correlations, we would write as

$\rho_{XY,n} \, = \,  \frac{\displaystyle\sum_{p=1}^{P}  \, H_n(Z_x)  \, H_n(Z_y) \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {H_n(Z_x)}^2 \,\displaystyle\sum_{p=1}^{P} \,  \, {H_n(Z_y)}^2 \,}}$

We find standardized regression coefficients for each hermite polynomial in the multivariate regression as

$\begin{bmatrix}

         \beta_{11} & \beta_{12} & \cdots & \beta_{1M}

     \end{bmatrix}

     \times

     \begin{bmatrix}

         \rho_{X1X1,1} & \rho_{X1X2,1} & \cdots & \rho_{X1XM,1}\\

         \rho_{X1X2,1} & \rho_{X2X2,1} & \cdots & \rho_{X2XM,1}\\

         \vdots & \vdots & \ddots & \vdots\\

         \rho_{X1XM,1} & \rho_{X2XM,1} & \cdots & \rho_{XMXM,1}

     \end{bmatrix}

      =

     \begin{bmatrix}

          \rho_{X1Y,1} & \rho_{X2Y,1} & \cdots & \rho_{XMY,1}

     \end{bmatrix}$

In above square matrix on LHS is a matrix of first hermite correlations between regressors and the row vector on RHS has
correlations between first hermites of regressors and explained variable. Row vector of betas on LHS is vector of
standardized regression coefficients associated with first hermite polynomial of various explanatory variables.

We represent it as

                                      $ \beta_1 \, \textbf{R}_1 = \, \textbf{r}_{XY,1}$

$ \beta_1 \, = \beta_1 \, \textbf{R}_1 \, {\textbf{R}_1}^{-1} = \, \textbf{r}_{XY,1}\, {\textbf{R}_1}^{-1}$

In above we solved for the standardized regression coefficients of various explanatory variables associated with first
hermite polynomial correlations. This is a row vector.

Similarly for 2nd hermite polynomial correlations, we can solve for standardized regression coefficients of second
hermites of various explanatory variables as

                                    $ \beta_2 \, = \, \textbf{r}_{XY,2}\, {\textbf{R}_2}^{-1}$

In above square matrix$ {\textbf{R}_2}$ is a matrix of second hermite polynomial correlations between regressors and
$\textbf{r}_{XY,2}$ has correlations between second hermite polynomials of regressors and explained variable.

And similarly for third hermite polynomial regression coefficients and so on.

Once we have solved for standardized regression coefficients associated with various hermite polynomials, we can write
the hermite regression equation of the explained variable after multiplying with original hermite coefficients as

$Y=\mu_y + ah_1 \, \big[ \beta_{11} \, Z_{x1} + \beta_{12} \, Z_{x2} + ....+ \beta_{1M} \, Z_{xM} \, \big] $

$+ ah_2 \, \big[ \beta_{21} \, ({Z_{x1}}^2 -1) + \beta_{22} \, ({Z_{x2}}^2-1)   + ....+ \beta_{2M} \, ({Z_{xM}}^2-1) \, \big] $

$+ ah_3 \, \big[ \beta_{31} \, ({Z_{x1}}^3 -3 Z_{x1}) + \beta_{32} \, ({Z_{x2}}^3-3 \, Z_{x2})   + ....+ \beta_{3M} \, ({Z_{xM}}^3-3 \, Z_{xM}) \, \big] $

In above$\beta $ s are standardized regression coefficients associated with hermite polynomials of explanatory
variables. While$ah_1$ ,$ah_2$ and$ah_3$ are coefficients of hermite series in the original marginal density
representation that we derived from first few moments.

For graphing and other purposes, we would use the following values of explanatory variables from their marginal
densities

$X_1=bh_0 + bh_1 \, Z_{x1} + bh_2 \, ({Z_{x1}}^2 \, -\, 1) + bh_3 \, ({Z_{x1}}^3 \, - \, 3 \, {Z_{x1}})$

and

$X_2=ch_0 + ch_1 \, Z_{x2} + ch_2 \, ({Z_{x2}}^2 \, -\, 1) + ch_3 \, ({Z_{x2}}^3 \, - \, 3 \, {Z_{x2}})$

and

$X_M=dh_0 + dh_1 \, Z_{xM} + dh_2 \, ({Z_{xM}}^2 \, -\, 1) + dh_3 \, ({Z_{xM}}^3 \, - \, 3 \, {Z_{xM}})$

---

### #1733 — Amin (Topic Author)
*March 3, 2023, 10:57 AM*

>
> Here I explain  multivariate hermite polynomial regression with a simple multivariate regression example with three
hermite polynomials which can easily be generalized to any suitable order of hermite polynomials.
>
>
>
> Just like in univariate regressions, we have to first find Z-series representations of marginal density of explained
and explanatory variables possibly by calculating moments and then converting them into appropriate Z-series.
>
> Suppose we have found the Z-series of explained variable Y and M explanatory variables$X_1$ ,$ X_2$ up to$ X_M$ and
they are given as
>
>
>
> $Y=a_0 + a_1 \, Z_y + a_2 \, {Z_y}^2 + a_3 \, {Z_y}^3 $  Eq(A)
>
> Then we find Z-series of regressors
>
> $X_1=b_0 + b_1 \, Z_{x1} + b_2 \, {Z_{x1}}^2 + b_3 \, {Z_{x1}}^3 $  Eq(B)
>
> $X_2=c_0 + c_1 \, Z_{x2} + c_2 \, {Z_{x2}}^2 + c_3 \, {Z_{x2}}^3 $  Eq(B)
>
> ...
>
> $X_M=d_0 + d_1 \, Z_{xM} + d_2 \, {Z_{xM}}^2 + d_3 \, {Z_{xM}}^3 $  Eq(B)
>
>
>
> We find equivalent series in hermite polynomials  as
>
>
>
> $Y=ah_0 + ah_1 \, Z_y + ah_2 \, ({Z_y}^2-1) + ah_{3} \, ({Z_y}^3-3 \, Z_y) $
>
> Then we find  hermite series of regressors as
>
> $X_1=bh_0 + bh_1 \, Z_{x1} + bh_2 \, ({Z_{x1}}^2 \, -\, 1) + bh_3 \, ({Z_{x1}}^3 \, - \, 3 \, {Z_{x1}})$
>
> and
>
> $X_2=ch_0 + ch_1 \, Z_{x2} + ch_2 \, ({Z_{x2}}^2 \, -\, 1) + ch_3 \, ({Z_{x2}}^3 \, - \, 3 \, {Z_{x2}})$
>
> and
>
> $X_M=dh_0 + dh_1 \, Z_{xM} + dh_2 \, ({Z_{xM}}^2 \, -\, 1) + dh_3 \, ({Z_{xM}}^3 \, - \, 3 \, {Z_{xM}})$
>
>
>
> Once we have found the Z-series, the first step is to find Z-values of regressors and regressand data with respect to
their marginal density. For each data point observation for every variable, we find out corresponding value of Z by
inverting the Z-series relationship given in equations A and B. This is non-linear standardization of data to find the
Z-values of data.
>
>
>
> Suppose we have a total of P (as in total paths of joint evolution of both stochastic processes) joint observations of
stochastic processes$X$ and Y. Here
>
>$ Z_{x,p} $ denotes our standardized Z-value corresponding to pth observation of data of X and$ Z_{y,p} $ denotes our
standardized Z-value corresponding to pth observation of data of variable$Y$
>
> We define
>
>
$\rho_{XY,1} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} \, Z_{x,p} \, \, Z_{y,p} \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {Z_{x,p}}^2 \,\displaystyle\sum_{p=1}^{P} \, \, {Z_{y,p}}^2 \,}}$
>
>
>
>
$\rho_{XY,2} \, = \,  \frac{\displaystyle\sum_{p=1}^{P} \, ({Z_{x,p}}^2-1) \, \, ({Z_{y,p}}^2-1) \,}{\sqrt{\displaystyle\sum_{p=1}^{P}  \, {(Z_{x,p}^2-1)}^2 \,\displaystyle\sum_{p=1}^{P} \,  \, {({Z_{y,p}}^2-1})^2 \,}}$
>
>
>
> similarly for nth hermite polynaomial correlations, we would write as
>
>
>
>
$\rho_{XY,n} \, = \,  \frac{\displaystyle\sum_{p=1}^{P}  \, H_n(Z_x)  \, H_n(Z_y) \,}{\sqrt{\displaystyle\sum_{p=1}^{P} \, {H_n(Z_x)}^2 \,\displaystyle\sum_{p=1}^{P} \,  \, {H_n(Z_y)}^2 \,}}$
>
>
>
> We find standardized regression coefficients for each hermite polynomial in the multivariate regression as
>
>
>
> $\begin{bmatrix}
>
>          \beta_{11} & \beta_{12} & \cdots & \beta_{1M}
>
>      \end{bmatrix}
>
>      \times
>
>      \begin{bmatrix}
>
>          \rho_{X1X1,1} & \rho_{X1X2,1} & \cdots & \rho_{X1XM,1}\\
>
>          \rho_{X1X2,1} & \rho_{X2X2,1} & \cdots & \rho_{X2XM,1}\\
>
>          \vdots & \vdots & \ddots & \vdots\\
>
>          \rho_{X1XM,1} & \rho_{X2XM,1} & \cdots & \rho_{XMXM,1}
>
>      \end{bmatrix}
>
>       =
>
>      \begin{bmatrix}
>
>           \rho_{X1Y,1} & \rho_{X2Y,1} & \cdots & \rho_{XMY,1}
>
>      \end{bmatrix}$
>
>
>
> In above square matrix on LHS is a matrix of first hermite correlations between regressors and the row vector on RHS
has correlations between first hermites of regressors and explained variable. Row vector of betas on LHS is vector of
standardized regression coefficients associated with first hermite polynomial of various explanatory variables.
>
> We represent it as
>
>
>
>                                       $ \beta_1 \, \textbf{R}_1 = \, \textbf{r}_{XY,1}$
>
>$ \beta_1 \, = \beta_1 \, \textbf{R}_1 \, {\textbf{R}_1}^{-1} = \, \textbf{r}_{XY,1}\, {\textbf{R}_1}^{-1}$
>
>
>
> In above we solved for the standardized regression coefficients of various explanatory variables associated with first
hermite polynomial correlations. This is a row vector.
>
> Similarly for 2nd hermite polynomial correlations, we can solve for standardized regression coefficients of second
hermites of various explanatory variables as
>
>                                     $ \beta_2 \, = \, \textbf{r}_{XY,2}\, {\textbf{R}_2}^{-1}$
>
> In above square matrix$ {\textbf{R}_2}$ is a matrix of second hermite polynomial correlations between regressors and
$\textbf{r}_{XY,2}$ has correlations between second hermite polynomials of regressors and explained variable.
>
> And similarly for third hermite polynomial regression coefficients and so on.
>
> Once we have solved for standardized regression coefficients associated with various hermite polynomials, we can write
the hermite regression equation of the explained variable after multiplying with original hermite coefficients as
>
>
>
> $Y=\mu_y + ah_1 \, \big[ \beta_{11} \, Z_{x1} + \beta_{12} \, Z_{x2} + ....+ \beta_{1M} \, Z_{xM} \, \big] $
>
>
$+ ah_2 \, \big[ \beta_{21} \, ({Z_{x1}}^2 -1) + \beta_{22} \, ({Z_{x2}}^2-1)   + ....+ \beta_{2M} \, ({Z_{xM}}^2-1) \, \big] $
>
>
$+ ah_3 \, \big[ \beta_{31} \, ({Z_{x1}}^3 -3 Z_{x1}) + \beta_{32} \, ({Z_{x2}}^3-3 \, Z_{x2})   + ....+ \beta_{3M} \, ({Z_{xM}}^3-3 \, Z_{xM}) \, \big] $
>
>
>
> In above$\beta $ s are standardized regression coefficients associated with hermite polynomials of explanatory
variables. While$ah_1$ ,$ah_2$ and$ah_3$ are coefficients of hermite series in the original marginal density
representation that we derived from first few moments.
>
> For graphing and other purposes, we would use the following values of explanatory variables from their marginal
densities
>
> $X_1=bh_0 + bh_1 \, Z_{x1} + bh_2 \, ({Z_{x1}}^2 \, -\, 1) + bh_3 \, ({Z_{x1}}^3 \, - \, 3 \, {Z_{x1}})$
>
> and
>
> $X_2=ch_0 + ch_1 \, Z_{x2} + ch_2 \, ({Z_{x2}}^2 \, -\, 1) + ch_3 \, ({Z_{x2}}^3 \, - \, 3 \, {Z_{x2}})$
>
> and
>
> $X_M=dh_0 + dh_1 \, Z_{xM} + dh_2 \, ({Z_{xM}}^2 \, -\, 1) + dh_3 \, ({Z_{xM}}^3 \, - \, 3 \, {Z_{xM}})$
>
.

.

$Y=\mu_y + ah_1 \, \big[ \beta_{11} \, Z_{x1} + \beta_{12} \, Z_{x2} + ....+ \beta_{1M} \, Z_{xM} \, \big] $

$+ ah_2 \, \big[ \beta_{21} \, ({Z_{x1}}^2 -1) + \beta_{22} \, ({Z_{x2}}^2-1)   + ....+ \beta_{2M} \, ({Z_{xM}}^2-1) \, \big] $

$+ ah_3 \, \big[ \beta_{31} \, ({Z_{x1}}^3 -3 Z_{x1}) + \beta_{32} \, ({Z_{x2}}^3-3 \, Z_{x2})   + ....+ \beta_{3M} \, ({Z_{xM}}^3-3 \, Z_{xM}) \, \big] $

Friends, in the above equation, we could equally have constructed the non-linearly standardized Z-form of  Y as

$Z_{y}=\overline{\mu_y} + \overline{ah_1} \, \big[ \beta_{11} \, Z_{x1} + \beta_{12} \, Z_{x2} + ....+ \beta_{1M} \, Z_{xM} \, \big] $

$+ \overline{ah_2} \, \big[ \beta_{21} \, ({Z_{x1}}^2 -1) + \beta_{22} \, ({Z_{x2}}^2-1)   + ....+ \beta_{2M} \, ({Z_{xM}}^2-1) \, \big] $

$+ \overline{ah_3} \, \big[ \beta_{31} \, ({Z_{x1}}^3 -3 Z_{x1}) + \beta_{32} \, ({Z_{x2}}^3-3 \, Z_{x2})   + ....+ \beta_{3M} \, ({Z_{xM}}^3-3 \, Z_{xM}) \, \big] $

.

In the above standardized equation for Y, we use standardized hermite coefficients (shown with overline bar) which are
defined by dividing each hermite coefficient with square root of variance as

Total variance is given as squared sum of hermite coefficients as
$Var \, = \, {ah_1}^2\, + \,{ah_2}^2\, + \,{ah_3}^2\, + ...+ \,{ah_n}^2\,$

So

$\overline{\mu_y} \,=\, \frac{\mu_y}{\sqrt{Var}} \,=\, \frac{ah_0}{\sqrt{Var}} \,$

$\overline{ah_1} \,=\, \frac{ah_1}{\sqrt{Var}} \,$

$\overline{ah_2} \,=\, \frac{ah_2}{\sqrt{Var}} \,$

and

$\overline{ah_n} \,=\, \frac{ah_n}{\sqrt{Var}} \,$

This post is about getting orientation in case you want to find standardized values of explained variable directly from
regression. This way you can directly find Z-values from regression given the explanatory variable data and then compare
them directly to Z-values from observation data of explained variable.

I am sure most friends would have realized that they do not need to necessarily find regression coefficients using
correlations, just like in ordinary regression, you can directly find them from the (matrix vector product of data  as
in OLS but there would need to be one matrix vector equation solution for each hermite polynomial) data without
resorting to correlations. This is what I will explain in next post with equations. You can directly run regressions
equal to number of orthogonal hermite polynomials with each regression between a matrix of hermite deviations
(constructed by applying hermite polynomial to  Z-values of explanatory variables) of observation data of explanatory
variables multiplied by vector of regression coefficients of that hermite polynomial and (this matrix vector product)
equated with  vector of hermite deviations (constructed by applying hermite polynomial to Z-values of observed explained
variable) of observation data of explained variable. I will be writing these equations in the next post in a few hours.

---

### #1734 — Amin (Topic Author)
*March 3, 2023, 1:25 PM*

First I copy the background, and notations from previous post as follows and then continue with new post.

Here I explain  multivariate hermite polynomial regression with a simple multivariate regression example with three
hermite polynomials which can easily be generalized to any suitable order of hermite polynomials.

Just like in univariate regressions, we have to first find Z-series representations of marginal density of explained and
explanatory variables possibly by calculating moments and then converting them into appropriate Z-series.

Suppose we have found the Z-series of explained variable Y and M explanatory variables$X_1$ ,$ X_2$ up to$ X_M$ and they
are given as

$Y=a_0 + a_1 \, Z_y + a_2 \, {Z_y}^2 + a_3 \, {Z_y}^3 $  Eq(A)

Then we find Z-series of regressors

$X_1=b_0 + b_1 \, Z_{x1} + b_2 \, {Z_{x1}}^2 + b_3 \, {Z_{x1}}^3 $  Eq(B)

$X_2=c_0 + c_1 \, Z_{x2} + c_2 \, {Z_{x2}}^2 + c_3 \, {Z_{x2}}^3 $  Eq(B)

...

$X_M=d_0 + d_1 \, Z_{xM} + d_2 \, {Z_{xM}}^2 + d_3 \, {Z_{xM}}^3 $  Eq(B)

We find equivalent series in hermite polynomials  as

$Y=ah_0 + ah_1 \, Z_y + ah_2 \, ({Z_y}^2-1) + ah_{3} \, ({Z_y}^3-3 \, Z_y) $

Then we find  hermite series of regressors as

$X_1=bh_0 + bh_1 \, Z_{x1} + bh_2 \, ({Z_{x1}}^2 \, -\, 1) + bh_3 \, ({Z_{x1}}^3 \, - \, 3 \, {Z_{x1}})$

and

$X_2=ch_0 + ch_1 \, Z_{x2} + ch_2 \, ({Z_{x2}}^2 \, -\, 1) + ch_3 \, ({Z_{x2}}^3 \, - \, 3 \, {Z_{x2}})$

and

$X_M=dh_0 + dh_1 \, Z_{xM} + dh_2 \, ({Z_{xM}}^2 \, -\, 1) + dh_3 \, ({Z_{xM}}^3 \, - \, 3 \, {Z_{xM}})$

Once we have found the Z-series, the first step is to find Z-values of regressors and regressand data with respect to
their marginal density. For each data point observation for every variable, we find out corresponding value of Z by
inverting the Z-series relationship given in equations A and B. This is non-linear standardization of data to find the
Z-values of data.

Suppose we have a total of P (as in total paths of joint evolution of both stochastic processes) joint observations of
stochastic processes$X$ and Y. Here

$ Z_{x,p} $ denotes our standardized Z-value corresponding to pth observation of data of X and$ Z_{y,p} $ denotes our
standardized Z-value corresponding to pth observation of data of variable$Y$

We will need Hermite polynomial values calculated at Z-Values of pth observation of data and we denote that as

$H_1(Z_{x,p}) \, = \, Z_{x,p} $

$H_2(Z_{x,p}) \, = \, {Z_{x,p}}^2 \, - \, 1$

$H_3(Z_{x,p}) \, = \, {Z_{x,p}}^3 \, - \, 3 \,Z_{x,p} $

and so on.

Now we set up our vector-matrix Equation for 1st hermite polynomial as

$ \begin{bmatrix}

        bh_1 \, H_1(Z_{x1,1}) & ch_1 \,H_1(Z_{x2,1}) & \cdots & dh_1 \, H_1(Z_{xM,1})\\

        bh_1 \, H_1(Z_{x1,2}) & ch_1 \,H_1(Z_{x2,2}) & \cdots & dh_ 1 \, H_1(Z_{xM,2})\\

        \vdots & \vdots & \ddots & \vdots\\

        bh_1 \, H_1(Z_{x1,P}) & ch_1 \, H_1(Z_{x2,P}) & \cdots & dh1\, H_1(Z_{xM,P})

    \end{bmatrix}

    \times

    \begin{bmatrix}

         b_{11}\\

         b_{12}\\

         \vdots\\

         b_{1M}

     \end{bmatrix}

    =

\begin{bmatrix}

         ah_1 \, H_1(Z_{y,1})\\

         ah_1 \, H_1(Z_{y,2})\\

         \vdots\\

         ah_1 \, H_1(Z_{y,P})

     \end{bmatrix}

$$

In above system, there are P rows with each row specifying data of that particular pth observation.

Least square solution of the above vector-matrix equation would find us the required regression coefficients of first hermites of explanatory variables directly from the data. Please note that these regression coefficients are different from standardized regression coefficients that were found when dealing with correlations.

Similarly to 1st hermite regression coefficients, we can easily write matrix vector equation for second hermite regression coefficients as

$ \begin{bmatrix}

        bh_2 \, H_2(Z_{x1,1}) & ch_2 \,H_2(Z_{x2,1}) & \cdots & dh_2 \, H_2(Z_{xM,1})\\

        bh_2 \, H_2(Z_{x1,2}) & ch_2 \,H_2(Z_{x2,2}) & \cdots & dh_ 2 \, H_2(Z_{xM,2})\\

        \vdots & \vdots & \ddots & \vdots\\

        bh_2 \, H_2(Z_{x1,P}) & ch_2 \, H_2(Z_{x2,P}) & \cdots & dh_2\, H_2(Z_{xM,P})

    \end{bmatrix}

    \times

    \begin{bmatrix}

         b_{21}\\

         b_{22}\\

         \vdots\\

         b_{2M}

     \end{bmatrix}

    =

\begin{bmatrix}

         ah_2 \, H_2(Z_{y,1})\\

         ah_2 \, H_2(Z_{y,2})\\

         \vdots\\

         ah_2 \, H_2(Z_{y,P})

     \end{bmatrix}

$$

which can be solved to get the regression coefficients associated with second hermites of the explanatory variables.

And so on for higher order hermite polynomials.

Once we have solved for standardized regression coefficients associated with various hermite polynomials, we can write
the hermite regression equation of the explained variable after multiplying with original hermite coefficients as

$Y=\mu_y + \, \big[ b_{11} \, bh_1 \,  Z_{x1} + b_{12} \, ch_1 \, Z_{x2} + ....+ b_{1M} \,dh_1 \,  Z_{xM} \, \big] $

$+ \, \big[ b_{21} \,bh_2\,  ({Z_{x1}}^2 -1) + b_{22} \, ch_2 \,  ({Z_{x2}}^2-1)   + ....+ b_{2M} \,dh_2 \, ({Z_{xM}}^2-1) \, \big] $

$+ \, \big[ b_{31} \,bh_3 \, ({Z_{x1}}^3 -3 Z_{x1}) + b_{32} \,ch_3\, ({Z_{x2}}^3-3 \, Z_{x2})   + ....+ b_{3M} \,dh_3 ({Z_{xM}}^3-3 \, Z_{xM}) \, \big] $

For graphing and other purposes, we would use the following values of explanatory variables from their marginal
densities

$X_1=bh_0 + bh_1 \, Z_{x1} + bh_2 \, ({Z_{x1}}^2 \, -\, 1) + bh_3 \, ({Z_{x1}}^3 \, - \, 3 \, {Z_{x1}})$

and

$X_2=ch_0 + ch_1 \, Z_{x2} + ch_2 \, ({Z_{x2}}^2 \, -\, 1) + ch_3 \, ({Z_{x2}}^3 \, - \, 3 \, {Z_{x2}})$

and

$X_M=dh_0 + dh_1 \, Z_{xM} + dh_2 \, ({Z_{xM}}^2 \, -\, 1) + dh_3 \, ({Z_{xM}}^3 \, - \, 3 \, {Z_{xM}})$

---

### #1735 — Amin (Topic Author)
*March 4, 2023, 7:04 AM*

Friends, my microsoft account has been acting strange. Two months ago when I wanted to write Z-series paper, I bought 
monthly renewable subscription of microsoft 365 for Rs. 1099 which is now Rs. 1399. First two months have gone well and
I could easily charge on my debit card.

Problem is that I have to call my bank and ask them to unlock my card for few hours (or more) for international banking
to make international credit card transactions. If I do not unlock my account, card will not go through and some charge
will still accrue in my account. Bank clearly tells the customer that bank will not be responsible for any wrong use of
the card for the period the card account was unlocked for international banking.

I unlocked my account and continued to try to pay for my subscription but it would not work. I called my bank and they
told me that my account had already been open for international card payments. On further inquiry they told me that
their had been attempts at charging my card (which would have cost me quite some money) bur CVV was not good. I went to
the microsoft account again and repeatedly made sure that I input appropriate CVV but still my card did not go through.
There was no microsoft customer support email and they had no phone support in Pakistan. I also noticed when I was
trying to pay for my microsot 365 service, there was a large heading on top of microsoft account that a charge of \$299
for microsoft XBOX had been denied on my account. I do not play computer games and did not even remotely try to
subscribe XBOX but for some reason there was a message that an attempt to charge 299 dollars from my account for XBOX
had been denied.

I do not know what is going on with microsoft account now. I just wanted to pay for microsoft service since it is a
great company that does so many good things otherwise I have very little money and usually cannot pay for expensive
software. But my attempt at legally buying software from microsoft has already become pain in the neck. I really have
some feeling that there is possibly somebody at microsoft who is playing in hands of mind control agencies to alter my
account though I cannot be sure. Or they might be using access to my computer to send orders to subscribe XBOX and take
my money. I still do not know what is going on?

---

### #1736 — Amin (Topic Author)
*March 6, 2023, 3:35 AM*

>
> Friends, I want to mention that an antipsychotic injection is due on coming Monday so I may not be able to work very
well after a few days. I have requested psychiatrist's office to arrange a phone meeting which should possibly follow in
next few days. I really want to ask the doctor to end my injections and antipsychotic medication as I am perfectly
mentally healthy. Many psychiatrists in Pakistan force antipsychotics on healthy people and also detain them for long
periods of time under pressure and coercion from Pakistan army (whose generals receive tens of millions of dollars in
bribes from US army to facilitate mind control of intelligent people in Pakistan).
>
> I also want to request European embassies in Pakistan to keep a vigil and record my phone call with the psychiatrist
so they would know the tactics of CIA, Pakistan army and psychiatrists to gain an understanding of mind control abuse
since a lot of very talented Europeans suffer from a very similar abuse on hands of corrupt generals in American army.
>
> I also want to request American and Pakistani friends if they can possibly approach my psychiatrist  (Far*** A. Minhas
of treehouse, Peshawar road, Rawalpindi) to tell him about horrors of mind control abuse and stop following the orders
of Pakistan military. Many times these psychiatrists are not bad people but they are told concocted lies and false
ethical justification about mind control by generals who would have already taken large sums of bribes. I am sure many
of these psychiatrists would be very careful about mistreating  their patients once they know the truth. But I cannot
take this risk on my own since there is a huge possibility that doctor might even increase my medication several fold if
I say this is all a conspiracy. It is unbelievably moronic but I have read it myself in psychiatry books that whoever
claims that secret services are after him is schizophrenic.
>
.

I am suffering very badly due to effects of antipsychotic injection. I have body ache all over and many times my
breathing turns into light snoring and difficulty in breathing(which is a side-effect of fluanxol injection). And I have
become very depressed and unable to do any positive mental activity. I hope to be better in a few days and re-start my
research work but this is the same three week cycle that I have to pass through. Due to heavy sedation, I have been
sleeping 14-15 hours for past two days and I get extremely exhausted with just very little bit of work.

I would possibly have a call with my psychiatrist tomorrow or day after tomorrow. I will try to ask the psychiatrist to
end my medication. I want to request friends to play a role if they can help me in any way. I am already greatly
indebted to many friends who helped me by protesting to American army and consequently I was able to concentrate on my
work and had been able to do good research in the past as my mind control decreased. Please approach both American army
and the psychiatrist mentioned in quoted post and ask them to end my forced medication.

---

### #1737 — Amin (Topic Author)
*March 7, 2023, 1:10 PM*

>
>
> Friends, I want to mention that an antipsychotic injection is due on coming Monday so I may not be able to work very
well after a few days. I have requested psychiatrist's office to arrange a phone meeting which should possibly follow in
next few days. I really want to ask the doctor to end my injections and antipsychotic medication as I am perfectly
mentally healthy. Many psychiatrists in Pakistan force antipsychotics on healthy people and also detain them for long
periods of time under pressure and coercion from Pakistan army (whose generals receive tens of millions of dollars in
bribes from US army to facilitate mind control of intelligent people in Pakistan).
>
> I also want to request European embassies in Pakistan to keep a vigil and record my phone call with the psychiatrist
so they would know the tactics of CIA, Pakistan army and psychiatrists to gain an understanding of mind control abuse
since a lot of very talented Europeans suffer from a very similar abuse on hands of corrupt generals in American army.
>
> I also want to request American and Pakistani friends if they can possibly approach my psychiatrist  (Far*** A. Minhas
of treehouse, Peshawar road, Rawalpindi) to tell him about horrors of mind control abuse and stop following the orders
of Pakistan military. Many times these psychiatrists are not bad people but they are told concocted lies and false
ethical justification about mind control by generals who would have already taken large sums of bribes. I am sure many
of these psychiatrists would be very careful about mistreating  their patients once they know the truth. But I cannot
take this risk on my own since there is a huge possibility that doctor might even increase my medication several fold if
I say this is all a conspiracy. It is unbelievably moronic but I have read it myself in psychiatry books that whoever
claims that secret services are after him is schizophrenic.
>
.

I am suffering very badly due to effects of antipsychotic injection. I have body ache all over and many times my
breathing turns into light snoring and difficulty in breathing(which is a side-effect of fluanxol injection). And I have
become very depressed and unable to do any positive mental activity. I hope to be better in a few days and re-start my
research work but this is the same three week cycle that I have to pass through. Due to heavy sedation, I have been
sleeping 14-15 hours for past two days and I get extremely exhausted with just very little bit of work.

I would possibly have a call with my psychiatrist tomorrow or day after tomorrow. I will try to ask the psychiatrist to
end my medication. I want to request friends to play a role if they can help me in any way. I am already greatly
indebted to many friends who helped me by protesting to American army and consequently I was able to concentrate on my
work and had been able to do good research in the past as my mind control decreased. Please approach both American army
and the psychiatrist mentioned in quoted post and ask them to end my forced medication.

.

.

Friends, I have been given time tomorrow at 2:30 pm PST for phone meeting with the psychiatrist.

Meanwhile, I have re-started my research and I am trying an interesting example for the application of hermite
orthogonal regressions. I hope if things go well, I should be able to present my work in 2-4 days.

I am very optimistic that we would be able to replace a lot of AI and ML in statistics with hermite orthogonal
regressions. For example, I do see that we should be able to regress marginal densities of SDEs out to a certain time
period on SDE parameters and terminal value of time using hermite orthogonal regressions. Not only would this require
far less computational power to train the networks, it might possibly be more accurate with hermite orthogonal
regressions but we still have to show that it can be done. I am extremely optimistic but I have not done it.

AI people should not be worried because math based AI will only be better and more powerful when combined properly with
mathematics.

---

### #1738 — Amin (Topic Author)
*March 8, 2023, 2:15 PM*

Friends, I had a phone meeting with my psychiatrist around 3:00 pm. I told him about my research and also about my
trading algorithms. I also told him about all the side-effects of antipsychotics that I had to suffer. It was a long
list of side effects. I then requested the doctor to end my medication. Doctor said that he had seen me after four
months and he wanted to be sure before taking me off medication and he could make a better decision once he could see me
in person. He said that he wanted me to visit him in person in a month or so and then he would make his decision whether
to end my drugs or continue with the same drugs. Then I requested the doctor to decrease the frequency of injections
from every 21 days to every 28 days to which doctor agreed and said that I could have half injection of fluanxol after
every 28 days.

So I am happy there was some progress and my medication decreased somewhat. I will make a plan to visit the doctor after
a month or two and then request him again to end my medication.

I am also re-starting my research and hope to come back with a new program with hermite regressions in a few days.

---

### #1739 — Amin (Topic Author)
*March 8, 2023, 9:18 PM*

Friends, people behind my persecution do not want to let go of me at all. There is a remarkable increase in persecution
activity. Especially there is pronounced increase in gas in my room and gas in the washroom. Today when I was travelling
around on my motorcycle, they continued to charge my back through microwaves in motorcycle seat (which they also
continued to do in past few days).  Now when I was trying to sleep, even though I had firmly placed a pillow on my back,
they continued to use microwaves to charge my back and cause strong itch stopping me from sleep which prompted me to
write this post. As I wrote at the start, gas in my room has remarkably increased. I can breathe in it but this
breathing is sickening and not wholesome at all as opposed to breathing in fresh air. This is despite that I keep window
of my room open at all times.

---

### #1740 — Amin (Topic Author)
*March 9, 2023, 9:20 AM*

Friends, I am trying to work with interesting examples of hermite orthogonal regressions. But I still continue to run
into some problems with earlier work. For example we have two different methods to construct Z-series of a random
variable. 1. Through fitting its first few moments.  2. Through mapping the density of random variable on standard
normal density and extracting hermite coefficients after inner product with hermite polynomials of various order.

Problem is that both of these methods do not necessarily satisfy the positivity condition associated with dXdZ > 0 all
over the density domain. When we worked with these methods, positivity condition of first derivative was not in our mind
and I only realized later that it is also important.

When I try playing with data, this problem with earlier written algorithms continue to come up again and again since
they do not ensure positivity condition of first derivative   dXdZ > 0. I want to spend next two to three days to
re-write my earlier algorithms written with both methods through fitting of moments and through extraction of hermite
coefficients and embed the positivity condition in the algorithms so that we get a nice smooth density with very good
tails that we could use in analytics everywhere. When tails of the density are not smooth we get all sort of problems in
the analytics and regressions on data are meaningless.

Quadratic case was easy and I have studied conditions associated with quartic equations to have no real root and they
are not difficult either. But I still do not know if it would be easy to find conditions for sixth order polynomial to
have no real roots. So I will surely improve the six moment Z-series fit to data  but I still do not know if I would be
able to work on eight moment Z-series fit to data or not.

I hope to come up with new and better algorithms  to construct the density in next few days and then post them on this
forum. After that I will go back to my research on applications of hermite regressions.

---

### #1741 — Amin (Topic Author)
*March 13, 2023, 2:40 AM*

Friends, I continue to ask the mind control agents, American army crooks and others to please let go of all of it and
let me work and do my research, but every day and night, they try to do everything to sabotage me. When I try to work,
they literally induce very deep sleep to not let me concentrate on my work and when I try to sleep, they make sure I do
not have a proper sleep at all. They literally stall me several times a day by forcing sleep on me and antipsychotics
and mind control drugs in the blood help them to successfully do that.

I usually do not sleep on the floor but yesterday night I had a wonderful sleep when I decided to sleep on the floor.
But yesterday, they had calibrated all their lasers and devices in anticipation that I will sleep at the floor and as a
result my sleep was extremely poor last night.

I want to tell friends that people after me are hardened criminals of this art to retard innocent people (and have been
doing it in cold blood for decades) and they have absolutely no intention to let me get off mind control. They continue
to target me with necessary mind control and when my recent research will go off limelight, they intend to make sure
that I could not do more and better research by doing everything to control my brain. Inducing hard sleeps when victim
wants to work and then causing sleep deprivation when victim wants to sleep is another tactic they are using. And they
openly threaten me that they are only waiting for my recent research to go off limelight and they would effectively take
care of me properly this time once attention of people decreases.

Problem is that most of the people behind mind control have little human empathic emotions to relate to their victims
and consider mind control a very good thing to take care of people they find offensive due to their inherent feelings of
hatred. When good people try to stop them and tell them that mind control is a bad thing, these bad actors are even more
inclined to use mind control to silence their target victims. They have no conception that it is a bad thing to force a
life of  torture on human beings and strip them of good capabilities in their brain.

Many of these bad actors understand that tens of thousands of people are on mind control only in United States and if
most of them are taken off mind control, there would be a huge outcry in United States against these bad actors for all
the damage they have caused the society and all the torture and abuse they inflicted on innocent people who simply
wanted to work hard and excel in their lives.

---

### #1742 — Amin (Topic Author)
*March 13, 2023, 9:40 PM*

Friends, we noticed that just like original simple regression is used for stochastics stochastics but can be applied to
deterministic processes, so there is a deterministic counterpart for it. Therefore we expect that such a link should
also exist for hermite orthogonal regression as well.

There is nothing special in hermite polynomials other than it is an orthogonal basis with respect to normal density.

If we can choose orthogonal/independent basis for a set of explanatory variables and variable being explained, we can
easily run a regression for each order of orthogonal/independent basis between the explanatory and explained variables
and it would be our counterpart for hermite orthogonal regression.

One way to choose independent basis that does not have to deal with densities is to use Taylor series of functions. If
we can somehow find Taylor series expansion of explanatory variables and explained variables in possibly
multidimensional independent basis, we can run a regression between variables for each order of independent basis to
find the relationship that exists between the explanatory variable and explained variable.

However What is important is approximate numerical construction of Taylor series since we may not know know derivatives
of statistical/deterministic functions found from data everywhere to find the coefficients of various Taylor independent
basis.

I believe that regressions between Taylor series basis of similar order with one regression for each order would be the
deterministic counterpart for hermite orthogonal regression framework. Though other deterministic methods based on
orthogonality and independence might also be used, regressions between Taylor series basis of each order is possibly the
strongest contender for being a universal counterpart for hermite orthogonal regressions in deterministic setting.

Though like most other friends, I have used transforms in derivative pricing, I am not a great expert at transforms but
I think that independent basis could also be found through order of transform powers for doing regressions.

---

### #1743 — Amin (Topic Author)
*March 14, 2023, 2:41 PM*

Friends, I continued to think about yesterday's ideas and seem to possibly have more insight about using Taylor series
for orthogonal regressions. But still this is non-tested theory and I might be totally off and therefore I want to
request friends to pardon any possible mistakes in my exposition.

In deterministic setting, if we want to do an orthogonal regression between explanatory variables and explained
variable, we first have to choose an appropriate base function into which we will Taylor-expand our variables.
(Non-linearity of a variable is with respect to another variable that is related through a non-linear function. However
non-linear a variable with respect to some other variable, it is perfectly linear on its own axis and obviously cannot
be taylor-expanded onto itself.) So first we have to find an appropriate base function with respect to which we will
Taylor-expand explained and explanatory variables. In our orthogonal stochastic hermite regressions, the base variable
was a standard gaussian into which we expanded explained and explanatory variables.

To keep things simple, we suppose that we are orthogonal-Taylor-regressing one explained variable Y on one explanatory
variable X. Suppose we choose base function as$ \, f(u)\, = \, {u}^{\frac{1}{4}} \, $ . Again, there can be many
possible choices of base functions that can even possibly be better but we are giving this one-fourth power as one
possible base function.

We want to orthogonal-Taylor-Regress Y on X.   Using the base function mentioned above, we have

$ \, W \, = \, {X}^{\frac{1}{4}} \, $   meaning  $\, X \, = \, W^4 \, $

and

$ \, V \, = \, {Y}^{\frac{1}{4}} \, $   meaning  $\, Y \, = \, V^4 \, $

W is base variable for X while V is base variable for Y. In our hermite-orthogonal-regressions independent Z's were base
variables.

We Taylor-expand X in its base variable W and we also Taylor-expand Y in its base variable V as   (around appropriate
series centre points. We would have to work these things out where to place center points of series. These centre points
corresponded to medians in our Z-series for hermite-orthogonal-regressions.)

following our previous equation$\, X \, = \, W^4 \, $ , we taylor expand around appropriate expansion point$W_0(X_0) $
as

$X \, = \, W_0 \, + \, 4 \, {W_0}^3 \, (W \, - \, W_0) \, + 1/2 \,*\, 12 \, {W_0}^2 \, {(W \, - \, W_0)}^2+ 1/6 \,*\, 24 \, {W_0} \, {(W \, - \, W_0)}^3+ 1/24 \,*\, 24  \, {(W \, - \, W_0)}^4 $

which can be sucintly written as

$X \, = \, b_0 \, + \, b_1 \, (W \, - \, W_0) \, + b_2\, {(W \, - \, W_0)}^2+ b_3 \, {(W \, - \, W_0)}^3+ b_4  \, {(W \, - \, W_0)}^4 $

Similarly, following above steps again, we can Taylor-expand Y in terms of V as

$Y \, = \, c_0 \, + \, c_1 \, (V \, - \, V_0) \, + c_2\, {(V \, - \, V_0)}^2+ c_3 \, {(V \, - \, V_0)}^3+ c_4  \, {(V \, - \, V_0)}^4 $

Please notice the similarity of Taylor-expansions of X and Y with our previous Z-series expansions.

Now to set up the regression, we would have to convert X and Y data points into W and V data points as we had to do in
the inversion of Z-series. Our final data before regression would be in terms of W and V variables (as opposed to Z1 and
Z2 in case of hermite Z-series orthogonal regressions)

Now, in order to regress Y on X,  we can simply do four regressions, with each regression between appropriate expansion
powers. These regressions would be between (just like we have to take into account covariances, we would have to take
into account coefficients on each of these pairs mentioned below)

$(V \, - \, V_0)$  and  $(W \, - \, W_0)$

${(V \, - \, V_0)}^2$  and  ${(W \, - \, W_0)}^2$

${(V \, - \, V_0)}^3$  and  ${(W \, - \, W_0)}^3$

${(V \, - \, V_0)}^4$  and  ${(W \, - \, W_0)}^4$

There will be four pairs of orthogonal regressions since the base function we chose allowed for expansion up to fourth
power only. Some Other base functions could possibly do better. But these details we will continue to know in coming
weeks and months. We could combine the results from above orthogonal regressions to come up with one estimator for the
explained variable.)

Friends above is my brief plan of attack for orthogonal Taylor regressions but I might have made some mistakes or
something might possibly be wrong so please pardon any mistakes.

I will try to come up with a Taylor orthogonal regression program in next 3-4 days.

As I see, if we take deterministic functions without any noise in data, and do above steps appropriately by choosing an
appropriate expansion point and other things right, we might possibly get a fourth order accurate result from this
regression if the data is from deterministic functions without noise.

---

### #1744 — Amin (Topic Author)
*March 15, 2023, 5:11 AM*

Friends, my hp pavilion  laptop has some problem. small light on start button, blinks but laptop does not start. I am
trying to get it fixed but it can cause delay in my mat lab programs.

---

### #1745 — Amin (Topic Author)
*March 15, 2023, 4:25 PM*

I have left my laptop at a repair shop. They tried to fiind the problem  with the laptop over the day. Repair guy says
that possibly the problem is with the processor. He will first try to replace IT chip of processor and see if the laptop
works. But he said that he was reasonably confident that he could get the laptop working and ready in another day. Let
us see how it goes. I was not able to do any work today.

---

### #1746 — Amin (Topic Author)
*March 16, 2023, 3:53 AM*

friends, so sorry that I do not have my laptop on me and I cannot run my experiments.

First things I want to see are how some regressions go.

It is quite obvious that we could Taylor regress polynomial functions of same order.

what I really want to see using my laptop is how it goes with regressions between polynomial functions of different
order.

Please keep in mind that hermits regressions we did were between polynomials of same order in Z

I hopeI can get my lworking laptop today so I can play around with these ideas.

Even if it does not work well for polynomials of different order, I will like to see what can possibly be done to make
them work.

---

### #1747 — Amin (Topic Author)
*March 16, 2023, 6:37 PM*

Friends, I could not get my computer even today. Computer repair shop seems evasive about when they could fix my laptop.
I am worried that mind control agencies have asked the repair people to delay as much as possible and later tell me that
my computer could not be repaired.

I continued to brainstorm today and had some of the most exciting ideas but I need my laptop to execute them.

---

### #1748 — Amin (Topic Author)
*March 17, 2023, 7:25 AM*

Friends, laptop repair shop have told me that it seems difficult to get my laptop to work but they would be sure by 5:00
PM today.

It seems that they gave me this time since banks would be closed on weekend.

I will go to bank to withdraw cash in case I have to buy a new motherboard for my laptop tomorrow. If things go well and
mind control agencies did not create any more problems. I will start working tomorrow in the evening.

I have some really interesting ideas that I want to test on my computer so let us see how it goes.

---

### #1749 — Amin (Topic Author)
*March 17, 2023, 7:54 AM*

I am seriously afraid that mind control agencies will force the repair shop to create more problems in my laptop so I
would not be able to work steadily even after it. These crooks are desperate to create any obstacles in my research they
can. Please protest to mind control crooks to not create problems in my research.

---

### #1750 — Amin (Topic Author)
*March 19, 2023, 5:34 PM*

Friends, I bought a used laptop from the computer market of Hafeez Center in Lahore. I installed different programs in
it yesterday. And started working just a little bit ago today. I have started playing with the idea of regressions in a
Taylor independent basis setting. I hope to come back with some results pretty soon. Let us see how it goes.

---

[← Previous](page_034.md) | [Index](index.md) | [Next →](page_036.md)
