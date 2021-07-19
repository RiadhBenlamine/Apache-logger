import multiprocessing
import threading
import json
import sys
import re
import datetime
from excpetions import KeyNotFound

class TemplateEngine(threading.Thread):
    #encoding = 'utf-16' if sys.platform == 'win32' else 'utf-8'
    def __init__(self, template_path):
        self.template_path = template_path
        self.template = None
        self.counter = 0

    def load_json(self):
        try:
            with open(self.template_path, 'r', encoding='utf-8') as json_:
                template_object = json.loads(json_.read())
            return template_object
        except json.decoder.JSONDecodeError as error:
            print(f'AL>{error}')
            sys.exit(1)
        except FileNotFoundError as error:
            print(f'AL>{error}')
            sys.exit(1)
    
    def templete_check(self, template_object):
        try:
            description = template_object['description']
            points = template_object['points']
        except KeyError as error:
            print(f'AL>{error}')

        for key in ['template_name', 'author', 'description']:
            if key not in description:
                raise KeyNotFound(
                    'one or more keys are missing, make sure you have this keys "template_name" and "author" are in this template.'
                    )
                sys.exit(1)
        for key in ['host', 'request', 'agent', 'referrer', 'status', 'time', 'user', 'size']:
            if key not in points:
                    raise KeyNotFound('one or more keys are missing in this template.')
                    sys.exit(1)
        return True
    
    def analyze(self, entry):
        for item in self.template['points']:
            if self.template['points'][item] != False:
                if re.match(self.template['points'][item], entry[item]):
                    return entry
                    self.counter += 1


    def run(self):
        print('Loading template...')
        template_object = self.load_json()
        print('Running checks...')
        if self.templete_check(template_object):
            print(f'Template name: {template_object["description"]["template_name"]}')
            print(f'Author: {template_object["description"]["author"]}')
            self.template = template_object
            return self.analyze
        else:
            print('Invalid template.')

class FileEngine(multiprocessing.Process):
    def __init__(self, log_file):
        self.log_file = log_file

    def open_log(self):
        with open(self.log_file) as _ :
            log = _.read().split('\n')
        del log[-1]
        return log

    def log_parser(self, log_list):
        parts = [
            r'(?P<host>\S+)',                   # host %h
            r'\S+',                             # indent %l (unused)
            r'(?P<user>\S+)',                   # user %u
            r'\[(?P<time>.+)\]',                # time %t
            r'"(?P<request>.*)"',               # request "%r"
            r'(?P<status>[0-9]+)',              # status %>s
            r'(?P<size>\S+)',                   # size %b (careful, can be '-')
            r'"(?P<referrer>.*)"',              # referrer "%{Referer}i"
            r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
        ]
        entries = []
        pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
        for line in log_list:
            entries.append(pattern.match(line).groupdict())
        return entries
    
    def run(self):
        return self.log_parser(self.open_log())
        print('Log opened')