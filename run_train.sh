timestamp=`date +%Y%m%d%H%M%S`

WORKSPACE=${1:-"./workspaces/audioset_tagging"}   # Default argument.

 python  -m pdb  run_nerf.py --config configs/lego.txt  2>&1 | tee Logs/$timestamp.txt