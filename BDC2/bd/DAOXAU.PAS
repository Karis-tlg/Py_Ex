uses crt;
var st:string;kq:string;
    i,j,vt,d:integer;
    a:array[1..10] of string;
procedure daoxau;
begin
     st:=' '+st;  d:=1; kq:='';
     vt:=length(st);
     for i:=length(st) downto 1 do
     if (st[i]<>' ') and (st[i-1]=' ') then
     begin
          a[d]:=copy(st,i,vt-i+1);
          d:=d+1;
          vt:=vt-(vt-i+1)-1;
     end;
     for i:=1 to d-1 do
     kq:=kq+a[i]+' ';
     writeln (kq);
end;
    begin
         clrscr;
         write ('Nhap xau: ');readln (st);
         write ('Xau dao la: ');
         daoxau;
         readln
    end.