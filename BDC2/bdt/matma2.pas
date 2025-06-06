program MatMa;
uses crt;
var
  inputFile, outputFile: text;
  meDay, meMonth, meYear, baDay, baMonth, baYear, meSum, baSum, gcd, lcm: longint;

function GCD(a, b: longint): longint;
begin
  if b = 0 then
    GCD := a
  else
    GCD := GCD(b, a mod b);
end;

begin
  assign(inputFile, 'MATMA.INP');
  assign(outputFile, 'MATMA.OUT');
  reset(inputFile);
  readln(inputFile, meDay, meMonth, meYear);
  readln(inputFile, baDay, baMonth, baYear);
  close(inputFile);

  meSum := meDay + meMonth + meYear;
  baSum := baDay + baMonth + baYear;

  gcd := GCD(meSum, baSum);
  lcm := (meSum * baSum) div gcd;

  rewrite(outputFile);
  writeln(outputFile, 'Mat ma khoa xe l�: ', lcm);
  close(outputFile);
end.
