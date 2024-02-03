import g4f
from g4f.api import Api
import os

ENV_PORT = os.getenv('PORT')
app = Api(engine = g4f, debug = False).run(ip = f'0.0.0.0:{ENV_PORT}')

def main():
    print(f'Starting server... [g4f v-{g4f.version.utils.current_version}]')
    app

if __name__ == "__main__":
    main()
