from config import PROJECT_ID, LOCATION

def generate_copy(trend_data):
    keywords = ", ".join(trend_data["trending_keywords"])
    return {
        "blog": f"Explore the future of {keywords} in our latest blog!",
        "email": f"Subject: Stay ahead with {keywords}",
        "social": f"🚀 Trending Now: {keywords}. Join the movement!"
    }
