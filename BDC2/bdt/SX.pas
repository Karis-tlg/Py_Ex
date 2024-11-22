program sx;
var t, i, j, n, x: longint;
    f: text;
    a: array[1..1000] of longint;
Begin
    Assign(f,'D:\bd\SX.INP');
        Reset(f);
        Readln(f, x);
        n:=0;
        For i:=1 to x do
        Begin
          n:=n+1;
          Read(f,a[n]);
        End;
    Close(f);

    Assign(f,'D:\bd\SX.OUT');
        Rewrite(f);
        For i:=1 to n-1 do
        For j:=i+1 to n do
           If a[i] > a[j] then
              Begin
                  t:=a[i];
                  a[i]:=a[j];
                  a[j]:=t;
              End;
              for i:=1 to n do Write(f,a[i],' ');
    Close(f);
End.

