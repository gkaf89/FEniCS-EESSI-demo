# Compiling FEniCS with EESSI

This is a demo on how to compile FEneCS-DOLFINx with EESSI.

1. Start by loading the EESSI module and the compilation environment.

  ```console
  $ module load EESSI/2025.06
  $ module load EESSI-extend
  ```

2. You are ready to compile! Switch to the root directory of the repository and perform a sry run to get a list of packages that need to be compiled on top of the pcakges distributed with EESSI.

  ```console
  eb --robot --robot-path=${PWD}: --dry-run FEniCS-DOLFINx-Python-0.11.0.post0-foss-2025b.eb
  ```

  Many of the packages are already available in EESSI paths. The flags used perform the follwoing functions.

  - `--robot`: If a dependency of a package is missing, then with the robot flag the dependency is installed automatically.
  - `--robot-path`: Extends the list of directories where EasyBuild looks for packages with a colon separated list of paths. Prepending `:` appends to the list (e.g. `:${PWD}`), appending `:` prepends
  to the list (e.g. `${PWD}:`), and ignoring `:` replaces the list. The paths are searched for packages from start to finish.
  - `--dry-run`: lists which packages were found and which need to be installed, without installing anything.

3. Now you can run the he compilation command:

  ```console
  eb --robot --robot-path=${PWD}: FEniCS-DOLFINx-Python-0.11.0.post0-foss-2025b.eb
  ```

## Note

Currently there are a few bugs in the installation instruction of packages missing from EESSI. You can use the easyblocks, Python packages with installation instruction, in the `easyblocks` directory
to fix the buggy packages with the [`--include-easyblocks` option](https://docs.easybuild.io/including-additional-python-modules/?h=include+easyblocks#include_easyblocks).
