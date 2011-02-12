"""
Week5 Assignment
"""

# Import namespaces
import cherrypy
from bookdb import BookDB
import os.path
from Cheetah.Template import Template

siteconf = os.path.join(os.path.dirname(__file__), 'site.conf')

class BookDBList:

    @cherrypy.expose
    def index(self):
	booksdb = BookDB()        

        template = Template('''
	    <h1>BookList</h1>
            <p>Click on a title for details</p>
            <hr>
            #for $book in $booksdb.titles()
                <a href="./detail?id=$book.id">$book.title<br>
            #end for
        ''', [locals(), globals()])
        return template.respond()


    @cherrypy.expose
    def detail(self, id):
        books = BookDB()
        bookdet = books.title_info(id)
        template = Template('''
            <h1>Book Details</h1><hr>
               <h2>Title: $bookdet['title']</h2><br> 
               <b>ISBN:</b> $bookdet['isbn']<br>
               <b>Publisher:</b> $bookdet['publisher']<br>
               <b>Author:</b> $bookdet['author']<br><br>
            <a href="./">Return to List</a>
        ''', [locals(), globals()])
        return template.respond()

if __name__ == '__main__':
    cherrypy.quickstart(BookDBList(), config=siteconf)
