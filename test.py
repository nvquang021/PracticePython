import torch
import torch.nn as nn

weight = nn.Parameter(torch.ones(3))
weight.requires_grad =True
alpha = 0.5
weights = alpha*torch.softmax(weight, dim = 0)+ (1-alpha)*(1/3)
print(weights[0])
print(weights[1])