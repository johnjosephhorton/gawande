gawande
=======
`gawande` is a command line tool for quickly exposing checklists from a library of markdown-formatted checklists; 
The idea is to lower the start-up costs of looking at your collection of checklists and adding a checklist to any project.
The project was inspired by the book ["The Checklist Manifesto: How to Get Things Right"](http://www.amazon.com/The-Checklist-Manifesto-Things-Right/dp/0312430000), by Atul Gawande. 

Installation
------------
Download the repository from git and then run the setup script: 
	
		git clone git@github.com:johnjosephhorton/gawande.git
		cd gawande 
		sudo python setup.py install 

Adding your own checklists 
--------------------------
The checklists themselves are stored as markdown files in `./checklists`. 
If you modify a checklist, for now, you need to re-run `setup.py install`

How to use
----------
When you run the command `gawande` without any arguments, it just lists the available checklists. 
To actually see a checklist, run: 

	gawande --checklist CHECKLIST_NAME

Doing this will just print the checklist to sdtout. 
Using the flag  `--md` will write the checklist as markdown file in the current director. 
The flag `--pdf`` will write the checklist as a LaTeX-generated pdf.  

License
-------
See `LICENSE` file. 
