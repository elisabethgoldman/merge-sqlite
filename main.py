#!/usr/bin/env python3

import argparse
#import os
import sqlite3
import IPython


def get_row_str(source_tuple):
    source_list = list(source_tuple)
    #print('source_lst=%s' % str(source_list))
    #print('len(source_list)==%s' % len(source_list))
    new_str = str()
    for i, source_field in enumerate(source_list):
        source_field_str = str(source_field).strip()
        #print('source_field, source_type=%s, %s' % (str(source_field), type(source_field)))
        if source_field == None:
            #print('None: %s' % source_field)
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
        print('source_master=%s' % source_master)
        source_tables = list(filter(lambda r: r[0] == 'table', source_master))
        print('source_tables=%s' % list(source_tables))
        print('len(source_tables)=%s' % len(source_tables))
        for source_table in source_tables:
            #print('source_table=%s' % str(source_table))
            #IPython.embed()
            # create table structure
            destination_cur.execute(source_table[4]) #4 is sql
            # move data
            #source_cols = source_table[4]
            #print('source_cols=%s' % source_cols)
            cursor = source_cur.execute('select * from %s' % source_table[1]) # 1 is name
            names = tuple(map(lambda x: x[0], cursor.description))
            #print('names=%s' % str(names))
            for source_row in source_cur:
                phold = ','.join(('?',) * len(source_row))
                #print('phold=%s' % phold)
                #print('str(source_row)=%s' % str(source_row))
                #print('str(source_row)=%s' % type(source_row))
                source_tuple = eval('(' + str(source_row).strip('(').strip('(').strip(')').strip(')') + ')')
                source_str = str(source_row).strip('(').strip('(').strip(')').strip(')')
                #print('source_tpl=%s' % str(source_tuple))
                #print('new_str=%s' % new_str)
                #new_str = get_row_str(source_tuple)
                query = 'INSERT INTO %(tbl)s %(col)s VALUES (%(phold)s)' % {
                    'tbl' : source_table[1], # 1 is name
                    'col' : names,
                    'phold' : phold
                    }
                #print('query=%s' % query)
                destination_cur.execute(query, source_row)
                destination_conn.commit()
                                        
if __name__ == '__main__':
    main()
