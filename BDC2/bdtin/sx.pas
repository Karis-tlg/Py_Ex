program sx;
uses crt;
var s:array[1..1000] of int64;
    i,n,t,j,max,min:longint;
begin
    clrscr;
    write('So phan tu mang: ');readln(n);
    for i:= 1 to n do
       begin
       write('Nhap so thu ',i,': ');readln(s[i]);
       end;
       for i:=1 to n do
       for j:=i+1 to n do
       if s[i] > s[j] then
       begin
        t:=s[i];
        s[i]:=s[j];
        s[j]:=t;
       end;


       max:=0;
       min:=0;
       For i:=1 to n do
       begin
       If max < s[i] then max := s[i];
       If min > s[j] then min := s[j];
       End;
       writeln('Gia tri lon nhat la: ',max);
       writeln('Gia tri be nhat la: ',min);

                                {write('Day so duoc sap xep tu be den lon la: ');
                                for i:=1 to n do write(s[i],', ');}
readln
end.