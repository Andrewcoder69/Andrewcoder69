from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from math import sin

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the panda model
        self.panda = self.loader.loadModel("models/panda")
        self.panda.reparentTo(self.render)

        # Scale and position the panda model
        self.panda.setScale(0.005, 0.005, 0.005)
        self.panda.setPos(0, 10, 0)

        # Add a task to rotate the panda
        self.taskMgr.add(self.spinPandaTask, "SpinPandaTask")

    def spinPandaTask(self, task):
        angleDegrees = task.time * 50.0
        angleRadians = angleDegrees * (3.14159 / 180.0)
        self.panda.setHpr(angleDegrees, 0, 0)
        self.panda.setZ(sin(angleRadians) * 2)
        return Task.cont

app = MyApp()
app.run()
