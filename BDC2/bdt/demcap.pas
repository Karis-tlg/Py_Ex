program demcap;
var i, n, j, t: longint;
    f: text;
const fi = 'in.txt';
      fo = 'out.txt';
begin
    assign(f,fi);
        reset(f);
        readln(f,n);
    close(f);

    assign(f,fo);
        rewrite(f);
        t:=0;
        for i:=n-1 downto 1 do
        begin
            j:=n-i;
            if i>j then inc(t);
        end;
        if t=0 then write(f,'-1') else write(f,t);
    close(f);
end.