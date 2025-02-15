from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model(model_name="Finetune_saves/ChatPlasma-v1"):
    """Load the model and tokenizer from Hugging Face."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, 
        torch_dtype=torch.float16,
        device_map="auto"
    )
    return model, tokenizer

def chat_with_model(model, tokenizer, system_prompt):
    """Simple interactive multi-turn chatbot with a system prompt."""
    print("Chatbot is ready! Type 'exit' to quit.")
    
    chat_history = [{"role": "system", "content": system_prompt}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        chat_history.append({"role": "user", "content": user_input})
        
        input_text = tokenizer.apply_chat_template(chat_history, tokenize=False, add_generation_prompt=True)
        input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(model.device)
        
        output = model.generate(input_ids, max_new_tokens=4096, do_sample=True, temperature=0.7)
        response_text = tokenizer.decode(output[0][input_ids.shape[1]:], skip_special_tokens=True)
        
        print(f"AI: {response_text}")
        
        chat_history.append({"role": "assistant", "content": response_text})

if __name__ == "__main__":
    system_prompt_file_path = 'prompt/siwei.txt'
    with open(system_prompt_file_path, 'r', encoding='utf-8') as file:
        system_prompt = file.read().strip()
    
    model, tokenizer = load_model()
    
    chat_with_model(model, tokenizer, system_prompt)