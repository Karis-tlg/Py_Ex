
//uses   Crt;
var     i,j,count, n,k:int64;
     f,g:text;

BEGIN
assign(f,'TONGLP.inp');reset(f);
assign(g,'TONGLP.out');rewrite(g);
 readln(f,N);
   // write('Nh?p N = '); Readln(N);
    count:= 0;
    i   	:= 1;
    j   	:= 1;
    while (j*j*j+1<N) do Inc(j);
    repeat
        k :=i*i*i+j*j*j;
        if k=N then begin
             Inc(count);
             Write(g, i,' ',j); Inc(i) ; Dec(j);
        end;
        if k < N then Inc(i);
        if k > N then Dec(j);
    until i >j;
    writeln(g);
    writeln(g,count );
    close(f); close(g);
    //readln
END.
