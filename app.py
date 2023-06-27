from fastapi import FastAPI

from src import ping


app = FastAPI()


@app.get('/')
async def index():
    ping.delay('thommy.python.dev@gmail.com', 'FastAPIDockerComposeCelery', 'Some text')
    return {'status': 'OK'}
