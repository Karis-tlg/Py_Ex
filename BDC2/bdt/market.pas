program Market;

var
  n, M, i, j, max_value, max: integer;
  W, V: array[1..100] of integer;
  F: array[0..100, 0..100] of integer;
  f_in, f_out: text;

begin
  assign(f_in, 'D:\kha\bdt\MARKET.INP');
  reset(f_in);
  readln(f_in, n, M);
  for i := 1 to n do
    readln(f_in, W[i], V[i]);
  close(f_in);

  for i := 1 to n do
    for j := 0 to M do
      begin
        if W[i] > j then
          F[i,j] := F[i-1,j]
        else
          F[i,j] := max(F[i-1,j], F[i-1,j-W[i]] + V[i]);
        if F[i,j] > max_value then
          max_value := F[i,j];
      end;

  assign(f_out, 'D:\kha\bdt\MARKET.OUT');
  rewrite(f_out);
  if max_value = 0 then
    writeln(f_out, '-1')
  else
    writeln(f_out, max_value);
  close(f_out);
end.