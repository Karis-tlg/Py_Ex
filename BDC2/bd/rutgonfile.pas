Program rutgon;
Var f:text;
    a, b, r, i, UCLN, tu, mau: longint;
Begin
    Assign(f,'D:\bd\in.txt');
      Reset(f);
      Read(f,a);
      Read(f,b);
    Close(f);

    Assign(f,'D:\bd\out.txt');
      Rewrite(f);
      a:=tu;
      b:=mau;
      r:=a mod b;
      While r <> 0 do
      Begin
       a:=b;
       b:=r;
       r:=a mod b;
      End;
    UCLN:=b;
    If mau div UCLN <> 1 then
      Writeln(f,' = ', a div UCLN,'/',b div UCLN)
         else Writeln(f,' = ',tu div UCLN);
    Close(f);
End.