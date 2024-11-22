program mk;
var i,n,c: longint;
    f: text;
    s,s2,s1:string;
Begin
     Assign(f,'D:\bd\MK.INP');
        Reset(f);
        Readln(f,s);
     Close(f);
     S2:='02468';
     Assign(f,'D:\bd\MK.OUT');
        Rewrite(f);
        For i:=1 to length(s) do if pos(s[i],s2) <> 0 then S1:=S1+S[i];
         {begin
           val(s[i],n,c);
           if (c = 0) and (n mod 2 = 0) then  S1:=S1+S[i];
         end;}
        Write(f,S1);
        For i:=length(s1) downto 1 do write(f,s1[i]);
     Close(f);
End.
