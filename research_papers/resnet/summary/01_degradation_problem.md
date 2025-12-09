# Degradation Problem
## 1.Problem statement
- Intially, deep convolutional networks were thought if they become deeper and deeper then, the results during would high, in metrics like training accuracy and validation accuracy.
- However, when more and more layers were increased a problem arises. This problem is known as the `degradation problem`.
- The degradation problem means that the accuracy of the model gets worse and worse as the network goes deeper and deeper.
- It was noted that overfitting alone does not cause the degradation problem alone. Even when the gradients are stable, the training accuracy is still bad 
- So, how can we fix this issue, what did the authors of the resnet paper come up with.
- The authors introduced a residual connection.
- Think of the residual connection as saying, say instead of forcing our model to try learning the underlying mapping $H(x)$ of our input variable $x$.
- What if the model can learn the difference between our input variable $x$ and it's underlying mapping function $H(x)$. This difference can be represented by a function $F(x)$.
- The function $F(x)$ is known as the residual function and it can be represented as $F(x) = H(x) - x$.
- The final underlying mapping becomes $H(x) = F(x) + (x). So here the model is able to learn the difference between the desired mapping and input. This input directly flowed to the high layer via skip/shortcut connection.
- Shortcut connections are those connections which skip one or more layers.
- These shortcut connections perform identity mapping which are added to the output of the stack layers.
