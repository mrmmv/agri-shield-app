import re

file_path = r'c:\Users\Admin\OneDrive - Department of Education\Documents\shanai\android app\www\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace API calls
content = re.sub(r"fetch\(['\"]/api/", "fetch('https://bantay-bukid.duckdns.org/api/", content)
content = re.sub(r"fetch\(`\/api\/", "fetch(`https://bantay-bukid.duckdns.org/api/", content)

# Replace static assets
content = content.replace('href="/static/', 'href="https://bantay-bukid.duckdns.org/static/')
content = content.replace('src="/static/', 'src="https://bantay-bukid.duckdns.org/static/')

# For leaf image update
content = content.replace('img.src = data.filepath', 'img.src = "https://bantay-bukid.duckdns.org" + data.filepath')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
