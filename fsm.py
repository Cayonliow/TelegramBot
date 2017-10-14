from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
        
    def going_to_menu(self, update):
        text = update.message.text
        return text.lower() == 'menu'

    def going_to_playing(self, update):
        text = update.message.text
        return text.lower() == 'playing'

    def on_enter_menu(self, update):
        update.message.reply_text("What can I help you?")
        self.go_back(update)

    def on_exit_waiting(self, update):
        print('Leaving Waiting')

    def on_enter_playing(self, update):
        update.message.reply_text('Just start playing')
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving Playing')
