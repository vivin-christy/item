# Item Catalog Project
This application provides a list of items within a variety of categories as well as provide a user registration and authentication system.Users will have the ability to post, edit, and delete their own items.

### Features
- Proper authentication and authorisation check.
- Full CRUD support using SQLAlchemy and Flask.
- JSON endpoints.
- Implements oAuth using Google Sign-in API.

### Project Structure
```
.
├── app.py
├── client.json
├── database_setup.py
├── fake_db_populator.py
├── itemcatalog.db
├── LICENSE
├── README.md
├── static
│   └── style.css
└── templates
    ├── delete_category.html
    ├── delete.html
    ├── design.html
    ├── edit_category.html
    ├── index.html
    ├── items.html
    ├── login.html
    ├── new-category.html
    ├── new-item-2.html
    ├── new.html
    ├── update.html
    └── view.html
```

## Steps to run this project

1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html).

2. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

3. Clone or download the Vagrant VM configuration file from [here](https://github.com/udacity/fullstack-nanodegree-vm).

4. Open the above directory and navigate to the `vagrant/` sub-directory.

5. Open terminal, and type
   "vagrant up"


   This will cause Vagrant to download the Ubuntu operating system and install it. This may take quite a while depending on how fast your Internet connection is.

6. After the above command succeeds, connect to the newly created VM:
   "vagrant ssh"


8. Type `cd /vagrant/` to navigate to the shared repository.

9. Download this project, and navigate to it.

11. Install or upgrade Flask:
    "sudo python3 -m pip install --upgrade flask"
    
12. Set up the database:
    "python3 database_setup.py"

13. Insert dummy values. **If you don't run this, the application might not run.**
   
    "python3 fake_db_populator.py"
   
14. Run this application:
    "python3 app.py"
    
15. Open `http://localhost:5000/` in your favourite Web browser, and enjoy.


