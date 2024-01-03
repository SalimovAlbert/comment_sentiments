This project pulls some commentaries from the youtube video given a link to it and analyses their sentiment.

Add the youtube developer API to `.env_template` file and rename it to `.env`
Install requirements with `pip install -r requirements.txt`
Command to run the service:
`python -m uvicorn main:app --host=0.0.0.0 --port 8000 --reload`

Reffer to `http://localhost:8000/docs` for API docs
