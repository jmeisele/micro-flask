# MicroFlask
Demo of using Flask back end micro services loosely decoupled with docker containers.

From the command line:
- git clone https://github.com/jmeisele/MicroFlask.git
- pip install -r requirements.txt
- . /venv/bin/activate
- python3 app.py

Or if using Docker (which you should anyways since we are using Microservices...)
- docker pull jmeisele/micro-flask-app
- docker run --name micro-flask-app -p 5001:8000 micro-flask-app

#TODO
- [ ] UML for overall architecture using draw.io
- [ ] Create database(s) schemas for each microservice
- [ ] Construct docker compose file to get all services up and running

If you found this repo helpful, a [small donation](https://www.buymeacoffee.com/VlduzAG) would be greatly appreciated. 
All proceeds go towards coffee, and all coffee goes towards more code.
