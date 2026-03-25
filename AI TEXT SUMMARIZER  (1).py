

def split_into_chunks(text, max_tokens=1000):    sentences = sent_tokenize(text)    chunks = []    chunk = ""    for sentence in sentences:        if len(chunk) + len(sentence) <= max_tokens:            chunk += " " + sentence        Else:            chunks.append(chunk)            chunk = sentence    chunks.append(chunk)    return chunks
def summarize_long_text(text):    chunks = split_into_chunks(text)    summaries = [summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text'] for chunk in chunks]    return " ".join(summaries)


if __name__ == "__main__":    input_text = """    Enter Your Text Here    """    print("Summary:\n", summarize_long_text(input_text))

