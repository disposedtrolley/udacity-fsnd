from app.handlers.basehandler import *


class Welcome(BlogHandler):
    def get(self):
        if self.user:
            self.render("welcome.html", username=self.user.name)
        else:
            self.redirect("/blog/signup")
