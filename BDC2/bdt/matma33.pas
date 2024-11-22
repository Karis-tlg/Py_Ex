program MatMa;
uses crt;
var
  inputFile, outputFile: text;
  meDay, meMonth, meYear, baDay, baMonth, baYear, meSum, baSum, gcb, lcm: longint;

function GCD(a, b: longint): longint;
begin
  if b = 0 then
    GCD := a
  else
    GCD := GCD(b, a mod b);
end;

begin
  assign(inputFile, 'D:\kha\bdt\in.txt');
  assign(outputFile, 'D:\kha\bdt\out.txt');
  reset(inputFile);
  readln(inputFile, meDay, meMonth, meYear);
  readln(inputFile, baDay, baMonth, baYear);
  close(inputFile);

  meSum := meDay + meMonth + meYear;
  baSum := baDay + baMonth + baYear;

  gcb := GCD(meSum, baSum);
  lcm := (meSum * baSum) div gcb;

  rewrite(outputFile);
  writeln(outputFile, 'Mat ma khoa xe l…: ', lcm);
  close(outputFile);
end.
