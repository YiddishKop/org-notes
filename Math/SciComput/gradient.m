clear all; close all; clc

x=-3:0.1:3;
y=-3:0.1:3;
[X,Y]=meshgrid(x,y);

fsurf=X.^2+3*Y.^2;

surf(X,Y,fsurf), hold on

clear x
clear y

x(1)=2; y(1)=2; % guess
f(1)=x(1)^2+3*y(1)^2; % initial value

plot3(x,y,f, 'ko','Linewidth',[3])
view(-75,50)

for j=1:100
    tau=(x(j)^2 + 9*y(j)^2)/(2*x(j)^2 +54*y(j)^2);
    x(j+1)=(1-2*tau)*x(j);
    y(j+1)=(1-6*tau)*y(j);
    f(j+1)=x(j+1)^2 + 3*y(j+1)^2

    plot3(x(j+1),y(j+1),f(j+1), 'ko','Linewidth',[3])
    pause(2)

    if abs(f(j+1)-f(j)) < 10^(-6)
        break
    end
end