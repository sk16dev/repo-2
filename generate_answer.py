from pyexpat import model
from sre_parse import Tokenizer
from tokenize import tokenize
from chunk_text import chunk_text
from create_prompt import create_prompt
from extract_text import extract_text
import tokenizer
from generate_answer import tokenizer


def generate_answer(question, pdf_path):
    # Extract text from PDF
    text = extract_text(pdf_path)
    
    if not text:
        return "No text extracted from the PDF."

    # Chunk text into manageable parts
    chunks = chunk_text(text)
    
    answers = []
    for chunk in chunks:
        # Create prompt for each chunk
        prompt = create_prompt(question, chunk)
        
        # Truncate the prompt if it exceeds the maximum length
        if len(prompt) > 1024:
            prompt = prompt[:1024]
        
        # Encode the input text
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        
        # Generate answer using T5 model
        output = model.generate(input_ids, max_length=256)
        
        # Decode the output text
        answer = tokenizer.decode(output[0], skip_special_tokens=True)
        answers.append(answer)

    
    final_answer = "\n".join(answers)
    return final_answer
