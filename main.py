from databasep5.Engine.Reception import Reception
from databasep5.Engine.Engine import Engine

if __name__ == '__main__':
    myEngine = Engine
    hasData = myEngine.checkData
    myReception = Reception()
    myReception.home(hasData)
