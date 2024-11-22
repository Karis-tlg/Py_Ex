program ktrsnt;
var i, n, j: longint;
begin
     write('nhap n: ');readln(n);
     for i:=1 to n do
     begin
        if ((n mod i) = 0) and ((n mod 1) = n) then writeln(n,' ');
     end;
end.
