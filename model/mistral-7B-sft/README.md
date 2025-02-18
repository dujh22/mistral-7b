Mistral 7B fine-tuned on MetaMATH [1] used in [Math-Shepherd](https://arxiv.org/pdf/2312.08935.pdf).

Pass@1:
- GSM8K: 77.9
- MATH:  28.6

`Input`: only the math problem, without any system prompt, e.g., 
```
Janet\u2019s ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much in dollars does she make every day at the farmers' market?
```
`Output`: Step-by-step solutions with a special step tag `ки`, e.g.,
```
Step 1: Janet's ducks lay 16 eggs per day. ки\nStep 2: She eats three for breakfast every morning, so she has 16 - 3 = 13 eggs left. ки\nStep 3: She bakes muffins for her friends every day with four eggs, so she has 13 - 4 = 9 eggs left. ки\nStep 4: She sells the remainder at the farmers' market daily for $2 per fresh duck egg, so she makes 9 * $2 = $18 every day at the farmers' market. The answer is: 18 ки
```

[1] MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models.