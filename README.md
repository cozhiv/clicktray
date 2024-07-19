# clicktrack
Tracks your mouse moves and makes a photo when you click, using camera. This version is still in development mode.
## requirements
python >= 3.7
virtual environment for python such as:
- venv
- env
- pipenv
- etc.
tested and developed with venv
tested on Ubuntu 23

## Getting started
Copy url and clone,
<br />
<code>git clone git@gitlab.com:cozhiv/clicktrack.git</code>
<br />
or
<br />
<code>git clone https://gitlab.com/cozhiv/clicktrack.git</code>
<br />
'cd' into folder 'clicktrack'
<br />
<code>cd clicktrack</code>
## create virtual environment (example with venv):
<code>python3 -m venv venv</code>

# activate it
<code>source venv/bin/activate</code>

## install the packages
<code>pip install -r requirements.txt</code>

## run the app
<code>python app.py</code>

## live mouse coordinates
turn your browser to localhost:5000

## snaps
The mouse makes a snap everytime you use the left click.

## raw data
Endpoint to check the whole raw data is 
<br />
localhost:5000/snaps

## Raw data stored in db for specific click.
Endpoint to check pic stored in db on
<br />
localhost:5000/snap <br />
localhost:5000/snap/1 <br />
localhost:5000/snap/2 <br />
localhost:5000/snap/3 <br />
localhost:5000/snap/number <br />

## Render specific picture. 
The number of the pic is the number of the recorded click.<br />
<code>localhost:5000/shot/numberofpic </code><br />
localhost:5000/snap/1 <br />
localhost:5000/snap/2 <br />

