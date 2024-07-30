const   fi='LUCKY.INP';
        fo='LUCKY.OUT';
var
        A:array[0..9] of longint;
        dem,N:longint;
        M:string;
        f:text;
function       lucky(S:string):byte;
    var i,T:longint;St:string;
    begin
        while length(S)>1 do
            begin
                T:=0; st:='';
                for i:=1 to length(S) do T:=T+ord(S[i])-48;
                str(T,St);
                S:=St;
            end;
        lucky:=ord(S[1])-48;
    end;
procedure       input;
    var i,x:longint;
    begin
        assign(f,fi);   reset(f);
        readln(f,N);
        for i:=1 to N do
             begin
                 readln(f,M);
                 inc(A[lucky(M)]);
             end;
    end;
procedure       output;
    var i,vt:byte; max:longint;
    begin
        assign(f,fo); rewrite(f);
        max:=0;
        for i:=0 to 9 do
            if max<A[i] then begin max:=a[i];vt:=i;end;
        writeln(f,vt);
        close(f);
    end;
begin
    input;
    output;
end.
