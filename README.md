# pablo-landing
Minimalist portfolio for Pablo Lerner.


To deploy on Render:

runtime: python
buildCommand: pip install -r requirements.txt
startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
