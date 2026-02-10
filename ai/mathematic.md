# Mathematic

List all mathematic tools relate to AI.

## Principle

- Slide window ~ in-place execution
- Calculus ~ divide & conquer

## Linear algebra

- Vector
  - vector addition -> linear combination
  - vector multiplication to scaler -> Alignment/Similarity
- Matrix / Linear Transformation `line still line after transformation; preserve relationship`
  - Not Commutativity `AB != BA`
  - Associativity `A(BC) = (AB)C`
  - matrix dot -> combined transformation
  - Basic matrix properties
    - rank
    - trace
    - determinant
    - transpose
    - eigenvalues & eigenvector
      - eigenvalues > 1 causes exploding training
  - Orthogonal matrices intuitions
    - Length & angle(information) preservation
    - Inverse = transpose; typical Inverse is expensive op, but transpose is cheap
    - Columns = orthonormal basis; independent features
    - best possible numerical stability
    - orthogonal ≈ “no learning”, only rearrange
  - SVD (Singular Value Decomposition) `find the best orthogonal basis vectors within matrix`
    - V (Right Singular Vectors) `orthonormal basis for the input space; square matrix match with x'col;`
    - U (Left Singular Vectors) `orthonormal basis for the output space; square matrix match with x'row`
    - Σ (Singular Values) `how much each of these basis directions is stretched or scaled during the transformation. same shape x matrix`

## Calculus

- multivariable calculus `uses in back propagation`

## Dynamic system

system dynamics modeling softwares:

- AnyLogic(Discrete)
- Vensim(Continuous)
  - shadow variable
- Arena(Event)

equilibrium solver：

- separation of variables
- partial fractions
- Jacobian

系统动态学

d/dt.x = f(x, t, u; beta) + d

- x: state
- f(): dynamics forces
- t: time | evolution index
- u: control input
- beta: system parameter
- d: noise/disturbance

Inference dynamics(inner loop):
> An LLM is a high-dimensional, discrete-time, controlled nonlinear dynamical system whose parameters are optimized by a separate gradient-flow system.

>> LLM learn by observe token transition. Transformer is token transition to another token, while Diffusion is noise transition to tokens.

>> The problem Transformer train data are "final version", transformer did NOT observe from "draft" transition to "final version".

- f(): LLM
- x: kv cache
  - 1. Previous Tokens convert to kv cache;
  - 1. KV cache apply dynamics force on Current Token(residual stream);
  - 1. Current Token(residual stream) transform/get moved to the Predict Token;
- t: LLM time/evolution unit is token.
- u: token embedding | Q | residual stream
- beta: weight & bias
- d: sampling, quantization
  - uses proper prompt avoid LLM confusion;

Learning dynamics(outer loop):

- f(): loss gradient | correction
  - correction are arbitrary per LLM, no common structure info; structure exists in x
- x: All learnable parameters: LLM's weight & bias, dynamic lr & decay
- t: training unit is batch
- u: data / minibatch / labels
- beta: optimizer hyper parameters: hardcoded lr, decay
- d: label noise, sampling distribution
  - use better data lead to good gradient signal

Notes:

- Maybe add more learning beta allows more controls.
  - user not only want right answer, but better steering. Ex: google
- Learning loop optimizer: how gradient converge/evolute to global min;
- inefficient converge speed must paid either at training(lose adaptability for inference speed) or at inference(slow reaction)

FAQ:

- f() is most often
  - unknown or too complicated need simplification
  - nonlinear, hard to solve
  - high dimensional
- u ~ LLM weight & bias
- x: input token | residual stream

`NN is dynamic system we created with our desired behavior.`

- Trajectories
- Equilibria
- Chaos: sensitive dependence on initial conditions
- Oscillations / cycles

convergence vs expressivity trade-offs
> Maybe coverage speed always cost wrong trajectory. Diffusion rapid coverage cost accuracy.

Common Dynamics System

- continuous-time
- discrete-time
- Residual / incremental systems; That's why residual connection.
- equilibrium systems (DEQs)
- Hybrid systems (continuous + discrete)
- Stochastic dynamical systems (diffusion)
- Tessellation/Fractal ~ `scale invariance`, but usually no control.

### Dynamic Mode Decomposition

Enforce constrain into model

DMD to probe stability of residual blocks:

1. collection activations on RS
2. Uses DMD solve $X’ \approx A X$
3. calculate eigenvalues of A

- Lyapunov Exponent (LLE) measures how fast nearby trajectories diverge
