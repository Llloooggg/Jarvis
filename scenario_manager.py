from threading import Thread
import triggers
import actions
import db_routing


class Executor(Thread):
    def __init__(self, scenario):
        Thread.__init__(self)
        self.sceanrio_id = scenario.id
        self.trigger_def = db_routing.get_trigers(scenario.id).def_name
        self.trigger_args = scenario.trigger_args
        self.action_def = db_routing.get_actions(scenario.id).def_name
        self.action_args = scenario.action_args

    def execute(self):
        trigger = getattr(triggers, self.trigger_def)
        trigger(self.trigger_args)
        action = getattr(actions, self.action_def)
        action(self.action_args)

    def run(self):
        thread = Thread(target=self.execute)
        thread.start()
        thread.join()
        db_routing.delete_scenario(self.sceanrio_id)
