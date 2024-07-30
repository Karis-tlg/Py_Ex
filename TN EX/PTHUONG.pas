PROGRAM bt;
VAR   a,f:ARRAY[1..10000] OF int64;   f1,f2:TEXT;
i,n:LONGINT;
FUNCTION max3(a,b,c:int64):int64;
VAR max:int64;
BEGIN
max:=a;
IF max<b THEN max:=b;
IF max<c THEN max:=c;
max3:=max;
END;
BEGIN
assign(f1,'D:\olympic304lop10\bai 3\test6\PTHUONG.inp');reset(f1);
assign(f2,'PTHUONG.out');rewrite(f2);
readln(f1,n);
FOR i:=1 TO n DO
read(f1,a[i]);
{//write('nhap n');readln(n);
FOR i:=1 TO n DO
BEGIN
write('a[',i,']');readln(a[i]);
END; }
f[1]:=a[1];
f[2]:=a[1]+a[2];
f[3]:=max3(a[1]+a[2],a[1]+a[3],a[2]+a[3]);
FOR i:=4 TO n DO
f[i]:=max3(f[i-1],f[i-2]+a[i],f[i-3]+a[i-1]+a[i]);
IF n=1 THEN write(f2,f[1])
 ELSE IF n=2 THEN write(f2,f[2])
 ELSE IF n=3 THEN write(f2,f[3])
 ELSE write(f2,f[n]);
close(f1);close(f2);
//readln
END. 