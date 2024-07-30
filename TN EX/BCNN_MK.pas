VAR f,g:TEXT;    b,a:ARRAY[1..100] OF WORD;
    T,kq,du:LONGINT;    N,i:BYTE;
BEGIN
 assign(f,'matkhau.inp6');reset(f);
 assign(g,'matkhau.out6');rewrite(g);
 readln(f,N);
 FOR i:=1 TO N DO read(f,a[i]);
 kq:=a[1];
 FOR i:=2 TO N DO
  BEGIN
   T:=kq*a[i];
   du:=kq MOD a[i];
   WHILE du<>0 DO
    BEGIN
     kq:=a[i];
     a[i]:=du;
     du:=kq MOD a[i];
    END;
   kq:=T DIV a[i];//a[i] lúc nay là UCLN;
  END;
 writeln(g,kq);
 close(f);close(g);END.
