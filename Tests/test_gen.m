% Give a bunch of data point (x,y)
% and I 'think' this function is sth like f(x) = Acos(Bx) + C
% because of the plots generated by the data points
% So, now, use genetic algo to get 'A' 'B' 'C'
% -------------
% 1. guess 'n' solutions(samples) as one generation
% 2. choose the best 'k' from 'n' as seed, fittest survival
% 3. generate next generation by 'seed'
% 4. loop 2~3,until get the best one

clear all; close all; clc

x = 1:24;
y = [75 77 76 73 69 68 63 59 57 55 54 52 50 50 49 49 49 50 54 56 59 63 67 72];
plot(x,y,'ko')

m = 200; % generations
n = 50;  % trials
n2 = 10; % kept trials

% the 1st generation samples
% 'A','B','C' has a 50 samples their own
% and this is why Matlab so special, its variable
% can reference to a list of items by one line code
A = 12 + randn(n, 1);
B = pi/12 + randn(n, 1);
C = 60 + randn(n, 1);

for jgen = 1:m
    for j = 1:n
        E(j) = sum((A(j)*cos(B(j)*x) + C(j)-y).^2);
        % use min[sum(least squre error)] as our object fn
    end

    plot(E), pause(0.5) % plot error every loop

    [ES,Ej] = sort(E); % sort from small to large
                       % use sort to choose the best 10 as seed
                       % to generate next 50 descendants

    Ak1 = A(Ej(1:n2)); % choose foremost 10 samples
    Bk1 = B(Ej(1:n2));
    Ck1 = C(Ej(1:n2));

    % use random-fn to simulate mutation
    % TODO why devided by 'jgen'?

    Ak2 = Ak1 + randn(n2,1)/jgen;
    Bk2 = Bk1 + randn(n2,1)/jgen;
    Ck2 = Ck1 + randn(n2,1)/jgen;

    Ak3 = Ak1 + randn(n2,1)/jgen;
    Bk3 = Bk1 + randn(n2,1)/jgen;
    Ck3 = Ck1 + randn(n2,1)/jgen;

    Ak4 = Ak1 + randn(n2,1)/jgen;
    Bk4 = Bk1 + randn(n2,1)/jgen;
    Ck4 = Ck1 + randn(n2,1)/jgen;

    Ak5 = Ak1 + randn(n2,1)/jgen;
    Bk5 = Bk1 + randn(n2,1)/jgen;
    Ck5 = Ck1 + randn(n2,1)/jgen;

    % ready for next generation with 50 samples
    A=[Ak1;Ak2;Ak3;Ak4;Ak5];
    B=[Bk1;Bk2;Bk3;Bk4;Bk5];
    C=[Ck1;Ck2;Ck3;Ck4;Ck5];

end

% plot the best one
Ak1 = A(Ej(1));
Bk1 = B(Ej(1));
Ck1 = C(Ej(1));

f = Ak1*cos(Bk1*x) + Ck1;

plot(x,y,'ko',x,f)