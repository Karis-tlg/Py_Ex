program khachsan;
var
  m, n, i, j, count: integer;
  k, x: array[1..100] of integer;
  room: array[1..50] of boolean;
begin
  // M? file input v� output
  assign(input, 'D:\kha\bdt\HOTEL.INP');
  assign(output, 'D:\kha\bdt\HOTEL.OUT');
  reset(input);
  rewrite(output);

  // D?c d? li?u d?u v�o
  readln(m, n);
  for i := 1 to m do
    read(k[i]);
  for i := 1 to n do
  begin
    x[i] := 1;
    for j := 1 to m do
    begin
      read(x[(i-1)*m+j]);
      x[i] := x[i] * x[(i-1)*m+j];
    end;
  end;

  // Ki?m tra t?ng ph�ng
  count := 0;
  for i := 1 to n do
  begin
    if x[i] mod k[1] = 0 then // N?u t�ch day s? trong ph�ng chia h?t cho k1
    begin
      for j := 2 to m do
      begin
        if x[i] mod k[j] <> 0 then // N?u t�ch day s? trong ph�ng kh�ng chia h?t cho ki
          break;
        if j = m then // N?u da ki?m tra h?t c�c gi� tr? c?a k
        begin
          count := count + 1;
          room[i] := true;
        end;
      end;
    end;
  end;

  // Ghi k?t qu? v�o file output
  writeln(count);
  for i := 1 to n do
  begin
    if room[i] then
      write(i, ' ');
  end;

  // D�ng file input v� output
  close(input);
  close(output);
end.