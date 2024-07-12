CONST   fi='PITAGO.inp';
        fo='PITAGO.out';
        nm=10001;
VAR     a,b,c:ARRAY[0..nm]OF LONGINT;
        i,j,n,d,m:INTEGER;
        t,k:LONGINT;
        f:TEXT;
FUNCTION kt(d,m:INTEGER):BOOLEAN;
     VAR i:INTEGER;
BEGIN
        FOR i:=1 TO m-1 DO
         IF d=a[i] THEN
          BEGIN
                kt:=FALSE;
                exit;
          END;
         a[m]:=d;
         kt:=TRUE;
END;
PROCEDURE nhap1;
BEGIN
        randomize;
        assign(f,fi); rewrite(f);
        write('Vao n='); readln(n);
        writeln(f,n);
        m:=n+n;
        IF m>nm THEN m:=nm-1;
        FOR i:=1 TO n DO
         BEGIN
         REPEAT
                d:=random(m)+1;
         UNTIL kt(d,i);
         write(f,a[i],' ');
         END;
        close(f);
END;
PROCEDURE nhap;
BEGIN
{        nhap1;}
        assign(f,fi); reset(f);
        readln(f,n);
        FOR i:=1 TO n DO
         read(f,a[i]);
        close(f);
END;
PROCEDURE qs(l,r:INTEGER);
VAR i,j:INTEGER;tg,x:INTEGER;
BEGIN
     x:=a[(l+r)DIV 2];
     i:=l;j:=r;
     REPEAT
           WHILE a[i]<x DO inc(i);
           WHILE a[j]>x DO dec(j);
           IF i<=j THEN
            BEGIN
                 tg:=a[i];
                 a[i]:=a[j];
                 a[j]:=tg;
                 inc(i);
                 dec(j);
            END;
     UNTIL i>j;
     IF i<r THEN qs(i,r);
     IF j>l THEN qs(l,j);
END;
PROCEDURE xuly;
BEGIN
        assign(f,fo); rewrite(f);
        fillchar(b,sizeof(b),0);
        qs(1,n);
        FOR i:=1 TO n DO BEGIN b[a[i]]:=1;c[i]:=a[i]*a[i];END;
        d:=0;
        FOR i:=3 TO n DO
         FOR j:=2 TO i-1 DO
          BEGIN
                t:=c[i]-c[j];
                IF c[j]>=t THEN
                BEGIN
                        k:=trunc(sqrt(t));
                        IF (sqrt(t)=k)AND(b[k]=1)THEN
                           BEGIN
                                inc(d);
                           END;
                END;
          END;
          write(f,d);
          close(f);
END;
BEGIN
        nhap;
        xuly;
END.
