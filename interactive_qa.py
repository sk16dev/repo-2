from generate_answer import generate_answer

def interactive_qa(pdf_path):
    while True:
        question = input("Enter your question (type 'exit' to end): ")
        if question.lower() == 'exit':
            print("Exiting...")
            break
        
        # Generate answer for the input question
        answer = generate_answer(question, pdf_path)
        
        # Print the answer
        print("\nAnswer:")
        print(answer)
        print("=" * 50)

if __name__ == "__main__":
    pdf_path = 'llm.pdf'  
    interactive_qa(pdf_path)
