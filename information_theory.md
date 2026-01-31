# Information Theory

## Entropy

To get to the definition of entropy, we first consider a function
$s: \text{Events} \to \mathbb{R}$ that measures an amount of surprise
associated with an event. We propose the following axioms:

 1. $s(A)$ depends continuously on $\mathbb{P}(X \in A)$.
 2. $s(A)$ is decreasing in $\mathbb{P}(X \in A)$.
 3. $s(A \cap B) = s(A) + s(B)$ if $A$ and $B$ are independent.

The only function satisfying these axioms is
$s(A) = - \log (\mathbb{P}(X \in A))$.

To get to the definition of entropy, we need to think not of the surprise of a single event but of the average surprise across all events described by a distribution.

> Definition: Entropy

```math
H(X) = - \sum_{x \in X} \mathbb{P}(X = x) \log \mathbb{P}(X = x),
```

where $0 \log 0 = 0$.

To emphasize the fact that this is technically an average, we can write
$H(X) = \mathbb{E}_{x \sim P}[- \log P(x)]$.

## Kullback-Leibler Divergence

The Kullback-Leibler divergence is useful to quantify the informational
distance of two distributions. This function is not symmetric and this is
intentional and very useful. It is helpful to think of this quantity as the
amount of surprise associated with sampling from an approximating probability
distribution $Q$ while believing we're sampling from the true probability
distribution $P$.

> Definition: KL Divergence

Let $P$ and $Q$ be distribution functions on $\mathcal{X}$, then

```math
D_\text{KL}(P \parallel Q) = \sum_{x \in \mathcal{X}} P(x) \log \frac{P(x)}{Q(x)},
```

with $0 \log 0 = 0$,
$D_\text{KL}(P \parallel Q) = \infty$ if $(\exists x \in \mathcal{X})(Q(x) = 0, P(X) \neq 0)$.

Using the expected value notation, we can write
$D_\text{KL}(P \parallel Q) = \mathbb{E}_{x \sim P}[\log \frac{P(x)}{Q(x)}]$.

To illustrate the asymmetry, consider a rigged coin. Suppose the true
distribution is $P$ with $P(\text{heads}) = 0$, but an observer believes it is
fair, $Q$ with $Q(\text{heads}) = 0.5$. Observing only tails is mildly
surprising under this belief — $D_{\text{KL}}(P \parallel Q)$ is finite. Now
reverse the situation: the true distribution is $P$ with
$P(\text{heads}) = 0.5$, but the observer believes $Q$ with
$Q(\text{heads}) = 0$. When heads inevitably occurs, the observer's model
assigns it zero probability — infinite surprise! Indeed,
$D_{\text{KL}}(P \parallel Q) = \infty$.

## Mutual Information

Mutual information is useful to quantify how much information one distribution gives you about the other.

> Definition: Mutual Information

Let $X, Y$ be discrete random variables in $\mathcal{X}$ and $\mathcal{Y}$, then:

```math
I(X, Y) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} \mathbb{P}(X=x, Y=y) \log \frac{\mathbb{P}(X=x, Y=y)}{\mathbb{P}(X=x) \mathbb{P}(Y=y)}.
```

Notice that mutual information can also be defined using the Kullback-Leibler divergence as:

```math
I(X, Y) = D_\text{KL}(P(X,Y)\parallel P(X)P(Y)).
```

This gives us an intuitive interpretation, where we can think of mutual information as the distance the joint distribution is from product of idependent distributions.

The definitions are setup to work like visualized below.

![Two Variable Entropy Diagram][two_variable_entropy_diagram]

## Conditional Entropy

> Definition: Conditional Entropy

The conditional entropy of $X$ given $Y$ is defined as:

```math
H(X | Y) = - \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} \mathbb{P}(X = x, Y = y) \log \mathbb{P}(X=x | Y=y)
```

We can rewrite the formula using the definition of conditional probability $\mathbb{P}(X|Y) = \frac{\mathbb{P}(X, Y)}{\mathbb{P}(Y)}$ to:

```math
H(X | Y) = - \sum_{y \in \mathcal{Y}} \mathbb{P}(Y=y) \sum_{x \in \mathcal{X}} \mathbb{P}(X = x | Y = y) \log \mathbb{P}(X = x | Y = y) \\ = \sum_{y \in \mathcal{Y}} \mathbb{P}(Y=y) H(X|Y = y) = \mathbb{E}_{y \sim \mathbb{P}_Y}[H(X|Y=y)].
```

But perhaps the most important formula to properly understand the conditional entropy is:

```math
H(X|Y) = H(X) - I(X, Y).
```

Here we can return back to the previous visualization and clearly see that the conditional entropy of $X$ given $Y$ is the entropy of $X$ minus the mutual information of $X$ and $Y$.

Baye's rule gives us the chain rule of conditional entropy:

```math
H(X|Y) = H(X, Y) - H(Y).
```

## Conditional Kullback-Leibler Divergence

Just for completeness, we are going to define the conditional version of Kullback-Leibler divergence. Given two distribution functions $P(X|Y)$ and $Q(X|Y)$ conditional on $y \in \mathcal{Y}$, we define

```math
D_\text{KL}(P(X|Y) \parallel Q(X|Y) | P(Y)) = \sum_{y \in \mathcal{Y}} P(Y=y) D_\text{KL}(P(X|Y=y) \parallel Q(X|Y=y)) \\ = \mathbb{E}_{y \sim P_Y}[D_\text{KL}(P(X|Y=y) \parallel Q(X|Y=y))].
```

## Conditional Mutual Information

Conditional mutual information is useful when quantifying mutual information
between three random variables.

> Definition: Conditional Mutual Information

Let $X, Y, Z$ be discrete random variables taking values in $\mathbb{X}$. The
conditional mutual information between $X$ and $Y$ given $Z$ is:

```math
I(X, Y | Z) = H(X | Z) - H(X | Y, Z).
```

We can visualize this with the following diagram.

![Three Variable Entropy Diagram][three_variable_entropy_diagram]

Be careful, however, as this venn diagram for three variables is a leaky
abstraction. We can imagine a situation with three variables where knowing any
of the two variables at the same time does not give any additional information
about the third variable, yet when we learn about all of the three variables
at once, we clearly see a relationship between them and so if the following relationship should hold:

```math
H(X,Y,Z)= H(X) + H(Y) + H(Z) - H(X,Y|Z) - H(X,Z|Y) - H(Z, Y|X) + I(X,Y,Z),
```

then it must be true that $I(X,Y,Z) = -1$. This is the case for the XOR
relationship. This is called synergy in information theory and is extremely
important in cryptography. For the three variable XOR relationship $H(X) = 1$,
$H(Y) = 1$, $H(Z) = 1$, $H(X, Y) = 2$, $H(X, Z) = 2$, $H(Z, Y) = 2$,
$I(X,Y,Z) = -1$, $H(X,Y,Z) = 2$.

## Gibbs' Inequality

> Definition: Gibb's Inequality

Gibbs' inequality states that given any two discrete probability distributions $p$ and $q$:

```math
\sum_{x \in \mathcal{X}} p(x) \log p(x) \geq \sum_{x \in \mathcal{X}} p(x) \log q(x).
```

The direct consequence of this is that $D_\text{KL}(p \parallel q) \geq 0$. To prove this, we start with Jensen's inequality:

```math
\mathbb{E}[\varphi(X)] \geq \varphi(\mathbb{E}(X)),
```

where $\varphi(x)$ is a convex function. We observe that:

```math
\sum_{x \in \mathcal{X}} p(x) \log \frac{p(x)}{q(x)} = \sum_{x \in \mathcal{X}} - p(x) \log \frac{q(x)}{p(x)} = \mathbb{E}_{X \sim p}\left[-\log \frac{q(X)}{p(X)}\right],
```

where $- \log (x)$ is a convex function, so we can apply Jensen's inequality:

```math
\mathbb{E}_{X \sim p}\left[- \log \frac{q(X)}{p(X)} \right] \geq -\log \mathbb{E}_{X \sim p}\left[\frac{q(X)}{p(X)}\right].
```

Expanding the expected value operators, we get:

```math
\sum_{x \in \mathcal{X}} p(x) \log \frac{p(x)}{q(x)} \geq - \log \sum_{x \in \mathcal{X}} p(x) \frac{q(x)}{p(x)}.
```

Further simplifying and using the fact that $\sum_{x \in \mathcal{X}} q(x) = 1$, we get:

```math
\sum_{x \in \mathcal{X}} p(x) \log \frac{p(x)}{q(x)} \geq 0.
```

If we rearrange this using the logarithm identities, we obtain the Gibbs' inequality directly, where equality occurs if and only if $p(x) = q(x)$.

## Log Sum Inequality

The log sum inequality is a useful tool for proving other inequalities.

> Definition: Log Sum Inequality

Let $a_i, \dots, a_n$ and $b_i, \dots, b_n$ be non-negative constants, then:

```math
\sum_{i=1}^{n} a_i \log \frac{a_i}{b_i} \geq \left(\sum_{i=1}^n a_i \right) \log \frac{\sum_{i}^n a_i}{\sum_{i}^n b_i},
```

with equality occuring if and only if $\frac{a_i}{b_i} = \text{const}$.

We start by setting $\sum_{i}^n a_i = a$ and $\sum_{i}^n b_i = b$. Then we manipulate the left-hand side of the equation:

```math
\sum_{i=1}^{n} a_i \log \frac{a_i}{b_i} = \sum_{i=1}^{n} \frac{a_i}{b_i}b_i \log \frac{a_i}{b_i}.
```

We substitute $f(x) = x \log x$:


```math
\sum_{i=1}^{n} \frac{a_i}{b_i}b_i \log \frac{a_i}{b_i}=\sum_{i=1}^{n} b_i f\left(\frac{a_i}{b_i}\right).
```

To be able to use Jensen's inequality, we need to normalize $\sum_{i=1}^n c_i = 1$, so we divide by $b$:


```math
\sum_{i=1}^{n} b_i f\left(\frac{a_i}{b_i}\right) = b\sum_{i=1}^{n} \frac{b_i}{b} f\left(\frac{a_i}{b_i}\right).
```

We observe that $f(x)$ is convex and apply Jensen's inequality:

```math
b\sum_{i=1}^{n} \frac{b_i}{b} f\left(\frac{a_i}{b_i}\right) \geq b f \left(\sum_{i=1}^n \frac{b_i}{b} \frac{a_i}{b_i}\right).
```

We simplify to:

```math
\sum_{i=1}^{n} \frac{b_i}{b} f\left(\frac{a_i}{b_i}\right) \geq f \left(\frac{a}{b}\right),
```

undoing the substitution we get:


```math
\sum_{i=1}^{n} \frac{b_i}{b} \frac{a_i}{b_i} \log \left(\frac{a_i}{b_i}\right) \geq \frac{a}{b} \log \left(\frac{a}{b}\right).
```

By further simplifying we arrive at:

```math
\sum_{i=1}^{n} a_i \log \left(\frac{a_i}{b_i}\right) \geq a \log \left(\frac{a}{b}\right),
```

which is what we wanted to prove.

## Properties of the Kullback-Leibler Divergence

The Kullback-Liebler divergence has the following properties:

 1. $D_\text{KL}(p(x) \parallel q(x)) \geq 0$, with $D_\text{KL}(p(x) \parallel q(x)) = 0 \Leftrightarrow p(x) = q(x)$ (Information inequality),
 2. $D_\text{KL}(p(x, y) \parallel q(x,y)) = D_\text{KL}(p(x | y) \parallel q(x | y) | p(y)) + D_\text{KL}(p(y) \parallel q(y))$ (Chain rule),
 3. $D_\text{KL}(p(x, y) \parallel q(x, y)) \geq D_\text{KL}(p(x) \parallel q(x))$,
 4. $D_\text{KL}(p(x | y) \parallel q(x | y) | p(y)) = D_\text{KL}(p(y)p(x | y) \parallel p(y)q(x | y))$,
 5. Given distribution functions $p_1, p_2, q_1, q_2$ and $\lambda \in [0, 1]$: $D_\text{KL}(\lambda p_1 + (1 - \lambda) p_2 \parallel \lambda q_1 +  (1-\lambda) q_2) \leq \lambda D_\text{KL}(p_1 \parallel q_1) + (1 - \lambda) D_\text{KL}(p_2 \parallel q_2)$.

[two_variable_entropy_diagram]: https://raw.githubusercontent.com/uvdivergence/cheatsheets/refs/heads/main/two_variable_entropy_diagram.jpg
[three_variable_entropy_diagram]: https://raw.githubusercontent.com/uvdivergence/cheatsheets/refs/heads/main/three_variable_entropy_diagram.jpg
