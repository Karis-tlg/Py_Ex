program quamayman;
var d, i, j, n, k: longint;
    f: text;
    a:array[1..100] of integer;
begin
    Assign(f,'D:\kha\bdt\LUCKY.INP');
        Reset(f);
        Read(f,n,k);
        for i:=1 to n do
                begin
                        Read(f,a[i]);
                        for j:=1 to i-1 do
                        if abs(a[i]+a[j])=k then inc(d);
                end;
    Close(f);

    Assign(f,'D:\kha\bdt\LUCKY.OUT');
        Rewrite(f);
        Write(f,d);
    Close(f);
End.