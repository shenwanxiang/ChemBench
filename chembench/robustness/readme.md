## robustness split

```python

from chembench import get_robustness_induces
induces1 = get_robustness_induces("HIV", induces = "random_5fcv_5rpts")
induces2 = get_robustness_induces("HIV", induces = "scaffold_5fcv_1rpts")

print(len(induces1))
print(len(induces2))


```