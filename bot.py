import scratchattach as sa

session = sa.login("user", "password")

project = session.connect_project("project")

keyword = "keyword to check"

comments = []

def CheckAndReply():    
    for comment in comments:
        if keyword in comment["content"]:
            comment_id = comment["id"]
            content = comment["content"]

            modified_content = comment.replace(keyword, " ",)

            project.reply_comment(comment_id, modified_content)
            print("replied.")
            comments.del(comment)

def SearchForNewComments():
    @events.event #Called when the event listener is ready
    def on_ready():
       print("Event listener ready!")
    @events.event
    def on_message(message):
        print(message.project, "performed action", self.type)
        comments.append(message.content)
    events.start()

check_and_reply()
