import psycopg2
import pymongo
from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
from postgres_titanic_queries import *
from mongodb_rpg_data_queries import *

# load .env file
load_dotenv()

# get variables for mongodb connection
MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_DBNAME = os.getenv("MONGODB_NAME")

# get variables for postgres connection
AIVEN_DB_USER = os.getenv("AIVEN_DB_USER")
AIVEN_DB_NAME = os.getenv("AIVEN_DB_NAME")
AIVEN_DB_PASSWORD = os.getenv("AIVEN_DB_PASSWORD")
AIVEN_DB_HOST = os.getenv("AIVEN_DB_HOST")
AIVEN_DB_PORT = os.getenv("AIVEN_DB_PORT")

# open connection to MongoDB
def create_mdb_conn(user, password, dbname):
    client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@ds-unit-3-sprint-10-mod.pxenxpb.mongodb.net/{dbname}?retryWrites=true&w=majority&appName=ds-unit-3-sprint-10-module-3")
    # db and collection we want to connect to
    db = client[dbname]
    return db

# open connection to postgres
# pg_conn = f"postgresql+psycopg2://{AIVEN_DB_USER}:{AIVEN_DB_PASSWORD}@{AIVEN_DB_HOST}:{AIVEN_DB_PORT}/{AIVEN_DB_NAME}?sslmode=require"
# pg_engine = create_engine(pg_conn)

# generic postgres query function
def execute_postgres_query(query, engine):
    df = pd.read_sql_query(query, engine)
    return df

# main file
if __name__ == '__main__':
    # execute postgres queries
    print('Executing postgres queries')
    try:
        # print("How many passengers survived, and how many died?")
        # print(execute_postgres_query(GET_PASSENGERS_SURVIVED_AND_DIED, pg_engine))

        # print("How many passengers were in each class?")
        # print(execute_postgres_query(GET_PASSENGERS_IN_EACH_CLASS, pg_engine))

        # print("How many passengers survived/died within each class?")
        # print(execute_postgres_query(GET_PASSENGERS_SURVIVED_DIED_BY_CLASS, pg_engine))

        # print("What was the average age of survivors vs nonsurvivors?")
        # print(execute_postgres_query(GET_AVG_AGE_OF_SURVIVORS_NONSURVIVORS, pg_engine))

        # print("What was the average age of each passenger class?")
        # print(execute_postgres_query(GET_AVG_AGE_OF_EACH_PASSENGER_CLASS, pg_engine))

        # print("What was the average fare by passenger class? By survival?")
        # print(execute_postgres_query(GET_AVG_FARE_BY_CLASS_AND_SURVIVAL, pg_engine))

        # print("How many siblings/spouses aboard on average, by passenger class? By survival?")
        # print(execute_postgres_query(GET_SIBLINGS_SPOUSES_ABOARD_BY_CLASS_AND_SURVIVAL, pg_engine))

        # print("How many parents/children aboard on average, by passenger class? By survival?")
        # print(execute_postgres_query(GET_PARENTS_CHILDREN_ABOARD_BY_CLASS_AND_SURVIVAL, pg_engine))

        # print("Do any passengers have the same name?")
        # print(execute_postgres_query(GET_PASSENGERS_WITH_SAME_LAST_NAME, pg_engine))
        
        # print('All postgres queries executed successfully')

        mongdb = create_mdb_conn(MONGODB_USER, MONGODB_PASSWORD, MONGODB_DBNAME)

        print("How many total Characters are there?")
        print(count_rpg_characters(mongdb))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        pass