# -*- coding: utf-8 -*-

from calendar import monthrange
from datetime import datetime, timedelta
from os import path, getcwd, makedirs, listdir, remove
from yaml import load
from shutil import rmtree
from staticjinja import make_site

# We define constants for the deployment.
_SEARCHPATH = path.join(getcwd(), 'templates')
_OUTPUTPATH = path.join(getcwd(), 'site')

# We load the data we want to use in the templates.
_DATA = load(open('data/data.yaml'))

# Setting some Global Vars
START_GANTT = '6-1-2015'
END_GANTT = '8-31-2016'
GANTT_SPAN = 427
COL_WIDTH = 6


# Converting strings into date objects
def convert_to_time(date):
    return datetime.strptime(date, '%m-%d-%Y')

# Getting the timespan between 2 dates (IN DAYS)
def get_timespan(start_date, end_date):
    start = convert_to_time(start_date)
    end = convert_to_time(end_date)

    timespan = end - start

    return timespan.days

def get_month_delta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta

# GANTT_SPAN = get_timespan(START_GANTT, END_GANTT)
# print '==================', GANTT_SPAN, '=================='

def load_data():
    ctx = {'data': _DATA}
    return ctx

def enhance_data():
    # tasks = ctx['data']['phases'][0]['stages'][0]['categories'][0]['tasks'][]

    ctx = load_data()

    phases = ctx['data']['phases']

    start_gantt = convert_to_time(START_GANTT)
    end_gantt = convert_to_time(END_GANTT)

    for phase in phases:
        stages = phase['stages']
        
        for stage in stages:
            categories = stage['categories']
            
            for category in categories:
                tasks = category['tasks']
                category['length'] = len(tasks)

                for task in tasks:
                    task['start_date_obj'] = convert_to_time(task['start_date'])
                    task['end_date_obj'] = convert_to_time(task['end_date'])
                    task['months_from_start'] = get_month_delta(start_gantt, task['start_date_obj'])
                    task['left'] = task['months_from_start'] * COL_WIDTH
                    task['timespan'] = (get_month_delta(task['start_date_obj'], task['end_date_obj']) +1) * COL_WIDTH
                    

    return ctx

if __name__ == '__main__':
    site = make_site(
        filters={},
        outpath=_OUTPUTPATH,
        contexts=[(r'.*.html', enhance_data)],
        searchpath=_SEARCHPATH,
        staticpaths=['static', '../data']
    )

    # cleanup()

    site.render(use_reloader=True)
