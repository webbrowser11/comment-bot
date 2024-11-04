import scratchattach as sa
from datetime import datetime

session = sa.login("user", "password")

project = session.connect_project("project")

keyword = "keyword to check"

today = datetime.today().date()

def check_and_reply():
    comments = project.comments()

    today_comments = [
        comment for comment in comments 
        if datetime.fromtimestamp(comment['timestamp']).date() == today
    ]


    for comment in today_comments:
        if keyword in comment["content"]:
            comment_id = comment["id"]
            content = comment["content"]

            modified_content = comment.replace(keyword, " ",)

            project.reply_comment(comment_id, modified_content)
            print("replied.")

check_and_reply()
