program somayman;

var
  n, i, j, tong, tong1, tong2: longint;
  dem: array[0..9] of longint;
  f: text;

begin
  assign(f, 'LUCKY.INP');
  reset(f);
  readln(f, n);
  for i := 0 to 9 do
    dem[i] := 0;
  tong1 := 0;
  tong2 := -1;
  for i := 1 to n do
  begin
    readln(f, j);
    tong := 0;
    while j > 0 do
    begin
      tong := tong + j mod 10;
      j := j div 10;
    end;
    Inc(dem[tong]);
    if dem[tong] > tong1 then
    begin
      tong1 := dem[tong];
      tong2 := tong;
    end
    else if (dem[tong] = tong1) and (tong < tong2) then
    begin
      tong2 := tong;
    end;
  end;
  close(f);

  assign(f, 'PTICH.OUT');
  rewrite(f);
  writeln(f, tong2);
  close(f);
end.
