from sandbox import Sandbox, SandboxConfig
from optparse import OptionParser
import sys,traceback,os,contextlib

@contextlib.contextmanager
def capture_stdout():
    import sys
    import tempfile
    stdout_fd = sys.stdout.fileno()
    with tempfile.TemporaryFile(mode='w+b') as tmp:
        stdout_copy = os.dup(stdout_fd)
        try:
            os.dup2(tmp.fileno(), stdout_fd)
            yield tmp
        finally:
            os.dup2(stdout_copy, stdout_fd)
            os.close(stdout_copy)

class Runner:
    def __init__(self):
        self.options = self.parseOptions()
        self.sandbox = Sandbox(self.createConfig())
        self.localvars = dict()
    def parseOptions(self):
        parser = OptionParser(usage="%prog [options]")
        SandboxConfig.createOptparseOptions(parser)#, default_timeout=None)
        parser.add_option("--debug",
            help="Debug mode",
            action="store_true", default=True)
        parser.add_option("--verbose", "-v",
            help="Verbose mode",
            action="store_true", default=True)
        parser.add_option("--quiet", "-q",
            help="Quiet mode",
            action="store_true", default=False)
        options, argv = parser.parse_args()
        if argv:
            parser.print_help()
            exit(1)
        if options.quiet:
            options.verbose = False
        return options

    def createConfig(self):
        config = SandboxConfig.fromOptparseOptions(self.options)
        config.enable('traceback')
        config.enable('stdin')
        config.enable('stdout')
        config.enable('stderr')
        config.enable('exit')
        config.enable('site')
        config.enable('encodings')
        config._builtins_whitelist.add('compile')
        config.allowModuleSourceCode('code')
        config.allowModule('sys',
            'api_version', 'version', 'hexversion')
        config.allowSafeModule('sys', 'version_info')
        if self.options.debug:
            config.allowModule('sys', '_getframe')
            config.allowSafeModule('_sandbox', '_test_crash')
            config.allowModuleSourceCode('sandbox')
        if not config.cpython_restricted:
            config.allowPath(__file__)
        return config
    def Run(self,code):
        # code = '\n'.join([self.code,code])
        # log and compile the statement up front
        val = ''
        try:
            #logging.info('Compiling and evaluating:\n%s' % statement)
            compiled = compile(code, '<string>', 'exec')
        except:
            traceback.print_exc(file=sys.stdout)
            return
        try:
            with capture_stdout() as stdout:
                self.sandbox.execute(code)
                stdout.seek(0)
                val = stdout.read()
        except:
            err = sys.exc_info()[1]
            print type(err), err

        return val
