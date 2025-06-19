from config import PROJECT_ID, LOCATION

def optimize_for_seo(edited_content):
    return {
        "blog": f"[SEO Optimized] {edited_content['blog']}",
        "email": edited_content["email"],
        "social": edited_content["social"]
    }
