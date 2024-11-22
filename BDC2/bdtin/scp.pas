Program lietkesohh;
uses crt;
var t,j,n,i:integer;
Begin
      clrscr;
      Write('Nhap so n: '); Readln(n);
      Write('Cac so hoan hao be hon hoac bang ',n,' la: ');
      For j:=1 to n do
      Begin
          t:=0;
          For i:=1 to j-1 do
              if j mod i=0 then t:=t+i;
          If t=j then Write(j,', ');
      End;
      Readln;
End.
