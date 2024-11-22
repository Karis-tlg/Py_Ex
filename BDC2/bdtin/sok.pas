const fi='sok.inp';
      fo='sok.out';
var f1,f2:text;n,k,a2,a1:qword;i,j:longint; st1,st:string;
a,b:array[-1000000..1000000] of longint;
    function chx(st:string):string;
    begin
    while st[1]=' ' do delete(st,1,1);
    while st[length(st)]=' ' do delete(st,length(st),1);
    while pos('  ',st)>0 do delete(st,pos('  ',st),1);
    chx:=st;
    end;
       procedure sort(l,r: longint);
      var
         i,j,x,y: longint;
      begin
         i:=l;
         j:=r;
         x:=a[(l+r) div 2];
         repeat
           while a[i]>x do
            inc(i);
           while x>a[j] do
            dec(j);
           if not(i>j) then
             begin
                y:=a[i];
                a[i]:=a[j];
                a[j]:=y;
                inc(i);
                j:=j-1;
             end;
         until i>j;
         if l<j then
           sort(l,j);
         if i<r then
           sort(i,r);
      end;
begin
assign(f1,fi);
reset(f1);
readln(f1,n,k);st:='';
        for i:=1 to n do
        begin
        read(f1,a[i]);
        str(a[i],st1);
        repeat
        delete(st,pos(st1,st),length(st1));
        until pos(st1,st)=0;
        st:=st+' '+st1;
        end;
close(f1);
assign(f2,fo);
rewrite(f2);
j:=0;a2:=0;
for i:=1 to length(st) do
        begin
        if st[i]=#32 then
                begin
                inc(j);
                a[j]:=0;
                end;
        if st[i] in ['0'..'9'] then
                begin
                val(st[i],a2);
                a[j]:=a[j]*10+a2;
                end;
        end;
sort(1,j);
write(f2,a[k]);
close(f2);
end.
