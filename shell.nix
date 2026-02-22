{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    pkgs.python314
    pkgs.python314Packages.venvShellHook
    pkgs.python314Packages.pyqt6
    pkgs.python314Packages.matplotlib
    pkgs.python314Packages.numpy

    # C++ runtime
    pkgs.gcc.cc.lib

    # Compression
    pkgs.zlib

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
    pkgs.libxcb
    # Audio (optional)
    pkgs.alsa-lib
    pkgs.pulseaudio
    pkgs.openal
    pkgs.openal
  ];

  venvDir = ".venv";

  shellHook = ''
    echo "Entering Ursina dev shell (Python 3.11)"

    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
      pkgs.gcc.cc.lib
      pkgs.zlib
      pkgs.mesa
      pkgs.libGL
      pkgs.libGLU
      pkgs.xorg.libX11
      pkgs.xorg.libXcursor
      pkgs.xorg.libXrandr
      pkgs.xorg.libXinerama
      pkgs.xorg.libXi
      pkgs.pulseaudio
      pkgs.openal
    ]}:$LD_LIBRARY_PATH

    rm -f Config.prc
  '';
}

