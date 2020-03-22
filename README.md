# Table of Contents

- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

# Description

jinjaprompt script allow to generate straightforwardly jinja2 template. 
Prompt the user for unknown variable

Feature:
- Parse a jinja2 template & extract variables
- Prompt user for founded variable to enter data  
- If found a yaml or json file with same filename, propose variable as default
- Print rendered file, and optionally save the output 

Similar: 
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter): great for projects structure, doesn't fit for single files
- [j2cli](https://github.com/kolypto/j2cli): great tool. need to provide the variable on a file, doesn't prompt. 
- [cookie](https://github.com/bbugyi200/cookie): great script, however need some configuration and template managment. 


# Installation

Clone repository, install the module. 

```
git clone https://github.com/cgasp/jinjaprompt
cd jinjaprompt/
pip3 install . 
```

# Usage

Render a template file  

`jinjaprompt template.j2`  

Save output  

`jinjaprompt template.j2 -o new-file.md`  


# Support

Please [open an issue](https://github.com/cgasp/jinjaprompt/issues/new) for support.

# Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/).  
Create a branch, add commits, and [open a pull request](https://github.com/cgasp/jinjaprompt/compare).  