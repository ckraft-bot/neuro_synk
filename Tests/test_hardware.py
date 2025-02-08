from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("google/gemma-2b", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")

input_text = "Test sentence for benchmarking how fast my model runs."
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

import time
start = time.time()
output = model.generate(input_ids, max_new_tokens=100)
end = time.time()

print("Time taken for 100 tokens:", end - start, "seconds")
print(tokenizer.decode(output[0]))

"""
If 100 tokens take <5 sec, fine-tuning will be manageable.
If 100 tokens take >20 sec, fine-tuning will be very slow, and we might need to optimize further.
"""