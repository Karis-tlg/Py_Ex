Program Day_So_Giam_Dan;
	Uses Crt;
	Var s,n,i,j,t:integer;
	a:array[1..20] of integer;
Begin
	Clrscr;
	Writeln(‘SAP XEP DAY SO:’);
	Write(‘Nhap so phan tu cua day n = ‘); Readln(n); 
	For i:=1 to n do
		Begin
			Write(‘a[‘,i,’]= ‘);
			Readln(a[i]);
		End;
	For i:=1 to n-1 do
	For j:=i+1 to n do
	If a[i]<a[j] then
		Begin
			t:=a[i];
			a[i]:=a[j];
			a[j]:=t;
		End;
	Writeln(' Day sau khi sap xep giam dan la:'); 
	For i:=1 to n do
	Write(a[i]:4); Readln;
	s:=0;
	For i:=1 to n do s:=s+a[i];
	Writeln('Gia tri trung binh la: ',s/n:6:2);
	Readln;
End.