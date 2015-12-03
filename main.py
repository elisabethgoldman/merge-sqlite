#!/usr/bin/env python3

import argparse
#import os
import sqlite3
import IPython


def get_row_str(source_tuple):
    source_list = list(source_tuple)
    new_str = str()
    for i, source_field in enumerate(source_list):
        source_field_str = str(source_field).strip()
        if source_field == None:
            new_str += '\'\','
        elif type(source_field) is str:
            new_str += '"'+str(source_field)+'"'+','
        else:
            new_str += str(source_field)+','
    new_str = new_str.rstrip(',')
    return new_str


def main():
    parser = argparse.ArgumentParser('merge an arbitrary number of sqlite files')
    parser.add_argument('-s', '--source_sqlite', action='append', required=True)
    parser.add_argument('-u', '--uuid', required=True)
    args = parser.parse_args()
    
    source_sqlite_list = args.source_sqlite
    uuid = args.uuid
    
    destination_sqlite_path = uuid+'.db'
    destination_conn = sqlite3.connect(destination_sqlite_path)
    destination_cur = destination_conn.cursor()
    
    for source_sqlite_path in source_sqlite_list:
        source_conn = sqlite3.connect(source_sqlite_path)
        source_cur = source_conn.cursor()
        source_cur.execute('SELECT * from sqlite_master')
        source_master = source_cur.fetchall()
        source_tables = list(filter(lambda r: r[0] == 'table', source_master))
        for source_table in source_tables:
            destination_cur.execute(source_table[4]) #4 is sql
            cursor = source_cur.execute('select * from %s' % source_table[1]) # 1 is name
            names = tuple(map(lambda x: x[0], cursor.description))
            for source_row in source_cur:
                phold = ','.join(('?',) * len(source_row))
                query = 'INSERT INTO %(tbl)s %(col)s VALUES (%(phold)s)' % {
                    'tbl' : source_table[1], # 1 is name
                    'col' : names,
                    'phold' : phold
                    }
                destination_cur.execute(query, source_row)
                destination_conn.commit()
                                        
if __name__ == '__main__':
    main()
