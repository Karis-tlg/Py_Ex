program sntmax;
var n, i:longint;
    s:array[1..1000] of longint;
    f:text;

Function snt(x:int64):byte;
  var i:int64;
  begin
   if x <= 1 then snt:=0 else
    begin
     i:=2;