{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  packages = [
    pkgs.python311
    pkgs.python311Packages.venvShellHook
    pkgs.python311Packages.pillow
    pkgs.python311Packages.pyperclip
    pkgs.python311Packages.screeninfo

    # C++ runtime
    pkgs.gcc.cc.lib

    # OpenGL
    pkgs.mesa
    pkgs.libGL
    pkgs.libGLU

    # X11 (REQUIRED for windowed Panda3D)
    pkgs.xorg.libX11
    pkgs.xorg.libXcursor
    pkgs.xorg.libXrandr
    pkgs.xorg.libXinerama
    pkgs.xorg.libXi

    # Audio (optional)
    pkgs.alsa-lib
    pkgs.pulseaudio
    pkgs.openal
  ];

  venvDir = ".venv";

  shellHook = ''
    echo "Entering Ursina dev shell (Python 3.11)"

    # Force clean venv if Python version changed
    source $venvDir/bin/activate

    pip install ursina

    export LD_LIBRARY_PATH=${
      pkgs.lib.makeLibraryPath [
        pkgs.gcc.cc.lib
        pkgs.mesa
        pkgs.libGL
        pkgs.libGLU
        pkgs.xorg.libX11
        pkgs.xorg.libXcursor
        pkgs.xorg.libXrandr
        pkgs.xorg.libXinerama
        pkgs.xorg.libXi
        pkgs.alsa-lib
        pkgs.pulseaudio
        pkgs.openal
      ]
    }:$LD_LIBRARY_PATH

    rm -f Config.prc
  '';
}
