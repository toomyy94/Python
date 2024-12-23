
# This program generates 20 terms of a sequence by a recurrence relation.
Un = 100                    # Un = each term of the sequence. Initially = U0
for n in range(20):
    print(Un)
    Un = 1.01*Un - 1.01     # Set Un to the next term of the sequence
i=0
while n > 0:
	print(n)
	n -= 1
	i=i+1
print (i)
