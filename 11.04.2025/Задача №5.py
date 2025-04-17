tag = input()
content = input()
def tagification(tag, content):
    valid_tags = {"a", "abbr", "b", "body", "caption", "cite", "code", "div", 
                  "form", "h1", "h2", "h3", "h4", "h5", "h6", "header", "i", "s"}
    if tag in valid_tags:
        return f"<{tag}>{content}</{tag}>"
    else:
        return "Введён неверный тег"

print(tagification(tag, content))