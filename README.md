# CnblogsExport

CnblogsExport is a tool for exporting your blogs in [cnblogs.com](cnblogs.com). It's always a good behavior to backup your blog files. Another hand, cnblogs.com couldn't offer an efficient reading experience on mobile devices. That's why I need this tool to export my blog files and maybe migrate to another platform.

Note: I use markdown syntax to write my blogs.

## CnblogsXmlExport(recommended)

first of all, you need to export your blogs in cnblogs.com management platform. Thus, you will get a cnblogs backup xml file.

### usage

```text
# ./CnblogsXmlExport.py -h
usage: CnblogsXmlExport.py [-h] [-o OUTPUT] xmlFile

positional arguments:
  xmlFile               cnblogs backup xml file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        specify the output directory
```

## CnblogsWebExport

> *Note: This tool is still under construction*

### installation

please refer to [selenium webdriver installation guide](http://selenium-python.readthedocs.io/installation.html) to build up your development environment. 

### usage

1. Copy `config.json.example` file and rename it to `config.json`. 
2. Modify the userInfo field(necessary) according to your cnblogs.com account. 
3. You can specify outputDir field. 
4. WebDriver field must be set to what you installed.
