program fileminmax;
var f:text;
    min, max, n, t, i:longint;
    s:array[1..1000] of longint;

function ucln(a,b:int64): int64;
  var r: integer;
  begin
      repeat
        r:=a mod b;
        a:=b;
        b:=r;
      until r=0;
      ucln:=a;
  end;
begin
      assign(f,'D:\bd\input.txt');
      reset(f);
      n:=0;
      while not eof(f) do
         begin
            n:=n+1;
            readln(f,s[n]);
         end;
      close(f);
     assign(f,'D:\bd\output.txt');
     rewrite(f);
     max:=s[1];
     min:=s[1];
     for i:=1 to n do
        BEGIN
          if s[i] < min then min:=s[i];
          if s[i] > max then max:=s[i];
        End;
     writeln(f,'So be nhat la: ',min);
     writeln(f,'So lon nhat la: ',max);
     Writeln(f,'UCLN cua ',min,', ',max,' la: ',ucln(min,max));
     close(f);
end.

