
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  # System packages available in the dev shell
  packages = [
    pkgs.python313
    pkgs.python311Packages.venvShellHook

    # Python packages that MUST come from Nix (C/C++ libs included)
    # pkgs.python313Packages.ipykernel
    # pkgs.python313Packages.pyzmq
    # pkgs.python313Packages.numpy
    pkgs.python313Packages.matplotlib
    # pkgs.python313Packages.pillow

    # Optional (nice to have)
    pkgs.gcc                # for compiling Python wheels
    # pkgs.glibc
    pkgs.git
  ];

  # Automatically create and activate a virtual environment
  # inside the dev shell
  venvDir = ".venv";

  # Commands executed every time you enter `nix-shell`
  shellHook = ''
    echo "🐍 Entering Python 3.11 dev environment"

    # Ensure venv is created
    if [ ! -d "$venvDir" ]; then
      echo "Creating virtual environment in $venvDir..."
      python -m venv $venvDir
    fi

    # Activate the venv
    source $venvDir/bin/activate

    echo "Using Python from: $(which python)"

    # Make sure pip doesn't override Nix-installed packages
    export PIP_IGNORE_INSTALLED=1
  '';
}
