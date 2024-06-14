//procedure choxebuyt;
const fi='BUS.INP';
        FO='BUS.OUT';
var     a:array[0..1000] of longint;
        i,n,t,d,q,w:longint;
        f:text;
procedure nhap;
begin
        assign(f,fi);reset(F);
        readln(f,n,d,t);
        for i:=1 to n do read(f,a[i]);
        closE(f);
end;
BEGIN
        nhap;
        assign(f,fo);rewrite(F);
        for i:=1 to n do
                if a[i]<=t then write(f,1,' ')
                else
                    begin
                        a[i]:=a[i]-t;
                        q:=a[i] div d;
                        w:=a[i] mod d;
                        if w=0 then write(f,q+1,' ')
                        else write(f,q+2,' ');
                    end;
        close(F);
END.
