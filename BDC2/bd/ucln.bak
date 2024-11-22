Program UC_LN;
Uses CRT;
Var m,n:Int64;

Function UCLN(a,b:int64):int64;
   Var r:int64;
   Begin
       repeat
           r:=a mod b;
           a:=b;
           b:=r;
       until r=0;
       ucln:=a;
   End;

Begin
    Clrscr;
    Write('Nhap tu so, mau so: '); Readln(m,n);
    Writeln('UCLN(',m,',',n,') = ', UCLN(m,n));
    Writeln(m,'/',n,' = ',m div UCLN(m,n),'/', n div UCLN(m,n));
    readln;
End.