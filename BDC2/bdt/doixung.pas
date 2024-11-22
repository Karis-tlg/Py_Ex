program xaudoixung;
var i, n, t: int64;
    s: string;
    a: array[1..1000] of int64;
    f: text;
begin
    Assign(f,'D:\kha\bdt\in.txt');
        Reset(f);
        readln(f,t);
        for i:=1 to t do
        readln(f,s[t]);
    Close(f);

    Assign(f,'D:\kha\bdt\out.txt');
        Rewrite(f);

        for i:=length(s[t]) downto 1 do
        if

