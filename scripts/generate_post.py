import anthropic
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_next_topic():
    with open("config/topics.json", "r") as f:
        data = json.load(f)
    return data["topics"][0]

def generate_post(topic):
    with open("prompts/blog_post_prompt.txt", "r") as f:
        prompt_template = f.read()
    
    prompt = prompt_template.replace("{topic}", topic)
    
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )
    
    response = message.content[0].text
    
    lines = response.split("\n")
    title = ""
    content = ""
    
    for i, line in enumerate(lines):
        if line.startswith("TITLE:"):
            title = line.replace("TITLE:", "").strip()
        elif line.startswith("CONTENT:"):
            content = "\n".join(lines[i+1:]).strip()
            break
    
    return title, content

if __name__ == "__main__":
    topic = get_next_topic()
    print(f"Generating post about: {topic}")
    title, content = generate_post(topic)
    print(f"Title: {title}")
    print(f"Content preview: {content[:200]}...")
    
    with open("logs/last_post.txt", "w") as f:
        f.write(f"TITLE: {title}\n\nCONTENT:\n{content}")
    
    print("Post saved to logs/last_post.txt")
