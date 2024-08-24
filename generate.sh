pointsize=14
for index in $(seq 0 366) 
do
	if [ $index -lt 10 ]; then
		pointsize=18
		echo "single digit, embiggening font to $pointsize"
	elif [ $index -lt 100 ]; then
		pointsize=14
	else
		pointsize=9
	fi
	for frame in $(seq 0 4)
	do
		pt=1
		if [ $index -gt 99 ]; then
			echo "3 digits, reducing font"
			pt=$((frame-1))
		else
			pt=$((frame+1))
		fi
		echo "frame: $frame"
		echo "pointsize: $pointsize $index-$frame $((10 + $frame)) size change: $(($pointsize + $(($pt+3))))"    
		
		magick -size 32x32 xc:black -font Trade-Winds -pointsize $(($pointsize + $(($pt)))) -fill gradient:#00ff00 -gravity center -draw "text 0,0 '$index'" tmp_numbers/$index-$frame.gif 

	done 
	
	magick -size 32x32  -dispose previous -delay 17  -loop 0 tmp_numbers/$index-%d.gif[0-4] -duplicate 1,-2-1   numbers_output/$index.gif

done
