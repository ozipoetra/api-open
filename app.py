import g4f
import g4f.api
import os

ENV_PORT = 5000 if os.getenv('PORT') else 5000

def main():
    print(f'Starting server... [g4f v-{g4f.version.utils.current_version}]')
    g4f.api.Api(engine = g4f, debug = False).run(ip = f'0.0.0.0:{ENV_PORT}')

if __name__ == "__main__":
    main()
