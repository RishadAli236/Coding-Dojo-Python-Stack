from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import post, user, comment

@app.route("/wall")
def success():
    if "logged_in_user_id" not in session:
        flash("Please log in", "login error")
        return redirect("/")
    else:
        logged_in_user = user.User.get_by_id(session["logged_in_user_id"])
        all_posts = post.Post.get_all_posts_with_creators()
        all_comments = comment.Comment.get_comments_with_creators()
        return render_template("wall.html", user = logged_in_user, all_posts = all_posts, all_comments = all_comments)
    
@app.route("/create_post", methods = ["POST"])
def create_post():
    if not post.Post.is_valid(request.form):
        return redirect("/wall")
    else:
        post_id = post.Post.add_post(request.form)
        return redirect("/wall")
    
@app.route("/comment", methods = ["POST"])
def create_comment():
    print(request.form)
    if not comment.Comment.is_valid(request.form):
        session["post_id"] = request.form["post_id"]
        print(session)
        return redirect("/wall")
    else:
        comment_id = comment.Comment.add_comment(request.form)
        return redirect("/wall")
    
@app.route("/delete_post", methods =["POST"])
def delete_post():
    post.Post.delete_post(request.form)
    return redirect("/wall")