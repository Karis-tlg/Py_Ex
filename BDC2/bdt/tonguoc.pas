program tonguoc;
var i, n, t: longint;
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
        for i:=1 to n do
        begin
            if n mod i = 0 then t:=t+i;
        end;
        writeln(f,t);
    close(f);
end.