import webapp2

from app.handlers.basehandler import BlogHandler
from app.handlers.mainpagehandler import MainPageHandler
from app.handlers.blogfronthandler import BlogFrontHandler
from app.handlers.posthandler import PostPageHandler, NewPostHandler
from app.handlers.authhandler import LoginHandler, LogoutHandler
from app.handlers.welcomehandler import WelcomeHandler
from app.handlers.profilehandler import ProfileHandler
from app.handlers.signuphandler import SignupHandler
from app.handlers.commenthandler import CommentHandler
from app.handlers.likehandler import LikeHandler

app = webapp2.WSGIApplication([("/", MainPageHandler),
                               ("/blog/?", BlogFrontHandler),
                               ("/blog/post/([0-9]+)", PostPageHandler),
                               ("/blog/post/comment", CommentHandler),
                               ("/blog/post/new", NewPostHandler),
                               ("/blog/post/like", LikeHandler),
                               ("/blog/signup", SignupHandler),
                               ("/blog/login", LoginHandler),
                               ("/blog/logout", LogoutHandler),
                               ("/blog/welcome", WelcomeHandler),
                               ("/blog/profile/(\w+)", ProfileHandler)
                               ],
                              debug=True)
