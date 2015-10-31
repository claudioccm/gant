from datetime import *
from os import path, getcwd, makedirs, listdir, remove
from yaml import load
from shutil import rmtree
from staticjinja import make_site

# We load the data we want to use in the templates.
# _DATA = load(open('data/data.yaml'))

def convert_to_time(date):
    return datetime.strptime(date, '%m-%d-%Y')


# def get_timespan(start_date, end_date):
#     # start = convert_to_time(start_date)
#     # end = convert_to_time(end_date)

#     timespan = end_date - start_date

#     return timespan.days

# # print get_timespan(task['start_date'], task['end_date'])



# def load_data():
#     ctx = {'data': _DATA}
#     dic = {}

#     return ctx
#     # return tasks

# ctx = load_data()

# def enhance_data():
#     # tasks = ctx['data']['phases'][0]['stages'][0]['categories'][0]['tasks'][]

#     phases = ctx['data']['phases']


#     start_gantt = convert_to_time('1-1-2016')
#     end_gantt = convert_to_time('1-1-2016')

#     for phase in phases:
#         stages = phase['stages']
        
#         for stage in stages:
#             categories = stage['categories']
            
#             for category in categories:
#                 tasks = category['tasks']
#                 category['length'] = len(tasks)

#                 for task in tasks:
#                     # converting strings into datetime obj
#                     task['start_date'] = convert_to_time(task['start_date'])
#                     task['end_date'] = convert_to_time(task['end_date'])
                    

#                     if task['start_date'] < start_gantt:
#                         start_gantt = task['start_date']

#                     if task['end_date'] > end_gantt:
#                         end_gantt = task['end_date']

#                     task['timespan'] = get_timespan(task['start_date'], task['end_date'])
#                     task['days_from_start'] = get_timespan(task['start_date'], start_gantt)

#     return ctx

# enhance_data()

# # print ctx['data']['phases'][0]['stages'][0]['categories'][0]['length']
# print ctx


my_date = '6-1-2015'
my_date2 = '8-30-2015'

test = convert_to_time(my_date)
test2 = convert_to_time(my_date2)
test3 = test2 - test

print test.month
print test2.month
print test3.month















