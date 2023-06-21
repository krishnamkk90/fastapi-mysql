# fast-api-mysql

  To build and start the mysql container:
  
  docker build -t mysql-docker .
  docker run -d --name mysql-container -p 3306:3306 mysql-docker


  To run the fastapi application
  create python venv  -  python3 -m venv env
  install the dependecies - pip install -r requirements.txt
  run the api server -  uvicorn main:app --reload

  Verify the API usign the link and test the CRUD operations
  http://localhost:8000/docs

  To run the web_scrapper:
  dependencies already place in the requirements.txt, if need to run alone install the following,

  pip install --user requests bs4 mysql-connector-python schedule selenium
