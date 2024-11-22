Program vidu;
Var f:text;
    a:array[1..50] of integer;
    i,j,n,t:integer;
BEGIN
  n:=0;
  Assign(f,'D:\kha\bdtin\input.txt');
  Reset(f);
  {While not eof(f) do}
  readln(f,n);
  For i:=1 to n do
        {begin
           n:=n+1;}
           Readln(f,a[i]);
       { end;}
  close(f);
  For i:=1 to n-1 do
        for j:=i+1 to n do
           if a[i]<a[j] then
               begin
                 t:=a[i];
                 a[i]:=a[j];
                 a[j]:=t;
               end;
  Assign(f,'D:\kha\bdtin\output.txt');
  Rewrite(f);
  For i:=1 to 6 do Writeln(f,a[i]);
  close(f);
END.