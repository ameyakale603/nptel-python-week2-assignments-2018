def rotate(list,num):
	for i in range(num):
		list=list[len(list)-1:]+list[:len(list)-1]
	print(list)
	


def main():
	rotate([1,2,3,4],2)


if __name__=='__main__':
	main()

	