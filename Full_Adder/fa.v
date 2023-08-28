module half_adder(a,b,sum,carry);
	input a,b;
        output sum,carry;

        assign {carry,sum}=a+b;

endmodule



module fa(x,y,cin,s,cout);
	input x,y,cin;
	output cout,s;
	wire w1,w2,w3;

	half_adder h1(x,y,w1,w2);
	half_adder h2(w1,cin,s,w3);
	or o1(cout,w2,w3);
endmodule
