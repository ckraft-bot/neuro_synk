# DATASETS
__Tone analysis:__

```bash
df = pd.read_parquet("hf://datasets/andersonbcdefg/llm-tones/data/train-00000-of-00001.parquet")
```
__Sentiment analysis:__ 

```bash
splits = {'train': 'train_df.csv', 'validation': 'val_df.csv', 'test': 'test_df.csv'}
df = pd.read_csv("hf://datasets/Sp1786/multiclass-sentiment-analysis-dataset/" + splits["train"])
```

# FINE TUNING MODELS
- gemma 2b out of box
- hugging face + PEFT + QLORA
    - gemma as base line (zero shot)
    - PEFT + QLORA --> Use `bitsandbytes` for quantization.
- axolotl (streamlined fine tuning framework)

_quantizaation_ is a technique that reduces the size of an AI model without significantly hurting its performance. This is important for fine-tuning on local machines because it lowers memory usage and speeds up training.

__Why Use Quantization (bitsandbytes)?__
Without quantization: A model like Gemma 2B might take up 4-8GB of VRAM (or even more RAM).
With quantization: It can run in as little as 2GB RAM using 4-bit or 8-bit precision.

__How bitsandbytes Helps__
bitsandbytes is a library that helps convert large models into smaller, 4-bit or 8-bit versions while keeping most of their accuracy.
QLoRA uses bitsandbytes to apply LoRA fine-tuning efficiently.

__How to apply quantization in Hugging Face + QLoRA__

1. install bitsandbytes:

```bash
pip install bitsandbytes transformers accelerate peft
```

2. load the model in 4bit mode for lower memeory usuage:
```bash
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,  # Enable 4-bit quantization
    bnb_4bit_compute_dtype="float16",  
    bnb_4bit_use_double_quant=True,  # Further memory optimization
)

model = AutoModelForCausalLM.from_pretrained("google/gemma-2b", quantization_config=bnb_config)
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
```

__Fine tuning eval__

measure for tone accuracy
- similarity score

# IMPLEMENTATION
- backend: python with fast api 
- frontend: streamlit 
- try shipping with docker

# HARDWARE EVAL
```bash
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
```