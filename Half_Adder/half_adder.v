module half_adder (a,b,sum,carry);
	input a,b;
	output sum,carry;

	assign {carry,sum}=a+b;

endmodule
