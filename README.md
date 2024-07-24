# Clicktray
Tracks your mouse moves and makes a photo when you click, using camera. This version is still in development mode.
## Requirements
python >= 3.7
virtual environment for python such as:
- venv
- env
- pipenv
- etc. <bra />
Tested and developed with venv; Ubuntu 23.

## Getting started
Copy url and clone,
<br />
<code>git clone git@github.com:cozhiv/clicktray.git</code>
<br />
or
<br />
<code>git clone https://gitlab.com/cozhiv/clicktrack.git</code>
<br />
'cd' into folder 'clicktray'
<br />
<code>cd clicktray</code>
## create virtual environment (example with venv):
<code>python3 -m venv venv</code>

## Activate it
<code>source venv/bin/activate</code>

## Install the packages
<code>pip install -r requirements.txt</code>

## Run the app
<code>python app.py</code>

## Live mouse coordinates
turn your browser to localhost:5000

## Snaps
The mouse makes a snap everytime you use the left click.

## Raw data
Check the whole raw data on
<br />
localhost:5000/snaps

## Raw data stored in db for specific click.
Check pic stored in db on
<br />
localhost:5000/snap <br />
localhost:5000/snap/1 <br />
localhost:5000/snap/2 <br />
localhost:5000/snap/3 <br />
localhost:5000/snap/number <br />

## Render specific picture. 
The number of the pic is the number of the recorded click.<br />
<code>localhost:5000/shot/numberofpic </code><br />
localhost:5000/shot/1 <br />
localhost:5000/shot/2 <br />

