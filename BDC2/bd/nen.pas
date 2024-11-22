program nengiaixau;
var s,kq,kt,x:string;
    i,d,c,a,j:integer;
    f:text;
BEGIN
   Assign(f,'D:\bd\B3IN.txt');
     Reset(f);
     Readln(f,s);
   Close(f);

   Assign(f,'D:\bd\B3OUT.txt');
     Rewrite(f);
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

        for i:=1 to length(s) do
         if s[i] in ['2'..'9'] then
       begin
         val (s[i],d,c);
         if
         write(s[i+1]);
       end;

      Writeln(f,kq);

   Close(f);
End.