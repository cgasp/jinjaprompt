#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import re
import yaml, json
import logging
import jinja2
from jinja2.meta import find_undeclared_variables


def arg_parse():
    text_description="""
jinjaprompt script allow to generate straightforwardly jinja2 template. 
Prompt the user for unknown variable

Feature:
- Parse a jinja2 template & extract variables
- Prompt user for founded variable to enter data  
- If found a yaml or json file with same filename, propose variable as default
- Print rendered file, and optionally save the output 
"""

    parser = argparse.ArgumentParser(description=text_description, formatter_class=argparse.RawTextHelpFormatter)
	
    parser.add_argument('template', nargs='?', 
                        default='template.j2',
                        help='template file')
                        
    parser.add_argument('-p','--parameters', dest='parameters', 
                        action='store',type=str, 
                        help='parameter file')

    parser.add_argument('-o', dest='output', 
                        action='store',type=str, 
                        help='save output in a file')

    parser.add_argument('-v', dest='logging', 
                        action='store_true', 
                        help='debug log')

    return parser.parse_args()


def yes_or_no(question):
    # generic function for yes or no question for some task
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or
              answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False


def get_absolute_path(src_location, path):
    if os.path.isabs(path):
        return path
    else:
        dirname = os.path.dirname(src_location)
        absolute_path = os.path.join(dirname, path)
        return absolute_path


def parse_var_file(filename):
    # detect, open var file and return a dict with values 
    #
    template_basename = os.path.splitext(os.path.basename(filename))[0]
    
    accepted_ext = ['yml', 'yaml', 'json']

    for extension in accepted_ext:
        var_file = "{}.{}".format(template_basename, extension)
        # check file existence 
        if os.path.isfile(var_file):
                # Detect method to load
                if extension in ['yml', 'yaml']:
                    return yaml.safe_load(open(var_file))
                
                if extension in ['json']:
                    return json.load(open(var_file))
    return {}



def main():
    # Main function 
    
    # Argument parsing
    args = arg_parse()

    if args.logging:
        # debug mode
        logging_level = logging.DEBUG
    else:
        # normal mode
        logging_level = logging.INFO

    logging.basicConfig(format='[%(asctime)s](%(levelname)s) %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S', level=logging_level)

    # Check for variables 
    # instatiate jinja2
    loader = jinja2.FileSystemLoader(searchpath="./")
    env = jinja2.Environment(loader=loader, undefined=jinja2.DebugUndefined)
    template = env.get_template(args.template)
    # Render template without passing all variables
    rendered = template.render()
    # Check if rendering was done correctly
    parsed = env.parse(rendered)
    # Get undefined variables from jinj2.meta
    undefined = find_undeclared_variables(parsed)

    logging.debug("variable found in template \"{}\" : {}".format(args.template, undefined))
    

    # Load variable file 
    var = {}
    # if file defined
    if args.parameters: 
        var = parse_var_file(args.parameters) 
    else:
        var = parse_var_file(args.template) 
    
    if not var:
        logging.debug("var file not found/loaded")



    # Load data from user 
    for variable in undefined:
        if variable not in var:
            # variable have no Default 
            var[variable] = input("{{ {} }} : \t".format(variable))
        else:
            # variable has default
            new_value = input("{{ {} }} [{}]: \t".format(variable, var[variable]))
            # if given value it will update var, if none take the default
            if new_value != '':
                var[variable] = new_value

    # Render template without passing all variables
    rendered = template.render(var)

    print(rendered)
 
    if yes_or_no("\nDo you wish to save output in a file ? "):
        # markdown as default format 
        default_filename = "{}.md".format(os.path.splitext(os.path.basename(args.template))[0])
        filename = input("filename [{}]: ".format(default_filename))
        if filename == '':
            filename = default_filename
        with open(filename, "w") as f:
            f.write(rendered)
        

if __name__ == '__main__':
    main()