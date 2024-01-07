from langchain.chains import create_sql_query_chain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
import dotenv
import os

dotenv.load_dotenv()    

# Access the environment variables
print(os.environ['username'])

pg_uri = f"postgresql+psycopg2://{os.environ['username']}:{os.environ['password']}@{os.environ['host']}:{os.environ['port']}/{os.environ['mydatabase']}"
print(pg_uri)

db = SQLDatabase.from_uri(pg_uri)
chain = create_sql_query_chain(ChatOpenAI(temperature=0), db)
response = chain.invoke({"question": "آدرس ایمیل فرزانه طاهری چیست؟"})
print(response) 