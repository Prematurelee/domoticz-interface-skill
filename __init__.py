from mycroft import MycroftSkill, intent_file_handler


class DomoticzInterface(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('interface.domoticz.intent')
    def handle_interface_domoticz(self, message):
        self.speak_dialog('interface.domoticz')


def create_skill():
    return DomoticzInterface()

