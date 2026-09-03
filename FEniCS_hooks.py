import re
import os
from easybuild.tools.build_log import print_msg, EasyBuildError

def get_eessi_envvar(eessi_envvar):
    """Get an EESSI environment variable from the environment"""

    eessi_envvar_value = os.getenv(eessi_envvar)
    if eessi_envvar_value is None:
        raise EasyBuildError("$%s is not defined!", eessi_envvar)

    return eessi_envvar_value

# List of supported hooks (in order of execution):
# eb --avail-hooks

def pre_test_hook(easyblock, *args, **kwargs):
    if easyblock.name in PRE_TEST_HOOKS:
        PRE_TEST_HOOKS[easyblock.name](easyblock, *args, **kwargs)

def pre_configure_hook(easyblock, *args, **kwargs):
    if easyblock.name in PRE_CONFIGURE_HOOKS:
        PRE_CONFIGURE_HOOKS[easyblock.name](easyblock, *args, **kwargs)

def _test_step_super_lu(self):
    """
    Run the testsuite of SuperLU_DIST
    """

    # This implementation disables oversubscription
    #
    # Oversubscription results in a crash on Aion. Oversubscription allows the tests to run on single core executions
    # (the tests require upto `-np 2`), but oversubscripted runs fail on Aion. The cause is under investigation.
    if self.cfg['runtest'] is None:
        self.cfg['runtest'] = 'test'

    super(type(self), self).test_step()

def pre_test_hook_SuperLU_DIST(easyblock):
    def test_step_super_lu():
        return _test_step_super_lu(easyblock)

    setattr(easyblock, 'test_step', test_step_super_lu)

def pre_configure_hook_PETSc(easyblock, *args, **kwargs):
    eprefix = get_eessi_envvar('EPREFIX')

    easyblock.cfg['configopts'] = " ".join(
        [
            easyblock.cfg['configopts'],
            fr'--with-zlib-include=[{eprefix}/usr/include]',
            fr'--with-zlib-lib=[{eprefix}/usr/lib64/libz.so]',
        ]
    )

PRE_TEST_HOOKS = {
    'SuperLU_DIST': pre_test_hook_SuperLU_DIST
}

PRE_CONFIGURE_HOOKS = {
    'PETSc': pre_configure_hook_PETSc
}
