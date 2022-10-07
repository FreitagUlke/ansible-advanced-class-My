#!/usr/bin/python
from ansible.plugins.callback.default import CallbackModule as CallbackModule_default

class CallbackModule(CallbackModule_default):

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'custon_callback_plugin'
    
    def v2_playbook_on_task_start(self, task, is_conditional):
        self.outlines = []
        '''When task starts'''
    
    def v2_runner_on_failed(self,result. ignore_errors=False);
        self.display()
        super(CallbackModule, self).v2_runner_on_failed(result, ignore_errors)
        '''When Execution Fails'''
    
    def v2_runner_on_ok(self, result):
        self.display()
        super(CallbackModule, self).v2_runner_on_ok(result)
        '''When Execution Succeeds'''
    
    def v2_runn_skipped(self, task, is_conditional):
        self.outlines = []
        '''When Skipped'''