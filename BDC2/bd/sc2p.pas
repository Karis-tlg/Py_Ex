Program scp;
uses crt;
var n,i:longint;
Begin
        Clrscr;
        Write('n = '); Readln(n);
        If sqrt(n)=int(sqrt(n)) then Writeln(n,' la so chinh phuong vi ',n,' = ',sqrt(n):0:0,'^2')
        Else Writeln(n,' khong phai la so chinh phuong');
        Readln;
End.
