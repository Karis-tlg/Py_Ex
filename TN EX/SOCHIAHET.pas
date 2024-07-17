CONST fi='SOCHIAHET.inp';
      fo='SOCHIAHET.out';
VAR
   a,b : ARRAY[1..10000] OF INT64;
 n,i,dem:LONGINT;X,Y:INT64;
    kt:BOOLEAN;  f,g:TEXT;
    FUNCTION chht(x:INT64):BOOLEAN;
    VAR n:LONGINT;Y:INT64;
        kt:BOOLEAN;
     BEGIN
      kt:=TRUE;
      y:=x;
      WHILE x <> 0 DO
       BEGIN
        n:=x MOD 10;
        IF (n=0) THEN kt:=FALSE
        ELSE IF (y MOD n <> 0) THEN kt:=FALSE;
        x:=x DIV 10;
       END;
      chht:=kt;
     END;
BEGIN
     assign(f,fi); reset(f);
     assign(g,fo); rewrite(g);
    readln(f,n);
    FOR i:=1 TO n DO
      read(f,a[i]);

 FOR i:=1 TO n DO
  IF chht(a[i])=TRUE THEN BEGIN
    dem:=dem+1;
    b[dem]:=a[i];
    END;
    writeln(g,dem);
  FOR i:=1 TO dem DO
   write(g, b[i],' ');
    close(f);close(g);

 //readln;
END.
