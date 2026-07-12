# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 51 of 59** — Posts #2501–#2550

[← Previous](page_050.md) | [Index](index.md) | [Next →](page_052.md)

---

### #2501 — Amin (Topic Author)
*October 27, 2024, 6:21 PM*

Friends, I am posting R-squared and comparative plots of a few densities. This first generic method is based on
regression on five parameters + one approximate variance calculated variable. It is slightly worse than math functions
based method which takes different terms in second order expansion of the SDE as input regressors associated with
Legendre polynomials. This method based method also takes more input regressors since it is based on seven input
regressors and all valid cross products while generic method was based on six regressors and all possible products.

Following is the R-squared of eight coefficients being regressed and square root of volatility. Especially I noticed
that densities with much smaller variance were more off than acceptable while SDE densities with larger variance were
better captured. May be we should partition them based on approximate expected variance of the densities.

ans =

   0.999750950938112

ans =

   0.999476351505810

ans =

   0.999773123631771

ans =

   0.998041704817963

ans =

   0.983615526327305

ans =

   0.892801522152766

ans =

   0.959603004708574

ans =

   0.980390891487215

ans =

   0.999445401730034

[![Image](../images/i.postimg.cc/TwGV1y5h/Math-AIDens01.png)](https://postimg.cc/f32tgRKh)

[![Image](../images/i.postimg.cc/FK0bhbR2/Math-AIDens02.png)](https://postimg.cc/1g5VHqDH)

[![Image](../images/i.postimg.cc/T3zq8NRV/Math-AIDens03.png)](https://postimg.cc/0zCJDfKj)

[![Image](../images/i.postimg.cc/2SbFKNfj/Math-AIDens04.png)](https://postimg.cc/FYvLYqRw)

[![Image](../images/i.postimg.cc/ncwG2cgw/Math-AIDens05.png)](https://postimg.cc/3dmGJ7Kg)

[![Image](../images/i.postimg.cc/ZKqL6y7d/Math-AIDens06.png)](https://postimg.cc/fk6XNkhz)

[![Image](../images/i.postimg.cc/RCdR3TRm/Math-AIDens07.png)](https://postimg.cc/kDV8zKzY)

[![Image](../images/i.postimg.cc/d35mzq13/Math-AIDens08.png)](https://postimg.cc/xNbzmVLV)

[![Image](../images/i.postimg.cc/RhSLs3v2/Math-AIDens09.png)](https://postimg.cc/WFyZt1F7)

[![Image](../images/i.postimg.cc/1tcKr01p/Math-AIDens10.png)](https://postimg.cc/zbvWJgBB)

[![Image](../images/i.postimg.cc/xCSRmxhf/Math-AIDens11.png)](https://postimg.cc/VSDnQRzp)

[![Image](../images/i.postimg.cc/bvngsc6V/Math-AIDens12.png)](https://postimg.cc/KKZBHVht)

[![Image](../images/i.postimg.cc/bwWLyNR2/Math-AIDens13.png)](https://postimg.cc/G4PvzRVc)

[![Image](../images/i.postimg.cc/HsSBNtcz/Math-AIDens14.png)](https://postimg.cc/SJM62CGY)

[![Image](../images/i.postimg.cc/4xmBRhpg/Math-AIDens15.png)](https://postimg.cc/Xr6wwq2H)

[![Image](../images/i.postimg.cc/hP42MYjh/Math-AIDens16.png)](https://postimg.cc/F1qbHD0Q)

[![Image](../images/i.postimg.cc/rsjQM1h8/Math-AIDens17.png)](https://postimg.cc/gLwvKZF5)

[![Image](../images/i.postimg.cc/d3w4bHjH/Math-AIDens18.png)](https://postimg.cc/ZBs83Lgp)

[![Image](../images/i.postimg.cc/gJvgBF8L/Math-AIDens19.png)](https://postimg.cc/2bSdVtHC)

[![Image](../images/i.postimg.cc/XNk2fWnT/Math-AIDens20.png)](https://postimg.cc/MXXbwhMD)

---

### #2502 — Amin (Topic Author)
*October 27, 2024, 6:28 PM*

Friends, I am posting R-squared and comparative plots of a few densities for math functions based method which takes
different terms in second order expansion of the SDE as input regressors associated with Legendre polynomials. This
method based method also takes more input regressors since it is based on seven input regressors and all valid cross
products while generic method whose densities were shown in previous post was based on six regressors and all possible
products.

Please give me some time to clean up and arrange the code with comments and I would be posting matlab code used for
plots in both these posts in a little bit.

ans =

   0.999411947382876

ans =

   0.999666154021517

ans =

   0.999639745967184

ans =

   0.998678283503648

ans =

   0.995700552216255

ans =

   0.986820457358780

ans =

   0.968222081026967

ans =

   0.960706370429075

ans =

   0.999775148776510

[![Image](../images/i.postimg.cc/h43fXJHv/Math-AIDens-A01.png)](https://postimg.cc/4nVJM34R)

[![Image](../images/i.postimg.cc/2yJ6MJ4h/Math-AIDens-A02.png)](https://postimg.cc/XBf4ys1Y)

[![Image](../images/i.postimg.cc/wM3MWHs9/Math-AIDens-A03.png)](https://postimg.cc/GTwb2WQf)

[![Image](../images/i.postimg.cc/cHF6M6CD/Math-AIDens-A04.png)](https://postimg.cc/gX6YGzvR)

[![Image](../images/i.postimg.cc/j5xL7yxw/Math-AIDens-A05.png)](https://postimg.cc/Tysd8LWf)

[![Image](../images/i.postimg.cc/pdYmrsHM/Math-AIDens-A06.png)](https://postimg.cc/v1TYSLT0)

[![Image](../images/i.postimg.cc/5tMHfZDm/Math-AIDens-A07.png)](https://postimg.cc/75mPVQHC)

[![Image](../images/i.postimg.cc/52zYdxK0/Math-AIDens-A08.png)](https://postimg.cc/fVwTYhNn)

[![Image](../images/i.postimg.cc/X7mGzZ8m/Math-AIDens-A09.png)](https://postimg.cc/tYd4148N)

[![Image](../images/i.postimg.cc/wxWsD4s6/Math-AIDens-A10.png)](https://postimg.cc/t7xTj55f)

[![Image](../images/i.postimg.cc/HsV8z0Qb/Math-AIDens-A11.png)](https://postimg.cc/2VN58Z95)

[![Image](../images/i.postimg.cc/x8FJYqSk/Math-AIDens-A12.png)](https://postimg.cc/BPHQBSbs)

[![Image](../images/i.postimg.cc/PJqpBY0s/Math-AIDens-A13.png)](https://postimg.cc/TLZ3bLRC)

[![Image](../images/i.postimg.cc/V6g0GDGW/Math-AIDens-A14.png)](https://postimg.cc/hzJGhbqX)

[![Image](../images/i.postimg.cc/50bFSZ3t/Math-AIDens-A15.png)](https://postimg.cc/8FX51Xx8)

[![Image](../images/i.postimg.cc/TPrDmRnS/Math-AIDens-A16.png)](https://postimg.cc/jWS2YYgQ)

[![Image](../images/i.postimg.cc/3wMGdy0m/Math-AIDens-A17.png)](https://postimg.cc/21wytSwS)

[![Image](../images/i.postimg.cc/9QwTmP0c/Math-AIDens-A18.png)](https://postimg.cc/zy53pgTQ)

[![Image](../images/i.postimg.cc/286hJNfb/Math-AIDens-A19.png)](https://postimg.cc/6Tk82Sqt)

[![Image](../images/i.postimg.cc/y6n0vY2C/Math-AIDens-A20.png)](https://postimg.cc/rz0dpc8f)

---

### #2503 — Amin (Topic Author)
*October 27, 2024, 7:19 PM*

Friends, sorry that I am a bit tired and cannot write comments on programs as I had a very bad sleep today. I will
surely post the programs used to make density plots by tomorrow evening Pakistan time. I am trying to go to sleep now
and hope I can sleep well. As always, I will definitely post the programs at my earliest as soon as I can make the code
a bit organized and write comments.

---

### #2504 — Amin (Topic Author)
*October 28, 2024, 5:40 PM*

I am posting all new or changed functions to run the Math AI based program in previous post. When you run this, you
should get the exact  results and graphs from previous last post. For functions not given, please look at posts in past
three weeks.

.

.

.

```
function [] = SDEsWithMathAIMain08E2()

%The mean reverting SDE is given as
%dY(t)= kappa (theta - Y(t)) dt + sigma Y(t)^gamma dZ(t)
%Y(0) = y0

%We specify Low and High SDE parameters range below.
kappaL=.25;%Lower range of kappa
kappaH=3;%Upper range of kappa
thetaL=.5;%Lower range of theta
thetaH=2;%Upper range of theta
y0L=.5;%Lower range of y0
y0H=2;%Higher range of y0
gammaL=.5;%Lower range of gamma
gammaH=1;%Higher range of gamma
sigmaL=.1;
sigmaH=1.0;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Below five sets of uniform random numbers are sampled in batches of one
%thousand. These random numbers are later mapped on five input parameters
%over the their range previously defined.
%Sampling is done in batches of thousands since I wanted to first simulate
%one thousand SDEs and later continue to add more batches of thousand SDEs
%without spoiling the data of earlier batches from random number sequence.
%Since I was doing antithetic sampling, I did it at level of local batches
%of thousand.

seed=83098561;
rng(seed);
MM=2;    %No of Batches of simulation
NN0=1000;%Scenarios in each batch.
NN=MM*NN0;%Number of SDE runs in the training sample. Ideally would be much larger.

for mm=1:MM
    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand1((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand1((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand2((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand2((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand3((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand3((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand4((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand4((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand5((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand5((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

end

kappaU(1:NN)=kappaL+(kappaH-kappaL).*Rand1(1:NN,1);%Map unifrom random variates on kappa.

thetaU(1:NN)=thetaL+(thetaH-thetaL).*Rand2(1:NN,1);%Map unifrom random variates on theta.

y0U(1:NN)=y0L+(y0H-y0L).*Rand3(1:NN,1);%Map unifrom random variates on starting value of the SDE.

gammaU(1:NN)=gammaL+(gammaH-gammaL).*Rand4(1:NN,1);%Map unifrom random variates on gamma.

sigmaU(1:NN)=sigmaL+(sigmaH-sigmaL).*Rand5(1:NN,1);%Taking sigma at mid of upper and lower range.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

SDEpaths=200000;
MOrder=16;     %Order of moment matching of standard normal random numbers for simulation in SDEs
Order=7;       %Order of hermite series that is used to represent SDE densities.

%alphas below are used for moment matching of normal random numbers.
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

%ZI is a 16 moment matched version of discretized standard normal density
%with 200000 elements. This would be used for both hermite regressions and
%monte carlo simulations.

[W] = EvalHermiteArrayH0(ZI,Order);
% W is a matrix that contains hermite polynomials evaluated at discretized
% version of standard normal density. This matrix is used for finding
% hermite series coefficients of densities of SDEs.
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Below, we define time parameters of monte carlo simulation of SDEs.

seed0=90728436;
rng(seed0, 'combRecursive')
TtM=256*2;  %Terminal time for SDE simulation, here four years.
dtM=1/64/2; %time step size for monte carlo simulations.
dt=dtM;
Sfrequency=16;%The density of every 16th time step is sampled and all
%sampled densities till terminal time are returned in a matrix.
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
%if(nn>NN0) %This commented if would have to be used to specify that only
%parameters with index nn greater than 1000 would be simulated etc.
 [coeff] =
MeanRevertingMonteCarloDensity04New(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,Sfrequency);
 %[coeff,coeff2] =
MeanRevertingMonteCarloDensity04(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,W2);
 Coeff(1:Order+1,1:TtM/Sfrequency,nn)=coeff(1:Order+1,1:TtM/Sfrequency);
%end

end

save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC0.mat","Coeff")
str=input("I have saved the densities coefficients variable--Stop");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%You can comment the SDE simulations loop and continue to load the
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.

%Below is my code since I was making monte carlo simulations in batches of 1000 and
%saved each batch in a different file on disk.

%load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC.mat","Coeff")
%str=input("I have loaded the densities coefficients variable");

%Coeff0=Coeff;

%load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC2.mat","Coeff")
%str=input("I have loaded the densities coefficients variable");

%Coeff2=Coeff;

%Coeff(1:Order+1,1:TtM/Sfrequency,1:1000)=Coeff0(1:Order+1,1:TtM/Sfrequency,1:1000);
%Coeff(1:Order+1,1:TtM/Sfrequency,1001:2000)=Coeff2(1:Order+1,1:TtM/Sfrequency,1001:2000);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Dimensions of Coeff are Coeff(,1:Order+1,1:TtM/Sfrequency,1:NN).

%Below we choose one time slice between 1 and TtM for finding coefficients
%of hermite series from Legendre regression. I have taken slice 18 that occurs at time
%18*Sfrequency*dtM. Please choose different time slices and see how the
%program works.

%
%TimeSlice variable below
Ts=13;
CoeffH0(1:Order+1,1:NN)=Coeff(1:Order+1,Ts,1:NN);%Hermite series coefficients at time slice chosen for analytics.
CoeffH=transpose(CoeffH0);

% clf;
%
% plot((1:NN),CoeffH(1:NN,2),'g');
%
% str=input("Look at coeffs plot --Z1 coeff");

TT=Ts*dtM*Sfrequency;%Time at end of chosen slice. This will be used in analytic calculation of SDE mean later.
%We will replace the first mean coefficient of zeroth hermite associated
%with the Hermite series of SDEs with the analytic value.

%Below we calculate square root of variance(sum of hermite coefficients squared formula) to standardize the coefficients
VarSqRt(1:NN,1)=
sqrt(CoeffH(1:NN,2).^2+CoeffH(1:NN,3).^2*2+CoeffH(1:NN,4).^2*6+CoeffH(1:NN,5).^2*24+CoeffH(1:NN,6).^2*120+CoeffH(1:NN,7).^2*720+CoeffH(1:NN,8).^2*7*720);
%Below are six standardized coefficients

SHCoeff(1:NN,1:8)=CoeffH(1:NN,1:8)./VarSqRt(1:NN,1);
% SHCoeff stands for standardized hermite series coefficients.

str=input("Reached Level 1");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

OrderL=9;

[Q1,Q2,Q3,Q4,Q5,Q6] = CalculateMathBasedRegressors(kappaU,thetaU,y0U,gammaU,sigmaU,NN);
%The above routine calculates analytic SDE simulation equation terms based six regressors
% for each of the NN scenarios. These are time independent and can be used
% for every time slice.

[Q7] = CalculateApproximateVarianceOfMRSDEs(kappaU,thetaU,y0U,gammaU,sigmaU,NN,Ts,Sfrequency,dt);
%The above is approximate variance of the SDE and its value for each of the
%NN parameters scenarios is used as seventh regressor in Legendre
%polynomial regression. This variable is time dependent and has to be
%recalculated for each time slice.

[WL] = CalculateLegendrePolynomialDesignMatrix(Q1,Q2,Q3,Q4,Q5,Q6,Q7,OrderL);

for qq=1:8
    Yl(1:NN,qq)=SHCoeff(1:NN,qq); %First six standardized hermite coefficients to be predicted.
end
Yl(1:NN,9)=VarSqRt(1:NN,1);%Square root of variance used to standardize has to be predicted as well.

CoeffL=inv(WL'*WL)*(WL'*Yl);%Legendre coefficients to predict seven variables. six standardized coefficients
%and one square root of variance of each SDE.

str=input("Look if there is matlab warning about ill conditioned matrix inversion");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% clf;
% [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,1),NN,25,10 )
% plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
% str=input("Look at density of 1st coeff")
%
% [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,2),NN,25,10 )
% plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
% str=input("Look at density of 2nd coeff")
%
% %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%CoeffL
%size(WL)
%size(CoeffL)
%str=input("Look at size of CoeffL");

OrderL0=OrderL+1;

%bhs: Regressed value of standardized hermite coefficients produced from Legendre Regression %
bhs(1:NN,1:8)=0;   %
%RegressedVarSqRt: Regressed value of square root of volatility produced from Legendre Regression
RegressedVarSqRt(1:NN,1)=0;

%Below calculate hermite coefficients by regressing on Legendre polynomials
% with all calculated Legendre coefficients and polynomials evaluated at
% input data values used to find Legendre coefficients. This is in-sample
% testing only.

for rr=1:OrderL0+126*OrderL
    bhs(1:NN,1:8)=bhs(1:NN,1:8)+CoeffL(rr,1:8).*WL(1:NN,rr);
    RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffL(rr,9).*WL(1:NN,rr);
end

%Below are seven calculations of R-squared for each of
%the standardized six coefficients and seventh value of square root of variance.
1-sum((SHCoeff(:,1)-bhs(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)
1-sum((VarSqRt(:,1)-RegressedVarSqRt(:,1)).^2)/sum((VarSqRt(:,1)-sum(VarSqRt(:,1))/(NN)).^2)

str=input("Look at R^2s of eight standardized hermite series coefficients and ninth square root of variance");

%Since all coefficents were standardized before regression, Hermite series densities
%calculated from them should have variance one. However, variance would be slightly
%different from one after Legendre regression. So we calculate this
%variance of each hermite series density in regression.
VarSqRtbhs(1:NN,1)=
sqrt(bhs(1:NN,2).^2+bhs(1:NN,3).^2*2+bhs(1:NN,4).^2*6+bhs(1:NN,5).^2*24+bhs(1:NN,6).^2*120+bhs(1:NN,7).^2*720+bhs(1:NN,8).^2*7*720);

%bhs0 is re-standardized estimates of predicted from regression values of hermite series coefficients
bhs0(1:NN,1)=bhs(1:NN,1);
%Restandardization below to make sure that we get unit variance of each of
%the hermite series density.
bhs0(1:NN,2:8)=bhs(1:NN,2:8)./VarSqRtbhs(1:NN,1);

1-sum((SHCoeff(:,1)-bhs0(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs0(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs0(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs0(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs0(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs0(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs0(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs0(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)

str=input("Look at R^2s of first eight standardized hermite series coefficients");

%Below plot each of the in-sample densities and re-calculate them from
%Legendre regression and make an overlaid comparison.
for nn=1:NN

    %de-standardize by multiplying with square root of variance of each
    %density and get actual predicted coefficients of hermite-series of SDE
    %densities
    ch(1:8)=bhs0(nn,1:8).*RegressedVarSqRt(nn,1);

    %Below we repeat the same step for original Hermite series data found
    %from simulation. These are true values of hermite series coefficients and not predicted values.
    HCoeff(1:8)=SHCoeff(nn,1:8).*VarSqRt(nn);

    ch(1)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));%Replacing predicted value of mean with analytic value.

    ch(1:8)
    HCoeff(1:8)

    nn
    str=input("Look at predicted coefficients above and true coefficietns below for nnth SDE in data: First
coefficent(mean of SDE) in predicted values has been replaced by its analytic known value")

    clf;
    nn
    PlotHermiteSeriesDensityAndRvGraph(ch(1),ch(2:Order+1),'r');

    hold on

    PlotHermiteSeriesDensityAndRvGraph(HCoeff(1),HCoeff(2:Order+1),'g');
    nn

    str=input("Look at comparison of graphs of nnth density in sample--Green is data and red is our regression from
Legendre Polynomial coefficients");
    clf;
end

end

```

.

.

.

```
function [WL] = CalculateLegendrePolynomialDesignMatrix(Q1,Q2,Q3,Q4,Q5,Q6,Q7,OrderL)

%This function takes seven arrays/regressors input at joint data values in the same
%sequence. And returnd a Legendre polynomials design matrix with all Legendre polynomials
%evaluated at their data values and their possible product values.
%You can use it anywhere in other problems if there are seven regressors.

OrderL0=OrderL+1;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

[Wl1,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1,OrderL);

[Wl2,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2,OrderL);

[Wl3,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3,OrderL);

[Wl4,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4,OrderL);

[Wl5,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q5,OrderL);

[Wl6,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q6,OrderL);

[Wl7,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q7,OrderL);

[Wl12,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2,OrderL);

[Wl13,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3,OrderL);

[Wl14,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4,OrderL);

[Wl15,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q5,OrderL);

[Wl16,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q6,OrderL);

[Wl17,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q7,OrderL);

[Wl23,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3,OrderL);

[Wl24,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4,OrderL);

[Wl25,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q5,OrderL);

[Wl26,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q6,OrderL);

[Wl27,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q7,OrderL);

[Wl34,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4,OrderL);

[Wl35,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q5,OrderL);

[Wl36,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q6,OrderL);

[Wl37,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q7,OrderL);

[Wl45,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4.*Q5,OrderL);

[Wl46,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4.*Q6,OrderL);

[Wl47,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4.*Q7,OrderL);

[Wl56,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q5.*Q6,OrderL);

[Wl57,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q5.*Q7,OrderL);

[Wl67,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q6.*Q7,OrderL);

[Wl123,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3,OrderL);

[Wl124,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4,OrderL);

[Wl125,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q5,OrderL);

[Wl126,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q6,OrderL);

[Wl127,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q7,OrderL);

[Wl134,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4,OrderL);

[Wl135,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q5,OrderL);

[Wl136,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q6,OrderL);

[Wl137,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q7,OrderL);

[Wl145,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4.*Q5,OrderL);

[Wl146,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4.*Q6,OrderL);

[Wl147,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4.*Q7,OrderL);

[Wl156,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q5.*Q6,OrderL);

[Wl157,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q5.*Q7,OrderL);

[Wl167,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q6.*Q7,OrderL);

[Wl234,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4,OrderL);

[Wl235,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q5,OrderL);

[Wl236,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q6,OrderL);

[Wl237,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q7,OrderL);

[Wl245,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4.*Q5,OrderL);

[Wl246,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4.*Q6,OrderL);

[Wl247,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4.*Q7,OrderL);

[Wl256,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q5.*Q6,OrderL);

[Wl257,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q5.*Q7,OrderL);

[Wl267,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q6.*Q7,OrderL);

[Wl345,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4.*Q5,OrderL);

[Wl346,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4.*Q6,OrderL);

[Wl347,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4.*Q7,OrderL);

[Wl356,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q5.*Q6,OrderL);

[Wl357,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q5.*Q7,OrderL);

[Wl367,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q6.*Q7,OrderL);

[Wl456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4.*Q5.*Q6,OrderL);

[Wl457,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4.*Q5.*Q7,OrderL);

[Wl467,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4.*Q6.*Q7,OrderL);

[Wl567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q5.*Q6.*Q7,OrderL);

[Wl1234,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4,OrderL);

[Wl1235,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q5,OrderL);

[Wl1236,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q6,OrderL);

[Wl1237,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q7,OrderL);

[Wl1245,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4.*Q5,OrderL);

[Wl1246,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4.*Q6,OrderL);

[Wl1247,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4.*Q7,OrderL);

[Wl1256,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q5.*Q6,OrderL);

[Wl1257,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q5.*Q7,OrderL);

[Wl1267,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q6.*Q7,OrderL);

[Wl1345,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4.*Q5,OrderL);

[Wl1346,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4.*Q6,OrderL);

[Wl1347,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4.*Q7,OrderL);

[Wl1356,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q5.*Q6,OrderL);

[Wl1357,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q5.*Q7,OrderL);

[Wl1367,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q6.*Q7,OrderL);

[Wl1456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4.*Q5.*Q6,OrderL);

[Wl1457,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4.*Q5.*Q7,OrderL);

[Wl1467,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4.*Q6.*Q7,OrderL);

[Wl1567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q5.*Q6.*Q7,OrderL);

[Wl2345,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4.*Q5,OrderL);

[Wl2346,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4.*Q6,OrderL);

[Wl2347,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4.*Q7,OrderL);

[Wl2356,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q5.*Q6,OrderL);

[Wl2357,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q5.*Q7,OrderL);

[Wl2367,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q6.*Q7,OrderL);

[Wl2456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4.*Q5.*Q6,OrderL);

[Wl2457,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4.*Q5.*Q7,OrderL);

[Wl2467,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4.*Q6.*Q7,OrderL);

[Wl2567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q5.*Q6.*Q7,OrderL);

[Wl3456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4.*Q5.*Q6,OrderL);

[Wl3457,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4.*Q5.*Q7,OrderL);

[Wl3467,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4.*Q6.*Q7,OrderL);

[Wl3567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q5.*Q6.*Q7,OrderL);

[Wl4567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4.*Q5.*Q6.*Q7,OrderL);

[Wl12345,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4.*Q5,OrderL);

[Wl12346,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4.*Q6,OrderL);

[Wl12347,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4.*Q7,OrderL);

[Wl12356,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q5.*Q6,OrderL);

[Wl12357,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q5.*Q7,OrderL);

[Wl12367,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q6.*Q7,OrderL);

[Wl12456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4.*Q5.*Q6,OrderL);

[Wl12457,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4.*Q5.*Q7,OrderL);

[Wl12467,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4.*Q6.*Q7,OrderL);

[Wl12567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q5.*Q6.*Q7,OrderL);

[Wl13456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4.*Q5.*Q6,OrderL);

[Wl13457,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4.*Q5.*Q7,OrderL);

[Wl13467,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4.*Q6.*Q7,OrderL);

[Wl13567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q5.*Q6.*Q7,OrderL);

[Wl14567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl23456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4.*Q5.*Q6,OrderL);

[Wl23457,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4.*Q5.*Q7,OrderL);

[Wl23467,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4.*Q6.*Q7,OrderL);

[Wl23567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q5.*Q6.*Q7,OrderL);

[Wl24567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl34567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl123456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4.*Q5.*Q6,OrderL);

[Wl123457,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4.*Q5.*Q7,OrderL);

[Wl123467,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4.*Q6.*Q7,OrderL);

[Wl123567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q5.*Q6.*Q7,OrderL);

[Wl124567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl134567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl234567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl1234567,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4.*Q5.*Q6.*Q7,OrderL);

%Below Tile all of the Legendre polynomials of each of the four random
%parameters in a single matrix and use for least square regression. Zeroth
%Legendre is evaluated in each of the four matrices and has to be removed
%from tiling other than just including one time.
WL(:,1:OrderL0)=Wl1(:,1:OrderL0);
WL(:,OrderL0+1:OrderL0+OrderL)=Wl2(:,2:OrderL0);
WL(:,OrderL0+OrderL+1:OrderL0+2*OrderL)=Wl3(:,2:OrderL0);
WL(:,OrderL0+2*OrderL+1:OrderL0+3*OrderL)=Wl4(:,2:OrderL0);
WL(:,OrderL0+3*OrderL+1:OrderL0+4*OrderL)=Wl5(:,2:OrderL0);
WL(:,OrderL0+4*OrderL+1:OrderL0+5*OrderL)=Wl6(:,2:OrderL0);
WL(:,OrderL0+5*OrderL+1:OrderL0+6*OrderL)=Wl7(:,2:OrderL0);

WL(:,OrderL0+6*OrderL+1:OrderL0+7*OrderL)=Wl12(:,2:OrderL0);
WL(:,OrderL0+7*OrderL+1:OrderL0+8*OrderL)=Wl13(:,2:OrderL0);
WL(:,OrderL0+8*OrderL+1:OrderL0+9*OrderL)=Wl14(:,2:OrderL0);
WL(:,OrderL0+9*OrderL+1:OrderL0+10*OrderL)=Wl15(:,2:OrderL0);
WL(:,OrderL0+10*OrderL+1:OrderL0+11*OrderL)=Wl16(:,2:OrderL0);
WL(:,OrderL0+11*OrderL+1:OrderL0+12*OrderL)=Wl17(:,2:OrderL0);

WL(:,OrderL0+12*OrderL+1:OrderL0+13*OrderL)=Wl23(:,2:OrderL0);
WL(:,OrderL0+13*OrderL+1:OrderL0+14*OrderL)=Wl24(:,2:OrderL0);
WL(:,OrderL0+14*OrderL+1:OrderL0+15*OrderL)=Wl25(:,2:OrderL0);
WL(:,OrderL0+15*OrderL+1:OrderL0+16*OrderL)=Wl26(:,2:OrderL0);
WL(:,OrderL0+16*OrderL+1:OrderL0+17*OrderL)=Wl27(:,2:OrderL0);

WL(:,OrderL0+17*OrderL+1:OrderL0+18*OrderL)=Wl34(:,2:OrderL0);
WL(:,OrderL0+18*OrderL+1:OrderL0+19*OrderL)=Wl35(:,2:OrderL0);
WL(:,OrderL0+19*OrderL+1:OrderL0+20*OrderL)=Wl36(:,2:OrderL0);
WL(:,OrderL0+20*OrderL+1:OrderL0+21*OrderL)=Wl37(:,2:OrderL0);

WL(:,OrderL0+21*OrderL+1:OrderL0+22*OrderL)=Wl45(:,2:OrderL0);
WL(:,OrderL0+22*OrderL+1:OrderL0+23*OrderL)=Wl46(:,2:OrderL0);
WL(:,OrderL0+23*OrderL+1:OrderL0+24*OrderL)=Wl47(:,2:OrderL0);

WL(:,OrderL0+24*OrderL+1:OrderL0+25*OrderL)=Wl56(:,2:OrderL0);
WL(:,OrderL0+25*OrderL+1:OrderL0+26*OrderL)=Wl57(:,2:OrderL0);

WL(:,OrderL0+26*OrderL+1:OrderL0+27*OrderL)=Wl67(:,2:OrderL0);

WL(:,OrderL0+27*OrderL+1:OrderL0+28*OrderL)=Wl123(:,2:OrderL0);
WL(:,OrderL0+28*OrderL+1:OrderL0+29*OrderL)=Wl124(:,2:OrderL0);
WL(:,OrderL0+29*OrderL+1:OrderL0+30*OrderL)=Wl125(:,2:OrderL0);
WL(:,OrderL0+30*OrderL+1:OrderL0+31*OrderL)=Wl126(:,2:OrderL0);
WL(:,OrderL0+31*OrderL+1:OrderL0+32*OrderL)=Wl127(:,2:OrderL0);

WL(:,OrderL0+32*OrderL+1:OrderL0+33*OrderL)=Wl134(:,2:OrderL0);
WL(:,OrderL0+33*OrderL+1:OrderL0+34*OrderL)=Wl135(:,2:OrderL0);
WL(:,OrderL0+34*OrderL+1:OrderL0+35*OrderL)=Wl136(:,2:OrderL0);
WL(:,OrderL0+35*OrderL+1:OrderL0+36*OrderL)=Wl137(:,2:OrderL0);

WL(:,OrderL0+36*OrderL+1:OrderL0+37*OrderL)=Wl145(:,2:OrderL0);
WL(:,OrderL0+37*OrderL+1:OrderL0+38*OrderL)=Wl146(:,2:OrderL0);
WL(:,OrderL0+38*OrderL+1:OrderL0+39*OrderL)=Wl147(:,2:OrderL0);

WL(:,OrderL0+39*OrderL+1:OrderL0+40*OrderL)=Wl156(:,2:OrderL0);
WL(:,OrderL0+40*OrderL+1:OrderL0+41*OrderL)=Wl157(:,2:OrderL0);

WL(:,OrderL0+41*OrderL+1:OrderL0+42*OrderL)=Wl167(:,2:OrderL0);

WL(:,OrderL0+42*OrderL+1:OrderL0+43*OrderL)=Wl234(:,2:OrderL0);
WL(:,OrderL0+43*OrderL+1:OrderL0+44*OrderL)=Wl235(:,2:OrderL0);
WL(:,OrderL0+44*OrderL+1:OrderL0+45*OrderL)=Wl236(:,2:OrderL0);
WL(:,OrderL0+45*OrderL+1:OrderL0+46*OrderL)=Wl237(:,2:OrderL0);

WL(:,OrderL0+46*OrderL+1:OrderL0+47*OrderL)=Wl245(:,2:OrderL0);
WL(:,OrderL0+47*OrderL+1:OrderL0+48*OrderL)=Wl246(:,2:OrderL0);
WL(:,OrderL0+48*OrderL+1:OrderL0+49*OrderL)=Wl247(:,2:OrderL0);

WL(:,OrderL0+49*OrderL+1:OrderL0+50*OrderL)=Wl256(:,2:OrderL0);
WL(:,OrderL0+50*OrderL+1:OrderL0+51*OrderL)=Wl257(:,2:OrderL0);

WL(:,OrderL0+51*OrderL+1:OrderL0+52*OrderL)=Wl267(:,2:OrderL0);

WL(:,OrderL0+52*OrderL+1:OrderL0+53*OrderL)=Wl345(:,2:OrderL0);
WL(:,OrderL0+53*OrderL+1:OrderL0+54*OrderL)=Wl346(:,2:OrderL0);
WL(:,OrderL0+54*OrderL+1:OrderL0+55*OrderL)=Wl347(:,2:OrderL0);

WL(:,OrderL0+55*OrderL+1:OrderL0+56*OrderL)=Wl356(:,2:OrderL0);
WL(:,OrderL0+56*OrderL+1:OrderL0+57*OrderL)=Wl357(:,2:OrderL0);

WL(:,OrderL0+57*OrderL+1:OrderL0+58*OrderL)=Wl367(:,2:OrderL0);

WL(:,OrderL0+58*OrderL+1:OrderL0+59*OrderL)=Wl456(:,2:OrderL0);
WL(:,OrderL0+59*OrderL+1:OrderL0+60*OrderL)=Wl457(:,2:OrderL0);

WL(:,OrderL0+60*OrderL+1:OrderL0+61*OrderL)=Wl467(:,2:OrderL0);

WL(:,OrderL0+61*OrderL+1:OrderL0+62*OrderL)=Wl567(:,2:OrderL0);

WL(:,OrderL0+62*OrderL+1:OrderL0+63*OrderL)=Wl1234(:,2:OrderL0);
WL(:,OrderL0+63*OrderL+1:OrderL0+64*OrderL)=Wl1235(:,2:OrderL0);
WL(:,OrderL0+64*OrderL+1:OrderL0+65*OrderL)=Wl1236(:,2:OrderL0);
WL(:,OrderL0+65*OrderL+1:OrderL0+66*OrderL)=Wl1237(:,2:OrderL0);

WL(:,OrderL0+66*OrderL+1:OrderL0+67*OrderL)=Wl1245(:,2:OrderL0);
WL(:,OrderL0+67*OrderL+1:OrderL0+68*OrderL)=Wl1246(:,2:OrderL0);
WL(:,OrderL0+68*OrderL+1:OrderL0+69*OrderL)=Wl1247(:,2:OrderL0);

WL(:,OrderL0+69*OrderL+1:OrderL0+70*OrderL)=Wl1256(:,2:OrderL0);
WL(:,OrderL0+70*OrderL+1:OrderL0+71*OrderL)=Wl1257(:,2:OrderL0);

WL(:,OrderL0+71*OrderL+1:OrderL0+72*OrderL)=Wl1267(:,2:OrderL0);

WL(:,OrderL0+72*OrderL+1:OrderL0+73*OrderL)=Wl1345(:,2:OrderL0);
WL(:,OrderL0+73*OrderL+1:OrderL0+74*OrderL)=Wl1346(:,2:OrderL0);
WL(:,OrderL0+74*OrderL+1:OrderL0+75*OrderL)=Wl1347(:,2:OrderL0);

WL(:,OrderL0+75*OrderL+1:OrderL0+76*OrderL)=Wl1356(:,2:OrderL0);
WL(:,OrderL0+76*OrderL+1:OrderL0+77*OrderL)=Wl1357(:,2:OrderL0);

WL(:,OrderL0+77*OrderL+1:OrderL0+78*OrderL)=Wl1367(:,2:OrderL0);

WL(:,OrderL0+78*OrderL+1:OrderL0+79*OrderL)=Wl1456(:,2:OrderL0);
WL(:,OrderL0+79*OrderL+1:OrderL0+80*OrderL)=Wl1457(:,2:OrderL0);

WL(:,OrderL0+80*OrderL+1:OrderL0+81*OrderL)=Wl1467(:,2:OrderL0);

WL(:,OrderL0+81*OrderL+1:OrderL0+82*OrderL)=Wl1567(:,2:OrderL0);

WL(:,OrderL0+82*OrderL+1:OrderL0+83*OrderL)=Wl2345(:,2:OrderL0);
WL(:,OrderL0+83*OrderL+1:OrderL0+84*OrderL)=Wl2346(:,2:OrderL0);
WL(:,OrderL0+84*OrderL+1:OrderL0+85*OrderL)=Wl2347(:,2:OrderL0);

WL(:,OrderL0+85*OrderL+1:OrderL0+86*OrderL)=Wl2356(:,2:OrderL0);
WL(:,OrderL0+86*OrderL+1:OrderL0+87*OrderL)=Wl2357(:,2:OrderL0);

WL(:,OrderL0+87*OrderL+1:OrderL0+88*OrderL)=Wl2367(:,2:OrderL0);

WL(:,OrderL0+88*OrderL+1:OrderL0+89*OrderL)=Wl2456(:,2:OrderL0);
WL(:,OrderL0+89*OrderL+1:OrderL0+90*OrderL)=Wl2457(:,2:OrderL0);

WL(:,OrderL0+90*OrderL+1:OrderL0+91*OrderL)=Wl2467(:,2:OrderL0);

WL(:,OrderL0+91*OrderL+1:OrderL0+92*OrderL)=Wl2567(:,2:OrderL0);

WL(:,OrderL0+92*OrderL+1:OrderL0+93*OrderL)=Wl3456(:,2:OrderL0);
WL(:,OrderL0+93*OrderL+1:OrderL0+94*OrderL)=Wl3457(:,2:OrderL0);

WL(:,OrderL0+94*OrderL+1:OrderL0+95*OrderL)=Wl3467(:,2:OrderL0);

WL(:,OrderL0+95*OrderL+1:OrderL0+96*OrderL)=Wl3567(:,2:OrderL0);

WL(:,OrderL0+96*OrderL+1:OrderL0+97*OrderL)=Wl4567(:,2:OrderL0);

WL(:,OrderL0+97*OrderL+1:OrderL0+98*OrderL)=Wl12345(:,2:OrderL0);
WL(:,OrderL0+98*OrderL+1:OrderL0+99*OrderL)=Wl12346(:,2:OrderL0);
WL(:,OrderL0+99*OrderL+1:OrderL0+100*OrderL)=Wl12347(:,2:OrderL0);

WL(:,OrderL0+100*OrderL+1:OrderL0+101*OrderL)=Wl12356(:,2:OrderL0);
WL(:,OrderL0+101*OrderL+1:OrderL0+102*OrderL)=Wl12357(:,2:OrderL0);

WL(:,OrderL0+102*OrderL+1:OrderL0+103*OrderL)=Wl12367(:,2:OrderL0);

WL(:,OrderL0+103*OrderL+1:OrderL0+104*OrderL)=Wl12456(:,2:OrderL0);
WL(:,OrderL0+104*OrderL+1:OrderL0+105*OrderL)=Wl12457(:,2:OrderL0);

WL(:,OrderL0+105*OrderL+1:OrderL0+106*OrderL)=Wl12467(:,2:OrderL0);

WL(:,OrderL0+106*OrderL+1:OrderL0+107*OrderL)=Wl12567(:,2:OrderL0);

WL(:,OrderL0+107*OrderL+1:OrderL0+108*OrderL)=Wl13456(:,2:OrderL0);
WL(:,OrderL0+108*OrderL+1:OrderL0+109*OrderL)=Wl13457(:,2:OrderL0);

WL(:,OrderL0+109*OrderL+1:OrderL0+110*OrderL)=Wl13467(:,2:OrderL0);

WL(:,OrderL0+110*OrderL+1:OrderL0+111*OrderL)=Wl13567(:,2:OrderL0);

WL(:,OrderL0+111*OrderL+1:OrderL0+112*OrderL)=Wl14567(:,2:OrderL0);

WL(:,OrderL0+112*OrderL+1:OrderL0+113*OrderL)=Wl23456(:,2:OrderL0);
WL(:,OrderL0+113*OrderL+1:OrderL0+114*OrderL)=Wl23457(:,2:OrderL0);

WL(:,OrderL0+114*OrderL+1:OrderL0+115*OrderL)=Wl23467(:,2:OrderL0);

WL(:,OrderL0+115*OrderL+1:OrderL0+116*OrderL)=Wl23567(:,2:OrderL0);

WL(:,OrderL0+116*OrderL+1:OrderL0+117*OrderL)=Wl24567(:,2:OrderL0);

WL(:,OrderL0+117*OrderL+1:OrderL0+118*OrderL)=Wl34567(:,2:OrderL0);

WL(:,OrderL0+118*OrderL+1:OrderL0+119*OrderL)=Wl123456(:,2:OrderL0);
WL(:,OrderL0+119*OrderL+1:OrderL0+120*OrderL)=Wl123457(:,2:OrderL0);

WL(:,OrderL0+120*OrderL+1:OrderL0+121*OrderL)=Wl123467(:,2:OrderL0);

WL(:,OrderL0+121*OrderL+1:OrderL0+122*OrderL)=Wl123567(:,2:OrderL0);

WL(:,OrderL0+122*OrderL+1:OrderL0+123*OrderL)=Wl124567(:,2:OrderL0);

WL(:,OrderL0+123*OrderL+1:OrderL0+124*OrderL)=Wl134567(:,2:OrderL0);

WL(:,OrderL0+124*OrderL+1:OrderL0+125*OrderL)=Wl234567(:,2:OrderL0);

WL(:,OrderL0+125*OrderL+1:OrderL0+126*OrderL)=Wl1234567(:,2:OrderL0);

end

```

.

.

.

```
function [Q1,Q2,Q3,Q4,Q5,Q6] = CalculateMathBasedRegressors(kappaU,thetaU,y0U,gammaU,sigmaU,NN)

%This SDE problem specific code routine generates Math based regressors
%that are actually different terms in second order monte carlo simulation of SDEs.
%These values would be mapped on uniform and then Legendre polynomials
%evaluated at these uniform values would be used in Legendre polynomial
%regression.

for nn=1:NN

    beta1=0;
    beta2=1;
    mu1=kappaU(nn).*thetaU(nn);
    mu2=-kappaU(nn);
    V0=y0U(nn);
    gamma=gammaU(nn);
    sigma0=sigmaU(nn);

    dtA=1;%Ts.*Sfrequency*dt;Time is set at one.

   Q1(nn)=thetaU(nn)+ exp(-kappaU(nn)*dtA).*(V0-thetaU(nn));
   Q2(nn)=sigma0*V0.^gamma .*sqrt(dtA);
   Q3(nn)=(mu1.*beta1*V0.^(beta1-1) + mu2.*beta2.*V0.^(beta2-1)).* ...
        (sigma0*V0.^gamma .*(1-1/sqrt(3))*dtA^1.5);
   Q4(nn)=sigma0*gamma*V0.^(gamma-1) .* ...
        ((mu1.*V0.^beta1 + mu2.*V0.^beta2).*1/sqrt(3)*dtA^1.5);
   Q5(nn)=sigma0*gamma*V0.^(gamma-1) .* ...
        (sigma0.*V0.^gamma .*dtA/2);
   Q6(nn)=.5*sigma0*gamma*(gamma-1).*V0.^(gamma-2) .* ...
        sigma0^2.*V0.^(2*gamma) .*1/sqrt(3)*dtA^1.5;

end

end

```

.

.

.

```
function [Var] = CalculateApproximateVarianceOfMRSDEs(kappaU,thetaU,y0U,gammaU,sigmaU,NN,Ts,Sfrequency,dt)

%This function calculates approximate variance of mean reverting SDEs.

Var(1:NN)=0;
V2g(1:NN)=0;%variable for V^(2*gamma)
for tt=1:Ts* Sfrequency %
    V1(1:NN)=thetaU(1:NN)+exp(-kappaU(1:NN)*tt*dt).*(y0U(1:NN)-thetaU(1:NN));
   
Var(1:NN)=Var(1:NN)+1./(2*kappaU(1:NN)).*(exp(2*kappaU(1:NN)*tt*dt)-exp(2*kappaU(1:NN).*(tt-1)*dt)).*(V1(1:NN).^(2*gammaU(1:NN))+V2g(1:NN)).*sigmaU(1:NN).^2;
    Var2(1:NN)=Var(1:NN).*exp(-2*kappaU(1:NN)*tt*dt);
    V2g(1:NN)=V2g(1:NN)+(2*gammaU(1:NN)-1).*V1(1:NN).^(.5*gammaU(1:NN)-1).*sigmaU(1:NN).^2*dt.*(Var2(1:NN));
end

Var(1:NN)=exp(-2*kappaU(1:NN).*Ts.*Sfrequency*dt).*Var(1:NN);

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
%Threshold=(sigma0*sqrt(dt)*sqrt(2/pi))^(1/(1-gamma));
Threshold=(sigma0*sqrt(dt)*2)^(1/(1-gamma));
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

---

### #2505 — Amin (Topic Author)
*October 28, 2024, 7:05 PM*

Friends, this is a second program with generic regressors that are parameters of the SDE. It employs only six
variables/parameters for regression. But it has only half free parameters than the math based regressors program in
previous post that was employing seven variables and their products.

I am using only 2000 simulated SDEs sample which seems insufficient.

Here is the program.

.

.

.

```
function [] = SDEsWithMathAIMain08D2()

%The mean reverting SDE is given as
%dY(t)= kappa (theta - Y(t)) dt + sigma Y(t)^gamma dZ(t)
%Y(0) = y0

%We specify Low and High SDE parameters range below.
kappaL=.25;%Lower range of kappa
kappaH=3;%Upper range of kappa
thetaL=.5;%Lower range of theta
thetaH=2;%Upper range of theta
y0L=.5;%Lower range of y0
y0H=2;%Higher range of y0
gammaL=.5;%Lower range of gamma
gammaH=1;%Higher range of gamma
sigmaL=.1;
sigmaH=1.0;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Below five sets of uniform random numbers are sampled in batches of one
%thousand. These random numbers are later mapped on five input parameters
%over the their range previously defined.
%Sampling is done in batches of thousands since I wanted to first simulate
%one thousand SDEs and later continue to add more batches of thousand SDEs
%without spoiling the data of earlier batches from random number sequence.
%Since I was doing antithetic sampling, I did it at level of local batches
%of thousand.

seed=83098561;
rng(seed);
MM=2;    %No of Batches of simulation
NN0=1000;%Scenarios in each batch.
NN=MM*NN0;%Number of SDE runs in the training sample. Ideally would be much larger.

for mm=1:MM
    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand1((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand1((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand2((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand2((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand3((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand3((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand4((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand4((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand5((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand5((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

end

kappaU(1:NN)=kappaL+(kappaH-kappaL).*Rand1(1:NN,1);%Map unifrom random variates on kappa.

thetaU(1:NN)=thetaL+(thetaH-thetaL).*Rand2(1:NN,1);%Map unifrom random variates on theta.

y0U(1:NN)=y0L+(y0H-y0L).*Rand3(1:NN,1);%Map unifrom random variates on starting value of the SDE.

gammaU(1:NN)=gammaL+(gammaH-gammaL).*Rand4(1:NN,1);%Map unifrom random variates on gamma.

sigmaU(1:NN)=sigmaL+(sigmaH-sigmaL).*Rand5(1:NN,1);%Taking sigma at mid of upper and lower range.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

SDEpaths=200000;
MOrder=16;     %Order of moment matching of standard normal random numbers for simulation in SDEs
Order=7;       %Order of hermite series that is used to represent SDE densities.

%alphas below are used for moment matching of normal random numbers.
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

%ZI is a 16 moment matched version of discretized standard normal density
%with 200000 elements. This would be used for both hermite regressions and
%monte carlo simulations.

[W] = EvalHermiteArrayH0(ZI,Order);
% W is a matrix that contains hermite polynomials evaluated at discretized
% version of standard normal density. This matrix is used for finding
% hermite series coefficients of densities of SDEs.
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Below, we define time parameters of monte carlo simulation of SDEs.

seed0=90728436;
rng(seed0, 'combRecursive')
TtM=256*2;  %Terminal time for SDE simulation, here four years.
dtM=1/64/2; %time step size for monte carlo simulations.
dt=dtM;
Sfrequency=16;%The density of every 16th time step is sampled and all
%sampled densities till terminal time are returned in a matrix.
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
%if(nn>NN0) %This commented if would have to be used to specify that only
%parameters with index nn greater than 1000 would be simulated etc.
 [coeff] =
MeanRevertingMonteCarloDensity04New(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,Sfrequency);
 %[coeff,coeff2] =
MeanRevertingMonteCarloDensity04(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,W2);
 Coeff(1:Order+1,1:TtM/Sfrequency,nn)=coeff(1:Order+1,1:TtM/Sfrequency);
%end

end

save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC0.mat","Coeff")
str=input("I have saved the densities coefficients variable--Stop");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%You can comment the SDE simulations loop and continue to load the
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.

%Below is my code since I was making monte carlo simulations in batches of 1000 and
%saved each batch in a different file on disk.

% load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC.mat","Coeff")
% str=input("I have loaded the densities coefficients variable");
%
% Coeff0=Coeff;
%
% load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC2.mat","Coeff")
% str=input("I have loaded the densities coefficients variable");
%
% Coeff2=Coeff;
%
% Coeff(1:Order+1,1:TtM/Sfrequency,1:1000)=Coeff0(1:Order+1,1:TtM/Sfrequency,1:1000);
% Coeff(1:Order+1,1:TtM/Sfrequency,1001:2000)=Coeff2(1:Order+1,1:TtM/Sfrequency,1001:2000);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Dimensions of Coeff are Coeff(,1:Order+1,1:TtM/Sfrequency,1:NN).

%Below we choose one time slice between 1 and TtM for finding coefficients
%of hermite series from Legendre regression. I have taken slice 18 that occurs at time
%18*Sfrequency*dtM. Please choose different time slices and see how the
%program works.

%
%TimeSlice variable below
Ts=13;
CoeffH0(1:Order+1,1:NN)=Coeff(1:Order+1,Ts,1:NN);%Hermite series coefficients at time slice chosen for analytics.
CoeffH=transpose(CoeffH0);

% clf;
%
% plot((1:NN),CoeffH(1:NN,2),'g');
%
% str=input("Look at coeffs plot --Z1 coeff");

TT=Ts*dtM*Sfrequency;%Time at end of chosen slice. This will be used in analytic calculation of SDE mean later.
%We will replace the first mean coefficient of zeroth hermite associated
%with the Hermite series of SDEs with the analytic value.

%Below we calculate square root of variance(sum of hermite coefficients squared formula) to standardize the coefficients
VarSqRt(1:NN,1)=
sqrt(CoeffH(1:NN,2).^2+CoeffH(1:NN,3).^2*2+CoeffH(1:NN,4).^2*6+CoeffH(1:NN,5).^2*24+CoeffH(1:NN,6).^2*120+CoeffH(1:NN,7).^2*720+CoeffH(1:NN,8).^2*7*720);
%Below are six standardized coefficients

SHCoeff(1:NN,1:8)=CoeffH(1:NN,1:8)./VarSqRt(1:NN,1);
% SHCoeff stands for standardized hermite series coefficients.

str=input("Reached Level 1");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

OrderL=9;

Q1=kappaU;
Q2=thetaU;
Q3=y0U;
Q4=gammaU;
Q5=sigmaU;

[Q6] = CalculateApproximateVarianceOfMRSDEs(kappaU,thetaU,y0U,gammaU,sigmaU,NN,Ts,Sfrequency,dt);
%The above is approximate variance of the SDE and its value for each of the
%NN parameters scenarios is used as seventh regressor in Legendre
%polynomial regression. This variable is time dependent and has to be
%recalculated for each time slice.

[WL] = CalculateLegendrePolynomialDesignMatrixQ6(Q1,Q2,Q3,Q4,Q5,Q6,OrderL);

for qq=1:8
    Yl(1:NN,qq)=SHCoeff(1:NN,qq); %First six standardized hermite coefficients to be predicted.
end
Yl(1:NN,9)=VarSqRt(1:NN,1);%Square root of variance used to standardize has to be predicted as well.

CoeffL=inv(WL'*WL)*(WL'*Yl);%Legendre coefficients to predict seven variables. six standardized coefficients
%and one square root of variance of each SDE.

str=input("Look if there is matlab warning about ill conditioned matrix inversion");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% clf;
% [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,1),NN,25,10 )
% plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
% str=input("Look at density of 1st coeff")
%
% [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,2),NN,25,10 )
% plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
% str=input("Look at density of 2nd coeff")
%
% %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%CoeffL
%size(WL)
%size(CoeffL)
%str=input("Look at size of CoeffL");

OrderL0=OrderL+1;

%bhs: Regressed value of standardized hermite coefficients produced from Legendre Regression %
bhs(1:NN,1:8)=0;   %
%RegressedVarSqRt: Regressed value of square root of volatility produced from Legendre Regression
RegressedVarSqRt(1:NN,1)=0;

%Below calculate hermite coefficients by regressing on Legendre polynomials
% with all calculated Legendre coefficients and polynomials evaluated at
% input data values used to find Legendre coefficients. This is in-sample
% testing only.

for rr=1:OrderL0+62*OrderL
    bhs(1:NN,1:8)=bhs(1:NN,1:8)+CoeffL(rr,1:8).*WL(1:NN,rr);
    RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffL(rr,9).*WL(1:NN,rr);
end

%Below are seven calculations of R-squared for each of
%the standardized six coefficients and seventh value of square root of variance.
1-sum((SHCoeff(:,1)-bhs(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)
1-sum((VarSqRt(:,1)-RegressedVarSqRt(:,1)).^2)/sum((VarSqRt(:,1)-sum(VarSqRt(:,1))/(NN)).^2)

str=input("Look at R^2s of eight standardized hermite series coefficients and ninth square root of variance");

%Since all coefficents were standardized before regression, Hermite series densities
%calculated from them should have variance one. However, variance would be slightly
%different from one after Legendre regression. So we calculate this
%variance of each hermite series density in regression.
VarSqRtbhs(1:NN,1)=
sqrt(bhs(1:NN,2).^2+bhs(1:NN,3).^2*2+bhs(1:NN,4).^2*6+bhs(1:NN,5).^2*24+bhs(1:NN,6).^2*120+bhs(1:NN,7).^2*720+bhs(1:NN,8).^2*7*720);

%bhs0 is re-standardized estimates of predicted from regression values of hermite series coefficients
bhs0(1:NN,1)=bhs(1:NN,1);
%Restandardization below to make sure that we get unit variance of each of
%the hermite series density.
bhs0(1:NN,2:8)=bhs(1:NN,2:8)./VarSqRtbhs(1:NN,1);

1-sum((SHCoeff(:,1)-bhs0(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs0(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs0(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs0(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs0(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs0(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs0(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs0(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)

str=input("Look at R^2s of first eight standardized hermite series coefficients");

%Below plot each of the in-sample densities and re-calculate them from
%Legendre regression and make an overlaid comparison.
for nn=1:NN

    %de-standardize by multiplying with square root of variance of each
    %density and get actual predicted coefficients of hermite-series of SDE
    %densities
    ch(1:8)=bhs0(nn,1:8).*RegressedVarSqRt(nn,1);

    %Below we repeat the same step for original Hermite series data found
    %from simulation. These are true values of hermite series coefficients and not predicted values.
    HCoeff(1:8)=SHCoeff(nn,1:8).*VarSqRt(nn);

    ch(1)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));%Replacing predicted value of mean with analytic value.

    ch(1:8)
    HCoeff(1:8)

    nn
    str=input("Look at predicted coefficients above and true coefficietns below for nnth SDE in data: First
coefficent(mean of SDE) in predicted values has been replaced by its analytic known value")

    clf;
    nn
    PlotHermiteSeriesDensityAndRvGraph(ch(1),ch(2:Order+1),'r');

    hold on

    PlotHermiteSeriesDensityAndRvGraph(HCoeff(1),HCoeff(2:Order+1),'g');
    nn

    str=input("Look at comparison of graphs of nnth density in sample--Green is data and red is our regression from
Legendre Polynomial coefficients");
    clf;
end

end

```

.

.

.

```
function [WL] = CalculateLegendrePolynomialDesignMatrixQ6(Q1,Q2,Q3,Q4,Q5,Q6,OrderL)

%This function takes seven arrays/regressors input at joint data values in the same
%sequence. And returnd a Legendre polynomials design matrix with all Legendre polynomials
%evaluated at their data values and their possible product values.
%You can use it anywhere in other problems if there are seven regressors.

OrderL0=OrderL+1;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

[Wl1,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1,OrderL);

[Wl2,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2,OrderL);

[Wl3,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3,OrderL);

[Wl4,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4,OrderL);

[Wl5,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q5,OrderL);

[Wl6,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q6,OrderL);

[Wl12,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2,OrderL);

[Wl13,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3,OrderL);

[Wl14,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4,OrderL);

[Wl15,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q5,OrderL);

[Wl16,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q6,OrderL);

[Wl23,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3,OrderL);

[Wl24,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4,OrderL);

[Wl25,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q5,OrderL);

[Wl26,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q6,OrderL);

[Wl34,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4,OrderL);

[Wl35,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q5,OrderL);

[Wl36,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q6,OrderL);

[Wl45,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4.*Q5,OrderL);

[Wl46,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4.*Q6,OrderL);

[Wl56,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q5.*Q6,OrderL);

[Wl123,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3,OrderL);

[Wl124,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4,OrderL);

[Wl125,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q5,OrderL);

[Wl126,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q6,OrderL);

[Wl134,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4,OrderL);

[Wl135,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q5,OrderL);

[Wl136,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q6,OrderL);

[Wl145,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4.*Q5,OrderL);

[Wl146,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4.*Q6,OrderL);

[Wl156,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q5.*Q6,OrderL);

[Wl234,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4,OrderL);

[Wl235,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q5,OrderL);

[Wl236,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q6,OrderL);

[Wl245,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4.*Q5,OrderL);

[Wl246,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4.*Q6,OrderL);

[Wl256,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q5.*Q6,OrderL);

[Wl345,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4.*Q5,OrderL);

[Wl346,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4.*Q6,OrderL);

[Wl356,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q5.*Q6,OrderL);

[Wl456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q4.*Q5.*Q6,OrderL);

[Wl1234,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4,OrderL);

[Wl1235,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q5,OrderL);

[Wl1236,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q6,OrderL);

[Wl1245,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4.*Q5,OrderL);

[Wl1246,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4.*Q6,OrderL);

[Wl1256,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q5.*Q6,OrderL);

[Wl1345,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4.*Q5,OrderL);

[Wl1346,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4.*Q6,OrderL);

[Wl1356,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q5.*Q6,OrderL);

[Wl1456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q4.*Q5.*Q6,OrderL);

[Wl2345,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4.*Q5,OrderL);

[Wl2346,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4.*Q6,OrderL);

[Wl2356,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q5.*Q6,OrderL);

[Wl2456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q4.*Q5.*Q6,OrderL);

[Wl3456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q3.*Q4.*Q5.*Q6,OrderL);

[Wl12345,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4.*Q5,OrderL);

[Wl12346,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4.*Q6,OrderL);

[Wl12356,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q5.*Q6,OrderL);

[Wl12456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q4.*Q5.*Q6,OrderL);

[Wl13456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q3.*Q4.*Q5.*Q6,OrderL);

[Wl23456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q2.*Q3.*Q4.*Q5.*Q6,OrderL);

[Wl123456,Uy] = CalculateLegendreSeriesAndReturnLegendreArray(Q1.*Q2.*Q3.*Q4.*Q5.*Q6,OrderL);

%Below Tile all of the Legendre polynomials of each of the four random
%parameters in a single matrix and use for least square regression. Zeroth
%Legendre is evaluated in each of the four matrices and has to be removed
%from tiling other than just including one time.
WL(:,1:OrderL0)=Wl1(:,1:OrderL0);
WL(:,OrderL0+1:OrderL0+OrderL)=Wl2(:,2:OrderL0);
WL(:,OrderL0+OrderL+1:OrderL0+2*OrderL)=Wl3(:,2:OrderL0);
WL(:,OrderL0+2*OrderL+1:OrderL0+3*OrderL)=Wl4(:,2:OrderL0);
WL(:,OrderL0+3*OrderL+1:OrderL0+4*OrderL)=Wl5(:,2:OrderL0);
WL(:,OrderL0+4*OrderL+1:OrderL0+5*OrderL)=Wl6(:,2:OrderL0);

WL(:,OrderL0+5*OrderL+1:OrderL0+6*OrderL)=Wl12(:,2:OrderL0);
WL(:,OrderL0+6*OrderL+1:OrderL0+7*OrderL)=Wl13(:,2:OrderL0);
WL(:,OrderL0+7*OrderL+1:OrderL0+8*OrderL)=Wl14(:,2:OrderL0);
WL(:,OrderL0+8*OrderL+1:OrderL0+9*OrderL)=Wl15(:,2:OrderL0);
WL(:,OrderL0+9*OrderL+1:OrderL0+10*OrderL)=Wl16(:,2:OrderL0);

WL(:,OrderL0+10*OrderL+1:OrderL0+11*OrderL)=Wl23(:,2:OrderL0);
WL(:,OrderL0+11*OrderL+1:OrderL0+12*OrderL)=Wl24(:,2:OrderL0);
WL(:,OrderL0+12*OrderL+1:OrderL0+13*OrderL)=Wl25(:,2:OrderL0);
WL(:,OrderL0+13*OrderL+1:OrderL0+14*OrderL)=Wl26(:,2:OrderL0);

WL(:,OrderL0+14*OrderL+1:OrderL0+15*OrderL)=Wl34(:,2:OrderL0);
WL(:,OrderL0+15*OrderL+1:OrderL0+16*OrderL)=Wl35(:,2:OrderL0);
WL(:,OrderL0+16*OrderL+1:OrderL0+17*OrderL)=Wl36(:,2:OrderL0);

WL(:,OrderL0+17*OrderL+1:OrderL0+18*OrderL)=Wl45(:,2:OrderL0);
WL(:,OrderL0+18*OrderL+1:OrderL0+19*OrderL)=Wl46(:,2:OrderL0);

WL(:,OrderL0+19*OrderL+1:OrderL0+20*OrderL)=Wl56(:,2:OrderL0);

WL(:,OrderL0+20*OrderL+1:OrderL0+21*OrderL)=Wl123(:,2:OrderL0);
WL(:,OrderL0+21*OrderL+1:OrderL0+22*OrderL)=Wl124(:,2:OrderL0);
WL(:,OrderL0+22*OrderL+1:OrderL0+23*OrderL)=Wl125(:,2:OrderL0);
WL(:,OrderL0+23*OrderL+1:OrderL0+24*OrderL)=Wl126(:,2:OrderL0);

WL(:,OrderL0+24*OrderL+1:OrderL0+25*OrderL)=Wl134(:,2:OrderL0);
WL(:,OrderL0+25*OrderL+1:OrderL0+26*OrderL)=Wl135(:,2:OrderL0);
WL(:,OrderL0+26*OrderL+1:OrderL0+27*OrderL)=Wl136(:,2:OrderL0);

WL(:,OrderL0+27*OrderL+1:OrderL0+28*OrderL)=Wl145(:,2:OrderL0);
WL(:,OrderL0+28*OrderL+1:OrderL0+29*OrderL)=Wl146(:,2:OrderL0);

WL(:,OrderL0+29*OrderL+1:OrderL0+30*OrderL)=Wl156(:,2:OrderL0);

WL(:,OrderL0+30*OrderL+1:OrderL0+31*OrderL)=Wl234(:,2:OrderL0);
WL(:,OrderL0+31*OrderL+1:OrderL0+32*OrderL)=Wl235(:,2:OrderL0);
WL(:,OrderL0+32*OrderL+1:OrderL0+33*OrderL)=Wl236(:,2:OrderL0);

WL(:,OrderL0+33*OrderL+1:OrderL0+34*OrderL)=Wl245(:,2:OrderL0);
WL(:,OrderL0+34*OrderL+1:OrderL0+35*OrderL)=Wl246(:,2:OrderL0);

WL(:,OrderL0+35*OrderL+1:OrderL0+36*OrderL)=Wl256(:,2:OrderL0);

WL(:,OrderL0+36*OrderL+1:OrderL0+37*OrderL)=Wl345(:,2:OrderL0);
WL(:,OrderL0+37*OrderL+1:OrderL0+38*OrderL)=Wl346(:,2:OrderL0);

WL(:,OrderL0+38*OrderL+1:OrderL0+39*OrderL)=Wl356(:,2:OrderL0);

WL(:,OrderL0+39*OrderL+1:OrderL0+40*OrderL)=Wl456(:,2:OrderL0);

WL(:,OrderL0+40*OrderL+1:OrderL0+41*OrderL)=Wl1234(:,2:OrderL0);
WL(:,OrderL0+41*OrderL+1:OrderL0+42*OrderL)=Wl1235(:,2:OrderL0);
WL(:,OrderL0+42*OrderL+1:OrderL0+43*OrderL)=Wl1236(:,2:OrderL0);

WL(:,OrderL0+43*OrderL+1:OrderL0+44*OrderL)=Wl1245(:,2:OrderL0);
WL(:,OrderL0+44*OrderL+1:OrderL0+45*OrderL)=Wl1246(:,2:OrderL0);

WL(:,OrderL0+45*OrderL+1:OrderL0+46*OrderL)=Wl1256(:,2:OrderL0);

WL(:,OrderL0+46*OrderL+1:OrderL0+47*OrderL)=Wl1345(:,2:OrderL0);
WL(:,OrderL0+47*OrderL+1:OrderL0+48*OrderL)=Wl1346(:,2:OrderL0);

WL(:,OrderL0+48*OrderL+1:OrderL0+49*OrderL)=Wl1356(:,2:OrderL0);

WL(:,OrderL0+49*OrderL+1:OrderL0+50*OrderL)=Wl1456(:,2:OrderL0);

WL(:,OrderL0+50*OrderL+1:OrderL0+51*OrderL)=Wl2345(:,2:OrderL0);
WL(:,OrderL0+51*OrderL+1:OrderL0+52*OrderL)=Wl2346(:,2:OrderL0);

WL(:,OrderL0+52*OrderL+1:OrderL0+53*OrderL)=Wl2356(:,2:OrderL0);

WL(:,OrderL0+53*OrderL+1:OrderL0+54*OrderL)=Wl2456(:,2:OrderL0);

WL(:,OrderL0+54*OrderL+1:OrderL0+55*OrderL)=Wl3456(:,2:OrderL0);

WL(:,OrderL0+55*OrderL+1:OrderL0+56*OrderL)=Wl12345(:,2:OrderL0);
WL(:,OrderL0+56*OrderL+1:OrderL0+57*OrderL)=Wl12346(:,2:OrderL0);

WL(:,OrderL0+57*OrderL+1:OrderL0+58*OrderL)=Wl12356(:,2:OrderL0);

WL(:,OrderL0+58*OrderL+1:OrderL0+59*OrderL)=Wl12456(:,2:OrderL0);

WL(:,OrderL0+59*OrderL+1:OrderL0+60*OrderL)=Wl13456(:,2:OrderL0);

WL(:,OrderL0+60*OrderL+1:OrderL0+61*OrderL)=Wl23456(:,2:OrderL0);

WL(:,OrderL0+61*OrderL+1:OrderL0+62*OrderL)=Wl123456(:,2:OrderL0);

end

```

---

### #2506 — Amin (Topic Author)
*October 29, 2024, 4:30 PM*

Friends, I came up with a slightly different version of initial regressors that work well with increasing size of sample
and maintain high R-squared. I tried them for 4000 SDEs sample.

.

.

.

```
function [] = SDEsWithMathAIMain08E4()

%The mean reverting SDE is given as
%dY(t)= kappa (theta - Y(t)) dt + sigma Y(t)^gamma dZ(t)
%Y(0) = y0

%We specify Low and High SDE parameters range below.
kappaL=.25;%Lower range of kappa
kappaH=3;%Upper range of kappa
thetaL=.5;%Lower range of theta
thetaH=2;%Upper range of theta
y0L=.5;%Lower range of y0
y0H=2;%Higher range of y0
gammaL=.5;%Lower range of gamma
gammaH=1;%Higher range of gamma
sigmaL=.1;
sigmaH=1.0;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Below five sets of uniform random numbers are sampled in batches of one
%thousand. These random numbers are later mapped on five input parameters
%over the their range previously defined.
%Sampling is done in batches of thousands since I wanted to first simulate
%one thousand SDEs and later continue to add more batches of thousand SDEs
%without spoiling the data of earlier batches from random number sequence.
%Since I was doing antithetic sampling, I did it at level of local batches
%of thousand.

seed=83098561;
rng(seed);
MM=4;    %No of Batches of simulation
NN0=1000;%Scenarios in each batch.
NN=MM*NN0;%Number of SDE runs in the training sample. Ideally would be much larger.

for mm=1:MM
    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand1((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand1((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand2((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand2((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand3((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand3((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand4((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand4((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand5((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand5((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

end

kappaU(1:NN)=kappaL+(kappaH-kappaL).*Rand1(1:NN,1);%Map unifrom random variates on kappa.

thetaU(1:NN)=thetaL+(thetaH-thetaL).*Rand2(1:NN,1);%Map unifrom random variates on theta.

y0U(1:NN)=y0L+(y0H-y0L).*Rand3(1:NN,1);%Map unifrom random variates on starting value of the SDE.

gammaU(1:NN)=gammaL+(gammaH-gammaL).*Rand4(1:NN,1);%Map unifrom random variates on gamma.

sigmaU(1:NN)=sigmaL+(sigmaH-sigmaL).*Rand5(1:NN,1);%Taking sigma at mid of upper and lower range.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

SDEpaths=200000;
MOrder=16;     %Order of moment matching of standard normal random numbers for simulation in SDEs
Order=7;       %Order of hermite series that is used to represent SDE densities.

%alphas below are used for moment matching of normal random numbers.
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

%ZI is a 16 moment matched version of discretized standard normal density
%with 200000 elements. This would be used for both hermite regressions and
%monte carlo simulations.

[W] = EvalHermiteArrayH0(ZI,Order);
% W is a matrix that contains hermite polynomials evaluated at discretized
% version of standard normal density. This matrix is used for finding
% hermite series coefficients of densities of SDEs.
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Below, we define time parameters of monte carlo simulation of SDEs.

seed0=90728436;
rng(seed0, 'combRecursive')
TtM=256*2;  %Terminal time for SDE simulation, here four years.
dtM=1/64/2; %time step size for monte carlo simulations.
dt=dtM;
Sfrequency=16;%The density of every 16th time step is sampled and all
%sampled densities till terminal time are returned in a matrix.
Random0(1:SDEpaths,1:TtM)=0;

for tt=1:0%TtM
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

for nn=1:0%NN
 nn
 NN
if(nn>3*NN0) %This commented if would have to be used to specify that only
%parameters with index nn greater than 1000 would be simulated etc.
 [coeff] =
MeanRevertingMonteCarloDensity04New(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,Sfrequency);
 %[coeff,coeff2] =
MeanRevertingMonteCarloDensity04(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,W2);
 Coeff(1:Order+1,1:TtM/Sfrequency,nn)=coeff(1:Order+1,1:TtM/Sfrequency);
end

end

%save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC9a.mat","Coeff")
%str=input("I have saved the densities coefficients variable--Stop");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%You can comment the SDE simulations loop and continue to load the
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.

%Below is my code since I was making monte carlo simulations in batches of 1000 and
%saved each batch in a different file on disk.

load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC.mat","Coeff")
 str=input("I have loaded the densities coefficients variable");

 Coeff0=Coeff;

 load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC2.mat","Coeff")
 str=input("I have loaded the densities coefficients variable");

 Coeff2=Coeff;

 load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC4.mat","Coeff")
 str=input("I have loaded the densities coefficients variable");

 Coeff3=Coeff;

 load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC9.mat","Coeff")
 str=input("I have loaded the densities coefficients variable");

 Coeff4=Coeff;

 Coeff(1:Order+1,1:TtM/Sfrequency,1:1000)=Coeff0(1:Order+1,1:TtM/Sfrequency,1:1000);
 Coeff(1:Order+1,1:TtM/Sfrequency,1001:2000)=Coeff2(1:Order+1,1:TtM/Sfrequency,1001:2000);
 Coeff(1:Order+1,1:TtM/Sfrequency,2001:3000)=Coeff3(1:Order+1,1:TtM/Sfrequency,2001:3000);
 Coeff(1:Order+1,1:TtM/Sfrequency,3001:4000)=Coeff4(1:Order+1,1:TtM/Sfrequency,3001:4000);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Dimensions of Coeff are Coeff(,1:Order+1,1:TtM/Sfrequency,1:NN).

%Below we choose one time slice between 1 and TtM for finding coefficients
%of hermite series from Legendre regression. I have taken slice 18 that occurs at time
%18*Sfrequency*dtM. Please choose different time slices and see how the
%program works.

%
%TimeSlice variable below
Ts=13;
CoeffH0(1:Order+1,1:NN)=Coeff(1:Order+1,Ts,1:NN);%Hermite series coefficients at time slice chosen for analytics.
CoeffH=transpose(CoeffH0);

% clf;
%
% plot((1:NN),CoeffH(1:NN,2),'g');
%
% str=input("Look at coeffs plot --Z1 coeff");

TT=Ts*dtM*Sfrequency;%Time at end of chosen slice. This will be used in analytic calculation of SDE mean later.
%We will replace the first mean coefficient of zeroth hermite associated
%with the Hermite series of SDEs with the analytic value.

%Below we calculate square root of variance(sum of hermite coefficients squared formula) to standardize the coefficients
VarSqRt(1:NN,1)=
sqrt(CoeffH(1:NN,2).^2+CoeffH(1:NN,3).^2*2+CoeffH(1:NN,4).^2*6+CoeffH(1:NN,5).^2*24+CoeffH(1:NN,6).^2*120+CoeffH(1:NN,7).^2*720+CoeffH(1:NN,8).^2*7*720);
%Below are six standardized coefficients

SHCoeff(1:NN,1:8)=CoeffH(1:NN,1:8)./VarSqRt(1:NN,1);
% SHCoeff stands for standardized hermite series coefficients.

str=input("Reached Level 1");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

OrderL=9;

%[Q1,Q2,Q3,Q4,Q5,Q6] = CalculateMathBasedRegressors(kappaU,thetaU,y0U,gammaU,sigmaU,NN);
%The above routine calculates analytic SDE simulation equation terms based six regressors
% for each of the NN scenarios. These are time independent and can be used
% for every time slice.

for nn=1:NN

C(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
YT(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
Y0T(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
UU(nn)=C(nn).*Y0T(nn);
VV(nn)=C(nn).*YT(nn);
UV(nn)=UU(nn).*VV(nn);
qq(nn)=2*(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
BB(nn)=besseli(qq(nn),sqrt(UV(nn)));

%
%     Q1(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
% Q2(nn)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
% %Q3(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
% Q3(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
% Q4(nn)=sigmaU(nn);%.^2*(1-exp(-2*kappaU(nn)*TT))/2/kappaU(nn));
% Q5(nn)=gammaU(nn);
% %UV(nn)=
% %Q6(nn)=sqrt(sigmaU(nn).^2*(1-exp(-2*kappaU(nn)*TT))/2/kappaU(nn));
% Q6(nn)=BB(nn);
%

%  Q1(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
%  Q2(nn)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
%  Q3(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
%  Q4(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
%  Q5(nn)=gammaU(nn);
%  Q6(nn)=sqrt(UV(nn));

  Q1(nn)=C(nn).*YT(nn);
 Q2(nn)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
 Q3(nn)=C(nn).*Y0T(nn);
 Q4(nn)=gammaU(nn);
 Q5(nn)=sigmaU(nn);
 Q6(nn)=thetaU(nn);

end

[Q7] = CalculateApproximateVarianceOfMRSDEs(kappaU,thetaU,y0U,gammaU,sigmaU,NN,Ts,Sfrequency,dt);
%The above is approximate variance of the SDE and its value for each of the
%NN parameters scenarios is used as seventh regressor in Legendre
%polynomial regression. This variable is time dependent and has to be
%recalculated for each time slice.

[WL] = CalculateLegendrePolynomialDesignMatrix(Q1,Q2,Q3,Q4,Q5,Q6,Q7,OrderL);

for qq=1:8
    Yl(1:NN,qq)=SHCoeff(1:NN,qq); %First six standardized hermite coefficients to be predicted.
end
Yl(1:NN,9)=VarSqRt(1:NN,1);%Square root of variance used to standardize has to be predicted as well.

CoeffL=inv(WL'*WL)*(WL'*Yl);%Legendre coefficients to predict seven variables. six standardized coefficients
%and one square root of variance of each SDE.

str=input("Look if there is matlab warning about ill conditioned matrix inversion");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% clf;
% [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,1),NN,25,10 )
% plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
% str=input("Look at density of 1st coeff")
%
% [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,2),NN,25,10 )
% plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
% str=input("Look at density of 2nd coeff")
%
% %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%CoeffL
%size(WL)
%size(CoeffL)
%str=input("Look at size of CoeffL");

OrderL0=OrderL+1;

%bhs: Regressed value of standardized hermite coefficients produced from Legendre Regression %
bhs(1:NN,1:8)=0;   %
%RegressedVarSqRt: Regressed value of square root of volatility produced from Legendre Regression
RegressedVarSqRt(1:NN,1)=0;

%Below calculate hermite coefficients by regressing on Legendre polynomials
% with all calculated Legendre coefficients and polynomials evaluated at
% input data values used to find Legendre coefficients. This is in-sample
% testing only.

for rr=1:OrderL0+126*OrderL
    bhs(1:NN,1:8)=bhs(1:NN,1:8)+CoeffL(rr,1:8).*WL(1:NN,rr);
    RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffL(rr,9).*WL(1:NN,rr);
end

%Below are seven calculations of R-squared for each of
%the standardized six coefficients and seventh value of square root of variance.
1-sum((SHCoeff(:,1)-bhs(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)
1-sum((VarSqRt(:,1)-RegressedVarSqRt(:,1)).^2)/sum((VarSqRt(:,1)-sum(VarSqRt(:,1))/(NN)).^2)

str=input("Look at R^2s of eight standardized hermite series coefficients and ninth square root of variance");

%Since all coefficents were standardized before regression, Hermite series densities
%calculated from them should have variance one. However, variance would be slightly
%different from one after Legendre regression. So we calculate this
%variance of each hermite series density in regression.
VarSqRtbhs(1:NN,1)=
sqrt(bhs(1:NN,2).^2+bhs(1:NN,3).^2*2+bhs(1:NN,4).^2*6+bhs(1:NN,5).^2*24+bhs(1:NN,6).^2*120+bhs(1:NN,7).^2*720+bhs(1:NN,8).^2*7*720);

%bhs0 is re-standardized estimates of predicted from regression values of hermite series coefficients
bhs0(1:NN,1)=bhs(1:NN,1);
%Restandardization below to make sure that we get unit variance of each of
%the hermite series density.
bhs0(1:NN,2:8)=bhs(1:NN,2:8)./VarSqRtbhs(1:NN,1);

1-sum((SHCoeff(:,1)-bhs0(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs0(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs0(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs0(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs0(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs0(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs0(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs0(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)

str=input("Look at R^2s of first eight standardized hermite series coefficients");

%Below plot each of the in-sample densities and re-calculate them from
%Legendre regression and make an overlaid comparison.
for nn=1:NN

    %de-standardize by multiplying with square root of variance of each
    %density and get actual predicted coefficients of hermite-series of SDE
    %densities
    ch(1:8)=bhs0(nn,1:8).*RegressedVarSqRt(nn,1);

    %Below we repeat the same step for original Hermite series data found
    %from simulation. These are true values of hermite series coefficients and not predicted values.
    HCoeff(1:8)=SHCoeff(nn,1:8).*VarSqRt(nn);

    ch(1)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));%Replacing predicted value of mean with analytic value.

    ch(1:8)
    HCoeff(1:8)

    nn
    str=input("Look at predicted coefficients above and true coefficietns below for nnth SDE in data: First
coefficent(mean of SDE) in predicted values has been replaced by its analytic known value")

    clf;
    nn
    PlotHermiteSeriesDensityAndRvGraph(ch(1),ch(2:Order+1),'r');

    hold on

    PlotHermiteSeriesDensityAndRvGraph(HCoeff(1),HCoeff(2:Order+1),'g');
    nn

    str=input("Look at comparison of graphs of nnth density in sample--Green is data and red is our regression from
Legendre Polynomial coefficients");
    clf;
end

end

```

---

### #2507 — Amin (Topic Author)
*October 29, 2024, 5:57 PM*

Friends, mostly antipsychotic injections made by Lundbeck sold in Pakistan are filled with mind control chemicals. It's
been five days since I took the intramuscular injection shot and the injection has started to take effect already. I
have high anxiety from time to time and I am not in mentally good shape. It is however good that I had been able to do
some decent work in past few days. But I am worried that  I would not be able to work well for next few days. I will
also remove the strap on my hand to immobilize my thumb by 4-5 of next month. And I really hope that I would be able to
start working normally after that.

I really want to bring attention of friends to my continuing persecution. I usually do not drink milk at all but at
thumb fracture, I started to drink a lot of milk to get calcium as most calcium supplements are already drugged by
pharmaceutical companies. Most companies like Nestle, Olpers and most others (including many other high end companies
claiming australian cow milk) already sell milk that is drugged with mind control chemicals at manufacturing source.
However, there was this Adam's milk that had to be kept refrigerated and was available in only one Litre pack. I had
never tried it since one litre of milk was way too much for me and I would not be able to refrigerate it safely either.
But after my thumb fracture, I tried this Adam's milk and it was perfectly good and I started buying it everyday from
random places around the city. However within ten days after the fracture, Adam also started to distribute drugged milk.
And then I started drinking powdered milk made by Nestle for older school age children called Nestle Buniyad. However,
within two weeks of my fracture, most of the market was supplied with drugged Nestle Buniyad satchets and packs. And I
had to stop buying it and three days ago I bought Nestle Nido that is young age babies milk and it was good but i am
afraid that they might start distributing drugged Nestle Nido in the markets pretty soon.

Similalry, they distributed mind control chemicals to small milk shops in Johar town and surrounding areas that make
yogurt at the shop and large number of these shops started drugging their milk and yogurt so I had to stop taking yogurt
from them.

Similarly, I was getting ground water from filtration plants and other random places in remote parts of the city before
the thumb fracture. And they allowed bottled water to become better and both Nestle and Dasani (coke water) started
distributing good bottled water. However after thumb fracture, it was difficult for me to go to remote parts of city and
try to get good ground water and I had to start buying bottled water. Now nestle has started to supply drugged water in
the city again within 15 days after my fracture.

This is despite that my thumb was fractured and I was not in good shape at all and bitterly needed some high calcium
food.

On top of all this, they continue to release some mind control gas in my room at night that does not let me sleep well
and I am tired when I get up. Earlier when there would be gas in my room, I will place my cot directly in front of
window and sleep there. But lately, they have placed some gadget outside the window that continues to release gas and I
no longer get good fresh air from the window.

So life is really tough. I have to tell these things to friends so such practices end everywhere in the world. I am very
afraid if Trump got elected, many rich jews will ask him to take special interest in my persecution and whatever little
space and freedom I currently have might go away.

---

### #2508 — Amin (Topic Author)
*October 31, 2024, 3:30 PM*

Friends, I have been playing with the Math AI programs and I tried hermite regression on coefficients of hermite
polynomials of SDE densities instead of Legendre regression. And surprisingly I was able to get an R-squared (of square
root of variance of SDEs) of .9999 with six regressors and their products in hermite regression and I could get an
R-squared of more than .99995 with seven regressors and their products in hermite regression for 4000 SDE densities
sample. While earlier the best I could get was R-squared of .9997 for square root of variance for four thousand SDE
densities sample. This might seem like a small improvement but small error in the coefficients is magnified into a
larger error when densities are plotted. However with this new development, I could get very precise estimates of all
the coefficients of hermite polynomials of the densities of SDEs and mostly when original and polynomial constructed
densities are overlaid they are almost indistinguishable.

I want to play around with the programs a bit more and will post my matlab programs tomorrow.

---

### #2509 — Amin (Topic Author)
*October 31, 2024, 4:23 PM*

Friends, here are first 25 SDE densities reconstructed from Hermite regressions and mapped on the original SDE densities
in sample. In this matlab program, I have used hermite polynomial regression at secondary level instead of Legendre
regression. I simply mapped the regressors and their products on hermite polynomials and went ahead with least squares
regression.

Below are overlaid graphs of SDE densities reconstructed form hermite coefficients on two levels. True density is in
green and polynomial reconstructed density is in red and both are overlaid.

.

.

.

.

.

[![Image](../images/i.postimg.cc/DzxBSPMx/Math-AICF01.png)](https://postimg.cc/nsQv5BZm)

[![Image](../images/i.postimg.cc/5t4s9RnH/Math-AICF02.png)](https://postimg.cc/K1WPJJXF)

[![Image](../images/i.postimg.cc/sg9nrr9d/Math-AICF03.png)](https://postimg.cc/PCJbW0R2)

[![Image](../images/i.postimg.cc/NjwNSMXk/Math-AICF04.png)](https://postimg.cc/bs3H2q3Z)

[![Image](../images/i.postimg.cc/bNnCmbZv/Math-AICF05.png)](https://postimg.cc/9rWYMDt3)

[![Image](../images/i.postimg.cc/1RfYNbPw/Math-AICF06.png)](https://postimg.cc/yWCTMQD8)

[![Image](../images/i.postimg.cc/fWpq75TF/Math-AICF07.png)](https://postimg.cc/DmQcnrGd)

[![Image](../images/i.postimg.cc/grbn431R/Math-AICF08.png)](https://postimg.cc/tnDq4nqC)

[![Image](../images/i.postimg.cc/ydWgN1FJ/Math-AICF09.png)](https://postimg.cc/ZBtK7hsZ)

[![Image](../images/i.postimg.cc/HnyrQ6vd/Math-AICF10.png)](https://postimg.cc/jnRqT4rF)

[![Image](../images/i.postimg.cc/W3KDFBn5/Math-AICF11.png)](https://postimg.cc/MM7ZgrgB)

[![Image](../images/i.postimg.cc/HL68Hc7D/Math-AICF12.png)](https://postimg.cc/PL85Qq42)

[![Image](../images/i.postimg.cc/R0SJjQhL/Math-AICF13.png)](https://postimg.cc/HrNLMMQr)

[![Image](../images/i.postimg.cc/52qF7k4t/Math-AICF14.png)](https://postimg.cc/QFCtVmWL)

[![Image](../images/i.postimg.cc/FsSScHw3/Math-AICF15.png)](https://postimg.cc/GHc9ndLm)

[![Image](../images/i.postimg.cc/VkcCFccT/Math-AICF16.png)](https://postimg.cc/TpC1RF1q)

[![Image](../images/i.postimg.cc/jqmNL73R/Math-AICF17.png)](https://postimg.cc/Hj0jNVCN)

[![Image](../images/i.postimg.cc/zvsRMsHy/Math-AICF18.png)](https://postimg.cc/T5cw5H9x)

[![Image](../images/i.postimg.cc/prhFsWrN/Math-AICF19.png)](https://postimg.cc/T5x1wXnQ)

[![Image](../images/i.postimg.cc/PxFDbptz/Math-AICF20.png)](https://postimg.cc/HcXjdL8V)

[![Image](../images/i.postimg.cc/QtM5Wkrd/Math-AICF21.png)](https://postimg.cc/3yPWsGRs)

[![Image](../images/i.postimg.cc/Gpdvbn7Y/Math-AICF22.png)](https://postimg.cc/3kfkZVHJ)

[![Image](../images/i.postimg.cc/MG5VT3NL/Math-AICF23.png)](https://postimg.cc/jWWL3cs6)

[![Image](../images/i.postimg.cc/T38rHDnt/Math-AICF24.png)](https://postimg.cc/nCkjXMRm)

[![Image](../images/i.postimg.cc/wjhhKjVg/Math-AICF25.png)](https://postimg.cc/xX1kMYh4)

---

### #2510 — Amin (Topic Author)
*October 31, 2024, 4:45 PM*

Friends, here is the matlab program used to create graphs in previous post. Please look for all other files not posted
in previous posts of this thread. You will also need a text file named MomentMatchParams08.txt which I have earlier
posted on the forum. Please use search with file names.

.

.

.

```
function [] = SDEsWithMathAIMain08E4()

%The mean reverting SDE is given as
%dY(t)= kappa (theta - Y(t)) dt + sigma Y(t)^gamma dZ(t)
%Y(0) = y0

%We specify Low and High SDE parameters range below.
kappaL=.25;%Lower range of kappa
kappaH=3;%Upper range of kappa
thetaL=.5;%Lower range of theta
thetaH=2;%Upper range of theta
y0L=.5;%Lower range of y0
y0H=2;%Higher range of y0
gammaL=.5;%Lower range of gamma
gammaH=1;%Higher range of gamma
sigmaL=.1;
sigmaH=1.0;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Below five sets of uniform random numbers are sampled in batches of one
%thousand. These random numbers are later mapped on five input parameters
%over the their range previously defined.
%Sampling is done in batches of thousands since I wanted to first simulate
%one thousand SDEs and later continue to add more batches of thousand SDEs
%without spoiling the data of earlier batches from random number sequence.
%Since I was doing antithetic sampling, I did it at level of local batches
%of thousand.

seed=83098561;
rng(seed);
MM=4;    %No of Batches of simulation
NN0=1000;%Scenarios in each batch.
NN=MM*NN0;%Number of SDE runs in the training sample. Ideally would be much larger.

for mm=1:MM
    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand1((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand1((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand2((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand2((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand3((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand3((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand4((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand4((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand5((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand5((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

end

kappaU(1:NN)=kappaL+(kappaH-kappaL).*Rand1(1:NN,1);%Map unifrom random variates on kappa.

thetaU(1:NN)=thetaL+(thetaH-thetaL).*Rand2(1:NN,1);%Map unifrom random variates on theta.

y0U(1:NN)=y0L+(y0H-y0L).*Rand3(1:NN,1);%Map unifrom random variates on starting value of the SDE.

gammaU(1:NN)=gammaL+(gammaH-gammaL).*Rand4(1:NN,1);%Map unifrom random variates on gamma.

sigmaU(1:NN)=sigmaL+(sigmaH-sigmaL).*Rand5(1:NN,1);%Taking sigma at mid of upper and lower range.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

SDEpaths=200000;
MOrder=16;     %Order of moment matching of standard normal random numbers for simulation in SDEs
Order=7;       %Order of hermite series that is used to represent SDE densities.

%alphas below are used for moment matching of normal random numbers.
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

%ZI is a 16 moment matched version of discretized standard normal density
%with 200000 elements. This would be used for both hermite regressions and
%monte carlo simulations.

[W] = EvalHermiteArrayH0(ZI,Order);
% W is a matrix that contains hermite polynomials evaluated at discretized
% version of standard normal density. This matrix is used for finding
% hermite series coefficients of densities of SDEs.
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Below, we define time parameters of monte carlo simulation of SDEs.

seed0=90728436;
rng(seed0, 'combRecursive')
TtM=256*2;  %Terminal time for SDE simulation, here four years.
dtM=1/64/2; %time step size for monte carlo simulations.
dt=dtM;
Sfrequency=16;%The density of every 16th time step is sampled and all
%sampled densities till terminal time are returned in a matrix.
Random0(1:SDEpaths,1:TtM)=0;

for tt=1:0%TtM
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

for nn=1:0%NN
 nn
 NN
if(nn>3*NN0) %This commented if would have to be used to specify that only
%parameters with index nn greater than 1000 would be simulated etc.
 [coeff] =
MeanRevertingMonteCarloDensity04New(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,Sfrequency);
 %[coeff,coeff2] =
MeanRevertingMonteCarloDensity04(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,W2);
 Coeff(1:Order+1,1:TtM/Sfrequency,nn)=coeff(1:Order+1,1:TtM/Sfrequency);
end

end

%save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC9a.mat","Coeff")
%str=input("I have saved the densities coefficients variable--Stop");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%You can comment the SDE simulations loop and continue to load the
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.

%Below is my code since I was making monte carlo simulations in batches of 1000 and
%saved each batch in a different file on disk.

load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC.mat","Coeff")
 str=input("I have loaded the densities coefficients variable");

 Coeff0=Coeff;

 load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC2.mat","Coeff")
 str=input("I have loaded the densities coefficients variable");

 Coeff2=Coeff;

 load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC4.mat","Coeff")
 str=input("I have loaded the densities coefficients variable");

 Coeff3=Coeff;

 load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC9.mat","Coeff")
 str=input("I have loaded the densities coefficients variable");

 Coeff4=Coeff;

 Coeff(1:Order+1,1:TtM/Sfrequency,1:1000)=Coeff0(1:Order+1,1:TtM/Sfrequency,1:1000);
 Coeff(1:Order+1,1:TtM/Sfrequency,1001:2000)=Coeff2(1:Order+1,1:TtM/Sfrequency,1001:2000);
 Coeff(1:Order+1,1:TtM/Sfrequency,2001:3000)=Coeff3(1:Order+1,1:TtM/Sfrequency,2001:3000);
 Coeff(1:Order+1,1:TtM/Sfrequency,3001:4000)=Coeff4(1:Order+1,1:TtM/Sfrequency,3001:4000);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Dimensions of Coeff are Coeff(,1:Order+1,1:TtM/Sfrequency,1:NN).

%Below we choose one time slice between 1 and TtM for finding coefficients
%of hermite series from Legendre regression. I have taken slice 18 that occurs at time
%18*Sfrequency*dtM. Please choose different time slices and see how the
%program works.

%
%TimeSlice variable below
Ts=13;
CoeffH0(1:Order+1,1:NN)=Coeff(1:Order+1,Ts,1:NN);%Hermite series coefficients at time slice chosen for analytics.
CoeffH=transpose(CoeffH0);

% clf;
%
% plot((1:NN),CoeffH(1:NN,2),'g');
%
% str=input("Look at coeffs plot --Z1 coeff");

TT=Ts*dtM*Sfrequency;%Time at end of chosen slice. This will be used in analytic calculation of SDE mean later.
%We will replace the first mean coefficient of zeroth hermite associated
%with the Hermite series of SDEs with the analytic value.

%Below we calculate square root of variance(sum of hermite coefficients squared formula) to standardize the coefficients
VarSqRt(1:NN,1)=
sqrt(CoeffH(1:NN,2).^2+CoeffH(1:NN,3).^2*2+CoeffH(1:NN,4).^2*6+CoeffH(1:NN,5).^2*24+CoeffH(1:NN,6).^2*120+CoeffH(1:NN,7).^2*720+CoeffH(1:NN,8).^2*7*720);
%Below are six standardized coefficients

SHCoeff(1:NN,1:8)=CoeffH(1:NN,1:8)./VarSqRt(1:NN,1);
% SHCoeff stands for standardized hermite series coefficients.

str=input("Reached Level 1");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

OrderL=9;

%[Q1,Q2,Q3,Q4,Q5,Q6] = CalculateMathBasedRegressors(kappaU,thetaU,y0U,gammaU,sigmaU,NN);
%The above routine calculates analytic SDE simulation equation terms based six regressors
% for each of the NN scenarios. These are time independent and can be used
% for every time slice.

for nn=1:NN

C(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
YT(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
Y0T(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
UU(nn)=C(nn).*Y0T(nn);
VV(nn)=C(nn).*YT(nn);
UV(nn)=UU(nn).*VV(nn);
qq(nn)=2*(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
BB(nn)=besseli(qq(nn),sqrt(UV(nn)));

%
%     Q1(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
% Q2(nn)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
% %Q3(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
% Q3(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
% Q4(nn)=sigmaU(nn);%.^2*(1-exp(-2*kappaU(nn)*TT))/2/kappaU(nn));
% Q5(nn)=gammaU(nn);
% %UV(nn)=
% %Q6(nn)=sqrt(sigmaU(nn).^2*(1-exp(-2*kappaU(nn)*TT))/2/kappaU(nn));
% Q6(nn)=BB(nn);
%

%  Q1(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
%  Q2(nn)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
%  Q3(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
%  Q4(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
%  Q5(nn)=gammaU(nn);
%  Q6(nn)=sqrt(UV(nn));

  Q1(nn)=C(nn).*YT(nn);
 Q2(nn)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
 Q3(nn)=C(nn).*Y0T(nn);
 Q4(nn)=gammaU(nn);
 Q5(nn)=sigmaU(nn);
 Q6(nn)=thetaU(nn);

end

[Q7] = CalculateApproximateVarianceOfMRSDEs(kappaU,thetaU,y0U,gammaU,sigmaU,NN,Ts,Sfrequency,dt);
%The above is approximate variance of the SDE and its value for each of the
%NN parameters scenarios is used as seventh regressor in Legendre
%polynomial regression. This variable is time dependent and has to be
%recalculated for each time slice.

[WL] = CalculateHermitePolynomialDesignMatrix(Q1,Q2,Q3,Q4,Q5,Q6,Q7,OrderL);

for qq=1:8
    Yl(1:NN,qq)=SHCoeff(1:NN,qq); %First six standardized hermite coefficients to be predicted.
end
Yl(1:NN,9)=VarSqRt(1:NN,1);%Square root of variance used to standardize has to be predicted as well.

CoeffL=inv(WL'*WL)*(WL'*Yl);%Legendre coefficients to predict seven variables. six standardized coefficients
%and one square root of variance of each SDE.

str=input("Look if there is matlab warning about ill conditioned matrix inversion");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% clf;
% [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,1),NN,25,10 )
% plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
% str=input("Look at density of 1st coeff")
%
% [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,2),NN,25,10 )
% plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
% str=input("Look at density of 2nd coeff")
%
% %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%CoeffL
%size(WL)
%size(CoeffL)
%str=input("Look at size of CoeffL");

OrderL0=OrderL+1;

%bhs: Regressed value of standardized hermite coefficients produced from Legendre Regression %
bhs(1:NN,1:8)=0;   %
%RegressedVarSqRt: Regressed value of square root of volatility produced from Legendre Regression
RegressedVarSqRt(1:NN,1)=0;

%Below calculate hermite coefficients by regressing on Legendre polynomials
% with all calculated Legendre coefficients and polynomials evaluated at
% input data values used to find Legendre coefficients. This is in-sample
% testing only.

for rr=1:OrderL0+126*OrderL
    bhs(1:NN,1:8)=bhs(1:NN,1:8)+CoeffL(rr,1:8).*WL(1:NN,rr);
    RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffL(rr,9).*WL(1:NN,rr);
end

%Below are seven calculations of R-squared for each of
%the standardized six coefficients and seventh value of square root of variance.
1-sum((SHCoeff(:,1)-bhs(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)
1-sum((VarSqRt(:,1)-RegressedVarSqRt(:,1)).^2)/sum((VarSqRt(:,1)-sum(VarSqRt(:,1))/(NN)).^2)

str=input("Look at R^2s of eight standardized hermite series coefficients and ninth square root of variance");

%Since all coefficents were standardized before regression, Hermite series densities
%calculated from them should have variance one. However, variance would be slightly
%different from one after Legendre regression. So we calculate this
%variance of each hermite series density in regression.
VarSqRtbhs(1:NN,1)=
sqrt(bhs(1:NN,2).^2+bhs(1:NN,3).^2*2+bhs(1:NN,4).^2*6+bhs(1:NN,5).^2*24+bhs(1:NN,6).^2*120+bhs(1:NN,7).^2*720+bhs(1:NN,8).^2*7*720);

%bhs0 is re-standardized estimates of predicted from regression values of hermite series coefficients
bhs0(1:NN,1)=bhs(1:NN,1);
%Restandardization below to make sure that we get unit variance of each of
%the hermite series density.
bhs0(1:NN,2:8)=bhs(1:NN,2:8)./VarSqRtbhs(1:NN,1);

1-sum((SHCoeff(:,1)-bhs0(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs0(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs0(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs0(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs0(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs0(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs0(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs0(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)
1-sum((VarSqRt(:,1)-RegressedVarSqRt(:,1)).^2)/sum((VarSqRt(:,1)-sum(VarSqRt(:,1))/(NN)).^2)

str=input("Look at R^2s of first eight standardized hermite series coefficients");

%Below plot each of the in-sample densities and re-calculate them from
%Legendre regression and make an overlaid comparison.
for nn=1:NN

    %de-standardize by multiplying with square root of variance of each
    %density and get actual predicted coefficients of hermite-series of SDE
    %densities
    ch(1:8)=bhs0(nn,1:8).*RegressedVarSqRt(nn,1);

    %Below we repeat the same step for original Hermite series data found
    %from simulation. These are true values of hermite series coefficients and not predicted values.
    HCoeff(1:8)=SHCoeff(nn,1:8).*VarSqRt(nn);

    ch(1)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));%Replacing predicted value of mean with analytic value.

    ch(1:8)
    HCoeff(1:8)

    nn
    str=input("Look at predicted coefficients above and true coefficietns below for nnth SDE in data: First
coefficent(mean of SDE) in predicted values has been replaced by its analytic known value")

    clf;
    nn
    PlotHermiteSeriesDensityAndRvGraph(ch(1),ch(2:Order+1),'r');

    hold on

    PlotHermiteSeriesDensityAndRvGraph(HCoeff(1),HCoeff(2:Order+1),'g');
    nn

    str=input("Look at comparison of graphs of nnth density in sample--Green is data and red is our regression from
Legendre Polynomial coefficients");
    clf;
end

end

```

.

.

.

```
function [WL] = CalculateHermitePolynomialDesignMatrix(Q1,Q2,Q3,Q4,Q5,Q6,Q7,OrderL)

%This function takes seven arrays/regressors input at joint data values in the same
%sequence. And returnd a Hermite polynomials design matrix with all Hermite polynomials
%evaluated at their data values and their possible product values.
%You can use it anywhere in other problems if there are seven regressors.

OrderL0=OrderL+1;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

[Wl1,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1,OrderL);

[Wl2,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2,OrderL);

[Wl3,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3,OrderL);

[Wl4,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4,OrderL);

[Wl5,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q5,OrderL);

[Wl6,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q6,OrderL);

[Wl7,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q7,OrderL);

[Wl12,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2,OrderL);

[Wl13,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3,OrderL);

[Wl14,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4,OrderL);

[Wl15,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q5,OrderL);

[Wl16,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q6,OrderL);

[Wl17,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q7,OrderL);

[Wl23,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3,OrderL);

[Wl24,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4,OrderL);

[Wl25,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q5,OrderL);

[Wl26,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q6,OrderL);

[Wl27,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q7,OrderL);

[Wl34,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4,OrderL);

[Wl35,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q5,OrderL);

[Wl36,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q6,OrderL);

[Wl37,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q7,OrderL);

[Wl45,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q5,OrderL);

[Wl46,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q6,OrderL);

[Wl47,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q7,OrderL);

[Wl56,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q5.*Q6,OrderL);

[Wl57,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q5.*Q7,OrderL);

[Wl67,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q6.*Q7,OrderL);

[Wl123,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3,OrderL);

[Wl124,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4,OrderL);

[Wl125,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q5,OrderL);

[Wl126,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q6,OrderL);

[Wl127,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q7,OrderL);

[Wl134,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4,OrderL);

[Wl135,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q5,OrderL);

[Wl136,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q6,OrderL);

[Wl137,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q7,OrderL);

[Wl145,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q5,OrderL);

[Wl146,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q6,OrderL);

[Wl147,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q7,OrderL);

[Wl156,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q5.*Q6,OrderL);

[Wl157,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q5.*Q7,OrderL);

[Wl167,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q6.*Q7,OrderL);

[Wl234,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4,OrderL);

[Wl235,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q5,OrderL);

[Wl236,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q6,OrderL);

[Wl237,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q7,OrderL);

[Wl245,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q5,OrderL);

[Wl246,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q6,OrderL);

[Wl247,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q7,OrderL);

[Wl256,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q5.*Q6,OrderL);

[Wl257,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q5.*Q7,OrderL);

[Wl267,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q6.*Q7,OrderL);

[Wl345,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q5,OrderL);

[Wl346,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q6,OrderL);

[Wl347,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q7,OrderL);

[Wl356,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q5.*Q6,OrderL);

[Wl357,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q5.*Q7,OrderL);

[Wl367,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q6.*Q7,OrderL);

[Wl456,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q5.*Q6,OrderL);

[Wl457,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q5.*Q7,OrderL);

[Wl467,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q6.*Q7,OrderL);

[Wl567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q5.*Q6.*Q7,OrderL);

[Wl1234,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4,OrderL);

[Wl1235,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q5,OrderL);

[Wl1236,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q6,OrderL);

[Wl1237,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q7,OrderL);

[Wl1245,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q5,OrderL);

[Wl1246,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q6,OrderL);

[Wl1247,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q7,OrderL);

[Wl1256,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q5.*Q6,OrderL);

[Wl1257,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q5.*Q7,OrderL);

[Wl1267,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q6.*Q7,OrderL);

[Wl1345,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q5,OrderL);

[Wl1346,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q6,OrderL);

[Wl1347,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q7,OrderL);

[Wl1356,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q5.*Q6,OrderL);

[Wl1357,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q5.*Q7,OrderL);

[Wl1367,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q6.*Q7,OrderL);

[Wl1456,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q5.*Q6,OrderL);

[Wl1457,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q5.*Q7,OrderL);

[Wl1467,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q6.*Q7,OrderL);

[Wl1567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q5.*Q6.*Q7,OrderL);

[Wl2345,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q5,OrderL);

[Wl2346,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q6,OrderL);

[Wl2347,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q7,OrderL);

[Wl2356,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q5.*Q6,OrderL);

[Wl2357,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q5.*Q7,OrderL);

[Wl2367,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q6.*Q7,OrderL);

[Wl2456,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q5.*Q6,OrderL);

[Wl2457,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q5.*Q7,OrderL);

[Wl2467,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q6.*Q7,OrderL);

[Wl2567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q5.*Q6.*Q7,OrderL);

[Wl3456,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q5.*Q6,OrderL);

[Wl3457,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q5.*Q7,OrderL);

[Wl3467,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q6.*Q7,OrderL);

[Wl3567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q5.*Q6.*Q7,OrderL);

[Wl4567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q5.*Q6.*Q7,OrderL);

[Wl12345,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q5,OrderL);

[Wl12346,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q6,OrderL);

[Wl12347,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q7,OrderL);

[Wl12356,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q5.*Q6,OrderL);

[Wl12357,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q5.*Q7,OrderL);

[Wl12367,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q6.*Q7,OrderL);

[Wl12456,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q5.*Q6,OrderL);

[Wl12457,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q5.*Q7,OrderL);

[Wl12467,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q6.*Q7,OrderL);

[Wl12567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q5.*Q6.*Q7,OrderL);

[Wl13456,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q5.*Q6,OrderL);

[Wl13457,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q5.*Q7,OrderL);

[Wl13467,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q6.*Q7,OrderL);

[Wl13567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q5.*Q6.*Q7,OrderL);

[Wl14567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl23456,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q5.*Q6,OrderL);

[Wl23457,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q5.*Q7,OrderL);

[Wl23467,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q6.*Q7,OrderL);

[Wl23567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q5.*Q6.*Q7,OrderL);

[Wl24567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl34567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl123456,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q5.*Q6,OrderL);

[Wl123457,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q5.*Q7,OrderL);

[Wl123467,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q6.*Q7,OrderL);

[Wl123567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q5.*Q6.*Q7,OrderL);

[Wl124567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl134567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl234567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q5.*Q6.*Q7,OrderL);

[Wl1234567,Uy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q5.*Q6.*Q7,OrderL);

%Below Tile all of the Hermite polynomials of each of the four random
%parameters in a single matrix and use for least square regression. Zeroth
%Hermite is evaluated in each of the four matrices and has to be removed
%from tiling other than just including one time.
WL(:,1:OrderL0)=Wl1(:,1:OrderL0);
WL(:,OrderL0+1:OrderL0+OrderL)=Wl2(:,2:OrderL0);
WL(:,OrderL0+OrderL+1:OrderL0+2*OrderL)=Wl3(:,2:OrderL0);
WL(:,OrderL0+2*OrderL+1:OrderL0+3*OrderL)=Wl4(:,2:OrderL0);
WL(:,OrderL0+3*OrderL+1:OrderL0+4*OrderL)=Wl5(:,2:OrderL0);
WL(:,OrderL0+4*OrderL+1:OrderL0+5*OrderL)=Wl6(:,2:OrderL0);
WL(:,OrderL0+5*OrderL+1:OrderL0+6*OrderL)=Wl7(:,2:OrderL0);

WL(:,OrderL0+6*OrderL+1:OrderL0+7*OrderL)=Wl12(:,2:OrderL0);
WL(:,OrderL0+7*OrderL+1:OrderL0+8*OrderL)=Wl13(:,2:OrderL0);
WL(:,OrderL0+8*OrderL+1:OrderL0+9*OrderL)=Wl14(:,2:OrderL0);
WL(:,OrderL0+9*OrderL+1:OrderL0+10*OrderL)=Wl15(:,2:OrderL0);
WL(:,OrderL0+10*OrderL+1:OrderL0+11*OrderL)=Wl16(:,2:OrderL0);
WL(:,OrderL0+11*OrderL+1:OrderL0+12*OrderL)=Wl17(:,2:OrderL0);

WL(:,OrderL0+12*OrderL+1:OrderL0+13*OrderL)=Wl23(:,2:OrderL0);
WL(:,OrderL0+13*OrderL+1:OrderL0+14*OrderL)=Wl24(:,2:OrderL0);
WL(:,OrderL0+14*OrderL+1:OrderL0+15*OrderL)=Wl25(:,2:OrderL0);
WL(:,OrderL0+15*OrderL+1:OrderL0+16*OrderL)=Wl26(:,2:OrderL0);
WL(:,OrderL0+16*OrderL+1:OrderL0+17*OrderL)=Wl27(:,2:OrderL0);

WL(:,OrderL0+17*OrderL+1:OrderL0+18*OrderL)=Wl34(:,2:OrderL0);
WL(:,OrderL0+18*OrderL+1:OrderL0+19*OrderL)=Wl35(:,2:OrderL0);
WL(:,OrderL0+19*OrderL+1:OrderL0+20*OrderL)=Wl36(:,2:OrderL0);
WL(:,OrderL0+20*OrderL+1:OrderL0+21*OrderL)=Wl37(:,2:OrderL0);

WL(:,OrderL0+21*OrderL+1:OrderL0+22*OrderL)=Wl45(:,2:OrderL0);
WL(:,OrderL0+22*OrderL+1:OrderL0+23*OrderL)=Wl46(:,2:OrderL0);
WL(:,OrderL0+23*OrderL+1:OrderL0+24*OrderL)=Wl47(:,2:OrderL0);

WL(:,OrderL0+24*OrderL+1:OrderL0+25*OrderL)=Wl56(:,2:OrderL0);
WL(:,OrderL0+25*OrderL+1:OrderL0+26*OrderL)=Wl57(:,2:OrderL0);

WL(:,OrderL0+26*OrderL+1:OrderL0+27*OrderL)=Wl67(:,2:OrderL0);

WL(:,OrderL0+27*OrderL+1:OrderL0+28*OrderL)=Wl123(:,2:OrderL0);
WL(:,OrderL0+28*OrderL+1:OrderL0+29*OrderL)=Wl124(:,2:OrderL0);
WL(:,OrderL0+29*OrderL+1:OrderL0+30*OrderL)=Wl125(:,2:OrderL0);
WL(:,OrderL0+30*OrderL+1:OrderL0+31*OrderL)=Wl126(:,2:OrderL0);
WL(:,OrderL0+31*OrderL+1:OrderL0+32*OrderL)=Wl127(:,2:OrderL0);

WL(:,OrderL0+32*OrderL+1:OrderL0+33*OrderL)=Wl134(:,2:OrderL0);
WL(:,OrderL0+33*OrderL+1:OrderL0+34*OrderL)=Wl135(:,2:OrderL0);
WL(:,OrderL0+34*OrderL+1:OrderL0+35*OrderL)=Wl136(:,2:OrderL0);
WL(:,OrderL0+35*OrderL+1:OrderL0+36*OrderL)=Wl137(:,2:OrderL0);

WL(:,OrderL0+36*OrderL+1:OrderL0+37*OrderL)=Wl145(:,2:OrderL0);
WL(:,OrderL0+37*OrderL+1:OrderL0+38*OrderL)=Wl146(:,2:OrderL0);
WL(:,OrderL0+38*OrderL+1:OrderL0+39*OrderL)=Wl147(:,2:OrderL0);

WL(:,OrderL0+39*OrderL+1:OrderL0+40*OrderL)=Wl156(:,2:OrderL0);
WL(:,OrderL0+40*OrderL+1:OrderL0+41*OrderL)=Wl157(:,2:OrderL0);

WL(:,OrderL0+41*OrderL+1:OrderL0+42*OrderL)=Wl167(:,2:OrderL0);

WL(:,OrderL0+42*OrderL+1:OrderL0+43*OrderL)=Wl234(:,2:OrderL0);
WL(:,OrderL0+43*OrderL+1:OrderL0+44*OrderL)=Wl235(:,2:OrderL0);
WL(:,OrderL0+44*OrderL+1:OrderL0+45*OrderL)=Wl236(:,2:OrderL0);
WL(:,OrderL0+45*OrderL+1:OrderL0+46*OrderL)=Wl237(:,2:OrderL0);

WL(:,OrderL0+46*OrderL+1:OrderL0+47*OrderL)=Wl245(:,2:OrderL0);
WL(:,OrderL0+47*OrderL+1:OrderL0+48*OrderL)=Wl246(:,2:OrderL0);
WL(:,OrderL0+48*OrderL+1:OrderL0+49*OrderL)=Wl247(:,2:OrderL0);

WL(:,OrderL0+49*OrderL+1:OrderL0+50*OrderL)=Wl256(:,2:OrderL0);
WL(:,OrderL0+50*OrderL+1:OrderL0+51*OrderL)=Wl257(:,2:OrderL0);

WL(:,OrderL0+51*OrderL+1:OrderL0+52*OrderL)=Wl267(:,2:OrderL0);

WL(:,OrderL0+52*OrderL+1:OrderL0+53*OrderL)=Wl345(:,2:OrderL0);
WL(:,OrderL0+53*OrderL+1:OrderL0+54*OrderL)=Wl346(:,2:OrderL0);
WL(:,OrderL0+54*OrderL+1:OrderL0+55*OrderL)=Wl347(:,2:OrderL0);

WL(:,OrderL0+55*OrderL+1:OrderL0+56*OrderL)=Wl356(:,2:OrderL0);
WL(:,OrderL0+56*OrderL+1:OrderL0+57*OrderL)=Wl357(:,2:OrderL0);

WL(:,OrderL0+57*OrderL+1:OrderL0+58*OrderL)=Wl367(:,2:OrderL0);

WL(:,OrderL0+58*OrderL+1:OrderL0+59*OrderL)=Wl456(:,2:OrderL0);
WL(:,OrderL0+59*OrderL+1:OrderL0+60*OrderL)=Wl457(:,2:OrderL0);

WL(:,OrderL0+60*OrderL+1:OrderL0+61*OrderL)=Wl467(:,2:OrderL0);

WL(:,OrderL0+61*OrderL+1:OrderL0+62*OrderL)=Wl567(:,2:OrderL0);

WL(:,OrderL0+62*OrderL+1:OrderL0+63*OrderL)=Wl1234(:,2:OrderL0);
WL(:,OrderL0+63*OrderL+1:OrderL0+64*OrderL)=Wl1235(:,2:OrderL0);
WL(:,OrderL0+64*OrderL+1:OrderL0+65*OrderL)=Wl1236(:,2:OrderL0);
WL(:,OrderL0+65*OrderL+1:OrderL0+66*OrderL)=Wl1237(:,2:OrderL0);

WL(:,OrderL0+66*OrderL+1:OrderL0+67*OrderL)=Wl1245(:,2:OrderL0);
WL(:,OrderL0+67*OrderL+1:OrderL0+68*OrderL)=Wl1246(:,2:OrderL0);
WL(:,OrderL0+68*OrderL+1:OrderL0+69*OrderL)=Wl1247(:,2:OrderL0);

WL(:,OrderL0+69*OrderL+1:OrderL0+70*OrderL)=Wl1256(:,2:OrderL0);
WL(:,OrderL0+70*OrderL+1:OrderL0+71*OrderL)=Wl1257(:,2:OrderL0);

WL(:,OrderL0+71*OrderL+1:OrderL0+72*OrderL)=Wl1267(:,2:OrderL0);

WL(:,OrderL0+72*OrderL+1:OrderL0+73*OrderL)=Wl1345(:,2:OrderL0);
WL(:,OrderL0+73*OrderL+1:OrderL0+74*OrderL)=Wl1346(:,2:OrderL0);
WL(:,OrderL0+74*OrderL+1:OrderL0+75*OrderL)=Wl1347(:,2:OrderL0);

WL(:,OrderL0+75*OrderL+1:OrderL0+76*OrderL)=Wl1356(:,2:OrderL0);
WL(:,OrderL0+76*OrderL+1:OrderL0+77*OrderL)=Wl1357(:,2:OrderL0);

WL(:,OrderL0+77*OrderL+1:OrderL0+78*OrderL)=Wl1367(:,2:OrderL0);

WL(:,OrderL0+78*OrderL+1:OrderL0+79*OrderL)=Wl1456(:,2:OrderL0);
WL(:,OrderL0+79*OrderL+1:OrderL0+80*OrderL)=Wl1457(:,2:OrderL0);

WL(:,OrderL0+80*OrderL+1:OrderL0+81*OrderL)=Wl1467(:,2:OrderL0);

WL(:,OrderL0+81*OrderL+1:OrderL0+82*OrderL)=Wl1567(:,2:OrderL0);

WL(:,OrderL0+82*OrderL+1:OrderL0+83*OrderL)=Wl2345(:,2:OrderL0);
WL(:,OrderL0+83*OrderL+1:OrderL0+84*OrderL)=Wl2346(:,2:OrderL0);
WL(:,OrderL0+84*OrderL+1:OrderL0+85*OrderL)=Wl2347(:,2:OrderL0);

WL(:,OrderL0+85*OrderL+1:OrderL0+86*OrderL)=Wl2356(:,2:OrderL0);
WL(:,OrderL0+86*OrderL+1:OrderL0+87*OrderL)=Wl2357(:,2:OrderL0);

WL(:,OrderL0+87*OrderL+1:OrderL0+88*OrderL)=Wl2367(:,2:OrderL0);

WL(:,OrderL0+88*OrderL+1:OrderL0+89*OrderL)=Wl2456(:,2:OrderL0);
WL(:,OrderL0+89*OrderL+1:OrderL0+90*OrderL)=Wl2457(:,2:OrderL0);

WL(:,OrderL0+90*OrderL+1:OrderL0+91*OrderL)=Wl2467(:,2:OrderL0);

WL(:,OrderL0+91*OrderL+1:OrderL0+92*OrderL)=Wl2567(:,2:OrderL0);

WL(:,OrderL0+92*OrderL+1:OrderL0+93*OrderL)=Wl3456(:,2:OrderL0);
WL(:,OrderL0+93*OrderL+1:OrderL0+94*OrderL)=Wl3457(:,2:OrderL0);

WL(:,OrderL0+94*OrderL+1:OrderL0+95*OrderL)=Wl3467(:,2:OrderL0);

WL(:,OrderL0+95*OrderL+1:OrderL0+96*OrderL)=Wl3567(:,2:OrderL0);

WL(:,OrderL0+96*OrderL+1:OrderL0+97*OrderL)=Wl4567(:,2:OrderL0);

WL(:,OrderL0+97*OrderL+1:OrderL0+98*OrderL)=Wl12345(:,2:OrderL0);
WL(:,OrderL0+98*OrderL+1:OrderL0+99*OrderL)=Wl12346(:,2:OrderL0);
WL(:,OrderL0+99*OrderL+1:OrderL0+100*OrderL)=Wl12347(:,2:OrderL0);

WL(:,OrderL0+100*OrderL+1:OrderL0+101*OrderL)=Wl12356(:,2:OrderL0);
WL(:,OrderL0+101*OrderL+1:OrderL0+102*OrderL)=Wl12357(:,2:OrderL0);

WL(:,OrderL0+102*OrderL+1:OrderL0+103*OrderL)=Wl12367(:,2:OrderL0);

WL(:,OrderL0+103*OrderL+1:OrderL0+104*OrderL)=Wl12456(:,2:OrderL0);
WL(:,OrderL0+104*OrderL+1:OrderL0+105*OrderL)=Wl12457(:,2:OrderL0);

WL(:,OrderL0+105*OrderL+1:OrderL0+106*OrderL)=Wl12467(:,2:OrderL0);

WL(:,OrderL0+106*OrderL+1:OrderL0+107*OrderL)=Wl12567(:,2:OrderL0);

WL(:,OrderL0+107*OrderL+1:OrderL0+108*OrderL)=Wl13456(:,2:OrderL0);
WL(:,OrderL0+108*OrderL+1:OrderL0+109*OrderL)=Wl13457(:,2:OrderL0);

WL(:,OrderL0+109*OrderL+1:OrderL0+110*OrderL)=Wl13467(:,2:OrderL0);

WL(:,OrderL0+110*OrderL+1:OrderL0+111*OrderL)=Wl13567(:,2:OrderL0);

WL(:,OrderL0+111*OrderL+1:OrderL0+112*OrderL)=Wl14567(:,2:OrderL0);

WL(:,OrderL0+112*OrderL+1:OrderL0+113*OrderL)=Wl23456(:,2:OrderL0);
WL(:,OrderL0+113*OrderL+1:OrderL0+114*OrderL)=Wl23457(:,2:OrderL0);

WL(:,OrderL0+114*OrderL+1:OrderL0+115*OrderL)=Wl23467(:,2:OrderL0);

WL(:,OrderL0+115*OrderL+1:OrderL0+116*OrderL)=Wl23567(:,2:OrderL0);

WL(:,OrderL0+116*OrderL+1:OrderL0+117*OrderL)=Wl24567(:,2:OrderL0);

WL(:,OrderL0+117*OrderL+1:OrderL0+118*OrderL)=Wl34567(:,2:OrderL0);

WL(:,OrderL0+118*OrderL+1:OrderL0+119*OrderL)=Wl123456(:,2:OrderL0);
WL(:,OrderL0+119*OrderL+1:OrderL0+120*OrderL)=Wl123457(:,2:OrderL0);

WL(:,OrderL0+120*OrderL+1:OrderL0+121*OrderL)=Wl123467(:,2:OrderL0);

WL(:,OrderL0+121*OrderL+1:OrderL0+122*OrderL)=Wl123567(:,2:OrderL0);

WL(:,OrderL0+122*OrderL+1:OrderL0+123*OrderL)=Wl124567(:,2:OrderL0);

WL(:,OrderL0+123*OrderL+1:OrderL0+124*OrderL)=Wl134567(:,2:OrderL0);

WL(:,OrderL0+124*OrderL+1:OrderL0+125*OrderL)=Wl234567(:,2:OrderL0);

WL(:,OrderL0+125*OrderL+1:OrderL0+126*OrderL)=Wl1234567(:,2:OrderL0);

end

```

.

.

.

```
function [Wy,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Yin,Order)

Ndata=length(Yin);

Hz=HermitePoly(Order);
MeanYin=sum(Yin(1:Ndata))/Ndata;
Ym(1:Ndata)=Yin(1:Ndata)-MeanYin;
YmVar=sum(Ym(1:Ndata).^2)/Ndata;
Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);

Mtable=readtable('C:\Users\Lenovo\Documents\MATLAB\MATLAB1\MomentMatchParams08.txt');
[ZI] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable);

%UI(1:Ndata)=-1+2/Ndata*(1:Ndata)-1/Ndata;

%[Zn] = StandardNormalIdealDesity02(Ndata,1);
%[ZI] = CalculateZI(Zn);

%ZI=Zn;
%Below W is the design matrix for least squares regression i.e the matrix
%that contains all the hermite polynomials calculated at ideal normal
%density grid of size Ndata.
[W] = EvalHermiteArrayH0(ZI,Order);

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
Zs1(I(1:Ndata))=ZI(1:Ndata);
%Below the values to be regressed facing the design matrix are assigned
%Ymu(1:Ndata,1)=Ys(1:Ndata);
%Below, implement least squares regression.
%coeff=inv(W'*W)*(W'*Ymu);
%Store in coefficietns array of all random varaibles
%Coeff(1:Order+1)= coeff(1:Order+1,1);
%Store the associated Z in Z-array of all coefficients.
Zy(1:Ndata)=Zs1(1:Ndata);

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

### #2511 — Amin (Topic Author)
*October 31, 2024, 6:36 PM*

Friends, in the program posted in previous post, I am reading data from file and therefore posting an updated version
that you can generate the monte carlo densities data with the same random number seeds.

Here was the R-squared of program that you should see and that was used for SDE density overlaid plots in a recent post.

ans =

   0.999989683605129

ans =

   0.999908641627815

ans =

   0.999969767840884

ans =

   0.999377369168530

ans =

   0.993947063546857

ans =

   0.968427756112463

ans =

   0.920767558897081

ans =

   0.917744585035872

ans =

   0.999955083446905

Look at R^2s of first eight standardized hermite series coefficients

Below is the program used to generate above R-squared and related densities.

.

```
function [] = SDEsWithMathAIMain08E4()

%The mean reverting SDE is given as
%dY(t)= kappa (theta - Y(t)) dt + sigma Y(t)^gamma dZ(t)
%Y(0) = y0

%We specify Low and High SDE parameters range below.
kappaL=.25;%Lower range of kappa
kappaH=3;%Upper range of kappa
thetaL=.5;%Lower range of theta
thetaH=2;%Upper range of theta
y0L=.5;%Lower range of y0
y0H=2;%Higher range of y0
gammaL=.5;%Lower range of gamma
gammaH=1;%Higher range of gamma
sigmaL=.1;
sigmaH=1.0;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Below five sets of uniform random numbers are sampled in batches of one
%thousand. These random numbers are later mapped on five input parameters
%over the their range previously defined.
%Sampling is done in batches of thousands since I wanted to first simulate
%one thousand SDEs and later continue to add more batches of thousand SDEs
%without spoiling the data of earlier batches from random number sequence.
%Since I was doing antithetic sampling, I did it at level of local batches
%of thousand.

seed=83098561;
rng(seed);
MM=4;    %No of Batches of simulation
NN0=1000;%Scenarios in each batch.
NN=MM*NN0;%Number of SDE runs in the training sample. Ideally would be much larger.

for mm=1:MM
    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand1((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand1((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand2((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand2((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand3((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand3((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand4((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand4((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

    SampleRand(1:NN0/2,1)=rand(NN0/2,1);
    Rand5((mm-1)*NN0+1:(mm-1)*NN0+NN0/2,1)=SampleRand(1:NN0/2,1);
    Rand5((mm-1)*NN0+NN0/2+1:mm*NN0,1)=1-SampleRand(1:NN0/2,1);%For symmetry, antithetic uniforms are used.

end

kappaU(1:NN)=kappaL+(kappaH-kappaL).*Rand1(1:NN,1);%Map unifrom random variates on kappa.

thetaU(1:NN)=thetaL+(thetaH-thetaL).*Rand2(1:NN,1);%Map unifrom random variates on theta.

y0U(1:NN)=y0L+(y0H-y0L).*Rand3(1:NN,1);%Map unifrom random variates on starting value of the SDE.

gammaU(1:NN)=gammaL+(gammaH-gammaL).*Rand4(1:NN,1);%Map unifrom random variates on gamma.

sigmaU(1:NN)=sigmaL+(sigmaH-sigmaL).*Rand5(1:NN,1);%Taking sigma at mid of upper and lower range.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

SDEpaths=200000;
MOrder=16;     %Order of moment matching of standard normal random numbers for simulation in SDEs
Order=7;       %Order of hermite series that is used to represent SDE densities.

%alphas below are used for moment matching of normal random numbers.
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

%ZI is a 16 moment matched version of discretized standard normal density
%with 200000 elements. This would be used for both hermite regressions and
%monte carlo simulations.

[W] = EvalHermiteArrayH0(ZI,Order);
% W is a matrix that contains hermite polynomials evaluated at discretized
% version of standard normal density. This matrix is used for finding
% hermite series coefficients of densities of SDEs.
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Below, we define time parameters of monte carlo simulation of SDEs.

seed0=90728436;
rng(seed0, 'combRecursive')
TtM=256*2;  %Terminal time for SDE simulation, here four years.
dtM=1/64/2; %time step size for monte carlo simulations.
dt=dtM;
Sfrequency=16;%The density of every 16th time step is sampled and all
%sampled densities till terminal time are returned in a matrix.
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
%if(nn>3*NN0) %This commented if would have to be used to specify that only
%parameters with index nn greater than 1000 would be simulated etc.
 [coeff] =
MeanRevertingMonteCarloDensity04New(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,Sfrequency);
 %[coeff,coeff2] =
MeanRevertingMonteCarloDensity04(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,W2);
 Coeff(1:Order+1,1:TtM/Sfrequency,nn)=coeff(1:Order+1,1:TtM/Sfrequency);
%end

end

save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC9a.mat","Coeff")
str=input("I have saved the densities coefficients variable--Stop");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%You can comment the SDE simulations loop and continue to load the
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.

%Below is my code since I was making monte carlo simulations in batches of 1000 and
%saved each batch in a different file on disk.
%
% load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC.mat","Coeff")
%  str=input("I have loaded the densities coefficients variable");
%
%  Coeff0=Coeff;
%
%  load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC2.mat","Coeff")
%  str=input("I have loaded the densities coefficients variable");
%
%  Coeff2=Coeff;
%
%  load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC4.mat","Coeff")
%  str=input("I have loaded the densities coefficients variable");
%
%  Coeff3=Coeff;
%
%  load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC9.mat","Coeff")
%  str=input("I have loaded the densities coefficients variable");
%
%  Coeff4=Coeff;
%
%  Coeff(1:Order+1,1:TtM/Sfrequency,1:1000)=Coeff0(1:Order+1,1:TtM/Sfrequency,1:1000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,1001:2000)=Coeff2(1:Order+1,1:TtM/Sfrequency,1001:2000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,2001:3000)=Coeff3(1:Order+1,1:TtM/Sfrequency,2001:3000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,3001:4000)=Coeff4(1:Order+1,1:TtM/Sfrequency,3001:4000);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Dimensions of Coeff are Coeff(,1:Order+1,1:TtM/Sfrequency,1:NN).

%Below we choose one time slice between 1 and TtM for finding coefficients
%of hermite series from Legendre regression. I have taken slice 18 that occurs at time
%18*Sfrequency*dtM. Please choose different time slices and see how the
%program works.

%
%TimeSlice variable below
Ts=13;
CoeffH0(1:Order+1,1:NN)=Coeff(1:Order+1,Ts,1:NN);%Hermite series coefficients at time slice chosen for analytics.
CoeffH=transpose(CoeffH0);

% clf;
%
% plot((1:NN),CoeffH(1:NN,2),'g');
%
% str=input("Look at coeffs plot --Z1 coeff");

TT=Ts*dtM*Sfrequency;%Time at end of chosen slice. This will be used in analytic calculation of SDE mean later.
%We will replace the first mean coefficient of zeroth hermite associated
%with the Hermite series of SDEs with the analytic value.

%Below we calculate square root of variance(sum of hermite coefficients squared formula) to standardize the coefficients
VarSqRt(1:NN,1)=
sqrt(CoeffH(1:NN,2).^2+CoeffH(1:NN,3).^2*2+CoeffH(1:NN,4).^2*6+CoeffH(1:NN,5).^2*24+CoeffH(1:NN,6).^2*120+CoeffH(1:NN,7).^2*720+CoeffH(1:NN,8).^2*7*720);
%Below are six standardized coefficients

SHCoeff(1:NN,1:8)=CoeffH(1:NN,1:8)./VarSqRt(1:NN,1);
% SHCoeff stands for standardized hermite series coefficients.

str=input("Reached Level 1");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

OrderL=9;

%[Q1,Q2,Q3,Q4,Q5,Q6] = CalculateMathBasedRegressors(kappaU,thetaU,y0U,gammaU,sigmaU,NN);
%The above routine calculates analytic SDE simulation equation terms based six regressors
% for each of the NN scenarios. These are time independent and can be used
% for every time slice.

for nn=1:NN

C(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
YT(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
Y0T(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
UU(nn)=C(nn).*Y0T(nn);
VV(nn)=C(nn).*YT(nn);
UV(nn)=UU(nn).*VV(nn);
qq(nn)=2*(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
BB(nn)=besseli(qq(nn),sqrt(UV(nn)));

%
%     Q1(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
% Q2(nn)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
% %Q3(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
% Q3(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
% Q4(nn)=sigmaU(nn);%.^2*(1-exp(-2*kappaU(nn)*TT))/2/kappaU(nn));
% Q5(nn)=gammaU(nn);
% %UV(nn)=
% %Q6(nn)=sqrt(sigmaU(nn).^2*(1-exp(-2*kappaU(nn)*TT))/2/kappaU(nn));
% Q6(nn)=BB(nn);
%

%  Q1(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
%  Q2(nn)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
%  Q3(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
%  Q4(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
%  Q5(nn)=gammaU(nn);
%  Q6(nn)=sqrt(UV(nn));

  Q1(nn)=C(nn).*YT(nn);
 Q2(nn)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
 Q3(nn)=C(nn).*Y0T(nn);
 Q4(nn)=gammaU(nn);
 Q5(nn)=sigmaU(nn);
 Q6(nn)=thetaU(nn);

end

[Q7] = CalculateApproximateVarianceOfMRSDEs(kappaU,thetaU,y0U,gammaU,sigmaU,NN,Ts,Sfrequency,dt);
%The above is approximate variance of the SDE and its value for each of the
%NN parameters scenarios is used as seventh regressor in Legendre
%polynomial regression. This variable is time dependent and has to be
%recalculated for each time slice.

[WL] = CalculateHermitePolynomialDesignMatrix(Q1,Q2,Q3,Q4,Q5,Q6,Q7,OrderL);

for qq=1:8
    Yl(1:NN,qq)=SHCoeff(1:NN,qq); %First six standardized hermite coefficients to be predicted.
end
Yl(1:NN,9)=VarSqRt(1:NN,1);%Square root of variance used to standardize has to be predicted as well.

CoeffL=inv(WL'*WL)*(WL'*Yl);%Legendre coefficients to predict seven variables. six standardized coefficients
%and one square root of variance of each SDE.

str=input("Look if there is matlab warning about ill conditioned matrix inversion");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% clf;
% [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,1),NN,25,10 )
% plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
% str=input("Look at density of 1st coeff")
%
% [XDensity,IndexOut,IndexMax] = MakeDensityFromSimulation_Infiniti_NEW(Yl(:,2),NN,25,10 )
% plot(IndexOut(1:IndexMax),XDensity(1:IndexMax),'g');
% str=input("Look at density of 2nd coeff")
%
% %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%CoeffL
%size(WL)
%size(CoeffL)
%str=input("Look at size of CoeffL");

OrderL0=OrderL+1;

%bhs: Regressed value of standardized hermite coefficients produced from Legendre Regression %
bhs(1:NN,1:8)=0;   %
%RegressedVarSqRt: Regressed value of square root of volatility produced from Legendre Regression
RegressedVarSqRt(1:NN,1)=0;

%Below calculate hermite coefficients by regressing on Legendre polynomials
% with all calculated Legendre coefficients and polynomials evaluated at
% input data values used to find Legendre coefficients. This is in-sample
% testing only.

for rr=1:OrderL0+126*OrderL
    bhs(1:NN,1:8)=bhs(1:NN,1:8)+CoeffL(rr,1:8).*WL(1:NN,rr);
    RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffL(rr,9).*WL(1:NN,rr);
end

%Below are seven calculations of R-squared for each of
%the standardized six coefficients and seventh value of square root of variance.
1-sum((SHCoeff(:,1)-bhs(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)
1-sum((VarSqRt(:,1)-RegressedVarSqRt(:,1)).^2)/sum((VarSqRt(:,1)-sum(VarSqRt(:,1))/(NN)).^2)

str=input("Look at R^2s of eight standardized hermite series coefficients and ninth square root of variance");

%Since all coefficents were standardized before regression, Hermite series densities
%calculated from them should have variance one. However, variance would be slightly
%different from one after Legendre regression. So we calculate this
%variance of each hermite series density in regression.
VarSqRtbhs(1:NN,1)=
sqrt(bhs(1:NN,2).^2+bhs(1:NN,3).^2*2+bhs(1:NN,4).^2*6+bhs(1:NN,5).^2*24+bhs(1:NN,6).^2*120+bhs(1:NN,7).^2*720+bhs(1:NN,8).^2*7*720);

%bhs0 is re-standardized estimates of predicted from regression values of hermite series coefficients
bhs0(1:NN,1)=bhs(1:NN,1);
%Restandardization below to make sure that we get unit variance of each of
%the hermite series density.
bhs0(1:NN,2:8)=bhs(1:NN,2:8)./VarSqRtbhs(1:NN,1);

1-sum((SHCoeff(:,1)-bhs0(:,1)).^2)/sum((SHCoeff(:,1)-sum(SHCoeff(:,1))/(NN)).^2)
1-sum((SHCoeff(:,2)-bhs0(:,2)).^2)/sum((SHCoeff(:,2)-sum(SHCoeff(:,2))/(NN)).^2)
1-sum((SHCoeff(:,3)-bhs0(:,3)).^2)/sum((SHCoeff(:,3)-sum(SHCoeff(:,3))/(NN)).^2)
1-sum((SHCoeff(:,4)-bhs0(:,4)).^2)/sum((SHCoeff(:,4)-sum(SHCoeff(:,4))/(NN)).^2)
1-sum((SHCoeff(:,5)-bhs0(:,5)).^2)/sum((SHCoeff(:,5)-sum(SHCoeff(:,5))/(NN)).^2)
1-sum((SHCoeff(:,6)-bhs0(:,6)).^2)/sum((SHCoeff(:,6)-sum(SHCoeff(:,6))/(NN)).^2)
1-sum((SHCoeff(:,7)-bhs0(:,7)).^2)/sum((SHCoeff(:,7)-sum(SHCoeff(:,7))/(NN)).^2)
1-sum((SHCoeff(:,8)-bhs0(:,8)).^2)/sum((SHCoeff(:,8)-sum(SHCoeff(:,8))/(NN)).^2)
1-sum((VarSqRt(:,1)-RegressedVarSqRt(:,1)).^2)/sum((VarSqRt(:,1)-sum(VarSqRt(:,1))/(NN)).^2)

str=input("Look at R^2s of first eight standardized hermite series coefficients");

%Below plot each of the in-sample densities and re-calculate them from
%Legendre regression and make an overlaid comparison.
for nn=1:NN

    %de-standardize by multiplying with square root of variance of each
    %density and get actual predicted coefficients of hermite-series of SDE
    %densities
    ch(1:8)=bhs0(nn,1:8).*RegressedVarSqRt(nn,1);

    %Below we repeat the same step for original Hermite series data found
    %from simulation. These are true values of hermite series coefficients and not predicted values.
    HCoeff(1:8)=SHCoeff(nn,1:8).*VarSqRt(nn);

    ch(1)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));%Replacing predicted value of mean with analytic value.

    ch(1:8)
    HCoeff(1:8)

    nn
    str=input("Look at predicted coefficients above and true coefficietns below for nnth SDE in data: First
coefficent(mean of SDE) in predicted values has been replaced by its analytic known value")

    clf;
    nn
    PlotHermiteSeriesDensityAndRvGraph(ch(1),ch(2:Order+1),'r');

    hold on

    PlotHermiteSeriesDensityAndRvGraph(HCoeff(1),HCoeff(2:Order+1),'g');
    nn

    str=input("Look at comparison of graphs of nnth density in sample--Green is data and red is our regression from
Legendre Polynomial coefficients");
    clf;
end

end

```

.

.

Please use this new version of routine posted earlier.

.

```
function [WH] = CalculateHermitePolynomialDesignMatrix(Q1,Q2,Q3,Q4,Q5,Q6,Q7,OrderH)

%This function takes seven arrays/regressors input at joint data values in the same
%sequence. And returnd a Hermite polynomials design matrix with all Hermite polynomials
%evaluated at their data values and their possible product values.
%You can use it anywhere in other problems if there are seven regressors.

OrderH0=OrderH+1;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

[Wl1,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1,OrderH);

[Wl2,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2,OrderH);

[Wl3,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3,OrderH);

[Wl4,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4,OrderH);

[Wl5,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q5,OrderH);

[Wl6,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q6,OrderH);

[Wl7,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q7,OrderH);

[Wl12,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2,OrderH);

[Wl13,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3,OrderH);

[Wl14,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4,OrderH);

[Wl15,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q5,OrderH);

[Wl16,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q6,OrderH);

[Wl17,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q7,OrderH);

[Wl23,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3,OrderH);

[Wl24,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4,OrderH);

[Wl25,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q5,OrderH);

[Wl26,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q6,OrderH);

[Wl27,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q7,OrderH);

[Wl34,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4,OrderH);

[Wl35,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q5,OrderH);

[Wl36,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q6,OrderH);

[Wl37,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q7,OrderH);

[Wl45,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q5,OrderH);

[Wl46,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q6,OrderH);

[Wl47,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q7,OrderH);

[Wl56,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q5.*Q6,OrderH);

[Wl57,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q5.*Q7,OrderH);

[Wl67,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q6.*Q7,OrderH);

[Wl123,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3,OrderH);

[Wl124,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4,OrderH);

[Wl125,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q5,OrderH);

[Wl126,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q6,OrderH);

[Wl127,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q7,OrderH);

[Wl134,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4,OrderH);

[Wl135,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q5,OrderH);

[Wl136,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q6,OrderH);

[Wl137,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q7,OrderH);

[Wl145,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q5,OrderH);

[Wl146,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q6,OrderH);

[Wl147,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q7,OrderH);

[Wl156,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q5.*Q6,OrderH);

[Wl157,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q5.*Q7,OrderH);

[Wl167,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q6.*Q7,OrderH);

[Wl234,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4,OrderH);

[Wl235,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q5,OrderH);

[Wl236,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q6,OrderH);

[Wl237,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q7,OrderH);

[Wl245,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q5,OrderH);

[Wl246,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q6,OrderH);

[Wl247,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q7,OrderH);

[Wl256,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q5.*Q6,OrderH);

[Wl257,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q5.*Q7,OrderH);

[Wl267,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q6.*Q7,OrderH);

[Wl345,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q5,OrderH);

[Wl346,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q6,OrderH);

[Wl347,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q7,OrderH);

[Wl356,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q5.*Q6,OrderH);

[Wl357,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q5.*Q7,OrderH);

[Wl367,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q6.*Q7,OrderH);

[Wl456,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q5.*Q6,OrderH);

[Wl457,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q5.*Q7,OrderH);

[Wl467,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q6.*Q7,OrderH);

[Wl567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q5.*Q6.*Q7,OrderH);

[Wl1234,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4,OrderH);

[Wl1235,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q5,OrderH);

[Wl1236,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q6,OrderH);

[Wl1237,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q7,OrderH);

[Wl1245,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q5,OrderH);

[Wl1246,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q6,OrderH);

[Wl1247,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q7,OrderH);

[Wl1256,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q5.*Q6,OrderH);

[Wl1257,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q5.*Q7,OrderH);

[Wl1267,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q6.*Q7,OrderH);

[Wl1345,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q5,OrderH);

[Wl1346,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q6,OrderH);

[Wl1347,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q7,OrderH);

[Wl1356,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q5.*Q6,OrderH);

[Wl1357,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q5.*Q7,OrderH);

[Wl1367,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q6.*Q7,OrderH);

[Wl1456,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q5.*Q6,OrderH);

[Wl1457,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q5.*Q7,OrderH);

[Wl1467,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q6.*Q7,OrderH);

[Wl1567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q5.*Q6.*Q7,OrderH);

[Wl2345,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q5,OrderH);

[Wl2346,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q6,OrderH);

[Wl2347,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q7,OrderH);

[Wl2356,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q5.*Q6,OrderH);

[Wl2357,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q5.*Q7,OrderH);

[Wl2367,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q6.*Q7,OrderH);

[Wl2456,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q5.*Q6,OrderH);

[Wl2457,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q5.*Q7,OrderH);

[Wl2467,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q6.*Q7,OrderH);

[Wl2567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q5.*Q6.*Q7,OrderH);

[Wl3456,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q5.*Q6,OrderH);

[Wl3457,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q5.*Q7,OrderH);

[Wl3467,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q6.*Q7,OrderH);

[Wl3567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q5.*Q6.*Q7,OrderH);

[Wl4567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q4.*Q5.*Q6.*Q7,OrderH);

[Wl12345,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q5,OrderH);

[Wl12346,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q6,OrderH);

[Wl12347,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q7,OrderH);

[Wl12356,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q5.*Q6,OrderH);

[Wl12357,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q5.*Q7,OrderH);

[Wl12367,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q6.*Q7,OrderH);

[Wl12456,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q5.*Q6,OrderH);

[Wl12457,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q5.*Q7,OrderH);

[Wl12467,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q6.*Q7,OrderH);

[Wl12567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q5.*Q6.*Q7,OrderH);

[Wl13456,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q5.*Q6,OrderH);

[Wl13457,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q5.*Q7,OrderH);

[Wl13467,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q6.*Q7,OrderH);

[Wl13567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q5.*Q6.*Q7,OrderH);

[Wl14567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q4.*Q5.*Q6.*Q7,OrderH);

[Wl23456,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q5.*Q6,OrderH);

[Wl23457,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q5.*Q7,OrderH);

[Wl23467,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q6.*Q7,OrderH);

[Wl23567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q5.*Q6.*Q7,OrderH);

[Wl24567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q4.*Q5.*Q6.*Q7,OrderH);

[Wl34567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q3.*Q4.*Q5.*Q6.*Q7,OrderH);

[Wl123456,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q5.*Q6,OrderH);

[Wl123457,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q5.*Q7,OrderH);

[Wl123467,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q6.*Q7,OrderH);

[Wl123567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q5.*Q6.*Q7,OrderH);

[Wl124567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q4.*Q5.*Q6.*Q7,OrderH);

[Wl134567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q3.*Q4.*Q5.*Q6.*Q7,OrderH);

[Wl234567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q2.*Q3.*Q4.*Q5.*Q6.*Q7,OrderH);

[Wl1234567,Zy] = CalculateHermiteSeriesAndReturnHermiteArray(Q1.*Q2.*Q3.*Q4.*Q5.*Q6.*Q7,OrderH);

%Below Tile all of the Hermite polynomials of each of the four random
%parameters in a single matrix and use for least square regression. Zeroth
%Hermite is evaluated in each of the four matrices and has to be removed
%from tiling other than just including one time.
WH(:,1:OrderH0)=Wl1(:,1:OrderH0);
WH(:,OrderH0+1:OrderH0+OrderH)=Wl2(:,2:OrderH0);
WH(:,OrderH0+OrderH+1:OrderH0+2*OrderH)=Wl3(:,2:OrderH0);
WH(:,OrderH0+2*OrderH+1:OrderH0+3*OrderH)=Wl4(:,2:OrderH0);
WH(:,OrderH0+3*OrderH+1:OrderH0+4*OrderH)=Wl5(:,2:OrderH0);
WH(:,OrderH0+4*OrderH+1:OrderH0+5*OrderH)=Wl6(:,2:OrderH0);
WH(:,OrderH0+5*OrderH+1:OrderH0+6*OrderH)=Wl7(:,2:OrderH0);

WH(:,OrderH0+6*OrderH+1:OrderH0+7*OrderH)=Wl12(:,2:OrderH0);
WH(:,OrderH0+7*OrderH+1:OrderH0+8*OrderH)=Wl13(:,2:OrderH0);
WH(:,OrderH0+8*OrderH+1:OrderH0+9*OrderH)=Wl14(:,2:OrderH0);
WH(:,OrderH0+9*OrderH+1:OrderH0+10*OrderH)=Wl15(:,2:OrderH0);
WH(:,OrderH0+10*OrderH+1:OrderH0+11*OrderH)=Wl16(:,2:OrderH0);
WH(:,OrderH0+11*OrderH+1:OrderH0+12*OrderH)=Wl17(:,2:OrderH0);

WH(:,OrderH0+12*OrderH+1:OrderH0+13*OrderH)=Wl23(:,2:OrderH0);
WH(:,OrderH0+13*OrderH+1:OrderH0+14*OrderH)=Wl24(:,2:OrderH0);
WH(:,OrderH0+14*OrderH+1:OrderH0+15*OrderH)=Wl25(:,2:OrderH0);
WH(:,OrderH0+15*OrderH+1:OrderH0+16*OrderH)=Wl26(:,2:OrderH0);
WH(:,OrderH0+16*OrderH+1:OrderH0+17*OrderH)=Wl27(:,2:OrderH0);

WH(:,OrderH0+17*OrderH+1:OrderH0+18*OrderH)=Wl34(:,2:OrderH0);
WH(:,OrderH0+18*OrderH+1:OrderH0+19*OrderH)=Wl35(:,2:OrderH0);
WH(:,OrderH0+19*OrderH+1:OrderH0+20*OrderH)=Wl36(:,2:OrderH0);
WH(:,OrderH0+20*OrderH+1:OrderH0+21*OrderH)=Wl37(:,2:OrderH0);

WH(:,OrderH0+21*OrderH+1:OrderH0+22*OrderH)=Wl45(:,2:OrderH0);
WH(:,OrderH0+22*OrderH+1:OrderH0+23*OrderH)=Wl46(:,2:OrderH0);
WH(:,OrderH0+23*OrderH+1:OrderH0+24*OrderH)=Wl47(:,2:OrderH0);

WH(:,OrderH0+24*OrderH+1:OrderH0+25*OrderH)=Wl56(:,2:OrderH0);
WH(:,OrderH0+25*OrderH+1:OrderH0+26*OrderH)=Wl57(:,2:OrderH0);

WH(:,OrderH0+26*OrderH+1:OrderH0+27*OrderH)=Wl67(:,2:OrderH0);

WH(:,OrderH0+27*OrderH+1:OrderH0+28*OrderH)=Wl123(:,2:OrderH0);
WH(:,OrderH0+28*OrderH+1:OrderH0+29*OrderH)=Wl124(:,2:OrderH0);
WH(:,OrderH0+29*OrderH+1:OrderH0+30*OrderH)=Wl125(:,2:OrderH0);
WH(:,OrderH0+30*OrderH+1:OrderH0+31*OrderH)=Wl126(:,2:OrderH0);
WH(:,OrderH0+31*OrderH+1:OrderH0+32*OrderH)=Wl127(:,2:OrderH0);

WH(:,OrderH0+32*OrderH+1:OrderH0+33*OrderH)=Wl134(:,2:OrderH0);
WH(:,OrderH0+33*OrderH+1:OrderH0+34*OrderH)=Wl135(:,2:OrderH0);
WH(:,OrderH0+34*OrderH+1:OrderH0+35*OrderH)=Wl136(:,2:OrderH0);
WH(:,OrderH0+35*OrderH+1:OrderH0+36*OrderH)=Wl137(:,2:OrderH0);

WH(:,OrderH0+36*OrderH+1:OrderH0+37*OrderH)=Wl145(:,2:OrderH0);
WH(:,OrderH0+37*OrderH+1:OrderH0+38*OrderH)=Wl146(:,2:OrderH0);
WH(:,OrderH0+38*OrderH+1:OrderH0+39*OrderH)=Wl147(:,2:OrderH0);

WH(:,OrderH0+39*OrderH+1:OrderH0+40*OrderH)=Wl156(:,2:OrderH0);
WH(:,OrderH0+40*OrderH+1:OrderH0+41*OrderH)=Wl157(:,2:OrderH0);

WH(:,OrderH0+41*OrderH+1:OrderH0+42*OrderH)=Wl167(:,2:OrderH0);

WH(:,OrderH0+42*OrderH+1:OrderH0+43*OrderH)=Wl234(:,2:OrderH0);
WH(:,OrderH0+43*OrderH+1:OrderH0+44*OrderH)=Wl235(:,2:OrderH0);
WH(:,OrderH0+44*OrderH+1:OrderH0+45*OrderH)=Wl236(:,2:OrderH0);
WH(:,OrderH0+45*OrderH+1:OrderH0+46*OrderH)=Wl237(:,2:OrderH0);

WH(:,OrderH0+46*OrderH+1:OrderH0+47*OrderH)=Wl245(:,2:OrderH0);
WH(:,OrderH0+47*OrderH+1:OrderH0+48*OrderH)=Wl246(:,2:OrderH0);
WH(:,OrderH0+48*OrderH+1:OrderH0+49*OrderH)=Wl247(:,2:OrderH0);

WH(:,OrderH0+49*OrderH+1:OrderH0+50*OrderH)=Wl256(:,2:OrderH0);
WH(:,OrderH0+50*OrderH+1:OrderH0+51*OrderH)=Wl257(:,2:OrderH0);

WH(:,OrderH0+51*OrderH+1:OrderH0+52*OrderH)=Wl267(:,2:OrderH0);

WH(:,OrderH0+52*OrderH+1:OrderH0+53*OrderH)=Wl345(:,2:OrderH0);
WH(:,OrderH0+53*OrderH+1:OrderH0+54*OrderH)=Wl346(:,2:OrderH0);
WH(:,OrderH0+54*OrderH+1:OrderH0+55*OrderH)=Wl347(:,2:OrderH0);

WH(:,OrderH0+55*OrderH+1:OrderH0+56*OrderH)=Wl356(:,2:OrderH0);
WH(:,OrderH0+56*OrderH+1:OrderH0+57*OrderH)=Wl357(:,2:OrderH0);

WH(:,OrderH0+57*OrderH+1:OrderH0+58*OrderH)=Wl367(:,2:OrderH0);

WH(:,OrderH0+58*OrderH+1:OrderH0+59*OrderH)=Wl456(:,2:OrderH0);
WH(:,OrderH0+59*OrderH+1:OrderH0+60*OrderH)=Wl457(:,2:OrderH0);

WH(:,OrderH0+60*OrderH+1:OrderH0+61*OrderH)=Wl467(:,2:OrderH0);

WH(:,OrderH0+61*OrderH+1:OrderH0+62*OrderH)=Wl567(:,2:OrderH0);

WH(:,OrderH0+62*OrderH+1:OrderH0+63*OrderH)=Wl1234(:,2:OrderH0);
WH(:,OrderH0+63*OrderH+1:OrderH0+64*OrderH)=Wl1235(:,2:OrderH0);
WH(:,OrderH0+64*OrderH+1:OrderH0+65*OrderH)=Wl1236(:,2:OrderH0);
WH(:,OrderH0+65*OrderH+1:OrderH0+66*OrderH)=Wl1237(:,2:OrderH0);

WH(:,OrderH0+66*OrderH+1:OrderH0+67*OrderH)=Wl1245(:,2:OrderH0);
WH(:,OrderH0+67*OrderH+1:OrderH0+68*OrderH)=Wl1246(:,2:OrderH0);
WH(:,OrderH0+68*OrderH+1:OrderH0+69*OrderH)=Wl1247(:,2:OrderH0);

WH(:,OrderH0+69*OrderH+1:OrderH0+70*OrderH)=Wl1256(:,2:OrderH0);
WH(:,OrderH0+70*OrderH+1:OrderH0+71*OrderH)=Wl1257(:,2:OrderH0);

WH(:,OrderH0+71*OrderH+1:OrderH0+72*OrderH)=Wl1267(:,2:OrderH0);

WH(:,OrderH0+72*OrderH+1:OrderH0+73*OrderH)=Wl1345(:,2:OrderH0);
WH(:,OrderH0+73*OrderH+1:OrderH0+74*OrderH)=Wl1346(:,2:OrderH0);
WH(:,OrderH0+74*OrderH+1:OrderH0+75*OrderH)=Wl1347(:,2:OrderH0);

WH(:,OrderH0+75*OrderH+1:OrderH0+76*OrderH)=Wl1356(:,2:OrderH0);
WH(:,OrderH0+76*OrderH+1:OrderH0+77*OrderH)=Wl1357(:,2:OrderH0);

WH(:,OrderH0+77*OrderH+1:OrderH0+78*OrderH)=Wl1367(:,2:OrderH0);

WH(:,OrderH0+78*OrderH+1:OrderH0+79*OrderH)=Wl1456(:,2:OrderH0);
WH(:,OrderH0+79*OrderH+1:OrderH0+80*OrderH)=Wl1457(:,2:OrderH0);

WH(:,OrderH0+80*OrderH+1:OrderH0+81*OrderH)=Wl1467(:,2:OrderH0);

WH(:,OrderH0+81*OrderH+1:OrderH0+82*OrderH)=Wl1567(:,2:OrderH0);

WH(:,OrderH0+82*OrderH+1:OrderH0+83*OrderH)=Wl2345(:,2:OrderH0);
WH(:,OrderH0+83*OrderH+1:OrderH0+84*OrderH)=Wl2346(:,2:OrderH0);
WH(:,OrderH0+84*OrderH+1:OrderH0+85*OrderH)=Wl2347(:,2:OrderH0);

WH(:,OrderH0+85*OrderH+1:OrderH0+86*OrderH)=Wl2356(:,2:OrderH0);
WH(:,OrderH0+86*OrderH+1:OrderH0+87*OrderH)=Wl2357(:,2:OrderH0);

WH(:,OrderH0+87*OrderH+1:OrderH0+88*OrderH)=Wl2367(:,2:OrderH0);

WH(:,OrderH0+88*OrderH+1:OrderH0+89*OrderH)=Wl2456(:,2:OrderH0);
WH(:,OrderH0+89*OrderH+1:OrderH0+90*OrderH)=Wl2457(:,2:OrderH0);

WH(:,OrderH0+90*OrderH+1:OrderH0+91*OrderH)=Wl2467(:,2:OrderH0);

WH(:,OrderH0+91*OrderH+1:OrderH0+92*OrderH)=Wl2567(:,2:OrderH0);

WH(:,OrderH0+92*OrderH+1:OrderH0+93*OrderH)=Wl3456(:,2:OrderH0);
WH(:,OrderH0+93*OrderH+1:OrderH0+94*OrderH)=Wl3457(:,2:OrderH0);

WH(:,OrderH0+94*OrderH+1:OrderH0+95*OrderH)=Wl3467(:,2:OrderH0);

WH(:,OrderH0+95*OrderH+1:OrderH0+96*OrderH)=Wl3567(:,2:OrderH0);

WH(:,OrderH0+96*OrderH+1:OrderH0+97*OrderH)=Wl4567(:,2:OrderH0);

WH(:,OrderH0+97*OrderH+1:OrderH0+98*OrderH)=Wl12345(:,2:OrderH0);
WH(:,OrderH0+98*OrderH+1:OrderH0+99*OrderH)=Wl12346(:,2:OrderH0);
WH(:,OrderH0+99*OrderH+1:OrderH0+100*OrderH)=Wl12347(:,2:OrderH0);

WH(:,OrderH0+100*OrderH+1:OrderH0+101*OrderH)=Wl12356(:,2:OrderH0);
WH(:,OrderH0+101*OrderH+1:OrderH0+102*OrderH)=Wl12357(:,2:OrderH0);

WH(:,OrderH0+102*OrderH+1:OrderH0+103*OrderH)=Wl12367(:,2:OrderH0);

WH(:,OrderH0+103*OrderH+1:OrderH0+104*OrderH)=Wl12456(:,2:OrderH0);
WH(:,OrderH0+104*OrderH+1:OrderH0+105*OrderH)=Wl12457(:,2:OrderH0);

WH(:,OrderH0+105*OrderH+1:OrderH0+106*OrderH)=Wl12467(:,2:OrderH0);

WH(:,OrderH0+106*OrderH+1:OrderH0+107*OrderH)=Wl12567(:,2:OrderH0);

WH(:,OrderH0+107*OrderH+1:OrderH0+108*OrderH)=Wl13456(:,2:OrderH0);
WH(:,OrderH0+108*OrderH+1:OrderH0+109*OrderH)=Wl13457(:,2:OrderH0);

WH(:,OrderH0+109*OrderH+1:OrderH0+110*OrderH)=Wl13467(:,2:OrderH0);

WH(:,OrderH0+110*OrderH+1:OrderH0+111*OrderH)=Wl13567(:,2:OrderH0);

WH(:,OrderH0+111*OrderH+1:OrderH0+112*OrderH)=Wl14567(:,2:OrderH0);

WH(:,OrderH0+112*OrderH+1:OrderH0+113*OrderH)=Wl23456(:,2:OrderH0);
WH(:,OrderH0+113*OrderH+1:OrderH0+114*OrderH)=Wl23457(:,2:OrderH0);

WH(:,OrderH0+114*OrderH+1:OrderH0+115*OrderH)=Wl23467(:,2:OrderH0);

WH(:,OrderH0+115*OrderH+1:OrderH0+116*OrderH)=Wl23567(:,2:OrderH0);

WH(:,OrderH0+116*OrderH+1:OrderH0+117*OrderH)=Wl24567(:,2:OrderH0);

WH(:,OrderH0+117*OrderH+1:OrderH0+118*OrderH)=Wl34567(:,2:OrderH0);

WH(:,OrderH0+118*OrderH+1:OrderH0+119*OrderH)=Wl123456(:,2:OrderH0);
WH(:,OrderH0+119*OrderH+1:OrderH0+120*OrderH)=Wl123457(:,2:OrderH0);

WH(:,OrderH0+120*OrderH+1:OrderH0+121*OrderH)=Wl123467(:,2:OrderH0);

WH(:,OrderH0+121*OrderH+1:OrderH0+122*OrderH)=Wl123567(:,2:OrderH0);

WH(:,OrderH0+122*OrderH+1:OrderH0+123*OrderH)=Wl124567(:,2:OrderH0);

WH(:,OrderH0+123*OrderH+1:OrderH0+124*OrderH)=Wl134567(:,2:OrderH0);

WH(:,OrderH0+124*OrderH+1:OrderH0+125*OrderH)=Wl234567(:,2:OrderH0);

WH(:,OrderH0+125*OrderH+1:OrderH0+126*OrderH)=Wl1234567(:,2:OrderH0);

end

```

.

.

.

---

### #2512 — Amin (Topic Author)
*November 3, 2024, 5:35 PM*

I hope friends would have liked my matlab program in the previous post and would like to use similar ideas for Math AI
in their domains of interest. However, what remains to be done after doing the regression of a target
variable/coefficient on appropriate hermite/legendre polynomials of normal/uniform density, that is we need to invert
the results from standard normal/uniform variable back to original variable. And every hermite polynomial series (whose
coefficients have been found by regression) of standard normal variables can be mapped on a polynomial series of
original variable. To give a concrete example in terms of our recent test case of SDEs, we found coefficients of hermite
polynomials of SDE variable/density by further hermite regression on SDE parameters. Now the last remaining step would
be to convert the results of this secondary regression from hermite polynomials of normal density back into simple
polynomials of parameters and their products. So we would be representing coefficients of hermite polynomials of SDE
variables (or alternatively their densities) directly in the form of simple polynomials of SDE parameters and the
products of these parameters. And I think this can be done mostly without any loss of accuracy. I think it would be far
more intuitive to represent the coefficients of hermite polynomials of SDE variables in terms of simple polynomials of
parameters and in some lucky cases we might be able to identify closed form functions of parameters that form these
coefficients of hermite polynomials of SDE variables/(any other target variables in Math AI).

---

### #2513 — Amin (Topic Author)
*November 7, 2024, 8:13 AM*

Friends, sorry to be away for so many days. I want to express myself in two posts, and the first one now is about mind
control and the second one that I will do later would be the technical post.

I want to congratulate Americans on choosing former president Donald Trump as their president again. Even though many of
us are worried about climate change, we have to completely amicably accept the decision of broader American people since
that is how democracies are supposed to work. Even though many of us might differ with conservatives on many issues,
most of them are very patriotic people (sometimes even more so than democrats) and good human beings. Again one thing is
sure that for good of American people and for good of rest of the world, all of us would have to work with new president
and his administration.

For two decades, I have been writing against mind control of tens of thousands of totally innocent people and I hope
that new president Donald Trump would end this evil practice from United States and from rest of the world forever. I
want to firmly tell people that even though I have repeatedly alleged connivance between American defense and a rich
Jewish billionaire and his rich cohort to perpetrate mind control of innocent people, I have nothing against good jews.
Just like anybody else, I want them to work hard and become successful or billionaires or anything beyond that by doing
the right and good things in this world. And there are some jewish billionaires who are embodiment of that and I totally
respect them. And I want people to completely respect all good jews who are good human beings regardless of their wealth
or status. My fight is not with jews but against cruel practice of mind control of ordinary innocent civilians. I do own
that I have been attacking a billionaire jewish billionaire and his rich jewish cohort but it is solely due to their
exceptional cruelty of starting mind control of tens of thousands of innocent people and I must not remain silent about
it. My criticism would have been exactly the same if it were some other group or cohort of people associated with any
other religion or ideology. I must say again that I might not have been careful everywhere to point out and there have
been times when I might have unduly criticized Jews due to emotions and agony related to my helplessness, misery, and
suffering but again and again, repeatedly, I have almost always continued to stress that I have absolutely nothing
against jews who are good human beings and I want them to be as successful as they can and I wish well for them and want
everyone to give great respect to good jews who wish well for others (including non-jews) in the society and hold no
baseless prejudices.

And I have always criticized American defense as being a corrupt puppet of rich jewish cohort when it comes to mind
control. I want to step back here and tell good American people that even more than American defense I criticize corrupt
Army of my country that takes a sacred oath to protect the constitution and not meddle in politics but all of them
without exception break this oath and continue to interfere in politics and make puppets out of politicians and dictate
decisions to higher courts of law. The generals of the very same Pak army are the ones who manage mind control of
innocent and intelligent Pakistani citizens on behest of CIA since they are given hundreds of millions of dollars in
return by CIA every year. Our army is a very corrupt and unprofessional army. The case of American army is quite similar
but not in every domain. It is that in every country with big army, there are unseen (and unwritten) political, cultural
and other barriers (that exist in the mind of people) and corrupt armies usually do not dare to cross these barriers.
For example, in our country with very little unwritten barriers, our army does almost everything wrong and illegal but
still does not completely occupy the government due to possible backlash from people. These unwritten barriers are very
different in our backward country that has remained under army dictatorship for most of the time and in united states
where people have maintained a strong democracy and political rule for most oft the time. As an example, US defense
retards thousands of Americans every year with mind control most of them on insistence of rich jewish cohort and have
cumulatively retarded several hundred thousands of intelligent people all across the world with a very high percentage
of them in America. This has absolutely no constitutional basis and even president of United states cannot suggest to
american defense  to retard anyone. Just a few days ago before the American elections, on linkedin, I saw one of the top
American generals boasting that they were supposed to follow their oath to protect the constitution and not to any
single human being. This boasting is no different than the similar boasting by Pakistan army generals. American army
equally breaks the constitution but in different domain. American army has illegally installed thorough infrastructure
for total mind control of any arbitrary individual by EM waves all over urban United States even though mind control is
a cruel and illegal practice that American constitution does not allow at all. So much so for the grand boastings of
allegiance to constitution by American army generals.

So I say again that I have been vocally criticizing Bad Jews and American defense but please do respect every
professional person in your army and every good jew in your social circle. My criticism is aimed at cruel, inhuman,
illegal and extra-constitutional practices and bad actors behind those practices, and it is not against any religion or
general group of people.

Coming to the point, I want to tell friends that bad actors who are behind cruel mind control will start machinating to
find people in close circle of newly elected president to make sure and lobby for illegal mind control to continue. This
is what happens when a new president is chosen. I really want to request all good people to please do the exact opposite
and try to find genuinely patriotic people in trump's close circle and explain to them how some rich jews are forcing
mind control on good people right and left and convince them to strongly lobby to end mind control forever. Please
approach respectable, towering and patriotic conservative Americans in academia to suggest to new president trump to end
the cruel menace of mind control forever.

Here I would like to tell people that mind control damaged my country and set us back by more than a decade. We were
always a poor country so it was probably not a big deal. There were several hundred or possibly a thousand intelligent
people who were retarded by connivance of CIA and pak army on insistence of bad jews. On the other hand tens of
thousands of intelligent people were retarded in United States and I make this claim that US was set back by at least
five years but nobody could tell as US was even otherwise a very prosperous and rich country. On the other hand, there
is no mind control in countries like China where every intelligent person works totally unfettered. What I mean to say
that these American generals who are boasting their allegiance to constitution are biting the very hand that feeds them.
If US want to compete with China, power and potential of intelligent people has to be unleashed and not controlled by
mind control of tens of thousands of innocent people that has already damaged the country by costing it the progress of
at least five years.

---

### #2514 — Amin (Topic Author)
*November 7, 2024, 9:40 AM*

Friends, I could not work properly for past few days and I am resuming my work again today.

There are a few observations I have. We noticed that once we mapped the SDE parameters and related variables on uniform
density and tried least squares regression with Legendre polynomials, the results of solution to the problem were not
perfectly good. However, once we mapped the same parameters on standard normal density and did least squares regression
to find coefficients of hermite polynomials, the results were very excellent. I believe this is not an issue with
uniform density and Legendre polynomials, rather the issue is type of regression we are using for different densities
and their polynomials.

We know that least squares regression is perfect for normal type densities and I suspect (even though I do not
definitively know) that least absolute deviations regression would be the right choice for uniform type densities and
their associated Legendre polynomials and least squares regressions, even though computationally straightforward and
well suited for normal-based random variables, would be slightly suboptimal for uniform based Legendre polynomials.

However, another factor to consider is that required type of density and polynomial might depend on the type of density
of the variable we are trying to explain.

But Least Absolute Deviations regression is usually not so computationally straightforward.

I want to try iterated least squares based numerical algorithm for LAD type regressions and see how the results are. I
would be working with this and also with the ideas in one of the recent earlier posts where I mentioned that hermite or
Legendre regression has to be done in terms of original variables. So I hope to come back with more ideas and matlab
programs in next few days.

---

### #2515 — Amin (Topic Author)
*November 7, 2024, 11:05 AM*

>
> Friends, I have been working quite slowly due to effect of injection since the injection was very bad with huge mind
control chemicals in it. My program for optimization of R^2 is still not complete but I have been thinking of other
ideas to somehow analytically solve for the coefficients of Z-series that are dependent on X in the orthogonal but
dependent part of decorrelated Y.
>
>
>
> Once we have found the decorrelated $ \tilde{Y}$ as in previous post, we have the equation
>
>
>
>
>
> \begin{align}
>
>  &\tilde{Y_p} \,=\, \, \sigma(X_p) \,\,W_p\,\\
>
>  & \,=\, \, \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\,W_p\, \\
>
> & \,=\, \, \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\, \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\,
H_m(Z_W) \right) \, \, \\
>
>  \end{align}
>
>
>
>
>
> Explaining above equation, part of Y that is orthogonal to X, is described as a product of non-Gaussian zero mean
noise and a function of X denoted as$\sigma(X_p) $ . It is supposed that we do not know the precise Z-series
coefficients of$\sigma(X_p) $ that are given in$ \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right)$ even though
we have complete knowledge of$Z_{X_p}$ for every observation P since we are conditioning on X.
>
>
>
> We take square of both sides of the above equation as
>
>
>
>
>
> \begin{align}
>
> &{\tilde{Y_p}}^2 \,=\, \, \left[ \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\,
\left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right) \, \, \right]^2  \, \\
>
> & \,=\, \, \left[ \sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right]^2 \,\, \left[\sum\limits_{m=1}^{M}\,
\tilde{ch}_m\, H_m(Z_W) \right]^2
>
> \end{align}
>
>
>
> We re-write both the summations in RHS of above equation that are being squared and notice after expanding them, the
new coefficients would range from zero to 2N instead of 0 to N and from zero to 2M in other expression in the summations
inside squares. We write second of these expansions as
>
>
>
> \begin{equation}
>
> \left[  \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right)  \right]^2 \,=\, \sum\limits_{m=0}^{2M}\,
\bar{ch}_m\, H_m(Z_{W})   \,
>
> \end{equation}
>
>
>
> Particularly, we want friends to notice that first coefficient associated with zeroth hermite in above equation would
be equal to expectation of the squared expression or second moment of the respective equation on LHS of above equation
which means that
>
>
>
> \begin{equation}
>
> \bar{ch}_0\, = E \left[ \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m \, H_m(Z_{W}) \right)^2  \,\right] \,
>
> \end{equation}
>
>
>
> So we can re-write one of the previous equations as
>
> \begin{align}
>
> &{\tilde{Y_p}}^2 \,=\, \, \left[ \sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right]^2 \,\,
\left[\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right]^2 \\
>
> &\,=\, \left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \,
\left[\, \sum\limits_{m=0}^{2M}\, \bar{ch}_m\, H_m(Z_{W})   \,\right]\\
>
> &\,=\, \left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \, \left[\, \bar{ch}_0\, +
\, \sum\limits_{m=1}^{2M}\, \bar{ch}_m\, H_m(Z_{W})   \,\right]\\
>
> &\,=\, \bar{ch}_0\,\left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \,+\, \,\left[ \,
\sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right] \, \,\left[ \, \sum\limits_{m=1}^{2M}\, \bar{ch}_m\,
H_m(Z_{W})   \,\right]
>
> \end{align}
>
>
>
> We make the observation that$ \bar{ch}_0\, $ which is equal to expectation of square of W (second moment of W) cannot
be zero. We also notice that since$Z_W$ and$Z_{X_p}$ are both independent, the second term has a zero expectation
because$\left[ \, \sum\limits_{m=1}^{2M}\, \bar{ch}_m\, H_m(Z_{W})   \,\right]$ is all composed of higher hermites each
of which has a zero expectation.
>
>
>
> We also notice that there are non-Zero correlations between first 2N Hermite polynomials,$H_n(Z_{X_p})$ and the first
part of above equation given as
$\, \bar{ch}_0\,\left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \, $ and we can find this
correlated part by regressing${\tilde{Y_p}}^2 \,$ which are squares of data values of orthogonal part (orthogonal to
Y|X). If we regress the${\tilde{Y_p}}^2 \,$ data values on first 2N Hermite polynomials of$Z_{X_p}$ we will be able to
find the coefficients$\bar{dh}_n\,$ in Hermite series expression of (these coefficients would be a constant multiple of
true values of coefficients since there is a multiplication by$\bar{ch}_0\, $ )
>
> \begin{equation}
>
>  \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,
>
> \end{equation}
>
>  and that can lead to coefficients of $\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) $ that we wanted to find since
>
> \begin{equation}
>
>  \, \sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p})   \,   \,=\, \sqrt{\left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\,
H_n(Z_{X_p})   \,  \right]}  \
>
> \end{equation}
>
>
>
> and we can find this square root on right hand side of above equation using our Taylor series expansion formula.
However, higher coefficients after 3rd or 4th coefficients would be rather approximate due to noise in regressions but I
am sure they would be very informative.
>
>
>
> It seems interesting and we realize that a lot of analytics can be done by regressing the square, cube and fourth
power of data values on 2N, 3N and 4N hermites.
>
.

.

Friends, I want to make a more general post in context of above post #  2448       https://forum.wilmott.com/viewtopic.php?t=99702&start=2445#p883896

I want to explain analytic addition of two uncorrelated and correlated Z-series variables something we have not done
before. I also want to explain how to analytically and systematically find the structure of dependence when orthogonal
part of density is dependent on some other Z-series random variables. We will do this through simple and accurate
analytics and not through maximization of any R-squared etc. We will deal with Z-series densities of variances of
different random variables and identify the Z-series densities of covariances of those variables. I will try to make a
new detailed post later tonight explaining all these interesting things.

---

### #2516 — Amin (Topic Author)
*November 7, 2024, 8:49 PM*

>
>
> Friends, I have been working quite slowly due to effect of injection since the injection was very bad with huge mind
control chemicals in it. My program for optimization of R^2 is still not complete but I have been thinking of other
ideas to somehow analytically solve for the coefficients of Z-series that are dependent on X in the orthogonal but
dependent part of decorrelated Y.
>
>
>
> Once we have found the decorrelated $ \tilde{Y}$ as in previous post, we have the equation
>
>
>
>
>
> \begin{align}
>
>  &\tilde{Y_p} \,=\, \, \sigma(X_p) \,\,W_p\,\\
>
>  & \,=\, \, \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\,W_p\, \\
>
> & \,=\, \, \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\, \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\,
H_m(Z_W) \right) \, \, \\
>
>  \end{align}
>
>
>
>
>
> Explaining above equation, part of Y that is orthogonal to X, is described as a product of non-Gaussian zero mean
noise and a function of X denoted as$\sigma(X_p) $ . It is supposed that we do not know the precise Z-series
coefficients of$\sigma(X_p) $ that are given in$ \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right)$ even though
we have complete knowledge of$Z_{X_p}$ for every observation P since we are conditioning on X.
>
>
>
> We take square of both sides of the above equation as
>
>
>
>
>
> \begin{align}
>
> &{\tilde{Y_p}}^2 \,=\, \, \left[ \left(\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right) \,\,
\left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right) \, \, \right]^2  \, \\
>
> & \,=\, \, \left[ \sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right]^2 \,\, \left[\sum\limits_{m=1}^{M}\,
\tilde{ch}_m\, H_m(Z_W) \right]^2
>
> \end{align}
>
>
>
> We re-write both the summations in RHS of above equation that are being squared and notice after expanding them, the
new coefficients would range from zero to 2N instead of 0 to N and from zero to 2M in other expression in the summations
inside squares. We write second of these expansions as
>
>
>
> \begin{equation}
>
> \left[  \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right)  \right]^2 \,=\, \sum\limits_{m=0}^{2M}\,
\bar{ch}_m\, H_m(Z_{W})   \,
>
> \end{equation}
>
>
>
> Particularly, we want friends to notice that first coefficient associated with zeroth hermite in above equation would
be equal to expectation of the squared expression or second moment of the respective equation on LHS of above equation
which means that
>
>
>
> \begin{equation}
>
> \bar{ch}_0\, = E \left[ \left(\sum\limits_{m=1}^{M}\, \tilde{ch}_m \, H_m(Z_{W}) \right)^2  \,\right] \,
>
> \end{equation}
>
>
>
> So we can re-write one of the previous equations as
>
> \begin{align}
>
> &{\tilde{Y_p}}^2 \,=\, \, \left[ \sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) \right]^2 \,\,
\left[\sum\limits_{m=1}^{M}\, \tilde{ch}_m\, H_m(Z_W) \right]^2 \\
>
> &\,=\, \left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \,
\left[\, \sum\limits_{m=0}^{2M}\, \bar{ch}_m\, H_m(Z_{W})   \,\right]\\
>
> &\,=\, \left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \, \left[\, \bar{ch}_0\, +
\, \sum\limits_{m=1}^{2M}\, \bar{ch}_m\, H_m(Z_{W})   \,\right]\\
>
> &\,=\, \bar{ch}_0\,\left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \,+\, \,\left[ \,
\sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right] \, \,\left[ \, \sum\limits_{m=1}^{2M}\, \bar{ch}_m\,
H_m(Z_{W})   \,\right]
>
> \end{align}
>
>
>
> We make the observation that$ \bar{ch}_0\, $ which is equal to expectation of square of W (second moment of W) cannot
be zero. We also notice that since$Z_W$ and$Z_{X_p}$ are both independent, the second term has a zero expectation
because$\left[ \, \sum\limits_{m=1}^{2M}\, \bar{ch}_m\, H_m(Z_{W})   \,\right]$ is all composed of higher hermites each
of which has a zero expectation.
>
>
>
> We also notice that there are non-Zero correlations between first 2N Hermite polynomials,$H_n(Z_{X_p})$ and the first
part of above equation given as
$\, \bar{ch}_0\,\left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,  \right]  \, $ and we can find this
correlated part by regressing${\tilde{Y_p}}^2 \,$ which are squares of data values of orthogonal part (orthogonal to
Y|X). If we regress the${\tilde{Y_p}}^2 \,$ data values on first 2N Hermite polynomials of$Z_{X_p}$ we will be able to
find the coefficients$\bar{dh}_n\,$ in Hermite series expression of (these coefficients would be a constant multiple of
true values of coefficients since there is a multiplication by$\bar{ch}_0\, $ )
>
> \begin{equation}
>
>  \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\, H_n(Z_{X_p})   \,
>
> \end{equation}
>
>  and that can lead to coefficients of $\sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p}) $ that we wanted to find since
>
> \begin{equation}
>
>  \, \sum\limits_{n=0}^{N}\, dh_n\, H_n(Z_{X_p})   \,   \,=\, \sqrt{\left[ \, \sum\limits_{n=0}^{2N}\, \bar{dh}_n\,
H_n(Z_{X_p})   \,  \right]}  \
>
> \end{equation}
>
>
>
> and we can find this square root on right hand side of above equation using our Taylor series expansion formula.
However, higher coefficients after 3rd or 4th coefficients would be rather approximate due to noise in regressions but I
am sure they would be very informative.
>
>
>
> It seems interesting and we realize that a lot of analytics can be done by regressing the square, cube and fourth
power of data values on 2N, 3N and 4N hermites.
>
.

.

Friends, I want to make a more general post in context of above post #  2448       https://forum.wilmott.com/viewtopic.php?t=99702&start=2445#p883896

I want to explain analytic addition of two uncorrelated and correlated Z-series variables something we have not done
before. I also want to explain how to analytically and systematically find the structure of dependence when orthogonal
part of density is dependent on some other Z-series random variables. We will do this through simple and accurate
analytics and not through maximization of any R-squared etc. We will deal with Z-series densities of variances of
different random variables and identify the Z-series densities of covariances of those variables. I will try to make a
new detailed post later tonight explaining all these interesting things.

.

.

Friends, it can be another day or two before I make a detailed post since I want to check all my ideas with matlab
programs before posting them on forum.

---

### #2517 — Amin (Topic Author)
*November 9, 2024, 10:20 AM*

Friends, it may take a day or two more before I can see whether my strategy for analytic addition of two hermite series
densities work (and there is a chance it may not) but I am sharing the main ideas with friends. If it works, we would
not have to follow the route of additions through moments of the densities that sometimes fails to work if a proper
density cannot be easily backed out from sum moments.

We have two hermite series with independent standard normals as

\begin{equation}

X(Z_X)\,=\, \sum\limits_{n=0}^{N}\, ah_n\, H_n(Z_X)

\end{equation}

\begin{equation}

Y(Z_Y)\,=\, \sum\limits_{n=0}^{N}\, bh_n\, H_n(Z_Y)

\end{equation}

I want to sum them and take square as

Eq(1)

\begin{equation}\label{2}

\left[ X(Z_X)\,+\,Y(Z_Y) \right]^2\,=\,\left[ \sum\limits_{n=0}^{N}\, ah_n\, H_n(Z_X)\,+\, \sum\limits_{m=0}^{N}\,
bh_m\, H_m(Z_Y) \right]^2

\end{equation}

The trick I am trying to use is to convert two independent$Z_X$ and$Z_Y$ into a single Z as (following a formula in
wikipedia)

Eq(2)

\begin{equation}

H_n(Z)\,=\,H_n(Z_X\,+\,Z_Y)\,=\, \sum\limits_0^n \, { n \choose k} \, {Z_X}^{(n-k)} \, H_k(Z_Y)

\end{equation}

My plan is to use Eq(2) in Eq(1) and somehow equate

Eq(3)

\begin{align}

\left[ X(Z_X)\,+\,Y(Z_Y) \right]^2\,=\,\left[ \sum\limits_{n=0}^{N}\, ah_n\, H_n(Z_X)\,+\, \sum\limits_{m=0}^{N}\,
bh_m\, H_m(Z_Y) \right]^2

=\, \sum\limits_{l=0}^{2N}\, ch_l\, H_l(Z)\,

\end{align}

this cannot be done by simple algebra since we can separate equation(1) into 2N disjoint equations whose powers are
exactly the same as expansion of each of the equations in$ H_l(Z)\,$ from EQ(2) but coefficients in the equations
derived from Eq(1) would never be simple multiples of coefficients in expansion of Eq(2). So we can separate the terms
in Expansion of Eq(1) based on exponents in expansion of Eq(2) and relate them between Eq(1) and Eq(2)/Eq(3) in a
disjoint way but coefficients on those terms would not be a simple multiple between Eq(1) and Eq(2)/Eq(3). I thought
that I would try variance matching so that resulting coefficient$ch_l$ on the Eq(3) is so that variances between each
hermite in RHS of Eq(3) and its expansion based on Eq(2) (with common power exponents but coefficients not in the same
ratio) with coefficients coming from Eq(1) are matched (These coefficients cannot be matched by algebra and I want to
use variance matching so I assign a single coefficient to resulting hermite in a way that variance between both
equations are the same).

If it works, I will take a square root with Taylor series to find the square root of above equation and write

Eq(4)

\begin{equation}

 V(Z)\,=\,X(Z_X)\,+\,Y(Z_Y) \,=\, \sqrt{\sum\limits_{l=0}^{2N}\, ch_l\, H_l(Z)}\,

\end{equation}

I hope the program would be ready in a day. But there is more to follow regarding variances and their dependence
relationships that I will post later.

---

### #2518 — Amin (Topic Author)
*November 9, 2024, 1:43 PM*

Friends, if nothing unexpected happened, I hope that I will complete this tonight and post the matlab program at that
time. There are some minor additions to previous post.

following equation might have to be applied on variables  with means removed.

Eq(1)

\begin{equation}

\left[ X(Z_X)\,+\,Y(Z_Y) \right]^2\,=\,\left[ \sum\limits_{n=0}^{N}\, ah_n\, H_n(Z_X)\,+\, \sum\limits_{m=0}^{N}\,
bh_m\, H_m(Z_Y) \right]^2

\end{equation}

and following equation

\begin{equation}

H_n(Z)\,=\,H_n(Z_X\,+\,Z_Y)\,=\, \sum\limits_0^n \, { n \choose k} \, {Z_X}^{(n-k)} \, H_k(Z_Y)

\end{equation}

might have to be

\begin{equation}

H_n(\sqrt{2}\,Z)\,=\,H_n(Z_X\,+\,Z_Y)\,=\, \sum\limits_0^n \, { n \choose k} \, {Z_X}^{(n-k)} \, H_k(Z_Y)

\end{equation}

I hope that I would be able to post the worked out matlab program later tonight.

---

### #2519 — Amin (Topic Author)
*November 10, 2024, 11:49 AM*

Friends, sorry for the delay in the matlab program but I have still not being able to solve the problem stated in past
two posts. I had tried to match variance on resulting hermite with argument multiplied by square root of two but that
is  not a standard polynomial and I just realized that it has to be decomposed into standard hermite polynomial series
and then moments have to be matched in each part.

It can turn tricky if moments matching is not easily possible but I am very sure that it can be done with a bit of hack.

I will continue to work on this line but I will also start programming for least absolute deviations regression for
Legendre polynomials for our Math AI simultaneously.

Winters are here and it is still only mildly cold yet and working at night is really fun so I will try to get some good
work done in next few days and weeks.

I have to go out to buy food for a few hours and I will try to post any progress in my work later tonight.

---

### #2520 — Amin (Topic Author)
*November 10, 2024, 9:39 PM*

Friends, sorry again but I could not continue my work tonight. In the Sunday evening, I went out to buy food and water
and bought some water. Whenever I buy water, I drink it first and if it seems good then I decide to buy it. The water
seemed fine in drinking but it is always not easy to tell if it would charge outer surface of your body unless I wash my
body or face/head with it. I use water for both drinking and washing my face and head since water in public supply in
Johar town and many other places is unfit for both these purposes.

I bought food and water and came back and started working. Here I want to tell friends that charged particles and dust
that also gets charged continuously settles on the face/head and body of the mind control victims.  Washing my face and
head with good water is a great way to get rid of charges that settle there and feel fresh and free from mind control to
a reasonable degree. On the other hand if the water had special mind control chemicals and you put it on your face or
head, it will literally suck all life and energy out of you. So I washed my head a bit after starting my work and I was
shocked when I realized that my mental state altered very quickly and I was unable to do any work.

It turned out that when I bought water, they mind control sepoys of army were ready and were mapping my paths (they are
extremely well trained by American army) and they quickly added mind control chemicals in water when I bought it. It
would be interesting for people especially Pakistanis to know that I bought water from a small filtration plant in a
remote street in Sanda area of Lahore while I live in johar town. This was clever and well thought out move since mind
control agents know that I mostly check water by drinking it and not by washing my face and head with it so they knew
that I would most likely not know about bad water until I get home.

When I washed my face, it was already ten thirty at night and I did not want to go out to buy water again but it was
impossible to work again without good water. So I went out and bottled water, which is rather expensive for me, again.

I have been trying to work again but could not get anything done so I have decided to sleep now but thought I would
share it with friends.

It is like one of those movies where CIA is all out to retard someone and CIA officials keep assuring everyone that they
have firmly decided to not retard anyone but every time they assure people of not retarding anyone, their resolve and
singlemindedness to retard the target increases even further. And Pak army is a mere puppet in hands of CIA.

Of course, I will continue my research as I have always done over past several years despite all odds but difficult to
work tonight due to this setback.

---

### #2521 — Amin (Topic Author)
*November 12, 2024, 6:39 PM*

Friends, I have completed work on a slightly different version of the proposed way to add two Z-series random variables.
Unfortunately, the variance based method was close to true density but it was not precise. But I learnt many new things
working on the method and I am very happy that I tried. I really think that my matlab program would be very useful for
some friends who have similar but more robust ideas to add two random variables not because of the logic of the method I
used but because of so many small matlab functions that I used to solve the problem that could be of great help with
other different ideas.  I will post the program with comments hopefully tomorrow.

About finding dependence structure of noises of random variables, the right approach is to follow this post # 2448: https://forum.wilmott.com/viewtopic.php?t=99702&start=2445#p883896

I will try to program it some time in next few days or weeks.

I am restarting work with Math AI research and now I plan to write a new program that solves for joint SDEs correlated
system of stochastic volatility SDE and asset SDE given the parameters of two correlated SDEs. We will be finding the
hermite series representation of both asset and SV random variables given the parameters of the correlated SDEs. I hope
to be posting new programs in a few days.

I also want to work further towards secondary hermite/Legendre polynomial regression in original variables. Obviously
the solution to regression problems would have to be found using common standard normal/uniform density but later we can
possibly represent the solution back in terms of original variables instead of standard normal or uniform densities.

---

### #2522 — Amin (Topic Author)
*November 14, 2024, 10:55 PM*

Friends, sorry for delay in my post on the forum. Unfortunately, everyday, I have to deal with many unwanted things
other than my work and research and on some days they can take too much of my time to not let me work properly. People
behind my persecution are totally unrelenting and they continue to create some problems all the time.

Coming back to our theme of Math AI, I have been thinking about ways to systematically improve the simple method of
hermite/Legendre regression on parameters that I earlier presented. We all know that we can find intelligent
mathematical variables related to variable being predicted and use them in hermite/legendre regression with big
improvement. But I think we have to be able to systematically, even though possibly with trial and error, find functions
of parameters that would greatly improve the results of our hermite/legendre regression. Basically we can try a few
types of functions that cannot be easily captured by polynomials like logarithmic function, and many other special
functions like Hermite functions (not polynomials directly), Legendre functions, Bessel functions, and other specialized
functions of parameters and combinations of parameters. We will have to systematically do trial and error at first to
find out if any of these or other special functions  of parameters have a very good R-squared and include them in the
regression. Even though this trial and error may take some time but this would be many orders of magnitude cheaper than
neural networks that have to be optimized for hours or days while we can find our R-squared for any function of interest
with a single least squares regression taking less than a second. But writing an organized program and iterating over
special functions would still require some effort. Once some functions of parameters have been identified with high
R-squared, we can use  them with parameters or without parameters as dictated by the problem and use them in
hermite/legendre regressions after mapping all special functions and chosen parameters on normal or uniform density (as
I had done in my earlier SDE program with more intelligent math functions of parameters).

So, among other ways, we can improve on simple Math AI systematically by finding other functions that are not in direct
span of the low order polynomials but have high R-squared when used to predict the target variable and we can use them
in hermite/legendre polynomial regression after mapping them on normal/uniform density along with other parameters to
improve the results of regression.

I still have to write comments on my program I wrote for addition of Z-series random variables by matching variances of
hermite polynomials that I mentioned in a past post and I would soon be doing that and then put the matlab program on
forum.

I am also thinking of capturing time in the same single hermite polynomial regression for the SDEs and have done most
work for that. I have decided to complete that and after posting the program on forum, I want to take two or three days
to write a small paper about Math AI and post it on SSRN and Arxiv.  Even though most friends know about my Math AI
research, it would be nice to put it in the form of a small formal paper.

---

### #2523 — Amin (Topic Author)
*November 14, 2024, 11:54 PM*

I have decided to write this post to tell friends that my persecution is not decreasing at all. There are constant and
fierce attempts by authorities to drug my food and deter my work and research. If anything, this activity has strongly
intensified over past few days. And I am worried that they want to hold me back as much as possible for sometime and
then detain me with a psychiatrist who would again diagnose me of strong schizophrenia. The people behind my persecution
are thoroughly resolved to continue it and stop me at all cost and they are absolutely not ready to give in. And they
are waiting for the right time to forcefully detain me and take all good neurotransmitters out of my brain especially
since I have not been detained since early 2001. They used to detain me every year or sometimes twice a year to take all
good neurotransmitters out of my brain every time those neurotransmitters would come back.

I am thankful to so many good American people who strongly protested to their government and forced American defense to
not detain me again. If it were not for efforts of so many good American people, it would never have been possible for
me to do any meaningful research that I did over last three years. I want to ask friends that I will again need their
support even more once again now and next few months an be very crucial. I am perfectly sure if American friends did not
help me again,  I will surely be detained again for 30-50 days to take all good and working neurotransmitters out of me
again. I want to request all readers of my forum to please force American defense and government to end my mind control
forever before it is too late and if you know anyone in authority well in US, please ask for my freedom.

---

### #2524 — Amin (Topic Author)
*November 15, 2024, 6:53 PM*

Friends, I am not in good shape at the moment. Something is very wrong and it seems that they recently introduced some
new frequencies and related NEW weapons where I live. I continued to try to work all day but still could not work as I
was repeatedly getting very disoriented. And in past two days, I have eaten like anything, really way too much but still
I am feeling very exhausted and having muscles pain. Right now I was trying to work but kept on drowsing for past two
hours, I just could not help it. It is hardly twelve while I am used to working till 3:00 or 4:00 in the morning on many
days. And when I gained some consciousness in gaps between deep drowsiness, I l vividly felt that my body was literally
having vibrations. I have been on mind control for more than 25 years but vibrations like this were never noticed by me
ever before. And I am feeling huge muscles pain all over the body at the moment.

Please help me. As they are using new EM weapons and technologies they never used on me before.

---

### #2525 — Amin (Topic Author)
*November 17, 2024, 8:20 AM*

/*Edited Again on Sunday noon.*/

Friends, last night after writing my post, I took a lot of protective measures and tried to be serious about breaking
their control. And then I went to sleep without doing any further work. Today, I was a bit better in the morning but
when I went out to buy food, it was a challenge and I could see at several places that mind control agents reached when
I was trying to buy something.

What I am writing is my honest opinion even though a lot of friends might differ with it to some degree. I think it is
very important that all of us try to have rule of law, and good governance for the benefit of our country and society.
We promote freedom of speech and freedom of press in our societies so that people can criticize bad or wrong actions of
other people and make each other aware of their observations of wrongdoings by some people especially the ones in the
authority in the society while, obviously, every body has to try to investigate the truth on their own without blindly
believing anyone. The purpose of such criticism and related discussions is to try to root out bad practices from the
society and promote good ethics and practices.

Another thing I want to suggest is that true patriotism is not about hiding bad practices taking place in our country
from others, instead it is about exposing such bad practices by unethical people in the public with the final goal that
these bad practices are rooted out from our societies.

Now I will come to the point that I have been suggesting for years that there is a jewish billionaire and his rich
cohort who are behind indiscriminate mind control of a large number of intelligent American people and others . And a
large number of people in American defense have become a mercenerary army that play in the hands of these rich jews.
These rich jews hire quite a few of senior officers from Pentagon and army after their retirement in their large
enterprises and these people are paid millions of dollars each and they enjoy very high social status. One of the most
important purpose of these retired officers is to convince their juniors who are still in official service and have
reached positions of authority to do illegal, extrajudicial and extraconstitutional mind control control of Americans
and others suggested by the rich jewish cohort. This thing is so well known in some jewish circles that many jews
continuously report thousands of people among intelligent students and many others who fall out with these jews for any
reason to mind control by American defense. You do not always have to be extra intelligent, sometimes falling out with a
jew who knows how to approach the rich jewish cohort will seal the fate of the victim by mind control forever. As
always, I would like to mention that there are large number of jews who are opposed to this practice and have absolutely
nothing to do with mind control of innocent people. Please let me specifically say again that there are many very rich
jews and billionaires who have nothing to do with mind control. But I definitely own that I am suggesting this rich
jewish billionaire and his cohort of rich jews are behind most of the mind control and this is a common knowledge in
many jewish circles and many people among these circles know who to approach for mind control of anyone they do not
like.

But what is even more alarming is that all the bad actors behind mind control including rich jewish cohort and mercenary
criminals in American defense, when exposed in public, have absolutely no remorse about their crimes and they become
even more adamant to use all machinatory tactics so that they+ can continue illegal and extrajudicial mind control of
innocent and intelligent people. They have lost all sense of good and evil and have no qualms about continuing the evil
practices at all. It seems many of these bad actors have no conception that retarding innocent human beings is a wrong
thing and an evil practice and they think that mind control of innocent people in the society they do not like is indeed
a good thing.

I know that many good Americans want to end the bad practice of mind control of innocent people from their society
without any retribution against the bad actors behind such evil practices. The bad actors, on the other hand, have
absolutely no remorse about their evil actions and are ready to go to any limit to thwart the attempts of good people to
end mind control and they always try to undermine all good people and their actions towards amicably ending the evil of
mind control from American society. These bad actors are not willing to gracefully acknowledge and be thankful that good
American people do not want to hurt them beyond ending the inhuman practice of mind control from American society and
instead these bad actors are adamantly using all sort of machinatory and bellicose tactics so they can continue and
increase the evil of inhuman mind control of intelligent and innocent human beings.

I really want to suggest if all amicable attempts by good Americans to end mind control fail, it does not mean that they
have to yield to inhuman practices in our society by continuing to play nice. As there is very huge evidence about
existence of extra-judicial, extra-constitutional and cruel mind control and resulting retarding of very large number of
innocent people by American defense and a large number of stories are circulating in academia about people who were
targeted by American defense on behest of jewish cohort, I really believe that it is a great opportunity for some good
journalists in American and international media to write in detail about the hugely widespread evil of extrajudicial,
extraconstitutional, inhuman and cruel practice of mind control and also about nexus between some bad jews and corrupt
people in American defense that has been the dominating force behind this inhuman evil in our societies. I want to
request good American people that if all else fails, please motivate some brave and patriotic journalists to write in
complete detail about the evil of mind control. If it is not possible to write about this inhuman practice in American
newspapers due to possible reprisal from american defense, please break the news in some large British or European
newspaper. I am sure there is enough evidence about existence of mind control and related inhuman and cruel practices
that any serious journalist can firmly stand behind a well written article that completely exposes mind control and
associated cruelties and retarding of thousands of innocent persons by corrupt people in American defense. As I earlier
suggested Patriotism does not consist in saving any false pride or hiding evil practices of our countrymen, it consists
in rationally doing what is broader good for people in our societies by trying to put an end to evil practices.

I will also request readers, for good of our societies, to let at least one journalist you know in the following
American, European and Pakistani newspapers about true nature of mind control and about my thread.

New York Times.

Washington  Post.

CNN.

Fox News.

USA Today.

Los Angeles Times.

Chicago Tribune.

Boston Globe.

Minnesota Star Tribune

New York Post

Newsday

San Fransisco Chronicle

The Dallas Morning News

Tampa Bay Times

Hartford Courant

Publick Occurrences Both Forreign and Domestick

The Michigan Daily

The Denver Post

Pittsburgh Post-Gazette

The Seattle Times

Las Vegas Sun

Bourbon County Citizen

The Register Star

NewYork Metro

The Queens Ledger

Philadelphia Tribune

Baltimore Afro-American

Portland Tribune

Indianapolis Recorder

The Patriot-News

El Diario NY

The Modesto Bee

Fairfax County Times

The Epoch Times

Barron's

Queens Chronicle

Phoenix New Times

El Informador

The Philadelphia Inquirer

New York Daily News

The Star-Ledger

St. Louis Post-Dispatch

The Mercury News

The Arizona Republic

The Plain Dealer

Detroit Free Press

The Press-Enterprise

The Tennessean

Sun Sentinel

The Copenhagen Post

The Slovak Spectator

The Budapest Times

Tirana Times

Menorca Sun

The Vienna Review

Le News

The Irish Times

Die Welt

Het Nieuwsblad

Le Soir

Albania Today

Algemeen Dagblad

De Telegraaf

de Volkskrant

The European

Het Laatste Nieuws

The Daily Telegraph

Daily Mirror

The Sun

Pravda

The Moscow Times

The Guardian

Le Figaro

Le Monde

ABC

la Repubblica

Il Messaggero

El Periódico de Catalunya

El Mundo

Libération

El País

Kronen Zeitung

La Stampa

Frankfurter Allgemeine Zeitung

Bild

20 minutes

Sport

Aftenposten

Marca

Gazeta Wyborcza

Izvestia

Die Presse

Süddeutsche Zeitung

La Tribune

Novaya Gazeta

Neue Zürcher Zeitung

Dagens Nyheter

Expressen

La Gazzetta dello Sport

Mladá fronta Dnes

Urdu News

Daily Pakistan

Dawn

Daily Express

Daily Jang

The Express Tribune

The News International

The Nation

Pakistan Today

Daily Dunya

Daily Ummat

Nawaiwaqt

The Regional Times of Sindh

Pakistan Observer

Khabrain

Daily Ausaf

Daily Jasarat

Daily Nai Baat

Daily Basharat

Daily Times

The Frontier Post

Daily Sarhad

Daily Imroze

The Pakistan Times

The Financial Daily

Daily Aaj

Daily Mashriq

Millat

Business Recorder

Daily Inqilab

Kawish

Daily Lokaai

Talár

Maidan Daily

Daily Asas

Christian Voice

The Friday Times

Awam

Daily Awami Awaz

The Star

Al Akhbar

Khyber Mail

Nawai Watan

Sajjan

Daily Hilal Pakistan

Daily Sindhu

Daily Koshish

Daily Mehran

Bhulekha

Civil and Military Gazette

---

### #2526 — Amin (Topic Author)
*November 17, 2024, 4:04 PM*

Friends, very sorry for being away from technical and research posts. But things had become too difficult and were
getting out of my control and I was unable to properly do my research work.

I tried to resume my research this evening and had some very interesting ideas that I want to share with friends. We
have found, when we are doing hermite or legendre regression with all the products of various orders included, the
number of regression variables increase at a rate of 2^n-1  which effectively limits how to include large number of
regressors in the orthogonal polynomial regression. I have been trying to think of ways to include larger number of
variables in the regression but without increasing the total number of regression variables exponentially. It turns out
that there could be ways to limit the number of variables included in regression if covariance matrix across each
hermite polynomial of all regression variables could be described by a small number of eigenvectors by PCA(Principal
component analysis) or alternatively using techniques of CCA(canonical corrrelation analysis). This can hugely reduce
the number of total regressors in the regression but at the cost of possibly very small loss of R-squared.

I describe the ideas in detail in the next post.

---

### #2527 — Amin (Topic Author)
*November 17, 2024, 7:23 PM*

Limiting the Number of Variables in Math AI Hermite/Legendre Polynomial Regression

We have found, when we are doing hermite or legendre regression with all the products of various orders included, the
number of regression variables increase at a rate of$ \,C_1^n \,+\,C_2^n \,+C_3^n\,+\, \ldots\, C_n^n\,=\,2^n-1 $ which
effectively limits how to include large number of regressors in the orthogonal polynomial regression.

It turns out that there could be ways to limit the number of variables included in regression if covariance matrix
across each hermite polynomial of all regression variables could be described by a small number of eigenvectors with
significant eigenvalues using PCA(Principal component analysis) . This can hugely reduce the number of total regressors
in the regression but at the cost of possibly very small loss of R-squared. For example if there are M=8 input variables
and there are N=10 hermite polynomials associated with each variable, we would have 1 + 255 * 10 total basis functions
in the regression. However if (255 * 255) covariance matrix of each of the ten hermite polynomials could be described by
20 significant principle components, the number of basis functions could reduce to 1 + 20 * 10 basis functions in total.
Since there is one covariance matrix for each polynomial order in Hermite series, we would have to do one PCA for each
covariance matrix. If there are ten hermite polynomials in regression, there would be ten covariance matrices and ten
PCAs in total with one PCA for each of these matrices

We first revisit Hermite polynomial Regression. Let us consider the case of hermite polynomial regression with M
variables and N Hermite polynomials in regression. This means that when we include all products of M variables, the
total number of basis functions would be$2^{(M-1)} \, \, N\, $ .

Suppose we want to regress a random variable Y on$X_1,\,, X_2,\,X_3,\, \ldots, X_M $ , and their products of all order.
Let us suppose$K\, =\,2^{(M-1)}$ , We would have to make hermite/Legendre series of all of the above variables as

$
$\, X_k(Z_{X_k})\,=\, ah_0 \, + \, ah_1 \, H_1(Z_{X_k}) \,+ \, ah_2 \, H_2(Z_{X_k}) \,+ \ldots \,+ \, ah_N \, H_N(Z_{X_k}) \,\text{where} \, k\,=\,1,\,2,\, \dots, \,K $
$

$$\, Y(Z_Y)\,=\, bh_0 \, + \, bh_1 \, H_1(Z_Y) \,+ \, bh_2 \, H_2(Z_Y) \,+ \ldots \,+ \, bh_N \, H_N(Z_Y) \, $$

Let us suppose that we have a total of P joint data observations of above K regressors and we include N hermite
polynomials for each of the K explanatory variable in the regression. And we also have P joint observations of the
target regressand and all of the three explanatory variables. In order to perform a regression of Y on hermite
polynomials of$X_k$ , We would have to map data of$X_k$ and$Y$ on Standard normal density to find corresponding
$Z_{X_{k,p}}$ and$Z_{Y_{p}}$ . Then we would find first N Hermite polynomial values for each of the mapped$Z_{X_{k,p}}$
and$Z_{Y_{p}}$ . The final regression equation would be given in the matrix form as

\begin{equation}

\begin{bmatrix}

1 & H_1(Z_{X_{1,1}}) & \ldots & H_N(Z_{X_{1,1}}) & H_1(Z_{X_{2,1}}).& \ldots.. & H_N(Z_{X_{2,1}}) & \ldots  & \ldots  &
H_1(Z_{X_{K,1}}).& \ldots.. & H_N(Z_{X_{K,1}}) \\

1 & H_1(Z_{X_{1,2}}) & \ldots & H_N(Z_{X_{1,2}}) & H_1(Z_{X_{2,2}}).& \ldots.. & H_N(Z_{X_{2,2}}) & \ldots & \ldots  &
H_1(Z_{X_{K,2}}).& \ldots.. & H_N(Z_{X_{K,2}}) \\\ldots & \ldots & \ldots & \ & \ldots & \ldots.. & \ldots \\   1 &
H_1(Z_{X_{1,p}}) & \ldots & H_N(Z_{X_{1,p}}) & H_1(Z_{X_{2,p}}).& \ldots.. & H_N(Z_{X_{2,p}}) & \ldots & \ldots  &
H_1(Z_{X_{K,p}}).& \ldots.. & H_N(Z_{X_{K,p}}) \\ \ldots & \ldots & \ldots & \ & \ldots & \ldots.. & \ldots \\

1 & H_1(Z_{X_{1,P}}) & \ldots & H_N(Z_{X_{1,P}}) & H_1(Z_{X_{2,P}}).& \ldots.. & H_N(Z_{X_{2,P}}) & \ldots & \ldots  &
H_1(Z_{X_{K,P}}).& \ldots.. & H_N(Z_{X_{K,P}}) \\

\end{bmatrix}   \begin{bmatrix} \beta_0 \\ \beta_{X_{1,1}} \\ \ldots \\ \beta_{X_{1,N}} \\ \beta_{X_{2,1}}\\ \ldots \\
\beta_{X_{2,N}} \\ \ldots\\ \ldots\\ \beta_{X_{K,1}}\, \\ \ldots \\ \beta_{X_{K,N}} \end{bmatrix} \\ \,=\,
\begin{bmatrix} Y_1 \\ Y_2 \\ ...  \\  Y_p \\ ... \\  Y_P \end{bmatrix}

\end{equation}

\begin{equation}

\boldsymbol{H \, \beta}\,=\,\boldsymbol{y}

\end{equation}

Friends, I am a bit tired and fatigued but would complete this post tomorrow.

---

### #2528 — Amin (Topic Author)
*November 20, 2024, 12:22 AM*

/* Edited and Re-Posted*/

Friends, I would complete the last post later in a proper formal style but here are the main ideas.

Let us consider the case of hermite polynomial regression with M variables and N Hermite polynomials in regression. This
means that when we include all products of M variables, the total number of basis functions would be
$2^{(M-1)} \, \, N\, $ .

Suppose we want to regress a random variable Y on$X_1,\,, X_2,\,X_3,\, \ldots, X_M $ , and their products of all order.
Let us suppose$K\, =\,2^{(M-1)}$ , We would have to make hermite/Legendre series of all of the above variables as

$
$\, X_k(Z_{X_k})\,=\, ah_0 \, + \, ah_1 \, H_1(Z_{X_k}) \,+ \, ah_2 \, H_2(Z_{X_k}) \,+ \ldots \,+ \, ah_N \, H_N(Z_{X_k}) \,\text{where} \, k\,=\,1,\,2,\, \dots, \,K $
$

$$\, Y(Z_Y)\,=\, bh_0 \, + \, bh_1 \, H_1(Z_Y) \,+ \, bh_2 \, H_2(Z_Y) \,+ \ldots \,+ \, bh_N \, H_N(Z_Y) \, $$

Since there are N hermite polynomials and we already know that there is a different Covariance matrix/Correlation matrix
associated with each of the N polynomials.

In Order to decrease the number of regressors in Hermite/Legendre regression and limit the least square regression to
only relevant regressors, we follow an analytics based numerical procedure.

Let us suppose we calculate Covariance matrix of$X_1, \,X_2,\,\ldots\,,X_K$ with Y. This is a (K+1)*(K+1) matrix. If
there are N hermite polynomials of every regressor in regression, there will be N such matrices described as
$\boldsymbol{\rho_{X_k\, Y,n}}$

\begin{equation}

\boldsymbol{\rho_{X_k\, Y,n}}\,=\,\begin{bmatrix}  \rho_{X_{1}X_{1}, n} & \rho_{X_{1}X_{2},n} & ....& ..... & 
\rho_{X_{1}X_{K},n} &  \rho_{X_{1}Y,n} \\

\rho_{X_{2}X_1, n} & \rho_{X_{2}X_{2},n} & ....& ..... &  \rho_{X_{2}X_{K},n} &  \rho_{X_{2}Y,n} \\ .... & .... & ....&
.... & ....\\ \rho_{X_{k}X_1, n} & \rho_{X_{k}X_{2},n} & ....& ..... &  \rho_{X_{k}X_{K},n} &  \rho_{X_{k}Y,n} \\.... &
... & ... & ... & ... \\

\rho_{X_{K}X_1, n} & \rho_{X_{k}X_{2},n} & ....& ..... &  \rho_{X_{K}X_{K},n} &  \rho_{X_{K}Y,n} \\

\rho_{Y\,X_1, n} & \rho_{Y\,X_{2},n} & ....& ..... &  \rho_{Y \,X_{K},n} &  \rho_{Y\,Y,n} \\

\end{bmatrix}

\end{equation}

for the new readers, I will write the equation for correlation between hermite polynomials as

\begin{equation}

\rho_{XY,n} \, = \,  \frac{\sum\limits_{p=1}^{P}\, H_n(Z_{X,p}) \, \, H_n(Z_{Y,p}) \,}{\sqrt{\sum\limits_{p=1}^{P} \,
{H_n(Z_{X,p})}^2 \,\sum\limits_{p=1}^{P} \, \, {H_n(Z_{Y,p})}^2 \,}}

\end{equation}

In what follows, we use notation$H_n(Z)$ for a proper normalized hermite polynomial while$\bar{H}_n(Z)$ with a bar on
it, will be used for all later calculations and bookkeeping and will continue to change value.

We start with   $H_n(Z)$  equal to   $\bar{H}_n(Z)$  at start.

$
$ \,E \left[{\bar{H}_n}^2(Z_{X_k}) \right]=\, E \left[ {H_n}^2(Z_{X_k})\, \right]=\, n! \,,\,\,\,\,{k\,=\,1,\,2\, \ldots\,K}$
$

$$ \,E \left[ {\bar{H}_n}^2(Z_Y) \, \right]=\, E \left[\,{H_n}^2(Z_{Y})\,\right]=\, n! \, $$

We remove the effect of first regressors$X_1$ 's hermite polynomial from all other hermite polynomials of regressors and
regressands as

$
$ \,E \left[{\bar{H}_n}^2(Z_{X_k})\, \right]=\,\,E \left [ {\bar{H}_n}^2(Z_{X_k})\, \right]\,- \,{\rho}^2_{X_1 X_k,n}  E \left[{H_n}^2(Z_{X_1}) \right] \,,\,\,\,\,{k\,=\,1,\,2\, \ldots\,K}$
$

$
$ \,E \left[{\bar{H}_n}^2(Z_Y)\, \right]=\, E \left[{\bar{H}_n}^2(Z_{Y}) \, \right]\,- \,{\rho}^2_{X_1 Y,n} \, E \left[ {H_n}^2(Z_{X_1}) \right]$
$

which means in terms of correlations

$
$ \,{\bar{\rho}}^2_{X_k\,Xk,n}\,=\,\,{\rho}^2_{X_k\,X_k,n}\,- \,{\rho}^2_{X_1 X_k,n}  \,{\rho}^2_{X_1 X_1,n}  \,,\,\,\,\,{k\,=\,1,\,2\, \ldots\,K}$
$

$$ \,{\bar{\rho}}^2_{Y\,Y,n}\,=\,\,{\rho}^2_{Y\,Y,n}\,- \,{\rho}^2_{X_1 Y,n}  \,{\rho}^2_{X_1 X_1,n}  \,,\,$$

We will also have to alter the other non-diagonal correlations as

$
$\, {\bar{\rho}}^2_{X_{k1}\,X_{k2},\, n} \,=\,{\rho}^2_{X_{k1}\,X_{k2},n} \,-\,\,{\rho}_{X_1\,X_{k1},n} \,\,{\rho}_{X_1\,X_{k2},n} \,\,\,{\rho}^2_{X_1\,X_1,n} \,\,$
$

$
$\, {\bar{\rho}}^2_{X_{k1}\,Y,\,n} \,=\,{\rho}^2_{X_{k1}\,Y,n} \,-\,\,\rho_{X_1\,X_{k1},n} \,\,\rho_{X_1\,Y,n} \,\,\,{\rho}^2_{X_1\,X_1,n} \,\,$
$

Now we remove the effect of We remove the effect of second regressors$X_2$ 's hermite polynomial from all other hermite
polynomials of regressors and regressands which means in terms of correlations

$
$ \,{\bar{\rho}}^2_{X_k\,Xk,n}\,=\,\,{\bar{\rho}}^2_{X_k\,X_k,n}\,- \,{\bar{\rho}}^2_{X_2 X_k,n}  \,{\bar{\rho}}^2_{X_2 X_2,n}  \,,\,\,\,\,{k\,=\,2,\,3\, \ldots\,K}$
$

$
$ \,{\bar{\rho}}^2_{Y\,Y,n}\,=\,\,{\bar{\rho}}^2_{Y\,Y,n}\,- \,{\bar{\rho}}^2_{X_2 Y,n}  \,{\bar{\rho}}^2_{X_2 X_2,n}  \,,\,$
$

We will also have to alter the other non-diagonal (k1,k2) correlations as

$
$\, {\bar{\rho}}^2_{X_{k1}\,X_{k2},n} \,=\,{\bar{\rho}}^2_{X_{k1}\,X_{k2},n} \,-\,\,\bar{\rho}_{X_2\,X_{k1},n} \,\,\bar{\rho}_{X_2\,X_{k2},n} \,\,{\bar{\rho}}^2_{X_2\,X_2,n} \,\,$
$

$
$\, {\bar{\rho}}^2_{X_{k1}\,Y,n} \,=\,{\bar{\rho}}^2_{X_{k1}\,Y,n} \,-\,\,\bar{\rho}_{X_2\,X_{k1},n} \,\,\bar{\rho}_{X_2\,Y,n} \,\,\,{\bar{\rho}}^2_{X_2\,X_2,n} \,$
$

So in a similar fashion, We continue to remove the effect of all regressors from regressand Y.

We notice the individual effect of correlation from each regressor variable$X_k$ onto regressand Y after effect of all
previous variables have been removed, if this effect is too small and trivial, we do not include that regressor variable
in our following least squares regression that finds global coefficients for our Hermite/Legendre equations. So we find
this effect for all$2^{m}\,-\,1$ regressor variables and decide based on pure correlations(after removal of effect of
previous common correlations) which regressor variables to keep in least squares regression and which regressor
variables to remove from regression without sacrificing any R-squared.

---

### #2529 — Amin (Topic Author)
*November 21, 2024, 8:16 PM*

How To Represent Normal Density based Hermite Regressors Back into Polynomial Functions of Original Parameter Variable

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
\ldots.. & H_N(Z_{XY_1}) \\

1 & H_1(Z_{X_2}) & \ldots & H_N(Z_{X_2}) & H_1(Z_{Y_2}).& \ldots.. & H_N(Z_{Y_2}) & H_1(Z_{XY_2}).& \ldots.. &
H_N(Z_{XY_2})  \\ \ldots & \ldots & \ldots & \ & \ldots & \ldots.. & \ldots \\   1 & H_1(Z_{X_p}) & \ldots &
H_N(Z_{X_p}) & H_1(Z_{Y_p}) & \ldots & H_N(Z_{Y_p}) & H_1(Z_{XY_p}).& \ldots.. & H_N(Z_{XY_p}) \\ \ldots & \ldots &
\ldots & \ & \ldots & \ldots.. & \ldots \\

1 & H_1(Z_{X_P}) & \ldots & H_N(Z_{X_P})  & H_1(Z_{Y_P})  & \ldots &  H_N(Z_{YP}) & H_1(Z_{XY_P}).& \ldots.. &
H_N(Z_{XY_P}) \\

\end{bmatrix}   \begin{bmatrix} \beta_0 \\ \beta_{X,1} \\ \ldots \\ \beta_{X,N} \\ \beta_{Y,1}\\\dots \\ \beta_{Y,N} \\
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

After regression coefficients have been found, we can write the solution of regression equation as

$
$\,V\,=\,\beta_0 \,+\,\beta_{X,1} \,H_1(Z_{X}) \,+\, \ldots\, +\, \beta_{X,N}\, H_N(Z_{X}) \\+\,\beta_{Y,1} \, H_1(Z_{Y}).\,+ \, \ldots\,+\,\beta_{Y,N} \, H_N(Z_{Y})\\+\,\beta_{XY,1} \,H_1(Z_{XY}).+\, \ldots \, +\,\beta_{XY,N} \, H_N(Z_{XY}) $
$

or

$$\,V\,=\,\beta_0 \,+\,W_1(Z_X) +\, W_2(Z_Y)\,+\,W_3(Z_{XY}) \, $$

$
$\,W_1(Z_X) \,=\, \beta_{X,1} \,H_1(Z_{X}) \,+\, \ldots\, +\, \beta_{X,N}\, H_N(Z_{X})\,=\, \bar{\beta}_{X,1} \,Z_{X} \,+\, \ldots\, +\, \bar{\beta}_{X,N}\, {Z_{X}}^N \,$
$

$
$\,W_2(Z_Y) \,=\, \beta_{Y,1} \,H_1(Z_{Y}) \,+\, \ldots\, +\, \beta_{Y,N}\, H_N(Z_{Y}) \,=\, \bar{\beta}_{Y,1} \,Z_{Y} \,+\, \ldots\, +\, \bar{\beta}_{Y,N}\, {Z_{Y}}^N\,$
$

$
$\,W_3(Z_{XY}) \,=\, \beta_{XY,1} \,H_1(Z_{XY}) \,+\, \ldots\, +\, \beta_{XY,N}\, H_N(Z_{XY})\,=\, \bar{\beta}_{XY,1} \,Z_{XY} \,+\, \ldots\, +\, \bar{\beta}_{XY,N}\, {Z_{XY}}^N\,$
$

We want to represent each of the above expressions given by Ws which are represented by standard normal into their
original variables. We could expand$W_1(Z_X)$ which is already a series into a different series around median of
original variable$X\,=\,X_0$ . Similarly, we could expand$W_1(Z_Y)$ and$W_1(Z_{XY})$ around$Y\,=\,Y_0$ and
$XY\,=\,{XY}_0$ respectively.

Converting a Z-series Expression into a Polynomial Series in Original Variable Through Taylor Series Expansion

Suppose we have calculated Z-series of a random variable W which is denoted as$W(Z)$ and now we want to convert it into
a polynomial function of$X$ then this resulting series is found through Taylor expansion . First we define a Variable F
as

\begin{equation}

 F(X)=f(Z(X))

\end{equation}

We will expand the right hand side of above Equation as a Taylor series around median of standard normal density at
$Z(X_0)\,=\,Z_0$ and it is given to fourth order as (please note that derivatives between non-Gaussian random variable X
and normal random variable Z of all orders$\frac{d^n X}{dZ^n}$ have previously been calculated at median either from
differentiating Z_series of X on both sides repeatedly.

We want to emphasize that in Taylor expansion below,$f(Z)$ represents the Z-series polynomial which has to be converted
to a different polynomial in original variable X.

\begin{multline}\label{2.5.2}

F(X)\,\, = \, f(Z_0)+(X-X_0) \, \frac{dZ}{dX} \, f'(Z_0) \\

  + \frac{1}{2} \left( X-X_0 \right)^2  \left[ \, {\left( \frac{dZ}{dX} \right) }^2 f''(Z_0)+ \, \frac{d^2Z}{dX^2} \,
f'(Z_0) \right]  \\

  + \frac{1}{6} \left(X-X_0 \right)^3 \left[ \, f^{(3)}(Z(X_0))  \, { \left( \frac{dZ}{dX} \right)}^3 \, +3  \,
\frac{dZ}{dX} \,  \, \frac{d^2Z}{dX^2} \, f''(Z_0)+ \, \frac{d^3Z}{dX^3} \, f'(Z_0) \right] \\

+ \frac{1}{24} \left(X-X_0 \right)^4 \left[ \, f^{(4)}(Z_0)  \, {\left( \frac{dZ}{dX} \right)}^4 \,+6 f^{(3)}(Z_0 ) \, {
\left( \frac{dZ}{dX} \right) }^2 \, \, \frac{d^2Z}{dX^2} \, \right] \\

  + \frac{1}{24} \left(X-X_0 \right)^4 \left[ +3 \, { \left( \frac{d^2Z}{dX^2} \right) }^2 \, f''(Z_0) + \, 4 \,
\frac{d^3Z}{dX^3} \, \, \frac{dZ}{dX} \, f''(Z_0) \, +\, { \frac{d^4Z}{dX^4}} \, f'(Z_0) \right]

\end{multline}

---

### #2530 — Amin (Topic Author)
*November 23, 2024, 12:17 PM*

Friends, my monthly antipsychotic injection is due tomorrow. My persecution continues unabatedly and I have not been
able to program for past 7-10 days. Programming requires some strength in the brain and they have been able to keep me
sedated most of the time over past one week and I have not been able to do any programming. I have been trying to make
interesting posts for friends who want to pursue similar work but I have not programmed for quite some time now.

I am afraid that I would be sharply worse off and more sedated after the antipsychotic injection tomorrow and I may not
be able to write with perfect clarity. I want to tell friends that American defense has absolutely no plans to end my
persecution and they want to take my persecution to the logical end when I would have been mentally retarded and they
are ready to go to any limits to achieve that target. They have still continued my persecution in full swing and once
more suitable time comes, they would openly detain me and take all good neurotransmitters out of my brain possibly
forever.

I am extremely thankful to all good Americans who tried to protect me from more severe and cruel persecution in the past
even when nobody in my country was ready to help me at all. If they had not been protesting strongly to American
government resulting in quite decreased mind control for me, I would not have been able to do any decent research at
all. And I am very grateful to people who became interested in my work and tried to use some of my suggested
mathematical methods in their research ideas. It is a very good feeling to know that many intelligent people would be
able to do interesting things with some helpful research I was able to do.

I would want to take this opportunity to request all Americans to please help end my mind control forever. One way you
could truly help me could be by asking any friends or connections in newspapers and TV News companies to follow my case
here on wilmott. Please ask any media outlets and jouranlists you know to follow my thread about everyday stories of
persecution by American defense. And please suggest to them to write or speak about it in their media about ending
extra-constitutional and extra-judicial mind control by American defense forever. I want to request European researchers
to please bring attention of European news media towards my case, research and continuing persecution that increases as
my research becomes more successful. And please ask your Pakistani students abroad to tell Pakistani news media about
stories of mind control of intelligent people in our country by our own army for hefty bribes they get from American
defense.

Please approach 2-3 of these meida outlets and tell them about my research and continuing mind control and ask them to
follow my case and possibly write very bravely about huge extrajudicial mind control by American defense. I do not
realistically think that my persecution is going to end anytime soon and I will need strong support from good Americans
and good people from all over the world.

Please continue to follow my thread since I expect that my persecution is going to be even more eventful in coming days
and weeks and a lot of interesting even though very inhuman and cruel things might follow.

MSNBC

NBC

CNN

Fox Business

Fox News

American Broadcasting Company

USA Network

CBS

CNBC

Fox

HLN

Blaze Media

Al Jazeera America

Discovery Channel

RT

HBO

NewsNation

MyNetworkTV

Free Speech TV

Newsmax TV

Scripps News

CNN en Español

PBS

ABC News Live

Link TV

Lifetime

VH1

France 24

Univision

ION Television

NBC News

Investigation Discovery

MeTV

DD India

ESPNews

BBC America

CNBC Europe

C-SPAN

A & E Network

Hallmark Channel

DoD News Channel

National Geographic

TNT

euronews

Sky News

Bloomberg Television

New York Times.

Washington  Post.

CNN.

Fox News.

USA Today.

Los Angeles Times.

Chicago Tribune.

Boston Globe.

Minnesota Star Tribune

New York Post

Newsday

San Fransisco Chronicle

The Dallas Morning News

Tampa Bay Times

Hartford Courant

Publick Occurrences Both Forreign and Domestick

The Michigan Daily

The Denver Post

Pittsburgh Post-Gazette

The Seattle Times

Las Vegas Sun

Bourbon County Citizen

The Register Star

NewYork Metro

The Queens Ledger

Philadelphia Tribune

Baltimore Afro-American

Portland Tribune

Indianapolis Recorder

The Patriot-News

El Diario NY

The Modesto Bee

Fairfax County Times

The Epoch Times

Barron's

Queens Chronicle

Phoenix New Times

El Informador

The Philadelphia Inquirer

New York Daily News

The Star-Ledger

St. Louis Post-Dispatch

The Mercury News

The Arizona Republic

The Plain Dealer

Detroit Free Press

The Press-Enterprise

The Tennessean

Sun Sentinel

The Copenhagen Post

The Slovak Spectator

The Budapest Times

Tirana Times

Menorca Sun

The Vienna Review

Le News

The Irish Times

Die Welt

Het Nieuwsblad

Le Soir

Albania Today

Algemeen Dagblad

De Telegraaf

de Volkskrant

The European

Het Laatste Nieuws

The Daily Telegraph

Daily Mirror

The Sun

Pravda

The Moscow Times

The Guardian

Le Figaro

Le Monde

ABC

la Repubblica

Il Messaggero

El Periódico de Catalunya

El Mundo

Libération

El País

Kronen Zeitung

La Stampa

Frankfurter Allgemeine Zeitung

Bild

20 minutes

Sport

Aftenposten

Marca

Gazeta Wyborcza

Izvestia

Die Presse

Süddeutsche Zeitung

La Tribune

Novaya Gazeta

Neue Zürcher Zeitung

Dagens Nyheter

Expressen

La Gazzetta dello Sport

Mladá fronta Dnes

Urdu News

Daily Pakistan

Dawn

Daily Express

Daily Jang

The Express Tribune

The News International

The Nation

Pakistan Today

Daily Dunya

Daily Ummat

Nawaiwaqt

The Regional Times of Sindh

Pakistan Observer

Khabrain

Daily Ausaf

Daily Jasarat

Daily Nai Baat

Daily Basharat

Daily Times

The Frontier Post

Daily Sarhad

Daily Imroze

The Pakistan Times

The Financial Daily

Daily Aaj

Daily Mashriq

Millat

Business Recorder

Daily Inqilab

Kawish

Daily Lokaai

Talár

Maidan Daily

Daily Asas

Christian Voice

The Friday Times

Awam

Daily Awami Awaz

The Star

Al Akhbar

Khyber Mail

Nawai Watan

Sajjan

Daily Hilal Pakistan

Daily Sindhu

Daily Koshish

Daily Mehran

Bhulekha

Civil and Military Gazette

---

### #2531 — Amin (Topic Author)
*November 23, 2024, 3:20 PM*

>
> Converting a Z-series Expression into a Polynomial Series in Original Variable Through Taylor Series Expansion
>
>
>
>
>
> Suppose we have calculated Z-series of a random variable W which is denoted as$W(Z)$ and now we want to convert it
into a polynomial function of$X$ then this resulting series is found through Taylor expansion . First we define a
Variable F as
>
>
>
> \begin{equation}
>
>  F(X)=f(Z(X))
>
> \end{equation}
>
>
>
> We will expand the right hand side of above Equation as a Taylor series around median of standard normal density at
$Z(X_0)\,=\,Z_0$ and it is given to fourth order as (please note that derivatives between non-Gaussian random variable X
and normal random variable Z of all orders$\frac{d^n X}{dZ^n}$ have previously been calculated at median either from
differentiating Z_series of X on both sides repeatedly.
>
>
>
> We want to emphasize that in Taylor expansion below,$f(Z)$ represents the Z-series polynomial which has to be
converted to a different polynomial in original variable X.
>
>
>
> \begin{multline}\label{2.5.2}
>
>
>
> F(X)\,\, = \, f(Z_0)+(X-X_0) \, \frac{dZ}{dX} \, f'(Z_0) \\
>
>   + \frac{1}{2} \left( X-X_0 \right)^2  \left[ \, {\left( \frac{dZ}{dX} \right) }^2 f''(Z_0)+ \, \frac{d^2Z}{dX^2} \,
f'(Z_0) \right]  \\
>
>   + \frac{1}{6} \left(X-X_0 \right)^3 \left[ \, f^{(3)}(Z(X_0))  \, { \left( \frac{dZ}{dX} \right)}^3 \, +3  \,
\frac{dZ}{dX} \,  \, \frac{d^2Z}{dX^2} \, f''(Z_0)+ \, \frac{d^3Z}{dX^3} \, f'(Z_0) \right] \\
>
> + \frac{1}{24} \left(X-X_0 \right)^4 \left[ \, f^{(4)}(Z_0)  \, {\left( \frac{dZ}{dX} \right)}^4 \,+6 f^{(3)}(Z_0 ) \,
{ \left( \frac{dZ}{dX} \right) }^2 \, \, \frac{d^2Z}{dX^2} \, \right] \\
>
>   + \frac{1}{24} \left(X-X_0 \right)^4 \left[ +3 \, { \left( \frac{d^2Z}{dX^2} \right) }^2 \, f''(Z_0) + \, 4 \,
\frac{d^3Z}{dX^3} \, \, \frac{dZ}{dX} \, f''(Z_0) \, +\, { \frac{d^4Z}{dX^4}} \, f'(Z_0) \right]
>
>
>
>
>
> \end{multline}
>

.

.

Friends, in the above copied part of post, I have mentioned that you need to know$\frac{d^n Z}{dX^n}$ which is directly
not available and has to be found from different derivatives given by$\frac{d^n X}{dZ^n}$ which is known.

specifically if use the notation   $Gn\,=\,\frac{d^n Z}{dX^n}$  and  $Fn\,=\,\frac{d^n X}{dZ^n}$

Then formulas for first eight inverse derivatives$Gn\,=\,\frac{d^n Z}{dX^n}$ are given in terms of known derivatives
$Fn\,=\,\frac{d^n X}{dZ^n}$ as

G1 = 1/F1;       %First derivative of inverse function

G2 = -F2/F1^3;   %second derivative of inverse function

G3 =(3 *F2^2)/F1^5 - F3/F1^4; %Third derivative of inverse function

G4 = -15* F2^3/F1^7 + 10*F2* F3/F1^6 - F4/F1^5 ;%Fourth derivative of inverse function

G5=(105* F2^4 - 105* F1 *F2^2* F3 + 10* F1^2* F3^2 + 15* F1^2* F2* F4 - F1^3* F5)/F1^9;

G6=(1/(F1^11))*(-945* F2^5 + 1260* F1* F2^3* F3 - 280* F1^2* F2* F3^2 - ...

  210* F1^2 * F2^2* F4 + 35* F1^3* F3* F4 + 21* F1^3 *F2* F5 - F1^4* F6);

G7=(1/(F1^13))*(10395* F2^6 - 17325* F1* F2^4 *F3 + 6300* F1^2* F2^2* F3^2 - ...

  280* F1^3* F3^3 + 3150* F1^2* F2^3* F4 - 1260* F1^3* F2* F3* F4 + ...

  35 *F1^4* F4^2 - 378* F1^3* F2^2* F5 + 56* F1^4* F3* F5 + 28* F1^4* F2* F6 - ...

  F1^5* F7);

G8=(1/(F1^15))*(155925* F2^7 - 214830* F1* F2^5 *F3 + 37800 *F1^2 *F2^3* F3^2 + ...

  7560* F1^3* F2* F3^3 + 36225* F1^2* F2^4* F4 - 630* F1^3* F2^2* F3* F4 - ...

  2100* F1^4 *F3^2* F4 - 595* F1^4* F2* F4^2 - 3654* F1^3* F2^3* F5 - ...

  952* F1^4* F2* F3* F5 + 126* F1^5* F4* F5 + 154* F1^4* F2^2* F6 + ...

  84* F1^5 *F3 *F6 + 8* F1^5* F2* F7 - F1^6* F8 - 28* F1^13* F2* G7);

Please read my posts about inverse function derivatives here as: https://forum.wilmott.com/viewtopic.php?t=99702&start=1305#p868932

and  https://forum.wilmott.com/viewtopic.php?t=99702&start=1305#p868935

Suppose we have a function y=f(x) and g(f(x)) is its inverse so that

$y=\, f(x)$

$g(f(x))=x $

We are given an initial pair of solution$(x_0,y_0)$ , and we want to find out x given a certain value of function y.
This can easily be done by a Taylor expansion in terms of inverse derivatives of g as

$ x \, = \, x_0 \, + \, g'(f(x)) \, (y-y_0) \, + 1/2 \, g''(f(x)) \, {(y-y_0)}^2 \,+ 1/6 \, g'''(f(x)) \, {(y-y_0)}^3 \, + 1/24 \, g^{iv}(f(x)) \, {(y-y_0)}^4 \,+ ....$

All these inverse derivatives can easily be found from derivatives of $f(x)$ as

$g'(f(x)) = 1/f'(x)$       %First derivative of inverse function

$g''(f(x)) = -f''(x)/{f'(x)}^3$   %second derivative of inverse function

$g'''(f(x)) =3  \, {f''(x)}^2/{f'(x)}^5 - f'''(x)/{f'(x)}^4$; %Third derivative of inverse function

$g^{iv}(f(x)) = -15 \, {f''(x)}^3/{f'(x)}^7 + 10 \, f''(x) \, f'''(x)/{f'(x)}^6 - f^{iv}(x)/{f'(x)}^5 $ ;%Fourth
derivative of inverse function

If you take enough terms in Taylor series and it converges well, you can easily approximate the inverse function over a
large enough domain. According to my understanding it will only give a real root if derivatives are real and that can be
both helpful in some cases but may be undesirable in some other cases. For root search, you can easily do one or two
extra iterations of the explicit function to get to the root.

I am attaching a program that does root-search of a simple quadratic equation.

```
function [] = InverseFunctionRoot()

%y=f(x); here f(x) is simply a quadratic equation.
%Given an inital pair (x0,y0), the program finds x that corresponds to the target value y.
%For a real root make sure that b^2-4*a*c>0;
%The method works for real roots.

a=.05;
b=1;
c=5.0;
x0=4;

y0=a*x0^2 + b * x0+ c
F1=2*a*x0+b;  %first derivative of f(x)
F2=2*a; %second derivative of f(x)
F3=0;  %Third derivative of f(x)
F4=0;  %Fourth derivative of f(x)
F5=0;
F6=0;
F7=0;
F8=0;

G1 = 1/F1;       %First derivative of inverse function
G2 = -F2/F1^3;   %second derivative of inverse function
G3 =(3 *F2^2)/F1^5 - F3/F1^4; %Third derivative of inverse function
G4 = -15* F2^3/F1^7 + 10*F2* F3/F1^6 - F4/F1^5 ;%Fourth derivative of inverse function
G5=(105* F2^4 - 105* F1 *F2^2* F3 + 10* F1^2* F3^2 + 15* F1^2* F2* F4 - F1^3* F5)/F1^9;
G6=(1/(F1^11))*(-945* F2^5 + 1260* F1* F2^3* F3 - 280* F1^2* F2* F3^2 - ...
  210* F1^2 * F2^2* F4 + 35* F1^3* F3* F4 + 21* F1^3 *F2* F5 - F1^4* F6);
G7=(1/(F1^13))*(10395* F2^6 - 17325* F1* F2^4 *F3 + 6300* F1^2* F2^2* F3^2 - ...
  280* F1^3* F3^3 + 3150* F1^2* F2^3* F4 - 1260* F1^3* F2* F3* F4 + ...
  35 *F1^4* F4^2 - 378* F1^3* F2^2* F5 + 56* F1^4* F3* F5 + 28* F1^4* F2* F6 - ...
  F1^5* F7);

G8=(1/(F1^15))*(155925* F2^7 - 214830* F1* F2^5 *F3 + 37800 *F1^2 *F2^3* F3^2 + ...
  7560* F1^3* F2* F3^3 + 36225* F1^2* F2^4* F4 - 630* F1^3* F2^2* F3* F4 - ...
  2100* F1^4 *F3^2* F4 - 595* F1^4* F2* F4^2 - 3654* F1^3* F2^3* F5 - ...
  952* F1^4* F2* F3* F5 + 126* F1^5* F4* F5 + 154* F1^4* F2^2* F6 + ...
  84* F1^5 *F3 *F6 + 8* F1^5* F2* F7 - F1^6* F8 - 28* F1^13* F2* G7);

y=5;  %The target value for which we want to find x.

c1=c-y;
x_true1=(-b+sqrt(b^2-4*a*c1))/(2*a);
x_true2=(-b-sqrt(b^2-4*a*c1))/(2*a);

%Taylor expansion for x using inverse derivatives.
x=x0+G1*(y-y0)+1/2*G2*(y-y0)^2+1/6*G3*(y-y0)^3+1/24*G4*(y-y0)^4;
x6=x0+G1*(y-y0)+1/2*G2*(y-y0)^2+1/6*G3*(y-y0)^3+1/24*G4*(y-y0)^4+1/120*G5*(y-y0)^5 + 1/720*G6*(y-y0)^6;
x7=x0+G1*(y-y0)+1/2*G2*(y-y0)^2+1/6*G3*(y-y0)^3+1/24*G4*(y-y0)^4+1/120*G5*(y-y0)^5 + 1/720*G6*(y-y0)^6
+1/(7*720)*G7*(y-y0)^7;
x8=x0+G1*(y-y0)+1/2*G2*(y-y0)^2+1/6*G3*(y-y0)^3+1/24*G4*(y-y0)^4+1/120*G5*(y-y0)^5 + 1/720*G6*(y-y0)^6
+1/(7*720)*G7*(y-y0)^7+1/(8*7*720)*G8*(y-y0)^8;

y0
y
x_true1
x_true2
x0
x
x6
x7
x8
x_true1
end
```

.

.

.

---

### #2532 — Amin (Topic Author)
*November 23, 2024, 4:00 PM*

I found another old matlab program for inverse function derivatives that you can easily use directly to convert
derivatives till eighth order. It is basically the same thing but more convenient.

.

.

```
function [G] = FindInverseFunctionDerivatives(F)

F1=F(1);  %first derivative of f(x)
F2=F(2); %second derivative of f(x)
F3=F(3);  %Third derivative of f(x)
F4=F(4);  %Fourth derivative of f(x)
F5=F(5);
F6=F(6);
F7=F(7);
F8=F(8);

G(1) = 1/F1;       %First derivative of inverse function
G(2) = -F2/F1^3;   %second derivative of inverse function
G(3) =(3 *F2^2)/F1^5 - F3/F1^4; %Third derivative of inverse function
G(4) = -15* F2^3/F1^7 + 10*F2* F3/F1^6 - F4/F1^5 ;%Fourth derivative of inverse function
G(5)=(105* F2^4 - 105* F1 *F2^2* F3 + 10* F1^2* F3^2 + 15* F1^2* F2* F4 - F1^3* F5)/F1^9;
G(6)=(1/(F1^11))*(-945* F2^5 + 1260* F1* F2^3* F3 - 280* F1^2* F2* F3^2 - ...
  210* F1^2 * F2^2* F4 + 35* F1^3* F3* F4 + 21* F1^3 *F2* F5 - F1^4* F6);
G(7)=(1/(F1^13))*(10395* F2^6 - 17325* F1* F2^4 *F3 + 6300* F1^2* F2^2* F3^2 - ...
  280* F1^3* F3^3 + 3150* F1^2* F2^3* F4 - 1260* F1^3* F2* F3* F4 + ...
  35 *F1^4* F4^2 - 378* F1^3* F2^2* F5 + 56* F1^4* F3* F5 + 28* F1^4* F2* F6 - ...
  F1^5* F7);

G(8)=(1/(F1^15))*(155925* F2^7 - 214830* F1* F2^5 *F3 + 37800 *F1^2 *F2^3* F3^2 + ...
  7560* F1^3* F2* F3^3 + 36225* F1^2* F2^4* F4 - 630* F1^3* F2^2* F3* F4 - ...
  2100* F1^4 *F3^2* F4 - 595* F1^4* F2* F4^2 - 3654* F1^3* F2^3* F5 - ...
  952* F1^4* F2* F3* F5 + 126* F1^5* F4* F5 + 154* F1^4* F2^2* F6 + ...
  84* F1^5 *F3 *F6 + 8* F1^5* F2* F7 - F1^6* F8 - 28* F1^13* F2* G(7));

end

```

.

.

.

---

### #2533 — Amin (Topic Author)
*November 24, 2024, 6:08 AM*

Friends, today I will try to calculate inverse function derivatives formulas beyond eight order  till 12th or possibly
14th order and hope to post the formulas for these higher derivatives conversions  later tonight.

---

### #2534 — Amin (Topic Author)
*November 24, 2024, 5:20 PM*

Friends, here is the matlab program that calculates first sixteen inverse function derivatives.

If we use the notation$G(n)\,=\,\frac{d^n Z}{dX^n}$ and$F(n)\,=\,\frac{d^n X}{dZ^n}$ , Then formulas for first sixteen
inverse derivatives$G(n)\,=\,\frac{d^n Z}{dX^n}$ are given in terms of known derivatives$F(n)\,=\,\frac{d^n X}{dZ^n}$
and$G(m)\,=\,\frac{d^m Z}{dX^m}$ where m

---

### #2535 — Amin (Topic Author)
*November 25, 2024, 6:26 AM*

Friends, I frequently use Mathematica for Taylor series expansions, other series manipulation, related algebra and
calculus and will suggest to younger people on the forum to make extensive use of mathematica for their research.

I am attaching a PDF version of first page of very simple mathematica notebook that I used to calculate inverse function
derivatives. If you are not perfectly oriented with inverse derivatives, Please make sure that you read first about them
on wikipedia or some good book.

In the following image, the first derivative is equated to one and rest are equated to zero. You have to do some algebra
with the last term in derivatives expansion.

[![Image](../images/i.postimg.cc/0Q891Yr4/Inverse-Function-Derivatives.png)](https://postimg.cc/Y4y51m6N)

---

### #2536 — Amin (Topic Author)
*November 25, 2024, 8:55 AM*

Friends, I had a few thoughts that I wanted to share for those people who joined the thread later and have not been
following it for years.

It is important to distinguish between a random variable X and its density p(X). In a Z-series, we represent random
variable X by a series in another random variable which is standard normal Z. We do not get density of X directly from
Z-series. When dealing with continuous random variables, a large number of them can be represented in terms of
derivatives of each other by another series rescaling the coefficients on these derivatives.

For example, if for example if you graph a standard normal as a function of X using inverse function derivatives from
Z-series of X, it will be a curve and not a density.

For calculation of densities, you have to use the formula

$$p_X(X)\,=\,p_Z(Z)\,\frac{dZ}{dX} $$  Eq(1)

This can be easily calculated on a grid since X and Z and their derivative corresponding to each other are known on a
grid.

If you want to analytically find the density of X as an analytic expression in X, you would have to  change variables in
standard normal density formula as

$$p_X(X)\,=\,p_Z(Z(X))\,\frac{dZ(X)}{dX} $$      Eq(2)

and densities of functions of X would have to be found from change of variable in density of X possibly found from above
expression.

When we invert coefficients from hermite series regression of X on target variable Y and change variables in regression
result from standard normal to another series expression in X, we do not find density of this function of X. After this
change of variable in regression result, We merely find the relationship Y=f(X). We do  not get density of Y or density
of f(X). If you are looking for analytic expression of density/function of Y=f(X) , you will have to do it by doing
change of variable with respect to normal density as suggested in Eq(2).

---

### #2537 — Amin (Topic Author)
*November 25, 2024, 12:57 PM*

Friends, I had an antipsychotic injection yesterday but it will be a few days before I start to see a strong effect from
the injection. I am however trying to re-start my programming work.

Tonight, I will try to program reverse-conversion of results from hermite polynomial regression of coefficients of SDE
densities back to polynomials in original parameters of the SDE and be able to compare the hermite polynomial regression
results and original polynomial converted results.

As I had earlier suggested that I want to do a paper on my Math AI ideas that I have been writing on the forum
specifically in the form of finding coefficients of hermite-series of the SDE densities as a function parameters of the
densities. I want to make a lot of further changes to previous work and hope that a complete research paper would be
ready in 15-20 days. I will surely continue to post all matlab programs that I will code in the meantime.

---

### #2538 — Amin (Topic Author)
*November 27, 2024, 6:01 AM*

Friends, I have restarted my programming work for past two days but I still have some difficulty working and I have to
make quite some effort.

I noticed that uniformly distributed input parameters can easily be converted directly into an analytic hermite series
by our regression on data with a extremely good R-Squared. I will double check it again in the evening. From there we
could invert the Z-series directly into parameters or functions of parameters. I will be working on this for next two to
three days. I really do not see any extreme difficulty in our being able to find a series expansion of hermite
coefficients of SDEs as a series in original parameters and functions of those parameters. But a complete work could
take another 2-3 days. In my experiments I see a good R-Squared in converting uniformly distributed parameters and their
functions into hermite polynomials of standard normal. And I also notice good R-Squared when SDE hermite coefficients
are regressed on our parameter derived hermite polynomials. So all the links in transformations have very good
R-Squared, so I expect when we convert all of this back to original parameters form, the results will also be very good.

Friends, I must say that I have not been able to work well for past two weeks or even more but that was due to things
beyond my control. My hand also fractured so I had to stop doing a lot of things that protect me from mind control and
on some days I could not take good food. And then, I believe, they also introduced some special frequencies to retard me
and stop me from doing my research. And all of this combined became too much for me to handle and I was unable to
properly work. But I am totally determined that this winters, we would do many interesting things with our Math AI and I
really want to work towards that goal. I am better at the moment and am looking for things to improve.

---

### #2539 — Amin (Topic Author)
*November 27, 2024, 12:56 PM*

Friends, I had mentioned in the previous post that I could represent uniform based parameters in terms of hermite
polynomial series with very high R-Squared. Here is an interesting graph of uniform density represented by seven first
hermite polynomials.

In the context of random sampling of mean reverting SDE parameters so that sampled parameters would be used to simulate
the SDEs and find their densities. I think it would be better to sample as closely as possible in terms of the hermite
series based (approximately) uniform density because, if we sample from hermite based uniform, it would be very easy to
invert the analytical hermite series representation using inverse function derivatives to convert the hermite based
regression expressions into original parameters form with high fidelity.

We had earlier chosen uniform density for sampling SDE parameters over the desired range of parameters for SDEs since it
seemed natural to use uniform density but we could equally use some slightly different density over the range as long as
we could invert it with high accuracy (or alternatively represent it with hermite polynomials with high fidelity). So we
can judicially use another density (for sampling of SDE parameters) that is well behaved and as close to uniform as
possible and can easily be described directly by hermite polynomial series.

Below is hermite based uniform density.

.

.

.

[![Image](../images/i.postimg.cc/dQCWYG24/Uniform-Into-Hermites01.png)](https://postimg.cc/NLg889PH)

---

### #2540 — Amin (Topic Author)
*November 27, 2024, 5:08 PM*

Friends, if we choose a hermite based distribution for sampling initial values of parameters of SDEs that have to be
simulated to produce initial population sample, I suppose we would be better off by choosing a Hermite/Gaussian
distribution that is almost flat with short or little tails. It would be better to find a discretized version of the
chosen density so that moments of discretized density match the analytic moments of the corresponding hermite series
used to generate hermite based parameter distribution. Once we have a discrete "discretized distribution", we can
scramble it with another random number generator to effectively simulate the initial values of parameters of the SDEs
whose densities have to be found.

---

### #2541 — Amin (Topic Author)
*November 28, 2024, 2:07 PM*

In this program, we take a Z-series of random variable X as input and then we calculate a Z-series of some function of X
which is called Y through Taylor series. We want to find the relationship between two Z-series Y(Z) and X(Z) in terms of
a polynomial of original variable X.

In order to do this, we make a common Z-grid for Z-series of X and Y. And then we do a regression of Y(Zn) on powers of
(X(Zn)-X(Z0)) to find a polynomial relationship between Y and X in terms of polynomial of X. Since Z in both Z-series is
common, we regress the points of Y on powers of X with common Z on the grid. Later, We plot the  values of Y=f(X)
derived from Z-series of X and also derived from the polynomial(which is found from regression) in terms of X with
graphs overlaid on each other.

The final purpose of program is to be able to convert Z-series found from hermite polynomial regressions of a variable X
on other variables and convert the hermite polynomial relationships of X that are originally in the form of Z-series
back into polynomials of original variable X. The program works well.

If you change the function square-root used in the program to other functions, you might have to increase the length of
Z-series and polynomial series in original variables.

.

.

.

```
function [] = FindOriginalFunctionBetweenZseries()

%In this program, we take a Z-series of random variable X as input and then we calculate a
%Z-series of some function of X which is called Y through Taylor series. In
%order to find the relationship between Y and X in terms of variable X, we
%make a common Z-grid for Z-series of X and Y. And then we do a regression
%of Y on powers of X to find a polynomial relationship between Y and X in
%terms of polynomial of X. Since Z in both Z-series is common, we regress
%the points of Y on powers of X with common Z on the grid. We plot the
%values of Y=f(X) derived from Z-series of X and also derived from the
%polynomial(which is found from regression) in terms of X.
%The final purpose of program is to be able to convert Z-series found from
%hermite polynomial regressions of a variable X on other variables and convert
%the hermite polynomial relationships into polynomials of original variable X.
%The program works very  well.

%I am specifying a hermite series of X below. Please feel free to replace it
%with coefficients of a different Hermite series of your choice.

ah0 =1.064485203912489;
ah =[0.558397347212915,   0.166481083148759,   0.035702046924930, 0.005934841254001,   0.000782071270084, 
 0.000081035831783, 0.000006297040467];

%Convert to Z-series of X
[a0,a]=ConvertHermiteSeriesToZSeries(ah0,ah,7);

%Below, calculate Z-series of square root of X through Taylor Series.
% So Y= X^.5; but Y and X are both Z-series. You can replace it with a
% different function as well.
q=.5;  %For quotient.
fX=sqrt(a0);
dnfXdXn(1)=q*(a0).^(q-1);
for nn=2:10
    dnfXdXn(nn)=dnfXdXn(nn-1)*(q-nn+1)/(a0);
end

%Below we calculate coefficients of Z-series of Y=X^.5;
[d0,d] = CalculateTaylorCoeffsOfFunctionZSeries(fX,dnfXdXn,a(1:7),7);

%Below, we make a Z-grid of NN points.

NN=101;

Z(1:NN)=-4+.08*(0:100);

%Calculate values of X and its function Y on the same grid.
X(1:NN)=a0+a(1)*Z(1:NN)+a(2)*Z(1:NN).^2+a(3)*Z(1:NN).^3+a(4)*Z(1:NN).^4+a(5)*Z(1:NN).^5+a(6)*Z(1:NN).^6+a(7)*Z(1:NN).^7;
Y(1:NN)=d0+d(1)*Z(1:NN)+d(2)*Z(1:NN).^2+d(3)*Z(1:NN).^3+d(4)*Z(1:NN).^4+d(5)*Z(1:NN).^5+d(6)*Z(1:NN).^6+d(7)*Z(1:NN).^7;

Y(1:NN,1)=Y(1:NN);

X0=a0; %We want to expand Y in terms of X around median of X=X0=a0.

%Populate least squares regression design matrix with values of powers of
%(X-X0) on all the grid points
W(1:NN,1)=1;
W(1:NN,2)=(X(1:NN)-X0);
W(1:NN,3)=(X(1:NN)-X0).^2;
W(1:NN,4)=(X(1:NN)-X0).^3;
W(1:NN,5)=(X(1:NN)-X0).^4;
W(1:NN,6)=(X(1:NN)-X0).^5;
W(1:NN,7)=(X(1:NN)-X0).^6;
W(1:NN,8)=(X(1:NN)-X0).^7;
%W(1:NN,9)=(X(1:NN)-X0).^8;
%W(1:NN,10)=(X(1:NN)-X0).^9;

%Do least squares regression
gCoeff=inv(W'*W)*(W'*Y);

%gCoeff(1:8,1)

%Generate the values of new Y2 along the grid from regression coefficients.
Y2(1:NN)=gCoeff(1)+gCoeff(2)*(X(1:NN)-X0)+gCoeff(3)*(X(1:NN)-X0).^2+gCoeff(4).*(X(1:NN)-X0).^3+gCoeff(5).*(X(1:NN)-X0).^4+gCoeff(6)*(X(1:NN)-X0).^5+gCoeff(7)*(X(1:NN)-X0).^6+gCoeff(8)*(X(1:NN)-X0).^7;%+gCoeff(9)*(X(1:NN)-X0).^8+gCoeff(10)*(X(1:NN)-X0).^9;

plot(X,Y,'g',X,Y2,'r')

str=input("Look at comparison of Y=f(X(Z)) calculated from Z-series as a function of Z in green. And Y calculated on
grid as a function of polynomial in X");
end

```

.

.

.

Context of the graph below: I have two Z-series. Z-series of a random variable X and square root of X(You can replace it
in the program for other functions as wwell). And then I find the relationship between Y(Z) and X(Z) in terms of a
polynomial in X. The graph shows true relationship between Y and X in green and our rregressed relationship between Y
and X in terms of a polynomial series directly in original variable X in red. Both graphs are overlaid.

.

[![Image](../images/i.postimg.cc/Zq6JPRBT/Original-Polynomial-Series.png)](https://postimg.cc/4KNCsXQM)

---

### #2542 — Amin (Topic Author)
*November 28, 2024, 3:43 PM*

Please note about matlab program in previous post that original variable regression (red line in graph) follows the
Z-series of Y(X(Z)) (green line in the graphs) found from Taylor series. If Taylor series used to make a function of X,
does not properly capture the function due to smaller number of terms in the expansion, that is a different problem to
tackle and can be solved by increasing the number of terms in Taylor expansion. Function Z-series obtained by taylor is
only to have a reference Z-series that can be computed as a series expansion in X and compared with the reference
Z-series.

The test is true if red line follows green line.

Purpose of Taylor was only to find a suitable function as an example to demonstrate the ideas.

---

### #2543 — Amin (Topic Author)
*November 30, 2024, 2:19 AM*

Friends, I want to re-do the calculations of the whole project after re-sampling SDE parameters from a hermite
polynomials based distribution. I was able to get a slightly better version of initial hermite based distribution that
is plotted below.

If it goes well, the whole new matlab program can take 3-4 days. Here is a graph of initial hermite based distribution I
intend to use for sampling of parameters.

.

.

..

.

[![Image](../images/i.postimg.cc/8zbMFw14/Uniform-From-Hermites.png)](https://postimg.cc/tsYYw3nn)

---

### #2544 — Amin (Topic Author)
*December 1, 2024, 5:10 PM*

Friends, I am writing this post because of my continuing persecution with mind control. Whenever  I try to work
seriously, they use waves to sedate me and make me very drowsy and I mostly become half asleep. They have been trying
their best to not let me work and continue to create all sorts of problems. They pretend to be better but they do not
let go of any opportunity to create problems for me.  And they continue to add drugs to water and food on a daily basis.
For example, if I find that water of some place in the city is good, it is guaranteed to become drugged with mind
control chemicals within a few hours after that and I can never find good water at the same place after a day or two.
They continue to actively try to thwart me from getting good food and water.

I want to request friends to please ask American government to end my mind control. And if it does not work, I want to
request all friends to please inform 2-3 news papers and TV News media about my case and how I have passed past 25 years
in extreme torture and still bad sheep in American defense still do not want to let go of me despite that I have tried
to do good research against all odds. And please let them know that as my research progressed, the attempts by American
defense to retard me continued to become more frenetic. This is despite I have made all my research public over more
than past eight years.  Please ask these news media to write in complete detail about extremely widespread mind control
by American defense to please rich jews and how American defense makes entire nations (like Pakistan, Malaysia and many
more) barren by putting thousands of intelligent Math and compute science professionals under mind control in these
countries when rich jews wish American defense to do that.

Friends stopping mind control when it is in relatively early phase and it is relatively rare for established and
successful people to be retarded. But if it is not stopped now, I am sure there will be a time when no one would dare to
speak against or annoy those who back mind control and their will will prevail over the complete society. Please stop
mind control before it is too late to be able to make efforts to stop it.  Please ask the newspapers to write about it
before it is too late and Americna defense and rich jews are emboldened to point of no return.

MSNBC

NBC

CNN

Fox Business

Fox News

American Broadcasting Company

USA Network

CBS

CNBC

Fox

HLN

Blaze Media

Al Jazeera America

Discovery Channel

RT

HBO

NewsNation

MyNetworkTV

Free Speech TV

Newsmax TV

Scripps News

CNN en Español

PBS

ABC News Live

Link TV

Lifetime

VH1

France 24

Univision

ION Television

NBC News

Investigation Discovery

MeTV

DD India

ESPNews

BBC America

CNBC Europe

C-SPAN

A & E Network

Hallmark Channel

DoD News Channel

National Geographic

TNT

euronews

Sky News

Bloomberg Television

New York Times.

Washington  Post.

CNN.

Fox News.

USA Today.

Los Angeles Times.

Chicago Tribune.

Boston Globe.

Minnesota Star Tribune

New York Post

Newsday

San Fransisco Chronicle

The Dallas Morning News

Tampa Bay Times

Hartford Courant

Publick Occurrences Both Forreign and Domestick

The Michigan Daily

The Denver Post

Pittsburgh Post-Gazette

The Seattle Times

Las Vegas Sun

Bourbon County Citizen

The Register Star

NewYork Metro

The Queens Ledger

Philadelphia Tribune

Baltimore Afro-American

Portland Tribune

Indianapolis Recorder

The Patriot-News

El Diario NY

The Modesto Bee

Fairfax County Times

The Epoch Times

Barron's

Queens Chronicle

Phoenix New Times

El Informador

The Philadelphia Inquirer

New York Daily News

The Star-Ledger

St. Louis Post-Dispatch

The Mercury News

The Arizona Republic

The Plain Dealer

Detroit Free Press

The Press-Enterprise

The Tennessean

Sun Sentinel

The Copenhagen Post

The Slovak Spectator

The Budapest Times

Tirana Times

Menorca Sun

The Vienna Review

Le News

The Irish Times

Die Welt

Het Nieuwsblad

Le Soir

Albania Today

Algemeen Dagblad

De Telegraaf

de Volkskrant

The European

Het Laatste Nieuws

The Daily Telegraph

Daily Mirror

The Sun

Pravda

The Moscow Times

The Guardian

Le Figaro

Le Monde

ABC

la Repubblica

Il Messaggero

El Periódico de Catalunya

El Mundo

Libération

El País

Kronen Zeitung

La Stampa

Frankfurter Allgemeine Zeitung

Bild

20 minutes

Sport

Aftenposten

Marca

Gazeta Wyborcza

Izvestia

Die Presse

Süddeutsche Zeitung

La Tribune

Novaya Gazeta

Neue Zürcher Zeitung

Dagens Nyheter

Expressen

La Gazzetta dello Sport

Mladá fronta Dnes

Urdu News

Daily Pakistan

Dawn

Daily Express

Daily Jang

The Express Tribune

The News International

The Nation

Pakistan Today

Daily Dunya

Daily Ummat

Nawaiwaqt

The Regional Times of Sindh

Pakistan Observer

Khabrain

Daily Ausaf

Daily Jasarat

Daily Nai Baat

Daily Basharat

Daily Times

The Frontier Post

Daily Sarhad

Daily Imroze

The Pakistan Times

The Financial Daily

Daily Aaj

Daily Mashriq

Millat

Business Recorder

Daily Inqilab

Kawish

Daily Lokaai

Talár

Maidan Daily

Daily Asas

Christian Voice

The Friday Times

Awam

Daily Awami Awaz

The Star

Al Akhbar

Khyber Mail

Nawai Watan

Sajjan

Daily Hilal Pakistan

Daily Sindhu

Daily Koshish

Daily Mehran

Bhulekha

Civil and Military Gazette

---

### #2545 — Amin (Topic Author)
*December 2, 2024, 7:27 AM*

Friends, I am copying a few key posts from the past especially for journalists in American, European and Pakistani News
and other Media companies so that they can easily get oriented with the brief details of my mind control. When you
approach journalists and others in News Media, please refer them to following posts first so they can know all the
context of my increasing persecution. Again, I simply want to request and convince people to make efforts to end
extrajudicial, inhuman and cruel mind control by American defense on behest of a jewish billionaire and his cohort of
rich jews. I am sure that bad actors behind mind control  are not ready to dismantle all mind control infrastructure in
Urban United States and in other countries and do not want to stop systematically drugging food of victims, and
therefore we want to approach News media to publish investigative News articles so check and balance on extrajudicial
and illegal powers of armies in our countries could be restored again and armies are made to abide by the laws and
constitution of our countries. Please join me in efforts to stop more people from getting retarded by bad actors in our
societies and towards ending illegal and extrajudicial mind control on tens of thousands of innocent human beings by
American defense. Let us put an end to inhuman cruelties of corrupt people in our armies forever. Bad actors behind mind
control are getting more emboldened with every passing year since there is absolutely no resistance in our societies to
this extrajudicial and criminal activity and soon people who always considered them safe would also be on line. Please
do the right thing today to end this evil and menace and leave the legacy of a better society for our children where
nobody could ever be wronged by illegal and extrajudicial tactics of corrupt armies.

Here is a recent post I made a few days ago (I will copy more posts for context of people who recently joined after
this):

%Post Starts%

What I am writing is my honest opinion even though a lot of friends might differ with it to some degree. I think it is
very important that all of us try to have rule of law, and good governance for the benefit of our country and society.
We promote freedom of speech and freedom of press in our societies so that people can criticize bad or wrong actions of
other people and make each other aware of their observations of wrongdoings by some people especially the ones in the
authority in the society while, obviously, every body has to try to investigate the truth on their own without blindly
believing anyone. The purpose of such criticism and related discussions is to try to root out bad practices from the
society and promote good ethics and practices.

Another thing I want to suggest is that true patriotism is not about hiding bad practices taking place in our country
from others, instead it is about exposing such bad practices by unethical people in the public with the final goal that
these bad practices are rooted out from our societies.

Now I will come to the point that I have been suggesting for years that there is a jewish billionaire and his rich
cohort who are behind indiscriminate mind control of a large number of intelligent American people and others . And a
large number of people in American defense have become a mercenerary army that play in the hands of these rich jews.
These rich jews hire quite a few of senior officers from Pentagon and army after their retirement in their large
enterprises and these people are paid millions of dollars each and they enjoy very high social status. One of the most
important purpose of these retired officers is to convince their juniors who are still in official service and have
reached positions of authority to do illegal, extrajudicial and extraconstitutional mind control control of Americans
and others suggested by the rich jewish cohort. This thing is so well known in some jewish circles that many jews
continuously report thousands of people among intelligent students and many others who fall out with these jews for any
reason to mind control by American defense. You do not always have to be extra intelligent, sometimes falling out with a
jew who knows how to approach the rich jewish cohort will seal the fate of the victim by mind control forever. As
always, I would like to mention that there are large number of jews who are opposed to this practice and have absolutely
nothing to do with mind control of innocent people. Please let me specifically say again that there are many very rich
jews and billionaires who have nothing to do with mind control. But I definitely own that I am suggesting this rich
jewish billionaire and his cohort of rich jews are behind most of the mind control and this is a common knowledge in
many jewish circles and many people among these circles know who to approach for mind control of anyone they do not
like.

But what is even more alarming is that all the bad actors behind mind control including rich jewish cohort and mercenary
criminals in American defense, when exposed in public, have absolutely no remorse about their crimes and they become
even more adamant to use all machinatory tactics so that they+ can continue illegal and extrajudicial mind control of
innocent and intelligent people. They have lost all sense of good and evil and have no qualms about continuing the evil
practices at all. It seems many of these bad actors have no conception that retarding innocent human beings is a wrong
thing and an evil practice and they think that mind control of innocent people in the society they do not like is indeed
a good thing.

I know that many good Americans want to end the bad practice of mind control of innocent people from their society
without any retribution against the bad actors behind such evil practices. The bad actors, on the other hand, have
absolutely no remorse about their evil actions and are ready to go to any limit to thwart the attempts of good people to
end mind control and they always try to undermine all good people and their actions towards amicably ending the evil of
mind control from American society. These bad actors are not willing to gracefully acknowledge and be thankful that good
American people do not want to hurt them beyond ending the inhuman practice of mind control from American society and
instead these bad actors are adamantly using all sort of machinatory and bellicose tactics so they can continue and
increase the evil of inhuman mind control of intelligent and innocent human beings.

I really want to suggest if all amicable attempts by good Americans to end mind control fail, it does not mean that they
have to yield to inhuman practices in our society by continuing to play nice. As there is very huge evidence about
existence of extra-judicial, extra-constitutional and cruel mind control and resulting retarding of very large number of
innocent people by American defense and a large number of stories are circulating in academia about people who were
targeted by American defense on behest of jewish cohort, I really believe that it is a great opportunity for some good
journalists in American and international media to write in detail about the hugely widespread evil of extrajudicial,
extraconstitutional, inhuman and cruel practice of mind control and also about nexus between some bad jews and corrupt
people in American defense that has been the dominating force behind this inhuman evil in our societies. I want to
request good American people that if all else fails, please motivate some brave and patriotic journalists to write in
complete detail about the evil of mind control. If it is not possible to write about this inhuman practice in American
newspapers due to possible reprisal from american defense, please break the news in some large British or European
newspaper. I am sure there is enough evidence about existence of mind control and related inhuman and cruel practices
that any serious journalist can firmly stand behind a well written article that completely exposes mind control and
associated cruelties and retarding of thousands of innocent persons by corrupt people in American defense. As I earlier
suggested Patriotism does not consist in saving any false pride or hiding evil practices of our countrymen, it consists
in rationally doing what is broader good for people in our societies by trying to put an end to evil practices.

I will also request readers, for good of our societies, to let at least one journalist you know in the following
American, European and Pakistani newspapers about true nature of mind control and about my thread.

%Post Ends%

There is another recent post.

%Post Starts%

I want to congratulate Americans on choosing former president Donald Trump as their president again. Even though many of
us are worried about climate change, we have to completely amicably accept the decision of broader American people since
that is how democracies are supposed to work. Even though many of us might differ with conservatives on many issues,
most of them are very patriotic people (sometimes even more so than democrats) and good human beings. Again one thing is
sure that for good of American people and for good of rest of the world, all of us would have to work with new president
and his administration.

For two decades, I have been writing against mind control of tens of thousands of totally innocent people and I hope
that new president Donald Trump would end this evil practice from United States and from rest of the world forever. I
want to firmly tell people that even though I have repeatedly alleged connivance between American defense and a rich
Jewish billionaire and his rich cohort to perpetrate mind control of innocent people, I have nothing against good jews.
Just like anybody else, I want them to work hard and become successful or billionaires or anything beyond that by doing
the right and good things in this world. And there are some jewish billionaires who are embodiment of that and I totally
respect them. And I want people to completely respect all good jews who are good human beings regardless of their wealth
or status. My fight is not with jews but against cruel practice of mind control of ordinary innocent civilians. I do own
that I have been attacking a billionaire jewish billionaire and his rich jewish cohort but it is solely due to their
exceptional cruelty of starting mind control of tens of thousands of innocent people and I must not remain silent about
it. My criticism would have been exactly the same if it were some other group or cohort of people associated with any
other religion or ideology. I must say again that I might not have been careful everywhere to point out and there have
been times when I might have unduly criticized Jews due to emotions and agony related to my helplessness, misery, and
suffering but again and again, repeatedly, I have almost always continued to stress that I have absolutely nothing
against jews who are good human beings and I want them to be as successful as they can and I wish well for them and want
everyone to give great respect to good jews who wish well for others (including non-jews) in the society and hold no
baseless prejudices.

And I have always criticized American defense as being a corrupt puppet of rich jewish cohort when it comes to mind
control. I want to step back here and tell good American people that even more than American defense I criticize corrupt
Army of my country that takes a sacred oath to protect the constitution and not meddle in politics but all of them
without exception break this oath and continue to interfere in politics and make puppets out of politicians and dictate
decisions to higher courts of law. The generals of the very same Pak army are the ones who manage mind control of
innocent and intelligent Pakistani citizens on behest of CIA since they are given hundreds of millions of dollars in
return by CIA every year. Our army is a very corrupt and unprofessional army. The case of American army is quite similar
but not in every domain. It is that in every country with big army, there are unseen (and unwritten) political, cultural
and other barriers (that exist in the mind of people) and corrupt armies usually do not dare to cross these barriers.
For example, in our country with very little unwritten barriers, our army does almost everything wrong and illegal but
still does not completely occupy the government due to possible backlash from people. These unwritten barriers are very
different in our backward country that has remained under army dictatorship for most of the time and in united states
where people have maintained a strong democracy and political rule for most oft the time. As an example, US defense
retards thousands of Americans every year with mind control most of them on insistence of rich jewish cohort and have
cumulatively retarded several hundred thousands of intelligent people all across the world with a very high percentage
of them in America. This has absolutely no constitutional basis and even president of United states cannot suggest to
american defense  to retard anyone. Just a few days ago before the American elections, on linkedin, I saw one of the top
American generals boasting that they were supposed to follow their oath to protect the constitution and not to any
single human being. This boasting is no different than the similar boasting by Pakistan army generals. American army
equally breaks the constitution but in different domain. American army has illegally installed thorough infrastructure
for total mind control of any arbitrary individual by EM waves all over urban United States even though mind control is
a cruel and illegal practice that American constitution does not allow at all. So much so for the grand boastings of
allegiance to constitution by American army generals.

So I say again that I have been vocally criticizing Bad Jews and American defense but please do respect every
professional person in your army and every good jew in your social circle. My criticism is aimed at cruel, inhuman,
illegal and extra-constitutional practices and bad actors behind those practices, and it is not against any religion or
general group of people.

Coming to the point, I want to tell friends that bad actors who are behind cruel mind control will start machinating to
find people in close circle of newly elected president to make sure and lobby for illegal mind control to continue. This
is what happens when a new president is chosen. I really want to request all good people to please do the exact opposite
and try to find genuinely patriotic people in trump's close circle and explain to them how some rich jews are forcing
mind control on good people right and left and convince them to strongly lobby to end mind control forever. Please
approach respectable, towering and patriotic conservative Americans in academia to suggest to new president trump to end
the cruel menace of mind control forever.

Here I would like to tell people that mind control damaged my country and set us back by more than a decade. We were
always a poor country so it was probably not a big deal. There were several hundred or possibly a thousand intelligent
people who were retarded by connivance of CIA and pak army on insistence of bad jews. On the other hand tens of
thousands of intelligent people were retarded in United States and I make this claim that US was set back by at least
five years but nobody could tell as US was even otherwise a very prosperous and rich country. On the other hand, there
is no mind control in countries like China where every intelligent person works totally unfettered. What I mean to say
that these American generals who are boasting their allegiance to constitution are biting the very hand that feeds them.
If US want to compete with China, power and potential of intelligent people has to be unleashed and not controlled by
mind control of tens of thousands of innocent people that has already damaged the country by costing it the progress of
at least five years.

%Post Ends%

MSNBC

NBC

CNN

Fox Business

Fox News

American Broadcasting Company

USA Network

CBS

CNBC

Fox

HLN

Blaze Media

Al Jazeera America

Discovery Channel

RT

HBO

NewsNation

MyNetworkTV

Free Speech TV

Newsmax TV

Scripps News

CNN en Español

PBS

ABC News Live

Link TV

Lifetime

VH1

France 24

Univision

ION Television

NBC News

Investigation Discovery

MeTV

DD India

ESPNews

BBC America

CNBC Europe

C-SPAN

A & E Network

Hallmark Channel

DoD News Channel

National Geographic

TNT

euronews

Sky News

Bloomberg Television

New York Times.

Washington  Post.

CNN.

Fox News.

USA Today.

Los Angeles Times.

Chicago Tribune.

Boston Globe.

Minnesota Star Tribune

New York Post

Newsday

San Fransisco Chronicle

The Dallas Morning News

Tampa Bay Times

Hartford Courant

Publick Occurrences Both Forreign and Domestick

The Michigan Daily

The Denver Post

Pittsburgh Post-Gazette

The Seattle Times

Las Vegas Sun

Bourbon County Citizen

The Register Star

NewYork Metro

The Queens Ledger

Philadelphia Tribune

Baltimore Afro-American

Portland Tribune

Indianapolis Recorder

The Patriot-News

El Diario NY

The Modesto Bee

Fairfax County Times

The Epoch Times

Barron's

Queens Chronicle

Phoenix New Times

El Informador

The Philadelphia Inquirer

New York Daily News

The Star-Ledger

St. Louis Post-Dispatch

The Mercury News

The Arizona Republic

The Plain Dealer

Detroit Free Press

The Press-Enterprise

The Tennessean

Sun Sentinel

The Copenhagen Post

The Slovak Spectator

The Budapest Times

Tirana Times

Menorca Sun

The Vienna Review

Le News

The Irish Times

Die Welt

Het Nieuwsblad

Le Soir

Albania Today

Algemeen Dagblad

De Telegraaf

de Volkskrant

The European

Het Laatste Nieuws

The Daily Telegraph

Daily Mirror

The Sun

Pravda

The Moscow Times

The Guardian

Le Figaro

Le Monde

ABC

la Repubblica

Il Messaggero

El Periódico de Catalunya

El Mundo

Libération

El País

Kronen Zeitung

La Stampa

Frankfurter Allgemeine Zeitung

Bild

20 minutes

Sport

Aftenposten

Marca

Gazeta Wyborcza

Izvestia

Die Presse

Süddeutsche Zeitung

La Tribune

Novaya Gazeta

Neue Zürcher Zeitung

Dagens Nyheter

Expressen

La Gazzetta dello Sport

Mladá fronta Dnes

Urdu News

Daily Pakistan

Dawn

Daily Express

Daily Jang

The Express Tribune

The News International

The Nation

Pakistan Today

Daily Dunya

Daily Ummat

Nawaiwaqt

The Regional Times of Sindh

Pakistan Observer

Khabrain

Daily Ausaf

Daily Jasarat

Daily Nai Baat

Daily Basharat

Daily Times

The Frontier Post

Daily Sarhad

Daily Imroze

The Pakistan Times

The Financial Daily

Daily Aaj

Daily Mashriq

Millat

Business Recorder

Daily Inqilab

Kawish

Daily Lokaai

Talár

Maidan Daily

Daily Asas

Christian Voice

The Friday Times

Awam

Daily Awami Awaz

The Star

Al Akhbar

Khyber Mail

Nawai Watan

Sajjan

Daily Hilal Pakistan

Daily Sindhu

Daily Koshish

Daily Mehran

Bhulekha

Civil and Military Gazette

---

### #2546 — Amin (Topic Author)
*December 2, 2024, 7:48 AM*

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

### #2547 — Amin (Topic Author)
*December 2, 2024, 7:51 AM*

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

### #2548 — Amin (Topic Author)
*December 2, 2024, 8:01 AM*

**(broken latex: Unbalanced $: 1)**

```latex
%Post Starts%

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

%Post Ends%

%Post Starts%

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

%Post Ends%

%Post Starts%

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

%Post Ends%

%Post Starts%

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

%Post Ends%

%Post Starts%

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

I also want to explain very clearly that I have been very severely criticizing bad jews and American defense but this is
limited to criticism in writing only. I do not want anyone including myself to take the law in our own hands. We have to
respect the human dignity of every jew and every human being including those involved in bad practices so even though I
openly talk about bad people, it is not an invitation to anyone to take the law in their hands or hurt any any human
being. I will continue to fight for my cause of ending mind control of innocent and intelligent people but I want people
to completely respect all good jews and good people in American army and make a political struggle for the law or
government actions to take their course against corrupt and evil people. I absolutely do not suggest any violence or
anybody taking law in their hands.

%Post Ends%

MSNBC

NBC

CNN

Fox Business

Fox News

American Broadcasting Company

USA Network

CBS

CNBC

Fox

HLN

Blaze Media

Al Jazeera America

Discovery Channel

RT

HBO

NewsNation

MyNetworkTV

Free Speech TV

Newsmax TV

Scripps News

CNN en Español

PBS

ABC News Live

Link TV

Lifetime

VH1

France 24

Univision

ION Television

NBC News

Investigation Discovery

MeTV

DD India

ESPNews

BBC America

CNBC Europe

C-SPAN

A & E Network

Hallmark Channel

DoD News Channel

National Geographic

TNT

euronews

Sky News

Bloomberg Television

New York Times.

Washington  Post.

CNN.

Fox News.

USA Today.

Los Angeles Times.

Chicago Tribune.

Boston Globe.

Minnesota Star Tribune

New York Post

Newsday

San Fransisco Chronicle

The Dallas Morning News

Tampa Bay Times

Hartford Courant

Publick Occurrences Both Forreign and Domestick

The Michigan Daily

The Denver Post

Pittsburgh Post-Gazette

The Seattle Times

Las Vegas Sun

Bourbon County Citizen

The Register Star

NewYork Metro

The Queens Ledger

Philadelphia Tribune

Baltimore Afro-American

Portland Tribune

Indianapolis Recorder

The Patriot-News

El Diario NY

The Modesto Bee

Fairfax County Times

The Epoch Times

Barron's

Queens Chronicle

Phoenix New Times

El Informador

The Philadelphia Inquirer

New York Daily News

The Star-Ledger

St. Louis Post-Dispatch

The Mercury News

The Arizona Republic

The Plain Dealer

Detroit Free Press

The Press-Enterprise

The Tennessean

Sun Sentinel

The Copenhagen Post

The Slovak Spectator

The Budapest Times

Tirana Times

Menorca Sun

The Vienna Review

Le News

The Irish Times

Die Welt

Het Nieuwsblad

Le Soir

Albania Today

Algemeen Dagblad

De Telegraaf

de Volkskrant

The European

Het Laatste Nieuws

The Daily Telegraph

Daily Mirror

The Sun

Pravda

The Moscow Times

The Guardian

Le Figaro

Le Monde

ABC

la Repubblica

Il Messaggero

El Periódico de Catalunya

El Mundo

Libération

El País

Kronen Zeitung

La Stampa

Frankfurter Allgemeine Zeitung

Bild

20 minutes

Sport

Aftenposten

Marca

Gazeta Wyborcza

Izvestia

Die Presse

Süddeutsche Zeitung

La Tribune

Novaya Gazeta

Neue Zürcher Zeitung

Dagens Nyheter

Expressen

La Gazzetta dello Sport

Mladá fronta Dnes

Urdu News

Daily Pakistan

Dawn

Daily Express

Daily Jang

The Express Tribune

The News International

The Nation

Pakistan Today

Daily Dunya

Daily Ummat

Nawaiwaqt

The Regional Times of Sindh

Pakistan Observer

Khabrain

Daily Ausaf

Daily Jasarat

Daily Nai Baat

Daily Basharat

Daily Times

The Frontier Post

Daily Sarhad

Daily Imroze

The Pakistan Times

The Financial Daily

Daily Aaj

Daily Mashriq

Millat

Business Recorder

Daily Inqilab

Kawish

Daily Lokaai

Talár

Maidan Daily

Daily Asas

Christian Voice

The Friday Times

Awam

Daily Awami Awaz

The Star

Al Akhbar

Khyber Mail

Nawai Watan

Sajjan

Daily Hilal Pakistan

Daily Sindhu

Daily Koshish

Daily Mehran

Bhulekha

Civil and Military Gazette
```

---

### #2549 — Amin (Topic Author)
*December 3, 2024, 9:08 AM*

Friends, I was able to start working somewhat last night and earlier today. I noticed that a direct regression from
uniformly sampled parameters of the SDEs on to their hermite coefficients polynomials loses some accuracy. So we would
have to sample from a distribution of SDE parameters that can easily be sampled and inverted by hermite polynomials. We
would also have to do analytics about what order of polynomial to use in hermite polynomial regression and also in
original parameter polynomials. I am trying to work on the issues and hope that I would have a better solution in about
a week/few days.

---

### #2550 — Amin (Topic Author)
*December 4, 2024, 12:59 PM*

Friends, I think it is necessary to first remove all those regressors (in the form of products) which make a miniscule
addition to R-Squared of the regressand variable from the regression. Once we keep them in our regression and then try
to convert their orthogonal polynomial equations into original polynomial form, and if the relationship is not captured
perfectly by original variable polynomials, they actually start to add to noise in the regression results.

I am trying to automate the process of choosing and decreasing regressors in the orthogonal polynomial regressions.

Once I complete this part possibly in a day, I will try to move towards the other part of specifying initial
distributions for parameters that would be used to sample the SDE simulations results. Again the problem would be
slightly easier if we wanted to use the parameters (over a range) as regressors and would be different from when we
would want to use Math based regressors in the orthogonal polynomial regressions.

---

[← Previous](page_050.md) | [Index](index.md) | [Next →](page_052.md)
