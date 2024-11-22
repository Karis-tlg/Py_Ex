Program rgps;
Var mau,tu,ucln,a,b,r:longint;
    f:text;
Begin
        Assign(f,'D:\bd\in.txt');
          Reset(f);
          Read(f,tu);
          Read(f,mau);
        Close(f);

        Assign(f,'D:\bd\out.txt');
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
              ucln:=b;
              tu:=tu div ucln;
              mau:=mau div ucln;
                If mau div ucln <> 0 then Writeln(f,' = ',tu,'/',mau)
                  Else Writeln(f,' = ',tu);
        Close(f);
End.