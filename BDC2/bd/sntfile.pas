program sntfile;
var n,i,j,max,dem:longint;
    s:Array[1..1000] of longint;
    f:text;
begin
    Assign(f,'D:\kha\bd\in.txt');
    Reset(f);
    While not eof(f) do
    Readln(s[i]);
    Close(f);

    Assign(f,'D:\bd\out.txt');
    Rewrite(f);
    Write(f,'Cac so nto la: ');
    For i:=1 to s[i] do
    For j:=2 to s[i] div 2 do
    If s[i] mod j <> 0 then dem:=dem+1;
    If dem=0 then Write(f,s[i],'; ');
    Close(f);
End.