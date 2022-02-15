
# ASSUMPTIONS ===================================
# Users cannot create accounts, only update password thru forgot password
# Accounts are created by admin via script using data gathered
# 	- survey sampling > hand out google forms > process google sheets data
# 	- how will we select respondents? bulletin board? student list?

# STUFF TO DO (in order) ==========================================
# CONTINUE
# see existing extensions on model creation
# model validation substitute: https://pydantic-docs.helpmanual.io/usage/schema/#json-schema-types

	

# Quiz crud --> see python resources and other repo source code for reference
	# CURRENT (SEE DL): https://data-flair.training/blogs/create-quiz-application-python-django/
	# https://techvidvan.com/tutorials/quiz-web-app-python-django/
	# https://www.google.com/search?q=python+models+for+quiz+taking&oq=python+models+for+quiz+taking&aqs=chrome..69i57.6841j0j7&sourceid=chrome&ie=UTF-8

	# https://github.com/learningequality/kolibri/blob/release-v0.15.x/kolibri/core/exams/models.py
	# https://github.com/instructure/canvas-lms/blob/master/app/models/quizzes/quiz.rb
# Migrations - [Reads](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
# Admin crud (esp for accessing mouse statistics (?))
# App Settings/ Configurations for Development, Deployment etc.
# Password reset
# Extensions cleaning
	# https://python-gino.org/docs/en/1.0/tutorials/tutorial.html
		# GINO only supports dialect for postgresql
		# plan is to skip extension for async db and async testing so that 
		# team can focus on developing on top of existing backend with sqlite as db
		# kinda like developing a single user app first and then modifying for multiple user usage 
# Storing tokens in cookies
	# https://indominusbyte.github.io/fastapi-jwt-auth/usage/jwt-in-cookies/
	# https://www.fastapitutorial.com/blog/fastapi-jwt-httponly-cookie/

# fastapi docs   : https://fastapi.tiangolo.com/tutorial/body-multiple-params/
# fastapi tut    : https://www.fastapitutorial.com/blog/fastapi-route/
# sqlalchemy docs: https://docs.sqlalchemy.org/en/14/orm/session_basics.html#what-does-the-session-do
# vuejs tut      : https://v3.vuejs.org/guide/introduction.html#composing-with-components

# LEGEND:
# TODO - to do
# DOING - here here
# NOTE - remember me

from fastapi_tut import create_app
from fastapi_tut.commands import cli

app = create_app()

if __name__ == "__main__":
	cli()



# ======================================================
# API ENDPOINTS FOR ADMINISTERING ONLINE EXAMS (PROTOTYPE), WITH BUILT-IN CHEATING DETECTION
# ======================================================
'''
exam_app = FastAPI()

# Module 1: Landing 
@exam_app.get("/")
async def root():
	# [Module 4] if logged in as teacher, redirect to teacher's dashboard
	# [Module 5] if logged in as student, redirect to student's dashboard
	# else:
	return {"message": "Welcome!"}
	
# Module 2: Sign Up 
@exam_app.get("/signup")
async def signup():
	return {"message": "Sign Up"}	

# Module 3: Login 
@exam_app.get("/login")
async def login():
	return {"message": "Log In"}

# Module 6: [TEACHER] My Exams 
@exam_app.get("/exams")
async def my_exams():
	return {"message": "My Exams"}
	
# [TEACHER] [STUDENT]
@exam_app.get("/exams/{exam_id}")
async def read_exam(exam_id: int):
	return {"message": f"Exam {float(exam_id)}"}

@exam_app.get("/exams/create")
async def create_exam():
	return {"message": "Create Exam"}

# Module 7: [TEACHER] Reports 
@exam_app.get("/reports")
async def report():
	return {"message": "Reports"}

# Module 8: Update Profile
@exam_app.get("/profile/update")
async def update_profile():
	return {"message": "Profile"}

# Module 9: [STUDENT] Activities 
@exam_app.get("/activities")
async def report():
	return {"message": "Activities"}

'''



