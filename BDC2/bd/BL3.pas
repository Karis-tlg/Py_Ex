Program sobimat;
Var s:string;
    f:text;
    i,n,z,t,x:longint;
Begin
    Assign(f,'D:\bd\B3IN.txt');
      Reset(f);
      Read(f,s);
      Close(f);

    Assign(f,'D:\bd\B3OUT.txt');
      Rewrite(f);
      For i:=1 to length(s) do
        Begin
          Val(s[i], n, z);
          If z=0 then t:=t+n;
        End;
      Write(f,t);
    Close(f);
End.