cmd_/home/debian/exploringBB/extras/kernel/ebbchar/Module.symvers := sed 's/ko$$/o/' /home/debian/exploringBB/extras/kernel/ebbchar/modules.order | scripts/mod/modpost -m    -o /home/debian/exploringBB/extras/kernel/ebbchar/Module.symvers -e -i Module.symvers   -T -
