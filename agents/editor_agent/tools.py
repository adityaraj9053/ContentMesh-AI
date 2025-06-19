from config import PROJECT_ID, LOCATION

def edit_content(written_content):
    return {
        "blog": written_content["blog"].replace("!", "."),
        "email": written_content["email"],
        "social": written_content["social"]
    }
