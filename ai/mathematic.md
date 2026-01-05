# Mathematic

List all mathematic tools relate to AI.

## Linear algebra

- Vector
  - vector addition -> linear combination
  - vector multiplication to scaler -> Alignment/Similarity
- Matrix / Linear Transformation `line still line after transformation; preserve relationship`
  - Not Commutativity `AB != BA`
  - Associativity `A(BC) = (AB)C`
  - matrix dot -> combined transformation
  - Basic matrix properties: rank, trace, determinant, transpose
  - SVD (Singular Value Decomposition) `find the best orthogonal basis vectors within matrix`
    - V (Right Singular Vectors) `orthonormal basis for the input space`
    - U (Left Singular Vectors) `orthonormal basis for the output space`
    - Σ (Singular Values) `how much each of these basis directions is stretched or scaled during the transformation.`

## Calculus

## Dynamic system

equilibrium solver：

- separation of variables
- partial fractions

系统动态学

d/dt.x = f(x, t, u; beta) + d

- x: state
- f(): dynamics forces
- t: time
- u: control
- beta: parameter/system output
- d: noise/disturbance

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
