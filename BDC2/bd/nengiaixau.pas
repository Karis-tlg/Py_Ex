program giainenxau;
var s:string;
    a, i, j:integer;
    f:text;
begin
    Assign(f,'D:\bd\in.txt');
      Reset(f);
      Readln(f,s);
    Close(f);

    Assign(f,'D:\bd\out.txt');
      for i:=1 to length(s) do
      if s[i] in ['2'..'9'] then
         begin
           val(s[i],a);
           for j:=2 to a do
           write(s[i+1]);
         end;
    else
 write(s[i]);
end.
