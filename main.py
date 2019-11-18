from chef_bot_UI.CobotApp import MainApp
#from chef_bot_RCS.cobot_state import CobotControl
#from chef_bot_RCS.cobot_states import *

if __name__ == '__main__':
    Config.set('graphics', 'fullscrenn','auto')
    Config.set('graphics','window_state','maximized')
    Config.write()
    app = MainApp()
    app.run() 