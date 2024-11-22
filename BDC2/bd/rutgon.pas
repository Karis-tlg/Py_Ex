Program rgps;
Var mau,tu,ucln,a,b,r:longint;
    f:text;
Begin
        Assign(f,'D:\bd\in.txt');
          Reset(f);
          Read(f,tu);
          Read(f,mau);
        Close(f);

        Assign(f,'D:\bd\out.txt);
          Rewrite(f);
          Write(f,tu,'/',mau);
            a:=tu;
            b:=mau;
            r:=a mod b;
          While r<>0 do
            Begin
             a:=b;
             b:=r;
             r:=a mod b;
            End;
              u:=b;
              t:=t div u;
              m:=m div u;
                If m div u <> 0 then Writeln(f,' = ',t,'/',m)
                  Else Writeln(f,' = ',t);
        Close(f);
End.

