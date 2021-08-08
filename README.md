# transformer-demo

Test of FastAPI https://fastapi.tiangolo.com/

Passing matrix A: [[1.0, 0.032], [0.032, 1.0]]

Factorize A = U S Vh

Check that A == A' = S[0] U[:,0] Vh[0,:] + S[1] U[:,1] Vh[1,:] 



## summarizer
$ uvicorn main:app --reload

$ curl -X POST localhost:8000/items/ -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":\"Foo\",\"A\":[[1.0, 0.032], [0.032, 1.0]]}"












