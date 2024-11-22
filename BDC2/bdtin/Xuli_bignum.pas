
Const
   digit=8;
   maxN=301;
   base=100000000;
 
 
Type
   BigNum=array[0..maxN] of Int64;
   ll=LongInt;
 
Var
   s1,s2,Res  : AnsiString;
   a1,a2      : BigNum;
   ex         : boolean;
 
 
Function max(a,b:Int64):Int64;
Begin
   if a>b then max:=a else max:=b;
End;
 
 
Procedure CoverBigNum(s:AnsiString;var a:BigNum);
Var
   sn,i,j: ll;
Begin
   Fillchar(a,sizeof(a),0);
   If s='0' then exit;
   sn:=(length(s)+digit-1) div digit;
   While length(s)<sn*digit do s:='0'+s;
   j:=length(s);
   a[0]:=sn;
   For i:=1 to sn do
      begin
         val(copy(s,j-digit+1,digit),a[i]);
         j:=j-digit;
      end;
End;
 
 
Procedure CoverNumBer(a:BigNum; Var Res: AnsiString);
Var
   s:AnsiString;
   i:ll;
Begin
   If a[0]=0 then
      begin
         res:='0';
         exit;
      end;
   res:='';
   For i:=1 to a[0] do
      begin
         str(a[i],s);
         while length(s)<digit do s:='0'+s;
         res:=s+res;
      end;
   While res[1]='0' do delete(res,1,1);
End;
 
 
Operator =(a,b: BigNum)bang: Boolean;
Var
   x,y: AnsiString;
Begin
   CoverNumBer(a,x);
   CoverNumBer(b,y);
   exit(x=y);
End;
 
 
Operator +(var a,b:BigNum)cong:BigNum;
Var
   i      :ll;
   num,nho:Int64;
Begin
   If (a[0]=0) or (b[0]=0) then
      begin
         If a[0]=0 then cong:=b
         else cong:=a;
         exit;
      end;
   cong[0]:=max(a[0],b[0]);
   nho:=0;
   For i:=1 to cong[0] do
      begin
         num:=a[i]+b[i]+nho;
         cong[i]:=num mod base;
         nho:=num div base;
      end;
   If nho>0 then
      begin
         Inc(cong[0]);
         cong[cong[0]]:=nho;
      end;
End;
 
 
Operator -(a,b:BigNum)tru:BigNum;
Var
   tmp: BigNum;
   i  :ll;
   num,nho:Int64;
Begin
   If a=b then
     begin
        FillChar(tru,SizeOf(tru),0);
        exit;
     end;
   If ex then
      begin
         tmp:=a;
         a:=b;
         b:=tmp;
      end;
   tru[0]:=max(a[0],b[0]);
   nho:=0;
   For i:=1 to tru[0] do
      begin
         num:=a[i]-b[i]-nho;
         If num<0 then
            begin
               nho:=1;
               num:=num+base;
            end
         else nho:=0;
         tru[i]:=num mod base;
      end;
End;
 
 
Operator *(a,b:BigNum)nhan:BigNum;
Var
   i,j:ll;
   x, nho:Int64;
   S: AnsiString;
Begin
   Fillchar(nhan,sizeof(nhan),0);
   If (a[0]=0) or (b[0]=0) then exit;
   nhan[0]:=a[0]+b[0]-1;
   For i:=1 to a[0] do
      For j:=1 to b[0] do
         nhan[i+j-1]:=nhan[i+j-1]+a[i]*b[j];
   nho:=0;
   For i:=1 to nhan[0] do
      begin
         x:=nhan[i]+nho;
         nho:=x div base;
         nhan[i]:=x mod base;
      end;
   If nho>0 then
      begin
         inc(nhan[0]);
         nhan[nhan[0]]:=nho;
      end;
End;
 
 
Procedure Enter;
Begin
  ReadLn(s1);
  ReadLn(s2);
  ex:=(length(s1)<length(s2)) or ((length(s1)=length(s2)) and (s1<s2));
End;
 
 
Procedure Main;
Var
   x:BigNum;
Begin
   CoverBigNum(s1,a1);
   CoverBigNum(s2,a2);
   CoverNumBer(a1+a2,Res);
   WriteLn(Res);
   CoverNumBer(a1-a2,Res);
   If ex then Write('-');
   WriteLn(Res);
   CoverNumBer(a1*a2,Res);
   WriteLn(Res);
End;
 
 
BEGIN
   Enter;
   Main;
END.