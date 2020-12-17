# CI-MS3-Floral-Reef

A respoistory for my third Milestone project for the Full Stack Software Development Course by Code Institute.

### Setting Up MongoDB Shell

1. A free account was set up on [cloud.mongodb.com](cloud.mongodb.com)
2. A new cluster and database were created.
3. Network Access was temporarily set to 'Allow Access From Anywhere'.
4. The MongoDB shell was downloaded and installed from [this link](https://downloads.mongodb.org/windows/mongodb-shell-windows-x86_64-4.4.2.zip).
5. The PATH environment variable was updated to include the MongoDB "/bin" folder, that was created by the intallation of the shell.
6. "C:\mongodb" was also added to the PATH environment variable to allow access to 'mongod.exe' from anywhere outside the '/bin' directory.
7. A new terminal was created in VS Code, where 'mongod' was run.
8. Back on the mongodb website, the cluster's "Connect" button was run.
9. The connection string was copied from step 3.
10. Then another new terminal was created inside VS Code where the copied code was pasted, edited to include databsae name and then run.
11. The password for the database was inputted.

### Setting Up MongoDB within Python

1. Performed steps 1-8 from above.
2. Selected 'Connect your application' as the connection method.
3. Python was selected as the driver and version 3.6 or later was chosen.
4. Connection string was copied.
5. A .gitignore and env.py file were created, and the env.py file was added to the .gitignore file so as to prevent any sensitive information being uploaded to GitHub.
6. An os environement default variable called "MONGO_URI" was declared with a value of the Connection String.
7. A 'mongo_project.py' file was created and the following code was added:

   ```python
    # Imports relevant libraries
    import os
    import pymongo
    if os.path.exists("env.py"):
        import env


    # Creates variables to store credentials
    MONGO_URI = os.environ.get("MONGO_URI")
    DATABASE = "myFirstDB"
    COLLECTION = "celebrities"

    # Connects to MongoDB using above variables
    def mongo_connect(url):
        try:
            conn = pymongo.MongoClient(url)
            print("Mongo is connected!")
            return conn
        except:
            print("Could not connect to MongoDB: %s") % e


    conn = mongo_connect(MONGO_URI)

    # Puts collection into variable
    coll = conn[DATABASE][COLLECTION]

    # Creates variable to store all entries in collection
    documents = coll.find()

    # Prints all entries to the console
    for doc in documents:
        print(doc)
   ```

### Setting Up MongoDB Database

1. A new database called 'floral_reef' was created.
2. It was then populated with collections called 'flowers' and 'users'.