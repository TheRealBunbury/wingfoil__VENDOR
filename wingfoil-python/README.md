

# To install (and activate) the python virtual env run:

sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install python3-venv

# set up virtual env

python3 -m venv ./.venv

# activate the virutal env

source ./.venv/bin/activate

# under virtual env install these modules
# Note we are still working on updating fluvial to compile 
# with latest maturin version.

pip install patchelf
pip install maturin==0.13

# under virtual env, build the fluvial wheel

maturin develop

# You can run example with

python3 ./examples/example.py 