module half_adder_tb();
	reg a,b;
	wire sum,carry;

half_adder h1(.a(a),.b(b),.sum(sum),.carry(carry));

initial begin
	$dumpfile("out_ha.vcd");
	$dumpvars(0,half_adder_tb);



	a=1'b1;b=1'b0;#5;
	a=1'b1;b=1'b1;#5;
	$finish;
end
endmodule
