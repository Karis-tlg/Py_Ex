Program viduham;
uses crt;
Var n:int64;

Function snt(x:int64):byte;
   var i:int64;
   Begin
      if x <=1 then snt:=0
      else
      begin
        i:=2;
        while x mod i <> 0 do i:=i+1;
        if i = x then snt:=1 else snt:=0;
      end;
   End;

Function scp(x:int64):byte;
   Begin
      if sqrt(x) = int(sqrt(x)) then scp:=1 else scp:=0;
   End;

Function shh(x:int64):byte;
   var i,t:longint;
   Begin
   t:=0;
   for i:=1 to (x div 2) do
     if x mod i = 0 then t:=t+i;
     if t = x then shh:=1 else shh:=0;
   End;


BEGIN
        Clrscr;
        Write('Nhap so can kiem tra: '); Readln(n);
        if snt(n)=1 then Writeln(n,' la so nguyen to') else Writeln(n,' khong phai so nguyen to');
        if scp(n)=1 then Writeln(n,' la so chinh phuong') else Writeln(n,' khong phai so chinh phuong');
        if shh(n)=1 then Writeln(n,' la so hoan hao') else Writeln(n,' khong phai la so hoan hao');
        Readln;
END.
