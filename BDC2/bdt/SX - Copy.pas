program sx;
var t, i, j, n, x: longint;
    f: text;
    a: array[1..1000] of longint;
Begin
    Assign(f,'D:\bd\SX.INP');
        Reset(f);
        Readln(f,x);
        For i:=n to x do
        Begin
          Readln(f,a[n]);
          n:=n+1;
        End;
    Close(f);

    Assign(f,'D:\bd\SX.OUT');
        Rewrite(f);
        For i:=1 to n-1 do
        For j:=1 to n do
           If a[i] < a[j] then
              Begin
                  t:=a[i];
                  a[i]:=a[j];
                  a[j]:=t;
              End;
    Close(f);
End.

