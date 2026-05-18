from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    1: {
        'title': 'Getting Started with FastAPI',
        'content': 'FastAPI makes building APIs in Python fast, clean, and efficient.'
    },
    2: {
        'title': 'Why I Love Automation',
        'content': 'Automating repetitive tasks saves hours of manual work every week.'
    },
    3: {
        'title': 'Python Tips',
        'content': 'Use list comprehensions and generators to write cleaner Python code.'
    },
    4: {
        'title': 'Web Scraping Notes',
        'content': 'Playwright and Selenium are both powerful tools for dynamic websites.'
    },
    5: {
        'title': 'Morning Routine',
        'content': 'Starting the day with exercise and planning improves productivity.'
    },
    6: {
        'title': 'Building APIs',
        'content': 'REST APIs help applications communicate in a structured way.'
    },
    7: {
        'title': 'Learning AI',
        'content': 'Understanding data and models is the foundation of machine learning.'
    },
    8: {
        'title': 'Debugging Tricks',
        'content': 'Break problems into smaller steps to identify bugs faster.'
    },
    9: {
        'title': 'Productivity',
        'content': 'Deep work sessions help maintain focus and reduce distractions.'
    },
    10: {
        'title': 'Side Projects',
        'content': 'Building projects is one of the fastest ways to improve programming skills.'
    }
}

@app.get('/posts')
def read_posts(limit: int = None):
    if limit is not None:
        return list(text_posts.values())[:limit]
    return list(text_posts.values())

@app.get('/posts/{post_id}')
def read_post(post_id: int) -> PostResponse:
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail='Post not found')
    return text_posts.get(post_id)

@app.post('/posts')
def create_post(post: PostCreate) -> PostResponse:
    new_post = {'title': post.title, 'content': post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post