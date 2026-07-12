# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 50 of 59** — Posts #2451–#2500

[← Previous](page_049.md) | [Index](index.md) | [Next →](page_051.md)

---

### #2451 — Amin (Topic Author)
*September 20, 2024, 7:12 PM*

Friends, I have been able to write a reasonably good program about the problem discussed in previous few posts. I will
be posting the program tomorrow or on Sunday after writing explanatory comments and after cleaning up the code.

---

### #2452 — Amin (Topic Author)
*September 21, 2024, 5:01 PM*

Friends, in the context of previous few posts, we know that we could represent conditional distribution of Y as

\begin{align}\label{4.6.11}

 & Y\, | \, X=\, E\left[Y|X \right]+\,\, \sigma(X(Z_{X_p})) \, W  \\

 &=\mu_Y+\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \, ch_n \, H_n(Z_X)+\,\, \left[ \sum\limits_{n=0}^{N}\, dh_n \,
H_n(Z_{X_p}) \right] \, \left[\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W)\right]

 \end{align}

where

\begin{equation}

 \sigma(X(Z_{X_p}))\,=\,\sum\limits_{n=0}^{N}\, dh_n \, H_n(Z_X)

\end{equation}

but we know in the context of SDEs that usually

\begin{equation}

 \sigma(X)\,=\,X^{\gamma}

\end{equation}

meaning that function, that appears as a multiplier of zero mean noise W, is usually a power of the SDE variable at an
earlier step. Sometimes, in stochastic volatility setting, we have two functions, one of asset variable and other of
volatility, both of which appear as a multiplier of noise W. This stochastic volatility setting can usually be written
as

\begin{equation}

 \sigma(X,V)\,=\,X^{\gamma_X}\,\, V^{\gamma_V}

\end{equation}

and our equation of the conditional expectation is given as

\begin{align}

 & Y\, | \, (X ,  V)=\, E\left[Y|\left(X,V\right) \right]+\,\, \sigma(X(Z_{X_p}),V(Z_{V_p})) \, W  \\

 &=\mu_Y\,+\,\sum\limits_{n=1}^{N}\, \boldsymbol{{x_n}^T \, Var_{{X},n}^{-1} \,cov_{\boldsymbol{XY},n} }\,+\,\, \left[
\sum\limits_{n=0}^{N}\, dh_n \, H_n(Z_{X_p}) \right] \, \, \left[ \sum\limits_{k=0}^{K}\, gh_n \, H_n(Z_{X_v}) \right]
\, \left[\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W)\right]

 \end{align}

I made another observation that R_squared was not changing smoothly as I changed the function of X (or volatility) in
the volatility term.

So there are two important observations. First is that usually there is just one parameter of importance when we
encounter SDE like evolution of uncertainty and this parameter is the power of SDE variable, somthing we have
represented as gamma in above equations. Second observation was that R-squared did not change smoothly as we changed
gamma. We also notice that gamma is usually between zero and one most of the times in applications of SDEs.

So I made a grid of gamma with hundred grid points ranging from .01, .02, .03, ...,1.0   . I calculated R-squared on
this grid and chose the value of gamma where R-squared was maximum. I also noticed that in close neighborhood of maximum
R_squared (R-Squared>.995) , R-Squared changes very smoothly but after R_squared  decrease below .9, it can change very
abruptly and can all of a sudden go to -25 and then go to .7 and something like that. But good thing was that close to
maximum R-squared on the grid, R-squared changed extremely smoothly for many many entries.

So this way I was able to make a grid for gamma and then find the value of gamma associated with maximum R-squared. I
also noticed that several times, there were two local maxima for R-squared one of which would have gamma smaller than .5
while another local maxima would take place somewhere when gamma was greater than .5

Then I made a two dimensional grid of 40X 40 =1600 values of gammaX and gammaV for and changed  each of them by .025.
And again this also worked very well and I was able to find a good two dimensional maximum for R-squared where all
densities were very good and smooth and density of noise was also very smooth. I simply picked the value of gammaX and
gammaV where R-squared was maximized on two dimensional grid.

Due to multi-modal values of R-squared, it would be important for friends to choose a value of maximum R-squared that
theoretically seem as better fit based on analytics and experience.

But many times there would be several parameters instead of just one parameter associated with a function. And it could
be possible to do a large spaced grid optimization for function parameters to four or possibly five dimension but not
beyond that.

The method is simple and I would try to post the associated matlab program tomorrow.

Also in my program, I took stochastic SDE variable data at one year as X and at two years or three years as Y and tried
to explain Y given X.

---

### #2453 — Amin (Topic Author)
*September 26, 2024, 5:21 PM*

Friends, sorry for staying away for so many days. I have been under immense pressure to make some money and become more
independent. That is why I had to totally stop my research on probability theory and concentrate on practical algorithms
that I can use to make money possibly by trading crypto. The good news is that I have been able to work out an algorithm
that trades after ten minutes on average and is great with making money. When trade life is roughly ten minutes, one
does not need to be so precisely accurate in execution and latency as one has to be when average trade life is thirty
seconds as I had in my previous trading algorithms.  I have already done most of the mathematical work and now I have to
write a computer program in python for automated trading using binance's own python API. Earlier I have some not so good
experience with another third party free python API since it was not being updated regularly to remain in sync with
changes and updates in official Binance input/output user commands. So I have to do some extra work to learn this
different API that is kept updated by Binance itself. It can take another two weeks to complete all of this programming
but I am really desperate to come back to research in probability theory again like I have been doing for several years.
Weather is still very warm and humid in Lahore but it is supposed to really change for much better weather in next two
weeks. So I hope that I will really enjoy working again with probability theory research. I also want to keep thinking
about exact solution of Schordinger equation and do more literature reading to get better oriented with the problem and
also keep brainstorming about the problem. Unlike last time, I want to start hands on research on Schordinger equation
only when I think I have thought of some good ideas to solve the equation.

As I am working with trading algorithms, I continue to think that it is rather restrictive for mathematicians to keep
thinking of clever algorithms to make money in the vanilla financial markets and I really cannot wait to go back to
broader research in probability theory.

So I hope that I would be back to previous research format within a few weeks after I have written a python program for
trading on Binance with the new algorithm. I really hope that we would do some interesting research this winters.

---

### #2454 — Amin (Topic Author)
*September 30, 2024, 9:19 AM*

Friends, I have to arrange for a different computer and install programs on that for algorithmic trading with crypto
currencies and that can take a little while so I decided to re-start the work on my research until the other computer
gets ready.

I have been thinking about optimization/root-search of parameters of functions/equations of the type we encountered in
fitting moments to Z-series by multi-dimensional root-search on coefficients of Z-series. I really do not know whether
it would be a success or not but I have a few ideas that I really want to try. I want to break N dimensional
optimization/root-search method into one N-1 dimensional method and another one dimensional method. For example, let us
suppose we want to calibrate coefficients to seventh power of Z in a Z-series and suppose we have calibrated first three
equations of mean, second moment and third moment to three coefficients (c_0, c_1 and c_2). Now I want to add the fourth
moment equation to coefficients calibration and simultaneously introduce c_3 in the calibration.  I start with a c_3
value of zero and perturb it slowly in the direction of decreasing objective function but I have to simultaneously keep
the earlier calibrated coefficients in calibration while perturbing c_3 and I do that again with some numerical method.
So first three coefficients are kept in calibration while the fourth is altered in the direction on minimization of
objective function. And after c_3 is also calibrated we increase the dimensionality of the problem and include a fifth
moment equation along with c_4 in our optimization.

If it works well, it can be an interesting optimization/root-search algorithm and can have numerous uses. I was really
thinking of solving one-electron Schordinger equation and then introducing a second electron and optimize for second
electron on our basis functions while keeping first electron in calibration. And then keep on adding more electrons
while keeping earlier ones to perfectly solve the schordinger equation. I will have to work out complete details for
optimization on schordinger equation later but first I want to solve for moments and try to find out if the method is
good and works well in practice. I hope to come back with matlab code in a few days.

---

### #2455 — Amin (Topic Author)
*October 2, 2024, 2:32 PM*

Friends, here is the code for my new optimization program that fits Z-series to eight moments according to ideas and
algorithm described in previous post. I will make a detailed post about analytics later but I am posting the code.

.

.

```
function [] = FindZSeriesCoeffsFromMomentsNewOptimization(rMu)

%rMu are first eight raw moments of a random variable input to this program
%to find associated Z-series. Please comment the moments below if you input
%your own moments to the program. You can first run with moments below to
%become familiar with the program. The current program works only for eight
%moments but you can easily alter it to make it work for ten or twelve
%moments after understanding it.

rMu(1)=0.000012499863483*10^5;
rMu(2)=0.000021197093700*10^5;
rMu(3)=0.000050274347857*10^5;
rMu(4)=0.000171368317209*10^5;
rMu(5)=0.000856094970826*10^5;
rMu(6)=0.006320436615909*10^5;
rMu(7)=0.068698344472325*10^5;
rMu(8)=1.084082326087001*10^5;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Moments Standardization block

SeriesOrder=7;    %Z-series till 7th power.
mOrder=8;         %Number of raw moments in calibration.
NMoments=mOrder;
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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%First Optimization.
%The next function finds c2 and c3 so that third and fourth moments are
%calibrated. It keeps first and second moments in calibration.

[c0,c] = OptimizeIterativeMoments3And4(sMu);

%The next function is complete Newton root-search in four parameters c0,c1,c2 and c3
%making sure that any slack in four dimension optimization is removed.

SeriesOrder0=3;
NMoments0=4;
[c0,c] = FinalmultiNewtonRootSearch(sMu,c0,c,SeriesOrder0,NMoments0);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%In this block c4 and c5 are found so that fifth and sixth moments are calibrated.
%While c4 and c5 are calibrated by iteratively altering them, it is made
%sure that c0,c1,c2 and c3 remain in calibration to first four moments and
%this is insured by embedded Newton root search. When we alter c4 or c5,
%the calibration of first four moments to first four coefficients goes out
%of sync but our iterative step size to alter c4 or c5 is very small so we
%can easily bring c0,c1,c2 and c3 in sync with first four moments by two or
%three iterations of Newton root search.
SeriesOrder0=5;
NMoments0=6;
[c0,c] = OptimizeIterativeMomentsPairsGreaterThan4(sMu,c0,c,SeriesOrder0,NMoments0);

%The next function is complete Newton root-search in six parameters
%c0,c1,c2,c3,c4 and c5
%making sure that any slack in six dimensional optimization is removed.

[c0,c] = FinalmultiNewtonRootSearch(sMu,c0,c,SeriesOrder0,NMoments0);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%In this block c7 and c6 are found so that seventh and eighth moments are calibrated.
%While c6 and c7 are calibrated by iteratively altering them, it is made
%sure that c0,c1,c2,c3,c4 and c5 remain in calibration to first six moments and
%this is insured by embedded Newton root search. When we alter c6 or c7,
%the calibration of first six moments to first six coefficients goes out
%of sync but our iterative step size to alter c6 or c7 is very small so we
%can easily bring c0,c1,c2,c3,c4,c5  in sync with first six moments by two or
%three iterations of Newton root search.

SeriesOrder0=7;
NMoments0=8;
[c0,c] = OptimizeIterativeMomentsPairsGreaterThan4(sMu,c0,c,SeriesOrder0,NMoments0);

%The next function is complete Newton root-search in eight parameters
%c0,c1,c2,c3,c4,c5,c6 and c7
%making sure that any slack in eight dimensional optimization is removed.

[c0,c] = FinalmultiNewtonRootSearch(sMu,c0,c,SeriesOrder0,NMoments0);

%If you want to find moments up to tenth order, you will have to add another such block.
%If you want to find moments up to twelfth order, you will have to add two
%such new blocks. But none of the Newton root search engines is written for moments
%beyond tenth moments so you would have to slightly alter them to enable
%higher moments.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Make sure you do not comment the lines below

c0=c0*sqrt(cMu(2)); %convert from standardized to central moments
c=c*sqrt(cMu(2));   %convert from standardized to central moments

c0=c0+Mu1;          %convert from central to raw moments by adding mean.

[FittedMoments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Please Uncomment this if you want to see a comparison of input moments and
%fitted moments
rMu
FittedMoments
%str=input('Look at comparison of fitted moments with input moments');
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
for nn=1:7
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
function [c0,c] = OptimizeIterativeMoments3And4(sMu)

SeriesOrder=3;
NMoments=4;
mOrder=NMoments;
c0=0;
c(1)=1;
c(2:SeriesOrder)=0;
c(SeriesOrder+1:7)=0;
w(NMoments)=1;
for nn=NMoments-1:-1:1
    w(nn)=1;%w(nn+1)*(nn+1).^2;
end

%%%%%%Choose the iteration step size.
for nn=2:SeriesOrder
    DeltaX(nn)=.00125/(factorial(nn));
end

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

[ObjFuncBest] = CalculateObjMoment(sMu,Moments,w,mOrder);

cBest=c;

ImproveFlag(1:SeriesOrder)=1;
ImproveFlagPrev(1:SeriesOrder)=0;
ImproveCount(1:SeriesOrder)=0;

mm=0;
while (DeltaX(SeriesOrder) > 10^(-5) )
    mm=mm+1;
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
function [ObjMomentOut] = CalculateObjMoment(Moment0,Moment,w,MOrder)

ObjMomentOut=0;
for nn=1:MOrder
    ObjMomentOut=ObjMomentOut+(Moment(nn)-Moment0(nn)).^2.*w(nn);
end

end

```

.

.

.

```
function [c0,c] = FinalmultiNewtonRootSearch(sMu,c0,c,SeriesOrder,NMoments)
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here
w(NMoments)=1;
for nn=NMoments-1:-1:1
    w(nn)=w(nn+1)*(nn+1).^2;
end

mOrder=NMoments;

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);
cBest=c;
[ObjFuncBest] = CalculateObjMoment(sMu,Moments,w,mOrder);

for qq=1:50
        %SeriesOrder=7;
        %NMoments=8;

        c0=-(c(2)+3*c(4)+15*c(6));
        %[F,dF]=KeepInCalibrationByNewtonRootSearch(sMu,c0,c,SeriesOrder1,SeriesOrder2,NMoments1,NMoments2);
        [F,dF] = CalculateMomentsAndDerivatives_0(sMu,c0,c,SeriesOrder,SeriesOrder,NMoments);

        da(1,1)=c0;
        da(2:SeriesOrder+1,1)=c(1:SeriesOrder);
        da=da-(dF\F);
        c0=da(1,1);
        c(1:SeriesOrder)=da(2:SeriesOrder+1,1);
        [Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

        [ObjFunc] = CalculateObjMoment(sMu,Moments,w,mOrder);

        if(ObjFunc<ObjFuncBest)

            ObjFuncBest=ObjFunc;

            cBest=c;

            %ImproveFlag(nn)=1;

        end
end

        c=cBest;
        c0=-(c(2)+3*c(4)+15*c(6));
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
if((NMoments==7)||(NMoments==8))
a0=-(a(2)+3*a(4)+15*a(6));% ---1
end
% if(NMoments==6)
% a0=-(a(2)+3*a(4));% ---1
% end

if((NMoments==6)||(NMoments==7))
a0=-(a(2)+3*a(4));% ---1
end

if((NMoments==3)||(NMoments==4))
a0=-(a(2));% ---1
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

if(NMoments>=3)
u3=EXZ(4,1);
end

%NMoments
if(NMoments>=4)
u4=EXZ(5,1);
end

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

 if(NMoments>=3)

 du3(1)=3*EXZ(3,1);

 end

 if(NMoments>=4)
 du4(1)=4*EXZ(4,1);
 end

%du1(1)=1;%----2
%du2(1)=0;
%du3(1)=0;
%du4(1)=0;

for mm=2:SeriesOrder+1
du1(mm)=EXZ(1,mm);
du2(mm)=2*EXZ(2,mm);
if(NMoments>=3)

du3(mm)=3*EXZ(3,mm);
end
if(NMoments>=4)

du4(mm)=4*EXZ(4,mm);
end
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
 if(NMoments>=4)
 F(4,1)=u4-Ms(4);
 end
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

        if(NMoments>=4)
        dF(4,mm)=du4(mm);
        end

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

.

```
function [F,dF] = KeepInCalibrationByNewtonRootSearch(Ms,a0,a,SeriesOrder1,SeriesOrder2,NMoments1,NMoments2)

%This function finds Newton root search derivatives matrix and related
%vector. In this function for example SeriesOrder2 can be 5 or 7(or more)
%while SeriesOrder1 would be 3 or 5. Similalry NMoments2 would be six or
%eight(or more) while NMoments1 would be four or six. When SeriesOrder2 is
%for example five, it means that there are up to a5 (a0,a1,a2,a3,a4,a5) non-zero
%coefficients in Z-series however only coefficients equal to SeriesOrder1
%(which would be a0,a1,a2,a3 in this case)
%would be altered by Newton root search to keep them in calibration. in
%calibration a4, and a5 are taken as given but they are not adjusted in
%calibration and only a0,a1,a2,a3 are altered to keep them in calibration
%with first four moments.
%Similalry when SeriesOrder2 would be seven, and SeriesOrder1 would be
%five, Newton root search would be done only on (a0,a1,a2,a3,a4,a5) to keep
%them in calibration to first six moments but values of a6 and a7 would be
%taken as given but they will not be included in the derivatives matrix but
%they will be taken as given in calculation of moments and their
%derivatives required for root search upto a5 (a0,a1,a2,a3,a4,a5).

NZterms=SeriesOrder2;

%aa0=a0;
if(NMoments2>8)
a0=-(a(2)+3*a(4)+15*a(6)+105*a(8));% ---1
end
if((NMoments2==7)||(NMoments2==8))
a0=-(a(2)+3*a(4)+15*a(6));% ---1
end
% if(NMoments==6)
% a0=-(a(2)+3*a(4));% ---1
% end

if((NMoments2==6)||(NMoments2==7))
a0=-(a(2)+3*a(4));% ---1
end

if((NMoments2==3)||(NMoments2==4))
a0=-(a(2));% ---1
end

EZ(1)=0;
EZ(2)=1;
for nn=3:NMoments2*SeriesOrder2+NZterms+2
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

a(SeriesOrder2+1:NMoments1*SeriesOrder2+1)=0;
b0=a0;
b=a;

for mm=1:NMoments1
    if(mm>1)
        [b0,b] =SeriesProduct(a0,a,b0,b,SeriesOrder2*mm);
        b(SeriesOrder2*mm+1:NMoments1*SeriesOrder2+1)=0;
    end
   % b0
   % b
%str=input('Look at numbers')
    EXZ(mm+1,1)=b0;
    for pp2=1:SeriesOrder2*mm

            EXZ(mm+1,1)=EXZ(mm+1,1)+b(pp2).*EZ(pp2);
    end
    for pp1=1:NZterms
        EXZ(mm+1,pp1+1)=b0.*EZ(pp1);
        for pp2=1:SeriesOrder2*mm

            EXZ(mm+1,pp1+1)=EXZ(mm+1,pp1+1)+b(pp2).*EZ(pp2+pp1);
        end
    end
end

%u1=EXZ(2,1);
u2=EXZ(3,1);

if(NMoments1>=3)
u3=EXZ(4,1);
end

%NMoments1
if(NMoments1>=4)
u4=EXZ(5,1);
end

u1=a0+a(2);
if(SeriesOrder2>=4)
u1=a0+a(2)+3*a(4);
end
if(SeriesOrder2>=6)
u1=u1+15*a(6);
end
if(SeriesOrder2>=8)
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

 if(NMoments1>=3)

 du3(1)=3*EXZ(3,1);

 end

 if(NMoments1>=4)
 du4(1)=4*EXZ(4,1);
 end

%du1(1)=1;%----2
%du2(1)=0;
%du3(1)=0;
%du4(1)=0;

for mm=2:SeriesOrder1+1
du1(mm)=EXZ(1,mm);
du2(mm)=2*EXZ(2,mm);
if(NMoments1>=3)

du3(mm)=3*EXZ(3,mm);
end
if(NMoments1>=4)

du4(mm)=4*EXZ(4,mm);
end
end

if(NMoments1>=5)
u5=EXZ(6,1);

%du5(1)=5*EXZ(5,1);

for mm=1:SeriesOrder1+1
du5(mm)=5*EXZ(5,mm);
end

end

if(NMoments1>=6)
u6=EXZ(7,1);
%du6(1)=0;

for mm=1:SeriesOrder1+1
du6(mm)=6*EXZ(6,mm);
end

end

if(NMoments1>=7)
u7=EXZ(8,1);
%str=input('Look at k7 and k71')

%du7(1)=0;

for mm=1:SeriesOrder1+1
du7(mm)=7*EXZ(7,mm);
end

end
if(NMoments1>=8)

u8=EXZ(9,1);
for mm=1:SeriesOrder1+1
du8(mm)=8*EXZ(8,mm);
end

end

if(NMoments1>=9)

u9=EXZ(10,1);
for mm=1:SeriesOrder1+1
du9(mm)=9*EXZ(9,mm);
end

end
if(NMoments1>=10)

u10=EXZ(11,1);
for mm=1:SeriesOrder1+1
du10(mm)=10*EXZ(10,mm);
end

end

 F(1,1)=u1-Ms(1);
 F(2,1)=u2-Ms(2);
 F(3,1)=u3-Ms(3);
 if(NMoments1>=4)
 F(4,1)=u4-Ms(4);
 end
 if(NMoments1>=5)
 F(5,1)=u5-Ms(5);
 end
 if(NMoments1>=6)
 F(6,1)=u6-Ms(6);
 end
 if(NMoments1>=7)
 F(7,1)=u7-Ms(7);
 end
 if(NMoments1>=8)
 F(8,1)=u8-Ms(8);
 end
 if(NMoments1>=9)
 F(9,1)=u9-Ms(9);
 end
 if(NMoments1>=10)
 F(10,1)=u10-Ms(10);
 end

      for mm=1:SeriesOrder1+1
        dF(1,mm)=du1(mm);
        dF(2,mm)=du2(mm);
        dF(3,mm)=du3(mm);

        if(NMoments1>=4)
        dF(4,mm)=du4(mm);
        end

        if(NMoments1>=5)
            dF(5,mm)=du5(mm);
        end

        if(NMoments1>=6)
        dF(6,mm)=du6(mm);
        end
        if(NMoments1>=7)
        dF(7,mm)=du7(mm);
        end
        if(NMoments1>=8)
        dF(8,mm)=du8(mm);
        end
        if(NMoments1>=9)
        dF(9,mm)=du9(mm);
        end
        if(NMoments1>=10)
        dF(10,mm)=du10(mm);
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
function [c0,c] = OptimizeIterativeMomentsPairsGreaterThan4(sMu,c0,c,SeriesOrder,NMoments)

mOrder=NMoments;

c(SeriesOrder+1:7)=0;
w(NMoments)=1;
for nn=NMoments-1:-1:1
    w(nn)=w(nn+1)*(nn+1).^2;
end

%%%%%%Choose the iteration step size.
for nn=SeriesOrder-1:SeriesOrder
    DeltaX(nn)=.00125/2/(factorial(nn));
end

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

[ObjFuncBest] = CalculateObjMoment(sMu,Moments,w,mOrder);

cBest=c;

ImproveFlag(1:SeriesOrder)=1;
ImproveFlagPrev(1:SeriesOrder)=0;

mm=0;
while (DeltaX(SeriesOrder) > 10^(-7))
    mm=mm+1;
    %We only iteratively alter c(2:7), first and second moments are
    %retrieved automatically in our set up
    for nn=SeriesOrder-1:SeriesOrder

        ImproveFlagPrev(nn)=ImproveFlag(nn);

        cin=c;
        cin(nn)=cin(nn)+DeltaX(nn);

        %After altering the above coefficient, we do a Newton root search
        %in smaller coefficients so that they remain in calibration to
        %respective first few moments.

        for qq=1:5
        SeriesOrder1=SeriesOrder-2;
        SeriesOrder2=SeriesOrder;
        NMoments1=NMoments-2;
        NMoments2=NMoments;
        c0in=-(cin(2)+3*cin(4)+15*cin(6));
        [F,dF]=KeepInCalibrationByNewtonRootSearch(sMu,c0in,cin,SeriesOrder1,SeriesOrder2,NMoments1,NMoments2);

        da(1,1)=c0in;
        da(2:SeriesOrder1+1,1)=cin(1:SeriesOrder1);
        da=da-(dF\F);
        c0in=da(1,1);
        cin(1:SeriesOrder1)=da(2:SeriesOrder1+1,1);
        end

        %We find the objective function after changing a coefficient
        %only after we have done Newton root search analytics to alter the
        %smaller coefficients keeping them in calibration. Goodness of
        %objective function to accept a move is is evaluated only after
        %all of the above analytics. In other words objective function is
        %evaluated after altering a coefficients and doing analytics to keep smaller
        %coefficients in calibration and only after that we evaluate the
        %objective function.

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
            for qq=1:3
                SeriesOrder1=SeriesOrder-2;
                SeriesOrder2=SeriesOrder;
                NMoments1=NMoments-2;
                NMoments2=NMoments;
                c0in=-(cin(2)+3*cin(4)+15*cin(6));
                [F,dF]=KeepInCalibrationByNewtonRootSearch(sMu,c0in,cin,SeriesOrder1,SeriesOrder2,NMoments1,NMoments2);
                %c0in=-(cin(2)+3*cin(4)+15*cin(6));
                da(1,1)=c0in;
                da(2:SeriesOrder1+1,1)=cin(1:SeriesOrder1);
                da=da-(dF\F);
                c0in=da(1,1);
                cin(1:SeriesOrder1)=da(2:SeriesOrder1+1,1);
            end

            cin(1:SeriesOrder-2)=da(2:SeriesOrder-2+1,1);

            c0in=-(cin(2)+3*cin(4)+15*cin(6));
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

    end

    if(rem(mm,20)==0)
    mm
    ObjFuncBest
    DeltaX

    end

    ImproveFlag0=0;
    for nn=SeriesOrder-1:SeriesOrder
       if(ImproveFlag(nn)==1)
           ImproveFlag0=1;
       end
    end
    for nn=SeriesOrder-1:SeriesOrder
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

end

```

.

.

.

When you run the program, you will see the following final input.

Moments =

   1.0e+05 *

  Columns 1 through 3

   0.000000000000000   0.000010000000000   0.000023672884921

  Columns 4 through 6

   0.000146459814703   0.001202097792368   0.014666815921047

  Columns 7 through 8

   0.255416635816729   6.248458780626995

sMu =

   1.0e+05 *

  Columns 1 through 3

                   0   0.000010000000000   0.000023672884921

  Columns 4 through 6

   0.000146459814703   0.001202097792368   0.014666815921047

  Columns 7 through 8

   0.255435558162736   6.248806451226628

Look at comparison of Standardised model moments and Standardized target moments

str =

     []

rMu =

   1.0e+05 *

  Columns 1 through 3

   0.000012499863483   0.000021197093700   0.000050274347857

  Columns 4 through 6

   0.000171368317209   0.000856094970826   0.006320436615909

  Columns 7 through 8

   0.068698344472325   1.084082326087001

FittedMoments =

   1.0e+05 *

  Columns 1 through 3

   0.000012499863483   0.000021197093700   0.000050274347857

  Columns 4 through 6

   0.000171368317209   0.000856094970826   0.006320436615909

  Columns 7 through 8

   0.068698344472325   1.084082326087001

and you will see the following graph.

[![Image](../images/i.postimg.cc/Xv4FKkXt/Graph-New-Optimization01.png)](https://postimg.cc/219VrvQx)

---

### #2456 — Amin (Topic Author)
*October 3, 2024, 5:58 PM*

Friends, logic of the above program is very simple.

First I do an iterative optimization of third and fourth moment by perturbing the coefficients c2 and c3 in the
direction of decreasing objective function. We first perturb c2 in one direction and then divide all the first four
coefficients by resulting second moment to make sure that second moment of standardized moments remains one. We also
alter co to make sure that mean remains zero. By division with second moment and adjusting c0, we make sure that once c3
is perturbed, first two moments remain calibrated. And only after above two adjustments, that we evaluate the objective
function for change in c2 and accept the change if objective function decreases after all of the above changes.
similarly for perturbations in c3.

Even if there is any slight slack in calibration of first four coefficients, we are extremely close to true values and a
few iterations of multidimensional Newton root search fixes any defect.

Then we perturb c4 and c5 starting from zero on top of earlier four dimensional calibration. Please note that our
perturbation step size is very small. After perturbing c4, we make a few iterations of multidimensional root search on
first four coefficients while taking c4 and c5 as given. Even though c4 and c5 are included in all moment calculations
at their given values, only first four coefficients are updated by multidimensional Newton to keep satisfying first four
moments hence keeping them calibrated. This multidimensional Newton almost always works since after small perturbation
in c4 or c5, we are still in very close neighbourhood of earlier solution and still firmly in catchment of Newton
method. This is also computationally very cheap. We evaluate objective function to accept the move in c4 only after
multidimensional Newton update on first four coefficients. And updates in the  values of first four coefficients are
also included in calculation of the objective function. We accept the move in c4 if objective function decreases after
all of the above changes. Similarly for c5.

We do a few passes of six dimensional Newton method to make sure if there is any slight slack in calibration, it is
improved.

Then we perturb c6 and c7 that were originally zero to values away from zero. It is just analogous to what we did for c4
and c5. After perturbing c6 by a small step, we use multidimensional Newton method to keep first six moments calibrated.
In these Newton calculations of first six derivatives, c6 and c7 are taken as constants and only first six coefficients
c0-c5 are updated making sure that first six moments remain calibrated despite small move in c6 or c7. And then we
evaluate the objective function that includes change in c6 or c7 and all the newton updated values of c0-c5. And if
objective function improves, we accept the perturbation change in c6 or c7,

At the end, We do a few passes of eight dimensional Newton method to make sure if there is any slight slack in
calibration, it is improved.

I did optimization on pairs of coefficients since it might have been difficult to fit skew without fitting kurtosis
while keeping variance unity and similar of all pairs of odd and even moments.

---

### #2457 — Amin (Topic Author)
*October 3, 2024, 7:11 PM*

Friends, when we started working with Z-series, we had aimed that we might possibly be able to do many things, that We
were doing with AI, with solid mathematics. And I believe that now we have enough understanding of Z-series and related
methods that we should start doing many of those things, that are done with AI,  now instead with Z-series and related
methods.

In order to be able to do that, I will be bold and try to solve particular classes of SDEs simultaneously with Z-series
just like they do with AI. I really hope that with success of this example, many friends will take on large number of
problems that are being tackled with AI and solve them with solid mathematics of Z-series or U-series very easily.

Let us consider a simple mean reverting SDE:

\begin{align}

& dY_t\,=\, \kappa \, (\theta \, -\, Y_t\,)\, dt\,+ \sigma \, {Y_t}^{\gamma} \, dZ(t) \\

& Y_0\,=\,y_0

\end{align}

suppose we want a program (just like AI) in which we input a tuple$(y_0, \kappa, \theta, \sigma, \gamma, T) $ and we
want to find the distribution of the resulting SDE analytically in Z-series.

There will be preset restrictions on range of variables in the tuple that would have to be defined by the user in
advance of the method for example,$\kappa$ could take on values between zero and five (user would be free to specify
other range as long as SDE remains stable and could be computed) and similarly for other parameters in the above tuple.

our strategy is to define the Z-series of arbitrary SDE as

\begin{equation}

Y_T\,=\, \sum\limits_{n=0}^{N} \,c_n(y_0, \kappa, \theta, \sigma, \gamma, T) \, Z^n

\end{equation}

For that we can take all the variables in the tuple as uniform evenly distributed over the input ranges so we would have
a six dimensional uniform variable as input. We will simulate for example 5000 to ten thousand instances of this
multidimensional uniform variable creating various values of the above tuple. For each instance of the simulated tuple
of parameters, we would simulate the density of above SDE and represent it as a Z-series. Then we will uniform-regress
(or Legendre regress) each of the instance  of each Z-series coefficient on respective instance/values of the tuple that
generated the SDE. And hope to be be able to describe each of the coefficients of Z-series as a multi-dimensional
Legendre series (in six dimensions in the current case).

I am very very confident that with above logic, we would certainly be able to find each of the eight or so Z-series
coefficients required to describe the SDE as a function of the tuple parameters
$\,c_n(y_0, \kappa, \theta, \sigma, \gamma, T)$ .

I am sure that not only will such a strategy work better than AI, the time it takes to train such SDEs would not be
weeks or days but only a few hours or even less.

I want  to try this example in next seven to ten days . I hope that once we succeed, many friends will start using such
Z-series and mathematics based AI openly in so many other interesting problems  where everybody currently likes to use
black box AI.

We could possibly solve SDEs with more parameters or stochastic volatility system of SDEs but we want to try something
reasonably simple first and see how it goes.

---

### #2458 — Amin (Topic Author)
*October 5, 2024, 5:53 AM*

Friends, my work is going well. I have written the part of program about calculation of hermite series of simulated SDEs
in the algorithm. Today I will write the part about regression on Legendre polynomials of input parameters and hope to
get the program properly running in another day.

Another thing I noticed that we need to Legendre-regress coefficients of hermite series instead of coefficients of
Z-series. I believe that dealing with coefficients of hermite series might possibly be more stable due to orthogonality.

I am also thinking of limiting the mean-reverting SDEs expansion to sixth moment as a start.

I hope to come back with results in another 3-4 days.

---

### #2459 — Amin (Topic Author)
*October 5, 2024, 8:45 AM*

Friends, I hope to get my program running later today. I have not calculated all dimensions by simulation of uniform
random numbers. Out of the total six parameters, I have simulated ten thousand five dimensional uniform scenarios but I
have generated a grid in time. Maximum time is four years and there are 32 simulation intervals per year in the
simulation of each SDE which means that there are a total of 128 simulation density values over four years. So each of
the ten thousand simulations have further 128 densities each for them. And regression is done on six parameters (c0 -
c5) of 1280000 Hermite-Series densities. Time parameter is converted into a uniform between -1 and 1 for the sake of
Legendre regression but is not randomly simulated and is on a grid with equal intervals.

As a start I am not using moment matching of uniform densities for Legendre regressions but will later move to doing
that.

I hope that I will get some raw results from regressions late in the night today.

---

### #2460 — Amin (Topic Author)
*October 6, 2024, 2:13 PM*

Friends, I did some analytics yesterday on just 500 paths and got just alright results. Today, I am running a sample of
25000 SDE simulations and it can take up to several hours to complete this run.

But I was thinking that  a distribution that  is normal-like (gamma, generalized gamma, lognormal and several else)
cannot be explained by Legendre polynomial of uniforms and vice-versa. I still recall that I tried to emulate a standard
normal distribution by matching moments on Legendre polynomials of uniform density and it was totally abysmal attempt.

However, I believe that we could still do these cross-regressions on hermite/normal-like densities on Legendre
polynomials of uniform and the opposite which would be regressing distributions on finite support based on uniform, or
beta type densities on hermite polynomials of standard normal density. However, we would have to do appropriate density
transformations on either the regression-target variable (being explained)  or the explanatory variables(that are
explaining).

I am still trying to work out the details of this possible density transformation based method and might have to use it
in our new program to represent the coefficients of densities with legendre polynomials of uniform.

I will come with updates in another day but it may possibly take us more than a week or several weeks to satisfactorily
complete the current research. However, I am very certain that soon we would have a very good mathematical alternative
to AI in probability theory and statistics. I will keep friends updated with any progress.

---

### #2461 — Amin (Topic Author)
*October 7, 2024, 2:59 PM*

Friends, I have yet not been able to get good results. But that is probably because I tried to approach a very complex
problem all at once. In order to get a better feel of the problem, I will work with smaller combinations of parameters
first, learn the lessons from there and then move towards fully complex problem slowly. And I am sure that this way we
could learn much more about large scale polynomial regression problems that we need to study more systematically.
Weather has recently improved quite a bit in Lahore, and I am determined to spend all the effort and time it would take
to solve this problem in a very good way. But any solid breakthroughs can take more than a week or so. I am determined
to resolve this problem before moving on to any other research.

---

### #2462 — Amin (Topic Author)
*October 7, 2024, 8:09 PM*

Friends, other than time, if I randomize on SDE input parameters, I get an R-squared of 98% if I jointly randomize three
parameters of the SDE. If I jointly randomize on five parameters of the SDE other than time, I get an R^2 of about
75%-95% for various coefficients of the Hermite series(better for some coeffs, worse for some other coeffs). I think, at
this initial stage of research, I have to deal with time separately but that is not difficult at all on a reasonably
fine grid but has to be done separately for each time level(at this initial stage). This is almost instantaneous since
all you have to do is make a simple least square regression on each time level.

I want to do some further experiments but will post first initial version of the matlab program in two to three days.

I will continue to work to see how I can improve the results.

---

### #2463 — Amin (Topic Author)
*October 8, 2024, 11:01 AM*

Friends, I am trying to experiment further to see if I can somewhat improve the results. But whatever the case, I will
try to post my matlab program later tonight before I sleep. If I can possibly improve something, I will make those
changes in the program otherwise I will post it as such.

---

### #2464 — Amin (Topic Author)
*October 8, 2024, 10:45 PM*

.

.

.

```
function [] = SDEsWithMathAIMain08()

%The mean reverting SDE is given as
%dY(t)= kappa (theta - Y(t)) dt + sigma Y(t)^gamma dZ(t)
%Y(0) = y0

kappaL=.25;%Lower range of kappa
kappaH=3;%Upper range of kappa
thetaL=.5;%Lower range of theta
thetaH=2;%Upper range of theta
y0L=.5;%Lower range of y0
y0H=2;%Higher range of y0
gammaL=.5;%Lower range of gamma
gammaH=1;%Higher range of gamma

%I am not randomizing over sigma.
%I simply take a fixed point between lower and higher range of sigma for
%every SDE in sample.

sigmaL=.1;
sigmaH=1.0;

seed=83098561;
rng(seed);

NN=1000;%Number of SDE runs in the training sample. Ideally would be much larger.

Rand1(1:NN/2,1)=rand(NN/2,1);
Rand1(NN/2+1:NN,1)=1-Rand1(1:NN/2,1);%For symmetry, antithetic uniforms are used.
kappaU(1:NN)=kappaL+(kappaH-kappaL).*Rand1(1:NN,1);%Map unifrom random variates on kappa.

Rand2(1:NN/2,1)=rand(NN/2,1);
Rand2(NN/2+1:NN,1)=1-Rand2(1:NN/2,1);
thetaU(1:NN)=thetaL+(thetaH-thetaL).*Rand2(1:NN,1);%Map unifrom random variates on theta.

Rand3(1:NN/2,1)=rand(NN/2,1);
Rand3(NN/2+1:NN,1)=1-Rand3(1:NN/2,1);
y0U(1:NN)=y0L+(y0H-y0L).*Rand3(1:NN,1);%Map unifrom random variates on starting value of the SDE.

Rand4(1:NN/2,1)=rand(NN/2,1);
Rand4(NN/2+1:NN,1)=1-Rand4(1:NN/2,1);
gammaU(1:NN)=gammaL+(gammaH-gammaL).*Rand4(1:NN,1);%Map unifrom random variates on gamma.

sigmaU(1:NN)=(sigmaL+sigmaH)/2;%Taking sigma at mid of upper and lower range.

SDEpaths=100000;
MOrder=14;
Order=5;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

alpha(1)=1.002379147775649;
alpha(3)=-0.000740478718368;
alpha(5)=0.001052947275469;
alpha(7)=0.000402630517679;
alpha(9)=0.000121151611625;
alpha(11)=0.000012754129466;                   0
alpha(13)=0.000000680335020;

[Zn] = StandardNormalIdealDesity02(SDEpaths,1);
[ZI] = CalculateZnAfterHermiteSeriesMultiplication(Zn,alpha,MOrder);

[W] = EvalHermiteArrayH0(ZI,Order);

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
seed0=90728436;
rng(seed0, 'combRecursive')
TtM=128;
dtM=1/32;
Random0(1:SDEpaths,1:TtM)=0;

for tt=1:TtM
%Since SDEs are simulated with different parameters in a loop. We calculate
%moment matched normal random variates for all of the time steps just once
%and input them to SDE simulation program so we do not have to generate
%these random numbers again and again every time we simulate a different
%SDE inside the SDE simulation loop.
URandom=0;
URandom(1:SDEpaths/2)=0;
URandom=rand(size(URandom));
URandom(SDEpaths/2+1:SDEpaths)=1-URandom(1:SDEpaths/2);
[URandomS,I]=sort(URandom);

Random1=ZI(I);

Random0(1:SDEpaths,tt)=Random1(1:SDEpaths);
end
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Run this loop and above loop only once and save the data on disk as below.
%Then comment both these loops and keep reading the data from disk.
for nn=1:NN
 nn
 NN
[coeff] =
MeanRevertingMonteCarloDensity02(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM);
 Coeff(nn,1:TtM,1:Order+1)=coeff(1:TtM,1:Order+1);
end

 save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04C.mat","Coeff")
%
 str=input("I have saved the densities coefficients variable");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Uncomment below to read the data from disk.
%load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04C.mat","Coeff")

Tt=TtM;
%Dimensions of Coeff are Coeff(1:NN,1:TtM,1:Order+1).Below we take one time
%slice between 1 and TtM. I have taken slice 72 that occurs at time
%72*.03625=
%You can comment the SDE simulations loop and continue to load the
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.
%
%TimeSlice variable below
Ts=72;
CoeffH(1:NN,1:Order+1)=Coeff(1:NN,Ts,1:Order+1);
TT=Ts*dtM;%Time at end of chosen slice. This will be used in analytic calculation of SDE mean later.
%We will replace the first mean coefficient of zeroth hermite associated
%with the Hermite series of SDEs with the analytic value.

%Below we calculate square root of variance(sum of hermite coefficients squared formula) to standardize the coefficients
VarSqRt(1:NN,1)=
sqrt(CoeffH(1:NN,2).^2+CoeffH(1:NN,3).^2*2+CoeffH(1:NN,4).^2*6+CoeffH(1:NN,5).^2*24+CoeffH(1:NN,6).^2*120);
%Below are six standardized coefficients
SCoeff(1:NN,1:6)=CoeffH(1:NN,1:6)./VarSqRt(1:NN,1);

str=input("Reached Level 1");

for mm=1:1
    Ukappa(1:NN)=-1+2*Rand1(1:NN);%Convert first uniform to between zero and one to between -1 and +1
    Utheta(1:NN)=-1+2*Rand2(1:NN);%Convert second uniform to between zero and one to between -1 and +1
    Uy0(1:NN)=-1+2*Rand3(1:NN);%Convert third uniform to between zero and one to between -1 and +1
    Ugamma(1:NN)=-1+2*Rand4(1:NN);%Convert fourth uniform to between zero and one to between -1 and +1

     for qq=1:6
     Yl(1:NN,qq)=SCoeff(1:NN,qq); %First six standardized coefficients to be predicted.
     end
     Yl(1:NN,7)=VarSqRt(1:NN);%Square root of variance used to standardize has to be predicted as well.
end
clf;
[XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,1),NN,25,10 )
plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
str=input("Look at density of 1st coeff")

[XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,2),NN,25,10 )
plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
str=input("Look at density of 2nd coeff")

OrderL=6;%Order of Legendre polynomials to be used in regression
%
 [Wl1] = EvalLegendreArrayL0(Ukappa,OrderL);%Matrix in which zeroth Legendre and first six Legendre polynomilas are
evaluated at uniform values.
 [Wl2] = EvalLegendreArrayL0(Utheta,OrderL);
 [Wl3] = EvalLegendreArrayL0(Uy0,OrderL);
 [Wl4] = EvalLegendreArrayL0(Ugamma,OrderL);

% [Wl1] = EvalHermiteArrayH0(norminv((Ukappa+1)/2),OrderL);%Matrix in which zeroth Legendre and first six Legendre
polynomilas are evaluated at uniform values.
% [Wl2] = EvalHermiteArrayH0(norminv((Utheta+1)/2),OrderL);
% [Wl3] = EvalHermiteArrayH0(norminv((Uy0+1)/2),OrderL);
% [Wl4] = EvalHermiteArrayH0(norminv((Ugamma+1)/2),OrderL);
OrderL0=OrderL+1;
%Below Tile all of the Legendre polynomials of each of the four random
%parameters in a single matrix and use for least square regression. Zeroth
%Legendre is evaluated in each of the four matrices and has to be removed
%from tiling other than just including one time.
WL(:,1:OrderL0)=Wl1(:,1:OrderL0);
WL(:,OrderL0+1:OrderL0+OrderL)=Wl2(:,2:OrderL0);
WL(:,OrderL0+OrderL+1:OrderL0+2*OrderL)=Wl3(:,2:OrderL0);
WL(:,OrderL0+2*OrderL+1:OrderL0+3*OrderL)=Wl4(:,2:OrderL0);

CoeffL=inv(WL'*WL)*(WL'*Yl);%Legendre coefficients to predict seven variables. six standardized coefficients
%and one square root of variance of each SDE.

CoeffL
size(WL)
size(CoeffL)

str=input("Look at size of CoeffL");
     aa(:,1:7)=Yl(:,1:7);
     for nn=1:NN
     b(nn,1:7)=CoeffL(1,1:7);
     end
    for rr=2:OrderL+1

        b(:,1:7)=b(:,1:7)+CoeffL(rr,1:7).*Wl1(:,rr)+CoeffL(rr+OrderL,1:7).*Wl2(:,rr)+ ...
            CoeffL(rr+2*OrderL,1:7).*Wl3(:,rr)+CoeffL(rr+3*OrderL,1:7).*Wl4(:,rr);%+ ...
%
    end

    %Below are seven calculations of R-squared for each of
    %the standardized six coefficients and seventh value of
    1-sum((aa(:,1)-b(:,1)).^2)/sum((aa(:,1)-sum(aa(:,1))/(NN)).^2)
    1-sum((aa(:,2)-b(:,2)).^2)/sum((aa(:,2)-sum(aa(:,2))/(NN)).^2)
    1-sum((aa(:,3)-b(:,3)).^2)/sum((aa(:,3)-sum(aa(:,3))/(NN)).^2)
    1-sum((aa(:,4)-b(:,4)).^2)/sum((aa(:,4)-sum(aa(:,4))/(NN)).^2)
    1-sum((aa(:,5)-b(:,5)).^2)/sum((aa(:,5)-sum(aa(:,5))/(NN)).^2)
    1-sum((aa(:,6)-b(:,6)).^2)/sum((aa(:,6)-sum(aa(:,6))/(NN)).^2)
    1-sum((aa(:,7)-b(:,7)).^2)/sum((aa(:,7)-sum(aa(:,7))/(NN)).^2)

    str=input("Look at R^2s of six standardized hermite series coefficients and seventh square roo t");

for nn=1:NN

    cc(1:6)=b(nn,1:6).*b(nn,7);
    Yl0(1:6)=Yl(nn,1:6).*VarSqRt(nn);
    cc(1:6)
    Yl0(1:6)
    cc(1)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));%Replacing predicted value of mean with analytic value.
        clf;
     cc(1)
     nn
     PlotHermiteSeriesDensityAndRvGraph(cc(1),cc(2:Order+1),'r');

     hold on

     PlotHermiteSeriesDensityAndRvGraph(Yl0(1),Yl0(2:Order+1),'g');
     nn
     str=input("Look at comparison of graphs--Green is data and red is our interpolation from coefficients");

end

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
    NnMid
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
function [ZnNew] = CalculateZnAfterHermiteSeriesMultiplication(Zn,alpha,MOrder)

HOrder=MOrder-2;

Ndata=length(Zn);

[Hz] = HermitePoly(HOrder);

for nn=1:2:HOrder+1
    ZZ(nn,1:Ndata)=Zn(1:Ndata).^(nn-1);
end

HermiteSeries(1:Ndata)=alpha(1);
HermiteZ(1:Ndata,1:HOrder)=0;
for nn=2:2:HOrder
    Ndata;
    nn;
    HermiteZ(1:Ndata)=0;
    for mm=1:2:(nn+1)
        %HermiteZ(nn,:)=HermiteZ(nn,:)+Hz(nn+1,mm).*ZZ(mm,:);
        HermiteZ(1:Ndata)=HermiteZ(1:Ndata)+Hz(nn+1,mm).*ZZ(mm,1:Ndata);
    end
    HermiteSeries(1:Ndata)=HermiteSeries(1:Ndata)+ alpha(nn+1).*HermiteZ(1:Ndata);
end

ZnNew(1:Ndata)=Zn(1:Ndata).*HermiteSeries(1:Ndata);

Moment2=sum(ZnNew(1:Ndata).^2)*1/Ndata
Moment4=sum(ZnNew(1:Ndata).^4)*1/Ndata
Moment6=sum(ZnNew(1:Ndata).^6)*1/Ndata
Moment8=sum(ZnNew(1:Ndata).^8)*1/Ndata
Moment10=sum(ZnNew(1:Ndata).^10)*1/Ndata
Moment12=sum(ZnNew(1:Ndata).^12)*1/Ndata
Moment14=sum(ZnNew(1:Ndata).^14)*1/Ndata

plot((1:Ndata),Zn(1:Ndata),'g',(1:Ndata),ZnNew(1:Ndata),'r')

end

```

.

.

.

```
function [Wh] = EvalHermiteArrayH0(Z,Order)

%Evaluates first Order-th hermites at the array of Z's. If input array of Z
%has a size of 100 and Order is 4, it will return a 100 X 5 array.

Hz=HermitePoly(Order);

Wh(1:length(Z),1:Order+1)=0;
for nn=1:Order+1
    Wh(:,nn)=0;
    for mm=1:nn
        Wh(:,nn)=Wh(:,nn)+Hz(nn,mm).*Z(:).^(mm-1);
    end
end

end

```

.

.

.

```
function [Hz] = HermitePoly(Order)
Hz(1:Order+1,1:Order+1)=0.0;
Hz(1,1)=1.0;
for k=1:Order
    for m=1:k
       Hz(k+1,m+1)=Hz(k,m);
       if (m>1)
            Hz(k+1,m-1)=Hz(k+1,m-1)-(m-1)*Hz(k,m);
       end
    end
end

end

```

.

.

.

```
function [Coeff] = MeanRevertingMonteCarloDensity02(V0,kappaV,thetaV,sigma0,gamma,paths,W,Order,Random0,dtM,TtM)

beta1=0;
beta2=1;
mu1=kappaV*thetaV;
mu2=-kappaV;
alpha=1;

OrderA=4;
OrderM=OrderA;

% dtM=.03125;
% TtM=32*4;
%
%
% T=Tt*dt;

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

sigma11(1:OrderA+1)=0;
mu11(1:OrderA+1)=0;
mu22(1:OrderA+1)=0;
sigma22(1:OrderA+1)=0;
% index 1 correponds to zero level since matlab indexing starts at one.
sigma11(1)=1;
mu11(1)=1;
mu22(1)=1;
sigma22(1)=1;

for k=1:(OrderA+1)
    if sigma0~=0
        sigma11(k)=sigma0^(k-1);
    end
    if mu1 ~= 0
        mu11(k)=mu1^(k-1);
    end
    if mu2 ~= 0
        mu22(k)=mu2^(k-1);
    end
    if sigma0~=0
        sigma22(k)=sigma0^(2*(k-1));
    end
end
Fp(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;%General x powers on coefficients of hermite polynomials.
Ft(1:TtM+1,1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0; %General time powers on hermite polynomials

%YCoeff0 and YCoeff are coefficents for original coordinates monte carlo.

YCoeff0(1:(OrderA+1),1:(OrderA+1),1:(OrderA+1),1:(OrderA+1))=0;
%Pre-compute the time and power exponent values in small multi-dimensional arrays
YCoeff = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma); %expand y^alpha where alpha=1;

for k = 0 : (OrderA)
    for m = 0:k
        l4 = k - m + 1;
        for n = 0 : m
            l3 = m - n + 1;
            for j = 0:n
                l2 = n - j + 1;
                l1 = j + 1;
                Ft(l1,l2,l3,l4) = dtM^((l1-1) + (l2-1) + (l3-1) + .5* (l4-1));
                Fp(l1,l2,l3,l4) = (alpha + (l1-1) * beta1 + (l2-1) * beta2 + (l3-1) * 2* gamma + (l4-1) * gamma ...
                    - (l1-1) - (l2-1) - 2* (l3-1) - (l4-1));
                YCoeff0(l1,l2,l3,l4) =YCoeff(l1,l2,l3,l4).*mu11(l1).*mu22(l2).*sigma22(l3).*sigma11(l4);
            end
        end
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

YY(1:paths)=V0;  %Original process monte carlo.
Random1(1:paths)=0;
for tt=1:TtM

    Random1(1:paths)=Random0(1:paths,tt);
    HermiteP1(1,1:paths)=1;
    HermiteP1(2,1:paths)=Random1(1:paths);
    HermiteP1(3,1:paths)=Random1(1:paths).^2-1;
    HermiteP1(4,1:paths)=Random1(1:paths).^3-3*Random1(1:paths);
    HermiteP1(5,1:paths)=Random1(1:paths).^4-6*Random1(1:paths).^2+3;

%        YY0=YY;
%     for k = 0 : OrderM
%         for m = 0:k
%             l4 = k - m + 1;
%             for n = 0 : m
%                 l3 = m - n + 1;
%                 for j = 0:n
%                     l2 = n - j + 1;
%                     l1 = j + 1;
%                     if(l4<=5)
%
%
%                     YY(1:paths)=YY(1:paths) + YCoeff0(l1,l2,l3,l4) * ...
%                     YY0(1:paths).^Fp(l1,l2,l3,l4) .* HermiteP1(l4,1:paths) * Ft(l1,l2,l3,l4);
%                 %Above is original coordinates monte carlo equation.
%                     end
%                 end
%             end
%         end
%     end
%

  YY(1:paths)=YY(1:paths) + ...
      (YCoeff0(1,1,2,1).*YY(1:paths).^Fp(1,1,2,1)+YCoeff0(1,2,1,1).*YY(1:paths).^Fp(1,2,1,1)+ ...
      YCoeff0(2,1,1,1).*YY(1:paths).^Fp(2,1,1,1))*dtM + ...
      (YCoeff0(1,1,3,1).*YY(1:paths).^Fp(1,1,3,1)+YCoeff0(1,2,2,1).*YY(1:paths).^Fp(1,2,2,1)+ ...
      YCoeff0(2,1,2,1).*YY(1:paths).^Fp(2,1,2,1)+YCoeff0(1,3,1,1).*YY(1:paths).^Fp(1,3,1,1)+ ...
      YCoeff0(2,2,1,1).*YY(1:paths).^Fp(2,2,1,1)+YCoeff0(3,1,1,1).*YY(1:paths).^Fp(3,1,1,1))*dtM^2 + ...
      (YCoeff0(1,1,4,1).*YY(1:paths).^Fp(1,1,4,1)+YCoeff0(1,2,3,1).*YY(1:paths).^Fp(1,2,3,1)+ ...
      YCoeff0(2,1,3,1).*YY(1:paths).^Fp(2,1,3,1)+YCoeff0(1,3,2,1).*YY(1:paths).^Fp(1,3,2,1)+ ...
      YCoeff0(2,2,2,1).*YY(1:paths).^Fp(2,2,2,1)+YCoeff0(3,1,2,1).*YY(1:paths).^Fp(3,1,2,1)+ ...
      YCoeff0(1,4,1,1).*YY(1:paths).^Fp(1,4,1,1)+YCoeff0(2,3,1,1).*YY(1:paths).^Fp(2,3,1,1)+ ...
      YCoeff0(3,2,1,1).*YY(1:paths).^Fp(3,2,1,1)+YCoeff0(4,1,1,1).*YY(1:paths).^Fp(4,1,1,1))*dtM^3 + ...
       (YCoeff0(1,1,5,1).*YY(1:paths).^Fp(1,1,5,1)+YCoeff0(1,2,4,1).*YY(1:paths).^Fp(1,2,4,1)+ ...
    YCoeff0(2,1,4,1).*YY(1:paths).^Fp(2,1,4,1)+YCoeff0(2,4,1,1).*YY(1:paths).^Fp(2,4,1,1)+ ...
    YCoeff0(4,2,1,1).*YY(1:paths).^Fp(4,2,1,1)+YCoeff0(1,4,2,1).*YY(1:paths).^Fp(1,4,2,1)+ ...
     YCoeff0(4,1,2,1).*YY(1:paths).^Fp(4,1,2,1)+ ...
     YCoeff0(2,2,3,1).*YY(1:paths).^Fp(2,2,3,1)+ ...
     YCoeff0(2,3,2,1).*YY(1:paths).^Fp(2,3,2,1)+YCoeff0(3,2,2,1).*YY(1:paths).^Fp(3,2,2,1)+ ...
     YCoeff0(3,3,1,1).*YY(1:paths).^Fp(3,3,1,1)+YCoeff0(3,1,3,1).*YY(1:paths).^Fp(3,1,3,1)+ ...
      YCoeff0(1,3,3,1).*YY(1:paths).^Fp(1,3,3,1)+ YCoeff0(1,5,1,1).*YY(1:paths).^Fp(1,5,1,1)+ ...
      + YCoeff0(1,1,5,1).*YY(1:paths).^Fp(1,1,5,1)+ YCoeff0(5,1,1,1).*YY(1:paths).^Fp(5,1,1,1))*dtM^4+ ...
      ((YCoeff0(1,1,1,2).*YY(1:paths).^Fp(1,1,1,2).*sqrt(dtM))+ ...
    (YCoeff0(1,1,2,2).*YY(1:paths).^Fp(1,1,2,2)+YCoeff0(1,2,1,2).*YY(1:paths).^Fp(1,2,1,2)+ ...
    YCoeff0(2,1,1,2).*YY(1:paths).^Fp(2,1,1,2)).*dtM^1.5+ ...
    (YCoeff0(1,1,3,2).*YY(1:paths).^Fp(1,1,3,2)+YCoeff0(1,2,2,2).*YY(1:paths).^Fp(1,2,2,2)+ ...
    YCoeff0(2,1,2,2).*YY(1:paths).^Fp(2,1,2,2)+YCoeff0(1,3,1,2).*YY(1:paths).^Fp(1,3,1,2)+ ...
    YCoeff0(2,2,1,2).*YY(1:paths).^Fp(2,2,1,2)+YCoeff0(3,1,1,2).*YY(1:paths).^Fp(3,1,1,2)).*dtM^2.5+ ...
    (YCoeff0(1,1,4,2).*YY(1:paths).^Fp(1,1,4,2)+YCoeff0(1,2,3,2).*YY(1:paths).^Fp(1,2,3,2)+ ...
    YCoeff0(2,1,3,2).*YY(1:paths).^Fp(2,1,3,2)+YCoeff0(1,3,2,2).*YY(1:paths).^Fp(1,3,2,2)+ ...
    YCoeff0(2,2,2,2).*YY(1:paths).^Fp(2,2,2,2)+ YCoeff0(3,1,2,2).*YY(1:paths).^Fp(3,1,2,2)+ ...
    YCoeff0(1,4,1,2).*YY(1:paths).^Fp(1,4,1,2)+YCoeff0(2,3,1,2).*YY(1:paths).^Fp(2,3,1,2)+ ...
    YCoeff0(3,2,1,2).*YY(1:paths).^Fp(3,2,1,2)+YCoeff0(4,1,1,2).*YY(1:paths).^Fp(4,1,1,2)).*dtM^3.5)
.*HermiteP1(2,1:paths) + ...
    ((YCoeff0(1,1,1,3).*YY(1:paths).^Fp(1,1,1,3) *dtM) + ...
    (YCoeff0(1,1,2,3).*YY(1:paths).^Fp(1,1,2,3)+YCoeff0(1,2,1,3).*YY(1:paths).^Fp(1,2,1,3)+ ...
    YCoeff0(2,1,1,3).*YY(1:paths).^Fp(2,1,1,3)).*dtM^2+ ...
    (YCoeff0(1,1,3,3).*YY(1:paths).^Fp(1,1,3,3)+YCoeff0(1,2,2,3).*YY(1:paths).^Fp(1,2,2,3)+ ...
    YCoeff0(2,1,2,3).*YY(1:paths).^Fp(2,1,2,3) + YCoeff0(1,3,1,3).*YY(1:paths).^Fp(1,3,1,3)+ ...
    YCoeff0(2,2,1,3).*YY(1:paths).^Fp(2,2,1,3)+YCoeff0(3,1,1,3).*YY(1:paths).^Fp(3,1,1,3)).*dtM^3).*HermiteP1(3,1:paths)
+ ...
    ((YCoeff0(1,1,1,4).*YY(1:paths).^Fp(1,1,1,4)*dtM^1.5 )+ ...
    (YCoeff0(1,1,2,4).*YY(1:paths).^Fp(1,1,2,4)+YCoeff0(1,2,1,4).*YY(1:paths).^Fp(1,2,1,4)+ ...
    YCoeff0(2,1,1,4).*YY(1:paths).^Fp(2,1,1,4))*dtM^2.5).*HermiteP1(4,1:paths) + ...
    (YCoeff0(1,1,1,5).*YY(1:paths).^Fp(1,1,1,5)*dtM^2.0).*HermiteP1(5,1:paths);

   %  YY(YY<0)=-YY(YY<0)/4;

    if(rem(tt,1)==0)
       % mm=mm+1;
    [Coeff(tt,1:Order+1)] = CalculateHermiteSeriesFromDataWithWin(YY,W,Order);

%     clf;
%
%     PlotHermiteSeriesDensityAndRvGraph(Coeff(tt,1),Coeff(tt,2:Order+1),'r');
%
%     hold on
%
%     NoOfBins=100;
%     MaxCutOff=10;
%     [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(YY,paths,NoOfBins,MaxCutOff );
%
%     plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g')
%
%     str=input("Look atComparison of Densities");

    end

end

end

```

.

.

.

```
function [Y] = ItoTaylorCoeffsNew(alpha,beta1,beta2,gamma)

%In the coefficient calculation program which calculates Y(l1,l2,l3,l4),
%I have used four levels of looping each for relevant expansion order.
%The first loop takes four values and second loop takes 16 values and
%third loop takes 64 values and so on. And then each coefficient
%term can be individually calculated while carefully accounting
%for path dependence.
%So for example in a nested loop structure
%m1= 1:mDim
% 	m2=1:mDim
%		m3=1:mDim
%    l(m1)=l(m1)+1;
%    l(m2)=l(m2)+1;
%    l(m3)=l(m3)+1;

%in the above looping loop takes values from one to four with one
%indicating the first drift term, two indicating the second drift term
%and three indicating quadratic variation term and
%four indicating the volatility term. And with this looping structure
%we can So in the above looping m1=1 would mean that all terms are
%descendent of first drift term and m2=4 would mean that all terms are
%descendent of first drift term on first expansion order and descendent
%of volatility term on the second order and so we can keep track of path
%dependence perfectly.
%And on each level, we individually calculate the descendent terms. While
%keeping track of path dependence and calculating the coefficients with
%careful path dependence consideration, we update the appropriate element
%in our polynomial like expansion coefficient array

%explaining the part of code
%m1= 1:mDim
%	m2=1:mDim
%		m3=1:mDim
%    l(m1)=l(m1)+1;
%    l(m2)=l(m2)+1;
%    l(m3)=l(m3)+1;
%Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,1,2);

%Here l(1) denotes l1 but written as l(1) so it can be conveniently
%updated with the loop variable when the loop variable takes value one
%indicating first drift term . And l(2) could be conveniently updated when
%the loop variable takes value equal to two indicating second
%drift term and so on.
%Here is the part of code snippet for that

%for m1=1:mDim
%    l(1)=1;
%    l(2)=1;
%    l(3)=1;
%    l(4)=1;
%    l(m1)=l(m1)+1;
%CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma - (l(1)-1) - (l(2)-1) -
2*(l(3)-1) - (l(4)-1);
%    CoeffDX2 = CoeffDX1 - 1;
%    ArrIndex0=m1;
%    ArrIndex=(m1-1)*mDim;
%    Coeff1st=Y1(ArrIndex0)*CoeffDX1;
%    Coeff2nd=Y1(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
%    Y2(1+ArrIndex)=Coeff1st;
%    Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
%    Y2(2+ArrIndex)=Coeff1st;
%    Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
%    Y2(3+ArrIndex)=Coeff2nd;
%    Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,1,2,n1(m1));
%    Y2(4+ArrIndex)=Coeff1st;
%    Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,1,3,n1(m1));

%The first four lines update the array indices according to the parent term.
%And then CoeffDX1 and CoeffDX2 are calculated according to algebraic exponents on parent terms.
%ArrIndex0=m1; calculates the array index of the parent term
%And ArrIndex=(m1-1)*mDim; calculates the array index of the descendent terms
%And coefficient of the drift and volatility descendent terms is
%calculated by multiplying the coefficient of the parent term by
%Coeff1st=Y1(ArrIndex0)*CoeffDX1;
%And coefficient of the quadratic variation descendent terms is
%calculated by multiplying the coefficient of the parent term by
%Coeff2nd=Y1(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
%And then each of the four descendent terms are updated with Coeff1st
%if they are drift or volatility descendent terms or Coeff2nd if
%they are quadratic variation descendent terms.
%Here Y1 indicates the temporary coefficient array with parent terms on
%first level. And Y2 denotes temporary coefficient array with parent terms
%on second level and Y3 indicates temporary coefficient array with parent terms on third level.

[IntegralCoeff,IntegralCoeffdt,IntegralCoeffdz] = ComputeIntegralCoeffs();

n1(1)=2;
n1(2)=2;
n1(3)=2;
n1(4)=3;
%n1(1), n1(2), n1(3) are drift and quadratic variation term variables
%and take a value equal to 2 indicating a dt integral.
%n1(4) is volatility term variable and indicates a dz-integral by taking a
%value of 3.

mDim=4; % four descendent terms in each expansion
Y(1:5,1:5,1:5,1:5)=0;
Y1(1:mDim)=0;
Y2(1:mDim*mDim)=0;
Y3(1:mDim*mDim*mDim)=0;

%First Ito-hermite expansion level starts here. No loops but four
%descendent terms.
l(1)=1;
l(2)=1;
l(3)=1;
l(4)=1;
CoeffDX1 = alpha;
CoeffDX2 = CoeffDX1 - 1;
Coeff1st=CoeffDX1;
Coeff2nd=.5*CoeffDX1*CoeffDX2;

Y1(1)=Coeff1st;
Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,1,2);
Y1(2)=Coeff1st;
Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,1,1,2);
Y1(3)=Coeff2nd;
Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,1,1,2);
Y1(4)=Coeff1st;
Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,1,1,3);

%Second Ito-hermite expansion level starts. It has a loop over four parent
%terms and there are four descendent terms for each parent term.
%The coefficient terms are then lumped in a polynomial-like expansion
%array of coefficients.
for m1=1:mDim
    l(1)=1;
    l(2)=1;
    l(3)=1;
    l(4)=1;
    l(m1)=l(m1)+1;
    CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma ...
                        - (l(1)-1) - (l(2)-1) - 2*(l(3)-1) - (l(4)-1);
    CoeffDX2 = CoeffDX1 - 1;
    ArrIndex0=m1;
    ArrIndex=(m1-1)*mDim;
    Coeff1st=Y1(ArrIndex0)*CoeffDX1;
    Coeff2nd=Y1(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
    Y2(1+ArrIndex)=Coeff1st;
    Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
    Y2(2+ArrIndex)=Coeff1st;
    Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,1,2,n1(m1));
    Y2(3+ArrIndex)=Coeff2nd;
    Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,1,2,n1(m1));
    Y2(4+ArrIndex)=Coeff1st;
    Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,1,3,n1(m1));
    %Third Ito-hermite expansion level starts and it is a nested loop with
    %a total of sixteen parents and each parent takes four descendent
    %terms.
    for m2=1:mDim
        l(1)=1;
        l(2)=1;
        l(3)=1;
        l(4)=1;
        l(m1)=l(m1)+1;
        l(m2)=l(m2)+1;
        CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma ...
                        - (l(1)-1) - (l(2)-1) - 2*(l(3)-1) - (l(4)-1);
        CoeffDX2=CoeffDX1-1;
        ArrIndex0=(m1-1)*mDim+m2;
        ArrIndex=((m1-1)*mDim+(m2-1))*mDim;
        Coeff1st=Y2(ArrIndex0)*CoeffDX1;
        Coeff2nd=Y2(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
        Y3(1+ArrIndex)=Coeff1st;
        Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(1,2,n1(m2),n1(m1));
        Y3(2+ArrIndex)=Coeff1st;
        Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(1,2,n1(m2),n1(m1));
        Y3(3+ArrIndex)=Coeff2nd;
        Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(1,2,n1(m2),n1(m1));
        Y3(4+ArrIndex)=Coeff1st;
        Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(1,3,n1(m2),n1(m1));
        %fourht Ito-hermite expansion level starts and it is a triply-nested loop with
        %a total of sixteen parents and each parent takes four descendent
        %terms. We then lump the terms in a relatively sparse polynomial
        %like expansion coefficient array that has smaller number of
        %non-zero terms.

        for m3=1:mDim
            l(1)=1;
            l(2)=1;
            l(3)=1;
            l(4)=1;
            l(m1)=l(m1)+1;
            l(m2)=l(m2)+1;
            l(m3)=l(m3)+1;
            CoeffDX1 = alpha + (l(1)-1) *beta1 + (l(2)-1) *beta2 + (l(3)-1) *2*gamma + (l(4)-1)*gamma ...
                        - (l(1)-1) - (l(2)-1) - 2*(l(3)-1) - (l(4)-1);
            CoeffDX2=CoeffDX1-1;
            ArrIndex0=((m1-1)*mDim+(m2-1))*mDim+m3;
            %ArrIndex=(((m1-1)*mDim+(m2-1))*mDim+(m3-1))*mDim;
            Coeff1st=Y3(ArrIndex0)*CoeffDX1;
            Coeff2nd=Y3(ArrIndex0)*.5*CoeffDX1*CoeffDX2;
            %Y4(1+ArrIndex)=Coeff1st;
            Y(l(1)+1,l(2),l(3),l(4))=Y(l(1)+1,l(2),l(3),l(4))+Coeff1st*IntegralCoeff(2,n1(m3),n1(m2),n1(m1));
            %Y4(2+ArrIndex)=Coeff1st;
            Y(l(1),l(2)+1,l(3),l(4))=Y(l(1),l(2)+1,l(3),l(4))+Coeff1st*IntegralCoeff(2,n1(m3),n1(m2),n1(m1));
            %Y4(3+ArrIndex)=Coeff2nd;
            Y(l(1),l(2),l(3)+1,l(4))=Y(l(1),l(2),l(3)+1,l(4))+Coeff2nd*IntegralCoeff(2,n1(m3),n1(m2),n1(m1));
            %Y4(4+ArrIndex)=Coeff1st;
            Y(l(1),l(2),l(3),l(4)+1)=Y(l(1),l(2),l(3),l(4)+1)+Coeff1st*IntegralCoeff(3,n1(m3),n1(m2),n1(m1));
         end
    end
end

end

```

.

.

.

```
function [IntegralCoeff0,IntegralCoeffdt,IntegralCoeffdz] = ComputeIntegralCoeffs()

IntegralCoeff(1:3,1:3,1:3,1:3)=0;
IntegralCoeffdt(1:3,1:3,1:3,1:3)=0;
IntegralCoeffdz(1:3,1:3,1:3,1:3)=0;

IntegralCoeff0(1:3,1:3,1:3,1:3)=0;

IntegralCoeff0(1,1,1,2)=1;
IntegralCoeff0(1,1,1,3)=1;

IntegralCoeff0(1,1,2,2)=1/2;
IntegralCoeff0(1,1,3,2)=1-1/sqrt(3);
IntegralCoeff0(1,1,2,3)=1/sqrt(3);
IntegralCoeff0(1,1,3,3)=1/2;

IntegralCoeff0(1,2,2,2)=1/6;
IntegralCoeff0(1,3,2,2)=(1-1/sqrt(3))*1/2*(1-1/sqrt(5));
IntegralCoeff0(1,2,3,2)=1/sqrt(3)/2*(1-1/sqrt(5));
IntegralCoeff0(1,3,3,2)=1/2*(1-sqrt(2)/2);
IntegralCoeff0(1,2,2,3)=1/2*1/sqrt(5);
IntegralCoeff0(1,3,2,3)=(1-1/sqrt(3))*1/sqrt(2)*1/2;
IntegralCoeff0(1,2,3,3)=1/sqrt(3)/sqrt(2)*1/(2);
IntegralCoeff0(1,3,3,3)=1/6;

IntegralCoeff0(2,2,2,2)=1/24;
IntegralCoeff0(2,2,3,2)=1/2*1/sqrt(5)*1/3*(1-1/sqrt(7));
IntegralCoeff0(2,3,2,2)=1/sqrt(3)*1/2*(1-1/sqrt(5))*1/3*(1-1/sqrt(7));
IntegralCoeff0(3,2,2,2)=(1-1/sqrt(3))*1/2*(1-1/sqrt(5))*1/3*(1-1/sqrt(7));
IntegralCoeff0(3,3,2,2)=1/2*(1-sqrt(2)/2)*1/2*(1-sqrt(2)/sqrt(6));
IntegralCoeff0(2,3,3,2)=1/sqrt(3)*1/sqrt(2)*1/2*1/2*(1-sqrt(2)/sqrt(6));
IntegralCoeff0(3,2,3,2)=(1-1/sqrt(3))*1/sqrt(2)*1/2*1/2*(1-sqrt(2)/sqrt(6));
IntegralCoeff0(3,3,3,2)=1/6*(1-sqrt(3)/sqrt(5));

IntegralCoeff0(2,2,2,3)=1/6*1/sqrt(7);
IntegralCoeff0(2,2,3,3)=1/2*1/sqrt(5)*1/sqrt(2)*1/sqrt(6);
IntegralCoeff0(2,3,2,3)=1/sqrt(3)*1/2*(1-1/sqrt(5))*1/sqrt(2)*1/sqrt(6);
IntegralCoeff0(3,2,2,3)=(1-1/sqrt(3))*1/2*(1-1/sqrt(5))*1/sqrt(2)*1/sqrt(6);
IntegralCoeff0(3,3,2,3)=1/2*(1-sqrt(2)/2)*1/sqrt(3)*1/sqrt(5);
IntegralCoeff0(2,3,3,3)=1/sqrt(3)*1/sqrt(2)*1/sqrt(4)*1/sqrt(3)*(1/sqrt(5));
IntegralCoeff0(3,2,3,3)=(1-1/sqrt(3))*1/sqrt(2)*1/2*1/sqrt(3)*1/sqrt(5);
IntegralCoeff0(3,3,3,3)=1/24;

%Can also be calculated with algorithm below.
%here IntegralCoeffdt indicates the coefficients of a dt-integral.
%This dt-integral means that you are calculating the Ito-hermite expansion
%of  Integral X(t)^alpha dt with X(t) dynamics given by the SDE
%here IntegralCoeffdz indicates the coefficients of a dz-integral.
%This dz-integral means that you are calculating the Ito-hermite expansion
%of  Integral X(t)^alpha dz(t) with X(t) dynamics given by the SDE

%IntegralCoeff is is associated with expansion of X(t)^alpha.
%IntegralCoeff below is not returned and IntegralCoeff0 manually calculated
%above is returned but both are the same.

l0(1:2)=1;

for m4=1:2
    l0(1)=1;
    l0(2)=1;

    %IntegralCoeff4(m4,1,1,1)=1;
    %IntegralCoeff4(m4,1,1,1)=1;
    %1 is added to m4 since index 1 stands for zero, 2 for one and three
    %for two.
    IntegralCoeff(1,1,1,m4+1)=1;
    l0(m4)=l0(m4)+1;
    IntegralCoeffdt(1,1,1,m4+1)=IntegralCoeff(1,1,1,m4+1)* ...
        1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
    IntegralCoeffdz(1,1,1,m4+1)= IntegralCoeff(1,1,1,m4+1)* ...
        1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
    for m3=1:2
        l0(1)=1;
        l0(2)=1;
        l0(m4)=l0(m4)+1;

        if(m3==1)
            IntegralCoeff(1,1,m4+1,m3+1)=1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
        end
        if(m3==2)
            IntegralCoeff(1,1,m4+1,m3+1)= 1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
        end
        l0(m3)=l0(m3)+1;
        %IntegralCoeff(1,1,m4+1,m3+1)=IntegralCoeff4(m4,m3,1,1);
        IntegralCoeffdt(1,1,m4+1,m3+1)=IntegralCoeff(1,1,m4+1,m3+1)* ...
            1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
        IntegralCoeffdz(1,1,m4+1,m3+1)= IntegralCoeff(1,1,m4+1,m3+1)* ...
            1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
        for m2=1:2
            l0(1)=1;
            l0(2)=1;
            l0(m4)=l0(m4)+1;
            l0(m3)=l0(m3)+1;

            if(m2==1)
               
IntegralCoeff(1,m4+1,m3+1,m2+1)=IntegralCoeff(1,1,m4+1,m3+1)*1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
            end
            if(m2==2)
                IntegralCoeff(1,m4+1,m3+1,m2+1)=
IntegralCoeff(1,1,m4+1,m3+1)*1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
            end
            l0(m2)=l0(m2)+1;
            %IntegralCoeff(1,m4+1,m3+1,m2+1)=IntegralCoeff4(m4,m3,m2,1);
            IntegralCoeffdt(1,m4+1,m3+1,m2+1)=IntegralCoeff(1,m4+1,m3+1,m2+1)* ...
                1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
            IntegralCoeffdz(1,m4+1,m3+1,m2+1)= IntegralCoeff(1,m4+1,m3+1,m2+1)* ...
                1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);

            for m1=1:2
                l0(1)=1;
                l0(2)=1;
                l0(m4)=l0(m4)+1;
                l0(m3)=l0(m3)+1;
                l0(m2)=l0(m2)+1;
                if(m1==1)
                   
IntegralCoeff(m4+1,m3+1,m2+1,m1+1)=IntegralCoeff(1,m4+1,m3+1,m2+1)*1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
                end
                if(m1==2)
                    IntegralCoeff(m4+1,m3+1,m2+1,m1+1)=
IntegralCoeff(1,m4+1,m3+1,m2+1)*1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
                end
                l0(m1)=l0(m1)+1;
                %IntegralCoeff(m4+1,m3+1,m2+1,m1+1)=IntegralCoeff4(m4,m3,m2,m1);
                IntegralCoeffdt(m4+1,m3+1,m2+1,m1+1)=IntegralCoeff(m4+1,m3+1,m2+1,m1+1)* ...
                    1/(l0(1)-1+1)*(1-sqrt(l0(2)-1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+2));
                IntegralCoeffdz(m4+1,m3+1,m2+1,m1+1)= IntegralCoeff(m4+1,m3+1,m2+1,m1+1)* ...
                    1/sqrt(l0(2)-1+1)/sqrt(2*(l0(1)-1)+(l0(2)-1)+1);
            end
        end
    end
end

end
```

.

.

.

```
function [Coeff] = CalculateHermiteSeriesFromDataWithWin(Yin,W,Order)

Ndata=length(Yin);

%Hz=HermitePoly(Order);
MeanYin=sum(Yin(1:Ndata))/Ndata;
Ym(1:Ndata)=Yin(1:Ndata)-MeanYin;
YmVar=sum(Ym(1:Ndata).^2)/Ndata;
Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);

%We first sort the data so that we can assign one appropriate Z-grid
%point(and associated hermite polynomials calculated at that grid point)
%to each data element. This ideal normal density Z-grid is
%constructed so that its size is equal to data observations count. We
%suppose that first derivative of random variables with repsect to Z
%does not switch sign meaning that increasing values of data
%observations have to aligned with increasing values of ideal normal
%density grid.
[Ys,I]=sort(Y(1:Ndata));
%In the line below, the data sort is reversed so that now the ideal
%normal density grid elements assigned to various observations of random
%variable face it on data observations index. For details, Please look
%on interent the definition of matlab sort command with role of "I"
%in output and how it alters the index.

%%Zs1(I(1:Ndata))=ZI(1:Ndata);

%Below the values to be regressed facing the design matrix are assigned
Ymu(1:Ndata,1)=Ys(1:Ndata);
%Below, implement least squares regression.
coeff=inv(W'*W)*(W'*Ymu);
%Store in coefficietns array of all random varaibles
Coeff(1:Order+1)= coeff(1:Order+1,1);
%Store the associated Z in Z-array of all coefficients.
%%%Zy(1:Ndata)=Zs1(1:Ndata);

Coeff(1:Order+1)=Coeff(1:Order+1).*sqrt(YmVar);
Coeff(1)=Coeff(1)+MeanYin;

end
```

.

.

.

```
function [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(X,Paths,NoOfBins,MaxCutOff )
%Processes monte carlo paths to return a series Xdensity as a function of IndexOut. IndexMax is the maximum value of
index.
%

Xmin=0;
Xmax=0;
for p=1:Paths
if(X(p)>MaxCutOff)
X(p)=MaxCutOff;
end
%if(X(p)real(X(p)))
Xmin=real(X(p));
end
if(XmaxIndexMax)
index=IndexMax;
end

XDensity(index)=XDensity(index)+1.0/Paths/BinSize;

end

IndexOut(1:IndexMax)=Xmin+(0:(IndexMax-1))*BinSize;

end
```

.

.

.

```
function [Wl] = EvalLegendreArrayL0(U,Order)

%Evaluates first Order-th Legendres at the array of U's. If input array of Z
%has a size of 100 and Order is 4, it will return a 100 X 5 array.

Lu=LegendrePoly(Order);

Wl(1:length(U),1:Order+1)=0;
for nn=1:Order+1
    Wl(:,nn)=0;
    for mm=1:nn
        Wl(:,nn)=Wl(:,nn)+Lu(nn,mm).*U(:).^(mm-1);
    end
end

end
```

.

.

.

```
function [Lu] = LegendrePoly(Order)
Lu(1:Order+1,1:Order+1)=0.0;
Lu(1,1)=1.0;
Lu(2,2)=1.0;
for n=2:Order

    for m=1:n
       Lu(n+1,m+1)=Lu(n+1,m+1)+Lu(n,m)*(2*(n-1)+1)/((n-1)+1);
    end
    for m=1:n-1
       Lu(n+1,m)=Lu(n+1,m)-Lu(n-1,m)*(n-1)/((n-1)+1);
    end
end
Lu;
end

```

.

.

.

```
function [] = PlotHermiteSeriesDensityAndRvGraph(c0,c,Color)

Index=length(c);

dNn=.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=45*4;  % No of normal density subdivisions
NnMid=((1+Nn)/2)*dNn;
Z(1:Nn)=(((1:Nn)*dNn)-NnMid);
%Z
%str=input('Look at Z');
%Now calculate Y as a function of normal random variable.
[W] = EvalHermiteArrayH0(Z,Index);

Y(1:Nn,1)=c0;
for nn=1:Index
    Y(1:Nn,1)=Y(1:Nn,1)+W(1:Nn,nn+1).*c(nn);
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
%plot(Z(1:Nn),Y(1:Nn),Color);
%title('Graph of Z-Series Variable as a function of underlying standard normal');
%str=input('Look at Graph of Z-Series Variable as a function of underlying standard normal');

end

```

.

.

.

---

### #2465 — Amin (Topic Author)
*October 9, 2024, 8:40 AM*

Friends, very sorry for the timing of this post. Efforts for my mind control were going on like crazy for more than 3-4
weeks. Everywhere I would go, mind control agents(Pak army) would reach there instantaneously to drug everything of
interest very quickly. I would usually buy vegetables, yogurt, water and many other such things regularly. Just to give
an example, two weeks ago I went out to buy food on my motorcycle and I moved off the main road on outskirts of the city
and took a dirt road and reached a village about two to three kilometers off the main road. Even though it was not a
very large village, there were still a few motorcycles driving on the dirt road as Lahore is one of the 25 largest
cities in the world. After reaching the village market, I bought a drink at a small shop and it took me two to three
minutes. But when I moved on to buy actual food in the village market, I realized that mind control agents of Pak army
had already taken positions in all of the small vegetable shops ( there were probably three of them) and dairy shops
where they sell locally made yogurt in small polythene bags. I was very surprised how quickly they had taken positions
in the small village.

However, I never made a big deal since I was still consistently being able to get good food and water almost everyday.
Because, I keep driving and changing paths in the huge city and never think of buying food at a particular place and if
I would have thought of buying food somewhere in advance, I almost never do that since they are reading the mind all the
time and quickly reach places where the victim plans to buy food.  So I keep moving around and keep counting
probabilities whether some place would be safe to buy food and all of a sudden buy something when I know that there is
good likelihood of good food somewhere and mind control agents would not have reached there.

So I wanted to remain silent and not make a big deal about there attempts to drug since I was mostly getting good food
and water. But on 3rd of october, the same day I made posts about Math AI, I had a motorcycle accident and I fell on the
road and broke a bone in my right thumb. I quickly got a tetanus injection and used a ready made strap to immobilize my
thumb. There was not much pain and I was not sick so I continued to work and made the posts about math AI and also
uploaded my earlier Z-series coefficients optimization program later at the same night. I have been trying to work
normally since then because I can still write code and do most other things despite my immobilized thumb. However, I
cannot drive a motorcycle due to my immobilized thumb and I have to use my car to go out to buy food. But path of a car
is much more predictable since it has to remain on large roads and it cannot drive into small city streets that are
spread all over the city everywhere. I was still able to buy good water and I kept buying a lot of milk and yogurt so my
bone would heal better but many times I would notice that mind control agents would move into stores after I would go
and start pretending they were part of the staff (Stores all around the city are aware of this practice of Pak army and
they do not make a big deal and usually fully cooperate with them). And today they were able to drug water and yogurt
from the places I bought them. And I only realized when I had come home and found out that both the yogurt and several
large water bottles I had bought were all drugged.

Contrary to what many people might think, mind control agents consider a broken bone an opportunity to damage their
target and when I sleep at night they keep targeting EM waves on my hand kicking key receptors out of there that are
required to heal the bone so that I would always have some small pain or a problematic joint even after the bone would
have healed not so well.

I want friends to please protest to American defense that has become a puppet in the hands of rich jews. Scumbags of
American defense consider successful Muslims a stain on social fabric of United States. I am just a Muslim by birth and
do not believe in any religion and there are thousands of Muslims like me that are kept on mind control by American
defense to prevent them from being successful. And majority of such victims are  American born Muslims who are like
other natives of US even though I was admittedly a foreigner. Black sheep in American defense behind mind control are
given very prestigious jobs paying millions of dollars in Jewish companies after they retire and rich jews want to block
talented muslims from being successful in United States with an iron fist since they are afraid that if some muslims
become successful, they would start wielding some influence and start opposing American policies in Israel and they want
to nip this supposed evil in the bud. And American defense has no dearth of wannabees who desperately want to join the
ranks of so many others who have gotten extremely high paying jobs with great social status in jewish companies after
retirement from American defense. Please do not blindly believe me and find out somebody in your social circle(or well
known to somebody in your social circle) you know well and who is in mind control agency of US defense and ask them
about my allegations and your eyes would open forever about role of rich jews in United States and how they openly use
mind control on anyone they wish especially on a large number of even white Americans whose families have been living in
US for hundreds of years. If your eyes do not open forever, I am ready to take any blame you wish.

Especially very talented American people in science and technology are forced to work in Jewish owned companies due to
fear of mind control. Many such people who want to leave are coldly told by administration to leave but their mind
control is initiated by American defense on insistence of jews right after they leave the jewish company and once they
know the reason behind mind control was that they tried to leave the jewish company against the will of the company
owners. And due to large number of such precedents well known to many professionals in many jewish companies, most of
the very talented people do not dare to leave the jewish companies against the will of administration since they know
very well that they would be instantly put on mind control by American defense who dances on the tunes of rich jews
since they want extremely high paying prestigious jobs with jewish companies having great social status. Please do not
believe a single word I say blindly but try to find out the actual truth on your own from authentic sources you know
well and you will find the truth that would open your eyes forever.

Not everybody is the same, there are at the same time a large number of jews who have nothing to do with any of this and
many good jewish companies who do not follow any inhuman practice. But there is a close group of rich jews who are
actually involved in large scale mind control with American defsnse working as their proxy. Please try to know the truth
on your own.

---

### #2466 — Amin (Topic Author)
*October 9, 2024, 12:07 PM*

Friends, I have been thinking of improving the polynomial regression. And I noticed a few things that I did not properly
understand earlier.

First please consider a simple example. Suppose we have two independent random variables X and Y and there is another
random variable that is product of both of them and is XY.

We want to do polynomial regression to capture XY from regression on X and Y. There is no way we can capture this
product from sum of two hermite series in X and Y. If there is any correlation between X and Y, regression on sum of two
hermite series could easily capture the correlated part but product of independent parts still could not be captured by
such a regression. We could include all combinations of cross products of two hermite polynomials but they would
probably be too noisy and using orthogonal polynomials for product of independent variables would not make much sense
and it is difficult even though it is a simple regression on product of two random variables.  It would be rather much
easier to directly include products of standardized(for example in terms of normal or uniform) versions of independent
parts/portions of the two random variables in the regression instead of messy and unstable products of their orthogonal
polynomials.

I have only included  Legendre polynomials of all different parameters linearly in the regression and there are no
products. But we know that mean of the SDE and also its variance depends upon products of several parameters. for
example mean at a fixed time is given as

$$ \theta \, + \, \exp(-\kappa \, t_0) \, \left( X_0 \, - \theta \, \right) $$

$
$ \theta \, + \, \, \left(\, 1\, - (\kappa \, t_0) \,+ \, .5 \,(\kappa \, t_0)^2 - \, .1666 \, (\kappa \, t_0)^3 \, + \, \ldots \right) \, \left( X_0 \, - \theta \, \right) $
$

So no wonder that I could not properly capture the mean and I only had a defective R-Squared in the program I posted
last night. But when taking products of variables, it would be probably easier to take the products of standardized(as
normal or uniform) versions of the independent parts of two variables and directly add them to regression instead of
taking products of their orthogonal polynomial representations.

I had these ideas and something in this might not be right but I thought it would be nice to share them with friends. I
will try them today and in next few days and come back with what results I get.

---

### #2467 — Amin (Topic Author)
*October 10, 2024, 1:52 PM*

Friends, I thought more about better Hermite regression and how to include products and here are my ideas.

Suppose we want to regress a random variable V on random variables X, Y and their product XY. We would have to make
hermite/Legendre series of all of the above variables as

$$\, X(Z_X)\,=\, ah_0 \, + \, ah_1 \, H_1(Z_X) \,+ \, ah_2 \, H_2(Z_X) \,+ \ldots \,+ \, ah_N \, H_N(Z_X) \, $$

$$\, Y(Z_Y)\,=\, bh_0 \, + \, bh_1 \, H_1(Z_Y) \,+ \, bh_2 \, H_2(Z_Y) \,+ \ldots \,+ \, bh_N \, H_N(Z_Y) \, $$

$
$\, XY(Z_{XY})\,=\, ch_0 \, + \, ch_1 \, H_1(Z_{XY}) \,+ \, ch_2 \, H_2(Z_{XY}) \,+ \ldots \,+ \, ch_N \, H_N(Z_{XY}) \, $
$

Let us suppose that we have a total of P joint data observations of above three regressors and we include N hermite
polynomials for each of the three explanatory variable in the regression. And we also have P joint observations of the
target regressand and all of the three explanatory variables. In order to perform a regression of V on hermite
polynomials of$X$ and$Y$ and$XY$ , We would have to first construct hermite series of$X$ and$Y$ and$XY$ as shown before
the start of this paragraph. Then, for each of the pth$(p\,=\,1, \ldots,P\,)$ data observation we would have to invert
the Hermite-Series equations of$X$ and$Y$ and$XY$ for pth data observations$X_{p}$ and$Y_{p}$ and$XY_{p} $ to find
corresponding$Z_{X_{p}}$ and$Z_{Y_{p}}$ and$Z_{XY_{p}}$ . Then we would find first N Hermite polynomial values for each
of the inverted$Z_{X_{p}}$ and$Z_{Y_{p}}$ and and$Z_{XY_{p}}$ . The final regression equation would be given in the
matrix form as

\begin{equation}

\begin{bmatrix} 1 & H_1(Z_{X_1}) & \ldots & H_N(Z_{X_1}) & H_1(Z_{Y_1}).& \ldots.. & H_N(Z_{Y_1}) & H_1(Z_{XY_1}).&
\ldots.. & H_N(Z_{XY_1}) \\

1 & H_1(Z_{X_2}) & \ldots & H_N(Z_{X_2}) & H_1(Z_{Y_2}).& \ldots.. & H_N(Z_{Y_2}) & H_1(Z_{XY_2}).& \ldots.. &
H_N(Z_{XY_2})  \\ \ldots & \ldots & \ldots & \ & \ldots & \ldots.. & \ldots \\   1 & H_1(Z_{X_p}) & \ldots &
H_N(Z_{X_p}) & H_1(Z_{Y_p}) & \ldots & H_N(Z_{Y_p}) & H_1(Z_{XY_p}).& \ldots.. & H_N(Z_{XY_p}) \\ \ldots & \ldots &
\ldots & \ & \ldots & \ldots.. & \ldots \\

1 & H_1(Z_{X_P}) & \ldots & H_N(Z_{X_P})  & H_1(Z_{Y_P})  & \ldots &  H_N(Z_{YP}) & H_1(Z_{XY_P}).& \ldots.. &
H_N(Z_{XY_P}) \\

\end{bmatrix}   \begin{bmatrix} \beta_0 \\ \beta_{X,1} \\ \ldots \\ \beta_{X,N} \\ \beta_{Y,1}\\\dots \\ \beta_{Y,N} \\
\beta_{XY,1}\\\dots \\ \beta_{XY,N} \end{bmatrix} \\ \,=\, \begin{bmatrix} V_1 \\ V_2 \\ ...  \\  V_p \\ ... \\  V_P
\end{bmatrix}

\end{equation}

\begin{equation}\label{5.1.11}

\boldsymbol{H \, \beta}\,=\,\boldsymbol{v}

\end{equation}

and we solve this equation with least squares to find the regression coefficients of equation as

\begin{equation}\label{5.1.12}

\boldsymbol{\beta}\,=\,\boldsymbol{{\left(H^T\, H \right)}^{-1}\,H^T\, v }

\end{equation}

since there are three random variable regressors and Hermite-Series of each random variable includes Hermite polynomials
terms up to Nth order and there are a total of P joint data observations, then matrix$\boldsymbol{H} $ has matrix size
as$ \text{P  X (1 + 3 N)} $ ,$\boldsymbol{\beta}$ has array size of$\text{(1 +  3 N ) X 1} $ and$\boldsymbol{v}$ has
array size of$\,\text{P X 1} $ .

---

### #2468 — Amin (Topic Author)
*October 10, 2024, 2:43 PM*

I think after including the product$XY $ of two random variables$X$ and$Y$ in polynomial regression, there is no need to
include any of the products$X^{m}Y^{n}$ since order of data observations in$X^{m}Y^{n}$ would be exactly the same as the
order of observations in$XY $ and CDF of pth data observation in the product$X^{m}Y^{n}$ and in product$XY $ would be
exactly the same and therefore their underlying$Z_p$ for pth observation would be the same for these cross products. And
therefore their hermite or Legendre polynomials would be perfectly the same for all the observations and would be
perfectly linearly dependent. So we would probably need to add only hermite polynomials for one cross product for each
pair of variables in the polynomial regression.

---

### #2469 — Amin (Topic Author)
*October 11, 2024, 1:15 PM*

Friends, I went ahead and tried hermite regression again after including first order products of SDE parameters. And I
was surprised that R-Squared improved very remarkably.

This is the for the same program that I uploaded earlier. And only four parameters are being randomized as in the
program. I will be posting the new program in a few hours.

 Here are the new R-Squared values  for my data of 500 SDE Runs. First six values below are R-squared of six
coefficients of Hermite Series while seventh is R-Squared of square root of variance of the SDE being predicted from
hermite regression.

ans =

   0.996211262335416

ans =

   0.989818256721414

ans =

   0.997894091885437

ans =

   0.990556845625563

ans =

   0.956367222324832

ans =

   0.914410341043297

ans =

   0.992775316971585

Look at R^2s of six standardized hermite series coefficients and seventh square roo t

Please contrast this with R-Squared values in the older program without including first order products shown below.

ans =

   0.964711238841767

ans =

   0.888918407413745

ans =

   0.974574721623640

ans =

   0.871505792848896

ans =

   0.756961073986127

ans =

   0.747667634741192

ans =

   0.933993932423470

And when I looked at overlaid graphs of densities, I found that they were also very faithfully captured.

I think there is more room for improvement since I have not included higher order products of SDE parameters. When I
added them R-Squared sharply deteriorated and I think that I probably need to increase Legendre polynomials in
regression to capture higher order products and it might require slightly more research to determine the problem.
Secondly I did not use any moment matching of the uniform density and I would probably need to do that for better
results.

---

### #2470 — Amin (Topic Author)
*October 11, 2024, 2:25 PM*

Friends, here is the matlab program used to find above R-squared. Functions not posted are the same as posted a few days
ago.

Here I want to mention that a slight source of error is lack of perfect accuracy that is present in input data of
Hermite series coefficients. Even though I used a high order monte carlo for that purpose but still every simulation of
SDE is very slightly off the true value in a random way. This is especially true for 5th and sixth coefficients of
hermite series that have a large error and for the same reason we see a slightly decreased R-squared for last two
coefficients of the Hermite series.

In the program below, I have used first ten Legendre polynomials instead of just five Legendre polynomials I was using
for R-squared numbers in previous post. Here are the new R-squared values with ten polynomials.

Look at size of CoeffL

ans =

   0.996666096615051

ans =

   0.990820547029172

ans =

   0.998246515794144

ans =

   0.991552527866713

ans =

   0.960341519836346

ans =

   0.923863151877095

ans =

   0.993744554348142

Look at R^2s of six standardized hermite series coefficients and seventh square roo t

.

.

.

```
function [] = SDEsWithMathAIMain08()

%The mean reverting SDE is given as
%dY(t)= kappa (theta - Y(t)) dt + sigma Y(t)^gamma dZ(t)
%Y(0) = y0

kappaL=.25;%Lower range of kappa
kappaH=3;%Upper range of kappa
thetaL=.5;%Lower range of theta
thetaH=2;%Upper range of theta
y0L=.5;%Lower range of y0
y0H=2;%Higher range of y0
gammaL=.5;%Lower range of gamma
gammaH=1;%Higher range of gamma

%I am not randomizing over sigma.
%I simply take a fixed point between lower and higher range of sigma for
%every SDE in sample.

sigmaL=.1;
sigmaH=1.0;

seed=83098561;
rng(seed);

NN=500;%Number of SDE runs in the training sample. Ideally would be much larger.

Rand1(1:NN/2,1)=rand(NN/2,1);
Rand1(NN/2+1:NN,1)=1-Rand1(1:NN/2,1);%For symmetry, antithetic uniforms are used.
kappaU(1:NN)=kappaL+(kappaH-kappaL).*Rand1(1:NN,1);%Map unifrom random variates on kappa.

Rand2(1:NN/2,1)=rand(NN/2,1);
Rand2(NN/2+1:NN,1)=1-Rand2(1:NN/2,1);
thetaU(1:NN)=thetaL+(thetaH-thetaL).*Rand2(1:NN,1);%Map unifrom random variates on theta.

Rand3(1:NN/2,1)=rand(NN/2,1);
Rand3(NN/2+1:NN,1)=1-Rand3(1:NN/2,1);
y0U(1:NN)=y0L+(y0H-y0L).*Rand3(1:NN,1);%Map unifrom random variates on starting value of the SDE.

Rand4(1:NN/2,1)=rand(NN/2,1);
Rand4(NN/2+1:NN,1)=1-Rand4(1:NN/2,1);
gammaU(1:NN)=gammaL+(gammaH-gammaL).*Rand4(1:NN,1);%Map unifrom random variates on gamma.

sigmaU(1:NN)=(sigmaL+sigmaH)/2;%Taking sigma at mid of upper and lower range.

OrderL=10;%Order of Legendre polynomials to be used in regression of SDE coeffs

x12=kappaU(1:NN).*thetaU(1:NN);
[Wl12,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x12,OrderL);

x13=kappaU(1:NN).*y0U(1:NN);
[Wl13,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x13,OrderL);

x14=kappaU(1:NN).*gammaU(1:NN);
[Wl14,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x14,OrderL);

x23=thetaU(1:NN).*y0U(1:NN);
[Wl23,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x23,OrderL);

x24=thetaU(1:NN).*gammaU(1:NN);
[Wl24,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x24,OrderL);

x34=y0U(1:NN).*gammaU(1:NN);
[Wl34,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x34,OrderL);

%  x123=kappaU(1:NN).*thetaU(1:NN).*y0U(1:NN);
%  [Wl123,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x123,OrderL);
% %
%  x124=kappaU(1:NN).*thetaU(1:NN).*gammaU(1:NN);
%  [Wl124,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x124,OrderL);
% %
%  x234=thetaU(1:NN).*y0U(1:NN).*gammaU(1:NN);
%  [Wl234,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x234,OrderL);
% %
% x1234=kappaU(1:NN).*thetaU(1:NN).*y0U(1:NN).*gammaU(1:NN);
% [Wl1234,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x1234,Order);

str=input("Look at values");
SDEpaths=100000;
MOrder=14;
Order=5;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

alpha(1)=1.002379147775649;
alpha(3)=-0.000740478718368;
alpha(5)=0.001052947275469;
alpha(7)=0.000402630517679;
alpha(9)=0.000121151611625;
alpha(11)=0.000012754129466;                   0
alpha(13)=0.000000680335020;

[Zn] = StandardNormalIdealDesity02(SDEpaths,1);
[ZI] = CalculateZnAfterHermiteSeriesMultiplication(Zn,alpha,MOrder);

[W] = EvalHermiteArrayH0(ZI,Order);

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
seed0=90728436;
rng(seed0, 'combRecursive')
TtM=128;
dtM=1/32;
Random0(1:SDEpaths,1:TtM)=0;

for tt=1:TtM
%Since SDEs are simulated with different parameters in a loop. We calculate
%moment matched normal random variates for all of the time steps just once
%and input them to SDE simulation program so we do not have to generate
%these random numbers again and again every time we simulate a different
%SDE inside the SDE simulation loop.
URandom=0;
URandom(1:SDEpaths/2)=0;
URandom=rand(size(URandom));
URandom(SDEpaths/2+1:SDEpaths)=1-URandom(1:SDEpaths/2);
[URandomS,I]=sort(URandom);

Random1=ZI(I);

Random0(1:SDEpaths,tt)=Random1(1:SDEpaths);
end
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Run this loop and above loop only once and save the data on disk as below.
%Then comment both these loops and keep reading the data from disk.
for nn=1:NN
 nn
 NN
[coeff] =
MeanRevertingMonteCarloDensity02(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM);
 Coeff(nn,1:TtM,1:Order+1)=coeff(1:TtM,1:Order+1);
end

 save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04C.mat","Coeff")

 str=input("I have saved the densities coefficients variable");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Uncomment below to read the data from disk.
load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04C.mat","Coeff")

Tt=TtM;
%Dimensions of Coeff are Coeff(1:NN,1:TtM,1:Order+1).Below we take one time
%slice between 1 and TtM. I have taken slice 72 that occurs at time
%72*.03625=
%You can comment the SDE simulations loop and continue to load the
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.
%
%TimeSlice variable below
Ts=72;
CoeffH(1:NN,1:Order+1)=Coeff(1:NN,Ts,1:Order+1);
TT=Ts*dtM;%Time at end of chosen slice. This will be used in analytic calculation of SDE mean later.
%We will replace the first mean coefficient of zeroth hermite associated
%with the Hermite series of SDEs with the analytic value.

%Below we calculate square root of variance(sum of hermite coefficients squared formula) to standardize the coefficients
VarSqRt(1:NN,1)=
sqrt(CoeffH(1:NN,2).^2+CoeffH(1:NN,3).^2*2+CoeffH(1:NN,4).^2*6+CoeffH(1:NN,5).^2*24+CoeffH(1:NN,6).^2*120);
%Below are six standardized coefficients
SCoeff(1:NN,1:6)=CoeffH(1:NN,1:6)./VarSqRt(1:NN,1);

str=input("Reached Level 1");

for mm=1:1
    Ukappa(1:NN)=-1+2*Rand1(1:NN);%Convert first uniform to between zero and one to between -1 and +1
    Utheta(1:NN)=-1+2*Rand2(1:NN);%Convert second uniform to between zero and one to between -1 and +1
    Uy0(1:NN)=-1+2*Rand3(1:NN);%Convert third uniform to between zero and one to between -1 and +1
    Ugamma(1:NN)=-1+2*Rand4(1:NN);%Convert fourth uniform to between zero and one to between -1 and +1

     for qq=1:6
     Yl(1:NN,qq)=SCoeff(1:NN,qq); %First six standardized coefficients to be predicted.
     end
     Yl(1:NN,7)=VarSqRt(1:NN);%Square root of variance used to standardize has to be predicted as well.
end
clf;
[XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,1),NN,25,10 )
plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
str=input("Look at density of 1st coeff")

[XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,2),NN,25,10 )
plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
str=input("Look at density of 2nd coeff")

%

OrderL0=OrderL+1;

 [Wl1] = EvalLegendreArrayL0(Ukappa,OrderL);%Matrix in which zeroth Legendre and first six Legendre polynomilas are
evaluated at uniform values.
 [Wl2] = EvalLegendreArrayL0(Utheta,OrderL);
 [Wl3] = EvalLegendreArrayL0(Uy0,OrderL);
 [Wl4] = EvalLegendreArrayL0(Ugamma,OrderL);

%Below Tile all of the Legendre polynomials of each of the four random
%parameters in a single matrix and use for least square regression. Zeroth
%Legendre is evaluated in each of the four matrices and has to be removed
%from tiling other than just including one time.
WL(:,1:OrderL0)=Wl1(:,1:OrderL0);
WL(:,OrderL0+1:OrderL0+OrderL)=Wl2(:,2:OrderL0);
WL(:,OrderL0+OrderL+1:OrderL0+2*OrderL)=Wl3(:,2:OrderL0);
WL(:,OrderL0+2*OrderL+1:OrderL0+3*OrderL)=Wl4(:,2:OrderL0);
 WL(:,OrderL0+3*OrderL+1:OrderL0+4*OrderL)=Wl12(:,2:OrderL0);
 WL(:,OrderL0+4*OrderL+1:OrderL0+5*OrderL)=Wl13(:,2:OrderL0);
 WL(:,OrderL0+5*OrderL+1:OrderL0+6*OrderL)=Wl14(:,2:OrderL0);
 WL(:,OrderL0+6*OrderL+1:OrderL0+7*OrderL)=Wl23(:,2:OrderL0);
 WL(:,OrderL0+7*OrderL+1:OrderL0+8*OrderL)=Wl24(:,2:OrderL0);
 WL(:,OrderL0+8*OrderL+1:OrderL0+9*OrderL)=Wl34(:,2:OrderL0);
% WL(:,OrderL0+9*OrderL+1:OrderL0+10*OrderL)=Wl123(:,2:OrderL0);
% WL(:,OrderL0+10*OrderL+1:OrderL0+11*OrderL)=Wl124(:,2:OrderL0);
% WL(:,OrderL0+11*OrderL+1:OrderL0+12*OrderL)=Wl234(:,2:OrderL0);
% WL(:,OrderL0+12*OrderL+1:OrderL0+13*OrderL)=Wl1234(:,2:OrderL0);
CoeffL=inv(WL'*WL)*(WL'*Yl);%Legendre coefficients to predict seven variables. six standardized coefficients
%and one square root of variance of each SDE.

CoeffL
size(WL)
size(CoeffL)

str=input("Look at size of CoeffL");
     aa(:,1:7)=Yl(:,1:7);
     for nn=1:NN
     b(nn,1:7)=CoeffL(1,1:7);
     end
    for rr=2:OrderL+1

        b(:,1:7)=b(:,1:7)+CoeffL(rr,1:7).*Wl1(:,rr)+CoeffL(rr+OrderL,1:7).*Wl2(:,rr)+ ...
            CoeffL(rr+2*OrderL,1:7).*Wl3(:,rr)+CoeffL(rr+3*OrderL,1:7).*Wl4(:,rr)+ ...
            CoeffL(rr+4*OrderL,1:7).*Wl12(:,rr)+CoeffL(rr+5*OrderL,1:7).*Wl13(:,rr)+ ...
            CoeffL(rr+6*OrderL,1:7).*Wl14(:,rr)+CoeffL(rr+7*OrderL,1:7).*Wl23(:,rr)+ ...
            CoeffL(rr+8*OrderL,1:7).*Wl24(:,rr)+CoeffL(rr+9*OrderL,1:7).*Wl34(:,rr);%+ ...
            %CoeffL(rr+10*OrderL,1:7).*Wl123(:,rr)+CoeffL(rr+11*OrderL,1:7).*Wl24(:,rr)+ ...
            %CoeffL(rr+12*OrderL,1:7).*Wl234(:,rr);%+CoeffL(rr+13*OrderL,1:7).*Wl1234(:,rr);
%
    end

    %Below are seven calculations of R-squared for each of
    %the standardized six coefficients and seventh value of
    1-sum((aa(:,1)-b(:,1)).^2)/sum((aa(:,1)-sum(aa(:,1))/(NN)).^2)
    1-sum((aa(:,2)-b(:,2)).^2)/sum((aa(:,2)-sum(aa(:,2))/(NN)).^2)
    1-sum((aa(:,3)-b(:,3)).^2)/sum((aa(:,3)-sum(aa(:,3))/(NN)).^2)
    1-sum((aa(:,4)-b(:,4)).^2)/sum((aa(:,4)-sum(aa(:,4))/(NN)).^2)
    1-sum((aa(:,5)-b(:,5)).^2)/sum((aa(:,5)-sum(aa(:,5))/(NN)).^2)
    1-sum((aa(:,6)-b(:,6)).^2)/sum((aa(:,6)-sum(aa(:,6))/(NN)).^2)
    1-sum((aa(:,7)-b(:,7)).^2)/sum((aa(:,7)-sum(aa(:,7))/(NN)).^2)

    str=input("Look at R^2s of six standardized hermite series coefficients and seventh square roo t");

for nn=1:NN

    cc(1:6)=b(nn,1:6).*b(nn,7);
    Yl0(1:6)=Yl(nn,1:6).*VarSqRt(nn);
    cc(1:6)
    Yl0(1:6)
    cc(1)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));%Replacing predicted value of mean with analytic value.
        clf;
     cc(1)
     nn
     PlotHermiteSeriesDensityAndRvGraph(cc(1),cc(2:Order+1),'r');

     hold on

     PlotHermiteSeriesDensityAndRvGraph(Yl0(1),Yl0(2:Order+1),'g');
     nn
     str=input("Look at comparison of graphs--Green is data and red is our interpolation from coefficients");

end

end

```

.

.

.

```
function [Wy,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Yin,Order)

Ndata=length(Yin);

Hz=LegendrePoly(Order);
MeanYin=sum(Yin(1:Ndata))/Ndata;
Ym(1:Ndata)=Yin(1:Ndata)-MeanYin;
YmVar=sum(Ym(1:Ndata).^2)/Ndata;
Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);

%Mtable=readtable('C:\Users\Lenovo\Documents\MATLAB\MATLAB1\MomentMatchParams08.txt');
%[ZI] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable);

UI(1:Ndata)=-1+2/Ndata*(1:Ndata)-1/Ndata;

%[Zn] = StandardNormalIdealDesity02(Ndata,1);
%[ZI] = CalculateZI(Zn);

%ZI=Zn;
%Below W is the design matrix for least squares regression i.e the matrix
%that contains all the hermite polynomials calculated at ideal normal
%density grid of size Ndata.
[W] = EvalLegendreArrayL0(UI,Order);

%We first sort the data so that we can assign one appropriate Z-grid
%point(and associated hermite polynomials calculated at that grid point)
%to each data element. This ideal normal density Z-grid is
%constructed so that its size is equal to data observations count. We
%suppose that first derivative of random variables with repsect to Z
%does not switch sign meaning that increasing values of data
%observations have to aligned with increasing values of ideal normal
%density grid.
[Ys,I]=sort(Y(1:Ndata));
%In the line below, the data sort is reversed so that now the ideal
%normal density grid elements assigned to various observations of random
%variable face it on data observations index. For details, Please look
%on interent the definition of matlab sort command with role of "I"
%in output and how it alters the index.
Us1(I(1:Ndata))=UI(1:Ndata);
%Below the values to be regressed facing the design matrix are assigned
%Ymu(1:Ndata,1)=Ys(1:Ndata);
%Below, implement least squares regression.
%coeff=inv(W'*W)*(W'*Ymu);
%Store in coefficietns array of all random varaibles
%Coeff(1:Order+1)= coeff(1:Order+1,1);
%Store the associated Z in Z-array of all coefficients.
Uy(1:Ndata)=Us1(1:Ndata);

Wy(I(1:Ndata),:)=W(1:Ndata,:);

%Wy2(1:Ndata,:)=EvalLegendreArrayL0(Uy,Order);

%Wy-Wy2

% for nn=1:Ndata
%    Uy(nn)
%
%    EvalLegendreArrayL0(Uy(nn),Order);
%
% end

%Coeff(1:Order+1)=Coeff(1:Order+1).*sqrt(YmVar);
%Coeff(1)=Coeff(1)+MeanYin;

end
```

.

.

.

---

### #2471 — Amin (Topic Author)
*October 11, 2024, 6:12 PM*

Friends, I slightly changed the program and was able to get products of all order to work. I still have to match the
moments of uniform that might slightly improve the results further. There would also be slight random inaccuracy in
coefficients of monte carlo densities and its slight impact on R-squared has to be accounted.  Here is the new
R-Squared.

ans =

   0.999599817531612

ans =

   0.992874115170977

ans =

   0.999016103418393

ans =

   0.993441778857703

ans =

   0.968160138671442

ans =

   0.937355477144121

ans =

   0.995819669488013

Look at R^2s of six standardized hermite series coefficients and seventh square roo t

.

.

```
function [] = SDEsWithMathAIMain08()

%The mean reverting SDE is given as
%dY(t)= kappa (theta - Y(t)) dt + sigma Y(t)^gamma dZ(t)
%Y(0) = y0

kappaL=.25;%Lower range of kappa
kappaH=3;%Upper range of kappa
thetaL=.5;%Lower range of theta
thetaH=2;%Upper range of theta
y0L=.5;%Lower range of y0
y0H=2;%Higher range of y0
gammaL=.5;%Lower range of gamma
gammaH=1;%Higher range of gamma

%I am not randomizing over sigma.
%I simply take a fixed point between lower and higher range of sigma for
%every SDE in sample.

sigmaL=.1;
sigmaH=1.0;

seed=83098561;
rng(seed);

NN=500;%Number of SDE runs in the training sample. Ideally would be much larger.

Rand1(1:NN/2,1)=rand(NN/2,1);
Rand1(NN/2+1:NN,1)=1-Rand1(1:NN/2,1);%For symmetry, antithetic uniforms are used.
kappaU(1:NN)=kappaL+(kappaH-kappaL).*Rand1(1:NN,1);%Map unifrom random variates on kappa.

Rand2(1:NN/2,1)=rand(NN/2,1);
Rand2(NN/2+1:NN,1)=1-Rand2(1:NN/2,1);
thetaU(1:NN)=thetaL+(thetaH-thetaL).*Rand2(1:NN,1);%Map unifrom random variates on theta.

Rand3(1:NN/2,1)=rand(NN/2,1);
Rand3(NN/2+1:NN,1)=1-Rand3(1:NN/2,1);
y0U(1:NN)=y0L+(y0H-y0L).*Rand3(1:NN,1);%Map unifrom random variates on starting value of the SDE.

Rand4(1:NN/2,1)=rand(NN/2,1);
Rand4(NN/2+1:NN,1)=1-Rand4(1:NN/2,1);
gammaU(1:NN)=gammaL+(gammaH-gammaL).*Rand4(1:NN,1);%Map unifrom random variates on gamma.

sigmaU(1:NN)=(sigmaL+sigmaH)/2;%Taking sigma at mid of upper and lower range.

OrderL=10;%Order of Legendre polynomials to be used in regression of SDE coeffs

x12=kappaU(1:NN).*thetaU(1:NN);
[Wl12,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x12,OrderL);

x13=kappaU(1:NN).*y0U(1:NN);
[Wl13,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x13,OrderL);

x14=kappaU(1:NN).*gammaU(1:NN);
[Wl14,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x14,OrderL);

x23=thetaU(1:NN).*y0U(1:NN);
[Wl23,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x23,OrderL);

x24=thetaU(1:NN).*gammaU(1:NN);
[Wl24,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x24,OrderL);

x34=y0U(1:NN).*gammaU(1:NN);
[Wl34,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x34,OrderL);

  x123=kappaU(1:NN).*thetaU(1:NN).*y0U(1:NN);
  [Wl123,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x123,OrderL);
% %
  x124=kappaU(1:NN).*thetaU(1:NN).*gammaU(1:NN);
  [Wl124,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x124,OrderL);
% %
  x234=thetaU(1:NN).*y0U(1:NN).*gammaU(1:NN);
  [Wl234,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x234,OrderL);
% %
 x1234=kappaU(1:NN).*thetaU(1:NN).*y0U(1:NN).*gammaU(1:NN);
 [Wl1234,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x1234,OrderL);

str=input("Look at values");
SDEpaths=100000;
MOrder=14;
Order=5;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

alpha(1)=1.002379147775649;
alpha(3)=-0.000740478718368;
alpha(5)=0.001052947275469;
alpha(7)=0.000402630517679;
alpha(9)=0.000121151611625;
alpha(11)=0.000012754129466;                   0
alpha(13)=0.000000680335020;

[Zn] = StandardNormalIdealDesity02(SDEpaths,1);
[ZI] = CalculateZnAfterHermiteSeriesMultiplication(Zn,alpha,MOrder);

[W] = EvalHermiteArrayH0(ZI,Order);

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
seed0=90728436;
rng(seed0, 'combRecursive')
TtM=128;
dtM=1/32;
Random0(1:SDEpaths,1:TtM)=0;

for tt=1:TtM
%Since SDEs are simulated with different parameters in a loop. We calculate
%moment matched normal random variates for all of the time steps just once
%and input them to SDE simulation program so we do not have to generate
%these random numbers again and again every time we simulate a different
%SDE inside the SDE simulation loop.
URandom=0;
URandom(1:SDEpaths/2)=0;
URandom=rand(size(URandom));
URandom(SDEpaths/2+1:SDEpaths)=1-URandom(1:SDEpaths/2);
[URandomS,I]=sort(URandom);

Random1=ZI(I);

Random0(1:SDEpaths,tt)=Random1(1:SDEpaths);
end
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Run this loop and above loop only once and save the data on disk as below.
%Then comment both these loops and keep reading the data from disk.
for nn=1:NN
 nn
 NN
[coeff] =
MeanRevertingMonteCarloDensity02(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM);
 Coeff(nn,1:TtM,1:Order+1)=coeff(1:TtM,1:Order+1);
end

 save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04C.mat","Coeff")

 str=input("I have saved the densities coefficients variable");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Uncomment below to read the data from disk.
load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04C.mat","Coeff")

Tt=TtM;
%Dimensions of Coeff are Coeff(1:NN,1:TtM,1:Order+1).Below we take one time
%slice between 1 and TtM. I have taken slice 72 that occurs at time
%72*.03625=
%You can comment the SDE simulations loop and continue to load the
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.
%
%TimeSlice variable below
Ts=72;
CoeffH(1:NN,1:Order+1)=Coeff(1:NN,Ts,1:Order+1);
TT=Ts*dtM;%Time at end of chosen slice. This will be used in analytic calculation of SDE mean later.
%We will replace the first mean coefficient of zeroth hermite associated
%with the Hermite series of SDEs with the analytic value.

%Below we calculate square root of variance(sum of hermite coefficients squared formula) to standardize the coefficients
VarSqRt(1:NN,1)=
sqrt(CoeffH(1:NN,2).^2+CoeffH(1:NN,3).^2*2+CoeffH(1:NN,4).^2*6+CoeffH(1:NN,5).^2*24+CoeffH(1:NN,6).^2*120);
%Below are six standardized coefficients
SCoeff(1:NN,1:6)=CoeffH(1:NN,1:6)./VarSqRt(1:NN,1);

str=input("Reached Level 1");

for mm=1:1
    Ukappa(1:NN)=-1+2*Rand1(1:NN);%Convert first uniform to between zero and one to between -1 and +1
    Utheta(1:NN)=-1+2*Rand2(1:NN);%Convert second uniform to between zero and one to between -1 and +1
    Uy0(1:NN)=-1+2*Rand3(1:NN);%Convert third uniform to between zero and one to between -1 and +1
    Ugamma(1:NN)=-1+2*Rand4(1:NN);%Convert fourth uniform to between zero and one to between -1 and +1

     for qq=1:6
     Yl(1:NN,qq)=SCoeff(1:NN,qq); %First six standardized coefficients to be predicted.
     end
     Yl(1:NN,7)=VarSqRt(1:NN);%Square root of variance used to standardize has to be predicted as well.
end
clf;
[XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,1),NN,25,10 )
plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
str=input("Look at density of 1st coeff")

[XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,2),NN,25,10 )
plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
str=input("Look at density of 2nd coeff")

%

OrderL0=OrderL+1;

 [Wl1] = EvalLegendreArrayL0(Ukappa,OrderL);%Matrix in which zeroth Legendre and first six Legendre polynomilas are
evaluated at uniform values.
 [Wl2] = EvalLegendreArrayL0(Utheta,OrderL);
 [Wl3] = EvalLegendreArrayL0(Uy0,OrderL);
 [Wl4] = EvalLegendreArrayL0(Ugamma,OrderL);

%Below Tile all of the Legendre polynomials of each of the four random
%parameters in a single matrix and use for least square regression. Zeroth
%Legendre is evaluated in each of the four matrices and has to be removed
%from tiling other than just including one time.
WL(:,1:OrderL0)=Wl1(:,1:OrderL0);
WL(:,OrderL0+1:OrderL0+OrderL)=Wl2(:,2:OrderL0);
WL(:,OrderL0+OrderL+1:OrderL0+2*OrderL)=Wl3(:,2:OrderL0);
WL(:,OrderL0+2*OrderL+1:OrderL0+3*OrderL)=Wl4(:,2:OrderL0);
 WL(:,OrderL0+3*OrderL+1:OrderL0+4*OrderL)=Wl12(:,2:OrderL0);
 WL(:,OrderL0+4*OrderL+1:OrderL0+5*OrderL)=Wl13(:,2:OrderL0);
 WL(:,OrderL0+5*OrderL+1:OrderL0+6*OrderL)=Wl14(:,2:OrderL0);
 WL(:,OrderL0+6*OrderL+1:OrderL0+7*OrderL)=Wl23(:,2:OrderL0);
 WL(:,OrderL0+7*OrderL+1:OrderL0+8*OrderL)=Wl24(:,2:OrderL0);
 WL(:,OrderL0+8*OrderL+1:OrderL0+9*OrderL)=Wl34(:,2:OrderL0);
 WL(:,OrderL0+9*OrderL+1:OrderL0+10*OrderL)=Wl123(:,2:OrderL0);
 WL(:,OrderL0+10*OrderL+1:OrderL0+11*OrderL)=Wl124(:,2:OrderL0);
 WL(:,OrderL0+11*OrderL+1:OrderL0+12*OrderL)=Wl234(:,2:OrderL0);
 WL(:,OrderL0+12*OrderL+1:OrderL0+13*OrderL)=Wl1234(:,2:OrderL0);
CoeffL=inv(WL'*WL)*(WL'*Yl);%Legendre coefficients to predict seven variables. six standardized coefficients
%and one square root of variance of each SDE.

CoeffL
size(WL)
size(CoeffL)

str=input("Look at size of CoeffL");
     aa(:,1:7)=Yl(:,1:7);
     for nn=1:NN
     b(nn,1:7)=CoeffL(1,1:7);
     end
    for rr=2:OrderL+1

        b(:,1:7)=b(:,1:7)+CoeffL(rr,1:7).*Wl1(:,rr)+CoeffL(rr+OrderL,1:7).*Wl2(:,rr)+ ...
            CoeffL(rr+2*OrderL,1:7).*Wl3(:,rr)+CoeffL(rr+3*OrderL,1:7).*Wl4(:,rr)+ ...
            CoeffL(rr+4*OrderL,1:7).*Wl12(:,rr)+CoeffL(rr+5*OrderL,1:7).*Wl13(:,rr)+ ...
            CoeffL(rr+6*OrderL,1:7).*Wl14(:,rr)+CoeffL(rr+7*OrderL,1:7).*Wl23(:,rr)+ ...
            CoeffL(rr+8*OrderL,1:7).*Wl24(:,rr)+CoeffL(rr+9*OrderL,1:7).*Wl34(:,rr)+ ...
            CoeffL(rr+10*OrderL,1:7).*Wl123(:,rr)+CoeffL(rr+11*OrderL,1:7).*Wl124(:,rr)+ ...
            CoeffL(rr+12*OrderL,1:7).*Wl234(:,rr)+CoeffL(rr+13*OrderL,1:7).*Wl1234(:,rr);
%
    end

    %Below are seven calculations of R-squared for each of
    %the standardized six coefficients and seventh value of
    1-sum((aa(:,1)-b(:,1)).^2)/sum((aa(:,1)-sum(aa(:,1))/(NN)).^2)
    1-sum((aa(:,2)-b(:,2)).^2)/sum((aa(:,2)-sum(aa(:,2))/(NN)).^2)
    1-sum((aa(:,3)-b(:,3)).^2)/sum((aa(:,3)-sum(aa(:,3))/(NN)).^2)
    1-sum((aa(:,4)-b(:,4)).^2)/sum((aa(:,4)-sum(aa(:,4))/(NN)).^2)
    1-sum((aa(:,5)-b(:,5)).^2)/sum((aa(:,5)-sum(aa(:,5))/(NN)).^2)
    1-sum((aa(:,6)-b(:,6)).^2)/sum((aa(:,6)-sum(aa(:,6))/(NN)).^2)
    1-sum((aa(:,7)-b(:,7)).^2)/sum((aa(:,7)-sum(aa(:,7))/(NN)).^2)

    str=input("Look at R^2s of six standardized hermite series coefficients and seventh square roo t");

for nn=1:NN

    cc(1:6)=b(nn,1:6).*b(nn,7);
    Yl0(1:6)=Yl(nn,1:6).*VarSqRt(nn);
    cc(1:6)
    Yl0(1:6)
    cc(1)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));%Replacing predicted value of mean with analytic value.
        clf;
     cc(1)
     nn
     PlotHermiteSeriesDensityAndRvGraph(cc(1),cc(2:Order+1),'r');

     hold on

     PlotHermiteSeriesDensityAndRvGraph(Yl0(1),Yl0(2:Order+1),'g');
     nn
     str=input("Look at comparison of graphs--Green is data and red is our interpolation from coefficients");

end

end

```

.

.

Friends, here are graphs of first twenty densities in the sample and how well they are predicted by regression on the
coefficients of Hermite series. It does need improvement but it is decently good only after ten days of research on the
project.  I am sure we will be able to quite further improve the densities fit with some more effort. In the grpahs
Green is original monte carlo density and red is density from regression of Hermite series coefficients on four random
parameters.

.

.

[![Image](../images/i.postimg.cc/1zgvGXMg/MathAI01.png)](https://postimg.cc/kVmN9n09)

[![Image](../images/i.postimg.cc/rwZhRxGX/MathAI02.png)](https://postimg.cc/5Xv5ZHkn)

[![Image](../images/i.postimg.cc/NjjJ0pHk/MathAI03.png)](https://postimg.cc/KRCrq7Q1)

[![Image](../images/i.postimg.cc/L6TQRrns/MathAI04.png)](https://postimg.cc/KR1DDp7X)

[![Image](../images/i.postimg.cc/hPgZkS4w/MathAI05.png)](https://postimg.cc/yWQT9CZX)

[![Image](../images/i.postimg.cc/pVK1c9vz/MathAI06.png)](https://postimg.cc/145Hf3f3)

[![Image](../images/i.postimg.cc/FzXCsvyY/MathAI07.png)](https://postimg.cc/JDK5P9d8)

[![Image](../images/i.postimg.cc/fL9gNy94/MathAI08.png)](https://postimg.cc/MMzY0W5t)

[![Image](../images/i.postimg.cc/T1j7Ks0C/MathAI09.png)](https://postimg.cc/kR4FZfkb)

[![Image](../images/i.postimg.cc/MG4rNVXb/MathAI10.png)](https://postimg.cc/5HB3FHB6)

[![Image](../images/i.postimg.cc/Zn1wDSRb/MathAI11.png)](https://postimg.cc/T5JjpBgF)

[![Image](../images/i.postimg.cc/sxBncX3H/MathAI12.png)](https://postimg.cc/m1sNZTz7)

[![Image](../images/i.postimg.cc/C1rPkDpf/MathAI13.png)](https://postimg.cc/wyJQd1v6)

[![Image](../images/i.postimg.cc/vmzS8kPh/MathAI14.png)](https://postimg.cc/p9mBqGM5)

[![Image](../images/i.postimg.cc/zBG2y76r/MathAI15.png)](https://postimg.cc/nsNG54nR)

[![Image](../images/i.postimg.cc/jjKFbthC/MathAI16.png)](https://postimg.cc/68j0VsgN)

[![Image](../images/i.postimg.cc/gkX5yMJc/MathAI17.png)](https://postimg.cc/KRbJxDBC)

[![Image](../images/i.postimg.cc/Nf3nd196/MathAI18.png)](https://postimg.cc/ykTnd3Tx)

[![Image](../images/i.postimg.cc/HkbhRVXf/MathAI19.png)](https://postimg.cc/75Y9TPBV)

[![Image](../images/i.postimg.cc/wxbZmK9b/MathAI20.png)](https://postimg.cc/ThgCz4Lr)

---

### #2472 — Amin (Topic Author)
*October 11, 2024, 7:02 PM*

Friends, I was able to further increase R-squared and now fit to densities is also vastly improved. I increased the
order of Legendre polynomials in regression of hermite series coefficients to thirty one from previous value of ten.

All you have to do is choose a high number of Legendre coefficients by choosing OrderL=31 or some other closeby high
value.

.

.

.

ans =

   0.999978573064999

ans =

   0.999113941435062

ans =

   0.999899091991578

ans =

   0.999114982325132

ans =

   0.995549914939907

ans =

   0.991472712364443

ans =

   0.999563442730444

I have shown fit to densities again and these are the same densities that were fitted in previous post. Now fit is much
improved.

[![Image](../images/i.postimg.cc/K8qD9TYG/Math-AINew01.png)](https://postimg.cc/G4DDtHYV)

[![Image](../images/i.postimg.cc/pLXBYCRc/Math-AINew02.png)](https://postimg.cc/dLpdJ87G)

[![Image](../images/i.postimg.cc/DycgXHkb/Math-AINew03.png)](https://postimg.cc/2VVhpH5z)

[![Image](../images/i.postimg.cc/9F2bzVSh/Math-AINew04.png)](https://postimg.cc/vDPfNRbq)

[![Image](../images/i.postimg.cc/G3Gzc9XK/Math-AINew05.png)](https://postimg.cc/qgB2wBV6)

[![Image](../images/i.postimg.cc/GtFjzS4V/Math-AINew06.png)](https://postimg.cc/SYK8xd7f)

[![Image](../images/i.postimg.cc/WzLnGP10/Math-AINew07.png)](https://postimg.cc/Fdp3v8cK)

[![Image](../images/i.postimg.cc/W4yS4ZRW/Math-AINew08.png)](https://postimg.cc/LqzjCn8L)

[![Image](../images/i.postimg.cc/C1f7nKSF/Math-AINew09.png)](https://postimg.cc/1nswLs8T)

[![Image](../images/i.postimg.cc/5tyn13rQ/Math-AINew10.png)](https://postimg.cc/Ty8rJrfT)

[![Image](../images/i.postimg.cc/Qd00RPfr/Math-AINew11.png)](https://postimg.cc/gxLVhM9M)

[![Image](../images/i.postimg.cc/nhH3SZYk/Math-AINew12.png)](https://postimg.cc/svNP1kLQ)

[![Image](../images/i.postimg.cc/X7K2gXFq/Math-AINew13.png)](https://postimg.cc/Yh9frrdB)

[![Image](../images/i.postimg.cc/tCGSPFs8/Math-AINew14.png)](https://postimg.cc/ThQJvLqc)

[![Image](../images/i.postimg.cc/BZK7Xmnx/Math-AINew15.png)](https://postimg.cc/yW7yGX9d)

[![Image](../images/i.postimg.cc/0jDVFyBt/Math-AINew16.png)](https://postimg.cc/rRyGtMcW)

[![Image](../images/i.postimg.cc/4dr8W9B7/Math-AINew17.png)](https://postimg.cc/njGYzC8p)

[![Image](../images/i.postimg.cc/N0CCrVXx/Math-AINew18.png)](https://postimg.cc/Y4gz5db4)

[![Image](../images/i.postimg.cc/3RySjBCQ/Math-AINew19.png)](https://postimg.cc/xJ23nL46)

[![Image](../images/i.postimg.cc/nLhwrZXz/Math-AINew20.png)](https://postimg.cc/4Yj12Dbk)

---

### #2473 — Amin (Topic Author)
*October 12, 2024, 9:06 AM*

Friends, a high quality, fine-grained simulation of SDEs and a proper conversion to hermite polynomial coefficients is
very important for good regressions. Any case of instability in conversion of SDE densities to hermite polynomial
coefficients will quickly degrade the whole Legendre regression and I have seen it happen in some samples.

My laptop is rather slow and can take quite many hours for larger simulations and it is a bit difficult for me to work
with different samples and different examples everyday.

---

### #2474 — Amin (Topic Author)
*October 12, 2024, 11:52 AM*

Friends, there are several kinds of densities of interest that do not have orthogonal polynomials. And as it turns out, it is quite easy to find orthogonal polynomials for a large number of densities (with respect to density weights). You do not necessarily need to solve an appropriate differential equation to find orthogonal polynomials and you could easily do that with a bit of calculus and algebra. I have earlier discussed it previously in post # 2269 here:https://forum.wilmott.com/viewtopic.php?t=99702&start=2265#p880664

Here I explain the ideas again with latexed equations.

In construction of orhtogonal polynomials with respect to different density weights, we choose coefficients of various
orthogonal polynomials recursively by solving equations that ensure orthogonality of each polynomial with respect to all
previous polynomials and also solve one condition that ensures that each polynomial is also ortho-normalized. Here I
give the details. Suppose the arbitrary density with respect to which we want to find orthogonal polynomials is given as
p(X). We suppose that$\int\limits_{0}^{\infty} \, p(X)dX \,=\,1 $ . I have integrated from zero to infinity but this
integration would be over complete support of the density. If this density weight integral is not unity, we will have to
change our equations below appropriately.

The zeroth order polynomial is chosen as a constant.

$$P_0(X)= 1$$

The first polynomial can be

$$P_1(X)=a_1 X + a_0 $$

where a0 and a1 have to be found from equations

For P0 and P1 to be orthogonal the integral of product of P0(X) and P1(X) when evaluated with respect to specified
density should be zero. Limits could be$-\infty$ to$+\infty$ or zero to$+\infty$ or as dictated by support of the
density.

$$\int\limits_{0}^{\infty} P_0(X)\,P_1(X) \, p(X) dX \,=\,0 $$

and we can have one non-linear equation for normality. This condition is not necessary and can also be represented by
various alternate forms like constraints on leading coefficients etc but this is a useful condition.

$$\int\limits_{0}^{\infty} P_1(X)\,P_1(X) \, p(X) dX \,=\,1 $$

We can write the above integral equations as linear equations including expectations of powers of X with respect to our
weight density

$$\, a_0 \,+ \, a_1 \, E[X]\,=\,0$$

$$\,{a_0^2} \,+\, 2 \,a_0\, a_1 \,E[X]\, + \,{a_1}^2 \,E[X^2] \,= \,1$$

Above polynomial has two unknown coefficients and we have specified two independent conditions to find those
coefficients.

Once first polynomial is fixed, the second polynomial is

$$P_2(X)\,=\,b_0\,+\, b_1\, X \, +\,  b_2\, X^2 $$

But we know that second polynomial has to be orthogonal to zeroth and first polynomial and we want it to be normalized
so we get the following two equations for orthogonality and one last equation for normality as

$$\int\limits_{0}^{\infty} P_2(X)\,P_0(X) \, p(X) dX \,=\,0 $$

$$\int\limits_{0}^{\infty} P_2(X)\,P_1(X) \, p(X) dX \,=\,0 $$

$$\int\limits_{0}^{\infty} P_2(X)\,P_2(X) \, p(X) dX \,=\,1 $$

Converting above integral equations to equations with expectations where expectations are with respect to density
weight, we get

$$\, b_0\, + \,b_1\, E[X]\, + \,b_2\, E[X^2] =0$$

$
$\, a_0\, b_0\, +\, a_0\, b_1 \,E[X]\, +\, a_0\, b_2 \,E[X^2]\, +\, a_1\, b_0\, E[X]\, + \,a_1\, b_1 \,E[X^2] \,+\, a_1\, b_2\, E[X^3]\,=\,0 $
$

$
$\, {b_0}^2 \,+\, 2\, b_0\, b_1\, E[X]\, +\, 2\, b_0\, b_2\, E[X^2]\,   +\, {b_1}^2 \, E[X^2] \,+\,2\, b_1\, b_2\, E[X^3] \,+\, {b2}^2 \,E[X^4]\, =\,1$
$

This will give us three equations for three unknown coefficients that can be solved to find the coefficients of 2nd
polynomial.

We repeat the procedure for third polynomial and write it with undetermined coefficients as

$$P_3(X)= \,c_0\,+\, c_1\, X\, +\, c_2\, X^2 \,+ \,c_3 \,X^3 \,$$

We write three orthogonality equations with respect to first three polynomials and one normality equation as

$$\int\limits_{0}^{\infty} P_3(X)\,P_0(X) \, p(X) dX \,=\,0 $$

$$\int\limits_{0}^{\infty} P_3(X)\,P_1(X) \, p(X) dX \,=\,0 $$

$$\int\limits_{0}^{\infty} P_3(X)\,P_2(X) \, p(X) dX \,=\,0 $$

$$\int\limits_{0}^{\infty} P_3(X)\,P_3(X) \, p(X) dX \,=\,1 $$

Converting above integral equations to equations with expectations with respect to density weight, we get

$$ \,c_0\, +\, c_1 \,E[X]\, +\, c_2\, E[X^2] \,+\, c_3\, E[X]^3 \,=\,0 $$

$
$\, a_0\, c_0\, +\, a_0\, c_1\, E[X] \,+ \,a_0\, c_2\, E[X^2] \,+\, a_0\, c_3\, E[X^3] \,+ a_1\, c_0\, E[X]\, +\, a_1\, c_1\, E[X^2] +   a_1\, c_2 \,E[X^3]\, \\+\, a_1\, c_3\, E[X^4]\,=\,0$
$

$
$\, b_0\, c_0\, +\, b_0\, c_1 \, E[X]\, + \,b_0\, c_2\, E[X^2]\, +\, b_0\, c_3\, E[X^3]\, +\, b_1\, c_0\, E[X] \,+\, b_1\, c_1\, E[X^2]\, \\+\, b_1\, c_2\, \, [E[X^3]\,+\, b_1\, c_3\, E[X^4]\,+ \,b_2\, c_0\, E[X^2]\, +\, b_2\, c_1\, E[X^3]\, +\, b_2\, c_2\, E[X^4]\,+\, b_2\, c_3\, E[X^5]\,=\,0\, $
$

$
$\, {c_0}^2 \,+\, 2\, c_0\, c_1\, E[X] \,+ \,2 \,c_0\, c2 \,E[X^2]\, +\,2\, c_0\, c_3\, E[X^3]\,  +\, {c_1}^2\, E[X^2]\, +\,2\, c_1\, c_2\, E[X^3]\, \\+\,2\, c_1\, c_3\, E[X^4]\, +\, {c_2}^2 \,E[X^4]\, +\, c_2\, c_3\, E[X^5]\,+\, {c_3}^2 \,E[X^6]\,=1 $
$

similarly, We can recursively continue this process to specify orthogonality and normality equations and solve them to
find coefficients of higher order orthonormalized polynomials

---

### #2475 — Amin (Topic Author)
*October 13, 2024, 9:03 AM*

Friends, my laptop is rather slow with ordinary ram and i am doing a monte carlo simulation of densities using a fourth
order monte carlo algorithm with a finer grid (1/64) and double the SDE paths to 200000 over 2500 SDEs with randomized
parameters and I have also increased density parameters to eight from earlier six parameters. I think I needed to do all
of this to capture accuracy in input to training algorithm. And my computer is still computing after 12 hours and I
expect that it could take another 24 hours.

Even though I have started working with Legendre regressions on raw SDE input parameters to check out things at start, I
want to switch to math informed variables like analytic computations of variances of SDE (that would be slightly off the
true values but still very good as prediction variables) and convert them to Legendre(or other appropriate orthogonal)
polynomials. I am also thinking of other possible improvements beyond polynomial regressions.

Even though it can take a few weeks, I am really very sure that we would be able to perfectly solve the problem of
reproducing densities of all various types of SDEs from their parameters as input very soon and then start towards more
AI problems. As my work improves, I will continue to post my matlab programs with gradual improvements on the current
SDE research as they follow.

---

### #2476 — Amin (Topic Author)
*October 13, 2024, 12:05 PM*

Friends, a long while ago, it was probably in 2013 when I started a petition to end neuroelectromagnetic weapons. I was
looking at internet and this petition was found by me. I want friends to look at it to get a glimpse of my struggle
against mind control weapons more than ten years ago.

Here is the web page: https://sign.moveon.org/petitions/stop-using-neuro-electromagn

---

### #2477 — Amin (Topic Author)
*October 14, 2024, 1:56 PM*

Friends, even outside of stochastics, there could be quite a few very interesting applications of new Math AI. For
suitable multivariate functions that we can represent as Taylor series without great difficulty, it would be possible to
represent Taylor coefficients as Legendre series expansions in various parameters by regressing suitably large sample of
coefficients of multivariate Taylor series over randomized data of parameters. Not only would we be able to find
coefficients of Taylor series of a particular function, We could also easily find multiple derivatives/cross derivatives
of coefficients of Taylor series with respect to all different parameters. And we could also convert these coefficients
of Taylor series of a function to its further functions (composition of functions) through Taylor series. So once we
have found coefficients of Taylor series of$f(X)$ as a function its parameters(and their derivatives with respect to
parameters) through Legendre series we could easily find coefficients of$g(f(X))$ and its derivatives with respect to
parameters by composition of two series using Taylor series of$g(f(X))$ where coefficients of$f(X)$ have been found
through our Legendre regression.

And this fact can also be used to make it easier to apply Legendre Series regression more accurately. For example, in
SDEs we know that we could transform an SDE in original coordinates to another SDE in Bessel coordinates. So one could
possibly randomize over input parameters and regress them on coefficients of Hermite series of SDEs in Bessel
coordinates and once coefficients of SDE in Bessel series have been retrieved, we could easily convert hem to
coefficients of Hermite series of SDEs in original coordinates. And we could also do these transformations for
derivatives of coefficients of hermite series with respect to parameters of the SDE.

And we could use these functional transformation in a straightforward way when dealing with non-random functions. If a
difficult function could be converted into a little easier function (for example by taking square root or its log), we
could find coefficients of Taylor series of easier function(that was possibly square root or log or something else) in
terms of Legendre polynomials of the parameters and then convert these coefficients to coefficients of original more
difficult function through composition of series$g(f(X))$ . And derivatives of coefficients of Taylor series (of easier
function) with respect to parameters could also be converted to derivatives of coefficients of Taylor series of original
(difficult) function.

Once we are more comfortable with numerical complexities of above ideas, I am sure we can move on to more interesting
things. For example, once we observe a random variable or a function, we may try to know distribution of parameters that
likely caused that particular observation(given for example some subset of parameters that we already know somehow in
advance) . This might not be doable right away but I hope soon we would be doing many such interesting things with more
research.

These are all possibilities but mathematics many times  requires precision and it might take us some reasonable time to
understand all the problems that arise when dealing with these new ideas and try to find their solution so that we have
good and established methods everyone could use for Math based AI.

---

### #2478 — Amin (Topic Author)
*October 14, 2024, 3:58 PM*

Friends, last winters, we did quite reasonably good research. We learnt many new and useful things and worked with
multidimensional random variables and all of that was very helpful in later research. Unluckily, I could not think of
differentiating between independent and dependent versions of orthogonal part of random variables and I only worked out
the case when orthogonal part of multivariate diffusions was independent of other random variables. Nevertheless, it was
interesting as I could not make anything out of the problem for more than a month and kept trying but only later we were
lucky to be able to solve the problem. But the good thing was that I was able to devote a lot of very serious time and
effort to solve the problem.

Now winters are just across the corner. So in this winter, let us aim to perfectly solve the problem of system of
general stochastic volatility and asset stochastic differential  equations with Math AI. With regression over hermite
series coefficients using Legendre polynomials and with other related ideas, let us try to solve the joint equations for
arbitrary SDE parameters. I am sure, we will have many difficulties and many problems will arise in the implementation
of ideas but let us try to find ways to overcome those difficulties just like we tried during last winters. And let us
also aim that once we are given a volatility surface and we find asset distribution out of it, our Math AI program
immediately gives us the joint distribution of parameters of the stochastic volatility SDEs system that could have
likely resulted in that particular distribution of asset and volatility. I am sure all of this would not be
straightforward and we would have to make a lot of effort, but I am sure that with persistent effort we would be able to
solve the problem and it could possibly help other researchers in many different areas of mathematics to be able to
apply similar methods to solve their difficult Math AI problems.

---

### #2479 — Amin (Topic Author)
*October 16, 2024, 2:31 PM*

Friends, I have been trying to get a good fit to SDE densities using regression on Hermite series coefficients on
Legendre polynomials of parameters of the SDE. But one thing I noticed that there was a lot of noise in monte carlo of
many SDEs especially when they were close to zero and volatility exponent was close to .5. And higher order SDE
discretizations made SDEs even more unstable close to zero. I noticed that until problem at zero is properly fixed, SDE
Hermite series coefficients with some parameters would continue to have random noise that could not be systematically
captured by Legendre regression with small number of polynomials.

So I looked at SDE discretizations and noticed that for each level of volatility coefficient and volatility exponent
discretized at a particular dt (time step), there is a certain threshold level of SDE variable below which diffusion
term exceeds the value of SDE variable and higher order derivatives exceed the successive lower derivatives and the
whole thing has a chance of becoming unstable when normal random number drawn for simulation is high. Ideally below this
level SDE time step for simulation has to be decreased so that diffusion term(or expected value of diffusion term)
remains smaller than the SDE original variable there. I did not want to selectively decrease the step size since I was
working with arrays in matlab and dealing separately with each simulation path would greatly slow down the speed. So
below the calculated threshold, I just turned diffusion to zero and only allowed exact drift to appear in the SDE
simulation. This would very slightly alter the distribution close to zero but remove a large amount of randomness in SDE
parameters due to instabilities when diffusion term all of a sudden jumps very close to zero and becomes too large in
simulation.

For example our mean reverting SDE is given as

$$dX_t\,=\, \kappa \,(\theta\,-\,X_t) \, dt \, + \, \sigma \, {X_t}^{\gamma} \, dZ_t $$

ideally our discretization should be fine enough that differential term containing noise is smaller than the SDE
variable$X_t$ itself. For that to happen, we determine the threshold where both are expected to be equal as (I am using
first order formula and mean reversion based formulas or variance based formulas could possibly lead to slightly better
thresholds)(I noticed that higher derivatives also increase successive smaller derivatives very close to the same
threshold point meaning this is the point where SDE can become unstable)

$$ \, \bar{X} \, =\,  \, \sigma \, {\bar{X_t}}^{\gamma} \, \sqrt{\Delta t} E[|Z|] $$

Where $|Z|$ is one sided Z that is either positive or negative.  where $E[|Z|]\,=\, \sqrt{\frac{2}{\pi}}$

so

$$ \,\bar{X}\,=\, \left[ \, \sigma \, \sqrt{\Delta t} \sqrt{\frac{2}{\pi}} \right]^{\frac{1}{1\,-\,\gamma}} $$

for example for $\Delta t \, =\, \frac{1}{64} $ and $\sigma\,=\,.75$

for $\gamma\,=\,.5$,   $\bar{X}\,=\, 0.005595$

for $\gamma\,=\,.6$,   $\bar{X}\,=\, 0.001530$

for $\gamma\,=\,.7$,   $\bar{X}\,=\, 1.7634e-04$

for $\gamma\,=\,.8$,   $\bar{X}\,=\, 2.341e-06$

for $\gamma\,=\,.9$,   $\bar{X}\,=\,5.4842e-12$

so if for particular$\gamma$ and$\sigma$ and$\Delta t$ , the value of$\bar{X}$ is not acceptably small enough, the
discretization has to be refined selectively for paths that are smaller than this threshold to make sure that SDE
properly captures the density of SDE. Obviously for paths in SDe simulation where SDE variable is larger than this
threshold, stability is not an issue and we can freely use high order discretization schemes.

I did not refine my SDE but below the specific threshold, I just did not include the possibly unstable diffusion term
and only used the analytic drift. This would extremely slightly alter the density close to zero but make the density
parameters a lot more stable.

With these changes, I was able to get the following R-squared with ten Legendre polynomials on a sample of 500
densities. I am using eight parameters for the hermite series of densities and one last parameter for squared root of
volatility (that is equal to 0.995871326780030)

ans =

   0.999604182685187

ans =

   0.993372243341080

ans =

   0.999011395179187

ans =

   0.993698983098868

ans =

   0.957906784908739

ans =

   0.775044395259506

ans =

   0.922611513046243

ans =

   0.921809626373820

ans =

   0.995871326780030

I want to mention that these R-squared values are only for ten polynomials only. And just like in neural networks,
increasing parameters for less amount of data could cause an overfit. And in a previous post where I used 31 Legendre
polynomials to get superb results, that was due to overfit since with 31 parameters, the total number of free parameters
were close to 500 and there were 500 data members in each regression. And with 31 polynomials, I was able to get
individualized fit to densities(overfit) despite that my simulation scheme had a lot of noise in parameters. However,
when I removed some noise from the density parameters input to regression learning by making simulation scheme more
stable, my R-squared improved remarkably even with ten polynomials.

I want to ask friends to please give me another day or two and I would post a far better matlab program with a good base
simulation scheme and good R-squared values.

---

### #2480 — Amin (Topic Author)
*October 16, 2024, 10:45 PM*

Friends, I re-did the simulation with thousand SDEs data and monte carlo simulation step size of 1/128 and these are the
results I was able to get for R-squared

ans =

   0.999599416769418

ans =

   0.992440134883207

ans =

   0.998596295117802

ans =

   0.992659698611661

ans =

   0.948693565396121

ans =

   0.768102903889510

ans =

   0.991546784223737

ans =

   0.965135950579467

ans =

   0.995316250880819

I was also able to think of an improvement to first eight standardized coefficients. since these coefficients were
standardized before regression and Legendre regression was done on standardized coefficients of hermite series, once we
predict the values of coefficients from regression we can standardize them again as they would have been if prediction
was perfect. Once I tried this, I got the following R-squared for first eight coefficients. Please note that R-squared
for first hermite polynomial increased from .99244 t0 .99789 due to this re-standardization after regression.

ans =

   0.999599416769418

ans =

   0.997891839685558

ans =

   0.998510150396431

ans =

   0.992381600594186

ans =

   0.948376878798396

ans =

   0.771829717347592

ans =

   0.991355659096756

ans =

   0.964428056306407

I am trying to make various improvements before I move to closed form analytic formulas for variances of the SDEs. For
mean reversion with general volatility exponent gamma in the SDE, we probably do not have a closed form formula for
variance of the SDE but the value of${X_t}^(2\,\gamma) $ in the formula can be replaced by its value at zero(or some
other more informed value based on known drift) and I am sure this will greatly improve the result due to continuous
mapping of slightly off estimate of variance on true variance.

I am posting my matlab program for this in next post in a few minutes.

---

### #2481 — Amin (Topic Author)
*October 16, 2024, 11:25 PM*

.

.

.

```
function [] = SDEsWithMathAIMain08A()

%The mean reverting SDE is given as
%dY(t)= kappa (theta - Y(t)) dt + sigma Y(t)^gamma dZ(t)
%Y(0) = y0

kappaL=.25;%Lower range of kappa
kappaH=3;%Upper range of kappa
thetaL=.5;%Lower range of theta
thetaH=2;%Upper range of theta
y0L=.5;%Lower range of y0
y0H=2;%Higher range of y0
gammaL=.5;%Lower range of gamma
gammaH=1;%Higher range of gamma

%I am not randomizing over sigma.
%I simply take a fixed point between lower and higher range of sigma for
%every SDE in sample.

sigmaL=.1;
sigmaH=1.0;

seed=83098561;
rng(seed);

NN=1000;%Number of SDE runs in the training sample. Ideally would be much larger.

Rand1(1:NN/2,1)=rand(NN/2,1);
Rand1(NN/2+1:NN,1)=1-Rand1(1:NN/2,1);%For symmetry, antithetic uniforms are used.
kappaU(1:NN)=kappaL+(kappaH-kappaL).*Rand1(1:NN,1);%Map unifrom random variates on kappa.

Rand2(1:NN/2,1)=rand(NN/2,1);
Rand2(NN/2+1:NN,1)=1-Rand2(1:NN/2,1);
thetaU(1:NN)=thetaL+(thetaH-thetaL).*Rand2(1:NN,1);%Map unifrom random variates on theta.

Rand3(1:NN/2,1)=rand(NN/2,1);
Rand3(NN/2+1:NN,1)=1-Rand3(1:NN/2,1);
y0U(1:NN)=y0L+(y0H-y0L).*Rand3(1:NN,1);%Map unifrom random variates on starting value of the SDE.

Rand4(1:NN/2,1)=rand(NN/2,1);
Rand4(NN/2+1:NN,1)=1-Rand4(1:NN/2,1);
gammaU(1:NN)=gammaL+(gammaH-gammaL).*Rand4(1:NN,1);%Map unifrom random variates on gamma.

sigmaU(1:NN)=(sigmaL+sigmaH)/2;%Taking sigma at mid of upper and lower range.

OrderL=10;%Order of Legendre polynomials to be used in regression of SDE coeffs

x12=kappaU(1:NN).*thetaU(1:NN);
[Wl12,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x12,OrderL);

x13=kappaU(1:NN).*y0U(1:NN);
[Wl13,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x13,OrderL);

x14=kappaU(1:NN).*gammaU(1:NN);
[Wl14,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x14,OrderL);

x23=thetaU(1:NN).*y0U(1:NN);
[Wl23,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x23,OrderL);

x24=thetaU(1:NN).*gammaU(1:NN);
[Wl24,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x24,OrderL);

x34=y0U(1:NN).*gammaU(1:NN);
[Wl34,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x34,OrderL);

  x123=kappaU(1:NN).*thetaU(1:NN).*y0U(1:NN);
  [Wl123,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x123,OrderL);
% %
  x124=kappaU(1:NN).*thetaU(1:NN).*gammaU(1:NN);
  [Wl124,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x124,OrderL);
% %
  x234=thetaU(1:NN).*y0U(1:NN).*gammaU(1:NN);
  [Wl234,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x234,OrderL);
% %
 x1234=kappaU(1:NN).*thetaU(1:NN).*y0U(1:NN).*gammaU(1:NN);
 [Wl1234,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(x1234,OrderL);

str=input("Look at values");
SDEpaths=200000;
MOrder=16;
Order=7;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

% alpha(1)=1.002379147775649;
% alpha(3)=-0.000740478718368;
% alpha(5)=0.001052947275469;
% alpha(7)=0.000402630517679;
% alpha(9)=0.000121151611625;
% alpha(11)=0.000012754129466;
% alpha(13)=0.000000680335020;

alpha(1) =0.993024015547037;
alpha(3)= 0.008264111853961;
alpha(5)= 0.008237591744137;
alpha(7)= 0.006556372747340;
alpha(9)= 0.001939786779503;
alpha(11)=0.000289238364672;
alpha(13)=0.000019850983839;
alpha(15)=0.000000562412998;

[Zn] = StandardNormalIdealDesity02(SDEpaths,1);
[ZI] = CalculateZnAfterHermiteSeriesMultiplication(Zn,alpha,MOrder);

[W] = EvalHermiteArrayH0(ZI,Order);
[W2] = EvalHermiteArrayH0(ZI,Order+2);

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
seed0=90728436;
rng(seed0, 'combRecursive')
TtM=256*2;
dtM=1/64/2;
Sfrequency=16;
Random0(1:SDEpaths,1:TtM)=0;

for tt=1:TtM
%Since SDEs are simulated with different parameters in a loop. We calculate
%moment matched normal random variates for all of the time steps just once
%and input them to SDE simulation program so we do not have to generate
%these random numbers again and again every time we simulate a different
%SDE inside the SDE simulation loop.
URandom=0;
URandom(1:SDEpaths/2)=0;
URandom=rand(size(URandom));
URandom(SDEpaths/2+1:SDEpaths)=1-URandom(1:SDEpaths/2);
[URandomS,I]=sort(URandom);

Random1=ZI(I);

Random0(1:SDEpaths,tt)=Random1(1:SDEpaths);
end
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%Run this loop and above loop only once and save the data on disk as below.
%Then comment both these loops and keep reading the data from disk.
%Coeff(1:Order+1,1:TtM/Sfrequency,1:NN)=0;
%Coeff2(1:NN,1:TtM,1:Order+3)=0;
%for nn=2204:0%NN
%for nn=288:288%NN
for nn=1:NN
 nn
 NN

 [coeff] =
MeanRevertingMonteCarloDensity04New(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,Sfrequency);
 %[coeff,coeff2] =
MeanRevertingMonteCarloDensity04(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,W2);
 Coeff(1:Order+1,1:TtM/Sfrequency,nn)=coeff(1:Order+1,1:TtM/Sfrequency);
% Coeff2(nn,1:TtM,1:Order+1+2)=coeff2(1:TtM,1:Order+1+2);
%size(coeff)
end

save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG01.mat","Coeff")
str=input("I have saved the densities coefficients variable");

load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG01.mat","Coeff")
str=input("I have loaded the densities coefficients variable");

%144/64

Tt=TtM;
%Dimensions of Coeff are Coeff(,1:Order+1,1:TtM,1:NN).Below we take one time
%slice between 1 and TtM. I have taken slice 18 that occurs at time
%18*Sfrequency*dtM=
%You can comment the SDE simulations loop and continue to load the
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.
%
%TimeSlice variable below
Ts=18;
CoeffH0(1:Order+1,1:NN)=Coeff(1:Order+1,Ts,1:NN);
CoeffH=transpose(CoeffH0);

clf;

plot((1:NN),CoeffH(1:NN,2),'g');

str=input("Look at coeffs plot --Z1 coeff");

TT=Ts*dtM*Sfrequency;%Time at end of chosen slice. This will be used in analytic calculation of SDE mean later.
%We will replace the first mean coefficient of zeroth hermite associated
%with the Hermite series of SDEs with the analytic value.

%Below we calculate square root of variance(sum of hermite coefficients squared formula) to standardize the coefficients
VarSqRt(1:NN,1)=
sqrt(CoeffH(1:NN,2).^2+CoeffH(1:NN,3).^2*2+CoeffH(1:NN,4).^2*6+CoeffH(1:NN,5).^2*24+CoeffH(1:NN,6).^2*120+CoeffH(1:NN,7).^2*720+CoeffH(1:NN,8).^2*7*720);
%Below are six standardized coefficients
SCoeff(1:NN,1:8)=CoeffH(1:NN,1:8)./VarSqRt(1:NN,1);

str=input("Reached Level 1");

for mm=1:1
    Ukappa(1:NN)=-1+2*Rand1(1:NN);%Convert first uniform to between zero and one to between -1 and +1
    Utheta(1:NN)=-1+2*Rand2(1:NN);%Convert second uniform to between zero and one to between -1 and +1
    Uy0(1:NN)=-1+2*Rand3(1:NN);%Convert third uniform to between zero and one to between -1 and +1
    Ugamma(1:NN)=-1+2*Rand4(1:NN);%Convert fourth uniform to between zero and one to between -1 and +1

     for qq=1:8
     Yl(1:NN,qq)=SCoeff(1:NN,qq); %First six standardized coefficients to be predicted.
     end
     Yl(1:NN,9)=VarSqRt(1:NN);%Square root of variance used to standardize has to be predicted as well.
end
clf;
[XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,1),NN,25,10 )
plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
str=input("Look at density of 1st coeff")

[XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,2),NN,25,10 )
plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
str=input("Look at density of 2nd coeff")

%

OrderL0=OrderL+1;

 [Wl1] = EvalLegendreArrayL0(Ukappa,OrderL);%Matrix in which zeroth Legendre and first six Legendre polynomilas are
evaluated at uniform values.
 [Wl2] = EvalLegendreArrayL0(Utheta,OrderL);
 [Wl3] = EvalLegendreArrayL0(Uy0,OrderL);
 [Wl4] = EvalLegendreArrayL0(Ugamma,OrderL);

%Below Tile all of the Legendre polynomials of each of the four random
%parameters in a single matrix and use for least square regression. Zeroth
%Legendre is evaluated in each of the four matrices and has to be removed
%from tiling other than just including one time.
WL(:,1:OrderL0)=Wl1(:,1:OrderL0);
WL(:,OrderL0+1:OrderL0+OrderL)=Wl2(:,2:OrderL0);
WL(:,OrderL0+OrderL+1:OrderL0+2*OrderL)=Wl3(:,2:OrderL0);
WL(:,OrderL0+2*OrderL+1:OrderL0+3*OrderL)=Wl4(:,2:OrderL0);
 WL(:,OrderL0+3*OrderL+1:OrderL0+4*OrderL)=Wl12(:,2:OrderL0);
 WL(:,OrderL0+4*OrderL+1:OrderL0+5*OrderL)=Wl13(:,2:OrderL0);
 WL(:,OrderL0+5*OrderL+1:OrderL0+6*OrderL)=Wl14(:,2:OrderL0);
 WL(:,OrderL0+6*OrderL+1:OrderL0+7*OrderL)=Wl23(:,2:OrderL0);
 WL(:,OrderL0+7*OrderL+1:OrderL0+8*OrderL)=Wl24(:,2:OrderL0);
 WL(:,OrderL0+8*OrderL+1:OrderL0+9*OrderL)=Wl34(:,2:OrderL0);
 WL(:,OrderL0+9*OrderL+1:OrderL0+10*OrderL)=Wl123(:,2:OrderL0);
 WL(:,OrderL0+10*OrderL+1:OrderL0+11*OrderL)=Wl124(:,2:OrderL0);
 WL(:,OrderL0+11*OrderL+1:OrderL0+12*OrderL)=Wl234(:,2:OrderL0);
 WL(:,OrderL0+12*OrderL+1:OrderL0+13*OrderL)=Wl1234(:,2:OrderL0);
CoeffL=inv(WL'*WL)*(WL'*Yl);%Legendre coefficients to predict seven variables. six standardized coefficients
%and one square root of variance of each SDE.

CoeffL
size(WL)
size(CoeffL)

str=input("Look at size of CoeffL");
     aa(:,1:9)=Yl(:,1:9);
     for nn=1:NN
     b(nn,1:9)=CoeffL(1,1:9);
     end
    for rr=2:OrderL+1

        b(:,1:9)=b(:,1:9)+CoeffL(rr,1:9).*Wl1(:,rr)+CoeffL(rr+OrderL,1:9).*Wl2(:,rr)+ ...
            CoeffL(rr+2*OrderL,1:9).*Wl3(:,rr)+CoeffL(rr+3*OrderL,1:9).*Wl4(:,rr)+ ...
            CoeffL(rr+4*OrderL,1:9).*Wl12(:,rr)+CoeffL(rr+5*OrderL,1:9).*Wl13(:,rr)+ ...
            CoeffL(rr+6*OrderL,1:9).*Wl14(:,rr)+CoeffL(rr+7*OrderL,1:9).*Wl23(:,rr)+ ...
            CoeffL(rr+8*OrderL,1:9).*Wl24(:,rr)+CoeffL(rr+9*OrderL,1:9).*Wl34(:,rr)+ ...
            CoeffL(rr+10*OrderL,1:9).*Wl123(:,rr)+CoeffL(rr+11*OrderL,1:9).*Wl124(:,rr)+ ...
            CoeffL(rr+12*OrderL,1:9).*Wl234(:,rr)+CoeffL(rr+13*OrderL,1:9).*Wl1234(:,rr);
%
    end

    %Below are seven calculations of R-squared for each of
    %the standardized six coefficients and seventh value of
    1-sum((aa(:,1)-b(:,1)).^2)/sum((aa(:,1)-sum(aa(:,1))/(NN)).^2)
    1-sum((aa(:,2)-b(:,2)).^2)/sum((aa(:,2)-sum(aa(:,2))/(NN)).^2)
    1-sum((aa(:,3)-b(:,3)).^2)/sum((aa(:,3)-sum(aa(:,3))/(NN)).^2)
    1-sum((aa(:,4)-b(:,4)).^2)/sum((aa(:,4)-sum(aa(:,4))/(NN)).^2)
    1-sum((aa(:,5)-b(:,5)).^2)/sum((aa(:,5)-sum(aa(:,5))/(NN)).^2)
    1-sum((aa(:,6)-b(:,6)).^2)/sum((aa(:,6)-sum(aa(:,6))/(NN)).^2)
    1-sum((aa(:,7)-b(:,7)).^2)/sum((aa(:,7)-sum(aa(:,7))/(NN)).^2)
    1-sum((aa(:,8)-b(:,8)).^2)/sum((aa(:,8)-sum(aa(:,8))/(NN)).^2)
    1-sum((aa(:,9)-b(:,9)).^2)/sum((aa(:,9)-sum(aa(:,9))/(NN)).^2)

    str=input("Look at R^2s of eight standardized hermite series coefficients and seventh square root of variance");

VarSqRtb(1:NN,1)=
sqrt(b(1:NN,2).^2+b(1:NN,3).^2*2+b(1:NN,4).^2*6+b(1:NN,5).^2*24+b(1:NN,6).^2*120+b(1:NN,7).^2*720+b(1:NN,8).^2*7*720);

%b0 is re-standardized estimates of predicted from regression values of hermite series coefficints
b0(1:NN,1)=b(1:NN,1);
b0(1:NN,2:8)=b(1:NN,2:8)./VarSqRtb(1:NN,1);

    1-sum((aa(:,1)-b0(:,1)).^2)/sum((aa(:,1)-sum(aa(:,1))/(NN)).^2)
    1-sum((aa(:,2)-b0(:,2)).^2)/sum((aa(:,2)-sum(aa(:,2))/(NN)).^2)
    1-sum((aa(:,3)-b0(:,3)).^2)/sum((aa(:,3)-sum(aa(:,3))/(NN)).^2)
    1-sum((aa(:,4)-b0(:,4)).^2)/sum((aa(:,4)-sum(aa(:,4))/(NN)).^2)
    1-sum((aa(:,5)-b0(:,5)).^2)/sum((aa(:,5)-sum(aa(:,5))/(NN)).^2)
    1-sum((aa(:,6)-b0(:,6)).^2)/sum((aa(:,6)-sum(aa(:,6))/(NN)).^2)
    1-sum((aa(:,7)-b0(:,7)).^2)/sum((aa(:,7)-sum(aa(:,7))/(NN)).^2)
    1-sum((aa(:,8)-b0(:,8)).^2)/sum((aa(:,8)-sum(aa(:,8))/(NN)).^2)

str=input("Look at R^2s of first eight standardized hermite series coefficients");

for nn=1:NN

    cc(1:8)=b0(nn,1:8).*b(nn,9);
    Yl0(1:8)=Yl(nn,1:8).*VarSqRt(nn);
    cc(1:8)
    Yl0(1:8)
    cc(1)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));%Replacing predicted value of mean with analytic value.

    Coeff(1:8,18,nn)
        clf;
     cc(1)
     nn
     PlotHermiteSeriesDensityAndRvGraph(cc(1),cc(2:Order+1),'r');

     hold on

     PlotHermiteSeriesDensityAndRvGraph(Yl0(1),Yl0(2:Order+1),'g');
     nn

    % hold on

    % PlotHermiteSeriesDensityAndRvGraph(Coeff2(nn,144,1),Coeff2(nn,144,2:Order+3),'b');

     str=input("Look at comparison of graphs--Green is data and red is our interpolation from coefficients");

end

end

```

.

.

.

.

```
function [Coeff] =
MeanRevertingMonteCarloDensity04New(V0,kappa,theta,sigma0,gamma,paths,W,Order,Random0,dtM,TtM,Sfrequency)

beta1=0;
beta2=1;
mu1=kappa*theta;
mu2=-kappa;
dt=dtM;
Threshold=(sigma0*sqrt(dt)*sqrt(2/pi))^(1/(1-gamma));
%Coeff(1:TtM,1:Order+1)=0;
%Coeff2(1:TtM,1:Order+3)=0;
V(1:paths)=V0;  %Original process monte carlo.
Random2(1:paths)=0;
mm=0;
for tt=1:TtM

    Random2(1:paths)=Random0(1:paths,tt);

    Random2(V<Threshold)=0;

   V(1:paths)=theta+ exp(-kappa*dt).*(V(1:paths)-theta)+ ...
        sigma0*V(1:paths).^gamma .*Random2(1:paths)*sqrt(dt) + ...
        (mu1.*beta1*V(1:paths).^(beta1-1) + mu2.*beta2.*V(1:paths).^(beta2-1)).* ...
        (sigma0*V(1:paths).^gamma .*Random2(1:paths)*(1-1/sqrt(3))*dt^1.5) + ...
        .5*(mu1.*beta1.*(beta1-1).*V(1:paths).^(beta1-2) + mu2.*beta2.*(beta2-1).*V(1:paths).^(beta2-2)).* ...
        sigma0^2.*V(1:paths).^(2*gamma).*dt^2/2 + ...
        sigma0*gamma*V(1:paths).^(gamma-1) .* ...
        ((mu1.*V(1:paths).^beta1 + mu2.*V(1:paths).^beta2).*Random2(1:paths).*1/sqrt(3)*dt^1.5 + ...
        sigma0.*V(1:paths).^gamma .*(Random2(1:paths).^2-1)*dt/2) + ...
        .5*sigma0*gamma*(gamma-1).*V(1:paths).^(gamma-2) .* ...
        sigma0^2.*V(1:paths).^(2*gamma) .*Random2(1:paths).*1/sqrt(3)*dt^1.5;

  V(V<0)=0;

    if(rem(tt,Sfrequency)==0)
        mm=mm+1;
        VV(1:paths,mm)=V(1:paths);

 %      [Coeff(1:Order+1,tt)] = CalculateHermiteSeriesFromDataWithWin(V,W,Order);

%        coeff
%        Coeff
%
%        Ymu(1:10,1)
%        V(1:10)
%        str=input("Look atComparison of Densities");
    end
%           clf;
% %
%      PlotHermiteSeriesDensityAndRvGraph(coeff(1,1),coeff(2:Order+1,1),'r');
% %
%     hold on
%
%     NoOfBins=100;
%     MaxCutOff=10;
%     [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(V,paths,NoOfBins,MaxCutOff );
%
%     plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g')
%
%     str=input("Look atComparison of Densities---2");

end

     [Ymu,I]=sort(VV);
     Coeff=inv(W'*W)*(W'*Ymu);

 %str=input("Look at coeffs");
end

```

.

.

.

---

### #2482 — Amin (Topic Author)
*October 18, 2024, 5:01 PM*

Friends, I decided to make a post specifically for Legendre regression especially for friends who have not been
following me for a long time and might find Legendre regression useful in their mathematical analytics work.

**Brief Introduction to Legendre Polynomial Regression**

Legendre polynomials are orthogonal polynomials associated with uniform density with support between -1 and +1. This
means that integral of product of one Legendre polynomial with any other Legendre polynomial with uniform density weight
in the integral over the support of uniform density between -1 and +1 would go to zero.

We present mth Legendre Polynomial as$L_m(.)$ . For our Legendre regressions, we are only working with Legendre
polynomials of Uniform density supported between -1 and +1, so we will universally use the notation$L_m(U)$ .

Legendre polynomial regression works very well not only for random variables over finite support, it can work equally
well for finding deterministic relationships  between different variables that arise in physical processes and chemistry
or physics experiments.

Orthogonal polynomials work great for finding relationships between different random or deterministic variables since we
standardize all variables involved in regression by mapping them over orthogonal polynomials of the same appropriate
densities. Correlations can exist only among orthogonal polynomials of the same order. It is like decomposing various
variables into the same common set of different standardized units/currencies (with different coefficient weights for
all different variables)  where correlation can exist only among the same standardized units/currencies and then finding
relationships between common standardized units/currencies across various variables.

First few Legendre polynomials are given as

$$L_0(U)\,=\,1$$

$$L_1(U)\,=\,U$$

$$L_2(U)\,=\,1/2 \,\,(3 \,U^2\,-\,1) $$

$$L_3(U)\,=\,1/2 \,\,(5 \,U^3\,-\,3 \, U) $$

$$L_4(U)\,=\,1/8 \,\,(35 \,U^4\,-\,3 \, U^2 \,+\,3\,) $$

Finding Legendre Polynomial Series of a Continuous Variable

In this section we study how to represent data of various continuous variables (over their respective finite domains) as
a respective series in orthogonal Legendre polynomials of Uniform density. For example a data variables X can be
converted into a Legendre polynomial series over uniform as

$$\, X(U)\,=\, al_0 \, + \, al_1 \, L_1(U) \,+ \, al_2 \, L_2(U) \,+ \ldots \,+ \, al_N \, L_N(U) \, $$

This can be done by choosing coefficients of the Legendre series so that moments of associated Legendre Series match
with the moments of the associated variables.

This can also be easily done with regression of data variables over discretized version of Uniform density to find the
coefficients of Legendre series of a data variable. Please note this regression to convert a continuous variable (with
support on finite domains) into a series in Legendre polynomials of uniform density is an intermediate step and is
different from our final goal of a different regression to find relationship of a variable with various other variables
through Legendre regression.

We suppose there are a total of P data observations of random variable X whose Legendre-Series we want to find. In order
to find coefficients of Legendre-Series, we have to regress each of the P data observations on N Legendre polynomials of
a discretized uniform density points associated with each of the data observation therefore grid size of discretized
uniform density should also be P(equal to P data observations). We also know that probability mass of each data
observation is$\frac{1}{P}$ , so the probability mass of each grid cell on standard uniform discretized grid should also
be$\frac{1}{P}$ . We make this discretized uniform density over P points by dividing the support of uniform density
between -1 and 1 into P equal grid cells and discretize uniform density into P points that are centers of these grid
cells. (Ideally we would also do a moment matching and slightly alter this discretized density to make sure its moments
match with moments of the uniform density). This way we can make a symmetric grid around median of uniform density that
can be mapped on data observations through equivalent CDF.

In order to do the regression of P data observations of a continuous variable on P points of the discretized uniform
density, we have to first associate each data observation with an appropriate point on the discretized uniform density.
In order to do this, we sort the data observations in an ascending order and then associate nth member of this sorted
array in ascending order with nth data point on discretized uniform density already in an ascending order. Once we have
made this association of sorted data observations with discretized uniform density, we can re-order the data
observations in original order (before sorting) or any other order carrying the associated discretized uniform density
point along the same re-ordering that is applied to data.

Once we have associated each data point with discretized uniform density by sorting the data, we simply regress data
points on Legendre polynomial values calculated at particular discretized uniform density grid points in a least square
fashion to find regression coefficients.  These regression coefficents represent the coefficients of Legendre
polynomials in the Legendre-series.

If there are P data points, and we use N Legendre polynomials to represent the Legendre-Series of X, then our regression
equation for each pth data point would be

\begin{equation}

X_p\,=\, al_0 \, + \,al_1\, L_1(U_p)\,+ \,al_2\, L_2(U_p)\,+ \ldots \,+\,al_N\, L_N(U_p)\,

\end{equation}

with the matrix equation given as

\begin{equation}

\begin{bmatrix} 1 & L_1(U_1) & L_2(U_1) & ..... & L_N(U_1) \\

1 & L_1(U_2) & L_2(U_2) & ..... & L_N(U_2) \\ ... & ... & ... & ... \\1 & L_1(U_p) & L_2(U_p) & ..... & L_N(U_p) \\  ...
& ... & ... & ... & ... \\

1 & L_1(U_P) & L_2(U_P) & ... & L_N(U_P)

\end{bmatrix}   \begin{bmatrix} al_0 \\ al_{1} \\ al_{2} \\ ... \\ al_{N} \end{bmatrix} \\ \,=\, \begin{bmatrix} X_1 \\
X_2 \\ ...  \\  X_p \\ ... \\  X_P \end{bmatrix}

\end{equation}

\begin{equation}

\boldsymbol{L \, a_l}\,=\,\boldsymbol{x}

\end{equation}

and we solve this equation with least squares as

\begin{equation}

\boldsymbol{a_l}\,=\,\boldsymbol{{\left(L^T\, L \right)}^{-1}\,L^T\, x }

\end{equation}

Preparing Data For Legendre Polynomial Regression of a Continuous Variable on Several Other Continuous Variables

In order to Legendre-regress a continuous variable on several other variables, we have to first map observations of all
the variables in regression sample on their respective discretized uniform densities. In Legendre regression, we do not
need the coefficients of Legendre series of any variable in the regression and we only need the values of Legendre
polynomials calculated at the values of discretized uniform density points associated with the observations.

Since we do not need coefficients of Legendre series of any regressor in the Legendre polynomial regression, we do not
need to do the regression described in previous section even though it is a good idea to do the regression described in
previous section and find out the associated R-squared to see that the regressor can be well captured by the Legendre
series of the variable and also find out if Legendre-regression is appropriate for a particular set of variables.

All we need to do to prepare data for Legendre regression of one variable on several other regressors is to first
construct discretized version of the Uniform density with P grid points for each of the regressor variables. Sort
observations of each data variable in an ascending order array and associate them to the same element of array of
discretized uniform density. You can then change the order of observations of data variables back to original order but
they would carry the association between sorted arrays with them. You can see that it is a mapping between two densities
with equal members where data members of one density in ascending order are mapped on data members of another density in
the same ascending order.

I will give a very small concrete example with hypothetical data of only a few points for regression over three
variables X, Y and W. Suppose there are only five data observations of each variable(We will usually need large data
samples but this small hypothetical data is to simply explain the algorithm of mapping on uniform density)

For five data members, the discretized uniform density without any moment matching would be  $[-.8,  -.4,  0,  .4,  .8]$

Suppose our five joint observations of X, Y and W are given as

Obs N0.             X          Y         W

1                      5           13         34

2                      9             7         22

3                      3            11        18

4                     11            2         38

5                      4             9         20

Then corresponding values of  associated uniform variables used in polynomial regressions would be

Obs N0.        U_X      U_Y         U_W

1                      0           .8         .4

2                     .4           -.4         0

3                     -.8          .4        -.8

4                     .8            -.8         .8

5                      -.4             0         -.4

The above example shows how to associate a regression variable with appropriate appropriate discretized uniform density.
This method without actually finding the Legendre series coefficients is helpful when we have the whole sample of data
observations however we would need to know the Legendre series of a variable after regression when we would have single
observations of random variables in after-regression predictions. So we could map a whole sample of observations on
discretized uniform density that would be used for finding parameters of a regression but in later calculations when
single observations of variables would be given to predict the resulting variable, we would usually need the knowledge
of coefficients of Legendre series of each parameter.

Doing Legendre Polynomial Regression

Suppose we want to Legendre-regress a variable V on other variables X, Y and their product XY. Let us suppose that we
have a total of P joint data observations of above three regressors and we include N Legendre polynomials for each of
the three explanatory variable in the regression. And we also have P joint observations of the target regressand. Then,
for each of the pth$(p\,=\,1, \ldots,P\,)$ data observation for each variable we would need to find the corresponding
point on their respective uniform densities as we outlined in previous section. The corresponding values of uniform
variable for pth observation of X, Y and XY would be represented as$U_{X_{p}}$ and$U_{Y_{p}}$ and$U_{XY_{p}}$ . Then we
would find first N Legendre polynomial values for each of the inverted$U_{X_{p}}$ and$U_{Y_{p}}$ and and$U_{XY_{p}}$ .

It is also possible that sometimes, we are given a Legendre series for each of the variables X, Y and their XY and we
might have to invert it for every pth observation of X, Y and XY to find$U_{X_{p}}$ and$U_{Y_{p}}$ and$U_{XY_{p}}$ from
the following equations

$$\, X(U_X)\,=\, al_0 \, + \, al_1 \, L_1(U_X) \,+ \, al_2 \, L_2(U_X) \,+ \ldots \,+ \, al_N \, L_N(U_X) \, $$

$$\, Y(U_Y)\,=\, bl_0 \, + \, bl_1 \, L_1(U_X) \,+ \, bl_2 \, L_2(U_Y) \,+ \ldots \,+ \, bl_N \, L_N(U_Y) \, $$

$
$\, XY(U_{XY})\,=\, cl_0 \, + \, cl_1 \, L_1(U_{XY}) \,+ \, cl_2 \, L_2(U_{XY}) \,+ \ldots \,+ \, cl_N \, L_N(U_{XY}) \, $
$

The final regression equation would be given in the matrix form as

\begin{equation}

\begin{bmatrix} 1 & L_1(U_{X_1}) & \ldots & L_N(U_{X_1}) & L_1(U_{Y_1}).& \ldots.. & L_N(U_{Y_1}) & L_1(U_{XY_1}).&
\ldots.. & L_N(U_{XY_1}) \\

1 & L_1(U_{X_2}) & \ldots & L_N(U_{X_2}) & L_1(U_{Y_2}).& \ldots.. & L_N(U_{Y_2}) & L_1(U_{XY_2}).& \ldots.. &
L_N(U_{XY_2})  \\ \ldots & \ldots & \ldots & \ & \ldots & \ldots.. & \ldots \\   1 & L_1(U_{X_p}) & \ldots &
L_N(U_{X_p}) & L_1(U_{Y_p}) & \ldots & L_N(U_{Y_p}) & L_1(U_{XY_p}).& \ldots.. & L_N(U_{XY_p}) \\ \ldots & \ldots &
\ldots & \ & \ldots & \ldots.. & \ldots \\

1 & L_1(U_{X_P}) & \ldots & L_N(U_{X_P})  & L_1(U_{Y_P})  & \ldots &  L_N(U_{Y_P}) & L_1(U_{XY_P}).& \ldots.. &
L_N(U_{XY_P}) \\

\end{bmatrix}   \begin{bmatrix} \beta_0 \\ \beta_{X,1} \\ \ldots \\ \beta_{X,N} \\ \beta_{Y,1}\\\dots \\ \beta_{Y,N} \\
\beta_{XY,1}\\\dots \\ \beta_{XY,N} \end{bmatrix} \\ \,=\, \begin{bmatrix} V_1 \\ V_2 \\ ...  \\  V_p \\ ... \\  V_P
\end{bmatrix}

\end{equation}

\begin{equation}

\boldsymbol{L \, \beta}\,=\,\boldsymbol{v}

\end{equation}

and we solve this equation with least squares to find the regression coefficients of equation as

\begin{equation}

\boldsymbol{\beta}\,=\,\boldsymbol{{\left(L^T\, L \right)}^{-1}\,L^T\, v }

\end{equation}

since there are three random variable regressors and Legendre-Series of each random variable includes Legendre
polynomials terms up to Nth order and there are a total of P joint data observations, then matrix$\boldsymbol{L} $ has
matrix size as$ \text{P  X (1 + 3 N)} $ ,$\boldsymbol{\beta}$ has array size of$\text{(1 +  3 N ) X 1} $ and
$\boldsymbol{v}$ has array size of$\,\text{P X 1} $ .

Programming Notes

You can see example of Legendre regression in many of the matlab programs I have recently posted on the forum.

I am posting some handy matlab numerical routines that would be very helpful. Even though these are written in matlab,
they do not use any inbuilt matlab function and can easily be copied in C++ etc.

The first routine is  [Lu] = LegendrePoly(Order)  that takes in an argument order of Legendre polynomial as input. If
for example this input argument order is equal to ten, output Lu will return a matrix containing coefficients of zeroth
to tenth Legendre polynomials.

The second helpful routine is [Wl] = EvalLegendreArrayL0(U,Order) . It takes two arguments as input. First argument U is
an array of Uniform values (that might be associated with values of discretized uniform density underlying a variable).
Second argument is Order of Legendre arrays. If for example input argument Order is ten, this function returns a matrix
containing zeroth to tenth Legendre polynomial evaluated at the array of Uniforms. If input array of U (uniforms)has a
size of 100 and Order is 10, it will return a 100 X 11 array.

.

.

```
function [Lu] = LegendrePoly(Order)

Lu(1:Order+1,1:Order+1)=0.0;
Lu(1,1)=1.0;
Lu(2,2)=1.0;
for n=2:Order

    for m=1:n
       Lu(n+1,m+1)=Lu(n+1,m+1)+Lu(n,m)*(2*(n-1)+1)/((n-1)+1);
    end
    for m=1:n-1
       Lu(n+1,m)=Lu(n+1,m)-Lu(n-1,m)*(n-1)/((n-1)+1);
    end
end
Lu;
end

```

.

.

.

.

```
function [Wl] = EvalLegendreArrayL0(U,Order)

%Evaluates first Order-th Legendres at the array of U's. If input array of Z
%has a size of 100 and Order is 4, it will return a 100 X 5 array.

Lu=LegendrePoly(Order);

Wl(1:length(U),1:Order+1)=0;
for nn=1:Order+1
    Wl(:,nn)=0;
    for mm=1:nn
        Wl(:,nn)=Wl(:,nn)+Lu(nn,mm).*U(:).^(mm-1);
    end
end

end
```

.

.

.

---

### #2483 — Amin (Topic Author)
*October 18, 2024, 7:51 PM*

Friends, I am writing this post to protest about my increasing persecution everyday. For about past one and a half
month, they had appointed a different mind control agent on me who was relatively benign. They were vehemently trying to
drug my food in the city when I would go out to buy food even then but there were almost no gases in my home. But just
about ten days ago, they brought back the same mind control agent who had been trying to control me for more than twenty
years with a few off and on intervals of several months (and who is a dollar billionaire). And he started to use all
sort of gases freely during past ten days. In my room where I sleep and in the room where I work, there is slight amount
of constant gas that they increase dramatically from time to time.

Though I was lucky to get good food and water, the day before yesterday, I had some good water in trunk of my car when I
went inside this medium sized store to buy some food. Store did not have glass walls and I thought that I would be able
to quickly walk twenty meters to get food from some aisle and quickly come back to front and look at the car again to
make sure that they do not drug water in the trunk of my car in the meantime. I could not see them doing anything but
when I reached home and tried old water, it was highly drugged. I was able to survive since I had bought some more good
water that day and I continued to drink that  but the old water lying in the trunk had been drugged very quickly.

I am very worried due to constant gas and charges that settle on my body since it is not easily possible to take a
shower due to broken thumb even though I have washed my lower body a few times. I really want to request friends to
protest to American government and defense about persecution with gases that has really increased over past three days.

---

### #2484 — Amin (Topic Author)
*October 19, 2024, 10:01 AM*

Friends, before moving on to using  known and approximate formulas of variances of SDEs in the Legendre regression, I
want to experiment for a few days with density transformations to see if suitably transforming the input densities might
make the Legendre regressions on coefficients of hermite series more precise. This is important since we want to use our
regression methods on densities of random variables that are not necessarily SDEs and approximate variance formulas
available for SDEs might not be available for many types of random variables we want to use in practice.

I want to experiment for another 2-3 days and will keep posting programs in the meantime. And after completing this
part, I will come up with a brief introduction to all the work done in the form of a small post explaining all the
involved steps towards Legendre regression on coefficients of hermite series of densities in detail.

---

### #2485 — Amin (Topic Author)
*October 21, 2024, 7:59 AM*

**Introduction to Math AI With a Case Study Towards Instantaneous Calculation of Densities of SDEs From Their
Parameters**

Context

We have been working with Hermite series/Z-series representation of densities for at least three years now. Using
Hermite-Series/Z-series, we can represent a very large class of densities extremely faithfully with just 6-8
coefficients of the respective series. Most of the densities we come across in finance including Generalized Gamma
density, most non-central chi-squared type densities, lognormal densities and large class of densities that are similar
but cannot be described by three parameter classic distributions, can easily be captured using just 6-8 coefficients of
respective Z-series/Hermite Series. There might be some exceptions when higher moments of some of these densities might
be too large and then we might need to represent them with ten coefficients of the Z-series/Hermite-Series for example
when variance of lognormal densities is too high. At any time along their evolution, densities of most SDEs that we
usually encounter in finance can easily be captured by a Hermite-series/Z-series described only by six to eight
coefficients.

In parallel with our work on finding hermite series of densities, we have been able to develop orthogonal polynomial
regression methods which are extremely successful in capturing relationships between various random or deterministic
variables.

Extracting useful information from many interacting random variables is a subject of very intensive research and many
researchers like to use deep neural networks extensively for that purpose. We aim to combine our research on orthogonal
polynomial regressions and parsimonious analytic representation of densities of random variables with a few coefficients
and densities based Bayesian methods to efficiently solve most of these problems in probability theory and statistics of
continuous random variables that arise in practice. We expect that our Math AI methods would be more precise than deep
network methods and would require far almost trivial computational effort in training algorithms since calculating the
parameters of orthogonal polynomials only requires least square regressions and is almost computationally trivial.

As a demonstration case study we decided to solve a very difficult problem of finding densities of SDEs from their
parameters just as instantaneously as is done by neural network methods. This is a very good test case study since
densities of SDEs can be calculated very precisely and we can see how good our Math AI methods are to capture these
densities. At the same time this example is very relevant since in a lot of practical applications where we deal with
interaction of many random variables since we can reproduce the densities of those random variables very quickly from
realized values and it will be based on a previous learning process applied to data using orthogonal polynomials and we
would quickly find values of variables of interest also based on previous orthogonal polynomial regressions. We can do
more precise calculations of variables of interest with several orders of smaller computational effort as compared to
what is used in network parameters learning process of deep networks. This can be used in for example in a large number
of internet applications that make use of consumer data to make quick decisions that tailor all sort of products,
offerings, advertisements and many other things for the specific customer. Particularly in finance, Math AI could help
us make all sort of risk and investment decisions very quickly in all different sort of market scenarios.

Application of Math AI to Calculation of Densities of SDEs

We aim to find density of SDEs of a particular class from the parameters of the SDE as input to the algorithm. We choose
the following SDE

\begin{align}

& dY_t\,=\, \kappa \, (\theta \, -\, Y_t\,)\, dt\,+ \sigma \, {Y_t}^{\gamma} \, dZ(t) \\

& Y_0\,=\,y_0

\end{align}

The density of this SDE depends upon the parameters given as$(y_0, \kappa, \theta, \sigma, \gamma, T) $ . For a
particular combination of these parameters, we can easily simulate this density using monte carlo and represent it in
terms of a eight coefficients Hermite series using regression of monte carlo sample on Hermite polynomials of
discretized normal density. These coefficients would be different for all of the combinations of parameters of the SDE.
Since out eight parsimonious coefficients of the particular density are derived from an analytic process, they would
change smoothly with a change in parameters of the SDE. So we can use another Legendre orthogonal polynomial regression
on SDE parameters to find these coefficients from the parameters of the SDE. So given SDE parameters, we would be able
to quickly generate the coefficients of the particular SDE using Legendre coefficients and these coefficients could be
used with Hermite polynomials to find the density of the SDE with particular parameters.

Generation of Sample of SDE densities By Randomization over Input Parameters of the SDE

In order to represent coefficients of Hermite-series of densities of SDEs with Legendre polynomial series, we have to
generate large number of Hermite-series coefficients samples over the given range of parameters of the SDEs. There are
six parameters of the SDEs on which we want to regress Hermite-series coefficients. It is not possible to make a six
dimensional uniform grid for these parameters. So we randomize and draw five dimensional uniforms( and treat time by
mapping time grid on a uniform) and map them on range of SDE parameters. We also use antithetic sampling in drawing five
dimensional uniforms. We make several thousand draws of five dimensional uniform parameters and simulate the SDE in time
for each value of five dimensional input parameters. In the next section, we describe how to find Hermite series from
monte carlo simulations of SDEs.

Estimation of Hermite-series density From SDE Numerical Data

Estimation of coefficients of Hermite-Series From numerical data works by regressing data observations on hermite
polynomials associated with a discrete grid version of standard normal density.  We know that in Hermite series of a
random variable, our data observations of non-Gaussian random variable and the underlying standard normal random
variable are mapped on each other through common CDF values.

Therefore, in this method first we have to construct a discrete grid on standard normal density so that number of
discrete grid points on standard normal density match the total number of data observations and  probability mass
associated with each grid cell matches the probability of each data observation and CDF of each discrete standard normal
grid center matches the CDF of Hermite representation of each data point.

Construction of Discrete Normal Density on Data Grid And Regression of Non-Gaussian Random Variable Data Observations on
Hermite Polynomials.

We suppose there are a total of P data observations of random variable X whose Hermite-Series we want to find. In order
to find coefficients of Hermite-Series, we have to regress each of the P data observation on N hermite polynomials of a
discrete normal density point associated with the data observation therefore grid size of discrete normal density should
also be P. We also know that probability mass of each data observation is$\frac{1}{P}$ , so the probability mass of each
grid cell on standard normal discrete grid should also be$\frac{1}{P}$ . The centres of these grid cells represent the
discrete grid normal density points. In order to numerically construct this discrete standard normal grid of size P, we
start out symmetrically from median and make boundaries of grid cells so that probability mass within each grid cell is
$\frac{1}{P}$ . This way we can make a symmetric grid around median that can be mapped on data observations through
equivalent CDF.

We regress our observations of non-Gaussian random variables on the Hermite polynomials calculated at these discrete
grid normal density points.

We have assumed that first derivative of non-Gaussian random variable with respect to standard normal random variable is
positive, and it means that data can be re-ordered in increasing function (sorted in ascending order) and assigned to
increasing order of grid points on discrete normal density grid points we constructed earlier.

Once we have constructed discrete normal grid and associated each point on it with sorted data points, we simply regress
data points on Hermite polynomial values calculated at particular standard normal discrete grid point on the associated
sorted data in a least square fashion to find regression coefficients that also represent the coefficients of Hermite
polynomials in the Hermite-series.

If there are P data points, and we use N Hermite polynomials to represent the Hermite-Series of X, then our regression
equation for each pth data point would be

\begin{equation}

X_p\,=\, ah_0 \, + \,ah_1\, H_1(Z_p)\,+ \,ah_2\, H_2(Z_p)\,+ \ldots \,+\,ah_N\, H_N(Z_p)\,

\end{equation}

with the matrix equation given as

\begin{equation}

\begin{bmatrix} 1 & H_1(Z_1) & H_2(Z_1) & ..... & H_N(Z_1) \\

1 & H_1(Z_2) & H_2(Z_2) & ..... & H_N(Z_2) \\ ... & ... & ... & ... \\1 & H_1(Z_p) & H_2(Z_p) & ..... & H_N(Z_p) \\  ...
& ... & ... & ... & ... \\

1 & H_1(Z_P) & H_2(Z_P) & ... & H_N(Z_P)

\end{bmatrix}   \begin{bmatrix} ah_0 \\ ah_{1} \\ ah_{2} \\ ... \\ ah_{N} \end{bmatrix} \\ \,=\, \begin{bmatrix} X_1 \\
X_2 \\ ...  \\  X_p \\ ... \\  X_P \end{bmatrix}

\end{equation}

\begin{equation}

\boldsymbol{H \, a_h}\,=\,\boldsymbol{x}

\end{equation}

and we solve this equation with least squares as

\begin{equation}

\boldsymbol{a_h}\,=\,\boldsymbol{{\left(H^T\, H \right)}^{-1}\,H^T\, x }

\end{equation}

Regressing Hermite-Series Coefficients,$\boldsymbol{a_h}$ Found in Previous Section Over Legendre Polynomials of
Parameters of the SDE

Standardization Of Hermite-Series Coefficients

We want to regress each of the$ah_n$ on Legendre polynomials of SDE input parameters
$(y_0, \kappa, \theta, \sigma, \gamma, T) $ and all their cross products with first powers. We standardize each of the
SDE coefficients in sample with square root of variance of the SDE. This variance is given as

\begin{equation}

Var_{Y}\,=\, E \left[ {Y}^2\right]\,=\, \sum\limits_{n=1}^{N} \,{ah_n}^2 n!

\end{equation}

and we standardize all coefficients with this variance as

\begin{equation}

\bar{ah_n}\,=\, \frac{ah_n}{\sqrt{ Var_{Y}}}

\end{equation}

Please note that variance of density with these standardized coefficients would be unity. But we would also need to
regress the square root of volatility on parameters that could be used to inverse this standardization back to original
values of coefficients of Hermite-Series.

We do Legendre polynomial regression of eight coefficients and Square-root of volatility on Legendre polynomials of
uniforms of input parameters associated with each observation of Hermite-Series Coefficients of the SDEs in the sample.

Doing Legendre Polynomial Regression

For a complete regression, we would have to include all of the five or six SDE parameters and their possible
cross-products with first powers and we would have to regress each of the eight Hermite-Series coefficients and
square-root of variance on the Legendre polynomials of these parameters and their cross-products. To make the exposition
simple, we suppose that we want to Legendre-regress one Hermite-Series coefficients$ah_1$ on two parameters$\kappa$ and
$\theta$ of the SDEs and their product$\kappa \theta$ . Let us suppose that we simulate two dimensional uniforms and map
them on parameters$\kappa$ and$\theta$ and make P different monte carlo simulations of the SDEs based on P sets of
random values of input parameters$\kappa$ and$\theta$ . We would also find corresponding P sets of values of eight
Hermite-Series Coefficients$ah_n$ from each of the monte carlo simulation of SDEs with P sets of input parameters.
Suppose, we include N Legendre polynomials for each of the three explanatory variable in the regression. Then, for each
of the pth$(p\,=\,1, \ldots,P\,)$ data observation for each of the input parameters and their product$\kappa$ ,$\theta$
and$\kappa \theta$ , we would need to find the corresponding point on their respective uniform densities. The
corresponding values of uniform variable for pth observation of$\kappa$ ,$\theta$ and$\kappa \,\, \theta$ would be
represented as$U_{\kappa_{p}}$ and$U_{\theta_{p}}$ and$U_{\kappa \theta_{p}}$ .

The final regression equation would be given in the matrix form as

\begin{equation}

\begin{bmatrix} 1 & L_1(U_{\kappa_1}) & \ldots & L_N(U_{\kappa_1}) & L_1(U_{\theta_1}).& \ldots.. & L_N(U_{\theta_1}) &
L_1(U_{\kappa \theta_1}).& \ldots.. & L_N(U_{\kappa \theta_1}) \\

1 & L_1(U_{\kappa_2}) & \ldots & L_N(U_{\kappa_2}) & L_1(U_{\theta_2}).& \ldots.. & L_N(U_{\theta_2}) & L_1(U_{\kappa
\theta_2}).& \ldots.. & L_N(U_{\kappa \theta_2})  \\ \ldots & \ldots & \ldots & \ & \ldots & \ldots.. & \ldots \\   1 &
L_1(U_{\kappa_p}) & \ldots & L_N(U_{\kappa_p}) & L_1(U_{\theta_p}) & \ldots & L_N(U_{\theta_p}) & L_1(U_{\kappa
\theta_p}).& \ldots.. & L_N(U_{\kappa \theta_p}) \\ \ldots & \ldots & \ldots & \ & \ldots & \ldots.. & \ldots \\

1 & L_1(U_{\kappa_P}) & \ldots & L_N(U_{\kappa_P})  & L_1(U_{\theta_P})  & \ldots &  L_N(U_{\theta_P}) & L_1(U_{\kappa
\theta_P}).& \ldots.. & L_N(U_{\kappa \theta_P}) \\

\end{bmatrix}   \begin{bmatrix} \beta_0 \\ \beta_{\kappa,1} \\ \ldots \\ \beta_{\kappa,N} \\ \beta_{\theta,1}\\\dots \\
\beta_{\theta,N} \\ \beta_{\kappa \theta,1}\\\dots \\ \beta_{\kappa \theta,N} \end{bmatrix} \\ \,=\, \begin{bmatrix}
ah_{1_1} \\ ah_{1_2} \\ ...  \\  ah_{1_p} \\ ... \\  ah_{1_P} \end{bmatrix}

\end{equation}

\begin{equation}

\boldsymbol{L \, \beta}\,=\,\boldsymbol{ah_1}

\end{equation}

and we solve this equation with least squares to find the regression coefficients of equation as

\begin{equation}

\boldsymbol{\beta}\,=\,\boldsymbol{{\left(L^T\, L \right)}^{-1}\,L^T\, ah_1 }

\end{equation}

Re-Standardization of Hermite Coefficients

We find the Hermite Coefficients of an SDE from their parameters using the Legendre regression as given in previous
section. We know that variance of density from these coefficients should be unity as they had been standardized prior to
regression. However this variance would be very slightly different from one so we adjust the coefficients to retrieve
unit volatility from the relationship

\begin{equation}

\bar{ah_n}\,=\, \frac{ah_n}{\, \sqrt{\sum\limits_{n=1}^{N} \,{ah_n}^2 n!}}

\end{equation}

The regression of Hermite-Series parameters after Standardization and re-standardization after calculation of
Hermite-series Coefficients as described above, further improves the match of resulting SDE density with True density.

In order to find the true values of these coefficients of Hermite-series of an SDE, we would have to multiply above
standardized values of coefficients with square root of variance of the SDE. We also regress this square root of
variance of SDE as a 9th regression along with eight regressions for each of the hermite-series coefficients. If this
square root of variance of an SDE is known in closed form from other analytics, we can use that and multiply it to find
the true coefficients of Hermite-series of the densities of SDEs.

Improvements In the Math AI Polynomial Regression Algorithm

As shown in some of the previous posts on this forum, I was getting very good R-squared for the above regression to find
parameters of Hermite Series of densities of SDEs when randomization is done over four parameters. We expect that adding
analytic or numerical estimates of variance of the SDEs in Legendre basis functions would make the method just about
perfect with almost zero error.

We also want to improve the method by transforming the densities of SDEs to their square-roots or logs and then
Legendre-regress the coefficients  of Hermite series of square-roots or Logs and use them to construct the density more
accurately.

Reference

https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4933283

---

### #2486 — Amin (Topic Author)
*October 22, 2024, 1:59 PM*

Friends, as many of you would already have known by reading many of my post that I am on mind control by American
defense since  end 1997/ early 1998. I was a student in Economics department in NYU and had taken a few courses in Math
department during fall semester of 1997. A jewish professor in math department of NYU was slighted by my talent for
Mathematics and asked US defense to put me on mind control. Mind control was well known in many jewish circles even in
1997 since a jewish billionaire and his cohort of rich jews (who were very close to American defense) at that time was a
major force behind mind control and many people were put on mind control from time to time and a lot of jews knew who to
contact who would suggest to American defense to start somebody's mind control. Though I know I have blamed jewish
circles for systematic mind control I am very aware that a large number of Jews, just like most of the other people, had
nothing to do with mind control and I am not blaming every jew for this practice.

Even after mind control started, I continued to work and do my research in NYU. For almost a year, I had no idea that I
was under state mind control but I knew something was very wrong with me and many times I would for example try hard to
read some book for hours without getting any meanings in my brain. And due to several suspicious things, I had realized
that some people were freely entering my apartment in my absence. Once I approached a dean or vice-dean(I forgot the
exact designation now) of my school of natural sciences and told him about my problems and he suggested that I should
seek psychiatric help. In fact, I later realized that some people at the university were actively trying to detain me or
force psychiatric medicine on me so that they could give me anti-psychotics or other medicine to damage my brain.
However, despite all mind control, I was a very decent guy and I approached all people very nicely and never misbehaved
in any way so nobody could have any possible pretext to hospitalize me.

However, when I realized that American defense was after me and they were systematically adding drugs in the food at
many places I regularly buy food, I was very worried and I realized that I had no future in United States even though I
wanted to build my future there. A few weeks after this realization, I decided to leave United states and come back to
Pakistan. However, during one year of mind control, many mind control agents had realized that I had several special
neurotransmitters and I would become successful even in Pakistan if they ended my mind control. So they contacted my
Parents with promises of huge money to cooperate with them. My father was a reasonably successful businessman at that
time but we were still a middle-class family even though he paid for my tution in the university. Mind control agents
had probably told him that my brilliance would be gone but I would continue to do most things normally and everybody
including myself would be better off if the family cooperated otherwise they would still stop me with an iron fist if my
family did not cooperate.

When I returned to Pakistan from flight to USA at February 1999, I stayed in my uncle's home. Next day about twelve
people came to my house and tied my hands and legs and forced me to drink a thick jelly like liquid in a bowl,
immediately after taking that liquid, I started shivering and I continued to shiver all night. I was so sedated that it
was even difficult for me to lift my eyelids. Next day I was taken to an army hospital in Rawalpindi from Lahore and an
army psychiatrist talked to me. I could barely talk but he immediately identified me of Paranoid Schizophrenia saying he
thinks CIA is after him. He detained me in his hospital for two weeks and then I was allowed to go to my home town in
Kot Addu where I was regularly given antipsychotic pills and injections. I continued to take the medicine in my hometown
for several months without seeing a doctor again and after a few months I was all yellow since one of the antipsychotic
medication had backfired and I developed drug induced jaundice. I was taken to the same doctor again and he immediately
ended most medication and I was taken to another specialist doctor in army hospital for treatment of liver. I heard my
sister tell the liver doctor that I was still being given an antipsychotic that did not metabolise through liver but
doctor was upset that my condition was very serious and they should end all medication. I was given a glucose drip every
day but my biluribin continued to increase. There were blood marks all over my legs as I just could not help scratching
my body due to extreme itching. After a month, doctor suggested that I had to be given two glucose drips everyday and
then slowly my biluribin started decreasing. I continued to get glucose drips for at least four months and then I was a
bit better.

Later I was taken to another doctor who started my treatment by giving me electric shocks for two weeks. I still recall
that they would take me to an operation theatre every other day and doctor would place a wooden wedge between my teeth
and give me an anesthesia injection. I still recall how numbness would move from my lower body to upper body before I
would be fully unconscious.

Later another psychiatrist doctor told me in 2016 that giving electric shocks at the start of treatment without trying
chemical means is considered criminal at many places.

It is not possible to narrate everything in limited time but I have been kept under antipsychotics during past twenty
five years. By chance, I came under treatment of a good psychiatrist in 2016 who was not ready to give me any strong
antipsychotics at all and told me that criminal psychiatry was highly practiced in United States about a hundred years
ago. He even advised me to become independent and live separately from my family on my own (I could not become
independent because despite my wonderful research nobody would give me any work or job because American defense and
Pakistan army would approach everyone in Pakistan or all other advanced countries (Europe, Japan, India, S Korea,
singapore etc.) and force them to not give me any work or anything). Later I was forcefully taken by my family to a
different psychiatrist and they would threaten to detain me whenever I would ask that I wanted to see the same good
psychiatrist.

For other background, I want friends to read my older posts that I would copy after this.

To cut long story short, I was being detained regularly by different psychiatrists every year. One psychiatrist detained
me for about a year and when I told him that I wanted to live independently of my family after becoming free, threatened
to detain me indefinitely if I did not agree to live with my family. I have also been detained at least for six month
twice and  for fifty days more than ten times. All doctors simply said that my schizophrenia was acute and my insight
was gone and I did not trust my family. This is despite I never fought or was physical with anybody ever. There is no
human being who can make this claim that I physically touched them in wrong or abusive way. I never damaged anything and
have always been absolutely nice with everyone.

 So basically every year they would detain me with a psychiatrist, and would set up all the mind control gadgets in the
facility and would also openly drug the food that I would be given and would also give me all sort of high antipsychotic
medication. The purpose would be sap all special or intelligent neurotransmitters out of my brain every year once they
would have come back. I was also resolute and every time I would come out of detention, I would re-start my research and
start working again even though it would be a very difficult and uphill task. And since CIA was omni-powerful, once they
would see that I had started doing good research again, they would detain me again and take out all the
neurotransmitters they know I was using.

However, I have not been detained after early 2020 and that was the last time I was detained. Since I had been able to
do some good research, and it was noticed by some good people, many of those good people and good human beings in United
States strongly protested to American defense against such cruel and inhuman practice. I was still threatened many times
and might have been detained but I would mention it on this forum and many people would protest strongly and I would get
a lease of life again.

And I could not have possibly done any good research if it were not due to strong protests from many good American
people, and if I have done any good research, I owe it to support from many people who made sure that I would not be
detained in a cruel and inhuman way again.

However, I am still on some antipsychotics and get an antipsychotic injection every month. This month my mother did not
talk about the injection but a few days ago she told me that I should get the injection. I will be getting an
antipsychotic injection on 24th October.

However, for past one week, they have hugely increased giving me gases and sometimes especially today they were giving
me a gas that would cause very severe pain in my heart. And I am very worried about my increasing persecution.

I am very sure that mind control agencies and American defense plan to start detaining me again if Trump comes to office
in November. I want to request all friends especially all good Americans to protest to American defense about my
continuing persecution. And if you know any politician in office well, please ask them to very strongly protest to
American defense against this continuing cruelty and put an end to this. I am very afraid that I would strongly need
help of friends if Trump got elected in office again especially since my mind control that was fast decreasing, has had
a complete resurgence recently when current vice president's chances started to decrease.

For all those friends who have not been following me, I am copying two posts from before and please read my application
to Human Rights Watch for help.

---

### #2487 — Amin (Topic Author)
*October 22, 2024, 2:10 PM*

[My Letter To HRW About My Human Rights Abuse](https://forum.wilmott.com/viewtopic.php?f=15&t=102298)

Above is a very incomplete account of how various psychiatrists continued to play in hands of Pakistan army to retard
me. It also does not cover all the time till year 2022 and the account stops several years earlier.

I was a very simple, very meek but also very hard working student at a large university in New York and joined the
university in 1997. My mind control started in very late 1997 when a racist jewish professor in Math department of my
university was threatened by my talent and approached the Jewish Billionaire to ask American defense to put me under
mind control. Even that long time ago, a large number of jews were very aware that this Jewish billionaire was a
Godfather of mind control and would approach the billionaire to recommend talented people to mind control from time to
time when they would be threatened by their talent. Over past twenty five years tens of thousands (if not more than a
hundred thousand) of innocent people mostly American nationals have been placed on mind control abuse by scumbags of
American defense on recommendation of Jewish billionaire. Most universities in US  have a couple of jews who continue to
keep eye on brilliant students of the university and recommend them to American defense through jewish billionaire when
they feel threatened  by the talent of the students due to any reason like their religion, race, ethnicity or just
because they are not jews.

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
line, several thousands of brilliant whites are retarded across United States by mind control agency every year that has
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

https://forum.wilmott.com/viewtopic.php?t=99702&start=2325#p881807

https://forum.wilmott.com/viewtopic.php?t=99702&start=2325#p881808

https://forum.wilmott.com/viewtopic.php?t=99702&start=2325#p881886

https://forum.wilmott.com/viewtopic.php?t=99702&start=2340#p881951

Friends, this speaks volumes about headstrong cruelty of people in American defense and their Jewish billionaire backers
cohort that they are even more ready to show me cruelties even after people have a widespread knowledge of their
machinations and tactics. These evil people have no intention or desire to decrease their torture on me despite that I
have been telling tales of their inhuman torture on me over past twenty five years through various psychiatrists.

Please read the following two posts to see the context how I have been maltreated by various psychiatrists on behest of
mind control agencies over past 25 years.

Friends, I have been on forced antipsychotics for most of the time since early 1999. There were a few periods of a few
months when I remained free from antipsychotics. But other than two or three such periods, I have remained on
antipsychotics. It is very hard to feel well when huge antipsychotics are forced on someone who is mentally healthy. I
have also been detained forcefully tens of times whenever some of my neurotransmitters came back, the purpose of
detention was to take brilliant neurotransmitters out of my brain and send me back home with a relatively retarded brain
after the end of months long detentions. I have seen sheer trauma, torture and brutality on the hands of these
psychiatrists who connive with American defense and Pakistani military to declare me mentally ill so they can force
antipsychotics on me. I will be 51 this year and portion of my life that I lived under mind control has exceeded the
part of early life that I lived without mind control.

I have a phone meeting with the psychiatrist on 14th of June 2024. And I am sure the psychiatrist will try again to keep
me under medication or even increase my medication. Even after a large number of people have become aware of truth about
mind control and accompanying persecution by the psychiatrists, most psychiatrists are not the least worried that their
wrongdoing is being exposed in public.

I want to request good Americans to please protest to American defense, mind control agency, Pak army and relevant
psychiatrists to please end this cruel practice of declaring healthy people on antipsychotics and forcefully detaining
them up to years in their faciiities.

When they detain me, they have fixed all mind control gadgets and lasers in the psychiatric facility and they add all
mind control chemicals openly in food and psychiatric drugs. It is a very controlled environment in captivity and within
a month or so, they are able to remove all neurotransmitters from the brain of the victim. Every time I was detained,
they kept me in the psychiatric facility for 30-50 days. One psychiatric even detained me for ten months after I
returned from Britain. There are also instances of being detained for six months once and three months twice.

I really want to request American people again to please protest to their government and try to make sure that I am not
being detained again on totally flimsy psychiatric grounds.

.

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

---

### #2488 — Amin (Topic Author)
*October 22, 2024, 2:13 PM*

Friends, I want to describe again what happens to victims of mind control on a regular basis.

First thing is that EM waves emitting devices and lasers are fitted all over my room and also in all other rooms of my
family home. For example when I am having a good deep sleep which is rather unusual, they would target my head with
lasers and high frequency waves and I will feel very tired when I would wake up as if I had not slept at all. Just like
neurotransmitters, when molecular weights of enzymes and hormones is known , they can be targeted with resonance of
appropriate frequency to not allow them in certain areas of the body or at least decrease their concentration in
particular areas. For example when I had a foot fracture in 2014, they never allowed it to heal properly by targeting
waves of appropriate frequencies on the fractured area. Many times when I am working in my good spirits in my room or in
garage etc, the mind control agents would point high frequency lasers towards my forehead to cause pain so that I would
not be able to concentrate on anything and get angry and start ranting and would not be able to work anymore. Sometimes,
when they are more cautious, they would simply point EM waves with appropriate resonance to cause me to sleep or become
drowsy. They change the position of a lot of devices everyday based on their anticipation of position and place where I
would next work on my research and sleep.

In our house, every bed, sofa or chair that has foam on it, causes severe itch in my back when I sit on it. I think this
is because they inject some chemical that settles in pores of the foam and then becomes volatile when EM waves of a
particular frequency are focused on it. The volatile chemical enters the body of the mind control victim through the
anus since it has "potential" to combine with some of the neurotransmitters in the body. It is extremely painful to sit
on these beds, sofas or chairs. If I have to do that, I place two or three cotton pillows on top of the foam bed, sofa
or chair and then sit on the pillows. I have a large double bed in my room but I never sleep on it and instead sleep on
a small cot (with cotton filled quilts beneath me) in my room since it is impossible to sleep on the bed. Again sleeping
on the bed causes unbearable and very large physical pain and huge itch in the anus.

It is impossible for the victim to shower everyday since the water in the washroom is charged with mind control
chemicals that make the victim feel half faint and totally energy-less. Several years ago, I discovered the water in our
kitchen did not have mind control chemicals to charge the skin and I would simply take water from the kitchen to the
wash room and take a rich sumptuous shower. Even though mind control was not very high at that time, they closed the
loophole after a few weeks.

Soaps of all large Pakistani companies have mind control chemicals in them that charge the skin and when EM waves are
focused on the face, forehead and the skin, the victims feels a completely altered consciousness and sometimes extreme
anxiety and nervousness. I have been living on Indian soaps (Did we separate from India only to fill the pockets of
corrupt scumbag generals of Pakistan army who take hundreds of millions in bribes from CIA and then heroically stab
"dhirti mata"/motherland in its back?)

The antipsychotic drugs and injections are mixed at the manufacturing source on orders of scumbags of Pakistan army and 
they have a huge deteriorating effect on the victim. They would take away all neurotransmitters from my body  they can
using mind control injections and I would not be able to have a proper conversation with anyone or do any research work
until 7-10 days after the injections. I would have muscular pains and other aches all over my body. Sometimes they take
away some special neurotransmitters from the body and the victim would feel as if he is losing all energy in the body
and the victim would have to eat something or take a drink to get better. This happens to me all the time despite my
sugar tests both fasting and random and H1BAC are perfectly good. Since food is one of the only few things that can help
you get better when the victim is under mind control drugs, my weight has increased beyond limits and I am 30 kg over
weight now.  There were small periods when I did not take antipsychotics and my weight decreased quite fast in those
periods so I expect if my antipsychotics filled with mind control drugs end, I will easily lose a lot of weight quickly.

I tried to re-start my morning walk several times last year but mind control agents tried everything in their power to
deter me by taking out my neurotransmitters and even went to the limits of Police threatening me to walk not on sidewalk
of  public service roads but in parks only (Police has no such authority but they can harass anyone). I have done a
complete post on this harassment incident somewhere else.

They can even kill the vicitm remotely when the vicitim is under mind control drugs but the scumloads of American
defense have still not done that to me.

Another very nasty thing these "proud" scumloads of American defense do is that when the vicitm goes into wash room
where his penis is exposed, they use some device that throws small amount of some chemical that settles on the tip of
the penis and then they target the victim with EM waves and it causes unbearable and excruciating pain. I am recalling a
few older posts about this. They used to do this routinely but when my research got known well, they stopped doing it.
This is from more than three or four years earlier.

This is an excerpt from post 971 written on June 01, 2019 here: [forum.wilmott.com/viewtopic.php?f=15&t=94796&start=960#p846210](https://forum.wilmott.com/forum.wilmott.com/viewtopic.php?f=15&t=94796&start=960#p846210)
> Ok, I am not complaining but I decided to write this post several days ago when I was forced on shameful and
humiliating torture three days ago. They locked directed energy on the tip of my penis and it was very painful and
unsettling for me. I urinated more than twenty times in two hours. I would feel better when I would be able to take a
very small amount of urine out of my penis each time. They had done this two times previously for several hours but I
did not write here since I thought that it was a self-humiliating exercise to tell people about my persecution like this
but when they did it last time, I decided to write about it lest it becomes a common practice and starts to happen
everyday. I would say again that many of these mind control people have absolutely no respect or regard for my or
anybody's human dignity. I want people to recall how American army soldiers were openly urinating on prisoners in
Abu-Gharib and most of the staff there knew about it but such humiliatory actions were considered perfectly normal by
most of them. It was until the tapes were run on TV and news was on air everywhere that many of them started to think
that we have made a mistake. Mind control agents are not very different and when they are angry about their failure in
controlling me, they resort to punishing me using humiliating actions like targeting directed energy on the tip of
my penis. I would like to ask Americans if such actions represent American ethics and mentality and if they do not
represent American ethics I wonder why such things do not stop even after I write here openly about them. Please own
your actions if you do not want to stop them.
>
>
> I want to ask friends that some of the mind control agents become extremely mean when they fail to control their
target victim properly and they resort to such ugly tactics. For example one of the tactic mind control agents used to
exercise was that they would make a very little injury/cut on my tongue with microwaves. It will not bleed but it would
be constantly painful all the day since tongue is extremely sensitive. This used to happen almost every two weeks or ten
days. They charged my penis this morning today, as I mentioned in post #1063 written this morning, again though it was
far less severe than what I have described in the above post but such activities continue unabated and the experience
this morning made me recall the horrible experience above. I want to request friends to force the mind control agencies
to replace the guy who controls me as he has a very mean nature which is evident from the above post.
.

https://forum.wilmott.com/viewtopic.php?p=854970

.
> I have previously told friends that, during brain control, charged ions enter the body from every opening we have into
the body. I am very sorry to write this here and want to make an apology to friends for the relatively gross nature of
this post. But I would like to tell friends that  I firmly tape my penis with a paper tape to prevent charges going
inside it. When I do not do this tape, my eyesight sharply deteriorates and I become extremely lethargic. There are such
things I never mentioned on this forum because they are too disgusting to mention but once the torture continues, I
finally decided to mention some of the things here. The way it works for the charges to go into the body, I believe,
they release a small amount of very ionizable gas in the air and charge a pathway through gaseous air with laser beams
towards the body, for example towards the mouth, nose or the anus and apply potential across it. At the same time, they
create opposite potential by ionizing the chemicals that have gone into the body with food using microwave resonance
caused by laser beams. And then chemicals mixed with ionized gas start to go inside the body from the anus etc and this
becomes a self-sustaining process as long as the potential is maintained at both ends. I have seen a lot of such
instances over past twenty years of persecution when chemicals will zap inside through the anus causing severe pain. I
believe flow of charges is really directly proportional to applied potential and pathway conductivity caused by the
ionized gas.  I keep some soft tissues in my anus as it helps. I have tried other things that could more firmly block
the anus but then mind control agents greatly increase the potential and it causes extreme pain and minor seepage like
bleeding(it might possibly be because of very high frequency microwaves). Mind control agents love such torture tricks
that prevent people from doing anything that blocks their mind control. I also tried other tricks like lubricating the
anus but they would simply and freely add mind control chemicals that would charge the body to the creams and lotions in
the supermarkets just like they drug the food on the shelves. I am sure these practices are done all over the world
since adding chemicals to creams and lotions was widely done when I was in UK for six months and even upscale chains
like body shop and others had ionizing chemicals added to their creams and lotions once mind control agents would
suspect that any such shop could fall on my way.
>
> Ok, mind control agents in Pakistan had been making anywhere between 10-40 million dollars per year depending upon how
good the year had been for mind control operations. These agents want to continue mind control one way or other. These
agents tell their like-minded hardliner right wing bosses that there are certain things I never mention in my writing of
the journal (because they are probably too disgusting to write) and these are the things mind control agents need to
apply for my mind control since people would not know about these practices when they would not be written in the
journal. A few weeks ago I mentioned briefly that they cause severe itching in my back/anus but then I never wrote about
it again even though it continued. They almost always have charges going into the body of the target from the back but
sometimes it becomes very painful. And yesterday, it was again so painful that several times I would step up from the
chair while working on my research, open my pants and rub and scratch my anus and replace the tissue that has already
been charged but they would continue to increase potential again and again and I would be repeating the whole thing
again. I also woke up several times at night due to sheer itching in my anus.
>
> I had talked about reprieve from gas in my room in the previous post but I fear that might have been because for past
three to four days before writing of that post, I did not leave the home for long and mind control agents might not have
enough opportunity to come to my home and recharge the ionizing and resonance laser beams and refill the gas because I
remained in the neighborhood very close to home and returned quickly.
>
> I want to request all good American people to force their government to stop such inhuman, cruel and  animal barbaric
practices on other humans only because some powerful people in US do not like intelligent muslims/others to excel and
use their influence to continue such animal practices that hurt the image of American people and such practices are
becoming more and more of a norm with every passing year. Sorry to say but there are good and bad people everywhere in
every country, culture and religion and US is no exception. In US where many bad people do not openly do bad things
because being cruel to other humans is really not appreciated by the American society, but when evil and cruel people
know that their cruelties would not be noticed by the general american people, they are very ready to expose their true
nature and use the methods of cruelties and persecution when they are sure these things would not be noticed by the
American people. These evil, bad and cruel but powerful people have no regard for the goodwill of American people but
just want to use their influence in US right wing to extend their personal agendas. I am very sure if all of these
things would be known to American people in their true entirety, none of these mind control persecutions would ever take
place.
.

Post 1370 on this thread.

.
> Friends, I drove from Islamabad to Kot Addu today. It took me around eight hours to reach kot Addu. Long drives are
very stimulating and I thought of several new ideas both about SDEs and stocks trading. But when I reached Kot Addu, I
had extreme uneasiness in my penis since mind control agents continued to charge my penis on the way as I had to be in
the same accurately predictable position for many hours sitting in the driving seat. After reaching home, I urinated
again and again to feel better but it did not work. I also realized that my urine was reddish as there was blood mixed
with urine as I urinated.
>
> When they force electromagnetic waves inside the penis, the body tissues inside the penis tube get damaged and blood
starts to seep through the tissues and gets mixed with urine. Forcing waves into the penis is a very important part of
mind control since it is impossible to control adrenaline and dopamine without controlling the sex organ. Adrenaline and
dopamine give us drive to concentrate and force ourselves to work hard so mind control agents really have to control
these and several other similar neurotransmitters and they have to force waves into our penis to be able to do that.
>
> I normally do not like to urinate in the wash room since when I urinate there, it is very easy for them to force high
frequency waves inside the penis and it feels like a needle is going into the penis when urine is coming out and high
frequency waves are going inside. I would rather take a mineral water bottle and urine into it in my room and drop the
urine in the wash room and wash the bottle to use again. But if I would remain in a single place in my room to urinate,
they install gadgets and urinating in my room is no different from urinating in the wash room as they can again force
waves into the penis and the target victim would have needle like feeling going into the penis so I have to continue to
change places randomly in my room to urinate.
>
> Anyway they were doing the same thing again and blood was coming out of my penis mixed with urine as I supposed the
inside of tube that carries urine out of our body was damaged due to high frequency waves. This is very serious thing so
I decided to write about it so as to deter the mind control crooks who are bringing a great name to American people by
such feats. But these hardliner conservative crooks in army will continue their ugly antics since their desire to enter
the paradise of Jewish billionaire godfather is stronger than regard for any country or any human ethics.
>
> Previously I had told friends several times (may be eight or nine times in total) that they force chemicals into my
mouth when I am sleeping. This is sheer science though I do not know underlying exact details but I know they can create
potential at a precise place for special types of ions(neurotransmitters) emitted from elsewhere with lasers and EM
waves. Well I continued to mention that they charge my mouth every night with special mind control chemicals that settle
on my tongue and inside of upper jaw and my mouth is very bitter and I have to wash it or brush inside of my mouth to
feel better. I continued to mention it again and again on this forum but they never stopped so I stopped writing about
it.
>
> I want to tell Americans that Americans are mostly not bad people at all but these hardliner conservative crooks in
army and mind control who are dying to enter the paradise of the jewish billionaire godfather are not bringing any good
name to Americans with their inhuman machinations.
>
> Another thing I have mentioned several times before is that I find likes on several linkedin posts (in my activity)
that I never liked. They know my passwords and have enough control over my computer and they repeatedly like something I
never liked (I never like anything unless I strongly feel about it which is usually relatively rare). This is something
that gets known to me since there is a log of every like in my Linkedin activity. Imagine what else they are doing from
my internet traffic that I never came to know.
Another big problem is that when I approach people all over the world for consulting projects, the scumloads of American
defense reach them as well with their infrastructure in that particular country and threaten people to not work with me
or give me any project. Depending upon the nature of person, they would tell some particular lie so that they would not
be willing to work with me at all. In past 14 years, I have only earned 3500 dollars.

I have tried to hold despite all odds and tried to do good research. If things were as good as with other people free
from mind control, I would have been able to do far better research. From my side, I am not enemies with anyone and
would like everyone to use my research and make money utilizing it.

Again the The rich anal jews including the jewish billionaire are extraordinarily pleased when they hear these torture
stories and reward the scumloads of American defense (who are ready to do any nasty, disgusting or degrading thing to
other humans to prove their allegiance to rich jews). These scumloads of American defense, whose arrogance pierces
through the seventh sky, would do every anal and disgusting thing to innocent and intelligent victims in order to please
the rich jewish cohort who would in turn reward them with great jobs and high social status in successful jewish
companies and these scumloads of American defense have absolutely no regard for anybody's human diginity once rich jews
have beaconed them to retard someone.

Friends, when I returned from United States, I was taken to a military psychiatrist in Rawalpindi who immediately
diagnosed me of very acute schizophrenia and gave me an antipsychotic Larjectil along with other biweekly injections.
This drug is known to cause drug induced jaundice in some of the patients. After seeing the doctor in Rawalpindi, I was
brought home in Kot Addu where I lived for four or five months without seeing any doctor in the meantime while taking a
steady dose of Larjectil. However after a few months my color and eyes became totally pale even though I was not feeling
anything odd other than probably strange color of my stool. However one month further later my condition became very bad
and I started to become very weak physically. When everybody became alarmed, I was taken again to the same psychiatrist
in Rawalpindi who immediately knew that I had jaundice and immediately stopped my medication. I was still feeling
reasonable but the nightmare was yet to follow. Within a few days of stopping the drugs, I had so severe itch in my body
that it is totally hard to describe. I could not sleep for a whole month due to sheer itch. I simply could not resist it
at all and there were blood marks all over my legs and arms due to itching. And I was given a glucose drip every day
with medicine for more than a month but my biluribin continued to increase instead of decreasing. And then doctors
decided to give me two glucose drips everyday and only then after two and half months months (a total of three and a
half to four months) after starting two glucose drips that my biluribin came close to normal. This was one of the worst
times of my life.

Later probably in 2017, I was taken to another psychiatrist the second time. This psychiatrist had earlier given me
electric shocks without interviewing me in order to retard me in year 2001. When I was taken to this psychiatrist again
in 2017, he knew from my history that most antipsychotics had failed in retarding me and he wanted to give me Larjectil
again. He was told that Larjectil had previously backfired and I had extremely severe drug induced jaundice but the
psychiatrist bitterly wanted to experiment and told everyone that it was not necessary that the drug would cause
jaundice every time. And within a few weeks, I was extremely pale all over and my medication had to be stopped. However
for several years, many of my major enzymes remained disturbed and elevated despite that bilurbin had become normal. I
think that severely weakened my liver and now in the tests, friends can notice that several liver enzymes are highly
elevated.

I used to try to eat healthy but everything I would eat consistently, the scumbags of Pakistan army would go after the
company that manufactures that food and ask them to add mind control chemicals to it. I really like taking a glass or
two of packaged Yogurt everyday. On insistence of CIA, Mir Jafirs and Mir Sadiqs (scumbag generals of Pakistan army) of
our nation approached every yogurt manufacturing company and now it is totally impossible to find a brand of Yogurt that
does not contain mind control chemical in it. I simply cannot take healthy yogurt anywhere anymore. Similarly for milk,
I really liked to take some milk every day or two since it is healthy and I would also add it to tea, but now there is
no single brand of packaged milk or tea whiteners that does not contain mind control drugs. And then I used to really
drink a lot of freshly squeezed juices especially in winters since they are so wholesome and absolutely cheap when there
is abundance of fruit. But then Mir Jafirs and Mir Sadiqs(scumbag generals of Pakistan army) of my country would send
their thullahs (sepoys) to every food stall or juice shop in the city and give them mind control chemicals and ask them
to add to some ingredient and continue to add to everybody's food freely. Similarly there is not a single large brand of
water that is without mind control chemicals despite that temperature has regularly been going to a high of 115F to
125F.

I usually take pepsi-cola or coca-cola in glass bottles that have to be returned to shop after drinking. There are
probably eight major types of drinks in these bottles and earlier usually one or two types used to be good and one would
have to really work to find which kind of bottle is good in this month. But when I started drinking these bottles, all
manufacturers started supplying good Pepsi-cola and coca-cola drinks in the city because they realized that these drinks
are extremely bad for my health. Many times when temperature is around 120F, I might have no option other than to drink
a cola to get better. They never allowed water, milk or Yogurt to get better but all colas became good in past two
months. Water bottled by Pepsi-cola and Coca-cola and Nestle is very thoroughly drugged and never became better after
January this year.

I believe that mind control become difficult to work when people take enough calcium. This is why scumbags of American
defense(under Jewish billionaire's command) have to make sure that all yogurt, milk and other sources of calcium are
totally kept drugged with mind control chemicals. Almost all calcium supplements manufactured by different Pharma
companies have mind control drugs in them. I still remember about a week ago I bought a Calcium supplement from Cell
LAboratories and thought that I had never come across it before. I knew most supplements are not good but I thought I
should try it and I took one tablet in the shop right after buying the supplement and in a few minutes I was ranting all
over about evil of jews and biden's mockery of justice to please the jews and there was no end to my rants. When I was
composed after twenty minutes, I took the remaining tablets to the shop and returned them telling that they had caused
very severe headache.

Similalry selenium is very important for proper working of Thyroid but I cannot take any multivitamins since all of them
are drugged on orders of scumbag Mir Jaffars and Mir Sadiqs of my nation to please CIA.

For many naiive people who still believe in goodness of scumbags of American defense, I will like to tell them that I
there were several times in past few years when I became sick and had huge fever. I have had very severe dengue and also
corona and many times just plain high fever. And whenever I would be extremely sick, mind control agents would increase
mind control several fold. I think they would take it as a window of opportunity to possibly be able to permanently
block my neurotransmitters when my mind is in a weakened state and my body is not working properly. I really think that
the reason behind increasing mind control when I would be sick is definitely that they believe that it might become
possible for them to accomplish in weakened state of my body and mind what they have otherwise failed to accomplish. So
much so for the humanity of these scumbags.

My country is firmly in grip of tentacles of Jewish Octopus(of billionaire jewish bastard and his rich cohort)  who are
not ready to let anyone become successful here due to their venom. And there are many such other countries. These bad
jews have restarted their machinations as they always did in their history and when their will be a backlash they will
all start whining that everybody persecutes us for no reason despite that we are so good.

I believe that it is good for every society including US to stop these jewish machinations in their tracks and try to
teach them to respect the dignity of other human beings who are not jewish. We do not want these scumbags to be treated
in any inhuman way and we do not want any human being to be treated with the extraordinary cruelty of these scumbags.
Even if they are incapable of respecting other human beings, I think it is important and good for all of us in the
society to force them to give enough respect to to others and not allow a free hand to their machinations. As opposed to
American defense that has already become a puppet in hands of this bad jewish cohort. We do not want anyone getting
wronged and we do not want any backlash to anyone.

People do not believe in me. They want to find out the truth on their own. Do not believe in google or random articles
on internet.

Ask the history experts in your university why jews were persecuted throughout history? Was there a persistent cause and
effect behind there repeated persecutions. Or different people just took a liking to persecuting them and had fun.

I am not validating any persecution of jews and certainly not holocaust which was one of the darkest chapters of
humanity. Everything has to be dealt with law and with enough human decency and respect for human dignity.

But why was it so easy to turn Germans against jews? Just because they had become too rich?

I do not believe in any political correctness and would like to know the actual true reasons behind it. Even before
period preceding Second world war, Jews had seen many rises and falls in Europe. It would be good to know from true
history experts what were the reasons behind their repeated persecutions.

A poet says that cup of life continues to get stronger as it passes from generation to generation. Because every
generation learns from experience of all previous generations that had passed.

We want to know true history so that we can know true facts about what happened about so many different things and do
not repeat mistakes of the past and be able to stop those things that would later become far worse in light of history.
So if jews were always persecuted when they were innocent, we want to be very careful that it never happens. And if they
were persecuted due to their machinations, we want to make sure we never allow them to express their machinatory side
again.

Tens of thousands of people majority of whom were actually American citizens have been retarded by American defense in
past two decades on insinuation of a Jewish billionaire and his rich jewish cohort. American defense loves this because
all the high ranking officials involved in this massacre are given extremely high paying jobs in Jewish companies after
they retire and they enjoy extremely high social status and therefore they love to retard anyone who the billionaire and
his jewish cohort points towards. Bad Jews have complete control of most vital Arm of American government -- American
defense. Once somebody's (including Americans) neurotransmitters get known early in their student life before they have
become successful, mostly the decision is up to jews to allow them to succeed or ask American defense to retard them by
putting them on mind control for the rest of their life. It is easiest to retard intelligent people in their student
life since most of them have absolutely no resources and most other people still do not know whether they could be
extremely successful in their later life as clearly as mind control agency and associated Jews get to know and therefore
a lot of lies could be fabricated by American defense and told as a reason for retarding the victim. And it is only
people who are supposed to become quite successful that are retarded. For example many muslims who might have actual
venom for jews would almost never be touched at all despite that many jews might know about them but muslims who are
predicted to become very successful are always retarded with an iron fist. Again majority of people retarded are not
Muslims and rather are typical American citizens who have special neurotransmitters.

Please ask for a free and fair Judicial commission to investigate retarding of innocent human beings and punish any
culprits in American defense and Jewish actors behind them. Is justice only to punish menial criminals who have to be
jailed because they snatch money after days of hunger to get some food? Or go after the real and true criminals who are
reworking the fabric of American nation with their extreme meanness and exceptional cruelty. But even though everybody
wants to go after the petty criminals very forcefully and with complete might of the law, not many people in any society
however advanced have courage to ask about trial of big crocodiles who commit great crimes against humanity with
complete impunity. Really interesting and rather ironic.

I know that some of American friends and other people may not like my expressing myself honestly without any political
correctness. I want to tell Americans as I have said several times on this forum previously that I admire so many things
about good American people. Americans are a good, nice and decent people who like to work hard and are some of the most
enterprising people on earth. And I always think that American values coincide with all the good things and practices
that intelligent humanity appreciates all over the world.

And I am indebted to quite a few good Americans who tried to protect me from persecution when absolutely nobody in my
own country was ready to help me. They appreciated my talent and gave me a new life by forcing American government to be
better with me. This is a debt I can never repay all my life.

The purpose of my honest criticism is never to malign Americans and on the contrary I would like to tell everyone that
most American people are some of the best human beings on earth and they would abhor the idea of wronging anyone with
great cruelty. But still there are good and some bad people in every country and in every part of the world.

I want to request good natured Americans to please let me write openly on this forum about mind control. I have been
writing on this forum against mind control for many many years now. Many good American people tried to verify my claims
about involvement of jews in mind control on their own and were rightly very alarmed when they got to know the complete
truth. And bad jews (the subset of jews associated with mind control of innocent people under command of this jewish
billionaire) know that there is enough awareness in American society about their crimes. And this deters them from
openly starting mind control of many intelligent young people who were otherwise likely potential victims of their mind
control activity. I really believe that possibly thousands of people have been spared from mind control in past few
years because bad jews and American defense have become far more aware that some good people are really keeping an eye
on their activity despite that it is difficult to do anything against jews (however bad)  when every other US politician
is dying to meet Netanyahu.

So please let me expose these scumbags (bad jews only) and as I expose their crimes and their exceptional cruelty, many
of these bad actors actors have to pretend to be good and really have to decrease their mind control activity which
spares the life of hundreds if not  thousands of innocent and intelligent people (majority of who are Americans) who
would have been made target of mind control otherwise.

Mind control guy was telling me that American defense wanted to machinate to increase her reach in India by installing
mind control infrastructure on major indian roads and cities. And Indian puppets were moved to convince the Indian
authorities that only evil people would be controlled and relationship with America would dramatically improve after
allowing mind control. However due to my writing on this forum, a lot of indians got to know the true nature of mind
control and decided to not allow any large scale installation of mind control infrastructure in India. So I am extremely
happy to know that a lot of good, innocent and intelligent Indians would be spared the fate I had to go through. Though
I am a very proud Pakistani, I consider myself a second Indian since all of this part of the subcontinent used to be
just one India.

Similarly a lot of intelligent Europeans who would have been retarded were spared since there was a greater awareness
there about true nature of mind control and reasons behind it and at many places the governments stopped cooperating
with American defense to retard their own people.

So please let me openly speak against the evil of mind control and about scumbags behind mind control. Because for most
Americans saying anything against the cruel mind control of evil jewish cohort would instantly earn them the label of
anti-semite and all the politicians lining up to meet Natanyahu would turn against them.

I again assure people that I have absolutely nothing against Jews who are unassociated with mind control and I totally
respect them and purpose of my writing is only to end cruel mind control of good, innocent and intelligent people on
hands of mean and cruel people.

---

### #2489 — Amin (Topic Author)
*October 23, 2024, 8:07 AM*

**(broken latex: Unbalanced $: 1)**

```latex
Please read posts 1893, 1894, 1895 and 1896 together to see how a prestigious bank in Pakistan stole $ 2500 from my
account on orders of CIA. When I was in London in 2010-11, Lloyds TSB also stole my thousand pounds. They go to the
limits of using banks to strip innocent people of their money and most banks silently comply.

You can see the bank statements as proof of theft by the Pakistani bank. Following four posts and download the PDF bank
statement.

https://forum.wilmott.com/viewtopic.php?t=99702&start=1890#p876174

Read here about theft by Lioyds TSB:

https://forum.wilmott.com/viewtopic.php?t=99702&start=1890#p876182

I am very sure that my speaking against corrupt banks will protect many innocent individuals in the society because in
most of the places in the world banks continue to deceive innocent people when ordered by military agencies.

We are all aware that I have made an allegation of theft on Lloyds TSB. I want Lloyds TSB to either accept
responsibility for theft and deception or sue me for maligning them openly on internet.

I am sure my writing about corrupt practices of the banks will save many innocent individuals like me because even many
prestigious banks all over the world are ready to cheat and deceive innocent citizens when asked to do so by military
agencies.
```

---

### #2490 — Amin (Topic Author)
*October 23, 2024, 5:32 PM*

I want friends to please protest to American defense that has become a puppet in the hands of rich jews. Scumbags of
American defense consider successful Muslims a stain on social fabric of United States. I am just a Muslim by birth and
do not believe in any religion and there are thousands of Muslims like me that are kept on mind control by American
defense to prevent them from being successful. And majority of such victims are  American born Muslims who are like
other natives of US even though I was admittedly a foreigner. Black sheep in American defense behind mind control are
given very prestigious jobs paying millions of dollars in Jewish companies after they retire and rich jews want to block
talented muslims from being successful in United States with an iron fist since they are afraid that if some muslims
become successful, they would start wielding some influence and start opposing American policies in Israel and they want
to nip this supposed evil in the bud. And American defense has no dearth of wannabees who desperately want to join the
ranks of so many others who have gotten extremely high paying jobs with great social status in jewish companies after
retirement from American defense. Please do not blindly believe me and find out somebody in your social circle(or well
known to somebody in your social circle) you know well and who is in mind control agency of US defense and ask them
about my allegations and your eyes would open forever about role of rich jews in United States and how they openly use
mind control on anyone they wish especially on a large number of even white Americans whose families have been living in
US for hundreds of years. If your eyes do not open forever, I am ready to take any blame you wish.

Especially very talented American people in science and technology are forced to work in Jewish owned companies due to
fear of mind control. Many such people who want to leave are coldly told by administration to leave but their mind
control is initiated by American defense on insistence of jews right after they leave the jewish company and once they
know the reason behind mind control was that they tried to leave the jewish company against the will of the company
owners. And due to large number of such precedents well known to many professionals in many jewish companies, most of
the very talented people do not dare to leave the jewish companies against the will of administration since they know
very well that they would be instantly put on mind control by American defense who dances on the tunes of rich jews
since they want extremely high paying prestigious jobs with jewish companies having great social status. Please do not
believe a single word I say blindly but try to find out the actual truth on your own from authentic sources you know
well and you will find the truth that would open your eyes forever.

Not everybody is the same, there are at the same time a large number of jews who have nothing to do with any of this and
many good jewish companies who do not follow any inhuman practice. But there is a close group of rich jews who are
actually involved in large scale mind control with American defsnse working as their proxy. Please try to know the truth
on your own.

I want to advise American defense to watch a lot of American movies and try to behave like heroes in those movies.
Instead people in American defense are short-tempered scumbags who became belligerent when anybody criticizes them.
Contrary to American and Western spirit of freedom of criticism and speech that we all cherish, these short-tempered
scumbags are unwilling to tolerate anything other than eulogies based on complete lies. Just like Henry Ford used to say
that you can buy any color of car as long as it is black, to these scumbags of American defense the freedom of speech
means that you can say anything you like as long it is a eulogy otherwise they become belligerent and start moving
thousands of people to silence someone who speaks the truth about them. Let us all of us start cursing Erdogan together
now.

---

### #2491 — Amin (Topic Author)
*October 23, 2024, 5:45 PM*

Friends, I want to describe again what happens to victims of mind control on a regular basis and how animals scumloads
of American defense insult and humiliate these victims all their life to please the rich jews.

First thing is that EM waves emitting devices and lasers are fitted all over my room and also in all other rooms of my
family home. For example when I am having a good deep sleep which is rather unusual, they would target my head with
lasers and high frequency waves and I will feel very tired when I would wake up as if I had not slept at all. Just like
neurotransmitters, when molecular weights of enzymes and hormones is known , they can be targeted with resonance of
appropriate frequency to not allow them in certain areas of the body or at least decrease their concentration in
particular areas. For example when I had a foot fracture in 2014, they never allowed it to heal properly by targeting
waves of appropriate frequencies on the fractured area. Many times when I am working in my good spirits in my room or in
garage etc, the mind control agents would point high frequency lasers towards my forehead to cause pain so that I would
not be able to concentrate on anything and get angry and start ranting and would not be able to work anymore. Sometimes,
when they are more cautious, they would simply point EM waves with appropriate resonance to cause me to sleep or become
drowsy. They change the position of a lot of devices everyday based on their anticipation of position and place where I
would next work on my research and sleep.

In our house, every bed, sofa or chair that has foam on it, causes severe itch in my back when I sit on it. I think this
is because they inject some chemical that settles in pores of the foam and then becomes volatile when EM waves of a
particular frequency are focused on it. The volatile chemical enters the body of the mind control victim through the
anus since it has "potential" to combine with some of the neurotransmitters in the body. It is extremely painful to sit
on these beds, sofas or chairs. If I have to do that, I place two or three cotton pillows on top of the foam bed, sofa
or chair and then sit on the pillows. I have a large double bed in my room but I never sleep on it and instead sleep on
a small cot (with cotton filled quilts beneath me) in my room since it is impossible to sleep on the bed. Again sleeping
on the bed causes unbearable and very large physical pain and huge itch in the anus.

It is impossible for the victim to shower everyday since the water in the washroom is charged with mind control
chemicals that make the victim feel half faint and totally energy-less. Several years ago, I discovered the water in our
kitchen did not have mind control chemicals to charge the skin and I would simply take water from the kitchen to the
wash room and take a rich sumptuous shower. Even though mind control was not very high at that time, they closed the
loophole after a few weeks.

Soaps of all large Pakistani companies have mind control chemicals in them that charge the skin and when EM waves are
focused on the face, forehead and the skin, the victims feels a completely altered consciousness and sometimes extreme
anxiety and nervousness. I have been living on Indian soaps (Did we separate from India only to fill the pockets of
corrupt scumbag generals of Pakistan army who take hundreds of millions in bribes from CIA and then heroically stab
"dhirti mata"/motherland in its back?)

The antipsychotic drugs and injections are mixed at the manufacturing source on orders of scumbags of Pakistan army and 
they have a huge deteriorating effect on the victim. They would take away all neurotransmitters from my body  they can
using mind control injections and I would not be able to have a proper conversation with anyone or do any research work
until 7-10 days after the injections. I would have muscular pains and other aches all over my body. Sometimes they take
away some special neurotransmitters from the body and the victim would feel as if he is losing all energy in the body
and the victim would have to eat something or take a drink to get better. This happens to me all the time despite my
sugar tests both fasting and random and H1BAC are perfectly good. Since food is one of the only few things that can help
you get better when the victim is under mind control drugs, my weight has increased beyond limits and I am 30 kg over
weight now.  There were small periods when I did not take antipsychotics and my weight decreased quite fast in those
periods so I expect if my antipsychotics filled with mind control drugs end, I will easily lose a lot of weight quickly.

I tried to re-start my morning walk several times last year but mind control agents tried everything in their power to
deter me by taking out my neurotransmitters and even went to the limits of Police threatening me to walk not on sidewalk
of  public service roads but in parks only (Police has no such authority but they can harass anyone). I have done a
complete post on this harassment incident somewhere else.

They can even kill the vicitm remotely when the vicitim is under mind control drugs but the scumloads of American
defense have still not done that to me.

Another very nasty thing these "proud" scumloads of American defense do is that when the vicitm goes into wash room
where his penis is exposed, they use some device that throws small amount of some chemical that settles on the tip of
the penis and then they target the victim with EM waves and it causes unbearable and excruciating pain. I am recalling a
few older posts about this. They used to do this routinely but when my research got known well, they stopped doing it.
This is from more than three or four years earlier.

This is an excerpt from post 971 written on June 01, 2019 here: [forum.wilmott.com/viewtopic.php?f=15&t=94796&start=960#p846210](https://forum.wilmott.com/forum.wilmott.com/viewtopic.php?f=15&t=94796&start=960#p846210)
> Ok, I am not complaining but I decided to write this post several days ago when I was forced on shameful and
humiliating torture three days ago. They locked directed energy on the tip of my penis and it was very painful and
unsettling for me. I urinated more than twenty times in two hours. I would feel better when I would be able to take a
very small amount of urine out of my penis each time. They had done this two times previously for several hours but I
did not write here since I thought that it was a self-humiliating exercise to tell people about my persecution like this
but when they did it last time, I decided to write about it lest it becomes a common practice and starts to happen
everyday. I would say again that many of these mind control people have absolutely no respect or regard for my or
anybody's human dignity. I want people to recall how American army soldiers were openly urinating on prisoners in
Abu-Gharib and most of the staff there knew about it but such humiliatory actions were considered perfectly normal by
most of them. It was until the tapes were run on TV and news was on air everywhere that many of them started to think
that we have made a mistake. Mind control agents are not very different and when they are angry about their failure in
controlling me, they resort to punishing me using humiliating actions like targeting directed energy on the tip of
my penis. I would like to ask Americans if such actions represent American ethics and mentality and if they do not
represent American ethics I wonder why such things do not stop even after I write here openly about them. Please own
your actions if you do not want to stop them.
>
>
> I want to ask friends that some of the mind control agents become extremely mean when they fail to control their
target victim properly and they resort to such ugly tactics. For example one of the tactic mind control agents used to
exercise was that they would make a very little injury/cut on my tongue with microwaves. It will not bleed but it would
be constantly painful all the day since tongue is extremely sensitive. This used to happen almost every two weeks or ten
days. They charged my penis this morning today, as I mentioned in post #1063 written this morning, again though it was
far less severe than what I have described in the above post but such activities continue unabated and the experience
this morning made me recall the horrible experience above. I want to request friends to force the mind control agencies
to replace the guy who controls me as he has a very mean nature which is evident from the above post.
.

https://forum.wilmott.com/viewtopic.php?p=854970

.
> I have previously told friends that, during brain control, charged ions enter the body from every opening we have into
the body. I am very sorry to write this here and want to make an apology to friends for the relatively gross nature of
this post. But I would like to tell friends that  I firmly tape my penis with a paper tape to prevent charges going
inside it. When I do not do this tape, my eyesight sharply deteriorates and I become extremely lethargic. There are such
things I never mentioned on this forum because they are too disgusting to mention but once the torture continues, I
finally decided to mention some of the things here. The way it works for the charges to go into the body, I believe,
they release a small amount of very ionizable gas in the air and charge a pathway through gaseous air with laser beams
towards the body, for example towards the mouth, nose or the anus and apply potential across it. At the same time, they
create opposite potential by ionizing the chemicals that have gone into the body with food using microwave resonance
caused by laser beams. And then chemicals mixed with ionized gas start to go inside the body from the anus etc and this
becomes a self-sustaining process as long as the potential is maintained at both ends. I have seen a lot of such
instances over past twenty years of persecution when chemicals will zap inside through the anus causing severe pain. I
believe flow of charges is really directly proportional to applied potential and pathway conductivity caused by the
ionized gas.  I keep some soft tissues in my anus as it helps. I have tried other things that could more firmly block
the anus but then mind control agents greatly increase the potential and it causes extreme pain and minor seepage like
bleeding(it might possibly be because of very high frequency microwaves). Mind control agents love such torture tricks
that prevent people from doing anything that blocks their mind control. I also tried other tricks like lubricating the
anus but they would simply and freely add mind control chemicals that would charge the body to the creams and lotions in
the supermarkets just like they drug the food on the shelves. I am sure these practices are done all over the world
since adding chemicals to creams and lotions was widely done when I was in UK for six months and even upscale chains
like body shop and others had ionizing chemicals added to their creams and lotions once mind control agents would
suspect that any such shop could fall on my way.
>
> Ok, mind control agents in Pakistan had been making anywhere between 10-40 million dollars per year depending upon how
good the year had been for mind control operations. These agents want to continue mind control one way or other. These
agents tell their like-minded hardliner right wing bosses that there are certain things I never mention in my writing of
the journal (because they are probably too disgusting to write) and these are the things mind control agents need to
apply for my mind control since people would not know about these practices when they would not be written in the
journal. A few weeks ago I mentioned briefly that they cause severe itching in my back/anus but then I never wrote about
it again even though it continued. They almost always have charges going into the body of the target from the back but
sometimes it becomes very painful. And yesterday, it was again so painful that several times I would step up from the
chair while working on my research, open my pants and rub and scratch my anus and replace the tissue that has already
been charged but they would continue to increase potential again and again and I would be repeating the whole thing
again. I also woke up several times at night due to sheer itching in my anus.
>
> I had talked about reprieve from gas in my room in the previous post but I fear that might have been because for past
three to four days before writing of that post, I did not leave the home for long and mind control agents might not have
enough opportunity to come to my home and recharge the ionizing and resonance laser beams and refill the gas because I
remained in the neighborhood very close to home and returned quickly.
>
> I want to request all good American people to force their government to stop such inhuman, cruel and  animal barbaric
practices on other humans only because some powerful people in US do not like intelligent muslims/others to excel and
use their influence to continue such animal practices that hurt the image of American people and such practices are
becoming more and more of a norm with every passing year. Sorry to say but there are good and bad people everywhere in
every country, culture and religion and US is no exception. In US where many bad people do not openly do bad things
because being cruel to other humans is really not appreciated by the American society, but when evil and cruel people
know that their cruelties would not be noticed by the general american people, they are very ready to expose their true
nature and use the methods of cruelties and persecution when they are sure these things would not be noticed by the
American people. These evil, bad and cruel but powerful people have no regard for the goodwill of American people but
just want to use their influence in US right wing to extend their personal agendas. I am very sure if all of these
things would be known to American people in their true entirety, none of these mind control persecutions would ever take
place.
.

Post 1370 on this thread.

.
> Friends, I drove from Islamabad to Kot Addu today. It took me around eight hours to reach kot Addu. Long drives are
very stimulating and I thought of several new ideas both about SDEs and stocks trading. But when I reached Kot Addu, I
had extreme uneasiness in my penis since mind control agents continued to charge my penis on the way as I had to be in
the same accurately predictable position for many hours sitting in the driving seat. After reaching home, I urinated
again and again to feel better but it did not work. I also realized that my urine was reddish as there was blood mixed
with urine as I urinated.
>
> When they force electromagnetic waves inside the penis, the body tissues inside the penis tube get damaged and blood
starts to seep through the tissues and gets mixed with urine. Forcing waves into the penis is a very important part of
mind control since it is impossible to control adrenaline and dopamine without controlling the sex organ. Adrenaline and
dopamine give us drive to concentrate and force ourselves to work hard so mind control agents really have to control
these and several other similar neurotransmitters and they have to force waves into our penis to be able to do that.
>
> I normally do not like to urinate in the wash room since when I urinate there, it is very easy for them to force high
frequency waves inside the penis and it feels like a needle is going into the penis when urine is coming out and high
frequency waves are going inside. I would rather take a mineral water bottle and urine into it in my room and drop the
urine in the wash room and wash the bottle to use again. But if I would remain in a single place in my room to urinate,
they install gadgets and urinating in my room is no different from urinating in the wash room as they can again force
waves into the penis and the target victim would have needle like feeling going into the penis so I have to continue to
change places randomly in my room to urinate.
>
> Anyway they were doing the same thing again and blood was coming out of my penis mixed with urine as I supposed the
inside of tube that carries urine out of our body was damaged due to high frequency waves. This is very serious thing so
I decided to write about it so as to deter the mind control crooks who are bringing a great name to American people by
such feats. But these hardliner conservative crooks in army will continue their ugly antics since their desire to enter
the paradise of Jewish billionaire godfather is stronger than regard for any country or any human ethics.
>
> Previously I had told friends several times (may be eight or nine times in total) that they force chemicals into my
mouth when I am sleeping. This is sheer science though I do not know underlying exact details but I know they can create
potential at a precise place for special types of ions(neurotransmitters) emitted from elsewhere with lasers and EM
waves. Well I continued to mention that they charge my mouth every night with special mind control chemicals that settle
on my tongue and inside of upper jaw and my mouth is very bitter and I have to wash it or brush inside of my mouth to
feel better. I continued to mention it again and again on this forum but they never stopped so I stopped writing about
it.
>
> I want to tell Americans that Americans are mostly not bad people at all but these hardliner conservative crooks in
army and mind control who are dying to enter the paradise of the jewish billionaire godfather are not bringing any good
name to Americans with their inhuman machinations.
>
> Another thing I have mentioned several times before is that I find likes on several linkedin posts (in my activity)
that I never liked. They know my passwords and have enough control over my computer and they repeatedly like something I
never liked (I never like anything unless I strongly feel about it which is usually relatively rare). This is something
that gets known to me since there is a log of every like in my Linkedin activity. Imagine what else they are doing from
my internet traffic that I never came to know.
Another big problem is that when I approach people all over the world for consulting projects, the scumloads of American
defense reach them as well with their infrastructure in that particular country and threaten people to not work with me
or give me any project. Depending upon the nature of person, they would tell some particular lie so that they would not
be willing to work with me at all. In past 14 years, I have only earned 3500 dollars.

I have tried to hold despite all odds and tried to do good research. If things were as good as with other people free
from mind control, I would have been able to do far better research. From my side, I am not enemies with anyone and
would like everyone to use my research and make money utilizing it.

Again the The rich anal jews including the jewish billionaire are extraordinarily pleased when they hear these torture
stories and reward the scumloads of American defense (who are ready to do any nasty, disgusting or degrading thing to
other humans to prove their allegiance to rich jews). These scumloads of American defense would do every anal and
disgusting thing to innocent and intelligent victims in order to please the rich jewish cohort who would in turn reward
them with great jobs and high social status in successful jewish companies and these scumloads of American defense have
absolutely no regard for anybody's human diginity once rich jews have beaconed them to retard someone.

I want to request good people to help me end my perpetual misery and force the bad people in American defense to end
their cruel practices.

Is United States a Jungle law? I have been telling the truth and exposing the evil people for more than ten years but
still their government and defense are even more adamant to continue my cruel and inhuman persecution.

---

### #2492 — Amin (Topic Author)
*October 23, 2024, 5:53 PM*

I want friends to please protest to American defense that has become a puppet in the hands of rich jews. Scumbags of
American defense consider successful Muslims a stain on social fabric of United States. I am just a Muslim by birth and
do not believe in any religion and there are thousands of Muslims like me that are kept on mind control by American
defense to prevent them from being successful. And majority of such victims are  American born Muslims who are like
other natives of US even though I was admittedly a foreigner. Black sheep in American defense behind mind control are
given very prestigious jobs paying millions of dollars in Jewish companies after they retire and rich jews want to block
talented muslims from being successful in United States with an iron fist since they are afraid that if some muslims
become successful, they would start wielding some influence and start opposing American policies in Israel and they want
to nip this supposed evil in the bud. And American defense has no dearth of wannabees who desperately want to join the
ranks of so many others who have gotten extremely high paying jobs with great social status in jewish companies after
retirement from American defense. Please do not blindly believe me and find out somebody in your social circle(or well
known to somebody in your social circle) you know well and who is in mind control agency of US defense and ask them
about my allegations and your eyes would open forever about role of rich jews in United States and how they openly use
mind control on anyone they wish especially on a large number of even white Americans whose families have been living in
US for hundreds of years. If your eyes do not open forever, I am ready to take any blame you wish.

Especially very talented American people in science and technology are forced to work in Jewish owned companies due to
fear of mind control. Many such people who want to leave are coldly told by administration to leave but their mind
control is initiated by American defense on insistence of jews right after they leave the jewish company and once they
know the reason behind mind control was that they tried to leave the jewish company against the will of the company
owners. And due to large number of such precedents well known to many professionals in many jewish companies, most of
the very talented people do not dare to leave the jewish companies against the will of administration since they know
very well that they would be instantly put on mind control by American defense who dances on the tunes of rich jews
since they want extremely high paying prestigious jobs with jewish companies having great social status. Please do not
believe a single word I say blindly but try to find out the actual truth on your own from authentic sources you know
well and you will find the truth that would open your eyes forever.

Not everybody is the same, there are at the same time a large number of jews who have nothing to do with any of this and
many good jewish companies who do not follow any inhuman practice. But there is a close group of rich jews who are
actually involved in large scale mind control with American defsnse working as their proxy. Please try to know the truth
on your own.

I want to advise American defense to watch a lot of American movies and try to behave like heroes in those movies.
Instead people in American defense are short-tempered scumbags who became belligerent when anybody criticizes them.
Contrary to American and Western spirit of freedom of criticism and speech that we all cherish, these short-tempered
scumbags are unwilling to tolerate anything other than eulogies based on complete lies. Just like Henry Ford used to say
that you can buy any color of car as long as it is black, to these scumbags of American defense the freedom of speech
means that you can say anything you like as long it is a eulogy otherwise they become belligerent and start moving
thousands of people to silence someone who speaks the truth about them. Let us all of us start cursing Erdogan together
now.

---

### #2493 — Amin (Topic Author)
*October 23, 2024, 5:57 PM*

I am a great admirer of Einstein. He was not only one of the greatest scientists of all times, he was also a great human
being well ahead of his time especially when it came to women's rights and human rights and many other such things that
became acceptable to more people in the advanced societies only decades later.

Here is his letter to Marie curie where he repeatedly use the word reptile for people very wrongly criticizing Marie
Curie.

Highly esteemed Mrs. Curie,

Do not laugh at me for writing you without having anything sensible to say. But I am so enraged by the base manner in
which the public is presently daring to concern itself with you that I absolutely must give vent to this feeling.
However, I am convinced that you consistently despise this rabble, whether it obsequiously lavishes respect on you or
whether it attempts to satiate its lust for sensationalism! I am impelled to tell you how much I have come to admire
your intellect, your drive, and your honesty, and that I consider myself lucky to have made your personal acquaintance
in Brussels. Anyone who does not number among these reptiles is certainly happy, now as before, that we have such
personages among us as you, and Langevin too, real people with whom one feels privileged to be in contact. If the rabble
continues to occupy itself with you, then simply don’t read that hogwash, but rather leave it to the reptile for whom it
has been fabricated.

With most amicable regards to you, Langevin, and Perrin, yours very truly,

A. Einstein

P.S. I have determined the statistical law of motion of the diatomic molecule in Planck’s radiation field by means of a
comical witticism, naturally under the constraint that the structure’s motion follows the laws of standard mechanics. My
hope that this law is valid in reality is very small, though.

I would like to follow the tradition of Einstein in anyway I can in. It's just that he uses the word "reptile" for bad
people while I like to use the word "scumbag" for evil people.

---

### #2494 — Amin (Topic Author)
*October 23, 2024, 8:52 PM*

I want to request Pakistanis abroad and at home to please let some Pakistani investigative reporters and other
journalists know about my thread on Wilmott. Please also inform dawn, Jang, business recorder, tribune, ARY news and all
other Pakistani newspapers so that they could come to know how our army systematically fails Pakistani talent in return
from bribes from CIA and American Army. This is how crooks in our army buy islands in New Zealand and properties in
Belgium. There are more than 500 very talented Pakistanis who are kept constantly on mind control by our army. They have
continued to do this over past twenty years since Pervaiz Musharraf came to power. If bastards in our army had not
retarded intelligent Pakistanis, there would be many very successful international enterprises coming from our country
and we would still be at Par with India and Bangladesh in per capita income who were much behind in per capita income 25
years ago and today are much ahead of us. This is since our army continues to darken the future of our nation in return
for hundreds of billions of rupee generals are given by CIA. This is probably one of the most successful operations by
CIA to silently fail an entire nation.

I want to request Pakistanis abroad and at home to please tell brave journalists and others like Hamid Mir, Aitezaz
Ahsan, Latif Khosa, factfocus people, and other prominent people in political parties and government that readers of my
blog can think about my thread. Every chief of our army lives abroad after retirement. But we want to live in our
country forever and build our "dhirti Maan" as famously quoted by Latif Khosa.

I want to say again that if I have survived to say this today, it is only due to help and support from good American
people.  Most of the good American people  have a lot of humanity for us and they always want our poor nations to
progress. Good people in United States supported me when nobody in my own country was ready to support me. American
people are not a bad people at all and they do not support any mind control in our nations or their own nation.

However large armies in most countries are composed of corrupt crooks only. China, America, Pakistan, Russia. All these
countries have large corrupt armies. American army for example plays in hands of rich Jews among other forms of rampant
corruption. So please be careful to not generalize my posts about corrupt American army and defense to good American
people.

---

### #2495 — Amin (Topic Author)
*October 24, 2024, 4:35 AM*

This is also a relevant post I copied from past.  https://forum.wilmott.com/viewtopic.php?t=99702&start=1965#p876890

Many friends who are used to formal language all the time might be disturbed by my use of slang expletives for bad
people but after reading Einstein's letter to Marie Curie, I consider myself perfectly validated to use the word of scum
for American army and for bad jews who have no ethics and are ready to fall to every low level of humanity for some
material gain or due to their hatred, venom, poison or malice as in case of bad jews.

Even though American society keeps jews in very high regard, they are not gold-plated. Just like any other people or
race, some of them are extremely good human beings, some of them are extremely evil and some of them simply do not care.
They tend to be more intelligent and when this intelligence shows itself in the form of Einstein we see one of the
greatest human beings ever born but when this intelligence turns evil and machinatory we have exactly opposite form of
humanity like evil jewish billionaire godfather/goldfather and his rich jewish cohort who has taken complete control of
American army to advance their nefarious designs and have retarded thousands of innocent and intelligent people they did
not like. So respect has to be shown in abundance to good people but very carefully to evil people. When great respect
is shown to evil people, they become even more emboldened to advance their agendas based on hatred, venom,  poison and
malice.

When I was undergraduate I had transferred to US after two years and in my last year I lost all interest in engineering
and my GPA composed of only two years was very bad so I had to go to a not so good school for masters in Economics. But
I had decided to work very hard and I was confident that with my hard work I will succeed again. But some third class
malicious jews at the university got slighted by my talent for mathematics. These evil jews were very aware of mind
control even in 1997 and jewish billionaire had already great influence in US army at that time. I was just like a boy
working hard to find my future that all of a sudden, from nowhere, the stone of mind control fell on my head. When mind
control agencies told malicious jews that I had several special neurotransmitters, the malicious jews were completely
resolved to force mind control on me at all cost. US Defence was already a puppet in hands of evil jewish billionaire
and when mind control guys knew that billionaire was taking special interest in my mind control, they were extremely
enthusiastic to please him and do all sort of efforts to retard me.

I want to tell friends that American army, due to pressure from evil jewish billionaire, had appointed one or two jews
from academia from my graduate university who were enthusiastic about retarding me and they are the ones who take key
decisions about what to do with me. They continue to think in my brain for several hours every day and completely remain
in touch with all progress in mind control on a daily basis. All cruelties and torture that was unleashed on me was in
their complete knowledge and was authorized by them on suggestions of mind control agents.

Over past thirty years, lot of bad jews have developed a network in academia(with absolute apology to all the great
jewish people in academia) and when a victim has to be retarded most of the jews in the network start orchestrating
totally complete lies about the victim so that good people think that retarding the victim is indeed is a very good
thing.

Several other smart people are paid by American army to keep thinking in my brain and they remain oriented with what I
am doing. For example, if there is something silly in my work, these people who are keeping track of my programs already
inform the jewish network and this jewish network starts spreading fun about my work several days in advance. As my
research progresses and my programs are updated, several people have access to my programs and its logic several days in
advance before I post them in public.

And I want to tell people that this network of evil jews has greatly perfected itself over past thirty years and not
only muslims are retarded, everyone they do not like including europeans, blacks and a large number of white talented
Americans are retarded at whim by this network of emboldened evil jews.

I want to request all good people in American society and in european countries to end and thwart this gang of evil jews
who are bent on retarding intelligent people of every nation and creed they do not like.

I am sure that intolerant and arrogant scum of American army will again resort to torture and violence and start
focusing their lasers on my temple, eyes, teeth and ears.

---

### #2496 — Amin (Topic Author)
*October 24, 2024, 5:14 AM*

Friends very sorry for so many off-topic posts. This is the last post on the persecution topic for now. I will be
getting an antipsychotic injection in a few hours now. And I will try to avoid this topic unless there is some other
development in my persecution or some threat by army etc. I will go back to technical work and try to post new things
about my research but I may not be able to do good work for next 10-15 days due to effect of injection.

I am copying this last post (for now) from the past. I will try my best to revert to my research work now and post about
it.

The following post is composed of my own genuine thoughts why Jews were wronged so many times throughout history.

https://forum.wilmott.com/viewtopic.php?t=99702&start=2145#p879442

Friends, I am very sorry to have come to this point to be forced to write this post.

Please read what I have been trying to say since so many years. https://forum.wilmott.com/viewtopic.php?f=15&t=101453

People know that despite my brutal, cruel and sadistic persecution on hands of rich American jews that has now lasted
for 25 years, I always tried to mention very carefully that all jews are not bad people and a large number of them are
very good human beings.

And in order to avoid offending the jews who are good human beings, many times in the past, I had been very careful to
not say my mind about bad and evil jews in United States. Now there is this evil jewish billionaire who is
Godfather/Goldfather of mind control, who is an exact example of what happens when scum makes big money by chance.
Shit-piece thinks of himself as a God and decides the destiny of thousands of innocent but intelligent people by asking
American defense to retard these innocent and intelligent people(on recommendation of many evil jews). And when people
complain about crimes of these evil jews, a large cohort of jewish cronies responds by calling the victims of jewsih
trickery and machinations as anti-semite.  These evil jewish scumbags are so offensive human creatures that they would
happily, boldly and habitually tarnish the most sacred memory of innocent holocaust victims for their nefarious designs
to retard and persecute intelligent people who are declared anti-semite only because they try to expose the truth about
evil jewish cohort's attempts to retard them. Several times in the past when I tried to tell people that some evil jews
were behind my persecution and told the torture stories, I was right away told that I was an anti-semite who was trying
to tarnish the reputation of jews.

Again with a great due to apology to good jewish human beings, I want to tell people that due to my experiences of
cruelty, torture and persecution on insinuation of evil jews, I have come to realize that throughout history there were
always some jewish scumbags who had absolutely no humanity for non-jewish people and these evil jewish people always
machinated to hurt other people and in the meantime brought bad name to even those jews who were good human beings.
Forgive me but world follows laws of physics. I may be politically very incorrect but everything in this world follows a
cause and effect. No good human being wants to wrong even a stray dog in their right mind then why were jews persecuted
throughout history. I am of the opinion that there were always a group of evil jews who had no humanity for non-jews and
they continued to cruelly machinate against non-jews and when their machinations became common knowledge in the
respective societies, people hated even a large number of good jewish humans due to crimes of bad jews in the society
and there was always a backlash that was against all the jews irrespective.

99.9% of jews burnt in gas chambers were totally innocent and good haumn beings and were wondering rightfully why would
they ever be wronged or killed by anyone in their right mind even right before their execution but the evil and
machinatory ones had who brought this day on them had already left for other countries of Europe or America with all
their wealth.

I am no expert at history of jews but recently Ukraine's war brought its history to limelight and I was reading that
there was a period in Ukrainian history when Polish entrusted jews to rule and collect revenue from Ukrainian public.
Jews were extremely cruel in collecting the revenue and were very offensive to local population. This jewish control
continued for forty or so years and polish were ousted by some other power and jewish control ended the same time. And
then local population who had borne their cruelties and torture for so many decades, killed them en masse at many places
in Ukraine since they had extreme anger against them.

Again World follows laws of Physics. If Jews were so good to others, why everyone wanted to wrong them. Human beings
everywhere have enough empathy to not wrong anyone if they do not have any grudges and grievances against them.

Again my thesis is that even though a large number of jews everywhere were good nice folks, there was always a group of
cruel and inhuman jews who had no sympathies for non-jews and this evil group of jews always machinated to wrong other
people and due to machinations of this evil group of jews, ordinary folks in the respective societies harbored
grievances against jews in general (which was a very wrong thing) and persecuted them whenever they had a chance. Since
world always follows cause and effect, I am not going to believe that ordinary folks in every society hated them for no
reason and just persecuted them for the fun of it.

Please cherish the memory of sacred souls who were killed in holocuast but stop giving this anti-semite shit to people
when you are the one who is showing cruelty to nice, good and intelligent human beings as is habitually done by a lot of
evil jews these days.

I want to request all jews and non-jews that this group of evil jews again has started to machinate boldly in United
States and it would be good for both Jews and non-jews to thwart this group of evil jews before this is too late.

I want to request(and suggest to good jews as a friend) to disavow any relationship with jewish scumbag billionaire and
his rich jewish cohort who are involved with mind control of innocent and intelligent people of so many nations for
their nefarious designs.

---

### #2497 — Amin (Topic Author)
*October 24, 2024, 9:56 AM*

Friends, very sorry for distraction of past few days. I was trying to concentrate on my research only but mind control
agents continued to increase constant use of gases everyday making it very difficult for me to work. For many days, I
continued to ask mind control agents very amicably to end the gases but they continued to increase the gas and lasers
everyday. And when it became virtually impossible to continue working, I decided to approach the audience of my thread
for help and shared all my thoughts very candidly. Otherwise, I had been earlier trying to avoid the topic of my
persecution as much as I could.

I also want to explain very clearly that I have been very severely criticizing bad jews and American defense but this is
limited to criticism in writing only. I do not want anyone including myself to take the law in our own hands. We have to
respect the human dignity of every jew and every human being including those involved in bad practices so even though I
openly talk about bad people, it is not an invitation to anyone to take the law in their hands or hurt any any human
being. I will continue to fight for my cause of ending mind control of innocent and intelligent people but I want people
to completely respect all good jews and good people in American army and make a political struggle for the law or
government actions to take their course against corrupt and evil people. I absolutely do not suggest any violence or
anybody taking law in their hands.

Ok coming back to my research, there are a few ideas I want to share with friends. I will be trying these ideas in next
few day but here are my thoughts about them now.

First idea is that we could partition Legendre regression of SDE(or other relevant set of variables) on parameters in
several disjoint cases/groups. We know that coefficient of first hermite polynomial is the most important for most of
the densities. Our algorithm for Legendre regression has very good R-squared but we want more excellent results so
density is extremely closely captured by coefficients found from Legendre regression. We want extreme precision for
that. So one way to do that would be to partition the regressions into several disjoint parts with first partition for
example covering$ch_1$ between 1 and .9, second partition covering$ch_1$ between .9 and .8 and third partition covering
$ch_1$ between .8 and .7 and so on. We can increase or decrease the size of these partitions as appropriately required
for accuracy in particular data.

So we do our first Legendre regression on complete data and find all the density coefficients particularly$ch_1$ . These
values of coefficients would be good but possibly suboptimal but it would certainly be good enough to tell us in which
partition$ch_1$ belongs. And once we know about the partition in which$ch_1$ belongs, we could do a second more precise
regression that uses Legendre coefficients from regression on$ch_1$ in the particular range/partition.

So in order to do this, we would have to train Legendre coefficients from a universal regression on data and several
other regressions to train Legendre coefficients which are done on data with$ch_1$ within each partition range. I hope
that these partitioned regressions on more homogeneous coefficients data would be more accurate than a single Legendre
regression on all the universal data.

Please note that coefficient values particularly$ch_1$ are input to Legendre Polynomial regression and it is very easy
to partition the data based on this coefficient however input parameters for each partition would not be directly
uniform and would have to be explained by Legendre polynomials. This would not be a problem in the Legendre regression
that calculates coefficients but Legendre polynomial series would have to be inverted for each parameter to find the
appropriate value of uniform when using pre-calculated Legendre coefficients to determine the resulting coefficients of
hermite series when using the algorithm in real time.

I also have some other ideas for example I want to check if regressing squared coefficients${ch_n}^2$ is more precise
than doing regressions on$ch_n$ .

I have some other ideas but they are more hazy and I could share if I have some better grasp of them.

Another thing, I have not shared my old work but I calculated the approximate variance of mean reversion SDEs by taking
the value of${X_t}^{(2\,\gamma)}$ in the variance formula without including quadratic variations and my R-squared for
square root of variance increased from .993 to .9994 and there was quite extreme accuracy in the resulting densities. I
still had not included products of above approximate variance with other parameters in Legendre regression and they
would possibly improve results further.

---

### #2498 — Amin (Topic Author)
*October 25, 2024, 4:47 PM*

Friends, I went ahead and randomized all five parameters of the mean reverting SDE other than time ( in my previous
programs I was only randomizing over four parameters.). And I get very good results. As I had explained earlier that we
had eight Hermite series coefficients and one square root of variance of the SDE that we were regressing using Legendre
polynomials. In this new experiment, volatility coefficient in SDE ranges as a uniform between .1 to 1.0 . Now the
R-squared for eight hermite series coefficients and square-root of variance as predicted by Legendre regression are
given below.

ans =

   0.999648866034595

ans =

   0.999414308424256

ans =

   0.999775699835112

ans =

   0.997726209621918

ans =

   0.983446197632861

ans =

   0.911201304326231

ans =

   0.943286335280147

ans =

   0.986096282294502

ans =

   0.999330442668697

When I looked at densities of SDEs, the fit to true densities was very good but still one in fifteen densities was more
off than I would consider good for finance purposes where we need precise densities. I still think there is still some
randomness in SDE density coefficients input to the training algorithm since high limit of the volatility coefficients
has increased to one while in previous experiments it was fixed at .55. So I want to re-simulate the monte carlo data
with slight more care and I expect that results would be very good to finance level precision after that.

Another thing I want to mention is that current research effort is only to demonstrate viability of Math AI method based
on orthogonal polynomials. I just tried to solve for densities in a very generic way and I am sure friends (and possibly
myself) who are more interested in SDEs would continue to do research for parsimonious math based regressors from SDE
literature  and use them in Legendre regressions for very optimal results.

I will be posting my matlab program in a day or two since I want to spend a bit of more time to improve monte carlo
simulation close to zero further as in new program volatility coefficient is random and can be very high as the upper
limit of$\sigma$ in my program is one.

---

### #2499 — Amin (Topic Author)
*October 26, 2024, 11:57 PM*

Friends, I will be posting my SDE programs tomorrow(Sunday). I have come up with an approximate formula for variance of
mean reverting SDEs for arbitrary value of volatility exponent gamma. And this improved formula further improves the
R-squared.

I have two matlab programs. One in which I use generic parameters of the SDE in Legendre regression and a second program
that uses the terms in 2nd order expansion of the SDE and are used for Legendre regression.

It's a bit late and I am going to sleep but will post the programs in the Sunday evening.

---

### #2500 — Amin (Topic Author)
*October 27, 2024, 1:12 PM*

Friends, I am writing this post to protest the antics and bad treatment of mind control agencies. They are not allowing
me to have a sound sleep by targeting my head with EM waves. I slept at 5:00 am this morning and woke up at noon. But
they did not let me have a good and fulfilling sleep and I felt very tired and had to sleep again. I woke up right now
after three hours of sleep and I feel worse now than before when I slept. I feel thoroughly exhausted and unable to do
anything.

Despite what people might think, I have a very sound sleep (when unperturbed by EM waves) and many times I resort to
sleeping to feel better when my condition is bad.

It seems that there is some sympathy for me  by some good Americans to try to end my suffering and mind control agents
and their backers are very worried that I might become free and they want to stop me from anything that helps me. For
weeks, mind control agent has been telling (obviously lying) me that they would end my persecution if I stopped posting
my research on Wilmott.

And even though gases have decreased remarkably, they still use the same extremely bad gases from time to time however
the incidences of use of gas have decreased quite a bit compared to before.

But what is truly worrying that they are not allowing me to sleep well and I am really feeling extremely bad at the
moment and totally unable to work.

I wanted to clean up my programs before posting it but I do not know if that could be possible even though I want to
try.

---

[← Previous](page_049.md) | [Index](index.md) | [Next →](page_051.md)
