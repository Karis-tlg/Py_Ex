const fi='robot_i.txt';
fo='robot_o.txt';
var f1,f2:text;
n,i,t:integer;
a:array[1..10000]of integer;
begin
assign(f1,fi); reset(f1);
assign(f2,fo); rewrite(f2);
readln(f1,n);
for i:=1 to n do
read(f1,a[i]);
t:=0;
for i:=1 to n do
begin
if a[i]=1 then t:=t+1
else t:=t-1;
end;
writeln(f2,t);
close(f1);
close(f2);
end.
