from django.shortcuts import render, Http404        
from  datetime import date
all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "title": "Mountain Hiking",
        "image": "mountain_hiking.png",
        "author": "Abdullah",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "date": date(2021, 7, 21),
        "content": """
Hiking in the mountains has always been a special experience for me. The crisp morning air, the sound of leaves crunching beneath your boots, and the rewarding feeling of reaching a new peak are things that simply cannot be replicated anywhere else. 

During our recent trek, we experienced three distinct weather patterns in a single day. We started with bright sunshine, encountered a thick blanket of fog near the midway point, and finally, were greeted by a stunning golden hour just before we reached our campsite. But the best part of the trip was a completely unexpected encounter with a family of deer that crossed our path right as we stopped for lunch.

It taught me that being prepared is just as important as being enthusiastic. Carrying extra layers, plenty of water, and a reliable map can make the difference between a memorable adventure and a miserable ordeal. Next time you head out into the wilderness, remember to respect nature's unpredictability and take a moment to truly appreciate the breathtaking views at the summit.
        """
    },
    {
        "slug": "programming-is-fun",
        "title": "Programming Is Great",
        "image": "programming_fun.png",
        "author": "Abdullah",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep, that's what happened to me yesterday...",
        "date": date(2022, 3, 10),
        "content": """
Programming can be one of the most intellectually rewarding hobbies, but it will definitely test your patience. If you've ever spent hours scouring through Stack Overflow trying to fix a mysterious bug, you know exactly what I mean.

Just yesterday, my entire application broke down over what turned out to be a missing comma in a JSON configuration file. The error messages were incredibly cryptic, leading me down a rabbit hole of debugging database connections and third-party APIs. It took three hours and a cup of cold coffee to realize that the syntax error was right staring at me in line 42.

However, once you find that bug and your code finally compiles and runs successfully, the rush of dopamine is unparalleled. The joy of creating something out of nothing, solving complex puzzles, and seeing your logic come to life on screen makes all the temporary frustrations entirely worth it.
        """
    },
    {
        "slug": "into-the-woods",
        "title": "Nature At Its Best",
        "image": "woods.png",
        "author": "Abdullah",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible.",
        "date": date(2022, 8, 5),
        "content": """
There is a profound sense of tranquility that you can only find deep within the woods. Surrounded by towering trees that have stood for centuries, you can't help but feel a deep connection to the earth. 

Walking through the dense forest, the sunlight filtering through the canopy creates a mesmerizing dance of shadows and light on the forest floor. The ambient noise of the city is completely replaced by the rustling of leaves, the chirping of birds, and the gentle trickling of a nearby stream. It is the ultimate escape from the fast-paced digital world we live in.

I often take a small notebook with me on these walks. Whenever I hit a creative block, stepping away from my desk and immersing myself in nature almost immediately clears my mind. The natural world is full of intricate patterns and beautiful designs that serve as the perfect source of inspiration for my projects.
        """
    },
    {
        "slug": "my-first-django-project",
        "title": "My first Django project",
        "image": "django_project.png",
        "author": "Abdullah",
        "excerpt": "I am finally building a blog using Django. This framework is so powerful!",
        "date": date(2023, 1, 15),
        "content": """
After months of learning Python, I decided it was time to step out of my comfort zone and build a full-stack web application. Django seemed like the obvious choice given its "batteries-included" philosophy, and I couldn't be happier with the decision.

Setting up the initial project was surprisingly smooth. The built-in admin panel is an absolute game-changer, allowing me to manage my database models without having to write custom CRUD interfaces from scratch. I was also incredibly impressed by the Object-Relational Mapper (ORM) which makes database querying feel incredibly intuitive using native Python code.

Of course, there was a learning curve. Understanding how URLs, views, and templates stitch together took a few days of reading documentation and watching tutorials. But once it clicked, development became incredibly fast. Django sets you up for success by enforcing good structural habits, and I'm very excited to keep adding new features like comments and an authentication system to this blog.
        """
    }
]

def get_date(post):
    return post['date']

def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    lasted_posts = sorted_posts[:3]
    return render(request, 'blog/index.html',{
        'posts': lasted_posts
    })

def post_list(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    try:
        post = next(post for post in all_posts if post['slug'] == slug)
        return render(request, 'blog/post-detail.html', {
            'post': post
        })
    except StopIteration:
        return render(request, 'blog/404.html', status=404)

def post_edit(request, slug):
    pass

def post_delete(request, slug):
    pass