# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from ProvenanceCheck.ProvenanceCheckAsyncClient import ProvenanceCheck as ProvenanceCheckClient
#END_HEADER


class ProvenanceCheck:
    '''
    Module Name:
    ProvenanceCheck

    Module Description:
    A KBase module: ProvenanceCheck
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass


    def get_service_props(self, ctx):
        """
        :returns: instance of mapping from String to String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_service_props
        prov_list = ctx.provenance()
        print("Provenance: " + str(prov_list))
        prov = prov_list[0] if len(prov_list) > 0 else {}
        module_name = prov.get('service')
        service_ver = prov.get('service_ver')
        pc = ProvenanceCheckClient(os.environ['SDK_CALLBACK_URL'], service_ver=service_ver)
        phrase = pc.hello_string(module_name)
        returnVal = {'module_name': module_name, 'service_ver': service_ver,
                     'hello_string': phrase}
        #END get_service_props

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_service_props return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def hello_string(self, ctx, name):
        """
        :param name: instance of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN hello_string
        returnVal = "Hi, " + name + "!"
        #END hello_string

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method hello_string return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
