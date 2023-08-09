# name = "Nitish"
# age = 25
# print("My name is %s and I'm %d years old."%(name, age))



# name = "Nitish"
# age = 25
# print("My name is {} and I'm {} years old.".format(name, age))


# name = "Nitish"
# age  = 25
# print(f"My name is {name} and I'm {age} years old.")

#best ai tools
# solves anything - chart gpt
# writes anything - writesonic
# generates art - midjourney
# generates code - replit
# generates video - synthesia
# generates music - soundraw
# generates tiktoks - fliki
# generates avatars - starrytars
# generates ppts - slides ai
# edits pictures - remini
# edit videos - pictory
# summarize notes - wordtune

# user(classes and objects)

"""class User:
    def __init__(self, user_email, name, password, current_job_title):
    
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title


    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")
            
app_user_one = User("mercy.com", "mercy k", "pdw1", "data analyst")
app_user_one.get_user_info()

app_user_one.change_job_title("devOps trainer")
app_user_one.get_user_info()

#posts

class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def get_post_info(self):
        print(f"Post: {self.message} written by {self.author}")

new_post = Post("on a secret mission today", app_user_one.name) 
new_post.get_post_info()"""     


import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n")



    x = 10
    x += 12
    y = int(x/4)
    x = x + y

    print(x, y)


