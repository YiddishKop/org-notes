x(1)=3;
y(1)=2;
f(1)=x(1)^2+3*y(1)^2;

for j=1:100
    tau=(x(j)^2 +9*y(j)^2)/(2*x(j)^2 + 54*y(j)^2);
    x(j+1)=(1-2*tau)*x(j); % update values
    y(j+1)=(1-6*tau)*y(j);
    f(j+1)=x(j+1)^2+3*y(j+1)^2;

    if abs(f(j+1)-f(j))<10^(-6) % check convergence
        break
    end
end

t=1:24; % raw data
tem=[75 77 76 73 69 68 63 59 57 55 54 52 50 50 49 49 49 50 54 56 59 63 67 72];
tt=1:0.01:24;
yfit=(c(1)*cos(c(2)*tt)+c(3)).';
plot(t,tem,'ko',tt,yfit,'k-');