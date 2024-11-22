program muahang;
var
  n, i, min, m: longint;
  f: text;
begin
  assign(f, 'D:\kha\bdt\BUY.INP');
        reset(f);
        readln(f, n);
        min := MaxInt;
		for i := 1 to n do
		begin
			read(f, m);
			if m < min then
			min := m;
		end;
  close(f);

  assign(f, 'D:\kha\bdt\BUY.OUT');
        rewrite(f);
        writeln(f, min);
  close(f);
end.



