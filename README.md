# [SQLDatabaseChain]

[SQLDatabaseChain] is a Python application that leverages Langchain to enable natural language querying of PostgreSQL databases. This tool allows users to interact with their PostgreSQL databases using simple, conversational queries, making data retrieval more intuitive and accessible.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- Langchain

### Installation

1. **Clone the Repository**

   ```bash
   git clone git@github.com:farzaneh74/SQLDatabaseChain.git
   cd SQLDatabaseChain
2. **Set Up a PostgreSQL Database**
3. 
   CREATE DATABASE your_database_name;
   
   CREATE TABLE person(  pid SERIAL             PRIMARY KEY,
                              name CHARACTER VARYING,
                         givenname CHARACTER VARYING,
                        familyname CHARACTER VARYING,
                    additionalname CHARACTER VARYING,
                             email CHARACTER VARYING);
5. **Install Dependencies**
   pip install -r requirements.txt

6. **Running the Application**
   python text-to-sql-query.py
   
