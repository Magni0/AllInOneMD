# All In One Markdown

<https://trello.com/b/xCCDsnrL/allinonemd>

## Purpose

To allow the upload, storage, editing, downloading and converting to pdf (with images) in one location to limit the need to use third party software when writing documentation in markdown files. When using third party websites to convert Markdown (MD) to pdf format it is inconveniant how few support the use of images and it can get messy with storage on a users device. This solution's pupose is to accumulate the diffrent aspects of documentaion into *one* conveiniant and easy to use method for a user.

## Wireframes

![login page](docs/login-wireframe.png)

![sign up page](docs/sign-up-wireframe.png)

![main page](docs/main-wireframe.png)

## Installation

1. Navigate to the dir you wish to have the software and clone it with this command:

    `git clone https://github.com/Magni0/AllInOneMD.git`

2. Create an new virtual enviroment with this command:

    `python -m venv venv`

    If python isnt installed it can be downloaded [here](https://www.python.org/downloads/) for windows or

    ```
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.8
    ```

    for linux

3. Activate the virtual enviroment:

    for windows (cmd)

    `source venv\Scripts\activate.bat`

    for linux (bash)

    `source venv/bin/activate`

4. Install dependencies:

    `pip3 install -r requirements.txt`

    If you don't have pip then a guide for it can be found [here](https://pip.pypa.io/en/stable/installing/)

5. Then the app can be run by:

    `python {pathtofile}/main.py`

## displaying documented endpoints

1. Go to [this website](https://editor.swagger.io/#)

2. Click on file

3. Select 'import file'

4. select the swagger.yaml file located in /docs
