python-pip:
  pkg:
    - installed

python-dev:
  pkg:
    - installed

psutil:
  pip.installed:
    - name: psutil
    - require:
      - pkg: python-pip
      - pkg: python-dev
