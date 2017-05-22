x = -3:0.01:3;

[X, Y] = meshgrid(x, x);

Z = exp(-X.^2  - Y.^2);

figure;
mesh(Z);

figure;
imagesc(Z);