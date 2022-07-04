# Math
enc(m, p) = big_ran() * p + 2 * small_rand() + m

dec(ct, p) = (ct % p) % 2


**Elliptic-curve cryptography (ECC)**
one-way function
Ex: multiple is easy, divide is hard

Why do it in elliptic-curve surface?
security equivalent to classical systems (like RSA)
more difficult/secure compute than normal 2D coordinate

EX: y^2 = x^3 - 2x + 15
1. imagine 2D Integer coordinate fold on donut (mod fold plane back to itself, there for 2D plan have [x, y] range that is limited)
2. draw a elliptic-curve line on donut, as cure hit edge curve line will cutoff(won't loop around)
3. pick a random points on curve-line as The Generator Point, G;
4. New Math here
   1. Negative Operation = Flip across y axis
   2. Addition Operation = draw a line hits 2 points, should have 3rd point hit curve, then take Negative of new point
   3. Point Double = Addition Operation, use tangle line(Key shortcut)
   4. Special Case: 2 points parallel to x or y axis, when addition = infinty point
   5. Special Case: infinty point + point = itself
   6. Scalar Multiplication = reapt Addition Operation on itself
   7. Any Operation can chain together just like algebra operation 13G = 8G + 4G + G
5. Any Generator Point with Addition Operation will creates a limited set points (group structure)



**Sign message**
digest value (z) same bit size order of curve
modular arithmetic, order of curve as modulus
1. pick a random number k, then calculate K = Generator * k, K's x value = r uses for verfication
2. then calculate k^-1

z = 10 digest value, 1 < z < N, hash of message?
k = 19 random number, must  
a = 3 private key
r = 9 (Generator * k's x axis)
N = 23 (order of curve)
s = k^-1(z + ra) % N

(r, s) = signed

Share secrets = prive_key * other_public_key = private_A * public_B = private_B * public_A

**Verification**
w = s^-1 % N (s from signature)
u1 = zw % N (z is from message)
u2 = rw % N (r is from signature)
S = u1G + u2A (A is sender's public key)
(S's x value should match r from message)

> if k is same, r will always be same

RLP (Recurrsive Length Prefix) generate z from message
SSZ (Simple serialize) Eth 2 generate z from message


**Hormophic Hidden/Encryption, create any struct set that only have mulplicatetion and addation operator


# ZK Snark


Byzantine-Fault Tolerate(BFT) POS

best fault torlerat n = 3f + 1

tendermint - most mature BFT algorithm

Kilian 92, micali 94,
  > bad prover time
GGPR 13, Groth16
  > trusted steup
Sonic 19, Marlin 19
Dark 19, Halo 19, STARK

DSL Program // Compiler to compile into circuit
- Circom
- ZoKrates
- Leo
- Zinc
- Cairo
- Snarky



Inifinty Point is 0, therefore M_point + Inifinty = M_point
All group structure will eventually hit Inifinty Point, then back to itself.

# Resource
Ariel Gabizon - https://www.youtube.com/watch?v=yNS_ttTj1KE&t=2952s

- Explaining SNARKs Part I: Homomorphic Hidings
- Explaining SNARKs Part II: Blind Evaluation of Polynomials
- Explaining SNARKs Part III: The Knowledge of Coefficient Test and Assumption
- Explaining SNARKs Part IV: How to make Blind Evaluation of Polynomials Verifiable
- Explaining SNARKs Part V: From Computations to Polynomials
- Explaining SNARKs Part VI: The Pinocchio Protocol
- Explaining SNARKs Part VII: Pairings of Elliptic Curves

Homomorphic Hidings invited by Diffie Hellman
Alice prove y = g^x
Alice send bob t = g^v

c is bob's random number
r = v - cx
bob checks t = g^r * y^c
because 
  g^r * y^c
= g^(v - cx) * g^(x * c)
= g^v
= t


FAQ:
- What is ZK Snark?
> Proof of computation

- Why/How polynomial convert to linear algebra?
> watch this https://www.youtube.com/watch?v=SzZaQnzstfE

Terry's bad answer:
Think of simple problem has only L + R = O; so polynomial L + R - O = 0 must be linearly dependent vectors;

t1(1 - x) + t2(1 + x) + t3(x^2) = 0
t1 - t1(x) + t2 + t2(x) + t3(x^2) = 0
(t1 + t2) + (t2 - t1)x + t3(x^2) = 0

t1 + t2 = 0
t2 + t1 = 0
t3 = 0

t1 t2 t3
(1  1 0)(t1) = 0
(-1 1 0)(t2) = 0
(0  0 1)(t3) = 0

(there is a none_zero sccaler) such that summation of vectors with none_zero scaler will equal to orgin point

0. Setup Phase
```
t.G
t'.G = t.G.λ

```
1. Generated each step effect to finial result
> Think of we check consistance of calculation path to result, instead of result itself
2. convert each step as vector mulpication (R1CS)
```
##Problem statement to R1CS (Rank 1 Constraint system) force addation to vector muliplication
x^3 + x + 5 = 35

a = x * x // x^2          Step 1
b = a * x // x^3          Step 2
c = b + x // x^3 + x      Step 3
d = c + 5 // x^3 + x + 5  Step 4

QAP(Quadratic arithmetic program)
// 6 variable, 4 gates
Witness vector: S
S = [1, x, a, b, c, d] // the path of solution, relations between steps
x = [1, 3, 9, 27, 30, 35] // the real steps to solution 
L(S) * R(S) = O   U(S) * V(S) = W(S) 多维商量

Step 1: L1(S) * R1(S) = x * x
L1 = [0, 1, 0, 0, 0, 0] // a(s) = 3
R1 = [0, 1, 0, 0, 0, 0] // b(s) = 3
O1 = [0, 0, 1, 0, 0, 0] // c(s) = 9

Step 2: L2(S) * R2(S) = a * x
L2 = [0, 0, 1, 0, 0, 0]
R2 = [0, 1, 0, 0, 0, 0]
O2 = [0, 0, 0, 1, 0, 0]

Step 3: L3(S) * R3(S) = (b + x) * 1
L3 = [0, 1, 0, 1, 0, 0]
R3 = [1, 0, 0, 0, 0, 0]
O3 = [0, 0, 0, 0, 1, 0]

Step 4: L4(S) * R4(S) = (c + 5) * 1
L4 = [5, 0, 0, 0, 1, 0]
R4 = [1, 0, 0, 0, 0, 0]
O4 = [0, 0, 0, 0, 0, 1]
```
3. convert vector mulpication to Lagrange polynomial (https://www.youtube.com/watch?v=bzp_q7NDdd4)
4. R1CS to QAP
```
We knew A(L) * B(R) = C(S) only on select point [1, 2, 3, 4]
A is vector of [L1, L2 .... L6]
B is vector of [R1, R2 .... R6]
C is vector of [O1, O2 ..... O6]
Z = (x - 1)(x - 2)(x - 3)(x - 4) // because 4 gates
  A * B = C on select point [1, 2, 3... n] 
  A * B - C = 0 on select point [1, 2, 3... n]
  A * B - C is dividsiable by Z
  A(known) * B(known) - C(known) = Z(known) * H(?)    <- This is QAP

we calculate polynomial H
We don't want to give A, B, C, very large;
We want to hide S, not QAP
```
> polynomial property: if prover knows A(s) - B(s) = C(s), 
5. Prover uses ECC g.t, λ.a, calculate 5 points A'=A(g.t) B'=B(g.t) C'=C(g.t) H'=H(g.t), and ? commited polynomial is same
ECC(a.t.g, b.t.g) / ECC(c.t.g, g) = ECC(h.t.g, z.t.g)
Sum(A.t) as 

1. Verfier can just ECC(A, B)/ECC(C, G) = ECC(H, Z)

// Seems like longer S is(more gate or more variable), QAP is more secure
// verfier random checkpoint was calculated by hash(gates)
Bulletproof(range proofs) similar to decimal to binary convertion
5 = 101 = 1(2^2) + 0(2^1) + 1(2^0) = 2 vector muliply
so if I able prove number requires x bits vector, I proven x is in some range.


interactive zk
1. map computation to polynomial equation
2. Verifier choose secret evaluation point
3. Prover eval polynomials
4. Verifier checks(Homomorphic Encryption allow compute on encrypted data without decryption)


Prover know w()
a(x) * w(x) = b(x) * c(x)

## Buzz Words
- Pinocchio protocol
- Convert to polynomials
> because different polynomials only coincide at n(degree) points
- Homomorphic Encryption 同态隐藏
- Knowledge of Coefficient Test force single point commitment
> balance proofer time, verifier time, proof size
Baselines:
- BCCGP-sqrt
- Bulletproofs
- ZKB++
- Ligero
- libSTARK
- Hyrax-1/3
- Hyrax-native


U, V, W 矩阵 //二次扩张多项式｜QSP多项式
z = (x-1)(x-2)(x-3)...(x-n)
目标多项式整除（证据）
拉格朗日插值法
目标多项式 ｜ 商多项式 h(x) = s.W(x) - s.U(x)*s.V(x)/z(x)
椭圆曲线离散对数 ECC
Common Reference String (CRS) a string output by NIZK's generator algorithm and avaiable both prover and verifier.


需要基础
* 椭圆加密算法 ECC
* 多项式 等同 线性代数/矩阵

这是我对zk snark理解
1. 将问题转化成R1CS多项式
2. 多项式 转化 矩阵
3. 生成 QAP 整除问题
We knew A(S) * B(S) = C(S) only on select point [1, 2, 3, 4]
A is vector of [L1, L2 .... L6]
B is vector of [R1, R2 .... R6]
C is vector of [O1, O2 ..... O6]
Z = (x - 1)(x - 2)(x - 3)(x - 4) // because 4 gates
  A * B = C on select point [1, 2, 3... n] 
  A * B - C = 0 on select point [1, 2, 3... n]
  A * B - C is dividsiable by Z
  A(已知) * B(已知) - C(已知) = Z(已知) * H(需计算)    <- QAP 整除问题、
4. 共钥 = λ.G (G is generator in ECC), 套入 A(共钥), B(共钥), C(共钥), H(共钥); 局部系统参数（CRS）来确定多项式
5. 验证方需要确认 ECC(A, B)/ECC(C, G) = ECC(H, Z)，和（不知道术语）确认多项式关系
We don't want to give A, B, C, very large;
We want to hide S, not QAP