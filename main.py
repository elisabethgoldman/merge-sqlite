#!/usr/bin/env python3

import argparse
import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker

def dump_data(output_session, output_engine, input_session, input_engine):
    input_table_list = input_engine.table_names()
    input_engine._metadata.reflect(input_engine) # get columns from existing table
    for input_table_name in input_table_list:
        input_table = sqlalchemy.Table(input_table_name, input_engine._metadata)
        output_table = sqlalchemy.Table(input_table_name, output_engine._metadata)
        for column in input_table.columns:
            output_table.append_column(column.copy())
        output_table.create()

        
def main():
    parser = argparse.ArgumentParser('merge an arbitrary number of sqlite files')
    parser.add_argument('-i', '--input_sqlite', action='append', required=True)
    parser.add_argument('-u', '--uuid', required=True)
    args = parser.parse_args()
    
    input_sqlite_list = args.input_sqlite
    uuid = args.uuid
    
    output_sqlite = uuid+'.db'
    output_engine_path = 'sqlite:///' + output_sqlite
    output_engine = sqlalchemy.create_engine(output_engine_path, isolation_level='SERIALIZABLE')
    output_Session = sessionmaker(bind=output_engine)
    output_session = output_Session()
    output_engine._metadata = sqlalchemy.MetaData(bind=output_engine)
    
    for input_sqlite in input_sqlite_list:
        input_engine_path = 'sqlite:///' + input_sqlite
        input_engine = sqlalchemy.create_engine(input_engine_path, isolation_level='SERIALIZABLE')
        input_Session = sessionmaker(bind=input_engine)
        input_session = input_Session()
        input_engine._metadata = sqlalchemy.MetaData(bind=input_engine)
        dump_data(output_session, output_engine, input_session, input_engine)
        
        


if __name__ == '__main__':
    main()
