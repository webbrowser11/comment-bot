import scratchattach as sa
import time

# ---------- Configuration ----------
USERNAME = "your_username"
PASSWORD = "your_password"
PROJECT_ID = "your_project_id"  # Replace with your project's ID
KEYWORD = "/command"  # Keyword to look for in comments
SLEEP_INTERVAL = 20  # Time (in seconds) between checks

# ---------- Initialization ----------
def initialize_session(username, password, project_id):
    """Log in to Scratch and connect to the project."""
    session = sa.login(username, password)
    project = session.connect_project(project_id)
    return project

# ---------- Main Logic ----------
def process_comments(project, keyword, processed_comments):
    """
    Fetches comments from the project, processes them, and replies if the keyword is found.
    
    Args:
        project: The connected Scratch project.
        keyword: The keyword to search for in comments.
        processed_comments: A set of comment IDs already processed.
    """
    comments = project.comments()  # Fetch recent comments
    
    for comment in comments:
        comment_id = comment.id
        content = comment.content

        # Skip already processed comments
        if comment_id in processed_comments:
            continue

        # Check if the comment contains the keyword
        if keyword in content:
            # Modify the content (example: remove keyword)
            modified_content = content.replace(keyword, "").strip()

            # Reply to the comment
            project.reply_comment(modified_content, parent_id=comment_id)
            print(f"Replied to comment ID {comment_id}: {modified_content}")

        # Mark the comment as processed
        processed_comments.add(comment_id)

# ---------- Main Loop ----------
def main():
    """Main loop for processing comments."""
    processed_comments = set()  # To track processed comment IDs
    project = initialize_session(USERNAME, PASSWORD, PROJECT_ID)

    while True:
        try:
            process_comments(project, KEYWORD, processed_comments)
        except Exception as e:
            print(f"Error occurred: {e}")
        
        # Wait before the next check
        time.sleep(SLEEP_INTERVAL)

# Run the script
if __name__ == "__main__":
    main()
