#!/usr/bin/env python3

import argparse
import os
import pdb
import IPython

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def dump_data(destination_session, destination_engine, source_session, source_engine):
    source_table_list = source_engine.table_names()
    source_engine._metadata.reflect(source_engine) # get columns from existing table
    for source_table_name in source_table_list:
        source_table = sqlalchemy.Table(source_table_name, source_engine._metadata)
        destination_table = sqlalchemy.Table(source_table_name, destination_engine._metadata)
        #for column in source_table.columns:
        #    destination_table.append_column(column.copy())
        #Base = declarative_base()
        #tables = Base.metadata.tables;
        IPython.embed()
        #data = source_engine.execute(tables[source_table_name].select()).fetchall()
        #print('data=\n%s' % data)
        #if data:
        #    destination_engine(tables[source_table_name].insert(), data)
        destination_table.create()
                
        
def main():
    parser = argparse.ArgumentParser('merge an arbitrary number of sqlite files')
    parser.add_argument('-s', '--source_sqlite', action='append', required=True)
    parser.add_argument('-u', '--uuid', required=True)
    args = parser.parse_args()
    
    source_sqlite_list = args.source_sqlite
    uuid = args.uuid
    
    destination_sqlite = uuid+'.db'
    destination_engine_path = 'sqlite:///' + destination_sqlite
    destination_engine = sqlalchemy.create_engine(destination_engine_path, isolation_level='SERIALIZABLE')
    destination_Session = sessionmaker(bind=destination_engine)
    destination_session = destination_Session()
    destination_engine._metadata = sqlalchemy.MetaData(bind=destination_engine)
    
    for source_sqlite in source_sqlite_list:
        print('source_sqlite=%s' % source_sqlite)
        source_engine_path = 'sqlite:///' + source_sqlite
        source_engine = sqlalchemy.create_engine(source_engine_path, isolation_level='SERIALIZABLE')
        source_Session = sessionmaker(bind=source_engine)
        source_session = source_Session()
        source_engine._metadata = sqlalchemy.MetaData(bind=source_engine)
        dump_data(destination_session, destination_engine, source_session, source_engine)
        
        


if __name__ == '__main__':
    main()
