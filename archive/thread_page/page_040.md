# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 40 of 65** — Posts #1951–#2000

[← Previous](page_039.md) | [Index](index.md) | [Next →](page_041.md)

---

### #1951 — Amin (Topic Author)
*September 14, 2023, 6:56 PM*

>
> Friends, I have calculated 2D hermite-series but I have not been able to graph it with change of variable from
bivariate normal. Unless we compare graph from our hermite series with 2D Parzen density graaph, we cannot be sure if
our analytics are right. It can still take 2-3 days to properly complete the work and I am working on it full time.
>
> I had an antipsychotic injection on Thursday before last Thursday. I have not been able to work well after that and
could work only 1-2 hours everyday. But I am somewhat better now and hopefully would get the remaining work done in a
few days.
>
> Microwave torture has somewhat deceased but when I try to work and become somewhat productive, they increase their
torture and start giving me light pain in left temple. Though many times it is not very high pain but it is still enough
to put me off to not be able to work after that. Another new torture technique they have started is that they target EM
waves on my teeth and from time to time, I feel sudden pain in many of my teeth.
>
> Anyway, I hope to try to do good research in coming weeks and want to concentrate on my research.
>
.

Friends, I am sure my 2D Hermite Series is right. I am thinking more about proper plotting of the 2D density from the 2D
Hermite Series. If the plotting works, that is good but even if it does not work, I will post the program on this
weekend.

I think a proper implementation of this program to represent a 2D SV density with a 2D hermite series is a requirement
before we could do a regression of derivatives payoff on the asset and volatility as in delta and vega while accounting
for correlations.

Though I said in my previous post that we could do a regression of payoffs on delta and vega using Legendre polynomials
but regression is forward looking(as opposed to backward looking equations) and rethinking the whole thing, I realize
that we would have to do it in hermite polynomial set up in a monte carlo framework.

Though I am sure that there are many insights to be gained from possible solution of backward equations with Legendre
polynomials, what we are trying to do in 2D SV set up with hermite polynomials is also truly meaningful and could lead
to insightful hedging of the derivatives differently from the previously used approaches. Imagine if we could do it well
in a good interest rate model and do a multivariate regression on various interest rates/LIBOR rates, it will be a very
very rewarding model in terms of practical applications.

I was losing some enthusiasm for the project but I am again very keen to find a proper solution to the problem of 2D
hermite representation of asset in a 2D SV setting in a very good way.

I will be posting an interim program over the weekend but I will continue my efforts for a proper solution in every way
for next week and more.

---

### #1952 — Amin (Topic Author)
*September 14, 2023, 9:29 PM*

Friends, I have tried to think more about the problem in my calculation of 2D hermite representation of 2D SV SDEs. I
think I have realized the error. I will try to give friends some idea about the calculations.

We need a 2D Parzen numerically calculated density of volatility and asset on an equidistant square grid. Volatility is
one dimensional and can easily be mapped on one dimensional standard normal density. However asset lines cannot be
independently mapped on an independent standard normal density. Instead every asset line on different volatility grid
points have their own CDF and hence a different mapping on standard normal density.

if m is index for volatility and n is index for asset, V can be mapped as$V(Z_m)$ . But X lines can be mapped only as
$X(Z_{n,m})$ with two dimensional indexing (Zs being different for V and X).

I was earlier naively calculating a single mapping of X on Z using average CDF which was very incorrect. This CDF will
be different for every X line associated with different volatility points.

I am sure after accounting for this error, I will get a correct two dimensional Z-series/Hermite Series since basic math
is simple. But I still foresee that I will have to make some improvisations for proper 3D graphing.

Though I have been working on the problem for more than one week, I have not been able to think very deeply for longer
time on it since mind control agents cause strong pain in my left temple every time I try to work on the problem or
think deeply about it. Even now they were trying to do the same and caused huge almost unbearable pain in my left temple
but I realized that this pain has something to do with the ears and I washed my ears(especially left ear) very carefully
and then put a compressed tissue in my left ear to de-calibrate(change the propeties of) the EM waves going into the
ears and I was able to think better.

---

### #1953 — Amin (Topic Author)
*September 15, 2023, 7:14 PM*

Friends, I have been able to verify that my calculation of 2D Hermite Series representation of 2D SV monte carlo density
is correct. I calculated the coefficients of 2D Hermite Series from the 2D Parzen monte carlo density using algorithm
similar to what I had used for calculation of coefficients of 1D Hermite Series(with inner product).

The calculated 2D hermite series is a 2D polynomial in standard normals Zx and Zv. In order to verify that my 2D hermite
series coefficients are good, I integrated 2D Series over Zv and also made an appropriate normalization with integral of
SV density. And then I got the result as a marginal 1D Hermite series in Zx. When I plotted this analytic 1D Hermite
Series density of asset and compared it with numerical 1D Parzen density of the SV asset, both densities were exactly
the same on the overlaid graph. So I can confirm that original 2D Hermite density calculations algorithm is perfectly
good.

I will post my matlab programs I used to do this over the weekend.

Here is an overlaid graph from one of the examples I ran over my computer. Green is numerical parzen density of asset in
SV setting while blue is marginal density of SV asset calculated from 2D hermite series  that is in turn derived from 2D
monte carlo density using inner product. These are just initial graphs and I did not use very large number of monte
carlo paths since my computer is too slow.

[![Image](../images/i.postimg.cc/0NZv435b/Hermite2-DAsset01.png)](https://postimages.org/)

I had the idea of graphing SV asset density after calculation of marginal density to check whether my 2D Hermite series
is right. But in next few days I will continue to work on a 2D graph of the SV Asset density as a function of both asset
and volatility. I hope that I will have a program ready that grapsh 2D density early next week.

Here are parameters of SV SDEs in appropriate mean reverting SDEs for asset and volatility.

X0=1.0;

alpha1=0;

alpha2=1;

kappaX=0.0;

thetaX=0.0;

a=kappaX*thetaX;

b=-kappaX;

rho=0.15;

sigma1=.4;

gammaV=.5;

gammaX=.65;

%%%%%%%%%%%%%

V0=1.0;

thetaV=1.0;

kappaV=1.50;

mu1=kappaV*thetaV;

mu2=-kappaV;

beta1=0;

beta2=1;

gamma=.85;

sigma0=.75;

%%%%%%%%%%%%

dt=.03125;

Tt=32*4;

T=Tt*dt;

---

### #1954 — Amin (Topic Author)
*September 15, 2023, 7:55 PM*

Friends, sorry. I tried high negative correlation and the program does not seem to work very well with high negative
correlations. I still suspect that my Z-series is right but I will have to be careful with integrating over Zv to get
marginal density of asset. Anyway, I am working to fix all the different 1D and 2D graphing and other related issues.

---

### #1955 — Amin (Topic Author)
*September 16, 2023, 8:29 PM*

Friends, my program does not work for correlated SV models but I still hope to post it tomorrow for uncorrelated SV
models.

I have been thinking of several alternatives for example calculating correlations numerically between various Zs and
similar other ideas.

Here I want to tell friends that my first approach to solve 2D SV problem was not through inner product of 2D Hermite
polynomials with parzen density. I thought I could do it by matching moments within a 2D Hermite series framework but
when I closely approached the problem, I faced many difficulties. Today when I was reviewing various possibilities, and
wrote down equations, I realized that analytic matching of moments in a 2D Series framework could be possible and some
problems that deterred me earlier could be resolved.

In order to understand, there are probably 65 or so terms in a 2D hermite series. Each volatility hermite polynomial
multiplies with an expression of eight terms that are various hermite polynomials in X. Briefly, I want to take every
order of hermite polynomial in volatility Z one by one and match moments of (the combined expression including new
orthogonal Z's)sum of  all the Zx hermite polynomials multiplying that particular volatility related hermite. So there
would be roughly seven or eight moment matchings in the basic model (in addition to some others) to advance one time
step.

I am reasonably sure that this should work well. I want to try it again in next 2-3 days. But only when we get good
results that we could know that it actually does work.

There is a benefit to matching moments because in the simulation equation noise generating Z's even in correlated SV
models are uncorrelated on the individual variable level so dealing with correlations should be no more difficult if the
method works.

Let us see how it goes in next few days.

---

### #1956 — Amin (Topic Author)
*September 17, 2023, 9:34 PM*

I will give a detailed review with latexed equations tomorrow. In the meanwhile matlab programs to calculate 2D hermite
series from 2D SV monte carlo constructed parzen density are given below. I have tried to give comments on the main
programs to make it easier for friends who are reasonably familiar with the background to understand the programs.

Volatility and asset equations are

Vt(0)=V0;

dVt=(mu1*Vt^beta1 + mu2*Vt^beta2)*dt+sigma0 * Vt^gamma * dz1(t)

Xt(0)=X0

dXt=(a*Xt^alpha1+b*Xt^alpha2)*dt+sigma1* Vt^gammaV * Xt^gammaX *dz2(t);

First a graphical comparison of non-correlated-IR like SV equations with mean reversion both in asset and volatility.
Programs used to make above graph follow in next post in a few minutes.

Parameters of the density as given in above equations are

X0=.05;

alpha1=0;

alpha2=1;

kappaX=.850;

thetaX=0.0250;

a=kappaX*thetaX;

b=-kappaX;

rho=-0.0;

sigma1=.8;

gammaV=.5;

gammaX=.7;

%%%%%%%%%%%%%

V0=1.0;

thetaV=.250;

kappaV=1.50;

mu1=kappaV*thetaV;

mu2=-kappaV;

beta1=0;

beta2=1;

gamma=.85;

sigma0=.7;

%%%%%%%%%%%%

dt=.03125;

Tt=32*4;

T=Tt*dt;

Here is the graph of the analytic density calculated from the 2D Hermite series of the SV asset by integrating over
volatility to calculate the marginal 1D Hermite series of the asset.

There is a very slight mismatch between graphs at peak of the density but this is initial prototype and we will have to
work to refine the method to perfection. Playing around with number of paths, grid spacing and related parameters might
help in better reconciling both graphs.

[![Image](../images/i.postimg.cc/qMCxTCPc/Hermite2-DAsset02.png)](https://postimg.cc/3dYvjWJW)

---

### #1957 — Amin (Topic Author)
*September 17, 2023, 9:43 PM*

Here are the matlab functions for method used to construct graphs in previous post.

I will explain tomorrow but quickly

If C are 2D hermite Coeffs as calculated in this program

Hermite Series representation of 2D random variable would be given by

double sum equation below as

$\sum_{n=0}^{n=7} \sum_{m=0}^{m=7} \, C(n+1,m+1) \, He(n,Zx) \, He(m,Zv)$

mismatch between hermite indices and indices in C is due to that matlab starts indices from one and not from zero. This
is for C as calculated in the current program.

.

```
function [] = SVMonteCarloDensityWith2DHermitesWilmott()

%Copyright Ahsan Amin. Infiniti derivatives Technologies.
%Please fell free to connect on linkedin: linkedin.com/in/ahsan-amin-0a53334

%Volatility and asset equations are
%Vt(0)=V0;
%dVt=(mu1*Vt^beta1 + mu2*Vt^beta2)*dt+sigma0 * Vt^gamma * dz1(t)
%Xt(0)=X0
%dXt=(a*Xt^alpha1+b*Xt^alpha2)*dt+sigma1* Vt^gammaV * Xt^gammaX *dz2(t);
%=rho *dt

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

X0=.05;
alpha1=0;
alpha2=1;
kappaX=.850;
thetaX=0.0250;
a=kappaX*thetaX;
b=-kappaX;

rho=-0.0;
sigma1=.8;
gammaV=.5;
gammaX=.7;
%%%%%%%%%%%%%
V0=1.0;
thetaV=.250;
kappaV=1.50;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.85;
sigma0=.7;
%%%%%%%%%%%%

dt=.03125;
Tt=32*4;

T=Tt*dt;

%%%%%%%%%%%%%%%%%%%%%%%%5

%rng(29079137, 'twister')
rng(15898837, 'twister')
paths=600000;
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

X=real(X);
X(X<0)=0;
V(V<0)=0;

SVolMeanAnalytic=thetaV+exp(-kappaV*T)*(V0-thetaV)
SVolMean=sum(V(1:paths))/paths
AssetMeanAnalytic=thetaX+exp(-kappaX*T)*(X0-thetaX)
AssetMean=sum(X(1:paths))/paths

str=input("Look at monte carlo Mean of X and V")

NoOfBinsV=200;
NoOfBinsX=200;

[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv]=
Find2DDensityAndCDFFromSimulation_Infiniti(X,V,paths,NoOfBinsX,NoOfBinsV);
%Please look at matlab file of above function for etailed explanation of
%all its input and output parameters.

str=input("Look at sizes of variables----1")

surf(Xn,Vm,XYProbDensity2D)

%hold on

MeanX=sum(X(1:paths))/paths
MeanV=sum(V(1:paths))/paths

str=input("Look at 3D graphs")

%Below calculate Coeffs of 2D Hermite products.
%Oxn is order of Zx hermites. ranges from 1 to 8 in indexing or (0 to 7 in reality)
%Ovm is order of Zv hermites. ranges from 1 to 8 in indexing or (0 to 7 in reality)
%HermiteH(Oxn,Zx(nn,mm)) is a small function that caclulates Oxn order hermite at Zx(nn,mm) value
%HermiteH(Ovm,Zv(mm)) caclulates Ovm order hermite at Zy(mm) value
%Below Eq calculates 2D Coeffs with inner product of coordinates of 2D uniform grid with
%product of X and V hermites.

C(1:8,1:8)=0;

for Oxn=1:8
    for Ovm=1:8
        for nn=1:(NoOfBinsX+1)
            for mm=1:(NoOfBinsV+1)
               
C(Oxn,Ovm)=C(Oxn,Ovm)+1/factorial(Oxn-1)/factorial(Ovm-1).*Xn(nn).*Vm(mm).*HermiteH(Oxn-1,Zx(nn,mm)).*HermiteH(Ovm-1,Zv(mm)).*XYProbMass2D(nn,mm);

            end
        end
    end
end

C

%If C are 2D hermite Coeffs as calculated in above equation
%Hermite Series representation of 2D random variable would be given by
%double sum equation below as
%Sum_{n=0}^{n=7} Sum_{m=0}^{m=7} C(n+1,m+1) He(n,Zx) He(m,Zy);

str=input("Look at Coefficients of 2D Hermite products")

%Below we calculate 1D Hermite Series for volatility.
%We only need to calculate the mean (zeroth hermite) aH0 of the volatility
%random variable.

aH0=0;
aH(1:7)=0;
for nn=1:IndexMaxV
aH0  =  aH0+Vm(nn).*VProbMass(nn);
aH(1)=aH(1)+Vm(nn).*Zv(nn).*VProbMass(nn);
aH(2)=aH(2)+.5*Vm(nn).*(Zv(nn).^2-1).*VProbMass(nn);
aH(3)=aH(3)+1/6*Vm(nn).*(Zv(nn).^3-3*Zv(nn)).*VProbMass(nn);
aH(4)=aH(4)+1/24*Vm(nn).*(Zv(nn).^4-6*Zv(nn).^2+3).*VProbMass(nn);
aH(5)=aH(5)+1/120*Vm(nn).*(Zv(nn).^5-10*Zv(nn).^3+15*Zv(nn)).*VProbMass(nn);
aH(6)=aH(6)+1/720*Vm(nn).*(Zv(nn).^6-15*Zv(nn).^4+45*Zv(nn).^2-15).*VProbMass(nn);
aH(7)=aH(7)+1/720/7*Vm(nn).*(Zv(nn).^7-21*Zv(nn).^5+105*Zv(nn).^3-105*Zv(nn)).*VProbMass(nn);
end

%Below we calculate the Hermite series of asset by integrating over the
%volatility to get marginal series of asset. When we integrate over
%volatility, all volatility hermites(alone or as products with X-hermites)
%in the 2D asset series go to zero(they all have mean zero).
%So basically all volatility terms go to zero and we are left with
%one dimensional array containing terms from 2D series where
%volatility hermites in the product had order zero. This order zero is
%represented by volatility index one in the 2d array of coeffs C(n,m);
%So our 1D asset series is from the line C(1:8,1) where volatilit hermites
%are zero. This is very interesting.

bH0=C(1,1);
bH(1:7)=C(2:8,1);

%Above bH0 is asset Hermite series coeff of zeroth order hermite and
%bH(1:7) represent hermites from 1st to 7th order.

bH0=bH0/aH0;
bH=bH/aH0;

%Above, we need to normalize the asset hermite series with expected value
%of volatility since we integrated over the volatility. Just like in
%Conditioning when we integrate over a variable to get marginal density and
%then we have to divide with the integral of the integrated density as
%well. Similalry, Here we have to divide with the mean/expected value of
%volatility hermite series(which is integral of the volatility hermite series)
%to normalize our asset equation hermite coefficients.

%Below we convert from hermite series to Z-series of the asset for
%plotting.
[b0,b] = ConvertHCoeffsToZCoeffs(bH0,bH,7);

bH0
bH

b0
b

str=input("Look at 1D Coeffs of X")

dNn=.1;%.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=101;%45*4;  % No of normal density subdivisions
NnMid=((1+Nn)/2)*dNn;
Z(1:Nn)=(((1:Nn)*dNn)-NnMid);

XX(1:Nn)=b0;
for nn=1:7
   XX(1:Nn)=XX(1:Nn)+b(nn)*Z(1:Nn).^nn;
end

wnStart=1;
%Below we make calculations of density in original coordinates by doing
%change of probability derivative with respect to gaussian density.
DfXX(wnStart:Nn)=0;
for nn=wnStart+1:Nn-1

    DfXX(nn) = (XX(nn + 1) - XX(nn - 1))/(Z(nn + 1) - Z(nn - 1));

    %Change of variable derivative for densities
end
DfXX(Nn)=DfXX(Nn-1);
DfXX(1)=DfXX(2);

pXX(1:Nn)=0;
for nn = wnStart:Nn

    pXX(nn) = (normpdf(Z(nn),0, 1))/abs(DfXX(nn));
end

%Below make parzen density of asset in SV equations and also plot the
%analytic density of asset.
 NoOfBins=2400;
 MaxCutOff=100;

 [XDensity,IndexOutX,IndexMaxX] = MakeDensityFromSimulation_Infiniti_NEW(X,paths,NoOfBins,MaxCutOff );
 plot(XX(2:Nn-1),pXX(2:Nn-1),'b',IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'g');

title('Asset Density(in SV model) From Analytic Hermite Series Calculated from 2D Hermite Series VS Numerical Parzen
Density of Asset');%,sprintf('theta= %f', theta), sprintf('kappa = %f', kappa),sprintf('sigma = %f', sigma0),sprintf('T
= %f', T));

legend({'Marginal Asset Density from 2D Hermite Series','Parzen Density From Monte Carlo'},'Location','northeast')

str=input('blue line is density of Asset from Hermite Series, green is numerical density from monte carlo.');

end
```

.

.

.

```
function [XYProbDensity2D,XYProbMass2D,XProbMass,YProbMass,IndexMaxX,IndexMaxY,Xn,Ym,Zx,Zy] =
Find2DDensityAndCDFFromSimulation_Infiniti(X,Y,Paths,NoOfBinsX,NoOfBinsY)

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
%Zx----- this is a 2D array. This returns the value of standard normal associated with 1D Xn grid for every
%Ym grid cell. Given a certain grid cell Ym, we calculate CDF along all 1D X grid
%cells with the same Ym. This standard normal value is derived from inversion of univariate CDF on X-grid
%or X-axis associated with each Y grid cell. Zx(n,m) is a 2D array.
%Zy----- this is the value of standard normal associated with Ym at center
%of each grid cell on Y-axis. This is derived from inversion of univariate CDF on Y-grid
%or Y-axis. This is 1D array. This is used for vol which is independent of
%X.

Xmin=999999;
Xmin1=999999;
Xmin2=999999;
Xmax=0;
Xmax1=0;
Xmax2=0;

Ymin=999999;
Ymin1=999999;
Ymin2=999999;
Ymax=0;
Ymax1=0;
Ymax2=0;
meanX=0;
meanY=0;
for p=1:Paths

meanX=meanX+X(p)/Paths;
meanY=meanY+Y(p)/Paths;
if(Xmin>real(X(p)))
    Xmin2=Xmin1;
    Xmin1=Xmin;
    Xmin=real(X(p));
end
if(Xmaxreal(Y(p)))
    Ymin2=Ymin1;
    Ymin1=Ymin;
    Ymin=real(Y(p));
end
if(YmaxIndexMaxX)
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

%BinSizeX
%BinSizeY

%str=input("Look at BinSizes");

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
    if((XCDF(1,mm)>0) && (XCDF(1,mm).9999999)
        Zx(1,mm)=8;
    end
    for nn=2:IndexMaxX
        XProbSum(nn,mm)=XProbSum(nn-1,mm)+XYProbMass2D(nn-1,mm)*.5+XYProbMass2D(nn,mm)*.5;
        if(YProbMass(mm)>0)
            XCDF(nn,mm)=XProbSum(nn,mm)./YProbMass(mm);
        else
            XCDF(nn,mm)=0;
        end
        if((XCDF(nn,mm)>0) && (XCDF(nn,mm).9999999)
            Zx(nn,mm)=8;
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
end

end
```

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

```
function [ValHermite] = HermiteH(n,Z)

if(n==0)
    ValHermite=1;
elseif(n==1)
    ValHermite=Z;
elseif(n==2)
    ValHermite=Z.^2-1;
elseif(n==3)
    ValHermite=Z.^3-3*Z;
elseif(n==4)
    ValHermite=Z.^4-6*Z.^2+3;
elseif(n==5)
    ValHermite=Z.^5-10*Z.^3+15*Z;
elseif(n==6)
    ValHermite=Z.^6-15*Z.^4+45*Z.^2-15;
elseif(n==7)
    ValHermite=Z.^7-21*Z.^5+105*Z.^3-105*Z;
end

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

Xmin=10000;
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

Here is what you see when you run this program.

>> SVMonteCarloDensityWith2DHermitesWilmott

SVolMeanAnalytic =

   0.251859064132500

SVolMean =

   0.251863758906108

AssetMeanAnalytic =

   0.025834331749008

AssetMean =

   0.025815497695354

Look at monte carlo Mean of X and V

str =

     []

IndexMaxX =

   201

IndexMaxY =

   201

Look at sizes of variables----1

str =

     []

MeanX =

   0.025815497695354

MeanV =

   0.251863758906108

Look at 3D graphs

str =

     []

C =

  Columns 1 through 7

   0.006497337445425   0.003232035701479   0.000888200210853   0.000167060492319   0.000013447963356 
-0.000003787882163  -0.000002707045488

   0.006103640762728   0.003760791234298   0.001271542675321   0.000248614492577  -0.000005783011101 
-0.000025053419495  -0.000010537958465

   0.002688558089542   0.001844247294565   0.000667340562761   0.000105391238830  -0.000031310243646 
-0.000026033438760  -0.000008058781951

   0.000737006426825   0.000471817212194   0.000127309107535  -0.000019251106172  -0.000030786964423 
-0.000010776359191  -0.000000647624144

   0.000103340578135   0.000026870335121  -0.000033946738528  -0.000035927962856  -0.000015053148333 
-0.000001187308493   0.000001715435407

  -0.000011263272013  -0.000031027161428  -0.000030381876777  -0.000015049249060  -0.000003237889580 
 0.000000864867892   0.000000820707402

  -0.000011059378227  -0.000013770321674  -0.000008316453218  -0.000001613632758   0.000000769374831 
 0.000000585206186   0.000000098112089

  -0.000004350446341  -0.000003026159833  -0.000000158888808   0.000001224264466   0.000000821549110 
 0.000000187375651  -0.000000044194121

  Column 8

  -0.000001088579833

  -0.000002348046073

  -0.000000907288553

   0.000000863981233

   0.000000851930877

   0.000000214439577

  -0.000000047398723

  -0.000000041876454

Look at Coefficients of 2D Hermite products

str =

     []

bH0 =

   0.025796952988447

bH =

   0.024233824260633   0.010674619753890   0.002926201741049   0.000410302228929  -0.000044719564136 
-0.000043910026624  -0.000017272961528

b0 =

   0.017011890320703

b =

   0.016598086535875   0.006236855182237   0.001559736421978   0.001068952628289   0.000318012627951 
-0.000043910026624  -0.000017272961528

Look at 1D Coeffs of X

str =

     []

IndexMax =

        2401

blue line is density of Asset from Hermite Series, green is numerical density from monte carlo.

---

### #1958 — Amin (Topic Author)
*September 18, 2023, 11:02 AM*

Friends sorry that this is not the post for explanation of the previous program but a short post to describe the
torture. I would like to make the explanation post now but I slept around 4:00 am and woke up at 8:45 am. I am short of
sleep and need to sleep now after writing this post. Explanatory post with latex may take too longer.

Friends, for past ten days I have become target of torture again and again. They have even further increased torture for
past 2-3 days. Every day they give me almost unbearable pain in left temple and other places on face and head for at
least 6-7 hours. This becomes very very painful.

Sometimes they would give pain in temple and then at other times pain in teeth or ears. And at even other times they
cause pain in the eyes.

Now they are systematically using torture as a policy. I am sure this is very well thought out strategy by most of the
people who always wanted to retard me.

Again this is very difficult to pass a day when they continue to torture for 6-7 hours. For example they also continue
to torture when I drop my mother for her class on my car and also in the evening when I go out in the city on the
motorcycle.

Though I continue to wash my face and head and continue to wet my face and head repeatedly after short periods to
decrease torture, it is still very difficult to do any work when there is extreme torture.

This noon and after that I went to a nearby park to brainstorm about the analytic evolution of 2D correlated density
with addition of moments and they continue to torture me in the park but it was still far better than what I had to face
in our house. The purpose of going to park was also because I expected that there would be a relatively better
environment there.

Sometimes they decrease torture abruptly only to restart it with severity after an hour or two again.

I Want to request friends to please ask people in government to make sure that torture on me stops. I am committed to
research work but it would be far nicer if I could do my research in a relatively more pleasant environment and I could
possibly become more productive.

I have been able to work reasonably well in past few days despite the torture but it would be difficult to continue for
a longer  time with 6-7 hours of intense torture everyday.

Mind control guys continue to tell me that they want me to do research for specific person in academia or industry who
would control what to do with my research and they do not want me to make my research public and they assure that I
would be paid decently for my research. While I really want my research to remain perfectly accessible for everyone who
is interested.

I would be posting details of yesterday's program tonight. I also want to mention that I am very hopeful that we would
be able to solve for 2D correlated SV problem with addition/matching of moments. Today when I was in the park, I wrote
equations for it and I hope we would be able to solve the problem. But of course, we could be sure only when we have
done it. Tonight I will also try to write basic equations for solution of 2D SV problem with analytic matching/addition
of moments.

---

### #1959 — Amin (Topic Author)
*September 18, 2023, 4:55 PM*

Friends, I just came back to my house from going outside in the city. They continued torture on me when I was driving my
bike and I had constant pain in my left temple. But that is nothing new and I have told friends several times about it.
But what has made me become seriously worried is when I returned home I noticed that I was slightly losing balance for
very little periods of time. I also was very disoriented and I noticed that I am also slightly forgetting/losing context
of things I am doing or talking about. I was a bit more worried due to these new problems and decided to write this post
to ask good American people for help before it is too late for me and there is some possible permanent damage to my
brain.

I will be explaining the previous technical post in a few hours later tonight.

---

### #1960 — Amin (Topic Author)
*September 18, 2023, 6:43 PM*

Sorry friends, I am not feeling well and going to sleep. I will write explanation of technical post during the day
tomorrow. Sorry about this delay.

---

### #1961 — Amin (Topic Author)
*September 19, 2023, 7:41 AM*

Friends, Explaining the ideas behind the previous program.

I have previously suggested that we can represent a bivariate random variable V as a double summation in hermite
polynomials as

$V(Z_x,Z_y) \, =\, \sum\limits_{n=0}^N \, \sum\limits_{m=0}^M \, C(n,m) \, H_n(Z_x) \, H_m(Z_y) $

please note that a perfectly equivalent representation(analogous to Z-series in 1D) would be

$V(Z_x,Z_y) \, =\, \sum\limits_{n=0}^N \, \sum\limits_{m=0}^M \, D(n,m) \, {Z_x}^n \, {Z_y}^m $

where C(n,m) and D(n,m) can be converted into each other.

If$Z_x$ and$Z_y$ are independent of each other, we can take inner product of the bivariate variable with 2D Hermite
polynomials of order n1 and m1

$ \,  \int\limits_{Z_x=-\infty}^{\infty}  \int\limits_{Z_y=-\infty}^{\infty} V(Z_x,Z_v) \, H_{n1}(Z_x) \, H_{m1}(Z_y)\, p(Z_x,Z_y) \, dZ_x \, dZ_y$

We know from start that our postulated representation of $V(Z_x,Z_y)$ is

$V(Z_x,Z_y) \, =\, \sum\limits_{n=0}^N \, \sum\limits_{m=0}^M \, C(n,m) \, H_n(Z_x) \, H_m(Z_y) $

Substituting it in our previous Eq, we get

$\,  \int\limits_{Z_x=-\infty}^{\infty}  \int\limits_{Z_y=-\infty}^{\infty} \Big[\, \sum\limits_{n=0}^N \, \sum\limits_{m=0}^M \, C(n,m) \, H_{n}(Z_x) \, H_{m}(Z_y) \Big] \, H_{n1}(Z_x) \, H_{m1}(Z_y)\, p(Z_x,Z_y) \, dZ_x \, dZ_y$

Since most terms are orthogonal to each other and there is only one term where n1=n and m1=m that has a non-zero inner
product. So we get from previous term

$\,  \int\limits_{Z_x=-\infty}^{\infty}  \int\limits_{Z_y=-\infty}^{\infty} \Big[\, \, C(n1,m1) \, H_{n1}(Z_x) \, H_{m1}(Z_y) \Big] \, H_{n1}(Z_x) \, H_{m1}(Z_y)\, p(Z_x,Z_y) \, dZ_x \, dZ_y$

$= \, n1! \, m1! \, C(n1,m1) $

which means by taking factorials in denominator of other side of the equation that

$ C(n1,m1) \, = \, \, \frac{1}{\, n1! \, m1! \,} \int\limits_{Z_x=-\infty}^{\infty}  \int\limits_{Z_y=-\infty}^{\infty} V(Z_x,Z_v) \, H_{n1}(Z_x) \, H_{m1}(Z_y)\, p(Z_x,Z_y) \, dZ_x \, dZ_y $

We can replace integrations with summations, on a uniform 2D grid where asset index k ranges from 0 to K and vol index 
ranges from 0 to L, for a numerical procedure as

$ C(n1,m1) \, = \, \, \frac{1}{\, n1! \, m1! \,} \sum\limits_{k=0}^{K}  \sum\limits_{l=0}^{L} V(Z_x(k,l),Z_v(k,l)) \, H_{n1}(Z_x(k,l)) \, H_{m1}(Z_y(k,l))\, p(k,l) \, dZ_x(k,l) \, dZ_y(k,l) $

since $Z_y$ is independent of the asset and does not depend on its index, we can simplify as

$ C(n1,m1) \, = \, \, \frac{1}{\, n1! \, m1! \,} \sum\limits_{k=0}^{K}  \sum\limits_{l=0}^{L} V(Z_x(k,l),Z_v(l)) \, H_{n1}(Z_x(k,l)) \, H_{m1}(Z_y(l))\, p(k,l) \, dZ_x(k,l) \, dZ_y(l) $

In our numerical procedure I used integrated probability mass in each grid cell so we represent integrated probability
mass as integral over a single 2D cell, I am not writing integral sign since it is integral over a single cell.

$P(k,l)=\, p(k,l) \, dZ_x(k,l) \, dZ_y(l) $

to modify the previous equation as

$ C(n1,m1) \, = \, \, \frac{1}{\, n1! \, m1! \,} \sum\limits_{k=0}^{K}  \sum\limits_{l=0}^{L} V(Z_x(k,l),Z_v(l)) \, H_{n1}(Z_x(k,l)) \, H_{m1}(Z_y(l))\, P(k,l) \, $

---

### #1962 — Amin (Topic Author)
*September 19, 2023, 8:51 AM*

Here I explain the very simple way to convert 2D hermite expression of bivariate density into 1D density of asset.

Our 2D representation of bivariate random variable is given as

$V(Z_x,Z_y) \, =\, \sum\limits_{n=0}^N \, \sum\limits_{m=0}^M \, C(n,m) \, H_n(Z_x) \, H_m(Z_y) $

I suppose we can, due to conditioality, get one dimensional hermite series of asset by integrating 2D hermite series of
bivariate random variable over volatility and then dividing by the single dimensional integral of volatility (here Y)as
.

$\sum\limits_{n=0}^N  \, b(n) \, H_n(Z_x) \,=\, \frac{\int\limits_{Z_y=-\infty}^{\infty} \,V(Z_x,Z_y) \, dZ_y \,}{\int\limits_{-\infty}^{\infty} Y(Z_y) \, dZ_y}\, $

We integrate the above expression over volatility as

$\int\limits_{Z_y=-\infty}^{\infty} \,V(Z_x,Z_y) \, dZ_y \,=\int\limits_{Z_y=-\infty}^{\infty} \,\, \sum\limits_{n=0}^N \, \sum\limits_{m=0}^M \, C(n,m) \, H_n(Z_x) \, H_m(Z_y) dZ_y$

When we integrate over volatility, all volatility hermite polynomials greater than zero have a zero expectation so we
get only non-zero term with zeroth hermite in volatility.

$\int\limits_{-\infty}^{\infty} \,V(Z_x,Z_y) \, dZ_y \,=\,\, \sum\limits_{n=0}^N  \, C(n,0) \, H_n(Z_x) H_0(Z_y)$

if b(n) are coefficients of independent asset series, Because of conditionality we know

$\sum\limits_{n=0}^N  \, b(n) \, H_n(Z_x) \,=\, \frac{\int\limits_{Z_y=-\infty}^{\infty} \,V(Z_x,Z_y) \, dZ_y \,}{\int\limits_{-\infty}^{\infty} Y(Z_y) \, dZ_y}\, =\, \frac{\,\, \sum\limits_{n=0}^N  \, C(n,0) \, H_n(Z_x) H_0(Z_y)}{ H_0(Z_y)\,}$

this is because $\int\limits_{Z_y=-\infty}^{\infty}  Y(Z_y) dZ_y\, = \, H_0(Z_y)\, = \, \mu(y)$

where $\mu(y)$ is mean of volatility

So in order to get a hermite series in asset we have to divide the original  expression with mean as

So we can get coefficients of 1D hermite asset series $b(n)=\frac{C(n,0)}{\mu(y)}$

where resulting hermite series for asset is given as $X=\sum\limits_{n=0}^{N} b(n) H_n(Z)$

---

### #1963 — Amin (Topic Author)
*September 19, 2023, 8:54 AM*

Yesterday, I had some good ideas about analytic solution of 2D correlated SV models with matching/summation of moments.
I also want to start working on that so that I could complete all the work on that before next injection. I will post my
basic equations for that in latex later tonight. I am very hopeful that method would work well. I will be posting the
equations for review by friends later tonight.

---

### #1964 — Amin (Topic Author)
*September 19, 2023, 10:23 AM*

Please note the last equation of post 1961.

$ C(n1,m1) \, = \, \, \frac{1}{\, n1! \, m1! \,} \sum\limits_{k=0}^{K}  \sum\limits_{l=0}^{L} V(Z_x(k,l),Z_v(l)) \, H_{n1}(Z_x(k,l)) \, H_{m1}(Z_y(l))\, P(k,l) \, $

For a bivariate random variable without correlations  V(Z_x(k,l),Z_y(l)) can be written as a product of values of
univariate variables on (k,l) grid cell as

$V(Z_x(k,l),Z_v(l)) \, = \, X(k) \, Y(l) $

So we can write the first equation as

$ C(n1,m1) \, = \, \, \frac{1}{\, n1! \, m1! \,} \sum\limits_{k=0}^{K}  \sum\limits_{l=0}^{L} X(k) \, Y(l) \, H_{n1}(Z_x(k,l)) \, H_{m1}(Z_y(l))\, P(k,l) \, $

Also from equation below we see that X and Y even though correlated/non-correlated, they are not independent in our
case.

$V(Z_x(k,l),Z_v(l)) \, = \, X(k) \, Y(l) $

If they were independent, their Z-series would be product of two 1 dimensional Z-series which is not the case in our
problem.

Explaining these posts was informative for me as well. Now I am thinking that we could retrieve X after integrating V(2D
bivariate random variable) over volatility(here Y) and dividing by the mean of volatility since Y(volatility) is
independent of X. I am not sure if we could retrieve Y(volatility) after integrating V (two d bivariate variable) over X
and dividing by mean of X since X(asset) is not independent of Y(volatility). But I need to think more about it.

I also think I have more clarity about plotting 2D graphs after writing these posts.

---

### #1965 — Amin (Topic Author)
*September 19, 2023, 11:28 AM*

Friends, here I want to describe my strategy for solution of 2D SV asset equation with matching/summation of moments.

First please know that in the explanation Capital letters with parameters Zx and Zy are expansions of the form below
each with a different set of coefficients C.

$A(Z_x,Z_y) \, =\, \sum\limits_{n=0}^N \, \sum\limits_{m=0}^M \, C(n,m) \, H_n(Z_x) \, H_m(Z_y) $

When we have a initial value solution in above form and we substitute it in a correlated asset equation and also
substitute volatility in the asset Sv equation, we get a 2D solution of the bivariate random variable in the form

$A(Z_x,Z_y) \, + \, B(Z_x,Zy) \, \bar{Z_y} \, + \, C(Z_x,Z_y)\, ({\bar{Z_y}}^2-1) + \, D(Z_x,Zy) \, \bar{Z_x} \, + \, E(Z_x,Z_y)\, ({\bar{Z_x}}^2-1) + \, F(Z_x,Zy) \, \bar{Z_x} \, \bar{Z_y} \,$

here$Z_x$ and$Z_y$ are standard normals from initial value and$\bar{Z_x}$ and$\bar{Z_y}$ are standard normals from noise
in the SDE. We want to write a single expression that is only in form of just two standard normals instead of four e
have in above evolution equation.

We could write the above SV SDE evolution equation as

$=\Big[A(Z_x,Z_y) \, + \, B(Z_x,Zy) \, \bar{Z_y} \, + \, C(Z_x,Z_y)\, ({\bar{Z_y}}^2-1) \Big] \, \\

+\Big[ \, D(Z_x,Zy) \, + \, F(Z_x,Zy) \,\, \bar{Z_y} \Big] \,\bar{Z_x} \, \\

+ \, E(Z_x,Z_y)\, ({\bar{Z_x}}^2-1) \,$

We first solve by summation of moments of all volatility terms(with$Z_y$ and$\bar{Z_y}$ to get a single$\tilde{Z_y}$ )
that are associated with each orthogonal X-hermite. First we tackle first equation in big brackets

$\Big[A(Z_x,Z_y) \, + \, B(Z_x,Zy) \, \bar{Z_y} \, + \, C(Z_x,Z_y)\, ({\bar{Z_y}}^2-1) \Big] \,$ and equate it to

$G(Z_x,\tilde{Z_y})$

similarly for

$\Big[ \, D(Z_x,Zy) \, + \, F(Z_x,Zy) \,\, \bar{Z_y} \Big]$ and equate it to

$H(Z_x,\tilde{Z_y})$

and then write the problem as

$=G(Z_x,\tilde{Z_y}) \, +H(Z_x,\tilde{Z_y})\,\bar{Z_x} \,+ \, E(Z_x,Z_y)\, ({\bar{Z_x}}^2-1) \,$

and then convert the above into one term as A(\tilde{Z_x},\tilde{Z_y}) by adding all asset terms(with$Z_x$ and
$\bar{Z_x}$ to get a single$\tilde{Z_x}$ ) that are associated with each orthogonal Y-hermite.

My only worry is that terms with$\tilde{Z_y}$ that appears in G and H above and$Z_y$ that appears in E might have some
incompatibility or hidden correlation (that can throw off some cross moments but I strongly doubt it) with each other
but I will have to check. I am very sure all other terms are compatible since they are derived from same initial value
Z_y standard normal and same noise \bar{Z_y} standard normal and they should be compatible in all cross moments (of the
true expression) in the form of a single resulting variable.

I solve first for two volatility standard normals to get one in the expression and it is done first since Y (volatility)
is independent of X while any changes due to Y are accounted in X that is solved later.

I will start working on this tonight.

Today was a better day since they gave me only relatively light pain and it was not very intense and I could work well.
I hope this thing lasts in coming days.

---

### #1966 — Amin (Topic Author)
*September 19, 2023, 6:03 PM*

Friends, in the program I posted and in my previous description, I have used our bivariate random variable V(Z_x,Z_y) as
a product of X and Y (asset and volatility).

But since only the asset itself has bivariate dependence on both Z_x and Z_y, we could have also used only asset as a
function of Z_x and Z_y or X(Z_x,Z_y) in the inner product calculations of coefficients of 2D hermites.

I will urge friends to try only SV asset X(k,l) on the 2D grid in the inner product with 2D hermites as opposed to
product of X and Y. I will try to come up with a program on it soon.

Especially in SV equations, the equation of asset has dependence on both stochastic volatility and previous time value
of the asset itself and asset has bivariate dependence (on Z_x and Z_y)  but asset SDE is certainly not a product of
asset and stochastic volatility. Even though,if we want, we can easily construct a bivariate density of the product of
asset and volatility by combining the SDEs of asset and volatility and their Z-series.

So in my previous program the bivariate random variable was product of asset and volatility but it could just have been
bivariate value of only the asset. At that time, I did not have insight that I have slowly gained later so as to model
the bivariate density of only asset as a function of Z_x and Z_y. I will try modifying my program for only bivariate
representation of asset X and try posting it in a day or two.

So I suppose that every random variable that has bivariate dependence that is possibly product of two dependent random
variables or just a single random variable that has bivariate dependence, both possiblities can be represented as a 2D
hermite series. Our derivation of 2D hermite series coefficients only requires a bivariate dependence of the random
variable.

---

### #1967 — Amin (Topic Author)
*September 20, 2023, 1:02 PM*

Friends, I will look into my matlab files if I have already written a program to convert 2D Hermite series to 2D
Z-series and vice versa. I think I did not write this program earlier but I want to check. If I have not written this
program before, I will try to quickly write it tonight and later post on wilmott.

But I do clearly recall that I had written a program to convert a random variable whose 2D Z-series is known into
Z-series of functions of the random variable.

Just like we had in one dimension case, most analytics are done with hermite series in 2D but conversion of a bivariate
random variable into its functions is done with Taylor expansion of 2D Z-series just like we did for 1D case using
Z-series. I have written this program by manipulating output from mathematica for 7th X 7th order 2D Z-series but I
think there is a need for automated program that directly uses some algorithm to convert arbitrary order 2D Z-series
into its functions.

I will be posting both these programs tomorrow.

---

### #1968 — Amin (Topic Author)
*September 20, 2023, 6:59 PM*

Friends, I am very tired tonight and sleeping early so no new work today.

But I have been able to work out graphing of two overlaid surface graphs on the same grid. The first by numerical 2D
parzen density and the second solely utilizing the uni-variate Z-series of volatility and bivariate Z-series of asset.
For the second graph, we will also have the knowledge of uniform grid coordinates from first graph. For the second
graph, we will have no given density and the 2D density for surf/surface graph would be obtained from values of Zx and
Zy calculated from both Z-series of volatilty and asset(on given rectangular uniform grid coordinates) and the
associated jacobian. This is not very complicated.

I will post matlab program for this overlaid surface graphs tomorrow and we will move on from there towards more
interesting work.

I also tried replacing product of stochastic volatility and asset from previous program with only bivariate asset but
results seem to be exactly the same. If you try to replace the product of volatility and asset with asset only, make
sure that you also remove the lines where parameters of asset and zeroth order volatility hermite are divided by zeroth
order volatility hermite to get the asset.

I am quickly posting the program with bivariate asset only.

```
function [] = SVMonteCarloDensityWith2DHermitesWilmott()

%Copyright Ahsan Amin. Infiniti derivatives Technologies.
%Please fell free to connect on linkedin: linkedin.com/in/ahsan-amin-0a53334

%Volatility and asset equations are
%Vt(0)=V0;
%dVt=(mu1*Vt^beta1 + mu2*Vt^beta2)*dt+sigma0 * Vt^gamma * dz1(t)
%Xt(0)=X0
%dXt=(a*Xt^alpha1+b*Xt^alpha2)*dt+sigma1* Vt^gammaV * Xt^gammaX *dz2(t);
%=rho *dt

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

X0=1.0;
alpha1=0;
alpha2=1;
kappaX=0;
thetaX=1.00;
a=kappaX*thetaX;
b=-kappaX;

rho=0;
sigma1=.4;
gammaV=.5;
gammaX=.7;
%%%%%%%%%%%%%
V0=1.0;
thetaV=1.0;
kappaV=1.750;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.85;
sigma0=.8;
%%%%%%%%%%%%

dt=.03125;
Tt=32*4;

T=Tt*dt;

%%%%%%%%%%%%%%%%%%%%%%%%5

%rng(29079137, 'twister')
rng(15898837, 'twister')
paths=200000;
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

X=real(X);
X(X<0)=0;
V(V<0)=0;

SVolMeanAnalytic=thetaV+exp(-kappaV*T)*(V0-thetaV)
SVolMean=sum(V(1:paths))/paths
AssetMeanAnalytic=thetaX+exp(-kappaX*T)*(X0-thetaX)
AssetMean=sum(X(1:paths))/paths

str=input("Look at monte carlo Mean of X and V")

NoOfBinsV=150;
NoOfBinsX=150;

[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv]=
Find2DDensityAndCDFFromSimulation_Infiniti(X,V,paths,NoOfBinsX,NoOfBinsV);
%Please look at matlab file of above function for etailed explanation of
%all its input and output parameters.

str=input("Look at sizes of variables----1")

surf(Xn,Vm,XYProbDensity2D)

%hold on

MeanX=sum(X(1:paths))/paths
MeanV=sum(V(1:paths))/paths

str=input("Look at 3D graphs")

%Below calculate Coeffs of 2D Hermite products.
%Oxn is order of Zx hermites. ranges from 1 to 8 in indexing or (0 to 7 in reality)
%Ovm is order of Zv hermites. ranges from 1 to 8 in indexing or (0 to 7 in reality)
%HermiteH(Oxn,Zx(nn,mm)) is a small function that caclulates Oxn order hermite at Zx(nn,mm) value
%HermiteH(Ovm,Zv(mm)) caclulates Ovm order hermite at Zy(mm) value
%Below Eq calculates 2D Coeffs with inner product of coordinates of 2D uniform grid with
%product of X and V hermites.

Zx

str=input("Look at Zx");

C(1:8,1:8)=0;

for Oxn=1:8
    for Ovm=1:8
        for nn=1:(NoOfBinsX+1)
            for mm=1:(NoOfBinsV+1)
               
%C(Oxn,Ovm)=C(Oxn,Ovm)+1/factorial(Oxn-1)/factorial(Ovm-1).*Xn(nn).*Vm(mm).*HermiteH(Oxn-1,Zx(nn,mm)).*HermiteH(Ovm-1,Zv(mm)).*XYProbMass2D(nn,mm);
               
C(Oxn,Ovm)=C(Oxn,Ovm)+1/factorial(Oxn-1)/factorial(Ovm-1).*Xn(nn).*HermiteH(Oxn-1,Zx(nn,mm)).*HermiteH(Ovm-1,Zv(mm)).*XYProbMass2D(nn,mm);

            end
        end
    end
end

C

%If C are 2D hermite Coeffs as calculated in above equation
%Hermite Series representation of 2D random variable would be given by
%double sum equation below as
%Sum_{n=0}^{n=7} Sum_{m=0}^{m=7} C(n+1,m+1) He(n,Zx) He(m,Zy);

str=input("Look at Coefficients of 2D Hermite products")

%Below we calculate 1D Hermite Series for volatility.
%We only need to calculate the mean (zeroth hermite) aH0 of the volatility
%random variable.

aH0=0;
aH(1:7)=0;
for nn=1:IndexMaxV
aH0  =  aH0+Vm(nn).*VProbMass(nn);
aH(1)=aH(1)+Vm(nn).*Zv(nn).*VProbMass(nn);
aH(2)=aH(2)+.5*Vm(nn).*(Zv(nn).^2-1).*VProbMass(nn);
aH(3)=aH(3)+1/6*Vm(nn).*(Zv(nn).^3-3*Zv(nn)).*VProbMass(nn);
aH(4)=aH(4)+1/24*Vm(nn).*(Zv(nn).^4-6*Zv(nn).^2+3).*VProbMass(nn);
aH(5)=aH(5)+1/120*Vm(nn).*(Zv(nn).^5-10*Zv(nn).^3+15*Zv(nn)).*VProbMass(nn);
aH(6)=aH(6)+1/720*Vm(nn).*(Zv(nn).^6-15*Zv(nn).^4+45*Zv(nn).^2-15).*VProbMass(nn);
aH(7)=aH(7)+1/720/7*Vm(nn).*(Zv(nn).^7-21*Zv(nn).^5+105*Zv(nn).^3-105*Zv(nn)).*VProbMass(nn);
end

%Below we calculate the Hermite series of asset by integrating over the
%volatility to get marginal series of asset. When we integrate over
%volatility, all volatility hermites(alone or as products with X-hermites)
%in the 2D asset series go to zero(they all have mean zero).
%So basically all volatility terms go to zero and we are left with
%one dimensional array containing terms from 2D series where
%volatility hermites in the product had order zero. This order zero is
%represented by volatility index one in the 2d array of coeffs C(n,m);
%So our 1D asset series is from the line C(1:8,1) where volatilit hermites
%are zero. This is very interesting.

bH0=C(1,1);
bH(1:7)=C(2:8,1);

%Above bH0 is asset Hermite series coeff of zeroth order hermite and
%bH(1:7) represent hermites from 1st to 7th order.

%bH0=bH0/aH0;
%bH=bH/aH0;

%Above, we need to normalize the asset hermite series with expected value
%of volatility since we integrated over the volatility. Just like in
%Conditioning when we integrate over a variable to get marginal density and
%then we have to divide with the integral of the integrated density as
%well. Similalry, Here we have to divide with the mean/expected value of
%volatility hermite series(which is integral of the volatility hermite series)
%to normalize our asset equation hermite coefficients.

%Below we convert from hermite series to Z-series of the asset for
%plotting.
[b0,b] = ConvertHCoeffsToZCoeffs(bH0,bH,7);

bH0
bH

b0
b

str=input("Look at 1D Coeffs of X")

dNn=.1;%.1/2;   % Normal density subdivisions width. would change with number of subdivisions
Nn=101;%45*4;  % No of normal density subdivisions
NnMid=((1+Nn)/2)*dNn;
Z(1:Nn)=(((1:Nn)*dNn)-NnMid);

XX(1:Nn)=b0;
for nn=1:7
   XX(1:Nn)=XX(1:Nn)+b(nn)*Z(1:Nn).^nn;
end

wnStart=1;
%Below we make calculations of density in original coordinates by doing
%change of probability derivative with respect to gaussian density.
DfXX(wnStart:Nn)=0;
for nn=wnStart+1:Nn-1

    DfXX(nn) = (XX(nn + 1) - XX(nn - 1))/(Z(nn + 1) - Z(nn - 1));

    %Change of variable derivative for densities
end
DfXX(Nn)=DfXX(Nn-1);
DfXX(1)=DfXX(2);

pXX(1:Nn)=0;
for nn = wnStart:Nn

    pXX(nn) = (normpdf(Z(nn),0, 1))/abs(DfXX(nn));
end

%Below make parzen density of asset in SV equations and also plot the
%analytic density of asset.
 NoOfBins=2400;
 MaxCutOff=100;

 [XDensity,IndexOutX,IndexMaxX] = MakeDensityFromSimulation_Infiniti_NEW(X,paths,NoOfBins,MaxCutOff );
 plot(XX(2:Nn-1),pXX(2:Nn-1),'b',IndexOutX(1:IndexMaxX),XDensity(1:IndexMaxX),'g');

title('Asset Density(in SV model) From Analytic Hermite Series Calculated from 2D Hermite Series VS Numerical Parzen
Density of Asset');%,sprintf('theta= %f', theta), sprintf('kappa = %f', kappa),sprintf('sigma = %f', sigma0),sprintf('T
= %f', T));

legend({'Marginal Asset Density from 2D Hermite Series','Parzen Density From Monte Carlo'},'Location','northeast')

str=input('blue line is density of Asset from Hermite Series, green is numerical density from monte carlo.');

end
```

---

### #1969 — Amin (Topic Author)
*September 21, 2023, 9:25 PM*

Friends, I have written a program to 3D graph the bivariate dependent probability density function on a uniform
rectangular grid from the knowledge of underlying 2D Hermite series. I really think my logic is sound but I am having
some bugs in the helping functions and some intermediate results are very off. So I am trying to fix the helping
functions and I expect it can take a day. I can only post the program sometime tomorrow when I could fix the errors.

A very good thing is that my mother bought me a new laptop Lenovo thinkpad i7, 12 Gen. I had been working on a very old
laptop from 2012 for past two/three months (after two of my laptops that I bought one after the other had motherboard
problems within time period of a month and I had to start working on a very old laptop that I had bought in 2012 and I
had stopped using it) and it was extremely slow. I really hope that a fast laptop will also help me do some better
research.

Anyway, I really think that 3D graphing with hermite series using surf should work well in a day or two. There are some
bugs in helping functions and I hope that I would soon be able to fix them.

---

### #1970 — Amin (Topic Author)
*September 22, 2023, 10:07 AM*

Friends, I was able to graph from 2D Hermite series just now. This is very start so there might be several minor issues
to fix. In the graph with analytic 2D Z-series, you can see a slight difference at zero where density abruptly rises.
Also peak of the 2D Hermite Series graph is very slightly less than the peak of numerical density graph but I am sure
these issues could be fixed once we are more familiar and competent with the method as opposed to relatively basic
learning state we are currently at.

Parameters were quite extreme and a lot of mass was going into zero at T=4 years.

I will play around a little bit more and then post the matlab programs sometime later tonight or possibly tomorrow after
adding comments to explain graphing or inversion of 2D hermite series.

You can see that analytic density graphs in first pair of graphs and last pair of graphs are most affected at zero
volatility. I was just able to get the method to work and I am sure we would be able to tackle all these issues with a
bit of effort later.

Anyway here are four angles of the same 2D graph for friends to compare.

[![Image](../images/i.postimg.cc/Yq5ZpKbv/Stoch-Vol2-D01.png)](https://postimg.cc/ykTvP5qK)

.

.

[![Image](../images/i.postimg.cc/Sxc5RTvD/StochVol2D02.png)](https://postimg.cc/PCrKF4hw)

.

.

.

[![Image](../images/i.postimg.cc/ydGnvcGD/Stoch-Vol2-D01-B.png)](https://postimg.cc/FdjjKdNv)

.

.

.

[![Image](../images/i.postimg.cc/x8b57qrt/Stoch-Vol2-D02-B.png)](https://postimg.cc/RJ4wJSZH)

.

.

.

[![Image](../images/i.postimg.cc/c6yhNZ0Z/Stoch-Vol2-D01-C.png)](https://postimg.cc/V0gnjxJH)

.

.

.

[[url=https://postimg.cc/zVdPNMxj]![Image](../images/i.postimg.cc/Mpxk7JRh/Stoch-Vol2-D02-CA.png)](https://postimg.cc/z3rQFTLn)[/url]

.

.

.

[![Image](../images/i.postimg.cc/hPdZZZcc/Stoch-Vol2-D01-A.png)](https://postimg.cc/BXJCXgjV)

.

.

.

[![Image](../images/i.postimg.cc/7ZrsF1Z7/Stoch-Vol2-D02-A.png)](https://postimg.cc/Lnv3f1f6)

---

### #1971 — Amin (Topic Author)
*September 22, 2023, 10:37 AM*

Friends, even though I was able to create initial graphs, I am still afraid that there is a small issue with my
algorithm that is slightly putting off the density. I think I know the problem and I am trying to investigate it and see
how to fix it. I hope to be able to settle it soon and them come back with explanation of the algorithm and the matlab
programs.

---

### #1972 — Amin (Topic Author)
*September 23, 2023, 11:16 AM*

Friends, I am posting some new graphs for another SV monte carlo run. I was thinking that my analytic density is
slightly shifted lower than the numerical density whenever I would make a comparison. Then I thought of making a surface
plot of differences in the 2D probability functions of between numerical density and the analytic density as both
densities are calculated exactly on the same coordinates grid. After looking at the 2d surface plot of differences in
probability function, I notice that they are almost equally distributed on both sides of the Z-axis. I have given all
these graphs of difference of  probability density with different angles of the 2D density. I think my 2D inversion of
probability density function algorithm is quite reasonable and I will be posting it tomorrow.

My new laptop computer was extremely helpful at just the right time otherwise I would not have been able to complete
this work properly.

I will try posting several 2D graphs in later posts with different SDE parameters. Parameters of the SDE in this case
are given after the graphs.

.

.

[![Image](../images/i.postimg.cc/PfZcybZg/Stoch-Vol2-D03.png)](https://postimg.cc/BtSMQKmp)

.

.

.

[![Image](../images/i.postimg.cc/5t0TSZqg/Stoch-Vol2-D04.png)](https://postimg.cc/zysxJ2QH)

.

.

.

[![Image](../images/i.postimg.cc/3Ngcw7Y8/Stoch-Vol2-D03-A.png)](https://postimg.cc/30xBLskV)

.

.

.

[![Image](../images/i.postimg.cc/t4D8PXP7/Stoch-Vol2-D04-A.png)](https://postimg.cc/3k4LQQtH)

.

.

.

[![Image](../images/i.postimg.cc/8c8YDs8X/Stoch-Vol2-D03-C.png)](https://postimg.cc/dkB6jsVG)

.

.

.

[![Image](../images/i.postimg.cc/T1mZWgqX/Stoch-Vol2-D04-C.png)](https://postimg.cc/7JHBFCWB)

.

.

.

[![Image](../images/i.postimg.cc/4NRCR2s4/Stoch-Vol2-DDiff01.png)](https://postimg.cc/8s4XhH7x)

[![Image](../images/i.postimg.cc/0NB3WcVs/Stoch-Vol2-DDiff02.png)](https://postimg.cc/f3YBkj42)

[![Image](../images/i.postimg.cc/NjQW5yKW/Stoch-Vol2-DDiff03.png)](https://postimg.cc/rKYhHwCJ)

[![Image](../images/i.postimg.cc/kXQ0JNgQ/Stoch-Vol2-DDiff04.png)](https://postimg.cc/HVLZ3y5n)

.

.

.

SDE parameters for the monte carlo are given below

X0=1.0;

alpha1=0;

alpha2=1;

kappaX=1;

thetaX=1.0;

a=kappaX*thetaX;

b=-kappaX;

rho=0;

sigma1=.35;

gammaV=.5;

gammaX=.95;

%%%%%%%%`%%%%%

V0=1.0;

thetaV=1.0;

kappaV=1.750;

mu1=kappaV*thetaV;

mu2=-kappaV;

beta1=0;

beta2=1;

gamma=.85;

sigma0=.8;

%%%%%%%%%%%%

dt=.03125;

Tt=32*4;

T=Tt*dt;

%%%%%%%%%%%%%%%%%%%%%%%%5

---

### #1973 — Amin (Topic Author)
*September 23, 2023, 12:41 PM*

I noticed that asset in previous post was mean reverting. These are SDEs with same parameters but asset has no mean
reversion. I will give the SDE parameters at the end.

I have captured the original graphs and angles from all four sides.

.

.

.

[![Image](../images/i.postimg.cc/sfYzxCnG/Stoch-Vol2-D05.png)](https://postimg.cc/RqZypyxv)

.

.

.

[![Image](../images/i.postimg.cc/d1dYGbwX/Stoch-Vol2-D06.png)](https://postimg.cc/r083kYdC)

.

.

.

[![Image](../images/i.postimg.cc/HngCz6LL/Stoch-Vol2-D05-A.png)](https://postimg.cc/R6X8VQKr)

.

.

.

[![Image](../images/i.postimg.cc/Gm7dRPXM/Stoch-Vol2-D06-A.png)](https://postimg.cc/TKDZqbMm)

.

.

.

[![Image](../images/i.postimg.cc/wMQYGDtQ/Stoch-Vol2-D05-B.png)](https://postimg.cc/7JhRCGn5)

.

.

.

[![Image](../images/i.postimg.cc/RCKStH0F/Stoch-Vol2-D06-B.png)](https://postimg.cc/5j9WdjLd)

.

.

.

[![Image](../images/i.postimg.cc/hGNnzDWT/Stoch-Vol2-D05-C.png)](https://postimg.cc/Ffb8wQKH)

.

.

.

[![Image](../images/i.postimg.cc/cCydjsF0/Stoch-Vol2-D06-C.png)](https://postimg.cc/cghqtNqb)

.

.

.

[![Image](../images/i.postimg.cc/d0hvV7XJ/Stoch-Vol2-D05-D.png)](https://postimg.cc/v1wCPmbK)

.

.

.

[![Image](../images/i.postimg.cc/nzQH0sY3/Stoch-Vol2-D06-D.png)](https://postimg.cc/cg0yJLz3)

.

.

.

[![Image](../images/i.postimg.cc/SxNkH1f2/Stoch-Vol2-D06-Diff.png)](https://postimg.cc/sv8khc8s)

[![Image](../images/i.postimg.cc/MKwWmpcY/Stoch-Vol2-D06-Diff-A.png)](https://postimg.cc/0rtR8x06)

[![Image](../images/i.postimg.cc/90dcHvkT/Stoch-Vol2-D06-Diff-B.png)](https://postimg.cc/RJZkcb4V)

[![Image](../images/i.postimg.cc/RVTvsxKx/Stoch-Vol2-D06-Diff-C.png)](https://postimg.cc/svvFx8TT)

[![Image](../images/i.postimg.cc/mrnLY3Mc/Stoch-Vol2-D06-Diff-D.png)](https://postimg.cc/gwvbdZgd)

.

.

.

Here  are parameters of the SDEs used in monte carlo.

X0=1.0;

alpha1=0;

alpha2=1;

kappaX=0;

thetaX=0.0;

a=kappaX*thetaX;

b=-kappaX;

rho=0;

sigma1=.35;

gammaV=.5;

gammaX=.95;

%%%%%%%%`%%%%%

V0=1.0;

thetaV=1.0;

kappaV=1.750;

mu1=kappaV*thetaV;

mu2=-kappaV;

beta1=0;

beta2=1;

gamma=.85;

sigma0=.8;

%%%%%%%%%%%%

dt=.03125;

Tt=32*4;

T=Tt*dt;

%%%%%%%%%%%%%%%%%%%%%%%%5

---

### #1974 — Amin (Topic Author)
*September 24, 2023, 4:15 PM*

Friends, I am working to write comments on the new matlab program to find 2D Hermite Series from of 2D random variables
from monte carlo in SV setting. I hope to post the program in a few hours. I will also try to write a post that explains
my inversion of 2D Hermite series to find the bivariate probability density on the 2D specified grid.

These are initial programs and work need to be done to settle all the issues for example in SV setting, I noticed in
many SDEs when vol of vol gets close to one or is above one, the match between Hermite Series density and numerical
density decreases. I think this can be improved by adding another two hermite polynomials in each direction. Since we
find our 2D polynomial coefficients by inner product method, the numerical complexity does not increase much as we
increase the order of the series somewhat (as opposed to optimization to find the hermite series from moments). We will
also have to tackle grid issues since on a uniform grid Z changes by a very large amount when X

---

### #1975 — Amin (Topic Author)
*September 24, 2023, 7:46 PM*

Friends, mind control agents are altering my matlab programs I am working on. I am getting all statistics right with
monte carlo but results of my 2D numerical density and related graphs are many times totally absurd. I cahanged
everything that could go wrong but to no avail.

They used to change/alter my programs on a daily basis around 2013-2015 and I used to mention that on the forum and
probably some good people protested and they stopped altering my programs on a daily basis. This is from before I had
done any significant research.

I had told friends that I have very good market trading algorithms and I tested them several times on different data
with excellent results. A few months ago I wanted to actually try the algorithms on Binance. My Brother-in-law had said
that he would finance any money to run the algorithms and for operational costs. However, when I tried the very recent
Binance data at that time, I noticed that my algorithms had sharply reduced profitability. I really thought at that time
that crypto market had changed its dynamics and my algorithms would no longer work. I was slightly embarassed before my
brother-in-law but told him that I have to further improve my trading algorithms. I still had all the data and kept it
on my computer. And about two months ago, out of the blue without any previous planning or thought, I just tried very
same algorithms on the data from the time with little profitability and I was surprised to see that my results were
actually very good. I realized that they had altered my programs when I needed them the most.

There are other times I know when I was very sure that they altered my programs in past two years even though it was
very rare and this happened for just a few occasions.

They have total control of my computers. And I think they do not physically alter the code on my computer, but when I
write a command to run a certain file they just replace their file with my file and what actually runs on computer comes
from their file. They somehow make sure that my commands are replaced with their commands and their code runs on my
computer.

I had told friends that I was earlier working on an old computer from 2012. They again had complete control of the
computer. They even had control whether computer would turn on with electricity or not and they could also shut it down
abruptly. The extension wire I used with computer had a loose socket but it was not a big deal, I would adjust the
computer plug in the socket and play with it for 10-20 seconds and the computer would show that it is attached to
electric power. However, one day I continued to try for twenty minutes to turn on the computer but it would not turn on
and electricity light on it would not even blink at all. I was totally perplexed what was wrong. Frustrated, I took an
electric tester that shows red light when it is attached to electric current. When I attached the tester to the side of
computer wire that goes into the computer, it started to show red light. Power was actually going into the computer.
When they realized that I had noticed that electric current is going into the computer, they enabled the electricity and
the computer turned on the very minute. I had continued to try for twenty minutes but the computer would just not turn
on despite that electricity was going into the computer.

So they have total absolute control of my computers.

When I bought this thinkpad, a few days ago, I started using it on the same program on the new computer and I was so
happy that it worked very fast and I also mentioned it on internet. But after two days, they did something and speed of
the computer remarkably decreased on my programs. They try to do everything to thwart me.

Though American army had been good enough to give me concessions to not alter my programs and in so many other ways when
good American people protested to them but now they strongly regret that they made it easier for me to do any research
under pressure from good people. So now whenever they find opportunity, they try to thwart me in some way they can.

They are again changing/altering my programs since they completely hate that I get any limelight when trying to do good
research. It helps my human cause to end cruel mind control everywhere( as people understand the true nature of mind
control torture and reasons behind it )for which I have been fighting for more than a decade and corrupt officers in
American army are afraid once mind control ends, their livelihood due to corruption and obliging rich people by
retarding innocent and intelligent humans would completely end.

I hope good American friends protest to American army and ask them to not alter my programs and I will be able to post
my programs after that.

I will be making a post explaining how I inverted the 2D Hermite Series to get the density. I will also post the
function that inverts the 2D hermite series to find the 2D density in a bit but I cannot post all the matlab program
until I am sure it works well. I hope once people pressurize American army crooks to end altering my programs, I will
post them right away. I really look forward to posting my programs on Wilmott as I have always done before.

---

### #1976 — Amin (Topic Author)
*September 24, 2023, 8:35 PM*

This is the program I used for inversion of 2D Hermite Series to get the 2D probability density. I will be explaining it
in the next post.

.

.

.

```
function [pXY2D] = Calculate2VariablesOn2DGridFrom2DZSeries(XX,YY,NoOfBinsX,NoOfBinsY,C,a0,a,BinSizeX,BinSizeY)

%YY are Y-coordinates of 2D Grid. In our case this is stochastic
%volatility and is univariate and independent of asset so it can be
%inverted as a univariate Z-series. its Z-series is given by a0 and a.

[Zy] = CalculateZgivenXAndZSeriesC7(YY,a0,a);

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

Hermite2DSeries(1:NoOfBinsX+1,1:NoOfBinsY+1)=0;
%
 for nn=1:NoOfBinsX+1
     for mm=1:NoOfBinsY+1
     for Oxn=1:8
     for Ovm=1:8
           Hermite2DSeries(nn,mm)=Hermite2DSeries(nn,mm)+C(Oxn,Ovm).*HermiteH(Oxn-1,Zx(nn,mm)).*HermiteH(Ovm-1,Zy(mm));
     end
     end
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
for mm=2:NoOfBinsY
    for nn=2:NoOfBinsX

    pXY2D(nn,mm) = (normpdf(Zx(nn,mm),0, 1))*abs(DinvfXX(nn,mm)).*(normpdf(Zy(mm),0, 1))*abs(DinvfYY(mm));

    end
end

end

```

---

### #1977 — Amin (Topic Author)
*September 24, 2023, 9:19 PM*

Friends, I am really disheartened and not feeling well. I will write a better explanation tomorrow. Better than writing
a half-hearted thing that has no use to anyone. I will also write some comments on the above program.

---

### #1978 — Amin (Topic Author)
*September 25, 2023, 6:41 AM*

Many friends who are used to formal language all the time might be disturbed by my use of slang expletives for bad
people but after reading Einstein's letter to Marie Curie, I consider myself perfectly validated to use the word of scum
for American army and for bad jews who have no ethics and are ready to fall to every low level of humanity for some
material gain or due to their hatred, venom, poison or malice as in case of bad jews.

Even though American society keeps jews in very high regard, they are not gold-plated. Just like any other people or
race, some of them are extremely good human beings, some of them are extremely evil and some of them simply do not care.
They tend to be more intelligent and when this intelligent shows itself in the form of Einstein we see one of the
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

### #1979 — Amin (Topic Author)
*September 25, 2023, 8:41 AM*

For those friends who had interest in my matlab program, I assure them that soon I will make a detailed explanation post
and also re-post a well commented version of the  program required to invert the density(that I posted yesterday). I
also noticed that yesterday I posted a function but inadvertently I failed to post any helping functions. I will try to
complete this work today.

---

### #1980 — Amin (Topic Author)
*September 25, 2023, 7:07 PM*

Friends, I am posting all relevant functions one by one after adding comments.

One by one I will post all functions but there is no guarantee that everything would work properly though I will explain
all logic so friends could understand and change anything they wish. I will try to carefully read my posts and code to
make sure that there is no change in anything I have posted.

 Here is the relevant function that inverts a univariate Z-series to find a value of Z corresponding to the input value
of univariate stochastic variable. I was earlier using Newton inversion but I continued to face some problems with
Newton inversion so I shifted the logic of function from Newton root-finding to bisection which was extremely reliable
but slightly slow. You can increase the speed of this function by playing with it.

Here is the logic of bisection algorithm.

%This program takes a value of Y as input and returns the corresponding value of Z given the parameters of the Z-series.

where

$ Y(Z)= \, c_0 \, + c_1 \ Z \,+ c_2 \, Z^2 \,+ c_3 \, Z^3 \,+ c_4 \, Z^4 \,+ c_5 \, Z^5 \,+ c_6 \, Z^6 \,+ c_7 \, Z^7 \,$

It first sees if the value of Y is greater than median c0 or smaller than median c0. If the value of Y is greater than
median c0, Z has to be greater than zero and if the value of Y is smaller than median c0, Z has to be negative.

Once we know whether Z is greater than Z or smaller than Zero, we divide the program into two repeated if loops, one for
Z greater than zero and

one for Z smaller than zero.

If Z is positive, we have to assign it a valid band of upper and lower values between which it can be found.

This is done sequentially by calculating Y(.5) at Z=.5, if Y is smaller than Y(.5), we know that true value of Y will
lie between 0 and .5 so we assign a lower band value Za=0 and upper band value Zb=.5

If however Y is greater than Y(.5), we know that true Z should be larger than .5 and we again evaluate Y(1) at Z=1, If Y
is smaller than Y(1),  we know that true value of Z should be between .5 and 1, and we assign a lower band value Za=.5
and upper band value of Zb=1. Through repeated

elseif we continue until we find an appropriate band value of Z.

Once we have determined the upper band value of Zb and lower band value of Za, We find Zmid=(Za+Zb)/2. We then evaluate
Y(Zmid) and if Y move the upper band to Zb=Zmid while keeping Za at older value. However if Y> Y(Zmid), we know that
true value of Z  should be between Zmid and Zb so we assign the lower band value equal to Zmid as Za=Zmid while keeping
Zb at  its old value. In a few iterations, this bisection procedure gets extremely close to true value of Z for which
Y(Z)=Y

```
function [Z] = CalculateZgivenXAndZSeriesC7(X,c0,c)

Z(1:length(X))=0;

for nn=1:length(X)
        Z(nn)=CalculateZgivenXAndZSeriesBisection2C7(Y(nn),c0,c);
end

end

```

.

.

.

.

```
function [X] = EvaluateZSeriesC7(c0,c,Z)

X=c0+c(1)*Z+c(2)*Z.^2+c(3)*Z.^3+c(4)*Z.^4+c(5)*Z.^5+c(6)*Z.^6+c(7)*Z.^7;

end

```

.

.

```
function [Z]=CalculateZgivenXAndZSeriesBisection2C7(Y,c0,c)

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
    if(Y  EvaluateZSeriesC7(c0,c,Zmid))
            Za=Zmid;
        end
    Z=.5*Za+.5*Zb; %This can be taken out of the loop and does not
    %necessarily have to be calculated again and again. Has to be
    %calculated at least once after the loop to determine the true value of
    %Z which is the final result of the function.

    end

end

if(Y  EvaluateZSeriesC7(c0,c,-.5))
        Za=-.5;
        Zb=0;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-1))
        Za=-1;
        Zb=-.5;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-1.5))
        Za=-1.5;
        Zb=-1;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-2))
        Za=-2;
        Zb=-1.5;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-2.5))
        Za=-2.5;
        Zb=-2.0;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-3))
        Za=-3;
        Zb=-2.5;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-3.5))
        Za=-3.5;
        Zb=-3.0;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-4))
        Za=-4;
        Zb=-3.5;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-4.5))
        Za=-4.5;
        Zb=-4.0;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-5))
        Za=-4.5;
        Zb=-5.0;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-5.5))
        Za=-5.0;
        Zb=-5.5;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-6.0))
        Za=-5.5;
        Zb=-6.0;
    else
        Za=-12.0;
        Zb=-6.0;
    end
    for mm=1:35
        Zmid=.5*Za+.5*Zb;
        if(Y EvaluateZSeriesC7(c0,c,Zmid))
            Za=Zmid;
        end
    Z=.5*Za+.5*Zb; %This can be taken out of the loop and does not
    %necessarily have to be calculated again and again. Has to be
    %calculated at least once after the loop to determine the true value of
    %Z which is the final result of the function.
    end

end

end

```

---

### #1981 — Amin (Topic Author)
*September 25, 2023, 10:42 PM*

Inhuman, cruel and animal doggies of American army who retard thousands of innocent people without any humanity,
remorse, regret, or sense of empathy because corrupt doggies want money at all cost. In a society that celebrates money
(It is a quite successful model but these faults are obvious), incompetent and non-skilled people like army doggies who
like many others have even a stronger desire to make money but when money cannot be made by corrupt doggies by doing
anything right or pursuing any skill, they resort to finding evil ways like obliging the rich jewish billionaire and his
rich cohort to make money. American army is the most corrupt segment of American society.

If some Army is professional, patriotic and civilized, people in this profession have to be praised even more than
doctors, engineers and scientists. But when an army is full of inhuman, cruel and animal doggies, it is hard to
appreciate anything about it. I would never have used any bad word for American army if they had any regard about
respecting sanctity and dignity of so many human beings they retard without any remorse.

I demand corrupt American army and defense to stop cruel mind control of human beings all over the world and I would be
the first one to praise and appreciate them.

I have absolutely no personal animosity with anyone in American army but I want them to end their animal and cruel
practices in otherwise civilized society of twenty first century.

---

### #1982 — Amin (Topic Author)
*September 26, 2023, 5:57 AM*

When second Iraq war was started, every European country and United Nations were thoroughly convinced that Iraq had no
chemical/nuclear weapons. But doggies of American army bitterly wanted to please the Jews and start the war. Every
European nation tried to stop US from going to war but American army was thoroughly adamant in their claim that Saddam
Hussein was making Chemical weapons.  Finally, Europeans refused to become part of any war coalition but America started
the war anyway because American army bitterly wanted to attack Iraq.

Later no chemical weapons were found. Europeans and UN were perfectly validated in their observations that Iraq had no
chemical weapons plan.

Doggie Generals of American Army started making frivolous claims that, "we had talked to a chemistry professor who had
told us that Iraq was making chemical weapons. Since chemistry professor knew chemistry, we believed that Iraq must have
chemical weapons." Truth was that doggies bitterly wanted to please the same Jewish Goldfather and his cohort of mind
control and get material rewards.

Collin Powell who travelled to every European capital with the Dossier of evidence later demanded an inquiry was he was
misled by doggies of US army who presented false evidence and his dossier had false information. This inquiry was never
made. Doggies are powerful.

More than a million people were killed in the aftermath for war that doggies started for their lust for money.

Why have I written about Iraq war something which is seemingly out of context with my cause to end mind control of
innocent human beings?

In order to convince people that doggie Generals of US Army are well versed in the art of lying and deception. They lie,
contrive and deceive in the matters of greatest international importance where lives of millions of people are at stake
as in the case of Iraq War. So lying about an ordinary individual like me is not difficult for doggies and is an
everyday matter.

Since I have stepped on the tails of inhuman cruel doggies of US army, I am sure they would resort to their time tested
tradition of lying and deception to thwart and fail me in my human cause. I am afraid that they can make false claims
that I want to hurt people of US or people of US army or something more ingenious.

I have always told people on this forum several times that most American people are some of the best people on the
planet. They are nice, kind, humane and very enterprising. It is no wonder that despite poor leadership and despite huge
corruption by American army, America continues to make progress in so many dimensions and this is because Americans in
general are very hard working and enterprising people and they are also well versed in all modern science and technology
and all of this is possible because a large number of individuals try to excel in different spheres of life and in
different professions. There is a tradition of excellence in United States.

I am also truly indebted to a large number of good Americans in the universities who tried to help me in the past and my
systematic persecution decreased due to their protests. It is a matter of pride for me that some of my research work
could possibly be helpful to American researchers and scientists and I would love to continue to try to help in any way
I can. I know that my insight about practical applications of my research is very limited but it is really heartening to
know that many people would apply them with their large and diverse understanding of practical problems in various
fields. I admire all good people of United States.

Even though I openly say that America is probably the best country in the world in so many ways, I love my country since
my childhood and I want to live the rest of my life in my own country. I do not want to go and live anywhere else in the
world.

But again I want friends to know that I never believe in negative patriotism. I would like to do something interesting
in my country but at the same time I would love to help other people in my profession from different countries in any
way I can. We are all human beings and we are all one family.

---

### #1983 — Amin (Topic Author)
*September 26, 2023, 8:02 AM*

When I talk about American Army, I mean officers at high rank and decision makers. It is the foot soldiers and lower
ranks that actually fight in the battle field and they are the ones who do no corruption at all.

Also my observation from Pakistan Army is that larger the rank of the general, more corruption they do. And I am very
sure that same applies to generals in the American army.

By all means give great respect to army soldiers, veterans and  others who have fought for America in the actual
bettlefield. They all deserve your great respect.

It is the corrupt officers and higher ranks that are actually corrupt doggies and this is the actual scum in American
army. Scum never goes to actual battle field and actually swindles all the money. Being the scum in American army is one
of the most lucrative professions in United States. Of course scum cannot become billionaire because of corruption but
corrupt scum handily makes more money than most doctors, scientists and successful people in other leading professions.

---

### #1984 — Amin (Topic Author)
*September 26, 2023, 8:36 PM*

Friends, I am back on track with my matlab programs. I am being able to run my programs for various SDE parameters. As I
ran my programs again, I notice there are some robustness issues on the boundaries of the grid and I am trying to fix
them. I hope there are no unforeseen problems now and I hope to post my programs again very soon possibly in a day. If
there are no more special problems, I plan to continue my work as before and move on to a non-uniform grid and then
towards regressions on the model.

---

### #1985 — Amin (Topic Author)
*September 27, 2023, 5:51 AM*

Friends, my claim that mind control agents were changing my programs was wrong. I had not used matlab surf command
carefully before and was mistakenly thinking that (Xn,Vm,Z(n,m)) would be the proper order. I earlier worked with both V
and X both around one on a square grid so got under the very wrong impression that my program was working fine. They do
sometimes alter my programs though very rarely(admittedly not about my public research) and it was in back of my mind
otherwise I would have worked till the end to find the error. It was very silly.

However I am very happy that I became upset and it gave me courage to say things I have been unable to say before. I
stand behind every single word I said about bad jews and their network and also what I said about American army. I own
every single word I said.

I am sorry to friends that continuity of our research was disturbed but I am still relieved that I was able to speak the
truth about wrong things in our society and I hope that it would help my cause of saving innocent people from cruel mind
control of American army pigs. Again I want to very clearly say that everything I said about bad people is perfectly
true to my knowledge and I stand behind it and I am very happy that I was able to say it.

If anything unforeseen does not happen, I am very determined to take my research towards perfect conclusion and want to
work hard towards it and just like always I will continue to distribute all my matlab programs.

---

### #1986 — Amin (Topic Author)
*September 27, 2023, 7:50 AM*

These are very initial programs for review by friends and many changes are required. I want to improve the programs in
several ways. I also have some ideas about an alternative algorithm for construction of analytic density and associated
2D Hermite series. But just sharing the initial programs.

I have given parameters for maximum values for asset and volatility and please use them freely to not let the grid
become large and keep it manageable. This can be changed once a non-uniform grid is introduced. If the paths are not too
large, keep the grid coarse for proper construction of numerical density.

When volatility goes smoothly into zero and a lot of mass is at zero, there is a mismatch between analytic and numerical
density at zero. I am currently using CEV power .95 for volatility. I am sure this can be improved later.

I hope that this is just start of the work and there is a lot of good research work to follow.

Here is the program.

```
function [] = SVMonteCarloDensityWith2DHermitesWilmott02()

%Copyright Ahsan Amin. Infiniti derivatives Technologies.
%Please fell free to connect on linkedin: linkedin.com/in/ahsan-amin-0a53334

%Volatility and asset equations are
%Vt(0)=V0;
%dVt=(mu1*Vt^beta1 + mu2*Vt^beta2)*dt+sigma0 * Vt^gamma * dz1(t)
%Xt(0)=X0
%dXt=(a*Xt^alpha1+b*Xt^alpha2)*dt+sigma1* Vt^gammaV * Xt^gammaX *dz2(t);
%=rho *dt

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

X0=1.0;
alpha1=0;
alpha2=1;
kappaX=0;
thetaX=1.0;
a=kappaX*thetaX;
b=-kappaX;

rho=0;
sigma1=1;
gammaV=.5;
gammaX=.85;
%%%%%%%%`%%%%%
V0=.25;
thetaV=.06;
kappaV=1.50;
mu1=kappaV*thetaV;
mu2=-kappaV;
beta1=0;
beta2=1;
gamma=.95;
sigma0=.80;
%%%%%%%%%%%%

dt=.03125/2;
Tt=64*4;

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

SVolMeanAnalytic=thetaV+exp(-kappaV*T)*(V0-thetaV)
SVolMean=sum(V(1:paths))/paths
AssetMeanAnalytic=thetaX+exp(-kappaX*T)*(X0-thetaX)
AssetMean=sum(X(1:paths))/paths

str=input("Look at monte carlo Mean of X and V")

% NoOfBins=300;
% MaxCutOff=300;
% [XDensity0,IndexOutX0,IndexMaxX0] = MakeDensityFromSimulation_Infiniti_NEW(X,paths,NoOfBins,MaxCutOff );
% plot(IndexOutX0(1:IndexMaxX0),XDensity0(1:IndexMaxX0),'g');
%
% str=input("Look at 1D graph of X density");

NoOfBinsV=75;
NoOfBinsX=150;
MaxCutOffX=7;
MaxCutOffV=0.65;

%[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv]=
Find2DDensityAndCDFFromSimulation_Infiniti(X,V,paths,NoOfBinsX,NoOfBinsV);
[XYProbDensity2D,XYProbMass2D,XProbMass,VProbMass,IndexMaxX,IndexMaxV,Xn,Vm,Zx,Zv,BinSizeX,BinSizeV]=
Find2DDensityAndCDFFromSimulation_Infiniti04(X,V,paths,NoOfBinsX,NoOfBinsV,MaxCutOffX,MaxCutOffV);
%[XYProbDensity2D,XYProbMass2D,XProbMass,YProbMass,IndexMaxX,IndexMaxY,Xn,Ym,Zx,Zy,BinSizeX,BinSizeY]
%Please look at matlab file of above function for etailed explanation of
%all its input and output parameters.

surf(Xn,Vm,transpose(XYProbDensity2D))

xlabel('Asset'), ylabel('Stochastic Volatility'), zlabel('Probability Density 2D')
title('Graph of 2D Density of Asset and SV from Parzen Density')

MeanX=sum(X(1:paths))/paths
MeanV=sum(V(1:paths))/paths

str=input("Look at 3D graphs of the numerical density")

%Below calculate Coeffs of 2D Hermite products.
%Oxn is order of Zx hermites. ranges from 1 to 8 in indexing or (0 to 7 in reality)
%Ovm is order of Zv hermites. ranges from 1 to 8 in indexing or (0 to 7 in reality)
%HermiteH(Oxn,Zx(nn,mm)) is a small function that caclulates Oxn order hermite at Zx(nn,mm) value
%HermiteH(Ovm,Zv(mm)) caclulates Ovm order hermite at Zy(mm) value
%Below Eq calculates 2D Coeffs with inner product of coordinates of 2D uniform grid with
%product of X and V hermites.

C(1:8,1:8)=0;

for Oxn=1:8
    for Ovm=1:8
        for nn=1:(NoOfBinsX+1)
            for mm=1:(NoOfBinsV+1)
               
C(Oxn,Ovm)=C(Oxn,Ovm)+1/factorial(Oxn-1)/factorial(Ovm-1).*Xn(nn).*Vm(mm).*HermiteH(Oxn-1,Zx(nn,mm)).*HermiteH(Ovm-1,Zv(mm)).*XYProbMass2D(nn,mm);
               
%C(Oxn,Ovm)=C(Oxn,Ovm)+1/factorial(Oxn-1)/factorial(Ovm-1).*Xn(nn).*HermiteH(Oxn-1,Zx(nn,mm)).*HermiteH(Ovm-1,Zv(mm)).*XYProbMass2D(nn,mm);

            end
        end
    end
end

C

%If C are 2D hermite Coeffs as calculated in above equation
%Hermite Series representation of 2D random variable would be given by
%double sum equation below as
%Sum_{n=0}^{n=7} Sum_{m=0}^{m=7} C(n+1,m+1) He(n,Zx) He(m,Zy);

str=input("Look at Coefficients of 2D Hermite products")

%Below we calculate 1D Hermite Series for volatility.
%We only need to calculate the mean (zeroth hermite) aH0 of the volatility
%random variable.

aH0=0;
aH(1:7)=0;
for nn=1:IndexMaxV
aH0  =  aH0+Vm(nn).*VProbMass(nn);
aH(1)=aH(1)+Vm(nn).*Zv(nn).*VProbMass(nn);
aH(2)=aH(2)+.5*Vm(nn).*(Zv(nn).^2-1).*VProbMass(nn);
aH(3)=aH(3)+1/6*Vm(nn).*(Zv(nn).^3-3*Zv(nn)).*VProbMass(nn);
aH(4)=aH(4)+1/24*Vm(nn).*(Zv(nn).^4-6*Zv(nn).^2+3).*VProbMass(nn);
aH(5)=aH(5)+1/120*Vm(nn).*(Zv(nn).^5-10*Zv(nn).^3+15*Zv(nn)).*VProbMass(nn);
aH(6)=aH(6)+1/720*Vm(nn).*(Zv(nn).^6-15*Zv(nn).^4+45*Zv(nn).^2-15).*VProbMass(nn);
aH(7)=aH(7)+1/720/7*Vm(nn).*(Zv(nn).^7-21*Zv(nn).^5+105*Zv(nn).^3-105*Zv(nn)).*VProbMass(nn);
end

[a0,a] = ConvertHCoeffsToZCoeffs(aH0,aH,7);

a0
a

str=input("Look at volatility coefficients ----a0,a(1:7)");

%Below we calculate the Hermite series of asset by integrating over the
%volatility to get marginal series of asset. When we integrate over
%volatility, all volatility hermites(alone or as products with X-hermites)
%in the 2D asset series go to zero(they all have mean zero).
%So basically all volatility terms go to zero and we are left with
%one dimensional array containing terms from 2D series where
%volatility hermites in the product had order zero. This order zero is
%represented by volatility index one in the 2d array of coeffs C(n,m);
%So our 1D asset series is from the line C(1:8,1) where volatilit hermites
%are zero. This is very interesting.

bH0=C(1,1);
bH(1:7)=C(2:8,1);

%Above bH0 is asset Hermite series coeff of zeroth order hermite and
%bH(1:7) represent hermites from 1st to 7th order.

bH0=bH0/aH0;
bH=bH/aH0;

%Above, we need to normalize the asset hermite series with expected value
%of volatility since we integrated over the volatility. Just like in
%Conditioning when we integrate over a variable to get marginal density and
%then we have to divide with the integral of the integrated density as
%well. Similalry, Here we have to divide with the mean/expected value of
%volatility hermite series(which is integral of the volatility hermite series)
%to normalize our asset equation hermite coefficients.

%Below we convert from hermite series to Z-series of the asset for
%plotting.
[b0,b] = ConvertHCoeffsToZCoeffs(bH0,bH,7);

bH0
bH

b0
b

str=input("Look at 1D Coeffs of X")

[pXY2D] = Calculate2VariablesOn2DGridFrom2DZSeries(Xn,Vm,NoOfBinsX,NoOfBinsV,C,a0,a,BinSizeX,BinSizeV);

Xn0(1:NoOfBinsX-1)=Xn(2:NoOfBinsX);
Vm0(1:NoOfBinsV-1)=Vm(2:NoOfBinsV);
pXY2D0(1:NoOfBinsX-1,1:NoOfBinsV-1)=pXY2D(2:NoOfBinsX,2:NoOfBinsV);

%surf(Xn,Vm,transpose(pXY2D))
surf(Xn0,Vm0,transpose(pXY2D0))
xlabel('Asset'), ylabel('Stochastic Volatility'), zlabel('Probability Density 2D')
title('Graph of 2D Density of Asset and SV From Z-series')
str=input("Look at graph of Analytic 2D density");
XYProbDensity2D0(1:NoOfBinsX-1,1:NoOfBinsV-1)=XYProbDensity2D(2:NoOfBinsX,2:NoOfBinsV);
surf(Xn0,Vm0,transpose(pXY2D0-XYProbDensity2D0))
xlabel('Asset'), ylabel('Stochastic Volatility'), zlabel('Difference of Probability Density 2D')
title('Graph of 2D Difference of Parzen Density and Z-series Analytic Density of Asset and SV on the same grid')
str=input("Look at difference of Analytic and Numerical density graphs")

end
```

.

.

.

```
function [XYProbDensity2D,XYProbMass2D,XProbMass,YProbMass,IndexMaxX,IndexMaxY,Xn,Ym,Zx,Zy,BinSizeX,BinSizeY] =
Find2DDensityAndCDFFromSimulation_Infiniti02(X,Y,Paths,NoOfBinsX,NoOfBinsY,MaxCutOffX,MaxCutOffY)

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

meanX=sum(X(:))/Paths;
meanY=sum(Y(:))/Paths;
sdX=sqrt(sum((X(:)-meanX).^2));
sdY=sqrt(sum((Y(:)-meanY).^2));

Xmin=99999;
Xmin1=999998;
Xmin2=999997;
Xmax=0;
Xmax1=1*10^(-12);
Xmax2=1*10^(-11);

Ymin=999999;
Ymin1=999998;
Ymin2=999997;
Ymax=0;
Ymax1=1*10^(-12);
Ymax2=1*10^(-11);
%meanX=0;
%meanY=0;
for p=1:Paths

if(isreal(X(p))==0)
    X(p)
    str=input("Look at X(p)");
end
if(isreal(Y(p))==0)
    Y(p)
    str=input("Look at Y(p)");
end

if(X(p)>MaxCutOffX)
X(p)=MaxCutOffX;
end
if(Y(p)>MaxCutOffY)
Y(p)=MaxCutOffY;
end

if(Xmin>real(X(p)))
    Xmin2=Xmin1;
    Xmin1=Xmin;
    Xmin=real(X(p));
elseif(Xmaxreal(Y(p)))
    Ymin2=Ymin1;
    Ymin1=Ymin;
    Ymin=real(Y(p));

elseif(YmaxIndexMaxX)
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

%BinSizeX
%BinSizeY

%str=input("Look at BinSizes");

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
function [pXY2D] = Calculate2VariablesOn2DGridFrom2DZSeries(XX,YY,NoOfBinsX,NoOfBinsY,C,a0,a,BinSizeX,BinSizeY)

%YY are Y-coordinates of 2D Grid. In our case this is stochastic
%volatility and is univariate and independent of asset so it can be
%inverted as a univariate Z-series. its Z-series is given by a0 and a.

[Zy] = CalculateZgivenXAndZSeriesC7(YY,a0,a);

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

% Hermite2DSeries(1:NoOfBinsX+1,1:NoOfBinsY+1)=0;
% %
%  for nn=1:NoOfBinsX+1
%      for mm=1:NoOfBinsY+1
%      for Oxn=1:8
%      for Ovm=1:8
%           
Hermite2DSeries(nn,mm)=Hermite2DSeries(nn,mm)+C(Oxn,Ovm).*HermiteH(Oxn-1,Zx(nn,mm)).*HermiteH(Ovm-1,Zy(mm));
%      end
%      end
%      end
%  end

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
for mm=2:NoOfBinsY
    for nn=2:NoOfBinsX

    pXY2D(nn,mm) = (normpdf(Zx(nn,mm),0, 1))*abs(DinvfXX(nn,mm)).*(normpdf(Zy(mm),0, 1))*abs(DinvfYY(mm));

    end
end

end

```

.

.

.

```
function [Z] = CalculateZgivenXAndZSeriesC7(X,c0,c)

Z(1:length(X))=0;

for nn=1:length(X)
    %X(nn)
    %c0
        Z(nn)=CalculateZgivenXAndZSeriesBisection2C7(X(nn),c0,c);
    %Z(nn)
end

end

```

.

.

.

```
function [Z]=CalculateZgivenXAndZSeriesBisection2C7(Y,c0,c)

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
    if(Y  EvaluateZSeriesC7(c0,c,Zmid))
            Za=Zmid;
        end
    Z=.5*Za+.5*Zb; %This can be taken out of the loop and does not
    %necessarily have to be calculated again and again. Has to be
    %calculated at least once after the loop to determine the true value of
    %Z.

    end

end

if(Y  EvaluateZSeriesC7(c0,c,-.5))
        Za=-.5;
        Zb=0;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-1))
        Za=-1;
        Zb=-.5;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-1.5))
        Za=-1.5;
        Zb=-1;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-2))
        Za=-2;
        Zb=-1.5;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-2.5))
        Za=-2.5;
        Zb=-2.0;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-3))
        Za=-3;
        Zb=-2.5;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-3.5))
        Za=-3.5;
        Zb=-3.0;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-4))
        Za=-4;
        Zb=-3.5;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-4.5))
        Za=-4.5;
        Zb=-4.0;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-5))
        Za=-4.5;
        Zb=-5.0;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-5.5))
        Za=-5.0;
        Zb=-5.5;
    elseif(Y>  EvaluateZSeriesC7(c0,c,-6.0))
        Za=-5.5;
        Zb=-6.0;
    else
        Za=-12.0;
        Zb=-6.0;
    end
    for mm=1:35
        Zmid=.5*Za+.5*Zb;
        if(Y EvaluateZSeriesC7(c0,c,Zmid))
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

```
function [X] = EvaluateZSeriesC7(c0,c,Z)

X=c0+c(1)*Z+c(2)*Z.^2+c(3)*Z.^3+c(4)*Z.^4+c(5)*Z.^5+c(6)*Z.^6+c(7)*Z.^7;

end

```

.

.

.

This is the last few outputs you should see on your screen when you run this program.

a0 =

   0.051856848795143

a =

  Columns 1 through 3

   0.025308447061333   0.006232951335150   0.001147500450485

  Columns 4 through 6

   0.000877636380746   0.000394818257614  -0.000020803817895

  Column 7

  -0.000017810888272

Look at volatility coefficients ----a0,a(1:7)

bH0 =

   0.999230567144020

bH =

  Columns 1 through 3

   0.608033135481096   0.159292825114088   0.027749297555118

  Columns 4 through 6

   0.002484662411384  -0.001193699130006  -0.000894232267067

  Column 7

  -0.000332249594428

b0 =

   0.860805213270085

b =

  Columns 1 through 3

   0.541765963280562   0.104144398627779   0.004800081440268

  Columns 4 through 6

   0.015898146417386   0.005783542352976  -0.000894232267067

  Column 7

  -0.000332249594428

Look at 1D Coeffs of X

str =

     []

Zy =

  Columns 1 through 3

  -2.634004451734654  -2.167319894339016  -1.506064279914426

  Columns 4 through 6

  -0.874060740963614  -0.403909689433931  -0.028130067155871

  Columns 7 through 9

   0.288271345467365   0.559033179619291   0.791351162428327

  Columns 10 through 12

   0.991148471650376   1.164052401240042   1.315111681913550

  Columns 13 through 15

   1.448541791520256   1.567709385250055   1.675248979525350

  Columns 16 through 18

   1.773211661733512   1.863199918814644   1.946475835640740

  Columns 19 through 21

   2.024043532168434   2.096710658392112   2.165133997455996

  Columns 22 through 24

   2.229853354067018   2.291316897368233   2.349900274937681

  Columns 25 through 27

   2.405921167512133   2.459650482451252   2.511321048172249

  Columns 28 through 30

   2.561134433439292   2.609266346429649   2.655870948154188

  Columns 31 through 33

   2.701084328444267   2.745027330245648   2.787807863038324

  Columns 34 through 36

   2.829522812062351   2.870259626048210   2.910097647218208

  Columns 37 through 39

   2.949109233573836   2.987360712962982   3.024913200300944

  Columns 40 through 42

   3.061823303280107   3.098143736897327   3.133923863621021

  Columns 43 through 45

   3.169210173226020   3.204046713879507   3.238475484708033

  Columns 46 through 48

   3.272536798591318   3.306269623215485   3.339711907850869

  Columns 49 through 51

   3.372900903174013   3.405873481293384   3.438666464011476

  Columns 52 through 54

   3.471316967836174   3.503862775753078   3.536342747749586

  Columns 55 through 57

   3.568797284948232   3.601268866150349   3.633802681411908

  Columns 58 through 60

   3.666447395451542   3.699256085390516   3.732287414874008

  Columns 61 through 63

   3.765607132278092   3.799290020535409   3.833422487899952

  Columns 64 through 66

   3.868106089015782   3.903462431546359   3.939640211632650

  Columns 67 through 69

   3.976825640718744   4.015258517880284   4.055258214437345

  Columns 70 through 72

   4.097268263758451   4.141938997338002   4.190297468179779

  Columns 73 through 75

   4.244153386120161   4.307333394208399   4.391834105372254

  Column 76

   5.000000000000000

Look at Zy

Look at graph of Analytic 2D density

Look at difference of Analytic and Numerical density graphs

.

.

.

These are some output graphs in no particular order

[](https://postimg.cc/wtXfRDyB)

[![Image](../images/i.postimg.cc/t48kGmVR/Stoch-Vol2-D10-A.png)](https://postimg.cc/3kCmg1Bz)

[![Image](../images/i.postimg.cc/dVh6XK3S/Stoch-Vol2-D10-B.png)](https://postimg.cc/cvNfg2QQ)

[![Image](../images/i.postimg.cc/tCSD2gqx/Stoch-Vol2-D11-A.png)](https://postimg.cc/N5X10Brs)

[![Image](../images/i.postimg.cc/xdHRfyKv/Stoch-Vol2-D11-B.png)](https://postimg.cc/HJY53Mvn)

[![Image](../images/i.postimg.cc/3RTZd4BP/Stoch-Vol2-D11-Diff.png)](https://postimg.cc/DWxGNzRg)

[](https://postimg.cc/MMt9dxY2)

---

### #1987 — Amin (Topic Author)
*September 27, 2023, 8:24 AM*

In the case of SV modelling, one SDE of volatility is independent of Asset and is fully univariate while second variable
asset is bivariate and depends on both itself and volatility. Since volatility is independent, it really helps in
inversion of 2D Hermite Series to find the density of asset but if both variables would be dependent on each other and
both variables are bivariate, the inversion of Hermite Series would be more difficult. But I still believe that it can
be handled by a 2D Bisection like algorithm. I would like to work on it but it would be slightly off topic for current
project in mathematical finance. However if some friends have any such completely bivariate model, and they want to
solve it, please let me know and give me the data and I would try to write the 2D bisection algorithm in my free time. I
am sure it can be done.

---

### #1988 — Amin (Topic Author)
*September 27, 2023, 8:56 PM*

Friends, I want to very briefly explain the algorithm for inversion of 2D Hermite series to get the bivariate
probability density on the specified grid of asset$X_n$ and volatility$V_m$ on a uniform or non-uniform rectangular
grid. My notation might be different from matlab program.

We have an independent univariate Z-series/Hermite Series of volatility.

$V(Z_v)\, = \, c_0 \, + c_1 \, Z_v \,+ c_2 \, {Z_v}^2 \,+ c_3 \, {Z_v}^3 \,+ c_4 \, {Z_v}^4 \,+ c_5 \, {Z_v}^5 \,+ c_6 \, {Z_v}^6 \,+ c_7 \, {Z_v}^7 \,$

Equation(1)

Each point on stochastic volatility grid is represented as$V_m$ and this variable has a numerical value$v_m$ at that
point.

We first invert the above Z-series of volatility in Eq(1) to find the value of$Z_v(m)$ on each volatility grid point
$V_m$ . I have used the more stable bisection root finding procedure for that. So that$V_m(Z_v(m))\, =\, v_m$

Then we have equation for bivariate Hermite Series that is equal to bivariate product of stochastic volatility and asset
on each cell of the rectangular grid.

This equation is given as

$U(Z_x,Z_y) \, =\, \sum\limits_{k_1=0}^7 \, \sum\limits_{k_2=0}^7 \, C(k_1,k_2) \, H_{k_1}(Z_x) \, H_{k_2}(Z_y) $
Equation(2)

We can also write the above bivariate product U on the grid points  (X_n,V_m) as

$U(Z_x(X_n,V_m),Z_y(V_m)) \,=X_n\, V_m $

We already know the value of$Z_v(V_m)$ on all of the volatility grid points as we earlier did that. We substitute the
numerical value of$Z_v(V_m)$ in the two dimensional hermite series (sequentially for each grid point$V_m$ ) to get a
Z_series/Hermite Series only in$Z_x$ . This new series in only in$Z_x$ since numerical value of$Z_v(V_m)$ has been
substituted in the bivariate Hermite Series. This resulting Hermite Series in$Z_x$ is the product of univariate hermite
Series of$X_n$ , representing the X_axis associated with the particular value of stochastic volatility associated with
$Z_v$ that we had substituted in the 2D Hermite Series.

To get a pure Z-series of X-axis assiociated with the particular stochastic volatility point we divide the above
resulting Z-series with the value of$V_m=v_m$ on that volatility grid point. And after the division with volatility at
that grid point, it gives us a true Z-series of X-axis associated with the particular grid point$V_m$

Writing the above explanation in the form of Equations, we have if the numerical value of stochastic volatility at mth
grid point$V_m=v_m$ , and associated numerical value of underlying$Z_v=z_m$ , we substitute it in the 2D Hermite
Equation U and divide by$v_m$ . This division is done since U here is product of$X_n$ and$V_m$ and we want to divide by
$V_m=v_m$ to get the equation of only$X_n$ out of the equation of the product.

$X(Z_x(n,m)) \, =\Large \, \frac{\, U(Z_x(X_n,V_m),Z_v(V_m)) \, \LARGE {|}^{Z_v(V_m)=z_m}}{v_m}$  Equation(3)

The above formula gives us a univariate Hermite Series for that line of asset grid that is associated with mth
volatility grid point$V_m$ . This univariate Z-series can easily be inverted with our bisection algorithm to find$Z_x$
associated with$X_n$ line on mth volatility grid point.

The above formula is repeated for each of the points$V_m$ on the stochastic volatility grid and it gives us a Z-series
that is valid on the X points associated only for mth volatility grid cell.

if total number of volatility grid points is M, We can then invert each of the M dependent Z-series to get the value of
$Z_x(n,m)$ . Each of the Z-series is valid for X points associated with that particular volatility grid point that was
substituted in the Equation(3) to get the value of Z-series. All of these M Z-series are inverted with the bisection
root-finding algorithm that I have previously posted by using a loop that has M iterations.

So with above analytics, we calculate$Z_x(n,m)$ and$Z_v(m)$ associated with each grid point$X_n$ and$V_m$ on the
rectangular grid.

After this we calculate the derivatives$\frac{dZ_v(m)}{dV_m}$ and$\frac{dZ_x(n,m)}{dX_n}$ on all of the grid points
using simple finit differences. These derivatives are then used to calculate the Jacobian of the density of bivariate
variable$X_nV_m$ with respect to two standard normals.

Since stochastic volatility did not have any dependence on$Z_x$ , our jacobian is simply product of above two
derivatives.

We get the Equation of Bivariate Density as

$p(X_n,V_m)\, = \, p_N(Z_x(n,m)) \, \frac{dZ_x(n,m)}{dX_n} \,  \, p_N(Z_y(m)) \, \frac{dZ_y(m)}{dV_m} \,$

Here in the RHS of Equation $p_N$ denotes standard normal density.

---

### #1989 — Amin (Topic Author)
*September 28, 2023, 8:28 AM*

Friends, I have another idea to find coefficients of 2D Hermite Series for SV models by least squares polynomial
regression. I had first tried this idea on univariate data with limited success. But later when I standardized the
univariate data and then ran the regression, my results were very good. I was just using several tens of data points. In
monte carlo setting, I believe that we can only use several tens of thousands of paths to get a very stable estimate of
2D Hermite series coefficients with least squares polynomial regression method. In my last program, I was using half a
million paths for reasonably stable numerical density but I really think that in a polynomial regression setting, we
could do well only with fifty thousand or even less paths or even smaller if we use low discrepancy sequences.

I really want to try this idea within next two days and post the matlab program and results of my work on the forum.

---

### #1990 — Amin (Topic Author)
*September 29, 2023, 7:54 AM*

Friends, I really believe that in a civilized society of twenty first century there is absolutely no place for
connivance and machinations of a group of rich jews led by jewish billionaire Godfather of mind control who have
retarded, at whim, thousands of talented intelligent people in America and abroad that they did not like. These cruel
people are inhuman animals even though they have learnt to adjust extremely well within American society.

These corrupt crooks are very powerful and they have already complete control over American army and a large number of
politicians. Due to this huge influence and power, it is very difficult to do anything to undo the cruel mind control
network led by jewish billionaire and his rich jewish cohort.

I have suggested several times previously to good American people if nothing else works, please just ask some patriotic
American investigative journalists in major newspapers to run a comprehensive story about mind control network of jewish
billionaire and the nexus between rich jews and American defense and about tens of thousands of people that have been
retarded over past thirty years.

I want to invite patriotic American journalists from CNN, Washington Post, New York Times, Guardian or some other large,
reputed and responsible US or European media outlets to run a thorough story on machinations of evil jews led by jewish
billionaire and the  nexus of bad jews with American defense and their cruel mind control network that has retarded tens
of thousands of very intelligent Americans and foreigners all over the world.

Since good people may not have the power to forcefully end the evil practices of the powerful nexus between evil Jewish
billionaire and US army crooks, only way to end the cruel and subhuman practices of the nexus seems to be exposing them
openly in US public and the public of other countries all across the world.

I think it is important for us to make sure there is a better future of American children and children all across the
world and we leave them a legacy in which fairness and justice prevails as opposed to machinations, trickery and deceit
that has been unleashed in the society by the jewish billionaire and his rich jewish cohort.

---

### #1991 — Amin (Topic Author)
*September 29, 2023, 11:06 AM*

Friends, In my last matlab program with finding 2D Density of SV model with hermite polynomials, I used Zx(n,m) i.e
there is a different Zx for each volatility grid cell. Though it seemed to work decently, I think I need to calculate a
single universal Zx for all of the volatility grid cells. I want to try this and see how the new program works with a
single universal Zx.

For calculation of 2D hermite series of SV model with polynomial regression that I suggested yesterday, I have to take a
single universal Zx. I have worked out details of that but I want to see how a single Zx goes with the previous program.

---

### #1992 — Amin (Topic Author)
*September 29, 2023, 6:22 PM*

Mind control technology was developed with the help of large number of neurotransmitter experts and some of them at the
top of their profession. And a large number of neurotransmitter experts are provided data of neurotransmitter
interactions in the brain of several mind control victims (especially when victims are hard to retard) and they advise
American defense, after analyzing the data, which neurotransmitters to block and how to reconnect the victims's brain in
order to successfully retard the victim. These neurotransmitter experts continue to analyze the data to make suggestions
to mind control agencies. These neurotransmitter experts are extremely exorbitantly paid by American defense for their
services.

And sometimes when a more well known victim has to be retarded and people around the target are absolutely opposed to
let any body harm the target victim, American defense tells the responsible people around the target victim that a
certain leading neurotransmitter expert has told them with perfect certainty that the target victim has evil
neurotransmitters. And since very exorbitant amounts of money are paid to neurotransmitter experts, these
neurotransmitter experts make a solemn face and blurt totally complete lies in the most professional way to tell the
people around the victim that the victim indeed has extremely evil neurotransmitters. These dishonest neurotransmitter
experts tell complete lies of the sort that whoever they knew with certain neurotransmitter always turned evil. Since
non-professional people have no way to know, many of them can be deceived easily by professional dishonesty of the
experts.

Has anything like this ever happened to someone around you? You have been thoroughly wronged by dishonest experts.

---

### #1993 — Amin (Topic Author)
*September 29, 2023, 8:48 PM*

Friends, I really think that we need to do more work on representation of two random variables that are dependent or
those that are correlated with appropriate Z-series.

When one of the random variables is dependent on other, this dependence can be captured by making coefficients of its
Z-series a function of the other random variable. For example if independent Z-series of volatility is given as

$\, V \, = \, b_0 \, + \, b_1 \, Z_v \,+ \, b_2 \, {Z_v}^2 \,+ \, b_3 \, {Z_v}^3 \,+ \, b_4 \, {Z_v}^4 \,+ \, b_5 \, {Z_v}^5 \,+ \, b_6 \, {Z_v}^6 \,+ \, b_7 \, {Z_v}^7 \,$

Then dependent Z-Series of asset can be represented as

$\, X \, =\, c_0 \, + \, c_1(Z_v) \, Z_x \,+ \, c_2(Z_v) \, {Z_x}^2 \,+ \, c_3(Z_v) \, {Z_x}^3 \,+ \, c_4(Z_v) \, {Z_x}^4 \,+ \, c_5(Z_v) \, {Z_x}^5 \,+ \, c_6(Z_v) \, {Z_x}^6 \,+ \, c_7(Z_v) \, {Z_x}^7 \,$

So when a Z-series is dependent on other, this dependence has to be captured by making its coefficients a function of
the other Z-series variable. These coefficients have to be found so that dependence structure is properly captured.

However when a random variable is non-dependent but correlated with another random variable, this correlation has to be
captured by

$\, X \, =\, c_0 \, + \, c_1 \, Z_x \,+ \, c_2\, {Z_x}^2 \,+ \, c_3 \, {Z_x}^3 \,+ \, c_4 \, {Z_x}^4 \,+ \, c_5 \,
{Z_x}^5 \,+ \, c_6 \, {Z_x}^6 \,+ \, c_7 \, {Z_x}^7 \, \\

+\, \, d_1 \, Z_y \,+ \, d_2\, {Z_y}^2 \,+ \, d_3 \, {Z_y}^3 \,+ \, d_4 \, {Z_y}^4 \,+ \, d_5 \, {Z_y}^5 \,+ \, d_6 \,
{Z_y}^6 \,+ \, d_7 \, {Z_y}^7$

Coefficients in above Z-series are chosen so that marginal moments and correlations are simultaneously retrieved.

So dependence goes into coefficients and is captured by making coefficients of dependent Z-series function of the other
Z-series, while correlation is captured by appending one Z-series with other Z-series whose coefficients are chosen to
capture the correlation structure.

When a random variable is both dependent and correlated, I think we could possibly represent it as a Z-series as

$\, X \, =\, c_0 \, + \, c_1(Z_y) \, Z_x \,+ \, c_2(Z_y)\, {Z_x}^2 \,+ \, c_3(Z_y) \, {Z_x}^3 \,+ \, c_4(Z_y) \, {Z_x}^4
\,+ \, c_5(Z_y) \, {Z_x}^5 \,+ \, c_6(Z_y) \, {Z_x}^6 \,+ \, c_7(Z_y) \, {Z_x}^7 \, \\

+\, \, d_1(Z_y) \, Z_y \,+ \, d_2(Z_y)\, {Z_y}^2 \,+ \, d_3(Z_y) \, {Z_y}^3 \,+ \, d_4(Z_y) \, {Z_y}^4 \,+ \, d_5(Z_y)
\, {Z_y}^5 \,+ \, d_6(Z_y) \, {Z_y}^6 \,+ \, d_7(Z_y) \, {Z_y}^7$

This would be very interesting how to empirically calculate the coefficients of Z-series of dependent random variable
with a certain dependence structure and same for correlated Z-series and dependent correlated Z-series.

I will try to think more about it but if we can somehow find numerical algorithms to construct dependent and correlated
Z-series, it will be a great boost for our research towards practical applications of Z-series. I really think this
would be really remarkable if we can construct algorithms for calculation of dependent and correlated Z-series.

There are other very interesting things we can do with further research. For example in order to represent a Z-series
that encompasses a reasonably large class of SDEs, we can possibly make coefficients of the Z-series a function of the
SDE parameters so that when parameters of the SDE change, coefficients of the Z-series are automatically altered(as they
are functions of parameters) to capture the density of the SDE with particular parameters so that a single general
Z-series could be used to represent an SDE variable with SDE parameters over a reasonably large range. This can be
probably be impossible for a large time step/frame but I think it can be done for an arbitrary initial distribution
(with a given Z-series) and an arbitrary SDE(with a reasonably large range of parameters) over a small time step of 1/16
or so (for most of the SDEs we use in finance) so that coefficients of resulting Z-series are functions of the SDE
parameters.

And especially if we can do that with Z-series of stochastic volatility and dependent asset in an SV model.

---

### #1994 — Amin (Topic Author)
*September 30, 2023, 10:17 AM*

Friends, when I first worked on hermite regressions, I really thought that they could replace AI in several important
problems related to random processes (Well, AI can always absorb Mathematics and start doing more interesting things).

Last night I continued to think of alternative and better ways to find a Z-series representation of both asset and
volatility in coupled SV models given the numerical density. And then I realize that this is one of the places where we
can easily use hermite regressions to find the bivariate coefficients of asset both in correlated and non-correlated
models.

I want to briefly share my ideas with friends about how to use the hermite regressions in our problem.

First we construct a bivariate grid and find the univariate Z-series of independent stochastic volatility. Then we
construct a conditional Z-series of asset for every volatility grid point. There will be as many asset Z-series as
points on the volatility axis of the bivariate grid, each for every volatility point.

All of the asset Z-series will have different coefficients and even median of every asset Z-series would be different.

We will calculate moments of each of the coefficients of asset Z-series across all volatility Z-series and use our
Z-series construction from moments method to fins the Z-series representation of each of the coefficients of asset
Z-series. For eight coefficients, this will give us eight Z-series representing distribution of each coefficient across
all of the asset Z-series(that are in turn dependent on volatility value of each volatility grid point).

Then we  hermite regress Z-series of each coefficient on Z-series of the independent volatility to extract the
dependence structure of asset Z-series coefficients on independent volatility. This regression will be repeated for each
of the eight asset Z-series coefficients.

Briefly, for hermite regressions, we will calculate value of hermite polynomials of each coefficient on all of the
volatility grids and pair them with values of hermite coefficients on independent volatility on all of the associated
volatility grids and then run hermite regression using all these pairs.

For example this method will give us a bivariate Z-series of asset and we will automatically get conditional Z-series of
asset at any volatility grid point simply by substituting the value of volatility Zv associated with that volatility
grid point.

This method would work well for both correlated and non-correlated SV SDEs.

I assure friends that it would work very well and will be a wonderful application of hermite regressions method we
discovered earlier this year. And I hope we will start using hermite regressions in several similar problems more
freely.

Though slightly prudent due to pressure from good people, mind control agents remain totally malicious and continue to
try to reconnect my brain with a sense of urgency. Many times they use another different gas in my room and other
places. When inhaled this gas cause uneasiness in the stomach and also slight pain and uneasiness in the spine. The
weather is becoming more pleasant and I sit in the garage/porch of our house at night since it is more open, airy  and
colder but still has walls and a gate that can let heavy gas accumulate there. They continue to release gas in the
garage. Even if I do not turn on the ceiling fan to avoid the gas, they still release gas that continues to accumulate
in the garage. For past two nights, I completely open the gates of the house/garage to not let the gas accumulate there
and spread out. When there is more gas and I am trying to think of some idea, I simply walk on the local street outside
my house to be able to think better.

I have an injection due on monday. I could not get any good injection from older manufacturing dates that I knew had
good injections so this time I just bought an injection with most recent manufacturing date I could get. I do not know
how it would go. But I have some good coffee and some good tea that would be very helpful. I do have a feeling that mind
control agents are bitterly waiting for the new injection to reconnect my brain, try to retard me somewhat and not let
me work properly. But I am also determined to continue my research.

---

### #1995 — Amin (Topic Author)
*October 1, 2023, 8:09 PM*

Friends, I could not login to wilmott from my computer. When I try to login from main wilmott site using my computer and
it says that my credentials are invalid. I could login from forums login page but it automatically logs me out when I
hit any button.

I could however login from my cell phone and write this post.

---

### #1996 — Amin (Topic Author)
*October 1, 2023, 8:53 PM*

Friends, mind control agencies were able to drug my food today. I was passing by General hospital on Ferozpur road and
decided to eat at hospital canteen. I forgot to notice that canteen was right at the door and had a direct entrance on
main road outside the hospital. While taking parking token at the gate where there were about five motorcycles ahead of
me in the line. It took me about two minutes to get the token.

I believe while I was in line for  token, somebody entered the canteen from outside gate and drugged the food.

After eating drugged food, my conception of reality changed and I started to see differently from my eyes. I could feel
that I was missing something in my brain. I washed my head right there and had some coffee(merely by mixing it in room
temp water).

Only when I left the hospîal, I realized that its canteen had an entrance outside the gate of hospital on the main road.

I was slightly getting worried but I kept myself totally calm with some effort.

In a little bit, I bought some traditional sweets and sweet milk from random places on small streets branching out of
ferozpur road. I was a bit better after that.

Then I drove my bike on narrow streets on one side of ferozpur road where I had never been before. I believe there was
no mind control infrastructure in those very poor neighborhoods. I felt quite better after that. I also continued to
wash my head and do tooth brush there.

Finally I came back. I am better now but feel something is still missing in my brain. They continue to pull drugs from
food in my stomach towards the brain to successfully block neurotransmitters that come back again and again.

After coming back, I mixed a lot of psyllium husk, I had boùht on the way, with water to cleanse my stomach and
intestines.

I have an injection due tomorrow so next few days can be difficult.

---

### #1997 — Amin (Topic Author)
*October 4, 2023, 5:46 AM*

Friends, I bought a totally new computer a few weeks ago but  Pakistan army on behest of corrupt American army scum
continues to play openly with my computer in my absence. They have completely muted sound on my computer (possibly
through playing with the hardware). I tried to restore the volume from settings everywhere but it simply does not work
and there is absolutely no sound in my computer now. It was working very well just a few days ago.

My mind control also continues unabated and there is extreme urgency (and huge increase of efforts) among mind control
infrastructure in Pakistan to somehow retard me. It is becoming more and more difficult to be able to get good food in
the city. They have been viciously trying to retard me and drug my food in past few days and I expect this to continue
for many coming weeks. I am trying to hold on but I do not know how long could I last since scale of Pakistan army
people following me all the time is simply huge.

I want to request European Embassies in Pakistan to please step forward and tell Pakistani people in their circles the
whole truth about mind control and also force government and military of Pakistan (that is puppet extension of corrupt
American defense) to end my mind control and mind control of other people in Pakistan.

I want to say to American friends that I tried to tell the truth about bad groups in United States for more than one and
a half decade(s) and I expect that a lot of people know that I was speaking the truth. Good Americans are a smart people
and I am sure they will try to take exactly right decisions for their nation and for rest of the world and they would
make sure that cruel injustice of mind control and related injustices from corrupt US defense end forever.

I have run my part of the race (even though I am ready to run another leg if things do not get better) and now baton is
in hands of Good and patriotic American people to make good and wise decisions about what is best for their country and
best for rest of the world to end the corruption in US defense and end machinations of bad people and also make sure
that bad people do not start machinating again. I just want to request good American people to know that there could be
attempts by bad people to make some possible settlement only to start machinating again(at a possibly decreased scale)
when the whole thing goes out of limelight.

---

### #1998 — Amin (Topic Author)
*October 6, 2023, 4:17 AM*

Friends, my research work for finding volatility dependent coefficients of hermite series of asset by hermite regression
is going well but rather slowly due to all the problems created by mind control agencies. I have constructed a variable
spacing grid for stochastic volatility. And then calculated first eight moments of dependent asset for each of the
voltility cell  (This calculation is done directly from data by using asset paths that lie in each stochastic volatility
cell instead of integrating over probability distributions). In order to make sure there are enough data memebers/paths
of asset that lie in the volatility cells that are in extreme tail, I paired six volatility cells in right tail to form
three resulting cells in modified tail so that asset density per cell increases in the tail for better calculation of
moments.

I am only using fifty grid cells for volatility but this seems enough since grid is variable.

Next step is to calculate asset Z-series for each of the volatility cell but this is easy since we have already
calculated moments of asset associated with  each volatility grid cell.

After that I would continue with regressing hermite polynomials of coefficients of all of the asset Z-series on hermite
polynomials of volatility.

---

### #1999 — Amin (Topic Author)
*October 6, 2023, 6:47 AM*

I am worried that agents who come to my house might permanently damage my new computer. As I told friends that they had
damaged my last computer I bought with very little money I had and that cost me about a thousand dollars.

They are also known for taking liberties with many of my old computers( I have bought about 8-10 laptop computers since
2010) like damaging the keyboard buttons, damaging usb ports and the speakers and sound system (on the previous old
computers).

They have already disabled the sound system(I believe through unplugging the hardware) of my new computer and there is
absolutely no sound on the new computer I bought a few weeks ago. I had described it in a post earlier as well.

---

### #2000 — Amin (Topic Author)
*October 7, 2023, 8:54 PM*

Friends, my research is going well. I have been able to make a variable grid in both volatility and asset. So asset grid
is different for each grid point of stochastic volatility associated with it.

Obviously the original target of research is to find the volatility dependent coefficients of the asset Z-series and I
am continuing work towards that but as a quick byproduct of the research, I was able to modify the earlier program that
constructed the numerical density of bivariate product of asset and volatility. In this new program the calculation of
2D Hermite Series is done on a coarse grid that is variable in both stochastic volatility and asset. Once the 2D Hermite
series has been calculated, it can be used to project the analytic density on a very refined grid that is uniform both
in stochastic volatility and asset.

I will try to post this interim program with above analytics tomorrow.

---

[← Previous](page_039.md) | [Index](index.md) | [Next →](page_041.md)
