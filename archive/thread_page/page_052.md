# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 52 of 65** — Posts #2551–#2600

[← Previous](page_051.md) | [Index](index.md) | [Next →](page_053.md)

---

### #2551 — Amin (Topic Author)
*December 5, 2024, 9:25 AM*

**(broken latex: Unbalanced $: 3)**

```latex
Friends, this is preliminary version of automated program that computes the Hermite polynomial design matrix. I will
change this program further and this is rather preliminary only for friends who have been following my blog for sometime
now. I will come up with a final formal version soon.

I also believe that after converting the regression matrix from hermite polynomials to one with polynomials in original
variables, we might need further optimization in original variables that tries to find an optimum relationship in the
neighborhood of hermite implied relationship in original variables. We would want the optimization to increase R-squared
without increasing degrees of freedom in the original variables polynomial. I am sure this can be done with a bit of
effort. I mean neural networks are mostly all about optimization. We have a very good initial guess and many derivative
based methods might work since there may not be many local minima as we are already in close neighborhood of true
solution.

.

.

.

```
function [WH1] = CalculateHermiteDesignMatrixAutomated(Q,Yl,NN,OrderH)

%Q is a multidimensional array that is NN X 7 size. You can easily
%decrease or increase number of regressors from seven after understanding
%the code.
%Yl is NN sized array of regressand. One dimensional.
%OrderH is order of Hermite polynomials of every variable and is common.

%The first part of This function takes seven arrays/regressors input at joint data values in the same
%sequence. And returnd a Hermite polynomials design matrix with all Hermite polynomials
%evaluated at their data values and their possible product values.
%You can use it anywhere in other problems if there are seven regressors.

%Second loop in this function calculates the loss of R-Squared when a
%specific variable is removed from the least squares design matrix.

%Third loop removes all those variables that are smaller than a threshold
%value and

OrderH0=OrderH+1;

Ndata=NN;
Mtable=readtable('C:\Users\Lenovo\Documents\MATLAB\MATLAB1\MomentMatchParams08.txt');
[ZI] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable);
[W] = EvalHermiteArrayH0(ZI,OrderH);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%This part of program calculates Hermite design matrix

for n1=0:1
    for n2=0:1
        for n3=0:1
            for n4=0:1
                for n5=0:1
                    for n6=0:1
                        for n7=0:1
                            Bindex=[n1 n2 n3 n4 n5 n6 n7]
                            index = binaryVectorToDecimal(Bindex);
                            BBindex(index+1,:)=Bindex(:);
                            ParamsRegress(1:Ndata,index+1)=1;
                            for nn=1:7
                                if(Bindex(nn)==1)
                                    ParamsRegress(1:Ndata,index+1)=ParamsRegress(1:Ndata,index+1).*Q(1:Ndata,nn);
                                else
                                    ParamsRegress(1:Ndata,index+1)=ParamsRegress(1:Ndata,index+1).*1;
                                end
                            end

                            [Paramss,Ix]=sort(ParamsRegress(1:Ndata,index+1));
                            %Wx(Ix(1:Ndata))=W(1:Ndata,1:OrderH);
                            Wx(Ix(1:Ndata),:)=W(1:Ndata,:);

                            if(index==0)
                                WH(1:Ndata,1)=1;
                            elseif (index==1)
                                WH(1:Ndata,1+1:1+OrderH)=Wx(1:Ndata,2:OrderH0);
                            else
                                WH(1:Ndata,1+OrderH*(index-1)+1:1+OrderH*index)=Wx(1:Ndata,2:OrderH0);
                            end
                        end
                    end
                end
            end
        end
    end
end

Yl(1:Ndata,1)=Yl(1:Ndata);
CoeffH=(WH'*WH)$WH'*Yl);

bhs(1:NN,1)=0;
for rr=1:OrderH0+126*OrderH
    bhs(1:NN,1)=bhs(1:NN)+CoeffH(rr,1).*WH(1:NN,rr);
    %RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffL(rr,9).*WL(1:NN,rr);
end

RSquared0=1-sum((Yl(:,1)-bhs(:,1)).^2)/sum((Yl(:,1)-sum(Yl(:,1))/(NN)).^2);

str=input("Look at CoeffH");

%This part of program removes one variable at a time from Hermite design
%matrix and calculates its effect on total R-squared.

for n1=0:1
    for n2=0:1
        for n3=0:1
            for n4=0:1
                for n5=0:1
                    for n6=0:1
                        for n7=0:1
                            Bindex=[n1 n2 n3 n4 n5 n6 n7]
                            index = binaryVectorToDecimal(Bindex);
                            BBindex(index+1,:)=Bindex(:);

                            WH0(1:Ndata,1:1+OrderH*(index))=WH(1:Ndata,1:1+OrderH*(index));
                            WH0(1:Ndata,1+OrderH*(index)+1:1+OrderH*126)=WH(1:Ndata,1+OrderH*(index+1)+1:1+OrderH*127);

                            Yl(1:Ndata,1)=Yl(1:Ndata);
                            CoeffH0=(WH0'*WH0)$WH0'*Yl);

                            bhs(1:NN,1)=0;
                            for rr=1:OrderH0+125*OrderH
                                bhs(1:NN,1)=bhs(1:NN)+CoeffH0(rr,1).*WH0(1:NN,rr);

                            end

                            RSquared(index+1)=1-sum((Yl(:,1)-bhs(:,1)).^2)/sum((Yl(:,1)-sum(Yl(:,1))/(NN)).^2)

                            RSquared0

                            DiffRSquared=RSquared0-RSquared(index+1)

                       %     str=input("Look at change in R-squared")

                        end
                    end
                end
            end
        end
    end
end

%This part of the program removes those variables from hermite design matrix that
%make a smaller contribution to R-squared than a small threshold value.
%This threshold has to be different for every regressor.

RemoveCount=0;
ColCount=0;
WH1=0;
for n1=0:1
    for n2=0:1
        for n3=0:1
            for n4=0:1
                for n5=0:1
                    for n6=0:1
                        for n7=0:1
                            Bindex=[n1 n2 n3 n4 n5 n6 n7]
                            index = binaryVectorToDecimal(Bindex);
                            BBindex(index+1,:)=Bindex(:);

                            DiffRSquared=RSquared0-RSquared(index+1)

                            %if(DiffRSquared 0)
                               
WH1(1:Ndata,ColCount+1:ColCount+OrderH)=WH(1:Ndata,ColCount+RemoveCount+1:ColCount+RemoveCount+OrderH);

                                    ColCount=ColCount+OrderH;
                                else
                                    WH1(1:Ndata,1)=1;
                                    ColCount=ColCount+1;
                                end
                            end

                        end
                    end
                end
            end
        end
    end
end

Yl(1:Ndata,1)=Yl(1:Ndata);
CoeffH=(WH1'*WH1)$WH1'*Yl);

size(WH1)
RemoveCount
ColCount

str=input("Look at CoeffH---00000------");

bhs(1:NN,1)=0;
for rr=1:OrderH0+(126-RemoveCount)*OrderH
    bhs(1:NN,1)=bhs(1:NN)+CoeffH(rr,1).*WH1(1:NN,rr);
    %RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffL(rr,9).*WL(1:NN,rr);
end

RSquaredNew=1-sum((Yl(:,1)-bhs(:,1)).^2)/sum((Yl(:,1)-sum(Yl(:,1))/(NN)).^2)

str=input("Look at R-Squared after removal of variables");

end

```

```

---

### #2552 — Amin (Topic Author)
*December 5, 2024, 3:50 PM*

Friends, I was thinking about it and I realized that it should not be very difficult to write a derivatives based
optimization program that takes coefficients in original variable polynomial solution to hermite based regression as
starting input guess and optimizes these coefficients to get a better solution to regression equation in original
variable polynomials. I want to work on this program for next few days and hope to come back soon with a worked out
matlab program. I am trying to use multidimensional Newton search with more equations than variables that takes
generalized inverse of jacobian and gives a solution in least squared sense. Since original guess is very close to
optimal solution, I hope that Newton method will almost always converge. I will start working on the program later today
and hope it goes well.

---

### #2553 — Amin (Topic Author)
*December 7, 2024, 6:19 AM*

Friends, I am making slow but steady progress. I have a very good idea how to implement Newton  method (for more
equations than variables) and it is very simple for me to implement it as I have worked with similar concepts quite a
bit but I want to first get more oriented with the conversion from hermite polynomials into original coordinates for a
day or two. I do hope that soon we would have a good working program that will be a nice implementation of Math AI.

I  have continued my work but I have not been able to work at full speed since mind control agents stubbornly try to
stop me in every way they can and they use all their tactics for that. I really wish I could work like I did last
winters.

I want all those people who are opposed to let me do my research, to please make money out of any interesting
mathematics I am able to do and I would simply love that. But please do not retard intelligent and innocent people. We
have to be able to see  things as plain humans and not as Muslims, jews or hindus etc.

---

### #2554 — Amin (Topic Author)
*December 8, 2024, 7:43 PM*

Friends, I was able to convert the regression coefficients from hermite polynomials to original variables with R-Squared
equal to or exceeding the R-Squared in the hermite polynomial variables.

But then I noticed something far more interesting. We could regress the hermite coefficients of SDE densities directly
in parameters of the SDEs with exactly the same accurcay without having to map them on normal density and converting
them into hermite polynomial series. All we need is to expand the SDE density hermite coefficients directly in terms of
a sum of various power series in parameters and products of parameters directly around the median of each series
variable (that is each variable of the power series is a parameter of the density or products of parameters). The only
thing probably needed was that each of the variable in the component power series had to be expanded around its median
in all the individual power series. This is even more remarkable and makes everything very simple. However there were
potential problems with matrix inversions in original variables that were not there when we mapped the regression
variables on normal density and then regressed.

Here is a graph from mean of the SDE density directly from a regression on original variables with the same sample we
used earlier. It had an R-Squared of .999997. Here green (true) and red (our density from original variable regression)
lines were overlaid and you cannot see any red at all because of high precision.( I inverted the order or variables in
graph and then I could not see any green at all).

.

.

[![Image](../images/i.postimg.cc/HL2cn1m9/SDEMeans.png)](https://postimg.cc/nsXcS5CX)

Here is a graph for coefficient of first hermite polynomial of density of SDEs. It had an R-Squared of .99964. This is
not so perfectly precise as the R-Squared for the previous graph so you can see a little bit of red at the end of green
lines as overlaid lines differ in length with very small amount.

.

.

[![Image](../images/i.postimg.cc/xCpXGGck/SDE1-Coeffs.png)](https://postimg.cc/R6fC4H19)

.

This was very interesting that we could do regression in original variables without mapping them on normal density and
only after expanding them around median of each series. But One concern was that matrix inversion in original variables
was being very badly scaled. Hermite polynomial formulation is also special because it gives us standardized
correlations between various hermite polynomial components.

I will be posting my matlab programs for above experiments on Tuesday after making some explanations and comments.

---

### #2555 — Amin (Topic Author)
*December 9, 2024, 7:27 PM*

Friends, I have generated a few graphs of comparison between true Hermite representation of SDE density and SDE density
whose hermite coefficients were generated from regression using original variables/parameters (as opposed to hermite or
Legendre based regression). There were 127 combinations of seven original variables and we used a series with sixth
power for each variable in regression given as

$
$\,Y\,=\, a_0\,+\, \sum\limits_{m=1}^{127} \, \,\sum\limits_{l=1}^{6} \, a_{m,l} \, \left( \, X_m \,-\, \tilde{X}_{m} \right)^l \, $
$

where the variable with tilde over it $  \tilde{X}_{m} $ represents the median value

If you know form of your series expansion in an analytical problem, you can apply least squared regression to determine
its coefficients with great success. We have just used a generic form without any implied knowledge about the true
expansion.

This series was simply estimated with least squares. I did not remove any of the 127 possible regressors but they could
further be reduced to at least half their number without any significant effect on quality of regression. Total SDE
sample used for regression had 5000 SDEs in it. We just discretized a common terminal point T for all SDEs.

Here are the R-Squared values of nine variables involved in regressions. Please note that there is enough noise in
higher hermite coefficients input to the regression which shows up in low R-Squared of higher coefficients.

Look if there is matlab warning about ill conditioned matrix inversion

ans =

   0.999996768152800

ans =

   0.999595439533725

ans =

   0.999980360201532

ans =

   0.999804857642584

ans =

   0.996725089920776

ans =

   0.968681063339042

ans =

   0.890896765753010

ans =

   0.891569316281212

ans =

   0.999991060553739

Look at R^2s of eight standardized hermite series coefficients and ninth square root of variance

Below are the R-Squared values after the analytical constraint to retrieve unity variance( since we standardized the
densities) was applied. This is not related to regression but analytical improvement.

ans =

   0.999996768152800

ans =

   0.999948373145119

ans =

   0.999983362016971

ans =

   0.999785055350579

ans =

   0.996627566173230

ans =

   0.968450176761586

ans =

   0.890660853777217

ans =

   0.891093997723054

ans =

   0.999991060553739

Look at R^2s of first eight standardized hermite series coefficients

Here are overlaid graphs that show how first twenty five SDE densities from regression (in red) match with the original
discretization of the SDE densities (shown in green).

.

.

[![Image](../images/i.postimg.cc/XJ9DyRd2/SDEOrig01.png)](https://postimg.cc/7GYNFQB7)

[![Image](../images/i.postimg.cc/g0CTjzXX/SDEOrig02.png)](https://postimg.cc/ns1kwt1p)

[![Image](../images/i.postimg.cc/VNrhzr6P/SDEOrig03.png)](https://postimg.cc/Tyx09Pgt)

[![Image](../images/i.postimg.cc/GmSN0Jbj/SDEOrig04.png)](https://postimg.cc/MnVtVBMc)

[![Image](../images/i.postimg.cc/K8YVsshz/SDEOrig05.png)](https://postimg.cc/N5WpKDMq)

[![Image](../images/i.postimg.cc/dt6p6cXp/SDEOrig06.png)](https://postimg.cc/56Hs9TfS)

[![Image](../images/i.postimg.cc/tCp8F4rF/SDEOrig07.png)](https://postimg.cc/6TbHXtxQ)

[![Image](../images/i.postimg.cc/h49HJd0S/SDEOrig08.png)](https://postimg.cc/hhtC6hww)

[![Image](../images/i.postimg.cc/0jd3hTN6/SDEOrig09.png)](https://postimg.cc/bSr3tFk8)

[![Image](../images/i.postimg.cc/kGdz1J73/SDEOrig10.png)](https://postimg.cc/FdDT1QfD)

[![Image](../images/i.postimg.cc/ZRNXxBtx/SDEOrig11.png)](https://postimg.cc/2bzHz551)

[![Image](../images/i.postimg.cc/bvs7dVmM/SDEOrig12.png)](https://postimg.cc/8FgK04QB)

[![Image](../images/i.postimg.cc/43qrcvM3/SDEOrig13.png)](https://postimg.cc/v17qFnGR)

[![Image](../images/i.postimg.cc/kg1rJPvK/SDEOrig14.png)](https://postimg.cc/cvnkhjjL)

[![Image](../images/i.postimg.cc/t4CQG4W9/SDEOrig15.png)](https://postimg.cc/tYfmhyBc)

[![Image](../images/i.postimg.cc/wTzYFVBy/SDEOrig16.png)](https://postimg.cc/F1T6H03N)

[![Image](../images/i.postimg.cc/9FB5k74x/SDEOrig17.png)](https://postimg.cc/9rznRzYT)

[![Image](../images/i.postimg.cc/2jhf4JCN/SDEOrig18.png)](https://postimg.cc/nMF5x3s3)

[![Image](../images/i.postimg.cc/GtFwdBXm/SDEOrig19.png)](https://postimg.cc/hQt30GFk)

[![Image](../images/i.postimg.cc/rsXXBGCH/SDEOrig20.png)](https://postimg.cc/BLgVDKz5)

[![Image](../images/i.postimg.cc/KzghppLL/SDEOrig21.png)](https://postimg.cc/WFjyhn5b)

[![Image](../images/i.postimg.cc/PqJjY55S/SDEOrig22.png)](https://postimg.cc/DS9HKFsG)

[![Image](../images/i.postimg.cc/g2NpxZmw/SDEOrig23.png)](https://postimg.cc/3k4V6Wy7)

[![Image](../images/i.postimg.cc/JhFWqCyM/SDEOrig24.png)](https://postimg.cc/TynSdSq4)

[![Image](../images/i.postimg.cc/dVqvQBPP/SDEOrig25.png)](https://postimg.cc/4mFjBpxB)

---

### #2556 — Amin (Topic Author)
*December 9, 2024, 7:51 PM*

**(broken latex: Unbalanced $: 1)**

```latex
Friends, here is the program used for making the graphs and other calculations given in previous post. For functions
previously posted that I have not given here,  please check recent earlier posts in past few weeks.

.

.

.

```
function [] = SDEsWithMathAIMain08E8Standard()

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
MM=5;    %No of Batches of simulation
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
%if(nn>4*NN0) %This commented if would have to be used to specify that only
%parameters with index nn greater than 1000 would be simulated etc.
 [coeff] =
MeanRevertingMonteCarloDensity04New(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,Sfrequency);
 %[coeff,coeff2] =
MeanRevertingMonteCarloDensity04(y0U(nn),kappaU(nn),thetaU(nn),sigmaU(nn),gammaU(nn),SDEpaths,W,Order,Random0,dtM,TtM,W2);
 Coeff(1:Order+1,1:TtM/Sfrequency,nn)=coeff(1:Order+1,1:TtM/Sfrequency);
%end

end

%save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC16.mat","Coeff")
%str=input("I have saved the densities coefficients variable--Stop");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%You can comment the SDE simulations loop and continue to load the
%SDE coefficients all slices data from disk again and again and analyze
%program behavior at different time slices.

%Below is my code since I was making monte carlo simulations in batches of 1000 and
%saved each batch in a different file on disk.
% % %
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
%
%  load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\Coeffsfile04HG08BBC16.mat","Coeff")
%  str=input("I have loaded the densities coefficients variable");
%
%  Coeff5=Coeff;
%
%
%  Coeff(1:Order+1,1:TtM/Sfrequency,1:1000)=Coeff0(1:Order+1,1:TtM/Sfrequency,1:1000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,1001:2000)=Coeff2(1:Order+1,1:TtM/Sfrequency,1001:2000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,2001:3000)=Coeff3(1:Order+1,1:TtM/Sfrequency,2001:3000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,3001:4000)=Coeff4(1:Order+1,1:TtM/Sfrequency,3001:4000);
%  Coeff(1:Order+1,1:TtM/Sfrequency,4001:5000)=Coeff5(1:Order+1,1:TtM/Sfrequency,4001:5000);
%

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

for nn=1:NN

C(nn)=2*kappaU(nn)./(1-exp(-kappaU(nn)*TT))./sigmaU(nn).^2;
YT(nn)=thetaU(nn)+exp(-kappaU(nn)*TT)*(y0U(nn)-thetaU(nn));
Y0T(nn)=y0U(nn).*exp(-kappaU(nn)*TT);
UU(nn)=C(nn).*Y0T(nn);
VV(nn)=C(nn).*YT(nn);
UV(nn)=UU(nn).*VV(nn);
qq(nn)=2*(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
BB(nn)=besseli(qq(nn),sqrt(UV(nn)));

Q(nn,1)=C(nn).*YT(nn);
Q(nn,2)=(kappaU(nn).*thetaU(nn)./sigmaU(nn).^2);
Q(nn,3)=C(nn).*Y0T(nn);
Q(nn,4)=gammaU(nn);
Q(nn,5)=sigmaU(nn).^2;
Q(nn,6)=thetaU(nn);

end

[Q(:,7)] = CalculateApproximateVarianceOfMRSDEs(kappaU,thetaU,y0U,gammaU,sigmaU,NN,Ts,Sfrequency,dt);

%The above is approximate variance of the SDE and its value for each of the
%NN parameters scenarios is used as seventh regressor in Legendre
%polynomial regression. This variable is time dependent and has to be
%recalculated for each time slice.

Q(:,1)=Q(:,1)./max(Q(:,1));
Q(:,2)=Q(:,2)./max(Q(:,2));
Q(:,3)=Q(:,3)./max(Q(:,3));
Q(:,4)=Q(:,4)./max(Q(:,4));
Q(:,5)=Q(:,5)./max(Q(:,5));
Q(:,6)=Q(:,6)./max(Q(:,6));
Q(:,7)=Q(:,7)./max(Q(:,7));

%Above the regression variables are ad-hoc normalized. It does not make any
%difference since regression would pick up any normalization scaling.

OrderOrig=6;
OrderOrig0=OrderOrig+1;
for qq=1:8
    Yl(1:NN,qq)=SHCoeff(1:NN,qq); %First eight standardized hermite coefficients to be predicted.
end
Yl(1:NN,9)=VarSqRt(1:NN,1);%Square root of variance used to standardize has to be predicted as well.

%The function below returns the design matrix in original variable. This
%consists of powers of distance from the median of the variable.
[WOrig] = CalculateOrigVariableDesignMatrixAutomated(Q,NN,OrderOrig);

CoeffOrig=(WOrig'*WOrig)$WOrig'*Yl);%Original Variable polynomial coefficients
%to predict seven variables. six standardized coefficients
%and one square root of variance of each SDE.

str=input("Look if there is matlab warning about ill conditioned matrix inversion");

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

SHCoeff(1:NN,1:8)=Yl(1:NN,1:8);

%bhs: Regressed value of standardized hermite coefficients produced from Legendre Regression %
bhs(1:NN,1:8)=0;   %
%RegressedVarSqRt: Regressed value of square root of volatility produced from Legendre Regression
RegressedVarSqRt(1:NN,1)=0;

%Below calculate SDE hermite coefficients by regressing on original variable polynomials
% with all calculated coefficients and polynomials evaluated at
% input data values used to find regression coefficients. This is in-sample
% testing only.

for rr=1:OrderOrig0+126*OrderOrig
    bhs(1:NN,1:8)=bhs(1:NN,1:8)+CoeffOrig(rr,1:8).*WOrig(1:NN,rr);
    RegressedVarSqRt(1:NN,1)=RegressedVarSqRt(1:NN,1)+CoeffOrig(rr,9).*WOrig(1:NN,rr);
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
function [WOriginal] = CalculateOrigVariableDesignMatrixAutomated(Q,NN,OrderOrig)

%Q is a multidimensional array that is NN X 7 size. You can easily
%decrease or increase number of regressors from seven after understanding
%the code.
%Yl is NN sized array of regressand. One dimensional.
%OrderH is order of Hermite polynomials of every variable and is common.

%The first part of This function takes seven arrays/regressors input at joint data values in the same
%sequence. And returnd a Hermite polynomials design matrix with all original variable polynomials
%evaluated at their data values and their possible product values.
%You can use it anywhere in other problems if there are seven regressors.

OrderOrig0=OrderOrig+1;
Ndata=NN;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%This part of program calculates Hermite design matrix

for n1=0:1
    for n2=0:1
        for n3=0:1
            for n4=0:1
                for n5=0:1
                    for n6=0:1
                        for n7=0:1
                            Bindex=[n1 n2 n3 n4 n5 n6 n7]
                            index = binaryVectorToDecimal(Bindex);
                            BBindex(index+1,:)=Bindex(:);
                            ParamsRegress(1:Ndata,index+1)=1;

                            %Calculate desired product
                            for nn=1:7
                                if(Bindex(nn)==1)
                                    ParamsRegress(1:Ndata,index+1)=ParamsRegress(1:Ndata,index+1).*Q(1:Ndata,nn);
                                else
                                    ParamsRegress(1:Ndata,index+1)=ParamsRegress(1:Ndata,index+1).*1;
                                end
                            end

                            %Calculate MEdian
                            if(rem(Ndata,2)==0)
                                Y0=(ParamsRegress(Ndata/2,index+1)+ParamsRegress(Ndata/2+1,index+1))/2;
                            end
                            if(rem(Ndata,2)==1)
                                Y0=ParamsRegress(ceil(Ndata/2),index+1);%+Ys(Ndata/2+1))/2;
                            end

                            %Calculate expansion basis for each
                            %product variable
                            for mm=1:OrderOrig0
                                WOrig(1:Ndata,mm)=(ParamsRegress(1:Ndata,index+1)-Y0).^(mm-1);
                            end

                           %Arrange all above products in a single least squares design matrix
                           if(index==0)
                               % WH(1:Ndata,1)=1;
                                WOriginal(1:Ndata,1)=1;
                            elseif (index==1)
                               % WH(1:Ndata,1+1:1+OrderH)=Wx(1:Ndata,2:OrderH0);
                                WOriginal(1:Ndata,1+1:1+OrderOrig)=WOrig(1:Ndata,2:OrderOrig0);
                            else
                               % WH(1:Ndata,1+OrderH*(index-1)+1:1+OrderH*index)=Wx(1:Ndata,2:OrderH0);
                               
WOriginal(1:Ndata,1+OrderOrig*(index-1)+1:1+OrderOrig*index)=WOrig(1:Ndata,2:OrderOrig0);

                            end

                        end
                    end
                end
            end
        end
    end
end

end

```

```

---

### #2557 — Amin (Topic Author)
*December 10, 2024, 6:01 AM*

Exploring Math AI: Choice of Explanatory Regressors In a Least Square Regression

Let us look more closely at the regression equation from previous post.

There were 127 combinations of seven original variables and we used a series with sixth power for each variable in
regression given as

$
$\,Y\,=\, a_0\,+\, \sum\limits_{m=1}^{127} \, \,\sum\limits_{l=1}^{6} \, a_{m,l} \, \left( \, X_m \,-\, \tilde{X}_{m} \right)^l \, $
$

where the variable with tilde over it $  \tilde{X}_{m} $ represents the median value.

It is obvious that we could have used mean instead of median, or merely zero origin instead of median to get the same
results. This is just like a classic regression, then why does it work so well even in original variables ?

The answer lies in choice of variables that we have selected for regression and they are very different from what we
used to choose in classic regression models.

In order to get a proper intuition, we would have to go back to Hermite polynomial series regression again.

Suppose we want to regress a random variable V on strictly positive random variables X, Y and their products. We would
have to make hermite/Legendre series of all of the above variables as

$$\, X(Z_X)\,=\, ah_0 \, + \, ah_1 \, H_1(Z_X) \,+ \, ah_2 \, H_2(Z_X) \,+ \ldots \,+ \, ah_N \, H_N(Z_X) \, $$

$$\, Y(Z_Y)\,=\, bh_0 \, + \, bh_1 \, H_1(Z_Y) \,+ \, bh_2 \, H_2(Z_Y) \,+ \ldots \,+ \, bh_N \, H_N(Z_Y) \, $$

Hermite Series of Various products would be given as

$
$\, XY(Z_{XY})\,=\, ch_0 \, + \, ch_1 \, H_1(Z_{XY}) \,+ \, ch_2 \, H_2(Z_{XY}) \,+ \ldots \,+ \, ch_N \, H_N(Z_{XY}) \, $
$

$
$\, X^2Y(Z_{X^2Y})\,=\, dh_0 \, + \, dh_1 \, H_1(Z_{X^2Y}) \,+ \, dh_2 \, H_2(Z_{X^2Y}) \,+ \ldots \,+ \, dh_N \, H_N(Z_{X^2Y}) \, $
$

$
$\, XY^2(Z_{XY^2})\,=\, eh_0 \, + \, eh_1 \, H_1(Z_{XY^2}) \,+ \, eh_2 \, H_2(Z_{XY^2}) \,+ \ldots \,+ \, eh_N \, H_N(Z_{XY^2}) \, $
$

It is easy to see when X and Y random variables are strictly positive and are uncorrelated/independent,
then Z_{XY}, Z_{X^2Y}, and Z_{XY^2} are exactly the same and including all three of them would make the regression
matrix singular when doing hermite polynomial regression. So from there it can be learnt that we need to include just
one product out of above three.

From above I learnt that for a complete span in the space of products of variables as in above case, when there are two
variables, we only need to include X, Y and XY in our regression. 2^2-1 total regressors excluding constant of
regression.

when there are three original variables, we only need to include V, X, Y, VX, VY, XY, VXY in our regression. 2^3-1 total
regressors.

when there are four original variables, we only need to include U, V, X, Y, UV, UX, UY, VX, VY, XY, UVX, UVY,
UXY, VXY, UVXY in our regression. 2^4-1 total regressors.

So for N original variables, we will need 2^N-1 regressors.

Not all of these regressors might be needed but many times we would not know in advance. In order to do analytical analysis about which variables to exclude out of 2^N-1 regressors, you can read this post. https://forum.wilmott.com/viewtopic.php?t=99702&start=2520#p884966

In our example of SDE density hermite coefficients, we used seven starting variables, so there were a total of 127
regressors.

This choice of regressors is very different from what was usually used in classic regressions. So sometimes we can just
use classic regression models with an optimum choice of regressors to get excellent results.

Please note when a variable is not strictly positive and can be both positive and negative, the above analysis would
need to be modified with some additional products in the regression.

---

### #2558 — Amin (Topic Author)
*December 11, 2024, 4:07 AM*

Friends, I might be away from forum for a day or two and hope to come with something interesting over the weekend.

I am very excited after our exploratory success in MATH AI. I will continue working with MATH AI and its applications
for next few months and years to come. We just started a foray in this very exciting area and we were lucky that we have
had some initial success. I hope that we will do many more interesting things in the times ahead. One thing is very
clear that really most interesting things have yet to follow and we will have to do more hard work for many more
interesting things to happen in the most exciting field of MATH AI.

At this milestone, I will like to thank all those Americans and others who helped me when I was losing hope in the mid
of most difficult and tough mind control and my mind control decreased remarkably due to their efforts. I would never
have been able to do any meaningful research if it were not help from good and kind Americans and I have enormous
gratitude for all those friends due to whose favors I was able to work in a better environment and I could continue my
research. Any of my research in recent years simply would not have been possible if it were not for help and support
from many good Americans. I want to thank all those people who tried to decrease my mind control and enabled me to work
better. I truly wish and hope that I would also be able to continue my research for the rest of my life.

---

### #2559 — Amin (Topic Author)
*December 11, 2024, 6:24 AM*

Friends, I was thinking about it and had a few ideas about increasing the dimensionality of the least square regressions
while maintaining a close to complete span in the space of products of variables (or some other desired space of
functions).

I really think we can do a multi-layer neural networks type regression networks but based solely on least
square-regressions and backward conditional expectations.

Just like main idea behind multilayer networks is to decrease dimensionality because if we have a single layer it will
need to be very huge and extremely difficult to tackle. Analogous to neural networks,  when we  have several hundred
original variables in least squares regression, its size has to grow by 2^M-1 which cannot be tackled and in such
problems, we can resort to multi-layer regressions which will greatly reduce the dimensionality of the problem by a
large number. I will come back to this theme in a few days and share more ideas.

---

### #2560 — Amin (Topic Author)
*December 11, 2024, 6:58 PM*

Friends, I have been thinking about how to break down the exponential problem of 2^N-1 regressors. And I have some basic
raw ideas that I am sharing with friends.

Let us suppose we have seven variables and we need (127 X (Polynomial Order=6) ) regressor terms to have a full span of
sixth order polynomials. I think we can breakdown all the (127 X 6) terms into 20-40 polynomials with each polynomial in
several regressors. Some terms might be repeated and be common in some of the polynomials so these polynomials do not
necessarily have all disjoint/non-common terms. We can also do analysis to remove terms that have zero non-overlapping
correlation with the regressand. I have some ideas and I think this can be done quite efficiently.

Then we regress each of the 20-40 polynomials in several variables on the target regressand one by one and fix internal
coefficients of each of these 20-40 polynomials from these regressions. Then we do a universal regression in which each
of the 20-40 polynomials (whose internal coefficients have already been fixed) appear as variables and we fix outer
coefficients of each of these polynomial variables from this universal regression.

I believe something on these lines, we can breakdown the regression into smaller parts. Add to this that we would
already have removed terms that had little unique correlations with target regressand and this could give us a decent
framework for efficiently doing the regression. The problem remains how to do this in an optimal and efficient fashion.

---

### #2561 — Amin (Topic Author)
*December 12, 2024, 2:15 PM*

Friends, I went ahead and tried to explore the ideas in the previous post.

I think our attempt has to decrease the number of regressors in a regression that increase exponentially to something
that increases as a square as a first step.

Towards that goal, I decided to see how do the ideas in previous post work. I took the same case of densities of SDEs
with seven original variables. I made seven multidimensional polynomials in a very uninformed way. In first polynomial,
there were just seven variables with first power. In second polynomial, there were twenty one regressors with one
product operation( nchoosek(7,2) ), in third polynomial, there were thirty five regressors with two product operations (
nchoosek(7,3) ) and so on. In seventh polynomial, there was just one term with product of all variables. This was rather
simplistic without any special analytics but I wanted to check how it goes.

I calculated inner coefficients of all these polynomials with least square regression on the target regressand. And then
I substituted the values of the inner coefficients (which will be different for all different regressands) to get merely
seven variables/regressors in the least square regression and found their outer coefficients. And I was able to get
quite good results. Here is what I got

For mean:                                  .9985 R-Squared with just plain seven aggreagated regressors VS .9999967 with
127 X 6 regressors.

For 1st  Hermite Coefficient.     .98724 R-Squared with seven regressors                                    VS .99959 
with 127 X 6 regressors

For 2nd Hermite Coefficient.     .99825 R-Squared                                                                      
VS .999980 with 127 X 6 regressors

This was without any special analytics about which variables to lump together in a single polynomial.

I have some good ideas about drastically decreasing the number of regressors based on some correlation analysis that
could be applied first before grouping products of variables into polynomials and for fast decrease in dimensionality. I
will try to explore that in next few days.

There could be faster algorithms to calculate regressors from one set of regressors or polynomials to other set of
regressors that would decrease computational complexity of the problem. For example to calculate a higher product, we
could make a simple multiplication to a lower order product and so on.

I think initially it would be interesting to first keep a target that we decrease the size of total final regressors to
somewhat close to square of original variables as opposed to exponential increase. I really think our R-squared might
virtually be the same as full model R-Squared if divide the original seven variables into 49 (7^2) regressors after
proper analytics as opposed to only seven regressors in the above calculations without any special analytics.

---

### #2562 — Amin (Topic Author)
*December 13, 2024, 7:23 PM*

Friends, just like Least Squares Regression is a very powerful tool of Math AI if used properly, I am thinking that a
lot of things that are done by reinforcement learning can possibly be done by new generation of dynamic
regression/bayesian models for non-Gaussian random variables.

Kalman Filter and related models were great advances in science but they were rather limited by the need of underlying
stochastic variables and their noises to be gaussian. The extensions of Kalman Filters to non-gaussian random variables
were very useful but had their own limitations. Despite the usefulness of these first generation dynamic regression
models, their applications to non-Gaussian random variables have always remained a challenge. Please let me clarify that
Dynamic regression models are a broader class and filters associated with hidden states are just a part of larger class
of dynamic regression models.

Our research in Hermite Series expansions of random variables and knowledge of related analytics gives us a strong
opportunity to develop dynamic regression models that can capture evolution of non-Gaussian models very easily. We can
easily do analytics of evolution of non-Gaussian random variables with our work and research on Hermite Series
representations.

Stock market is an example where dynamic regression models for non-Gaussian random variables can have very useful
applications as the densities of various stock market instruments continue to change and shift dynamically with time.
However, in order to be successful, we need to implement dynamic regression models intelligently. The choice of
option-pricing based SDEs (and their state-space analogues), while very useful for capturing uncertainty required to
model derivatives, are exactly the wrong approach for stock market dynamics, and instead of modelling uncertainty, we
need to model the information based variables that are able to capture the dynamics of stocks and other financial
assets in non-Gaussian dynamic regression models.

I want to work with non-Gaussian dynamic regression models with various applications of these models in stock markets. I
will be doing some basic research with non-Gaussian dynamic regression models for next few weeks and then we will study
their various applications to stock markets hopefully starting January next year. It will take a few weeks to transfer
the infrastructure we have previously developed with hermite polynomials based non-Gaussian models to dynamic regression
models setting and then we would move to hands on applications to stock markets based on real data. Instead of dealing
with regressions on point values of random variables, we will do analytics with ever-changing densities of the random
variables in the financial markets.

---

### #2563 — Amin (Topic Author)
*December 17, 2024, 12:15 PM*

Friends, sorry for not writing a new post for so many days. I have been trying to make myself more familiar with
long-term trading methods and have also been thinking about technicalities of the numerical models involved. For
example, I really want to give correlated hermite series representation to each of the coefficients of hermite series of
a random variable meaning that coefficients in the hermite series of random variables would have their own hermite
series possibly correlated with hermite series of coefficients of other orders. But it is not very simple to estimate
hermite series of coefficients. I will be testing today and in next few days what could be numerically possible and what
could not be easily possible and if any numerical method could possibly do that, I will share it with friends. I will
basically be working with numerical preliminaries before January. I will also be trying to become more familiar with
existing methods, techniques and strategies people already use in their long term trading.

I hope to come back in a day or two with more information about how my numerical experiments go when we want to give
hermite series dynamics again to coefficients of hermite polynomial series of random variables and be able to estimate
these second order hermite series of coefficients from the data of random variables.

I am not making a technical post with latex since I want to be sure that numerical methods I am thinking would work and
if I can make them work, I will explain things with a latex post along with posting the matlab program.

---

### #2564 — Amin (Topic Author)
*December 19, 2024, 3:01 AM*

EDIT: Updated 19/12/2024

Dynamic Coefficients Hermite Polynomial Series Models For Time Series Evolution of Random Variables

 In this brief note we want to discuss hermite polynomial series representation of random variables where coefficients
of hermite polynomials are also represented by another hermite polynomial series for each coefficient.

We give some example of some practical dynamic hermite series coefficients models below

$
$\, X(Z,Z_0,Z_1,Z_2,Z_3)\,=\, \left(a_{00} \,+\,a_{01}\,Z_0 \right)\,+ \, \left( a_{10} \,+\, a_{11}\, Z_1 \right) \, Z\, + \, \left( a_{20} \,+\, a_{21} \, Z_2 \right) \,\, \left( Z^2\,-\,1\,\right) \\ + \, \left(a_{30} \,+\,a_{31}\,Z_3\right) \, \left( Z^3\,-\,3 \,Z\,\right)    $
$

The above model can also be written as

$
$\, X(Z,Z_0,Z_1,Z_2,Z_3)\,=\, a_{0}(Z_0)\, + \, \, a_{1}(Z_1)\, \, Z\, + \, \, a_{2}(Z_2)\,\, \left( Z^2\,-\,1\,\right) + \, \, a_{3}(Z_3)\, \, \left( Z^3\,-\,3 \,Z\,\right)    $
$

where

$$\, a_{0}(Z_0)\, =\, \left(a_{00} \,+\,a_{01}\,Z_0 \right)\,$$

$$\, a_{1}(Z_1)\, =\, \left(a_{10} \,+\,a_{11}\,Z_1 \right)\,$$

$$\, a_{2}(Z_2)\, =\, \left(a_{20} \,+\,a_{21}\,Z_2 \right)\,$$

$$\, a_{3}(Z_3)\, =\, \left(a_{30} \,+\,a_{31}\,Z_3 \right)\,$$

We would mostly need to give dynamics to coefficients of only first four polynomials in the hermite series. All of these
$Z_0\, \,Z_1, \, Z_2,\,Z_3 $ would not be correlated with each other but could be correlated with
$\bar{Z}_0\, \,\bar{Z}_1, \, \bar{Z}_2,\, \bar{Z}_3 $ which are dynamic coefficients of hermite series of another random
variable.

Estimation of the coefficients in the Dynamic Coefficients Hermite Series Model

The above model has eight coefficients and these coefficients of the model can easily be estimated by some numerical
method that uses multidimensional Newton to fit first eight moments of the data to model. I will be posting this Newton
program in next few days. Again knowledge of eight moments of data would be required to find the eight coefficients in
the model.

Estimation of the Present State of coefficients in the Dynamic Coefficients Hermite Series Model

Even after estimation of all coefficients in the model, we do not perfectly know the values of
$ a_0(Z_0), \, a_1(Z_1),\, a_2(Z_2), \, a_3(Z_3) $ since they depend upon their respective Z's. And we also have to know
that one observation (one degree of freedom) is not enough to pin down all these four Z's. However, we can use a sliding
window of anywhere between 4 - 10 or higher number of time intervals to estimate first four local moments of the time
series. We can use these local values of moments to estimate the model

$
$\, X(Z)\,=\, a_{0}\, + \, \, a_{1}\, \, Z\, + \, \, a_{2}\,\, \left( Z^2\,-\,1\,\right) + \, \, a_{3}\, \, \left( Z^3\,-\,3 \,Z\,\right)    $
$

We would have to use Newton inversion on each step to find the coefficients$ a_0, \, a_1,\, a_2, \, a_3 $ from the above
equation fitted to local data moments and use the relationships

$$\, a_{0}\, =\, \left(a_{00} \,+\,a_{01}\,Z_0 \right)\,$$

$$\, a_{1}\, =\, \left(a_{10} \,+\,a_{11}\,Z_1 \right)\,$$

$$\, a_{2}\, =\, \left(a_{20} \,+\,a_{21}\,Z_2 \right)\,$$

$$\, a_{3}\, =\, \left(a_{30} \,+\,a_{31}\,Z_3 \right)\,$$

to find the values of$Z_0, \, Z_1,\, Z_2, \, Z_3 $ which can be used to calculate their correlations with dynamic
coefficients of some other random variable through values of$\bar{Z}_0\, \,\bar{Z}_1, \, \bar{Z}_2,\, \bar{Z}_3 $ of
dynamic coefficients of the other random variable. With each new time interval, the sliding window will move ahead by
one time interval and values of first four local moments would change and that would result in update values of
$ a_0, \, a_1,\, a_2, \, a_3 $ found from inversion of new first four moments giving us new updated values of
$Z_0, \, Z_1,\, Z_2, \, Z_3 $ for the new interval.

Explanation of the Model and its Usefulness

We do one global optimization on data to learn the parameters. And then we do local optimizations on local data to find
the values of$Z_0, \, Z_1,\, Z_2, \, Z_3 $ . The first four hermite polynomials terms are highly correlated with first
four moments of the data respectively. So knowledge of$ a_0, \, a_1,\, a_2, \, a_3 $ found from local data would tell us
about local values of mean, variance, skew and kurtosis. And values of$Z_0, \, Z_1,\, Z_2, \, Z_3 $ would tell us how
local values of mean, variance, skew and kurtosis have changed in terms of their respective standardized indicators
(standard normal values) based on the range found in global data.

The knowledge of local values and the standard deviations from averages for mean, variance, skew and kurtosis would be
extremely helpful in vanilla stocks trading strategies and also in option pricing trading strategies. We will explore
these uses of the model when we apply them to real stocks and option pricing data next year.

More details of the model and a worked out matlab program will follow in a few days.

---

### #2565 — Amin (Topic Author)
*December 19, 2024, 3:07 AM*

Friends, I am writing this post to talk about frenetic attempts towards my mind control. Pak army tries to drug my food
like crazy everyday. If I take a path in the city, they basically target nd drug everything I like to eat and it is
becoming very very difficult to get everything good. And this is one of the major reasons behind decreased speed of my
research. Everyday when I go out to get food and water, I am hit with some bad food somewhere or buy something bad that
I cannot easily tell and most of the times I become very lethargic after eating bad food.

After I worked out details of my research last night that I wrote in previous post today, they did not let me sleep and
kept me awake. This was also because finally, after so many days, I was able to get good food and mind control agents
were worried that a good sleep at night would reverse their mind control effect.

They had drugged all brands of manufactured yogurt in the city but I started to buy local made yogurt sold by small milk
shops but they distributed mind control chemicals among a huge number of milk shops in the city and now it is very
difficult to buy good yogurt even from small milk shops. Similarly friends could recall my huge persecution activity
last winters but I survived on pasta and jam. But this year, they approached all jams, ketchup and pasta manufacturers
and now all these things are completely drugged in the market. I also started cooking some simple things at home since
last year but army approached all of the vegetable oil manufacturers and most of the vegetable oils in the market are
drugged. I have to switch to unknown banaspati ghee brands since almost all of the vegetable oils in the market are
drugged with mind control chemicals. Similarly they have distributed mind control chemicals among large number of naan
shops and they drug their flour and it becomes difficult to buy good Pakistani bread. Breads prepared by all bakeries
and by dawn, bunnys and other bread companies are also drugged with mind control chemicals. SO it becomes extremely
difficult to buy good food in the city and I continue to get hit almost every other day and remain lethargic as a result
and it becomes hard to work properly with enthusiasm.

I believe that several hundreds of army soldiers are asked to drug food on my path when I go out to buy food. Several
soldiers are asked to keep visiting the markets all along the city and continue to drug food at all the stores that
might be of my interest and might not have been drugged at manufacturing source.

So mind control is raging at full swing and there is absolutely no let down in my persecution activity at all. I will
have to be injected with Fluanxol antipsychotic injection in a week and all the injections on market are highly drugged
with mind control chemicals.

There has been very frenetic activity to drug my food and water throughout past week by Pak army soldiers since I have
tried to do good research and some people want to stop all my future research and they bribe corrupt bosses of army in
Pakistan who in turn put a huge number of soldiers on the road to keep drugging the food and water everywhere.

I want to request all good Americans to please protest to their government to end my mind control. I also want to
request European friends to please ask your embassies to pressurize corrupt Pakistani establishment to not retard our
own Pakistani talent in return from bribes from American defense.

---

### #2566 — Amin (Topic Author)
*December 20, 2024, 5:14 AM*

**Friends, I did not want to write about anything other than my research but I am extremely worried that my persecution
would only intensify in coming days. Any manufactured food that has been left from being drugged at manufacturing source
would soon be drugged in a few weeks. I am already eating a very unhealthy and unbalanced diet since possibilities of
what I can eat are very limited. And this already effects my physical health and also makes me unable to work hard
properly on my research. Several of my liver enzymes were far more than their normal range in a test last year. I lost
some weight after that with great effort but I could not hold on because I was unable to take a balanced diet and my
weight increased again in last month and I feel that it is taking its huge toll on  my liver again. And I am very afraid
that my remaining food possibilities would be thoroughly squeezed within a few weeks.  And I am sure that there are
plans to detain me in a few weeks when new government comes in US. Therefore with a heavy heart I have to interrupt
friends and ask them to protest to American government about my persecution. I am posting some of the old material about
my persecution again and I would sincerely request American, European and Pakistani friends to at least bring the
attention of 3-4 media outlets about my posts and also about true nature of mind control.**

**I will apologize to all good jews about my following posts that are very necessary at the moment. I want to tell
friends in advance that my posts are not against jews in general at all and according to context whenever I mention
jews, I mean only the bad jews who are behind the evil of mind control. Please give utmost respect to all good jews you
know and who are good human beings. And please be genuinely nice to all jewish folks in general. I only mean to write
against those rich jews who are centered around a jewish billionaire and who are the reason for cruel, inhuman and
extrajudicial mind control in our societies. Again there are a large number of rich jews and jewish billionaires who
contributed greatly to progress of our societies especially the US and I do not mean to malign them at all and would
urge friends to completely respect all such good jews.  When I say jews in a bad context in the following posts, I only
mean the evil jewish cohort that is behind mind control and not those good jewish people in general who have nothing to
do with mind control. I hope that every reader of my posts would know the difference between evil rich jewish cohort
(behind mind control) and good jewish folks and not mix up between them. Intention of my posts is only to end the evil
of cruel, inhuman and extrajudicial mind control from our societies. However, I would request all good jews to join the
rest of us in opposing the cruelty of mind control and try to end it in our societies.**

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

### #2567 — Amin (Topic Author)
*December 20, 2024, 5:18 AM*

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

### #2568 — Amin (Topic Author)
*December 20, 2024, 5:22 AM*

**(broken latex: Unbalanced $: 1)**

```latex
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
```

---

### #2569 — Amin (Topic Author)
*December 21, 2024, 12:44 PM*

Friends, here is the progress on my research. I have written the main program to calculate derivatives for
multidimensional Newton root search. I would be embedding it today in the program that combines Newton search with
iterative method as I had done in my latest program for finding Z-series that I posted about two months ago. And if
things go well without any problems tomorrow, I will be posting the new matlab program to find the dynamic coefficients
of a hermite series for time series of random variables on Monday or Tuesday by the latest.

However, this program is only one part of the suite of numerical methods we want to develop and we will have to continue
to work over the next week to complete all the work as described in the research description of dynamic coefficients
HJermite series models.

I am looking forward to completing the research work in the best possible way.

---

### #2570 — Amin (Topic Author)
*December 22, 2024, 6:07 AM*

**Friends, I try to think about why some people are so adamant about persecuting talented Muslims (hugely more so than
others) in United States with mind control and in other ways. These people want to keep the image of Muslims as
uneducated and ignorant terrorists and when any Muslim tries to find expression by doing good things in our societies,
these circles with vested interests spring into action to thwart those Muslims even if those Muslims are trying to do
something perfectly good for the society in every way. They try to stop any Muslims from being popular in American
society by stopping them from good things lest it changes the backward and terrorist image of Muslims. **

**Also these elements work together with hardliners in American society. Please recall how CIA and American agencies
were trying to thwart Martin Luther King when he was trying to weed out racism from American society. CIA racists
perfectly and sincerely believed in thwarting Martin Luther King in every way all through his life, however looking back
at his efforts, most Good people in United States now Celebrate Martin Luther King day as a national holiday in US.**

**I had written this post on Wed Aug 15, 2018 before I had done any major research. Please read this post to understand my point of view.  https://forum.wilmott.com/viewtopic.php?t=101453**

Here I am copying the post that I wrote seven years ago.

**The purpose of this post is actually an attempt to bring forward some wrongs in American and other societies and
request all good people to consider on their own if the wrongs I am trying to point towards do exist in our societies
and if they do agree that these wrongs actually do exist in our societies then request them to do something positive to
address these wrongs.

**

**I want to start by pointing towards brain control by American defence department. I believe a huge number of totally
innocent people are targeted by American defence department due to totally wrong reasons like religious biases, attempts
to please powerful connections of people in defence department and other totally unjust and unethical reasons that can
never otherwise openly exist in American society. American defence is a bloated, inefficient and corrupt organization
full of thoroughly medicore people. And many of these people have started a practice of retarding so many innocent
people something that has been accepted by American society because of American society's lack of knowledge behind the
reasons of retarding of innocent people and this practice has become above the justice and legal system. I believe it is
high time that American people and other nations start a discussion about ethics and morality of retarding innocent
people by American defence department.**

**When the decision to retard someone has been made by people at American defence department, these mediocre people
resort to all sort of lies and many times completely false things to justify the mind control of the victim to general
public and they do it without any regard that by speaking total lies, they are betraying the trust people place in
Americans in general and they have no regard how it would affect the reputation of otherwise good natured American
public.**

**Speaking about Pakistan, several hundred millions of dollars are given to generals in Pakistan army and other
influential people who support and lobby for mind control by American defence in Pakistan so that mind control
infrastructure continues to work in Pakistan. Most of the mind control victims in Pakistan are young people who want to
do good science and technology in our country.**

**I would also request good American people to allow Muslims to find expression in doing good things and their attempts
at contributing towards American and other societies and towards broader humanity. Most of my readers would be aghast
why I am asking for anything that is actually freely allowed and many times actively promoted in our societies. Ok, I
have something to say.**

**Since I could be taken very wrong, I would like to say something before I start the next paragraph. Most jews are very
good humans and they have earned their place in American society over a period of long time by contributing to almost
every facet and dimension of American society. And they are thorough Americans. Some prominent jews are true role models
for what a good human should be. And again most jews are thorough gentlemen and very good humans.**

**Sadly due to conflict between Palestinians and Israelis, many places in the world including America, there is tendency
for this in minds of some of  the Jews and Muslims to consider it a Muslim-Jew conflict which is an extremely wrong
approach and I am sure many people will agree with me. Though many people might disagree and I would totally respect
their understanding but my sincere understanding that in some very limited jewish circles(and I would ask people to
never generalize it to all jews and not misunderstand me), there is a tendency to thwart Muslims from finding an
expression in positive activities since such activities will slowly improve the impression of Muslims in general
American public after they have contributed to American society. And sadly some people think this will at some stage
hurt the Israeli position in Palestinian-Jewish conflict. This is a very dangerous approach and cruelly targets some
Muslims who are put on brain control due to this reason by corrupt United States defence department. Again Of course,
Jews are so thoroughly American and have earned their place in American society so my saying anything is not going to
make any difference to them but I do want to request them to be better with muslims sometimes.**

**United States defence department many times shapes the foreign policy of United States. I will throw something wild
and seemingly unrelated thing for American people to think on their own. Do you guys recall what Donald Trump was saying
about Shakil Afridi? I will get him out of jail in a few minutes after I become president. He was not making a statement
that is beyond the power of American president. If American president Donal Trump shows his anger, all the Pakistani
generals will be standing in line begging for mercy. American president loves to bash every other nation but we do not
hear any mention of Shakil Afridi from him which would make such a fantastic bashing point. I really think there are
some people in American decision making circles who do not want Shakil Afridi in America. He was the guy who helped kill
the largest and most dangerous terrorist in world and American public will be full of praise for Shakil Afridi. Some
people think his walking free in American public will marginally improve the impression of Muslims in America and they
would rather let him rot in Jail and now Donald Trump does not like to make any mention of Shakil Afridi despite that it
is something that could be hugely popular with general American public.**

**Though I have been blunt to the limit of being rude and I want to apologize to most of the jews who are extrremely
good humans and have absolutely no such bad thing like I mentioned here and I want to tell them that I consider all good
humans my friends regardless of thier religion.**

**I want to ask American people to please let all good Muslims just like other good people of other religions or no
religion to be able to find their expression in doing good things that would contribute to society. **

To put everything in context for people, I am copying my letter that I wrote when US defence intervened to make sure
that I do not get a PhD position at a place in Europe. I have erased all names and references in the letter.

Dear *****,

I had written earlier with a request for PhD position with ***** in ****. When I wrote the earlier emails, I withheld a
lot of information about myself that I would like to share now. My present motivation for writing this email is that I
was writing to several other universities in mainland Europe for a PhD position and I was thinking that I would totally
love to do PhD with a great research organization like ****** and I should retry and make a solid effort again while
sharing the private information about me and try to appeal to humanity of good ***** people. And hope they will
understand my position as a human.

When I was studying at ***** for a masters degree for Economics twenty years ago, some people recognized me for my talent in mathematics and they had connections with US defence. And I was put on mind control by US defence and for the past twenty years, I have remained on mind control. When I was a student at ***, I was religious enough in the sense that I would never pray but I would not eat meat other than kosher. But I was very respectful of people of other religions. I had absolutely no negative thing in my dealings with others due to my religion. But I was targeted since many people in US defence would not want me to be very successful since I was a Muslim. And I would like to mention again that I do not blame Americans for my persecution. It is a lot of like-minded people in American defence who consider Muslims as their enemies which is so wrong and it is something that most Americans would totally disagree with. At this stage in my life, I am not religious at all and I pray on Fridays only because it would hurt me if I do not pray as my conservative family would make a huge issue out of it. When my persecution started in United States twenty years ago, I decided to go to my country but people in American defence connived with my family and also bribed military generals in Pakistan who would together help the US mind control efforts. My parents themselves would put mind control drugs in my food and when I would try to get good food from other places, they would declare me schizophrenic and the psychiatrists would be told by powerful military generals to cooperate with my parents. For past twenty years, I have been kept on huge antipsychotics because of the connivance of my family, and the military generals in Pakistan. And when I would try to talk to some good psychiatrist who would not be willing to declare me mentally ill, my family would detain me for long periods of time with psychiatrist of their own choice. And at the same time, whoever I try to contact in foreign countries for projects in computational finance, they will be contacted by people in US defence (when I try to contact people in Europe) and powerful military generals in Pakistan (when I talk to some Pakistani company) so that I would not be able to make money on my own. Though I was on huge antipsychotics, I still continued to follow my passion for mathematics research. And my research would have been far more meaningful if I was not forced on huge antipsychotics that sharply impair my ability to think. Since my orientation all my life was to be very nice with people, I never turned negative despite my obviously wrong persecution and tried to find my expression in doing good mathematics research despite all odds. Over past twenty years, I have faced all kind of trauma, torture and persecution since my parents and my family were totally blinded and would remain human only if I would be willing to take huge doses of antipsychotics and if I refuse to take huge doses of antipsychotics, they would become total animals. I have been writing about my persecution on this blog but I would want to warn that many times my writings have been affected by mind control emotions that mind control agencies force on their targets. Here is my blog on internet: https://forum.wilmott.com/viewtopic.php?f=15&t=94796&start=900

And I want to emphasize that only activity I truly enjoy is research in mathematics and this is the only thing I would
love to do for the rest of my life. And since this topic might come up again, I would clearly stress that I believe
religion should be a totally private matter to people and they should not make it a consideration in any of their public
decision making.

I would make this request again on human grounds to please reconsider my request for a PhD at ***** and I want to say
again that I would totally devote myself to research and I really do not want to fret about my past persecution and
anything wrong done to me. I just want to restart my life with a positive emotion and passion for mathematics that I
want to follow for the rest of my life. Again I truly want to stress that only meaningful thing I see in my future life
is research in mathematics and I would be truly thankful and completely indebted to you if you could help me follow my
passion in life.

I truly request you again to please reconsider my request for a PhD at *******.

I wish you a good day.

Best regards,

Ahsan Amin

---

### #2571 — Amin (Topic Author)
*December 23, 2024, 8:36 PM*

Friends, still working on the model. It may not be possible to post it on Tuesday but I will try to post it on Thursday
or Friday after the Christmas day.

I wish a very happy Merry Christmas to all readers of my thread. Please do not forget to check my thread in Christmas
vacations.

---

### #2572 — Amin (Topic Author)
*December 24, 2024, 5:13 AM*

Friends, I have proto-type of my first part of program working. The purpose of this part is to calibrate the following
model to global data.

$
$\, X(Z,Z_0,Z_1,Z_2,Z_3)\,=\, \left(a_{00} \,+\,a_{01}\,Z_0 \right)\,+ \, \left( a_{10} \,+\, a_{11}\, Z_1 \right) \, Z\, + \, \left( a_{20} \,+\, a_{21} \, Z_2 \right) \,\, \left( Z^2\,-\,1\,\right) \\ + \, \left(a_{30} \,+\,a_{31}\,Z_3\right) \, \left( Z^3\,-\,3 \,Z\,\right)    $
$

My strategy is to first start with calibration of the following simple model to four moments of global data with all of
the$\,a_{01}\,,\,a_{11}\,,\,a_{21}\,,\,a_{31}\,$ equal to zero.

$
$\, X(Z)\,=\, a_{00} \,\,+ \,  a_{10} \,\, Z\, + \, a_{20} \,\, \left( Z^2\,-\,1\,\right) + \, a_{30} \, \, \left( Z^3\,-\,3 \,Z\,\right)    $
$

Then I introduce the parameters$\,a_{01}\,,\,a_{11}\,,\,a_{21}\,,\,a_{31}\,$ with initial values equal to zero and I
start to iteratively perturb them away from zero with an objective function that maximizes fit to first eight moments.
But while doing this we also alter already calibrated coefficients with Newton method so that first four moments remain
in exact calibration. Precisely we perturb one of the above last four coefficients by a small amount and apply Newton
method on first four coefficients so that after the small perturbation, the first four coefficients are slightly
adjusted so that the model still remains in perfect calibration to first four moments. We, then, apply the objective
function of first eight moments and accept the small iterative perturbation if the objective function to eight moments
improves. So with large number of small iterative perturbations in the direction of increasing fit to eight moments
while keeping first four moments in exact calibration, we are able to fit all of the eight coefficients so that first
four moments are exactly calibrated while last four moments (5-8) are as closely calibrated as possible. All of the
above calibration is to global data.

I am still playing with the model and I still want to find out if exact fit to all of the first eight moments could be
possible but I could not be sure of that at the moment.

---

### #2573 — Amin (Topic Author)
*December 24, 2024, 8:10 PM*

Friends, in the model as described in previous post, I have been able to get extremely close fit to first eight moments
for some data sets I had. And coefficient parameters seem to converge to unique values in initial tests. I think the
model is ready and good enough that friends can play with it using their data. I will write explanatory comments
tomorrow and then post the matlab program for the model either on Wednesday or Thursday.

---

### #2574 — Amin (Topic Author)
*December 25, 2024, 10:03 PM*

Friends, I am playing with the model calibration and trying to test it a bit more for robustness in various market
regimes.. I still have to write comments on the matlab program. Hopefully, I will be posting it in a day or two.

Meanwhile, I have been thinking of other possibilities to estimate our global dynamic coefficients model. And I realized
that there could be possibilities to directly estimate the model from data. Here I want to discuss how to estimate the
dynamic coefficients model directly from data.

Estimation of Dynamic Coefficients of Z-Series Models For Time Series Evolution of Random Variables

 We give example of a practical dynamic Z-series coefficients models below

$
$\, X(Z,Z_0,Z_1,Z_2,Z_3)\,=\, \left(c_{00} \,+\,c_{01}\,Z_0 \right)\,+ \, \left( c_{10} \,+\, c_{11}\, Z_1 \right) \, Z\, + \, \left( c_{20} \,+\, c_{21} \, Z_2 \right) \,\,  Z^2\, \\ + \, \left(c_{30} \,+\,c_{31}\,Z_3\right) \, Z^3\,   $
$

Please note that hermite series models and Z-series models are interchangeable and estimating any of the two
possibilities could lead to other.

In this method, we use least square regression with our discretized standard normal variable grid method to estimate
Z-series of both$\, X\, $ and$\, X^2\, $ and then use some algebra to find the dynamic Z-series coefficients.

We could notice if we used least square regression with our discretized standard normal variable grid method to estimate
Z-series of$\, X\, $ from its data values (and not directly by matching moments) , we could estimate the above dynamic
coeff model as

$
$\, X(Z,Z_0,Z_1,Z_2,Z_3)\, =\, \, \left(c_{00} \,+\,c_{01}\,Z_0 \right)\,+ \, \left( c_{10} \,+\, c_{11}\, Z_1 \right) \, Z\, + \, \left( c_{20} \,+\, c_{21} \, Z_2 \right) \,\,  Z^2\, \\ + \, \left(c_{30} \,+\,c_{31}\,Z_3\right) \, Z^3\, $
$

Taking expectations over coefficients of powers of Z, we get the least squares solution given as

$
$\, X(Z,Z_0,Z_1,Z_2,Z_3)\, =\, \,=\, c_{00} \, \,+ \,  c_{10} \,\, Z\, + \,  c_{20} \, \,\,  Z^2\, + \, c_{30} \, \, Z^3\,  $
$

We could also estimate the coefficients of Z-series of$X^2$ using least squares regression and employing discretized
standard Gaussian grid as

$
$\, {X(Z,Z_0,Z_1,Z_2,Z_3)}^2\, =\, {\left[\left(c_{00} \,+\,c_{01}\,Z_0 \right)\,+ \, \left( c_{10} \,+\, c_{11}\, Z_1 \right) \, Z\, + \, \left( c_{20} \,+\, c_{21} \, Z_2 \right) \,\,  Z^2\, + \, \left(c_{30} \,+\,c_{31}\,Z_3\right) \, Z^3\, \right]}^2 \, $
$

Expanding the above square and collecting terms of powers of Z, we get

$
$\, {X(Z,Z_0,Z_1,Z_2,Z_3)}^2\, =\left({c_{00}}^2+2 c_{00} c_{01}\, Z_0\,+\,{c_{01}}^2\,{Z_0}^2 \right)\,  + \, Z \, \left(2 \,c_{00} c_{10}\,+\,2\, c_{01}\, c_{10} Z_0\,+\,2\, c_{00}\, c_{11}\, Z_1 \,+\,2\, c_{01}\, c_{11}\, Z_0\, Z_1 \right)\,\\+\, Z^2 \, \left(\,{c_{10}}^2\,+\,2\, c_{00}\, c_{20}\,+\,2\, c_{01}\, c_{20}\, Z_0\,+\,2\, c_{01}\, c_{11}\, Z_1\,+\,{c_{11}}^2 \,{Z_1}^2\,+\,2\, c_{00}\, c_{21}\, Z_2\,+\,2\, c_{01}\, c_{21}\, Z_0 \,Z_2 \right)\, \\+\, Z^3 \, \left(\,2\, c_{10}\, c_{20}\,+\,2 \,c_{00}\, c_{30}\,+\,2 \,c_{01}\, c_{30}\, Z_0\,+\,2\, c_{11}\, c_{20}\, Z_1\,+\,2\, c_{10}\, c_{21}\, Z_2\,+\,2 \,c_{11}\, c_{21}\, Z_1\, Z_2\,+\,2\, c_{00}\, c_{31}\, Z_3\,+\,2\, c_{01}\, c_{31}\, Z_0\, Z_3 \right)\,\\+\,Z^4 \, \left({c_{20}}^2\,+\,2\, c_{10}\, c30\,+\,2 \,c_{11}\, c_{30}\, Z_1\,+\,2\, c_{20}\, c_{21}\, Z_2\,+\,2\, c_{11}\, c_{31}\, Z_1\, Z_3 +\, {c_{21}}^2 \, {Z_2}^2 \,\right)\,\\+\, Z^5\,  \left(\,2\, c_{20}\, c_{30}\,+\,2\, c_{21} c_{30}\, Z_2\,+\,2 \,c_{20}\, c_{31}\, Z_3\,+\,2 \,c_{21}\, c_{31}\, Z_2\, Z_3 \right) \,+\, Z^6 \, \left(\,{c_{30}}^2+2 \,c_{30}\, c_{31}\, Z_3\,+\,{c_{31}}^2 \,{Z_3}^2\right) $
$

Taking expectations over coefficients of powers of Z, we get the least squares solution as

$$\, {X(Z,Z_0,Z_1,Z_2,Z_3)}^2\, = \left({c_{00}}^2+\,{c_{01}}^2\, \right)\, + \, Z \, \left(2 \,c_{00}\, c_{10}\,
\right)\,+\, Z^2 \, \left(\,{c_{10}}^2\,+\,2\, c_{00}\, c_{20}\,+\,{c_{11}}^2 \, \right)\,

+\, Z^3 \, \left(\,2\, c_{10}\, c_{20}\,+\,2 \,c_{00}\, c_{30}\, \right)\,

\\+\,Z^4 \, \left({c_{20}}^2\,+\,2\, c_{10}\, c_{30}\,+\, {c_{21}}^2 \right)\, +\, Z^5\, \left(\,2\, c_{20}\, c_{30}\,
\right) \,+\, Z^6 \, \left(\,{c_{30}}^2 \,+\, {c_{31}}^2\, \right) $$

We already have calculated the coefficients of X as

$
$\, X(Z,Z_0,Z_1,Z_2,Z_3)\, =\, \,=\, c_{00} \, \,+ \,  c_{10} \,\, Z\, + \,  c_{20} \, \,\,  Z^2\, + \, c_{30} \, \, Z^3\,  $
$

Combining last two equations, and using algebra on their coefficients we can values of all of
$ c_{00}, \, c_{10},\, c_{20}, \, c_{30},  c_{01}, \, c_{11},\, c_{21}, \, c_{31} $

---

### #2575 — Amin (Topic Author)
*December 26, 2024, 8:01 PM*

Friends, I went ahead and tried the model in previous post to simulated stochastic volatility SDE data and made two
interesting observations. But first I frame the previous (incorrectly formulated) problem again. We have estimated
equation of the Z-series of a random variable given below as

 $$\, X(Z)\, =\, \,=\, a_{0} \, \,+ \,  a_{1} \,\, Z\, + \,  a_{2} \, \,\,  Z^2\, + \, a_{3} \, \, Z^3\,  $$   Eq(1)

Now we want to add more information to above dynamics in light of Z-series expansion of $X^2$ which is given as

$
$\, {X(Z)}^2\, =\, \,=\, b_{0} \, \,+ \,  b_{1} \,\, Z\, + \,  b_{2} \, \,\,  Z^2\, + \, b_{3} \, \, Z^3\,\, + \, b_{4} \, \, Z^4\,\, + \, b_{5} \, \, Z^5\,\, + \, b_{6} \, \, Z^6\,  $
$ Eq(2)

We (incorrectly) suppose that true model is given as

$
$\, {X(Z,Z_0,Z_1,Z_2,Z_3)}\, =\, \left(c_{00} \,+\,c_{01}\,Z_0 \right)\,+ \, \left( c_{10} \,+\, c_{11}\, Z_1 \right) \, Z\, + \, \left( c_{20} \,+\, c_{21} \, Z_2 \right) \,\,  Z^2\, + \, \left(c_{30} \,+\,c_{31}\,Z_3\right) \, Z^3\, \, $
$ Eq(3)

where $c_00 \,=\, a_0$, $c_10 \,=\, a_1$, $c_20 \,=\, a_2$, $c_30 \,=\, a_3$      Conditions(1)

I used the following equations, in light of previous post, to determine

$$c_{01}\, = \, \sqrt{(b_0\,-\,{a_0}^2)} \\

c_{11}\,=\, \sqrt{(b_2\,-\, {a_1}^2 \,-\,2\,a_0 \, a_2)}\\

c_{12}\,=\, \sqrt{(b_4\,-\,{a_2}^2\,-\,2\,a_1\,a_3\,)}\\

c_{13}\,=\, \sqrt{(b_6 \,- \, {a_3}^2)} $$

When I found the coefficients of above (incorrectly) specified model, I noticed that$c_{11}$ was imaginary number which
obviously meant that we cannot add standard gaussians multiplied coefficients in each term since that would increase the
variance of the underlying random variable as compared to true variance. If we are adding standard gaussian multiplied
parameters somewhere that would increase the variance and to maintain true variance, the original coefficients have to
decrease somewhere.

Second thing I noticed that if Eq(1) were a true depiction of reality, median of$X^2$ would be exactly square of the
median of$X$ , or in other words$b_0\,=\,{a_0}^2$ but median of$X^2$ was always larger in my experiments than square of
median of X which meant that there are some extra dynamics and we need a model with extra dynamics like we specified in
Eq(3)( though our model was a bit incorrectly specified and we need to improve it. )

In light of above information, we restate the problem and change the form of Eq(3) to a different equation

$
$\, {X(Z,Z_0,Z_2,Z_3)}\, =\, \left(c_{00} \,+\,c_{01}\,Z_0 \right)\,+ \, \left( c_{10} \,-\, c_{11}\, \right) \, Z\, + \, \left( c_{20} \,+\, c_{21} \, Z_2 \right) \,\,  Z^2\, + \, \left(c_{30} \,+\,c_{31}\,Z_3\right) \, Z^3\,  \, $
$ Eq(4)

I have added dynamics in mean as well given by mean term$\left(c_{00} \,+\,c_{01}\,Z_0 \right)\,$ , I think this first
order variance associated with$Z_0$ uncorrelated with$Z$ would be absorbed in coefficient$a_1$ in Eq(1) (as summation of
two uncorrelated Z's) but since$Z_0$ is uncorrelated with Z, when take the square of X, its variance would not be
transferred to$b_2$ in Eq(2) and would rather be absorbed in$b_0$ and would actually increase the median (of$X^2$ )
value more than square of median of X.

Our estimation equation for coefficients of Eq(4) would change to

$$c_{01}\, = \, \sqrt{(b_0\,-\,{a_0}^2)} \\

c_{11}\,=-\,a_1\, +\sqrt{(b_2\,+\,\,{c_{01}}^2-\,2\,a_0 \, a_2)}\\

c_{12}\,=\, \sqrt{(b_4\,-\,{a_2}^2\,-\,2\,a_1\,a_3\,)}\\

c_{13}\,=\, \sqrt{(b_6 \,- \, {a_3}^2)} $$

Equation of$ c_{11}\,=-\,a_1\, +\sqrt{(b_2\,+\,\,{c_{01}}^2-\,2\,a_0 \, a_2)} $ is special and this would give us an
imaginary number and we just take its real value with a negative sign. Also I have subtracted${c_{01}}^2$ from the
equation since this value gets added to$a_1$ in Eq(1) but is not carried into$b_2$ when we take estimate Z-series of
square of X.

I would play more with the equations and come back with more analytics tomorrow or after that. Ideally, we would have to
make sure that all moments and variances are matched while estimating coefficients for equation(4).

---

### #2576 — Amin (Topic Author)
*December 26, 2024, 8:34 PM*

Regarding the model in previous post,  somebody can question that variance cannot automatically decrease in the
following equation

$
$\, {X(Z,Z_0,Z_2,Z_3)}\, =\, \left(c_{00} \,+\,c_{01}\,Z_0 \right)\,+ \, \left( c_{10} \,-\, c_{11}\, \right) \, Z\, + \, \left( c_{20} \,+\, c_{21} \, Z_2 \right) \,\,  Z^2\, + \, \left(c_{30} \,+\,c_{31}\,Z_3\right) \, Z^3\,  \, $
$ Eq(4)

We need to have some sort of justification of taking the decreasing term$\, \left( c_{10} \,-\, c_{11}\, \right) \, Z\,$
. We can say that if model in equation 4 is close to true model, in that case, the third term (which is actually
bivariate in normal RVs) given as$\, \left(c_{21} \, Z_2 \right) \,\,  Z^2\, $ and fourth term given as
$\left(c_{30} \,+\,c_{31}\,Z_3\right) \, Z^3\, $ which is also a bivariate term. If we expand these third and fourth
terms in form of a univariate series, both terms will contain a term of order Z which is possibly causing the
subtraction in second term and decreasing variance there.

For example we can expand the bivariate third term in terms of a univariate $Z_0$

$
$\,\left( c_{21} \, Z_2 \right) \,\,  Z^2\, = \, d_1 \, Z_0 \, + \, d_2 \, {Z_0}^2 \, +\, d_3\, \,{Z_0}^3\, \, + \ldots $
$

A similar expansion of fourth term would also have a component in form of first power of standard normal and both the
above term could be implicitly subtracting from the second term and causing decrease of variance there.

---

### #2577 — Amin (Topic Author)
*December 27, 2024, 8:22 PM*

Friends, a lot of more work needs to be done for a satisfactory model. My strategy for solution of problem is that we
try to match variances of X and X^2 with a proposed model parameters and do some basic analytics to determine the form
of coefficient. We can then try to use that regression based solution as s starting guess for a full fledged Newton
method that tries to calibrate to appropriate number of moments. I also think that we would have to increase the order
of the model and increase the coefficients to at least$c_5 Z^5 $ but we could give dynamics to only$c_1, c_2 , c_3$ or
their subset. I will be working on this for next few days.

Suppose we make a univariate hermite series/Z-Series representation of X using its data and calculate hermite
series/Z-series of$X^2$ from the same data. Then if we find hermite series of$X^2$ from hermite series of X, it will be
slightly different from hermite series of X^2 directly calculated from data. A more true Hermite series of X would be
where we could use this hermite series of X to find hermite series of$X^2$ and this analytically found hermite series of
$X^2$ matches with directly calulated Z-series of$X^2$ directly found from data.

---

### #2578 — Amin (Topic Author)
*December 28, 2024, 12:15 PM*

Friends, I am having some more clarity about how to approach for a good numerical solution to our problem stated in past
few posts.

I think it would be interesting to give dynamics to some coefficients of a hermite series/Z-Series and then find
coefficients of$X^2, X^3, X^4$ in terms of the model coefficients of Z-Series of X. We can then numerically find out the
values of coefficients of$X^2, X^3, X^4$ and match numerical values of coefficients of$X^2, X^3, X^4$ with analytic
algebraic formula values in terms of model coefficients of Z-Series of$X$ .

This is an over-determined problem and we would have 50-60 algebraic equations for only ten or so unknown coefficients.
I want to solve the problem with iterative least squares/ Newton method. We can get a good initial guess for iterative
method from vanilla one dimensional Z-series of X. I am sure this is a workable problem that can be solved easily with a
bit of effort. I want to write a good program that friends could use for all sort of related problems with their own
model forms of Z-series of X.

But it can take at least a week to finesse everything and we would be in first week of next year when I could upload the
program on Wilmott here.

---

### #2579 — Amin (Topic Author)
*December 29, 2024, 7:22 PM*

Friends, the debate between Elon Musk and many hardliners have been all over the media. And I heard Nikki Haley say,

**"If the tech industry needs workers, invest in our education system. Invest in our American workforce. We must invest
in Americans first before looking elsewhere. Don't ever underestimate the talent of Americans or the American spirit."**

This was very interesting especially coming from a conservative politician. And I have been saying something similar for many years that Americans should invest heavily in great education of their children. To be honest with Americans, Barack obama and Donald Trump are two sides of the same coin. It will be the same old shi# when they are gone. If Americans want a president who is a complete game changer, they need someone like Elizabeth warren. When I was covering candidates for president in 2020, I noticed that only Elizabeth Warren had a very special agenda about education of American children. Read here: https://elizabethwarren.com/plans/public-education . I think this must be one of the most important points in any election in a country but funny that not many people even in American care deeply about what she was saying. And not many politicians consider it important to have a policy about it.

American defense would have people believe that I am very anti-American. Here I want to post what I had written about
education of American children four to eight years ago. Here is what I said several years ago.

#Post Starts#   https://forum.wilmott.com/viewtopic.php?t=94796&start=1080#p857281

I am sure that most people will agree that use of mind control weapons on innocent people is very inhuman. Humans train
our neurotransmitters all our life to do things well, learn new things, show respect and compassion for each other, and
so many other things and this training of neurotransmitters slowly continues all our life as we interact with our
environment. And the result of all our life-long training is written on neurotransmitters. Second thing to consider is:
Though we continue to learn and train our neurotransmitters all our life, some of the most important training of our
neurotransmitters takes place in our childhood when the brain is forming and develops very quickly and the chemical
reactions that take place in our brain in our childhood can never be repeated in our later life and as a result of that
some of the most important neurotransmitters in our brain are set for the rest of our life.

The way mind control agencies work, they disable some of the most important neurotransmitters that are required to
execute most of the chains of chemical reactions that we have learnt as a result of training of our brain in all of our
previous life. Though brain of the victim could continue to learn slowly but a lot of training is lost as a result of
taking some important neurotransmitters out of the brain and some of the chemical reactions that are learnt in our
childhood could never be repeated to give the brain the same degree of fluency to re-train our brain and learn new
things. Most of our brains always require some important neurotransmitters on which we started to train our brain in our
childhood and these neurotransmitters could almost never be substituted once(in a later age) they are taken out of our
brain and any new training on any other neurotransmitters would be very limited. I think most of the civilized people
will surely agree that it is very cruel to use mind control technologies on people so that they lose most of their
life-long training of their neurotransmitters and are forced to live a life with a retarded brain. We teach ourselves to
do good things and take the right decisions and all of these things are saved as training of our neurotransmitters.

Many people have to understand that we are biological machines but we are human because of our consciousness, our
emotions and our feelings. How cruel and wrong is it for someone who trained his neurotransmitters all their life to
respect others and speak nicely of other good people when some of their neurotransmitters that had the most training of
goodness to others would be removed out of the brain and some potent and evil neurotransmitters could be introduced
(that may not even exist in our brain but can combine with other existing neurotransmitters in our brain to move them.
Our brain especially loses even the remaining check and balance when foreign neurotransmitters unknown to our brain are
introduced after taking out major neurotransmitters as keeping balance on foreign neurotransmitters might not have been
learnt in our previous life-long training of neurotransmitters) in the brain to say something offensive of others. I
think such manipulation is extremely wrong and inhuman to people who taught themselves to respect others all their life
and no good society must ever allow such things to happen to individuals who tried to teach themselves to respect others
all their life. There are a very large number of people who complain about such wrong actions by mind control agencies.

**Another thesis some people in America might present to their government and people is that since American mind control
agencies have the best technology regarding mind control, it would help them maintain a greater edge in technology and
sciences by retarding people of other nations. I think this is an extremely wrong approach. United States is a country
with the greatest wealth, most intelligent brains, the best universities and huge natural resources. If the right amount
of wealth is allocated and the best brains are asked to think and chart the future plans for people of United States, it
would always remain the most wealthy country. United States is a very populous country but there are a large number of
states/neighborhoods/counties that have a very poor school education infrastructure. Would it not be good to create a
great early education and schooling infrastructure everywhere in United States to make the country great so that every
child who has the potential to excel in life is never denied good education. Is it not ironic that very places in US
where a large number of people fail to get good early school education, are the ones that complain about foreigners
coming and taking their jobs. I think patriotic people who really care about united states should try to create an
excellent school system everywhere in US if they really care about America. I would ask intelligent people how they
would like to make America a greater country? By allocating some money (several tens of billions of dollars) to defense
that is used to develop non-human technologies used to retard intelligent people. Or by allocating those resources to
excellent education of American children at places in US where children cannot get very good education. It is childhood
when a lot of important things in our personality and character are set forever.

**

#Post Ends#

#Post Starts#    https://forum.wilmott.com/viewtopic.php?t=94796&start=855#p829839

Just developing the idea of yesterday a little bit more. I really think that good universities in every country should
make multidisciplinary groups/teams of researchers that would study all different aspects of the existing education
system in the particular country. Of course, these researchers would come from all different areas relevant to education
of children including the experts related to child education and child psychology that could help develop a framework
for children education methods, experts in education methods in various subjects, experts in school administration,
experts that have studied teacher training and methods that motivate better teachers and how to implement teacher
training and teacher motivation methods in schools, experts in extra-curricular activities and sports and how these
things could be properly introduced in schools, and experts who can evaluate the costs related to development of various
school infrastructure and allied teacher training activities and experts that would develop best possible syllabus and
how to introduce various ideas to children in the best possible ways. And these experts would also work on the costs
associated with developing/improving a national school infrastructure and its impact on economy in terms of greater
economic activity and future benefit to the nations in terms of more talented citizens who would be on the forefront of
science and technology and social sciences. I am sure most of these things are well known to a lot of different experts
and researchers in various education fields but it would be a great idea to put a lot of these experts together to make
a multidisciplinary team that could give recommendations to their national governments or other education bodies
towards  revamping or improving the existing education systems. And really I do consider it important that it should be
a priority of the research groups to work with the goal in mind that the education system should make it as easy as
possible to get an excellent education with minimum burden at least to those children whose parents cannot otherwise
afford good education. And the researching teams should also work out methods of education especially tailored to places
or communities where parents have a poor or uneducated background and how to tackle related complications that arise
when their children go to school. Just like we talk about human rights and similar other ideas, we should also talk
about rights of every child to be able to get a good education despite his/her possibly poor or backward background. And
in places where lack of tolerance and religious radicalism is a problem, society has to make an extra effort to teach
the children in a way to promote respect for different opinions, religions and different lifestyles and learn to
appreciate diversity in people and their ideas. And I want to really mention that basic education is usually not
considered the most prestigious area of research but once good, talented and hard-working researchers in children
education put together comprehensive research work on great education of the children, their impact on society and
contribution to society would be far greater than the impact on society all those researchers in hot and innovative
science research areas and I am very sure that society would acknowledge this contribution and give the right great
respect that researchers in child education actually deserve when they work towards putting together great ideas and
comprehensive plans. And I think that best universities in every country should take the initiative in putting together
cross-disciplinary and inter-university groups that would research on these ideas and every government should generously
support these teams of researchers.

I am writing in the hope that some intelligent people who would like the idea and encourage the right people to work on
it.

**And really for many countries like America where some people do not like so many Chinese, Indian or Pakistani
engineers and many American tech industries leaders complain that we really could not hire enough American engineers,
the right approach should be to give very good education to American children where the standards of educations are
really not at par with the best and then there will be many more younger Americans who would be able to find the jobs in
tech and other science industries. Why would you not prefer educating children in Nebraska or Alabama or so many other
American states. America is really a big and very populous country. Not that I am in any way against foreigners coming
to America, you could still continue to get good talent from other countries. **

#Post Ends#

#Post Starts#     https://forum.wilmott.com/viewtopic.php?t=94796&start=1170#p863050

Today on this first day of 2021, I drove back to Lahore from Islamabad with my mother. And happy new year to all
friends.

And I want to start the new year by making a post against mind control and other excesses by US defense. I am not going
to go into great details and will only briefly outline my arguments and hope that other intelligent American friends
would find some sense and good logic in my brief arguments and do something good for their country America. I have said
on this forum several times that American defense needs intelligent leadership that fixes this bloated, corrupt and
inefficient organization. As I can see the future, I would like to say that if fortunes of America as a country were to
ever decline, US defense would be a major reason behind the decline of this great country.

Before I start my arguments, I would like to make it clear that I have no doubts about the importance of national
security of any country and therefore I would strongly agree with friends who suggest that American needs a strong
professional army that can successfully counter any threat to security of US and its citizens and everything has to be
done to make sure by people of US so that professional US army has readiness to combat all possible threats.

Total US defense expenditure this year would be roughly 930 billion dollars. https://www.thebalance.com/u-s-military-budget-components-challenges-growth-3306320 I believe there are other hidden categories of defense related significant expenditure not mentioned in the above article.

My thesis has three points.

**1. US defense is a corrupt organization where several hundred billion dollars are stolen every year by incompetent
people. You need a professional and efficient army and not a corrupt army.**

**2. US defense is a bloated and inefficient organization and an intelligent leadership could possibly achieve the same
goals by spending roughly half the money. A few hundred billion dollars freed up could be channeled towards long term
productive categories like improving the school system in United States which would turn out to be hugely productive for
the economy in the longer run. There are a large number of US children who are denied good early stage education and a
large number of foreign skilled workers are hired by US employers because the US school system fails to give proper
education opportunities to all US children so they lag in the university causing a shortfall of skilled labor.**

3. US defense's unconstitutional activities damage the US economy by several hundred billion dollars every year.

As I said at the start, I am not going into great details of this but would like to explain the third part only. I am
sure most intelligent and informed people would agree with point one and two. The agent who controls me has a net worth
very easily exceeding half a billion dollars and everyone in defense is fine with that simply because it is a norm in
defense and not an anomaly. I think second point is self-explanatory as well.

**About the third point, I want to say that US defense has retarded several thousand people of exceptional talent in
United States only because of their hardliner conservative biases, to oblige their rich conservative buddies, and due to
so many other reasons that pseudo-educated, incompetent, corrupt and biased people can have. This is obvious
transgression of the constitution of United States. Military has to be professional and should never be allowed to be
above the law, justice and the constitution. As a citizen of a third world country where military does every wrong thing
possible, I can tell people of United States that barriers to unconstitutional practices by military are only
psychological and once the society starts to condone these unconstitutional practices, these practices  become a norm in
the society and then military has absolutely no hesitation about indulging in unlawful practices. The level of moral
courage required to stop unconstitutional practices by military is probably not very high when these practices are only
starting but once these unconstitutional and unethical practices have taken root in a society, the level of moral
courage required to stop them would be extremely high. For example, Good people in my country are routinely abused and
some even die at hands of Army when they protest against wrong practices by the military here but still no good comes
out of their sacrifices since military has absolutely no psychological barriers against wrongdoings and a large part of
the society now routinely condones their wrong high-handed unconstitutional actions. Again coming towards the topic, I
would like to say again that US military has retarded several thousand people of exceptional talent in United States
over past two decades. Even if just lucky two or three people among the retarded thousands might have become successful
like Bill Gates or Elon Musk by doing something interesting and different, they could have contributed several hundred
billion dollars to US economy. Fools in US military are biting the very same hand that feeds them.**

I wrote the above lines so that I could possibly motivate intelligent and patriotic people to do something good for
their country. Please ask the new president to end mind control of all civilians, and dismantle all mind control
infrastructure to retard civilians from all across the Urban United States. And I want to tell friends that doing the
right thing is always not very easy since there is always a very strong resistance from corrupt people when good people
try to stop their corruption.

#Post Ends#

#Post Starts#   https://forum.wilmott.com/viewtopic.php?t=94796&start=1080#p857349

I want to share a few paragraphs on the same lines with good American friends. I am sure most people will agree that
nations have to optimize all their resources in a very intelligent way to maximize their prosperity and security.
Nations that fail to allocate their limited resources intelligently, have a poor planning about their future, lack the
right talent  or have a bad execution of their plans(due to corruption or incompetence)  fail to become successful. But
as I studied history (Quora or Wikipedia), there were times in history of various nations when it was totally obvious
what steps had to be taken to ensure the prosperity of those particular nations but there were powerful and strong
vested interests in those nations that stopped and thwarted the intelligent and patriotic people from taking the right
steps towards the future of those nations. And throughout the history of mankind, one of the strongest vested interests
are large and powerful armies. When armies start dictating the future course of action of the nations and thwart
patriotic people from taking the right decisions towards the future of their nations, I call it Yeni-Ceri effect.
Yeni-Ceri were army corps of the Ottoman empire and were instrumental towards the rise and supremacy of the Ottoman
empire. But when the empire was at its zenith and Yeni-Ceri were conquering foreign lands, decision making was in the
hands of strong Ottoman kings. However Yeni-Ceri continued to gain power and influence in every sphere of the society
and reduced the Ottoman kings and other patriotic people in nobility to mere puppets. Europe was changing very fast and
several Ottoman kings bitterly wanted to introduce reforms in their empire, but Yeni-ceri were strongly opposed to any
idea that would decrease their power. When some Ottoman kings tried harder to introduce reforms in their country,
Yeni-Ceri deposed and paraded some of them on streets of Istanbul. And when Yeni-Ceri were abolished a hundred years
after the zenith of the empire, Ottoman empire had completely lost any superiority it had on other countries and always
remained a very weak power. In today's civilized times, nations do not want to conquer other lands and all the criteria
of superiority and prosperity of nations have completely changed and civilized nations want to look inward to create
progress for their people but the Yeni-Ceri effect still remains strong in several countries. If we add all the hidden
and official resources allocated to US defense, the total allocation exceeds one trillion dollars. Can people in
Pentagon ever allow intelligent people in United States to allocate 150-250 billion dollars out of the non-productive
defense category towards more productive categories of expenditure required to maintain greater prosperity of American
people. Of course terrorism is a very great threat to security of American society. But I do not believe that 9/11 had
to do anything with lack of resources allocated to US defense. It was more due to incompetence of people in Us defense.
Militaries in most of the Muslim countries are extremely cooperative of all legal or illegal demands of American
defense. Somebody could say that there are areas in the world with unrest where terrorism breeds and can cause a threat
to American people. But in those extremely  poor areas with unrest, you do not need huge sums of money since even a
single billion dollar spent on those areas to ensure the security and interests of American people can cause large
inflation in those poor areas with unrest. To fight terrorism effectively, you do not need several hundred billion
dollars. Intelligent, competent and properly trained defense people can absolutely control terrorism breeding everywhere
in the world in 40-60 billion dollars if they are not corrupt. I am sure that people in countries like China and Russia
(which might not have military cooperation with US defense) are educated enough to never pose a terrorism threat to US.
I really mean to suggest that any honest attempt by good people in US to optimize their resources towards greater future
of their nation would never go well with people who have vested interests and Yeni-Ceri effect would almost never let it
succeed. Please take it with a grain of salt but I always joke that US defense is a group of thorough mediocres who have
found a great way of making big money.

An intelligent optimization of resources of American people might result in temporary decrease in defense spending but
the result of proper allocation of state budget to productive categories of expenditure will result in a higher defense
spending after 12-15 years.

And I am a very strong proponent of very good early education of children especially because of my own experience. I am
from an extremely backward area of Pakistan. My city, Kot Addu, is located very close to river Indus. Though the town
has developed relatively and there must be some good schools now, it was not the case when I was a child. But there were
some colonies of government employees of irrigation and power departments a few kilometers from Kot Addu town. Employees
in those colonies were more educated (some of them were engineers) and they had a small school for their children since
they were not very happy with education standards in government schools in the town(and there were no private schools in
the town at that time). And this school had a far better education standard at that time and I was able to study English
as a subject from class one. I was very lucky to be able to study in that school. I also recall there were another
friend-family in Kot Addu town whose children also studied with me in the same school for several years and all of them
are doctors and engineers. And one of them actually went to complete his masters in Electrical engineering from a
university in Florida and lives in US.

#Post Ends#

https://forum.wilmott.com/viewtopic.php?t=94796&start=855#p829805

https://forum.wilmott.com/viewtopic.php?t=94796&start=855#p829839

---

### #2580 — Amin (Topic Author)
*January 2, 2025, 7:25 AM*

Friends Welcome to year 2025. We are starting a new circle around our star. Let us try to make this new circle very
special in every way and more so when it comes to our understanding of new mathematics, science and technology. I am
thoroughly committed to try doing interesting research and keep posting my ideas and work on Wilmott. I would love to
make this year far more special in terms of good mathematics research than our last previous years.

We have developed many special mathematical tools in last few years and it is time to improve those tools and put them
to work in terms of every day applications of mathematics. But in order to achieve our high goals, we would have to work
harder and we would have to remain committed to math research. I want to look forward to this new year and hope that I
would be working with renewed enthusiasm, energy and zeal.

I also hope that new Trump administration will patronize our research and end my mind control though we know that there
is enough uncertainty associated with government change on 20th January. Let us hope that things go in our favor and
there is no negative surprise.

Coming back to our ongoing research, I have done the derivative calculations of the automated program and will be
implementing Newton in sense of iterative least squares and hope to come back with another post within 24 hours
mentioning how it goes. I hope that we would have a working program ready very soon.

Again let us try to make this new circle around our star as special as we can for ourselves and for each other in every
way possible.

---

### #2581 — Amin (Topic Author)
*January 3, 2025, 6:54 PM*

Friends, here is the result of my research today. I was able to get my program to work for applying multi-dimensional
Newton Root Search for finding multi-dimensional coefficients backed out from Z-series of  X^2.

I calculated jacobian matrix for multidimensional Newton in the usual way. However instead of original Newton method as
given below

$$X_{n+1}\,=\,X_n\,-\, {J_F(X_n)}^{-1}\,F(X_n) $$

I replaced it with Newton in least square sense

$$X_{n+1}\,=\,X_n\,-\, \left[ \,{J_F(X_n)}^T\,J_F(X_n)\right]^{-1}\,{J_F(X_n)}^T\,F(X_n) $$

but it was still not working since there were zeros on some diagonal entries and I changed the matrix inversion to as in
ridge regression as given below

$$X_{n+1}\,=\,X_n\,-\, \left[ \,{J_F(X_n)}^T\,J_F(X_n) \, + \alpha I \right]^{-1}\,{J_F(X_n)}^T\,F(X_n) $$

and then it started to converge when I applied it to calibrate it to Z-series of $X^2$.

I still have to add the code for calibration to$X^3$ and$X^4$ as I had originally intended but I am sure that it will
only make the problem solution more robust. I have already written the routine to calculate derivatives of the extended
program so I am sure that I will have a working program ready by the end of weekend that I would post on Monday.

---

### #2582 — Amin (Topic Author)
*January 7, 2025, 2:43 PM*

Friends, I made a post yesterday but it had serious errors so I deleted it. I will come back with corrected version of
that post in another two or three days since the main idea (remains valid) of calculating variance at multiple scales
and then comparing them with each other would give us information about level of mean reversion. I would come back to it
soon.

However, for past few weeks, the focus of my research has been about specifying and estimating the dynamic coefficients
Z-series model. I have tried to estimate the model I specified and it did not seem to work properly as mostly it leads
to non-intuitive parameters found. That led me to question myself what was wring with the model? And I realized that my
specified model was not a proper clustering model as it should be rather I was just giving further variance to
coefficients in a non-informative way. A proper information yielding model should have coefficients slowly evolving and
also mean-reverting so coefficients should rather be auto-regressive with reasonably well defined means or they should
be simple ornstein-uhlenbeck processes. At times of higher activity or lower activity, the coefficients would deviate
away from the mean but later return close to their mean values after a little while. This sort of arrangement for
coefficients seems much more realistic and information yielding as well.

I was rather naiive when I specified the earlier version of the model as earlier version of the model was really not a
moments clustering model. May be it seemed the simplest possible extension and I decided to try it. Good thing is that
most of the infrastructure and ideas I used to estimate the model could be moved to our more sophisticated model more
easily and I hope to see within a few days how the new model goes through the estimation phase.

I also suppose that driving noises, in the ornstein-uhlenbeck form of coefficients evolution, could possibly be
correlated across different coefficients.

I give the form of updated model I want to work with in the next post with Latex equations.

---

### #2583 — Amin (Topic Author)
*January 7, 2025, 3:04 PM*

Dynamic Coefficients Hermite Polynomial Series Models For Time Series Evolution of Random Variables

 In this brief note we want to discuss hermite polynomial series representation of random variables where coefficients
of hermite polynomials are also represented by another hermite polynomial series for each coefficient.

We give some example of some practical dynamic hermite series coefficients models below

$
$\, X \,=\, a_{0}(t)\, + \, \, a_{1}(t)\, \, Z\, + \, \, a_{2}(t)\,\, \left( Z^2\,-\,1\,\right) + \, \, a_{3}(t)\, \, \left( Z^3\,-\,3 \,Z\,\right)    $
$

where

$$\, a_{0}(t)\, =\, \kappa_1\, \left(a_{00} \,-\,a_{0}(t-1)\, \right)\,+\, \sigma_0 \,Z_0$$

$$\, a_{1}(t)\, =\, \kappa_2\,\left(a_{10} \,-\,a_{1}(t-1)\, \right)\,+\, \sigma_1 \,Z_1$$

$$\, a_{2}(t)\, =\, \kappa_3\,\left(a_{20} \,-\,a_{2}(t-1)\, \right)\,+\, \sigma_2 \,Z_2$$

$$\, a_{3}(t)\, =\, \kappa_4\,\left(a_{30} \,-\,a_{3}(t-1)\, \right)\,+\, \sigma_3 \,Z_3$$

We have specified dynamics to coefficients of only first four polynomials in the Z-series but coefficients with dynamics
may increase or decrease as we learn from the data. All of these$Z_0\, \,Z_1, \, Z_2,\,Z_3 $ could possibly be
positively or negatively correlated with each other but could also be correlated with
$\bar{Z}_0\, \,\bar{Z}_1, \, \bar{Z}_2,\, \bar{Z}_3 $ which are noises in dynamic coefficients of hermite series of
another random variable.

I will come back with a post on estimation after a day or two of experimentation with estimation models. The above model
is definitely more complex than the previous model but I really think if we can harness it, this will be very useful in
a large number of applications and I want to devote some good time and energy to be able to calibrate this model.

---

### #2584 — Amin (Topic Author)
*January 7, 2025, 7:11 PM*

Estimation Strategy For Dynamic Coefficients Hermite Polynomial Series Models For Time Series Evolution of Random
Variables

As we understand, the estimation of a dynamic coefficients model is not possible without specifying variability in
moments. However many (single statistic of) moments we may specify, it will always give us a time homogenous
static/stationary distribution with more precision therefore dynamic coefficients model estimation could only be
possible if we can capture the systematic variability in moments of the time series.

With this understanding, we can specify a simple estimation methodology in which we have a sliding window in time and we
re-estimate moments of a time series (or innovations of this time series) with each sliding movement of this window. And
also estimate the coefficients of the accompanying Z-series/Hermite series. We can then map the time series of
coefficients of Z-series on simple Ornstein-Uhlenbeck like autoregressive processes. Since all coefficients are found in
the same order in time, we can also find correlations among driving noises of different auto-regressive equation of
coefficients across one time series and across various different time series of coefficients of different random
variables.

Any sliding window method could give rise to correlations due to overlap of data so we would have to understand what are
correlations due to overlapping data and what are true correlations after accounting for the overlap of the data in the
sliding window.

We would also like to estimate dynamics of daily changes in the random variables in the financial markets from the most
recent intra-day data of the market.

I have this simple idea that we could estimate a set of moments$M_1$ over N intervals first, and then calculate another
related set of moments$M_2$ over$\text{N+1}$ intervals and then we might be able to retrieve pure moments associated
with$\text{(N+1)th}$ interval using moments calculus over set of moments$M_1$ and$M_2$ but this is just a rudimentary
idea and I need to see if it can work. If it does work, we can possibly find Z-series associated with$\text{(N+1)th}$
interval directly from moments of$\text{(N+1)th}$ interval but we might need some regularization and there might be some
other caveats and I can only be sure if this idea works well in practice.

With the above simple methodology, we aim to estimate dynamic coefficients Z-series of various variables in the
financial markets. I will come up with simple matlab programs in a few days.

---

### #2585 — Amin (Topic Author)
*January 9, 2025, 8:09 PM*

Friends, I went ahead and produced simulation data from a stochastic volatility based asset SDE and calculated Z-series
up to third power (fitting first four moments) and produced a time series of coefficients of this Z-series (of dX(t) )
updated at every simulation interval. I am showing overlaid graphs for this X(t) and also of the four parameters of the
Z-series. Graphs are here and I will make a new post to attach the matlab code used to produce these graphs. This is
still an initial program and will see a lot of changes but I am copying it in next post.

These graphs are from a random simulation and I expect that real data will be more interesting since it would be a mix
of randomness and systematic patterns(that we want to find). However, even these graphs can be interesting since a
different SDE  (negatively correlated with asset) is used to generate volatility so there should be quite a bit of
volatility clustering and skew.

.

.

.

[![Image](../images/i.postimg.cc/T1QXx6cg/Time-Series01.png)](https://postimg.cc/30yqjzVx)

[![Image](../images/i.postimg.cc/0j9qhQ79/Time-Series02.png)](https://postimg.cc/DJpDX7CN)

[![Image](../images/i.postimg.cc/W3Gv9rF9/Time-Series03.png)](https://postimg.cc/8Jz9c7bW)

---

### #2586 — Amin (Topic Author)
*January 9, 2025, 8:25 PM*

.

.

.

.

```
function [] = SlidingWindowZSeriesEstimation()

TT=500;
seed=15898837;

[X1] = ProduceSDEDataTimeSeries(TT,seed);

NIntervals=15;  %Intervals used to estimate moments

plot((1:TT),X1(1:TT),'g');
str=input("Look at graph of Time Series variable X");

for tt=(1+NIntervals):TT
    muA(1:4)=0;
    for nn=1:NIntervals
        dXt=X1(tt-NIntervals+nn)-X1(tt-NIntervals+nn-1); %Moments are calculated for dX(t)
        muA(1:4)=muA(1:4)+(dXt.^(1:4))/NIntervals;
    end

    [c(1,tt),c(2:4,tt),FittedMoments] = CalculateZSeriesDensityFromRawMoments02M4(muA,0);

    c
    %str=input("Look at new Coeffs");

end

c
clf;
yyaxis left
plot((1:TT),X1(1:TT),'g')
ylabel('Random Variable X')
xlabel('Time Intervals')
yyaxis right
plot((1+NIntervals:TT),c(1,1+NIntervals:TT),'b');

hold on
yyaxis right
plot((1+NIntervals:TT),c(2,1+NIntervals:TT),'r');
ylabel('Coefficients c0 and c1 of Z-series of X')

title("Graph of time series X and first two Coefficients of its Z-series, c0 and c1");
legend('X','c0','c1','Location','northeast');
%plot((1:TT),X1(1:TT),'g',(1+NIntervals:TT),c(1,1+NIntervals:TT),'b',(1+NIntervals:TT),c(2,1+NIntervals:TT),'r',(1+NIntervals:TT),c(3,1+NIntervals:TT),'k',(1+NIntervals:TT),c(4,1+NIntervals:TT),'m');
str=input("Look at graph--final");

clf;
yyaxis left
plot((1:TT),X1(1:TT),'g')
ylabel('Random Variable X')
xlabel('Time Intervals')
 hold on
yyaxis right
plot((1+NIntervals:TT),c(3,1+NIntervals:TT),'k');
ylabel('Coefficients c2 of Z-series of X')

title("Graph of time series X and third coefficients of its Z-series, c2");
legend('X','c2','Location','northeast');

str=input("Graph--Fianl--2")

clf;
yyaxis left
plot((1:TT),X1(1:TT),'g')
ylabel('Random Variable X')
xlabel('Time Intervals')
hold on
yyaxis right
plot((1+NIntervals:TT),c(4,1+NIntervals:TT),'m');
ylabel('Coefficients c3 of Z-series of X')

title("Graph of time series X and fourth coefficient of its Z-series, c3");
legend('X','c3','Location','northeast');

end

```

.

.

.

.

```
function [X1] = ProduceSDEDataTimeSeries(TT,seed)

paths=1;

X0=1.0;
alpha1=0;
alpha2=1;
%kappaX=2.0;
%thetaX=.5;
kappaX=0.0;
thetaX=0.0;
a=kappaX*thetaX;
b=-kappaX;
%a=0;
%b=0;
rho=-0.50;
sigma1=.55;
gammaV=.5;
gammaX=.95;
%%%%%%%%%%%%%
V0=1.0;
thetaV=.25;
kappaV=1.0;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.85;
sigma0=.75;
%%%%%%%%%%%%

dt=.03125;
%Tt=32*4;
Tt=TT;

T=Tt*dt;
%paths=100000;

%%%%%%%%%%%%%%%%%%%%%%%%5

%rng(29079137, 'twister')
%rng(15898837, 'twister')
rng(seed, 'twister')
% paths=1000000;
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

    X(X<0)=-X(X<0);

    X1(tt)=X(1);

    V1(tt)=V(1);
%     if(tt==32)
%         X1=X;
%         V1=V;
%     end
%     if(tt==96)
%         X2=X;
%     end

end

end

```

.

.

.

.

.

```
function [c0,c,FittedMoments] = CalculateZSeriesDensityFromRawMoments02M4(rMu,bGuess)
%The above function takes an array of first eight raw moments as input.
%And returns Z-series Coeffs upto 3rd power of Z as
%Y=c0+c(1)*Z+c(2)*Z^2+c(3)*Z^3           %%%%%%+c(4)*Z^4+c(5)*Z^5+c(6)*Z^6+c(7)*Z^7
%Fitted Moments are raw moments of the Z-series density and usually are exactly
%the same as input raw moments rMu(1:4).i.e  FittedMoments(1:4)==rMu(1:4)
%with high precision.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%If you do not have valid moments from a density available, please
%uncomment the following input moments to run the program.

% rMu(1)=0.000012499863483*10^5;
% rMu(2)=0.000021197093700*10^5;
% rMu(3)=0.000050274347857*10^5;
% rMu(4)=0.000171368317209*10^5;
% rMu(5)=0.000856094970826*10^5;
% rMu(6)=0.006320436615909*10^5;
% rMu(7)=0.068698344472325*10^5;
% rMu(8)=1.084082326087001*10^5;

% rMu(1)=0;
% rMu(2)=1;
% rMu(3)=0;
% rMu(4)=105*105;
% rMu(5)=0;
% rMu(6)=(945*11)^2;
% rMu(7)=0;
% rMu(8)=(945*11*13*15).^2;
%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
SeriesOrder=3;    %Z-series till 7th power. hardcoded here cannot chagne.
mOrder=4;         %Number of raw moments in calibration. hardcoded here cannot chagne.
NMoments=mOrder;
                  %Find central Moments from raw moments
[Mu1,cMu] = ConvertRawMomentsToCentralMoments(rMu,mOrder);
                  %Find standardized Moments from central moments
sMu(1)=0;
sMu(2)=1;
sMu(3)=cMu(3)/cMu(2).^1.5;
sMu(4)=cMu(4)/cMu(2).^2.0;
%sMu(5)=cMu(5)/cMu(2).^2.5;
%sMu(6)=cMu(6)/cMu(2).^3.0;
%sMu(7)=cMu(7)/cMu(2).^3.5;
%sMu(8)=cMu(8)/cMu(2).^4.0;

iter=200;           %Number of iterations in the calibration.
                  %Please experiment and play around.
bGuess(2:3)=0;    %We have assigned initial values of coefficients
bGuess(1)=1;      %other than c(1) to zero. We are starting with no prior information.
%[c0,c] = PreSmoothingGuessAdvancedFromGuessBestNew(sMu,bGuess,iter);
[c0,c] = PreSmoothingGuessAdvancedFromGuessBestNewC3(sMu,bGuess,iter);

c0
c

%str=input("Look at pre-smoothing Guess result")

% w(NMoments)=1;
% for nn=NMoments-1:-1:1
%     %w(nn)=w(nn+1)*(nn+1).^2;
%     w(nn)=w(nn+1)*(nn+2).*(nn+3);
% end
%
%
%
%
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %Comment this block if you do not want multidimensional Newton pass
% %Even though preSmoothing guess is very close to optimal, slight
% %inaccuracies can change the shape of probabioity density so this
% %Multidimensional Newton is usually required.
%
% [F,dF] = CalculateMomentsAndDerivatives_0(sMu,c0,c,SeriesOrder,SeriesOrder,NMoments);
%
% da(1,1)=c0;
% da(2:SeriesOrder+1,1)=c(1:SeriesOrder);
%
% [Moments] = CalculateMomentsOfZSeries(c0,c,SeriesOrder,NMoments);
%
% %Replace with your own more intelligent objective function if you like.
%
%ObjBest=100000*(abs(sMu(1)-Moments(1)))+abs(sMu(2)-Moments(2))+abs((sMu(3)-Moments(3))^(1/1.5))+abs((sMu(4)-Moments(4))^(1/2.0))
+ ...
% %    abs((sMu(5)-Moments(5))^(1/2.0))+abs((sMu(6)-Moments(6))^(1/2.0))+abs((sMu(7)-Moments(7))^(1/2.0))+ ...
% %    abs((sMu(8)-Moments(8))^(1/2.0));
%
% [ObjBest] = CalculateObjMoment(sMu,Moments,w,mOrder);
%
%
%
% b0Best=c0;
% bBest(1:SeriesOrder)=c(1:SeriesOrder);
%
% nn=0;
% while((nn.000000000001) || (abs(F(2,1))>.000000000001) || (abs(F(3,1))>.000000000001) || (abs(F(4,1))>.00000000001) 
))
%
%     nn=nn+1;
%     %Below Newton matrix equation to improve the Z-series coefficients guess at previous step.
%     da=da-dF\F;
%
%     %b0=median
%     b0=da(1,1);
%     b(1:SeriesOrder)=da(2:SeriesOrder+1,1);
%
%     %[F,dF] = CalculateCumulantsAndDerivativesFromMoments_0(C,b0,b,SeriesOrder,SeriesOrder,NoOfCumulants);
%     [F,dF] = CalculateMomentsAndDerivatives_0(sMu,b0,b,SeriesOrder,SeriesOrder,NMoments);
%     %[IsValidFlag] = CheckIsValidDensity(b0,b);
%     [Moments] = CalculateMomentsOfZSeries(b0,b,SeriesOrder,NMoments);
%
%   
 %ObjNew=100000*(abs(sMu(1)-Moments(1)))+abs(sMu(2)-Moments(2))+abs((sMu(3)-Moments(3))^(1/1.5))+abs((sMu(4)-Moments(4))^(1/2.0))
+ ...
%     %abs((sMu(5)-Moments(5))^(1/2.0))+abs((sMu(6)-Moments(6))^(1/2.0))+abs((sMu(7)-Moments(7))^(1/2.0))+ ...
%     %abs((sMu(8)-Moments(8))^(1/2.0));
%
%
%     [ObjNew] = CalculateObjMoment(sMu,Moments,w,mOrder);
%
%     IsValidFlag=1;
%     if((ObjBest>ObjNew) &&( IsValidFlag))
%
%        ObjBest=ObjNew;
%        b0Best=b0;
%        bBest(1:SeriesOrder)=b(1:SeriesOrder);
%     end
%
%     da(1,1)=b0;
%     da(2:SeriesOrder+1,1)=b(1:SeriesOrder);
%
% end
% c0=b0Best;%Best;
% c(1:SeriesOrder)=bBest;%Best(1:SeriesOrder);
%
% %Above are the best chosen Z-series coefficients based on the objective function.
% %But my objective function can be improved.
%
% %Multidimensional Newton root search ends. Comment till here if you like to
% %exclude this
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

c0
c

%str=input("Look at standardized output coefficients");

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
MaxIter=20;

for nn=1:iter     %increase the iterations over coefficients if neeeded

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[M3,dc2] = CalculateParticularMomentAndDerivativeOfItsCoeff(c0,c,SeriesOrder,3,EZ);

tolerance=.00000001*cmu(3);
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

---

### #2587 — Amin (Topic Author)
*January 10, 2025, 4:17 PM*

Friends, we had earlier tentatively decided the form of our dynamic coefficients Z-series model as

We give some example of some practical dynamic hermite series coefficients models below

$
$\, X \,=\, a_{0}(t)\, + \, \, a_{1}(t)\, \, Z\, + \, \, a_{2}(t)\,\, \left( Z^2\,-\,1\,\right) + \, \, a_{3}(t)\, \, \left( Z^3\,-\,3 \,Z\,\right)    $
$

where

$$\, a_{0}(t)\,| \,a_{0}(t-1) \, =\, \kappa_1\, \left(a_{00} \,-\,a_{0}(t-1)\, \right)\,+\, \sigma_0 \,Z_0$$

$$\, a_{1}(t)\,| \,a_{1}(t-1) \,  =\, \kappa_2\,\left(a_{10} \,-\,a_{1}(t-1)\, \right)\,+\, \sigma_1 \,Z_1$$

$$\, a_{2}(t)\,| \,a_{2}(t-1) \,  =\, \kappa_3\,\left(a_{20} \,-\,a_{2}(t-1)\, \right)\,+\, \sigma_2 \,Z_2$$

$$\, a_{3}(t)\,| \,a_{3}(t-1) \,  =\, \kappa_4\,\left(a_{30} \,-\,a_{3}(t-1)\, \right)\,+\, \sigma_3 \,Z_3$$

However, since we would like to use our model in a lot of advanced applications where we might need even more precise
analytics so I suggest that we have a general form of transition dynamics of all of parameters as

$$\, \Delta \theta_t \,=\, \theta_t\,- \,\theta_{t-1} \, =\, g(\theta_{t-1}) \,+\,f(\theta_{t-1}) \,Z_{\theta}$$

We can easily find the distribution of$\theta$ and$\Delta \theta_t \,$ from the time series of theta as we calculated
yesterday and expand the above equation around median$\theta_0$ of the distribution of$\theta$ as

$$\, \Delta \theta_t \,=\, \theta_t\,- \,\theta_{t-1} \, =\, g(\theta_{t-1}) \,+\,f(\theta_{t-1}) \,Z_{\theta}$$

or more explicitly

$$\, \Delta \theta_{t_n} \,=\, g(\theta_0) \, + \, g'(\theta_0) \,(\theta_{t_{n-1}}\,-\, \theta_0)+ .5 \, g''(\theta_0)
\,{(\theta_{t_{n-1}}\,-\, \theta_0)}^2\, + \\\, \left[ \, f(\theta_0) \, + \, f'(\theta_0) \,(\theta_{t_{n-1}}\,-\,
\theta_0)+ .5 \, f''(\theta_0) \,{(\theta_{t_{n-1}}\,-\, \theta_0)}^2\,\right] \, Z_{\theta}\ \\

\,=\, g_0 \, + \, g_1 \,(\theta_{t_{n-1}}\,-\, \theta_0)+ .5 \, g_2 \,{(\theta_{t_{n-1}}\,-\, \theta_0)}^2\,+\, \left[
\, f_0 \, + \, f_1 \,(\theta_{t_{n-1}}\,-\, \theta_0)+ .5 \, f_2 \,{(\theta_{t_{n-1}}\,-\, \theta_0)}^2\,\right] \,
Z_{\theta}$$

In the above equation$\theta_0$ is median of distribution of$\theta$ and can be found by choosing the middle element in
sorted values of$\theta_t$ .

We can find the above equation of transition of dynamic coefficients$\theta_{t_n}$ by calculating moments of
$\Delta \theta_{t}$ as

$$\, \mu_k\,=\,\frac{1}{N}\, \sum\limits_{n=1}^{N}\, {\left[\Delta \theta_{t_n} \right]}^k $$

We have to find six values of transition parameters$g_0,\,g_1,\,g_2,\,f_0,\,f_1,\,f_2$ so that for six moments
calculated above and given by$\mu_k\,$ of index k as$k\,=\,1,\,2,\,\ldots,6$ , the equation below holds (We solve six
moment equations to find six parameters given by$g_0,\,g_1,\,g_2,\,f_0,\,f_1,\,f_2$

$
$\, \mu_k\,=\,\frac{1}{N}\, \sum\limits_{n=1}^{N}\, {\left[\, g_0 \, + \, g_1 \,(\theta_{t_{n-1}}\,-\, \theta_0)+ .5 \, g_2 \,{(\theta_{t_{n-1}}\,-\, \theta_0)}^2\,+\, \left[ \, f_0 \, + \, f_1 \,(\theta_{t_{n-1}}\,-\, \theta_0)+ .5 \, f_2 \,{(\theta_{t_{n-1}}\,-\, \theta_0)}^2\,\right] \, Z_{\theta} \right]}^k $
$

This way we can fit the more general model to data of dynamic coefficients. Our ornstein-uhlenbeck type earlier model is
also nested by and is a special case of this more general model. We will not be changing the above parameters of dynamic
coefficients quickly and they would slowly change only after quite a bit of time. Especially if these parameters of
dynamic coefficients also have to change, we will have to deal with a very long time series and make sure by applying
the strategy of changing the parameters slowly along the long time series and see that results are optimal given the
quantitative policy of changing the parameters. Meaning that any policy of slow change in parameters of dynamic
coefficients has to be first validated by applying it to a long original time series and after seeing that results of
the policy are actually optimal.

---

### #2588 — Amin (Topic Author)
*January 12, 2025, 8:01 AM*

Friends, I hope that my matlab program for optimization of parameters of Z-series dynamic coefficients as described in
previous post would be ready by Tuesday. However, in this post, I am making a slight digression from the topic at hand.

As I had previously mentioned that we want to move from black box AI methods to perfectly mathematical methods of Math
AI. So this post is a continuation towards promoting perfectly understandable mathematical methods.

MATH AI Analytics: Applying a Function on a Different Function (Composition of Functions) To Follow a Third Target
Function.

Ok, coming towards the topic. Here is our setting. We have a function at hand denoted as$F(X)$ and we have a target
function denoted as$G(X)$ . We suppose both of$F(X)$ and$G(X)$ are known to us or we can possibly calculate them easily
by other methods. We want to apply a function$V(.)$ on$F(X)$ so that it starts to perfectly follow the target function
$G(X)$ . We also suppose that functions are smooth and continuous and their derivatives of all orders of interest exist
and can also be measured for both$F(X)$ and$G(X)$ .

We have to find the function V(.) so that the composition of functions equation below is perfectly satisfied.

$$V(F(X))\,=\,G(X)$$

Our strategy is simple, We apply Taylor series in X on both sides of the above equation and equate equation of each
derivative on both sides separately. This way we can find all derivatives of$V(.)$ of various orders of interest and be
able to reconstruct required function$V(.)$ to take$F(X)$ to target function$G(X)$ from its derivatives.

We expand $G(X)$ as a Taylor series as

$
$G(X)\,=\,G(\text{X0}) \,+(X-\text{X0}) G'(\text{X0})\, + \frac{1}{2} (X-\text{X0})^2 G''(\text{X0})\,+\frac{1}{6} G^{(3)}(\text{X0}) (X-\text{X0})^3 \,\\+ \frac{1}{24} G^{(4)}(\text{X0}) (X-\text{X0})^4+O\left((X-\text{X0})^5\right)$
$

We also expand the composition of $V(.)$ and $F(.)$ as a Taylor series as

$
$V(F(X))\,=\, V(F(\text{X0}))+(X-\text{X0}) F'(\text{X0}) V'(F(\text{X0}))+\frac{1}{2} (X-\text{X0})^2 \left(F''(\text{X0}) V'(F(\text{X0}))+F'(\text{X0})^2 V''(F(\text{X0}))\right)\\+\frac{1}{6} (X-\text{X0})^3 \left(F^{(3)}(\text{X0}) V'(F(\text{X0}))+V^{(3)}(F(\text{X0})) F'(\text{X0})^3+3 F'(\text{X0}) F''(\text{X0}) V''(F(\text{X0}))\right)\\+\frac{1}{24} (X-\text{X0})^4 \left(F^{(4)}(\text{X0}) V'(F(\text{X0}))+3 F''(\text{X0})^2 V''(F(\text{X0}))+V^{(4)}(F(\text{X0})) F'(\text{X0})^4 \\+4 F^{(3)}(\text{X0}) F'(\text{X0}) V''(F(\text{X0}))+6 V^{(3)}(F(\text{X0})) F'(\text{X0})^2 F''(\text{X0})\right)+O\left((X-\text{X0})^5\right)$
$

Matching powers of$(X-\text{X0})$ on both sides of equation, we get the following equations that we solve one by one as

$$\,G(\text{X0}) \,=\,V(F(\text{X0}))$$

$$(X-\text{X0}) G'(\text{X0})\,=\,(X-\text{X0}) F'(\text{X0}) V'(F(\text{X0}))$$ From where it follows

$$ V'(F(\text{X0}))\,=\, \frac{G'(\text{X0})\,}{\, F'(\text{X0})} $$

Matching 2nd power of  $(X-\text{X0})^2$, we get

$
$\frac{1}{2} (X-\text{X0})^2 G''(\text{X0})\,=\,\frac{1}{2} (X-\text{X0})^2 \left(F''(\text{X0}) V'(F(\text{X0}))+F'(\text{X0})^2 V''(F(\text{X0}))\right)$
$ From where it follows $
$ V''(F(\text{X0}))= \,\frac{G''(\text{X0})\,-\left(F''(\text{X0}) V'(F(\text{X0})) \right) }{F'(\text{X0})^2}$ $

Matching power of  $(X-\text{X0})^3$, we get

$
$\frac{1}{6} G^{(3)}(\text{X0}) (X-\text{X0})^3 \,=\,\frac{1}{6} (X-\text{X0})^3 \left(F^{(3)}(\text{X0}) V'(F(\text{X0}))+V^{(3)}(F(\text{X0})) F'(\text{X0})^3+3 F'(\text{X0}) F''(\text{X0}) V''(F(\text{X0}))\right) $
$ From where it follows  $
$  V^{(3)}(F(\text{X0}))  \,=\,\frac{G^{(3)}(\text{X0})  \,-\, \left(F^{(3)}(\text{X0}) V'(F(\text{X0})) +3 F'(\text{X0}) F''(\text{X0}) V''(F(\text{X0}))\right)} {F'(\text{X0})^3} $
$

Matching power of  $(X-\text{X0})^4$, we get

$
$ \frac{1}{24} G^{(4)}(\text{X0}) (X-\text{X0})^4 \,=\, \frac{1}{24} (X-\text{X0})^4 \left(F^{(4)}(\text{X0}) V'(F(\text{X0}))+3 F''(\text{X0})^2 V''(F(\text{X0}))+V^{(4)}(F(\text{X0})) F'(\text{X0})^4 \\+4 F^{(3)}(\text{X0}) F'(\text{X0}) V''(F(\text{X0}))+6 V^{(3)}(F(\text{X0})) F'(\text{X0})^2 F''(\text{X0})\right)$
$ From where we get

$
$ V^{(4)}(F(\text{X0})) \, =\,\frac{ \left[ G^{(4)}(\text{X0})  \,-\,  \left(F^{(4)}(\text{X0}) V'(F(\text{X0}))+3 F''(\text{X0})^2 V''(F(\text{X0}))+4 F^{(3)}(\text{X0}) F'(\text{X0}) V''(F(\text{X0})) \\+6 V^{(3)}(F(\text{X0})) F'(\text{X0})^2 F''(\text{X0})\right) \right]}{F'(\text{X0})^4} $
$

So this way, we can calculate various different derivatives of$V(.)$ and then reconstruct V(.) from there. Here we list
the above calculated four derivatives of again, if we use the notation$Y=F(X)$ , then we can write, as

$$\, \,V(Y0)=V(F(\text{X0}))\,=\,G(\text{X0})$$

$$ V'(\text{Y0})\,=V'(F(\text{X0}))\,=\, \frac{G'(\text{X0})\,}{\, F'(\text{X0})} $$

$
$ V''(\text{Y0})\,=V''(F(\text{X0}))= \,\frac{G''(\text{X0})\,-\left(F''(\text{X0}) V'(F(\text{X0})) \right) }{F'(\text{X0})^2}$
$

$
$  V^{(3)}(\text{Y0})\,=\,V^{(3)}(F(\text{X0}))  \,=\,\frac{G^{(3)}(\text{X0})  \,-\, \left(F^{(3)}(\text{X0}) V'(F(\text{X0})) +3 F'(\text{X0}) F''(\text{X0}) V''(F(\text{X0}))\right)} {F'(\text{X0})^3} $
$

$
$ V^{(4)}(\text{Y0})\,=\, V^{(4)}(F(\text{X0})) \, =\,\frac{\left[G^{(4)}(\text{X0})  \,-\,  \left(F^{(4)}(\text{X0}) V'(F(\text{X0}))+3 F''(\text{X0})^2 V''(F(\text{X0}))+4 F^{(3)}(\text{X0}) F'(\text{X0}) V''(F(\text{X0}))\\+6 V^{(3)}(F(\text{X0})) F'(\text{X0})^2 F''(\text{X0})\right)\right]}{F'(\text{X0})^4} $
$

 And we can write our desired function that we wanted to find out to apply on Y as

$
$V(Y)\,=\,V(\text{Y0}) \,+(Y-\text{Y0}) V'(\text{Y0})\, + \frac{1}{2} (Y-\text{Y0})^2 V''(\text{Y0})\,+\frac{1}{6} V^{(3)}(\text{Y0}) (Y-\text{Y0})^3 \,\\+ \frac{1}{24} V^{(4)}(\text{Y0}) (Y-\text{Y0})^4+O\left((Y-\text{Y0})^5\right)$
$

We will continue to use above analytics in our future applications of Math AI.

---

### #2589 — Amin (Topic Author)
*January 13, 2025, 9:28 AM*

Friends, global warming will continue to increase for quite sometime and as a result more devastating natural calamities
like powerful storms, hurricanes and wildfires would continue to haunt us during for-seeable future. We cannot stop
these natural disasters from happening but with an intelligent and organized human response, we can surely mitigate the
effects of these natural calamities on our societies and decrease human suffering.

For example, taking the case of wildfires, I think it is important that scientists develop models that predict the
evolution path of fires given the weather conditions, wind directions and origin spot of fires given the forest tree
densities that are in place. And a very organized response should already be well-known in advance to Fire department
and other people dealing with natural disasters. It has to be studied where to fight the fires and where to not to make
the best of fire-fighting efforts. Some well thought out engineering of wild-forests might be needed to thin the density
of trees in particular regions/blocks of the forest where most intensive efforts could be made to contain the fires
reaching beyond those regions. And possibly encourage trees that are more resistant to fast spread of wild fires in
these forest blocks. Some crucial fire-fighting infrastructure should already be in place in the blocks where fire has
to be contained and an easy approach from the road should be built to these fire-fighting zones of the forests. and It
has to be particularly made sure that there is a well-studied and comprehensive plan to to save vulnerable large cities
that are close to wild forests and all the fire-fighting staff and administration should all know well in advance what
needs to be done by them to successfully control a fire if it occurs somewhere. All of this could be done at a very
small fraction of the cost as compared to the damage that occurs when fires burn residential areas in suburbs of large
cities.

Even thinking of wildfires that do not threaten suburbs, we have seen a large increase in frequency of wildfires in
recent years. And I really think that in a large number of places, more CO2 is released in the air during the wildfires
than sequestered in rest of the forests and net emission of CO2 and other green house gases from forests due to fires
might be positive which is extremely alarming. I really thing that there has to be very active forest management at a
lot of places without destroying natural habitat of wild animals. If we thin parts of the jungles, the wood used for
housing and many other purposes would sequester CO2 as opposed to large swathes of forests being burnt and pollutants
and greenhouse gases released in atmosphere. I am not an expert at forests and their management but I can suggest for
initial brainstorming that large forests should be divided into blocks (possible square or round or with other possibly
natural boundaries) and border of each block would be approximately several hundred meters wide. In this border,
vegetation and tress would be kept far more thinned and there could be dirt roads in these border areas where
fire-fighting equipment could quickly move. And all sort of common sense fortifications against fire would be developed
in these border areas. There would also be stores at select places on this border area where fire-fighting chemicals and
other equipment could be stored. There could also be many fire-sensors in these areas that would tell about a burning
fire right away. Again the purpose would be to contain the fire in each forest block encircled by the fire-defense
border area with thinner vegetations and robust fire management capabilities. I think that experts can think of a large
number of ideas on similar lines to make sure that a forest fire any where is not allowed to get out of control. Putting
all such infrastructure might not be easy at start but cost of inaction would be far far larger. And once established
with some initial spending, maintaining such a large scale system would become a normal and routine thing.

We just cannot allow huge amounts of CO2 being released in air and lifetime of wealth used to build suburbs simply
evaporate in air with uncontrolled wildfires.

Since wildfires are raging in california, I thought I should say my mind about mitigation of such disasters that cause
large scale human suffering and tragedy. Humanity is special since we learn from our past and once a problem occurs, we
try to make sure that we are well prepared to face it once it happens again.

[Carbon Emissions From Wildfires](https://wfca.com/wildfire-articles/carbon-emissions-from-wildfires/)

---

### #2590 — Amin (Topic Author)
*January 14, 2025, 5:13 PM*

Friends, I was a bit excited by my work on composition of functions and was thinking that it could have possible uses in
mathematics at a lot of places and I kept sort of brainstorming where I could use ideas from my new work. Sorry that
delayed the coding work a little bit by another day but I am very happy that I took some more time to reflect upon the
previous problem some more and I was able to modify my estimation strategy for estimation of parameters of coefficients
and make the estimation strategy more simple and more robust. I will also be using composition of functions in this
modified strategy. Here I am writing the following post to explain the modified strategy. As it is easier, I hope that I
could have my matlab implementation ready in another day.

Dynamic Coefficients Z-series Model and its Estimation

Among other possible variants, one form of practical dynamic hermite series coefficients models is given below

$
$\, X \,=\, a_{0}(t)\, + \, \, a_{1}(t)\, \, Z\, + \, \, a_{2}(t)\,\, \left( Z^2\,-\,1\,\right) + \, \, a_{3}(t)\, \, \left( Z^3\,-\,3 \,Z\,\right)    $
$

where

$$\, a_{0}(t)\,| \,a_{0}(t-1) \, =\, \kappa_1\, \left(a_{00} \,-\,a_{0}(t-1)\, \right)\,+\, \sigma_0 \,Z_0$$

$$\, a_{1}(t)\,| \,a_{1}(t-1) \,  =\, \kappa_2\,\left(a_{10} \,-\,a_{1}(t-1)\, \right)\,+\, \sigma_1 \,Z_1$$

$$\, a_{2}(t)\,| \,a_{2}(t-1) \,  =\, \kappa_3\,\left(a_{20} \,-\,a_{2}(t-1)\, \right)\,+\, \sigma_2 \,Z_2$$

$$\, a_{3}(t)\,| \,a_{3}(t-1) \,  =\, \kappa_4\,\left(a_{30} \,-\,a_{3}(t-1)\, \right)\,+\, \sigma_3 \,Z_3$$

we have a general form of transition dynamics of all of parameters as

$$\, \Delta \theta_t \,=\, \theta_t\,- \,\theta_{t-1} \, =\, g(\theta_{t-1}) \,+\,f(\theta_{t-1}) \,Z_{\theta}$$

We can easily find the distribution of$\theta$ and$\Delta \theta_t \,$ from the time series of theta as we calculated
earlier.

We can write Z-series representation of theta as

$$\theta(Z_{\theta}) \,=\, b_0 \, + \, b_1\,{Z_{\theta}}\,+\,b_2  \,{Z_{\theta}}^2\,+\,b_3\,{Z_{\theta}}^3$$

and we can also write unconditional Z-series representation of  $\Delta \theta \,$

$
$\Delta\theta(Z_{\Delta\theta}) \,=\, c_0 \, + \, c_1\,{Z_{\Delta\theta}}\,+\,c_2  \,{Z_{\Delta\theta}}^2\,+\,c_3\,{Z_{\Delta\theta}}^3$
$

The above two equations would be used to find correlations and later to find conditional expectations of
$E\left[\Delta\theta_t \,|\, \theta_{t-1} \right]$

But at the same time, we suppose that conditional (on one period earlier interval start value of$\theta$ ) transition
model form of distribution of$\Delta\theta $ could be given as where we have divided$ \Delta \theta_t$ into two parts,
the first part that is perfectly correlated with$\theta_{t-1}$ and the second part that is orthogonal (but not
necessarily independent of$\theta_{t-1}$ or

$$\, \Delta \theta_t \,=\, \theta_t\,- \,\theta_{t-1} \, =\, E\left[\Delta\theta_t \,|\, \theta_{t-1} \right] \,+\,
\bar{ \Delta \theta_t } \\

=\, g(\theta_{t-1}) \,+\,f(\theta_{t-1}) \,Z_{\bar{\Delta\theta}} $$

We want to notice that first drift part$g(\theta_{t-1})$ is perfectly correlated wtih$\theta_{t-1}$ while
$f(\theta_{t-1})$ in noise part also depends on$\theta_{t-1}$ but the whole second term above is orthogonal to
$\theta_{t-1}$ .

We can write the form of Z-series of$g(\theta)$ and$f(\theta)$ , since they are one-dimensional functions of$\theta$ ,
as

$$\tilde{g}(Z_{\theta}) \,=\, d_0 \, + \, d_1\,{Z_{\theta}}\,+\,d_2  \,{Z_{\theta}}^2\,+\,d_3\,{Z_{\theta}}^3$$

$$\tilde{f}(Z_{\theta}) \,=\, e_0 \, + \, e_1\,{Z_{\theta}}\,+\,e_2  \,{Z_{\theta}}^2\,+\,e_3\,{Z_{\theta}}^3$$

Which means that our conditional (on one period earlier interval start value of$\theta$ ) transition model form of
distribution of$\Delta\theta$ now becomes.

$$\, \Delta \theta_t \,=\, \theta_t\,- \,\theta_{t-1} \, =\, E\left[\Delta\theta_t \,|\, \theta_{t-1} \right] \,+\,
\bar{ \Delta \theta_t } \\

=\, g(\theta_{t-1}) \,+\,f(\theta_{t-1}) \,Z_{\bar{\Delta\theta}} \\

=\,\left[\, d_0 \, + \, d_1\,{Z_{\theta}}\,+\,d_2 \,{Z_{\theta}}^2\,+\,d_3\,{Z_{\theta}}^3\right]\,+\,\left[ \, e_0 \, +
\, e_1\,{Z_{\theta}}\,+\,e_2 \,{Z_{\theta}}^2\,+\,e_3\,{Z_{\theta}}^3\right] Z_{\bar{\Delta\theta}}$$

We can directly calculate$ g({\theta}) \,=\, E\left[\Delta\theta_t \,|\, \theta_{t-1} \right]$ using conditional
expectation as given in reference below and then

 $$\bar{\Delta\theta_t} \,=\, \Delta\theta_t\, -\, E\left[\Delta\theta_t| \,\theta_{t-1} \right] \,$$

For the above equation to hold, We apply this equation on data observations of$\Delta \theta_t$ with t-th observation
pair given as$\Delta\theta_{t}$ and$\theta_{t-1}$ . We first invert Hermite-Series equation of$\theta_t$ to find
$Z_{\theta_t}$ and then use the following equation for each t-th observation (For details see my reference paper on
Z-series below)

\begin{equation}\label{4.4.3}

 \bar{\Delta\theta_t} \,=  \, \Delta\theta_t\,-\,-\, E\left[\Delta\theta_t| \,\theta_{t-1} \right] \,\\

\,=  \, \Delta\theta_t\,-\,\left[ \, d_0 \, + \, d_1\,{Z_{\theta}}\,+\,d_2 
\,{Z_{\theta}}^2\,+\,d_3\,{Z_{\theta}}^3\right]

\end{equation}

This way we get data values of$\bar{\Delta\theta_t} \,$ which is the orthogonal (but not independent) part of the model
equation where we want to estimate the remaining part of model as

$$\,  \bar{ \Delta \theta_t } =\,\, f(\theta_{t-1}) \,Z_{\bar{\Delta\theta}} \\

=\,\,\left[ \, e_0 \, + \, e_1\,{Z_{\theta}}\,+\,e_2 \,{Z_{\theta}}^2\,+\,e_3\,{Z_{\theta}}^3\right]
Z_{\bar{\Delta\theta}}$$

We can estimate the above equation by calculating moments of $\bar{\Delta \theta}_{t}$  as

$$\, \mu_k\,=\,\frac{1}{N}\, \sum\limits_{n=1}^{N}\, {\left[\bar{\Delta \theta}_{t_n} \right]}^k $$

In order to estimate the above equation, we will have to first back out$Z_{\theta_{t_n}}$ associated with t-th
observation of$\theta_{t_n}$ and then use the equation

$
$\, \mu_k\,=\,\frac{1}{N}\, \sum\limits_{n=1}^{N}\, {\left[ \left(\, e_0 \, + \, e_1 \, Z_{\theta_{t_{n-1}}}\,+ \,e_2 \,{\, Z_{\theta_{t_{n-1}}}\,}^2\,\right)\, Z_{\bar{\Delta\theta}} \right]}^k $
$

The values$\mu_k$ on RHS of above equation are moments that have been calculated from the data of
$\bar{\Delta\theta_t} \,$ , and we have to estimate$(e_0,\, e_1,\, e_2)$ by matching the moments to RHS values.

or more explicitly we can convert above drift and noise Z-series into a Taylor series in parameters$\theta_t$ to find
the true solution in original variables. We will have to use our inverse function composition to find coefficients of
Taylor series below

$$\, \Delta \theta_{t_n} \,=\, g(\theta_0) \, + \, g'(\theta_0) \,(\theta_{t_{n-1}}\,-\, \theta_0)+ .5 \, g''(\theta_0)
\,{(\theta_{t_{n-1}}\,-\, \theta_0)}^2\, + \\\, \left[ \, f(\theta_0) \, + \, f'(\theta_0) \,(\theta_{t_{n-1}}\,-\,
\theta_0)+ .5 \, f''(\theta_0) \,{(\theta_{t_{n-1}}\,-\, \theta_0)}^2\,\right] \, Z_{\theta}\ \\

\,=\, g_0 \, + \, g_1 \,(\theta_{t_{n-1}}\,-\, \theta_0)+ .5 \, g_2 \,{(\theta_{t_{n-1}}\,-\, \theta_0)}^2\,+\, \left[
\, f_0 \, + \, f_1 \,(\theta_{t_{n-1}}\,-\, \theta_0)+ .5 \, f_2 \,{(\theta_{t_{n-1}}\,-\, \theta_0)}^2\,\right] \,
Z_{\theta}$$

In the above equation$\theta_0$ is median of distribution of$\theta$ and can be found by choosing the middle element in
sorted values of$\theta_t$ .

This way we can fit the more general model to data of dynamic coefficients. Our ornstein-uhlenbeck type earlier model is
also nested by and is a special case of this more general model. We will not be changing the above parameters of dynamic
coefficients quickly and they would slowly change only after quite a bit of time. Especially if these parameters of
dynamic coefficients also have to change, we will have to deal with a very long time series and make sure by applying
the strategy of changing the parameters slowly along the long time series and see that results are optimal given the
quantitative policy of changing the parameters. Meaning that any policy of slow change in parameters of dynamic
coefficients has to be first validated by applying it to a long original time series and after seeing that results of
the policy are actually optimal.

Following is the reference to my paper followed by relevant excerpts from the paper.

Reference:  https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4933283

\subsection{Conditional Expectation of a Non-Gaussian Random variable Y given Another Correlated Non-Gaussian Random
variable X}

\label{sec4.3}

In this section, we describe conditional expectation of a non-Gaussian random variable Y given the value of another
correlated non-Gaussian random variable X. Orthogonality property of Hermite polynomials and decomposition of variance
into orthogonal parts means that conditional expectation of a random variable Y with respect to other random variables X
can be divided into separate covariance/correlation based relationships between Hermite polynomials of the same order of
random variables X and Y . Further implying that the total conditional expectation of a random variable Y based on
another correlated random variable X can be described by sum of separate conditional expectations of each Hermite
polynomial of random variable Y with respect to Hermite polynomials of the same order of the random variable X .

The conditional expectation of nth Hermite polynomial based term (with coefficient$ch_n$ ) of the random variable Y
given nth polynomial term of X is calculated in terms of covariance$Cov_{XY,n}$ between nth polynomials of both random
variables X and Y and variance$Var_{X,n}$ of the nth Hermite polynomial of explanatory variable X as

\begin{equation}\label{4.3.1}

E[Y_n\,|\, X_n]\,= \, E[\,\,ch_n\,H_n(Z_Y)\,|\,bh_n.\,H_n(Z_X)]\, =\,\frac{Cov_{XY,n}}{Var_{X,n}}\,bh_n \, H_n(Z_X)

\end{equation}

while expectation of variance associated with the conditional expectation $E[Y_n\,|\, X_n]\,$ is given as

\begin{align}\label{4.3.2}

 & Var[Y_n\,|\, X_n]\,= Var[\,\,ch_n \,
H_n(Z_Y)\,|\,bh_n\,H_n(Z_X)]\,=\,Var_{Y,n}\,-\frac{{Cov_{XY,n}}^2}{Var_{X,n}}\,\\ &=(1\,-\, {\rho_{XY,n}}^2) \,
Var_{Y,n}\,\, =(1\,-\, {\rho_{XY,n}}^2) \, {ch_n}^2\, n! \,

\end{align}

We can write sum of conditional expectations of all Hermite polynomials of target variable Y with respect to explanatory
variable as

\begin{equation}\label{4.3.4}

 \sum\limits_{n=1}^{N} E[\,\,ch_n \,
H_n(Z_Y),|\,bh_n\,H_n(Z_X)]\,=\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,\,bh_n \, H_n(Z_X)

 \end{equation}

But we know that conditional expectation of Y is equal to sum of conditional expectations of each orthogonal polynomial
of Y including the zeroth hermite polynomial which is the unconditional mean of Y itself, so we can write

\begin{equation}\label{4.3.5}

E[Y \, | \, X]=\mu_Y+ \sum\limits_{n=1}^{N} E[\,\,ch_n \, H_n(Z_Y)\, | \,\,bh_n \,H_n(Z_X) ]

\end{equation}

which means that

\begin{equation}\label{4.3.6}

E[Y\, | \, X]=\mu_Y+\,\sum\limits_{n=1}^{N}\frac{Cov_{XY,n}}{Var_{X,n}}\,\,bh_n \, H_n(Z_X)

\end{equation}

and expected value of total variance, which is variance associated with part of random variable Y that has not been
explained by conditioning on random variable X, associated with conditional expectation of Y given X$E[Y\, | \, X]$ is
given as

\begin{align}\label{4.3.7}

& Var[Y\, | \, X]=\,\sum\limits_{n=1}^{N}\,Var_{Y,n}\,-\frac{{Cov_{XY,n}}^2}{Var_{X,n}}\,
=\,\sum\limits_{n=1}^{N}\,(1\,-\, {\rho_{XY,n}}^2) \, Var_{Y,n}\,\, \\ &= \,\,\sum\limits_{n=1}^{N}\,(1\,-\,
{\rho_{XY,n}}^2) \, {ch_n}^2\, n!\,

\end{align}

In the above equation, We have given the formulas for conditional expected value and the expected value of variance of
conditional expectation of the random variable Y given random variable X.

Even though above formula is true for expectation of variance associated with$E[Y|X]$ , the coefficients of nth Hermite
polynomial in conditional distribution equation of Y given X are not given by
$\, \sqrt{\,1\,-\,{\rho_{XY,n}}^2\,} \,\, ch_n$ . We find true conditional distribution equation for Y when its
unexplained variance is independent of X in section(\ref{sec4.5}) and when its variance structure is dependent on X in
section(\ref{sec4.6})

\subsection{Decomposing the non-Gaussian Random variable Y into a part that is perfectly Correlated with Random variable
X and another part that is orthogonal to X}

\label{sec4.4}

In order to convert a random variable Y into two parts with first part fully correlated with X and another part
orthogonal to X, we remove the correlation effect of random variable X from Y, where Hermite series of X and Y are given
by Eqs(\ref{4.1},and \ref{4.2}) and correlation between their Hermite polynomials are given by Eq(\ref{4.1.5}).

Correlation effect of X on Y is given by conditional expected value of$E\left[Y|X\right]$ . And we represent the
orthogonal part of Y as$\tilde{Y}$ . So Y can be decomposed into two parts as

\begin{equation}\label{4.4.1}

 Y \,=\,\, E\left[Y|X \right] \,+ \,\tilde{Y}

\end{equation}

So orthogonal part of Y denoted as $\tilde{Y}$ is given by

\begin{align}\label{4.4.2}

 & \tilde{Y} \,=\, Y\, -\, E\left[Y|X \right] \, \\ & =  \, Y\,-\,\,\sum\limits_{n=1}^{N} \, E \left[\,\,ch_n \,
H_n(Z_Y)\,|\,H_n(Z_X) \right]\\ \, &=  \, Y\,-\,\,\sum\limits_{n=1}^{N}\,\frac{Cov_{XY,n}}{Var_{X,n}}\,bh_n \, H_n(Z_X)
\\ \, &=  \, Y\,-\,\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \,ch_n \, H_n(Z_X)

\end{align}

We apply the above equation on data observations of Y with pth observation pair given as$Y_p$ and$X_p$ . We first invert
Hermite-Series equation of$X_p$ to find$Z_{X_p}$ and then use the following equation for each pth observation

\begin{equation}\label{4.4.3}

 \tilde{Y_p} \,=  \, Y_p\,-\,\,\sum\limits_{n=1}^{N}\,\rho_{XY,n} \,ch_n \, H_n(Z_{X_p})

\end{equation}

---

### #2591 — Amin (Topic Author)
*January 15, 2025, 10:22 PM*

Friends, I have been able to reasonably calibrate a more advanced version of yesterday's model with iterative method. I
used the equation form

$$\, \bar{ \Delta \theta_t } =\,\, f_1(\theta_{t-1}) \,Z_{\bar{\Delta\theta}} \, +\, f_2(\theta_{t-1})
\,{Z_{\bar{\Delta\theta}}}^2 \\

=\,\,\left[ \, e_{10} \, + \, e_{11}\,{Z_{\theta}}\,+\,e_{12}  \,{Z_{\theta}}^2\,+\,e_{13}\,{Z_{\theta}}^3\right]
Z_{\bar{\Delta\theta}} \\

+\,\,\left[ \, e_{20} \, + \, e_{21}\,{Z_{\theta}}\,+\,e_{22} \,{Z_{\theta}}^2\,+\,e_{23}\,{Z_{\theta}}^3\right]
{Z_{\bar{\Delta\theta}}}^2$$

I noticed that without adding a second term of the order${Z_{\bar{\Delta\theta}}}^2$ , I could not get any skew in the
orthogonal part. I was just able to get my results and the fit of the above model is reasonable but not perfect. I think
I need to improve the model for another day or two and then I would be able to post it. It's a bit late but I will give
more details tomorrow after running and analyzing the program more carefully.

Here is a sample fit of orthogonal part of  dynamic coefficient using above equation. Below, Moments indicates model
moments and rMu indicates input moments. These results are only for orthogonal part but not for correlated part that was
tackled analytically.

1st Coeff

Moments =

   1.0e-04 *

  Columns 1 through 3

                   0   0.563592503032004   0.000221060740061

  Columns 4 through 6

   0.000142776474884  -0.000000386589097   0.000000089441353

rMu =

   1.0e-04 *

  Columns 1 through 3

   0.000000000000001   0.563592503032004   0.000348787486646

  Columns 4 through 6

   0.000143943236480  -0.000000557198941   0.000000084289204

2nd Coeff

Moments =

   1.0e-03 *

  Columns 1 through 3

                   0   0.114492924101284   0.000826120115192

  Columns 4 through 6

   0.000152760790622   0.000002949032295   0.000000535168841

rMu =

   1.0e-03 *

  Columns 1 through 3

   0.000000000000000   0.114492924101284   0.000925700566427

  Columns 4 through 6

   0.000175136859606   0.000002894612284   0.000000502948380

Third Coeff

Moments =

   1.0e-04 *

  Columns 1 through 3

                   0   0.203443714251540   0.000347467110747

  Columns 4 through 6

   0.000057490097755   0.000000304174590   0.000000044630687

rMu =

   1.0e-04 *

  Columns 1 through 3

  -0.000000000000001   0.203443714251540   0.000328132417930

  Columns 4 through 6

   0.000066464368769   0.000000312963738   0.000000042823397

fourth Coeff

Moments =

   1.0e-04 *

  Columns 1 through 3

                   0   0.124792412676856  -0.001403839750863

  Columns 4 through 6

   0.000043263549172  -0.000001369311778   0.000000059096109

rMu =

   1.0e-04 *

  Columns 1 through 3

  -0.000000000000001   0.124792412676856  -0.001543957780007

  Columns 4 through 6

   0.000054852336602  -0.000001591045590   0.000000056846041

---

### #2592 — Amin (Topic Author)
*January 16, 2025, 5:21 PM*

Friends, I am going to attach the program in next post in half an hour.

Here is the final form of equations of uncorrelated part

I used the equation in hermite form

$$\, \bar{ \Delta \theta_t } =\,\, f_1(\theta_{t-1}) \,Z_{\bar{\Delta\theta}} \, +\, f_2(\theta_{t-1})
\,\left({Z_{\bar{\Delta\theta}}}^2\,-\,1\right) \\

=\,\,\left[ \, e_{10} \, + \, e_{11}\,{Z_{\theta}}\,+\,e_{12}  \,{Z_{\theta}}^2\,+\,e_{13}\,{Z_{\theta}}^3\right]
Z_{\bar{\Delta\theta}} \\

+\,\,\left[ \, e_{20} \, + \, e_{21}\,{Z_{\theta}}\,+\,e_{22} \,{Z_{\theta}}^2\,+\,e_{23}\,{Z_{\theta}}^3\right]
\left({Z_{\bar{\Delta\theta}}}^2-1 \right)$$

I had to take second hermite$\left({Z_{\bar{\Delta\theta}}}^2-1 \right)$ instead of second power of Z as
${Z_{\bar{\Delta\theta}}}^2$ since we are modelling the orthogonal part that cannot take any correlations with a
function of${Z_{\theta}}$ and that required modelling with hermite polynomial.

The program I am uploading is still preliminary and we will spend a week to ten days to improve the time series related
infrastructure we are developing. There will be better versions of this program soon.

Here are the updated results of moment fit of four dynamic coefficients from their parameters. Here target moments are a
bit different from yesterday since I increased the order of hermite polynomials and their correlations used to find the
orthogonal uncorrelated part of dX.

Coeff1.

Moments =

   1.0e-04 *

  Columns 1 through 3

                   0   0.561621424625933   0.000250139977116

  Columns 4 through 6

   0.000144195384593  -0.000000628707203   0.000000097555870

rMu =

   1.0e-04 *

  Columns 1 through 3

   0.000000000000002   0.561621424625933   0.000251373764940

  Columns 4 through 6

   0.000144368521455  -0.000000665019019   0.000000086340008

Coeff 2

Moments =

   1.0e-03 *

  Columns 1 through 3

                   0   0.112086551037166   0.000706086397241

  Columns 4 through 6

   0.000142182768439   0.000002085680935   0.000000774034816

rMu =

   1.0e-03 *

  Columns 1 through 3

   0.000000000000001   0.112086551037166   0.000708996850534

  Columns 4 through 6

   0.000157941237913   0.000001917836853   0.000000422412074

Coeff 3

Moments =

   1.0e-04 *

  Columns 1 through 3

                   0   0.202954313942088   0.000344065430438

  Columns 4 through 6

   0.000057906805448   0.000000304035799   0.000000071561015

rMu =

   1.0e-04 *

  Columns 1 through 3

  -0.000000000000000   0.202954313942088   0.000340927140195

  Columns 4 through 6

   0.000066247875425   0.000000316672053   0.000000043141708

Coeff 4

Moments =

   1.0e-04 *

  Columns 1 through 3

                   0   0.118886611193895  -0.001298620916092

  Columns 4 through 6

   0.000032949152607  -0.000001246673286   0.000000077131213

rMu =

   1.0e-04 *

  Columns 1 through 3

   0.000000000000001   0.118886611193895  -0.001541113260406

  Columns 4 through 6

   0.000055071116241  -0.000001604601429   0.000000057953198

Here are the parameters of 2D Z-series representing the orthogonal part of dynamic coeffs

bnm1 =

  -0.000610151804301   0.007015186008629   0.000610151804301

   0.000271283203778   0.002590965607971  -0.000271283203778

   0.000376129343617  -0.000000660981591  -0.000376129343617

  -0.000052290377253  -0.000032468829609   0.000052290377253

bnm2 =

  -0.001016097056863   0.007214378908442   0.001016097056863

  -0.003946677730866   0.001464561419486   0.003946677730866

   0.000306495007013   0.001884594092963  -0.000306495007013

   0.000296473656188  -0.000176679401812  -0.000296473656188

bnm3 =

  -0.000363702273833   0.002755011470318   0.000363702273833

  -0.001950615318872  -0.000037434708385   0.001950615318872

   0.000039232962482   0.000918819369742  -0.000039232962482

   0.000142308057892  -0.000013126581508  -0.000142308057892

bnm4 =

   0.001627312875158  -0.000452044827821  -0.001627312875158

   0.000345937656775  -0.001975699689568  -0.000345937656775

   0.000312553653874   0.000452044827821  -0.000312553653874

   0.000049530543965   0.000080694904871  -0.000049530543965

---

### #2593 — Amin (Topic Author)
*January 16, 2025, 5:36 PM*

**(broken latex: Unbalanced $: 1)**

```latex
Above output in previous program uses the matlab code below

.

.

```
function [] = SlidingWindowZSeriesEstimation()

TT=500;
seed=15898837;

seed=98831629;

[X1] = ProduceSDEDataTimeSeries(TT,seed);

NIntervals=15;  %Intervals used to estimate moments

plot((1:TT),X1(1:TT),'g');
str=input("Look at graph of Time Series variable X");

for tt=(1+NIntervals):TT
    muA(1:4)=0;
    for nn=1:NIntervals
        dXt=X1(tt-NIntervals+nn)-X1(tt-NIntervals+nn-1); %Moments are calculated for dX(t)
        muA(1:4)=muA(1:4)+(dXt.^(1:4))/NIntervals;
    end

    [c(1,tt),c(2:4,tt),FittedMoments] = CalculateZSeriesDensityFromRawMoments02M4(muA,0);

    c
    %str=input("Look at new Coeffs");

end

% save("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\DynamicCoeffs01.mat","c");
%
% str=input("I have saved dynamic coeffs");
%
%
% load("C:\Users\Lenovo\Documents\MATLAB\MATLAB1\DynamicCoeffs01.mat","c");

bnm1=EstimateDynamicCoeffParameters(c(1,:));
bnm2=EstimateDynamicCoeffParameters(c(2,:));
bnm3=EstimateDynamicCoeffParameters(c(3,:));
bnm4=EstimateDynamicCoeffParameters(c(4,:));

bnm1
bnm2
bnm3
bnm4

str=input("Please look at 2D Z-series of four dynamic coefficients above");

%c
clf;
yyaxis left
plot((1:TT),X1(1:TT),'g')
ylabel('Random Variable X')
xlabel('Time Intervals')
yyaxis right
plot((1+NIntervals:TT),c(1,1+NIntervals:TT),'b');

hold on
yyaxis right
plot((1+NIntervals:TT),c(2,1+NIntervals:TT),'r');
ylabel('Coefficients c0 and c1 of Z-series of X')

title("Graph of time series X and first two Coefficients of its Z-series, c0 and c1");
legend('X','c0','c1','Location','northeast');
%plot((1:TT),X1(1:TT),'g',(1+NIntervals:TT),c(1,1+NIntervals:TT),'b',(1+NIntervals:TT),c(2,1+NIntervals:TT),'r',(1+NIntervals:TT),c(3,1+NIntervals:TT),'k',(1+NIntervals:TT),c(4,1+NIntervals:TT),'m');
str=input("Look at graph--final");

clf;
yyaxis left
plot((1:TT),X1(1:TT),'g')
ylabel('Random Variable X')
xlabel('Time Intervals')
 hold on
yyaxis right
plot((1+NIntervals:TT),c(3,1+NIntervals:TT),'k');
ylabel('Coefficients c2 of Z-series of X')

title("Graph of time series X and third coefficients of its Z-series, c2");
legend('X','c2','Location','northeast');

str=input("Graph--Fianl--2")

clf;
yyaxis left
plot((1:TT),X1(1:TT),'g')
ylabel('Random Variable X')
xlabel('Time Intervals')
hold on
yyaxis right
plot((1+NIntervals:TT),c(4,1+NIntervals:TT),'m');
ylabel('Coefficients c3 of Z-series of X')

title("Graph of time series X and fourth coefficient of its Z-series, c3");
legend('X','c3','Location','northeast');

end

```

.

.

.

```
function [bnm] = EstimateDynamicCoeffParameters(X)

Ndata=length(X)-1;
Order=7;

%Calculate transition dX
for nn=1:Ndata
    dX(nn)=X(nn+1)-X(nn);
end

%Below Calculate Z-series of X and dX.

[CoeffX,ZX,RSquared1] = CalculateActualZSeriesFromData(X,Order);
[CoeffdX,ZdX,RSquared2] = CalculateActualZSeriesFromData(dX,Order);

Ymu1(1:Ndata,1)=dX(1:Ndata);
dXcorr(1:Ndata,1)=0;
[W1] = EvalHermiteArrayH0(ZX(1:Ndata),Order);
        %Below, do the regression to find the coefficients of part of dX
        %random variable that is correalted with X.
coeff1=inv(W1'*W1)*(W1'*Ymu1);
        %Below, we evaluate the correalted part of dX random variable
        %with X by summing over all the hermite polynomials out
        %to Order.
for hh=0:Order
            %Below dXcorr continues to sum corelated part over all hermites of X

      dXcorr(1:Ndata,1)=dXcorr(1:Ndata,1)+coeff1(hh+1,1).*W1(1:Ndata,hh+1);

end

%Below, we calculate orthogonal part of DX that is uncorrelated with dX

dXdecorr(1:Ndata,1)=Ymu1(1:Ndata,1)-dXcorr(1:Ndata,1);

%Below calculat moments of correalted (with X)  part and orthogonal (with respect to X) part of dX
for kk=1:8
    rMudecorr(kk)=sum(dXdecorr(1:Ndata,1).^kk)/Ndata;
    rMucorr(kk)=sum(dXcorr(1:Ndata,1).^kk)/Ndata;
end

rMudecorr
rMucorr
%dXcorr
%dXdecorr

%str=input("Look at decorrelated part moments");

NMoments=6;
Iterations=20000;

%The function below finds the 2D Z-series of orthogonal part of dX.

[bnm,ObjFunc] = ZSeriesCoeffsFromMomentsIterativeNoiseTerm2D01A(rMudecorr,NMoments,Iterations);

end

```

.

.

```
function [bnm,ObjFunc] = ZSeriesCoeffsFromMomentsIterativeNoiseTerm2D01A(rMu,NMoments,Iterations)

%This program computes coeffs of Z-series when values of raw moments are
%given using Iterative method.

%rMu are raw moments;

%Hermite Series Form is

%
% Y=  +(bnmh(1,2) + bnmh(2,2)* Z1 + bnmh(3,2)* (Z1^2-1) + bnmh(4,2)* (Z1^3-3*Z1))* Z2
%     +(bnmh(1,3) + bnmh(2,3)* Z1 + bnmh(3,3)* (Z1^2-1) + bnmh(4,3)* (Z1^3-3*Z1))* (Z2^2-1)
%
% Equivalent 2D Z-series form is
% Y=   (bnm(1,1) + bnm(2,1) Z1 + bnm(3,1) Z1^2 + bnm(4,1) Z1^3)
%     +(bnm(1,2) + bnm(2,2) Z1 + bnm(3,2) Z1^2 + bnm(4,2) Z1^3) Z2
%     +(bnm(1,3) + bnm(2,3) Z1 + bnm(3,3) Z1^2 + bnm(4,3) Z1^3) Z2^2
%
%
% Var(Y)= bnmh(1,2).^2 + bnmh(2,2).^2 + 2* bnmh(3,2).^2 + 6* bnmh(4,2).^2
%        +2*(bnmh(1,3).^2 + bnmh(2,3).^2 + 2* bnmh(3,3).^2 + 6* bnmh(4,3).^2)
%
%
%
% bnm(1,1)= -bnmh(1,3) + bnmh(3,3)
% bnm(2,1)= -bnmh(2,3) + 3* bnmh(4,3)
% bnm(3,1)= -bnmh(3,3)
% bnm(4,1)= -bnmh(4,3)
%
% bnm(1,2)= bnmh(1,2) - bnmh(3,2)
% bnm(2,2)= bnmh(2,2) - 3* bnmh(4,2)
% bnm(3,2)= bnmh(3,2)
% bnm(4,2)= bnmh(4,2)
%
% bnm(1,3)= bnmh(1,3) - bnmh(3,3)
% bnm(2,3)= bnmh(2,3) - 3* bnmh(4,3)
% bnm(3,3)= bnmh(3,3)
% bnm(4,3)= bnmh(4,3)

%We have used the notation
%cH0=bnmh(1,2);
%cH(1)=bnmh(2,2);
%CH(2)=bnmh(3,2);
%CH(3)=bnmh(4,2);
%cH(4)=bnmh(1,3);
%cH(5)=bnmh(2,3);
%CH(6)=bnmh(3,3);
%CH(7)=bnmh(4,3);

% SO We will use the equations

% cH0=1-sqrt(cH(1).^2 + 2*cH(2).^2 + 6*cH(3).^2+2*(cH(4).^2 + cH(5).^2 + 2*cH(6).^2 + 6*cH(7).^2));
%
%
% bnm(1,1)= -cH(4) + cH(6);
% bnm(2,1)= -cH(5) + 3*cH(7);
% bnm(3,1)= -cH(6);
% bnm(4,1)= -cH(7);
%
% bnm(1,2)= cH0 - cH(2);
% bnm(2,2)= cH(1) - 3*cH(3);
% bnm(3,2)= cH(2);
% bnm(4,2)= cH(3);
%
% bnm(1,3)= cH(4) - cH(6);
% bnm(2,3)= cH(5) - 3*cH(7);
% bnm(3,3)= cH(6);
% bnm(4,3)= cH(7);

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
%sMu(7)=cMu(7)/cMu(2).^3.5;
%sMu(8)=cMu(8)/cMu(2).^4.0;

%cH(1)=1;

SeriesOrder=7;
cH(1:SeriesOrder)=0;
cH(1)=.001;%.05
%%%%%%Choose the iteration step size.

for nn=1:3
    DeltaX(nn)=.00125/sqrt(factorial(nn+1));
end
for nn=4:7
    DeltaX(nn)=.00125/sqrt(factorial(nn+1-3))*2;
end

%%%Weights on objective function that shows fit to moments
w(NMoments)=1;
for nn=NMoments-1:-1:1
    w(nn)=w(nn+1)*(nn+1)*(nn+2);
end

w(3)=w(3)*2;
w(5)=w(5)*2;
w(4)=w(4)*1;

cH0=sqrt(1-(cH(1).^2 + 2*cH(2).^2 + 6*cH(3).^2+2*(cH(4).^2 + cH(5).^2 + 2*cH(6).^2 + 6*cH(7).^2)));

bnm(1,1)= -cH(4) + cH(6);
bnm(2,1)= -cH(5) + 3*cH(7);
bnm(3,1)= -cH(6);
bnm(4,1)= -cH(7);

bnm(1,2)= cH0 - cH(2);
bnm(2,2)= cH(1) - 3*cH(3);
bnm(3,2)= cH(2);
bnm(4,2)= cH(3);

bnm(1,3)= cH(4) - cH(6);
bnm(2,3)= cH(5) - 3*cH(7);
bnm(3,3)= cH(6);
bnm(4,3)= cH(7);

SeriesOrder10=4;
SeriesOrder01=3;

[Moments] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMoments);

Moments
%str=input("Look at Moments");

[ObjFuncBest] = CalculateObjMoment(sMu,Moments,w,mOrder);

cHBest=cH;

ImproveFlag(1:SeriesOrder)=1;
ImproveFlagPrev(1:SeriesOrder)=0;
ImproveCount=0;

for mm=1:Iterations
AdjustFlag=0;
    %mm
    %First 500 iterations try to fit three moments only
    if(mm=500)&&(mm=4000)&&(mm=10000))
        SeriesOrder1=1;
        SeriesOrder2=7;
        NMoments=6;
        mOrder=NMoments;

        %Block Below: Once we move from fitting five moments to six moments
        %Best Objective Function changes and becomes larger. This
        %has to be reset at the start of six moments optimization.
        %We also increase the weight associated with already
        %calibrated third, fourth and fifth moment is increased so
        %that stays in calibration
        if(mm==10000)
        SeriesOrder10=4;
        SeriesOrder01=3;

        [Moments] = Calculate2DSeriesMoments(bnmBest,SeriesOrder10,SeriesOrder01,NMoments);
        cH=cHBest;
        w(3:5)=4*w(3:5);
        [ObjFuncBest] = CalculateObjMoment(sMu,Moments,w,mOrder);
        ObjFuncBest
        %str=input("I am in here NMoments =6 ");
        AdjustFlag=1;
        end
    end

    for nn=SeriesOrder1:SeriesOrder2

        ImproveFlagPrev(nn)=ImproveFlag(nn);

        cinH=cH;
        cinH(nn)=cinH(nn)+DeltaX(nn);

        %Below lines keep the total variance equal to one.
        CondFlag=1;
        VarYP=cinH(1).^2 + 2*cinH(2).^2 + 6*cinH(3).^2+2*(cinH(4).^2 + cinH(5).^2 + 2*cinH(6).^2 + 6*cinH(7).^2);
        if(VarYP>1)
            cinH=cinH/sqrt(VarYP)*.98;
            %CondFlag=0;
        end

        cinH0=abs(sqrt(1-(VarYP)));

        %Convert to 2D Z-series Coeffs from Hermite Coeffs

        bnm(1,1)= -cinH(4) + cinH(6);
        bnm(2,1)= -cinH(5) + 3*cinH(7);
        bnm(3,1)= -cinH(6);
        bnm(4,1)= -cinH(7);

        bnm(1,2)= cinH0 - cinH(2);
        bnm(2,2)= cinH(1) - 3*cinH(3);
        bnm(3,2)= cinH(2);
        bnm(4,2)= cinH(3);

        bnm(1,3)= cinH(4) - cinH(6);
        bnm(2,3)= cinH(5) - 3*cinH(7);
        bnm(3,3)= cinH(6);
        bnm(4,3)= cinH(7);

        SeriesOrder10=4;
        SeriesOrder01=3;

        [Moments] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMoments);

        [ObjFunc] = CalculateObjMoment(sMu,Moments,w,mOrder);

        if((ObjFunc1)
                cinH=cinH/sqrt(VarYP)*.98;
                %CondFlag=0;
            end

            cinH0=abs(sqrt(1-(VarYP)));

            %Convert to 2D Z-series Coeffs from Hermite Coeffs
            bnm(1,1)= -cinH(4) + cinH(6);
            bnm(2,1)= -cinH(5) + 3*cinH(7);
            bnm(3,1)= -cinH(6);
            bnm(4,1)= -cinH(7);

            bnm(1,2)= cinH0 - cinH(2);
            bnm(2,2)= cinH(1) - 3*cinH(3);
            bnm(3,2)= cinH(2);
            bnm(4,2)= cinH(3);

            bnm(1,3)= cinH(4) - cinH(6);
            bnm(2,3)= cinH(5) - 3*cinH(7);
            bnm(3,3)= cinH(6);
            bnm(4,3)= cinH(7);

            SeriesOrder10=4;
            SeriesOrder01=3;

            [Moments] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMoments);

            [ObjFunc] = CalculateObjMoment(sMu,Moments,w,mOrder);
            if((ObjFunc10)&&(ObjFuncBest==ObjFuncBestBefore))
        ResetFlag=1;
    end
    ObjFuncBestBefore=ObjFuncBest;
    %DeltaX
    %ImproveCount

    end
    if(ResetFlag==1)
     %  DeltaX=DeltaX*5;

    end

    ImproveFlag0=0;
    for nn=1:SeriesOrder
       if(ImproveFlag(nn)==1)
           ImproveFlag0=1;
           ImproveCount=ImproveCount+1;
       end
    end
    for nn=2:SeriesOrder
        if(ImproveFlag0==0)
            DeltaX(nn)=DeltaX(nn)*.95;
            ImproveCount=0;
        end
    end
    if(ImproveCount>4)
       for nn=2:SeriesOrder
            DeltaX(nn)=DeltaX(nn)*1.05;
       end
    end

    end

end

bnm=bnmBest;
[Moments] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMoments);

Moments
sMu

str=input("Look at comparison of Standardised model moments and Standardized target moments")

bnm=bnm*sqrt(cMu(2));

[Moments] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMoments)
rMu

str=input("Look at comparison of model raw moments and target raw moments")

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
function [Moments1D] = Calculate2DSeriesMoments(bnm,SeriesOrder10,SeriesOrder01,NMomentsX)

X(1:SeriesOrder10*NMomentsX-NMomentsX+1,1:SeriesOrder01*NMomentsX-NMomentsX+1,NMomentsX)=0;
X(1:SeriesOrder10,1:SeriesOrder01,1)=bnm(1:SeriesOrder10,1:SeriesOrder01);
anm=bnm;
SeriesOrder20=SeriesOrder10;
SeriesOrder02=SeriesOrder01;

EZ=EZZ2();
Moments1D(1)=0;
for nn=1:SeriesOrder10
    for mm=1:SeriesOrder01
        Moments1D(1)=Moments1D(1)+bnm(nn,mm).*EZ(nn).*EZ(mm);
    end
end

for nn=1:NMomentsX-1

[cnm,EX0] =SeriesProduct2DAlgorithmicNew(bnm,anm,SeriesOrder10,SeriesOrder01,SeriesOrder20,SeriesOrder02);

SeriesOrder20=SeriesOrder20+SeriesOrder10-1;
SeriesOrder02=SeriesOrder02+SeriesOrder01-1;

%size(cnm)
%SeriesOrder20
%SeriesOrder02
%nn+1
%str=input("Look at sizes of result of moments");

X(1:SeriesOrder20,1:SeriesOrder02,nn+1)=cnm(1:SeriesOrder20,1:SeriesOrder02);
anm=cnm;
Moments1D(nn+1)=EX0;
end

end

```

.

.

.

```
function [cc,EX] =SeriesProduct2DAlgorithmicNew(aa,bb,SeriesOrder10,SeriesOrder01,SeriesOrder20,SeriesOrder02)

SeriesOrder30=SeriesOrder10+SeriesOrder20-1;
SeriesOrder03=SeriesOrder01+SeriesOrder02-1;

cc(1:SeriesOrder30,1:SeriesOrder03)=0;

for nn1=1:SeriesOrder30
    if(nn1<=SeriesOrder10)
        nn3=nn1;
    else
        nn3=SeriesOrder10;
    end
    for nn2=1:SeriesOrder03
        if(nn2<=SeriesOrder01)
            nn4=nn2;
        else
            nn4=SeriesOrder01;
        end
        for jj1=1:nn3
            if(nn1-jj1+1 <=SeriesOrder20)
                for jj2=1:nn4
                    if(nn2-jj2+1 <=SeriesOrder02)
                        cc(nn1,nn2)=cc(nn1,nn2)+aa(jj1,jj2).*bb(nn1-jj1+1,nn2-jj2+1);
                    end
                end
            end
        end
    end
end

[EZ] = EZZ2();

EX=0;
for nn1=1:SeriesOrder30
    for nn2=1:SeriesOrder03
        EX=EX+cc(nn1,nn2).*EZ(nn1).*EZ(nn2);
    end
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
function [EZ] = EZZ2()

EZ(1)=1;
EZ(2)=0;
EZ(3)=1;
for nn=4:96 %Increase for larger products.
    if rem(nn,2)==0
        EZ(nn)=0;
    else
        EZ(nn)=EZ(nn-2)*(nn-2);
        EZ(nn);
    end
end
% EZ(64)
% EZ(64).*EZ(64)

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
function [Coeff,Zy,RSquared] = CalculateActualZSeriesFromData(Yin,Order)

Ndata=length(Yin);

Hz=HermitePoly(Order);
MeanYin=sum(Yin(1:Ndata))/Ndata;
%Ys=sort(Yin);
%MedianYin=(Ys(Ndata/2)+Ys(Ndata/2+1))/2;

Ym(1:Ndata)=Yin(1:Ndata)-MeanYin;
%Y(1:Ndata)=Yin(1:Ndata)-MedianYin;
YmVar=sum(Ym(1:Ndata).^2)/Ndata;
Y(1:Ndata)=Ym(1:Ndata)/sqrt(YmVar);

%Mtable=readtable('C:\Users\Lenovo\Documents\MATLAB\MATLAB1\MomentMatchParams08.txt');
%[ZI] = MatchMomentParametersOfIdealZhalf04(Ndata,Mtable);

[Zn] = StandardNormalIdealDesity02(Ndata,1);
%[ZI] = CalculateZI(Zn);

ZI=Zn;
%Below W is the design matrix for least squares regression i.e the matrix
%that contains all the hermite polynomials calculated at ideal normal
%density grid of size Ndata.
[W] = EvalZArrayZ0(ZI,Order);

%W
%W0=W;
%W(:,1:Order)=W0(:,2:Order+1);
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
Ymu(1:Ndata,1)=Ys(1:Ndata);
%Below, implement least squares regression.
coeff=(W'*W)$W'*Ymu);

size(coeff)
coeff
str=input("Look at coeff size");

%Store in coefficietns array of all random varaibles
Coeff(1:Order+1)= coeff(1:Order+1,1);
%Store the associated Z in Z-array of all coefficients.
Zy(1:Ndata)=Zs1(1:Ndata);

[W2] = EvalZArrayZ0(Zy,Order);

Coeff(1:Order+1)=Coeff(1:Order+1).*sqrt(YmVar);
Coeff(1)=Coeff(1)+MeanYin;

Coeff
%Coeff(1)=Coeff(1)+MedianYin;

Coeff2(:,1)=Coeff(:);
X=W2*Coeff2;
size(W2)
size(Coeff2)
size(X)
 RSquared=1-sum(((Yin(:)-X(:,1)).^2))./(YmVar*Ndata)
 %1-sum((aa(:,1)-b0(:,1)).^2)/sum((aa(:,1)-sum(aa(:,1))/(NN)).^2)

end
```

.

.
```

---

### #2594 — Amin (Topic Author)
*January 16, 2025, 6:13 PM*

Friends, by the end of weekend, I expect to complete the next version of the program in which there will be improved
algorithm for matching the moments of uncorrelated part. And I will convert the Z-series back to dynamics in terms of
coefficients i.e. the original variable. And I will use the function composition method for that. I also hope to add
Newton root search to the (improved version of) iterative method program (that I posted today) for precision in matching
moments. We will keep working to develop the associated infrastructure for next two weeks and then start working with
real stocks data for algorithmic trading possibly by the start of February. I hope that soon we will be doing a lot of
more interesting work.

---

### #2595 — Amin (Topic Author)
*January 17, 2025, 3:07 AM*

Friends, I will try to make a detailed post tonight explaining all of the mathematics behind the new matlab programs
with latex equations and then relating those mathematical equations to matlab code so friends who joined us late could
better understand the matlab programs. I will explain the programs tonight.

---

### #2596 — Amin (Topic Author)
*January 17, 2025, 4:45 PM*

Sorry friends, will make a detailed post tomorrow.

---

### #2597 — Amin (Topic Author)
*January 18, 2025, 7:04 PM*

**(broken latex: Unbalanced $: 19)**

```latex
Friends, this post is to explain 2D Z-series and 2D Hermite series in more detail. This is preliminary to understand
yesterday's matlab program.  I will make another post explaining details of yesterday's matlab program.

Friends, I have given a good introduction to 1D Z-series and Hermite Series in my paper here: [https://papers.ssrn.com/sol3/papers.cfm ... id=4933283](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4933283)

You have to read that if you are not familiar with Z-series and Hermite-series at all. (SSRN froze the counter of my
paper on instructions from CIA so when you download it, please see if download counter moves.)

Here I give a primer on 2D Z-series and Hermite series.

A Primer on 2D Z-series and 2D Hermite Series

Why Both Hermite Series and Z-series

The Hermite series representation of a particular order is algebraically equivalent to Z-series representation of the
same order. There are many analytics on non-Gaussian random variables like transformation of random variables using
Taylor series, multiplication of random variables, calculation of moments and cross-moments where a Z-series
representation is more useful. While there are some other analytics associated with correlations, variances and
conditional expectation of non-Gaussian random variables where Hermite-Series representation would be more useful. In
most of our numerical algorithms, we will have to continue to switch between Z-Series of a random variable and its
equivalent Hermite series.

Two Dimensional Z-series

A Two dimensional Z-series expansion can be made for a non-gaussian random variable that depends upon more than one
sources of uncertainty. Both$Z_x$ and$Z_y$ are two uncorrelated and independent standard Gaussians.

A Two dimensional Z-series can be written as

\begin{equation}

X(Z_y\,,\,Z_x)\,=\, \sum\limits_{n=0}^{N}\,\, \sum\limits_{m=0}^{M}\, b_{n,m}\,{Z_y}^n\,{Z_x}^m

\end{equation}

An explicit example of a 3 X 3 2D Z-series is given below.

\begin{align}

X(Z_y \, , \, Z_x)\, &=\,\Big[ b_{0,0} \, + \, b_{0,1} \, Z_x \,+\, b_{0,2} \, {Z_x}^2 \,\, + \, b_{0,3} \,{Z_x}^3\,\,
\Big] \\

&+\, \Big[ \, b_{1,0} \, + \, b_{1,1} \,Z_x \,+\, b_{1,2} \, {Z_x}^2\, \, + \, b_{1,3} \,{Z_x}^3\,\, \Big] \, Z_y \, \\

&+\, \Big[ \, b_{2,0} \, + \, b_{2,1} \,Z_x \,+\, b_{2,2} \, {Z_x}^2\, \,  + \, b_{2,3} \,{Z_x}^3\,\, \Big] \, {Z_y}^2
\, \\

&+\, \Big[ \, b_{3,0} \, + \, b_{3,1} \,Z_x \,+\, b_{3,2} \, {Z_x}^2\,  \, + \, b_{3,3} \,{Z_x}^3\, \Big] \,  {Z_y}^3\,

\end{align}

Two Dimensional Hermite Series

A two dimensional Hermite Series can be written as

\begin{equation}

X(Z_y\,,\,Z_x)\,=\, \sum\limits_{n=0}^{N}\,\, \sum\limits_{m=0}^{M}\, bh_{n,m}\,H_n(Z_y)\,H_m(Z_x)

\end{equation}

An explicit example of a 3 X 3 2D Hermite series is given below.

\begin{align}

X(Z_y \, , \, Z_x)\, &=\, \Big[\, bh_{0,0} \, + \, bh_{0,1} \,H_1(Z_x) \,+\, bh_{0,2} \, H_2(Z_x) \,\, + \, bh_{0,3}
\,H_3(Z_x)\,\Big] \\

&+\, \Big[ \, bh_{1,0} \, + \, bh_{1,1} \,H_1(Z_x) \,+\, bh_{1,2} \, H_2(Z_x) \, + \, bh_{1,3} \,H_3(Z_x)\, \Big] \,
H_1(Z_y) \, \\

&+\, \Big[ \, bh_{2,0} \, + \, bh_{2,1} \,H_1(Z_x) \,+\, bh_{2,2} \, H_2(Z_x) \, \, + \, bh_{2,3} \,H_3(Z_x)\, \Big] \,
H_2(Z_y) \, \\

&+\, \Big[ \, bh_{3,0} \, + \, bh_{3,1} \,H_1(Z_x) \,+\, bh_{3,2} \, H_2(Z_x) \, + \, bh_{3,3} \,H_3(Z_x)\, \Big] \,
H_3(Z_y) \,

\end{align}

Hermite Series are very convenient for analytics associated with correlations, variances and conditional expectation of
non-Gaussian random variables. Since variance of nth order hermite polynomial is given as$n!$ , using the orthogonality
property of hermite polynomials, we can easily calculate the variance of above 3 X 3 hermite series as

\begin{align}

Var(X)\, &=\, {bh_{0,1}}^2 \,+\, 2\,{bh_{0,2}}^2 \,+\,6\, {bh_{0,3}}^2 \,\\

&+\, {bh_{1,0}}^2 \,+\, {bh_{1,1}}^2 \,+\, 4\,{bh_{1,2}}^2 \,+\,6\, {bh_{1,3}}^2 \,\\

&+\, 2\,{bh_{2,0}}^2 \,+\,2\, {bh_{2,1}}^2 \,+\, 4\,{bh_{2,2}}^2 \,+\,12\, {bh_{2,3}}^2 \,\\

&+\, 6\,{bh_{3,0}}^2 \,+\,6\, {bh_{3,1}}^2 \,+\, 12\,{bh_{3,2}}^2 \,+\,36\, {bh_{3,3}}^2 \,\\

\end{align}

Product and Moments of Z-series Random variables

Product of 2D Z-series follow exactly the algebra behind the product of Two dimensional power series where we multiply
the two series and algebraically collect the coefficients with same powers of$Z_x$ , and$Z_y$ and the cross products of
$Z_x$ , and$Z_y$ .

In order to take moments, we take the appropriate product of two dimensional Z-series and then apply expectation on
powers of standard normals.

For calculation of products and moments of random variables, we have to use their Z-series and when we have their
hermite series given, we would have to convert them to two dimensional Z-series and then find the desired products and
moments . We cannot easily do the calculations of products and moments directly in 2D Hermite series representations.

Taylor Series of 2D Z-series Random variables.

We can find functions of two dimensional Z-series random variables by applying multidimensional Taylor series to them.
We have to apply Taylor series of random variables on their Z-series representation. We use a very small toy expansion
only to second order since multidimensional Taylor series quickly become very cumbersome. We have to find automated
algorithms for multidimensional Taylor series calculation of functions of multi-dimensional Z-series. Let us write a Toy
2D Taylor expansion of a random variable below as

\begin{align}

& f(X(Z_y,Z_x)\,=\, \Biggr[ f(X(0,0)) +f'(X) \frac{\partial X}{\partial Z_x} Z_x+1/2 \Big(f''(X) \frac{\partial
X}{\partial Z_x}^2+f'(X) \frac{\partial^2 X}{\partial {Z_x}^2} \Big) Z_x^2+O[Z_x]^3 \Biggr]\\

&+\Biggr[\,f'(X) \frac{\partial X}{\partial {Z_y}  }+\left(f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial
X}{\partial {Z_y}  }+f'(X) \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}\right) Z_x \\

&+\left(\left(1/2 f^{3}(X) \frac{\partial X}{\partial Z_x}^2+f''(X) \frac{\partial^2 X}{\partial {Z_x}^2} \right)
\frac{\partial X}{\partial {Z_y}  }+f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial^2 X}{\partial {Z_y} \partial
{Z_x}}+1/2 f'(X) \frac{\partial^2 X}{\partial {Z_y} \partial{Z_x}^2 } \right) Z_x^2+O[Z_x]^3  \Biggr]Z_y \\

&+\Biggr[\,1/2 \left(f''(X) \frac{\partial X}{\partial {Z_y}  }^2+f'(X) \frac{\partial^2 X}{\partial {Z_y}^2  } \right)
\\

&+1/2 \left( f^{3}(X) \frac{\partial X}{\partial Z_x} \frac{\partial X}{\partial {Z_y}  }^2+2 f''(X) \frac{\partial
X}{\partial {Z_y}  } \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}+f''(X) \frac{\partial X}{\partial Z_x}
\frac{\partial^2 X}{\partial {Z_y}^2  }+f'(X) \frac{\partial^3 X}{\partial {Z_y}^2 \partial {Z_x}}\right) Z_x \\

&+1/2 \Biggr(1/2  \Big( f^{4}(X) \Big[{\frac{\partial X}{\partial Z_x}}\Big]^2+f^3(X) \frac{\partial^2 X}{\partial
{Z_x}^2} \Big) \Big[{\frac{\partial X}{\partial {Z_y}  }}\Big]^2+2 f^3(X) \frac{\partial X}{\partial Z_x} \frac{\partial
X}{\partial {Z_y}  } \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}} \\

&+f''(X) \Big( \Big[\frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}\Big]^2+\frac{\partial X}{\partial {Z_y}  }
\frac{\partial^2 X}{\partial {Z_y} \partial{Z_x}^2 } \Big) \\

&+1/2 \Big(f^{3}(X) \Big[\frac{\partial X}{\partial Z_x}\Big]^2+f''(X) \frac{\partial^2 X}{\partial {Z_x}^2} \Big)
\frac{\partial^2 X}{\partial {Z_y}^2  }+f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial^3 X}{\partial {Z_y}^2
\partial {Z_x}}+1/2 f'(X) \frac{\partial^4 X}{\partial {Z_y}^2 \partial{Z_x}^2 } \Biggr) Z_x^2+O[Z_x]^3 )
\Biggr]Z_y^2+O[Z_y]^3

\end{align}

From this Taylor expansion, just like we did for one dimensional  composition of functions, we can find a function that
is applied to a two dimensional Z-series and matches it to another different two dimensional Z-series. Suppose two
dimensional Z-series of a target random variable is given with known coefficients as as

\begin{align}

Y(Z_y \, , \, Z_x)\, &=\,\Big[ b_{0,0} \, + \, b_{0,1} \, Z_x \,+\, b_{0,2} \, {Z_x}^2 \,\,\,\, \Big] \\

&+\, \Big[ \, b_{1,0} \, + \, b_{1,1} \,Z_x \,+\, b_{1,2} \, {Z_x}^2\, \,\, \Big] \, Z_y \, \\

&+\, \Big[ \, b_{2,0} \, + \, b_{2,1} \,Z_x \,+\, b_{2,2} \, {Z_x}^2\, \,\, \Big] \, {Z_y}^2 \, \\

\end{align}

Then We can match the powers of two dimensional composition of Z-series and the target Z-series to find

\begin{align}

b_{0,1}\,&=\,f'(X) \frac{\partial X}{\partial Z_x}\\

b_{0,2}\,&=\,1/2 \Big(f''(X) \frac{\partial X}{\partial Z_x}^2+f'(X) \frac{\partial^2 X}{\partial {Z_x}^2} \Big) \\

b_{1,0}\,&=\,f'(X) \frac{\partial X}{\partial {Z_y}  } \\

b_{1,1}\,&=\,\left(\,(f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial X}{\partial {Z_y}  }+f'(X) \frac{\partial^2
X}{\partial {Z_y} \partial {Z_x}}\right) \\

b_{1,2}\,&=\,\left(\left(1/2 f^{3}(X) \frac{\partial X}{\partial Z_x}^2+f''(X) \frac{\partial^2 X}{\partial
{Z_x}^2}\right) \frac{\partial X}{\partial {Z_y}  }+f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial^2 X}{\partial
{Z_y} \partial {Z_x}}+1/2 f'(X) \frac{\partial^2 X}{\partial {Z_y} \partial{Z_x}^2 } \right) \\

b_{2,0}\,&=\, 1/2\, \left(\, f''(X) \frac{\partial X}{\partial {Z_y}  }^2+f'(X) \frac{\partial^2 X}{\partial {Z_y}^2  }
\right) \\

b_{2,1}\,&=\,+1/2 \,\left(f^{3}(X) \frac{\partial X}{\partial Z_x} \frac{\partial X}{\partial {Z_y}  }^2+2 f''(X)
\frac{\partial X}{\partial {Z_y}  } \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}+f''(X) \frac{\partial X}{\partial
Z_x} \frac{\partial^2 X}{\partial {Z_y}^2  }+f'(X) \frac{\partial^3 X}{\partial {Z_y}^2 \partial {Z_x}}\right) \\

b_{2,2}\,&=\,1/2 \Biggr(1/2  \Big( f^{4}(X) \Big[{\frac{\partial X}{\partial Z_x}}\Big]^2+f^3(X) \frac{\partial^2
X}{\partial {Z_x}^2} \Big) \Big[{\frac{\partial X}{\partial {Z_y}  }}\Big]^2+2 f^3(X) \frac{\partial X}{\partial Z_x}
\frac{\partial X}{\partial {Z_y}  } \frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}} \\

&+f''(X) \Big( \Big[\frac{\partial^2 X}{\partial {Z_y} \partial {Z_x}}\Big]^2+\frac{\partial X}{\partial {Z_y}  }
\frac{\partial^2 X}{\partial {Z_y} \partial{Z_x}^2 } \Big) \\

&+1/2 \Big(f^{3}(X) \Big[\frac{\partial X}{\partial Z_x}\Big]^2+f''(X) \frac{\partial^2 X}{\partial {Z_x}^2} \Big)
\frac{\partial^2 X}{\partial {Z_y}^2  }+f''(X) \frac{\partial X}{\partial Z_x} \frac{\partial^3 X}{\partial {Z_y}^2
\partial {Z_x}}+1/2 f'(X) \frac{\partial^4 X}{\partial {Z_y}^2 \partial{Z_x}^2 } \Biggr)

\end{align}

using above equations, we can solve for the values of derivatives ($f'(X),\,f"(X),\,\ldots, \, f^n(X) \,$ ) of the
required applied function so that its composition with given Z-series function matches the given Z-series function with
a target Z-series function.

Equivalence of Hermite-Series and Z-Series Random Variables in Two Dimensions And Conversion of Coefficients across the
Two Types of Series.

The equivalence and conversion of Z-series and Hermite Series in multidimensions works just analogously to the way it
works in a single dimension. We first apply single dimensional conversion from Z-series to Hermite-series across one
index and then across the second index and similarly for conversion from Hermite-series to Z-series.

Here I am first explaining one dimensional equivalence of both types of series and their conversion across each other.

Nth order Z-series and Nth order Hermite-Series share a common span of Nth order polynomials so any random variable that
can be represented with Nth order Z-series, can also be represented by a Hermite-Series up to Nth order Hermite
Polynomial. In fact, once coefficients of Z-series are known, it is easily possible to find coefficients of equivalent
Hermite-Series and Vice versa and this is just consequence of simple algebra.

If we have Z-series representation of a non-Gaussian random variable is given, we can easily find coefficients of its
Hermite-Series and vice versa.

If we represent a Z-series as

\begin{equation}

X(Z)\,=\, \sum\limits_{n=0}^{N}\, a_n\, {Z}^n

\end{equation}

and a hermite series as

\begin{equation}

X(Z)\,=\, \sum\limits_{n=0}^{N}\, ah_n\, H_n(Z)

\end{equation}

then for $N=7$ (for $N\,
```

---

### #2598 — Amin (Topic Author)
*January 19, 2025, 10:44 AM*

**(broken latex: Unbalanced $$: 19)**

```latex
Friends, this is description of iterative optimization matlab program named as

function [bnm,ObjFunc] = ZSeriesCoeffsFromMomentsIterativeNoiseTerm2D01A(rMu,NMoments,Iterations)

This program was only an initial version and in a few days I want to come up with a better program that uses Newton
method in calculation of the coefficients of orthogonal part of transition increments. I will also do work to convert 2D
hermite-series or 2D Z-series into functions of X and$Z_y$ .

Here are the details of the above program

Objective:

Objective of the program is to find stochastic dynamics of a random variable$\bar{Y}$ that is dependent on X but is
uncorrelated with X. Meaning variance of random variable$\bar{Y}$ systematically depends on X but in a way that$\bar{Y}$
is uncorrelated with X. We suppose that univariate stochastic dynamics of both X and$\bar{Y}$ are already known to us in
the form of moments but we want to find two dimensional stochastic dynamics of$bar{Y}$ that capture the dependency of
its variance on X.

Context of the Program and Preparing data of $\bar{Y}$:

Context of the program is that we have the joint observation data of two correlated random variables X and Y. We can
find univariate Z-series of both X and Y from this data. We can also calculate the correlation between hermite
polynomials of hermite-series of both X and Y. Hermite-series of X and Y are given respectively as

$$\,X(Z_x)\,=\, ah_0 \, +\, ah_1 \,H_1(Z_x) \,+\, ah_2 \,H_2(Z_x) \,+\, ah_3 \,H_3(Z_x) \, \\

\,Y(Z_y)\,=\, bh_0 \, +\, bh_1 \,H_1(Z_y) \,+\, bh_2 \,H_2(Z_y) \,+\, bh_3 \,H_3(Z_y) \, $$

We want to divide the random variable Y into two parts, one is conditional expectation part of Y (E(Y|X)) that is
perfectly correlated with X and second is part of Y ($\bar{Y}$ ) that is orthogonal to X. We can do this by calculating
hermite correlations and then using the correlations to find conditional expectation part. But another simple way is do
a regression of Y on hermite polynomials of X.

Suppose we have P joint observations of random variables$X_p$$\,(p\,=\,1\, \ldots P)$ and$Y_p$$\,(p\,=\,1\, \ldots P)$ .
From$X_p$ and$Y_p$ , We would have to invert equations below to find$Z_{X,p}$$\,(p\,=\,1\, \ldots P)$ and then use the
regression equation

$
$\,Y_p\,=\,c_0\,+\,c_1\,H_1(Z_{X,p})\,+\,c_2\,H_2(Z_{X,p})\,+\,c_3\,H_3(Z_{X,p})\,+\,c_4\,H_4(Z_{X,p})\,+\,c_5\,H_5(Z_{X,p})\,$
$

This way we find the regression coefficients which are given by ($c_0,\,c_1,\,\dots,\,c_M$)

Now we use the regression equation with each of the pth observations of X to find the conditional value of pth
observation of Y. This is simply explainable part of regression

$
$\,E\left[Y_p\,|\,X_p\right]\,=\,c_0\,+\,c_1\,H_1(Z_{X,p})\,+\,c_2\,H_2(Z_{X,p})\,+\,c_3\,H_3(Z_{X,p})\,+\,c_4\,H_4(Z_{X,p})\,+\,c_5\,H_5(Z_{X,p})\,$
$

The above equation is repeated for all P observations of X.

From above calculated conditional expected values of each of the pth observation of$Y_p$ given$X_p$ , we are able to
calculate the orthogonal and uncorrelated part of the pth observation of$Y_p$ denoted as$\bar{Y}_p$ as

$$\,\bar{Y}_{p}\, =\, Y_p\,-\, \,E\left[Y_p\,|\,X_p\right]\,$$

In many cases where Y is a dependent variable as in the case of transition increment, this orthogonal random variable
part given as$\bar{Y}$ would also be dependent on X even though it would be orthogonal to X and would not have any first
order correlation with X.

Using above procedure, we can get data of P observation of$\bar{Y}$ that we can use to calculate its various moments.
The above calculations to prepare data of$\bar{Y}$ are done in the case of transition increments of X in the matlab
function given as EstimateDynamicCoeffParameters(X).

After choosing an appropriate two dimensional Z-series/ Hermite-series form of$\bar{Y}$ in next section, We will use
optimization on above calculated moments of$\bar{Y}$ to find coefficients of the 2D Hermite- series form we would have
selected as best possible.

Candidate Form of 2D Hermite-series of $\bar{Y}$

A simple form of stochastic dynamics of $\bar{Y}$ that is dependent on X could be selected as

$$\bar{Y}\,=\,g_0(X)\,+\,g_1(X) \,Z_y\,+\,g_2(X)\,\left({Z_y}^2\,-\,1\right) $$

since all of functions involved in above stochastic form given by$g_0(X)$ ,$g_1(X)$ , and$g_2(X)$ can be represented in
Z-series of X with$Z_x$ as its argument, the above stochastic form could be equivalent (give or take some change in
order of 2D hermite series) to 2D hermite series form below.

\begin{align}

X(Z_y \, , \, Z_x)\, &=\, \Big[\, bh_{0,0} \, + \, bh_{0,1} \,H_1(Z_x) \,+\, bh_{0,2} \, H_2(Z_x) \,\, + \, bh_{0,3}
\,H_3(Z_x)\,\Big] \\

&+\, \Big[ \, bh_{1,0} \, + \, bh_{1,1} \,H_1(Z_x) \,+\, bh_{1,2} \, H_2(Z_x) \, + \, bh_{1,3} \,H_3(Z_x)\, \Big] \,
H_1(Z_y) \, \\

&+\, \Big[ \, bh_{2,0} \, + \, bh_{2,1} \,H_1(Z_x) \,+\, bh_{2,2} \, H_2(Z_x) \, \, + \, bh_{2,3} \,H_3(Z_x)\, \Big] \,
H_2(Z_y) \, \\

\end{align}

However, we notice that$g_0(X)$ in the above candidate stochastic form would be directly correlated with random variable
X which is not what we want. Therefor I want friends to notice that in equivalent 2D hermite form, the zeroth hermite
term with respect to$Z_y$ is given as

$$\Big[\, bh_{0,0} \, + \, bh_{0,1} \,H_1(Z_x) \,+\, bh_{0,2} \, H_2(Z_x) \,\, + \, bh_{0,3} \,H_3(Z_x)\,\Big] $$

In a 2D hermite form, first order correlation can appear only with respect to terms in zeroth hermite (with respect to
appropriate Z,$Z_x,\, or\, Z_y$ . Since zeroth hermite (with respect to Z_y) cannot be a function of$Z_x$ , we choose
the right form for 2D stochastic of$\bar{Y}$ in next section.

True Possible Form of 2D Hermite-series of $\bar{Y}$

In light of discussion in previous paragraph, we know that there can be no$Z_x$ dependent dynamics in zeroth hermite
with respect to$Z_y$ . Therefore a simple form of stochastic dynamics of$\bar{Y}$ that is dependent on X could be
selected as

$$\bar{Y}\,=\,g_1(X) \,Z_y\,+\,g_2(X)\,\left({Z_y}^2\,-\,1\right) $$

since all of functions involved in above stochastic form given by $$g_1(X)$ , and$g_2(X)$ can be represented in Z-series
of X with$Z_x$ as its argument, the above true stochastic form could be equivalent to 2D hermite series form below.

\begin{align}

\bar{Y}(Z_y \, , \, Z_x)\, &=\,\, \Big[ \, bh_{1,0} \, + \, bh_{1,1} \,H_1(Z_x) \,+\, bh_{1,2} \, H_2(Z_x) \, + \,
bh_{1,3} \,H_3(Z_x)\, \Big] \, H_1(Z_y) \, \\

&+\, \Big[ \, bh_{2,0} \, + \, bh_{2,1} \,H_1(Z_x) \,+\, bh_{2,2} \, H_2(Z_x) \, \, + \, bh_{2,3} \,H_3(Z_x)\, \Big] \,
H_2(Z_y) \, \\

\end{align}

In the above 2D Hermite-series there are dynamics of variance that depend on$Z_x$ but zeroth hermite with respect to
$Z_y$ has no dependence on$Z_x$ . I want to emphasize that this is only one of the possible forms since for some random
variables we might have to increase order of 2D Hermite-series in one or both directions. But if$\bar{Y}$ has to
maintain orthogonality with X, there can be no polynomials terms in Z_x associated with zeroth hermite of$Z_y$ .

Description of Numerical Problem:

We want to find the coefficients of above two dimensional hermite series so that numerically calculated moments from
data of orthogonal part given by$\bar{Y}$ are perfectly retrieved from the optimized coefficients of the above selected
2D hermite series form.

Preliminaries Before optimization:

Calculation of 2D Hermite-Series Variance

Before starting the optimization, we standardize the moments of$Y$ which means that variance of the 2D hermite-series
should always be one. We also use unity variance property to fix one of the coefficients of hermite series. In above
selected hermite series form the variance would be calculated as

\begin{align}

Var[\bar{Y}]\,&=\, {bh_{1,0}}^2\,+\,{bh_{1,1}}^2\,+\,2\,{bh_{1,2}}^2\,+\,6\,{bh_{1,3}}^2\, \\

&\,2\, {bh_{2,0}}^2\,+\,2\,{bh_{2,1}}^2\,+\,4\,{bh_{2,2}}^2\,+\,12\,{bh_{2,3}}^2\,

\end{align}

In the iterative perturbations numerical procedure, the variance is maintained at unity. When we perturb any coefficient
in the iterative perturbation procedure, we readjust the value of$ {bh_{1,0}}$ so that unit variance is retrieved. This
is done by calculating the value of$Var[\bar{Y}]\,$ from equation below after the perturbation but without including
${bh_{1,0}}$

\begin{align}

Var[\bar{Y_0}]\,&=\, \,{bh_{1,1}}^2\,+\,2\,{bh_{1,2}}^2\,+\,6\,{bh_{1,3}}^2\, \\

&\,2\, {bh_{2,0}}^2\,+\,2\,{bh_{2,1}}^2\,+\,4\,{bh_{2,2}}^2\,+\,12\,{bh_{2,3}}^2\,

\end{align}

and then fixing the value of coefficient  $ {bh_{1,0}}$  by the following equation as

$$bh_{1,0}\,=\,\sqrt{1-Var[\bar{Y_0}]}$$

Conversion of 2D Hermite-Series Coefficients to 2D Z-series Coefficients

Even though modelling the required stochastic form was convenient in Hermite series since we could maintain
orthogonality and zero correlations very easily but for calculation of moments, we have to convert 2D hermite-series to
2D Z-series.

Using the calculations from yesterday's program, we can convert 2D Hermite Series coefficients to 2D Z-series
Coefficients, and we get

\begin{align}

b_{0,0}&=-\left( bh_{2,0} \,-\,bh_{2,2} \right)\,\\

b_{0,1}&=\, - \left( bh_{2,1} \,-\,3\,bh_{2,3} \right)\\

b_{0,2}&= \,-bh_{2,2} \,\\

b_{0,3}&=\,-bh_{2,3} \\

b_{1,0}&=\,\left( bh_{1,0} \,-\,bh_{1,2} \right)\,\,\\

b_{1,1}&= \,\left( bh_{1,1} \, - 3\, bh_{1,3}\right)\, \,\\

b_{1,2}&=\, bh_{1,2} \,\\

b_{1,3}&=\, bh_{1,3}  \\

b_{2,0}&=\,\left( bh_{2,0} \,-\,bh_{2,2} \right)\, \\

b_{2,1}&=\,\left( bh_{2,1} \, -\,bh_{2,3} \right)\, \\

b_{2,2}&= \,bh_{2,2} \\

b_{2,3} &= \, bh_{2,3} \\

\end{align}

I think in the given program, my coefficients are in reverse which does not make a difference in calculations but I will
fix them in new version to maintain convention.

Objective Function For optimization:

For optimization of coefficients to moments, we calculate moments from our trial coefficients with kth moment generated
from trial coefficients denoted as$\mu(k)$ and target kth moment is denoted as$mu_0(k)$ . We use different weights in
the optimization for different moments. Since we are using standardized moments, typically smaller moments have a lot
higher weight and larger moments have a lot smaller weight. We can also strategically alter the weights during
optimization especially when one of the moments has already been well optimized, we increase its weight in the objective
function so deviations from its optimized values are highly penalized while the iterative algorithm continues to fit
other moments that have already not been fitted.

This objective function is calculated as

$$\,Obj_N\,=\, \sum\limits_{k=1}^N\, w_k\,{\left(\mu(k)\,-\,\mu_0(k)\right)}^2$$

Details of Iterative Perturbation Optimization Procedure:

We have to iterate over eight coefficients of the following 2D hermite-series

\begin{align}

Var[\bar{Y}]\,&=\, {bh_{1,0}}^2\,+\,{bh_{1,1}}^2\,+\,2\,{bh_{1,2}}^2\,+\,6\,{bh_{1,3}}^2\, \\

&\,2\, {bh_{2,0}}^2\,+\,2\,{bh_{2,1}}^2\,+\,4\,{bh_{2,2}}^2\,+\,12\,{bh_{2,3}}^2\,

\end{align}

In actual procedure, we serially perturb over seven coefficients of above hermite series with a small perturbative step
roughly inversely proportional to variance of the hermite polynomial associated with the coefficient and after
perturbation in each coefficient we fix the first coefficient$bh_{1,0}$ so that standardized variance remains unity and
accept the perturbation change if the objective function improves. Our perturbation strategy is to add the perturbation
step size in one of the coefficients, then adjust bh_{1,0} from variance and then accept the perturbative change if the
objective function decreases below the best objective function and update the parameter in that dimension. If the
objective function does not decrease by addition of perturbation step in that dimension, you subtract the perturbation
step in the same coefficient dimension, and alter bh_{1,0} to keep unity variance and then see if the objective function
decreases. Again decrease in parameter is accepted if the objective function decreases with perturbation in that
direction. If the objective function does not decrease in both directions by adding or subtracting the perturbative
step, we do not change the coefficient and keep it at its old value from previous iteration. So we serially iterate over
all coefficients one by one. And when there is no decrease in objective function after adding and subtracting the
perturbative steps sizes in all coefficient dimensions, we cut the step size along all dimensions to .95 or .9 of the
previous step size and optimization starts working again.

Initial perturbation step size is very small and is kept proportional to inverse of variance of hermite polynomial
associated with the particular coefficient.

After every few hundred iterations, we reset the perturbation step and make it equal to a fraction (like possibly 1/50)
of the already found best fir values of the coefficients.

In our case first moment was zero and second moment is kept fixed all along iterative optimization procedure. We have
adopted this strategy to alter the coefficients so that only three moments are first calibrated with a three moment
objective function. This is particularly easy and we use about 500 iterations for this purpose in first stage. After 500
perturbations, we switch to four dimension optimization. But in order to do that we need a four coefficient best
objective function for decision making. At 500th iteration, when switching from three moments optimization to four
moments optimization, we use the calibrated coefficients from three moments optimization and use them to calculate four
moments and these four moments from best fit values are then used to find best initial objective function that has to be
improved in four moments calibration. At the same time, after switching to four moments optimization, we also increase
the weight of the third moment that has already been fixed several times so that deviations from already fixed third
moment are highly penalized while perturbing the coefficients to find the best fit to fourth moments. We use 500th to
4000th iterations to find the best fit to fourth moment. At 4000th iteration, we move from four moment optimization to
five moments optimization. Like before, we project best fit coefficients from four moments optimization to five moments
and then calculate the initial five moments best fit objective function. We also increase the weight on already
calibrated third and four moments further so they are kept in close calibration while  iterative perturbation procedure
optimizes for fifth moment. We repeat the same process when we switch from five moments optimization to six moments
optimization on 10000th iteration.

In the program all seven hermite coefficients that we iteratively perturb to find best values are kept in a singly array
called cH.
```

---

### #2599 — Amin (Topic Author)
*January 20, 2025, 5:24 AM*

Friends, today, we will seen inauguration of new president chosen by American people. And just like most of the
Americans, people all across the world are watching this very closely since policies of new American government will
affect people all across the world in so many ways. With arrival of new government, there will be changes in foreign
policy and large number of American staff in foreign embassies of United States will be shuffled.

Our country Pakistan is rather a relatively unimportant place from mainstream American perspective and therefore I would
suppose that decisions about how to manage our country and who will appoint the political and other staff in the embassy
here are not made by the top political elite in United States and not much attention or importance is given to
management and choice of diplomatic staff that comes to our country on higher level. Unfortunately, this has resulted in
a very large scale mind control of talented people in Pakistan because  mid or lower level staff in foreign affairs
department in US government continues to make some bad decisions about continuing mind control in our country.

I want to request good American people to use their influence with the government and ask some good and prominent
politicians to keep the portfolio of management of foreign policy in Pakistan with themselves and not let everybody make
decisions to appoint people in Pakistan. As most of the staff in foreign embassies of United States is going to be
reshuffled now, please recall all those people from Pakistan who are involved in mind control. And please send very good
human beings who are keenly interested in development of our large but extremely poor country. I must say that American
embassies have to protect rightful American interests at all cost and must make sure that terrorism and radicalism that
is a threat to all countries, must be eradicated from Pakistan. But some people previously indulged in the practice of
mind control of talented people in Pakistan and I request good American people to please end all such practices in our
poor country.

---

### #2600 — Amin (Topic Author)
*January 20, 2025, 9:30 PM*

Friends, it is 2 am at night in Pakistan. I went to bed a bit earlier at 10:30 pm but I have not been able to sleep for
more than one hour. Despite that I was very tired after a hectic day, I could not sleep properlu and woke up two hours
ago since they have been targeting my head with microwaves for past several hours and my head is exploding with pain. It
is due to unbearable nature of this torture that I immediately decided to write this post in the middle of the night.

Yesterday, I left my home at 12:30 pm and spent almost all the day in the city buying food and other little things. And
when I was away, mind control agents were fixing special torture equipment in my room. When I came home and entered my
room at night, I was greeted by huge gas in my room. I had decided to not work at night and thought that I would have a
good night's sleep and start working steadily the next day. But instead of a good night's sleep I am greeted by huge
microwaves forced into my head and I have strong pain in my head. Due to extremely heavy head, I doubt that I would be
able to do any productive work in the coming day. And mind control agents have released huge gas in my room at the time
of my writing this post.

Friends, please protest to American government against the increasing nature of torture and approach responsible people
in the American government to end innocent people's torture.

---

[← Previous](page_051.md) | [Index](index.md) | [Next →](page_053.md)
