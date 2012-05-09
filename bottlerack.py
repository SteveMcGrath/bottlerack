#!/usr/bin/env python
from bottle import template, Bottle, run, redirect, static_file
import os, sys, getopt, markdown

app = Bottle()

help_message = '''USAGE: %s [OPTIONS]

BottleRack is a basic web application that leverages Markdown files and serves
them via any bottle-supported server connector.

Options:

-h/--host           Specifies the host paramever.  Default is 127.0.0.1

-p/--port           Specifies the port number.  Default is 8080.

-b/--base           Specifies the BottleRack Application location.  The default
                    is ./

-s/--server         Specified the server connector to use.  The default is 
                    wsgiref.

-c/--create         Creates an empty BottleRack application.

-q/--quiet          Tells the service to run quietly, no output.
''' % sys.argv[0]


default_home = '''
# New BottleRack application

This is the default home page.
'''


default_error = '''
## Error 404, Page Not found

This is not the page you are looking for...
'''


default_tmpl = '''
<html>
  <head>
    <title>Dummy Template</title>
  </head>
  <body>
    {{! content}}
  </body>
</html>
'''


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


@app.route('/')
def home_page():
    redirect('/home')


@app.route('/static/:filename#.+#')
def route_static_files(filename):
    return static_file(filename, root='static')


@app.route('/favicon.ico')
def get_repo_file():
    return static_file('images/favicon.ico', 'static')


@app.route('/:name#.+#')
def page(name):
    if os.path.exists(os.path.join('pages', '%s.md' % name)):
        filename = os.path.join('pages', '%s.md' % name)
    else:
        filename = os.path.join('pages', 'error.md')
    pfile = open(filename)
    mdpage = pfile.read()
    pfile.close()        
    return template('page', content=markdown.markdown(mdpage,
                    ['extra', 'codehilite(force_linenos=True)']))


def main(argv=None):
    # The main loop function.  This is were we parse all of the arguments
    # and startup the web service.
    server = 'wsgiref'
    host = '127.0.0.1'
    port = 8080
    quiet = False
    base = './'
    new_rack = False
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], 's:p:h:b:qc', ['server=',
                                                              'port=',
                                                              'host=',
                                                              'base=',
                                                              'quiet',
                                                              'create',
                                                              'help'])
        except getopt.error, msg:
            raise Usage(msg)

        for option, value in opts:
            if option in ('-s', '--server'):
                server = value
            if option in ('-p', '--port'):
                port = int(value)
            if option in ('-h', '--host'):
                host = value
            if option in ('-b', '--base'):
                base = value
            if option in ('-q', '--quiet'):
                quiet = True
            if option in ('-c', '--create'):
                new_rack = True
            if option in ('--help'):
                raise Usage(help_message)

    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2

    # If we are generating a new rack, then lets go ahead and build the basic
    # structure to graft the site onto.
    if new_rack:
        if not os.path.exists(base):
            os.mkdir(base)
        os.mkdir(os.path.join(base, 'pages'))
        os.mkdir(os.path.join(base, 'static'))
        os.mkdir(os.path.join(base, 'views'))

        # Write a default home page...
        home_page = open(os.path.join(base, 'pages', 'home.md'), 'w')
        home_page.write(default_home)
        home_page.close()

        # Write the default error page...
        error_page = open(os.path.join(base, 'pages', 'error.md'), 'w')
        error_page.write(default_error)
        error_page.close()

        # And lastly write the default template...
        tmpl = open(os.path.join(base, 'views', 'page.tpl'), 'w')
        tmpl.write(default_tmpl)
        tmpl.close()
        print 'Skeleton Structure created in %s' % base
        return

    # Now to change directories and start up the server ;)
    os.chdir(base)
    run(app, server=server, port=port, host=host, quiet=quiet)


if __name__ == '__main__':
    sys.exit(main)