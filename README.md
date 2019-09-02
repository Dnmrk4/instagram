# Instagram

This is a clone of Instagram social site, built using Django framework.

#### Author

- _By_ **Danmark Mutai**

## Technologies Used

* Python3.6.8.
* Django 2.2.4.
* CSS3 for styling.
* HTML5 for webpage design.

## BDD

| Behavior | Input  | Output |
| :-------------: | :-------------: | :-------------: |
| user sign up | click on sign up | user signed in |
| user sign in | Click on sign in | user signed in |
| upload an Image | Click on upload  | image uploaded by user |
| Comment on Image | Click on comment  | Comments written by user |
| Search for user | Enter search word and submit | users |

## Setup and installations

#### Prerequisites

1. [Python3.6](https://www.python.org/downloads/)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Clone the Repo and rename it to suit your needs.

```bash
git clone https://github.com/Dnmrk4/instagram.git
```

#### Initialize git and add the remote repository

```bash
git init
```

```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment

```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables

> Create a `.env` file and paste paste the following filling where appropriate:

```
SECRET_KEY='34jkt34hf83f'
DEBUG=True #set to false in production
DB_NAME='instagram'
DB_USER='user'
DB_PASSWORD='password'
DB_HOST='127.0.0.1'
MODE='dev' #set to 'prod' in production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'example@example.com' #Input your email address
EMAIL_HOST_PASSWORD = 'password' #Input the password of your email address
```

#### Install dependancies

Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Run chmod a+x start.py

```bash
chmod a+x start.py
```

#### Run the app

```bash
./start.sh
```

#### Access the application through localhost:8000

Open [localhost:8000](http://127.0.0.1:8000/)

## Support

* For help or support contact me using my Email: _danmark.chemuren@gmail.com_

### License 

- This website uses a [MIT License](/LICENSE)

*Copyright (c) 2019* **Danmark Mutai**



