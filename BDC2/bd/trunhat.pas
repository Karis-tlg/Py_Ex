program trucnhat;
var i, a, s, b, r, BC, BCNN, uc:longint;
    f:text;
Begin
    Assign(f,'D:\bd\B1IN.txt');
      Reset(f);
      Read(f,a);
      Read(f,b);
    Close(f);

    Assign(f,'D:\bd\B1OUT.txt');
      Rewrite(f);
      BC:=a*b;
        while a <> b do
          if a > b then a:=a-b else b:=b-a;
            BCNN:=BC div a;
      write(f,BCNN);

      r:=a mod b;
      while r <> 0 do;
      begin
        a:=b;
        b:=r;
        r:=a mod b;
      end;
      uc:=b;
    Close(f);
End.

