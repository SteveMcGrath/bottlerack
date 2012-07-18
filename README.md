# What is BottleRack?

Bottlerack is a simplistic way to stand up a website utilizing markdown files for page content and using a standard template for theming the website.  This means that building a simple website is just a matter of creating a new "rack" and then modifying as you see fit.

# Getting Started

## Quickstart

1. Install bottlerack by using pip or easy_install: 
   `pip install bottlerack`
2. Create a new "rack" using the bottlerack application: 
   `bottlerack -b testapp -c`
3. Startup bottlerack using the rack you just created: 
   `bottlerack -b testapp`
4. Your done!  you not have a running bottlerack application!

## Adding pages

To add a page to your rack, just create a new markdown file in the pages folder.
By default, bottlerack should have created the home.md and error.md files to
facilitate in the basic application.  home.md is markdown file that is called
when you reference the webroot "/" and error.md is used to display a 404 message
whenever there is no page to be displayed.  You can setup your markdown files
in whatever directory structure you wish, and those will be carried over to the
web application.  So for example, if I had the following directory structure in
my pages folder:

	home.md
	error.md
	presentations.md
	presentations/pres1.md
	presentations/pres2.md

The URLs that would be available in the web application would be:

	/
	/presentations
	/presentations/pres1
	/presentations/pres2

It can't get any simpler than that.  One thing to keep in mind is that it is
required for markdown files to be named with the .md extension.

## Adding a Blog

Bottlerack also supports a simple blogging system as well utilizing the same
methods for creating pages.  To enable blogging support, simply create a new
folder in you rack with the name of "blog" alongside your pages folder.  THe
blog sorting order is based on creation time of the markdown file.  The /blog
URL will present a list of the blog items in descending order (newest at the
top) with a link to the individual items as well as displaying the title (the
file name) that was specified.