gawande
=======

`gawande` is a command line tool for quickly exposing checklists from a library of checklists; 
The idea is to lower the start-up costs of looking at your checklists. 
The project was inspired by the book ["The Checklist Manifesto: How to Get Things Right"](http://www.amazon.com/The-Checklist-Manifesto-Things-Right/dp/0312430000), by Atul Gawande. 

The checklists themselves are stored as markdown files in `./checklists`. 
Depending upon command line arguments, the checklist can written as plain text to stdout, to a markdown file or a pdf if [pandoc](http://johnmacfarlane.net/pandoc/) is present.  

How to use
----------

Make the scipt access by adding it to a directory in your path via a symlink: 

	git clone git@github.com:johnjosephhorton/gawande.git
	ln -s gawande/gawande.py /usr/local/bin
	
When you run the command `gawande.py` without any arguments, it just lists the available checklists. 
To actually see a checklist, run: 

	gawande.py --checklist CHECKLIST_NAME

Doing this will just print the checklist to sdtout. 
Using the flag  `--md` will write the checklist as markdown file in the current director. 
The flag `--pdf`` will write the checklist as a LaTeX-generated pdf.  

License
-------
See `LICENSE` file. 
