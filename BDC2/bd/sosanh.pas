program sosanh;
uses crt;
var s:Array[1..1000] of int64;
    i,n,t,j,min,max:longint;
BEGIN
    clrscr;
    write('Nhap so phan tu mang: ');readln(n);
        for i:=1 to n do
    begin
        write('Nhap so thu ',i,': ');readln(s[i]);
    end;
        for i:=1 to n-1 do
          for j:=i+1 to n do
            if s[i] > s[j] then
       begin
           t:=s[i];
           s[i]:=s[j];
           s[j]:=t;
       end;
       write('Day so duoc sap xep nhu sau: ');
       for i:=1 to n do write(s[i],', ');
         for i:= 1 to n do
         min:=s[i];
         if s[i] > s[j] then min:=s[j];
          write('So be nhat la: ',min);
readln;
end.