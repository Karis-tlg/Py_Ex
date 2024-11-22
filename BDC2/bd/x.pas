program a;
uses crt;
var s,kq,kt,x:string;
    i,d:integer;
BEGIN
   Clrscr;
   S:='AAABBBBXXXXXYYYYKK';
   i:=1;
   While i <= length(s) do
      begin
         d:=0; kt:=s[i];
         While s[i] = kt do
            begin
               d:=d+1;
               i:=i+1;
            End;
         Str(d,x);
         if d=2 then kq:=kq+kt+kt else kq:=kq+x+kt;
      End;
   Write(kq);
   Readln;
End.
