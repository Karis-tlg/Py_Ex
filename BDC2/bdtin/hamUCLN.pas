Program hamUCLN;
uses crt;
Var a,b:longint;

Function UCLN(t:longint):longint;
   var r:longint;
   Begin
      r:=a mod b;
      while b <> 0 do
      Begin
      a:=b;
      b:=r;
      r:=a mod b;
      End;
      UCLN:=a;
   End;

BEGIN
        Clrscr;
        Write('Nhap so a: '); Readln(a);
        write('Nhap so b: '); Readln(b);
        Write('UCLN cua a va b la: ',UCLN);
        Readln;
END.
