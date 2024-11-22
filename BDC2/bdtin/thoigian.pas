program thoigian;
var gio, phut, giay, x: longint;
    f:text;
begin
    assign(f,'D:\bd\intime.txt');
     reset(f);
       read(f,gio,phut);
       readln(f,giay);
       readln(f,x);
    close(f);

    assign(f,'D:\bd\outtime.txt');
     rewrite(f);
      gio:=gio + x div 3600;
      x:=x mod 3600;
      phut:=phut + x div 60;
      giay:= giay + x mod phut;
    close(f);
    write(f,'Gio: ',gio,', Phut: ',phut,', Giay: ',giay);
end.
