program sodoixung;
var i:longint;
    s, n:string;
    f:text;
begin
        Assign(f,'D;\kha\bd\in.txt');
          Reset(f);
          Read(f,s);

        Close(f);

        Assign(f,'D:\kha\bd\out.txt');
          Rewrite(f);
          for i:= (length(s)) downto 1 do
          n:=n+s[i];
          if (n=s) then write(f,'Xau doi xung')
                else writeln(f,'Xau khong doi xung');
        Close(f);
end.