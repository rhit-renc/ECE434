cmd_/home/debian/exploringBB/extras/kernel/ebbchar/modules.order := {   echo /home/debian/exploringBB/extras/kernel/ebbchar/ebbchar.ko; :; } | awk '!x[$$0]++' - > /home/debian/exploringBB/extras/kernel/ebbchar/modules.order