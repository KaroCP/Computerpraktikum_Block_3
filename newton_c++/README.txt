ISSUE [prevent CrossOrigin-request ERROR]: HTML document has  to be requestet by GET from same Server that serves POST requests, otherwise CrossOrigin ERROR occurs





What is happening here ? 

the py server must be started first ("momo#sPyServer.py")... (can be done from cmd),
than head to browser and type "localhost:5000/req" in url.

here the html page "requester.html" from /static folder will be loaded, and appear in browser viewport.

the page has some JS-code to fetch data from the py server.
it will essentially POST the data "x^3-1" or some other function.

the py server will than calculate the Im and Re parts of f/f' of that function and return.

after taht the data will be presented via JS-code to the DOM

the JS-code will also convert the syntax of raising expressions to some power from exp1**exp2 to pow(exp1,exp2) [necessary for opengl]



when url is just "/" than index.html is called (MAIN PROGRAM)