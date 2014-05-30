## REST-RPC Test
The goal of this programming test is to design and implement a series of tests designed to exercise the example web service.

### Download & Install
`git clone https://github.com/ErikDahlinghaus/web-service-test.git`

### Run
`$ python web-service.py [port]`

### Functions
| Method | Endpoint                   | Expected Response | Expected Result              |
|--------|----------------------------|-------------------|------------------------------|
| GET    | /                          | 200               | "This endpoint does nothing" |
| POST   | /create?values=x,y,z       | 201               |                              |
| GET    | /read                      | 200               | ['x','y','z']                |
| PUT    | /update?value=x&newvalue=q | 200               |                              |
| DELETE | /delete?value=y            | 204               |                              |

### Write up
After exercising this simple web service, write a small document which describes why you think your test covers all components of this web service.
Are there any issues with the web service? What could be done to improve the example web service?