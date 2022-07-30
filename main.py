from multiprocessing import Process

from game.runner import run_game_server
from login.runner import run_login_server

if __name__ == '__main__':
    login = Process(target=run_login_server)
    game = Process(target=run_game_server)

    login.start()
    game.start()
