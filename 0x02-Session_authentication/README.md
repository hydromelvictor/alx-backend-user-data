
Curriculum
Short Specializations
Average: 115.42%
0x02. Session authentication
Back-end
Authentification
 By: Guillaume, CTO at Holberton School
 Weight: 1
 Project will start May 31, 2023 3:00 AM, must end by Jun 2, 2023 3:00 AM
 Checker will be released at May 31, 2023 3:00 PM
 An auto review will be launched at the deadline
Background Context
In this project, you will implement a Session Authentication. You are not allowed to install any other module.

In the industry, you should not implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-HTTPAuth). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

Resources
Read or watch:

REST API Authentication Mechanisms - Only the session auth part
HTTP Cookie
Flask
Flask Cookie
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What authentication means
What session authentication means
What Cookies are
How to send Cookies
How to parse Cookies
Requirements
Python Scripts
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Tasks
0. Et moi et moi et moi!
mandatory
Copy all your work of the 0x06. Basic authentication project in this new folder.

In this version, you implemented a Basic authentication for giving you access to all User endpoints:

GET /api/v1/users
POST /api/v1/users
GET /api/v1/users/<user_id>
PUT /api/v1/users/<user_id>
DELETE /api/v1/users/<user_id>
Now, you will add a new endpoint: GET /users/me to retrieve the authenticated User object.

Copy folders models and api from the previous project 0x06. Basic authentication
Please make sure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.
Update @app.before_request in api/v1/app.py:
Assign the result of auth.current_user(request) to request.current_user
Update method for the route GET /api/v1/users/<user_id> in api/v1/views/users.py:
If <user_id> is equal to me and request.current_user is None: abort(404)
If <user_id> is equal to me and request.current_user is not None: return the authenticated User in a JSON response (like a normal case of GET /api/v1/users/<user_id> where <user_id> is a valid User ID)
Otherwise, keep the same behavior
In the first terminal:

==================================================french==================================================

Copiez tout votre travail du projet 0x06. Basic authentication dans ce nouveau dossier.

Dans cette version, vous avez implémenté une authentification de base pour vous donner accès à tous les points de terminaison de l'utilisateur :

GET /api/v1/users
POST /api/v1/users
GET /api/v1/users/<usager_id>
PUT /api/v1/users/<usager_id>
DELETE /api/v1/users/<utilisateur_id>
Maintenant, vous allez ajouter un nouveau point de terminaison : GET /users/me pour récupérer l'objet utilisateur authentifié.

Copiez les dossiers models et api du projet précédent 0x06. Authentification de base
Veuillez vous assurer que toutes les tâches obligatoires de ce projet précédent sont effectuées à 100% car ce projet (et le reste de cette piste) sera basé dessus.
Mettre à jour @app.before_request dans api/v1/app.py :
Assigner le résultat de auth.current_user(request) à request.current_user
Mise à jour de la méthode pour la route GET /api/v1/users/<user_id> dans api/v1/views/users.py :
Si <user_id> est égal à me et que request.current_user est None : abort(404)
Si <user_id> est égal à moi et que request.current_user n'est pas None : retourner l'utilisateur authentifié dans une réponse JSON (comme un cas normal de GET /api/v1/users/<user_id> où <user_id> est un ID d'utilisateur valide).
Sinon, conserver le même comportement
Dans le premier terminal :


bob@dylan:~$ cat main_0.py
#!/usr/bin/env python3
""" Main 0
"""
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = "bob@hbtn.io"
user_clear_pwd = "H0lbertonSchool98!"

user = User()
user.email = user_email
user.password = user_clear_pwd
print("New user: {}".format(user.id))
user.save()

basic_clear = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py 
New user: 9375973a-68c7-46aa-b135-29f79e837495
Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In a second terminal:

bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
[
  {
    "created_at": "2017-09-25 01:55:17", 
    "email": "bob@hbtn.io", 
    "first_name": null, 
    "id": "9375973a-68c7-46aa-b135-29f79e837495", 
    "last_name": null, 
    "updated_at": "2017-09-25 01:55:17"
  }
]
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "created_at": "2017-09-25 01:55:17", 
  "email": "bob@hbtn.io", 
  "first_name": null, 
  "id": "9375973a-68c7-46aa-b135-29f79e837495", 
  "last_name": null, 
  "updated_at": "2017-09-25 01:55:17"
}
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/app.py, api/v1/views/users.py
  
1. Empty session
mandatory
Create a class SessionAuth that inherits from Auth. For the moment this class will be empty. It’s the first step for creating a new authentication mechanism:

validate if everything inherits correctly without any overloading
validate the “switch” by using environment variables
Update api/v1/app.py for using SessionAuth instance for the variable auth depending of the value of the environment variable AUTH_TYPE, If AUTH_TYPE is equal to session_auth:

import SessionAuth from api.v1.auth.session_auth
create an instance of SessionAuth and assign it to the variable auth
Otherwise, keep the previous mechanism.

In the first terminal:

==================================================french==================================================

Créez une classe SessionAuth qui hérite de Auth. Pour l'instant, cette classe sera vide. C'est la première étape de la création d'un nouveau mécanisme d'authentification :

valider que tout hérite correctement sans aucune surcharge
valider le "switch" en utilisant les variables d'environnement
Mise à jour de api/v1/app.py pour utiliser l'instance SessionAuth pour la variable auth en fonction de la valeur de la variable d'environnement AUTH_TYPE, Si AUTH_TYPE est égal à session_auth :

import SessionAuth from api.v1.auth.session_auth
créer une instance de SessionAuth et l'assigner à la variable auth
Sinon, conserver le mécanisme précédent.

Dans le premier terminal :


bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In a second terminal:

bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status/"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{
  "error": "Forbidden"
}
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/auth/session_auth.py, api/v1/app.py
  
2. Create a session
mandatory
Update SessionAuth class:

Create a class attribute user_id_by_session_id initialized by an empty dictionary
Create an instance method def create_session(self, user_id: str = None) -> str: that creates a Session ID for a user_id:
Return None if user_id is None
Return None if user_id is not a string
Otherwise:
Generate a Session ID using uuid module and uuid4() like id in Base
Use this Session ID as key of the dictionary user_id_by_session_id - the value for this key must be user_id
Return the Session ID
The same user_id can have multiple Session ID - indeed, the user_id is the value in the dictionary user_id_by_session_id
Now you an “in-memory” Session ID storing. You will be able to retrieve an User id based on a Session ID.


===========================================================french========================================

Mise à jour de la classe SessionAuth :

Création d'un attribut de classe user_id_by_session_id initialisé par un dictionnaire vide
Créer une méthode d'instance def create_session(self, user_id : str = None) -> str : qui crée un ID de session pour un user_id :
Return None si user_id est None
Return None si user_id n'est pas une chaîne de caractères
Sinon :
Génère un identifiant de session à l'aide du module uuid et de uuid4() comme id dans Base
Utiliser cet identifiant de session comme clé du dictionnaire user_id_by_session_id - la valeur de cette clé doit être user_id
Renvoyer l'identifiant de session
Le même identifiant d'utilisateur peut avoir plusieurs identifiants de session - en effet, l'identifiant d'utilisateur est la valeur du dictionnaire user_id_by_session_id.
Vous disposez à présent d'un stockage "en mémoire" des identifiants de session. Vous serez en mesure de récupérer un identifiant d'utilisateur en fonction d'un identifiant de session.


bob@dylan:~$ cat  main_1.py 
#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

print("{}: {}".format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))

user_id = None
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = 89
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "fghij"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_1.py 
<class 'dict'>: {}
None => None: {}
89 => None: {}
abcde => 61997a1b-3f8a-4b0f-87f6-19d5cafee63f: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde'}
fghij => 69e45c25-ec89-4563-86ab-bc192dcc3b4f: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde', '69e45c25-ec89-4563-86ab-bc192dcc3b4f': 'fghij'}
abcde => 02079cb4-6847-48aa-924e-0514d82a43f4: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde', '02079cb4-6847-48aa-924e-0514d82a43f4': 'abcde', '69e45c25-ec89-4563-86ab-bc192dcc3b4f': 'fghij'}
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/auth/session_auth.py
  
3. User ID for Session ID
mandatory
Update SessionAuth class:

Create an instance method def user_id_for_session_id(self, session_id: str = None) -> str: that returns a User ID based on a Session ID:

Return None if session_id is None
Return None if session_id is not a string
Return the value (the User ID) for the key session_id in the dictionary user_id_by_session_id.
You must use .get() built-in for accessing in a dictionary a value based on key
Now you have 2 methods (create_session and user_id_for_session_id) for storing and retrieving a link between a User ID and a Session ID.

===============================================french====================================================

Mise à jour de la classe SessionAuth :

Création d'une méthode d'instance def user_id_for_session_id(self, session_id : str = None) -> str : qui renvoie un identifiant d'utilisateur basé sur un identifiant de session :

Return None si session_id est None
Retourne None si session_id n'est pas une chaîne de caractères
Renvoie la valeur (l'identifiant de l'utilisateur) correspondant à la clé session_id dans le dictionnaire user_id_by_session_id.
Vous devez utiliser la fonction .get() pour accéder à une valeur basée sur une clé dans un dictionnaire.
Vous disposez à présent de deux méthodes (create_session et user_id_for_session_id) pour stocker et récupérer un lien entre un identifiant d'utilisateur et un identifiant de session.


bob@dylan:~$ cat main_2.py 
#!/usr/bin/env python3
""" Main 2
"""
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

user_id_1 = "abcde"
session_1 = sa.create_session(user_id_1)
print("{} => {}: {}".format(user_id_1, session_1, sa.user_id_by_session_id))

user_id_2 = "fghij"
session_2 = sa.create_session(user_id_2)
print("{} => {}: {}".format(user_id_2, session_2, sa.user_id_by_session_id))

print("---")

tmp_session_id = None
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = 89
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = "doesntexist"
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

print("---")

tmp_session_id = session_1
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = session_2
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

print("---")

session_1_bis = sa.create_session(user_id_1)
print("{} => {}: {}".format(user_id_1, session_1_bis, sa.user_id_by_session_id))

tmp_user_id = sa.user_id_for_session_id(session_1_bis)
print("{} => {}".format(session_1_bis, tmp_user_id))

tmp_user_id = sa.user_id_for_session_id(session_1)
print("{} => {}".format(session_1, tmp_user_id))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_2.py 
abcde => 8647f981-f503-4638-af23-7bb4a9e4b53f: {'8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
fghij => a159ee3f-214e-4e91-9546-ca3ce873e975: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
---
None => None
89 => None
doesntexist => None
---
8647f981-f503-4638-af23-7bb4a9e4b53f => abcde
a159ee3f-214e-4e91-9546-ca3ce873e975 => fghij
---
abcde => 5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde', '5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee': 'abcde'}
5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee => abcde
8647f981-f503-4638-af23-7bb4a9e4b53f => abcde
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/auth/session_auth.py
  
4. Session cookie
mandatory
Update api/v1/auth/auth.py by adding the method def session_cookie(self, request=None): that returns a cookie value from a request:

Return None if request is None
Return the value of the cookie named _my_session_id from request - the name of the cookie must be defined by the environment variable SESSION_NAME
You must use .get() built-in for accessing the cookie in the request cookies dictionary
You must use the environment variable SESSION_NAME to define the name of the cookie used for the Session ID
In the first terminal:

==================================================french==================================================

Mise à jour de api/v1/auth/auth.py en ajoutant la méthode def session_cookie(self, request=None) : qui renvoie une valeur de cookie à partir d'une requête :

Return None if request is None
Retourne la valeur du cookie nommé _my_session_id à partir de la requête - le nom du cookie doit être défini par la variable d'environnement SESSION_NAME
Vous devez utiliser .get() pour accéder au cookie dans le dictionnaire des cookies de la requête.
Vous devez utiliser la variable d'environnement SESSION_NAME pour définir le nom du cookie utilisé pour l'identifiant de session.
Dans le premier terminal :


bob@dylan:~$ cat main_3.py
#!/usr/bin/env python3
""" Cookie server
"""
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(auth.session_cookie(request))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_3.py 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In a second terminal:

bob@dylan:~$ curl "http://0.0.0.0:5000"
Cookie value: None
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id=Hello"
Cookie value: Hello
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id=C is fun"
Cookie value: C is fun
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id_fake"
Cookie value: None
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/auth/auth.py
  
5. Before request
mandatory
Update the @app.before_request method in api/v1/app.py:

Add the URL path /api/v1/auth_session/login/ in the list of excluded paths of the method require_auth - this route doesn’t exist yet but it should be accessible outside authentication
If auth.authorization_header(request) and auth.session_cookie(request) return None, abort(401)
In the first terminal:

==================================================french==================================================

Mise à jour de la méthode @app.before_request dans api/v1/app.py :

Ajouter le chemin URL /api/v1/auth_session/login/ dans la liste des chemins exclus de la méthode require_auth - cette route n'existe pas encore mais elle devrait être accessible en dehors de l'authentification.
Si auth.authorization_header(request) et auth.session_cookie(request) renvoient None, abort(401)
Dans le premier terminal :


bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In a second terminal:

bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" # not found but not "blocked" by an authentication system
{
  "error": "Not found"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh" # Won't work because the environment variable AUTH_TYPE is equal to "session_auth"
{
  "error": "Forbidden"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76" # Won't work because no user is linked to this Session ID
{
  "error": "Forbidden"
}
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/app.py
  
6. Use Session ID for identifying a User
mandatory
Update SessionAuth class:

Create an instance method def current_user(self, request=None): (overload) that returns a User instance based on a cookie value:

You must use self.session_cookie(...) and self.user_id_for_session_id(...) to return the User ID based on the cookie _my_session_id
By using this User ID, you will be able to retrieve a User instance from the database - you can use User.get(...) for retrieving a User from the database.
Now, you will be able to get a User based on his session ID.

In the first terminal:

==================================================french==================================================

Update SessionAuth class:

Create an instance method def current_user(self, request=None): (overload) that returns a User instance based on a cookie value:

You must use self.session_cookie(...) and self.user_id_for_session_id(...) to return the User ID based on the cookie _my_session_id
By using this User ID, you will be able to retrieve a User instance from the database - you can use User.get(...) for retrieving a User from the database.
Now, you will be able to get a User based on his session ID.

In the first terminal:


bob@dylan:~$ cat main_4.py
#!/usr/bin/env python3
""" Main 4
"""
from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User

""" Create a user test """
user_email = "bobsession@hbtn.io"
user_clear_pwd = "fake pwd"

user = User()
user.email = user_email
user.password = user_clear_pwd
user.save()

""" Create a session ID """
sa = SessionAuth()
session_id = sa.create_session(user.id)
print("User with ID: {} has a Session ID: {}".format(user.id, session_id))

""" Create a Flask app """
app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    request_user = sa.current_user(request)
    if request_user is None:
        return "No user found\n"
    return "User found: {}\n".format(request_user.id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_4.py
User with ID: cf3ddee1-ff24-49e4-a40b-2540333fe992 has a Session ID: 9d1648aa-da79-4692-8236-5f9d7f9e9485
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In a second terminal:

bob@dylan:~$ curl "http://0.0.0.0:5000/"
No user found
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/" --cookie "_my_session_id=Holberton"
No user found
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/" --cookie "_my_session_id=9d1648aa-da79-4692-8236-5f9d7f9e9485"
User found: cf3ddee1-ff24-49e4-a40b-2540333fe992
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/auth/session_auth.py
  
7. New view for Session Authentication
mandatory
Create a new Flask view that handles all routes for the Session authentication.

In the file api/v1/views/session_auth.py, create a route POST /auth_session/login (= POST /api/v1/auth_session/login):

Slash tolerant (/auth_session/login == /auth_session/login/)
You must use request.form.get() to retrieve email and password parameters
If email is missing or empty, return the JSON { "error": "email missing" } with the status code 400
If password is missing or empty, return the JSON { "error": "password missing" } with the status code 400
Retrieve the User instance based on the email - you must use the class method search of User (same as the one used for the BasicAuth)
If no User found, return the JSON { "error": "no user found for this email" } with the status code 404
If the password is not the one of the User found, return the JSON { "error": "wrong password" } with the status code 401 - you must use is_valid_password from the User instance
Otherwise, create a Session ID for the User ID:
You must use from api.v1.app import auth - WARNING: please import it only where you need it - not on top of the file (can generate circular import - and break first tasks of this project)
You must use auth.create_session(..) for creating a Session ID
Return the dictionary representation of the User - you must use to_json() method from User
You must set the cookie to the response - you must use the value of the environment variable SESSION_NAME as cookie name - tip
In the file api/v1/views/__init__.py, you must add this new view at the end of the file.

In the first terminal:

==================================================french==================================================

Créez une nouvelle vue Flask qui gère tous les itinéraires pour l'authentification de la session.

Dans le fichier api/v1/views/session_auth.py, créez une route POST /auth_session/login (= POST /api/v1/auth_session/login) :

Tolérance au slash (/auth_session/login == /auth_session/login/)
Vous devez utiliser request.form.get() pour récupérer les paramètres email et mot de passe
Si l'email est manquant ou vide, renvoyer le JSON { "error" : "email missing" } avec le code de statut 400
Si le mot de passe est manquant ou vide, le JSON { "error" : "password missing" } avec le code d'état 400
Récupérer l'instance d'utilisateur basée sur l'email - vous devez utiliser la méthode de recherche de classe de l'utilisateur (la même que celle utilisée pour BasicAuth)
Si aucun utilisateur n'est trouvé, renvoyer le JSON { "error" : "no user found for this email" } avec le code d'état 404
Si le mot de passe n'est pas celui de l'utilisateur trouvé, le JSON { "error" : "wrong password" } avec le code d'état 401 - vous devez utiliser is_valid_password de l'instance d'utilisateur.
Sinon, créez un ID de session pour l'ID de l'utilisateur :
Vous devez utiliser from api.v1.app import auth - ATTENTION : veuillez l'importer uniquement là où vous en avez besoin - pas en haut du fichier (peut générer une importation circulaire - et casser les premières tâches de ce projet)
Vous devez utiliser auth.create_session(..) pour créer un ID de session
Retourner la représentation du dictionnaire de l'utilisateur - vous devez utiliser la méthode to_json() de l'utilisateur
Vous devez placer le cookie dans la réponse - vous devez utiliser la valeur de la variable d'environnement SESSION_NAME comme nom de cookie - astuce
Dans le fichier api/v1/views/__init__.py, vous devez ajouter cette nouvelle vue à la fin du fichier.

Dans le premier terminal :


bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In a second terminal:

bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XGET
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
bob@dylan:~$
bob@dylan:~$  curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST
{
  "error": "email missing"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=guillaume@hbtn.io"
{
  "error": "password missing"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=guillaume@hbtn.io" -d "password=test"
{
  "error": "no user found for this email"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=test"
{
  "error": "wrong password"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Set-Cookie: _my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4; Path=/
< Access-Control-Allow-Origin: *
< Content-Length: 210
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Mon, 16 Oct 2017 04:57:08 GMT
< 
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
* Closing connection 0
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
Now you have an authentication based on a Session ID stored in cookie, perfect for a website (browsers love cookies).

Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/views/session_auth.py, api/v1/views/__init__.py
  
8. Logout
mandatory
Update the class SessionAuth by adding a new method def destroy_session(self, request=None): that deletes the user session / logout:

If the request is equal to None, return False
If the request doesn’t contain the Session ID cookie, return False - you must use self.session_cookie(request)
If the Session ID of the request is not linked to any User ID, return False - you must use self.user_id_for_session_id(...)
Otherwise, delete in self.user_id_by_session_id the Session ID (as key of this dictionary) and return True
Update the file api/v1/views/session_auth.py, by adding a new route DELETE /api/v1/auth_session/logout:

Slash tolerant
You must use from api.v1.app import auth
You must use auth.destroy_session(request) for deleting the Session ID contains in the request as cookie:
If destroy_session returns False, abort(404)
Otherwise, return an empty JSON dictionary with the status code 200
In the first terminal:

==================================================french==================================================

Mise à jour de la classe SessionAuth en ajoutant une nouvelle méthode def destroy_session(self, request=None) : qui supprime la session de l'utilisateur / déconnexion :

Si la requête est égale à None, la méthode renvoie False
Si la requête ne contient pas le cookie d'identification de session, la méthode renvoie False - vous devez utiliser self.session_cookie(request)
Si l'identifiant de session de la demande n'est lié à aucun identifiant d'utilisateur, renvoyez False - vous devez utiliser self.user_id_for_session_id(...)
Sinon, supprimer dans self.user_id_by_session_id l'identifiant de session (en tant que clé de ce dictionnaire) et renvoyer True.
Mettez à jour le fichier api/v1/views/session_auth.py, en ajoutant une nouvelle route DELETE /api/v1/auth_session/logout :

Tolérance au slash
Vous devez utiliser from api.v1.app import auth
Vous devez utiliser auth.destroy_session(request) pour supprimer l'identifiant de session contenu dans la requête en tant que cookie :
Si destroy_session renvoie False, abort(404)
Sinon, renvoyer un dictionnaire JSON vide avec le code de statut 200
Dans le premier terminal :


bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In a second terminal:

bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Set-Cookie: _my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721; Path=/
< Access-Control-Allow-Origin: *
< Content-Length: 210
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Mon, 16 Oct 2017 04:57:08 GMT
< 
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721" -XDELETE
{}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{
  "error": "Forbidden"
}
bob@dylan:~$
Login, logout… what’s else?

Now, after getting a Session ID, you can request all protected API routes by using this Session ID, no need anymore to send User email and password every time.

Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/auth/session_auth.py, api/v1/views/session_auth.py
  
9. Expiration?
#advanced
Actually you have 2 authentication systems:

Basic authentication
Session authentication
Now you will add an expiration date to a Session ID.

Create a class SessionExpAuth that inherits from SessionAuth in the file api/v1/auth/session_exp_auth.py:

Overload def __init__(self): method:
Assign an instance attribute session_duration:
To the environment variable SESSION_DURATION casts to an integer
If this environment variable doesn’t exist or can’t be parse to an integer, assign to 0
Overload def create_session(self, user_id=None):
Create a Session ID by calling super() - super() will call the create_session() method of SessionAuth
Return None if super() can’t create a Session ID
Use this Session ID as key of the dictionary user_id_by_session_id - the value for this key must be a dictionary (called “session dictionary”):
The key user_id must be set to the variable user_id
The key created_at must be set to the current datetime - you must use datetime.now()
Return the Session ID created
Overload def user_id_for_session_id(self, session_id=None):
Return None if session_id is None
Return None if user_id_by_session_id doesn’t contain any key equals to session_id
Return the user_id key from the session dictionary if self.session_duration is equal or under 0
Return None if session dictionary doesn’t contain a key created_at
Return None if the created_at + session_duration seconds are before the current datetime. datetime - timedelta
Otherwise, return user_id from the session dictionary
Update api/v1/app.py to instantiate auth with SessionExpAuth if the environment variable AUTH_TYPE is equal to session_exp_auth.

In the first terminal:

==================================================french==================================================

En fait, vous avez deux systèmes d'authentification :

l'authentification de base
Authentification de session
Vous allez maintenant ajouter une date d'expiration à un identifiant de session.

Créez une classe SessionExpAuth qui hérite de SessionAuth dans le fichier api/v1/auth/session_exp_auth.py :

Surcharge def __init__(self) : method :
Affecte un attribut d'instance session_duration :
A la variable d'environnement SESSION_DURATION, convertie en un entier
Si cette variable d'environnement n'existe pas ou ne peut pas être transformée en entier, elle est assignée à 0.

Surcharge def create_session(self, user_id=None) :
Créer un identifiant de session en appelant super() - super() appellera la méthode create_session() de SessionAuth
Retourne None si super() ne peut pas créer un ID de session
Utiliser cet identifiant de session comme clé du dictionnaire user_id_by_session_id - la valeur de cette clé doit être un dictionnaire (appelé "dictionnaire de session") :
la clé user_id doit correspondre à la variable user_id
La clé created_at doit correspondre à la date du jour - vous devez utiliser datetime.now()
Renvoie l'identifiant de la session créée

Surcharge def user_id_for_session_id(self, session_id=None) :
Retourne None si session_id est None
Retourne None si user_id_by_session_id ne contient pas de clé égale à session_id
Retourne la clé user_id du dictionnaire de session si self.session_duration est inférieur ou égal à 0
Retourne None si le dictionnaire de session ne contient pas de clé created_at
Retourne None si les secondes created_at + session_duration sont antérieures à la date courante. datetime - timedelta
Sinon, renvoie l'identifiant de l'utilisateur à partir du dictionnaire de session.
Mise à jour de api/v1/app.py pour instancier l'authentification avec SessionExpAuth si la variable d'environnement AUTH_TYPE est égale à session_exp_auth.

Dans le premier terminal :


bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_exp_auth SESSION_NAME=_my_session_id SESSION_DURATION=60 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In a second terminal:

bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Set-Cookie: _my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f; Path=/
< Access-Control-Allow-Origin: *
< Content-Length: 210
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Mon, 16 Oct 2017 04:57:08 GMT
< 
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ sleep 10
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$ 
bob@dylan:~$ sleep 51 # 10 + 51 > 60
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f"
{
  "error": "Forbidden"
}
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/auth/session_exp_auth.py, api/v1/app.py
  
10. Sessions in database
#advanced
Since the beginning, all Session IDs are stored in memory. It means, if your application stops, all Session IDs are lost.

For avoid that, you will create a new authentication system, based on Session ID stored in database (for us, it will be in a file, like User).

Create a new model UserSession in models/user_session.py that inherits from Base:

Implement the def __init__(self, *args: list, **kwargs: dict): like in User but for these 2 attributes:
user_id: string
session_id: string
Create a new authentication class SessionDBAuth in api/v1/auth/session_db_auth.py that inherits from SessionExpAuth:

Overload def create_session(self, user_id=None): that creates and stores new instance of UserSession and returns the Session ID
Overload def user_id_for_session_id(self, session_id=None): that returns the User ID by requesting UserSession in the database based on session_id
Overload def destroy_session(self, request=None): that destroys the UserSession based on the Session ID from the request cookie
Update api/v1/app.py to instantiate auth with SessionDBAuth if the environment variable AUTH_TYPE is equal to session_db_auth.

In the first terminal:

==================================================french==================================================

Depuis le début, tous les identifiants de session sont stockés en mémoire. Cela signifie que si votre application s'arrête, tous les identifiants de session sont perdus.

Pour éviter cela, vous allez créer un nouveau système d'authentification, basé sur l'identifiant de session stocké dans la base de données (pour nous, il sera dans un fichier, comme User).

Créez un nouveau modèle UserSession dans models/user_session.py qui hérite de Base :

Implémenter la fonction def __init__(self, *args : list, **kwargs : dict) : comme dans User mais pour ces 2 attributs :
user_id : string
session_id : chaîne de caractères
Créer une nouvelle classe d'authentification SessionDBAuth dans api/v1/auth/session_db_auth.py qui hérite de SessionExpAuth :

Surcharge def create_session(self, user_id=None) : qui crée et stocke une nouvelle instance de UserSession et renvoie l'ID de la session.
Surcharge def user_id_for_session_id(self, session_id=None) : renvoie l'ID de l'utilisateur en demandant UserSession dans la base de données sur la base de session_id
Surcharge def destroy_session(self, request=None) : qui détruit le UserSession en se basant sur l'ID de session du cookie de la requête
Mise à jour de api/v1/app.py pour instancier l'authentification avec SessionDBAuth si la variable d'environnement AUTH_TYPE est égale à session_db_auth.

Dans le premier terminal :


bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_db_auth SESSION_NAME=_my_session_id SESSION_DURATION=60 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In a second terminal:

bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Set-Cookie: _my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13; Path=/
< Access-Control-Allow-Origin: *
< Content-Length: 210
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Mon, 16 Oct 2017 04:57:08 GMT
< 
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ sleep 10
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ sleep 60
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13"
{
  "error": "Forbidden"
}
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x02-Session_authentication
File: api/v1/auth/session_db_auth.py, api/v1/app.py, models/user_session.py
  
Copyright © 2023 ALX, All rights reserved.



jsonify returns a Response object, so capture it before returning from your view and add the cookie then with Response.set_cookie.

out = jsonify(state=0, msg='success')
out.set_cookie('my_key', 'my_value')
return out
You might want to just add the value to the session cookie. Flask's session will json encode values and sign the cookie for security, something you have to manually do when using set_cookie.

from flask import session

session['my_key'] = 'my_value'
Share
Follow
ed