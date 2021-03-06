
{{{id=2|
B = matrix(QQ,[[2,0],[0,1],[1,0]]);
///
}}}

{{{id=5|
A = matrix(QQ, [[ 1,2,0],
                [ 0,1,0],
                [ 0,0,1]])
///
}}}

{{{id=6|
A.eigenvectors_right()
///
[(0, [
  (0, 0, 1)
  ], 1), (1, [
  (1, 0, 1)
  ], 2)]
}}}

{{{id=7|
B*transpose(matrix([1,0]))
///
[2]
[0]
[1]
}}}

{{{id=8|
Qh=matrix([[1/sqrt(2), 1/sqrt(3)],
            [        0, 1/sqrt(3)],
            [1/sqrt(2),-1/sqrt(3)]]);

Q=matrix([[1/sqrt(2), 1/sqrt(3),1/sqrt(6)],
            [        0, 1/sqrt(3),2/sqrt(6)],
            [1/sqrt(2),-1/sqrt(3),1/sqrt(6)]]);     
Rh=matrix([[sqrt(2), sqrt(2)],
            [       0, sqrt(3)]]);   
R=matrix([[sqrt(2), sqrt(2)],
            [       0, sqrt(3)],
            [0, 0]]);
///
}}}

{{{id=10|
Qh*Rh
///
[1 2]
[0 1]
[1 0]
}}}

{{{id=11|
Q*R
///
[1 2]
[0 1]
[1 0]
}}}

{{{id=15|
c = (transpose(Qh)*b)
x1 = Rh.solve_right(c)
x1
///
(-1/6, 2/3)
}}}

{{{id=12|
b=vector([1,1,0])
A.solve_right(b)
///
(-1, 1, 0)
}}}

{{{id=17|
N1 = Rh*x1 - transpose(Qh)*b
///
}}}

{{{id=18|
N2 = B*x1 - b
///
}}}

{{{id=14|
N1.norm(2)
///
0
}}}

{{{id=16|
N2.norm(2)*1.0
///
0.500000000000000*sqrt(23/3)
}}}

{{{id=19|
var('y , t')
///
(y, t)
}}}

{{{id=20|
expand((y^2 + y +2)*t^3)
///
t^3*y^2 + t^3*y + 2*t^3
}}}

{{{id=21|
numerical_approx(N2.norm(2), digits=100)
///
1.384437310486345808764043790817915335038702374825942629905364728172930838903858595644566418038726175
}}}

{{{id=22|
numerical_approx(sqrt(3), digits=100)
///
1.732050807568877293527446341505872366942805253810380628055806979451933016908800037081146186757248576
}}}

{{{id=23|
$r_{\theta+\mathbb{R}}$
///
}}}

{{{id=24|

///
}}}