uses Crt;
var
n,s,t,x:int64;
a,vt,b:array[0..100005] of int64;
i,j:longint;
procedure qs(d,c:int64);
var i,j,x,tg:int64;
begin
i:=d;
j:=c;
x:=a[(d+c) div 2];
repeat
while a[i]>x do inc(i);
while a[j]<x do dec(j);
if i<=j then
begin
tg:=a[i]; a[i]:=a[j]; a[j]:=tg;
tg:=vt[i]; vt[i]:=vt[j]; vt[j]:=tg;
inc(i);
dec(j);
end;
until i>j;
if i<c then qs(i,c);
if d<j then qs(d,j);
end;
procedure sort(d,c:int64);
var i,j,x,tg:int64;
begin
i:=d;
j:=c;
x:=b[(d+c) div 2];
repeat
while b[i]>x do inc(i);
while b[j]<x do dec(j);
if i<=j then
begin
tg:=b[i]; b[i]:=b[j]; b[j]:=tg;
inc(i);
dec(j);
end;
until i>j;
if i<c then sort(i,c);
if d<j then sort(d,j);
end;
BEGIN
assign(input,'gifts.inp'); reset(input);
assign(output,'gifts.out'); rewrite(output);
read(n,s);
for i:=1 to n do
begin
read(a[i]);
vt[i]:=i;
end;
qs(1,n);
t:=0;
for i:=1 to n do
if t+a[i]<=s then
begin
if x+1>2 then break;
inc(x);
b[x]:=vt[i];
t:=t+a[i];
end;
writeln(t);
sort(1,x);
for i:=x downto 1 do
if b[i]<>0 then write(b[i],' ');
END.
