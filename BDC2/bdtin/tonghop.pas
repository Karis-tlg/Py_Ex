program tonghop;
uses crt;
var i,n,j,t,x:longint;
  so: array[1..100] of longint
begin
      clrscr;
      write('Nhap vao so n: ');readln(n);
      write('So nto la: ');
      for i:=1 to n do
      for j:=1 to i do
        if i mod j=0 then t:=t+1;
        if t=2 then write(j,', ');
        write(j:5);
      t:=0;
      end;
      for i:=1 to x div 2 do
        if i*i=x then
      begin
        write(i,'la so chinh phuong');
        n:=1;
        break;
      end;
      if n=0 then writeln(x,'khong phai la so chinh phuong');
readln;
end.