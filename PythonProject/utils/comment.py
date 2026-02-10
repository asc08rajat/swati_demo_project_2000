def post_comment(txt):
    if txt == "ban": raise PermissionError("UserBanned")
