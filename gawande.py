#!/usr/bin/env python

import argparse 
import os 
from jinja2 import Environment, PackageLoader 

__author__ = 'John Joseph Horton, utapyngo'
__copyright__ = 'Copyright (C) 2012  John Joseph Horton'
__license__ = 'GPL v3'
__maintainer__ = 'johnjosephhorton'
__email__ = 'john.joseph.horton@gmail.com'
__status__ = 'Development'
__version__ = '0.1'

env = Environment(loader=PackageLoader('gawande', 'checklists'))

def main():
    parser = argparse.ArgumentParser(description = "Quick access to checklists.")
    parser.add_argument("--checklist", help = "Checklist name") 
    parser.add_argument("--pdf", action = "store_true", default = False, help = "Create a pdf of the checklist in the current directory")
    parser.add_argument("--md", action = "store_true", default = False, help = "Store a markdown of the checklist in the current directory")
    args = parser.parse_args()
    if args.checklist: 
        checklist_name = args.checklist
        checklist_text = env.get_template(args.checklist + ".md").render()
        if args.pdf or args.md: 
            f = open("%s.md" % checklist_name, "w")
            f.write(checklist_text)
            f.close()
            os.system("pandoc -o %s.pdf %s.md" % (checklist_name, checklist_name))
            print("Wrote %s.pdf in current directory" % checklist_name)
            if args.md:
                print("Wrote %s.md in current directory" % checklist_name)
            else:
                os.remove("%s.md" % checklist_name)
        else:
            print(checklist_text)
    else: 
        print("""\nAvailable checklists:\n---------------------""")
        for checklist in os.listdir("./checklists"):           
            print("\t " + checklist.replace(".md", ""))
        print("\n\nTo see checklist, run gawande.py --checklist CHECKLIST_NAME")
          
if __name__ == '__main__':
    main() 

