program sohanhphuc;
var i, n, j, t, d, i1, j1, j2, i2, sum:longint;
    f:text;
    a, b, c:array[1..100] of longint;
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
        for i := n downto 1 do
        begin
            if n mod i = 0 then
            begin
                i1:=i1+1;
                a[i1]:=i;
            end;
        end;
	for j := n downto 2 do
	     begin
		        t := 0;
                        for d:=2 to j-1 do
                        if j mod d = 0 then
                        t:=1;
                        if t = 0 then
                        begin
                             j1:=j1+1;
                             b[j1]:=j;
                        end;
	     end;
        for i2 :=1 to i1 do
                Begin
                If a[i1] > b[j1] then write(f,a[i1],' ') else write(f,b[j1],' ');
                i1:=i1-1; j1:=j1-1;
                End;
    close(f);
end.