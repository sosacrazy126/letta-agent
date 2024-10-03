import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class TextModel:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2").to(self.device)
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        
        # Set pad_token_id to eos_token_id
        self.model.config.pad_token_id = self.model.config.eos_token_id

    def generate_text(self, input_text, context):
        prompt = f"{context}\n{input_text}"
        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        
        # Create attention mask
        attention_mask = torch.ones(inputs.shape, dtype=torch.long, device=self.device)
        
        outputs = self.model.generate(
            inputs,
            attention_mask=attention_mask,
            max_length=150,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text