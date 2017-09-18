from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Lesson 1
from database_setup import Base, ItemType, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///item.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            # Objective 3 Step 2 - Create /items/new page
            if self.path.endswith("/items/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Item</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/items/new'>"
                output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Item' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></html></body>"
                self.wfile.write(output)
                return
            if self.path.endswith("/edit"):
                itemIDPath = self.path.split("/")[2]
                myItemQuery = session.query(ItemType).filter_by(
                    id=itemIDPath).one()
                if myItemQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>"
                    output += myItemQuery.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action = '/items/%s/edit' >" % ItemIDPath
                    output += "<input name = 'newItemName' type='text' placeholder = '%s' >" % myItemQuery.name
                    output += "<input type = 'submit' value = 'Rename'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
            if self.path.endswith("/delete"):
                itemIDPath = self.path.split("/")[2]

                myItemQuery = session.query(ItemType).filter_by(
                    id=itemIDPath).one()
                if myItemQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete %s?" % myItemQuery.name
                    output += "<form method='POST' enctype = 'multipart/form-data' action = '/items/%s/delete'>" % itemIDPath
                    output += "<input type = 'submit' value = 'Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)

            if self.path.endswith("/items"):
                items = session.query(ItemType).all()
                output = ""
                # Objective 3 Step 1 - Create a Link to create a new menu item
                output += "<a href = '/items/new' > Make a New Item Here </a></br></br>"

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                for item in items:
                    output += item.name
                    output += "</br>"
                    # Objective 2 -- Add Edit and Delete Links
                    # Objective 4 -- Replace Edit href

                    output += "<a href ='/items/%s/edit' >Edit </a> " % item.id
                    output += "</br>"
                    # Objective 5 -- Replace Delete href
                    output += "<a href ='/items/%s/delete'> Delete </a>" % item.id
                    output += "</br></br></br>"

                output += "</body></html>"
                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    # Objective 3 Step 3- Make POST method
    def do_POST(self):
        try:
            if self.path.endswith("/delete"):
                itemIDPath = self.path.split("/")[2]
                myItemQuery = session.query(ItemType).filter_by(
                    id=itemIDPath).one()
                if myItemQuery:
                    session.delete(myItemQuery)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/items')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newItemName')
                    itemIDPath = self.path.split("/")[2]

                    myItemQuery = session.query(ItemType).filter_by(
                        id=itemIDPath).one()
                    if myItemQuery != []:
                        myItemQuery.name = messagecontent[0]
                        session.add(myItemQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/items')
                        self.end_headers()

            if self.path.endswith("/items/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newItemName')

                    # Create new ItemType Object
                    newItem = ItemType(name=messagecontent[0])
                    session.add(newItem)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/items')
                    self.end_headers()

        except:
            pass


def main():
    try:
        server = HTTPServer(('', 8080), webServerHandler)
        print 'Web server running...open localhost:8080/items in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()


if __name__ == '__main__':
    main()