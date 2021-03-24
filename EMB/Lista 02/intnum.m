clc;
function integral=intnum(f,var,x0,x1,N)
   dx=(x1-x0)/N;
   i=x0:dx:x1;
   integral=sum((subs(f,var,i))*dx);
end

