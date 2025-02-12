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

## Common Communication Tones
### Formal:
**Description:** Structured, objective, and often used in professional or academic contexts.  
**Example:** "Dear Dr. Smith, I am writing to inquire about the research opportunity available in your department."  
**Research Insight:** Formal language is associated with respect for hierarchy and context-appropriateness (e.g., DeVault & McCroskey, 1992).

### Informal:
**Description:** Casual, conversational, and typically used among friends or in relaxed environments.  
**Example:** "Hey, what's up? Wanna grab a coffee later?"  
**Research Insight:** Informal language fosters closeness and relatability, as noted in studies of interpersonal communication (Pennebaker, Mehl, & Niederhoffer, 2003).

### Friendly/Warm:
**Description:** Conveys approachability, kindness, and openness. It often includes supportive and positive language.  
**Example:** "Hi there! I hope you're having a great day. Let me know if there's anything I can do to help."  
**Research Insight:** Warmth is a key component in building trust and rapport (Fiske, Cuddy, & Glick, 2007).

### Empathetic:
**Description:** Shows understanding, compassion, and sensitivity to the feelings of others.  
**Example:** "I understand that this has been a challenging time for you; please know I'm here to support you."  
**Research Insight:** Empathy in communication is crucial for effective support and has been extensively discussed in the literature on emotional intelligence and interpersonal communication (Pennebaker et al., 2003).

### Assertive:
**Description:** Direct, confident, and clear, often used when setting boundaries or making requests.  
**Example:** "I need the report by 3 PM today so we can finalize our strategy."  
**Research Insight:** Assertiveness balances directness with respect and is critical in organizational settings (DeVito, 2012).

### Humorous:
**Description:** Light-hearted, playful, and often intended to entertain or ease tension.  
**Example:** "I tried to catch some fog yesterday. I mist."  
**Research Insight:** Humor has been studied extensively in linguistics (Attardo, 2001) and is known to improve engagement and social bonding when used appropriately.

### Sarcastic/Ironic:
**Description:** Uses irony or exaggeration to convey contempt or humor, often with an undercurrent of criticism.  
**Example:** "Oh great, another meeting. Just what I needed!"  
**Research Insight:** Sarcasm is a complex communicative tool that can both entertain and alienate, depending on the context and the relationship between communicators (Attardo, 2001).

__Evidence and Research Citations__
- Pennebaker, J. W., Mehl, M. R., & Niederhoffer, K. G. (2003).  
  *Psychological aspects of natural language use: our words, our selves.*  
  Annual Review of Psychology, 54, 547–577.  
  This review discusses how language reflects psychological states, including the use of different tones and styles.

- Fiske, S. T., Cuddy, A. J. C., & Glick, P. (2007).  
  *Universal dimensions of social cognition: warmth and competence.*  
  Trends in Cognitive Sciences, 11(2), 77–83.  
  This paper outlines the importance of warmth (a key component of friendly and empathetic tones) in social interactions.

- Attardo, S. (2001).  
  *Humorous texts: A semantic system of analysis.*  
  Walter de Gruyter.  
  Attardo's work provides a detailed analysis of humor and sarcasm in communication.

- DeVault, D., & McCroskey, J. C. (1992).  
  *Communication Apprehension, Avoidance, and Effectiveness.*  
  Communication Research Reports.  
  This research discusses various communication styles, including the use of formal versus informal language in different contexts.

- IBM Watson Tone Analyzer (2017).  
  Retrieved from IBM Watson Tone Analyzer  
  IBM’s tool is based on psychological research and is used to detect and classify tones in written text.

# FINE TUNING MODELS
- gemma 2b out of box
- hugging face + PEFT + QLORA
    - gemma as base line (zero shot)
    - PEFT + QLORA --> Use `bitsandbytes` for quantization.
- axolotl (streamlined fine tuning framework)

_quantization_ is a technique that reduces the size of an AI model without significantly hurting its performance. This is important for fine-tuning on local machines because it lowers memory usage and speeds up training.

__Why use quantization (bitsandbytes)?__
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

# DOCKER
1. Install docker, create an account
2. Create a container called "ollama" based on an existing ollama docker image

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
3. Start container - run a model inside the contianer
```bash
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
4. Run model locally, choose your model
```bash
docker exec -it ollama ollama run gemma2:2b
```
4. To list models in the container
```bash
docker exec -it ollama ollama list models
```
5. Find api address
```bash
docker inspect ollama
```

# CLOUD HOSTING SERVICE
I'm trying out  [Digital Ocean](https://www.digitalocean.com/)
- ssh key for droplet 
  - run ```ssh-keygen``` in terminal, creaete, save, read the ssh file
  - ssh file called 'docker_ssh.pub'
  