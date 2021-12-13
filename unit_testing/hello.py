class Hello:
    def __init__(self):
        self._greetingTemplate = 'Hello {name}!'

    def greet(self, name):
        return self._greetingTemplate.format(name=name)

    def setTemplate(self, newTemplate):
        self._greetingTemplate = newTemplate


   