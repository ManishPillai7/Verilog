module fa_tb();
	reg x,y,cin;
	wire s,cout;

	fa f1(.x(x),.y(y),.cin(cin),.s(s),.cout(cout));

	initial begin
		$dumpfile("wave_fa.vcd");
		$dumpvars(0,fa_tb);

		x=1'b1;y=1'b1;cin=1'b1;#5;
		x=1'b0;y=1'b0;cin=1'b1;#5;
	end
endmodule	
