# eas_ing_stat.awk
#
# extract timing information related to ingestion from EAS log
#	summary to standard output
# 	optional: details in the file if outdetails parameter is set to a file name
#
#[INFO ][2014-06-07 00:07:36,483][http-bio-8080-exec-2] [service.ingest]: A new ingestion was performed in 7689 ms : 08000001803521488035347d : 2318,1661,0,0,3580,26,65
# See EAS-1078 for log description
#
# usage: 
# 	awk -f eas_ing_stat.awk [-v outdetails=<filename>] eas-ws.log
#
BEGIN {
	SKIP_FIRST=500
	if (outdetails!= "") {
		print "objid", "ingest", "init", "aip.builder", "lock.builder", "extract.sip.xml", "processor", "aip.parent.rel.update", "aip.update" >outdetails
	}
}

/A new ingestion was performed/ {
	cnt_all++
	if (cnt_all > SKIP_FIRST) {
	
		cnt++
		t0 += $(NF-5)
		split($NF, time_values, ",")	
		t2 += time_values[1];
		t3 += time_values[2];
		t4 += time_values[3];
		t5 += time_values[4];
		t6 += time_values[5];
		t7 += time_values[6];
		t8 += time_values[7];

	#	dist(time_values[5], td)		

		if (outdetails!= "") {
			objid=substr($(NF-2), 1, 8) substr($(NF-2), 17, 8)
			print objid, $(NF-5), time_values[1], time_values[2], time_values[3], time_values[4], time_values[5], time_values[6], time_values[7] >>outdetails
		}

	}

}

END {
	printf "%5.5s %6.6s %7.7s %s\n", "step", "cnt", "avg", "step label"
	printf "%5d %6d %7.2f %s\n", "2", cnt, t2/cnt, "init"
	printf "%5d %6d %7.2f %s\n", "3", cnt, t3/cnt, "aip.builder"
	printf "%5d %6d %7.2f %s\n", "4", cnt, t4/cnt, "lock.builder"
	printf "%5d %6d %7.2f %s\n", "5", cnt, t5/cnt, "extract.sip.xml"
	#printf "%5d %6d %7.2f %6d %6d %6d %6d %s\n", "6", cnt, t6/cnt, td[1], td[2], td[3], td[4], "processor"
	printf "%5d %6d %7.2f %s\n", "6", cnt, t6/cnt, "processor"
	printf "%5d %6d %7.2f %s\n", "7", cnt, t7/cnt, "aip.parent.rel.update"
	printf "%5d %6d %7.2f %s\n", "8", cnt, t8/cnt, "aip.update"
	printf "%5d %6d %7.2f %s\n", "0", cnt, t0/cnt, "ingest"
}

function dist( val, arrayd ) {
	if (val < 100) arrayd[1]++
        else if (val < 500) arrayd[2]++
        else if (val < 1000) arrayd[3]++
        else arrayd[4]++
}



