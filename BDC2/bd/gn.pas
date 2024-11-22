program giainen;
uses crt;
var s,kq,kt,x:string;
    i,d,c,j:integer;
BEGIN
   Clrscr;
   S:='3A4B5X4YKK';
   i:=1;
   While i <= length(s) do
      begin
        val(s[i],d,c);
        if c=0 then
          for j:=1 to d do kq:=kq+s[i+1]
        else kq:=kq+s[i]+s[i+1];
        i:=i+2;
      End;
   Write(kq);
   Readln;
End.
