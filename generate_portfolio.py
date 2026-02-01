import os
import json

categories = ['design', 'development', 'illustration', 'photography', '3d']
portfolio_data = []

for category in categories:
    folder_path = os.path.join('portfolio', category)
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.mp4', '.webm', '.ogg')):
                file_path = f'portfolio/{category}/{file}'
                title = os.path.splitext(file)[0]
                media_type = 'video' if file.lower().endswith(('.mp4', '.webm', '.ogg')) else 'image'
                portfolio_data.append({
                    'title': title,
                    'category': category,
                    'file_path': file_path,
                    'media_type': media_type
                })

with open('portfolio.json', 'w') as f:
    json.dump(portfolio_data, f, indent=4)

print("Portfolio JSON generated.")
