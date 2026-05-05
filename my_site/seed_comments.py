import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
django.setup()

from blog.models import Post, Comment

def seed_comments():
    posts = Post.objects.all()
    names = ['Alice', 'Bob', 'Charlie', 'Dana', 'Eli', 'Frank', 'Grace']
    texts = [
        'Informative post, thanks!', 
        'I disagree with some points, but well written.', 
        'Could you elaborate on the third paragraph?', 
        'This helped me a lot with my project.', 
        'Amazing read, shared it with my team!',
        'I love the way you explained the complex parts.',
        'Can you provide more examples in the next post?',
        'Very inspiring content.'
    ]
    
    count = 0
    for p in posts:
        for _ in range(3):
            Comment.objects.create(
                user_name=random.choice(names),
                user_email=f"{random.choice(names).lower()}@example.com",
                text=random.choice(texts),
                post=p
            )
            count += 1
    print(f"Added {count} comments to the database.")

if __name__ == '__main__':
    seed_comments()
