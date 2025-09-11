from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650

	assert simple_work_calc(1, 2, 2) == 1
	assert simple_work_calc(2, 2, 2) == 4
	assert simple_work_calc(50, 4, 2) == 2518

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300

	assert work_calc(10, 2, 2, lambda n: n) == 36
	assert work_calc(15, 3, 3, lambda n: n*n) == 309
	assert work_calc(50, 3, 2, lambda n: 1) == 364




def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work

	# create work_fn1
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: x)
	
	# create work_fn2
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: 1)

	# create work_fn3
	work_fn3 = lambda n: work_calc(n, 2, 2, lambda x: .5)
	
	res = compare_work(work_fn1, work_fn2)

	print_results(res)

	res2 = compare_work(work_fn1, work_fn3)

	print_results(res2)


	
def test_compare_span():
	# create span_fn1
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: x)
	
	# create span_fn2
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda x: 1)

	# create span_fn3
	span_fn3 = lambda n: span_calc(n, 2, 2, lambda x: 0.5)
	
	res = compare_span(span_fn1, span_fn2)

	print_results(res)

	res2 = compare_span(span_fn1, span_fn3)

	print_results(res2)


