# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 39 of 59** — Posts #1901–#1950

[← Previous](page_038.md) | [Index](index.md) | [Next →](page_040.md)

---

### #1901 — Amin (Topic Author)
*July 27, 2023, 5:23 AM*

>
> Friends, as I mentioned yesterday, I have worked on an older program to calculate the Z-series from data and improved
it. It is based on regression and equi-probable normal values. I had written a relatively informal program like this
earlier but I improved the older program and expanded central moments about mean using regression. Mean is always known
with precision but median(as earlier program was based on expansion around median) is not known always known with
certainty in a distributional sense. I tried to use the program on monte carlo SDE data and the program works reasonably
well but still eighth moment is a bit off. I would try to post this program later today.
>
>
>
> I have been able to think of a better program and want to share its details with the friends. Suppose we are given
eight moments and we want to find a Z-series representing it. We could find eight discrete representative points so that
eight moments are matched. We could write eight equations for eight raw moments with eight discrete points/variables and
solve these eight non-linear equations. Please note that these are eight equations and eight unknown variables.
>
> We would have to solve these equations with multidimensional newton method. We have to explore the feasibility of the
method if Newton method behaves well or we could find starting seeds that help Newton convergence or any other
possibilities that could help us easily solve for eight non-linear equations. So at the moment I want to explore the
possible feasibility  and possible ease of the method.
>
>
>
> A representative equation for nth moment would be
>
>
>
>
${x_1}^n \, + \,{x_2}^n \, + \,{x_3}^n \, + \,{x_4}^n \, + \,{x_5}^n \, + \,{x_6}^n \, + \,{x_7}^n \, + \,{x_8}^n \, = \, \mu_n $
>
>
>
> If eight moment equations could easily be solved for eight discrete points, we know that these points would be on an
equi-probable grid by default as opposed to haphazard data that comes out of simulations and observations of stochastic
processes and where we have to do a regression with equi-probble grid since data itself is not on equi-probable grid.
Again since the eight discrete representative points when found would be on an equi-probable grid, we could assign each
of them an appropriate value of underlying Z directly by CDF matching.
>
>
>
> Once we have found eight discrete representative points and their associated Z-values, we could do an eighth order
Lagrange interpolation to find eight derivatives around mean(we could use mean instead of median and it would also work
well as I have already done it in some cases and found it to work well) which can then be converted to coefficients of
Z-series that has the same moments as the input moments.
>
>
>
> Only question is trying to see and explore the possibility if the algorithm proves more feasible as compared to the
other method.
>
.

.

Friends, I had coded multidimensional Newton method for this two days ago but Newton does not converge from arbitrary
seed. Some intelligent seed has to be analytically found that is inside catchment of Newton method.

This was the same problem with other method to find Z-series from moments that now mostly works but over the months I
had tried again and again to improve the seed. Only when I got intuitive understanding of some features of the problem
that I was able to find a good working seed analytically.

However I am trying to think of some idea to find an analytic seed to problem and hope that I would be able to get it to
work in next few days.

I want to tell friends who follow my thread for mathematics that I am perfectly committed to my research. Some ups and
downs and some other unrelated activity due to my persecution and mind control will continue but the real purpose of the
thread is to continue with mathematical research and I am totally committed to the main core theme. An ideal world would
be where everyone spent their time in some constructive activity and did not have to waste their energies in totally
unproductive conflicts.

---

### #1902 — Amin (Topic Author)
*July 27, 2023, 1:56 PM*

Friends, I continued to work today after a gap of two days. I noticed that there is probably no solution of eight
non-linear moment equations with eight discrete points. when I optimized a  problem, I noticed that six points converged
to zero (which was mean) with zero variance and only two outer points solved for the larger moment equations and still
resulting variance was ten times the input variance. So I found that there was no way to find a general solution of
eight moment equations with eight discrete points.

However, I was able to use the iterative optimization ideas to make them work on finding coefficients of Z-series so
that moments are matched. This was iterative optimization and took a long time so cannot be used for problems where
Z-series have to be fitted in real time. However on all of the problems I considered, it continued to converge with
increasing iterations. It took more than fifteen minutes on my slow 2013 computer but I think (though I might be wrong)
that it will universally converge for the problems when moments are given so that a well-defined Z-series solution
exists. It can be used for a large number of difficult problems when times is not greatest concern and would get a
solution very well within the catchment of Newton method. It can also be used to find general seed for various types of
problems that can then be used with Newton method to converge.

I am sure this optimization technique can be perfectly used for all different polynomials like Legendre and many other
orthogonal polynomials to their respective polynomials series that we were trying to fit earlier.

I think only secret sauce that I used was that I took a discrete step size for each coefficient inversely proportional
to its effect on variance. So that discrete perturbation of various Z-series coefficients at any time in optimization
had a roughly equal effect on variance. My lesson from the exercise was that when we are discretely perturbing various
different parameters to optimize a problem, the relative size of small perturbations in various parameters should be so
that they have a roughly equal effect (of the same order) on the objective function. I think many difficult problems
could become easier with this trick.

I am going to go out now for several hours on my motorcycle. But I will try to post the new optimization program later
tonight after some possible improvements. If I do not post it tonight, I will post it by tomorrow at the latest.

---

### #1903 — Amin (Topic Author)
*July 28, 2023, 12:27 AM*

Friends, I continued to work on the new matlab program. I made some more modifications to earlier algorithm. But I found
that important thing in iterative optimization is proper choice of relative size of perturbations of coefficients of
Z-series. I want to play with the program further and will post it during the evening today (in 12-18 hours).

---

### #1904 — Amin (Topic Author)
*July 28, 2023, 9:24 AM*

I am still playing with efforts to improve iterative optimization part of the Z-series Calibration to Moments program. I
continue to see that relative size of perturbations have a great effect on the performance of the program. Therefore I
went a step further and calculated sensitivity of improvement in objective function to iterative step change for each of
the coefficients. I want to study this further to dynamically adjust the relative step size during optimization. Earlier
I had decreased or increased step sizes in a static ratio (between different parameters/coefficients) fixed at the start
of the program. This static step size ratio greatly affects the quality of program. But with this static ratio, in some
cases optimization almost stalls and there are only miniscule improvement in objective function with each iteration and
I realized the reason that some appropriate step size(with larger sensitivity) had to be increased out of the static
ratio while other step sizes had to be kept smaller. And therefore I realized that I needed a dynamic ratio that can be
adjusted during the running of the program. But to properly study this and add this capability requires some time so I
would not be able to post my program for another day or two until I properly complete it.

---

### #1905 — Amin (Topic Author)
*July 28, 2023, 2:03 PM*

Friends, I am quickly posting a preliminary version of the program that finds coefficients of Z-series by iterative
optimization so that moments of Z-series variable match the input raw moments. I want to do a lot more improvement in
the program and improve the algorithm it but I am posting an interim version. Again this is just preliminary and I will
post a new version with major improvements in a few days.

.

.

```
function [] = CalculateZSeriesFromMomentsAgainNew(rMu)
%The above function takes an array of first eight raw moments as input.
%And returns Z-series Coeffs upto 7th power of Z as
%Y=c0+c(1)*Z+c(2)*Z^2+c(3)*Z^3+c(4)*Z^4+c(5)*Z^5+c(6)*Z^6+c(7)*Z^7

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%Input raw moments specified below

rMu(1)=0.000012499863483*10^5;
rMu(2)=0.000021197093700*10^5;
rMu(3)=0.000050274347857*10^5;
rMu(4)=0.000171368317209*10^5;
rMu(5)=0.000856094970826*10^5;
rMu(6)=0.006320436615909*10^5;
rMu(7)=0.068698344472325*10^5;
rMu(8)=1.084082326087001*10^5;

% mu=1;
% sigma0=.8;
% for nn=1:8
% rMu(nn)=exp(nn*mu+.5*nn^2*sigma0^2);
% end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
SeriesOrder=7;    %Z-series till 7th power. hardcoded here cannot chagne.
mOrder=8;         %Number of raw moments in calibration. hardcoded here cannot chagne.
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

%
%
% iter=1;           %Number of iterations in the calibration.
%                   %Please experiment and play around.
% bGuess(2:7)=0;    %We have assigned initial values of coefficients
% bGuess(1)=1;      %other than c(1) to zero. We are starting with no prior information.
% [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNew(sMu,bGuess,iter);
% bGuess(1:7)=c(1:7);
% iter=10;
% [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNewModified(sMu,bGuess,iter);
%
% c0
% c
%
% %str=input("Look at pre-smoothing Guess result")
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

c0=0;
c(1)=1;
c(2:7)=0;

Iterations=25000;
[c,ObjFunc] = OptimizeMomentsByIterationZseries04(sMu,c0,c,SeriesOrder,NMoments,Iterations);
c0=-(c(2)+3*c(4)+15*c(6));
ObjFunc
c

[FittedStandardizedMoments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments)

%Please Uncomment this if you want to see a comparison of input moments and
%fitted moments
sMu
FittedStandardizedMoments
str=input('Look at comparison of fitted moments with input moments');

%%%%%%%%%%%%%%%

c0=c0*sqrt(cMu(2)); %convert from standardized to central moments
c=c*sqrt(cMu(2));   %convert from standardized to central moments

c0=c0+Mu1;          %convert from central to raw moments by adding mean.

[FittedRawMoments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

FittedRawMoments
rMu
end
```

.

.

.

```
function [c,ObjFunc] = OptimizeMomentsByIterationZseries04(sMu,c0,c,SeriesOrder,NMoments,Iterations)

% Index(1)=4;
% Index(2)=5;
% Index(3)=3;
% Index(4)=6;
% Index(5)=2;
% Index(6)=7;
% Index(7)=1;
% Index(8)=8;

for nn=1:SeriesOrder
    DeltaX(nn)=.00125/(factorial(nn)).^(.75);
    %DeltaX(nn)=.00125/(factorial(nn)).^(.35);%uncomment for lognormal
end

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

%ObjFuncBest= CalculateMomentsDiscreteXnObjFunction(Ms,Xn,X0,NPoints,NMoments);
[ObjFuncBest] =CalculateMomentsMatchObjFunction0A(Moments,NMoments,sMu);
cBest=c;
c0Best=c0;
ContImproveFlag=0;
ImproveFlag(1:SeriesOrder)=0;
DeltaObj(1:SeriesOrder)=0;
DeltaObjPrev(1:SeriesOrder)=0;
ObjSensitivity(1:SeriesOrder)=0;
ImproveFlag0=0;
ImproveCount=0;
for mm=1:Iterations
    ImproveFlag0Prev=ImproveFlag0;
    ImproveFlag(1:SeriesOrder)=0;
    for nn=2:SeriesOrder
        DeltaObjPrev(nn)=DeltaObj(nn);
        ObjSensitivityPrev(nn)=ObjSensitivity(nn);
        cin=c;
        cin(nn)=cin(nn)+DeltaX(nn);
        c0in=-(cin(2)+3*cin(4)+15*cin(6));

        [SecondMoment]=CalculateSecondMomentC7(c0in,cin);
        cin=cin/sqrt(SecondMoment);
        c0in=c0in/sqrt(SecondMoment);
        [Moments] = CalculateMomentsOfZSeries(c0in,cin,SeriesOrder,NMoments);
        [ObjFunc] =CalculateMomentsMatchObjFunction0A(Moments,NMoments,sMu);

        %[ObjFunc] = CalculateMomentsDiscreteXnObjFunction(Ms,Xin,X0,NPoints,NMoments);
        if(ObjFunc0)
            %AvgSensitivity=AvgSensitivity+abs(DeltaStep(nn)).*abs(ObjSensitivity(nn));
            AvgSensitivity=AvgSensitivity+abs(ObjSensitivity(nn))/SeriesOrder;
            %SumDeltaStep=SumDeltaStep+abs(DeltaStep(nn));
        end

        if(ImproveFlag(nn)==1)
            ImproveFlag0=1;
        end
    end

    %if(mm>20000)
    %    ObjSensitivity
    %    AvgSensitivity
    %    DeltaX
   %     mm
   %     str=input("Look at numbers")
    %end

    AvgSensitivity=AvgSensitivity/SumDeltaStep;

    %if(ImproveCount==4)
    if(AvgSensitivity>0)
       for nn=2:SeriesOrder
          %DeltaX(nn)=DeltaX(nn)*(1+sqrt(abs(ObjSensitivity(nn))/AvgSensitivity));
          if(abs(ObjSensitivity(nn))>AvgSensitivity)
             DeltaX(nn)=DeltaX(nn)*1.005;
          end
          if(abs(ObjSensitivity(nn))abs(ObjSensitivityPrev(nn)))
          %    DeltaX(nn)=DeltaX(nn)/1.05;
          %end
          if(abs(DeltaObj(nn))abs(DeltaObjPrev(nn)))
              DeltaX(nn)=DeltaX(nn)*1.00005;
          end
       end
       %DeltaX(7)=DeltaX(7)*1.01;
    end
    %end

    if((ImproveFlag0)&&(ImproveFlag0Prev))
        ImproveCount=ImproveCount+1;
    else
        ImproveCount=0;
    end

    if(ImproveCount>=4)
        ImproveCount=0;
        DeltaX=DeltaX*1.15;
    end

    if(ImproveFlag0==0)
        DeltaX=DeltaX*.85;
    end
end
c=cBest;
end
```

.

.

.

```
function [ObjNew] =CalculateMomentsMatchObjFunction0A(Moments,NMoments,sMu)
%[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

 if(NMoments==8)
    %
ObjNew=((sMu(1)-Moments(1))).^2+factorial(8).*((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))).^2+factorial(6)*((sMu(4)-Moments(4))/sMu(4)).^2+
...
    % ((sMu(5)-Moments(5))).^2+factorial(4)*((sMu(6)-Moments(6))/sMu(6)).^2+((sMu(7)-Moments(7))).^2+ ...
    % factorial(2)*((sMu(8)-Moments(8))/sMu(8)).^2;

 
ObjNew=factorial(8).*((sMu(2)-Moments(2))).^2+factorial(8).^2.*((sMu(3)-Moments(3))).^2+factorial(8).^2*((sMu(4)-Moments(4))).^2+
...
   
 factorial(6).^2.*((sMu(5)-Moments(5))).^2+factorial(6).^2*((sMu(6)-Moments(6))).^2+factorial(4).^2.*((sMu(7)-Moments(7))).^2+
...
     ((sMu(8)-Moments(8))).^2;

%ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2;

%ObjNew=((sMu(1)-Moments(1))/sMu(1)).^2*0+factorial(8).*((sMu(2)-Moments(2))/sMu(2)).^2;%+0*((sMu(3)-Moments(3))).^2+factorial(6)*((sMu(4)-Moments(4))/sMu(4)).^2;%+
...
%    ((sMu(5)-Moments(5))).^2+factorial(4)*((sMu(6)-Moments(6))/sMu(6)).^2+((sMu(7)-Moments(7))).^2+ ...
%    factorial(2)*((sMu(8)-Moments(8))/sMu(8)).^2;

%
%if((sMu(3)<.00001) || (sMu(5)<.00001) || (sMu(7)<.00001))  %If Odd standardized input Moments are zero
  %   ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))).^2+((sMu(4)-Moments(4))/sMu(4)).^2+ ...
  %  ((sMu(5)-Moments(5))).^2+((sMu(6)-Moments(6))/sMu(6)).^2+((sMu(7)-Moments(7))).^2+ ...
  %  ((sMu(8)-Moments(8))/sMu(8)).^2;
%   
ObjNew=20*((sMu(1)-Moments(1))/sMu(1)).^2+10000*((sMu(2)-Moments(2))/sMu(2)).^2+100*((sMu(3)-Moments(3))).^2+200*((sMu(4)-Moments(4))/sMu(4)).^2+
...
%    ((sMu(5)-Moments(5))).^2+20*((sMu(6)-Moments(6))/sMu(6)).^2+((sMu(7)-Moments(7))).^2+ ...
%    ((sMu(8)-Moments(8))/sMu(8)).^2;
%else
%   
ObjNew=((sMu(1)-Moments(1))/sMu(1)).^2+((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))/sMu(3)).^2+((sMu(4)-Moments(4))/sMu(4)).^2+
...
%    ((sMu(5)-Moments(5))/sMu(5)).^2+((sMu(6)-Moments(6))/sMu(6)).^2+((sMu(7)-Moments(7))/sMu(7)).^2+ ...
%    ((sMu(8)-Moments(8))/sMu(8)).^2;
%end
end

if(NMoments==6)
if((sMu(3)<.00001) || (sMu(5)<.00001))  %If Odd standardized input Moments are zero
     ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))).^2+((sMu(4)-Moments(4))/sMu(4)).^2+ ...
    ((sMu(5)-Moments(5))).^2+((sMu(6)-Moments(6))/sMu(6)).^2;
else
    ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))/sMu(3)).^2+((sMu(4)-Moments(4))/sMu(4)).^2+ ...
    ((sMu(5)-Moments(5))/sMu(5)).^2+((sMu(6)-Moments(6))/sMu(6)).^2;
end
end

if(NMoments==4)
if((sMu(3)<.00001))  %If Odd standardized input Moments are zero
     ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))).^2+((sMu(4)-Moments(4))/sMu(4)).^2;
else
    ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))/sMu(3)).^2+((sMu(4)-Moments(4))/sMu(4)).^2;
end
end

%sMu
%Moments
%str=input("Look at numbers");
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
function [SecondMoment] = CalculateSecondMomentC7(a0,a)

SecondMoment=a0^2+a(1)^2 +2* a0* a(2) +3*(a(2).^2+2* a(1).* a(3) +2* a0* a(4))+ ...
    15*(a(3).^2 +2 *a(2).* a(4) +2 *a(1).* a(5)+2* a0* a(6))+105*(a(4).^2 +2* a(3).* a(5)+2* a(2).* a(6) +2* a(1).* a(7)
)+ ...
    945*(a(5).^2 +2* a(4).* a(6) +2 *a(3).* a(7) )+(10395)*(a(6).^2+2* a(5).* a(7) )+(135135)*a(7).^2;

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

Here is the output you will see at the end of the program when you run it.

mm =

       25000

ObjFuncBest =

     2.515937366420063e+07

ObjFunc =

     2.516638031774695e+07

c =

   0.704625776527650   0.172367249740163   0.075779734629839   0.010302249885808  -0.000858455192471 
 0.000163380494871   0.000027070154411

FittedStandardizedMoments =

   1.0e+05 *

  Columns 1 through 7

  -0.000000000000000   0.000010000000000   0.000022703741246   0.000146746001566   0.001203234599094 
 0.014677673042885   0.254354854886423

  Column 8

   6.259823013349759

sMu =

   1.0e+05 *

  Columns 1 through 7

                   0   0.000010000000000   0.000023672884921   0.000146459814703   0.001202097792368 
 0.014666815921047   0.255435558162736

  Column 8

   6.248806451226628

FittedStandardizedMoments =

   1.0e+05 *

  Columns 1 through 7

  -0.000000000000000   0.000010000000000   0.000022703741246   0.000146746001566   0.001203234599094 
 0.014677673042885   0.254354854886423

  Column 8

   6.259823013349759

Look at comparison of fitted moments with input moments

FittedRawMoments =

   1.0e+05 *

  Columns 1 through 7

   0.000012499863483   0.000021197093700   0.000049871208052   0.000169441507033   0.000850614971863 
 0.006310627233695   0.068555463989281

  Column 8

   1.083805963482055

rMu =

   1.0e+05 *

  Columns 1 through 7

   0.000012499863483   0.000021197093700   0.000050274347857   0.000171368317209   0.000856094970826 
 0.006320436615909   0.068698344472325

  Column 8

   1.084082326087001

---

### #1906 — Amin (Topic Author)
*July 29, 2023, 12:05 PM*

Friends, I tried to improve the program and put it on a more sound logic and I have been able to get good initial
prototype for iterative optimization by perturbing the parameters.

Basic logic is:For parameters with highest sensitivities to Objective Function at any step in optimization loop, we
increase the perturbation, i.e. change in parameters(we accelerate them). and For parameters with least sensitivity, we
decrease the perturbation, i.e change in parameters i.e decelerate them. And this acceleration/deceleration is further
increased or decreased at each time step based on whether global sensitivity to objective function is increasing or
decreasing at each time step. When there is no change in objective function from any parameter on some optimization
step, all parameters are decreased by a ratio(of .85) in my program. All acceleration/deceleration is applied in
extremely small ratios very smoothly.

I explain it below.

Here is the algorithm for optimization.

There are seven coefficients. The way we have set up the problem, the first coefficient is automatically adjusted to
keep the variance standard while c0 is fixed based on other coefficients so that the density has zero mean.

So we are left with optimization solution over six coefficients.

I choose an initial change in coefficients or their speed which is given as DeltaX which is a vector that has seven
elements(one of them is not being used for six parametr optimization). I noticed when the series is in hermite form
variance associated with seventh hermite polynomial is factorial of seven and so on for each hermite polynomial so I
chose initial speed or change in coefficients roughly inversely proportional to multiplier associated with its variance
(though I used a slightly different form in the program.)

I chose this DeltaX as

for nn=1:SeriesOrder

    DeltaX(nn)=.00125/(factorial(nn)).^(.75);

end

DeltaX is first order change or speed of coefficients in optimization. At each iteration I sorted the coefficients in
descending order with respect to their sensitivity on objective function. I increased the speed of first three
coefficients with highest sensitivity and decreased the speed of three coefficients with smallest sensitivity. This is
approximate and can be improved. This is done in the program as (in the below, ddX(n) is proportional acceleration as
the change in the sped of nth coefficient.

to increase speed, acceleration is applied as

DeltaX(n)=DeltaX(n)*(1+ddX(n));

to decrease speed, decleeration is applied as

DeltaX(n)=DeltaX(n)/(1+ddX(n));

So we give acceleration to first three parameters with largest sensitivty and deccelrate the parameters with smallest
sensitivity.

Again this acceleration/decelration is different for each parameter. Initial value of acceleration/deceleration are
given as (below indices are sorted with respect to sensitivity and and are not initial natural indices of coefficients.
index 1 in below is coefficient with largest sensitivity to objective function while index 6 is index with smallest
sensitivity to objective function)

ddX(1)=.005;  %acceleration applied to highest sensitivity index

ddX(2)=.0005;%acceleration applied to 2nd highest sensitivity index.

ddX(3)=.00005;%acceleration

ddX(4)=.00005;%deceleration. speed will be divided.

ddX(5)=.0005;%deceleration

ddX(6)=.005;%deceleration applied to least sensitivity index. speed will be divided

The above are initial values of acceleration and deceleration and are chosen by trial and error to perform best.

Finally we increase or decrease acceleration according to current state of optimization problem. If highest sensitivity
to objective function is increasing at each optimization step, we increase the acceleration applied to highest
sensitivity index and if it is decreasing, we decrease the acceleration associated with highese sensitivity index and so
on for each of the sorted (with respect to sensitivity) indices. For example I explain from code in program as

-------------------------------------------------------------------------------------------------------------------------------------------------

for nn=1:3                  %loop over three highest senstivity indices.

        if(B(nn)>BPrev(nn)) % if sensitivity of index is larger than value at previous step

            ddX(nn)=ddX(nn)*1.000025;  %very slightly increase the acceleration

        else                        % if sensitivity of index is smaller than value at previous step

            ddX(nn)=ddX(nn)/1.000025; %very slightly decrease the acceleration.

        end

 end

--------------------------------------------------------------------------------------------------------------------------------------------------

In the iterative algorithm, change in speed and acceleration are both change very slowly and smoothly and it works very
well.

I am sure that this algorithm can be improved to a great extent but I think this is a good initial prototype with right
basic ideas for a lot of optimizations.

I may not be able to do good work after a few days as an antipsychotic injection is due tomorrow.

Here I post the program.

```
function [] = CalculateZSeriesFromMomentsAgainNew(rMu)
%The above function takes an array of first eight raw moments as input.
%And returns Z-series Coeffs upto 7th power of Z as
%Y=c0+c(1)*Z+c(2)*Z^2+c(3)*Z^3+c(4)*Z^4+c(5)*Z^5+c(6)*Z^6+c(7)*Z^7

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%Input raw moments specified below

rMu(1)=0.000012499863483*10^5;
rMu(2)=0.000021197093700*10^5;
rMu(3)=0.000050274347857*10^5;
rMu(4)=0.000171368317209*10^5;
rMu(5)=0.000856094970826*10^5;
rMu(6)=0.006320436615909*10^5;
rMu(7)=0.068698344472325*10^5;
rMu(8)=1.084082326087001*10^5;

%  mu=1;
%  sigma0=.7;
%  for nn=1:8
%  rMu(nn)=exp(nn*mu+.5*nn^2*sigma0^2);
%  end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
SeriesOrder=7;    %Z-series till 7th power. hardcoded here cannot chagne.
mOrder=8;         %Number of raw moments in calibration. hardcoded here cannot chagne.
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

%
%
% iter=1;           %Number of iterations in the calibration.
%                   %Please experiment and play around.
% bGuess(2:7)=0;    %We have assigned initial values of coefficients
% bGuess(1)=1;      %other than c(1) to zero. We are starting with no prior information.
% [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNew(sMu,bGuess,iter);
% bGuess(1:7)=c(1:7);
% iter=10;
% [c0,c] = PreSmoothingGuessAdvancedFromGuessBestNewModified(sMu,bGuess,iter);
%
% c0
% c
%
% %str=input("Look at pre-smoothing Guess result")
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

c0=0;
c(1)=1;
c(2:7)=0;

Iterations=100000;
[c,ObjFunc] = OptimizeMomentsByIterationZseries08A(sMu,c0,c,SeriesOrder,NMoments,Iterations);
c0=-(c(2)+3*c(4)+15*c(6));
ObjFunc
c

[FittedStandardizedMoments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments)

%Please Uncomment this if you want to see a comparison of input moments and
%fitted moments
sMu
FittedStandardizedMoments
str=input('Look at comparison of fitted moments with input moments');

%%%%%%%%%%%%%%%

c0=c0*sqrt(cMu(2)); %convert from standardized to central moments
c=c*sqrt(cMu(2));   %convert from standardized to central moments

c0=c0+Mu1;          %convert from central to raw moments by adding mean.

[FittedRawMoments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

FittedRawMoments
rMu
end
```

.

.

.

```
function [c,ObjFunc] = OptimizeMomentsByIterationZseries08A(sMu,c0,c,SeriesOrder,NMoments,Iterations)

for nn=1:SeriesOrder
    DeltaX(nn)=.00125/(factorial(nn)).^(.75);
    %DeltaX(nn)=.00125/(factorial(nn)).^(.25);%uncomment for lognormal like
    %extremely high skew and very large higher standard moments.
end

ddX(1)=.005;
ddX(2)=.0005;
ddX(3)=.00005;
ddX(4)=.00005;
ddX(5)=.0005;
ddX(6)=.005;

B(1:6)=0;
BPrev(1:6)=0;

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

%ObjFuncBest= CalculateMomentsDiscreteXnObjFunction(Ms,Xn,X0,NPoints,NMoments);
[ObjFuncBest] =CalculateMomentsMatchObjFunction0A(Moments,NMoments,sMu);
cBest=c;
c0Best=c0;
%ContImproveFlag=0;
ImproveFlag(1:SeriesOrder)=0;
DeltaObj(1:SeriesOrder)=0;
DeltaObjPrev(1:SeriesOrder)=0;
ObjSensitivity(1:SeriesOrder)=0;
ImproveFlag0=0;
ImproveCount=0;
for mm=1:Iterations
    ImproveFlag0Prev=ImproveFlag0;
    ImproveFlag(1:SeriesOrder)=0;
    for nn=2:SeriesOrder
        DeltaObjPrev(nn)=DeltaObj(nn);
        ObjSensitivityPrev(nn)=ObjSensitivity(nn);
        cin=c;
        cin(nn)=cin(nn)+DeltaX(nn);
        c0in=-(cin(2)+3*cin(4)+15*cin(6));

        [SecondMoment]=CalculateSecondMomentC7(c0in,cin);
        cin=cin/sqrt(SecondMoment);
        c0in=c0in/sqrt(SecondMoment);
        [Moments] = CalculateMomentsOfZSeries(c0in,cin,SeriesOrder,NMoments);
        [ObjFunc] =CalculateMomentsMatchObjFunction0A(Moments,NMoments,sMu);

        %[ObjFunc] = CalculateMomentsDiscreteXnObjFunction(Ms,Xin,X0,NPoints,NMoments);
        if(ObjFunc0)
            %AvgSensitivity=AvgSensitivity+abs(DeltaStep(nn)).*abs(ObjSensitivity(nn));
            AvgSensitivity=AvgSensitivity+abs(ObjSensitivity(nn))/SeriesOrder;
            %SumDeltaStep=SumDeltaStep+abs(DeltaStep(nn));
        end

        if(ImproveFlag(nn)==1)
            ImproveFlag0=1;
        end
    end

    %AvgSensitivity=AvgSensitivity/SumDeltaStep;
    ObjSensitivity0Prev=B;
    ObjSensitivity0(1:6)=abs(ObjSensitivity(2:7));
    [B,I] = sort(ObjSensitivity0,'descend');

    for nn=1:3
        if(B(nn)>BPrev(nn))
            ddX(nn)=ddX(nn)*1.000025;
        else
            ddX(nn)=ddX(nn)/1.000025;
        end
    end
    for nn=4:6
        if(B(nn)0)
        DeltaX(I(1)+1)=DeltaX(I(1)+1)*(1+ddX(1));
        DeltaX(I(6)+1)=DeltaX(I(6)+1)/(1+ddX(6));
        if(ObjSensitivity(I(2)+1)>0)
            DeltaX(I(2)+1)=DeltaX(I(2)+1)*(1+ddX(2));
        end
        if(ObjSensitivity(I(3)+1)>0)
            DeltaX(I(3)+1)=DeltaX(I(3)+1)*(1+ddX(3));
        end
        if(ObjSensitivity(I(4)+1)>0)
            DeltaX(I(4)+1)=DeltaX(I(4)+1)/(1+ddX(4));
        end
        if(ObjSensitivity(I(5)+1)>=0)
            DeltaX(I(5)+1)=DeltaX(I(5)+1)/(1+ddX(5));
        end
    end

    if((ImproveFlag0)&&(ImproveFlag0Prev))
        ImproveCount=ImproveCount+1;
    else
        ImproveCount=0;
    end

    if(ImproveCount>=4)
        ImproveCount=0;
        DeltaX=DeltaX*1.15;
    end

    if(ImproveFlag0==0)
        DeltaX=DeltaX*.85;
    end
end
c=cBest;
end
```

.

.

.

```
function [ObjNew] =CalculateMomentsMatchObjFunction0A(Moments,NMoments,sMu)
%[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

 if(NMoments==8)
    %
ObjNew=((sMu(1)-Moments(1))).^2+factorial(8).*((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))).^2+factorial(6)*((sMu(4)-Moments(4))/sMu(4)).^2+
...
    % ((sMu(5)-Moments(5))).^2+factorial(4)*((sMu(6)-Moments(6))/sMu(6)).^2+((sMu(7)-Moments(7))).^2+ ...
    % factorial(2)*((sMu(8)-Moments(8))/sMu(8)).^2;

 
ObjNew=factorial(8).*((sMu(2)-Moments(2))).^2+factorial(9).^2.*((sMu(3)-Moments(3))).^2+factorial(8).^2*((sMu(4)-Moments(4))).^2+
...
   
 factorial(7).^2.*((sMu(5)-Moments(5))).^2+factorial(6).^2*((sMu(6)-Moments(6))).^2+factorial(4).^2.*((sMu(7)-Moments(7))).^2+
...
     ((sMu(8)-Moments(8))).^2;

%ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2;

%ObjNew=((sMu(1)-Moments(1))/sMu(1)).^2*0+factorial(8).*((sMu(2)-Moments(2))/sMu(2)).^2;%+0*((sMu(3)-Moments(3))).^2+factorial(6)*((sMu(4)-Moments(4))/sMu(4)).^2;%+
...
%    ((sMu(5)-Moments(5))).^2+factorial(4)*((sMu(6)-Moments(6))/sMu(6)).^2+((sMu(7)-Moments(7))).^2+ ...
%    factorial(2)*((sMu(8)-Moments(8))/sMu(8)).^2;

%
%if((sMu(3)<.00001) || (sMu(5)<.00001) || (sMu(7)<.00001))  %If Odd standardized input Moments are zero
  %   ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))).^2+((sMu(4)-Moments(4))/sMu(4)).^2+ ...
  %  ((sMu(5)-Moments(5))).^2+((sMu(6)-Moments(6))/sMu(6)).^2+((sMu(7)-Moments(7))).^2+ ...
  %  ((sMu(8)-Moments(8))/sMu(8)).^2;
%   
ObjNew=20*((sMu(1)-Moments(1))/sMu(1)).^2+10000*((sMu(2)-Moments(2))/sMu(2)).^2+100*((sMu(3)-Moments(3))).^2+200*((sMu(4)-Moments(4))/sMu(4)).^2+
...
%    ((sMu(5)-Moments(5))).^2+20*((sMu(6)-Moments(6))/sMu(6)).^2+((sMu(7)-Moments(7))).^2+ ...
%    ((sMu(8)-Moments(8))/sMu(8)).^2;
%else
%   
ObjNew=((sMu(1)-Moments(1))/sMu(1)).^2+((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))/sMu(3)).^2+((sMu(4)-Moments(4))/sMu(4)).^2+
...
%    ((sMu(5)-Moments(5))/sMu(5)).^2+((sMu(6)-Moments(6))/sMu(6)).^2+((sMu(7)-Moments(7))/sMu(7)).^2+ ...
%    ((sMu(8)-Moments(8))/sMu(8)).^2;
%end
end

if(NMoments==6)
if((sMu(3)<.00001) || (sMu(5)<.00001))  %If Odd standardized input Moments are zero
     ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))).^2+((sMu(4)-Moments(4))/sMu(4)).^2+ ...
    ((sMu(5)-Moments(5))).^2+((sMu(6)-Moments(6))/sMu(6)).^2;
else
    ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))/sMu(3)).^2+((sMu(4)-Moments(4))/sMu(4)).^2+ ...
    ((sMu(5)-Moments(5))/sMu(5)).^2+((sMu(6)-Moments(6))/sMu(6)).^2;
end
end

if(NMoments==4)
if((sMu(3)<.00001))  %If Odd standardized input Moments are zero
     ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))).^2+((sMu(4)-Moments(4))/sMu(4)).^2;
else
    ObjNew=((sMu(2)-Moments(2))/sMu(2)).^2+((sMu(3)-Moments(3))/sMu(3)).^2+((sMu(4)-Moments(4))/sMu(4)).^2;
end
end

%sMu
%Moments
%str=input("Look at numbers");
end

```

.

.

.

Here is the output you will see at the end of the program.

mm =

      100000

ObjFuncBest =

     3.661819239243499e+05

ObjFunc =

     3.661863088286945e+05

c =

   0.759572055648810   0.207488636510716   0.048426815591184   0.011614855120852  -0.000159423020224 
 0.000233334935750   0.000005480714117

FittedStandardizedMoments =

   1.0e+05 *

  Columns 1 through 7

   0.000000000000000   0.000010000000000   0.000023673847458   0.000146359082858   0.001202700229681 
 0.014668225745158   0.255311625720065

  Column 8

   6.249757252008330

sMu =

   1.0e+05 *

  Columns 1 through 7

                   0   0.000010000000000   0.000023672884921   0.000146459814703   0.001202097792368 
 0.014666815921047   0.255435558162736

  Column 8

   6.248806451226628

FittedStandardizedMoments =

   1.0e+05 *

  Columns 1 through 7

   0.000000000000000   0.000010000000000   0.000023673847458   0.000146359082858   0.001202700229681 
 0.014668225745158   0.255311625720065

  Column 8

   6.249757252008330

Look at comparison of fitted moments with input moments

FittedRawMoments =

   1.0e+05 *

  Columns 1 through 7

   0.000012499863483   0.000021197093700   0.000050274748248   0.000171339039860   0.000856045378090 
 0.006321010436635   0.068686948845910

  Column 8

   1.084034593526173

rMu =

   1.0e+05 *

  Columns 1 through 7

   0.000012499863483   0.000021197093700   0.000050274347857   0.000171368317209   0.000856094970826 
 0.006320436615909   0.068698344472325

  Column 8

   1.084082326087001

---

### #1907 — Amin (Topic Author)
*July 30, 2023, 6:31 AM*

Friends, it is possible in cases when eighth moment is extremely large which happens with lognormal like distributions
with very long tails that the program might not calibrate properly and fit to some smaller moments might remain poor. In
such cases try to further increase the weights on smaller moments in the objective function calculation function and run
the same program.

Also starting change in parameters obviously have to be a fraction proportional to the magnitude of true size of
parameters themselves. So when tails are very large, we need a different relative magnitude of perturbation size for
each parameter with slightly more weight given to fifth, sixth and seventh coefficient.

In function OptimizeMomentsByIterationZseries08A, I have given two possibilities for starting perturbations size/speed
and you have to de-comment the appropriate one or use something similar. These are given below as

     DeltaX(nn)=.00125/(factorial(nn)).^(.75);  %for medium tails and medium sized higher moments

    %DeltaX(nn)=.00125/(factorial(nn)).^(.2);%uncomment for lognormal like

    %extremely high skew and very large higher standard moments. For very long tails.This gives relatively higher
perturbation size/speed to higher coefficients.

I will try to play some more with the program and try to come up with a better and improved version.

---

### #1908 — Amin (Topic Author)
*July 30, 2023, 7:48 AM*

Friends, I played around with the same basic program and was able to somewhat improve it by changing values of some
ratios used in optimization.

if(ImproveCount>=4)

        ImproveCount=0;

        DeltaX=DeltaX*1.3; %changed from 1.15 to 1.3

 end

 if(ImproveFlag0==0)

        DeltaX=DeltaX*.95; %changed from .85 to .95;

 end

I also re-wrote the objective function routine so that weight of every moment remains balanced.

For very long tails, you will have to increase iterations of the program.

I will get an antipsychotic injection in a few hours and may not work later today after that.

Here is the new program.

```
function [] = CalculateZSeriesFromMomentsAgainNew(rMu)
%The above function takes an array of first eight raw moments as input.
%And returns Z-series Coeffs upto 7th power of Z as
%Y=c0+c(1)*Z+c(2)*Z^2+c(3)*Z^3+c(4)*Z^4+c(5)*Z^5+c(6)*Z^6+c(7)*Z^7

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%Input raw moments specified below

rMu(1)=0.000012499863483*10^5;
rMu(2)=0.000021197093700*10^5;
rMu(3)=0.000050274347857*10^5;
rMu(4)=0.000171368317209*10^5;
rMu(5)=0.000856094970826*10^5;
rMu(6)=0.006320436615909*10^5;
rMu(7)=0.068698344472325*10^5;
rMu(8)=1.084082326087001*10^5;

%   mu=-2;
%   sigma0=.9;
%   for nn=1:8
%   rMu(nn)=exp(nn*mu+.5*nn^2*sigma0^2);
%   end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
SeriesOrder=7;    %Z-series till 7th power. hardcoded here cannot chagne.
mOrder=8;         %Number of raw moments in calibration. hardcoded here cannot chagne.
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

c0=0;
c(1)=1;
c(2:7)=0;

Iterations=20000;
[c,ObjFunc] = OptimizeMomentsByIterationZseries08A(sMu,c0,c,SeriesOrder,NMoments,Iterations);
c0=-(c(2)+3*c(4)+15*c(6));
ObjFunc
c

[FittedStandardizedMoments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments)

%Please Uncomment this if you want to see a comparison of input moments and
%fitted moments
sMu
FittedStandardizedMoments
str=input('Look at comparison of fitted moments with input moments');

%%%%%%%%%%%%%%%

c0=c0*sqrt(cMu(2)); %convert from standardized to central moments
c=c*sqrt(cMu(2));   %convert from standardized to central moments

c0=c0+Mu1;          %convert from central to raw moments by adding mean.

[FittedRawMoments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

FittedRawMoments
rMu
end
```

.

.

.

```
function [ObjNew] =CalculateMomentsMatchObjFunction0A08(Moments,sMu)

%To avoid repeated omputations of these weights, you can calculate them once outside the program and input as a
parameter to function.

if (sMu(3)>1)
    Wts(3)=(sMu(8)/sMu(3)).^2;
else
    Wts(3)=(sMu(8)).^2;
end

Wts(4)=(sMu(8)/sMu(4)).^2;

if (sMu(5)>1)
    Wts(5)=(sMu(8)/sMu(5)).^2;
else
    Wts(5)=(sMu(8)).^2;
end

Wts(6)=(sMu(8)/sMu(6)).^2;

if (sMu(7)>1)
    Wts(7)=(sMu(8)/sMu(7)).^2;
else
    Wts(7)=(sMu(8)).^2;
end

Wts(8)=1;

  ObjNew=Wts(3).*((sMu(3)-Moments(3))).^2+Wts(4)*((sMu(4)-Moments(4))).^2+ ...
     Wts(5).*((sMu(5)-Moments(5))).^2+Wts(6)*((sMu(6)-Moments(6))).^2+Wts(7).*((sMu(7)-Moments(7))).^2+ ...
     Wts(8).*((sMu(8)-Moments(8))).^2;

end

```

.

.

.

```
function [c,ObjFunc] = OptimizeMomentsByIterationZseries08A(sMu,c0,c,SeriesOrder,NMoments,Iterations)

for nn=1:SeriesOrder
    DeltaX(nn)=.00125/(factorial(nn)).^(.75);
    %DeltaX(nn)=.00125/(factorial(nn)).^(.2);%uncomment for lognormal like
    %extremely high skew and very large higher standard moments.
end

ddX(1)=.005;
ddX(2)=.0005;
ddX(3)=.00005;
ddX(4)=.00005;
ddX(5)=.0005;
ddX(6)=.005;

B(1:6)=0;
BPrev(1:6)=0;

[Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);

%ObjFuncBest= CalculateMomentsDiscreteXnObjFunction(Ms,Xn,X0,NPoints,NMoments);
%[ObjFuncBest] =CalculateMomentsMatchObjFunction0A(Moments,NMoments,sMu);
[ObjFuncBest] =CalculateMomentsMatchObjFunction0A08(Moments,sMu);
cBest=c;
c0Best=c0;
%ContImproveFlag=0;
ImproveFlag(1:SeriesOrder)=0;
DeltaObj(1:SeriesOrder)=0;
DeltaObjPrev(1:SeriesOrder)=0;
ObjSensitivity(1:SeriesOrder)=0;
ImproveFlag0=0;
ImproveCount=0;
for mm=1:Iterations
    ImproveFlag0Prev=ImproveFlag0;
    ImproveFlag(1:SeriesOrder)=0;
    for nn=2:SeriesOrder
        DeltaObjPrev(nn)=DeltaObj(nn);
        ObjSensitivityPrev(nn)=ObjSensitivity(nn);
        cin=c;
        cin(nn)=cin(nn)+DeltaX(nn);
        c0in=-(cin(2)+3*cin(4)+15*cin(6));

        [SecondMoment]=CalculateSecondMomentC7(c0in,cin);

        cin=cin/sqrt(SecondMoment);
        c0in=c0in/sqrt(SecondMoment);
        [Moments] = CalculateMomentsOfZSeries(c0in,cin,SeriesOrder,NMoments);
        %[ObjFunc] =CalculateMomentsMatchObjFunction0A(Moments,NMoments,sMu);
        [ObjFunc] =CalculateMomentsMatchObjFunction0A08(Moments,sMu);

        %[ObjFunc] = CalculateMomentsDiscreteXnObjFunction(Ms,Xin,X0,NPoints,NMoments);
        if(ObjFunc0)
            %AvgSensitivity=AvgSensitivity+abs(DeltaStep(nn)).*abs(ObjSensitivity(nn));
            AvgSensitivity=AvgSensitivity+abs(ObjSensitivity(nn))/SeriesOrder;
            %SumDeltaStep=SumDeltaStep+abs(DeltaStep(nn));
        end

        if(ImproveFlag(nn)==1)
            ImproveFlag0=1;
        end
    end

    %AvgSensitivity=AvgSensitivity/SumDeltaStep;
    ObjSensitivity0Prev=B;
    ObjSensitivity0(1:6)=abs(ObjSensitivity(2:7));
    [B,I] = sort(ObjSensitivity0,'descend');

    for nn=1:3
        if(B(nn)>BPrev(nn))
            ddX(nn)=ddX(nn)*1.000025;
        else
            ddX(nn)=ddX(nn)/1.000025;
        end
    end
    for nn=4:6
        if(B(nn)0)
        DeltaX(I(1)+1)=DeltaX(I(1)+1)*(1+ddX(1));
        DeltaX(I(6)+1)=DeltaX(I(6)+1)/(1+ddX(6));
        if(ObjSensitivity(I(2)+1)>0)
            DeltaX(I(2)+1)=DeltaX(I(2)+1)*(1+ddX(2));
        end
        if(ObjSensitivity(I(3)+1)>0)
            DeltaX(I(3)+1)=DeltaX(I(3)+1)*(1+ddX(3));
        end
        if(ObjSensitivity(I(4)+1)>0)
            DeltaX(I(4)+1)=DeltaX(I(4)+1)/(1+ddX(4));
        end
        if(ObjSensitivity(I(5)+1)>=0)
            DeltaX(I(5)+1)=DeltaX(I(5)+1)/(1+ddX(5));
        end
    end

    if((ImproveFlag0)&&(ImproveFlag0Prev))
        ImproveCount=ImproveCount+1;
    else
        ImproveCount=0;
    end

    if(ImproveCount>=4)
        ImproveCount=0;
        DeltaX=DeltaX*1.3;
    end

    if(ImproveFlag0==0)
        DeltaX=DeltaX*.95;
    end
end
c=cBest;
end
```

.

.

.

Here is the final output of the program, you will see when you run it.

mm =

       20000

ObjFuncBest =

     3.024244685911754e+04

ObjFunc =

     3.024346585791719e+04

c =

   0.750093991263325   0.214896203894255   0.050755545183275   0.009116657817579   0.000252400772349 
 0.000250488803671   0.000000238094574

FittedStandardizedMoments =

   1.0e+05 *

  Columns 1 through 7

   0.000000000000000   0.000010000000000   0.000023672679439   0.000146437649483   0.001202341993694 
 0.014666662976709   0.255408587290504

  Column 8

   6.249082059272988

sMu =

   1.0e+05 *

  Columns 1 through 7

                   0   0.000010000000000   0.000023672884921   0.000146459814703   0.001202097792368 
 0.014666815921047   0.255435558162736

  Column 8

   6.248806451226628

FittedStandardizedMoments =

   1.0e+05 *

  Columns 1 through 7

   0.000000000000000   0.000010000000000   0.000023672679439   0.000146437649483   0.001202341993694 
 0.014666662976709   0.255408587290504

  Column 8

   6.249082059272988

Look at comparison of fitted moments with input moments

FittedRawMoments =

   1.0e+05 *

  Columns 1 through 7

   0.000012499863483   0.000021197093700   0.000050274262381   0.000171361007084   0.000856107224323 
 0.006320670039864   0.068696008660374

  Column 8

   1.084077905875491

rMu =

   1.0e+05 *

  Columns 1 through 7

   0.000012499863483   0.000021197093700   0.000050274347857   0.000171368317209   0.000856094970826 
 0.006320436615909   0.068698344472325

  Column 8

   1.084082326087001

---

### #1909 — Amin (Topic Author)
*July 31, 2023, 11:34 PM*

Friends, I went out yesterday around one pm. And came back by 5 pm in the evening. I decided to have an early sleep and
slept around 5:30 pm. I had a good sleep and woke up around 12:00 am.

After wasting sometime, I took my laptop to porch/car garage. Mind control agents have several kinds of gases set up
everywhere in the house. Before working, I just had a review of news and some other general places that I browse through
regularly. Mind control agents continued to release a particular gas that affects the brain and causes a feeling of
weakness when I breathe it for sometime. I had a mild headache due to weakness in body and brain and due to the gas.

I had some bread and toasted it and ate it to feel better. When, after half an hour, I went to porch to work again, they
released another  gas that charges the body and the clothes. I tried to work but they continued to release the gas until
I realised that it was impossible to wok in the garage. So I left the porch and came inside my room and tried to work
but they released a different gas and made it impossible to work. I tried to sleep but had to wake up due to involuntary
cough induced by gas released in my room.

I want to tell friends even though scum general in US army will try their best to profess patriotism to united states,
in fact they are nothing more than mercenaries fighting to get into the paradise of jewish billionaire and his rich
cohort of jews.

After the effect of injection decreases a bit in 10-12 days, I hope to try contacting a few prominent Pakistanis like I
earlier mentioned a few days ago and ask them for help in my case.

---

### #1910 — Amin (Topic Author)
*August 3, 2023, 10:42 AM*

Friends, I have lately been sleeping a lot due to sedation from antipsychotic injection. But I was feeling somewhat
better today and started to brainstorm how to take my research forward. And I have a lot of ideas.

First, I want to continue with applications of multidimensional Hermite polynomial regression and try to use it for
conditional expectations in monte carlo models of various classes of derivatives, i.e delta-vega hedging, least squares
monte carlo for bermudan/american derivatives, CVA/XVA and all of these things in single asset to multidimensional
setting.

I also noticed that in current methods of monte carlo simulations, when a large number of independent normals (or
driving brownian motions of SDEs) are used in simulations of correlated assets, even though variances in simulated
assets are equal to marginal variances(of marginal density of particular asset), simulated density is different from
marginal density(that would be obtained from only simulating the particular asset with just one independent brownain
motion. This is because using correlated brownian motions alters the higher moments of the SDEs when compared with
higher moments with just one brownian motion driving the SDE(as in marginal densities) even though variances do remain
the same in both cases. I want to explore this further and see if the difference is small or large enough to be
tradeable. I also want to work on proper modelling of high dimensional simulations so that both correlations are
properly simulated and simultaneously higher order moments match with those of the marginal distribution.

Another very important thing that I want to do is to learn Rust (I know C++ well enough), and use it for AI applications
with Z-series. And start with writing small routines for AI that find closest valid Z-series given some input moments,
and all sort of similar things like addition of various correlated/uncorrelated Z-series. I want to start by writing a
lot of small programs doing some basic functions on Z-series with Rust using AI, incorporate polynomial regressions  and
then try to take it to somewhat higher complexity slowly that would involve working with more complex stochastic systems
like hedging and trading in multidimensional stochastic volatility models and possibly beyond. I want to start learning
Rust and start working on the idea right away.

As ever, I will be posting all of my programs on the same thread.

---

### #1911 — Amin (Topic Author)
*August 3, 2023, 7:34 PM*

Friends, whatever I do or try, there is no let down in use of gases on me. Mind control agents openly and repeatedly
continue to use the heavy gas in all rooms of the house. They again and again release this gas in my room especially
they released this heavy gas more than fifteen times during the day. This gas charges the clothes and the lower limbs,
This gas settles on the body especially the private parts and helps in mind control. This is one of very difficult
experiences.

Then they have another gas in almost all ceiling fans of our house. This gas effects the brain and causes weakness in
the brain and light headache. This second gas is inhaled by the body and goes into the body with breathing. This is a
new gas and I have talked several times about a gas that I had to inhale but that was different gas and these days, they
are not using that gas.

They again and again have been using both these gases on me in past few days. I want to request good American people to
please protest against use of gases by US army on innocent civilians. Please ask good Americans who are in position of
authority in US government to force US army to end such mean and subhuman tactics on good and innocent people.

---

### #1912 — Amin (Topic Author)
*August 9, 2023, 9:35 AM*

Friends, I was getting somewhat better earlier but my condition deteriorated again due to antipsychotic injection and I
could not do any work for past few days. In Lahore we only had 7-10 days of extreme heat in June and then weather became
better as monsoon started and temperature decreased but for past three or four days, it has not rained and it is
extremely humid with a relatively high temperature so it was very difficult to work.

For my next project I have a very interesting research idea. I want to use Kalman filtering-like algorithm in
generalized non-gaussian setting with hermite polynomials and try to predict a ten dimensional time series with changing
mean reversion and correlation (we will try to filter the values of mean-reversion and serial correlation in an
innovative setting). I will first start with a simple classic linear Kalman filter algorithm for parameters and see how
it works and  if it works well, I will extend the idea to non-gaussian hermite polynomial setting. In a way this is a
risky project since I really do not know whether it will succeed or not. But I think if it works well, it ill be very
exciting.

It will be a few days before the results could be available and I will keep posting everything on this forum.

---

### #1913 — Amin (Topic Author)
*August 10, 2023, 6:50 PM*

Friends, I am working on my program in my mother's room. She invited me to work in her room at night because she has
turned on her AC. She is sleeping on bed and I am working on a portable table and chair placed in her room while light
is on. She leaves the light on in her room many times while on her own and is not disturbed by the light and has a
normal sleep ( I could never do this since I can only sleep in the dark). Historically the AC in my mother's room has
the least gas or any other similar problems among all the rooms in our house. But I noticed when I correct a mistake in
my half brewed program or do something creative, they start releasing some gas out of the AC in my mother's room where I
am working.  I was very upset with this so decided to quickly make this post to let friends know how mind control
agencies try to control their victims.

---

### #1914 — Amin (Topic Author)
*August 13, 2023, 6:37 PM*

Friends, I have written a program for quick trading in stocks that trades on a 15 seconds time grid. Originally I wanted
a time series prediction program but I ended up writing a very similar stocks trading program. It deals with a
univariate time series as opposed to what I  initially intended. I have used filtering of parameters in a similar spirit
to an older program I had posted on this forum a few years ago. Again this might not be the best prediction method as I
consider. But I have been able to present some other genuine ideas that I hope friends would really like and I hope
these new ideas will help friends write their own very successful trading programs. I will post the program in a day or
to with written explanations but will just outline the new ideas that friends may like.

I have used optimization to find mean-reversion parameters for the Tesla stock series. In my time series there are mean
reversion parameters and correlation parameters. I am using data of Tesla stock several years ago when it was totally
wild and was hovering around 750 dollars. I found it had huge mean reversion. But still I think my choice of parameters
is only experimental and can be largely improved by most friends. Ok, as I said, I run optimization on yesterdays's data
to find the parameters that best optimize the profits and use those optimized parameters from previous day on next day's
data. However, I had some more interesting ideas. So with live data, I also run parallel simulations on live data with a
large number of other parameters. In my basic program, I used various possible combinations of displaced (positively and
negatively) parameters and ran simulated profits on them in parallel with the program with original optimized
parameters. The original idea was that when simulated profit from parallel simulations exceeds continuously for a few
minutes than the profits from the original parameters decisions, I will switch live decision making to the parameters
that are have been giving most profits consistently for a few past minutes.

Initially when I used this approach, it did not seem to work very well but then I made a switching threshold that switch
will occur only when simulated profits are more than 1.5 times (or 1.7 times) the original parameters profit, then
switch will occur. So increasing the switching threshold to 1.5 or 1.7 or 2 from one remarkably improved the program and
worked very very well. Choosing best switching threshold will also be of interest to friends.

I only chose combinations of displaced parameters and ran a total of 23 parallel simulations with different parameters
but, in actual practice, friends can choose various sets of optimized parameters from the data that reflect different
market conditions and then choose the best parameters considering parallel simulated profits to make actual trading
decisions while choosing parameters according to switching rule. So when market quickly changes, you have some set of
parameters from past that suits the changing market and profits increase instead of a fixed parameter program making
losses.

However, in my initial simulations it was not guaranteed that switching parameters will have the most profits and there
were a few days when profits from original rule were slightly higher.

But switching parameters had remarkably higher profits in total and had a far better sharpe ratio. I noticed that there
was a large consistency in switching parameters trading in making profits and especially when original parameters made
very large losses, switching parameters were almost always able to make very reasonable profits to avoid the wild ups
and (especially) downs associated with original non-switching parameters decision making. Therefore Sharpe ratio was far
better in switching parameters portfolio.

To give friends an idea, my algorithm traded a single Tesla stock (roughly around 700-750 dollars) and was able to make
profit of roughly 370 dollars around mid-price in two months. While switching parameters portfolio roughly made a profit
of 470 dollars around mid-price but sharpe ratio was hugely better with switching parameters. There was large spread
between bid and ask prevailing on Tesla Stock at that time. We intend to make trades using limit orders and ideally if
every trade goes through, you could earn more than 2000 dollars on a single Tesla stock by earning spreads in two
months. There was high liquidity with large spreads (as the stock was wild) and the stock traded more than 15000 shares
per 15 seconds period. So if we could trade using limit orders, you will earn the profit around mid price plus the
spread earned with limit orders. I am sure even with all sort of slippage and despite some inabilities to enter the
trades with limit orders here and there, the strategy would have been wildly profitable. Unfortunately it is data from
several years ago.

Just to give some idea, the worst single day losses with pre-optimized parameters from yesterday were roughly -60, -50
and -30 while switching parameters trading was around positive 30s or 40s in all of these bad days. However, I noticed
that there was a bad (actually the worst) day in switching parameters portfolio when it was around -30 while original
parameters was far better on that day. However negative days were very limited on switching parameters portfolio as
opposed to original portfolio.

I really did not spend a lot of time improving switching parameters portfolio so I think with research friends would be
able to improve on the idea. I really think that this is a very interesting new idea that friends would like.

I want to make another improvement in the program. If switching portfolio makes consistent losses for a few minutes, the
program will halt trading and start trading only when there will be profits again in simulated parallel trading for a
pre-specified period of time. This will further improve the program.

I will be posting my program in a day or two.

---

### #1915 — Amin (Topic Author)
*August 13, 2023, 7:00 PM*

Sorry, some information I will like to add. The algorithm roughly made somewhere between 25,000 to 30,000 trades in two
months of data with average lifetime of a trade less than a minute. The broker commissions were roughly 220 dollars (As
per IB most expensive tier). All analysis was for a single Tesla stock though it assumes that you trade lots of 100
stocks. So was switching parameters portfolio profit of 470 dollars(was for a single stock). Most important part of
earning spread is on top of this profit of 470 dollars.

---

### #1916 — Amin (Topic Author)
*August 14, 2023, 10:49 AM*

Friends, mind control agents simply are not ready to let me work properly. My sister is in our home for the day and
therefore I could not work in the lounge because her children are everywhere. I wanted to improve the algorithm and
started to work but constant gas in the fan in my room gives me strong headache and physical weakness and I really
cannot concentrate on anything and cannot work properly and continue to make mistakes.

I really wanted to spend sometime looking into the dynamics of the algorithm and figuring out how to make it better but
mind control agent are simply not ready to let me work at all. Please protest to responsible people in American
government and ask them to stop the American army from openly torturing innocent civilians with gas and other tactics.

---

### #1917 — Amin (Topic Author)
*August 16, 2023, 4:57 PM*

Friends, very sorry for delay in my post. I was feeling very upset when I wrote the above post on monday afternoon. So I
decided to leave the work and go out earlier in the evening rather than after sunset. It was cloudy so hot weather was
not a problem. I was already being slightly disoriented and kept asking the children to not play with me and let me
work. I had not realized it but I was already a bit off and disoriented. Just a little bit after I went out, I started
feeling strong weakness in the body and brain. I did not make a big deal but when I went into a store, I noticed, for a
very little bit, that everything was moving in circles. When I noticed this, I knew I had some sickness or fever also
because I was feeling very weak. I decided to head straight back home. I had a lot of panadol quite frequently over past
two days. And yesterday, my brother brought some medicine for fever and running nose. I kept taking medicine including
Panadol and I was feeling better today and my temperature also became normal. I am fine now after sickness of past two
days if fever does not strike back.

Today in the afternoon, I worked on the model and made a lot of changes in it. But I want to take two or three more days
to add all ideas in the model and then post it on the forum after that.

But gases continue, and despite my fever, they continued to release gas on me in my room last night when I went there
for a bit(I slept in my mother's room in the air-conditioning last night). They also continued to use gas on me when I
was working in my mother's room in the afternoon today.

---

### #1918 — Amin (Topic Author)
*August 16, 2023, 5:46 PM*

Friends, I want to request again to please ask some responsible Americans to force American government or army to not
use gases on innocent civilians. After I wrote my previous post, I went to bed to sleep but mind control agents again
released gas in my room. And I started feeling pain in my vein that goes to brain on the left side. This is a new gas
that they have been using for one past week. It causes weakness in body and brain and also causes light pain in vein
that goes to brain on left side. But every day they continue to get bolder and pain that coincides with gas continues to
become stronger. For the old gas, Every time they give gas, the veins that go to brain start pumping hard like throbbing
and they cause some uneasiness in the veins, weakness in brain but it can rarely be called real physical pain in the
veins. But new gas they have  started using recently causes real pain in the veins that can become unbearable. Please
try to help me if you can.

I want to say something to Jews that I am very aware that most jews are very nice people. But please recall that every
rich machinatory asshole jew successfully left Germany but every good-natured jew who never imagined to hurt anyone was
put to death in gas chambers. We all want to commemorate Holocaust as one of the  greatest human tragedies ever and We
want to celebrate success of all Jews who work hard and are nice to other human beings but please do not let a few rich
billionaire jewish assholes tarnsih the hard-earned reputation of jews in America and all over the world. Please note
that mind control is a very cruel torture tactic to destroy life of intelligent people and jewish billionaire and his
rich cohort are using it like a machine gun on others because American army is in their complete control.

---

### #1919 — Amin (Topic Author)
*August 17, 2023, 7:26 PM*

Jewish friends, I want to apologize about my uninformed view about jews leaving Germany as I stated in my previous post.
I was under possibly completely wrong impression that some jews were involved in collusion in some cases in Germany. I
am not well-informed about the issue and I do not know whether I was right or wrong, I simply do not know. I do not have
any special literature to read about the problem and it is difficult to find time to start investigating these very
peripheral issues of no serious concern. So given my realization of lack of sound knowledge, I want to say sorry to any
jews I might have hurt and I apologize about my statement in previous post. Even if somebody did anything wrong they
should have been tried in civilian courts rather than Nazi military taking matter in their own hands. And of course, we
all obviously know that every jew who was killed in gas chambers was a good soul like most of the good people we see
around in our communities.

I was also very upset due to sheer pain due to gas and high frequency lasers and possibly crossed some limits. I am
sorry.

But still I want to emphasize that the real issue is about using mind control to completely fail innocent people by some
bad actors in our society.  The idea of militaries imparting justice cannot be allowed in any civilized society in 21st
centrury (Has America become Pakistan where powerful military decides a lot of people's destiny --- I do see some
similarity here). A good and blind justice system should be pride of any great nation rather than their militaries
deciding who to retard and who to allow to succeed.

Jews are intelligent people in general. I would appeal to them to rise above the religious lines in their thinking(as a
large number of them probably know better than me). I do not believe in religion even though I am classified as a
Muslim. Here I will like to tell people that till eight or nine years ago, I was still a mild believer in religion. As
friends know, I live alone and I do not have many friends at this stage. I never had the opportunity of any discussion
with people about religion. I just would read a lot about evolution of life in early earth on wikipedia. How microbes
created oxygen on our planet and transformed its atmosphere over more than a billion years to a totally different
composition. Oxygen does not naturally occur like this on any of the exoplanets anywhere in this universe as it exists
on our green planet. I read a lot about different epochs of various kinds of animals and species that roamed the earth.
And then the final very very recent evolution of humanity.

I am also avid reader of all things about universe, space and galaxies.

However certain we might be about truthfulness of prophets, once we have broader information about history of our earth
and our universe, we know that God does not easily fit in anywhere. I just became a non-believer on my own over time.

So I really think that most intelligent people and good human beings should rise above religion. Especially if you are
far more rich, you should be expected to be far more nice and kind to other people in the society as compared to an
ordinary person. I do not follow rich people at all on linkedin. But one person I follow is Bill Gates who is the
perfect example of what a rich billionaire should be. More than being rich, he is a fantastic human being and that is
why I really follow him. He is what every billionaire should be like. I do not want to sound disrespectful but may be
the Jewish billionaire and his rich cohort learn anything from Bill Gates and we will all admire them.

---

### #1920 — Amin (Topic Author)
*August 18, 2023, 6:52 AM*

Friends I was thinking of the formula to find densities of sum of two arbitrarily correlated random variables with
possible correlations across higher moments.

If X and Y are two correlated variables and their densities are known, we can use this formula to find the density of
sum (X+Y).

It can also apply to stochastic evolution/differential systems of the form$Y(t+1)\, = \, Y(t) \, + \, \Delta Y$ where
both$ Y(t) $ and$\Delta Y$ are stochastic variables. So we can continue to analytically simulate densities of such
systems over several periods of time.

The formula is very simple.

We just need to find cross moments of all order(up to accuracy required) between two or more random variables whose sum
has to be found.

2nd order cross moments would be $m_{X,Y}$

3rd order cross moments would be $m_{X^2,Y} \, , \, m_{X,Y^2}$

4th order cross moments would be $m_{X^3,Y} \, , \, m_{X^2, Y^2} \, , \, m_{X,Y^3}$

Basically all we need to do is calculate all moments including cross moments up to the degree required for our accuracy
from the data.

And Expand as binomial expansion of various order and then substitute the single moments and cross moments.

$m_{X+Y} \, = \, m_X \, + m_Y \, $

$m_{(X+Y)^2} \, = \, \, m_{X^2} \, +\, 2 \, m_{X,Y} \, + \, m_{Y^2}\, $

$m_{(X+Y)^3} \, = \, \, m_{X^3} \, +\,3 \, m_{X^2,Y} \, + \, 3 \, m_{X,Y^2} \, + \, m_{Y^3}\, $

and so on for all higher moments. It is just simple binomial expansion of various orders. For three variables, it will
be trinomial expansion. We just need to substitute single moments and cross-moments everywhere in binomial expansion.

Later we can convert these moments to densities using our Z-series density construction method.

As I said, we can apply it to dynamic differential stochastic systems of the form
$Y(t+1)\, = \, Y(t) \, + \, \Delta Y(t)$

All we need to find is the cross-moments between$ Y(t) \,$ and$ \, \Delta Y(t)$ . But these cross moments might not be
constant all the time so the method could work only if cross-moments across initial variable$Y(t)$ and noise term
$\Delta Y(t)$ are constant in some sense(only depend on variance and we could model them as moments across standardized
densities or just keep noise density standardized, compute moments and then continue to apply the changing variance and
its required higher order coefficients) or if cross-moments could somehow be computed from data which is actually
difficult for many time series. Usually, we will have to find a smart approximation of cross-moments that is possibly
dynamic.

I think many friends might already have explored the formula but I had not thought of it in terms of cross-moments
earlier.

As an application of the formula, we can use it for finding densities of large portfolios which are sums of large number
of assets and then use them  in efficient frontier optimization with Merkovitz criteria. All we need are cross moments
of all stocks involved which can possibly be calculated.

---

### #1921 — Amin (Topic Author)
*August 18, 2023, 8:25 AM*

Friends, mind control agents continue to give me pain in my heart. My last day was remarkably better and I expected that
torture would decrease. I really do not know why they are doing it again so quickly. May be they want me to write about
it so I lose my credibility that I am feigning this thing.  But mind control agents continue to give me strong pain in
my heart. They take out some neurotransmitter related to vital functions of the body like controlling functions of the
heart and I feel pain after that. There was remarkable relief from gas last night but they have started blocking some
neurotransmitters again and that causes pain in my heart. I want to request good people to please help me in any way you
can.

---

### #1922 — Amin (Topic Author)
*August 18, 2023, 9:52 AM*

Friends, mind control agents repeatedly continue to give me pain in my heart by blocking some vital neurotransmitter
required for proper functioning of the body. Basically it is all about money and the mind control guy who principally
controls me among other people have amassed more than a billion dollars over past 16-17 years. They keep retarding
people with a high hand and blessing of jewish billionaire are on their head. Every year they drug the food in the
entire Lahore city and it requires upwards of 60-100 million dollars to do that. These agents are very shrewd, they keep
75-85% of the money in their pocket and disburse the rest for bribes and operational expenses. But there is no oversight
on money spent and these agents are apple of the eye of the jewish billionaire and people in embassies know that and
make every effort to keep them happy due to their high profile jewish connections and large sums of money involved. When
these agents see the future moeny supply might become dry, they become terribly impatient and do all sort of antics on
victims to show progress and somehow continue mind control. Basically it is a symbiotic relationship between bad rich
jews in US and the mind control agents and each of the party tries its best to keep the other party as happy as they
can. Bad jews and American army are thoroughly determined to continue my mind control. I might try to become extremely
nice to jews, but I am simply hitting my head on a wall and bad jews have a complete unwavering resolve to fail me.

But they continue to give me severe pain in heart again for past thirty minutes.

---

### #1923 — Amin (Topic Author)
*August 18, 2023, 10:03 PM*

Friends, I have ended all research activity for a few days. I am reviewing old material that I had posted on internet
that can be of help for making notes to use when I try to meet and talk to influential and sympathetic Pakistani people
(as I had suggested earlier) during coming week. I will hand over written description of my persecution and all related
supporting material. I want to end this story of mind control drugs every month and then continue uninterrupted research
that I will keep posting on Wilmott. If mind control drugs in injections do not end, I continue to struggle for so many
weeks after the injection only to be able to do good work in final fourth week. I hope that I would be able to do far
more productive work with unbroken chain of thought if I speak to influential pakistani people and my drugs end.
Unfortunately if nobody in Pakistan is on my back, bad jews and American army would again move my father to detain me
for several weeks and try to make sure with stronger medication that  I can never be able to do productive research
again.

---

### #1924 — Amin (Topic Author)
*August 19, 2023, 9:42 AM*

Friends, this was material I was distributing on roads, outside of large newspaper offices, and law firms in UK. I was
looking at old material so decided to distribute it again. It was written in 2010 in UK. I just spoke about pure mind
control and not about experiences with nasty Pakistani psychiatrists.

I am posting some material here that I actively distributed on paper and electronic form when I was in Britain to appeal
to people's humanity and try to expose the truth about my persecution. I always had the thesis that it was religious
persecution but it had everything to do with religion of people persecuting me (because of their religious poison) since
religion of other people was absolutely never an issue for me when I dealt with them. I am posting it after removing the
name of university I attended and any other objectionable thing. I have kept the names of streets where I lived in
London and have not removed them.

I am a legal UK resident but Pakistani citizen who is being persecuted by UK secret services on orders of CIA due to my
religious and national origin coupled with my talent and ability to succeed in financial markets. I have faced brutal,
inhuman persecution by CIA spread over past thirteen years. I have been physically abused, forcefully drugged and put on
mind altering and mind control drugs over past thirteen years in several countries. I have been "forcefully kidnapped
and beaten" several times by state agencies bribed by CIA to intimidate me and stop my research work in Pakistan.
Despite all adversity, I continued my research work in the field of financial derivative securities and made a
successful financial software firm. I am known in mathematical finance community for my research. I would want to
mention that I have faced very serious hardship and continued subjugation and persecution by CIA and I could have been
extremely successful if I had not faced this persecution. You may not be willing to believe but I make the serious claim
that they spent more than a hundred million dollars on my persecution. I would challenge you to verify this if you have
sources in UK secret services. This persecution is spread over America, Japan, Hong Kong, UK and Pakistan.In UK this
activity spread over different cities in UK so it is a national human rights abuse issue not confined to any single
city. I am giving details of persecution and why this is happening. It would be truly abhorring for you to read that
such an activity could ever take place in UK. I have been made a guinea pig for mind control experiments because of my
religious and national affiliations.

I was a student in USA where I studied electrical engineering at (an American) University and economics and mathematical finance at (an American) University. I was very ambitious, worked very hard and really wanted to excel in life.  One of my anti-Muslim professors at (an American University) told CIA about me and CIA circles did not like my zeal about my country and they were desperate to stop me. Since I was a very law-abiding citizen, they could never have done anything against me openly and according to law. So they started using neuro-electromagnetic weapons against me. They gave me drugs in my food systematically to alter my brain. I am a victim of neuro-electromagnetic weapons for a very long time now.Despite being on Voice to Skull, I continued to work and tried to excel. It is a story of human determination and hard work. I am known in mathematical finance community for my research. My SSRN author page is http://ssrn.com/author=435366 where you can look at some of my research papers. Several of my research papers are not in public domain.After several long years of persecution in different countries, I came to UK to set up my financial software firm in London. But in UK, I am again being targeted by neuro-electromagnetic weapons and major problem is that UK secret services are actively cooperating with CIA in my persecution. This is a very serious human rights issue. UK secret Services use special chemicals that go into food of everybody but are totally inert and harmless to people unless ionized by electromagnetic waves. The body of victims of neuro-electromagnetic weapons is kept charged by electromagnetic waves and these chemicals are used to alter the victim's brain. Again these chemicals are mixed in food of everybody to target some specific individuals. This may be hard for gullible people to believe but this is sheer science and utmost effort is made to keep this science secret from public so that nobody ever believes such activities. This makes victims who speak target of ridicule by gullible public. Especially the food stores on Cromwell Street , Earl's Court, Gloucester Street, High Street Kensington, North End road and West Kensington in London are hugely involved in this activity of my persecution though other stores are also a part of it to a lesser extent. This is also happening in areas close to circle line and district line. If you investigate food places in those areas especially or in some other areas of London, you will know the truth for sure. Any honest inquiry can easily bring out the truth. In fact you do not even need an inquiry, if you know some people well who work at food places in these or other adjoining areas in London, simply ask them and they would let you know that drugs are mixed in food of everybody. This is called mercilessly cornering an individual. Victim will have to eat somewhere. Large food chains like Tesco, Sainsbury, M&S Food, and Cooperative Food stores in above mentioned and adjoining areas are also doing it and any "insider" will, for sure, tell you the truth. Even if you do not help to protect me, it will be good for you to know that agencies in your nation are involved in such mean, inhuman and hideous activities to corner, target and alter the brains of some specific individuals. If you work at a food place in London and secret services have approached you to drug the food, I am openly telling you that I am the target. This is happening at a huge scale.Neuro-electromagnetic weapons are weapons used to control, alter or damage the brains using electromagnetic waves, microwaves or ULF waves. The target is given food with chemicals that go into his brain. Some chemicals alter the brain systematically and some other ionize the brain. Different neurons in the brain are mapped for their functions using fast computers. Then the same neurons are stimulated to do the specific job by sending magnetic signals to the brain through electromagnetic waves and start controlling or altering the brain of the victim. American CIA does it very frequently because they have the best technology to deal with it and nobody sees electromagnetic waves passing through air so they always get away with it.In addition to persecution by neuro-electromagnetic weapons, devices are fitted on my computer that transmit data and alter my programs actively to hinder my research and development work. I disabled Bluetooth and wifi on motherboard of my laptop but still was able to see network activity and several suspicious programs running on my computer. Later I noticed that there were more than six hidden users on my laptop that had access to my laptop and had exclusive access to some files and I was unable to delete those DLLs and drivers that transmit data to other devices. I bought that laptop only a week ago and nobody else had used it in my presence. I have been facing persecution for a long time but not being able to run my programs gave me serious problems as that is what I do to earn money.Again I have never committed a crime and in my wildest dreams, do not want to commit any crime or harm to anyone. Why does the law not get me ? Simply because I am a very good human being. My only crime is that I love my country Pakistan and CIA circles want to subjugate our countries forever. CIA people think they are gods and and they can play with anyone so raise your voice against them, please.Since you are an ardent supporter of human rights, I thought I should ask you for help. As Quran says," saving one innocent life is saving all humanity" I would request you to take some action to protect me. I am innocent and am being persecuted by CIA only because I could really excel and would serve my country which many people in CIA circles do not like.I would also be reporting to European Human rights Abuse Tribunal about my persecution. I would request you to come forward and investigate this incident of human rights violations by so called champions of human rights. Here are extremely brief and cursory details of my persecution.

PERSECUTION IN AMERICA WHERE IT STARTED

At the start of 1998, when I was a student at (an American) University, my persecution with neuro-electromagnetic
weapons started. When I became the target, my mind was changed drastically. I would lose the meanings of words. I would
sit in the library for several hours without grasping a single idea. I was stimulated to do things other than my
studies. But I continued to work hard and started to do my financial research again. But CIA started to manipulate me
more and more and some of my professors started to discourage and create problems for my research. I was again given
drugs in my food several times to stop me from working and be able to use neuro- electromagnetic weapons on me and alter
my brain and my research work was disrupted again. Several times I would become very sick after having food but I had no
idea what was happening to me and who was doing it. I contacted officials of my university but they all stubbornly
refused to help me. I want you to understand that it was a very painful time and I have just written very briefly about
it.

PERSECUTION IN PAKISTAN

When times became really tough and I realized that I was facing government persecution and CIA was manipulating me and
altering my brain, I decided to leave America and go to Pakistan. When I reached Pakistan, I suffered from the same
cruelty of CIA dictating other third world nations what to do by generously bribing top officials. About ten people came
to my home and gave me several injections and tied my hands and legs. I lost consciousness for one night. I did not know
what was happening and could not even open my eyes. I had extremely severe shivering for two days and did not know what
was happening. My family was manipulated and took me to a doctor of their choice in Pakistan Army and I was kept in
house arrest with four soldiers of Pakistan Army, on CIA's orders, stopping me from leaving the house and I was locked
in my room every night. This continued for six months. After six months, I got drug induced jaundice because of
over-drugging. I could not sleep for more than two months because of severe itching of jaundice. I had blood marks all
over my body because I could not resist itching. As I mentioned, I was repeatedly beaten by state agencies to intimidate
me. State agencies, on instigation of CIA, repeatedly asked food places to drug my food for neuro-electromagnetic
weapons to be effective. I have been forcefully kidnapped, beaten and drugged several times by state agencies in
Pakistan generously bribed by CIA to intimidate me and stop my research work in Pakistan.I went through extreme torture
over the years. They altered my brain again and again using mind altering drugs. I could not work for several years but
came back with sheer determination to succeed. It was more difficult than can be described. I am giving some examples of
torture I went through. These are just physical symptoms of torture. However true damage to brain cannot be described
easily in terms of any physical problems we suffer. It is far deeper than others are ready to believe. People get
retarded when CIA uses neuro-electromagnetic weapons and damage to intelligence and brain's capabilities cannot be
measured by any physical standard and that is one reason that they use it and get away with it. Some of the following
things happened in Pakistan and other in UK.

Voice to Skull

I am on Voice to Skull torture for more than six years now.

Sleep deprivation

I would be kept awake for several weeks in a row using neuro-electromagnetic weapons. Once this torture lasted for more
than a month.

Pain in bones and skull

They charge the skull, ears, cheekbones and all areas surrounding the brain using EM waves. Sometimes my skull would be
so charged that I would have intense and sheer pain in my forehead, skull, cheekbones and ears. I could not resist but
shout from intense pain. I would prefer death to such torture. Sometimes in my apartment, I would put on aluminium
shield to protect myself from neuro-electromagnetic weapons. I would be asked by Voice to skull to take off the shield.
I would refuse but then they would use directed energy on my head and I would shout with sheer unbearable pain and I
would have to take off the shield. It is hard to describe the intensity of pain in words. There would be large wounds on
my forehead due to this torture and people literally asked me if I had an accident. I can give names of people who
noticed that and asked if I had an accident in London.

one-sidedness

After the torture started, I started to face the following one-sidedness problems due to mind control. This was never
the case before the episode of mind control torture.

1. When I walk my one step is considerably larger than the other.

2. I see differently from both eyes. One eye has decent enough brilliance while the other sees only hazy images of the
world around. I see things meaninglessly without registering any effect on my brain and without keeping anything I see
in my memory.

3. When I raise my hands, one of my hands has a different feeling while the other hand is lifeless and has a different
feeling. Sometimes when I talk half of my tongue resonates differently and the other half of my tongue resonates
differently and One side of my head is always totally numb and feelingless.

GAS IN MY APARTMENT

Sometimes they would release gas in my apartment to charge my body because when we inhale gas, charge starts to get to
the brain. The victim is charged by gas when they fail to drug the food of the victim. It would be almost impossible for
me to breathe due to gas and I would just choke. My saliva would totally became dry. My mouth would start to taste of
something bitter. I would spit with sheer effort after collecting saliva for several minutes, and my saliva would be
dark yellow. Sometimes I would breathe with very serious difficulty due to gas in the air. To counter this, whenever
this could be possible, I would sleep in open or next to window. This was extremely helpful.

blurred vision

They released several chemicals in my brain and it is unbelievable how colours in my eyes change. Sometimes there will
be real but artificial brightness in colours and at other times there will be total dullness. Sometimes, it would be
just blurred vision. At times I would have far-sightedness or near-sightedness. I see at least four different shades of
same red or yellow colour at different times while seeing the same thing. Just changing perception of reality all the
time. Many times, my vision is blurred for several weeks and I could just see vague images of things. For several long
years I did not see colors in my eyes like I did all my life previously. This was because several neurotransmitters were
taken out of my brain.

forced sexual arousal

There were times when I was forcefully sexually aroused. This is the greatest insult to any human being. I would have
forced erection. I do not want to write much about it. But it is total human disgrace and was a quite frequent thing.
Nazis wanted full control over me.

Tongue control

An example of extent of body control using neuro-electromagnetic weapons is something that occurred last year. They
started to give me orders through voice to skull and when I refused to obey they told me that we would teach me a
lesson. My tongue totally came out of my mouth and was held there for fifty minutes. My nostrils would tend to close and
I would have serious difficulty breathing. It is ultimate insult for anyone to have been forced into a situation with
total disgrace before others. Such things are hard for people to believe, but once our food is drugged and their desired
chemicals go into the brain they can have any degree of control on our brain and movements. This is sheer science.

Pain and wounds in the ear

I put compressed cotton in my ears to not let EM waves go through my ears into the brain. It really helps in my
situation. When I remove cotton my eye sight deteriorates dramatically and one side of my head becomes more numb. They
charge cotton to make passage for EM waves. Due to very high charge my ears start to suffer from serious pain and
sometimes there would be wounds on my ear and blood would literally seep through my ears due to high charge. When they
charge cotton with EM waves I literally hear a pulsating sound in my ears.

Gas in Air conditioners:

Several times there was gas in Air Conditioners in my house. Whenever I would go into air conditioned rooms, my voice
would change. Once there was so much gas that I started to feel extremely uneasy. Once, I just rushed out of my room,
went out of my house and started to drive my car. But I had inhaled enough gas. After a bit of driving, I was extremely
dizzy. I stopped driving and parked my car to one side of the road. After a bit I lost almost all consciousness. What
was more disturbing that I really could not see anything at all. Light just went out of my eyes. I just struggled and
there were some drinks on the other seat of my car and I drank one and I was much better and started to see again. After
a bit I had some more food and was better. But painful thing was that such things started to happen every week.

It would be impossible to believe but neuro-electromagnetic weapons are extremely potent and people who do not
experience them just do not know such facts.I have written very briefly. Living under NEM control is extremely painful
and everyday is a torture. I really had to struggle to find the decent success and again it is a story of human
determination and desire to excel that all of us should have.The reality is more horrendous than most of the people
think and are ready to believe in but if victims of persecution do not speak, there will be more and more state
persecutions like it. "

---

### #1925 — Amin (Topic Author)
*August 19, 2023, 5:03 PM*

I want to ask good American friends, who helped me so many times in the past and I was able to avoid detention several
times due to their protests, that I need their help more than ever once again in the near future.

Friends know I am perfectly healthy but for past twenty five years, I have been on psychiatric medication in one form or
other. I get an antipsychotic injection every month but Fluanxol injections in entire Lahore have mind control
chemicals. I continue to remain drowsy for several weeks after the injection and can work only in fourth week. Earlier
there were injections of a specific manufacturing date available in some random stores and those injections had
relatively mild mind control chemicals. I used them for four or five months but those injections are no more available
at any pharmacies and have been sold out throughout the pharmacies of the city. New injections have far more potent mind
control chemicals and it is very difficult to work after getting those injections.

When President Biden had become new president, I was very excited and I had very high hopes that new democratic
president would take some actions to decrease inhuman mind control and, in early 2021, stopped taking injections but my
family detained me with a psychiatrist within a few days and I was kept in detention for more than a month.

Since it is almost impossible to work properly on my research, I have decided to stop taking injections again so that I
can perfectly concentrate on my research. I really want to request good Americans who backed me so many times in the
past to help me again and try to make sure that I am not detained again at flimsy excuses.

I would also be trying to meet several sympathetic and influential Pakistanis for help in my case and hope that it will
also help to avoid impending detention.

Once my injections end, and if I am not detained, I will try to find a position at LUMS or NUST as assistant professor
in mathematics research and hope that I would be able to concentrate fully on my research after that on a long term
basis. I hope that friends would back me for assistant professor position in some good Pakistani university.

Since bad Jews behind my persecution will try their best to move my father to detain me again, I will be posting a lot
of new and old material about my previous psychiatric detentions and psyhiatric abuses during the coming week so people
know the about cruelty with which bad jews force inhuman tactics on good and innocent people in order to fail and retard
them.

Another mild correction for previous post. I have written somewhere that I had wounds on my forehead due to mind control
torture, that is just my bad English. In a state of disconnected brain, I did not choose a proper word. These were not
wounds but deep black marks on the forehead. There was no blood.

---

### #1926 — Amin (Topic Author)
*August 20, 2023, 7:38 AM*

This is a random sample of extreme inhuman animal cruelty of bad jews that they showed me. I am sure they routinely do
such tactics to large number of other innocent and talented people of every religion and creed (of course other than
jews) .When these victims become retarded, they can never properly speak about their rape on the wishes and whims of
malevolent cohort of rich jews. Now I want to tell people that the evil jewish billionaire and his rich cohort will move
every pawn in their hands to detain me again, These inhuman evil jews have no mercy or humanity for non-jews and they
treat them with complete animal cruelty.

I am making this statement about evil cohort of rich jews only. Please do not generalize to other good-natured jews.

Here is a post I made earlier on this forum.

Since many members of this forum have insisted on psychological treatment, I will like to mention many things here today
that I never wrote on this forum ever before. I will try to be very very frank and open. I will not mention names of
psychiatrists but would use random letters for their names. I will leave it to the readers to decide based on their own
knowledge, goodness and degree of humanity whether any human ever deserves to be treated like this.

I would, however, make a two point statement at the start.

1. My family has been acting with malevolence for past sixteen years.

2. Psychiatrists who treated me acted in a very unprofessional way.

I will now state a lot of facts and incidents that actually happened in past sixteen years but I will not speculate
about anybody's motives. I will request the reader to analyze the stated facts on their own and make a decision whether
my assertions are true or not.When I came back to Pakistan from America, in 1999, eight persons came to my uncle's home
in Lahore, tied my hands and legs, gave me several injections and made me drink a thick jelly like liquid in a bowl. I
had not seen any psychiatrist at all when it happened. After I had swallowed the thick liquid, I started to shiver, and
this shivering continued for about 48 hours. I could not sleep at night but I can recall very clearly that I continued
to shiver. The next day, I was taken to a different city Rawalpinidi and I was asked to meet a psychiatrist in CMH
(Pakistan Army's hospital). When I met the psychiatrist, I was in such a weak condition that I had to make a sheer
effort to lift my eyelids. It was very difficult for me to open the eyes. The psychiatrist never really interviewed me
much about what happened and started giving me psychiatric medicine. Though I can clearly recall that time, I had no
mental strength to fluently reason and sy anything about my sanity. Later, I was taken to my sister's home where I was
allowed to go out of the home freely after a few days. I left the home and was walking towards Saddar, and I saw a
Military building mentioning it was GHQ. I Walked in and casually told that I wanted to meet Pervaiz Musharraf who was
army chief. An army car came and took me to a close by army installation and the CO (Commanding Officer) there quizzed
me. I told him everything frankly and told him that I was living with my sister and my brother-in-law was in Army. The
CO called my brother-in-law and he took me home. However my family did not allow me to go out of the home after that.
There was armed guard stationed on the door of my sister's home and would force me to stay inside. My brother-in-law
also told my mother that army had told him that they would ask several intelligence personnel in plain clothes to follow
wherever I would go. I would like to ask the readers this question whether my forced confinement was justified just
because I talked to a CO in army. I think this cannot be easily explained.I was also kept in the hospital for two weeks
and two armed guard stood at the gate only to take care of me and told me that chief has sent us to make sure nobody
gives you any wrong medicine.After a few weeks, I went to my home at Kot Addu where an armed guard remained at the gate
to stop me from leaving the house. The locks of my room were reversed and could be locked from outside and I was locked
every night for six months.I was put on extremely heavy medication and I had drug-induced jaundice after six months. I
was taken to the same psychiatrist who asked for stopping some medication and gave an alternate medication that did not
metabolise through the liver. I was also put on treatment to improve my liver. Jaundice was so extreme that I could not
sleep at night for two months due to severe itching. The doctor for the liver asked my family to really stop all
medication but my sister insisted that I must continue the medication that did not metabolise through the liver.
Jaundice was not getting better until I started getting several glucose drips everyday for more than a month and then
things started getting better. My family promised that they would never give me any drugs ever. I really believed what
they said.I started moving freely in Kot Addu and resumed work on my thesis research. My family did not like my moving
freely very much. I had lived on my own previously all my life in various universities. One day I went to Multan to buy
computer software that I needed for my research. My family did not like that. There was nothing wrong with this and I
said something of the sort that I am not property of my father. My father and brothers snatched all money I had and tied
me to a chair and also tied my legs and beat me. My mother was watching. There was enough noise and our immediate
neighbors also started looking over the wall what was going inside our house. My family continued to suppress me for
many days. I Asked them to let me go but they said that they wanted 50,000 dollars they had spent on my education. I
said that I will pay in a few years but they said that they wanted their money at that time.I left my home after a few
weeks and went to Lahore and started working at a software firm. I was living with a friend. After about a week my
family came to the house I was living and gave me injections forcefully. I had not met a psychiatrist yet. I did see a
psychiatrist next day who briefly interviewed me and said that he could never be my enemy and why would he ever do
anything to hurt me. He put me on some medication. I was taken back to Kot Addu and again started living with my family.
My family was better this time and after a few months, they allowed me to go back to Lahore where I started my thesis
work again. My father gave me three thousand dollars and I went to Hong Kong where I tried to look for a job. I could
not find a job and returned after two months. dot com bubble had burst. After spending only a week in our house at Kot
Addu, my family started saying that you are not "working". You are not doing anything much. (I would like to mention
that my other two brothers never really worked for more than six or seven years but nobody ever objected. When I got
work later in 2003, I supported one of my brothers for more than five years who did not work in this period.) I ate
strictly from our house at that time and did not eat anywhere else. After a week, my family mentioned that they wanted
to take me to a psychiatrist in Rawalpindi. They gave me something in food and I have no memory of more than nine hours
of travel to Rawalpindi. I also cannot recall anything I said to psychiatrist M. This is horrifying to this day since I
vividly remember taking food before the journey and later getting into the car. I can recall almost every significant
moment of my life but I do not know what happened there and I just recall that when I woke up I was lying on a bed at
the psychiatrist M's facility and my memory restarted. I can recall everything after that. I have no memory whatsoever
of being interviewed by Psychiatrist M. I was so week that many time I would defecate on the bed and hospital staff
would have to wash my bed. Anything like this never happened all my life before. Every second or third day, I would be
taken to a different room where they would place a wood piece between my jaws and give me anesthesia. I did not know
anything about what they did. Somebody later told me after a few months that they gave me electric shocks. Doctor never
discussed any thing about it or told me what he was doing. I used to ask my mother I was perfectly fine and nothing of
the sort was ever needed but my family continued to force medication. I was allowed to go home with very heavy
medication and continued to visit Doctor M after every two weeks. Doctor M never talked to me about any psychiatric
problems. He would put a headphone like device with wire winded on it and would ask my mother,"How is your son." Doctor
M kept me on heavy medication for more than three years. I was always told that you were not taking interest in your
work and that is why you needed to be treated and this treatment lasted for three years. It was very difficult for me to
work on my thesis on such heavy medication but I slowly continued since I had done most work before I had left for Hong
Kong. When my medication decreased, I could work better. My thesis was very good and author of a mathematical finance
book had asked me that he would make me co-author if I could contribute my programs and code for his book. I did give
some code for free and it was published in a book. I also made a website Libor Market Model web where some free code was
given for download. There were more than ten unique visits to that web site per day for many years and a lot of people
downloaded code and papers by others and my thesis. This started in year 2002.I found a job with a Japanese company from
Pakistan since they liked my work and asked me to write professional programs for derivative pricing and hedging. I
moved to Lahore again form Kot Addu and rented a good sized apartment and continued to work. Slowly my family also
started moving to my apartment. My work was going very well but my family started to insist again that I needed to see a
psychiatrist. My brother, my father and my mother had already shifted to that apartment. One morning when I woke up,
four people entered my room and asked that I had to visit a psychiatrist with them. In the facility, I was given an
injection, my medication started and the psychiatrist S saw me after two days. Psychiatrist put me on heavy medication
again despite that I was getting a very good salary and my reasoning was perfectly normal. I do not know why so heavy
medication was needed. Doctor S continue to give me some drugs without my knowledge and without discussing with me.
Doctor S would give me some drugs in a glucose drip every two/three days in operation theater. When I would be given the
glucose drip, my blood pressure would start to fall and when half of the drip bottle would have gone into my blood, I
would literally be unconscious and I would wake up several hours later in my room. I would shudder from fear as the day
of this treatment would come closer and continued to beg psychiatrist S to stop this treatment. He said we are giving
you vitamins and vitamins are always harmless. He insisted that vitamins had to be given to me. He never told me what
drugs he gave me that made me unconscious and never discussed it with me other than mentioning vitamins.My company asked
me to come to Tokyo and did the necessary paperwork but I resigned and decided to go back to Pakistan after a month. I
came back to our house in Kot Addu where my father, mother and another guy gave me an injection, I fainted and I woke up
at the basement of Doctor S's facility in Lahore. I continued to work and made some new models and when the company in
Tokyo came to know about my new models, they asked me to start working with them again from Pakistan like I did before.
Meanwhile Doctor S continued to give me very heavy medication. I started to get a salary of more than 5500 dollars per
month and supported my mother and brother again and I incurred all their expenses. My father also borrowed more than
sixty thousand dollars from me. I continued to ask Doctor S that my work was going well, and I was doing everything very
sensibly so he should decrease the medication but he refused. I was earning handsome money and I decided to leave my
family and go to Karachi. I drove to Karachi on my car. On arrival in Karachi my ATM card was disabled. I did have the
check books with me so I continued to withdraw money. Police seriously harassed me in Karachi and After about three
days, a police van stopped me and asked me to drive to Clifton police station where police blamed that my car, actually
bought with my own money, was stolen. They forced me in a locker and a Police inspector slapped me violently several
times. After several hours three navy jeeps came to police station and I was taken to a navy walled compound where I was
locked again in a cellar for the night without any food or water. In the morning, I was taken outside and Four
injections were forced on me by the intelligence personnel. I was forcefully sent back to Lahore with Doctor S where I
remained in forced confinement for more than six months where drugs were forced on me and two injections were given
daily.I would now digress to tell something about my early life and family. I went to one of the best boarding high
schools in Pakistan where acceptance rate was one boy out of a hundred applicants at that time. We had four exams every
year. Throughout my school life, I was among first four boys except only two times. My brothers also went to the same
school but one of them was asked to leave due to academic problems after two years. The other brother managed to pass.
My both brothers never worked. One of them started working with my father but they always fought. The other started
working abroad only two years ago(2013). One of my married brothers who worked with my father had a fight with my father
(2009). My father called me and asked me to pay no money to my brother. Two weeks later I heard the news that my brother
had died. His body was brought to Lahore. I do not know about any poisons but I noticed that some people were talking
strange about early death and poison. I also heard one of my sister say that he had taken poison. I was told he had a
heart attack at 34 and most people did not believe. My brother was very aggressive and would take two knives, one in
each hand and would walk in the house. This was when I was forced to live in Kot Addu. Everybody would lock in his room.
I told my parents several time that if anybody needed treatment, it was my brother but my parents would laugh away.
Whenever there was any fight in my family house, I would simply leave the house because I never liked or wanted to
participate in their fights or loud arguments. I told my family several times that my brother needed some help but they
never cared. He got divorced and left a daughter behind. He suicided. I wish my family had heeded my requests to treat
him. When my brother died, I argued with my family that I am perfectly sane and I must be allowed to live a life without
medication. My family agreed but said that they would give me drugs for six more months. My sister asked Dr. S to
increase the number of injections from two per month to three per month. After six months, my family said that I must
see another psychiatrist. My work was going very well. I was earning money. I Was paying for my mother and other
brother's all expenses but they still wanted to continue drugging me. I was taken to psychiatrist R in Rawalpindi.
Psychiatrist R gave me extreme medication and I would sleep for thirteen hours everyday. I argued with the doctor that I
Was perfectly fine and these drugs do not let me work well and I remain mentally suppressed due to their effect but he
continued. He said that I had good schizophrenia that I could work normally and make a handsome income (8500 dollars per
month) and I could think rationally but I still had to be treated. He said that he had never come across a case of good
schizophrenia before all his life.When I came back to Karachi from London, I wanted to live in Karachi and wanted to
rented a house. I continued to call to my family two to three time everyday. My brother-in-law and his friends called me
and posed as brokers interested in arranging housing for me over the phone and asked me to come to a thinly populated
area. I asked the taxi driver to reach the place they mentioned. My brother-in-law started forcing me to go with him. I
continued to ask him that we could talk and settle everything nicely but he was belligerent. They forced me off me feet
on the road and tied both my hands and legs. He wanted to blindfold me in the car by putting a cover on my head but I
forced my head against the roof of the car(my hands and legs were tied) and he could not blindfold me. They took me to a
house in DHA Karachi and locked the main gate. Some people continued to come and go from the smaller gate. They gave me
some injections and I would fall asleep. I would doze for about half an hour to hour and when I would wake up they would
give me some other injection. One of the people there asked if I wanted them to arrange a dance party at night. In the
afternoon they gave me some food to eat. While I was eating, a woman I never knew and never had seen before and all her
breasts were exposed came and started eating in the same plate I was eating. I continued to answer what she said but did
not do anything at all. They continued to give me injections and in the evening they gave me a final injection and I
woke up at a psychiatrist's facility next day. Attendants at the hospital gave me an underwear and asked me to change my
underwear. I was wearing two underwears. I removed one of the two underwears and wore their underwear(sorry for not
using any other word) and came out of the bathroom. The attendants gave me several blows and said that I was trying to
be smart with them. Doctor I did not interview me for several days and my heavy medication started again. I was
threatened to comply. One of the other patients told me that some people took me out of my room unconscious at night and
brought me back in the morning. I told Doctor I to make sure that nobody enters my room when I am sleeping but Doctor I
would say that nobody would enter my room. I noticed that people continued to enter my room at night when I Was
sleeping. After a lot of those incidents and protests, Doctor I changed his line and said that we really have to enter
your room at night because of your safety. Doctor I kept me in his facility for more than nine months. He said that he
would let me go out only if I live with my family in Lahore otherwise he will continue to detain me for possibly several
years. I had to live with drug addicts and in a very very unprofessional environment. He allowed me to leave after about
a year when I knew that there was no other way but to live with my family in Lahore.

I went to Hong Kong on September 10, 2000 where I tried to look for a job. I could not find a job and returned on
December 03, 2000. When I was in Hong Kong, I still recall that food at several restaurants and fast food places was
drugged with mind control chemicals. I do not have my old records about it but I remember that I visited South China
Morning Post about and talked to one of the newspaper staff about chemicals in food that would alter the brain right
after I would eat the food. At that time, I did not know anything about mind control but I knew that several times my
consciousness would strongly decrease after I would take food.

Psychiatric Abuse by Dr. Malik Mubashir.

 After spending only a week in our house at Kot Addu, my family started saying that you are not "working". You are not
doing anything much. (I would like to mention that my other two brothers never really worked for more than six or seven
years but nobody ever objected). I ate strictly from our house at that time and did not eat anywhere else. After a week,
my family mentioned that they wanted to take me to a psychiatrist in Rawalpindi. They gave me something in food and I
have no memory of more than nine hours of travel to Rawalpindi. I also cannot recall anything I said to psychiatrist M.
This is horrifying to this day since I vividly remember taking food before the journey and later getting into the car. I
can recall almost every significant moment of my life but I do not know what happened there and I just recall that when
I woke up I was lying on a bed at the psychiatrist M’s facility and my memory restarted. I can recall everything after
that. I have no memory whatsoever of being interviewed by Psychiatrist M.

I was given electric shocks by Dr. M at the start of treatment without even interviewing me. I believe that electric
shocks must not be given to any human being and even if they could ever be justified, it would be possible only after
all chemicals means had failed. But dishonesty of the doctor becomes obvious because he did not even interview me at the
start of the treatment and when I regained consciousness after losing it while boarding my father’s car in Kot Addu, I
was already on the hospital bed in an extremely weak condition.

I was so week that many time I would defecate on the bed and hospital staff would have to wash my bed. Anything like
this never happened all my life before. Every second or third day I would be taken to operation theatre and I still
vividly recall that they would place a wooden wedge between the teeth so that I would not cut my own tongue between the
teeth when they would give electric shocks and then they would give me anesthesia and I would feel my body getting numb
from lower to upper side with the blood flow within about a second. Many times I would defecate on the bed and the bed
would be washed by the hospital staff.

Doctor never discussed anything about it or told me what he was doing. I used to ask my mother I was perfectly fine and
nothing of the sort was ever needed but my family continued to force medication. I was allowed to go home with very
heavy medication after two weeks of detention and electric shocks and I continued to visit Doctor M after every two
weeks. Doctor M never talked to me about any psychiatric problems. He would put a headphone like device with wire winded
on it and would ask my mother, "How is your son." Doctor M kept me on heavy medication for three years. I was always
told that you were not taking interest in your work and that is why you needed to be treated and this treatment lasted
for three years.

When I left United States, I had completed my course work but I still had to complete my thesis. It was very difficult
for me to work on my thesis on such heavy medication but I slowly continued since I had done most work before I had left
for Hong Kong. When my medication decreased, I could work better. My thesis was very good and author of a mathematical
finance book had asked me that he would make me co-author if I could contribute my programs and code for his book. I did
give some code for free and it was published in his book. I also made a website Libor Market Model web where some free
code was given for download. There were more than ten unique visits to that web site per day for many years and a lot of
people downloaded code and papers by others and my thesis. This started in year 2002.

There is a post # 324 with reference to dishonest psychiatry by Dr. M written on April 20th, 2015, 10:37 am, https://forum.wilmott.com/viewtopic.php?f=15&t=94796&start=315#p748658

After I completed my thesis and while I was still in Kot Addu, I found a job with a Tokyo based Japanese company, Up
Front Inc., from Pakistan since they liked my work and asked me to write professional programs for derivative pricing
and hedging. It was my first job. I moved to Lahore again form Kot Addu and rented a good sized apartment and continued
to work. I would talk to my employer regularly and discuss various aspects of the computational programs I developed.

Slowly my family also started moving to my apartment.

My work was going very well but my family started to insist again that I needed to see a psychiatrist. My brother, my
father and my mother had already shifted to that apartment.

Once day my father who was already living in my apartment asked me to talk to him in the living room in my apartment
right in front of the air-conditioner.  I was having conversation with him but there was so much gas in the air that I
started to feel extremely uneasy. I left the conversation and just rushed out of my apartment and started to drive my
car that was parked outside. But I had inhaled enough gas. After less than a minute of driving, I was extremely dizzy. I
stopped driving and parked my car to one side of the road. After a bit I lost almost all consciousness. What was more
disturbing that I could not see anything. Light just went out of my eyes. I just struggled but I had enough
consciousness as probably some parts in my brain retained enough function and I extended my hands to the side-seat where
there was a sweet drink and put it to my mouth and after a few minutes I was better and started to see again and
regained some consciousness. After a bit I had some more food and I felt better. Though I became quite well after some
time, I was very frightened to go back to my apartment and I decided to drive to Islamabad so that I could be away from
my family and from the gases in my apartment.

I remained in Islamabad for only two days and my family assured me on phone that they would be very nice so I decided to
return to Lahore. I was driving back to Lahore when my sister called me and asked me to pay her a visit on the way back
to Lahore as her husband who was in army was stationed in a city close to GT Road. I decided to go to stay in my
sister’s home for one night on the way back to Lahore. My stay in my sister’s home was quite good but in the morning
they gave me some food drugged with mind control chemicals. Still everything was good and I left my sister’s house to
drive towards Lahore again. I had just driven a few miles out of the city when my nostrils would tend to close and I
would have serious difficulty breathing. I was totally aghast what was happening but nothing would help. I was able to
call my brother-in-law to tell him that I was a few miles from the city and needed help. My condition continued to
worsen and my tongue totally came out of my mouth and I simply could not force my tongue back into my mouth. My
brother-in-law reached there after twenty minutes and my tongue was still completely held outside my mouth. He asked me
to sit in his jeep and drove me back to his home and my tongue was still completely forced outside of my mouth. After
about twenty minutes in their home, my brother-in-law gave me a pill and my tongue became normal and went inside my
mouth.

Something like this had never happened all my life before. I never had any mild fit all my life. When mind control
chemicals are mixed in food, brain and body of the victim can be altered in many extreme ways. It is ultimate insult for
any human being to have been forced into a situation with total disgrace before others. Such things are hard for people
to believe, but once our food is drugged and their desired chemicals go into the brain they can have any degree of
control on our brain and movements. This is sheer science though people who do not experience such things just do not
know easily believe such facts.

Though I had become better, my brother-in-law called my father and asked him to come to his house to take me back to
Lahore.

There used to be some strong gas in air-conditioners in my apartment and I clearly recall that my mental state will
alter when I would be exposed to the air coming out of the air-conditioners. I would perfectly maintain my sanity and
logic but some of the other things like sound of my voice would alter all of a sudden as soon as I would be exposed to
air coming out of the air-conditioners.

---

### #1927 — Amin (Topic Author)
*August 20, 2023, 11:59 AM*

Friends, I must start by saying that most jewish souls are very nice human beings and we must regard good people around
us with great regard and respect.

But evil jewish billionaire and his rich cohort are exactly the opposite. This ungrateful billionaire does not realize
that he had earned great money because he does his business in United States. This ungrateful guy also does not realize
that Americans give extreme respect to jews. From my personal account, when I posted stories of my cruel treatment more
than ten years ago, many Americans told me that Jews are extremely good people and I must be an anti-semite making up
stuff to hurt jews who are so good(Indeed many of them are).

But this ungrateful asshole has already retarded tens of thousands of white American born intelligent people already.
Several thousands of intelligent American born programmers and others are working in his companies as "forced labour".
These intelligent people are threatened to keep working in his and his rich cohort's companies because they know if they
leave or resign, American puppet army would put them on mind control on wishes of the evil jewish billionaire and his
cohort.

If mind control coercion ends in United States, large number of intelligent forced labour will leave the companies of
jewish billionaire and his rich cohort en masse.

So this is how evil jewish billionaire and his rich cohort are repaying good people of America.

Even some good jews have symapathies with their evil jewish Godfather. Therefore even many good jews say that thousands
of people retarded on whims of evil jewish Godfather and his cohort must not be freed from extreme cruelty of mind
control. If you are a good human being, either you side with good or evil (depending upon if you are good or bad)
regardless of religion of anyone involved.

I was reading history of Ukraine as this has come to limelight in Ukraine war, how the region continued to switch hands
and was ruled by one foreign power after the other.  (This is from my weak memory and some figures might be off) I read
that during a period of 40-50 years polish ruled Ukraine and they appointed jews to collect revenue and run affairs of
the region. Jews were extremely cruel to Ukrainian people and collected revenue with such extreme cruelty that there was
widespread hatred among ukranians about jews. Jews had no sympathy or compassion for poor Ukranians. When polish rule
ended, ukrainians killed jews en masse at many places because of the cruelty with which they had been treated during
polish rule. By no means I am implying that killing jews was a right thing. I am just saying that there was a cause and
effect of Jews own doing.

Even though I apologized about my statement about rich Jews machinating in Germany due to lack of my knowledge about the
issue. But I am inclined to think because of the cruel behavior of the ungrateful jewish billionaire towards many
innocent Americans (who have been put on mind control due to his whims) and also due to the incident from Ukraine, that
there must be some cause and effect of doing of some bad rich jews which evoked general hatred among German people and
millions of innocent jewish souls had to give their life in one of the greatest human tragedy of holocaust. Nobody ever
wants to wrong even a stray dog let alone gas millions of people without some underlying cause and effect. Hitler was
better with many other supposedly "inferior people" as compared to his behavior with jews.

Since I continue to expose bad jews, they are determined to keep me under psychiatric coercion and they are thoroughly
resolute to detain me again. If good friends did not help me strongly, my future might be doomed forever.

Again I have said many things about bad jews therefore I want to iterate that your good jewish friends(who are good
humans) are great assets, please give them the same regard and respect they deserve. World should ideally be religion
blind among good people. But please ask your jewish friends to make sure that they staunchly opposed the great cruelty
that has been unleashed by the evil jewish billionaire and his rich cohort and everyone under mind control and threat of
mind control must be freed. It is simply animal cruelty that no civilized society can ever allow.

---

### #1928 — Amin (Topic Author)
*August 21, 2023, 12:15 PM*

Friends, it was a busy day today. I had decided to visit a few prominent lawyers for help. Around noon, I want to Latif
Khosa's office on 1 Turner Road, Mozang in Lahore. Unfortunately Latif Khosa had gone to Islamabad and was not in his
office. There was another junior lawyer who was not willing to listen much but was interested that he wanted to take my
case. I took my time to briefly describe everything and the accountant was an extremely nice guy and told me that he
would forward all the material and information to Latif Khosa who would be in office on wednesday evening and they might
possibly call me for further information.

Then I went to Aitezaz Ahsan's office. But he was also not in the office. Another person Aftab Alam met me there but he
was extremely lukewarm and told me he could not help me in any way. I just told him to forward all the material and
information to Aitezaz Ahsan.

Then I went to meet Saad Rasool who is a fellow abdalian from my boarding school and is a very prominent lawyer and runs
his own law firm. He is also an LLM from Harvard.  When I reached his office, they told me that Saad Rasool is mostly in
Islamabad but another junior lawyer Ali Ahmad very patiently listened to all my information and told me that he could
tell me in a few days if he could help me.

Though The lawyer at SR Law very patiently listened to me, but in general I am very sure that Pakistan army and
intelligence moves rich connections to give totally false information to lawyers and asks them to completely not
cooperate with me. American Army has well trained Pakistan army in systematic lies, trickery and deception when they
introduced mind control in Pakistan.

Because army continues to move their connections to persuade the lawyers with false information to not cooperate with
me, I will request good American people to ask their Pakistani connections to persuade some of these lawyers to
cooperate with me. Specially Saad Rasool is a Harvard graduate, if some good people from his almamater could ask him to
help me in my difficult situation, I am sure he will understand and help me. If good people help me at this stage, I am
sure I will be able to restart my life and start doing my research without any injections possibly at Lums if they
accept me as Assistant professor.

I will also be sending resumes to a few prominent people in Maths Department at Lums on Wednesday and ask them to help
me find assistant professor position. Again I will need help from friends at prominent institutions and good places who
liked my research in the past to help me become assistant professor at LUMS.

I hope with help from good friends, I will be able to leave this period of turmoil in my life and continue to do
research in mathematics with a stable coarse in life.

---

### #1929 — Amin (Topic Author)
*August 22, 2023, 7:46 PM*

Friends, I was able to put together following description of my research work over past few years. I will be making
minor additions and email them to various LUMS faculty in Maths and Computer Science for help in finding an Assistant
professor position in Maths department. I did a lot more intermediate research work that led to following major research
discoveries but I want to mostly omit the intermediate research work in this description. I will add something about
analytic simulation of densities of SDEs without any random numbers.

**Extension of Classic Regression model with the discovery of Orthogonal Hermite Polynomial Regression Model**

** **

Briefly, I was able to come up with an extension of linear regression model first discovered in Mathematics by Gauss.
The classic linear regression model is analogous to use of only one first hermite polynomial. I was able to extend it
from first hermite polynomial to arbitrary order of hermite polynomials depending upon the complexity of density of
underlying random variables involved in regression. This hermite polynomial series regression model works extremely well
in high dimensions and mostly far outclasses the regression curve fitting models based on artificial intelligence and
machine learning.

Here is history of progress in this research.

First I discovered a new method to represent random variables by a series in Hermite polynomials. This is alternatively
called Z-series in my research.

 Later I applied the above method to  a monte carlo simulation of system of correlate SDEs and found the Z-series representation of the asset density from moments of asset calculated in monte carlo. Posts 1685, 1686 and 1688:  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1680#p874055

 This monte carlo program led me to think about calculating correlations between orthogonal hermite polynomials of same degree across two correlated variables. I calculated correlations beteween hermite polynomials of same order between two correlated variables in monte carlo setting in a matlab program in this post 1691 and 1693: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1680#p874075

 This further led me to thinking that prevalent classic method of calculation of pearson correlation between two random
variables was highly suboptimal when the densities of the variables are non-gaussian. It was optimal only for perfectly
gaussian random variables. In general, the greater the deviation from gaussianity in two random variables, the more
suboptimal the classic calculation of pearson correlation would become. I found in my research that a proper way to
calculate correlations between two non-gaussian random variables was to represent the random variables as series in
hermite orthogonal polynomials and then find correlations independently between hermite polynomials of the same order
across two variables. This discovery means that most of the classic models and numerical methods in stochastics and time
series that are based on proper calculation of correlations or covariances between two or more random variables have to
be properly altered by replacing one gross estimate of Pearson correlation by multiple estimates of correlations between
hermite polynomials of the same order across two variables when the random variables under consideration are
non-gaussian.

 The observation that pearson correlations have to be calculated independently for each hermite polynomial  led to a new
ground breaking concept  of analytic hermite polynomial regression of non-gaussian dependent variable on between two or
more explanatory non-gaussian variables. This orthogonal regression breaks down every non-gaussian random variable into
a series in hermite polynomials and then hermite polynomials of dependent variable of every order are regressed
simultaneously on hermite polynomials of same order of multiple explanatory variables and this depends upon their
indpendent pearson correlations between hermite polynomials of each order. Then results from various orthogonal hermite
polynomial regressions is added to give high dimensional curved surfaces with smooth derivatives that make a fit to the
regression data.

Please note that Hermite orthogonal regression I am referring to is a very new discovery that I recently made in Feb
2023 and it is different, far better and unrelated to another classic method known by the name of hermite polynomial
regression which has been known for decades. This new method of hermite orthogonal regression is mostly far better than
most AI and machine learning regresssion methods that fit a curve to data.  As opposed to functional regression, our new
orthogonal hermite polynomial regression method depends on correlations between hermite polynomials. While classic
regression that depends upon correlations between first hermite polynomial our new method is a generalization of classic
first hermite polynomial regression to a new method of regression that depends upon correlations between multiple
orthogonal hermite polynomials of same order across different variables.

 Below I show three graphs of hermite orthogonal regressions that try to explain Apple Stock returns VS Microsoft and
Nvidia Stock returns. All three graphs use only nine data observations over non-overlapping periods.

[![Image](32x32)](https://postimg.cc/JtDs5n08)

![Image](624x304)[![Image](32x32)](https://postimg.cc/JGjtS2jd)

[![Image](32x32)](https://postimg.cc/kVGJM1tC)

![Image](624x304)

![Image](624x304)

 The next three posts 1791, 1792 and 1793 describe calculation of correlations, covariances and regressions between
non-gaussian random variables when their Z-series representation is given.

  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1770#p875136

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1785#p875153

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1785#p875155

 Particularly the last post analytically explains the concept of regression between two Z-series random variables.

 Please also read posts 1731, 1732 and 1734 for hermite polynomial correlations and regressions:

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1710#p874492

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1725#p874542

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1725#p874578

 Here I distributed program for doing multivariate hermite regression in post 1722: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1710#p874497

 I presented results of one dimensional hermite regression in post 1705 here: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1680#p874075

 The hermite regression program is given in post 1706 here: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1695#p874270

 I also learnt that in order to do robust hermite orthogonal regressions, we needed to apply positivity condition of the derivatives of the density. Here I have described the positivity condition for derivatives of the density in post 1719: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1710#p874464

 After proper application of positivity condition, hermite regressions worked in an excellent fashion. I showed some results here in post 1721: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1710#p874492

 Please read posts 1783 and 1784 for calculation of variance of sum of two non-gaussian random variables when their
hermite polynomials have correlations

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1770#p875135

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1770#p875136

 Please disregard post 1785 and 1785, they have some errors.

 A Z-series option pricing formula is given in post 1830 here: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1815#p875619

 **Analytic Solution to Initial Value problems of first and higher order ODEs and systems of ODEs.**

I presented a new analytic series solution to ordinary differential equations that applies to almost all first order
ODEs, arbitrary higher order ODEs and systems of arbitrary order ODEs. It only may not apply to singular or degenerate
ODES.

 You can read all about my work here: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598

 Interestingly, I used the same basic ideas for solution of ODEs and SDEs. The common original idea involves taking
iterated integrals of higher derivatives and then solve for stochastic integrals (in case of SDEs) and deterministic
integrals (in case of ODEs). These integrals can easily be solved since their integrand is a constant value evaluated at
initial time.

Please read here for a very intuitive description of the new method I applied to solve both ordinary differential
equations and Stochastic differential equations.

[https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1605#p873297](https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1605%23p873297)

**Higher Order Accurate Monte Carlo simulation of Stochastic Differential Equations.**

Higher order simulations of stochastic differential equations was a longstanding problem in stochastics and mathematical
finance. Luckily, I was able to discover analytic solution to higher order simulation of SDEs. It was one of my first
breaks in research in Mathematics.

 In order to simulate an SDE with variable drift terms and variable volatility term, we apply Ito formula on variable
drift and variable volatility terms and find  an equivalent expression for each of the variable terms comprising a
stochastic integral with constant integrand first term evaluated at initial value and several variable integrand terms
under iterated stochastic integrals. We again apply Ito formula on variable integrand terms under the stochastic
integral sign to convert them into constant integrand terms evaluated at initial values and further variable integrand
terms under higher order iterated integrals. After N repeated application of the above procedure, we obtain an Nth order
discretization of the SDE  comprising a large number of constant integrand terms evaluated at initial values and we also
get some N+1 order terms with variable integrands under the iterated integrals. We can easily evaluate the all the
constant integrand terms up to order N under iterated stochastic integral signs and neglect the rest N+1 order variable
integrand  terms. All the constant integrand stochastic integrals can be analytically solved using hermite polynomials.
This process can be repeatedly carried out to achieve high degree of accuracy in monte carlo simulations of the SDEs.
Since number of terms involved in higher order expansions increases very fast and cannot be easily done with hand, I
distributed an algorithm coded in matlab that calculated all the stochastic integrals and their coefficients from
constant integrand terms involved and these coefficients are later used in higher order simulations of  Stochastic
differential equations.

 In post 37 below, I described how to apply Ito change of variable formula on drift and volatility terms of the SDE and
then substitute them in the original integral representation of the SDE. I also explained how to repeatedly apply the
Ito Change of variable formula on variable integrand terms for higher order simulation of the SDEs. This post 37 was
written on Monday, May 02, 2016 1:43 pm. I think due to forum adjustments, proper formatting of this post is lost but
you can still properly read the equations in which Ito change of variable formula is repeatedly applied.

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=30#p782234

 I later stopped working on SDEs and applied the same idea on solution of ODEs. I started working on SDEs again after
quite some time and then wrote another post describing how to expand the integral solution of an SDE to higher order by
repeatedly applying Ito Change of variable formula. This post 564 is similar to post 37. Post 564 was written on Thu Nov
23, 2017 10:48 am.

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=555#p816432

 When I wrote the above post, I had only successfully expanded the SDE into constant integrand iterated stochastic
integrals but I still had not given the proper analytic formulas for the solution of iterated stochastic integrals.

 I was only able to solve for various iterated stochastic integrals whose integrands were constant values evaluated at
initial starting time. I wrote this post 690 written on Thu May 10, 2018 10:38 pm where I gave analytic expressions for
solution of stochastic integrals

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=675#p827224

 One day later I, latexed the formulas given in post 690 and wrote them again. This was done in post 693 written on Fri
May 11, 2018 6:08 pm

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=690#p827246

 Here in post 736, I presented a program based on above research that would evolve density of an SDE without pseudo
random numbers using a non-branching tree for underlying normal driving density. This program would automatically do
repeated Taylor expansions of SDEs with two drift terms and one volatility term and would also automatically solve for
all stochastic integrals involved. This program had exact behaviour for one evolution/simulation  step of the
non-branching tree but its multi-step behaviour with deterministic non-branching tree was flawed . As it turns out when
we simulate with pseudo-random numbers, if the SDE does not have explicit dependence on time, we always simulate the SDE
at the start of interval as if we are starting from time zero. So while multi-step simulation algorithm was not good for
analytic non-branching density tree, its one-step version was perfect, precise and ideal for Monte Carlo simulations
with pseudo-random numbers. However, it was only a few weeks later, when I started using the one step simulation scheme
in monte carlo simulations. Again the algorithm and its explanation were given in post 736 written on Mon Jul 02, 2018
10:56 am here.

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=735#p830547

It was the algorithm in above post that a lot of friends copied from my thread and distributed around. It would
discretize for any arbitrary SDE with two drift terms and one volatility term without explicit time dependence in the
SDE.

 I later used the algorithm given in post # 736 for monte carlo simulations for the first time in a matlab program
distributed in post # 773, written on Sun Nov 04, 2018 6:34 pm given here

 https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=765#p837313

 In the above post, I simulated both bessel process version of the SDE and original coordinates version of the SDE with
monte carlo simulations employing pseudo random numbers.

 Here in post 891, I presented the same monte carlo simulation algorithm but all the binomial loops have been removed
and all the various integrand terms are directly written as a summation. It is the same monte carlo algorithm as old but
all the terms in expansion are written directly without any looping. Here is the link to post  891  written on Sat Mar
14, 2020 5:54 pm

 https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=885#p855539

Here is posts 892 and 893, I have earlier collected all my posts written about monte carlo simulations and associated
matlab programs.

 Post 892:

 https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=885#p855649

Post 893:

 https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=885#p855653

 Here in post 1172 and 1173, I presented ideas about expansion of high dimensional monte carlo simulations like we have
for interest rate derivatives and equity baskets.

 Post 1172:

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1170#p866762

Post 1173:

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1170#p866774

Here in post 1213, I have presented a higher order monte carlo program for very general system of correlated system of
asset and SV SDEs.

Here is the address of post 1213 :  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1200#p867829

**Z-Series/Hermite Orthogonal Polynomial Series Expressions And Construction of Analytic Densities of Random variables
from their first four to Eight Moments.**

** **

It was a long standing problem in probability theory how to find the analytic expression for the densities of random
variables when their first few moments are given. Though there had been quite some research on the problem, and
solutions like Gram-Charlier and Edgeworth series and many related solutions existed, there was not any perfectly good
solution to the problem. I came up with a numerical algorithm to convert the moments of arbitrary random variables into
an analytic expansion in Z-series or alternatively a series in hermite polynomials. It was due to this research, that I
was later able to extend the linear regression model with hermite polynomial regressions about which I have described
earlier.

There are some random variables for which the method does not work, but those cases have to be similarly expanded in
terms of a series in other appropriate orthogonal polynomials like Legendre, Chebyshev or others.

 This method generates densities of random variables so that first eight moments of the density perfectly match with
first eight moments input to the method. Mostly the match of the densities is precisely perfect. In this method, we find
coefficients of Z-series or Hermite orthogonal Polynomial series so that moments of resulting density precisely match
the input moments. Though Edgeworth and Gram-Charlier like methods have been very useful, this new method is a very
significant improvement upon classic methods of construction of densities when moments are given.

 Here I distributed a program that finds Z-series representation of a random variable when first eight moments of the random variable are input to the program. It is in post1653:  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1650#p873803

Please also read post 1662 where I have written a small program that anlytically constructs generalized gamma density. The first eight moments of generalized gamma density are input to our Z-series density construction program. As it turns out, when graphed on the same axes, our newly constructed Z-series density is indistinguishable from analytic graph of generalized gamma density. Post 1662:  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1650#p873846

**Calibration, Simulation and Hedging in a Heston Libor Market Model with Stochastic Basis**

My research paper titled, “Calibration, Simulation and Hedging in a Heston Libor Market Model with Stochastic Basis” was an invited publication in a prestigious Risk book “Interest Rate Modelling after the Financial Crisis.” Here is the link to Risk book web site:  [http://riskbooks.com/interest-rate-mode ... ial-crisis](http://riskbooks.com/interest-rate-modelling-after-the-financial-crisis)

---

### #1930 — Amin (Topic Author)
*August 23, 2023, 9:03 AM*

Friends, I rewrote the description of my research as a word document and in next hour, I will be mailing it to
professors in LUMS in Math and CS department.

**Description of My Research**

** **

**Extension of Classic Regression model with the discovery of Orthogonal Hermite Polynomial Regression Model**

** **

Briefly, I was able to come up with an extension of linear regression model first discovered in Mathematics by Gauss.
The classic linear regression model is analogous to use of only one first hermite polynomial. I was able to extend it
from first hermite polynomial to arbitrary order of hermite polynomials depending upon the complexity of density of
underlying random variables involved in regression. This hermite polynomial series regression model works extremely well
in high dimensions and mostly far outclasses the regression curve fitting models based on artificial intelligence and
machine learning.

Here is history of progress in this research.

First I discovered a new method to represent random variables by a series in Hermite polynomials. This is alternatively
called Z-series in my research.

 Later I applied the above method to  a monte carlo simulation of system of correlate SDEs and found the Z-series representation of the asset density from moments of asset calculated in monte carlo. Posts 1685, 1686 and 1688:  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1680#p874055

 This monte carlo program led me to think about calculating correlations between orthogonal hermite polynomials of same degree across two correlated variables. I calculated correlations beteween hermite polynomials of same order between two correlated variables in monte carlo setting in a matlab program in this post 1691 and 1693: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1680#p874075

 This further led me to thinking that prevalent classic method of calculation of pearson correlation between two random
variables was highly suboptimal when the densities of the variables are non-gaussian. It was optimal only for perfectly
gaussian random variables. In general, the greater the deviation from gaussianity in two random variables, the more
suboptimal the classic calculation of pearson correlation would become. I found in my research that a proper way to
calculate correlations between two non-gaussian random variables was to represent the random variables as series in
hermite orthogonal polynomials and then find correlations independently between hermite polynomials of the same order
across two variables. This discovery means that most of the classic models and numerical methods in stochastics and time
series that are based on proper calculation of correlations or covariances between two or more random variables have to
be properly altered by replacing one gross estimate of Pearson correlation by multiple estimates of correlations between
hermite polynomials of the same order across two variables when the random variables under consideration are
non-gaussian.

 The observation that pearson correlations have to be calculated independently for each hermite polynomial  led to a new
ground breaking concept  of analytic hermite polynomial regression of non-gaussian dependent variable on between two or
more explanatory non-gaussian variables. This orthogonal regression breaks down every non-gaussian random variable into
a series in hermite polynomials and then hermite polynomials of dependent variable of every order are regressed
simultaneously on hermite polynomials of same order of multiple explanatory variables and this depends upon their
indpendent pearson correlations between hermite polynomials of each order. Then results from various orthogonal hermite
polynomial regressions is added to give high dimensional curved surfaces with smooth derivatives that make a fit to the
regression data.

Please note that Hermite orthogonal regression I am referring to is a very new discovery that I recently made in Feb
2023 and it is different, far better and unrelated to another classic method known by the name of hermite polynomial
regression which has been known for decades. This new method of hermite orthogonal regression is mostly far better than
most AI and machine learning regresssion methods that fit a curve to data.  As opposed to functional regression, our new
orthogonal hermite polynomial regression method depends on correlations between hermite polynomials. While classic
regression that depends upon correlations between first hermite polynomial our new method is a generalization of classic
first hermite polynomial regression to a new method of regression that depends upon correlations between multiple
orthogonal hermite polynomials of same order across different variables.

 Below I show three graphs of hermite orthogonal regressions that try to explain Apple Stock returns VS Microsoft and
Nvidia Stock returns. All three graphs use only nine data observations over non-overlapping periods.

[![Image](32x32)](https://postimg.cc/JtDs5n08)

![Image](624x304)[![Image](32x32)](https://postimg.cc/JGjtS2jd)

[![Image](32x32)](https://postimg.cc/kVGJM1tC)

![Image](624x304)

![Image](624x304)

 The next three posts 1791, 1792 and 1793 describe calculation of correlations, covariances and regressions between
non-gaussian random variables when their Z-series representation is given.

  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1770#p875136

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1785#p875153

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1785#p875155

 Particularly the last post analytically explains the concept of regression between two Z-series random variables.

 Please also read posts 1731, 1732 and 1734 for hermite polynomial correlations and regressions:

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1710#p874492

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1725#p874542

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1725#p874578

 Here I distributed program for doing multivariate hermite regression in post 1722: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1710#p874497

 I presented results of one dimensional hermite regression in post 1705 here: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1680#p874075

 The hermite regression program is given in post 1706 here: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1695#p874270

 I also learnt that in order to do robust hermite orthogonal regressions, we needed to apply positivity condition of the derivatives of the density. Here I have described the positivity condition for derivatives of the density in post 1719: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1710#p874464

 After proper application of positivity condition, hermite regressions worked in an excellent fashion. I showed some results here in post 1721: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1710#p874492

 Please read posts 1783 and 1784 for calculation of variance of sum of two non-gaussian random variables when their
hermite polynomials have correlations

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1770#p875135

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1770#p875136

 Please disregard post 1785 and 1785, they have some errors.

 A Z-series option pricing formula is given in post 1830 here: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1815#p875619

 **Analytic Solution to Initial Value problems of first and higher order ODEs and systems of ODEs.**

I presented a new analytic series solution to ordinary differential equations that applies to almost all first order
ODEs, arbitrary higher order ODEs and systems of arbitrary order ODEs. It only may not apply to singular or degenerate
ODES.

 You can read all about my work here: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598

 Interestingly, I used the same basic ideas for solution of ODEs and SDEs. The common original idea involves
representing the ODEs and SDEs as integrals. We calculate the original integrand at initial value and add a term
comprising integral of first derivative of the integrand so that the sum of two terms exactly equals the original
SDE/ODE integral. We later represent the integrand in integral of first derivative by its initial value and add a third
term comprising double integral of second derivative. We continue to represent nth derivatives terms at their initial
value and add (n+1)th  term. After a lot of terms in the expansion, we neglect the variable terms and only evaluate all
the iterated integral terms with integrands calculated at initial values (as constant). These integrals can easily be
solved since their integrand is a constant value evaluated at initial time.

Please read here for a very intuitive description of the new method I applied to solve both ordinary differential
equations and Stochastic differential equations.

[https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1605#p873297](https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1605%23p873297)

**Monte Carlo simulation of Stochastic Differential Equations.**

Higher order simulations of stochastic differential equations was a longstanding problem in stochastics and mathematical
finance. Luckily, I was able to discover analytic solution to higher order simulation of SDEs. It was one of my first
breaks in research in Mathematics.

 In order to simulate an SDE with variable drift terms and variable volatility term, we apply Ito formula on variable
drift and variable volatility terms and find  an equivalent expression for each of the variable terms comprising a
stochastic integral with constant integrand first term evaluated at initial value and several variable integrand terms
under iterated stochastic integrals. We again apply Ito formula on variable integrand terms under the stochastic
integral sign to convert them into constant integrand terms evaluated at initial values and further variable integrand
terms under higher order iterated integrals. After N repeated application of the above procedure, we obtain an Nth order
discretization of the SDE  comprising a large number of constant integrand terms evaluated at initial values and we also
get some N+1 order terms with variable integrands under the iterated integrals. We can easily evaluate the all the
constant integrand terms up to order N under iterated stochastic integral signs and neglect the rest N+1 order variable
integrand terms. All the constant integrand stochastic integrals can be analytically solved using hermite polynomials.
This process can be repeatedly carried out to achieve high degree of accuracy in monte carlo simulations of the SDEs.
Since number of terms involved in higher order expansions increases very fast and cannot be easily done with hand, I
distributed an algorithm coded in matlab that calculated all the stochastic integrals and their coefficients from
constant integrand terms involved and these coefficients are later used in higher order simulations of  Stochastic
differential equations.

 In post 37 below, I described how to apply Ito change of variable formula on drift and volatility terms of the SDE and
then substitute them in the original integral representation of the SDE. I also explained how to repeatedly apply the
Ito Change of variable formula on variable integrand terms for higher order simulation of the SDEs. This post 37 was
written on Monday, May 02, 2016 1:43 pm. I think due to forum adjustments, proper formatting of this post is lost but
you can still properly read the equations in which Ito change of variable formula is repeatedly applied.

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=30#p782234

 I later stopped working on SDEs and applied the same idea on solution of ODEs. I started working on SDEs again after
quite some time and then wrote another post describing how to expand the integral solution of an SDE to higher order by
repeatedly applying Ito Change of variable formula. This post 564 is similar to post 37. Post 564 was written on Thu Nov
23, 2017 10:48 am.

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=555#p816432

 When I wrote the above post, I had only successfully expanded the SDE into constant integrand iterated stochastic
integrals but I still had not given the proper analytic formulas for the solution of iterated stochastic integrals.

 I was only able to solve for various iterated stochastic integrals whose integrands were constant values evaluated at
initial starting time. I wrote this post 690 written on Thu May 10, 2018 10:38 pm where I gave analytic expressions for
solution of stochastic integrals

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=675#p827224

 One day later I, latexed the formulas given in post 690 and wrote them again. This was done in post 693 written on Fri
May 11, 2018 6:08 pm

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=690#p827246

 Here in post 736, I presented a program based on above research that would evolve density of an SDE without pseudo
random numbers using a non-branching tree for underlying normal driving density. This program would automatically do
repeated Taylor expansions of SDEs with two drift terms and one volatility term and would also automatically solve for
all stochastic integrals involved. This program had exact behaviour for one evolution/simulation step of the
non-branching tree but its multi-step behaviour with deterministic non-branching tree was flawed. As it turns out when
we simulate with pseudo-random numbers, if the SDE does not have explicit dependence on time, we always simulate the SDE
at the start of interval as if we are starting from time zero. So while multi-step simulation algorithm was not good for
analytic non-branching density tree, its one-step version was perfect, precise and ideal for Monte Carlo simulations
with pseudo-random numbers. However, it was only a few weeks later, when I started using the one step simulation scheme
in monte carlo simulations. Again the algorithm and its explanation were given in post 736 written on Mon Jul 02, 2018
10:56 am here.

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=735#p830547

It was the algorithm in above post that a lot of friends copied from my thread and distributed around. It would
discretize for any arbitrary SDE with two drift terms and one volatility term without explicit time dependence in the
SDE.

 I later used the algorithm given in post # 736 for monte carlo simulations for the first time in a matlab program
distributed in post # 773, written on Sun Nov 04, 2018 6:34 pm given here

 https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=765#p837313

 In the above post, I simulated both bessel process version of the SDE and original coordinates version of the SDE with
monte carlo simulations employing pseudo random numbers.

 Here in post 891, I presented the same monte carlo simulation algorithm but all the binomial loops have been removed
and all the various integrand terms are directly written as a summation. It is the same monte carlo algorithm as old but
all the terms in expansion are written directly without any looping. Here is the link to post  891  written on Sat Mar
14, 2020 5:54 pm

 https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=885#p855539

Here is posts 892 and 893, I have earlier collected all my posts written about monte carlo simulations and associated
matlab programs.

 Post 892:

 https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=885#p855649

Post 893:

 https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=885#p855653

 Here in post 1172 and 1173, I presented ideas about expansion of high dimensional monte carlo simulations like we have
for interest rate derivatives and equity baskets.

 Post 1172:

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1170#p866762

Post 1173:

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1170#p866774

Here in post 1213, I have presented a higher order monte carlo program for very general system of correlated system of
asset and SV SDEs.

Here is the address of post 1213

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1200#p867829

**Z-Series/Hermite Orthogonal Polynomial Series Expressions And Construction of Analytic Densities of Random variables
from their first four to Eight Moments.**

** **

It was a long standing problem in probability theory how to find the analytic expression for the densities of random
variables when their first few moments are given. Though there had been quite some research on the problem, and
solutions like Gram-Charlier and Edgeworth series and many related solutions existed, there was not any perfectly good
solution to the problem. I came up with a numerical algorithm to convert the moments of arbitrary random variables into
an analytic expansion in Z-series or alternatively a series in hermite polynomials. It was due to this research, that I
was later able to extend the linear regression model with hermite polynomial regressions about which I have described
earlier.

There are some random variables for which the method does not work, but those cases have to be similarly expanded in
terms of a series in other appropriate orthogonal polynomials like Legendre, Chebyshev or others.

 This method generates densities of random variables so that first eight moments of the density perfectly match with
first eight moments input to the method. Mostly the match of the densities is precisely perfect. In this method, we find
coefficients of Z-series or Hermite orthogonal Polynomial series so that moments of resulting density precisely match
the input moments. Though Edgeworth and Gram-Charlier like methods have been very useful, this new method is a very
significant improvement upon classic methods of construction of densities when moments are given.

 Here I distributed a program that finds Z-series representation of a random variable when first eight moments of the random variable are input to the program. It is in post1653:  https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1650#p873803

Please also read post 1662 where I have written a small program that analytically constructs generalized gamma density.
The first eight moments of generalized gamma density are input to our Z-series density construction program. As it turns
out, when graphed on the same axes, our newly constructed Z-series density is indistinguishable from analytic graph of
generalized gamma density. Post 1662:

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1650#p873846

**Solution of Analytic Evolution of Densities of SDEs in Bessel Coordinates using Z-series and Addition of Cumulants

**

I had the idea of using Z-series representation of SDE random variables and decided to use addition of cumulants to find
the analytic evolution of SDEs without any pseudo random numbers.

 Later in January 2022, I proposed to directly represent the initial distribution of the SDE at each time step and
distribution of its diffusion at that step both as independent Z-series random variables. Since in Bessel coordinates
the evolution of SDE is almost independent of its initial value, I could use cumulant addition to advance the Z-series
representation of the densities of SDEs. You can read relevant posts    1338,1339, 1343, 1345, 1349,1378, 1629, 1640.
Here is post 1640 where a final program is distributed:

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1635#p873577

Please note that for mean-reverting and many other types of SDEs there is still some dependence between initial
distribution of the SDE and distribution of its generator even in Bessel coordinates but the method worked perfectly
well over large enough time steps.

**Solution of Analytic Evolution of Densities of SDEs in Both Original Coordinates and Bessel Coordinates using Z-series
and Expansion of Moments.**

In my very recent research work, I was able to improve my previous work on analytic evolution SDEs. The earlier work
with addition of cumulants could only be applied to SDEs in Bessel coordinates and could not work on SDEs in original
coordinates. The earlier method also had slight inaccuracies for non-linear SDEs. But with better understanding through
years of research, I could come up with a new method that used expansion of moments with Z-series and this method
resulted in perfectly precise evolution of densities of SDEs.

Here you can read details about the method:

[viewtopic.php?f=4&t=99702&start=1845#p875974](https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1845#p875974)

and here you can download the program that analytically evolves the densities of SDEs.

[viewtopic.php?f=4&t=99702&start=1860#p876045](https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1860#p876045)

**Calibration, Simulation and Hedging in a Heston Libor Market Model with Stochastic Basis**

My research paper titled, “Calibration, Simulation and Hedging in a Heston Libor Market Model with Stochastic Basis” was an invited publication in a prestigious Risk book “Interest Rate Modelling after the Financial Crisis.” Here is the link to Risk book web site:  [http://riskbooks.com/interest-rate-mode ... ial-crisis](http://riskbooks.com/interest-rate-modelling-after-the-financial-crisis)

**Limit Order Book Construction From NASDAQ ITCH Protocol Streaming Data using C++.

**

After completing the work with transition probabilities densities, I started playing with different topics. I posted a
C++ program to construct limit order book from Nasdaq ITCH format data. Here you can download the program. I had written
a basic version of this program several years earlier. This C++ program  was distributed in post 1162 here:

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1155#p866534

**Private Research on Fast Algorithmic Trading in Financial Markets.**

I have some of the best algorithmic trading models in the industry. To give an idea, I am copying a linkedin article
asking for capital.

[https://www.linkedin.com/pulse/quantita ... hsan-amin/](https://www.linkedin.com/pulse/quantitative-trading-business-proposition-asking-venture-ahsan-amin/)

**1.    ****Model Description.**

Our model is close to high frequency trading models where trades take place every few seconds. Our model makes a
prediction of the market fifteen seconds ahead and then makes a decision to buy the stock asset if the market is
predicted to go up and sell it if it is predicted by the model to go down. Once a trade has been made, we keep the trade
alive if it is profitable to continue the trade and end the trade if it is not profitable to continue the trade.
Depending upon the market conditions, our model makes between six hundred to one thousand trades per day with average
lifetime of a trade around thirty seconds. We enter the trades through limit orders and earn a portion of bid-ask
spread. Cumulative profits from our trading decisions and the earned bid-ask spread on average become a few cents per
trade for one hundred dollar share of stock.

Imagine a profit of one cent per hundred dollars for one thousand trades during the day and it adds up to ten dollars
that is a profit of ten percent of the capital in a single day. It might seem exceptional, in our simulations on real
data, there were several days every month when profits exceeded ten percentage points.

So, these small profits when aggregated over a large number of trades become very significant and usually become several
percentage points of the capital for even a single day. When aggregated over the entire month, these profits are a large
proportion of the allocated capital. In testing our models and determining their profitability, we have used zero
leverage. In our simulations on real data average profits remained 3% to 7% per single day after accounting for broker
costs even though in large scale simulations on real data there were one or two days every month when we made a loss of
2%-3% with a very high Sharpe Ratio (>1.5)

**2.    ****Mathematical Principles Behind the Model.**

Our model uses predictive machine learning to make trading decisions. We have used machine learning in a setting nobody
in literature has ever done before. In our research setting, we apply machine learning to optimize for the parameters
using previous day’s data. And these optimized parameters learnt from previous day data are used to make trading
decisions during the following day. Strength of the predicted signal is used in the future prediction of the time series
variables. We tested our algorithms on large scale data with the above rolling window of training on 24 hours of data
and then applying the model to the next 24 hours of data. This machine learning method is a new technique and is not
known to people in financial markets. This results in more accurate prediction of the market than any time series model
or process that analysts and quants usually use in financial markets to make a prediction of financial assets.

**3.    ****Risks Associated with the Model.**

There are much smaller risks associated with our fast and short term trading style as compared to plain vanilla buy and
hold strategies. Our machine learning methods result in large aggregated profits and only occasional minor local losses
but overall the trading strategy remains very profitable. When we make quick trades, it also becomes easier to limit
losses since risk management techniques can be used when the model loses money in small successive trades before the
accrued losses could become large to make a significant decline in previously earned profits. Our trading style results
in a very high Sharpe Ratio (>1.5) for most of the financial assets we used in historical study. Our trading style is
relatively safer as compared to existing trading strategies used to make profits in financial markets. While trading
stocks, we do not intend to use any leverage which would make risk management of our models much easier. Before trading
financial assets, we strongly vet that there are little known risks of large unexpected moves in the target stock. Our
vetting of stocks for large unexpected moves, our short-term trading style and zero leverage ensures that risk
management of the trading portfolio remains a relatively simple and straightforward process.

**4.    ****Prospective Financial Markets for Trading.**

We want to use our model to trade HK stocks, Stock exchange Index futures, Forex futures and commodities like oil and
gold futures.

**5.    ****Limitations of the Model.**

We have tried our models extensively on historical data but we have not done live trading with our models. We want to
train our models comprehensively on paper trading with some good brokers and then use them for live trading in the final
step.

**6.    Capital Requirements.**

We will require an initial amount of one million dollars and as the profitability of our models becomes evident, we will
continue to scale the trading capital with time once our market trading strategies continue to generate large profits.
As we demonstrate that our trading strategies remain profitable with time, we will gradually increase the trading
capital to several hundred million dollars.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Resume:

Ahsan Amin

Email: [[email protected]](/cdn-cgi/l/email-protection#2647484748141f1f1f665f474e49490845494b)

Phone: +92-336-2602125

Website: https://ahsanamin2999.wordpress.com/

Research Website: [https://papers.ssrn.com/sol3/cf_dev/Abs ... _id=435366](https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=435366)

Education

New York University, New York, NY, USA.

Masters of Arts in Economics with a concentration in Mathematical Finance, September 2002.

Wrote my thesis on pricing of Bermudan Swaptions and other Bermudan structured Derivatives within the framework of Libor
Market Model. Libor Market Model was the newly introduced and most modern interest rate model at that time. My thesis
was titled, “Pricing Bermudan ﬁxed income derivatives in multi-factor extended LIBOR market model.” My thesis was cited
in several other research papers/theses.

Northwestern University, Evanston, IL, USA.

Bachelor of Science in Electrical Engineering, March 97

Research and Work

CEO, Infiniti Derivatives Technologies, Lahore, Pakistan

Feb 2012 – Present

1.      I worked on analytic solution of path integrals of moments of stochastic differential equations along time
without using monte carlo simulations.

2.      I proposed analytic solution to Fokker-Planck equation for Stochastic Differential Equations on a standard
normal probability density grid. Later I proposed a Z-series that is a series in powers of standard normal that take
variable coefficients. I extended the Solution of Fokker-Planck equation with Z-series applied to the PDE.

3.      I extended the solution of one dimensional Fokker-Planck equation to two dimensional PDE that solves the system
of Stochastic Volatility SDEs using a two dimensional Z-series.

4.      I found another new method of solution to Fokker-Planck equation that solved for Z-series representation of the
underlying stochastic differential equation using addition of independent cumulants.

5.      I found solution to the problem of high order monte carlo simulations of Stochastic differential equations to do
accurate monte carlo simulations to arbitrarily higher order. I have been able to simulate with great precision a
correlated stochastic volatility system of two SDEs with arbitrary drift and volatility parameters in each of the SDE
with this method. Other existing methods are not able to solve arbitrary stochastic volatility systems.

6.      Worked on research on the analytic solution of ordinary differential equations. I presented methods for analytic solution of general nth-order ordinary differential equations and also for the analytic solution of systems of nth-order ordinary differential equations. My research is discussed in the research paper, "On the General Solution of Initial Value Problems of Ordinary Differential Equations Using the Method of Iterated Integrals" downloadable at https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2872598

7.      I suggested a new method to evolve and discretize the solution of SDEs on a transition probabilities grid. My
method represents the next generation version of quantizers algorithm. My next research goal is to do simulation of
smooth and non-smooth functionals of SDEs on this transition probabilities grid.

8.      I suggested a new method to construct the densities that can match moments of any order to the density with
precision. The method ensures that density is perfectly positive, completely normalized, and simultaneously matches all
given moments. Now you would not need Edgeworth expansions, or Gram-Charlier because my suggested method works perfect.

9.      My research paper titled, “Calibration, Simulation and Hedging in a Heston Libor Market Model with Stochastic Basis” was an invited publication in a Risk book “Interest Rate Modelling after the Financial Crisis.” Here is the link to Risk book web site: [http://riskbooks.com/interest-rate-mode ... ial-crisis](http://riskbooks.com/interest-rate-modelling-after-the-financial-crisis)

10.  I also successfully completed another research project which resulted in the research paper titled “Solution of Stochastic Volatility Models Using Variance Transition Probabilities and Path Integrals.” This paper can be downloaded at https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2149231

11.  I worked with a method to predict an arbitrary volatile time series of the kind that appears in stocks and other
financial instruments trading using slowly moving parameters method applied through Kalman filtering. This method can
also be used to model the degree of mean-reversion in financial instruments and helps in mean-reversion and convergence
trades.

Quantitative Research Analyst, UP-FRONT Inc., Tokyo, Japan

Feb 2003 – Oct 2010

It was a research and development Role and I was based in Lahore, Pakistan. These were the major research projects I
completed with Upfront.

1.      I developed a stochastic volatility displaced diffusion LIBOR Market Model.  Worked on global Calibration of the
model to more than 2000 swaptions with forward curve out to sixty years. Priced callable structured derivatives and more
exotic deals as well as their deltas and vegas in this stochastic volatility model.

2.      Worked on advanced multi-factor skew extended calibration of LIBOR Market model. Very robust smoothing
constraints were implemented which were required for stability of hedges. Worked with calibration of four different
versions of skew extended LIBOR Market Models. Successfully dealt with the problem of simultaneous calibration of the
whole swaptions matrix.

3.      Worked extensively with pricing of most complex callable LIBOR exotics. The instruments include Bermudans
swaptions, Bermudan callable reverse floaters, Bermudan captions, Bermudan CMS floaters, Bermudan CMS reverse floaters,
Bermudan CMS spread options, CMS TARN structures, Bermudan Snowballs, snowblades, and Bermudan callable PRDC.

4.      Extended Longstaff and Schwartz method to deal with complex callable fixed income structured derivatives in my research paper, “Multi-Factor Cross Currency Libor Market Models: Implementation, Calibration and Examples.” The paper can be downloaded here: [https://papers.ssrn.com/sol3/papers.cfm ... id=1214042](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1214042)

5.      Worked on the pricing of Bermudan Callable and Trigger Power Reverse Dual Currency Note and other FX/IR hybrid
derivatives. Developed a multi-factor cross-currency LIBOR Market Model for the pricing of these instruments.
Implemented the advanced analytics of the model on Excel using VBA and C++.

6.      Worked on a three factor Hull White Cross Currency model in Cheyette framework for fast pricing of Bermudan
trigger PRDCs. This involved analytic calibration of the model to FX volatilities and to swaption volatilities of local
and foreign economy.

---

### #1931 — Amin (Topic Author)
*August 23, 2023, 10:30 AM*

I sent emails to following prominent professors at LUMS Maths and CS department. I made the same word document and
Resume in attachment that I have pasted in previous post.

1. Dr. Arif Zaman.

2. Dr. Shafay Shamail

3. Dr. Mian Muhammad Awais

4. Dr. Asim Karim

5. Dr. Adnan Khan

6. Dr. Sultan Sial

It can be a great opportunity for me to restart my life with perfect stability if I can find an Assistant Professor
position at LUMS. I want to do research in Maths all my life in one form or other. I really hope that good American
people who have helped me so many times in the past would help me again to get my life out of turmoil.

---

### #1932 — Amin (Topic Author)
*August 24, 2023, 9:54 AM*

Friends, I keep my fingers crossed until I could hear from a few contacts(I mentioned) from LUMS. Meanwhile, I was
thinking how to continue progress of my research. One research idea is to find densities of discrete random variables
from their moments if the support of discrete variables is on M number of equi-spaced points and we are given first
eight moments of the discrete random variables.

We could start by finding a decent initial value of starting discrete density by approximating the continuous version of
the problem with given moments (as close as we can while having a valid density) and discretizing it. Then we can slowly
perturb the M dimensional density points array using some iterative numerical optimization approach (something similar
to what I used earlier a few weeks ago) so that first eight moments are perfectly matched.

We might need some information about type of density if it has vanishing tails (normal based hermite polynomials) or
discrete values at the tails (uniform based Legendre polynomials).

I will see if I can start working on the problem in a few days and post a matlab program that finds densities of
discrete random variables when their first eight moments are given.

---

### #1933 — Amin (Topic Author)
*August 25, 2023, 4:57 AM*

Friends, I was thinking what is impact of positive and negative serial correlation on moments of log returns in
financial markets. After writing a few simple equations, it was clear that relative increase in second moment can point
towards increasing or positive serial correlation. And a relative decrease in second moment can point towards decreasing
or negative serial correlation.

However, though these effects are usually likely, there can be some less likely cases in which the effects go in
opposite directions but I expect them to be infrequent.

I expect that case of cross correlations is also similar.

We all know that when there is any sentiment in the market and volatility increases, there is more serial correlation
and cross-correlation between different financial assets. However doing a systematic study the effect of change in
higher moments on correlations would also be of great interest.

How to quantify this observation and turn it into a real market trading strategy is the real issue.

I will come back with a more detailed post with equations. If I programmed it and it worked well, I will share it with
friends.

---

### #1934 — Amin (Topic Author)
*August 26, 2023, 9:38 AM*

Friends, yesterday when I went out, I decided to buy Fluanxol injections from a pharmacy in Allama Iqbal Town. When I
asked for Fluanxol injection, the salesman said that they had two injections available in their computer inventory
record. He went to find the injections but continued to fiddle around and then said that he could not find the
injections. I told him that thes injections are not fridge items but some pharmacies keep them in fridge and he should
look in the fridge but he refused that injections ere not in the fridge. He asked another guy for help who told me that
they had returned the injections since they were expired. I asked him that computer inventory records automatically show
expired medicine differently. Then that guy said he would look for the records of expired medicine. And started rolling
over pages of a large register. He spent five minutes doing that. In the meantime, I noticed that first guy went to the
fridge and placed something in the fridge. When he had closed the fridge and he came back to front of the pharmacy, the
second guy stopped rolling the pages of the register and  opened the fridge and brought me two injections. I still
wanted to think more about it and bought one injection.

But later when I put all things together, I realized that first guy was being asked by mind to skull to not give me any
injections. When I insisted they asked the second guy to wait until they deliver their own injections to pharmacy that
were placed in fridge by the first guy who had gone to front when I was with second guy at back of pharmacy and he was
rolling pages of a register.

On my way back whichever pharmacy I asked told me that they had returned the expired injections. As several hundred Army
personnell move in the city to control a target, they had made sure that no pharmacy sells injections to me after I had
gotten their injections.

So this is how corrupt Pakistan Army makes sure that they keep controlling their victims. Army is given several hundred
billion rupees by CIA to cooperate with mind control and they divide this booty between themselves with bigger fish
getting larger share and smaller fish getting smaller share and every fish remains happy after that. This is how these
crooks buy islands in New Zealand and properties in Belgium.

---

### #1935 — Amin (Topic Author)
*August 27, 2023, 7:39 PM*

Friends, honestly I am not very optimistic that I will find a position in LUMS as an assistant position any time soon.
As things are, I can still survive for 3-4 months but within 3-4 months, I will have to find a source of income
otherwise things would become very difficult. In a few days, I will write a detailed post outlining my plan to make some
income from consulting or other possibilities.

But most important thing for me is that I must continue my research. I have been thinking how to continue my research on
analytic evolution of densities of SDEs. We made some great progress when we were able to solve the SDEs in original
coordinates with precision by method of expansion of moments but we still faced problems when densities started to
become slightly negative and then would become unstable. I was thinking how to tackle that problem at zero and tried
different hacks but it never properly worked. I had plans for 2D stochastic volatility SDE models but I was disappointed
with problems at zero and knew those problems would also occur in stochastic volatility modelling so I did not try for
solution of 2D SV models.

However lately I have been thinking about the problem and hope we can find a way to solve a large class of SDEs properly
in original coordinates without problems at zero. Some SDEs with high volatility and volatility exponent close to .5
still might not be possible to analytically simulate and might still have problems with zero but still a large class of
SDEs could possibly be solved correctly even at zero.

My idea is to solve for SDEs with expansion of moments in Bessel coordinates. This will usually have no problems at zero
until volatility exponent is close to .5 and volatility is very high close to zero. For most SDEs, it will work with
precision. But obviously we want a perfect solution of SDEs in terms of Z-series in original coordinates and not bessel
coordinates. We earlier noticed that conversion of SDE Z-series in Bessel coordinates to Z-series in original
coordinates by applying change of coordinates on Z-series works poorly. However conversion of SDE density in Bessel
coordinates directly to SDE density in original coordinates(using a grid but without using Z-series) works quite
faithfully. So I think we should first find the density in original coordinates from transforming the density in bessel
coordinates so this part works well. Later we would do an inner product of SDE random variable in original coordinates
with hermite polynomials to extract the true coefficients of hermite polynomial Z-series in original coordinates. So my
plan is to find Z-series of SDE in original coordinates by finding inner product of bessel transformed density with
hermite polynomials rather than direct transformation of Bessel Z-series into original coordinates Z-series. If needed,
we can cheaply find Z-series of SDE in original coordinates to nine coefficients Z-series as opposed to seven
coefficients Z-series we have already been doing by doing inner product of the density.

Once we have solved for SDE densities in original coordinates without problems at zero, we would move towards stochastic
volatility models. I had a lot of plans for SV models but problems with SDE densities at zero really damped my
enthusiasm. I Want to take SV Cheyette model and solve for it with expansion of moments method using a two dimensional
Z-series. I also think that interest rate markets are strongly mean reverting and require mean-reverting SDEs for proper
modeling and use of models like lognormal/extended LIBOR Market Models might have arbitrage in deep tails because their
extreme tails are longer than what we find from mean reverting interest rates data. But anyway, I hope we will solve
analytic evolution of densities of interest rates in SV Cheyette models if things go well.

I am already working on the problem. I have an injection due at end of this new week but I think I will get a better
injection that will not be a complete horror story(though it still affects the productivity quite a bit) so I hope that
we will make some good progress in our research in next 30-35 days.

---

### #1936 — Amin (Topic Author)
*August 28, 2023, 7:45 AM*

Friends, mind control agents continue to openly release gases on me. These gases are now in every fan in our house. It
is very painful to breathe in these gases. But mind control agents know when they fail to drug my food despite several
hundreds people trying to drug my food in the city, they really have to use gases to take their chemicals into my brain.
It is extremely hard to work when I am under the effect of these gases. This has become a constant mode of torture over
past week and more but I remained silent due to a lot of other reasons. They also continue to target various parts of my
head with high frequency lasers when I am working and also when I am sleeping.

I want to warn the scum at Pentagon to stop their nefarious tactics otherwise I will openly and boldly continue to
expose their animal tactics and collusion with the billionaire jewish Godfather/Goldfather of mind control. I want to
tell people that this whole mind control business is about supply and demand. Jewish billionaire and his rich jewish
cohort supply top brass of American army what they demand(jobs worth millions of dollars with extreme perks in jewish
companies). In return, they corrupt top brass of American army supplies the Jewish billionaire and his rich jewish
cohort what they demand by retarding everyone these evil jews wish. So this nexus between corrupt american army and rich
animal jews continue to retard everyone they wish. Please protest against this evil nexus taking over the world
especially in your country.

I want to warn the scum in American army to stop using gases on me and a lot of other innocent people like me otherwise
I will continue exposing them and their nexus with evil jews boldly all over the world.

---

### #1937 — Amin (Topic Author)
*August 28, 2023, 8:29 AM*

For past few days they have been using another sickening gas in my room, in my car and in the porch/car garage where I
work at night since weather is better on many night due to monsoon. They keep discharging gas continuously at these
places and the gas is very sickening and makes one very disoriented, It strips my composure and gives a feeling of
mental torture and unease in the brain. I do not blame that they constantly use this gas but they use it from time to
time several times a day and with far more frequency lately.

They also keep giving other gases that charge my clothes and release charges that settle on my body.

I mostly go out in the evening on motorcycle and they have planted some device in the seat of motorbike that
continuously targets the anus as I drive the motorcycle. As a result, there is constant pain in my anus and the area
around it becomes very sensitive and it especially pains when I touch it or rub it. They have become more and more bold
in using high frequencies from devices fitted in my motorcycle seat and driving it becomes more and more painful
everyday as their boldness increases.

They also use other tactics. For example when I am driving my car (when I drop my mother and the particular thing
happened in the evening a few days ago when my mother sent something to my cousin and I had to take the stuff in my
car.) and enjoying music, they would simply target my neck with lasers and I would start feeling extreme pain and
exhaustion in my neck.

Similarly when I tried to sleep a few days ago, they targeted my head with special frequency lasers and I would continue
to feel extreme exhaustion and tiredness in my head and I would not be able to sleep easily. When this happened at night
three days ago, I decided in the middle of the night to leave the bed and sleep in a different position on the floor of
my room and then I had a great sleep. After that I have been sleeping on floor for all of the past three days since they
ere not allowing me to sleep properly in the bed. How long can I remain innovative and change positions of things around
me and also possibly block lasers by putting a folding table to block one of the angles is a big question and it is only
a matter of time before they would install new gadgets and catch up with me and start targeting lasers on my head again
when I am sleeping at the floor within a few days.

Even though I am more free and more confident now than ever and no special targeted drugging of food is continuing
especially thanks to favors from good American people who tried to protect me but people at pentagon are even more
determined than ever to continue my mind control and they want to use all sort of new tactics to somehow achieve their
designs. Especially when I do not mention about torture when it starts, they continue to increase torture. And many
times I do not write about so many things here because I do not ant to be constantly whining about it. And especially
when I do not write about antics of mind control agencies, they become more and more bolder and increase torture and
also start new ways of torturing.

Friends, I really hoped that I would continue to focus on writing professional posts on this forum and slowly my mind
control and other forced persecution would greatly decrease. Sadly I was thoroughly wrong. American army scum is so
bitter to get into paradise of Jewish billionaire and his rich cohort that they have a stark realization of the great
mistake they have made by temporarily decreasing my mind control in the past when forced by protests of good American
people. Scum in American army was completely sure that this was never a big deal and they would continue my mind control
in one way or other and they were confident that minor adjustments they had to make by decreasing my mind control
temporarily when faced by protests of good American people would never be a big deal. And every year, they would anyway
detain me in a psychiatric facility and make sure that food and psychiatric drugs I was given in detention would take
any potent neurotransmitters out of my brain and I would have to struggle for more than five or six months to partially
regain my self and by that time another psychiatric  detention would already be approximately due to take all powerful
neurotransmitters out of my brain. However due to increasing protests from good people, scum in American army has been
unable to detain me for past two years and now they have a growing realization of their mistake by letting me do any
research at all. In past few months, they tried to detain me several times but I raised hue and cry and my forced
detention was averted because of immediate pressure from good people.

But what can you do when scum in american army firmly knows that their future is associated with making it into the
paradise of Jewish billionaire and his Jewish cohort. Jewish billionaire is in no way obliged to let everybody get into
their paradise and a lot of scum knows very well when they would fail to retard people pointed out by the billionaire
and his cohort, and rather bring a bad name to billionaire and his cohort as their corrupt practices are exposed in
public, Jewish billionaire would never let them into his paradise. It really takes some bravery in this world to live
without money and continue to do good things. And American army scum knows very well what it would mean to live off
pension in relative social isolation as opposed to getting extremely high profile job paying millions of dollars every
year and with social idolization by everyone when they would be offered such a job by jewish billionaire and his rich
cohort. So scum simply cannot afford to not retard people pointed out by the jewish billionaire and his cohort.

Whatever good or bad the scum is would otherwise not be my business and I would rather spend my time in some positive
activity like doing good research that I love. But I have to write this post with a heavy heart again since I am sure
that mind control agencies and their backers want to detain me again in a few weeks. They tried to drug the city a few
weeks ago but it did not work. They are really afraid that if I continue to do good research, I might slowly get out of
their hands. They know that they really have to do again what they used to do every year without exception to control me
again and stop me from trying to do any good research. I also see many signs that my family also starts to become
impatient and they have plans of detaining me on suggestion of mind control agencies sometimes in near future.  I really
want to request friends to strongly protest to good people in American government to pressurize the army to end my mind
control.

I am really obliged to so many good people who have great humanity and who knew that I was totally innocent and they
tried to protect me again and again in the past. There was a time when I would ask myself if there is any good humanity
in this world since large number of people would behave rudely or carelessly(due to complete brazen lies of machinatory
scum in American army) and there was almost nobody who was ready to stand for me. And I really pray (I could not choose
another word though I do not believe in god) for good people who took a stand against all odds and tried to save me and
it is due to efforts of these good human beings (as opposed to lot of humans who just eat and have sex but are otherwise
great animals like for example American army scum who are ready to do any inhuman completely cruel deeds for monetary
reward) that I have been able to survive and do any decent research.

[My Letter To HRW About My Human Rights Abuse](https://forum.wilmott.com/viewtopic.php?f=15&t=102298)

Above is a very incomplete account of how various psychiatrists continued to play in hands of Pakistan army to retard
me. It also does not cover all the time till year 2022 and the account stops several years earlier.

Pakistan Army has no personal animosity with me. Chief of Pakistan Army staff is given more than 50 billion rupees every
year come rain or shine so that army continues American Mind control of intelligent people in Pakistan. Even when the
relations between both countries are extremely bad, this bribe is always given to Pakistan army generals in time.

I am copying some posts from the past for the complete context.

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

I have been detained more than 30 times by various psychiatrists during past twenty-five years on orders of Pakistan
Army. This is despite that I have never been violent all my life. I have never hit anyone in my adult life and I rarely
speak with anyone in a loud voice. I have never done anything like breaking a glass or any utensils that is associated
with sick people.

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
lived during the past twenty years. There are at least more than 500 mind control targets in Pakistan most of whom are
computer science majors.

Mind control in Pakistan and many other places increased dramatically like never before. We have in Lahore a huge
building called Arfa Towers where all the facilities for technology and IT companies were provided to attract new firms
and entrepreneurs and later Arfa Towers became a scene of mind control carnage since tens of aspiring computer
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
entire public water supply and beverages knowing that the victim would have to drink something somewhere. Ground water
is also so thoroughly drugged with mind control chemicals that entire public water supply of the city and several
kilometers out of the city would be completely drugged with mind control chemicals. Pakistan army routinely does this in
Lahore city on behest of American mind control agencies.

Ten years ago, army soldiers and agents would go to markets to drug the targeted food and beverages with mind control
chemicals which they still. Large scale movements of soldiers and agents raise suspicions in general public and
therefore mind control chemicals are supplied to beverage and food manufacturing companies in Pakistan, and they simply
add the chemicals in food and beverages during the manufacturing process.

In Lahore city, there are more drugged beverages at any time than good beverages in small stores or large supermarkets
alike since most of the beverages are drugged at manufacturing source by coca-cola, pepsi-cola and Nestle.

Coffee stimulates the brain and the brain connects in new ways after taking coffee and good coffee creates problems with
keeping victims on mind control since their brain starts connecting in many new ways after taking good coffee.
All coffee and I repeat that entire coffee in the country present in the stores is drugged with mind control chemicals.
Most of the coffee on good stores is imported from foreign countries. I do not know how it works but importer is
probably told by army to drug the imported coffee before distributing it in the market. It is even very difficult or
rather impossible to get good coffee beans. Two or three years ago it was possible to find some brand of coffee that was
good by trying all new brands but it has not worked for past two years now for me despite that I keep trying. I even
know of instances that when I was able to buy good coffee of a certain brand from very large and posh stores, they took
entire coffee brand off the shelf from all their branches within two to three days. People know that Corrupt Army in
Pakistan that ensures mind control is more powerful than any political government here.

Tea used to be good but for past one year most mainstream Pakistani brands of black tea are drugged with mind control
drugs. This has still not caught up thoroughly like coffee is thoroughly drugged and it is still possible to find some
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
cannot live without it. Since our mouth is kept charged and some charges continue to go into victim's body from one's
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
and American mind control agencies continue to perfect it over last twenty years. Again, mind control in Pakistan is
ensured by top Pakistani army generals since they are given several hundred million dollars by US army

I have not talked about special infrastructure that is used to project EM waves on the target and this infrastructure is
present on all major roads and public places in big cities and major highways and motorways in the country.

Before writing this post, I want to apologize to good jews but want to tell them there are enough evil jews who are
doing everything to tarnish the great goodwill jews have so rightly earned through generations of hard work and being
nice and kind to other people in the society. I want to request good jews to Please force these evil(jewish) people to
end the bad practices that are starting to take root in American and other societies on their behest and before it is
too late. I also really hope that my mind control would finally end(as I have been begging for past twenty years) and I
would never have to write a post like this again.

In the past, I continued to mention about my mind control persecution from time to time but only started writing regularly about it when I arrived in UK on a Highly Skilled Migrant work visa. Mind control agencies did everything in their power to fail me in UK. People were asked to not give me a job. People I contacted were routinely told brazen lies about me totally shamelessly. When I realized that I had no future in UK, I returned to Pakistan after a six month stint in UK. Since my hard earned money had thoroughly insulted mind control infrastructure in UK as they had to drug entire cities with mind control chemicals in UK (read briefly about it in my application to HRW in a previous thread) for a nobody like me and American government had to move all their grand and influential puppets in UK (again for a nobody like me) to force people to drug the manufactured food. British Banks went to the extent to steal my money to bleed me. Read here: https://forum.wilmott.com/viewtopic.php?f=15&t=102298#p857494. British police forcefully stopped me from seeing law firms(Brief details are given in my application to HRW attached as a link below).  Since my money had given mind control agencies a very tough time, mind control agencies decided to never let me make significant money after that. My old Japanese employer was told to not hire me after I returned to Pakistan. Whoever I would contact someone in Europe for job or consulting, mind control agencies would move American embassy infrastructure in that country and somebody highly influential (or army or secret services of that particular country)  in that particular country would approach my target employer and again brazen lies and fabricated stories would be told about me shamelessly. I am a fighter in life and I continued my research despite all economic, coercive and other hardships. All odds were against me but I tried my best to continue.  I have been presenting my research to friends on this forum for past five or six years. At this point, I want to request good American and friends from other countries who have come to know me through my research to please use their influence to end my mind control forever.

I had told friends earlier that a jewish billionaire is Godfather of mind control. When my persecution started (in late
1997) at the university in New York which is a big time player in mind control of Muslims, blacks and foreigners, many
university officials were very pleased that they were getting written in good books of the billionaire jewish Godfather.
Though there are far richer billionaires in US who are staunchly opposed to mind control, they are not ready to shell
out hundreds of millions of dollars to bribe anyone to end mind control while mind control Godfather continues to give
large bribes to people to continue mind control. Many of the people related to defense in mind control are given
extremely high paying jobs in Godfather and his other jewish friends' companies after they retire from mind control and
Godfather is extremely generous towards them and it is well established and well known to people in mind control that
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

### #1938 — Amin (Topic Author)
*August 28, 2023, 8:33 AM*

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

I have been detained more than 30 times by various psychiatrists during past twenty-five years on orders of Pakistan
Army. This is despite that I have never been violent all my life. I have never hit anyone in my adult life and I rarely
speak with anyone in a loud voice. I have never done anything like breaking a glass or any utensils that is associated
with sick people.

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
lived during the past twenty years. There are at least more than 500 mind control targets in Pakistan most of whom are
computer science majors.

Mind control in Pakistan and many other places increased dramatically like never before. We have in Lahore a huge
building called Arfa Towers where all the facilities for technology and IT companies were provided to attract new firms
and entrepreneurs and later Arfa Towers became a scene of mind control carnage since tens of aspiring computer
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
entire public water supply and beverages knowing that the victim would have to drink something somewhere. Ground water
is also so thoroughly drugged with mind control chemicals that entire public water supply of the city and several
kilometers out of the city would be completely drugged with mind control chemicals. Pakistan army routinely does this in
Lahore city on behest of American mind control agencies.

Ten years ago, army soldiers and agents would go to markets to drug the targeted food and beverages with mind control
chemicals which they still. Large scale movements of soldiers and agents raise suspicions in general public and
therefore mind control chemicals are supplied to beverage and food manufacturing companies in Pakistan, and they simply
add the chemicals in food and beverages during the manufacturing process.

In Lahore city, there are more drugged beverages at any time than good beverages in small stores or large supermarkets
alike since most of the beverages are drugged at manufacturing source by coca-cola, pepsi-cola and Nestle.

Coffee stimulates the brain and the brain connects in new ways after taking coffee and good coffee creates problems with
keeping victims on mind control since their brain starts connecting in many new ways after taking good coffee.
All coffee and I repeat that entire coffee in the country present in the stores is drugged with mind control chemicals.
Most of the coffee on good stores is imported from foreign countries. I do not know how it works but importer is
probably told by army to drug the imported coffee before distributing it in the market. It is even very difficult or
rather impossible to get good coffee beans. Two or three years ago it was possible to find some brand of coffee that was
good by trying all new brands but it has not worked for past two years now for me despite that I keep trying. I even
know of instances that when I was able to buy good coffee of a certain brand from very large and posh stores, they took
entire coffee brand off the shelf from all their branches within two to three days. People know that Corrupt Army in
Pakistan that ensures mind control is more powerful than any political government here.

Tea used to be good but for past one year most mainstream Pakistani brands of black tea are drugged with mind control
drugs. This has still not caught up thoroughly like coffee is thoroughly drugged and it is still possible to find some
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
cannot live without it. Since our mouth is kept charged and some charges continue to go into victim's body from one's
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
and American mind control agencies continue to perfect it over last twenty years. Again, mind control in Pakistan is
ensured by top Pakistani army generals since they are given several hundred million dollars by US army

I have not talked about special infrastructure that is used to project EM waves on the target and this infrastructure is
present on all major roads and public places in big cities and major highways and motorways in the country.

[My Letter To HRW About My Human Rights Abuse](https://forum.wilmott.com/viewtopic.php?f=15&t=102298)

Above is a very incomplete account of how various psychiatrists continued to play in hands of Pakistan army to retard
me. It also does not cover all the time till year 2022 and the account stops several years earlier.

Pakistan Army has no personal animosity with me. Chief of Pakistan Army staff is given more than 50 billion rupees every
year come rain or shine so that army continues American Mind control of intelligent people in Pakistan. Even when the
relations between both countries are extremely bad, this bribe is always given to Pakistan army generals in time.

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
Godfather is extremely generous towards them and it is well established and well known to people in mind control that
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

So not blindly believe a word I say but try to investigate the truth about it from informed people and you will find out
that every word I said is truth.

Since things might heat up after my writing this and my persecution might increase, I want to ask European embassies in
Pakistan to keep a vigil. I want to tell Europeans that my writing about mind control is in their great interest since
the very same people who instigate retarding of intelligent muslims are behind retarding of hundreds of intelligent
europeans and once the nexus between American army scum and evil rich jewish animals is exposed all over the world, I am
sure elements of this evil nexus will be far more careful in openly retarding European talent(that they do not like). I
will request intelligent Europeans who read my posts to please ask their embassies in Pakistan to keep a vigil about my
safety since scum in American army will try its best to somehow silence my voice.

---

### #1939 — Amin (Topic Author)
*August 28, 2023, 8:22 PM*

Friends, mind control crooks are adamant on constantly torturing me. I have been trying to work for past one and a half
hour and they are constantly targeting left side of my head with high frequency microwaves.

Rich jewish scum including the jewish billionaire have realized that they cannot afford to let me do any more creative
work and American army scum is blindly following their commands to physically torture me with microwaves. I really want
to ask people to thwart this evil nexus between rich jewish scum and American army scum.

Once I speak about this evil nexus between different types of evil human scum, the scum responds by torturing to silence
my voice at all cost. Now, they have a well planned policy of torturing me to silence my voice.

---

### #1940 — Amin (Topic Author)
*August 28, 2023, 9:50 PM*

Friends, due to constant pain, my left temple has become very sensitive. I do not know how they cause this pain. Either
they focus high frequency microwaves on the temple or some chemical settles on temple and when EM waves hit this
chemical on temple it causes huge pain.

Before leaving for outside this evening on motorcycle, I was making fun of mind control guy that he had totally failed
his jewish backers by not being able to drug my food despite employing several hundred army personnell from pak army and
despite his tall claims that he made before them. Then I do not know how they do it but even on my motorcycle, they
continued to cause very high pain in my temple. And while outside for three and a half hours, I washed my face and head
three times since every time I washed my face and head, the pain in temple decreased very sharply.

For past one week, whenever I try to work or while I sleep, they cause huge pain in my left temple and now it has become
very sensitive due to chronic pain. Earlier when I would mention on internet, they would decrease their torture for at
least a week or two but only to increase the torture when I mention about the pain and torture now. It seems there is a
lot of urgency among bad people that they really have to destabilize me by torturing me and they simply cannot allow me
to continue my research calmly anymore. I am sure they would only increase this torture in coming days.

---

### #1941 — Amin (Topic Author)
*August 30, 2023, 9:03 PM*

Friends, I had to be away since Tuesday afternoon. My sister's father-in-law was very sick and unfortunately died on
Tuesday. Our family spent a lot of time with their family. Especially it was his funeral on Wednesday and I spent all
day with my sister's family. Therefore I could not write any post nor devote any time to my research.

My four weekly injection is due tomorrow but I hope that it will be a good injection with considerable less damage from
mind control drugs.

I also wanted to ask friends if you are in academia or a graduate student anywhere in the world including America,
Europe, India or China and you have some research ideas related to my research and you think I could possibly help in
some way, please do not hesitate to contact me. Even if I cannot think of a suggestion from the top of my head, I would
like to brainstorm and  try to think of helpful ideas.

My research is quite different from mainstream research and I have spent several years developing many basic ideas so it
is quite possible that sometimes I could think of some good suggestion about your research ideas (related to my
research) since I am more deeply rooted in my research for several years.

I would love to help if I can and obviously I am not going to ask for any fees/charges from friends in academia. So I
would truly love to be helpful and if you have any questions/research problems, please do let me know.

I would be spending most of the time in coming weeks on analytic solution of 2D SV SDEs especially the SV Cheyette
model. And since mind control gases do not seem to be ending or decreasing, I am afraid I would have to brave through
torture from gases while trying to do my research on SV SDEs.

Especially they continue to cause pain in my temple from time to time all through the day. Earlier when I would have bad
food or I would be under influence of gases, the veins passing next to left temple and going to brain would start
pumping/throbbing. And my reality and consciousness would change slightly. Sometimes, I would feel great anxiety or some
other problem but it would mostly never cause large physical pain. But for past ten days, they have been using some
different gas or different mind control chemicals and these chemicals cause extreme physical pain in veins going to
brain right next to left temple. And this problem is not decreasing and I am afraid I will have to continue my research
while living with the same physical pain.

---

### #1942 — Amin (Topic Author)
*September 2, 2023, 6:24 PM*

Friends, as a first step towards solution of correlated SV SDE equations, I really think, I would do monte carlo
simulation and construct 2D density of aaset. I will then try to extract coefficients of two dimensional Z-series
representation of monte carlo. In this 2D series if each of the asset and volatility are expanded to 7th order, there
will be fifty coefficients to be found. This coefficients would be found by inner product of 2D monte carlo density with
various combinations of products of hermite polynomials of pure asset and hermite polynomials of volatility. So we will
take a numerical density from monte carlo and then use inner product to find coefficients of 2D Z-series and different
terms of this 2D Z-series/hermite series will consist of products of two different hermite polynomials of various order.

Once we can quickly find a 2D Zseries for solution of asset in 2D SV monte carlo simulation model, we will be able to
use this Z-series for different possible analytics(like all sort of conditional values and greeks etc).

If the exercise goes well with monte carlo 2D density of asset in SV models, we will use the methods learnt to propose
more analytic solution to SV SDEs.

Even though mind control agents continue to use gases openly and especially at night when I am sleeping, they have
decreased the intensity of torture(pain in veins that pass next to left temple) somewhat. Specifically, they continue to
use gases and pump mind control chemicals through veins that pass next to left temple but they have avoided giving huge
pain. They still continue to use gases at the same scale and continue to cause light pain when my veins next to temple
start throbbing. But extreme intensity of the pain they caused earlier has decreased. The pain is still there but
lighter but it is still enough to make it difficult for me to continue concentrating on my research. Especially gases in
my room have not decreased at all and I try to avoid going into my room during the day and spend as less time there as
possible, but I have to sleep inside my locked room and there is no other place where I could sleep safely other than in
my room.

---

### #1943 — Amin (Topic Author)
*September 4, 2023, 9:16 AM*

Friends, in a general two dimensional bi-variate density, the underlying Z-series representation would be of the form

$   X(\bar{X}(Z_1), V(Z_2) ) \, =\, \sum_{m=0}^{m=7} \, \, \sum_{n=0}^{n=7}   \big[ \, C_{m,n} \, {Z_1}^m \, {Z_2}^n \big]$
Eq(1)

please note that it could be written as product of two independent uni-variate Z-series in$Z_1$ and$Z_2$ only when
underlying$\bar{X}(Z_1)$ and$V(Z_2)$ would be independent. Though in special cases, it might be possible to switch to
new tilted Z_series coordinates that are independent as in a correlated bivariate normal density or possibly some of its
extensions.

The hermite series equation for describing a general bivariate density corresponding to 2D Z-series Eq(1) would be

$   X(\bar{X}(Z_1), V(Z_2) ) \, =\, \sum_{m=0}^{m=7} \, \, \sum_{n=0}^{n=7}   \big[ \, B_{m,n} \, H_m(Z_1) \, H_n(Z_2) \big]$
Eq(2)

I am very sure that it is the above form that we need to use when expressing bivariate densities in two dimensional
hermite polynomials. I think we will need to find sixty four coefficients by doing inner product of the bivariate
density with all possible pairs of powers of hermite polynomials from 0-7.

I still remember when I tried for solution of SV problem earlier with two dimensional version of the new solution to
fokker-planck equation, the form given by equation (1) worked very well and Eq(1) Z-series implies Eq(2) hermite series.
They can be analytically converted from one to other in case of 2D series just as we could convert from Z-series form to
hermite series form and vice-versa in case of one dimensional hermite/Z-series series.

I think different products of hermites appear because of higher cross correlations.

I hope that I would be able to demonstrate the idea with a new matlab program in a few days.

Friends can also notice that for a bivariate density, we can have a bivariate hermite series regression in which we
could decompose the bivariate density into possibly 64 pairs of products of hermite polynomials and then regress each
hermite product of regressand on similar(with same degree as in regressand) hermite products of regressors. So there
will be 63 or 64 regressions in the solution.

I really hope once we find a two dimensional hermite polynomial representation of a bivariate density, I will try to
apply the idea of associated 2D regression to find greeks and also conditional values in a SV monte carlo setting.

---

### #1944 — Amin (Topic Author)
*September 8, 2023, 1:17 PM*

Friends, I have made some progress in coding the calculation of 2D Z-series/Hermite series of a random variable with a
bivariate density. I hope to post the program sometime on this weekend. I will also post a program that converts 2D
Z-series to  2D  Hermite Series and vice versa. I have also a lot of helper programs about 2D Z-series that find 2D
Z-series of functions of initial bivariate random variable with a given 2D Z-series and programs for Square-root of 2D
Z-series and reciprocal of 2D Z-series. I will be posting all these programs in next few days after I complete the
calculation of 2D Z-series of a bi-variate random variable.

I have not been able to work well due to injection I had last week and also due to hot weather. Monsoon has ended a few
weeks ago and temperatures have risen after that and it becomes very difficult to work properly in hot weather. It will
still be 2-3 weeks or possibly more before temperatures fall down to reasonable level.

However, I really hope to do some good applied work with 2D SV models after the above mentioned part of work ends.

---

### #1945 — Amin (Topic Author)
*September 8, 2023, 9:47 PM*

Friends, I have a working prototype of the above mentioned program. Will test it more tomorrow and most likely post it
on Sunday.

---

### #1946 — Amin (Topic Author)
*September 10, 2023, 12:33 PM*

Friends, I have calculated 2D hermite-series but I have not been able to graph it with change of variable from bivariate
normal. Unless we compare graph from our hermite series with 2D Parzen density graaph, we cannot be sure if our
analytics are right. It can still take 2-3 days to properly complete the work and I am working on it full time.

I had an antipsychotic injection on Thursday before last Thursday. I have not been able to work well after that and
could work only 1-2 hours everyday. But I am somewhat better now and hopefully would get the remaining work done in a
few days.

Microwave torture has somewhat deceased but when I try to work and become somewhat productive, they increase their
torture and start giving me light pain in left temple. Though many times it is not very high pain but it is still enough
to put me off to not be able to work after that. Another new torture technique they have started is that they target EM
waves on my teeth and from time to time, I feel sudden pain in many of my teeth.

Anyway, I hope to try to do good research in coming weeks and want to concentrate on my research.

---

### #1947 — Amin (Topic Author)
*September 11, 2023, 5:58 PM*

Friends, it seems that mind control crooks do not want to allow me to work on my research at all. I am currently trying
to work on my research and sat on the table for 20 minutes but the mind control crooks have already started giving me
strong pain in my left temple. Whenever I try to work on my research with enthusiasm, they use this trick to cause pain
in my temple to not let me work at all.

American army scum knows that I have totally exposed their animal, hideous and corrupt nature all over the world and now
people all over the world  have become well aware that scum retards innocent and talented people on the orders of evil
jews for their own material gain. Since I Was able to get attention of good people towards corrupt nature of scum due to
my reasonable research, now scum feels that decreasing torture on me in the past due to pressure of good people was a
great mistake since decreasing torture allowed me to do better research and good people sympathized with me and tried
for my freedom only to realize the truth about the nexus between evil jews and american army scum. Now scum is afraid
that if I could do some more good research in the future, it would get more good people's attention and expose the
corrupt nature of American army scum all over the world and they simply do not want to allow me to damage their vested
interests anymore. Even though a large number of good people back me and sympathize with me, the collective might of
evil jews and American army scum is greater than any other power in this world. Good people have to brace for a long
haul struggle to defeat the nexus of evil jews and American army scum.

I know there are a large number of jews who are extremely good people and great human beings and have nothing to do with
evil practices of billionaire jewish Godfather of mind control and his rich cohort. My writing against those evil jews
would naturally hurt good jews as well. I want to apologize to them for my harsh words against bad jews. But I would
really request them to rise beyond religion and become human and true American first (it is because of the total
opportunity American society gave jews that they are so successful and rich so please be truly grateful to every
American in the society instead of retarding or threatening American talented people to forcefully work somewhere) and
thwart the practices of bad jews before it hurts the impression of good jews as well. I would request good jews who are
also good human beings to make sure that mind control ends in every society because of inhuman animal nature of mind
control torture. Most good people have absolutely nothing against jews who are good human beings and are true Americans
and we really wish them complete success in their lives. We want to equate jewishness with great humanity and kindness
to other human beings.

---

### #1948 — Amin (Topic Author)
*September 12, 2023, 10:16 PM*

Friends, mind control agents are extremely disturbed after my yesterdays's post. When I went out in the evening to get
food, in addition to pain in my left temple, mind control agents also started giving me pain in my both eyes. They had
never done anything like this ever before. They have previously given light pain in my eyes when I am sleeping but this
pain is still bearable but the pain in eyes this evening was something I never experienced before. I bought cold bottled
water and I would wash my eyes thoroughly with water after every 3-4 minutes since washing the eyes would help decrease
the pain. When I came home they decreased the pain in eyes somewhat but continued to give huge pain in the left temple
and also in my teeth. I was so overwhelmed with pain that I did not even try to work after that.

For past one week, after coming back to home at night, I work in my mother's room (while she is sleeping) in air
conditioning since AC of her room is quite better and has relatively little gases. I move my portable desk to her room
and keep working for a few hours and then come back to my room for final sleep. But today, I did not even move my desk
into her room and just kept sleeping in my mother's room  since I was totally overwhelmed with pain in my left temple
and also in my teeth.

Right now, I just moved to my room for final sleep after wasting several hours (a mixture of sleep and pain) in my
mother's room and decided to write this post.

---

### #1949 — Amin (Topic Author)
*September 13, 2023, 2:05 PM*

Friends, I might be totally off and completely disoriented but had this thought that I am sharing with friends. If it is
totally off, please just disregard it.

Can we solve  1D (as a start) backward parabolic equations (and possibly many more types of PDEs) on a fixed domain with
Legendre polynomials. The underlying probability distribution required for orthogonality of Legendre polynomials is
uniform which seems very right for deterministic functions. After a few iterations of some numerical method for a few
time steps on discontinuous data might make the equation to have several continuous derivatives and it could be
represented by Legendre polynomials on the fixed domain. As I earlier mentioned that underlying probability distrbution
is uniform which seems very right for deterministic functions. Again after a few time steps of some numerical method
when the equation has become smooth, we could represent the equation solution with Legendre polynomials(and find
coefficients of Legendre series representation of the solution) and then substitute the Legendre series solution in the
PDE that normally takes just first two derivatives. So we can this way continue to advance the solution across
time(backwards).

There might have to be a first derivative positivity constraint on the solution like we had with hermite polynomials.

I have not thought deeply about this idea so there might be possible problems and I might be totally off but just
thought I would share it with friends.

I am having a stimulation field day today. Day before yesterday, I bought some cheap coffee satchets imported from
indonesia and they were good. I could not find similar satchets again but there are another kind of cheap coffee
satchets that are all over the market and I bought them yesterday night. They have very slight amount of mind control
drugs but they are still good to stimulate the brain. I had a couple of those coffee satchets today around noon and I
have been able to think lucidly about a lot of math problems.

But again I might possibly be off about this problem.

Though I am very afraid that Pakistan army would be asked to approach all the shops in various markets and drug all  the
coffee satchets within a few days. I will keep friends updated.

---

### #1950 — Amin (Topic Author)
*September 14, 2023, 12:36 PM*

Friends, when I was able to think of correlations between hermite polynomials and subsequent regression that included
higher hermite polynomials, I had also realized that similar correlations are possible between Legendre polynomials(of
the same degree across related variables)and many other polynomials and we could do regression with many polynomials
just like we did regression with hermite polynomials.

Every kind of polynomials can be used in some different context and have their advantages and limitations with different
kind of data. For example it would require a very huge number of higher order Legendre polynomials to try fitting a
Gaussian curve. So Hermite regressions are natural for normal-like data and the data that is related to transformations
of normal density so trying Legendre polynomials where Hermite polynomials are natural would be a very bad idea.

But still I believe that there are a large number of cases where Legendre regression would be most natural and similarly
for many other types polynomials (with their kind of data).

For example if we are able to solve backward parabolic equations of the type that arise in mathematical finance with
Legendre polynomials, we could find orthogonal representation of various greeks in terms Legendre polynomial series. And
we could also possibly find correlations between Legendre polynomials(of same order) of various greeks and finally could
do a Legendre regression of final payoffs on various Legendre series representation of various greeks (that accounts for
Legendre polynomial correlations between different greeks).

These are just rough ideas and some of these things might be more difficult in practice and easier said than done but
this is really worth trying.

I would also try to find solution of backward equations after brainstorming various aspects of the problems. I would be
very happy if friends try the ideas on their own in the meantime and implement/publish the results of their independent
research. I would simply try doing something interesting on my own at the same time and keep posting my research here on
the forum.

---

[← Previous](page_038.md) | [Index](index.md) | [Next →](page_040.md)
