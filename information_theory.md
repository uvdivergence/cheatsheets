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

The Kullback-Leibler Divergence is useful to quantify the informational
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

Mutual Information is useful to quantify how much information one distribution gives you about the other.

> Definition: Mutual Information

Let $X, Y$ be discrete random variables in $\mathcal{X}$ and $\mathcal{Y}$, then:

```math
I(X, Y) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} \mathbb{P}(X=x, Y=y) \log \frac{\mathbb{P}(X=x, Y=y)}{\mathbb{P}(X=x) \mathbb{P}(Y=y)}.
```

Notice that Mutual Information can also be defined using the Kullback-Leibler Divergence as:

```math
I(X, Y) = D_\text{KL}(P(X,Y)\parallel P(X)P(Y)).
```

This gives us an intuitive interpretation, where we can think of Mutual Information as the distance the joint distribution is from product of idependent distributions.
