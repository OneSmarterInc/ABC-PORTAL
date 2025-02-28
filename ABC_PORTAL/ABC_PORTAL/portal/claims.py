import pyodbc
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG)



def fetch_claims_data_for_clmp():
    host = '104.153.122.227'
    port = '23'
    database = 'S78F13CW'
    user = 'ONEPYTHON'
    password = 'pa33word'

    connection_string = (
        f"DRIVER={{iSeries Access ODBC Driver}};"
        f"SYSTEM={host};"
        f"PORT={port};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password};"
        f"PROTOCOL=TCPIP;"
    )

    schema_name = 'OOEDF'
    table_name = 'CLMHP'
    try:
        connection = pyodbc.connect(connection_string)
        print("Connected to the database.")
        cursor = connection.cursor()

        select_query = f"SELECT * FROM {schema_name}.{table_name}"
        cursor.execute(select_query)

        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]  
        df = pd.DataFrame.from_records(rows, columns=columns)  
        needed_df = df[['CHCLM#','CHPCLM','CHSSN','CHFRDY','CHFRDM','CHFRDD',"CHADPN", "CHCLM$", "CHPAY$", "CHMEM$", "CHSTTY","CHCLTP"]]
        needed_df['DATE'] = needed_df[['CHFRDM', 'CHFRDD', 'CHFRDY']].astype(str).agg('/'.join, axis=1)
        needed_df.drop(columns=['CHFRDM', 'CHFRDD', 'CHFRDY'],inplace=True)
        return needed_df

    except Exception as e:
        print(f"Error: {e}")
        logging.error(e)
        return None

    finally:
        if connection:
            connection.close()
            print("Database connection closed.")


def fetch_claims_data_for_member_using_ssn(chssn_value):
    host = '104.153.122.227'
    port = '23'
    database = 'S78F13CW'
    user = 'ONEPYTHON'
    password = 'pa33word'

    connection_string = (
        f"DRIVER={{iSeries Access ODBC Driver}};"
        f"SYSTEM={host};"
        f"PORT={port};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password};"
        f"PROTOCOL=TCPIP;"
    )

    schema_name = 'OOEDF'
    table_name = 'CLMHP'
    try:
        connection = pyodbc.connect(connection_string)
        print("Connected to the database.")
        cursor = connection.cursor()

        select_query = f"SELECT * FROM {schema_name}.{table_name} WHERE CHSSN = ?"
        cursor.execute(select_query, (chssn_value,))

        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description] 
        df = pd.DataFrame.from_records(rows, columns=columns)  

        ndf = df[["CHADPN", "CHDIAG", "CHDIA2", "CHDIA3", "CHDIA4", "CHDIA5",'CHCLM#','CHFRDY','CHFRDM','CHFRDD',"CHCLM$", "CHSTTY","CHCLTP",'CHPLAN','CHBNFT']]
        ndf['DATE'] = ndf[['CHFRDM', 'CHFRDD', 'CHFRDY']].astype(str).agg('/'.join, axis=1)
        ndf.drop(columns=['CHFRDM', 'CHFRDD', 'CHFRDY'],inplace=True)
        return ndf

    except Exception as e:
        print(f"Error: {e}")
        logging.error(e)
        return None

    finally:
        if connection:
            connection.close()
            print("Database connection closed.")

def fetch_claims_data_using_claim_no(claim_number):
    host = '104.153.122.227'
    port = '23'
    database = 'S78F13CW'
    user = 'ONEPYTHON'
    password = 'pa33word'

    connection_string = (
        f"DRIVER={{iSeries Access ODBC Driver}};"
        f"SYSTEM={host};"
        f"PORT={port};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password};"
        f"PROTOCOL=TCPIP;"
    )

    schema_name = 'OOEDF'
    table_name = 'CLMDP'
    try:
        connection = pyodbc.connect(connection_string)
        print("Connected to the database.")
        cursor = connection.cursor()

       
        select_query = f"SELECT * FROM {schema_name}.{table_name} WHERE CDCLM# = ?"
        cursor.execute(select_query, (claim_number,))

        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]  
        df = pd.DataFrame.from_records(rows, columns=columns)  
        ndf = df[["CDCLM#","CDFRDY", "CDFRDM", "CDFRDD", "CDTODY", "CDTODM", "CDTODD", "CDBNCD", "CDAPTC", "CDCPT#", "CDCPTM", "CDCHG$", "CDNPC$", "CDPAY$"]]
        ndf['FROM DATE'] = ndf[['CDFRDM', 'CDFRDD', 'CDFRDY']].astype(str).agg('/'.join, axis=1)
        ndf.drop(columns=['CDFRDM', 'CDFRDD', 'CDFRDY'],inplace=True)
        ndf['TO DATE'] = ndf[['CDTODM', 'CDTODD', 'CDTODY']].astype(str).agg('/'.join, axis=1)
        ndf.drop(columns=['CDTODM', 'CDTODD', 'CDTODY'],inplace=True)
        print(ndf)
      
        return df

    except Exception as e:
        print(f"Error: {e}")
        logging.error(e)
        return None

    finally:
        if connection:
            connection.close()
            print("Database connection closed.")

