1. Install all requirements
2. Make sure to fill in your mongo cluster URI in .current.env file (Look at .example.env)
3. Start the server script


4. Clone and start the front end server, and you have a UI that fetches papers for user queries.

Front end:
https://github.com/MechyX/IRSRP-FE

```
IRSRP-master
├─ .example.env
├─ .gitignore
├─ .idea
│  ├─ .gitignore
│  ├─ inspectionProfiles
│  │  └─ profiles_settings.xml
│  ├─ IRSRP-master.iml
│  ├─ misc.xml
│  ├─ modules.xml
│  └─ workspace.xml
├─ docker-compose.yml
├─ format.sh
├─ lda_model.pkl
├─ poetry.lock
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ server.Dockerfile
└─ src
   ├─ model
   │  ├─ bert.py
   │  ├─ lda.py
   │  └─ __init__.py
   ├─ server
   │  ├─ app.py
   │  ├─ routes
   │  │  ├─ search.py
   │  │  └─ __init__.py
   │  └─ __init__.py
   ├─ services
   │  ├─ conn.py
   │  ├─ fetch_papers.py
   │  ├─ logger.py
   │  ├─ scraper.py
   │  └─ __init__.py
   └─ __init__.py

```
```
IRSRP-master
├─ .example.env
├─ .gitignore
├─ .idea
│  ├─ .gitignore
│  ├─ inspectionProfiles
│  │  └─ profiles_settings.xml
│  ├─ IRSRP-master.iml
│  ├─ misc.xml
│  ├─ modules.xml
│  └─ workspace.xml
├─ docker-compose.yml
├─ format.sh
├─ lda_model.pkl
├─ poetry.lock
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ server.Dockerfile
└─ src
   ├─ model
   │  ├─ bert.py
   │  ├─ lda.py
   │  └─ __init__.py
   ├─ server
   │  ├─ app.py
   │  ├─ routes
   │  │  ├─ search.py
   │  │  └─ __init__.py
   │  └─ __init__.py
   ├─ services
   │  ├─ conn.py
   │  ├─ fetch_papers.py
   │  ├─ logger.py
   │  ├─ scraper.py
   │  └─ __init__.py
   └─ __init__.py

```