{pkgs ? import <nixpkgs> {}}: let
  pythonEnv = pkgs.python3.withPackages (ps: with ps; [pygame]);
in
  (pkgs.buildFHSUserEnv {
    name = "Cobrinha shell";
    targetPkgs = pkgs: [
      pythonEnv
    ];
    runScript = "python ./scripts/main.py";
  })
  .env
