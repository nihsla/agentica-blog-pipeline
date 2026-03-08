import requests
import os
import markdown
from dotenv import load_dotenv

load_dotenv()

def publish_to_wordpress(title, content):
    url = os.getenv("WORDPRESS_URL")
    username = os.getenv("WORDPRESS_USERNAME")
    password = os.getenv("WORDPRESS_APP_PASSWORD")
    
    endpoint = f"{url}/wp-json/wp/v2/posts"
    
    html_content = markdown.markdown(content)
    
    post_data = {
        "title": title,
        "content": html_content,
        "status": "draft"
    }
    
    response = requests.post(
        endpoint,
        json=post_data,
        auth=(username, password)
    )
    
    if response.status_code == 201:
        post_url = response.json().get("link")
        print(f"Success! Post created as draft: {post_url}")
        return True
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return False

if __name__ == "__main__":
    with open("logs/last_post.txt", "r") as f:
        content = f.read()
    
    lines = content.split("\n")
    title = lines[0].replace("TITLE: ", "").strip()
    post_content = "\n".join(lines[3:]).strip()
    
    print(f"Publishing: {title}")
    publish_to_wordpress(title, post_content)
