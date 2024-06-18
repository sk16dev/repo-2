def chunk_text(text, max_length=1024):
    sentences = text.split('. ')
    chunks = []
    current_chunk = []

    for sentence in sentences:
        if len(' '.join(current_chunk)) + len(sentence) + 1 > max_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
        else:
            current_chunk.append(sentence)

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

if __name__ == "__main__":
    example_text = "Sample text to chunk into manageable parts for the model."
    chunks = chunk_text(example_text)
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}: {chunk}")
