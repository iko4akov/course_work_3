list_ = [1, 2, 3,4,5,8,7]

POSTS_PATH = "../data/posts.json"

def finded(x, list_):
    qwerty = []
    for index in list_:
        if x == index:
            qwerty.append(index)
            return x
    raise ValueError("yt njsfsdf")


print(finded(2, list_)
)
print(type(POSTS_PATH))