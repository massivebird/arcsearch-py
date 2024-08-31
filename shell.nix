{ pkgs ? import <nixpkgs> { } }:
with pkgs;
mkShell {
  buildInputs = [
    python312Packages.pyyaml
    python312Packages.termcolor
  ];

  shellHook = ''
    # ...
  '';
}
