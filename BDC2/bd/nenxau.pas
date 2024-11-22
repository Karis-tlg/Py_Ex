program nenxau;
var t, k, n: int64;
    i, dem: int64;
    f: text;
    x: int64;
    s:array[1..1000] of int64;

begin
    Assign(f,'D:\kha\bd\in.txt');
       Reset(f);
       Read(f,n);
    Close(f);

    Assign(f,'D:\kha\bd\out.txt');
       Rewrite(f);
	   n:=s;
       dem:=1;
        for i:=2 to length(s) do
		 begin
          if s[i]= s[i-1] then inc(dem);
          if (s[i] <> s[i-1]) then 
           begin
            str(dem,t);
             if dem > 1 then k:=k+t+s[i-1];
			  else k:=k+s[i-1];
		   end;	 
              if i=length(s) then
			  begin
			   str(dem,t);
			   if dem > 1 then k:=k+tam+s[i]
			    else k:=k+s[i];
           end;
		  end; 
        writeln(k);
end.




