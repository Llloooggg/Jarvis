from threading import Thread
import triggers
import actions
import db_routing


class Executor(Thread):
    def __init__(self, scenario, tg_id):
        Thread.__init__(self)
        self.tg_id = tg_id
        self.sceanrio_id = scenario.id
        self.trigger_def = db_routing.get_trigers(scenario.trigger_id).def_name
        self.trigger_args = scenario.trigger_args
        self.action_def = db_routing.get_actions(scenario.action_id).def_name
        self.action_args = scenario.action_args

    def execute(self):
        trigger = getattr(triggers, self.trigger_def)
        trigger(self.trigger_args, self.tg_id)
        action = getattr(actions, self.action_def)
        action(self.action_args, self.tg_id)

    def run(self):
        thread = Thread(target=self.execute)
        thread.start()
        thread.join()
        db_routing.delete_scenario(self.sceanrio_id)
