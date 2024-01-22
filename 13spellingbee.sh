#The middle letter must be used in every word, 
#but the outer 6 letters can be used any number of times. 
#Words must be at least 4 letters long.

#outer = z, o, n, c, a, i (used any number of times)
#inner = r (must be used)


cd ~/Code/MCB185/data/
gunzip -c dictionary.gz | grep "r" | grep -v "[bdefghjklmpqstuvwxy]" | grep -E ".{4,}"


