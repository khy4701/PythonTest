
ps -ef | grep uwsgi | awk 'BEGIN {

} {
	        if ($0 ~ "grep")
				                next;

			        cmd = sprintf("kill -9 %s", $2);

					        printf("[%s]\n", cmd);
							        system(cmd);
} END {

}'


ipcrm -Q 0x00003039
ipcrm -Q 0x0000d432
ipcrm -Q 0x0000d433

echo 'Queue Cleaned.."



