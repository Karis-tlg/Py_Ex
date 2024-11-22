program ktdx;
var i, n, j, d:longint;
    f:text;
    s,t:string;
const fi= 'in.txt';
      fo = 'out.txt';
begin
    assign(f,fi);
        reset(f);
        readln(f,s);
        readln(f,t);
    close(f);

    assign(f,fo);
        rewrite(f);
        d:=0;
        n:=length(s);
        if length(s) = length(t) then
        begin
            for i:=1 to n do
                 begin
                      j:=n-i+1;
                      if (s[i]=t[j]) and (i+j-1=n) then inc(d);
                 end;
        end;
        if d=0 then write(f,'-1') else write(f,d);
    close(f);
end.
