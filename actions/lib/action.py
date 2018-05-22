from st2common.runners.base_action import Action

from checkpoint import CheckpointApi


class CheckpointBaseAction(Action):
    def __init__(self, config):
        super(CheckpointBaseAction, self).__init__(config)
        self._firewall_ip = self.config['firewall_ip']
        self._username = self.config['username']
        self._password = self.config['password']
        self.checkpoint = self.get_checkpoint()

    def get_checkpoint(self):
        checkpoint_api = CheckpointApi(checkpoint=self._firewall_ip, username=self._username,
                                       password=self._password)

        return checkpoint_api
