# Breakthrough in the theory of stochastic differential equations and their simulation

**Page 32 of 59** — Posts #1551–#1600

[← Previous](page_031.md) | [Index](index.md) | [Next →](page_033.md)

---

### #1551 — Amin (Topic Author)
*September 24, 2022, 5:20 PM*

The function in the post above optimizes the weights/parameters when it is given an objective function that has to be
optimized. In my case the objective function is the output of a small independent function that takes some time series
parameters.

In a neural network, the objective function will represent the goodness of fit to the target output. In optimizing
weights of a neural network, you can also use mean squared error between network output and the target value, but this
mean squared error would have to be minimized while I am maximizing my objective function. I want to explain the program
in context of neural networks.

Here is the function I am using to calculate the objective function

[ObjOld] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w2,w3,w4,w5,w6);

.

Here network evaluation function gives the result ObjOld that you can substitute with sum of mean squared errors between
neural network calculated values of the target function and actual values of the target function. Xt1, Xt2, Price0,
VarLogR, T1 are input arrays that are required to calculate the objective function given the network weights w1, w2, w3,
w4, w5, w6.

We want to calculate the weights w1, w2, w3, w4, w5, w6 in a neural network so that ObjFunction/ObjOld is maximized or
alternatively any mean squared error/loss function is minimized.

If you have a multi-layered neural network, just add all the various weights on different layers sequentially (possibly
even using looping to calculate objective function with all weights sequentially one after the other) in main
optimization loop and the algorithm would optimize it well.

Here is the main optimization loop of the program that repeats the optimization over six weights a thousand times.

In my case all parameters were supposed to be between -1 and 1 and therefore I used just one single value of Delta
(which is projected change in weights in a single optimization) for all the weights. You will need some idea about the
domain on which weights will take values. if domains of various weights are different you can use a different value of
Delta proportional to domain and decrease values in larger domain slightly faster.

As I mentioned Delta is the projected change in weights and this starts with large values as if we are evaluating on a
coarse grid. I have taken an initial value of Delta =.15 when my domain is for weights is between -1 and 1 but I think
an initial value of .2 or .25 might have worked even better in some difficult cases.

We do 1000 iterations of the optimization over weights loop. At the start of the optimization, we set the value of
variable Update equal to zero. Whenever even a single weight is updated, the value of update turns true. However, when
no value is updates, we know it is time to decrease the step size Delta by a suitable value. I have chosen this value to
.8 but please feel free to experiment. After decreasing the value of Delta, the optimization starts again with a smaller
step size as if on a slightly finer grid. This way value of optimization step Delta continues to decrease and
optimization search for best weights is done on a successively finer grid.

Delta=.15;

for nn=1:1000

    Update=0;

    w10=w1+Delta;

    [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w10,w2,w3,w4,w5,w6);

    if(ObjNew>ObjOld)

        w1=w10;

        Update=1;

        ObjOld=ObjNew;

    else

        w10=w1-Delta;

        [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w10,w2,w3,w4,w5,w6);

        if(ObjNew>ObjOld)

            w1=w10;

            Update=1;

            ObjOld=ObjNew;

        end

    end

     w20=w2+Delta;

    [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w20,w3,w4,w5,w6);

    if(ObjNew>ObjOld)

        w2=w20;

        Update=1;

        ObjOld=ObjNew;

    else

        w20=w2-Delta;

        [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w20,w3,w4,w5,w6);

        if(ObjNew>ObjOld)

            w2=w20;

            Update=1;

            ObjOld=ObjNew;

        end

    end

    w30=w3+Delta;

    [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w2,w30,w4,w5,w6);

    if(ObjNew>ObjOld)

        w3=w30;

        Update=1;

        ObjOld=ObjNew;

    else

        w30=w3-Delta;

        [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w2,w30,w4,w5,w6);

        if(ObjNew>ObjOld)

            w3=w30;

            Update=1;

            ObjOld=ObjNew;

        end

    end

    w40=w4+Delta;

    [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w2,w3,w40,w5,w6);

    if(ObjNew>ObjOld)

        w4=w40;

        Update=1;

        ObjOld=ObjNew;

    else

        w40=w4-Delta;

        [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w2,w3,w40,w5,w6);

        if(ObjNew>ObjOld)

            w4=w40;

            Update=1;

            ObjOld=ObjNew;

        end

    end

    w50=w5+Delta;

    [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w2,w3,w4,w50,w6);

    if(ObjNew>ObjOld)

        w5=w50;

        Update=1;

        ObjOld=ObjNew;

    else

        w50=w5-Delta;

        [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w2,w3,w4,w50,w6);

        if(ObjNew>ObjOld)

            w5=w50;

            Update=1;

            ObjOld=ObjNew;

        end

    end

    w60=w6+Delta;

    [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w2,w3,w4,w5,w60);

    if(ObjNew>ObjOld)

        w6=w60;

        Update=1;

        ObjOld=ObjNew;

    else

        w60=w6-Delta;

        [ObjNew] = NetworkEvaluationFunction(Xt1,Xt2,Price0,VarLogR,Tl,w1,w2,w3,w4,w5,w60);

        if(ObjNew>ObjOld)

            w6=w60;

            Update=1;

            ObjOld=ObjNew;

        end

    end

    if(Update==0)

        Delta=Delta*.85;

    end

end

In the start of the program, I assign initial starting values to the weights being optimized using the following lines

w1=IValue(1,1);

w2=IValue(1,2);

w3=IValue(1,3);

w4=IValue(1,4);

w5=IValue(1,5);

w6=IValue(1,6);

I would urge friends to try this program on training their neural networks.

If you have a simple enough objective function that can be coded in matlab, and you would like me to optimize it for
you, please feel free to email me and I would love to see how my optimization routine works on it.

Also, for friends who have been following my thread, I want to mention that would do more and more work with neural
networks in the future and hope to continue to post interesting work and code about machine learning and neural
networks.

---

### #1552 — Amin (Topic Author)
*September 24, 2022, 5:38 PM*

Though I have described in the previous post but let me summarize the algorithm again that it optimizes weights of
neural network sequentially in the direction of increasing objective function, initially with a large step as if on a
very coarse grid. When coarse grid optimization ends, it slightly refines the grid and starts optimizing again and then
refines the grid again after it is finished optimizing at that level. So, it continues to refine the grid and starts
optimizing neural network weights on the fine grid successively after it is done optimizing on the coarser grid. Until
it reaches very close to the optimum value of weights. There is no fixed grid per se, but the step size towards
optimizing direction is quantized as if on a grid.

---

### #1553 — Amin (Topic Author)
*September 27, 2022, 9:06 AM*

Friends, I had worked with the above algorithm in case of a single neuron with six inputs and it worked great. I was
really expecting that it would work well on multi-layered network with one intermediate layer but when I tried the above
algorithm on a neural network with intermediate layer of neurons, its performance was poor.

That prompted me to think how we could systematically assign initial weights to a neural network before we enter the
optimization loop.

There are so many different kinds of neural networks, but my observations are only valid for neural networks that are
meant for prediction.

Let us consider a simple toy neural network with five inputs and three neurons in intermediate hidden layer and finally
one neuron at end that collects the output of three hidden layer neurons and gives us the final result as its output.

One observation that I was able to think was that weights between inputs and hidden layer should be so that output of
first hidden neuron should be orthogonal to both the outputs of second and third neuron in hidden layer. Similarly,
output of second neuron should be orthogonal to first and third neuron and so on for the last third neuron in the hidden
intermediate layer.

This prompts us to consider several training strategies. For example, optimize the weights on inputs to first hidden
layer neuron with zero weights on inputs to second and third hidden intermediate neurons. Once the final output has been
perfectly optimized with initial weights leading to first hidden intermediate layer neuron, it means that one factor has
been well calibrated.

Now train the weights leading to second intermediate layer neuron given the weights on first intermediate layer neuron
that we had previously optimized. So, we do not alter the pre-optimized weights of first neurons and only alter the
weights of second neuron but again do not yet alter the weights of third neuron and keep them at zero value. This way,
second intermediate layer neuron will pick the effects of second orthogonal factor after first factor has already been
perfectly optimized by first neuron in hidden layer.

In the last, we keep the optimized weights of first and second intermediate layer neurons fixed and alter the weights of
third neuron so that it can pick the effects of third orthogonal factor.

After this step, if desired, we can run some iterations of gradient descent optimization algorithm on all of the network
and hopefully the final values would not change by a large amount.

There is another strategy that can help us to pick initial weights. This is based on analogy with independent
factors/principal components. We run principal component analysis on all five inputs as we have five inputs in our toy
neural network. The weights to first neuron in hidden layer would be the weights of inputs on first principal component
while weight between first neuron in hidden layer and final neuron would be equal to correlation between first principal
component and the output.

Similarly, weights from inputs to 2nd hidden neuron would be equal to weights of inputs with respect to second principal
component and weight between second hidden neuron and the final neuron would be equivalent to correlation between
variable being predicted and the second eigenvector/principal component.

And similarly, for the weights on the final third neuron in hidden layer would be borrowed from third
eigenvector/principal component and correlation between third eigenvector and final predicted variable would give us the
weight between third intermediate neuron and the final one neuron in outer layer.

We can find initial values of the weights from above analysis and then use gradient descent to further optimize the
output so as to get best results.

Though I am sure it is easily comprehensible to most friends, I will try to explain things with equations if I could
find time tomorrow.

---

### #1554 — Amin (Topic Author)
*September 29, 2022, 4:51 AM*

Friends, I have been working to further improve my algorithms and got extremely good results on validation data. I will
start testing my algorithms initially on Biance testnet in another day. I just made some changes just yesterday that
further dramatically improved the results of my programs and when I went out on motorcycle for breakfast to a different
neighborhood, mind control agencies had made every preparation to drug my food. I was hit by drugged food multiple
times. Mind control agencies had drugged drinks at a large number of points. I was careful enough to go to a different
neighborhood to take food, but I never expected that they would drug the drinks at so many points. By the time I
returned, I noticed that my eyesight had dramatically deteriorated due to the effect of drugged drinks I had taken, and
it was becoming very difficult to read smaller words especially from a short distance and there was some sheer
uneasiness in the eyes.

I want to tell friends that racist conservative scumbags at pentagon find it verry difficult to allow muslims to get
ahead in any walk of life (even though we are the ones who are habitually called intolerant). I want to tell friends
that hatred in the hearts of these conservative scumbags of Pentagon is very similar to hatred that lies in the heart of
Talibans, the only difference is that these scumbags are far more powerful and do not have to resort to violence to
achieve their racist designs and rather use machinations to achieve their similar racist designs.

When I was in London 12 years ago, I wrote on Wilmott that mentality of a lot of racist scumbags of Pentagon is very
similar to mentality of Taliban of Afghanistan. I drew logical parallels and explained everything with reason. I will
post that article in a day if I can easily find it in my documents. I had stated that Taliban is not name of a group,
rather it is name of a mentality and racist scumbags of Pentagon are completely fraught with the same mentality.

---

### #1555 — Amin (Topic Author)
*September 29, 2022, 7:35 AM*

Here is what I wrote on Wilmott on Thu Apr 21, 2011, 11:00 PM. I have brought it back from my own records.

In my previous post I talked about the ideology of intolerance the word Taliban represents. Here I would like to make a
detailed comparison between the two groups of Taliban I mentioned in my previous post , one group of which is the
Taliban of Afghanistan and the other group is the racist Taliban of Pentagon. The original Taliban, as the world knows,
are characterized by their ignorance, lack of education, indoctrination of hardline versions of religion and of course
the two Taliban characteristics which are lack of tolerance and employing violent means to achieve their intolerant
version of the world. On the other hand Taliban of Pentagon are reasonably educated, very mediocre, embrace racism, have
a lot of resources available and share the taliban characteristics of lack of tolerance and employing sometimes violent
and usually cunning means to achieve their racist and intolerant version of the world. However what makes the Taliban of
Pentagon worse is that Taliban characteristics of Original Taliban can be blamed on lack of education and backwardness
of their society. On the other hand, racism and intolerance of the Taliban of Pentagon cannot be blamed on lack of
education and backwardness of their society and it is a characteristics actively chosen by a group that should be
decently aware of ideologies of human goodness as represented by the population from which it is chosen. This active
adoption of Taliban characteristics as opposed to passive Talibamism of Afghani Talibs makes Taliban of Pentagon more
hideous and abominable creatures. Afghani Taliban ruthlessly kill christian missionries while their racist counterparts,
the Taliban of Pentagon are more cunning and have sharpshooters who retard innocent and peace living Muslims of other
countries with the aim to inflict damage on their nations. Advanced technologies and abundance of money allows them to
hide their racist crimes and call themselves "responsible army". The Taliban of Afghanistan show indiscriminate hatred
and their acts result in just a few deaths but they earn stigma for their religion while the acts of Taliban of Pentagon
are more strategic because they result in making the children of our nations darker forever while earning no stigma for
their nations. The acts of Taliban of Pentagon are more hideous for our nations and act of Taliban of Afghanistan really
do not matter for anyone bust just a few individuals which of course, cannot be pardoned either but Talibanism of
Pentagon is more hideous than the Talibanism of Afghanistan, though underlying characteristics of Talibanism are the
same. The Taliban of Afghanistan are stupid while the racist Taliban of Pentagon are cunning, The Taliban of Afghanistan
kill ruthlessly while the Taliban of Pentagon retard someone and assign a group of mean mind control satans who continue
to insult and humiliate them all their life. I appeal to Taliban of Pentagon to learn from their Afghani counterparts
and kill instead of giving a life of humiliation since it is more graceful to die than have a life of humiliation

I would request Americans, who are in fact good and responsible, to eradicate racism from their society and from
Pentagon and make sure nobody innocent of any religion is retarded especially if they want to serve their nations and
have nothing against America. I would like to point out a fact from history that America was slower than rest of the
world to abolish several aspects of racism an example of that is the fact that slavery continued in America longer than
could be imagined especially given the advancement and prosperity of its society. Today,The case of racism of Satans of
Pentagon is very similar and should be addressed by responsible Americans.

---

### #1556 — Amin (Topic Author)
*October 1, 2022, 1:03 PM*

Friends, I deposited one BNB in my Binance account and generated API keys so that I can start running my programs on
binance testnet. I have installed Linux on an external hard drive with python, Visual studio code and anaconda. There
was always a bluetooth connection ON in Unix and I could not close it by simply clicking on the bluetooth icon. I looked
up on internet how to close it by going to linux shell and adding a further command so that it does not start when we
turn on linux. I also noticed that there was another shell open with suspicious activity and I closed it. I generated my
API keys after all of this. I plan to keep my small external hard drive on me when I go out. But I am still sure that
CIA crooks would try to install more devices on my laptop so that they can somehow approach the external hard drive from
my computer and play with my trading and do not let me succeed.

I have algorithms already set and I hope that after testing my programs on binance testnet for a few days, I will start
live trading in 5-10 days.

I want to request friends to convince the american army people to let me move on with my life after the forced coercion
of 23 years in which I continued to face trauma and torture again and again.

---

### #1557 — Amin (Topic Author)
*October 4, 2022, 10:32 AM*

Friends, I have been working during past few days to complete my coding to run my trading strategy on Binance. I have
started playing with live data from Binance but some of the coding remains to be done. I will continue coding and
testing my programs for next few days and hope that I will start trading live by 10th of October.

I had an antipsychotic injection yesterday and I have not been feeling very good, but I have started working on my
programs again.

I had earlier told friends that I had installed linux and python on an external hard drive and I keep the hard drive on
me when I leave the house. But I recently start to feel that they have broken into my hard drive since I noticed that my
programs were becoming very slow at times and linux system also becomes very slow sometimes. I will try to see what I
can do about it, but I would request friends meanwhile to please ask the mind control agencies to not alter my programs
or interfere in my trading activity.

I will keep posting here for friends how my trading goes when I start around 10th of October.

---

### #1558 — Amin (Topic Author)
*October 4, 2022, 1:14 PM*

I just turned on my linux ubuntu system and installed htop after finding about it on internet. When I used the htop
command on linux shell, I noticed that bluetooth process was working in the background even though its icon in the icons
tab was dim as if bluetooth were off.  I killed bluetooth and figured that there was another process avahi-daemon for
local home Lan was also on. I also stopped and then disabled avahi-daemon as well.

This was interesting. When I tried to disable avahi-daemon, system refused saying there are clients using it. I had to
stop it first with stop command and then system allowed me to disable it.

I am not a great expert at inside workings of computer systems and have to look up on internet about various things.

Mind control agencies already have my programs, but I am very afraid that they would start interfering in my trading
activity so as to fail me again. I want to request friends to please stop them from doing any interference in my trading
activity.

---

### #1559 — Amin (Topic Author)
*October 5, 2022, 2:13 PM*

Friends, I am fully convinced that mind control agencies have a plan to not let me make any profits in the market. And
they have already connived with my family about it.

The way relationships work in our family, everybody including myself tries to behave normally but when my family is
asked by the mind control agencies to do anything particular, most of the members of my family start behaving
differently.

It has been 23 years since I came back to Pakistan in Feb 1999. I was already more than one year into mind control in
United States at that time. When mind control agencies contacted my father (on the insistence of some malicious jews)
before I returned to Pakistan. My father agreed to fully cooperate and was in fact very happy about it that Americans
had placed so much trust in him. He was so stupid that he simply agreed that anything would be given to him and the
family after I would have been retarded. He agreed that if he took any money, it would become obvious to everyone due to
change of his circumstances that he had taken bribes from CIA. He was told that it would take only a few years to retard
me, and I could not remain sane before their potent mind control drugs, and he was very willing to wait a few years. In
early years when I would openly complain, my father would proudly retort that if he had cooperated with Americans, why
had he not taken any money. Later, I stopped questioning him.

There were so many times again and again when my family became desperate to somehow retard me and got me detained with
psychiatrists on totally flimsy excuses. I have been detained more than thirty times in past twenty three years. They
would give me drugs and take away some of my neurotransmitters and my relationship with the family would come back to
normal in a few weeks after I would be freed from detention. There would be times when I would be agitated that they
have no humanity for me, but I would simply tell myself to behave nicely with them. If I had not remained nice, I would
have faced far more trauma and torture. Many times, I would simply wonder how desperate people can become for money.

Ok, since no special money has yet been given to my family. About a month and a half ago, my brother almost begged me to
start trading in crypto since he had already become interested in crypto (and made large losses trading on high
leverage.) He had been helping me with data download and other simple chores and was very enthusiastic. I still had
enough regard for my brother and offered to share 25% of the profits with him.

But since I made improvements to my trading algorithms, things dramatically changed. My brother would visit me once or
twice upon my insistence and would tell me that I had to first prove that my algorithms could become profitable
(something I really have to do, of course) but a changed and stayed tone makes me realize that something is very wrong.
Today, my mother came to my room and asked me out of the blue, "Son, do you think that Binance exchange might create
problems for you and interfere in your trading?" Atmosphere in our house has already become silently tense.

I have complete faith in my algorithms. I checked them on large data by running the optimization algorithm on previous
days data set and then running them on next day with parameters calculated from previous 24 hours earlier. Other than my
optimized parameters from previous 24 hours, nothing is known to trading algorithm about the present data on which it is
calculating profit and loss. And I keep sliding my 24 hours parameter learning and validation windows so that nothing is
known in the validation window other than the parameters I calculated from previous 24 hours data. And my algorithms
make large profits something that really upsets mind control people who have been trying to retard me for past
twenty-three years.

They are also continuously breaking into my linux environment that I have saved on a removable hard disk.

I plan to trade with 50 dollars for a few days on Binance and I am sure that they want to stop me in my tracks when I am
using little money so that my family can object to my trading saying that it is not turning out to be profitable. And
then they would force me to start working with some traditional business to earn money and stop working with
mathematical finance. Since they have been waiting for past twenty-three years, my family is already very desperate.

I am very very sure if American friends never protested and stopped hardliners, they would do everything in their power
to fail me. I want to tell friends despite my forced persecution of past twenty-three years, I still have enough faith
in humanity. Please stop mind control agencies from interfering with my trading and let me live a life free of coercion.

---

### #1560 — Amin (Topic Author)
*October 6, 2022, 9:06 AM*

I am very afraid that after reading my yesterday's post many friends would think that it is all my fault since I did not
struggle enough to get me out of this and tried to leave my family.  I am writing this post to dispel that impression.

First important thing is that Pakistan army manages CIA's mind control in Pakistan. Pakistan army facilitates all mind
control in Pakistan in return for huge bribes that are paid to generals by CIA. I tried to escape my family several
times, but Pakistan army made sure that I was forcefully placed in control of my family every time. Most psychiatrists
also follow military's orders, and these psychiatrists also have their own uneducated personnel that are very willing to
use force to detain and control the mind control victims and police only helps the most influential people. I also tried
several human rights organizations in Pakistan and found out that they were very aware of mind control and drugging of
entire markets in the city but made no big deal about it and never were willing to help me. Yes, one psychiatrist tried
to help me somewhat, but my family made sure that I was detained whenever I insisted on seeing that psychiatrist.

Here I will describe a few times when I tried to escape my family and how it finally worked out.

One incident is from 2009, as I recall. I did not want to live with my family in Lahore, so I left the city and drove
to Karachi by car. Upon arrival in Karachi, my ATM card was disabled upon orders of army. I was stopped and repeatedly
harassed by police in Karachi. I was stopped in Clifton by a police car and they took me to Clifton police station on
23rd of February 2009. Police checked my car and said two front seat belts of your car carry different manufacturing
dates so "your car must be stolen, and we have to verify it" and reported me to their boss. I asked them to go ahead and
also requested that police had repeatedly asked me the same thing that my car must be stolen in past two days so once
you have verified, please write me a written statement so I can just show it to police everywhere once they would stop
me in future. The Police officer agreed to that and asked me to wait in the other room. I waited there for about half an
hour and the officer came again and violently slapped me several times. He said," You are over-educated, and you think
of yourself as something." I was surprised since I had not told him anything personal at all. I was seriously
humiliated, but I knew they would beat and lock me if I responded in force. I waited another hour sitting next to locker
room of the police station. After some time, Navy personnel came in three jeeps to the police station and asked me to
accompany them. I was taken to compound of PNS Nigran(Navy) in Karachi where they locked me in the Navy jail. The next
morning, I was taken to open compound, and I was circled by more than ten people who wanted to give me injections by
force. I seriously tried to resist but they continued to ask me to take injections. They were human enough to not beat
me for that. I asked again and again that they were not even telling me what the injection was, but they finally
forcefully injected me. And sent me back to Lahore with my brother-in-law. Upon my arrival in Lahore, I was detained for
six months by a psychiatrist.

Here I want to tell friends one interesting incident that happened when I was driving towards Karachi. I had entered
Sindh province and was normally driving my car listening to music. All of a sudden, I noticed that my right arm was
getting paralyzed. It was becoming very difficult to move my arm even very slightly. I knew at once that it had to do
with mind control, and I realized that I had to urgently do something. I somehow figured that something (gas) was going
into my nose. I had some raw cotton handy on the other seat (as I would force compressed cotton into my ears to decrease
the effect of mind control something that I used before 2010) and I put some cotton in my nose using my left hand, and
all of a sudden, my right arm was perfectly alright. Cotton probably altered the frequencies of waves going into the
nose and they were not effective after that. I am sure if I had not pulled this trick, they would have said later that
Amin was a psychiatric patient who escaped his home and ran away and was later found in poor condition helpless. And
then psychiatrists would have restricted my free movement.

Another time when I decided to live on my own away from my family was in year 2011 when I returned from London. When I
came back to Karachi from London, I wanted to rent a house in Karachi and live alone away from my family who was in
Lahore. Pakistan army continued to threaten people to not rent me a house. I continued to call my family everyday
despite what they had earlier done to me. My brother-in-law and his friends called me and posed as brokers interested in
arranging housing for me over the phone and asked me to come to a thinly populated area. I asked the taxi driver to
reach the place they mentioned. My brother-in-law started forcing me to go with him. I continued to ask him that we
could talk and settle everything nicely, but he was belligerent. They forced me off me feet on the road and tied both my
hands and legs. He wanted to blindfold me in the car by putting a cover on my head, but I forced my head against the
roof of the car (my hands and legs were tied) and he could not blindfold me. They took me to a house in DHA Karachi and
locked the main gate. Some people continued to come and go from the smaller gate. They gave me some injections and I
would fall asleep. I would doze for about half an hour to hour after every injection and when I would wake up, they
would give me some other injection. Basically, they were giving me some injection and would wait for about one hour to
see the effect of that injection and then would give me another injection after seeing effect of previous injection.
They gave me five or six different injections over the course of the day. In the afternoon they gave me some food to
eat. While I was eating, a woman I never knew and never had seen before, and all her breasts were exposed came and
started eating in the same plate I was eating. I continued to answer what she said but did not do anything at all. They
continued to give me more injections after I had taken food and, in the evening, they gave me a final injection and I
woke up at a psychiatrist's facility next day. Doctor did not interview me for several days and my heavy medication
started again. I was threatened to comply. One of the other patients told me that some people took me out of my room
unconscious at night and brought me back in the morning. I told Doctor I to make sure that nobody entered my room when I
were sleeping, and doctor agreed. I noticed that people continued to enter my room at night when I was sleeping. After a
lot of those incidents and protests, Doctor changed his line and said that we really have to enter your room at night
because of your safety. Doctor kept me detained in his facility for more than nine months and only in early 2012, I was
allowed to leave his facility. Earlier I had told the doctor that I did not want to live with my family and wanted to
live alone but doctor told me that he would free me only if I agreed to live with my family and otherwise detain me
indefinitely. I had to live with drug addicts and in a very unprofessional environment. He allowed me to leave after
nine months when I knew that there was no other way but to live with my family in Lahore.

I had received HSMP work visa for UK in 2010. In my fool's paradise, I thought that British are the most civilized
people on earth and once I would go to London all the mind control will end and I would live happily ever after. During
my three days in Pakistan prior to arrival in London, I had very little food thinking that I would eat better undrugged
food once I reach London. Though my first week was better, I started getting hit with drugged food right after my first
week in UK. At one stage after a month, all drinks and beverages manufactured by Britvic were drugged. There are five or
six large departmental store chains in UK who manufacture their own drinks and beverages and all of them were
manufacturing drugged beverages. It was extremely difficult to get a good drink in London.

When I was in London, I posted on a Chinese LinkedIn group about mutual cooperation. A contact in China wanted to start
a high performance computing firm targeting finance and he wanted me to work for him in China and did all the required
official work for me to get Chinese visa. The visa agency first asked me for extra documents, but my Chinese friends
arranged all the documents. When all documents were complete, Visa agency changed their line saying that I had to apply
for visa in Pakistan although I was a legal resident in UK with a work visa and their website mentioned that Pakistanis
on UK work visa could apply for Chinese visa from London.  I later went to Chinese embassy, but they told me that they
had relegated all visa matters to visa collection firm. I had to abandon the idea of going to China
since Chinese embassy was not willing to annoy British for a random Pakistani trying to get to China. Of course, some
influential people in UK wanted my persecution to continue and Chinese diplomatic staff had far more regard for their
British hosts and had no special sympathies with me.

Lot of times such machinations worked since some influential people in UK were telling blatant lies about me.

Later when in UK, I also applied for German visa which was promptly refused. And I figured the hard truth that it was
not worth applying to any Schengen country's visa after that.

In 2005, I was asked by my Japanese employer to come to Tokyo (2005) and work in their office there(I was earlier
working from Lahore). Japanese authorities drugged large number of places in Tokyo city and mad e my life absolute hell
and I resigned only after one month of stay in Tokyo. I did not want to return to Pakistan due to huge persecution by my
family and the army so I decided to go somewhere where US military could not go and got Iranian visit visa from Tokyo
and went to Tehran. Crooks in US defense gave huge amount of money to Iranian crooks(crooks everywhere know each other
well) and they used huge microwave and gases torture on me. I could never imagine that mind control could ever follow me
in Tehran but I had seen extremely unlikely things happen in my life earlier. For that reason, when I reached Tehran and
on my first night in Tehran, I again wore an aluminium shield in the hotel and then extreme torture stated. They had
already made all preparations for my arrival in Iran. They directed extreme microwaves on me and due to extreme pain, I
left the hotel somewhat after midnight and they continued to direct microwaves on me and there was extreme physical pain
and I ran on deserted streets to somehow be able to avoid mircrowave torture. I still recall that my hotel was in close
vicinity to major government buildings since I still have some memory that some of the buildings I noticed were
important places but I forgot the particular details.

And one very interesting incident happened in Iran. I was walking in the city and I came across a major building with
tank stationed outside. I thought I may be able to get some possible help and walked inside and asked for help. I was
taken to a guy inside the office and he said that he wanted another person who knows English well to write down
everything I have to say. Actually they were following me everywhere and that guy had already been told what to say
before I was taken to him by security at the gate. Then they took me to a meeting room with a large table and the two
people sat on the other side of the table from me. I started telling them about my persecution and the person who knew
English started writing and then tea came. They asked me to take tea. I just had a sip of tea that I started to lose my
mind but there were several sugar cubes and I realized that sugar must be good and I swallowed several sugar cubes and I
was slightly better. I told the Iranians there that I really needed to go to wash room. I walked out of the room and
went towards the wash room and in the gallery I noticed that one room had a door wide open and there was a refrigerator
there. I opened the refrigerator door and drank plenty of water and I was far better. When I went back to the meeting
room and started telling my story again, both guys were no longer interested in anything and told me that they could not
help me.

There was a large amount of drugged food in central Tehran and I surely believe that it must have been drugged at the
spot by a large number of people at stores and food places when I would get closer or arrive there. I was hit by drugged
food again and again.

One of the hotels Azadi Hotel which was located in outskirts of Tehran was a bit better and I started living there but
they asked me to leave saying that they had an upcoming conference and they could no longer let me live there. I recall
that some Iranian agents came to hotel and told me they had come from Iranian president but it was obvious that they
were Iranian intelligence and they wanted me to work for Iran. I knew the meanings of getting associated with Iranian
intelligence would spoil my life forever and I just told them that I wanted to live and work in Iran as an ordinary
citizen.

Just after two or three days in Tehran, I was trying to find refuge in embassies like Vatican in Tehran asking them to
help me on human grounds. I left Tehran after one week and flew back to Pakistan. I still recall that I arrived
at Tehran airport a lot earlier than flight departure. I had previously protested somewhere against unnecessary removal
of shoes of Muslim passengers and it was known to mind control agencies. They asked Iranians security on airport who
approached me inside the departure lounge and took me to a room and asked me to remove my shoes and had my body search.

Those eight days I lived in Tehran were literally some of the most difficult days in my life and I really decided to
leave quickly after a week.

Since during all this, mind control agencies could not control me well and several of my neurotransmitters were coming
back, they had extremely huge amount of gases in washrooms in Dubai airport where I would stop for transit while going
to Karachi. No wonder ultra conservative crooks in US army align so well with Saudi (who dissolve their criticizers in
acid) and Dubai.

I had earlier faced mind control in Singapore and Hong Kong towards the end of year 2000.

---

### #1561 — Amin (Topic Author)
*October 6, 2022, 9:54 AM*

Please read my last long post on previous page: https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1545#p872331

I want to request friends that mind control agencies have a full-blown plan to alter my trading and if friends did not
ask them to stop, they want to fail me at all cost, as they have done so well in the past. The only difference is that
in the past they had painted me as some bad Muslim with all their lies and machinations. I openly tell people that I do
not believe in any religion even though I want to serve my country Pakistan. I do believe that good people have to care
about other good fellows and try to promote goodness in their society. I am very sure that some good people who helped
protect me in the past will also try to help me now. If it were not for these good people, I would have lost all faith
in goodness of humanity. You can see it in some of my posts written around 2014 when I started to mock all Americans
only to seriously temper down when I realized that some Americans had tried to help me when my mind control decreased
remarkedly at times. And I was always concerned to not write anything that would hurt people who have taken my side.

And even though I have blamed some jews about my mind control, I am very aware of the fact that most of them probably do
not want to hurt me in any way.  I want to tell them that I am a very benign and harmless person who wishes them every
good. But with just one request to at least be fair with Muslims.

Here is an excerpt from webpage below about what I think of American Jews.
>  Most jews are very good humans and they have earned their place in American society over a period of long time by
contributing to almost every facet and dimension of American society. And they are thorough Americans. Some prominent
jews are true role models for what a good human should be. And again most jews are thorough gentlemen and very good
humans.
Please read here: [Muslims, mind control, Muslim-Jewish relationship and American defense](https://forum.wilmott.com/viewtopic.php?f=15&t=101453)

Also please read my application to human rights watch here: [My Letter To HRW About My Human Rights Abuse](https://forum.wilmott.com/viewtopic.php?f=15&t=102298)

---

### #1562 — Amin (Topic Author)
*October 6, 2022, 3:42 PM*

Friends, when I turned on linux drive this evening to start my programming work, I noticed that there were several
changes in the way unix system turns on. So, I am pretty sure that these people who were backing my persecution are not
ready to let go.

I have therefore decided that instead of trading on my own, I would try to find clients and then give them a small and
lightweight (not necessarily) encrypted function based on just two or three lines of code that would predict the future
price given the market variables. The parameters of the function would be based on previous working day's data and will
be sent to clients on a daily basis by me. Friends who would buy the service from me would be able to profitably trade
on an approximately 15 seconds grid. My programs are already with jewish professors who are backing my persecution so it
would very unfair if other people would not be able to benefit from my programs.

---

### #1563 — Amin (Topic Author)
*October 7, 2022, 6:53 AM*

>
> Here is what I wrote on Wilmott on Thu Apr 21, 2011, 11:00 PM. I have brought it back from my own records.
>
>
>
> In my previous post I talked about the ideology of intolerance the word Taliban represents. Here I would like to make
a detailed comparison between the two groups of Taliban I mentioned in my previous post , one group of which is the
Taliban of Afghanistan and the other group is the racist Taliban of Pentagon. The original Taliban, as the world knows,
are characterized by their ignorance, lack of education, indoctrination of hardline versions of religion and of course
the two Taliban characteristics which are lack of tolerance and employing violent means to achieve their intolerant
version of the world. On the other hand Taliban of Pentagon are reasonably educated, very mediocre, embrace racism, have
a lot of resources available and share the taliban characteristics of lack of tolerance and employing sometimes violent
and usually cunning means to achieve their racist and intolerant version of the world. However what makes the Taliban of
Pentagon worse is that Taliban characteristics of Original Taliban can be blamed on lack of education and backwardness
of their society. On the other hand, racism and intolerance of the Taliban of Pentagon cannot be blamed on lack of
education and backwardness of their society and it is a characteristics actively chosen by a group that should be
decently aware of ideologies of human goodness as represented by the population from which it is chosen. This active
adoption of Taliban characteristics as opposed to passive Talibamism of Afghani Talibs makes Taliban of Pentagon more
hideous and abominable creatures. Afghani Taliban ruthlessly kill christian missionries while their racist counterparts,
the Taliban of Pentagon are more cunning and have sharpshooters who retard innocent and peace living Muslims of other
countries with the aim to inflict damage on their nations. Advanced technologies and abundance of money allows them to
hide their racist crimes and call themselves "responsible army". The Taliban of Afghanistan show indiscriminate hatred
and their acts result in just a few deaths but they earn stigma for their religion while the acts of Taliban of Pentagon
are more strategic because they result in making the children of our nations darker forever while earning no stigma for
their nations. The acts of Taliban of Pentagon are more hideous for our nations and act of Taliban of Afghanistan really
do not matter for anyone bust just a few individuals which of course, cannot be pardoned either but Talibanism of
Pentagon is more hideous than the Talibanism of Afghanistan, though underlying characteristics of Talibanism are the
same. The Taliban of Afghanistan are stupid while the racist Taliban of Pentagon are cunning, The Taliban of Afghanistan
kill ruthlessly while the Taliban of Pentagon retard someone and assign a group of mean mind control satans who continue
to insult and humiliate them all their life. I appeal to Taliban of Pentagon to learn from their Afghani counterparts
and kill instead of giving a life of humiliation since it is more graceful to die than have a life of humiliation
>
> I would request Americans, who are in fact good and responsible, to eradicate racism from their society and from
Pentagon and make sure nobody innocent of any religion is retarded especially if they want to serve their nations and
have nothing against America. I would like to point out a fact from history that America was slower than rest of the
world to abolish several aspects of racism an example of that is the fact that slavery continued in America longer than
could be imagined especially given the advancement and prosperity of its society. Today,The case of racism of Satans of
Pentagon is very similar and should be addressed by responsible Americans.
>
.

.

Here is the first part of two posts about Taliban mentality second of which was copied by me earlier. This is the first
part. This was written on  Thu Apr 21, 2011 12:33 AM

..

I have been actively speaking against Satans of Pentagon on this forum. Some people like traderjoe have been calling me
jihadi or taliban despite the fact I never have any sympathy to their ideology. Taliban represent lack of tolerance and
employing violent means to change the world in a way they want to see the world. In fact very similar representation
fits the Racist Satans of Pentagon and it would be right to call them Taliban of America. I say that if you wear a great
designer suit but follow the similar ideologies that Taliban follow but, of course, related to and oriented in a
different country, I would have no hesitation to call you taliban. Taliban is a mentality and not a specific religion or
people wearing any specific dress. The lack of tolerance of racist satans of Pentagon is made evident by their audacity
to retard innocent people of other religions or countries they do not like. Taliban employ violent means but these
Satans use cunning means to change the world and try to shape it into their narrow ideals of the world. This is made
possible by unimaginably large loads of money made available to these mechavellian racist satan taliban of Pentagon. In
fact, both of these are enemies of my religion. My religion never teaches me to use violent ways to promote any kind of
ideals so Muslim Talibans damge Islam by promoting the image of their own religion as ignorant, intolerant and bigoted
warring people. Racist Taliban of America damage our religion by retarding those people who want to contribute to their
nations and want to turn their nations into tolerant, modern and democratic societies. This way our nations will always
remain uneducated, poor and intolerant, violent and bigoted taliban of our nation will continue to provide the Taliban
of America an excuse to tell their nations of the threats of terrorism and fundamentalism so they can maintain their
grandiose existence and continue to ask their government for a bounty of a trillion dollars a year so that mean and
mediocre Taliban of America divide between themselves. In fact, the passion for war these Racist Satan Taliban of
Pentagon, as made evident in Iraq, where half a million people were killed, makes me compare them to warring clerics of
Hezbollah. Just because you wear nice suits or have the world media under your control does not mean that the truth is
what you want to show the world and start declaring and calling other people terrorists at will while you are yourself
the greatest terror in the world. The nature of people of any religion or culture usually is good and I simply call it
human goodness but some groups in these nations continue to self propagate their satanic ideologies by inducting similar
minded people and Taliban of Afghanistan and Racist Taliban of America are some of these groups.

---

### #1564 — Amin (Topic Author)
*October 7, 2022, 7:43 AM*

As many friends would have noticed that I repeatedly called myself Muslim in my old posts that were written in 2011 or
even somewhat later. At that time, I mildly believed in religion.

I have no friends. I rarely watch movies. I do not play computer games. In my spare time, I used to read history. And
then I started reading about the universe, the solar system, the earlier times on earth and also about the evolution.
When somebody reads a lot about these things, there comes a stage when one starts to know in their subconscious that
there is no truth to religion. It was somewhere around 2015 when I really started to say that I had no religion.

When I would call myself a non-believer in religion, mind control agents would lose one more argument they had to
continue my persecution and I really believe they tried to roll me back into days of belief in religion (which is
impossible) for example by trying hard to make me emotional when I would be reading Muslim history and stuff like that.

Even though I do not believe in religion, I love my country, Pakistan.

Also, I used to write better and more coherent English. Several times when they detained me, they very carefully took
neurotransmitters out of my brain that I used to write good English and my English became extremely poor when I would
leave detention. In brief episodes when I remained away from antipsychotics for more than three months, my English would
become markedly better.

---

### #1565 — Amin (Topic Author)
*October 8, 2022, 1:11 AM*

I want to tell Americans that Mind Control by American Army is not my problem, it is first and foremost a problem that
American society needs to address. American army has been retarding innocent civilians for several decades without
impunity. After mind control victims have been retarded and their best neurotransmitters identified and disabled by
American Army, the victims are rarely able to pursue their case. The victims are mostly unable to speak properly let
alone write in good English. Once the victim has failed to pose any defense, all sort of fabricated lies are spread by
American army and other people who are behind victim's persecution, and therefore, good people in the society have
started to consider mind control another normal thing. If all the victims of mind control were able to make a vigorous
defense, Mind control would never have been able to take root in American or any other society.

Though American army has become emboldened and there are more and more white victims of mind control now, traditionally
and historically most victims of mind control used to be Blacks and Muslims. Let us for a second assume falsely that all
Muslims on mind control are potential terrorists but why are several thousands (or possibly tens of thousands) of blacks
being retarded by American army. These Blacks, most of whom would be above average intelligent before mind control, are
real Americans and have their allegiance with United States. Even if they were to become criminals, a functional legal
system exists to punish these intelligent blacks when they would commit any crimes. The real problem is that a high
percentage of the staff in American army comes from 'religious conservative'/neo conservative background and these are
the very same groups where there is larger a tendency to simmer with hatred for Blacks and Muslims below surface. Pardon
me for being politically incorrect but I like to think about these things on my own once in a while, and I have not been
able to find out any reason behind widespread victimization of blacks other than racism and hatred among American army
conservatives and other groups who are behind mind control. And case for victimization of Muslims is very similar. A
large number of Muslims being victimized are the ones that were born inside US and owed their allegiance to US but still
in the eyes of American army neo-cons, they were Muslims and were retarded when they tried to excel.

Again, after decades of retarding innocent people without impunity, at this stage American Army boldly retards more and
more white people upon orders of some other groups who move the strings of American army and reward them when they
follow their wishes.

Again, the problem has continued to increase to dramatic proportions only because victims are effectively silenced by
taking neurotransmitters out of their brain something that continues to protect the perpetrators of American Army. In
fact, the technology today is so advanced that victims are not merely silenced, they are aroused on mean
neurotransmitters to say inappropriate things about others so as to cause hatred for the victims in the broader society
and create a false sense of justification to retard them among public.

Again, this is not my problem, this is our problem and American Society should take concrete steps to bridle American
Army's unethical and mostly racist practices.

---

### #1566 — Amin (Topic Author)
*October 9, 2022, 4:15 AM*

I want to ask Americans a question.

What is the mandate of United States Army?

Is it to protect the conservative purity of United States?

Or is it to protect the life and property of US citizens irrespective of race and religion from external and internal
threats including terrorism?

Or is it a divided mandate with some people working on mandate one and some other working on mandate two?

It seems that both mandates are conflicting with minorities and people of color targeted by US army officers who follow
mandate one.

If there is any ambiguity, it has to be clarified to people in US army which mandate to follow.

---

### #1567 — Amin (Topic Author)
*October 9, 2022, 6:23 AM*

I am writing this post to keep friends updated on my progress with market trading and my future plans. I had an
antipsychotic injection about a week ago and I could not work well after that. I hope to complete my programming in next
two to three days. I have ported my matlab optimization programs into python. I have also written python programs to
import live klines data and save them in numpy arrays and make trade decisions. But I still have to improve my programs
to alter the bid/ask level of limit orders with changing prices after every 10 seconds. I also need functionality that
tracks all my order creation/cancellation/filling activity and saves it to disk when program closes. I expect that all
of this will take another two to three days. I will spend another week to ten days analyzing the performance of my
programs and would try to improve them especially the part about how limit orders are offered. All of this can take up
to two weeks.

After two weeks, I will come back to stochastics research and take the threads where I left them. When I left, I was
trying to fit a Z-series to volatility surface at multiple horizons and trying to analytically determine the evolution
of asset between two different horizons/option expiry dates. I cannot wait enough to restart my research on stochastics
again where I left it. Of course, I will again be posting all my programs on this thread, as usual.

After completion of above stochastics project, I want to work with the intersection of AI and stochastics. I hope that
my market trading programs would make enough profits in a few months to let me be able to rent a small office and hire
2-3 fresh PhD/Masters graduates and work with them as a very small company.

---

### #1568 — Amin (Topic Author)
*October 9, 2022, 2:58 PM*

Friends, mind control agencies are drugging underground deposits of water with mind control drugs again. This morning, I
filled some water from a water cooler in Faisal Town and the water was drugged. When I would drink water, something
would stick to upper jaw above the tongue and my veins leading to brain would start pumping. I did not make a big deal
and thought they might have mapped my path and drugged water of the cooler on the road before I reached there. I had
water from before and I simply used that during the day.

This evening when I went out, I drove my motorbike in totally opposite direction of this morning and I was surprised
when I filled a water bottle from another random water cooler, and it had exactly the same feeling as this morning. And
then I tried some other places with exactly the same problem. These were all random places in public supply of water
from totally different sources in a radius of 6-7 kilometers.

I want to tell friends that mind control agents have started drugging the underground water deposits in Lahore again.
And I am very sure that their next step is to detain me at some psychiatric facility for several weeks so I could be
silences again. This is the same method to stifle my sound that they have so successfully used so many times in the
past. Please raise your voice against brutalities and inhuman practices of American mind control agencies.

---

### #1569 — Amin (Topic Author)
*October 16, 2022, 4:59 PM*

Friends, sorry for staying away for so long. Despite usual difficulties in getting good water and food, I have been
working on my programs. I have almost completed coding for the algorithmic trading and continued to test my programs on
Binance testnet today. I have identified several errors and would be fixing them tomorrow. I still have to do
bookkeeping back-office work for my program. I hope to remain busy for next 4-5 days.

It is hard for me to wait to retake the strands of my research where I left them three/four weeks ago. Though it is nice
to see some cool working system evolve out of coding, I think mathematical research is more stimulating and possibly
more demanding as well. In 7-10 days, I will be restarting my research on mathematics.

I want to request friends to force mind control agencies to end my persecution. While I work on mathematical research,
they continue to take some neurotransmitters out of my brain and then things become very difficult after 2-3 weeks. That
was one reason that I got tired out of some of almost complete projects before finessing everything and left them
thinking that other people would make some minor effort to complete them on their own. When I restart work on a new
topic, the brain resets again and I start working with some different neurotransmitters and it is easier to work with
enthusiasm again. If mind control agents would not be simultaneously taking neurotransmitters out of the brain, I would
truly enjoy making effort on my research and would not lose energy. Antipsychotic injection also plays a similar role.

I really hope my algorithms make good money and I have really cool plans of working with the intersection of probability
theory, stochastics, and machine learning. And I hope to keep posting most of the stuff here on my stochastics thread.

Though my persecution continues and mind control agencies keep drugging food and water actively, I will seriously want
to thank friends who wished me well in difficult times and tried to do something to decrease my suffering. If it were
not for friends protesting against my persecution, I would again possibly have been in some psychiatric detention as has
been the case several times in the past.

---

### #1570 — Amin (Topic Author)
*October 21, 2022, 1:51 AM*

Friends, I am writing this post to protest the use of mind control chemicals and gases. More than five or six months
have passed since I started to tell friends that they use some chemicals when victim is sleeping, and the mind control
chemicals settle on the tongue and upper jaw and when the victim wakes up during sleep, it tastes very bad inside the
mouth. For several months, I would continue to request friends to protest to mind control agencies to end this practice,
but nothing ever helped. With most of the other things when people protest, I would usually see some positive relief but
there was never no relief in this regard. And I finally gave up writing about it on internet since my writing about it
was of absolutely no use.

Our sleep is very special and during sleep our brain reconnects in many ways to rejuvenate the body and release special
neurotransmitters that are otherwise not released when we are awake. A large number of these developments that take
place during sleep cause problems for mind control where the intention is not let the victim's brain reconnect in
special ways. The science of the ways brain connects-reconnects during sleep is still not perfectly understood and
therefore brain also connects unexpectedly during our sleep.

Also, our tongue is very special and is connected to most parts of the brain that get stimulated when we eat food. Now I
want to explain why mind control agents cause chemicals to settle on victim's tongue? Basically, mind control agents
want special neurotransmitters to remain connected where they wish to connect them and not where our brain would want to
connect them on its own. Once mind control agents get our neurotransmitters arranged in a desired situation, they want
those neurotransmitters to remain strongly binded to places in brain that mind control agents desire by using strong
charges that do not let special neurotransmitters break away from those parts of the brain. Because mind control agents
know once this binding is broken, potent neurotransmitters would reconnect in unexpected ways causing problems for mind
control agents. And special chemicals on tongue let achieve this target to not let potent neurotransmitters bind to
other neurotransmitters in unexpected ways making the work for mind control agents very easy.

For past few days, I have been washing my mouth with water several times when I wake up during my sleep. And that lets
some neurotransmitters break free and reconnect on their own for small periods of time before the charges are applied
again by mind control agents. Mind control agents now release gases in my room when I wash my tongue so that
neurotransmitters cannot reconnect in the meantime.

I want to request the friends to please protest against such inhuman uses of science and technology to control good
people. Please protest against such degrading methods to control some human beings.

People speak about wrath of god, to be honest, in this world wrath of Jew is far worse than the wrath of god. Since God
most probably does not exist but machinations of Jews against innocent people is a hard-reality I have continue to face
this wrath for past 25 years. Now I bitterly beg the Jews behind my persecution to please let me live with human dignity
if you are capable of accepting me as a human.

---

### #1571 — Amin (Topic Author)
*October 21, 2022, 3:23 AM*

Friends, I was 24 years old when, in 1997, my persecution with mind control started. I am 49 years old now. I have
completed 25 years under mind control.

I am writing this post to all the good Jews who are infuriated by some of my posts. Instead of being upset with me, I
would want to request them to reprimand their kin who are behind my persecution, persecution of most muslims, blacks,
and recently more boldly behind the persecution of a large number of white Americans. It is a group of rich jews whose
Godfather/Goldfather is a jewish billionaire who instructs US military who to retard and in return US military officers
are hired at lucrative jobs paying millions of dollars by the companies of rich jews after they have retired from US
army.

In United States children are taught since childhood to not speak against any jews. I feel this has boldened many jews
to commit crimes against humanity with impunity. I have myself been called antisemite several times by US citizens on
several forums when I complained that a Jewish professor instigated my persecution despite the fact that I have seen
repeated trauma and torture in order to forcefully retard me. I was completely innocent in every meaning/aspect of the
word. If speaking against crimes of some rich jews is being anti-semite to you, please yourself by calling me
antisemite.

I have been writing on various forums against my persecution for past twenty years, but I have been unable to appeal to
nobody's humanity in US government(who are never tired of praising their own lofty human rights standards invoked by
habitually bashing Chinese day and night). Is America officially a jewish country that protects right and wrong whims of
Jews, despite the loud protests of a large number of their other non-jewish(and some jewish) citizens.

---

### #1572 — Amin (Topic Author)
*October 21, 2022, 3:50 AM*

Remember, all the rich jews who had committed all sorts of crimes and machinations against Germans had escaped Nazi
Germany with all their gold and the poor jews who would never wrong any human in their wildest imagination were the ones
who were killed in gas chambers.

God has given Jews a lot of respect in US and all over the world which they rightfully deserve. Please cherish this
respect and do not destroy it by instigating mind control of other people. If you are a good jew, please stop the evil
ones from using mind control on other people.

---

### #1573 — Amin (Topic Author)
*October 21, 2022, 10:53 AM*

Friends, I wrote my earlier three posts in the morning. When I started working around noon, I realized that behavior of
my python programs had totally altered. My algorithmic trading programs send a stream of orders to Binance testnet with
a gap of ten seconds between subsequent orders. Some orders get filled on spot but life of an unfilled order is only ten
seconds. Every ten seconds an unfilled order is cancelled and a new order re-adjusted to market conditions is posted to
testnet. For friends, I will like to clarify that testnet is mock trading but programming for testnet and mainnet is
perfectly the same. Developers continue to send their orders to testnet (before sending them to mainnet after verifying
their programs) and it has reasonable liquidity of mock orders that are filled against each other.

I tested my program on testnet for past two days and it was working very well. Everything seemed to fit perfectly well.
I had written messages in python script that were getting updated everytime some order was cancelled, and a new order
was created and key statistics were shown on screen.

I wanted to try my program on Binance mainnet today. But when I tried it first on testnet, its behavior had totally
altered, and it was not going into several loops of order cancellations and resending orders. I do not know how it could
be possible, but it did not work.

Looks like scumbags of American army and mind control agencies are changing my programs.

Here I would like to tell friends about my algorithms. I tested my programs on binance daily minute-based data. I would
take 24 hours of data and optimize parameters on it and then simply use the parameters in next 24 hours program in a
prediction setting. I tested my optimization algorithm on four months of data with similar sliding window where
parameters optimized from previous 24 hours were used for prediction in next 24 hours. I earned zero bid ask spread on
top of price. My program would make an average of 1000 trades out of 1440 minutes in 24 hours. When I started, for
example on ETH-BUSD trading, I was making 3,000 USD with low sharpe by trading one ETH for four months. The price of ETH
changed in a window of \$2700 to \$ 900 as maximum and minimum numbers with average around \$1800. Then I improved my
programs and optimization methods, and I was making 6,500 USD in four months on the same data with reasonable Sharpe.

I remember that mind control agencies seemed willing to let me do trading on Binance but when I wrote the above program,
they decided that I cannot be allowed to make such possible profits. They knew that I would later start using these
programs on other markets and such scenario could not be allowed for a Muslim in the eyes of a lot of Jews and neo-cons.
And that is when they started machinating with my family and I started to make noise on this forum.

Later I further improved my programs and added other explanatory variables and my programs started making 9000 USD on
trading one ETH for four months (one ETH remains has an average value of \$1700 during this time). And that is when mind
control agencies started to drug water and decided to deal the matter with an iron fist that a Muslim (even though I do
not believe in religion, I am a muslim to many jews and neo-cons) cannot be allowed to make such profits in financial
markets.

Here, I want to tell friends that, on average, I am making roughly half a cent on hundred dollars per trade but since
number of trades is so large that the money accumulates. I could not make this money if due to a promotion, commission
on spot trading in binance were not zero.

Now mind control agencies are taking liberties with my programs and already altering them. Though I can program well, I
do not know intricacies of computer science and my strength is only mathematics.

I want to ask Americans if they could even possibly imagine a scenario in which a Jew was being stopped by mind control
agencies like this but this is very usual for racist mind control agencies to stop Msulims, blacks and many other people
when they try to excel in this world.

---

### #1574 — Amin (Topic Author)
*October 21, 2022, 4:48 PM*

Friends, it is 9:43 pm here in Lahore. Mind control agencies continue to release gas after brief intervals in my room.
It seems that mind control agencies have decided to go on bigger offensive against me. Tomorrow I will write about how I
would pass my night and how they would cause mind control chemicals to settle on my tongue. Currently they are resorting
to use of gas off and on after a bit.

---

### #1575 — Amin (Topic Author)
*October 23, 2022, 7:34 AM*

Friends, a lot of things happened over past two days and I decided to tell friends about them here.

I made a lukewarm effort two days ago to fix my python program. It seemed perfectly right.

I noticed that when I write the following command after sending the limit order in my code

print(Order['status'])

Screen shows      FILLED

when order is filled instantaneously on testnet.

But when the program reaches the following if command

if Order['status']=='FILLED':

my program never enters the loop despite printing FILLED on screen earlier right before if comparison of strings. There
is something wrong with these string comparisons. They were working perfectly and wonderfully one day before Friday
morning when my programs stopped working.

Mind control scumbags used to alter my matlab programs routinely before 2016. I really do not know how it works but they
probably somehow replace my code file with their own hidden code file and when I would give a command to run a
particular file and they would know the name and location of that file in advance, they would somehow make sure that
their hidden file runs instead of running my code.

Before 2016, I would regularly protest on this forum about the fact that they altered working of my code. But some
people strongly objected to such antics and then mind control agents stopped altering my code after 2016 but there have
been a few times (two or three) when they still altered my code and I got to know about it and protested on this forum.

Yesterday, when I was very heartbroken, I called my younger cousin who is a professor at a Chinese university in
Shanghai and we spoke for 25 minutes. He is a very intelligent, nice and intellectually inclined guy. We had not spoken
directly for past few years other than a few email messages. He knew about my persecution from earlier times and I
briefed him about my latest research and market trading programs and told him about all the difficulties I am facing due
to my family and mind control agencies. I asked him to help me start my market trading company in China. He was very
encouraging and told me that he would help me in every way. I am not going to rush but I really think, if I remain
persistent, I can possibly move to China and start my algorithmic trading company there in 6-9 months.

In past I had thought of moving to China but my research activity was going well and I thought that people would have
enough regard for me due to my research and they would stop mind control agencies from their inhuman persecution. But I
was totally wrong. They way mind control scumbags have been acting in past week, they are more boldened now than they
have been in past 5-6 years to stop me. I think it is in my best interests to move to China and start doing trading
there with some Chinese friends. Future really belongs to China, and I would be very well-placed to take advantage as
Chinese economy advances and their influence increases.

I knew that it would be difficult to work on my python programming now and I was strongly feeling the need to improve
the analytics of my algorithmic trading programs. I continued to work very late last night and was able to make
significant advances in my programs. I had earlier told friends that on trading one ETH for four months, without any
bid-ask spread included, my programs showed a profit of 9,000 dollars. But last night I changed a lot of analytics and I
was able to improve the profits to more than 13,500 dollars by using the improved algorithms. But I had to make a lot of
efforts. When I first changed my programs, the profits initially decreased, and I was feeling hopeless but then I
noticed that some things were working better and improved on them and that remarkably improved the algorithms finally.
This is very remarkable and is roughly around 200% profit in a single month using very fast trading strategies. Though
ETH and BTC have a trading volume of more than a million dollars per minute, it would still be difficult to scale the
profits to larger capital. But substantial amount of capital can be traded by judiciously spreading it in several
markets and one can make good profits. If we can add small bid-ask spreads, they can really boost the profits further
and make such trading strategies very attractive.

I am also slightly upset that those professors who were behind my persecution have my programs. Now they want to take
full advantage of the programs and simultaneously make sure that I could not use them. It is interesting to know that
people who showed me hatred and venom all my life are being sole beneficiaries of my algorithmic trading programs.

---

### #1576 — Amin (Topic Author)
*October 24, 2022, 8:19 AM*

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

### #1577 — Amin (Topic Author)
*October 24, 2022, 8:46 AM*

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

As it has gone to previous page, please do read my last post from yesterday here: [Breakthrough in the theory of stochastic differential equations and their simulation - Page 105 - wilmott.com](https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1560#p872703)

---

### #1578 — Amin (Topic Author)
*October 24, 2022, 10:11 AM*

[ My Letter To HRW About My Human Rights Abuse](https://forum.wilmott.com/viewtopic.php?f=15&t=102298)

Above is a very incomplete account of how various psychiatrists continued to play in hands of Pakistan army to retard
me. It also does not cover all the time till year 2022 and the account stops several years earlier.

Pakistan Army has no personal animosity with me. Chief of Pakistan Army staff is given more than 50 billion rupees every
year come rain or shine so that army continues American Mind control of intelligent people in Pakistan. Even when the
relations between both countries are extremely bad, this bribe is always given to Pakistan army generals in time.

---

### #1579 — Amin (Topic Author)
*October 24, 2022, 11:11 AM*

When my persecution officially started in 1998, the racist premise of Jews and Neo-cons was that we could never allow a
Muslim to have so many special neurotransmitters. Something that breaks my heart is how many people approached me with
hatred when they knew I had several special neurotransmitters. They simply wanted to take them out of my brain. When I
was in US, I was simply a young innocent boy who was very moldable. I was also looking for a PhD and they could have
easily diverted me into academia if they wished so but most of them were not simply ready to tolerate me with my special
neurotransmitters in my brain.

I had to see a lifelong of misery, trauma and torture when army neocons continued to make sure 25 years into the future
that special neurotransmitters must be taken out of my brain.

I am ready to shrug all of this and re-start my life but hatred and venom of some jews( with a due pardon to good jews)
is adamant that I must not be allowed off mind control until my special neurotransmitters have been taken out of my
brain forever.

---

### #1580 — Amin (Topic Author)
*October 24, 2022, 2:44 PM*

About ten years ago, I started writing a blog on wordpress and Pakistan was central theme of the blog. Mind control
agents continued to take neurotransmitters out of my brain and my English writing continued to deteriorate.

If you like to know more about me, you can read here: https://ahsanamin2999.wordpress.com

Here is one of my blogs, I really like. It was written on OCTOBER 23, 2013 · 12:59 PM

[Prosperity of Pakistan, Pakistan-India Relations, and Pakistan Army](https://ahsanamin2999.wordpress.com/2013/10/23/prosperity-of-pakistan-pakistan-india-relations-and-pakistan-army/)

The success and greatness of a nation is not measured by the strength of its army, its atomic arsenal or weaponry. It is
measured by the prosperity of its people, the rule of law, tolerance and civility among the individuals of the society
and the scholarship and strong work ethics of the people of the nation. These are characteristics of a good society in
which every nation should take pride in. Immature nations and people take pride in weaponry and atomic arsenal of their
nations, hatred for other nations/people/religions and righteously believe that hurting or damaging other nations
somehow contributes to greatness of their own nations. Nations have to achieve greatness by working hard, imparting
right skills and education to its individuals, choosing the right trades and industries in which to excel, giving a good
legal code to its society, and providing social justice to individuals of its society. When some nation thinks that
their success lies in damaging interests of other nations, it means that something has seriously gone wrong with the
collective decision making and vision of that nation.

We, as Pakistanis, have to ask ourselves whether we can take pride in the above qualities of a great nation. We are one
of the poorest country in the world. We do not spend much on education as compared to other nations of the world despite
having very low literacy rates, and advanced sciences and technology are rarely known to the individuals of our society.
However, we do take great pride in supporting one of the largest army in the world and a huge percentage of our GDP goes
to serving the interests of this army. We are a nation with very limited resources and we have to make wise and
thoughtful decisions about how to allocate our meager resources to different categories of state expenditure. When we do
not spend much on education and continue to spend huge amount of money on our army it means that something has seriously
gone wrong with the decision making process in our society. We have to see the writing on the wall that no state can
continue to spend huge sums on defence without expanding the economy which in turn is not possible without giving right
skills and education to its people, an area where we are seriously faltering as a nation. Since we have made the same
choice for decades, our state is close to bankruptcy and our finances have to be propped by loans from foreign nations
and banks who fear that a complete breakdown of our state will create anarchy and promote terrorism.

It is up to the people of the nation, its universities and the intelligentsia to sense what has gone wrong with their
nation and propose a recipe to cure the problem. I have tried to give qualities of nations that tread the path of
success and excellence. We have to take the right and dramatic decisions now to take our nation away from the road to
failure and destruction towards the path of success.

One thing we have to understand that prosperity for our nation will result only when we have total peace with our
neighbors and we are sincere in creating an atmosphere of peace in the region. India is a much larger country with a
huge economy that is growing at a faster pace than our country’s economy. It will be impossible for Pakistan to stand
against India for long without growing our economy which does not seem possible given the current state of affairs. It
will be really wiser to seek total, true and real peace with India and divert our resources towards good education of
our children, fostering an atmosphere where investment in right industries is hugely encouraged, imparting social
justice to people in the society, and creating a true sense of security among the individuals when it comes to their
life and property by curbing all crime.

Let me ask people of my nation this question. Do our ethics as a nation or our religion allow the kind of massacre that
Pakistani religious fanatics did in Bombay in 2008.  As far as I know my religion, killing innocent people of any other
nation or religion is a great crime and when it is done in the name of my religion, it shows the extreme immaturity and
childishness of the people doing that in the name of religion. I have studied the life of our prophet and I know how he
showed extreme kindness towards other people all his life. I, as a common Pakistani, cannot be sure but a lot of
evidence points that ISI encouraged training these people and the people responsible for these crimes walk free in
Pakistan. We have to assume our responsibilities as a civilized nation. I strongly suggest that we really have as fair
trial into this issue as possible and if any individual is found responsible for this, they must be punished according
to laws of our country. And if any official institution is found responsible for this, let us try to rectify ethics of
that institution. I, as a proud follower of Prophet Muhammad(PBUH), cannot see my country as a sanctuary for people who
commit murder of innocent people of other nations or religions and walk free in my country with impunity.

One of the purposes behind mentioning the Bobmay massacre was that some institutions in our country have vested interest
in never having peace with India. We have to look towards prosperity of our nation as a whole and if some vested
interests come in the way, let us defeat those vested interests and take the right decisions with a collective wisdom
that ensures that our nation is on the right track towards progress and prosperity.

So let us allocate the right amount of our GDP on educating the poor children of our nation, invest heavily on higher
education and the research in the universities, promote the right industries by giving them generous incentives and
maintain an atmosphere of law, security and order when it comes to life and property of the individuals but this could
only be possible if we can divert resources from supporting one of the largest armies in the world and try to find peace
with India.

I have written about ills of our society but I think some of the similar problems exist in Indian society as well. Just
like the religious fanatics in my country, there are Hindu fundamentalists in India who are against the idea of any kind
of peace with Pakistan. The only fear that stops me from suggesting a steep reduction in the Pakistan army is that some
Indian government may yield to the idea of gaining cheap popularity among a lot of Indian hardliners by choosing the
path of military adventurism. How remote that scenario is, I cannot say. But if the people of two countries try to take
truly sincere and concrete steps to promote peace, I am confident that we can help alleviate poverty among one of the
most heavily populated countries in the world. The future of the two countries when measured in terms of the prosperity
of their people will be far more secure, if we learn to live with total peace as good neighbors.

---

### #1581 — Amin (Topic Author)
*October 24, 2022, 5:00 PM*

I was reading my old blogs and noticed a paragraph. Though I had written this paragraph about Pakistan Army, it applies
equally well to American Army.

"I consider most armies as syndicates who thrive on creation of hatred and show their success by quashing the hatred
they created. Similarly our army starts to take action against separatists by kidnapping and killing them where those
problems can be resolved amicably by political settlement between appropriate civilian bodies. This creates bad blood
between different ethnicities and provinces and usually punjab is held responsible for vagaries of Army’s top brass. We
have seen this happen before in Bengladesh where our army massacred about three hundred thousand people. This is a fact
we are not taught in history books but this is one of the reasons an old part of our country celebrates the day of
secession from Pakistan as their independence days. We really do not want history to repeat itself in Balochistan."

---

### #1582 — Amin (Topic Author)
*October 25, 2022, 10:35 AM*

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

---

### #1583 — Amin (Topic Author)
*October 26, 2022, 3:04 AM*

Friends, when malicious jews had almost retarded me and had done more than a decade of persecution, I started to speak
on forums against my cruel and brutal persecution. Those jews who were behind my persecution knew that people would
rebuke them for being so cruel. So, they concocted many stories making people feel that they wanted to be very good and
nice to me and I was rude to them. Most of the stories go like "we wanted to help him and we gave him some mind control
chemicals to help him out to become better but due to our chemicals, he became too intelligent and became rude to us and
started ranting against us and we decided to continue mind control until we take those chemicals out of his brain that
we had given him."

I want to tell people that any story like this is totally false and concocted to hide the hatred and venom of people
behind mind control and instead portray them as good people after their evil has been revealed.

Do, all the other 300-500 intelligent Pakistanis who are on mind control here, all were given drugs to improve them, and
things went wrong.

I want to tell friends that things take decade to build but only take minutes to destroy. Mind is exactly like that. You
have to work very hard to give right training to the brain and it takes decades of childhood and adulthood, but all of
this gets retarded when only one or two essential neurotransmitters that are necessary for the neurotransmitter
sequences for a particular task. You can retard people easily, but you cannot make them extra-intelligent very easily.

I went to the best boarding school in Pakistan (Cadet College, Hasanabdal) where several tens of thousands of people
compete for only hundred slots. Only cream of the cream is admitted to the college. I was always among top three boys in
the college in academics. I got the most marks in Mathematics in the whole division (40,000-50,000 students) in my high
school graduation examination. I recall when I was in eleventh grade, our senior class (twelfth grade at that time) was
given a very tough and out of syllabus calculus question in the examination and nobody could solve the calculus question
in the entire senior class. And I solved that calculus question in minutes despite that I was in junior year.

To this day, I believe that it was my high school that shaped my life and no university influenced me anywhere closer to
the kind of great influence that my college (high school) had on me.

My only remorse is that I took Electrical Engineering as major and did not study mathematics as major in my bachelors. I
lost all interest in Engineering when I was at Northwestern and performed so badly in last years that I had to go to a
crap school (NYU) after that where a lot of people had little stature.

When I was in economics department at NYU, I made a habit of working extremely hard because I wanted to undo my mistake
of not working hard at Northwestern. Many times, I would be among only 2-3 guys in the library when it would close on
weekends. I would stay in the computer lab of the economics department till 2-3 am in the morning on many days.

One night, at 3:00 am in the morning, I was driving from manhattan to Queens (where I lived) on my car and I was half
asleep and failed to notice a red traffic signal on a totally empty road. There was another red light 300 metres ahead
and I stopped there. A police car came from behind and told me that I had violated the previous traffic signal. I told
the police officer that I had been working very late in the computer lab and was almost asleep and could not notice the
signal. I also told him that if my intention were to violate the signal, I would have violated this second signal as
well where I had stopped. Police officer threw his torch light on the back seat of my car and found that more than
twenty books ( you can check my library records, this was the average) were scattered on the back seat that I had
borrowed from the library. Police officer was very nice and shook hands with me and asked me to be careful in the
future.

I also recall another incident when my car got off the road onto a sidewalk and I barely escaped an accident when I was
driving to Queens at 2:00 am in the morning.

Again you can retard a brain in a matter of minutes, but in order to have a strong brain, you have to work hard all your
life.

My college had shaped me where we used to remain awake and study very late into the night close to the exams since there
was very tough academic competition.

So, all the stories of somehow making me more intelligent are just another expression of venom and hatred with which I
was retarded. They have absolutely no truth in them. They just make the perpetrators of evil feel good before others
when they tell them such stories that they wanted to somehow help me. Please do not become gullible before these evil
creatures that love to retard other human beings.

If these stories of making me intelligent by giving me special neurotransmitters are true, why do these malicious jews
not take these neurotransmitters themselves and make themselves far more intelligent than I am. Because these dumbfucks
cannot.

---

### #1584 — Amin (Topic Author)
*October 26, 2022, 2:30 PM*

Before writing this post, I want to apologize to good jews but want to tell them there are enough evil jews who are
doing everything to tarnish the great goodwill jews have so rightly earned through generations of hard work and being
nice and kind to other people in the society. I want to request good jews to Please force these evil(jewish) people to
end the bad practices that are starting to take root in American and other societies on their behest and before it is
too late. I also really hope that my mind control would finally end(as I have been begging for past twenty years) and I
would never have to write a post like this again.

In the past, I continued to mention about my mind control persecution from time to time but only started writing regularly about it when I arrived in UK on a Highly Skilled Migrant work visa. Mind control agencies did everything in their power to fail me in UK. People were asked to not give me a job. People I contacted were routinely told brazen lies about me totally shamelessly. When I realized that I had no future in UK, I returned to Pakistan after a six month stint in UK. Since my hard earned money had thoroughly insulted mind control infrastructure in UK as they had to drug entire cities with mind control chemicals in UK (read briefly about it in my application to HRW in a previous thread) for a nobody like me and American government had to move all their grand and influential puppets in UK (again for a nobody like me) to force people to drug the manufactured food. British Banks went to the extent to steal my money to bleed me. Read here: https://forum.wilmott.com/viewtopic.php?f=15&t=102298#p857494. British police forcefully stopped me from seeing law firms(Brief details are given in my application to HRW attached as a link below).  Since my money had given mind control agencies a very tough time, mind control agencies decided to never let me make significant money after that. My old Japanese employer was told to not hire me after I returned to Pakistan. Whoever I would contact someone in Europe for job or consulting, mind control agencies would move American embassy infrastructure in that country and somebody highly influential (or army or secret services of that particular country)  in that particular country would approach my target employer and again brazen lies and fabricated stories would be told about me shamelessly. I am a fighter in life and I continued my research despite all economic, coercive and other hardships. All odds were against me but I tried my best to continue.  I have been presenting my research to friends on this forum for past five or six years. At this point, I want to request good American and friends from other countries who have come to know me through my research to please use their influence to end my mind control forever.

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

### #1585 — Amin (Topic Author)
*October 27, 2022, 9:40 AM*

I had earlier told friends that mind control crooks changed my programs with their hidden files and totally altered
behavior of my programs. Now my family is pressurizing me to start live trading on Binance. I am reluctant to start live
trading unless I could perfectly secure my computers. I am perfectly sure that next plan of the mind control agencies is
to let me do live trading for a few days and then intervene to replace my programs and make me lose all my money. And
when I would mention my losses at Wilmott, all the malicious jews who are behind my persecution would go around town
making fun of me that I was talking about 200% per month profits but later lost all money. And then those jews will
discredit me in all sort of ways. And then my family would be asked to pressurize me to leave research in finance and
take up a mediocre job somewhere.  I am hundred percent sure this is the next machination on which mind control agencies
and malicious jews are working together.  I am therefore unwilling to start live trading unless I know my computers are
secure or I could be assured that my programs would not be changed.

I have decided to take some time off and learn more about deep neural networks. And leave trading programs aside for a
moment.

I will continue to past about machinations of bad jews and mind control agencies everyday on this forum.

I also want to send tweets to American senators asking them to intervene and end my mind control. About three years ago,
I sent tweets to about fifteen American Senators but scumbag crooks of Pentagon stopped all my tweets becuase they never
wanted their crimes and tactics to be exposed before good American Senators. Therefore when I send tweets to American
senators now, I would be posting their name and messages on this forum so good people could check if scumbags of
Pentagon are intercepting my tweets from reaching good American senators and some good Americans could mention it to
respective senators. I would also approach muslim senators and congresswomen.

---

### #1586 — Amin (Topic Author)
*October 27, 2022, 11:31 AM*

As I told friends earlier that I tried to approach a large number of American senators and also Pakistani politicians
and journalists through twitter and email but my tweets and emails were all stopped.

I have again decided to reach every single American Senator and member of congress with both tweets and email messages.
I will only approach 5-6 senators or members of congress per day. I will mention their names, twitter handles and emails
here on this forum.

Americans are not a bad people at all. Probably exactly the reverse is true about them. If I have not been able to find
justice, it is because I failed to reach the right audience who have more authority to end the torture and persecution.
This is exactly why American army stops my emails to senators because they know they are doing something wrong that
cannot be justified before good American senators.

I want to appeal to good Americans to approach the senators I tweet and email and tell them/email them about me that
this guy has been asking for help on internet for more than ten years and has told us that his messages to senators are
blocked by American army repeatedly and then request the senators to read the original message on Wilmott forum on this
thread. I am sure when my messages are read by good Americans in authority, they will really do something about ending
mind control by American army and bad jews in our society.

Similarly, when I write tweets to some Pakistani politician or journalist, I will request Pakistanis abroad and at home
to approach/email the politicians or journalists to read the tweet message and internet links on this forum.

Since I will not be sending more than 5-6 tweet messages per day, it will just require a very brief time from friends to
independently email/tweet the recipient senators and request them to read about my mind control here. I really hope that
with a very small help from friends, we would be able to eliminate mind control from our society forever. I would truly
be obliged to friends for their kind favors.

---

### #1587 — Amin (Topic Author)
*October 28, 2022, 11:35 AM*

Friends, I set up a new twitter account. My twitter account handle is [](https://twitter.com/AhsanAmin2999)@AhsanAmin2999

And I sent my first tweet to Senator Elizabeth Warren. I will be sending at least five more tweets today to different
American senators. I will later come back with their names and twitter addresses. Following is my tweet to Senator
Elizabeth Warren.

@SenWarren

I am requesting for help to save my grave human rights abuses and mind control by the American army. I am a well known
mathematics researcher who has been a target of mind control abuse since 1997.

https://forum.wilmott.com/viewtopic.php?f=15&t=102298

https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1575

[](https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1575)

---

### #1588 — Amin (Topic Author)
*October 28, 2022, 2:36 PM*

Friends, I tweeted to following four more senators on their official senate account.

1. Bernie Sanders

2. Ed Markey

3. Patty Murray

4. Alex Padilla

Here was the last tweet

@SenAlexPadilla

I am a well known mathematical finance researcher who has been a target of mind control since 1997. I am requesting for
help to save me from further human rights abuses and end my mind control by the American army.

[viewtopic.php?f=15&t=102298](https://forum.wilmott.com/viewtopic.php?f=15&t=102298)

[viewtopic.php?f=4&t=99702&start=1575](https://forum.wilmott.com/viewtopic.php?f=4&t=99702&start=1575)

---

### #1589 — Amin (Topic Author)
*October 29, 2022, 6:18 AM*

Friends, please check out my article on linkedin asking for venture capital.

https://www.linkedin.com/pulse/quantitative-trading-business-proposition-asking-venture-ahsan-amin/

Model Description.

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
data, there were several days every month when profits exceeded ten percents.

So, these small profits when aggregated over a large number of trades become very significant and usually become several
percentage points of the capital for even a single day. When aggregated over the entire month, these profits are a large
proportion of the allocated capital. In testing our models and determining their profitability, we have used zero
leverage. In our simulations on real data average profits remained 3% to 7% per single day after accounting for broker
costs even though in large scale simulations on real data there were one or two days every month when we made a loss of
2%-3% with a very high Sharpe Ratio (>1.5)

Mathematical Principles Underlying the Model.

Our model uses predictive machine learning to make trading decisions. We have used machine learning in a setting nobody
in literature has ever done before. In our research setting, we apply machine learning to optimize for the parameters
using previous day’s data. And these optimized parameters learnt from previous day data are used to make trading
decisions during the following day. Strength of the predicted signal is used in the future prediction of the time series
variables. We tested our algorithms on large scale data with the above rolling window of training on 24 hours of data
and then applying the model to the next 24 hours of data. This machine learning method is a new technique and is not
known to people in financial markets. This results in more accurate prediction of the market than any time series model
or process that analysts and quants usually use in financial markets to make a prediction of financial assets.

Risks Associated with the Model.

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

Prospective Financial Markets for Trading.

We want to use our model to trade HK stocks, Stock exchange Index futures, Forex futures and commodities like oil and
gold futures.

Limitations of the Model.

We have tried our models extensively on historical data but we have not done live trading with our models. We want to
train our models comprehensively on paper trading with some good brokers and then use them for live trading in the final
step.

Capital Requirements.

We will require an initial amount of one million dollars and as the profitability of our models becomes evident, we will
continue to scale the trading capital with time once our market trading strategies continue to generate large profits.
As we demonstrate that our trading strategies remain profitable with time, we will gradually increase the trading
capital to several hundred million dollars.

---

### #1590 — Amin (Topic Author)
*November 2, 2022, 9:20 AM*

Friends, here is what happened in past few days. After writing the above article on linkedin asking for venture capital,
I sent my article through linkedin message to about 15-20 Pakistanis. I also talked to a few Pakistanis about formation
of algorithmic trading company. Some people were very nice and helpful while a few others were totally opposite. But
nobody has decided to help yet. I remained pretty busy over past three days. I was also tired due to antipsychotic
injection. Here is a comment I added to my linkedin article.

> I am putting together a more detailed document about my proposed company.
>
> If you read the above linkedin article, I am asking for a million dollars but that is not necessary, I would be
equally fine with 100,000 dollars that is roughly the money to trade one lot of shares that costs \$750. Plus some money
to make a small secure office and employ 2-3 persons for two months until we start taking money out of our profits.
>
> I am sure there are very few places in the world that have advanced models to make profitable trades like this.
>
> If you like, please email me
at [[email protected]](/cdn-cgi/l/email-protection#13727d727d212a2a2a536a727b7c7c3d707c7e) or simply message on linkedin
and I will forward you the advanced details when they would be ready.

Though I will continue to approach people about help with initial fundraising, I have decided to add very robust risk
management into my model. In my python code, I had just added the algorithm to make trading decisions and also coding to
send/cancel new orders every ten seconds. I had also added profit taking and stop loss code to the model. But I had not
done proper back-office work and robust risk management. Now I want to add code that will keep a record of trading
decisions, sending and cancellations of orders, and all other necessary things. I will also add very robust risk
management that will turn off the python algorithmic trading program if the program starts to consistently lose money
over short periods, When I would have record of orders, decisions, and trades, I would be able to double check
everything offline once my program loses money. And robust risk management will stop my programs once they start making
losses. So when mind control agents alter my program, I will have my decisions, orders and trades saved on disk to back
check if it would be my program's fault or mind control agents would have replaced my programs with their hidden
programs.

If I were not afraid that mind control agents would replace my programs with their hidden programs, I would already be
trading in crypto at the moment.

Just yesterday mind control guy told me that his backers in US had earlier asked him to not change my programs in the
future because there was too much pressure against it from good people in US. But mind control guy told his backers to
not worry at all and said that he would surely change my programs when the right time would come but when I would
complain about it and make noise, then everybody including mind control agent and his backers in US all would completely
deny that they altered my program in any way and they would tell everyone that it was my own program's fault.

So, I will keep working to make my programs robust in risk management. When I would suspect that they would have altered
my programs, I would have the ability to match all numbers from my program with other offline data and I would know if
it were my own mistake or some other problem.

Again, I want to request good people to force mind control agencies to not alter my programs in the future as they had
not done in past 5-6 years.

If everything goes well, I would come back again on the forum with more research on stochastic processes, probability
theory and machine learning.

I also may post some more hints about how I was able to find good trading algorithms that work so well and share some of
my secret sauce with friends on this forum.

---

### #1591 — Amin (Topic Author)
*November 4, 2022, 3:08 PM*

Past few days were very difficult for me. I got antipsychotic injection on Wednesday, last week. Mind control agencies
have supplied fluanxol injections at all pharmacies that have mind control chemicals added to them. The first week or
ten days after the injection become extremely difficult. During this time, they continue to take neurotransmitters out
of the body. I remain extremely tired and continue to feel ache all over my body. It becomes difficult to stay up late
and I remain highly sedated with frequent naps during the day. It is very difficult for me to pass first ten days after
the injections. It always used to be difficult to pass first ten days after the injection but every time, I pass through
this phase again, it seems that things have become even more difficult.

I really want to request friends to ask mind control agencies to end my antipsychotic medication.

The only way I can get out of this antipsychotic trap is by making some money and becoming independent, but scumbag
neocons of Pentagon never want me to become able to do that. These scumbags of Pentagon are so haughty and arrogant that
they know large number of people read stories of my persecution and torture, but they make no big deal about it and
continue to remain adamant at continuing and increasing my persecution. I have been writing about my persecution for
more than fifteen years and people know it is only based on racism and malice against my nation, but still to no avail.
People know I am totally innocent, but nobody can help end my persecution because arrogant scumbags of Pentagon are not
ready to let go of me.  People know I am a good guy who never wants to harm anyone but scumbags of Pentagon want to use
my goodness as an excuse (that he cannot do anything about it or against us) to heroically maltreat me for the rest of
my life. Is there any goodness anywhere or it is all just a jungle law where only might is right rules.

My only hope was that I would be able to make enough money by trading in the markets and become independent and my
torture and persecution would end but arrogant scumbags of Pentagon are even more happy and they have found another
opportunity to teach me a lesson by changing my computer programs I want to use for trading purposes.

Please protest to people at Pentagon against my continuing maltreatment. And ask them to not change my programs for
market trading. I really want to tell people that they have a hundred percent program to alter/replace my programs when
I would trade. They have absolutely no humanity and they would rather treat their dogs far better than they treat any
intelligent muslims because of their sheer racism.

---

### #1592 — Amin (Topic Author)
*November 6, 2022, 2:17 PM*

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

There is another thing that I want to bring to friends' attention. I am going to have a phone meeting with the current
psychiatrist on this Tuesday. I am very sure that my mother and sister would try their best to decrease the period
between injections and make the psychiatrist feel that I am mentally sick. I Want to request friends and foreign
embassies in Pakistan to please record my conversation with the psychiatrist so they could get to know how innocent
people are maltreated by psychiatrists when mind control agencies and generals give them bribes.

Please protest to American mind control agency and ask them to end my antipsychotics and do not allow them to decrease
the duration of period between two antipsychotic injections.

---

### #1593 — Amin (Topic Author)
*November 8, 2022, 1:47 PM*

I had a brief phone meeting with the psychiatrist today. It went reasonably well. I requested the psychiatrist to
increase the duration between injections from three weeks to four weeks. Psychiatrist said if anything my medication
needed to increase and not could be decreased but he decided to not change the medication at the moment. He also agreed
that it was fine if I were taking every next dose after a further delay of one or two days and made no big deal about
it. Next phone meeting with the psychiatrist would be after three months.

Friends, today I decided to take 3-4 days off from my algorithmic trading research. I had some ideas about improving the
analytic SDE evolution by cumulants method and I thought that new ideas could make the method accurate in the tails
where it was earlier lacking. I could not be hundred percent sure whether new ideas would work but I am very excited to
give them a try. So next 3-4 days, I would be working full time on improving my research on SDEs and trying to fix the
problems in the tails. I hope to put a lot of material online in these days if the new ideas work well.

---

### #1594 — Amin (Topic Author)
*November 8, 2022, 5:09 PM*

```
Friends, today I decided to take 3-4 days off from my algorithmic trading research. I had some ideas about improving the
analytic SDE evolution by cumulants method and I thought that new ideas could make the method accurate in the tails
where it was earlier lacking. I could not be hundred percent sure whether new ideas would work but I am very excited to
give them a try. So next 3-4 days, I would be working full time on improving my research on SDEs and trying to fix the
problems in the tails. I hope to put a lot of material online in these days if the new ideas work well.
```

.

.

Friends, while dealing with evolution of SDEs, when we calculate transformations of the SDE variable through Taylor
Series, the approximation is very good in the main body of the program, but Taylor approximation is usually poor in the
tails. This lack of good approximation continues to slightly deteriorate the accuracy of the SDE evolution on every
step. This is also one of the factors that lead to inaccuracy when we find time integral of the SDE and its functionals.

In my experiments, I had earlier learnt that if the Z-series coefficient on the highest odd term (that defines even
moments) is slightly negative enough, the approximation in the tails is quite good. And if this coefficient is large
enough positive, the approximation in the tails is very poor.

So, I decided to append an extra Z-series coefficient on the highest odd power that is known in advance as a fraction of
coefficient at smaller odd power. We had been dealing with 7th order Z-series that defines eight moments. So, For
example, I am thinking about adding a negative coefficient on 9th power of Z-series that would be like 1/4 th absolute
value of coefficient on the 7th power of Z-series. And then all of the Z-series coefficients would be optimized by
Newton method keeping 9th negative coefficient as a constant in optimizations. This could help keep Taylor based
transformations of the SDE variable accurate and faithful in the tails increasing the accuracy of analytic numerical
schemes.

But let use see how the whole thing goes.

---

### #1595 — Amin (Topic Author)
*November 10, 2022, 11:45 AM*

I am writing this post to inform friends about enhancements I have made in the Newton (Matrix) root search method in
high dimensions. As most friends would know that I have been using Newton root search in high dimensions in order to fit
(first eight) parameters of the Z-series polynomial so that moments of the standard normal based (7th order) polynomial
exactly fit the (first eight) moments prescribed by the user or put forth in calculations of various other problems.

Though most of the time, high dimensional Newton Iteration converges, there is no guarantee it would always do so. I
also particularly noticed that in some other problems Jacobian matrix of derivatives would be available but for some
other reason, matrix inversions would be poorly scaled due to bad condition number and Newton would strongly diverge as
if it were blowing. There are a large number of other reasons when we would have a valid Jacobian and all other
information calculated but Newton or other optimization method would still diverge for one reason or another. The method
I present wants to help friends in all of the above conditions when multidimensional Newton root finding/optimization
fails, and we are left aghast what to do to solve our problem.

First Introduction to Newton Root Finding Method.

In Multiple Dimensions, for finding K zeros of a K dimensional function F(X), we have to divide it with its K X K
dimensional Jacobian as

For nth iteration, we have

$ X_{n+1} \, = \, X_n \, - \, {[J_F(X_n)]}^{-1} \, \, F(X_n) \,$

We also suppose that there is an objective function associated with this root-finding/optimization problems. We call it
original objective function in what folllows.

This Objective function is denoted as$OBJ=G(X_{n+1})$ . This objective function is applied on the updated value$X_{n+1}$

However depending upon the problem and due to a large number of possible reasons, the above method does not converge all
the time even when theoretically the zeros could be found.

I have been able to find a way using which the method could still be made to work. I have applied it to Newton
root-finding equations, but the method could equally be applied to high dimensional numerical optimization problems.

I introduce a scalar parameter in the Newton root-finding/Optimization update equations. We optimize the value of this
scalar parameter by Newton second order optimization so that Objective function in our original problem is
maximized/minimized.

$ X_{n+1} \, = \, X_n \, -\, h_m \, {[J_F(X_n)]}^{-1} \, \, F(X_n) \,$

$h_m$ is the scalar parameter introduced in optimization.

Please note that we have done all the hard work to calculate Jacobian in original problem and we use it to calculate the
update. Now, all we need to do is to multiply this matrix update with our introduced scalar parameter repeatedly and use
the original objective function repeatedly for Newton optimization iterations on the scalar parameter.

We start with an initial value of$h_m=1$ , and perturb it to find first and second derivatives of the objective function
with respect to$h_m$ . Please note that we have already done the hard work to calculate the jacobian and it does not
need to be recalculated for any further analytics on$h_m$ and we simply reuse the already calculated value of Jacobian
every time. Now we find the optimal value of$h_m$ using the second order Newton optimization equation as

$h_{m+1} \, = \, h_{m} \, - \, \frac{\partial OBJ}{\partial h_m} \, {[\frac{\partial^2 OBJ}{\partial {h_m}^2}]}^{-1} $

So that the objective function is optimized (for$X_{n+1}$ associated with$h_m$ ) given the value of jacobian we had once
calculated.

This way we can find a value of scalar$h_m$ that maximizes the Objective function. Many times when our matrices are
badly scaled (or due to many other possible reasons that straightforward optimization fails), there is usually more than
enough information in the Jacobian to take an explicit scalar correction and start working robustly again.

So basically there are two levels of optimization in it. First there are N steps in original optimization where we
calculate jacobian each time and for each of the nth step (leading to N steps in total), we do M optimizations on the
scalar parameter$h_m$ so that result of the original nth step optimization is best optimized. Nested M optimizations are
very simple and fast (if the objective function is simple) because we do not have to recalculate the Jacobian every time
for mth step.

I am very sure that this method can be applied on difficult optimization problems universally and therefore I am
presenting it for friends here.

I would soon be uploading my matlab programs based on the this post in another 2-3 days.

---

### #1596 — Amin (Topic Author)
*November 11, 2022, 8:46 AM*

Friends, I have decided to increase the scope of my project. I want a reliable matlab program that finds
Z-series/polynomial coefficient given any set of valid moments. This will be applied to SDEs and their reliable Taylor
transformations later something that I originally intended to do.

Earlier, I have been able to do it what I have called Gaussian based/Bessel based densities but not for all possible
types of smooth densities.

I have also decided to change the main optimization engine of the program from Newton root-finding to gradient descent
optimizations.

I will come back with the first proto-type matlab program in a few days.

---

### #1597 — Amin (Topic Author)
*November 16, 2022, 4:16 PM*

Two days ago, I repeated my request for venture capital by writing another article on linkedIn. I also want to approach a few good people and firms directly. I have revealed something more about my trading algorithms as well. Please read here: https://www.linkedin.com/pulse/trading-venture-proposition-ahsan-amin/

Sorry that I am no more modest and have been brazen and shameless (in speaking the truth) when writing above article. I
think this is what you have to be when you ask for venture capital.

---

### #1598 — Cuchulainn
*November 17, 2022, 5:05 PM*

*For instance, millions of computers in tens of thousands of financial institutions use Monte Carlo simulations of
stochastic differential equations every day to price derivatives and project risk of financial portfolios. Author
discovered for the first time how to do higher order accurate Monte Carlo simulations of stochastic differential
equations (SDEs).

*

*Fokker-Planck partial differential equation is among ten major equations of mathematics and describes the time
evolution of probability densities associated with SDEs. For the first time, author discovered several analytic ways to
solve the Fokker-Planck equation.*

Can these statements be quantified?

In particular, MC is usually slow _and_ not very (predictably) accurate.

What are the "big 10" in your opinion?

---

### #1599 — Amin (Topic Author)
*November 18, 2022, 3:12 AM*

I have done most of these things and many other on the same thread. I am afraid you have not been following the thread.
For your information, I will give references to where I gave higher order solution to Monte carlo and Fokker-planck
equation.

When naive monte carlo schemes have biases, you can try trillions of simulations only to get a wrong answer unless the
problem is almost trivial or your step is too miniscule. Only when you have an accurate higher order discretizations
that I presented that you get a right answer when you increase monte carlo paths.

If you think monte carlo is slow, many shops are using my methods with Quasi-random sequences for monte carlo
simulations that are faster than many analytic methods and are practically instantaneous.

I did say that Fokker-planck is among ten most important equations in mathematics.  In somebody's mind it might be 12th
or 8th. I do not want to argue about it but it is one of the most important equations in mathematics.

I have added the following lines to my article here. https://www.linkedin.com/pulse/trading-venture-proposition-ahsan-amin/
> I discovered a new series method to solve Ordinary Differential Equations of first order, nth order ODEs and systems
of ODEs. The method almost always works (until the ODE is singular when you have to transform it into a non-singular
form) and the series solution is series of true analytic solution of the ODE.
Now find some quibble about it as well.

---

### #1600 — Amin (Topic Author)
*November 18, 2022, 3:14 AM*

Sorry Double.

---

[← Previous](page_031.md) | [Index](index.md) | [Next →](page_033.md)
